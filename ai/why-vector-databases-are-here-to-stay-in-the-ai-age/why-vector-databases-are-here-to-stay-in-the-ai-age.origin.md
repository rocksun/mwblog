# Why Vector Databases Are Here to Stay in the AI Age
![Featued image for: Why Vector Databases Are Here to Stay in the AI Age](https://cdn.thenewstack.io/media/2025/01/e9ed1c3b-why-vector-databases-are-here-stay-ai-age-1024x576.jpg)
Vector databases, an important component within AI-driven architectures, have gained a lot of popularity with the advent of mainstream AI and large language models (LLMs).

In the most basic terms, [vector databases](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/) are databases that allow the storage and retrieval of vectors. Vectors are the key component of LLMs that abstract and reason about the data the model has been trained on.

Vector databases, however, being *databases*, can do more than just store and retrieve vectors. They also provide built-in approximate nearest neighbor (ANN) algorithms, which enable vector similarity search capabilities directly within the database.

## Types of Vector Databases
There are two general approaches to managing new types of data with databases: single-purpose and multimodel. Vectors are no different.

Single-purpose databases have produced many vector databases that focus entirely on vector storage, search and retrieval; however, they can’t manage any other types of data. They are built for one single purpose, hence the name *single-purpose database*. Examples of this include Chroma, [Pinecone](https://www.pinecone.io/?utm_content=inline+mention) and Weaviate.

The multimodel database approach adds vector storage, search and retrieval capabilities to an existing database technology. This allows management of vectors alongside [other types of data](https://thenewstack.io/what-data-type-should-you-use-for-storing-monetary-values_2/) within the same database. Examples of this include [PostgreSQL](https://roadmap.sh/postgresql-dba), [MySQL](https://thenewstack.io/a-cheat-sheet-to-database-access-control-mysql/) and [Oracle Database](https://www.oracle.com/database/).

## Benefits of Using a Vector Database
Regardless of which approach you use, storing vectors in databases means that vectors don’t need to be created repeatedly and on the fly when applying LLMs to existing data. Moreover, storing vectors in databases, rather than in files on filesystems, enables the smart management of them. For example, vectors can be indexed, compressed and partitioned in databases.

Besides vector similarity search, vector databases can be used for a multitude of other scenarios, such as recommendation engines, object detection and semantic search. Some vector databases also allow you to import and store pretrained LLMs and generate vectors of incoming data via these LLMs directly within the database. This often alleviates the need for an LLM mid-tier.

Vector databases are also often an essential component in an AI-driven architecture to implement [retrieval-augmented generation (RAG)](https://thenewstack.io/using-sql-powered-rag-to-better-analyze-database-data-with-genai/), which fine-tunes LLM responses by providing domain-specific knowledge.

## AI Advantages of Multimodel Databases
The multimodel approach, however, enables other important scenarios that can kickstart a company’s AI journey. Because the multimodel approach adds vector capabilities to an existing technology, the only thing you usually need to do is upgrade the existing system to a version that supports the new vector capability. This advantage should not be underestimated, as it means you don’t have to learn new technology skills from the ground up, put a new system in place or define any data pipelines from existing sources to the new system.

Furthermore, multimodel databases enable vector similarity search in combination with traditional analytics, and often via SQL. This means a vector similarity search can be part of a larger [SQL query](https://thenewstack.io/how-to-write-sql-queries) and include all existing data.

The example below shows retrieval of the top-10 best matches for houses for sale that fall within the budget and preferred location(s) of an interested buyer. It combines a vector similarity search to retrieve houses that look like one in a picture the users provided:

123456 |
SELECT picture, price, location FROM houses_for_sale WHERE price <= (SELECT budget FROM buyers WHERE buyer_id = :app_user_id) AND location IN (SELECT preferred_location FROM buyer_locations WHERE buyer_id = :app_user_id) ORDER BY VECTOR_DISTANCE (picture_vector, VECTOR_EMBEDDING(houses_llm USING :app_input_picture) FETCH FIRST 10 ROWS ONLY; |
The first part of the query is a regular relational SQL query. It selects the picture, price and location of all houses from the `houses_for_sale`
table where the selling price is less or equal to the buyer’s budget and the location matches one of the buyer’s preferred locations.
It then orders the results based on the similarity of the user-provided picture with pictures of houses in the `houses_for_sale`
table. This is where the vector similarity search comes in. Instead of comparing pictures directly, the `ORDER BY`
section does the following:

- Generates a vector of the user-provided house picture via the
`VECTOR_EMBEDDING()`
function using an imported LLM called`houses_llm`
. - Takes the generated vector and calculates the similarity, or distance, with stored vectors of pictures of houses for sale via the
`VECTOR_DISTANCE()`
function. - Then sorts the results based on the similarity of these vectors, returning the most similar ones first.
- Finally, it returns only the top 10 matches with the most similar vectors, for instance, houses that look the most similar to the picture the user provided.
Using the multimodel database approach also means that users familiar with SQL can perform vector similarity searches without deep knowledge of LLMs and vector generation. Oracle Database takes the multimodel approach one step further, following a converged database approach that not only provides multimodel capabilities but also enables users to apply the same security policies, compression, information life cycle management (ILM), performance acceleration and other features available in their database to vectors.

## Vector Databases Are Here to Stay
Because vector databases make storing, managing and retrieving vectors so easy and, in the case of multi-model vector databases, allow combining vector similarity search with existing data and analytics, they have become a popular component of AI-driven architectures. Vector databases not only accelerate but also help simplify a company’s journey to leveraging AI.

*Begin innovating with features such as **AI Vector Search** and **JSON Relational Duality** either locally with **Oracle Database 23ai Free** or in the cloud on OCI with **Oracle Autonomous Database** today.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)