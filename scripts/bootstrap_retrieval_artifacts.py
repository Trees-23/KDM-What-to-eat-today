#!/usr/bin/env python3
"""Build and publish the local PDS/Milvus retrieval artifact from Neo4j.

This command is intended for the Compose-managed local deployment. It never
deletes an existing Milvus collection: a changed graph produces a new PDS build
and collection, then atomically publishes the new manifest.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rag_modules.milvus_v2_index import (
    MilvusV2IndexBuilder,
    RetrievalArtifactManifest,
    create_milvus_client,
    pds_manifest_sha256,
)
from rag_modules.parent_document_materializer import ParentDocumentMaterializer
from rag_modules.parent_document_store import ParentDocumentStore


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="从 Neo4j 构建并发布本地检索工件")
    parser.add_argument("--neo4j-uri", required=True)
    parser.add_argument("--neo4j-user", required=True)
    parser.add_argument("--neo4j-password", required=True)
    parser.add_argument("--neo4j-database", default="neo4j")
    parser.add_argument("--milvus-uri", required=True)
    parser.add_argument("--milvus-database", default="default")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--embedding-model", required=True)
    parser.add_argument("--dimension", default=512, type=int)
    return parser


def _load_previous_manifest(path: Path) -> RetrievalArtifactManifest | None:
    if not path.is_file():
        return None
    return RetrievalArtifactManifest.read(path)


def _embed(texts: list[str], model_name: str) -> list[list[float]]:
    from langchain_huggingface import HuggingFaceEmbeddings

    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
    return embeddings.embed_documents(texts)


def bootstrap(args: argparse.Namespace) -> dict[str, object]:
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    pointer = output_dir / "parent_store.active"
    artifact_path = output_dir / "retrieval_artifact_manifest.json"

    materializer = ParentDocumentMaterializer(
        uri=args.neo4j_uri,
        user=args.neo4j_user,
        password=args.neo4j_password,
        database=args.neo4j_database,
    )
    try:
        result = materializer.materialize_from_neo4j()
    finally:
        materializer.close()

    build_id = result.manifest.build_id
    store_path = output_dir / f"parent_store.{build_id}.sqlite"
    if not store_path.exists():
        result.write(str(store_path), publish=True, active_pointer=str(pointer))
        pds_action = "created"
    else:
        ParentDocumentStore.publish_existing_build(str(store_path), build_id, str(pointer))
        pds_action = "reused"

    collection = f"cooking_knowledge_v2_{build_id[:12]}"
    client = create_milvus_client(args.milvus_uri, args.milvus_database)
    with ParentDocumentStore.open(str(store_path), active_build_id=build_id, active_pointer=str(pointer)) as store:
        builder = MilvusV2IndexBuilder(
            client,
            parent_store=store,
            database=args.milvus_database,
            collection=collection,
            build_id=build_id,
            dimension=args.dimension,
            embedding_model=args.embedding_model,
        )
        if client.has_collection(collection_name=collection):
            vector_report = builder.verify_existing()
            vector_action = "reused"
        else:
            chunks = list(store.iter_chunks(build_id))
            vectors = _embed([chunk.text for chunk in chunks], args.embedding_model)
            vector_report = builder.build(vectors, confirm_create=True)
            vector_action = "created"
        manifest_hash = pds_manifest_sha256(store, build_id)

    previous = _load_previous_manifest(artifact_path)
    manifest = RetrievalArtifactManifest(
        pds_build_id=build_id,
        pds_manifest_sha256=manifest_hash,
        milvus_database=args.milvus_database,
        milvus_collection=collection,
        milvus_schema_hash=vector_report["schema_hash"],
        milvus_build_id=build_id,
        created_at=datetime.now(timezone.utc).isoformat(),
        rollback_database=previous.milvus_database if previous else args.milvus_database,
        rollback_collection=previous.milvus_collection if previous else collection,
        rollback_pds_build=previous.pds_build_id if previous else build_id,
    )
    manifest.write_atomic(artifact_path)
    return {
        "build_id": build_id,
        "collection": collection,
        "pds": pds_action,
        "milvus": vector_action,
        "chunk_count": vector_report["chunk_count"],
        "artifact_manifest": str(artifact_path),
    }


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    print(json.dumps(bootstrap(args), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
