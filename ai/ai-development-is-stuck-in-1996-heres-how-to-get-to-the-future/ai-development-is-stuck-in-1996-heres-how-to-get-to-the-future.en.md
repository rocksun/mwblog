A funny thing is happening on the way to the AI future. We’re getting bogged down in the same old problems that have plagued us for decades. You’d think with all the talk about large language models (LLMs) and the promise of a brave new world, we’d have it figured out. But the truth is, the more things change, the more they stay the same. We’re still grappling with the basics, like choosing the right tools and making sure our systems can talk to each other.

The AI landscape is a lot like the early days of the internet. Back in 1996, building a website was a painful, manual process, filled with hard-coded HTML and clunky CGI-BIN scripts to handle things as simple as support document submissions. There was no CSS until the end of that year. There were no integrated frameworks or stacks to make the process easier. Everything was a puzzle you had to solve from scratch.

Today, we have [stacks like MEAN](https://thenewstack.io/the-evolution-of-the-ai-stack-from-foundations-to-agents/) (MongoDB, [Express.js](https://thenewstack.io/a-showdown-between-express-js-and-fastify-web-app-frameworks/), [Angular](https://thenewstack.io/angular-vs-react-how-to-choose-the-right-framework-for-you/), [Node.js](https://thenewstack.io/node-js-24-your-next-big-frontend-upgrade/)) that make web development a breeze. And we’re seeing a similar evolution in AI development, specifically with [retrieval-augmented generation (RAG)](https://thenewstack.io/no-mcp-hasnt-killed-rag-in-fact-theyre-complementary/) and [AI agents](https://thenewstack.io/23-of-devs-regularly-use-ai-agents-per-stack-overflow-survey/).

## The AI Adoption Curve and the Rise of RAG

According to a joint [2025 report from the World Economic Forum and Accenture](https://reports.weforum.org/docs/WEF_Transforming_Consumer_Industries_in_the_Age_of_AI_2025.pdf), 70% of organizations are in the “experimentation and pilot” phase of the AI adoption curve, running multiple AI experiments that are often disconnected from their core business strategy. A much smaller group of leaders, about 10-15%, have already started to see measurable value by deploying AI at scale in specific business domains like marketing or customer service. The good news is that early AI adopters are already seeing benefits, with some experiencing 18% higher revenue growth since 2019. The most successful companies — those classified as “AI future-built” — are achieving 50% higher revenue growth and 60% higher total shareholder return over a three-year average.

In 2024, the primary architectural approach for generative AI in the enterprise has been RAG. The [use of RAG has grown](https://menlovc.com/2024-the-state-of-generative-ai-in-the-enterprise/) 1.6 times from 2023 to 2024. While prompt engineering was the primary approach in 2023, its usage has plummeted. Meanwhile, the market for RAG is projected to grow to an astounding $74.5 billion by 2034 according to market.us, with a compound annual growth rate of 49.9%.

## The Agentic Turn and Its Challenges

While RAG is popular, AI agents are beginning to emerge as a new approach. A December 2024 [survey from LangChain](https://www.langchain.com/stateofaiagents) found that over half of companies (51.1%) have agents in production, and an even larger percentage (78.1%) are actively developing an agent with plans to deploy it. Agents are best suited for tasks like research and summarization (58.2%), personal assistance (53.5%) and customer service (45.8%).

But here’s the kicker: Building agents is hard. It’s a lot like the early days of web development. You have a dizzying array of choices, and the wrong one can send you down a rabbit hole of complexity and frustration. Just a few of the choices you need to make include:

* **Choosing a framework.** Do you go with a vendor-independent one like LangChain, LlamaIndex or CrewAI, or a vendor-specific one like Azure AI Foundry Agent Service?
* **Choosing an LLM and where to host it.** The options are vast, with players like OpenAI, Anthropic, Google and Meta all competing for market share. Enterprise [spend on foundation model APIs](https://menlovc.com/perspective/2025-mid-year-llm-market-update/) has more than doubled in the first six months of 2025 compared to all of 2024. When it comes to switching LLMs, the biggest triggers are performance (61%) and cost of ownership (36%).
* **Choosing a vector database.** This is another critical decision. As of June 2024, PostgreSQL and MongoDB were the top two [most frequently used vector databases](https://retool.com/blog/state-of-ai-h1-2024), at 21.3% and 21.1% usage, respectively.

## The Unseen Complexities: Vectors and Embeddings

Even after you’ve made these choices, you encounter the nuances of RAG and agentic development. The process of converting unstructured data like text, images or audio into a numerical representation called a vector is fraught with challenges. It’s a complicated process, and the choices you make can affect storage footprint and retrieval quality. You have to consider things like:

* **Chunk size**: How big are the pieces of content you embed?
* **Similarity function**: How do you measure the closeness of two vectors?
* **Dimensions**: How many vectors does your embedding model output?
* **Quantization**: Do you store vectors as floats, integers or binary arrays?
* **Reranking**: How do you order the retrieved text?

## The Path Forward

The good news is that we’re already seeing the kind of innovation that made web development so much easier. MongoDB, for example, is making the complex process of RAG easier by helping to manage some of the technical details. Specifically, it has introduced features that address chunking, dimensionality, quantization and reranking, simplifying the developer’s work.

Just as we moved from building static HTML pages by hand to using powerful, integrated web stacks, we’re seeing the same shift in AI. The goal is to move from a world where every AI project is a difficult, custom-built effort to one where developers can focus on building agents that deliver real value.

The future is multi-agent systems, where different agents, like an “orchestrator,” a “strategist,” and “utility agents” work together to solve complex problems. The “orchestrator” assigns tasks, the “strategist” turns goals into actionable plans and “utility agents” execute basic tasks autonomously. We’ve seen a demonstration of this in Claude Code, where a team of subagents collaboratively built a movie browsing web application. The orchestrator agent made a plan, and the backend and frontend subagents worked together to execute it, all in a matter of minutes. This collaborative, agentic approach is the next frontier.

The journey from a blank screen to a fully functional AI agent is still a bit bumpy, but the tools are evolving quickly. We’re on the cusp of an era where AI development will be as streamlined and accessible as modern web development. And that, my friends, is a future worth building.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2017/05/89ec47d3-pete-johnson-headshot.jpeg)

Pete Johnson is the AI field CTO at MongoDB, where he regularly discusses topics like large language models, vector search and the Model Context Protocol with analysts, press and customers alike. A 30+ year technology industry veteran, he has held...

Read more from Pete Johnson](https://thenewstack.io/author/petejohnson/)