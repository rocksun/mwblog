One of the most quoted business mantras today states that if a company wants to be successful, *data is everything*. This has been repeated for decades, but with the furious expansion and broad use of AI and AI agents, it may no longer be true.

Instead, companies are learning every day that while data *is* still important, the *context* of that data may be even more critical when using AI.

So, what changed?

As AI gained steam, unintended consequences started throwing wrenches into the works, including the vexing problem of “context rot,” which is when giant pools of critical data are amassed for use with AI. And for enterprises and data scientists, this context rot has been causing major challenges.

## What is “context rot?”

It turns out that sometimes you *can* have too much of a good thing, particularly when bringing huge amounts of new data into AI agents and [Large Language Models](https://thenewstack.io/llm/) (LLMs).

The problem is that as more fresh data is added, it can be at odds with the older data already there, diluting the results, introducing conflicting context, and causing agents and LLMs to become confused and lethargic. This context rot spoils the delicate brew that yields quality, trusted AI results. [Context relevance turns out to be central](https://www.elastic.co/search-labs/blog/context-engineering-relevance-ai-agents-elasticsearch) to successfully using massive pools of data with AI, agentic search, and hybrid search.

Because new data is brought in without removing out-of-date data, the LLMs processing it reach a saturation point when their “attention budgets” are exhausted. They become overloaded and simply cannot process every new piece of data they are receiving. The models then lose focus and derail their own reasoning, which defeats the strengths and speed of AI. The practice of context engineering was born from these needs to help enterprises learn to manage a model’s limited attention.

For business users, this serious disruption delivers a halting, growing mess within their critical business data.

## How the problem of context rot surfaces when enterprises use AI

When context rot causes these problems in a company’s work with AI and LLMs, they will see and experience them in several notable ways, [Abhimanyu Anand](https://www.linkedin.com/in/abhimanyu-anand), a senior data scientist at [**Elastic**](https://www.elastic.co/), an open-source AI search platform vendor, tells *The New Stack*.

“One is where your AI agent or your system falls into a loop, and you have clashing context,” Anand says. “The agent might establish that as a ground and then keep trying to get to an answer. But maybe it does not have relevant information, so it tries to make more tool calls to fetch more relevant documents.”

For the company, that manifests as unwanted delays, as the AI agent or LLM takes longer to answer a question because it is still searching for the right answer, he says.

> After trying for maybe 10 minutes, the agent is not able to find the right answer, but since it gathered so much context, it may hallucinate and provide you with a wrong answer.”

The problems spiral from there.

“After trying for maybe 10 minutes, the agent is not able to find the right answer, but since it gathered so much context, it may hallucinate and provide you with a wrong answer,” which is a confounding result, he says.

“The LLMs, even the best of them, have been trained by different companies, but they have not yet been trained on one million or 10 million pieces of data. So, what we see is if your agent or your LLM has a really large context, it hallucinates a lot, and its reasoning capabilities go down.”

With more tokens comes more data dilution and the dreaded context rot, says Anand.

## How to fix context rot

To discover and monitor these issues, enterprises and IT administrators must track critical data performance metrics for their applications and LLMs to get to the roots of the problems, Anand says.

Those metrics can include how much time it takes to generate a response, how many tokens are consumed, and other factors. Tokens in AI and LLM data are entities that represent words or other content and are split into chunks. Those chunks, or tokens, are then identified by multi-digit numbers, which are then analyzed and processed by AI and the LLMs.

“Having a good evaluation setup with the right metrics is the best way to get the first signals of something going wrong,” says Anand. “Agents and other applications that are built on top of LLMs, their performance in terms of accuracy and reasoning ability degrade as you feed in more and more data.”

For enterprises working with AI and LLMs, they want the best and most relevant context available, including documents, tools, external artifacts, and other sources, says Anand.  
“This is where solutions like Elastic can really help because we have features that are built around fetching the most relevant context from unstructured data,” he says.

Elastic’s platforms include a full range of tools to help solve context rot challenges, including its Elasticsearch distributed search and analytics engine and distributed vector database where embeddings can be stored; its [Elastic Agent Builder](https://www.elastic.co/docs/explore-analyze/ai-features/elastic-agent-builder) framework, which is a layer in [Elasticsearch](https://www.elastic.co/elasticsearch) for using structured, unstructured and vector data; and a vector store, that allows enterprises to ingest data and then retrieve the most relevant context. Vectors are arrays of numbers, while embeddings are vectors that represent words, sentences, images, videos, and other real-world objects.

Also helping to solve context rot issues are [Elastic’s built-in observability platform](https://www.elastic.co/observability), which allows administrators to view and monitor how AI agents, LLMs and more are performing; its Elastic Learned Sparse EncodeR ([ELSER](https://www.elastic.co/docs/explore-analyze/machine-learning/nlp/ml-nlp-elser)) that enables semantic search to retrieve more relevant search results based on contextual meaning rather than exact keyword matches; and its [JINA AI](https://ir.elastic.co/news/news-details/2025/Elastic-Completes-Acquisition-of-Jina-AI-a-Leader-in-Frontier-Models-for-Multimodal-and-Multilingual-Search/default.aspx) multilingual and multimodal embedding model that is used for processing images and texts into vector formats.

“That is a comprehensive package around the different things that you can do with Elastic,” says Anand. “It is hard to start from scratch and build things to do this.”

## Context rot requires enterprises to constantly fight back: Analyst

[James Kobielus](https://www.linkedin.com/in/jameskobielus/), research director and principal analyst at Franconia Research, tells *The New Stack* that enterprises must wage a battle against context rot to ensure they use the most accurate and up-to-date data while purging old and invalid data for their agentic AI and LLM operations. The business risks and impacts are even more severe when enterprises are using agentic AI systems, he says.

> “Unless nipped in the bud through strong governance in the LLMOps pipeline context, rot can trigger a vicious cycle of diminishing model validity.”

“Unless nipped in the bud through strong governance in the LLMOps pipeline context, rot can trigger a vicious cycle of diminishing model validity,” says Kobielus. “If the context window driving LLM-mediated conversation becomes polluted with false, obsolete, or irrelevant context, the end user, without their knowledge, may be mistargeted, misled, and otherwise mistreated by a deployed AI application.”

This model drift and decay from context rot “is a form of technical debt that is intrinsic to any deployed LLM, foundation model, or other AI model,” says Kobielus. “It can silently undermine the continued accuracy and effectiveness of any model, no matter how well-trained upfront.”

Reducing the susceptibility of an LLMOps practice to context rot requires some core governance practices, according to Kobielus. “That includes ensuring that inaccurate, conflicting, outdated, and irrelevant data and metadata are purged from a company’s knowledge base before the bad data is used to train an LLM reference within a retrieval-augmented generation (RAG) workflow,” he says.

For enterprises experiencing these problems, it is critical to find a vendor that focuses on solving them, says Kobielus.

“I like Elastic’s comprehensive approach to boosting context quality,” he says. “Within a RAG context, it comes down to boosting the value of context-data search and query across disparate and dynamic knowledge bases. Their features address the flexibility that LLM practitioners need in this regard, especially such features as temporal filtering, metadata boosting, data-chunk breakdown optimization, and calibration of retrieval volumes in order to optimize fact retrieval within token budgets and model windows.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/07/00ef81b0-cropped-0a249176-todd-r.-weiss-headshot-2-600x600.jpg)

Todd R. Weiss has been covering technology beats since 2000, first as a staff writer for Computerworld and eWEEK, and later as a freelancer for The New Stack, MSSP Alert, Computerworld, TechRepublic, CIO.com, eWEEK, Data Center Knowledge, IT Pro Today,...

Read more from Todd R. Weiss](https://thenewstack.io/author/todd-r-weiss/)