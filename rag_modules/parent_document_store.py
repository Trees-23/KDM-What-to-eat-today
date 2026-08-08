"""版本化 SQLite ParentDocumentStore。

该模块只负责读取已经校验并发布的父文档 build。写入由物化器通过
``create_build`` 完成；请求路径不会扫描 Markdown，也不会从 Milvus 反推正文。
"""

from __future__ import annotations

import hashlib
import json
import os
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any, Iterable, Iterator, Mapping, Optional, Sequence


SCHEMA_VERSION = "pds_schema_v1"


def text_hash(text: str) -> str:
    """返回正文的稳定 SHA-256 摘要。"""

    return hashlib.sha256(text.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class ParentRecord:
    parent_id: str
    node_type: str
    title: str
    full_content: str
    metadata: Mapping[str, Any] = field(default_factory=dict)
    content_hash: str = ""

    def with_hash(self) -> "ParentRecord":
        return ParentRecord(
            parent_id=self.parent_id,
            node_type=self.node_type,
            title=self.title,
            full_content=self.full_content,
            metadata=dict(self.metadata),
            content_hash=self.content_hash or text_hash(self.full_content),
        )


@dataclass(frozen=True)
class CanonicalChunk:
    chunk_id: str
    parent_id: str
    chunk_index: int
    total_chunks: int
    section_title: str
    text: str
    build_id: str
    text_hash: str = ""

    def with_hash(self) -> "CanonicalChunk":
        return CanonicalChunk(
            chunk_id=self.chunk_id,
            parent_id=self.parent_id,
            chunk_index=self.chunk_index,
            total_chunks=self.total_chunks,
            section_title=self.section_title,
            text=self.text,
            build_id=self.build_id,
            text_hash=self.text_hash or text_hash(self.text),
        )


@dataclass(frozen=True)
class AnchorRecord:
    anchor_type: str
    anchor_id: str
    parent_id: str
    build_id: str
    chunk_id: str
    ordinal: int
    source_relation: str


@dataclass(frozen=True)
class BuildManifest:
    build_id: str
    source_fingerprint: str
    builder_version: str
    chunk_config: Mapping[str, Any]
    created_at: str
    status: str
    parent_count: int = 0
    chunk_count: int = 0
    anchor_count: int = 0


@dataclass(frozen=True)
class ParentDocument:
    parent_id: str
    node_type: str
    title: str
    full_content: str
    build_id: str
    content_hash: str
    metadata: Mapping[str, Any]


@dataclass(frozen=True)
class TextEvidenceSource:
    parent_id: str
    build_id: str
    chunk_id: str
    chunk_index: int
    total_chunks: int
    section_title: str
    text: str
    anchor_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class LinkageReport:
    total_rows: int
    matched_rows: int
    missing_rows: tuple[str, ...] = ()
    mismatched_rows: tuple[str, ...] = ()

    @property
    def valid(self) -> bool:
        return not self.missing_rows and not self.mismatched_rows


class ParentDocumentBuildError(RuntimeError):
    """PDS 写入后校验失败；保留 staging SQLite 以便诊断。"""

    def __init__(self, message: str, staging_path: Path) -> None:
        super().__init__(message)
        self.staging_path = staging_path


SCHEMA_SQL = """
PRAGMA foreign_keys = ON;
CREATE TABLE builds (
    build_id TEXT PRIMARY KEY,
    source_fingerprint TEXT NOT NULL,
    builder_version TEXT NOT NULL,
    chunk_config TEXT NOT NULL,
    created_at TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('staging', 'ready', 'published', 'failed')),
    parent_count INTEGER NOT NULL DEFAULT 0,
    chunk_count INTEGER NOT NULL DEFAULT 0,
    anchor_count INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE parents (
    parent_id TEXT NOT NULL,
    build_id TEXT NOT NULL,
    node_type TEXT NOT NULL,
    title TEXT NOT NULL,
    full_content TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    metadata_json TEXT NOT NULL,
    PRIMARY KEY (parent_id, build_id),
    FOREIGN KEY (build_id) REFERENCES builds(build_id)
);
CREATE TABLE chunks (
    chunk_id TEXT NOT NULL,
    build_id TEXT NOT NULL,
    parent_id TEXT NOT NULL,
    chunk_index INTEGER NOT NULL,
    total_chunks INTEGER NOT NULL,
    section_title TEXT NOT NULL DEFAULT '',
    text TEXT NOT NULL,
    text_hash TEXT NOT NULL,
    PRIMARY KEY (chunk_id, build_id),
    UNIQUE (parent_id, build_id, chunk_index),
    FOREIGN KEY (parent_id, build_id) REFERENCES parents(parent_id, build_id),
    CHECK (chunk_index >= 0),
    CHECK (total_chunks > 0),
    CHECK (chunk_index < total_chunks)
);
CREATE TABLE anchors (
    anchor_type TEXT NOT NULL,
    anchor_id TEXT NOT NULL,
    parent_id TEXT NOT NULL,
    build_id TEXT NOT NULL,
    chunk_id TEXT NOT NULL,
    ordinal INTEGER NOT NULL,
    source_relation TEXT NOT NULL,
    PRIMARY KEY (anchor_type, anchor_id, build_id),
    FOREIGN KEY (chunk_id, build_id) REFERENCES chunks(chunk_id, build_id),
    FOREIGN KEY (parent_id, build_id) REFERENCES parents(parent_id, build_id)
);
CREATE INDEX chunks_parent_order ON chunks(build_id, parent_id, chunk_index);
CREATE INDEX anchors_parent_order ON anchors(build_id, parent_id, ordinal);
"""


class ParentDocumentStore:
    """读取不可变 PDS build，并提供原子 build 发布辅助。"""

    def __init__(
        self,
        db_path: Path,
        connection: sqlite3.Connection,
        *,
        active_build_id: Optional[str] = None,
        active_pointer: Optional[Path] = None,
    ) -> None:
        self.db_path = Path(db_path)
        self._connection = connection
        self.active_pointer = Path(active_pointer) if active_pointer else None
        self._active_build_id = active_build_id or self._read_active_pointer()
        if self._active_build_id is None:
            row = self._connection.execute(
                "SELECT build_id FROM builds WHERE status = 'published' ORDER BY created_at DESC LIMIT 1"
            ).fetchone()
            self._active_build_id = row[0] if row else None
        if self._active_build_id is None:
            raise ValueError("PDS 没有 active build")
        self._assert_build_exists(self._active_build_id)

    @classmethod
    def open(
        cls,
        path: str | os.PathLike[str],
        *,
        active_build_id: Optional[str] = None,
        active_pointer: Optional[str | os.PathLike[str]] = None,
        read_only: bool = True,
    ) -> "ParentDocumentStore":
        pointer_path = Path(active_pointer).expanduser().resolve() if active_pointer else None
        db_path = Path(path).expanduser().resolve()
        if db_path.is_dir():
            if pointer_path is None:
                raise ValueError("PDS 目录打开方式需要 active_pointer")
            pointer_data = cls._read_pointer(pointer_path)
            store_path = pointer_data.get("store_path")
            if not store_path:
                raise ValueError("active pointer 未记录 store_path")
            db_path = Path(store_path)
            if not db_path.is_absolute():
                db_path = pointer_path.parent / db_path
            db_path = db_path.resolve()
        if not db_path.exists():
            raise FileNotFoundError(f"PDS build 不存在: {db_path}")
        if read_only:
            connection = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        else:
            connection = sqlite3.connect(str(db_path))
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return cls(
            db_path,
            connection,
            active_build_id=active_build_id,
            active_pointer=pointer_path,
        )

    @classmethod
    def create_build(
        cls,
        path: str | os.PathLike[str],
        manifest: BuildManifest,
        parents: Iterable[ParentRecord],
        chunks: Iterable[CanonicalChunk],
        anchors: Iterable[AnchorRecord],
        *,
        publish: bool = False,
        active_pointer: Optional[str | os.PathLike[str]] = None,
    ) -> Path:
        """在临时 SQLite 中完成全部校验后原子发布一个新 build。"""

        destination = Path(path).expanduser().resolve()
        if publish and not active_pointer:
            raise ValueError("发布 PDS build 必须提供 active_pointer")
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            raise FileExistsError(f"目标 PDS 已存在，拒绝覆盖: {destination}")

        parent_rows = [parent.with_hash() for parent in parents]
        chunk_rows = [chunk.with_hash() for chunk in chunks]
        anchor_rows = list(anchors)
        calculated_manifest = make_build_manifest(
            parent_rows,
            chunks=chunk_rows,
            anchors=anchor_rows,
            chunk_config=manifest.chunk_config,
            builder_version=manifest.builder_version,
        )
        if (
            manifest.build_id != calculated_manifest.build_id
            or manifest.source_fingerprint != calculated_manifest.source_fingerprint
        ):
            raise ValueError("传入 manifest 与待持久化 PDS 工件不一致")
        expected_manifest = BuildManifest(
            **{
                **manifest.__dict__,
                "status": "staging",
                "parent_count": len(parent_rows),
                "chunk_count": len(chunk_rows),
                "anchor_count": len(anchor_rows),
            }
        )

        temp_path: Optional[Path] = None
        connection: Optional[sqlite3.Connection] = None
        try:
            with NamedTemporaryFile(
                prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent, delete=False
            ) as temp:
                temp_path = Path(temp.name)
            connection = sqlite3.connect(str(temp_path))
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA foreign_keys = ON")
            connection.executescript(SCHEMA_SQL)
            connection.execute(
                """INSERT INTO builds
                   (build_id, source_fingerprint, builder_version, chunk_config,
                    created_at, status, parent_count, chunk_count, anchor_count)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    expected_manifest.build_id,
                    expected_manifest.source_fingerprint,
                    expected_manifest.builder_version,
                    json.dumps(dict(expected_manifest.chunk_config), sort_keys=True, ensure_ascii=False),
                    expected_manifest.created_at,
                    "staging",
                    expected_manifest.parent_count,
                    expected_manifest.chunk_count,
                    expected_manifest.anchor_count,
                ),
            )
            connection.executemany(
                """INSERT INTO parents
                   (parent_id, build_id, node_type, title, full_content, content_hash, metadata_json)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                [
                    (
                        parent.parent_id,
                        expected_manifest.build_id,
                        parent.node_type,
                        parent.title,
                        parent.full_content,
                        parent.content_hash,
                        json.dumps(dict(parent.metadata), sort_keys=True, ensure_ascii=False),
                    )
                    for parent in parent_rows
                ],
            )
            connection.executemany(
                """INSERT INTO chunks
                   (chunk_id, build_id, parent_id, chunk_index, total_chunks,
                    section_title, text, text_hash)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                [
                    (
                        chunk.chunk_id,
                        expected_manifest.build_id,
                        chunk.parent_id,
                        chunk.chunk_index,
                        chunk.total_chunks,
                        chunk.section_title,
                        chunk.text,
                        chunk.text_hash,
                    )
                    for chunk in chunk_rows
                ],
            )
            connection.executemany(
                """INSERT INTO anchors
                   (anchor_type, anchor_id, parent_id, build_id, chunk_id, ordinal, source_relation)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                [
                    (
                        anchor.anchor_type,
                        anchor.anchor_id,
                        anchor.parent_id,
                        expected_manifest.build_id,
                        anchor.chunk_id,
                        anchor.ordinal,
                        anchor.source_relation,
                    )
                    for anchor in anchor_rows
                ],
            )
            connection.execute("UPDATE builds SET status = 'ready' WHERE build_id = ?", (expected_manifest.build_id,))
            connection.commit()
            cls._verify_connection(connection, expected_manifest.build_id)
            connection.close()
            connection = None

            os.replace(temp_path, destination)
            temp_path = None

            if publish and active_pointer:
                cls._write_active_pointer(Path(active_pointer), expected_manifest.build_id, destination)
            return destination
        except Exception as error:
            if connection is not None:
                connection.close()
            if temp_path and temp_path.exists():
                raise ParentDocumentBuildError(
                    f"PDS 构建失败，已保留 staging 文件: {temp_path}", temp_path
                ) from error
            raise

    @classmethod
    def publish_existing_build(
        cls,
        path: str | os.PathLike[str],
        build_id: str,
        active_pointer: str | os.PathLike[str],
    ) -> None:
        """把 active 指针原子切回已验证的历史 build，不改写 SQLite 内容。"""

        db_path = Path(path).expanduser().resolve()
        if not db_path.is_file():
            raise FileNotFoundError(f"历史 PDS build 不存在: {db_path}")
        connection = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        connection.row_factory = sqlite3.Row
        try:
            cls._verify_connection(connection, build_id)
            status = connection.execute(
                "SELECT status FROM builds WHERE build_id = ?", (build_id,)
            ).fetchone()["status"]
            if status not in {"ready", "published"}:
                raise ValueError(f"只能切回已验证 build: {build_id}")
        finally:
            connection.close()
        cls._write_active_pointer(Path(active_pointer), build_id, db_path)

    @staticmethod
    def _write_active_pointer(pointer: Path, build_id: str, store_path: Path) -> None:
        pointer = pointer.expanduser().resolve()
        pointer.parent.mkdir(parents=True, exist_ok=True)
        with NamedTemporaryFile(prefix=f".{pointer.name}.", dir=pointer.parent, mode="w", encoding="utf-8", delete=False) as temp_pointer:
            json.dump(
                {"build_id": build_id, "store_path": str(store_path.resolve())},
                temp_pointer,
                ensure_ascii=False,
                sort_keys=True,
            )
            temp_pointer.write("\n")
            temp_pointer.flush()
            os.fsync(temp_pointer.fileno())
            pointer_tmp = Path(temp_pointer.name)
        os.replace(pointer_tmp, pointer)

    @staticmethod
    def _verify_connection(connection: sqlite3.Connection, build_id: str) -> None:
        integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
        if integrity != "ok":
            raise ValueError(f"PDS integrity_check 失败: {integrity}")
        foreign_keys = connection.execute("PRAGMA foreign_key_check").fetchall()
        if foreign_keys:
            raise ValueError(f"PDS foreign_key_check 失败: {foreign_keys[:3]}")
        row = connection.execute(
            "SELECT status FROM builds WHERE build_id = ?", (build_id,)
        ).fetchone()
        if row is None or row[0] not in {"ready", "published"}:
            raise ValueError(f"PDS build 未通过状态校验: {build_id}")
        parent_rows = connection.execute(
            "SELECT parent_id, full_content, content_hash FROM parents WHERE build_id = ?", (build_id,)
        ).fetchall()
        for parent in parent_rows:
            if text_hash(parent["full_content"]) != parent["content_hash"]:
                raise ValueError(f"PDS parent 哈希校验失败: {parent['parent_id']}")
        chunk_rows = connection.execute(
            "SELECT chunk_id, text, text_hash FROM chunks WHERE build_id = ?", (build_id,)
        ).fetchall()
        for chunk in chunk_rows:
            if text_hash(chunk["text"]) != chunk["text_hash"]:
                raise ValueError(f"PDS chunk 哈希校验失败: {chunk['chunk_id']}")
        counts = connection.execute(
            """SELECT b.parent_count, b.chunk_count, b.anchor_count,
                      (SELECT count(*) FROM parents p WHERE p.build_id = b.build_id) AS actual_parents,
                      (SELECT count(*) FROM chunks c WHERE c.build_id = b.build_id) AS actual_chunks,
                      (SELECT count(*) FROM anchors a WHERE a.build_id = b.build_id) AS actual_anchors
               FROM builds b WHERE b.build_id = ?""",
            (build_id,),
        ).fetchone()
        if counts is None or tuple(counts[:3]) != tuple(counts[3:]):
            raise ValueError(f"PDS 记录数校验失败: {build_id}")
        mismatched_anchor = connection.execute(
            """SELECT a.anchor_id FROM anchors a
               JOIN chunks c ON c.chunk_id = a.chunk_id AND c.build_id = a.build_id
               WHERE a.build_id = ? AND a.parent_id <> c.parent_id LIMIT 1""",
            (build_id,),
        ).fetchone()
        if mismatched_anchor is not None:
            raise ValueError(f"PDS anchor 父文档不一致: {mismatched_anchor['anchor_id']}")
        parent_without_chunk = connection.execute(
            """SELECT p.parent_id FROM parents p
               LEFT JOIN chunks c ON c.parent_id = p.parent_id AND c.build_id = p.build_id
               WHERE p.build_id = ? GROUP BY p.parent_id HAVING count(c.chunk_id) = 0 LIMIT 1""",
            (build_id,),
        ).fetchone()
        if parent_without_chunk is not None:
            raise ValueError(f"PDS 父文档缺少 chunk: {parent_without_chunk['parent_id']}")

    def _read_active_pointer(self) -> Optional[str]:
        if not self.active_pointer or not self.active_pointer.exists():
            return None
        return self._read_pointer(self.active_pointer).get("build_id")

    @staticmethod
    def _read_pointer(pointer: Path) -> Mapping[str, str]:
        raw = pointer.read_text(encoding="utf-8").strip()
        if not raw:
            return {}
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            # 兼容第一版只保存 build_id 的指针；目录打开方式仍要求新格式的 store_path。
            return {"build_id": raw}
        if not isinstance(parsed, Mapping):
            raise ValueError(f"active pointer 格式错误: {pointer}")
        return {str(key): str(value) for key, value in parsed.items() if value is not None}

    def _assert_build_exists(self, build_id: str) -> None:
        row = self._connection.execute(
            "SELECT 1 FROM builds WHERE build_id = ? AND status IN ('ready', 'published')", (build_id,)
        ).fetchone()
        if row is None:
            raise ValueError(f"PDS active build 不存在或未通过校验: {build_id}")

    @property
    def active_build_id(self) -> str:
        return self._active_build_id

    def health_check(self) -> dict[str, Any]:
        self._verify_connection(self._connection, self.active_build_id)
        manifest = self.get_build_manifest(self.active_build_id)
        return {
            "status": "ok",
            "build_id": manifest.build_id,
            "parent_count": manifest.parent_count,
            "chunk_count": manifest.chunk_count,
            "anchor_count": manifest.anchor_count,
        }

    def get_full_parent(self, parent_id: str, expected_node_type: Optional[str] = None) -> Optional[ParentDocument]:
        row = self._connection.execute(
            """SELECT parent_id, node_type, title, full_content, build_id, content_hash, metadata_json
               FROM parents WHERE parent_id = ? AND build_id = ?""",
            (parent_id, self.active_build_id),
        ).fetchone()
        if row is None or (expected_node_type and row["node_type"] != expected_node_type):
            return None
        return ParentDocument(
            parent_id=row["parent_id"],
            node_type=row["node_type"],
            title=row["title"],
            full_content=row["full_content"],
            build_id=row["build_id"],
            content_hash=row["content_hash"],
            metadata=json.loads(row["metadata_json"]),
        )

    def get_chunk_window(
        self, parent_id: str, anchor_chunk_id: str, before: int, after: int
    ) -> list[TextEvidenceSource]:
        if before < 0 or after < 0:
            raise ValueError("before/after 必须为非负整数")
        anchor = self._connection.execute(
            """SELECT chunk_index FROM chunks
               WHERE chunk_id = ? AND parent_id = ? AND build_id = ?""",
            (anchor_chunk_id, parent_id, self.active_build_id),
        ).fetchone()
        if anchor is None:
            return []
        index = int(anchor["chunk_index"])
        rows = self._connection.execute(
            """SELECT c.chunk_id, c.parent_id, c.build_id, c.chunk_index,
                      c.total_chunks, c.section_title, c.text,
                      GROUP_CONCAT(a.anchor_id) AS anchor_ids
               FROM chunks c
               LEFT JOIN anchors a ON a.chunk_id = c.chunk_id AND a.build_id = c.build_id
               WHERE c.parent_id = ? AND c.build_id = ?
                 AND c.chunk_index BETWEEN ? AND ?
               GROUP BY c.chunk_id, c.parent_id, c.build_id, c.chunk_index,
                        c.total_chunks, c.section_title, c.text
               ORDER BY c.chunk_index""",
            (parent_id, self.active_build_id, max(0, index - before), index + after),
        ).fetchall()
        return [self._evidence_from_row(row) for row in rows]

    def get_anchor_window(
        self, parent_id: str, anchor_type: str, anchor_id: str, before: int, after: int
    ) -> list[TextEvidenceSource]:
        anchor = self._connection.execute(
            """SELECT chunk_id FROM anchors
               WHERE parent_id = ? AND anchor_type = ? AND anchor_id = ? AND build_id = ?""",
            (parent_id, anchor_type, anchor_id, self.active_build_id),
        ).fetchone()
        if anchor is None:
            return []
        return self.get_chunk_window(parent_id, anchor["chunk_id"], before, after)

    def get_build_manifest(self, build_id: str) -> BuildManifest:
        row = self._connection.execute("SELECT * FROM builds WHERE build_id = ?", (build_id,)).fetchone()
        if row is None:
            raise KeyError(f"未知 PDS build: {build_id}")
        return BuildManifest(
            build_id=row["build_id"],
            source_fingerprint=row["source_fingerprint"],
            builder_version=row["builder_version"],
            chunk_config=json.loads(row["chunk_config"]),
            created_at=row["created_at"],
            status=row["status"],
            parent_count=row["parent_count"],
            chunk_count=row["chunk_count"],
            anchor_count=row["anchor_count"],
        )

    def iter_chunks(self, build_id: Optional[str] = None) -> Iterator[CanonicalChunk]:
        selected_build = build_id or self.active_build_id
        self._assert_build_exists(selected_build)
        rows = self._connection.execute(
            """SELECT chunk_id, parent_id, chunk_index, total_chunks,
                      section_title, text, build_id, text_hash
               FROM chunks WHERE build_id = ? ORDER BY parent_id, chunk_index""",
            (selected_build,),
        )
        for row in rows:
            yield CanonicalChunk(
                chunk_id=row["chunk_id"],
                parent_id=row["parent_id"],
                chunk_index=row["chunk_index"],
                total_chunks=row["total_chunks"],
                section_title=row["section_title"],
                text=row["text"],
                build_id=row["build_id"],
                text_hash=row["text_hash"],
            )

    def validate_chunk_linkage(self, rows_from_milvus: Iterable[Mapping[str, Any]]) -> LinkageReport:
        rows = list(rows_from_milvus)
        missing: list[str] = []
        mismatched: list[str] = []
        matched = 0
        for item in rows:
            chunk_id = str(item.get("chunk_id", ""))
            row = self._connection.execute(
                """SELECT parent_id, text_hash FROM chunks
                   WHERE chunk_id = ? AND build_id = ?""",
                (chunk_id, self.active_build_id),
            ).fetchone()
            if row is None:
                missing.append(chunk_id)
                continue
            expected_parent = str(row["parent_id"])
            given_parent = str(item.get("parent_id", ""))
            given_hash = item.get("text_hash")
            if given_parent != expected_parent or (given_hash is not None and given_hash != row["text_hash"]):
                mismatched.append(chunk_id)
                continue
            matched += 1
        return LinkageReport(len(rows), matched, tuple(missing), tuple(mismatched))

    def close(self) -> None:
        self._connection.close()

    def __enter__(self) -> "ParentDocumentStore":
        return self

    def __exit__(self, *_exc: Any) -> None:
        self.close()

    @staticmethod
    def _evidence_from_row(row: sqlite3.Row) -> TextEvidenceSource:
        anchor_ids = tuple(filter(None, (row["anchor_ids"] or "").split(",")))
        return TextEvidenceSource(
            parent_id=row["parent_id"],
            build_id=row["build_id"],
            chunk_id=row["chunk_id"],
            chunk_index=row["chunk_index"],
            total_chunks=row["total_chunks"],
            section_title=row["section_title"],
            text=row["text"],
            anchor_ids=anchor_ids,
        )


def make_build_manifest(
    parents: Sequence[ParentRecord],
    *,
    chunk_config: Mapping[str, Any],
    builder_version: str,
    chunks: Sequence[CanonicalChunk] = (),
    anchors: Sequence[AnchorRecord] = (),
    build_id: Optional[str] = None,
    created_at: Optional[str] = None,
) -> BuildManifest:
    """依据全部持久化内容生成可复现 build_id 和 source_fingerprint。"""

    normalized_parents = [
        {
            "parent_id": parent.parent_id,
            "node_type": parent.node_type,
            "title": parent.title,
            "content_hash": parent.with_hash().content_hash,
            "metadata": dict(parent.metadata),
        }
        for parent in sorted(parents, key=lambda item: (item.parent_id, item.node_type))
    ]
    normalized_chunks = [
        {
            "chunk_id": chunk.chunk_id,
            "parent_id": chunk.parent_id,
            "chunk_index": chunk.chunk_index,
            "total_chunks": chunk.total_chunks,
            "section_title": chunk.section_title,
            "text_hash": chunk.with_hash().text_hash,
        }
        for chunk in sorted(chunks, key=lambda item: (item.parent_id, item.chunk_index, item.chunk_id))
    ]
    normalized_anchors = [
        {
            "anchor_type": anchor.anchor_type,
            "anchor_id": anchor.anchor_id,
            "parent_id": anchor.parent_id,
            "chunk_id": anchor.chunk_id,
            "ordinal": anchor.ordinal,
            "source_relation": anchor.source_relation,
        }
        for anchor in sorted(
            anchors,
            key=lambda item: (item.parent_id, item.anchor_type, item.ordinal, item.anchor_id),
        )
    ]
    source_snapshot = {
        "schema_version": SCHEMA_VERSION,
        "parents": normalized_parents,
        "chunks": normalized_chunks,
        "anchors": normalized_anchors,
    }
    source_payload = json.dumps(
        source_snapshot,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )
    source_fingerprint = hashlib.sha256(source_payload.encode("utf-8")).hexdigest()
    config_payload = json.dumps(dict(chunk_config), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    build_payload = json.dumps(
        {"builder_version": builder_version, "chunk_config": config_payload, "artifact": source_snapshot},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )
    computed_build_id = "pds_" + hashlib.sha256(build_payload.encode("utf-8")).hexdigest()[:24]
    if build_id and build_id != computed_build_id:
        raise ValueError(f"指定 build_id 与内容计算值不一致: {build_id} != {computed_build_id}")
    return BuildManifest(
        build_id=computed_build_id,
        source_fingerprint=source_fingerprint,
        builder_version=builder_version,
        chunk_config=dict(chunk_config),
        created_at=created_at or datetime.now(timezone.utc).isoformat(),
        status="staging",
    )
