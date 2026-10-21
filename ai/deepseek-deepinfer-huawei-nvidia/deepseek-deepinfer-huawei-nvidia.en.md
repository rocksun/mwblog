DeepSeek has open-sourced the inference engine it uses to serve its models in production, a step it said last year wasn’t yet practical.

Dubbed [DeepInfer](https://github.com/deepseek-ai/DeepInfer), the framework is designed to let developers run [DeepSeek’s V4.1 Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) model on their own infrastructure, with many of the same optimizations the company uses behind its API. Support for future DeepSeek models is also planned.

> “Running a model efficiently is a different matter altogether.”

DeepSeek has, of course, long made its model weights available for developers to download and run using third-party software [such as vLLM](https://thenewstack.io/introduction-to-vllm-a-high-performance-llm-serving-engine/). But running a model *efficiently* is a different matter altogether. The software that manages requests, distributes work across chips, and generates responses can have a significant impact on speed, throughput and computing costs. And so DeepInfer essentially gives developers access to DeepSeek’s own approach to those challenges.

> “We’re sharing our production stack to help the community lower compute costs, reduce energy use, and make AI more affordable.”

## ‘Making AI more affordable’

Taking [to X on Tuesday](https://x.com/deepseek_ai/status/2112476496283775135?s=20), DeepSeek said it was making its internal inference technology available to outside developers in an effort to bring down the expense of running large AI models.

“We’re sharing our production stack to help the community lower compute costs, reduce energy use, and make AI more affordable,” the company writes.

Released [under the Apache 2.0 license](https://github.com/deepseek-ai/DeepInfer?tab=Apache-2.0-1-ov-file), DeepInfer includes optimized computing kernels and communication libraries, including DeepSeek’s previously open-sourced [FlashMLA](https://github.com/deepseek-ai/FlashMLA), [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM), and [DeepEP](https://github.com/deepseek-ai/DeepEP), alongside mechanisms for distributing inference across multiple chips. It also supports [speculative decoding](https://en.wikipedia.org/wiki/Speculative_decoding), a technique that speeds up response generation by predicting and verifying multiple tokens at once, and asynchronous scheduling to reduce the time processors spend waiting for new work. The framework also supports structured outputs, allowing developers to specify how model responses should be formatted.

Alongside DeepInfer, the company is also open-sourcing [deepseek-recipe](https://github.com/deepseek-ai/deepseek-recipe), a companion library that handles how API requests are converted into model inputs, and how the resulting output is processed into responses. Available for Rust and Python, it’s designed to help developers reproduce the behavior of DeepSeek’s official API when running their own deployments. The library was [quietly released in September](https://github.com/deepseek-ai/deepseek-recipe/blob/main/CHANGELOG.md), with an updated version [published on Tuesday](https://github.com/deepseek-ai/deepseek-recipe/blob/main/CHANGELOG.md).

The announcement comes just days after DeepSeek [released an updated version of V4.1 Flash](https://api-docs.deepseek.com/news/news261017), called DeepSeek-V4.1-Flash-1017, touting improvements in coding performance and efficiency. That release coincided with the company making its in-house web search technology available to developers through new Search and Fetch APIs, as per *The New Stack*‘s [report on Monday](https://thenewstack.io/deepseek-web-search-api/).

## Why DeepSeek held back in 2025

DeepInfer goes further than DeepSeek’s previous plans to share its inference technology. Back in April 2025, the company [published a document](https://github.com/deepseek-ai/open-infra-index/blob/main/OpenSourcing_DeepSeek_Inference_Engine/README.md) outlining its plans for its inference engine, explaining that it had considered releasing the entire system before deciding to contribute individual components and improvements to existing projects instead.

At the time, DeepSeek identified several obstacles. Its inference software had evolved from an early version of vLLM into a highly customized system, and the company questioned whether its relatively small research team could maintain another major open-source project. There were also practical difficulties in making the software usable outside DeepSeek’s own infrastructure.

“The engine is tightly coupled with our internal infrastructure, including cluster management tools, making it impractical for public deployment without significant modifications,” the company wrote at the time.

So what’s changed now, exactly? Well, DeepSeek *hasn’t* explained how it overcame those earlier difficulties, although the scope of the new release offers some clues. The DeepInfer [documentation](https://github.com/deepseek-ai/DeepInfer#readme) makes clear that the publicly available software currently supports offline inference, with “the core features needed for serving at scale,” as the company puts it. However, several components needed to operate a complete production service are still missing. These include a [KV cache](https://huggingface.co/blog/not-lain/kv-caching) management system, infrastructure for separating different stages of inference across machines, and load balancing across replicas.

In other words, DeepSeek has opened up much of the engine responsible for running its models, while leaving developers to supply some of the surrounding infrastructure required to operate a full-fledged service. That narrower release may help explain how the company has made its technology available despite the challenges it identified last year.

## Nvidia and Huawei, side by side

While the release of DeepSeek’s inference engine is significant enough in its own right, arguably the more interesting tidbit is the hardware supported from day one.

> “Arguably the more interesting tidbit is the hardware supported from day one.”

Nvidia is included, as expected, though support is restricted to its SM100 architecture, used in Blackwell data center GPUs. Notably, the other supported platform is Huawei’s [Ascend 950 NPU series](https://www.huawei.com/en/news/2026/9/hc-agentic-thinkpro-pto-cann), putting the Chinese chipmaker alongside Nvidia in DeepSeek’s list of compatible hardware. Older Nvidia architectures, including [Hopper](https://www.nvidia.com/en-gb/data-center/technologies/hopper-architecture/), are conspicuously absent.

This also ties back to DeepSeek’s published [open-source plans from 2025](https://github.com/deepseek-ai/open-infra-index/blob/main/OpenSourcing_DeepSeek_Inference_Engine/README.md). While the company was reluctant to release its entire inference engine at the time, it committed to working with hardware manufacturers ahead of future model launches, with the aim of making its models available across different chip architectures from day one.

US [export restrictions](https://www.reuters.com/world/china/us-takes-step-halt-nvidia-ai-chip-shipments-chinese-firms-outside-china-2026-05-31/) have complicated Chinese companies’ access to Nvidia’s most advanced chips, adding another dimension to DeepSeek’s growing ties with Huawei. In September, [Bloomberg reported](https://www.bloomberg.com/news/articles/2026-09-04/deepseek-plans-big-huawei-ai-chip-order-to-power-new-data-center) that DeepSeek was planning to deploy at least 160,000 Huawei Ascend 950DT chips at a new data center in Inner Mongolia, specifically to run its models. The company has largely relied on Nvidia for training, although *The Information* reported [in September](https://www.theinformation.com/articles/deepseek-bets-big-huawei-chips-bypass-u-s-export-controls/) that DeepSeek also plans to increase its use of Huawei chips for training, with deliveries expected as early as the fourth quarter.

Later that month, [Reuters reported](https://www.reuters.com/world/asia-pacific/deepseek-partners-with-huawei-develop-chip-programming-tools-reducing-reliance-2026-09-30/) that DeepSeek and Huawei were collaborating on software tools intended to make Ascend processors easier to program, further underlining the company’s investment in Chinese AI hardware.

The Huawei inclusion has already attracted attention among the wider developer community. In a discussion [on Reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xanm55/deepseek_released_deepinfer_open_source/), one commenter [singled out](https://www.reddit.com/r/LocalLLaMA/comments/1xanm55/comment/phv5agw/) the two supported hardware platforms as a highlight of the news, while another pointed to DeepSeek’s [origins in quantitative finance](https://www.reuters.com/technology/artificial-intelligence/high-flyer-ai-quant-fund-behind-chinas-deepseek-2025-01-29/) as a possible explanation for its technical expertise.

“Once again Deepseek shows how good high-frequency traders are at optimizing performance… On Ascend NPUs nonetheless!!,” the commenter [wrote](https://www.reddit.com/r/LocalLLaMA/comments/1xanm55/comment/phv7zpm/).

Another user seemingly poked fun at Anthropic’s [Claude Opus 5.5](https://thenewstack.io/claude-opus-5-5-lifecycle/), following [reports](https://www.techtimes.com/articles/327994/20260924/anthropic-builds-own-ai-export-restriction-opus-55-amazons-chip-caught-too.htm) that requests involving kernel programming for Huawei’s AI chips could trigger safeguards that redirect certain advanced AI development tasks to an older model.

“Don’t let Opus 5.5 see this! It will delete the Ascend support,” the user [joked](https://www.reddit.com/r/LocalLLaMA/comments/1xanm55/comment/phv5xzw/).

It is worth noting that feature support differs between the Nvidia and Huawei implementations. DeepInfer’s batch-invariant inference and deterministic sampling features, which help ensure reproducible outputs under specified conditions, are available only on Nvidia hardware. DeepSeek’s [published performance measurements](https://github.com/deepseek-ai/DeepInfer?utm_source=chatgpt.com#performance-benchmarks) also use Nvidia GPUs, with four SM100 GPUs used for prefill and 64 for decoding, leaving open the question of how the framework performs on Huawei’s chips by comparison.

For developers without access to either chip family, the immediate value may lie in studying the newly available code and adapting its optimizations to other inference engines. For now, DeepSeek has given the wider open-source community considerably more of its inference technology to experiment with.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)