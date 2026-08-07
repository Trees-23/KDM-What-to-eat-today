// Incremental import for data/tips markdown knowledge.
// Run after generate_tips_csv.py has created tips_nodes.csv and tips_relationships.csv.

CREATE CONSTRAINT technique_doc_id_unique IF NOT EXISTS FOR (t:TechniqueDoc) REQUIRE t.nodeId IS UNIQUE;
CREATE CONSTRAINT technique_chunk_id_unique IF NOT EXISTS FOR (c:TechniqueChunk) REQUIRE c.nodeId IS UNIQUE;

CREATE INDEX technique_doc_name_index IF NOT EXISTS FOR (t:TechniqueDoc) ON (t.name);
CREATE INDEX technique_doc_category_index IF NOT EXISTS FOR (t:TechniqueDoc) ON (t.category);
CREATE INDEX technique_chunk_title_index IF NOT EXISTS FOR (c:TechniqueChunk) ON (c.title);

CREATE FULLTEXT INDEX technique_doc_fulltext_index IF NOT EXISTS FOR (t:TechniqueDoc) ON EACH [t.name, t.title, t.summary, t.content, t.tags];
CREATE FULLTEXT INDEX technique_chunk_fulltext_index IF NOT EXISTS FOR (c:TechniqueChunk) ON EACH [c.name, c.title, c.sectionTitle, c.summary, c.content, c.tags];

LOAD CSV WITH HEADERS FROM 'file:///tips_nodes.csv' AS row
WITH row
WHERE row.labels = 'TechniqueDoc'
  AND row.nodeId IS NOT NULL
  AND row.nodeId <> ''
  AND row.name IS NOT NULL
  AND row.name <> ''
MERGE (t:TechniqueDoc {nodeId: row.nodeId})
SET t.name = row.name,
    t.title = row.title,
    t.category = row.category,
    t.sourcePath = row.sourcePath,
    t.tags = row.tags,
    t.summary = row.summary,
    t.content = row.content,
    t.conceptType = 'TechniqueDoc',
    t.originalLabels = row.labels;

LOAD CSV WITH HEADERS FROM 'file:///tips_nodes.csv' AS row
WITH row
WHERE row.labels = 'TechniqueChunk'
  AND row.nodeId IS NOT NULL
  AND row.nodeId <> ''
  AND row.name IS NOT NULL
  AND row.name <> ''
MERGE (c:TechniqueChunk {nodeId: row.nodeId})
SET c.name = row.name,
    c.title = row.title,
    c.sectionTitle = row.sectionTitle,
    c.category = row.category,
    c.sourcePath = row.sourcePath,
    c.chunkIndex = CASE
        WHEN row.chunkIndex IS NOT NULL AND row.chunkIndex <> ''
        THEN toInteger(row.chunkIndex)
        ELSE null
    END,
    c.tags = row.tags,
    c.summary = row.summary,
    c.content = row.content,
    c.conceptType = 'TechniqueChunk',
    c.originalLabels = row.labels;

LOAD CSV WITH HEADERS FROM 'file:///tips_relationships.csv' AS row
WITH row
WHERE row.relationshipType = 'HAS_CHUNK'
  AND row.startNodeId IS NOT NULL
  AND row.endNodeId IS NOT NULL
MATCH (source:TechniqueDoc {nodeId: row.startNodeId})
MATCH (target:TechniqueChunk {nodeId: row.endNodeId})
MERGE (source)-[r:HAS_CHUNK]->(target)
SET r.relationshipId = row.relationshipId,
    r.chunkOrder = CASE
        WHEN row.chunkOrder IS NOT NULL AND row.chunkOrder <> ''
        THEN toInteger(row.chunkOrder)
        ELSE null
    END,
    r.originalType = row.relationshipType;

MATCH (n)
WHERE (n:TechniqueDoc OR n:TechniqueChunk)
  AND n.category IS NOT NULL
  AND n.category <> ''
MERGE (cat:Category {name: n.category})
MERGE (n)-[:BELONGS_TO_CATEGORY]->(cat);

MATCH (n)
WHERE (n:TechniqueDoc OR n:TechniqueChunk)
  AND n.conceptType IS NOT NULL
  AND n.conceptType <> ''
MERGE (ct:ConceptType {name: n.conceptType})
MERGE (n)-[:HAS_CONCEPT_TYPE]->(ct);

MATCH (t:TechniqueDoc)-[:HAS_CHUNK]->(c:TechniqueChunk)
RETURN count(DISTINCT t) AS technique_docs, count(DISTINCT c) AS technique_chunks;
