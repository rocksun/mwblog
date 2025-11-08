The [search landscape](https://thenewstack.io/why-ai-search-platforms-are-gaining-attention/) is shifting. In recent months, Microsoft announced the retirement of the Bing Search API, while Google limited its own API to a maximum of 10 results per query. These moves mark a notable change in the way the web’s dominant search providers view access to their data and who gets to build on it.

For more than a decade, search [APIs](https://thenewstack.io/why-api-first-matters-in-an-ai-driven-world/) like Bing and Google Custom Search have been part of the web’s plumbing. Developers have used them to retrieve web results, images and news without maintaining their own indexes. Enterprises have embedded them in applications such as customer support, knowledge bases and market intelligence to provide external context. Startups and research teams have used them to collect training data, ground language models or perform competitive analysis without running their own crawlers.

In short, search APIs have offered a simple way to access the open web programmatically, bridging the gap between consumer search and enterprise information retrieval.

## The AI Shift

The emergence of generative AI has changed [what the search infrastructure needs to deliver](https://thenewstack.io/enterprise-ai-search-vs-the-real-needs-of-customer-facing-apps/). With [retrieval-augmented generation (RAG)](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/) becoming central to AI systems, developers now require flexible retrieval layers within the AI pipeline, not just returning links.

Against this backdrop, the timing of Microsoft and Google’s decisions stands out. Microsoft has folded search access into Azure’s AI stack through its Grounding with Bing Search feature for AI agents, while Google continues to reduce external visibility into its own results. Limiting queries to 10 results per call fits with its long-standing goal of minimizing bulk data extraction and automated scraping.

The business thinking is clear: Both companies are steering developers away from large-scale, open retrieval and toward AI-mediated access inside their own ecosystems. Full result sets are expensive to serve and often used by automated systems such as SEO platforms, data-mining tools or research crawlers rather than by interactive users. Restricting APIs helps contain those costs while repositioning web data as a controlled resource for higher-level AI services.

## A Reset, Not a Retreat

This isn’t a collapse of search, but a realignment of control. The open, list-based APIs of the past belong to an era where raw results were the product. In the generative AI era, incumbents are redefining search around answers, grounding and context, tightly coupled with their cloud ecosystems.

But as the large providers step back, new players are moving in. Perplexity and Parallel represent a new generation of search APIs designed for AI workloads. They publish benchmarks, expose APIs openly and emphasize retrieval quality and low latency, the performance characteristics that matter most in RAG and agentic systems. You can read more about the [Perplexity search API here](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api).

Perplexity has also shown that it [outperforms Google on relevance](https://medium.com/@evolutionaihub/whats-new-in-perplexity-s-search-api-that-just-killed-google-s-edge-b95047ada22e) for RAG-style tasks. Not to be outdone, Parallel, founded by Twitter’s former CEO, Parag Agrawal, recently [reported better results](https://x.com/paraga/status/1971650814705127438) than Perplexity, using Perplexity’s own evaluation tool.

## A Hot Market, New Foundations

The search API market is heating up again, this time around AI native infrastructure. Beneath Perplexity and Parallel is a common component: Vespa, the open source engine built for large-scale retrieval, ranking and machine learning inference.

Vespa’s role in these systems reflects a broader shift in architecture: Search infrastructure is now part of the AI stack itself. As models depend more on retrieval, factors such as performance, scalability and the ability to combine [structured and unstructured data](https://thenewstack.io/automating-context-in-structured-data-for-llms/) have become key differentiators.

The incumbents are narrowing access; the innovators are expanding it. Either way, search is once again at the center of how the web is organized, only this time, it’s being rebuilt for AI.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/09/b24ea863-tim-young--541x600.jpg)

Tim Young leads marketing at Vespa.ai, drawing on his technical background to implement data-driven strategies. He began his career in large-scale data management for enterprises like British Telecom, T-Mobile, Shell, British Airways, and Ford. Tim has held key marketing roles...](https://thenewstack.io/author/tim-young/)