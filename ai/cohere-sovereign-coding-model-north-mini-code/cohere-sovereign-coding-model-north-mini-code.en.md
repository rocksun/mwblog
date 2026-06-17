Canadian foundation model company [Cohere](https://cohere.com/) has spent the [past few years](https://thenewstack.io/cohere-vs-openai-in-the-enterprise-which-will-cios-choose/) selling a specific idea to banks, governments, and healthcare providers: that AI should run on their infrastructure, under their control, with their data never leaving the perimeter.

Cohere’s pitch went down well in regulated industries. Now the company is taking it to a different audience, with the [launch of North Mini Code](https://cohere.com/blog/north-mini-code) — its first coding model, [released under an Apache 2.0 license from the get-go](https://huggingface.co/CohereLabs/North-Mini-Code-1.0).

## Model access as infrastructure

The sovereignty argument Cohere has long made to enterprise customers is, at its root, [about ownership](https://thenewstack.io/frontier-ai-models-now-becoming-available-for-takeout/). Regulated industries have hard requirements: data can’t leave certain boundaries, and the intelligence layer running on sensitive infrastructure needs to be something the organization controls. That requirement shaped how Cohere built its products — deployable anywhere, runnable on private infrastructure.

What’s changed, according to Cohere co-founder [Nick Frosst](https://www.linkedin.com/in/nick-frosst-19b80463/), is who is asking those same questions.

“We’re now hearing similar concerns from developers,” Frosst tells *The New Stack*. “They’re starting to think of model access as infrastructure, and infrastructure should be something you own and control. That is an extension of sovereignty.”

> “[Developers] are starting to think of model access as infrastructure, and infrastructure should be something you own and control.”

North Mini Code is a direct response to that demand. It’s a 30-billion-parameter Mixture of Experts (MoE) model with just 3 billion active parameters and is designed for agentic coding tasks: the kind of multi-step, tool-using work that coding agents like Claude Code and Cursor are built around.

Cohere says it runs on a single Nvidia H100 GPU, making self-hosting practical without a larger multi-GPU deployment. Developers who would rather not manage their own infrastructure can access it via API instead.

“We want to give developers a capable, fast, open-weight model they can run locally on their own terms, and that fits in their compute environments,” Frosst says.

> “We want to give developers a capable, fast, open-weight model they can run locally on their own terms, and that fits in their compute environments.”

Cohere claims it outperforms comparable open-weight models including [Alibaba’s Qwen3](https://qwen-3.com/en) and [Google’s Gemma 4](https://thenewstack.io/google-gemma-local-ai/) on the [Artificial Analysis Coding Index](https://artificialanalysis.ai/models/north-mini-code), where it scores 33.4, and says it delivers up to 2.8x higher output throughput than [Mistral’s Devstral Small](https://ollama.com/library/devstral-small-2) 2 on identical hardware.

Cohere’s own benchmark testing shows North Mini Code leading on terminal and code generation tasks — but results are mixed across the full evaluation suite, with Qwen 3.6 ahead on SWE-Bench Verified and LiveCodeBench v6, as its chart illustrates. Those comparisons are based on Cohere’s own testing and should be taken as indicative.

![North Mini Code’s performance in agentic software engineering and terminal tasks, along with complex code generation benchmarks, compared to leading open-source models of a similar size.](https://cdn.thenewstack.io/media/2026/06/df37238d-06e7b98d2b53bf7ca8b7dfa53d758991a031c2e5-3140x2400-1-1024x783.avif)

*North Mini Code’s performance in agentic software engineering and terminal tasks, along with complex code generation benchmarks, compared to leading open-source models of a similar size.* (**Credit: Cohere**)

## A growing club

Cohere’s timing puts it alongside a growing group of international companies that have made open-weight coding models a deliberate product choice. [Mistral](https://mistral.ai/), the [Paris-based AI company](https://thenewstack.io/mistral-vibe-cloud-agents/), [launched Devstral](https://mistral.ai/news/devstral/) in May 2025 — its first dedicated agentic coding model, also under Apache 2.0 — and [followed it with Devstral 2](https://mistral.ai/news/devstral-2-vibe-cli/) in December. [JetBrains](https://www.jetbrains.com/), the Czech developer tools company, recently [open-sourced Mellum2](https://thenewstack.io/jetbrains-mellum2-open-source-coding-model/), its second-generation coding model.

The emphasis differs. Mistral has explicitly linked open weights to AI sovereignty and the ability to deploy models on private infrastructure, while JetBrains focuses on latency, cost and deployment flexibility. In practice, both approaches give developers and enterprises more control over where models run and how they are operated.

## Owning the infrastructure

The appetite for open-weight alternatives to frontier models is clearly there. AI agent platform Lindy [recently announced it had moved](https://thenewstack.io/lindy-deepseek-anthropic-switch/) 100% of its inference traffic from Anthropic to China’s DeepSeek, saying the switch would save the company millions while actually improving performance on its core use cases. Lindy’s CEO Flo Crivello addressed the obvious question about routing through a Chinese-developed model: the company uses Atlas Cloud, a US-based inference provider that hosts DeepSeek on American soil. The open-weight nature of DeepSeek made that possible — the model can be hosted by any provider, in any jurisdiction.

That’s precisely the dynamic Frosst is pointing to. Open weights give developers optionality that a proprietary API does not: the ability to choose where the model runs, who operates it, and under what terms. For companies whose inference bill has grown to exceed payroll — as Crivello [noted](https://x.com/Altimor/status/2044108104816832576) is the case at Lindy — those are decisions with real commercial consequences.

Cohere’s [Command family](https://cohere.com/command) — its flagship line of enterprise models built for agentic, multilingual, and multimodal tasks — had previously shipped as open-weight models under more restrictive licenses. With Command A+, the [company moved to Apache 2.0 in May](https://cohere.com/blog/command-a-plus), making the legal terms around use and redistribution significantly more permissive.

> “Open-source development was concentrated in a small number of jurisdictions, and organizations running critical infrastructure had no reliable alternative.”

Frosst draws a direct line between the enterprise sovereignty argument Cohere has made for years and the thinking behind North Mini Code. The open-source coding model, he says, is a response to the same concentration problem Cohere saw in enterprise AI — only now playing out at the developer layer.

“Open-source development was concentrated in a small number of jurisdictions, and organizations running critical infrastructure had no reliable alternative,” Frosst says. “North Mini Code extends that thinking to the developer layer. As coding agents become the infrastructure software engineering runs on, whoever controls those systems controls how they work, how they evolve, and what they’re optimized for. We think that developers and enterprises should be in control.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)