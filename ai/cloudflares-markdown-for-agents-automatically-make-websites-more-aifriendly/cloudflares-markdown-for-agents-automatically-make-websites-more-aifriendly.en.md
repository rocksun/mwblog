[Cloudflare](https://www.cloudflare.com/), the well-regarded security and Content Delivery Network company, has launched a new feature called “[Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/)” that automatically converts web pages from HTML to Markdown whenever AI agents request them — cutting token usage by as much as 80 percent.

Why? Can’t large language models (LLMs) read HTML? Of course they can, but from a model’s perspective, HTML is expensive noise.

A typical webpage includes HTML formatting like divs, as well as scripts and other payloads, which all become tokens the model must then “pay” to read. LLMs couldn’t care less about this markup around the text. In the end, this only burns extra tokens.  

How bad is it? Cloudflare’s own blog post announcing this news, when rendered as HTML, would weigh in at 16,180 tokens. In Markdown, this would only be 3,150 tokens. That’s a 80% saving in token usage. This is a real savings in inference costs. 

## From HTML to Markdown

Cloudflare handles this by real‑time HTML‑to‑Markdown conversion at the edge for any site that enables Markdown for Agents. When a client includes an `Accept: text/markdown header`, [Cloudflare fetches the original HTML from the origin, converts it to Markdown,](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) and serves the transformed content instead of the full web page markup. The company says popular coding agents such as [Claude Code](https://code.claude.com/docs/en/overview) and [OpenCode](https://opencode.ai/) already send these headers, which means many existing AI tools can immediately take advantage of the feature.

To make the content more machine‑friendly, Cloudflare adds an `x-markdown-tokens` response header that exposes the token count, allowing agents to determine whether a document fits within their context window or must be chunked. Converted responses also include a `content-signal` header (`ai-train=yes, search=yes, ai-input=yes`), indicating that the publisher allows AI training, search indexing, and agentic use by default.

Cloudflare says future versions will let site owners customize these content‑signal policies beyond the current defaults.

![](https://cdn.thenewstack.io/media/2026/02/698c144a-cloudflare-markdown-headers.png)

Cloudlare’s response to a Markdown request (credit: Cloudflare).

Markdown for Agents relies on standard HTTP content negotiation, using the Accept header to distinguish human traffic from AI crawlers or other text-only clients. An AI agent can request Markdown by sending `Accept: text/markdown` (often alongside text/html), while regular browser visits continue to receive the normal HTML page. Cloudflare’s edge then performs the conversion “on the fly,” without requiring any changes to site templates, CMS setups, or separate Markdown endpoints.

## Getting started

Cloudflare customers on Pro and Business plans can flip the feature on from the AI Crawl Control section of the Cloudflare dashboard, where Markdown for Agents appears as a dedicated toggle. The same capability is available through the Cloudflare API.

For SaaS providers using [Cloudflare for SaaS](https://www.cloudflare.com/saas/), Markdown conversion can be turned on for all custom hostnames via a dashboard “Quick Actions” switch, or selectively enabled per hostname using custom metadata and configuration.

Cloudflare frames Markdown as a de facto lingua franca for AI agents. Cloudflare is far from the only company to have spotted the advantages of using Markdown for agents and ML. 

## Markdown Alternate

For example, [Joost de Valk](https://www.linkedin.com/in/jdevalk/), a Dutch Internet entrepreneur and [WordPress](https://wordpress.org/) developer, has a WordPress plugin, [Markdown Alternate](https://github.com/progressplanner/markdown-alternate), that also works with agents. He writes that his approach and Cloudflare can work together. “A WordPress site could [use Markdown Alternate for rich, WordPress-aware markdown with dedicated URLs](https://joost.blog/markdown-alternate/) and full metadata, while Cloudflare’s feature provides a baseline for every other site on their network. The plugin gives you control and depth; Cloudflare gives you breadth and zero effort.”

There are also more directly competitive programs, like [Fasterize EdgeSEO (Markdown for AI bots)](https://www.fasterize.com/en/blog/ai-bots-seo-why-converting-your-html-pages-to-markdown-could-change-the-game/). This is an edge service that dynamically converts HTML pages to Markdown for known AI bots, without separate .md URLs.​ Another Cloudflare rival in this space is [Firecrawl](https://www.firecrawl.dev/). This is a commercial “web data API for AI” that crawls, scrapes, and normalizes sites for LLM use.

For teams building AI-powered workflows that consume web content, some form of HTML-to-Markdown conversion is quickly becoming a necessity. Cloudflare’s edge-native approach lowers the barrier to entry: site owners flip a switch and every page becomes agent-ready.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)