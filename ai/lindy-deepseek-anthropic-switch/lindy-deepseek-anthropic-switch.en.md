**The biggest blocker to sustainable AI deployment** has emerged as [inference cost](https://thenewstack.io/confronting-ais-next-big-challenge-inference-compute/). GitHub [recently abandoned](https://thenewstack.io/github-copilot-token-billing/) its flat-rate Copilot subscription in favor of usage-based billing, after agentic coding sessions drove costs beyond what a fixed monthly fee could absorb — some subscribers woke up to bills several times higher than they’d been paying. Uber, meanwhile, [burned through its entire 2026 AI budget](https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/) in just four months, largely on Claude Code, leaving its COO questioning whether the returns justified the outlay.

In response to this broader reckoning, the [Linux Foundation launched the Tokenomics Foundation](https://thenewstack.io/tokenomics-foundation/) — backed by Google, Microsoft, IBM, Salesforce, among others — to build open standards around AI token costs, an acknowledgment that enterprises currently have no consistent way to measure or control what they owe.

## Flipping the switch

For companies running AI agents at volume, the economics of frontier models have become almost an existential question.

[Flo Crivello](https://www.linkedin.com/in/florentcrivello/), a former engineer and product lead at Uber, is the founder and CEO of Lindy, a no-code AI agent platform that automates everyday work tasks — from email triage and meeting scheduling to CRM management. Crivello founded Lindy in 2023 as a pivot from Teamflow, a virtual office startup for which he had previously raised [$52 million](https://www.teamflowhq.com/blog/teamflow-raises-35m-series-b) in capital — capital that now backs [Lindy’s development](https://ff.co/flo-crivello-lindy/).

![Lindy](https://cdn.thenewstack.io/media/2026/06/5d9a3984-lindya-1024x729.png)

*Lindy*

Crivello took to social media last week to [announce](https://x.com/Altimor/status/2062389885437366342) that Lindy had switched its entire model infrastructure from Anthropic to DeepSeek.

> “Saves us millions of $ and we’re actually seeing an increase in performance on many core use cases.”

“Pulled the trigger today and switched 100% of Lindy traffic to DeepSeek v4, churning from Anthropic models,” Crivello wrote on X. “Saves us millions of $ and we’re actually seeing an \*increase\* in performance on many core use cases. Transformative for the business.”

In truth, Crivello [had signaled his intentions](https://x.com/Altimor/status/2024166557107311057) some months earlier, [writing on X](https://x.com/Altimor/status/2044108104816832576?s=20) in April that inference was Lindy’s single biggest cost — exceeding payroll — and that open-source models had gone from “not even close” to “at the frontier, for most use cases” in the space of a year. At the time, he said Lindy had come close to making [Kimi K2.5](https://www.kimi.com/ai-models/kimi-k2-5) — a model from Chinese AI company [Moonshot AI](https://www.moonshot.ai/) — its default, before pivoting toward [GLM-5.1](https://z.ai/blog/glm-5.1), developed by Beijing-based lab [Zhipu AI](https://en.wikipedia.org/wiki/Z.ai).

As it turned out, the company settled on [DeepSeek v4](https://deepseek.ai/deepseek-v4), a flagship open-source model from the Chinese AI research company DeepSeek.

Of course, switching from one model provider to another at full production scale is no trivial task. Crivello tells *The New Stack* that the timeline to completion depends on when you start counting — but either way, it was a significant undertaking.

> “We’ve been looking to make this switch and evaluating new OSS models for 6-9 months.”

“We’ve been looking to make this switch and evaluating new OSS models for 6-9 months, and DeepSeek since it was released, about 2 months ago,” Crivello explains.

Notably, the migration proved far more demanding than Crivello initially anticipated — “100x more work than we thought,” as he put it. Evaluations — that is, systematically testing the new model across real-world tasks to verify it could match or exceed what Anthropic’s models had been delivering — were a major part of it.

![](https://cdn.thenewstack.io/media/2026/06/a8724953-1776918947306.jpg)

Flo Crivello, founder & CEO at Lindy

“Lots of work to eval the models, on online evals, offline evals, and tons of ‘vibe evals’,” Crivello says. “[We then did] a gradual rollout for both online evals, and to see the impact on retention; and [then] adapt our prompts to this new model.”

The effort would have been hard to justify on cost savings alone — but the performance results gave Crivello added confidence, particularly in its core use cases, which include email inbox triaging and pre-drafting replies based on the user’s voice.

“And that’s exactly where we’ve seen surprising performance gains with DeepSeek,” Crivello explains, adding that DeepSeek still trails Anthropic on some complex automation tasks.

“It’s still less good than [Sonnet](https://thenewstack.io/claude-sonnet-46-launch/) at ‘workflow automation,’ which is more secondary for us,” he says.

## DeepSeek moment

To understand why Lindy’s switch matters, it helps to understand what DeepSeek has come to represent in the AI industry.

DeepSeek sent shockwaves through Silicon Valley [in January](https://www.forkable.io/i/155825266/the-open-source-ai-debate-deepens-a-sputnik-or-google-moment)[2](https://thenewstack.io/icymi-deepseek-is-an-open-source-success-story/)[025](https://www.forkable.io/i/155825266/the-open-source-ai-debate-deepens-a-sputnik-or-google-moment), when its R1 model matched the performance of leading US frontier models at a fraction of the cost — prompting a brief but dramatic [selloff in Nvidia’s stock](https://www.bbc.co.uk/news/articles/c0qw7z2v1pgo) as investors questioned assumptions about AI’s compute requirements. What followed was a steady stream of releases that kept closing the gap with the frontier realm.

DeepSeek V4, released in [preview in April 2026](https://api-docs.deepseek.com/news/news260424), marked a further step change — and not just on price. [Marcel Salathe](https://www.linkedin.com/in/salathe/), professor at EPFL and co-director of the EPFL AI Center in Switzerland, [noted on LinkedIn](https://www.linkedin.com/posts/salathe_deepseek-v4-for-the-first-time-a-frontier-class-activity-7453409089885429760-zJir/) that v4 represented something more significant from a geopolitical standpoint: For the first time, a frontier-class AI stack exists that is fully Chinese from chip to framework to model. DeepSeek, it seems, [spent months rewriting](https://www.scmp.com/tech/big-tech/article/3351349/huawei-deepseek-strengthen-chinas-ai-self-reliance-collaboration-v4-model) v4 to run on [CANN](https://developer.huawei.com/consumer/en/doc/hiai-guides/introduction-0000001051486804) — Huawei’s equivalent of Nvidia’s CUDA — [reducing its reliance](https://www.reuters.com/technology/chinas-deepseek-returns-with-new-model-year-after-viral-rise-2026-04-24/) on US chip infrastructure.

That geopolitical shift has a direct commercial consequence. As *The New Stack* [previously reported](https://thenewstack.io/disappearing-ai-middle-class/), the arrival of cheaper open-weight models from predominantly Chinese AI labs has split the AI model market into two clusters — ultra-premium frontier models from the likes of OpenAI and Anthropic, and dramatically cheaper open-weight alternatives — with the comfortable middle thinning out. The numbers bear this out: Vercel’s AI Gateway, which routes traffic between apps and AI providers, recorded DeepSeek’s share of token volume [jumping from under 1% to 17%](https://vercel.com/blog/ai-gateway-production-index-june-2026) in a single month in May — while its share of actual spend remained near 1%, a reflection of just how cheaply those tokens are being served.

For companies running agents at volume, such as Lindy, that polarisation has forced a reckoning with which economics to route to. For Lindy’s founder, whose inference bill had grown to exceed payroll, the question really was just a matter of when.

Lindy settled on [Atlas Cloud](https://www.atlascloud.ai/), a US-based inference provider that [hosts DeepSeek v4](https://www.atlascloud.ai/models/deepseek) on American soil — an important detail given that questions around data sovereignty tend to follow Chinese-developed models. Crivello [addressed this directly](https://x.com/Altimor/status/2062565063312199867?s=20) in response to at least [one commenter on X](https://x.com/parenth_/status/2062559294101524603?s=20), noting that the model is hosted in the US by an American provider — and that [Atlas came out ahead](https://x.com/Altimor/status/2062423820636672069?s=20) after evaluating “all the major players.” Self-hosting, for what it’s worth, was never on the table.

“We did not seriously consider [self-hosting], no — it would seem like a massive distraction,” he says.

> “We did not seriously consider self-hosting…it would seem like a massive distraction.”

## Runway and future plans

While Crivello says the switch will ultimately save Lindy millions, the runway implications for a venture-backed company are significant.

But how much, exactly? “A ton,” is all Crivello will say.  
  
As for whether the move is permanent, Crivello is non-committal. “Nothing in life is permanent,” he says. “I wouldn’t be surprised if Anthropic’s next release earned [them] our business back, but they would need to significantly cut prices.”

> “I wouldn’t be surprised if Anthropic’s next release earned them our business back, but they would need to significantly cut prices.”

It’s also worth noting that Lindy remains an Anthropic customer — just not for its core product. The company still uses Claude internally, because the economics of the subscription make it viable.

“Our internal use is about [the Max plan](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) — if it wasn’t for it, and if we had to pay full token price, we’d switch to something else,” Crivello says.

Responding to [a question from](https://x.com/sqs/status/2062393582091424058?s=20) Amp CEO and founder [Quinn Slack](http://linkedin.com/in/quinnslack) about whether Lindy might eventually be forced back to Anthropic’s models for its external product, Crivello suggested the door isn’t entirely closed. “We’ll probably still escalate to Opus when we detect Lindy is failing at a task,” he [wrote](https://x.com/Altimor/status/2062398729349628162?s=20), “but that’ll be marginal.”

Crivello’s view is that companies in Lindy’s position — large token consumers — have little choice but to act. “Companies like us who spend a lot on tokens, 100% — you’d be irresponsible not to,” he says. “Other companies, it will depend, but I think a lot of folks just stick to the brand name.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)