Alibaba has revealed Qwen 3.8, its latest, greatest large language model (LLM) which, it says, is among the most powerful models today.

More specifically, the company claimed in its announcement on Sunday that it’s “second only to Fable 5,” Anthropic’s [much-hyped flagship model](https://thenewstack.io/fable-5-honeycomb-opus/). However, the company provided no model card, benchmarks, or any other meaningful data points beyond that.

Notably, the announcement comes just days after rival Chinese AI firm Moonshot debuted Kimi K3, drawing plaudits for [topping Arena’s coding leaderboard](https://thenewstack.io/kimi-k3-open-weight-coding/) and rivaling systems from Anthropic and OpenAI on internal benchmarks, while securing impressive headlines on the [BBC](https://www.bbc.co.uk/news/articles/cy9w4q8pgp0o), [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-20/moonshot-s-kimi-k3-may-be-more-about-memory-than-compute), and other mainstream news outlets.

While Moonshot has yet to release the K3 weights, it [has already](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart) published a [fairly substantial technical breakdown](https://www.kimi.com/blog/kimi-k3), complete with a full benchmark table against other leading systems, architecture details, and published pricing, with a July 27 date set for the open-weight release itself.

Alibaba, on the other hand, has largely relied on a single post on X to make its bold claims. On top of that, the message contained a couple of grammatical slip-ups, one of which seemingly conflated “compatible” with “comparable.”

While not hugely important in itself, it’s the kind of detail that might not instill much confidence in a launch meant to position the model as a genuine frontier contender.

## The open-weight factor

The broader appetite for open-weight AI has grown quickly this year. Analysts and infrastructure vendors argue that open models now trail the closed frontier [by as little as four months](https://thenewstack.io/open-weight-models-frontier-costs/), and at a fraction of the price.

That price gap is already changing how companies buy AI. In June, *The New Stack* reported that AI agent startup [Lindy was moving](https://thenewstack.io/lindy-deepseek-anthropic-switch/) all of its production traffic away from Anthropic’s models to DeepSeek v4, a switch its CEO said would save the company millions of dollars. Vendor lock-in is a growing concern too, with many in the industry [warning about deep dependence on a single proprietary model](https://thenewstack.io/karp-mensch-ai-lockin/) stack.

Qwen, for its part, has been a major beneficiary of that shift. Infrastructure provider [Runpod’s own platform data](https://thenewstack.io/runpod-ai-infrastructure-reality/) found that Qwen had overtaken Meta’s Llama as the most-deployed open-weight LLM among its users.

However, while Qwen built that reputation as a prolific open-weight publisher, its two most recent flagship models have broken from that pattern. [Qwen3.6-Max-Preview](https://qwen.ai/blog?id=qwen3.6-max-preview), launched in April, was the first flagship in Qwen’s history to ship API-only, with no weights published. [Qwen3.7-Max](https://qwen.ai/blog?id=qwen3.7), which followed in May, was equally closed, with no local-runnable version and no confirmed date for one.

With Qwen3.8, Alibaba is apparently returning to its roots, confirming that it will be released as an open-weight model. However, the big question this time around is when — and whether the timing of the announcement itself had more to do with a certain rival than with openness.

## The “checkpoint gap”

[Julien Simon](https://www.linkedin.com/in/juliensimon/), AI operating partner at private equity firm [Fortino Capital](https://www.fortino.capital/) and a former AI evangelist at Hugging Face and AWS, reckons that the real story sits in what he calls the “checkpoint gap” — the window between a frontier claim and the artifact that lets anyone actually verify it.

> “Every claim in [the Kimi K3] launch can be graded against a calendar.”

Kimi K3’s [version of that gap](https://www.airealist.ai/p/kimi-k3-and-the-checkpoint-gap), he [argues](https://www.airealist.ai/p/qwen-38-soon-is-not-a-date) in *The AI Realist* newsletter on Sunday, was “aggressive but disciplined”: a benchmark table, a published price, and a hard date of July 27 for the weights.

“Every claim in that launch can be graded against a calendar,” Simon writes.

Qwen3.8 opened the same gap, Simon argues, without any of that discipline: no benchmark table, no price, and no date — just “open-weight soon.” An undated gap functions as an option the vendor can exercise on its own timeline, all the while “collecting the open-weights narrative in the meantime.”

Both models, in different ways, sit behind the same company. Alibaba was Moonshot’s largest shareholder as of 2024, having put in roughly $800 million for what [was then a 36% stake](https://www.scmp.com/tech/big-tech/article/3264017/alibaba-emerges-major-backer-high-flying-chinese-start-moonshot-ai-36-stake) — a position likely diluted since, as Moonshot’s fundraising and valuation [has continued into the stratosphere](https://techcrunch.com/2026/05/07/chinas-moonshot-ai-raises-2b-at-20b-valuation-as-demand-for-open-source-ai-skyrockets/).

Kimi K3’s launch alone reportedly helped [wipe out more than $3 trillion](https://www.techtimes.com/articles/321066/20260720/kimi-k3-wipes-33t-chip-stocks-moonshot-moves-toward-hong-kong-ipo.htm) in global semiconductor value within days. And now, just days later, Alibaba has announced a marginally smaller model (2.4T parameters vs 2.8T), claimed a marginally better ranking, and attached the same open-weight language — only without key details.

> “The longer the gap between the words and the numbers, the more the announcement was the product.”

The obvious question, now, is why a company would seemingly compete against its own investment. Simon’s answer comes down to what a real benchmark table would have forced Alibaba to reveal. Numbers strong enough to beat Kimi K3, he argues, would make its own Moonshot stake look like a worse bet than its in-house model, at a time when Moonshot is [planning its entry to the public markets](https://finance.yahoo.com/technology/ai/articles/china-moonshot-plans-ipo-six-053131621.html).

Numbers that fell short would concede the “*second only to Fable 5*” crown outright. Saying nothing verifiable sidesteps both outcomes — Qwen gets to claim the position in headlines and enterprise conversations, without being placed next to K3 in a way that could be checked.

“The longer the gap between the words and the numbers, the more the announcement was the product,” Simon writes.

Put simply, the announcement itself was likely never really about the model. It was about injecting itself into the conversation around a much-hyped competitor.

> “The missing architecture details matter for a 2.4T model.”

There have been some early attempts to benchmark Qwen3.8 independently. One, [published Sunday](https://trilogyai.substack.com/p/qwen-38-max-benchmark-how-it-compares), ran the hosted preview against Kimi K3 on a matched task — the work of [Leonardo Gonzalez](https://www.linkedin.com/in/leonardo-gonzalez-technology/), VP of AI Center of Excellence at [Trilogy](https://trilogy.com/). But it’s a single test, scored by one reviewer, against a preview Alibaba itself says will keep changing before any formal release. It’s nowhere near a substitute for the benchmark table Alibaba has yet to publish.

“The missing architecture details matter for a 2.4T model,” Gonzalez concedes.

For now, that leaves Qwen3.8 exactly where it started: a tidy headline claim positioned against the mighty Anthropic, and not much more.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)