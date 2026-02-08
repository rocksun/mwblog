The retail AI protocol standards war is heating up.

[Google](https://cloud.google.com/?utm_content=inline+mention) has unveiled a new open standard, the [Universal Commerce Protocol (UCP)](https://ucp.dev/), under the Apache 2 open source license.

Google’s goal is for UCP to transform AI-driven product discovery into frictionless, instant purchases across its Search and Gemini software stack. Framed as core plumbing for “agentic commerce,” [UCP is designed to enable AI agents](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/), retail platforms and payment providers to transact without the custom, one-off integrations that currently fragment online shopping.

At the [National Retail Federation (NRF) conference](https://nrfbigshow.nrf.com/) in Manhattan, Google introduced UCP as an open, extensible protocol that establishes a common language for agents and commerce systems across the whole shopping journey, from discovery to post‑purchase support.

In its initial deployment, Google said UCP will soon power a native checkout flow for eligible product listings in AI mode in Search and in the [Gemini app](https://thenewstack.io/googles-new-gemini-3-flash-rivals-frontier-models-at-a-fraction-of-the-cost/), initially for U.S.-based retailers.

## The New Frictionless Shopping Flow With UCP

This is far from being just a Google play. Google says UCP has been co-developed and endorsed by more than 20 companies across retail and payments, including Shopify, which [played a big role in developing the protocol](https://www.shopify.com/news/ai-commerce-at-scale), along with Etsy, Wayfair, Target, Walmart, Visa and others.

The new flow lets users move from a conversational query (e.g., asking Gemini to find a lightweight carry-on suitcase) straight to purchase within the same interface, using stored payment and shipping details via Google Pay, with PayPal support “coming soon.”

Google positions this as a way to cut cart abandonment while keeping retailers in control as the merchant of record, including ownership of customer data and relationships.

Walmart, for one, is all in. In a statement, [John Furner](https://www.linkedin.com/in/furner/), president and CEO of Walmart, said, “The transition from traditional web or app search to agent-led commerce represents the [next great evolution in retail](https://corporate.walmart.com/news/2026/01/11/walmart-and-google-turn-ai-discovery-into-effortless-shopping-experiences). We aren’t just watching the shift, we are driving it.”

Shopify, [which has published its own technical account of the protocol](https://www.shopify.com/news/ai-commerce-at-scale), describes UCP as enabling any AI agent to transact with any merchant on [its platform](https://thenewstack.io/shopify-announces-biannual-product-and-dev-tool-rollouts/). It does this by discovering and invoking merchant‑defined capabilities instead of relying on tightly coupled integrations.

## UCP as a Modular Standard for Merchant Capabilities

So, much for the business side, technically UCP is presented as a modular, extensible standard that merchants can use to declare the capabilities they support (such as checkout, returns or loyalty) and lets agents dynamically discover and negotiate those capabilities. Rather than wiring bespoke APIs for each agent or platform, UCP defines how agents, apps, businesses and payment providers authenticate, exchange capabilities and execute transactions consistently.

UCP does this by sitting above the [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)‘s [Agent2Agent (A2A)](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/) and Anthropic’s [Model Context Protocol (MCP)](https://thenewstack.io/what-is-mcp-game-changer-or-just-more-hype/) in the stack; it standardizes the commerce workflow itself. At the same time, [A2A](https://thenewstack.io/most-developers-call-ai-data-with-apis-and-a2a/) handles agent-to-agent messaging, while MCP focuses on how models access tools and data.

Thus, UCP uses A2A and MCP rather than replacing them, providing agents with a consistent way to execute cart, checkout and post-purchase flows across surfaces. In short, UCP can treat A2A as a transport and coordination layer between agents, and [MCP](https://thenewstack.io/goodbye-plugins-mcp-is-becoming-the-universal-interface-for-ai/) as the mechanism agents use to pull the commerce data they need to drive UCP workflows.

## UCP’s Technical Architecture and Web Standards

Under the hood, UCP implementations rely on familiar web standards such as OAuth 2.0 for account‑linked checkout, Representational State Transfer (REST) endpoints for session creation and completion and tokenized payments to secure card data. If you’ve worked on retail software this decade, you know the drill. UCP e-commerce workflows can be implemented over REST, MCP or A2A.

Endorsements from large online and big‑box retailers provide Google with early distribution for the standard. But the company is also courting a long tail of developers. It is doing so through an open source governance model and an open specification. Developers are encouraged to experiment with capabilities such as checkout, embedded custom flows and post‑purchase updates, and to participate through [UCP GitHub discussions and pull requests](https://github.com/Universal-Commerce-Protocol/ucp).

In the short term, for retailers to use Google’s frontend, merchants must have an active [Google Merchant Center](https://merchants.google.com/) account and an eligible product feed before participating in UCP-powered checkout. Once approved, merchants are asked to implement a small set of core REST endpoints to create, update and complete checkout sessions, with optional embedded checkout for more complex or highly customized user experiences.

Retailers can choose between guest checkout, which requires no additional identity verification, and account‑linked checkout, which uses [OAuth 2.0](https://thenewstack.io/oauth-2-0-a-standard-in-name-only/) to sync profiles and order history between their systems and participating agents. Order status changes are pushed back to agents via webhooks, enabling post‑purchase support scenarios such as tracking, returns and subscription management to flow through the same protocol.

## UCP vs. Agent Payments Protocol

Google also has another e-commerce AI protocol: the [Agent Payments Protocol (AP2)](https://ap2-protocol.org/). The difference is that UCP is the full commerce workflow layer, while AP2 is the payment authorization layer that UCP can plug into. UCP orchestrates the entire shopping journey, while AP2 focuses narrowly on how agents initiate, prove and settle payments.

The UCP launch comes as Google pushes further into AI-led conversational commerce, bundling the protocol with new tools such as “Business Agent,” which lets brands embed their own voice and policies into agentic shopping experiences on Google platforms. [Google Cloud has also framed the move as part of a broader “agentic commerce” strategy](https://cloud.google.com/transform/a-new-era-agentic-commerce-retail-ai). Google is betting that standardized, interoperable protocols will be necessary as retailers deploy their own agents alongside consumer AIs from different vendors.

## The Competitive Landscape for AI Commerce Protocols

Of course, Google isn’t the only company making that bet. Its competitors include [OpenAI and Stripe’s Agentic Commerce Protocol (ACP)](https://developers.openai.com/commerce/) with [ChatGPT’s Instant Checkout](https://chatgpt.com/merchants/). Amazon, of course, is a de facto competitor through its tightly coupled, Amazon‑only, closed-system agentic shopping and payments infrastructure.

Which one will win? It’s too early to say. Still, the combination of Google Ads (which captures roughly 39%-40% of all digital ad spend), significant online retailer partnerships and open source is potent. For the first time in ages, Amazon, the 800-pound gorilla of retail, may be facing a true challenger in the Google UCP alliance.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)