# What Is Semantic Caching?
![Featued image for: What Is Semantic Caching?](https://cdn.thenewstack.io/media/2025/05/c614771a-semantic-caching-2-1024x576.jpg)
API requests to AI providers can rack up quite a bill. Barclay analysts found that a single prompt to OpenAI’s o3-high model resulted in a $3,500 fee, requiring 1,000 more tokens than its predecessor model, according to Business Insider.

Most developers know what [caching](https://thenewstack.io/is-a-database-caching-layer-still-necessary/) is. But semantic caching is the new thing for AI. It’s set to become more relevant as AI costs escalate and developers seek out sleeker designs to avoid pinging AI servers over and over for redundant queries.

“Everyone’s going to be looking at their AI cost structure, latency and performance,” [Randy Reddig](https://www.linkedin.com/in/ydnar/), vice president of technology research and incubation at [Fastly](https://www.fastly.com/), told The New Stack. “OpenAI even recommends you perform some kind of caching on their output.”

The benefits are clear: [A 2024 study](https://arxiv.org/pdf/2411.05276) found that semantic embedding caching can significantly reduce latency and reduce API calls by up to 68.8% across various query categories.

But what exactly is semantic caching, and how do you implement it? Below, we’ll explore semantic caching in the context of [large language models (LLMs)](https://thenewstack.io/llm/) and APIs, its benefits and possible drawbacks, and how it fits into broader AI development practices.

## Semantic Caching Builds On Standard Caching
Caching is the process of storing frequently accessed information to avoid slow load times, reduce server requests and improve user experience. Server-side and browser-side caching are fundamental strategies when designing [web applications and APIs](https://thenewstack.io/why-http-caching-matters-for-apis/).

Semantic caching and your typical web caching are pretty similar. Both access stored data to reduce unnecessary calls. What’s different is that semantic caching stores and retrieves prompts and responses to AI servers, like LLMs from [OpenAI](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/), [Google](https://cloud.google.com/?utm_content=inline+mention) [Gemini](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/), [Anthropic](https://www.anthropic.com/) and others.

How semantic caching works:

- A user sends a chat to an LLM-based AI agent.
- A layer intercepts the request and performs a semantic analysis to determine if the request matches any previously made prompts.
- If the system finds a suitable prompt, it rapidly returns the cached response.
- If no similar prompt exists, it funnels the request to the AI server for processing.
While retrieval-augmented generation (RAG) complements LLM queries with access to external data, semantic caching is unique in that it avoids further lookups altogether by pulling from a database, which could be local or externally stored.

According to Fastly’s Reddig, semantic caching is not much different than how a [content delivery network (CDN)](https://thenewstack.io/the-modern-cdn-means-complex-decisions-for-developers/) or gateway already works. The secret sauce is in the engine that determines semantic sameness.

“Many requests are phrased slightly differently, but their responses should be relatively the same,” says Fastly’s Reddig. For instance, he said, different users often make similar requests, such as comparing coffee types or asking for the best recommendations for a good car for a family of four.

In Fastly’s case, its AI Accelerator parses new requests and compares each against Fastly’s vast vector database of LLM interactions hosted on its distributed, low-latency edge network. It then returns responses with a high confidence level to similar queries to be sent to the client application. Unmatched queries are forwarded to the LLM API.

Other platforms are tackling AI caching, too. For example, [Redis](https://redis.com/?utm_content=inline+mention), the in-memory data store and caching system, [recently launched](https://thenewstack.io/redis-launches-vector-sets-and-a-new-tool-for-semantic-caching-of-llm-responses/) LangCache for caching LLM responses, and a new data type for storing and querying vector embeddings.

## The Results: Lower Cost and Better Performance
To date, AI has required massive amounts of GPU-based processing. According to [McKinsey & Company](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/ai-power-expanding-data-center-capacity-to-meet-growing-demand), AI could triple global data center capacity demand by 2030.

Reddig attributed high costs to inefficient interactions with AI models. When an LLM processes a prompt, it must tokenize the request, along with other context, such as project prompts, files and data pulled from RAG, and send it to an LLM to synthesize and generate a response. Subsequent requests then use this context in-memory and retokenize it with each request.

“The aggregate cost of a prompt is related to the number of tokens, and processing those sequentially over and over ends up consuming a lot,” said Reddig. “For a very long query, or a short query with a ton of context, that’s gonna be a more expensive query to process in terms of cost, CPU, power and time.”

Semantic caching can avoid initiating new LLM calls to an AI server altogether, avoiding heavy CPU demands. By calling upon more local data, you could avoid long wait times and cut round-trip calls, improving throughput.

According to [Fastly’s benchmarks](https://www.businesswire.com/news/home/20241216172993/en/Fastly-AI-Accelerator-Helps-Developers-Unleash-the-Power-of-Generative-AI), semantic cache setups result in 9x faster server response times compared to direct OpenAI server calls. The company says it’s a low-effort migration, too, only requiring application developers to point to a new endpoint to reroute API calls.

## Semantic Caching: Good for AI Agents
Semantic caching is an emerging area, and the exact use cases are still being ironed out. That said, it performs best in use cases that are conversational or prompt-based.

“Natural language input that produces natural language output is a great use case,” said Reddig. Although the same process could support other content types, like video and image, he added.

Semantic caching also shows promise in ultra-specific domains. “If the semantic space is narrow and you’re seeing a lot of common questions or prompts, that’s where this could be very suitable,” he said.

These factors make it a good fit for queries to user-facing AI agents in specific contexts, like retail, customer service or online shopping. In this context, real-time responses matter for customer experience, heightening the need for quality performance.

Responsiveness is also vital for agents working in enterprise contexts. “Agents have a huge dependency on quality data so they can act on accurate, timely and contextually relevant information,” [Archana Kannan](https://www.linkedin.com/in/archkan/), senior vice president of [Slack product at Salesforce](https://api.slack.com/?utm_content=inline+mention), told The New Stack. “The right data and context are the foundation for agents to deliver real value to employees and organizations.”

Others echo that fast, reliable data access is foundational for agentic AI. “Agentic AI demands better context integration, faster feedback loops and scalable orchestration,” [Andre Zayarni](https://www.linkedin.com/in/zayarni), co-founder and CEO of [Qdrant](https://qdrant.tech/), a vector database company, told The New Stack. “AI agents hit bottlenecks when retrieval is slow or context updates lag behind real-time needs.”

Zayarni views semantic caching as a tactic to reduce redundant lookups: “If a similar query was already answered, reuse it instead of recalculating.”

## Part of a Broader Optimization Strategy
Further innovation still needs to happen around semantic caching. One is refining the model to avoid erroneously connecting semantically similar prompts, said Reddig. Although, he added, there are ways to mitigate this with prompt engineering and other safeguards.

Zooming out, semantic caching is just one piece of the puzzle — it alone won’t solve hallucination issues and other inefficiencies. As such, it will take a town (of savvy strategies) to optimize agentic AI.

“Key advancements include GPU-accelerated index building for real-time vector ingestion, semantic caching to reduce redundant lookups and hybrid search models that blend dense vectors, sparse terms and metadata filters,” said Zayarni. He also mentioned using a multiagent system to delegate certain responsibilities to various agents.

Others agree that advancements in data handling and multiagent approaches are necessary to optimize agentic AI. “The most critical advancements will be centered around improvements in data integration, metadata management and multiagent collaboration,” said Salesforce’s Kannan.

“Adopting a multiagentic approach can significantly enhance optimization,” she added. “Teams of specialized ambient agents can collaborate behind the scenes, autonomously handling complex workflows, integrating disparate systems and streamlining multistep processes.”

Arguably, multiagent architectures are very complementary to semantic caching, since a dedicated agent could review user queries to determine semantically similar queries, and hand off deeper elements to other agents to process. This handoff could even behave within intraquery semantic segmentation, as in breaking down parts of a user’s request and routing them separately.

Lastly, there is an argument to be made that LLMs will become cheaper with future model advances and GPU efficiencies, decreasing the need for efficiency savings. But, as Moore’s Law plateaus and inference costs climb, semantic caching is emerging as a helpful method to curtail redundancy.

## Semantic Caching Changes the Game
Like how CDNs became the standard practice for optimizing web performance, Reddig predicted that caching layers between the client and LLM API will become the default for new AI development.

To date, high computational requirements bar small-to-medium companies from competing on a level playing field. But he hopes semantic caching will make AI development cheaper, democratizing access in the same way [TSMC](https://www.tsmc.com/) once did for chip designers by handling costly manufacturing.

As past breakthroughs lowered the bar, semantic caching could have similar ripple effects for emerging markets. As Reddig said, “Usage that wasn’t possible with the pre-existing cost structure now becomes more possible.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)