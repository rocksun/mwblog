[Alibaba](https://thenewstack.io/qwen-autonomous-coding-audit/) this week unveiled [Qwen3.8-Flash](https://github.com/QwenLM/Qwen3.8-Flash-Next/blob/main/tech_report.pdf?spm=a2ty_o06.30285417.0.0.1d73c921NCrGSC&file=tech_report.pdf), an open-weight, [multimodal](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) Mixture-of-Experts (MoE) model.

Hot on the heels of [Qwen 3.8 Max](https://qwen.ai/blog?id=qwen3.8&utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform), which [arrived at the start of the month](https://qwen.ai/blog?id=qwen3.8&utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform), this 125-billion-parameter AI model is offered as a prelude to Qwen 4. It is positioned as both a performance and value-for-money play. As such, it is claimed to have “superior capabilities in coding and office tasks” and an optimal balance among capability, latency, and cost.

“In this release, we are opening the weights of Qwen3.8-Flash-Next, a multimodal MoE model that also serves as an early preview of the architecture used in Qwen4,” confirmed Alibaba [in its release blog](https://qwen.ai/blog?id=qwen3.8-flash-next).

## How and why does Alibaba offer early access precursor models?

By releasing the architectural changes in Qwen3.8-Flash early, the organization hopes the community will examine the mechanics, constructs, and components within and start road-testing them before the full Qwen4 model family is built on top of them.

By stating that Qwen3.8-Flash paves the way for Qwen4, Alibaba is showcasing (and, importantly, openly sharing) design forms that it will carry into its subsequent models, so that developers can start building (or at least planning) their next codebases early.

Specifically then, Alibaba has stated that Qwen3.8-Flash “plays the same role” that Qwen3-Next played for Qwen3.5 i.e. by which the company means that Qwen3.8-Flash introduced developers to the company’s hybrid Gated DeltaNet + Gated Attention design (computational components that enable AI models to balance long-context efficiency with contextual focus and attention during inference and training), which was then used across the Qwen3.5, Qwen3.6, Qwen3.7 and Qwen3.8 series.

“Qwen3.8-Flash-Next upgrades the model systematically along four aspects – attention, residual, embedding and optimization –  improving model capability while further optimizing computational efficiency, model capacity and training stability,” stated Alibaba.

## Benchmark scores against rival models

When benchmarked on agentic coding, long-horizon agent tasks and multimodal intelligence, Qwen3.8-Flash appears to perform respectably against models including [DeepSeek-V4-Flash](https://thenewstack.io/deepseek-v4-flash-open-weights/) and [Claude-Opus-4.6](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/) across SWE-bench Pro (agentic coding), CoWorkBench (long-horizon office work), Toolathlon Verified (real-world tool use), MathVision (visual maths problem-solving), AndroidWorld (agentic mobile use) and ERQA (embodied intelligence).

> “Qwen3.8-Flash-Next upgrades the model systematically along four aspects – attention, residual, embedding and optimization – improving model capability while further optimizing computational efficiency, model capacity and training stability.”

Tested on agentic coding using SWE-bench Pro, Qwen3.8-Flash-Next scores 62.5, compared to 61.7 on Qwen3.8-27B, 55 on Qwen3.7-Plus, 56.0 on DeepSeek-V4-Flash-0731, and 53.4 on Claude-Opus-4.6 (Max).

Importantly, Qwen3.8-Flash requires only what Alibaba details as “around one-ninth of the training resources,” while delivering superior performance. The company says that this means Qwen3.8-Flash “significantly reduces” both training and inference costs compared with Qwen3.7-Plus, a model three times its size.

## What’s the difference between Qwen3.8-Flash-Next and Qwen3.8-Flash?

For the sake of nomenclature, Qwen3.8-Flash-Next is the open-weight research-frontier model available to developers on both the [Hugging Face](https://thenewstack.io/openai-huggingface-sandbox-breach/) AI developer hub and Alibaba’s [ModelScope](https://www.alibabacloud.com/blog/alibaba-cloud-launches-modelscope-platform-and-new-solutions-to-lower-the-threshold-for-materializing-business-innovation_599467) community portal. Built on the same underlying architecture, Qwen3.8-Flash is the production version of the model, offered via the QwenCloud API with 1 million tokens by default and official built-in tools.

Qwen3.8-Flash-Next features a 125B-parameter main model, supplemented by an additional 51B N-gram embeddings, with 6B parameters activated per token. It natively supports 262,144 tokens of context and can be extended to 1,000,000 tokens with YaRN.

## What architectural updates have happened?

As noted, Qwen3.8-Flash introduces architectural extensions across attention mechanisms, residual connections, embeddings, and optimization. Its hybrid attention architecture combines Gated DeltaNet (GDN), which compresses historical information, with Qwen Sparse Attention (QSA), a novel design that uses a lightweight compressed indexer to select relevant context, substantially reducing attention costs for long sequences.

Alibaba has explained that the Gated Residual (GR) mechanism expands data pathways between layers while strengthening cross-layer information flow and training stability. The N-gram Embedding technique scales model capacity with minimal additional computation, while the Muon Optimizer enhances the efficiency of large-scale model training.

> “I’d love it if local LLMs actually could replace remote ones today, and I have no reason to lie about my experience either…it’s just not there (yet) for local professional software development.”

## What do developers think of Qwen3.8-Flash?

In terms of developer reaction, it’s been a mixed bag so far.

Mechatronics engineer [Alok posts on X](https://x.com/analogalok/status/2092697021790708148), saying he thinks the [Video RAM](https://www.everpuredata.com/knowledge/what-is-vram.html) barrier (i.e., the need for physical, high-speed GPU-based memory for LLM memory management in the face of model quantization that aims to enable better long-context inference) is now officially dead.

“I just ran Qwen3.8-Flash-Next (MoE) 125B A6B with a  250,000 context window on a single 24GB RTX 4090 – 21 tokens/sec decode. 364 t/s prefill – no mtp. No dflash. No KV cache quantization! We are running datacenter models on consumer hardware,” enthused Alok.

Multi-disciplined software developer [Embedding Shapes](https://github.com/embedding-shapes/) is less happy.

They post on [Hacker News](https://news.ycombinator.com/item?id=49432317) using some colorful language to describe how models keep [insert expletive]-ing up very basic things before saying, “I’d love it if local LLMs actually could replace remote ones today, and I have no reason to lie about my experience either. But I too got hopeful reading the sentiment on the Internet about Qwen 3.8, but it’s just not there (yet) for local professional software development.”

## Pricing and access

Qwen3.8-Flash can be accessed via API Model Studio and Qwen Cloud, Alibaba’s AI-native cloud platform. Pricing per 1 million tokens is US$0.16 for input and US$0.47 (or 3 [RMB](https://en.wikipedia.org/wiki/Renminbi) for developers inside China) for output.

The model is also available on QwenWork, Alibaba’s workplace AI agent platform, where it runs a redesigned “standard mode” that cuts token consumption per task by 75% and “roughly doubles generation speed” compared with the current mode.

Alibaba has claimed that this brings flagship-level capabilities within reach of everyday workloads and that developers can run this model on hardware that they likely already own.

## When is Alibaba’s Qwen4 scheduled for launch?

Alibaba has not confirmed a firm launch date for Qwen4. Still, a casual web search on the topic yields a range of commentators and market watchers who broadly agree it will arrive before the end of the year, possibly as early as September.

Conjecture in this space explores whether the next model family could be optimized for complex 3D coding and design tasks in advanced spatial modeling. Others think that the Mixture-of-Experts (MoE) architecture will be extended and that deeper native multimodal processing capabilities might be featured.

Alibaba was contacted for broader comment on this story but declined to engage.

Qwen, in traditional Chinese, [通義千問](https://zh.wikipedia.org/zh-hant/%E9%80%9A%E4%B9%89%E5%8D%83%E9%97%AE) (pronounced Tōngyì qiān wèn), translates to “a thousand questions on general meaning” in English. Use that in your local pub quiz this weekend.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)