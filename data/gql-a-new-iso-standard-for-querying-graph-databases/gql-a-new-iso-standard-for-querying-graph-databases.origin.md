# GQL: A New ISO Standard for Querying Graph Databases
![Featued image for: GQL: A New ISO Standard for Querying Graph Databases](https://cdn.thenewstack.io/media/2024/04/dba5470c-map-1024x683.png)
Graph databases are now officially a first-class entity in the world of computer science.
The International Standard for Organization (ISO) has published an international standard for querying graphs, called the
[Graph Query Language](https://www.iso.org/standard/76120.html) (ISO/IEC 39075:2024).
It is the first database query language that ISO had published since 1987 when it ratified
[SQL](https://thenewstack.io/how-to-write-sql-queries/) in that year. The standards body spent over five years sorting the details.
“There’s nothing like international formal standard, a sibling to SQL that comes out from the same organization as SQL, to speak volumes for the mainstream value” of GQL, said
[Philip Rathle](https://www.linkedin.com/in/prathle/), chief technology officer at [Neo4j](https://thenewstack.io/neo4j-funding-shows-graph-databases-gained-acceptance/), in an interview with TNS.
The release “marks a new chapter in the history of query languages, revolutionizing the way we interact with and harness the power of interconnected data,” said
[Tony Holland](https://www.linkedin.com/in/tonyhollanduk/), communications lead, [ISO/ IEC Joint Technical Committee 1/AG 1](https://www.linkedin.com/company/jtc1news/), in a statement. “GQL represents a significant step forward in data querying and manipulation, offering a unified and expressive language for navigating complex graph structures.”
In addition to expertise from Neo4J, engineers from
[HypergraphDB](https://hypergraphdb.org/), [Redis Labs](https://redis.com/?utm_content=inline+mention), [TigerGraph](https://thenewstack.io/tigergraph-graph-dbs-to-become-a-must-have-in-2022/), [Oracle](https://developer.oracle.com/?utm_content=inline+mention) and Germany’s University of Bonn [also participated in the project](https://www.gqlstandards.org/existing-languages). ![](https://cdn.thenewstack.io/media/2024/04/bd89fc7a-graph-visualization-example-1024x825-1.png)
A visualization of a graph database (courtesy: Neo4J)
## Advantages of Standardization
Ratification of the language by a global standards body, much like it did for SQL itself, brings assurance of its stability, encouraging users and tool vendors to further invest in the technology.
The basis for graph computing is the
[property graph](https://neo4j.com/blog/gql-international-standard/), which is superior in describing dynamically changing data.
Graph databases have been
[widely used for decades](https://thenewstack.io/neo4j-biggest-break-in-data-journalism/), and only recently, the form has generated new interest in being a [pivotal component](https://www.gartner.com/en/articles/understand-and-exploit-gen-ai-with-gartner-s-new-impact-radar) in [Large Language Model-](https://thenewstack.io/how-to-cure-llm-weaknesses-with-vector-databases/)based [Generative AI apps](https://thenewstack.io/will-generative-ai-kill-devsecops/). A graph model can visualize complex, interconnected systems.
The downside of LLMs is that they are black boxes of a sort, Rathle explained. “There’s no way to understand the reasoning behind the language model. It is just following a neural network and doing it’s doing its thing,” he said. A knowledge graph can serve as external memory, a way to visualize how the LLM constructed its worldview.
“So I can trace through the graph and see why it arrived with that answer,” Rathle said.
Graph databases are also widely used in the health care companies for drug discovery and by aircraft and other manufacturers as a way to visualize complex system design, Rathle said. “You have all these cascading dependencies and that calculation works really well in the graph,” Rathle said.
## What’s in GQL?
The GQL standard is over 600 pages long and references more than 400 papers.
Components include:
- Graph-only data types (Vertex, Edge, Path)
- Scalar data types
- Operations, functions, and predicates for the scalar types
- a transaction model
- A security model
- Graph Pattern Matching
- Graph Types, to constrain the contents of a graph
[GQL](https://www.gqlstandards.org/home) is based on [Cypher](https://neo4j.com/product/cypher-graph-query-language) — and its open source variant [OpenCypher](https://opencypher.org/) — the query language for one of the most popular graph database systems, [Neo4j](https://neo4j.com/).
The Core Syntax for GQL is largely identical to Cypher, with the MATCH … RETURN statements working the same. The query:
|
1
2
|
MATCH (movie:Movie)
RETURN movie.title
will
[return all the nodes](https://neo4j.com/docs/cypher-manual/current/clauses/match/) with the “Movie” label in the database.
|
1
2
3
4
5
6
7
|
Table 2. Result
movie.title
"Wall Street"
"The American President"
Rows: 2
GQL also uses the same basic expressions, linear composition, and other aspects of Cypher.
The best part of GQL, naturally, is the ability to traverse a graph. For instance, this example query from Neo4J shows the next stop for a transport service that stops at Denmark Hill at 22:37:
|
1
2
3
4
|
MATCH (n:Station {name: 'Denmark Hill'})<-[:CALLS_AT]-
(s:Stop WHERE s.departs = time('22:37'))-[:NEXT]->
(:Stop)-[:CALLS_AT]->(d:Station)
RETURN d.name AS nextCallingPoint
With the result of…
|
1
2
3
|
Table 4. Result
nextCallingPoint
"Clapham High Street"
There are some
[basic differences](https://neo4j.com/blog/cypher-path-gql/) between Cypher and GQL, however.
GQL will use the keyword INSERT to add a node or relationship to a graph, whereas Cypher uses CREATE. The FOR statement takes the place of Cypher’s UNWIND.
Other
[graph query languages](https://www.nebula-graph.io/posts/graph-query-languages-you-should-know) include [NebulaGraph](https://www.nebula-graph.io/)‘s NQL, [Apache Tinkerpop’s Gremlin](https://thenewstack.io/tinkerpop-growing-graph-database-popularity/), [SPARQL for RDF](https://www.w3.org/TR/rdf11-concepts/), and [ArangoDB](https://arangodb.com/)‘s AQL. There’s also the [GraphQL language](https://thenewstack.io/graphql-growth-explodes-but-so-do-problems-federated-graphs-solve/), a graph-oriented query language for building APIs.
The upgrade path from existing graph query languages should be fairly easy, at least if those implementations were based on Cypher. According to Rathlee, at least a dozen different graph database systems are built on OpenCypher, including the popular
[Neptune](https://aws.amazon.com/neptune) from [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)