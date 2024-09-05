# Boost LLM Results: When to Use Knowledge Graph RAG
![Featued image for: Boost LLM Results: When to Use Knowledge Graph RAG](https://cdn.thenewstack.io/media/2024/08/7f543328-rag-1024x576.png)
Sometimes retrieval-augmented generation (RAG) systems don’t go deep enough into a document set to find the required answers. We might get generic or shallow responses, or we might get responses where the [RAG](https://www.datastax.com/guides/what-is-retrieval-augmented-generation?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval) system retrieves low detail and then fills in the gaps with unrelated or incorrect information — what is called “[hallucinations](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/).”

Deep knowledge bases and document sets may contain all the information we need to answer questions in a RAG prompt, but the [RAG system](https://thenewstack.io/enhancing-ai-coding-assistants-with-context-using-rag-and-sem-rag/) might not be able to find it all, especially if the required information is spread across multiple documents and different topics or subtopics. In particular, vector retrieval will often produce a good set of documents, but some concepts within those documents require more information in order for the system to understand them, so it would be helpful to also retrieve additional documents directly related to those concepts.

Some types of data sets that are likely to have these issues:

- Collections of documents that frequently reference each other.
- Documents with sections, definition of terms and glossaries, where checking the cross-references is the only way to have the complete picture of a given topic.
- Large wikis or knowledge bases in which almost every paragraph contains HTML links to other pages and to external websites.
Data sets like this are often found in:

- Legal documents
- Technical documentation
- Research and academic publications
- Highly interconnected websites
If your organization has deep and complex data sets of interrelated documents and other content, standard RAG implementations might not successfully address some of the most common use cases, especially when prompts ask for detailed explanations that include information at both broad and highly specific levels. Converting the implementation to [graph RAG](https://thenewstack.io/better-llm-integration-with-content-centric-knowledge-graphs/), which means augmenting the RAG system with a [knowledge graph](https://hackernoon.com/how-to-use-knowledge-graphs-for-retrieval-augmented-generationwithout-a-graph-db) that assists with retrieval, can enable the system to dive deeper into data sets to provide detailed and correct responses to prompts requesting detailed and specialized information.

Let’s explore the key concepts behind how a knowledge graph can improve performance of a RAG system, what such a graph might look like and how to start building a graph RAG system on your own data.

## How Does a Graph Help?
In a nutshell, a knowledge graph combined with a [vector store](https://www.datastax.com/guides/what-is-a-vector-database?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval) of documents can provide a way to directly connect chunks of text that might not be close or similar to each other in the vector space, and thus are not inherently seen as “relevant” to one another during the retrieval process.

A typical RAG system retrieves documents (or “[chunks](https://www.datastax.com/blog/chunking-to-get-your-data-ai-ready?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval)”) from the vector store that are most relevant to the prompt according to a measure of vector similarity. If those documents contain links or references to other documents, then clearly the authors of the documents thought they were meaningfully related. And if the documents are meaningfully related, why wouldn’t we want to use that information to dig deeper and get more details that might help answer the prompt?

To restate the situation: We have documents that are clearly and directly related — via links or references — and we want to ensure that our RAG system considers those connections when retrieving documents. Building a network of linked documents results in a graph structure that we can traverse to find related documents that might not otherwise be found during typical document retrieval, using a graph to augment RAG; this is known as graph RAG.

The main idea is that we already have an implicit and high-confidence graph that relates documents to one another — via direct links and references — and we want our RAG system to make full use of these known, high-certainty connections before it relies on less-certain vector similarity and relevancy scores to fill in the details in the response, which would run a higher risk of responding with hallucinations.

## What Types of Connections Can We Use?
The possibilities for defining a graph are limitless, but we’ve found that the best and most effective types of connections for use in graph RAG are those that are well-defined and meaningful. That is, we want it to be clear what is a connection and what is not, so we tend to avoid defining connections for fuzzy concepts like general topic and sentiment. And we want the connections to be meaningful, in the sense that having a connection between two documents in the [graph makes it very likely that the content](https://thenewstack.io/better-llm-integration-with-content-centric-knowledge-graphs/) in each document is relevant to the other. Below are some of the most useful ways to define connections between documents in graph RAG.

### HTML Links
One of the clearest and most obvious ways to connect documents these days is to have a direct link from one to the other, in the sense of HTML links in web-based documents. From a human perspective (as opposed to an AI perspective), if we click on a link in one document and end up at another document, there is a link between them. This can be defined and implemented in software with any number of link extraction tools. Generally, the author of the documents has added a link for a reason, and so there is a meaningful connection between them. In this way, HTML links are some of the most well-defined and meaningful links between documents that we can use in our knowledge graphs.

Building a knowledge graph from HTML links has worked very well on data sets such as technical documentation and large wikis or knowledge bases. The interconnected nature of these types of data sets makes graph RAG especially useful for diving into specialized details, definitions and subtopics that may not be found by vector search alone.

Some example code for extracting links from HTML documents:

For an end-to-end example of graph RAG using HTML link extraction to build the graph, check out this recent piece, “[Better LLM Integration and Relevancy With Content-Centric Knowledge Graphs](https://www.datastax.com/blog/better-llm-integration-and-relevancy-with-content-centric-knowledge-graphs?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval).”

### Keywords and Topics
Although building a graph from connections based on general topics or sentiment can be too fuzzy and uncertain for the purposes of graph RAG, it is often possible to effectively use highly specialized keywords and topics that are well-defined and meaningful. In particular, keywords within a specialized domain can be effective for making connections between documents within graph RAG. Specialized keywords are not always captured in the vector embedding representation of documents, and therefore would benefit from a stronger and more deliberate connection that a knowledge graph would give.

There are some excellent tools for extracting keywords; the following is a simple example of how to [extract keywords using “keyBERT”](https://github.com/MaartenGr/KeyBERT):

This extracts specialized domain keywords:

How we turn these keywords into a knowledge graph depends on our use case and data model. One example can be found in [the RAGStack docs on knowledge graph RAG](https://docs.datastax.com/en/ragstack/knowledge-graph/knowledge-graph.html).

Building a graph with meaningful keywords as nodes connected to the documents in which they appear can be an effective graph RAG strategy. Note that to connect documents to one another via the graph, we have to traverse the graph to a depth of two or more: one step from a document to its keywords and a second step to other documents containing those keywords.

### Terms and Definitions
In legal documents, academic publications and works of research, we have terms and definitions defined as a list or glossary, usually at the beginning or end of the document. In these cases, it’s helpful to reference these terms and definitions throughout the document so we can always be clear about what’s being said. Without these definitions of terms, some parts of documents can become vague or almost meaningless.

One particularly apt example is the case of a large number of documents that are contracts between tenants and landlords; we’ll query them using our RAG system. The documents would typically be chunked before being loaded into the data store, which means that any terms and definitions appearing at the beginning or end of the documents are not inherently included with the chunks themselves. And because there are many contracts between different tenants and landlords, any chunk that references the word “tenant” or the word “landlord” would be ambiguous without connecting it to the particular tenant and the particular landlord in question.

In this case, it would be extremely useful to have a knowledge graph that explicitly connects document chunks with the appropriate definitions of terms appearing in them. The specific implementation for extracting those definitions and terms, and connecting them to the correct chunks of documents, would depend on the format of the original documents themselves, the structure of the glossary or definitions relative to the rest of the document, etc. Many text and document parsers are available and appropriate for this purpose, and work is being done to standardize the process with graph RAG in mind.

### Document Structure – Section References, Page Numbers, etc.
When documents are chunked and loaded into a vector store, all document structure outside of the chunks is lost unless we capture it in some way. For many RAG use cases, it would be helpful for the system to know where each document chunk sits in the overall structure of the document, all headings and subheadings, page numbers, and which chunks come immediately before and after the given chunk.

Preserving this information in a knowledge graph connected to each chunk has two main advantages for the purposes of graph RAG. First, knowing where a chunk sits within the document allows us to pull in nearby text, which could be the chunks immediately before and after, text from the same page or text from the same sections — all of which could provide supporting evidence and details for the topics mentioned in the initial chunk. Second, some documents include cross-references to other section numbers, headings and page numbers, and thus it would be helpful to have a knowledge graph allowing the RAG system to directly retrieve the chunks in the sections that are referenced.

## How Do We Build This Graph to Improve Our Rag Systems?
We lay out more technical details in [this piece on content-centric knowledge graphs](https://www.datastax.com/blog/better-llm-integration-and-relevancy-with-content-centric-knowledge-graphs?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval), where we explain how to build a knowledge graph from web-based technical documentation using `langchain`
, `ragstack`
, Cassandra and related tools. We build the knowledge graph from HTML links appearing in the documents, which can be one of the easiest and most useful ways to build a knowledge graph for graph RAG.

To process an HTML document and add appropriate metadata for graph RAG, we can use a helper function such as:

And once the documents have been processed and the proper metadata has been added, they can be loaded to a graph vector store like the example below, which uses [Astra DB](https://www.datastax.com/products/datastax-astra?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval) as the underlying data store, and `CassandraGraphStore`
as the implementation of `GraphVectorStore`
, which functions as both the knowledge graph and vector store:

## Learn More
To learn more about optimizing the construction and use of knowledge graphs for graph RAG, read this recent article, “[Scaling Knowledge Graphs by Eliminating Edges](https://thenewstack.io/scaling-knowledge-graphs-by-eliminating-edges).” This includes an introduction to the handy “GraphVectorStore” in Langchain.

For the latest updates on how DataStax can help get you started with graph RAG, quickly and with minimal code changes, check out the work we’re doing on [RAG with Vector Graph](https://www.datastax.com/products/vector-graph?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=deeper-retrieval).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)