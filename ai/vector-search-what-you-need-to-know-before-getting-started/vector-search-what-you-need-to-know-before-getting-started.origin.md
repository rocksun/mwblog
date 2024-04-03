# Vector Search: What You Need to Know Before Getting Started
![Featued image for: Vector Search: What You Need to Know Before Getting Started](https://cdn.thenewstack.io/media/2024/03/46b69bf3-untangle-vector-search-1024x576.jpg)
Planning on adopting a vector database for your project? As you may have discovered, this is a worthy but not easy feat.
First, you need to navigate a vast landscape of market options to select the solution that best fits your business requirements. This, on its own, is an arduous task, but it’s just the beginning.
Developers must consider a variety of technical and other considerations to properly implement a vector database. Among these, choosing the right vector search algorithm can be challenging. These
[algorithms](https://roadmap.sh/datastructures-and-algorithms) require a deep understanding of mathematical concepts to establish the proper trade-off between accuracy and speed of vector retrieval.
This article demystifies the foundational concepts of vector search and the implementation details required to set up your vector database successfully.
## What Is a Vector Database?
A
[vector database](https://thenewstack.io/how-large-language-models-fuel-the-rise-of-vector-databases/) is a state-of-the-art solution for efficient [storage](https://thenewstack.io/storage/), swift retrieval and seamless processing of high-dimensional (HD) numerical data representations at scale.
These HD vectors, also known as embeddings, are the efficient and effective data structure behind information retrieval (e.g., powering rapid search engines), as well as for
[AI applications](https://aerospike.com/blog/business/5-questions-on-real-time-ai/?utm_source=prnewswire&utm_medium=press&utm_campaign=2024Q1PR&utm_content=artificial-intelligence-AI-applications) (e.g., real-time recommendation systems or document summarization).
Information of all types — from text and statistics to images and music — can be embedded into vectors. From this, vector databases can seamlessly enable multimodal use cases.
## How Do Vector Databases Work?
While
[machine learning (ML)](https://thenewstack.io/ai/) models provide inference capabilities, vector databases provide a solution for storing and searching across a large number of vectors, known as a vector space. With high-dimensionality vectors, the number of possibilities becomes incomprehensibly large.
To accomplish search performance, a vector database does the following:
- Writes vectors to the storage layer (ideally with high-performance characteristics).
- Calculates the distance between new vectors and some sampling of vectors already in the vector space.
- Uses these distances to build an index to optimize search performance.
- Finally, when a search request is made, executes an algorithm for the nearest neighbor results.
To ensure reliable and effective operations around vector indexing, vector databases incorporate features from
[classical databases](https://aerospike.com/products/database/?utm_source=prnewswire&utm_medium=press&utm_campaign=2024Q1PR&utm_content=classical-databases). These include: **Enhancing search efficiency**through techniques such as preprocessing (e.g., data normalization, dimensionality reduction), post-processing (e.g., reranking), caching, query rewriting, concurrency control and transaction management. **Scaling up solutions**through data partitioning, replication, pruning and other optimizations. **Monitoring and maintaining the database**with activities such as system analysis, index optimization, data backup and [security](https://thenewstack.io/artificial-intelligence-stopping-the-big-unknown-in-application-data-security/)through encryption and authentication. **Facilitating integrations**to seamlessly surface information to external systems.
## What Is Vector Similarity Search?
A vector similarity search entails looking for the vectors within a database most similar to a specific query vector based on a defined similarity metric or distance measure.
You need to choose your vector similarity search approach when setting up your vector solution.
### How Does Vector Similarity Search Work?
A vector summarizes the most meaningful information of source data into a compact, high-dimensional numerical value. The more dimensions, the more complex the data that can be meaningfully embedded.
The mapping from source data to the meaningful vector representation is achieved using an embedding model trained with AI to create a vector space in which similar concepts are mapped closely to one another. More generally, the vector space is such that the relative distance between vectors represents the conceptual distance between them.
The following image shows a simplified two-dimensional (2D) example to visualize the concept, where one dimension represents gender and the other represents age.
![Representation of concepts embedded in a 2D vector space.](https://cdn.thenewstack.io/media/2024/03/55a955e1-2d-vector-space.png)
Representation of concepts embedded in a 2D vector space.
In this vector space, “grandfather” is closer to “man” than “boy” is, “man” and “woman” are equidistant to “child,” and “man” is far from “woman” but symmetrical in the relationship to age.
Say now you want to query for “infant” and retrieve the most relevant concept associated with it, you need to calculate the trigonometric distance — most commonly one of Euclidean distance, cosine similarity and dot product — between “infant” and other vectors in the space, and then retrieve the N closest vectors.
A simple, albeit inefficient, solution is to calculate the distance between all vectors. In practice, using an index is best practice. An index is a data structure, such as a tree or a graph, that inherently encodes spatial information, allowing retrieval to converge faster to the right location of the vector space. At query time, your search is embedded into a vector, and the most similar indexed vectors in your databases are retrieved for you, with some optional post-processing available, such as candidate refinement or reranking.
### Why Is There a Trade-off Between Accuracy and Speed?
In the 2D example above, calculating the distance between vectors is simple: You can retrieve the most accurate results with close-to-zero latency. However, when moving to HD vector representations, calculating similarity scores becomes complex.
The curse of dimensionality — increased computational and memory requirements — and loss of intuitive geometry and visualization all appear in high-dimensional spaces.
This means that, while it is possible to perform an
*exact search* that precisely returns the most similar vectors to the query, these methods not only are costly but also have longer processing times (potentially hours!) that make it typically unfeasible to run in typical production systems.
An exact search is possible for small data sets and useful for a performance comparison with the approximate nearest neighbor (ANN) implementations. But, in practice, an
*approximate search* is performed.
Different approximate algorithms exist, each providing a unique performance trade-off between accuracy and speed. Understanding and choosing the right vector search algorithm implementation is thus fundamental to optimizing the vector database solution for each use case.
## What Are Popular Vector Search Algorithms?
The most popular — and almost only — algorithms behind vector search are nearest neighbor algorithms. This is why vector search is often referred to as nearest neighbor search, and the name of a vector index is based on the nearest neighbor algorithm it supports, the Hierarchical Navigable Small World (HNSW) index.
Nearest neighbor algorithms find data points that are closest to a given query point based on the chosen distance metric by organizing the data set into a tree, a hash or a graph, which are all spatially aware data structures. Techniques like quantization and clustering can also be introduced to enhance optimization by compacting vector representations, thus improving search efficiency.
The two categories of nearest neighbor algorithms are k-nearest neighbors (KNN) for exact searches and ANN for approximate searches.
### KNN and ANN Algorithms
For an exact search, KNN returns the closest k vectors to the query vector by comparing all vectors in the database. The complexity is O(n): When querying with a Word2vec vector of dimension 300 on a database of 100 million vectors, you need 30 billion operations to retrieve your (exact!) most similar k vectors.
With a complexity of O(log(n)), ANN algorithms are most commonly used for real-world applications. ANNs can be tree-based, graph-based or hash-based.
Nearest neighbor algorithms include:
**Approximate Nearest Neighbors Oh Yeah (ANNOY) and Fast Library for Approximate Nearest Neighbor (FLANN):**Common implementations of tree-based ANNs; best when you need to be as fast as possible, for example, an interactive real-time image similarity search for a photo-sharing platform. **Hierarchical Navigable Small World (HNSW) and Navigable Small World (NSW):**Common implementations of graph-based ANNs; best for applications that need to be as accurate as possible at scale, such as a recommendation system for a large worldwide e-commerce platform. **Locality-Sensitive Hashing (LSH) and Semantic Hashing (SH):**Common implementations of hashing-based ANNs; best for cost-effectiveness in scenarios where precision is less critical than resource efficiency, for example, a content deduplication solution for an in-house document management system.
## Why Does Choosing the Right Vector Search Algorithm Matter?
Choosing the right vector search algorithm is crucial for optimizing search performance and overall efficiency of the system, ultimately contributing to improved user experience and better outcomes for the application.
First, your algorithm selection should align with your data requirements, and then be tailored to provide optimal performance requirements. Beyond accuracy and latency, other metrics to consider when defining the performance trade-offs include throughput, cost and scalability.
Selecting a vector database involves navigating through a multitude of solutions and
[considerations](https://aerospike.com/blog/building-ai-apps-with-vectors/?utm_source=prnewswire&utm_medium=press&utm_campaign=2024Q1PR&utm_content=considerations), especially when looking for the right vector search algorithm.
The basic idea behind vector search is simple: High-dimensional data representations can be embedded in a vector space where distance reflects conceptual similarity. When structuring your vectors within a tree, graph or hashes, you can efficiently navigate the vector space at query time to strike a unique balance between accuracy and speed, aligning with data requirements and scalability needs.
Opting for a vector database solution that allows you to flexibly customize implementation details, like a vector search algorithm, can be a game changer for a successful application.
*Vector search solutions depend on real-time databases with the unlimited scalability and fast ingestion to process massive amounts of data. Learn more about how you can build the * *highest-performing, most precise and cost-effective AI applications* * with Aerospike.* [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)