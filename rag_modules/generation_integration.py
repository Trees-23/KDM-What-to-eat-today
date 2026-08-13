"""
生成集成模块
"""

import logging
import os
import json
import time
from types import SimpleNamespace
from typing import List, Sequence

import requests
try:
    from langchain_core.documents import Document
except ImportError:
    class Document:
        def __init__(self, page_content: str = "", metadata=None):
            self.page_content = page_content
            self.metadata = metadata or {}

from rag_modules.rag_audit import query_hash, safe_base_url_host
from rag_modules.evidence_builder import EvidenceBuilder
from rag_modules.retrieval_contracts import EvidenceBundle

logger = logging.getLogger(__name__)


class OpenAICompatibleHTTPClient:
    """Small requests-based client for OpenAI-compatible chat endpoints.

    Some proxy endpoints reject the official OpenAI SDK request shape while
    accepting plain HTTP requests. This class preserves the subset of
    client.chat.completions.create(...) used by the retrieval modules.
    """

    def __init__(self, api_key: str, base_url: str, timeout: float = 60.0):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.chat = SimpleNamespace(
            completions=SimpleNamespace(create=self._create_chat_completion)
        )

    def _create_chat_completion(self, **kwargs):
        stream = bool(kwargs.pop("stream", False))
        timeout = kwargs.pop("timeout", self.timeout)
        payload = {key: value for key, value in kwargs.items() if value is not None}
        if stream:
            payload["stream"] = True
        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            stream=stream,
            timeout=timeout,
        )
        if response.status_code >= 400:
            raise RuntimeError(self._extract_error_message(response))

        if stream:
            return self._iter_stream(response)

        data = response.json()
        choices = [
            SimpleNamespace(
                message=SimpleNamespace(
                    content=(choice.get("message") or {}).get("content", "")
                )
            )
            for choice in data.get("choices", [])
        ]
        return SimpleNamespace(choices=choices)

    def _iter_stream(self, response):
        response.encoding = "utf-8"
        for raw_line in response.iter_lines(decode_unicode=True):
            if not raw_line:
                continue
            line = raw_line.strip()
            if not line.startswith("data:"):
                continue
            data_text = line[len("data:"):].strip()
            if data_text == "[DONE]":
                break
            try:
                data = json.loads(data_text)
            except json.JSONDecodeError:
                continue
            for choice in data.get("choices", []):
                delta = choice.get("delta") or {}
                yield SimpleNamespace(
                    choices=[
                        SimpleNamespace(
                            delta=SimpleNamespace(content=delta.get("content", ""))
                        )
                    ]
                )

    @staticmethod
    def _extract_error_message(response) -> str:
        try:
            data = response.json()
            error = data.get("error")
            if isinstance(error, dict):
                return error.get("message") or response.text
            if isinstance(error, str):
                return error
        except Exception:
            pass
        return response.text or f"HTTP {response.status_code}"


class GenerationIntegrationModule:
    """生成集成模块 - 负责答案生成"""

    def __init__(self, model_name: str = "kimi-k2-0711-preview", temperature: float = 0.1, max_tokens: int = 2048):
        """
        初始化生成集成模块
        """
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        
        # 统一的LLM客户端配置（支持所有兼容OpenAI格式的供应商）
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("请设置 OPENAI_API_KEY 环境变量")

        self.base_url = os.getenv("OPENAI_BASE_URL", "https://api.moonshot.cn/v1")

        self.client = OpenAICompatibleHTTPClient(
            api_key=api_key,
            base_url=self.base_url
        )

        logger.info(f"生成模块初始化完成，模型: {model_name}, API地址: {self.base_url}")

    def _build_prompt(self, question: str, context: str) -> str:
        """构建统一的提示词"""
        return f"""
        作为一位专业的烹饪助手，请基于以下信息回答用户的问题。

        检索到的相关信息：
        {context}

        用户问题：{question}

        请提供准确、实用的回答。根据问题的性质：
        - 如果是询问多个菜品，请提供清晰的列表
        - 如果是询问具体制作方法，请提供详细步骤
        - 如果是一般性咨询，请提供综合性回答

        重要提醒：如果问题涉及之前对话中提到的具体菜谱或食材，请严格基于之前提供的信息回答，不要添加之前没有提到的食材或调料。

        回答：
        """

    def _build_evidence_prompt(self, question: str, context: str) -> str:
        """构建阶段 2 的分层证据提示词。

        GraphFact、正文和限制以独立标题传入，避免把正文相似性表达为图关系事实。
        """
        return f"""
        作为一位专业的烹饪助手，请严格基于下列分层证据回答问题。

        {context}

        用户问题：{question}

        回答规则：
        - 只有“已验证图事实”中的内容可以用来断言图关系或结构化事实。
        - “正文证据”只能作为烹饪说明，不得证明未在图事实中验证的关系。
        - 必须明确说明“限制与不可证明项”中的缺失或不可用状态，不得补造事实。
        - 没有正文证据时，不要编造食材、步骤或营养结论。
        - “推荐证据等级”为 soft_preference 时，只能表述为少油/清爽偏好，不能声称已验证低脂或给出脂肪数值。

        回答：
        """

    def _prepare_generation_input(self, question: str, evidence_or_documents):
        """兼容旧 Document 输入，并为 EvidenceBundle 选择独立提示模板。"""
        if isinstance(evidence_or_documents, EvidenceBundle):
            context = EvidenceBuilder.context(evidence_or_documents)
            return context, self._build_evidence_prompt(question, context), [], evidence_or_documents

        documents = list(evidence_or_documents or [])
        context_parts = []
        for doc in documents:
            content = doc.page_content.strip()
            if not content:
                continue
            level = doc.metadata.get('retrieval_level', '')
            context_parts.append(f"[{level.upper()}] {content}" if level else content)
        context = "\n\n".join(context_parts)
        return context, self._build_prompt(question, context), documents, None

    def generate_adaptive_answer(self, question: str, documents: Sequence[Document] | EvidenceBundle, audit_run=None) -> str:
        """
        智能统一答案生成
        自动适应不同类型的查询，无需预先分类
        """
        context, prompt, audit_documents, evidence_bundle = self._prepare_generation_input(question, documents)
        self._record_generation_context(
            audit_run, audit_documents, context, stream=False, evidence_bundle=evidence_bundle
        )
        terminal_response = self._terminal_evidence_response(evidence_bundle)
        if terminal_response:
            return terminal_response
        generation_started_at = time.time()
        
        try:
            if audit_run:
                audit_run.append_process(
                    "Generation Config",
                    {
                        "model_name": self.model_name,
                        "base_url_host": safe_base_url_host(self.base_url),
                        "temperature": self.temperature,
                        "max_tokens": self.max_tokens,
                        "stream": False,
                        "timeout": "client_default",
                        "max_retries": 0,
                    },
                )
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            answer = response.choices[0].message.content.strip()
            if not answer:
                raise RuntimeError("GENERATION_EMPTY_STREAM")
            if audit_run:
                audit_run.append_process(
                    "Generation Non-Stream",
                    {
                        "status": "success",
                        "duration_ms": int((time.time() - generation_started_at) * 1000),
                        "response_chars": len(answer),
                        "response_hash": query_hash(answer),
                    },
                )
                audit_run.append_process(
                    "Final Output",
                    {
                        "answer_chars": len(answer),
                        "answer_hash": query_hash(answer),
                        "success": True,
                    },
                )
            return answer
            
        except Exception as e:
            logger.error(f"LightRAG答案生成失败: {e}")
            if audit_run:
                audit_run.record_error("generation_non_stream", e, attempt=1)
                audit_run.append_process(
                    "Final Output",
                    {
                        "answer_chars": 0,
                        "answer_hash": query_hash(""),
                        "success": False,
                    },
                )
            return f"抱歉，生成回答时出现错误：{str(e)}"
    
    def generate_adaptive_answer_stream(self, question: str, documents: Sequence[Document] | EvidenceBundle, max_retries: int = 3, audit_run=None):
        """
        LightRAG风格的流式答案生成（带重试机制）
        """
        context, prompt, audit_documents, evidence_bundle = self._prepare_generation_input(question, documents)
        self._record_generation_context(
            audit_run,
            audit_documents,
            context,
            stream=True,
            max_retries=max_retries,
            evidence_bundle=evidence_bundle,
        )
        terminal_response = self._terminal_evidence_response(evidence_bundle)
        if terminal_response:
            yield terminal_response
            return
        generation_started_at = time.time()
        first_token_latency_ms = None
        chunk_count = 0
        fallback_used = False
        full_response = ""
        if audit_run:
            audit_run.append_process(
                "Generation Config",
                {
                    "model_name": self.model_name,
                    "base_url_host": safe_base_url_host(self.base_url),
                    "temperature": self.temperature,
                    "max_tokens": self.max_tokens,
                    "stream": True,
                    "timeout": 60,
                    "max_retries": max_retries,
                },
            )
        
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    stream=True,
                    timeout=60  # 增加超时设置
                )
                
                if attempt == 0:
                    print("开始流式生成回答...\n")
                else:
                    print(f"第{attempt + 1}次尝试流式生成...\n")
                
                for chunk in response:
                    if chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        if first_token_latency_ms is None:
                            first_token_latency_ms = int((time.time() - generation_started_at) * 1000)
                        chunk_count += 1
                        full_response += content
                        yield content  # 使用yield返回流式内容
                
                if not full_response.strip():
                    raise RuntimeError("GENERATION_EMPTY_STREAM")
                if audit_run:
                    audit_run.append_process(
                        "Generation Stream",
                        {
                            "status": "success",
                            "chunk_count": chunk_count,
                            "first_token_latency_ms": first_token_latency_ms,
                            "total_duration_ms": int((time.time() - generation_started_at) * 1000),
                            "fallback_used": fallback_used,
                        },
                    )
                    audit_run.append_process(
                        "Final Output",
                        {
                            "answer_chars": len(full_response),
                            "answer_hash": query_hash(full_response),
                            "success": True,
                        },
                    )
                # 如果成功完成，退出重试循环
                return
                
            except Exception as e:
                logger.warning(f"流式生成第{attempt + 1}次尝试失败: {e}")
                
                if attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 2  # 递增等待时间
                    print(f"⚠️ 连接中断，{wait_time}秒后重试...")
                    time.sleep(wait_time)
                    continue
                else:
                    # 所有重试都失败，使用非流式作为后备
                    logger.error(f"流式生成完全失败，尝试非流式后备方案")
                    print("⚠️ 流式生成失败，切换到标准模式...")
                    fallback_used = True
                    
                    try:
                        fallback_response = self.generate_adaptive_answer(question, documents)
                        if not isinstance(fallback_response, str) or not fallback_response.strip():
                            raise RuntimeError("GENERATION_EMPTY_STREAM")
                        full_response += fallback_response
                        if first_token_latency_ms is None:
                            first_token_latency_ms = int((time.time() - generation_started_at) * 1000)
                        chunk_count += 1
                        if audit_run:
                            audit_run.append_process(
                                "Generation Stream",
                                {
                                    "status": "fallback_success",
                                    "chunk_count": chunk_count,
                                    "first_token_latency_ms": first_token_latency_ms,
                                    "total_duration_ms": int((time.time() - generation_started_at) * 1000),
                                    "fallback_used": True,
                                },
                            )
                            audit_run.append_process(
                                "Final Output",
                                {
                                    "answer_chars": len(full_response),
                                    "answer_hash": query_hash(full_response),
                                    "success": True,
                                },
                            )
                        yield fallback_response
                        return
                    except Exception as fallback_error:
                        logger.error(f"后备生成也失败: {fallback_error}")
                        if audit_run:
                            audit_run.record_error("generation_stream", fallback_error, attempt=attempt + 1)
                            audit_run.append_process(
                                "Generation Stream",
                                {
                                    "status": "error",
                                    "chunk_count": chunk_count,
                                    "first_token_latency_ms": first_token_latency_ms,
                                    "total_duration_ms": int((time.time() - generation_started_at) * 1000),
                                    "fallback_used": True,
                                },
                            )
                        error_msg = f"抱歉，生成回答时出现网络错误，请稍后重试。错误信息：{str(e)}"
                        yield error_msg
                        return 

    def _record_generation_context(
        self,
        audit_run,
        documents: List[Document],
        context: str,
        stream: bool,
        max_retries: int = 0,
        evidence_bundle: EvidenceBundle | None = None,
    ):
        if not audit_run:
            return
        if evidence_bundle is None:
            audit_run.write_documents(
                "Final Prompt Context",
                documents,
                "generation_context",
            )
        else:
            sections = EvidenceBuilder.sections(evidence_bundle)
            audit_run.append_recall("Evidence / 已验证图事实", sections.verified_graph_facts)
            audit_run.append_recall("Evidence / 正文证据", sections.text_evidence)
            audit_run.append_recall("Evidence / 推荐证据等级", sections.recommendation_evidence)
            audit_run.append_recall("Evidence / 限制与不可证明项", sections.limitations)
        audit_run.append_process(
            "Prompt Assembly",
            {
                "prompt_template_name": "cooking_assistant_evidence" if evidence_bundle else "cooking_assistant_default",
                "prompt_template_version": "evidence_v1" if evidence_bundle else "v1",
                "prompt_template_hash": query_hash("cooking_assistant_evidence_v1" if evidence_bundle else "cooking_assistant_default_v1"),
                "context_doc_count": len(documents),
                "context_chars": len(context),
                "retrieval_levels": sorted({str((doc.metadata or {}).get("retrieval_level", "")) for doc in documents if getattr(doc, "metadata", None)}),
                "search_types": sorted({str((doc.metadata or {}).get("search_type", "")) for doc in documents if getattr(doc, "metadata", None)}),
                "stream": stream,
                "max_retries": max_retries,
                "evidence_bundle": evidence_bundle is not None,
                "verified_graph_fact_count": len(evidence_bundle.verified_graph_facts) if evidence_bundle else 0,
                "text_evidence_count": len(evidence_bundle.text_evidence) if evidence_bundle else 0,
                "limitation_count": len(evidence_bundle.limitations) if evidence_bundle else 0,
                "recommendation_evidence_level": (
                    evidence_bundle.recommendation_evidence.level
                    if evidence_bundle and evidence_bundle.recommendation_evidence
                    else None
                ),
                "recommendation_policy_version": (
                    evidence_bundle.recommendation_evidence.policy_version
                    if evidence_bundle and evidence_bundle.recommendation_evidence
                    else None
                ),
            },
        )

    @staticmethod
    def _terminal_evidence_response(evidence_bundle: EvidenceBundle | None) -> str | None:
        """对不能安全交给 LLM 的实体状态返回确定性提示。"""
        if evidence_bundle is None:
            return None
        limitations = set(evidence_bundle.limitations)
        if "NUTRITION_EVIDENCE_INSUFFICIENT" in limitations:
            return "当前没有可信营养数值或治理标签，无法验证严格低脂、脂肪克数或医疗饮食条件，因此不能给出满足该条件的推荐。"
        if "NUTRITION_CUISINE_EVIDENCE_UNAVAILABLE" in limitations:
            return "营养或菜系硬证据当前不可用，不能把未受限的向量结果称为低脂川菜。"
        if "NUTRITION_CUISINE_SCOPE_NOT_FOUND" in limitations:
            return "当前图谱没有可验证的川菜候选范围，不能把向量结果称为低脂川菜。"
        if "NUTRITION_PREFERENCE_RETRIEVAL_UNAVAILABLE" in limitations:
            return "当前少油/清爽偏好检索不可用，不能用旧路径补造低脂推荐。"
        if "ENTITY_NOT_FOUND" in limitations:
            return "知识库未收录该实体，无法在知识库中找到对应菜谱；因此不猜测或生成做法、食材和步骤。"
        if "ENTITY_AMBIGUOUS" in limitations:
            names = "、".join(candidate.display_name for candidate in evidence_bundle.entity_candidates[:3])
            suffix = f"候选包括：{names}。" if names else ""
            return f"找到多个并列实体候选，未自动选择。{suffix}请提供更具体的名称或补充描述。"
        if "PARENT_DOCUMENT_NOT_FOUND" in limitations or "PDS_ANCHOR_NOT_FOUND" in limitations:
            return "已定位实体，但当前父文档库没有可验证的正文证据，无法安全补全做法。"
        if "STEP_NOT_FOUND" in limitations or "TECHNIQUE_CHUNK_NOT_FOUND" in limitations:
            return "图谱未找到请求的目标步骤或技巧章节，无法用正文补造该定位结果。"
        if "GRAPH_RELATION_NOT_FOUND" in limitations:
            return "当前图谱未找到该关系，无法证明该关系存在；不能用文本证据把该关系表述为已成立。"
        if "GRAPH_UNAVAILABLE" in limitations:
            return "图证据当前不可用，无法验证请求的关系是否成立。"
        if "PDS_TEXT_UNAVAILABLE" in limitations or (
            "parent-store-unavailable" in limitations
            and evidence_bundle.query_plan
            and evidence_bundle.query_plan.get("intent") in {"RECIPE_STEP", "TECHNIQUE_CHUNKS"}
            and not evidence_bundle.text_evidence
        ):
            return "图谱已定位目标，但父文档正文当前不可用，不能据此补写步骤或技巧内容。"
        if "graph-unavailable" in limitations and not evidence_bundle.text_evidence:
            return "图证据当前不可用，无法验证请求的步骤或章节定位。"
        return None
