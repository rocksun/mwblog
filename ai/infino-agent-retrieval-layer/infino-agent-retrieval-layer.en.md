**Software vendors like to claim unified systems** that act as a so-called single pane of glass for any given coding task, data function, or broader workflow. Agentic data retrieval company Infino hints at that vibe, promising a single retrieval layer for all agents.

In this context, a single retrieval layer means a unified (there’s that word) database system that lets all AI agents query all data from one place.

## Agents have changed the data query paradigm

Formally launching its agent retrieval platform on Wednesday, [Infino](https://infino.ai/) says it built the platform because agents have changed the data query paradigm and don’t query like humans.

Infino CEO [Ekechi Nwokah](https://www.linkedin.com/in/ekechi/) tells *The New Stack* that agents are the “largest new consumer of data since the web browser”, but he laments that they are still “being served with a fragmented stack built for a different era,” i.e., [data warehouses](https://thenewstack.io/data-warehouses-and-customer-data-platforms-better-together/) for SQL, search engines for keywords, [vector databases](https://thenewstack.io/how-to-master-vector-databases/) for [semantic search](https://thenewstack.io/superlinked-democratizes-real-time-semantic-search/), and [ETL](https://thenewstack.io/from-etl-to-autonomy-data-engineering-in-2026/) pipelines to keep them all in sync.

“We’re collapsing that stack for agents,” Nwokah says. “Our approach is to put the data in Parquet in object storage and let agents search, rank, filter, join, aggregate, and reason over it directly. The result is one copy of the data that all agents read.”

As we know from database basics lesson #1, data stores have been traditionally optimized for a human or application that writes one query, waits, and reads the result.

“An agent behaves quite differently,” Nwokah says. “It issues many small questions to answer one large one, often at the same time, and every result it receives consumes context and can add cost and latency to subsequent model calls. That is a new kind of reader that existing data stores were not optimized for.”

> “An agent behaves quite differently. It issues many small questions to answer one large one, often at the same time, and every result it receives consumes context, and can add cost and latency to subsequent model calls.”

Nwokah explains that [Grep](https://thenewstack.io/the-grep-command-in-linux/) (the command-line tool that searches plain text for line matches on a specific keyword or pattern) returns matches, and the agent goes on to read whole files. Further, he notes that a vector database will return a handful of chunks, and then the agent asks again with additional queries. Additionally, a data warehouse returns rows, and the agent combines them itself.

“Infino is a retrieval layer designed for this data reader dynamic. It gives the agent one interface directly over object storage that combines structured and unstructured queries: ranked searches, exact counts, joins, filters and aggregates at low cost and large scale,” Nwokah clarifies.

During the good old years of data search, query patterns were comparatively predictable. When humans or applications queried, search ran on a search database. Analytics ran in a warehouse. Vector databases enabled approximate queries and unlocked a new class of use cases, but they didn’t fundamentally change those query patterns. Each query ran on its own system, with its own copy of the data, its own ingestion pipeline, and its own team to run it.

Today, those operations can still span a database plus a search engine, a vector database, and a data warehouse. The agent has to call each one and then spend additional model turns combining the results. Infino’s answer is to embed retrieval functions directly in SQL, so the whole question can be expressed in one query.

## Fewer data tasks, less glue code, centralized policy management

“For developers and data teams, it removes entire pipelines and the time it takes to manage them,” Nwokah enthuses. “That means fewer systems, fewer ingest paths, fewer ETL jobs, fewer schemas to keep aligned, fewer clients in the agent’s tool list, and less glue code to combine their results. It also means one place to govern agents.”

He underlines his organization’s method here and says that when an agent’s data lives in a single copy, developers “can enforce hard policies centrally”, so that means governance over who can read what, which rows and columns an agent can see, and what gets logged.

“Compare that with managing agent permissions across MCP gateways and SaaS tools,” urges Nwokah.

> “For developers and data teams, it removes entire pipelines and the time it takes to manage them.”

A developer can enter a single natural-language English question, and it becomes one query that completes in milliseconds, according to Infino. Infino has clarified that the important part isn’t SQL itself; it’s that keyword search, semantic search, filtering, aggregation, and grouping can happen together instead of forcing the agent to orchestrate several systems and reason over a pile of intermediate results.

As an additional challenge uncovered during the platform’s development, Infino noted that even when retrieval is fast, it found that agents spend a lot of time in retrieval loops, i.e., working to formulate a query, search, decide whether the results are good enough, try something else, validate the answer, and repeat. Infino says it integrates targeted inference models with the retrieval engine so these simpler tasks run faster and more cheaply than with frontier models.

## The data storage challenge: Apache Parquet

The other challenge Infino tackled is how it stores the data. Instead of maintaining separate copies for search, vectors, and analytics, Infino keeps a single copy in [Apache Parquet](https://thenewstack.io/an-introduction-to-apache-parquet/) (a column-oriented storage format) on object storage.

“The core engine is open source, Apache-2.0, on GitHub, and we store all data as valid Parquet files with the search indexes embedded beside the Parquet footer, so any tool that reads Parquet can read the data with or without Infino. Infino Cloud, our hosted service, has some additional proprietary features, like being able to point at your existing Parquet data and make it searchable without building any infrastructure yourself,” adds Nwokah.

Infino stores indexes inside the Parquet files to speed retrieval, while the underlying data remains Parquet. Iceberg and Hudi can manage the same table, and Spark, DuckDB, warehouses, and other Parquet readers can still read it. One copy of the data can therefore serve the different ways an agent needs to query it.

Infino also wanted the path from data to query to be simpler than with traditional data stores. Setting up clusters, nodes, shards, and headcount is a lot of complexity just to query data, the company argues. With Infino, developers can point at Parquet or JSON, ingest the data, then point their agent at Infino and start querying.

## Who benefits from this technology?

Nwokah lists four major software engineering practitioner groups who he promises can benefit from the approach outlined here:

* Platform or data engineers looking to get their arms around the proliferation of agents, with a far simpler and far less expensive stack to manage. There is no data lock-in (claims Nwokah), as their data stays in their bucket and is readable by any Parquet reader. Agents can combine both structured and unstructured data through one interface.
* Security engineers looking to put a proper governance layer around their agents. With a single copy of data, the auth policies an agent runs under are enforced centrally and deterministically rather than across a set of MCP gateways and SaaS connectors.
* ML and data science teams doing feature exploration. Infino searches, filters, joins and aggregates over both structured and unstructured data, cutting the time between messy data and clean features.
* Software developers building agent workflows across code, logs, CI output, issues and other engineering data. Instead of giving the agent a different retrieval system for each corpus, they can give it one query interface across all of them.

With its current architecture, Nwokah claims that Infino is designed to be roughly 10× cheaper than traditional search or analytics infrastructures. Infino’s own published comparison puts it at about 10.5× cheaper than Elasticsearch and 23× cheaper than OpenSearch for the workload it tested.

## Multi-billion-document use cases

Nwokah confirms that the company is already supporting multi-billion-document use cases in people search, document processing, product analytics, and security.

“We are particularly optimized for teams with agent use cases that are already on Parquet or considering migrating to Parquet, or alternatively who are looking to replace their search tool with something easier to manage and more scalable,” he concludes.

One of the organization’s customers, which Infino did not name, is putting petabytes of data from across their entire company on Infino, according to the company. The Parquet sits in their bucket and is still read by existing tools across different teams. Meanwhile, the product and engineering teams get the scalable agent infrastructure they need to launch AI-native solutions for their customers. Developers can then control their agents from a single interface.

Infino CEO [Nwokah](https://www.linkedin.com/in/ekechi/) formed the company alongside co-founder and head of engineering [Vinay Kakade](https://www.linkedin.com/in/vinaykakade/), co-founder [Asif Makhani](https://www.linkedin.com/in/asifmakhani/), and chief architect [Murali Krishna](https://www.linkedin.com/in/muralikpbhat/).

The group spent years building and operating ML and search systems across Amazon, Google, and LinkedIn, including AWS OpenSearch. The changing nature of agentic data querying is their rationale for building Infino: to enable any agent to query data at scale, in one query, over one copy of the data.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)