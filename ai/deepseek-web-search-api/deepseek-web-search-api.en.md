Not content with challenging the major frontier AI labs with [lower-cost models](https://thenewstack.io/deepseek-flash-pro-benchmark/), Chinese AI company [DeepSeek](https://deepseek.com/) is setting its sights on the search API market.  
  
On Saturday, the company announced it [has opened up](https://api-docs.deepseek.com/updates/#date-2026-10-17) its internally developed search engine to outside developers through two new APIs, [Search and Fetch](https://api-docs.deepseek.com/guides/search/), allowing them to retrieve live web search results and webpage content for use in their own apps and agents.

Both services cost $0.75 per 1,000 successful requests, and developers can use them independently of DeepSeek’s AI models.

The launch also came alongside [DeepSeek-V4.1-Flash-1017](https://api-docs.deepseek.com/news/news261017/), a minor update to the V4.1 Flash model the company released [in September](https://venturebeat.com/technology/deepseek-v4-1-flash-debuts-with-0-003-1m-off-peak-cached-input-rate-and-benchmarks-eclipsing-gpt-5-6-sol-claude-opus-5).

## Why AI agents need web search

Large language models (LLMs) are trained on data collected up to a certain point in time, meaning they can’t always answer questions about recent events, updated documentation, or any other kind of dynamic information. By supporting live web search, models can retrieve current information from the internet, which supplements their responses.

For developers building AI agents, this is particularly important. A coding agent, for example, might need to consult the latest software documentation, investigate a recently disclosed vulnerability, or otherwise check that a particular library has been updated.

Until now, developers using DeepSeek’s models had several ways to provide this functionality. They could connect their applications to third-party search services, or use DeepSeek’s existing search functionality through its model API.

Indeed, when DeepSeek [open-sourced its agent harness in August](https://thenewstack.io/deepseek-harness-open-source-plugins/), it included web search among its capabilities. The Harness supported interchangeable search providers, including [Exa](https://exa.ai/), [Perplexity](https://thenewstack.io/perplexity-agent-api/) and DeepSeek itself. However, accessing DeepSeek’s native search through the Harness required an additional model request, with each search running as a separate call to a DeepSeek model, according to the Harness documentation, introducing extra latency and token costs.

The new APIs are designed to simplify that process. Developers can now call DeepSeek’s Search endpoint directly to retrieve ranked web results, including titles, URLs, snippets and summaries, while the Fetch endpoint retrieves the contents of individual webpages in Markdown format.

> “Neither requires a separate model request, meaning developers can integrate DeepSeek’s search capabilities into applications powered by competing AI models, too.”

Neither requires a separate model request, meaning developers can integrate DeepSeek’s search capabilities into applications powered by competing AI models, too.

## DeepSeek develops an in-house engine

For much of the past two years, DeepSeek has relied on outside providers to power web search, even as it was building its own.

For context, in March 2025, Chinese business publication National Business Daily [reported](https://www.nbd.com.cn/articles/2025-03-07/3779901.html) that DeepSeek had integrated the search API of [Bocha](https://bochaai.com/), a Chinese AI search startup based in Hangzhou. Bocha’s CTO, Weng Rouying, noted that DeepSeek had been using its service prior to the chatbot’s surge in popularity earlier that year.

DeepSeek’s own [February 2025 privacy policy](https://web.archive.org/web/20261004083012/https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy-2025-02-14.html), meanwhile, also acknowledged its reliance on third-party search services, naming Microsoft’s Bing as an example of an external API provider.

> “Behind the scenes, the company has also been laying the groundwork for its own search infrastructure.”

Behind the scenes, the company has also been laying the groundwork for its own search infrastructure. In January this year, Bloomberg [reported](https://www.bloomberg.com/news/articles/2026-01-29/deepseek-sets-sights-on-ai-search-and-agents-job-postings-show?utm_source=chatgpt.com) that DeepSeek was recruiting engineers to build a multilingual AI search engine, according to job ads listed by the company. The planned capabilities reportedly extended beyond text searches to include images and audio.

Fast-forward some nine months, and the company says its internally developed search engine, dubbed DeepSeek Search, already handles hundreds of millions of requests daily, and maintains an index containing hundreds of billions of webpages.

According to its [October 17 changelog](https://api-docs.deepseek.com/updates/#date-2026-10-17), the engine supports multilingual searches and uses filtering mechanisms designed to identify search spam, low-quality AI-generated material, and attempts to manipulate search rankings.

DeepSeek has disclosed relatively little about the underlying architecture, or how it builds and maintains its index. It’s also not clear whether the company has entirely replaced its external search suppliers across the board.

## A growing market for AI search

Building a search engine is no trivial undertaking. It requires the infrastructure to crawl webpages, maintain an index of their contents and rank results, while continuously updating that information as the web changes. For years, that meant developers who wanted raw search results for their applications largely turned to Google and Microsoft, the two companies with web-scale indexes of their own.

Now, however, a growing number of companies are investing in their own search infrastructure, increasingly with AI applications and agents squarely in mind. [Brave](https://brave.com/), for example, operates [an independent index](https://brave.com/blog/most-powerful-search-api-for-ai/) of more than 40 billion webpages, which it says is maintained through its own crawler and other discovery mechanisms. AI search company Exa, meanwhile, has also [developed its own crawling and indexing infrastructure](https://exa.ai/blog/how-to-build-nextgen-search).

Perplexity has similarly [invested in proprietary search infrastructure](https://thenewstack.io/perplexity-agent-api/), including building its own [crawling and indexing systems](https://www.perplexity.ai/en-GB/hub/blog/architecting-and-evaluating-an-ai-first-search-api). Another competitor, [Parallel](https://parallel.ai/products/search), says it has built its search infrastructure from the ground up, including the crawling, indexing, query processing and ranking components.

Cloudflare is also entering the market from a different angle. Earlier this month, [the company launched a Web Search API](https://blog.cloudflare.com/introducing-web-search-api/) through its AI Gateway, allowing developers to access search results from serveral providers through a single interface. The service, currently in beta, [uses Ceramic as its default provider](https://developers.cloudflare.com/web-search/providers/) and charges customers at each provider’s published API rates, without additional markup.

> “DeepSeek, for its part, is competing aggressively against the incumbents on price.”

DeepSeek, for its part, is competing aggressively against the incumbents on price, although it’s not strictly the cheapest option available. [Ceramic.ai](https://www.ceramic.ai/), which provides keyword-based web search for AI agents, [charges $0.25 per 1,000 queries](https://www.ceramic.ai/pricing) on its pay-as-you-go plan.

Still, DeepSeek’s $0.75 per 1,000 successful searches compares favorably with many others, including [Parallel’s Turbo and Fast search services](https://parallel.ai/pricing) and [Perplexity’s Fast Search API](https://docs.perplexity.ai/docs/getting-started/pricing), both of which charge $1 per 1,000 searches. Meanwhile, Exa [charges $4](https://exa.ai/pricing#endpoint-pricing) per 1,000 Instant Search requests, while Brave charges [$5 per 1,000 searches](https://brave.com/search/api/). Other notable players include [Tavily](https://www.tavily.com/), a search API provider for AI agents that European AI infrastructure company [Nebius acquired in February](https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform). Tavily [charges](https://www.tavily.com/pricing) $8 per 1,000 basic searches on its pay-as-you-go plan.

It’s worth noting that the various services differ in terms of retrieval capabilities, result limits and performance, so the prices aren’t necessarily entirely comparable. But they provide some useful benchmarks for DeepSeek’s move into the search infrastructure space.

The emergence of these alternatives also comes as Google and Microsoft have withdrawn longstanding search API offerings. Microsoft retired its Bing Search APIs in August 2025, while Google has [closed its Custom Search JSON API to new customers](https://developers.google.com/custom-search/v1/overview), with existing users required to migrate by January 1, 2027. Both companies continue to provide search functionality through their respective AI platforms, including [Grounding with Google Search for Gemini](https://ai.google.dev/gemini-api/docs/google-search) and [Grounding with Bing Search](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/bing-tools?pivots=python) for Microsoft Foundry agents. These services allow AI models operating within their respective platforms to retrieve web information and generate answers with citations.

Standalone APIs such as DeepSeek’s give developers direct access to search results, which they can use with AI models and applications of their choosing.

## Developer reaction and the fine print

The announcement has sparked considerable discussion among developers about pricing and whether the new APIs offer much beyond existing search integrations. On Reddit, one user welcomed the cost in particular. “I don’t think any other search provider comes close to the price that DeepSeek is offering,” they [write](https://www.reddit.com/r/DeepSeek/comments/1x8d4u2/comment/phdnk6n/).

Others questioned what the announcement would ultimately change for users already accessing web search through third-party tools. One Reddit user [notes that they are already using](https://www.reddit.com/r/DeepSeek/comments/1x8d4u2/comment/phcazlt/) DeepSeek with the [Hermes AI agent](https://thenewstack.io/openclaw-hermes-agent-harness/), which could search the web. Another user responded that those who had already configured their own search tools might see little immediate benefit from the new APIs.

A similar discussion emerged [on Hacker News](https://news.ycombinator.com/item?id=50138531), where one developer [questions](https://news.ycombinator.com/item?id=50139399) the need for paid search APIs when free, self-hosted alternatives such as [SearXNG](https://github.com/searxng/searxng) were available. Another commenter argues that businesses [have additional requirements](https://news.ycombinator.com/item?id=50139481), citing “reliable latency, data processing guarantees” and the potential risk of exposing sensitive company information through search queries.

For businesses weighing DeepSeek’s APIs, that last point carries an extra dimension. DeepSeek’s [privacy policy](https://github.com/OpenTermsArchive/genai-eu-versions/blob/main/DeepSeek/Privacy%20Policy.md) states that it collects, processes and stores personal data in China, and that it generally keeps user inputs for as long as an account remains open. The Search and Fetch documentation, however, doesn’t say how long search queries specifically are retained.

The discussions highlight the differing needs of individual developers and businesses, particularly when it comes to cost, reliability, and handling large numbers of requests. And while DeepSeek’s pricing is certainly competitive, there are some practical restrictions worth considering.

According to its [API documentation](https://api-docs.deepseek.com/guides/search/), Search and Fetch requests are each capped at five per second per account, although individual searches can return up to 50 results without increasing the request price. DeepSeek also only bills for requests that return results, so failed calls, empty searches, and timeouts are free.

DeepSeek is temporarily waiving Search and Fetch charges for server-side tool calls made through DeepSeek Harness, Claude Code, and Codex when using its API. That is very much a temporary arrangement, however, one that ends on October 31, when the standard per-request charges take effect. Direct calls to the standalone APIs are already billable, according to DeepSeek’s announcement.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)