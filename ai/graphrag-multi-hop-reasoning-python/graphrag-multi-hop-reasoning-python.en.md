The current approach to designing LLMs within AI engineering is oversimplified. According to the echo chamber’s view, solving LLM hallucinations is easy: simply design a standard Retrieval-Augmented Generation (RAG) system in which you break your PDFs into 1,000-token chunks, embed them, insert them into a vector database, and perform cosine similarity searches.

It works perfectly well…until you actually deploy it.

After deployment, companies quickly discover that using only chunked text for retrieval does not work well for complex questions. The standard RAG assumes that semantic similarity implies relevance, which is not necessarily the case. When users ask a “multi-hop” question that requires making connections between Concept A and Concept B through Concept C, standard RAG will not work because these concepts usually don’t coexist in the same chunk of text. RAG also falls apart at global summarization (“what are the major risk factors discussed in all of our compliance reports?”)

> “The standard RAG assumes that semantic similarity implies relevance, which is not necessarily the case.”

If you are designing AI for enterprise systems, you need structured reasoning. Chunking text is fine, but you should stop doing it randomly. What you need is GraphRAG.

GraphRAG offers a powerful combination of the structural knowledge of knowledge graphs along with the semantic capabilities of vector search. This tutorial will explain how your current pipeline fails and help you implement a GraphRAG workflow using Python.

## The limits of naive vector search

We will now take apart a simple misconception that vector embeddings will save the day!

Assume you have a dataset of corporate contracts [stored in a vector](https://thenewstack.io/silent-llm-hallucination-loop/) database.

* **Chunk 1**: “Acme Corp acquired BetaTech in 2022.”
* **Chunk 2**: “Sarah Connor was appointed CEO of BetaTech in 2023.”

**The Query**: “Who leads the company that Acme Corp acquired?”

Naive vector search will embed the query and find the closest chunks. Inevitably, chunks with high similarity to “Acme Corp” and “leadership” will be found, but “Chunk 2” will be overlooked because “Sarah Connor” and “CEO of BetaTech” have nothing to do with “Acme Corp” semantically.

The regular RAG approach lacks a structured relationship with different entities. To answer multi-hop queries, you need to understand that there is an `(“Acme Corp”) - [ACQUIRED]` ->  `(BetaTech)` relationship, and `(“Sarah Connor”) - [LEADS] -> (BetaTech)`

This is where GraphRAG comes in.

## Enter GraphRAG

GraphRAG requires the LLM to process the documents during the ingestion step, extracting nodes (entities) and edges (relationships) to create a knowledge graph from your chunks.

Unlike traditional approaches, where queries consist of isolated text strings, in GraphRAG we first identify the starting node via vector search and then traverse the graph’s relationships to obtain a highly relevant subgraph for [reasoning with the LLM](https://thenewstack.io/how-diffusion-based-llm-ai-speeds-up-reasoning/).

Recently, frameworks such as Neo4j’s neo4j-graphrag have made this architecture accessible to everyone. We’ll use this framework to build a robust pipeline that performs ingestion, schema enforcement, and graph traversal.

## Practical implementation: Building GraphRAG in Python

We will build a pipeline [that can ingest unstructured text data](https://thenewstack.io/data-pipelines-serve-ai/), build a knowledge graph, and query the graph via dynamic Cipher traversal.

### Step 1: Install dependencies

You will need an active Neo4j database (local or cloud) and the following packages:

```

Bash
pip install neo4j neo4j-graphrag openai python-dotenv

```

### Step 2: Initialize connections and production guardrails

Production-ready pipelines require proper credential management and resilience.

GraphRAG ingestion is extremely expensive in terms of LLM API requests. Without configuring a rate-limit handler, your pipeline will fail with a `RateLimitError` on the first real document.

```

Python
import os
from neo4j import GraphDatabase
from neo4j_graphrag.llm import OpenAILLM
from neo4j_graphrag.embeddings import OpenAIEmbeddings 
from neo4j_graphrag.utils.rate_limit import RetryRateLimitHandler

# Initialize Neo4j Driver
neo4j_uri = os.environ.get("NEO4J_URI")
neo4j_user = os.environ.get("NEO4J_USERNAME")
neo4j_password = os.environ.get("NEO4J_PASSWORD")

if not all([neo4j_uri, neo4j_user, neo4j_password]):
raise ValueError("Missing required Neo4j environment variables (NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD).")

driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))
driver.verify_connectivity() 

# Initialize LLM with strict rate limiting for heavy extraction tasks
llm = OpenAILLM(
    model_name="gpt-4o",
    model_params={"temperature": 0},
    rate_limit_handler=RetryRateLimitHandler(max_attempts=5, min_wait=2.0)
)
embedder = OpenAIEmbeddings(model="text-embedding-3-small")

```

### Step 3: Enforcing schema in the knowledge graph builder

An unstructured graph is nothing more than an unorganized database. The moment you do not provide a proper schema, your LLM will hallucinate entity labels, duplicating nodes of “Acme Corp”, “Acme Corporation,” and “Ame.” We will build our architecture beforehand and feed it into the pipeline.

> “An unstructured graph is nothing more than an unorganized database.”

```

Python
from neo4j_graphrag.experimental.pipeline.kg_builder import SimpleKGPipeline

# Define explicit schema to prevent LLM hallucinations during extraction
schema = {
    "node_types": ["Organization", "Person", "Technology"],
    "relationship_types": ["ACQUIRED", "LEADS", "DEVELOPS"],
    "patterns": [
        ("Organization", "ACQUIRED", "Organization"),
        ("Person", "LEADS", "Organization")
    ]
}

# Define the pipeline enforcing the schema
kg_builder = SimpleKGPipeline(
    llm=llm,
    driver=driver,
    embedder=embedder,
    schema=schema
)

sample_text = """
Acme Corp acquired BetaTech in 2022. 
In 2023, Sarah Connor was appointed CEO of BetaTech to drive AI initiatives.
"""

import asyncio

# Execute extraction and graph population
asyncio.run(kg_builder.run_async(text=sample_text)) 

```

*Engineering note*: Under the hood, this pipeline still splits your text using a `FixedSizeSplitter`. The difference is that it uses the LLM to extract the semantic architecture *from* those chunks before saving them.

### Step 4: The vector Cipher retriever

This is where multi-hop reasoning happens. An ordinary vector retriever will provide us with nodes. To travel across the graph, we use a VectorCypherRetriever. We will embed the query, identify the semantic entry point, and finally perform a Cipher query on all the 1-hop connected neighbors.

```

Python
from neo4j_graphrag.retrievers import VectorCypherRetriever

# Define the traversal logic: Find the vector match, then expand 1-hop to get relationships
traversal_query = """
MATCH (node)[r](neighbor)
RETURN "Entity: " + coalesce(node.id, '') + " (Info: " + coalesce(node.text, '') + ") | " +
"Relationship: " + type(r) + " | " +
"Neighbor: " + coalesce(neighbor.id, '') + " (Info: " + coalesce(neighbor.text, '') + ")" AS text,
score
""" 

# Initialize a VectorCypherRetriever to enable actual GraphRAG
retriever = VectorCypherRetriever(
    driver=driver,
    index_name="entity_vector_index",
    embedder=embedder,
    retrieval_query=traversal_query
)

query = "Who leads the company that Acme Corp acquired?"

# Retrieve connected context based on the query
retrieved_context = retriever.search(query_text=query, top_k=3)

print(retrieved_context)

```

The retrieved context includes BetaTech, its acquisition by Acme Corp, and the fact that Sarah Connor leads it, since we provided a specific schema for retrieving relations. The LLM now has all the facts it needs to provide an accurate response.

## Lessons learned: What engineers must know before adopting GraphRAG

If you want to upgrade your RAG system, consider the following trade-offs:

1. **Ingestion cost is high**, whereas RAG costs are low because embedding models are inexpensive. To ingest each document chunk in GraphRAG, you need an LLM like GPT-4o to extract entities from the document. Filter your enterprise data carefully.
2. **Schema design is not optional:** As shown in step 3, you shouldn’t ignore data modeling. The schema is the difference between an efficient retrieval engine and a mess of nodes.
3. **Observability is superior**: To debug your naive RAG, you need to examine big floating-point arrays. To debug GraphRAG, you only need to look at your Neo4j dashboard to view the nodes. It is easy to see if the LLM has hallucinated.

Standard vector search is a very powerful solution, but treating it as a one-size-fits-all fix for enterprise AI is an easy way out. Real-world use cases need explicit data modeling and deterministic search capabilities.

> “Standard vector search is a very powerful solution, but treating it as a one-size-fits-all fix for enterprise AI is an easy way out.”

GraphRAG demands more intentionality in its design, strict guidelines to follow, and greater upfront computational effort. However, the rewards are immense: GraphRAG gives you the power to do something truly valuable—multi-hop reasoning over data, which is exactly what enterprises desire.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.