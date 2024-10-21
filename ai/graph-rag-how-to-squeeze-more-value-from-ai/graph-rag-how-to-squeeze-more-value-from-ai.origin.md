# Graph RAG: How To Squeeze More Value From AI
![Featued image for: Graph RAG: How To Squeeze More Value From AI](https://cdn.thenewstack.io/media/2024/10/54702e16-graph-rag-squeeze-value-1024x576.jpg)
These days, it seems like everyone is doing [retrieval-augmented generation (RAG)](https://thenewstack.io/fixing-relevancy-in-retrieval-augmentation), and more and more are adding knowledge graphs to make [graph RAG](https://thenewstack.io/boost-llm-results-when-to-use-knowledge-graph-rag/). But many of them get stuck in the R&D stage, struggling (at least a little bit) to pull their proofs of concept into production.

Graph RAG, just like most AI technologies, is subject to a few tough-to-avoid rules:

**Powerful potential:**Graph RAG can add significant enterprise value.**Easy to start:**Implementing simple graph RAG is straightforward.**Hard to perfect:**Bringing graph RAG from proof-of-concept to production is difficult.
One enterprise that has found success with graph RAG is [Glean](https://www.glean.com/), a platform for connecting an organization’s internal data and making it all searchable and interactive via artificial intelligence (AI) interfaces and agents. Glean [just secured over $260 million](https://www.glean.com/blog/glean-series-e-prompting-launch) in its latest funding round, based on the strength, popularity and revenue-generating ability of its core platform — the foundation of which is graph RAG.

Glean has implemented a graph RAG-based platform that adds value, cuts costs and streamlines internal processes, making it easier to get started with graph RAG using the latest tools. Even so, specific graph RAG challenges can make it difficult to move from R&D into production, but there are ways to maximize your chances of success.

## Connecting the Right Information at the Right Time Is $$$$
It’s important to note that Glean is a power user of its own product. If you’re wondering about the secret to success of this five-year-old company with a long list of prominent customers (including Pinterest, Reddit and Instacart), a well-run organization of this scale usually has streamlined how it operates as an organization. The fact that Glean runs on Glean — and its customers are very happy — has to be one of the strongest arguments in favor of its product — and its potential to add enterprise value.

One of Glean’s customers is “one of the world’s largest ride-sharing companies,” which turned to Glean after attempting to build an in-house solution that didn’t live up to expectations. Within a month, the company saw double the usage on the Glean platform compared to its internal solution.

We at DataStax love Glean, both from the perspective of being customers for a while now and, more recently, as partners [integrating Langflow and Glean](https://www.datastax.com/blog/glean-datastax-partner-to-help-developers-harness-enterprise-search?utm_medium=byline&utm_source=tds&utm_campaign=graph-glean&utm_content=glean?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=glean). But the main point here is that the Glean story is a perfect example of not only how powerful and valuable graph RAG can be but also of how getting graph RAG right is challenging, even for some of the biggest names in tech.

The big ride-sharing company says after switching to Glean it’s saving, on average, two to three hours per week per employee and over $200 million per year — all from employees simply “finding information faster,” [Matt Kixmoeller](https://www.linkedin.com/in/mattkix/), CMO at Glean, [told VentureBeat](https://venturebeat.com/data-infrastructure/how-to-take-advantage-of-a-generative-tool-fueling-gleans-260m-raise-graph-rag/). Time is money, and a lot of hours saved is a lot of money saved — but only if the work is done well.

Further down, I’ll discuss some nuanced differences between mediocre graph RAG and great graph RAG, but first let’s talk about how easy it is to get started.

## Getting Started With Graph RAG Is Easy
So if a big ride-sharing company couldn’t build its own platform effectively, then why would I say that it’s easy to implement graph RAG yourself?

Well, first of all, technologies supporting RAG and graph RAG have come a long way in the past year. Twelve months ago, most enterprises hadn’t even heard of retrieval-augmented generation. Now, not only is RAG support a key feature of the best AI-building tools, [like LangChain](https://python.langchain.com/docs/tutorials/rag/), but now there’s [Langflow,](https://www.datastax.com/blog/rag-development-is-hard-enter-langflow?utm_medium=byline&utm_source=tds&utm_campaign=graph-glean&utm_content=glean?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=glean) a visual IDE for LangChain-based RAG, which allows you to set up a RAG system with little to no code.

### Some Resources for Getting Started
There is a lot to learn about RAG, as our [guide to retrieval-augmented generation](https://www.datastax.com/guides/what-is-retrieval-augmented-generation?utm_medium=byline&utm_source=tds&utm_campaign=graph-glean&utm_content=glean) explains, but you don’t need to know all of that to get started. It takes only a few minutes to get a RAG app up and running (for free) [using Langflow and DataStax Astra DB](https://docs.datastax.com/en/langflow/examples/vector-rag-example.html).

[Graph RAG](https://medium.com/building-the-open-data-stack/a-guide-to-graph-rag-a-new-way-to-push-the-boundaries-of-genai-apps-f616d47758a0) is a newer variant of RAG strategies, so the software tools are generally as mature as they are with plain RAG. But there are still some easy ways to get started.
One of the quickest paths to a working graph RAG app, particularly if you are already using LangChain, is [GraphVectorStore](https://www.datastax.com/blog/now-in-langchain-graph-vector-store-add-structured-data-to-rag-apps?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=glean), recently added to LangChain. It essentially adds graph functionality to a typical vector store. With it, you can [easily turn RAG into graph RAG using links](https://thenewstack.io/boost-llm-results-when-to-use-knowledge-graph-rag/) that are (probably) already in your document data set.

Many folks new to graph RAG think that there is a huge step in complexity from plain RAG or that they need a specialized graph database. But [you don’t need a graph database](https://www.datastax.com/blog/knowledge-graphs-for-rag-without-a-graphdb?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=glean) to do graph things, including graph RAG.

Even scaling a graph RAG system can be straightforward, as the article “[Scaling Knowledge Graphs by Eliminating Edges](https://thenewstack.io/scaling-knowledge-graphs-by-eliminating-edges/)” explains.

Just about every major player in the AI space offers resources for understanding and getting started with RAG (there’s even [a Coursera course](https://www.coursera.org/projects/introduction-to-rag)).

With all of the tools and tutorials available, getting started with graph RAG is the easy part …

## But Bringing Graph RAG Into Production Is Hard
Graph RAG seems promising for enhancing retrieval-augmented generation (RAG) systems, especially when traditional vector search fails to handle complex queries involving multiple documents across varied contexts and formats. However, bringing graph RAG into production presents unique challenges.

### Understanding Graph RAG’s Role
Typically, RAG systems excel in straightforward scenarios but struggle when answers require aggregating information across diverse knowledge bases. This often leads to the system missing crucial documents — not due to a malfunction, but because these documents lack sufficient semantic similarity to the user’s query.

For instance, a RAG system might overlook relevant documents if the necessary information is embedded within dense, detailed content or if the documents cover a range of topics only loosely related semantically. This can be particularly problematic when addressing semantic search queries that necessitate both general and specific information.

### Addressing the Retrieval Gap
The core problem graph RAG aims to solve is the limitation of plain retrieval-augmented generation systems, which solely rely on semantic closeness, [thus failing to retrieve less semantically obvious but relevant information](https://towardsdatascience.com/vector-embeddings-are-lossy-heres-what-to-do-about-it-4f9a8ee58bb7). Modifying [vector](https://thenewstack.io/why-vector-size-matters) search to enhance retrieval often involves complex adjustments to embeddings, which are not only technically demanding but also costly and potentially ineffective for the specific nuances of a user query.

Instead of refining the semantic model to force a fit — potentially causing more issues — integrating a knowledge graph provides a more targeted approach. Knowledge graphs enable the connection of related concepts that semantic models miss. For example, linking geographically or contextually related terms, [like “Space Needle” and “Lower Queen Anne neighborhood,”](https://towardsdatascience.com/your-documents-are-trying-to-tell-you-whats-relevant-better-rag-using-links-386b7433d0f2) is more straightforward and reliable through a knowledge graph than trying to tweak embeddings to achieve the same outcome.

### Building Effective Graph RAG Systems
The key to a successful graph RAG implementation lies in accurately capturing and leveraging the non-semantic relationships among data. By augmenting semantic search with structured, graph-based data, we can enhance document retrieval to better respond to complex queries.

To summarize the issue that we’re trying to tackle with graph RAG: There is semi-structured, non-semantic information connecting many of the concepts that appear in unstructured documents. We would like to use this connection information to complement semantic vector search in order to retrieve documents that are best suited to answer prompts and questions within the use cases. We simply want to make retrieval better, and we want to use some external information or external logic to accomplish that, instead of relying solely on semantic vector search to connect prompts with documents.

### Guiding Principles for Integrating Graph and RAG
Some guiding principles to keep in mind while building and testing a graph RAG application are:

- The graph should contain high-quality, meaningful concepts and connections.
- Concepts and connections should be relevant to prompts within the set of use cases.
- Graph connections should complement, not replace, vector search.
- The usefulness of one- and two-step graph connections should be prioritized; relying on more than three steps to make connections should be reserved only for specialized use cases.
Following these principles is intended to jointly increase explainability, prevent over-complexity and maximize efficiency of building and using a graph RAG system.

### Challenges of Moving Graph RAG into Production
Most developers understand that there’s a lot of uncertainty in building a system like graph RAG. Unexpected things can happen during data prep and loading, while building a knowledge graph, while querying and traversing the graph, during results compilation and prompt construction, and at virtually any other point in the workflow. While initially implementing graph RAG is not difficult, here are some subsequent challenges of further building out and testing a graph RAG application:

**Graph RAG isn’t doing much better than plain RAG:**This is a very common symptom with many possible causes. One may be that vector search finds the right documents without using graph retrieval-augmented generation.**You (still) see hallucinations:**This is usually not caused by the graph, and the inability to generate relevant responses is present even when disabling the graph aspects of RAG.**The graph is too big:**Too many edges or nodes can cause problems with scaling and the quality of connections made during graph traversal.**The graph is too small:**A low number of edges or nodes leads to a low number of meaningful graph connections being made.**Your implementation requires increased deployment complexity:**Difficult deployments are always a challenge, especially if they involve new, specialized software tools.**Your implementation doesn’t scale:**This article on[scaling knowledge graphs](https://thenewstack.io/scaling-knowledge-graphs-by-eliminating-edges/)discusses this challenge and gives a potential solution.
This list of potential issues isn’t comprehensive, but it represents a few of the potential issues we have been looking at. To address them, we’re starting to build tools that simplify [the move from experimentation into production using the Langflow API](https://www.datastax.com/blog/experimentation-to-production-datastax-langflow-api-public-preview?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=glean). Hopefully, it can help with some of these issues.

## Simplifying Graph RAG Success
[Arjun Landes](https://www.linkedin.com/in/arjunlandes/), engineering manager at Glean, noted in VentureBeat, “The fact that we were able to build such a sophisticated knowledge graph and combine it with LLMs [large language models] is where the real power is.” I don’t know details of their system, but I agree with the idea that the power is in the combination, which Glean seems to have done very well.
It’s important to note that Glean’s internal document data set is an ideal use case for graph RAG. It effectively connects internal elements like people, projects and products — manageable due to the finite scope of organizational data compared to, say, the expansive data on Wikipedia. This focus likely contributed significantly to Glean’s success by making its challenge more tractable.

### Having the Right Data Is Key
Even with an ideal use case, the quality of the knowledge graph is key; it must connect the right elements at the right times without overwhelming the system with irrelevant data. An overly dense graph could burden the system, forcing it to sift through excess information, while a sparse yet high-quality graph might still surpass traditional RAG systems by focusing on essential connections.

Glean has also excelled in integrating diverse knowledge bases across various platforms, a feat more about solid data engineering than AI prowess. The advent of [generative AI](https://thenewstack.io/when-and-how-will-enterprise-genai-apps-get-real) (GenAI) and [large language models (LLMs)](https://thenewstack.io/the-current-state-of-llms-riding-the-sigmoid-curve) has made integration of disparate data types easier, enabling Glean to bring together diverse data sources into a cohesive RAG system.

Glean’s user interface also stands out, offering a seamless experience that masks the complexities of the integrated technologies. This user-centric design has made its system not only effective but also accessible, enhancing the overall user experience.

## Looking Ahead
The progress in graph RAG systems signifies a shift towards more sophisticated applications of AI models in processing and linking complex data. This evolution promises enhanced efficiency and the potential to revolutionize knowledge management across various industries.

As we move forward, the principles laid down today are expected to pave the way for groundbreaking applications in the near future, potentially heralding a new era of what some are calling the “Intelligence Age.”

To learn more, take a look at the [DataStax guide to graph RAG](https://medium.com/building-the-open-data-stack/a-guide-to-graph-rag-a-new-way-to-push-the-boundaries-of-genai-apps-f616d47758a0?utm_medium=byline&utm_source=tds&utm_campaign=graph-glean&utm_content=glean?utm_medium=byline&utm_source=thenewstack&utm_campaign=graph-rag&utm_content=glean).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)