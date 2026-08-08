"""从 Neo4j 同一构建会话物化 ParentDocumentStore。"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Iterable, Mapping, Optional, Sequence

from .parent_document_store import (
    AnchorRecord,
    BuildManifest,
    CanonicalChunk,
    ParentDocumentStore,
    ParentRecord,
    make_build_manifest,
)

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class AnchorSpec:
    anchor_type: str
    anchor_id: str
    marker: str
    ordinal: int
    source_relation: str


@dataclass(frozen=True)
class SourceParent:
    parent_id: str
    node_type: str
    title: str
    full_content: str
    metadata: Mapping[str, Any] = field(default_factory=dict)
    anchors: tuple[AnchorSpec, ...] = ()


@dataclass(frozen=True)
class MaterializationResult:
    manifest: BuildManifest
    parents: tuple[ParentRecord, ...]
    chunks: tuple[CanonicalChunk, ...]
    anchors: tuple[AnchorRecord, ...]

    def write(
        self,
        output_path: str,
        *,
        publish: bool = False,
        active_pointer: Optional[str] = None,
    ) -> str:
        path = ParentDocumentStore.create_build(
            output_path,
            self.manifest,
            self.parents,
            self.chunks,
            self.anchors,
            publish=publish,
            active_pointer=active_pointer,
        )
        return str(path)


class ParentDocumentMaterializer:
    """把稳定图 ID、正文、child chunk 和锚点物化为一个不可变 build。"""

    BUILDER_VERSION = "parent_document_materializer_v1"

    def __init__(
        self,
        *,
        driver: Any = None,
        uri: Optional[str] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
        database: str = "neo4j",
        chunk_size: int = 500,
        chunk_overlap: int = 50,
    ) -> None:
        if chunk_size <= 0:
            raise ValueError("chunk_size 必须为正数")
        if chunk_overlap < 0 or chunk_overlap >= chunk_size:
            raise ValueError("chunk_overlap 必须满足 0 <= chunk_overlap < chunk_size")
        self.database = database
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self._owns_driver = driver is None
        if driver is not None:
            self.driver = driver
        else:
            if all((uri, user, password)):
                from neo4j import GraphDatabase

                self.driver = GraphDatabase.driver(uri, auth=(user, password), database=database)
            elif any((uri, user, password)):
                raise ValueError("连接 Neo4j 物化需要同时提供 uri、user、password")
            else:
                # 合成 Document 单测不需要连接真实 Neo4j。
                self.driver = None

    def close(self) -> None:
        if self._owns_driver and getattr(self, "driver", None) is not None:
            self.driver.close()

    def __enter__(self) -> "ParentDocumentMaterializer":
        return self

    def __exit__(self, *_exc: Any) -> None:
        self.close()

    def materialize_documents(self, source_parents: Iterable[SourceParent]) -> MaterializationResult:
        source_rows = sorted(source_parents, key=lambda item: (item.parent_id, item.node_type))
        if len({item.parent_id for item in source_rows}) != len(source_rows):
            raise ValueError("parent_id 必须在一个 build 内唯一")
        parents = tuple(
            ParentRecord(
                parent_id=item.parent_id,
                node_type=item.node_type,
                title=item.title,
                full_content=item.full_content,
                metadata=dict(item.metadata),
            ).with_hash()
            for item in source_rows
        )
        chunk_config = {"chunk_size": self.chunk_size, "chunk_overlap": self.chunk_overlap, "splitter": "heading_v1"}
        manifest = make_build_manifest(
            parents,
            chunk_config=chunk_config,
            builder_version=self.BUILDER_VERSION,
        )
        chunks: list[CanonicalChunk] = []
        anchors: list[AnchorRecord] = []
        for source in source_rows:
            source_chunks, source_anchors = self._chunk_source(source, manifest.build_id)
            chunks.extend(source_chunks)
            anchors.extend(source_anchors)
        return MaterializationResult(manifest, parents, tuple(chunks), tuple(anchors))

    def materialize_from_neo4j(self) -> MaterializationResult:
        """从已核验 database 读取 Recipe 和 TechniqueDoc 的稳定事实。"""

        if self.driver is None:
            raise RuntimeError("当前物化器没有 Neo4j driver")
        source_parents: list[SourceParent] = []
        with self._session() as session:
            recipe_rows = session.run(
                """
                MATCH (r:Recipe)
                RETURN r.nodeId AS node_id, properties(r) AS properties
                ORDER BY r.nodeId
                """
            )
            for row in recipe_rows:
                source_parents.append(self._recipe_parent(session, row))

            technique_rows = session.run(
                """
                MATCH (t:TechniqueDoc)
                RETURN t.nodeId AS node_id, properties(t) AS properties
                ORDER BY t.nodeId
                """
            )
            for row in technique_rows:
                source_parents.append(self._technique_parent(session, row))
        return self.materialize_documents(source_parents)

    def _session(self) -> Any:
        try:
            return self.driver.session(database=self.database)
        except TypeError:
            return self.driver.session()

    @staticmethod
    def _value(row: Any, key: str, default: Any = None) -> Any:
        if isinstance(row, Mapping):
            return row.get(key, default)
        try:
            value = row.get(key)
        except AttributeError:
            value = row[key]
        return default if value is None else value

    @classmethod
    def _properties(cls, row: Any) -> dict[str, Any]:
        value = cls._value(row, "properties", {})
        return dict(value or {})

    def _recipe_parent(self, session: Any, row: Any) -> SourceParent:
        recipe_id = str(self._value(row, "node_id", ""))
        props = self._properties(row)
        recipe_name = str(props.get("name") or recipe_id)
        ingredients: list[str] = []
        ingredient_result = session.run(
            """
            MATCH (r:Recipe {nodeId: $recipe_id})-[req:REQUIRES]->(i:Ingredient)
            RETURN i.nodeId AS node_id, properties(i) AS properties, properties(req) AS relation
            ORDER BY i.name, i.nodeId
            """,
            {"recipe_id": recipe_id},
        )
        for ingredient_row in ingredient_result:
            ingredient_props = self._properties(ingredient_row)
            relation = dict(self._value(ingredient_row, "relation", {}) or {})
            amount = relation.get("amount", "")
            unit = relation.get("unit", "")
            name = str(ingredient_props.get("name") or self._value(ingredient_row, "node_id", ""))
            text = name
            if amount not in (None, "") and unit not in (None, ""):
                text += f"({amount}{unit})"
            if ingredient_props.get("description"):
                text += f" - {ingredient_props['description']}"
            ingredients.append(text)

        steps: list[tuple[str, str, int]] = []
        step_result = session.run(
            """
            MATCH (r:Recipe {nodeId: $recipe_id})-[c:CONTAINS_STEP]->(s:CookingStep)
            RETURN s.nodeId AS node_id, properties(s) AS properties, properties(c) AS relation
            ORDER BY COALESCE(c.stepOrder, s.stepNumber, 999), s.nodeId
            """,
            {"recipe_id": recipe_id},
        )
        for ordinal, step_row in enumerate(step_result, 1):
            step_id = str(self._value(step_row, "node_id", ""))
            step_props = self._properties(step_row)
            step_text = f"步骤: {step_props.get('name') or step_id}"
            if step_props.get("description"):
                step_text += f"\n描述: {step_props['description']}"
            if step_props.get("methods"):
                step_text += f"\n方法: {step_props['methods']}"
            if step_props.get("tools"):
                step_text += f"\n工具: {step_props['tools']}"
            if step_props.get("timeEstimate"):
                step_text += f"\n时间: {step_props['timeEstimate']}"
            steps.append((step_id, step_text, ordinal))

        content_parts = [f"# {recipe_name}"]
        if props.get("description"):
            content_parts.append(f"\n## 菜品描述\n{props['description']}")
        if props.get("cuisineType"):
            content_parts.append(f"\n菜系: {props['cuisineType']}")
        if props.get("difficulty") not in (None, ""):
            content_parts.append(f"难度: {props['difficulty']}星")
        time_info = []
        if props.get("prepTime"):
            time_info.append(f"准备时间: {props['prepTime']}")
        if props.get("cookTime"):
            time_info.append(f"烹饪时间: {props['cookTime']}")
        if time_info:
            content_parts.append(f"\n时间信息: {', '.join(time_info)}")
        if props.get("servings"):
            content_parts.append(f"份量: {props['servings']}")
        if ingredients:
            content_parts.append("\n## 所需食材")
            content_parts.extend(f"{index}. {ingredient}" for index, ingredient in enumerate(ingredients, 1))
        anchor_specs: list[AnchorSpec] = []
        if steps:
            content_parts.append("\n## 制作步骤")
            for step_id, step_text, ordinal in steps:
                marker = f"### 第{ordinal}步\n{step_text}"
                content_parts.append(f"\n{marker}")
                anchor_specs.append(AnchorSpec("CookingStep", step_id, marker, ordinal - 1, "CONTAINS_STEP"))
        if props.get("tags"):
            content_parts.append(f"\n## 标签\n{props['tags']}")
        metadata = {
            "node_id": recipe_id,
            "recipe_name": recipe_name,
            "node_type": "Recipe",
            "category": props.get("category", "未知"),
            "cuisine_type": props.get("cuisineType", "未知"),
            "difficulty": props.get("difficulty", 0),
            "prep_time": props.get("prepTime", ""),
            "cook_time": props.get("cookTime", ""),
            "servings": props.get("servings", ""),
            "ingredients_count": len(ingredients),
            "steps_count": len(steps),
            "doc_type": "recipe",
            "source": "neo4j",
        }
        return SourceParent(recipe_id, "Recipe", recipe_name, "\n".join(content_parts), metadata, tuple(anchor_specs))

    def _technique_parent(self, session: Any, row: Any) -> SourceParent:
        document_id = str(self._value(row, "node_id", ""))
        props = self._properties(row)
        title = str(props.get("title") or props.get("name") or document_id)
        category = props.get("category") or "烹饪技巧"
        content_parts = [f"# {title}"]
        if category:
            content_parts.append(f"\n分类: {category}")
        if props.get("tags"):
            content_parts.append(f"标签: {props['tags']}")
        if props.get("summary"):
            content_parts.append(f"\n## 摘要\n{props['summary']}")

        anchors: list[AnchorSpec] = []
        chunk_rows = session.run(
            """
            MATCH (t:TechniqueDoc {nodeId: $document_id})-[r:HAS_CHUNK]->(c:TechniqueChunk)
            RETURN c.nodeId AS node_id, properties(c) AS properties, properties(r) AS relation
            ORDER BY COALESCE(r.chunkOrder, c.chunkIndex, 999), c.nodeId
            """,
            {"document_id": document_id},
        )
        chunks = list(chunk_rows)
        if chunks:
            for ordinal, chunk_row in enumerate(chunks):
                chunk_props = self._properties(chunk_row)
                section_title = str(chunk_props.get("sectionTitle") or chunk_props.get("name") or "正文")
                chunk_content = chunk_props.get("content") or chunk_props.get("summary") or ""
                if not chunk_content:
                    continue
                marker = f"## {section_title}\n{chunk_content}"
                content_parts.append(f"\n{marker}")
                anchors.append(
                    AnchorSpec(
                        "TechniqueChunk",
                        str(self._value(chunk_row, "node_id", "")),
                        marker,
                        ordinal,
                        "HAS_CHUNK",
                    )
                )
        elif props.get("content"):
            content_parts.append(f"\n## 正文\n{props['content']}")
        metadata = {
            "node_id": document_id,
            "recipe_name": title,
            "node_type": "TechniqueDoc",
            "category": category,
            "cuisine_type": "技巧知识",
            "difficulty": 0,
            "source_path": props.get("sourcePath", ""),
            "tags": props.get("tags", ""),
            "doc_type": "technique",
            "source": "neo4j",
        }
        return SourceParent(document_id, "TechniqueDoc", title, "\n".join(content_parts).strip(), metadata, tuple(anchors))

    def _chunk_source(self, source: SourceParent, build_id: str) -> tuple[list[CanonicalChunk], list[AnchorRecord]]:
        content = source.full_content.strip()
        if not content:
            raise ValueError(f"父文档正文不能为空: {source.parent_id}")
        spans = self._split_spans(content)
        total = len(spans)
        chunks: list[CanonicalChunk] = []
        for index, (start, end, section_title) in enumerate(spans):
            chunk_text = content[start:end]
            chunks.append(
                CanonicalChunk(
                    chunk_id=f"{source.parent_id}:chunk:{index}",
                    parent_id=source.parent_id,
                    chunk_index=index,
                    total_chunks=total,
                    section_title=section_title,
                    text=chunk_text,
                    build_id=build_id,
                ).with_hash()
            )

        anchors: list[AnchorRecord] = []
        search_from = 0
        for spec in sorted(source.anchors, key=lambda item: (item.ordinal, item.anchor_type, item.anchor_id)):
            position = content.find(spec.marker, search_from)
            if position < 0:
                position = content.find(spec.marker)
            if position < 0:
                raise ValueError(f"无法为锚点定位正文: {source.parent_id}/{spec.anchor_id}")
            search_from = position + len(spec.marker)
            chunk_index = next(
                (index for index, (start, end, _title) in enumerate(spans) if start <= position < end),
                None,
            )
            if chunk_index is None:
                raise ValueError(f"锚点未落入任何 chunk: {source.parent_id}/{spec.anchor_id}")
            anchors.append(
                AnchorRecord(
                    anchor_type=spec.anchor_type,
                    anchor_id=spec.anchor_id,
                    parent_id=source.parent_id,
                    build_id=build_id,
                    chunk_id=chunks[chunk_index].chunk_id,
                    ordinal=spec.ordinal,
                    source_relation=spec.source_relation,
                )
            )
        return chunks, anchors

    def _split_spans(self, content: str) -> list[tuple[int, int, str]]:
        if len(content) <= self.chunk_size:
            return [(0, len(content), "主标题")]
        markers: list[int] = []
        cursor = 0
        while True:
            marker = content.find("\n## ", cursor)
            if marker < 0:
                break
            markers.append(marker + 1)
            cursor = marker + 1
        if markers:
            starts = [0] + markers
            spans: list[tuple[int, int, str]] = []
            for index, start in enumerate(starts):
                end = starts[index + 1] if index + 1 < len(starts) else len(content)
                section = content[start:end]
                title = section.splitlines()[0].lstrip("# ").strip() if section else "正文"
                spans.append((start, end, title or "正文"))
            return spans
        step = self.chunk_size - self.chunk_overlap
        spans = []
        start = 0
        while start < len(content):
            end = min(start + self.chunk_size, len(content))
            spans.append((start, end, "正文"))
            if end >= len(content):
                break
            start += step
        return spans
