# Writer.com’s Graph-Based RAG Alternative to Vector Retrieval
![Featued image for: Writer.com’s Graph-Based RAG Alternative to Vector Retrieval](https://cdn.thenewstack.io/media/2024/02/50c2cc56-dan-meyers-0onaidc0hua-unsplash-1024x683.jpg)
Retrieval-Augmented Generation (
[RAG](https://thenewstack.io/retrieval-augmented-generation-for-llms/)) is the most common method of integrating a pre-trained large language model (LLM) with an external data source; an important factor in creating enterprise AI applications. After all, what’s the point of an organization using an LLM if it can’t utilize its own unique — and probably proprietary — data set?
RAG is also one reason why
[vector databases](https://thenewstack.io/vector-databases-long-term-memory-for-artificial-intelligence/) have become so popular in AI engineering. In many cases, an app will use RAG to do vector retrieval and other LLM optimizations that are best achieved with vector databases.
However, one company is pitching an alternative use for RAG — one that doesn’t involve vector databases.
[Writer.com](https://writer.com/) is a proponent of “graph-based” RAG, which means building a knowledge graph and using graph databases instead of vector databases.
“Knowledge Graph, our graph-based retrieval-augmented generation (RAG), achieves higher accuracy than traditional RAG approaches that use vector retrieval,” claims Writer on its homepage.
To find out more about Writer’s graph-based RAG approach, I interviewed its CEO
[May Habib](https://www.linkedin.com/in/may-habib/).
I first asked how Writer defines “knowledge graph,” since that term has a fairly long history in the field of Knowledge Management. Traditionally, knowledge graphs have been a way to represent the relationships and connections between different pieces of data. More recently,
[Neo4j](https://thenewstack.io/illuminating-the-anonymous-with-neo4js-graph-database/) and similar [graph database](https://thenewstack.io/graph-databases-why-are-they-suddenly-popular/) companies have adopted the term (“Power your applications with knowledge graphs,” states Neo4j on its homepage).
“So, folks tend to get knowledge graphs confused with graph databases,” replied Habib, adding that “we’re not a replacement for Neo4j.” She then explained that Writer has a specialized LLM that maps semantic relationships between data points — and that is what the company means by a “knowledge graph.”
## No More Chunking
Writer’s semantic graphing approach is an alternative to the “chunking” process of RAG when it’s used with vector databases, Habib explained.
“The problem with that approach [RAG using vector databases] is so much of the context is lost, actually, when you do that first step of the data pre-processing to chunk out the data. And people spend a lot of time in engineering, and NLP cycles, to do contextual and hierarchical chunking, and try to then kind of re-embed the chunks into the context in which they came from, etc. A lot of those use cases are highly complex, dynamic enterprise use cases, [where] those approaches tend to be really brittle, and it is not a scalable approach — when you think about how much data needs to be updated and needing to do that kind of re-embedding every time something changes.”
According to Habib, Writer uses its “small but mighty” LLMs — they
[range from](https://writer.com/blog/palmyra/) 120 million parameters to 20 billion — to add “a new set of metadata layer” at the data pre-processing stage. Or as she put it in [a recent LinkedIn post](https://www.linkedin.com/posts/may-habib_2-core-facts-to-understand-if-you-want-to-activity-7157743924189491200-KZs5/), “we use LLMs to build AI knowledge graphs of your data before doing anything else.”
In
[a follow-up post](https://www.linkedin.com/posts/may-habib_mondays-post-on-rag-posted-in-comments-activity-7158841126613848064-v5ky/), Habib contended that the vector database RAG approach is not as semantic as it appears. “Embeddings capture semantic similarity between your data and a **query**, but *do not* also store or connect the relationships *between* data in said multi-dimensional space,” she wrote.
Writer’s approach is to gather more metadata at the start, using its own models, and then using graph databases instead of vector databases to manage the data.
“A graph DB is designed to store the actual information — those are the nodes — [and] the relationships between entities — those are the edges. So they scale really, really successfully too.”
## Is This the New Knowledge Management?
In the field of knowledge management (KM), an “ontology” is typically created to capture meaning within an organization. The World Wide Web Consortium (W3C) has two official ontology languages: RDFS (Resource Description Framework Schema) and OWL (Web Ontology Language). I was curious how LLMs are impacting this, so I asked Habib whether KM practitioners within enterprises are using Writer — or does its tool effectively replace that role in organizations?
“If you’ve got ontology systems that you have built already and graphs that you’ve invested in, generative AI is an incredible compliment,” she replied. However, she added that “the graphs that we build on top of data very much are for the consumption of machines, not people.”
What she seemed to be suggesting is that KM practitioners needn’t spend so much time creating new ontologies, because Writer can do that for them.
“So will somebody use Writer to help technical writers come up with ontologies that kind of feed knowledge graphs? [Yes] I’m sure. But I don’t think that role goes anywhere — I think
*the way* that job is done perhaps changes.”
I noted a common criticism of LLMs, especially in an organizational setting, is the “garbage in, garbage out” problem. I suggested that technical writers and other KM practitioners will still be needed to capture the core knowledge in an enterprise.
Habib acknowledged that this is an issue, and that sometimes someone has to “filter through all of the noise […] to come up with the golden set of documents.” But she said that Writer’s LLMs do take into account, when building its knowledge graphs, “what is the quality rubric?”
## Use Cases
In terms of enterprise use cases, Habib says it offers “solution maps” to its target verticals — in insurance, wealth management, in CPG [consumer packaged goods] and retail. She said it aims to simplify workflows in these industries. She used CPG and retail as an example — “it is digital shelf, it is customer and user engagement in corporate functions, it is finance and supply chain and RFPs [request for proposals].”
She added that Writer is a “full stack platform,” including an app studio. She wouldn’t elaborate on the app development tool, as it hasn’t yet been publicly released — but she said that “our largest customers use it already.”
In conclusion, it remains to be seen whether Writer’s knowledge graph approach to RAG can gain the kind of momentum that “traditional” RAG with vector databases already has. But it’s certainly an opportunity for Writer to differentiate, and perhaps an opportunity for graph database companies to explore too.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)