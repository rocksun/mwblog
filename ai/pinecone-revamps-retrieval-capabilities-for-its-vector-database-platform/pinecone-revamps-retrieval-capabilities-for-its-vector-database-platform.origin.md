# Pinecone Revamps Retrieval Capabilities for Its Vector Database Platform
![Featued image for: Pinecone Revamps Retrieval Capabilities for Its Vector Database Platform](https://cdn.thenewstack.io/media/2024/12/247ba1a3-aws-reinvent-1024x576.png)
Today at AWS re:Invent, Pinecone unveiled significant advancements to its [AI retrieval platform](https://thenewstack.io/vector-databases-are-having-a-moment-a-chat-with-pinecone/). As part of what the vendor has termed its “cascading search” method, the company’s vector database search system now includes re-ranking models for search results, a proprietary sparse vector embedding model for lexical search, and a new sparse vector index.

The vendor also revealed a number of security upgrades, including [Role-Based Access Controls](https://thenewstack.io/7-expert-strategies-for-managing-rbac-on-openshift/) (RBAC), customer-managed encryption keys, audit logs, and the general availability of Private Endpoints for AWS PrivateLink. With PrivateEndpoints for AWS PrivateLink, users can connect to the vector database without transmissions from their Virtual Private Clouds traversing the public internet.

By amalgamating its re-ranking capabilities with a methodology for implementing dense and sparse vector search in parallel, Pinecone aims to improve search results beyond those of conventional hybrid search. Typically, hybrid search in vector database settings combines the results of sparse vector search (a term for lexical or keyword-based search) with those for dense vector search (which involves retrieval of vector embeddings).

Pinecone’s cascading search technique adds re-rankers to this combination and synthesizes the results in a manner distinct from that of doing so with conventional hybrid search while still demonstrating the continuing relevance of keyword search.

“Pinecone’s always thought of vector database capabilities as something beyond semantic search, and it’s not surprising that many companies are looking for a wider set of tools to accomplish retrieval,” commented [Gareth Jones](https://www.linkedin.com/in/gareth--jones), [Pinecone](https://www.pinecone.io/) staff product manager. “You don’t just need dense vector and semantic search. You need keyword search and re-rankers to merge the keyword results together.”

## Cascading Search
The newly available re-ranking models include [Cohere Rerank](https://cohere.com/rerank) 3.5 and Pinecone’s proprietary model, pinecone-rerank-v0. Re-ranking models are typically neural networks that evaluate responses (such as documents) of a query with the actual query. They enable organizations “to run a more powerful comparison that says this document is specific to this query and produce a score for every query-document pair,” Jones explained.

Although hybrid search can involve re-ranking models, the difference between this paradigm and that Jones characterized as cascading search is the way results of dense and sparse vector search are combined.

Pinecone aims to improve search results beyond those of conventional hybrid search.

According to Jones, the hybrid search usually couples scores of search results from dense vector search with those from sparse vector search “and uses some technique to combine them that’s usually heuristic-based, like Reciprocal Rank Fusion.” With cascading search, there may be 100 results from a dense vector index and 100 from a sparse vector index, with both retrievals done in parallel.

“But, those aren’t weighted against each other, so you use the re-ranker,” Jones added. “Typically, this only produces 10 to 20 results on the other side of the re-ranker and those go to the LLM to be summarized. So, we think of this as a cascade of going from recall focus, tons of results at the top, to basically going to the minimal amount of context you can provide to the LLM.”

## A Single API Call
Although it’s far from uncommon for vector search engines to incorporate re-ranking models (as well as other techniques for re-ranking search results), Pinecone’s packaging of them is noteworthy for the user experience it provides. In its cloud-native, serverless computing offering, users can not only access re-ranking models, but also Pinecone’s proprietary sparse embedding model — [pinecone-sparse-english-v0](https://docs.pinecone.io/models/pinecone-sparse-english-v0) — and a new sparse vector index.

“We’re hosting and optimizing the models for inference,” Jones said. “For example, in this new release with Cohere, it’s not like you bring your Cohere API key and Pinecone calls out to Cohere to run the re-ranker or the embedding model. These models are entirely hosted on Pinecone’s infrastructure. We manage them end-to-end and handle billing and everything for the customer.”

This simplified user experience is designed to democratize the use of LLMs, in addition to considerable facets of the architecture and infrastructure required to do so. The newly available sparse vector index type (which, according to Jones, isn’t a hybrid index and outperforms BM25 in many use cases), along with Pinecone’s proprietary sparse embedding model, emphasizes the ongoing relevance of lexical search in the era of language models.

These capabilities are influential in Pinecone’s ability to provide a UX in which customers can send the vendor text, and it will “handle the embedding and re-ranking on a single API call,” Jones said.

## Re-Ranking Model Benefits
Using re-ranking techniques to refine search results and make them more pertinent to an organization’s specific data, query, and use case is a best practice for both sparse and dense vector search. They’re particularly valuable for dense vector search when organizations don’t [fine-tune or train the embedding model](https://thenewstack.io/the-secret-sauce-for-vector-search-training-embedding-models/). “When you embed a document, you don’t know the query,” Jones said. “The documents get embedded without knowing the queries, so they’re not tuned to that specific question.” Re-ranking models assuage this situation by comparing the query to the document or the embedded content. They also yield additional advantages such as:

**Improved Context:**Re-ranking models produce a positive effect on the context language models receive for queries. “What research has shown about them is it improves the quality of the context window,” Jones mentioned. “You either use the score to remove or cut off documents that aren’t relevant, even though the recall step, the embedding model… may be relevant.”**Cost Reduction:**Some models specialize in reducing the number of tokens — without compromising what the content means — sent to language models for RAG and other applications. Re-ranking models can also reduce the number of tokens sent to language models, which can lower cost. “If you’re passing less context as input, the number of tokens goes down,” Jones said.**Lost in the Middle Mitigation:**The Lost in the Middle problem is the phenomenon in which language models, including newer ones devised to accommodate longer prompts and greater quantities of context, produce poorer responses when relevant information isn’t at the beginning of the content they parse. “Even if you’re giving the LLM the right answer, you want that chunk, that piece of text that contains the answer, to be as far up in the context window as possible,” Jones said. “If it’s more in the middle it’s less likely to be attended by the LLM.”
## A Step Forward
Pinecone’s advancements in incorporating re-ranking models and developing its own models for re-ranking and embedding sparse vectors are significant additions to its platform. Since re-ranking models are applicable to lexical search, both of these efforts underscore the need to pair dense and sparse vector search to maximize the utility of vector database information retrieval.

The vendor’s capital value proposition, however, is likely its capacity to offer these models to customers in a singular manner in which much of the maintenance and work required to employ them is offloaded to Pinecone. “This is the first attempt, the first model we released under our own name and that we trained ourselves,” Jones said. “It’s to tackle a really big problem which is, there’s really not that many sparse models, and certainly not very many available for hosting.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)