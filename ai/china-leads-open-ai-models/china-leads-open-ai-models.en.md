Most of the AI spotlight shines on the biggest models from the biggest labs — [Claude from Anthropic](https://thenewstack.io/claude-million-token-pricing/), [GPT from OpenAI](https://thenewstack.io/gpt-54-nano-mini/), and [Gemini from Google](https://thenewstack.io/googles-gemini-3-1-pro-is-mostly-great/). These systems set the pace at the top end, with ever larger models and longer context windows.

But a parallel market has been building alongside these heavyweights. Open models — designed to be downloaded, adapted, and run in different environments — are seeing steady uptake among developers who want more control over cost, deployment, and customization.

That activity is perhaps most visible on [Hugging Face](https://huggingface.co/), the go-to platform where developers share models, datasets, and related tools. It [functions much like GitHub](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/), but for AI, making it a useful window into how open models are actually being used.

Until recently, US groups led much of that ecosystem, including [Meta’s Llama family](https://thenewstack.io/llama-stack-released-to-help-developers-build-agentic-apps/). But a steady [stream of data](https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment) from Hugging Face [over the past few months](https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment-blog-3) suggests [that the balance has shifted](https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment-blog-2), with China emerging as both a leading producer and user of open models.

In its latest report, *[State of Open Source on Hugging Face: Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)*, the company highlights several shifts across the AI model landscape — from which systems developers are building on most frequently, to the role that Big Tech plays in the ecosystem. But the geographic change — a shift in the center of gravity toward China — stands out most clearly.

However, it’s far from a clean transition: While China is gaining ground in the models themselves, the infrastructure those models run on remains firmly in Nvidia’s hands.

## The ‘DeepSeek moment’: China’s open AI surge

A joint [study by MIT and Hugging Face](https://www.dataprovenance.org/economies-of-open-intelligence.pdf), published in November, found that Chinese-developed open models accounted for about 17% of downloads through August 2025, narrowly surpassing the US share of 15.8% — the first time China had edged ahead on that measure. But that result was limited to a single one-year window. The latest Hugging Face data suggests a much bigger shift: China now leads in recent monthly downloads and has also pulled ahead in total downloads aggregated over roughly the past four years.

The change shows up first in usage. Chinese models accounted for 41% of downloads between February 2025 and February 2026, compared with 36.5% in the US.

![The geography of open source](https://cdn.thenewstack.io/media/2026/03/90433d6e-downloadsgeogrpah-1024x576.png)

*The geography of open source (credit: Hugging Face)*

That shift has been driven in part by the virality of models such as [DeepSeek R1](https://api-docs.deepseek.com/news/news250120), which [took the AI world by storm](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/) following its release in January 2025, offering performance that rivalled leading systems at a lower cost, with weights available for developers to run and adapt.

This, ultimately, [proved to be the catalyst for other Chinese companies](https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment). Baidu, for example, went from no releases on Hugging Face in 2024 to more than 100 [in 2025](https://finance.yahoo.com/news/baidu-launches-ai-models-touts-093000740.html). TikTok parent ByteDance and Tencent each expanded their output by up to 9 times, according to Hugging Face data. And companies that had previously focused on closed systems, such as [MiniMax](https://www.minimax.io/), have [also begun publishing models openly](https://www.minimax.io/news/minimaxm1).

On Wednesday, Chinese smartphone maker Xiaomi unveiled [MiMo-V2-Pro](https://mimo.xiaomi.com/mimo-v2-pro), a trillion-parameter model that it says approaches the performance of leading US systems at a fraction of the cost, with [plans to release open weights](https://x.com/_LuoFuli/status/2034379957913129140) once the model stabilizes.

This surge in releases from China is also reflected in deployment data. A [report from RunPod](https://thenewstack.io/runpod-ai-infrastructure-reality/), which tracks usage across its infrastructure, found that Alibaba’s Qwen models have overtaken Meta’s Llama as the most widely deployed self-hosted large language model.

The same pattern appears on Hugging Face itself, in what developers choose to build on top of. Models from Alibaba — including Qwen — have spawned more than 100,000 derivatives, reflecting how widely those systems are being adapted and reused.

![Derivatives on Hugging Face by Organization](https://cdn.thenewstack.io/media/2026/03/044751aa-derivaites-1024x576.png)

***Derivatives on Hugging Face by Organization (credit: Hugging Face)***

Another signal comes from how developers react to models on the platform. On Hugging Face, “likes” are a simple popularity signal — showing which models are drawing attention.

A year ago, the most liked models were largely concentrated around Meta’s Llama models, which occupied three of the top five positions. Fast-forward 12 months, and China’s DeepSeek-R1 is now at number one, alongside a broader mix of models from outside the US appearing in the top ranks.

![Most 'liked' models on Hugging Face](https://cdn.thenewstack.io/media/2026/03/c1c8f61c-sentiment.png)

*Most ‘liked’ models on Hugging Face (credit: Hugging Face)*

Suffice it to say, sentiment has segued from Meta toward a broader mix of players from China, Germany, and the UK.

## Nvidia and the hardware factor

Arguably, one of the biggest stories to emerge from the AI boom has been that of Nvidia – the chip designer once best known for powering gaming graphics cards, which has been able to [capitalise on the surge in demand](https://thenewstack.io/nvidias-hardware-roadmap-and-its-impact-on-developers/) for GPUs used to train and run AI models. Today, Nvidia is far and away the world’s most valuable public company, with its market value peaking at [more than $5 trillion last year](https://www.cnbc.com/2025/10/29/nvidia-on-track-to-hit-historic-5-trillion-valuation-amid-ai-rally.html).

Hardware is only part of the story, though. Nvidia has been [pushing further up the stack](https://thenewstack.io/nvidia-wants-to-rewrite-the-software-development-stack/), developing its own software, models, and tools aimed at shaping how AI systems are built and deployed — an effort to tie developers more closely to its ecosystem.

On Hugging Face, that push is also showing up in the company’s growing repository count. By the end of 2025, Nvidia had [built up more than 350 repositories on the platform](https://aiworld.eu/story/big-tech-is-all-in-on-open-source-ai-) — more than any other organization tracked — reflecting a steady increase in contributions over time.

![Nvidia tops the Hugging Face repo count](https://cdn.thenewstack.io/media/2026/03/1a0c3ef5-screenshot-2026-03-20-at-11-48-38-state-of-open-source-on-hugging-face-spring-2026.png)

*Nvidia tops the Hugging Face repo count (credit: Hugging Face)*

This rise very much reflects how Nvidia has been extending its reach beyond hardware into the software and model layer of late. This includes efforts such as its Nemotron model family and projects such as NemoClaw, an open-source platform for AI agents.

The reality is that most AI models are still designed to run on Nvidia GPUs. Even as support for alternative hardware improves — [including AMD systems](https://www.cnbc.com/2025/10/08/amd-deal-with-openai-gives-nvidia-a-needed-challenger-in-ai-chips.html) and, increasingly, chips [developed by Chinese companies](https://spectrum.ieee.org/china-ai-chip) — the bulk of the ecosystem continues to rely on Nvidia’s architecture.

That dependence helps explain why Nvidia is investing so heavily in the space. The company has outlined plans for tens of billions of dollars in spending tied to AI infrastructure, including a [reported $26 billion investment](https://www.fool.com/investing/2026/03/12/nvidia-is-making-a-massive-26-billion-bet-on-the-f/) over the next five years to develop open AI models, underscoring how closely its business is tied to the growth of model usage. The logic is fairly simple: if those models are tuned to Nvidia hardware, they strengthen the company’s wider grip on the AI stack.

At the same time, some of the same Chinese companies driving open model adoption are also working to reduce that reliance on US hardware. Alibaba, for instance, [has been investing](https://www.networkworld.com/article/4049120/alibaba-is-developing-an-ai-inference-chip-amid-us-export-curbs.html) in inference-focused chips designed to run open models within domestic data centers. Those efforts are still at an early stage, however, and have yet to displace the existing stack.

For now, that leaves a clear divide. At the model level, Hugging Face data shows how Chinese developers are gaining ground in both output and adoption. But at the infrastructure level, Nvidia remains central to how those models are run.

It’s a familiar story from the cloud: A handful of US companies control much of the underlying infrastructure, even as others try to build alternatives. [Europe is in the midst](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/900014236/How+the+DIGITAL+Building+Blocks+can+help+bring+EuroStacks+vision+of+European+digital+sovereignty+to+life) of reducing its reliance on those providers, [with limited success](https://www.theregister.com/2026/02/20/ditching_aws_euro_stack/) so far.

Those same concerns are now surfacing in AI, which sits atop that same cloud layer. Open models may be spreading like wildfire, but at the end of the day, they are still running on someone else’s machines — regardless of which country is leading the charge.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)