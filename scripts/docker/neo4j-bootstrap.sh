#!/usr/bin/env bash

# Rebuild only the Compose-managed graph when the checked-in graph sources change.
set -euo pipefail

readonly NEO4J_URI="${NEO4J_URI:-bolt://neo4j:7687}"
readonly NEO4J_USER="${NEO4J_USER:-neo4j}"
readonly NEO4J_PASSWORD="${NEO4J_PASSWORD:?NEO4J_PASSWORD is required}"
readonly NEO4J_DATABASE="${NEO4J_DATABASE:-neo4j}"
readonly IMPORT_DIR="/import"

source_hash="$({
  sha256sum \
    "${IMPORT_DIR}/nodes.csv" \
    "${IMPORT_DIR}/relationships.csv" \
    "${IMPORT_DIR}/tips_nodes.csv" \
    "${IMPORT_DIR}/tips_relationships.csv" \
    "${IMPORT_DIR}/neo4j_import.cypher"
} | sha256sum | awk '{print $1}')"

cypher() {
  cypher-shell -a "${NEO4J_URI}" -u "${NEO4J_USER}" -p "${NEO4J_PASSWORD}" -d "${NEO4J_DATABASE}" "$@"
}

current_hash="$(cypher --format plain "MATCH (s:DeploymentState {key: 'recipe-graph'}) RETURN s.sourceHash AS sourceHash" 2>/dev/null | tail -n 1 | tr -d '"')"
if [[ "${current_hash}" == "${source_hash}" ]]; then
  echo "Neo4j graph source is unchanged; retaining the existing project data."
  exit 0
fi

echo "Neo4j graph source changed or is uninitialized; rebuilding the Compose-managed graph."
cypher "MATCH (n) DETACH DELETE n"
cypher -f "${IMPORT_DIR}/neo4j_import.cypher"
cypher "MERGE (s:DeploymentState {key: 'recipe-graph'}) SET s.sourceHash = '${source_hash}', s.updatedAt = datetime()"
echo "Neo4j graph rebuild completed for source ${source_hash}."
