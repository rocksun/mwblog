Everyone knows the open-weight model pitch by now: companies can download the weights, customize them, run them on infrastructure of their choosing, and retain far greater control over where their data is processed — often at a much lower cost than using proprietary models.

Moreover, open-weight models are now thought to trail the leading frontier models by [only around four to five months](https://thenewstack.io/open-weight-models-frontier-costs/). Nvidia, the world’s most valuable company, is betting heavily on that future. In early September, [it agreed to acquire Hugging Face](https://thenewstack.io/nvidia-acquires-hugging-face/) — the sprawling “GitHub for AI” that hosts more than three million models — for $12.9 billion, while pledging to keep the platform open to different models, clouds and computing providers. And on Thursday, Nvidia detailed how [Nvidia is using its own open-weight Nemotron model](https://thenewstack.io/ai-factories-are-among-the-most-complex-systems-ever-built-nvidia-and-palantir-turn-nvidias-supply-chain-into-a-proving-ground-for-sovereign-ai/) to manage its vast global supply chain in partnership with Palantir.

That power also comes with serious security questions. OpenAI president Greg Brockman recently warned that increasingly capable open-weight models — [pointing specifically to China’s GLM-5.3](https://thenewstack.io/openai-open-weight-glm-5-3/) — could “significantly accelerate the threat landscape” as models with advanced cyber capabilities become freely downloadable and modifiable.

But for businesses accessing those models through third-party services, there is another concern closer to home: where their own data goes when they use those models, particularly when the model originated in China.

## China and the open-weight factor

Hugging Face data from February showed models from Chinese developers [accounted for 41% of downloads](https://thenewstack.io/china-leads-open-ai-models/) in the preceding 12 months, ahead of the US at 36.5%. Over on [OpenRouter](https://openrouter.ai/), meanwhile, open-weight models now account for around 60% of tokens consumed by US-originating requests, with the company noting that Chinese models constitute the majority.

![OpenRouter: Share of monthly tokens (Sept. '25 - Aug. '26)](https://cdn.thenewstack.io/media/2026/09/f0933dd1-openroutergraph-1024x576.png)

*OpenRouter: Share of monthly tokens (Sept. ’25 – Aug. ’26)* *— US and EU*

And that’s why OpenRouter is now giving companies a way to put a geographic fence around that traffic. The AI model marketplace has officially launched [US in-region routing](https://openrouter.ai/docs/guides/features/in-region-routing) into general availability for business and enterprise customers, promising that requests sent through its US endpoint are decrypted, processed and served entirely inside the country — or rejected if that can’t be done.

The feature itself had been quietly available in some form before now, with OpenRouter updating its documentation in [early August](https://github.com/OpenRouterTeam/docs/commit/40ca0ef2ec9d1f51af3d3f54841b8f548f5d1780) to say US in-region routing was available to enterprise customers by request. It’s also worth noting that this is in addition to European in-region routing, which it says has been available since October 2025.

Started in early 2023 by former OpenSea CTO [Alex Atallah](https://www.linkedin.com/in/alexatallah/), OpenRouter serves as an interface to the crowded AI model market, with developers able to switch between hundreds of models from myriad providers via a single API. Payments giant Stripe recently [announced plans to acquire](https://thenewstack.io/stripe-acquires-openrouter-tokens/) the company in a reported $8 billion deal, while a slew of other companies including Cursor, Ramp, and Meta, are [also building their own model routers](https://thenewstack.io/cursor-ramp-meta-model-router/).

The reason why model routers are such hot property right now is largely down to economics. Developers have traditionally hard-coded applications to send everything to the same model, while a model router can instead [make that choice request by request](https://thenewstack.io/stripe-ramp-openrouter-router/), sending easier jobs to cheaper models while reserving the pricier frontier systems for the work that actually needs them.

That intermediary role is also what makes OpenRouter’s new residency controls possible: it already decides which provider serves each request, and can now restrict that choice to provider endpoints operating in the US.

## Keeping Chinese models inside the US

In a [blog post](https://openrouter.ai/blog/announcements/us-in-region-routing/) announcing the new feature on Wednesday, [Cailee Moberg](https://www.linkedin.com/in/cailee-moberg/), who works on OpenRouter’s product team, notes that while US-developed models from Nvidia and [Thinking Machines](https://thinkingmachines.ai/news/introducing-inkling/) are contributing to the broader open-weight model boom, Chinese models dominate usage and raise tough questions for companies concerned about their data.

> “Models from Chinese labs are still most of the [open-weight model] volume, and procurement approval for those models can be difficult.”

“Models from Chinese labs are still most of the [open-weight model] volume, and procurement approval for those models can be difficult,” Moberg writes.

In its 2026 *[State of AI in the Enterprise](https://www.deloitte.com/uk/en/issues/generative-ai/state-of-ai-in-enterprise.html)* report, Deloitte [concluded](https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html) that sovereign AI was on the rise, noting that 77% of companies “now factor country of origin into their vendor selection,” while nearly 60% construct their AI stacks “primarily with local vendors.”

And this at least partly explains why OpenRouter is now offering in-region routing for US customers. Moberg points to [DeepSeek V4 Pro](https://thenewstack.io/deepseek-flash-pro-benchmark/), [Kimi K3](https://thenewstack.io/kimi-k3-open-weights/) and [GLM 5.2](https://z.ai/blog/glm-5.2) as specific examples. All three are available through US In-Region Routing because Baseten, Fireworks and Azure serve them from US data centers. Companies could already keep these models inside the US by self-hosting them or using a US provider directly; OpenRouter’s new routing gives its own customers that residency guarantee without having to manage those deployments themselves.

OpenRouter [maintains a live list](https://openrouter.ai/models?region=us) of models eligible for US in-region routing, ranging from proprietary frontier models from OpenAI and Anthropic to open-weight models from the major Chinese labs.

“In-Region Routing allows teams with data residency requirements to get the price and performance gains from Chinese open-weight models,” Moberg continues. “When a US or EU provider hosts a model, requests go to that provider and the lab is not involved.”

> “In-Region Routing allows teams with data residency requirements to get the price and performance gains from Chinese open-weight models.”

The technical change happens at the routing layer. With OpenRouter’s standard global endpoint, a request can be served by an eligible provider operating in any region, so even using a model from a US company does not guarantee that the request itself is processed in the US. With *us.openrouter.ai*, the request is decrypted on OpenRouter infrastructure inside the US and the pool of providers is filtered to endpoints OpenRouter has approved as operating there.

If no compliant US provider can serve the requested model, OpenRouter returns a *404 error*. Companies can also enforce the regional restriction through OpenRouter’s Guardrails at the workspace, team or API-key level, while tools that would send prompt data outside the US are disabled on the regional endpoint.

So while none of this ultimately changes where the DeepSeek, Kimi or GLM models are developed, in-region routing alters which copies of those models its US customers can be routed to, and where their prompts are handled along the way.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)