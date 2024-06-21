# Better LLM Integration With Content-Centric Knowledge Graphs
![Featued image for: Better LLM Integration With Content-Centric Knowledge Graphs](https://cdn.thenewstack.io/media/2024/06/8f360af6-knowledge-1024x575.png)
Extracting knowledge graphs using a [large language model (LLM)](https://roadmap.sh/guides/introduction-to-llms) is time-consuming and error-prone. These difficulties arise because the LLM is being asked to extract fine-grained, entity-specific information from the content. Inspired by the [benefits of vector search](https://thenewstack.io/vector-search-is-coming-to-apache-cassandra/), especially the ability to get good results from ingesting content with relatively little cleaning, let’s explore a coarse-grained [knowledge graph](https://thenewstack.io/how-knowledge-graphs-make-data-more-useful-to-organizations/) — the content knowledge graph — focused on the relationships between content.

If you want to jump right in, you can also [check out this notebook](https://colab.research.google.com/github/datastax/ragstack-ai/blob/main/libs/knowledge-store/notebooks/astra_support.ipynb).

## Entity-Centric Knowledge Graphs
Historically, knowledge graphs have had nodes represent specific concepts (or entities) and used edges to represent specific relationships between those concepts. For example, a knowledge graph built with information about me and my employer might look something like the following:

This fine-grained, entity-centric knowledge graph allows for a variety of queries to be expressed using a graph query language like Cypher or Gremlin. Recently, knowledge graphs have become popular as an alternative way to store and retrieve information for consumption by an LLM as part of advanced [retrieval-augmented generation](https://www.datastax.com/guides/what-is-retrieval-augmented-generation?utm_source=thenewstack&utm_medium=byline&utm_campaign=Knowledge-graph&utm_term=all-plays&utm_content=scaling-knowledge-graphs) (RAG) techniques. The ideas are compelling: The knowledge graph captures relationships between information that vector similarity search would miss, and LLMs make it possible to extract knowledge graph triples (source, relationship, target) from unstructured content with only a prompt. This is why this historic concept seems relevant to so many.

However, extracting this fine-grained knowledge graph from unstructured information is difficult, time-consuming and error-prone. To get the best results, you (and a domain expert) will need to:

- process all of your unstructured content with the LLM to extract information,
- guide the LLM on the kinds of nodes and relationships you wish to extract by creating a “knowledge schema” (or ontology),
- inspect the graph of extracted information to make sure the LLM is extracting the correct details, and
- reprocess all the content when you change the knowledge schema.
Between the need for human experts and the challenge of applying the LLM to all of the content, the cost of building and maintaining this graph is high. Bottom line: There’s a reason that most examples of using knowledge graphs for RAG operate on just a few sentences or paragraphs.

Using entity-centric knowledge graphs is much harder to scale and to get good results from than just chunking the content and dumping it into a vector store. Is there any way we could bring the benefits of vector search to knowledge graphs — specifically, making construction as easy as chunking and embedding the content while also preserving the original content until the LLM knows the question to be answered?

## Content-Centric Knowledge Graphs
If we start with nodes representing content (chunks of text, for example) instead of fine-grained concepts or entities, the nodes of the graph are exactly what is stored when using vector search. Nodes may represent a specific text passage, an image or table, a section of a document or other information. These nodes represent the original content, allowing the LLM to do what it does best: process the context and pick out the important information. When building the fine-grained graph, this happens before the question is known, necessitating speculation and/or human guidance when determining which facts matter.

In fact, this is part of why we believe these content-centric knowledge graphs are better: LLMs excel at processing large amounts of context, and doing so when they know the question enables them to find the most useful needles in the haystack. Entity-centric knowledge graphs require reducing the information to the simple annotations on edges, making them less useful as context to LLMs.

Edges between nodes represent a variety of structural, semantic and metadata-based properties. For instance, a chunk containing a hyperlink could have a `links_to`
edge pointing at the linked content, or two chunks with common keywords might have an edge indicating the similar content `has_keywords: [...]`
. A text passage may link to an image or table in the same section that it references, or passages in a document could link to definitions of key terms.

Starting from three documents about Ben and DataStax, a coarse-grained graph similar to the previous example might be:

Since the nodes are chunks of documents, the graph wouldn’t change if the article on DataStax had more information, such as when it was founded. With the fine-grained approach, we would need to decide whether that extra information should be extracted.

The main benefits of this compared to fine-grained knowledge graphs are that the approach is:

**Lossless**: The original content is preserved within the nodes, meaning no information is discarded (i.e., not extracted) during the creation process. This reduces the need to re-index information as your needs change, and allows the LLM to do what it does best: extract answers from that context based on the question.**Hands-off**: No experts are necessary to tune the knowledge extraction. You add some edge extraction based on keywords, hyperlinks or other properties of the data to your existing vector-search pipeline, and then links are automatically added.**Scalable**: The creation process can be implemented using simple operations on the content, with no need to invoke an LLM to create the knowledge graph.
### Creation
Unlike a fine-grained graph, the process to create these coarse-grained graphs is far simpler. No domain expert is needed. Instead, the content is loaded, chunked and written to the store. Each of the chunks can be run through a variety of analyses to identify links. For instance, links in the content may turn into `links_to`
edges, and keywords may be extracted from the chunk to link up with other chunks on the same topic.

We make use of several techniques for adding edges. Each chunk may be annotated with URLs that it represents, as well as HREFs that it references. This allows capturing explicit links between content, as well as representing cases such as a document linking to a definition within the same page through the use of fragments. Additionally, each chunk may be associated with keywords, and all chunks with a given keyword will be linked together.

More techniques for linking are being developed, including automatic links based on properties of the chunks as well as using structural properties such as locations on the page.

### Retrieval
Retrieval on these coarse-grained graphs combines the benefits of vector search and knowledge graph traversal. Starting points can be identified based on similarity to the question and then additional chunks can be selected by following edges, with a bound on how deep (distance from vector search nodes) to traverse.

Including nodes that are related via both embedding distance (similarity) and graph distance (related) leads to a more diverse set of chunks. Many of the edges in the graph will lead to information that deepens the context without being directly relevant to the question. These relationships allow expanding the context or limiting the context to “nearby” content. This additional related information improves the quality of answers and reduces hallucinations.

## Case Study: Astra Support Articles
We loaded 1,272 documents from the [DataStax Astra DB](https://www.datastax.com/products/datastax-astra?utm_source=thenewstack&utm_medium=byline&utm_campaign=knowledge-graph&utm_term=all-plays&utm_content=scaling-knowledge-graphs) support site and some external pages linked from them. It took less than five minutes to scrape, parse the HTML, extract hyperlinks, convert the content to markdown and write resulting documents to the Astra DB store.

This required almost no work on my part beyond basic data cleaning and a few lines to populate metadata describing the links. Specifically, I didn’t look at the data or try to create a knowledge schema (ontology) capturing the information I wished to extract. This is important, because I’m not sure what parts of the 1,272 documents would be useful for questions that might be asked.

I could have reduced the code by using more of [LangChain](https://www.langchain.com/)’s built-in document-loading functionality, but it had problems because it wanted to load all the pages into memory before writing them out, so I had to manage the iteration myself.

For the content-centric graph, we’ll use the `KnowledgeStore`
class available as part of [ragstack-ai-knowledge-store](https://pypi.org/project/ragstack-ai-knowledge-store/). This class provides an implementation of the content-centric knowledge graphs based on [LangChain interfaces](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/). In fact, it implements LangChain’s `VectorStore`
interface, so nothing needs to change to add documents to the graph.

While you can set the metadata for links yourself, there are also convenient utilities for doing so automatically. For our purposes, we wish to do the following to each HTML document:

- Use a CSS selector based on the source URL to locate the content (such as exclude the navigation, etc., from the chunk and links).
- Extract links from the HTML content.
- Convert the HTML content to markdown.
While LangChain document transformers perform parts of this procedure, they aren’t easily composable, so we just write some code to clean the HTML:

Again, because the knowledge graph implements the vector store interface, it’s easy to create a retriever and use it in a LangChain expression:

### Question
The question I used in all the examples is a relatively simple one about how Astra DB implements vector indexing.

*“What vector indexing algorithms does Astra use?”*
The answer to this question requires reading multiple parts of the documentation and connecting that with information available on externally linked sites.

### Vector Only
The answer is relatively shallow — just describing the library that is used to implement vector search ([JVector](https://github.com/jbellis/jvector)). This answer is correct, but it doesn’t include any details about the algorithms that Astra DB uses or how it actually works.

If we look at the pages retrieved to answer the question — those with the highest similarity to the question — we see that it didn’t get to any of the deeper documentation:

- https://docs.datastax.com/en/astra-db-serverless/get-started/concepts.html
- https://docs.datastax.com/en/cql/astra/getting-started/vector-search-quickstart.html
- https://docs.datastax.com/en/astra-db-serverless/databases/embedding-generation.html
- https://docs.datastax.com/en/astra-db-serverless/get-started/astra-db-introduction.html
### Depth 1 Traversal
Changing the retriever to perform traversal is easy and gives us better results.

The answer is better; it explains how JVector implements a graph-based index for scalable vector searches and how the documents are immediately available.

Note that the results take a lot longer to generate — 17.5 seconds (compared to 6.1 seconds for vector search only). Following the edges from the first four documents we retrieved with vector search led to 31 total documents being retrieved. The extra tokens took the LLM a bit longer to make sense of, although they still did a great job coming up with the answer. At the same time, it doesn’t feel like the result deeply answers the question. Perhaps because there was so much for the LLM to consider, it didn’t get to the most concise answer it could.

What if there was a way to retrieve fewer documents, while maximizing diversity? Was there a way to follow the edges when they provided additional relevant information, especially when that information increased the diversity of what was retrieved? We can modify maximum marginal relevance (MMR) retrieval to do exactly this.

### MMR Traversal
The MMR traversal search performs a combination of vector and graph traversal to retrieve a specific number of documents. Unlike traditional MMR, after a node is selected, its adjacent nodes become candidates for retrieval as well. This allows the MMR traversal to explore the graph, using the diversity parameter to decide how much to prefer similar nodes versus how much to prefer diverse nodes retrieved via vector search or graph traversal.

As with switching to traversal, using this technique is an easy change to the `retriever`
:

This answer seems even better. Not only does it talk about how JVector is implemented, but it provides details on some of the techniques that it uses to handle the search and update efficiently.

If we take a look at what was retrieved, we see that it only retrieved four documents (after considering 15 in total). It retrieved a combination of similar results (such as the “getting started” and indexing concepts) as well as the deeper results (the documentation for [JVector](https://github.com/jbellis/jvector/)) needed to answer the question.

- https://docs.datastax.com/en/astra-db-serverless/get-started/concepts.html
- https://docs.datastax.com/en/astra-db-serverless/cli-reference/astra-cli.html
- https://github.com/jbellis/jvector
- https://docs.datastax.com/en/cql/astra/developing/indexing/indexing-concepts.html
## Conclusion
Content-centric knowledge graphs are available for preview as part of [RAGStack](https://www.datastax.com/products/ragstack?utm_source=thenewstack&utm_medium=byline&utm_campaign=knowledge-graph&utm_term=all-plays&utm_content=scaling-knowledge-graphs). You can also check out the [notebook](https://colab.research.google.com/github/datastax/ragstack-ai/blob/main/libs/knowledge-store/notebooks/astra_support.ipynb) from the case study. We are working on contributing them to LangChain, as well as a variety of exciting improvements to how edges are created and traversed. Stay tuned for exciting follow-ups in this area.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)