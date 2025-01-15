# Vector Processing: Understand This New Revolution in Search
![Featued image for: Vector Processing: Understand This New Revolution in Search](https://cdn.thenewstack.io/media/2025/01/d364ee52-ato-nyah_macklin-1024x768.jpg)
“Vectorize EVERYTHING!”

These were the words of wisdom from [Nyah Macklin](https://github.com/MacklinEngineering), [Neo4j](https://neo4j.com/company/) senior developer advocate, in [a presentation](https://2024.allthingsopen.org/sessions/understanding-vector-databases) on [vector databases](https://thenewstack.io/integrating-vector-databases-with-existing-it-infrastructure/) at [All Things Open 2024](https://thenewstack.io/all-things-open-whats-your-future-as-a-developer/).

Vectorized data is going to be very important going forward, especially in the realms of machine learning and artificial intelligence.

Vector processing, once a niche concept, is now at the forefront of powering innovative applications like semantic search, recommendation systems and advanced chatbots.

“Vector search is a new way of information retrieval, which is up and coming,” agreed [Vadim Tkachenko](https://www.linkedin.com/in/vadimtk/), Percona co-founder and technology fellow, in [his ATO 2024 session](https://x.com/Joab_Jackson/status/1850920276243984831) on [vector searches in databases](https://www.youtube.com/watch?v=KGGml9pEORM).

## Vector: Beyond Keywords
At the heart of vector processing lies the concept of semantic search. Unlike traditional lexical searches that rely on matching keywords, semantic search delves into the meaning and context of words, aiming to understand the user’s intent.

It “allows us to understand the meanings behind words, not just the words themselves,” Macklin said.

It’s about deciphering the nuances of language, recognizing that the same word can have different meanings depending on the surrounding context. For instance, “Apple” in “Apple laptop” is distinct from “apple” in “apple pie.”

Semantic search leverages embeddings, numerical representations of words, phrases, or even entire documents to capture their semantic meaning. By converting textual (and other) information into numerical vectors, semantic search enables computers to understand and compare the meanings of different pieces of content.

Semantic search is all about finding and scoring related data, using context and intent. – Nyah Macklin

Semantic search also gains more context from what is known about the user. Search history or the location of a user can provide more clues about their intent — “Football” means something completely different in the U.S. and Britain, for example.

Semantic search results are scored against the intent of the search so they can be compared. Similarity scores are usually ranked between zero and one, with one representing the greatest similarity.

![Photo of Vadim Tkachenko.](https://cdn.thenewstack.io/media/2025/01/03ae54cf-ato-vadim_tkachenko-300x225.jpg)
Vadim Tkachenko at ATO 2024.

This numerical representation of a word or phrase is called an embedding. A ‘river bank’ has a different embedding than a ‘savings bank.’

Vector processing extends beyond text and semantic search. It can be applied to various data types, including images, audio and video. For instance, in image recognition, images can be converted into vectors, allowing for similarity searches to find images with similar content or features.

## Vectors: The Building Blocks of Semantic Search
A vector is essentially a list of numbers representing a magnitude and a direction. The number of elements in this list defines its dimensionality. In machine learning, vectors with hundreds or even thousands of dimensions are commonly used to represent complex concepts and relationships.

The breakthrough in using vectors for semantic search came in a 2013 paper, “[Efficient Estimation of Word Representations in Vector Space.](https://arxiv.org/abs/1301.3781)” The paper was authored by Google boffins Tomas Mikolov, Kai Chen, Greg Corrado and Jeffrey Dean, and provided a method to turn sentences into vectors.

The researchers found that vectors could be used to find similarities in very large data sets much more efficiently than the heretofore-used method of training a neural network to do the work.

“We observe large improvements in accuracy at much lower computational cost, i.e. it takes less than a day to learn high quality word vectors from a 1.6 billion words data set,” the researchers wrote. “Furthermore, we show that these vectors provide state-of-the-art performance on our test set for measuring syntactic and semantic word similarities.”

This paper introduced a new model, called Word2Vec, to efficiently convert words and phrases into dense vectors, in a way that captured their semantic relationships. Words with similar meanings have vectors that are closer together in the vector space, while dissimilar words have vectors that are farther apart.

![Vector embeddings graph.](https://cdn.thenewstack.io/media/2025/01/6a2d8b9b-ato24-vectory-tkachenko-percoa-vector_embeddings-02.png)
Wikipedia graphic illustrating vector embedding, via the presentation of Vadim Tkachenko.


In the years since the paper was posted, the industry has built an entire industry, [generative AI](https://thenewstack.io/generative-ai-is-just-the-beginning-heres-why-autonomous-ai-is-next/), around the technology.

“Vector search is just an easy way to find related objects that have similar characteristics,” explained [Olena Kutsenko](https://www.linkedin.com/in/olenakutsenko/?originalSubdomain=de), senior developer advocate for data platform provider [Aiven](https://aiven.io/about), in her [ATO 2024 presentation](https://2024.allthingsopen.org/sessions/vector-search-in-modern-databases).

“And in vector search, we rely on a machine loading model to help us to detect those characteristics of different things, whether they’re text, images, audio or something else.”

In the multidimensional space created by the model, images that are similar tend to have have close vectors, while those that are not have very different vectors. Each entity has a set of coordinates, and those coordinates can be compared across different entities.

## Vector Match: Searching in a Multidimensional Space
To effectively utilize embeddings for semantic search, specialized databases known as vector databases have emerged, such those offered by [Pinecone](https://www.pinecone.io/?utm_content=inline+mention) and the open source [Milvus](https://milvus.io/).

Vector support is also rapidly being added to traditional databases as well. [PostgreSQL](https://thenewstack.io/postgresql-17-gets-incremental-backup-sql-queries-for-json/) users, for instance can install [PGVector](https://github.com/pgvector/pgvector) for full vector support, including vector search. A 512-vector dimension simply gets stored as a 512-number array.

![database code.](https://cdn.thenewstack.io/media/2025/01/54d29573-ato24-vectory-tkachenko-percoa-vector_db-01.png)
Creating a vector table in PostGreSQL and then running a vector search against it (From the presentation of Vadim Tkachenko).

Kutsenko offered an example of how to use vectors to find movie recommendations.

With both types of databases, a user query (“A movie with cute puppies”) is turned into a vector, so it can then be compared to its “nearest neighbors” of other movies in the database. The vector database then performs a similarity search to find the movies whose vectors are closest to the query vector, effectively recommending movies that match the user’s preferences.

## Vector Databases: So Many Vectors
The databases employ algorithms like [k-nearest neighbors](https://www.ibm.com/think/topics/knn) (KNN) and [approximate nearest neighbor](https://www.mongodb.com/resources/basics/ann-search) (ANN) to quickly identify vectors that are closest to a given query vector.

KNN is a straightforward algorithm that compares the query vector to every other vector in the database, identifying the k-nearest neighbors based on a distance metric. While effective for smaller data sets, KNN becomes computationally expensive for large data sets.

ANN addresses this challenge by using indexing techniques to pre-process the data and speed up searches. These techniques, such as IVFFlat and HNSW, create clusters or graphs of related vectors, allowing the search algorithm to focus on specific regions of the vector space, thereby reducing the number of comparisons needed.

The first option, **IVFFlat** (inverted file with flat compression), builds clusters around groups of data so the user can specify the chunk of data closets to the query to inspect. This is an index to build only after you’ve entered much of your data.

![ivfflat-query](https://cdn.thenewstack.io/media/2025/01/bf58ee98-ato-kutsenko-vector-01-1024x587.png)
Kutsenko uses the IVFFlat technique to highlight relevant movies.

The second option, **HNSW** (Hierarchical Navigable Small Worlds), creates a graph with multiple layers, with least-likely material on the outer layers. This is more expensive to build, but it operates faster, Kutsenko noted. This is also the index to use if you are changing out a lot of your data.

![HNSW graph and code.](https://cdn.thenewstack.io/media/2025/01/91c5c91e-ato-kutsenko-vector-hnsw-02-1024x573.png)
Kutsenko uses the HNSW to highlight relevant movies.

## Vector Processing: A Search for Tomorrow
While vector processing offers significant advantages, there are challenges to consider. The accuracy of the results depends heavily on the quality of the embeddings and the chosen similarity metric. Additionally, balancing performance and precision is crucial, especially with large data sets. Choosing the right indexing technique and optimizing the search parameters can significantly impact the efficiency and accuracy of vector searches.

But as the presenters at ATO 2024 have shown, vector processing is revolutionizing how we interact with information, enabling machines to understand and process data in a more humanlike manner.

Kutsenko’s full presentation an be enjoyed here:

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)