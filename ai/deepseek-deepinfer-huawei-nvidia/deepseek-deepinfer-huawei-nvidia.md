<!--
title: DeepSeek开源API推理引擎，华为与英伟达获得平起平坐的地位
cover: https://cdn.thenewstack.io/media/2026/10/be91e6e6-deepseek-app.png
summary: DeepSeek正式开源其API背后的推理引擎DeepInfer，旨在降低计算成本并使AI更加普惠。该框架首发同时支持英伟达Blackwell和华为昇腾950系列芯片，引发业界广泛关注。
-->

DeepSeek正式开源其API背后的推理引擎DeepInfer，旨在降低计算成本并使AI更加普惠。该框架首发同时支持英伟达Blackwell和华为昇腾950系列芯片，引发业界广泛关注。

> 译自：[DeepSeek open-sources the inference engine behind its API. And Huawei gets equal billing with Nvidia.](https://thenewstack.io/deepseek-deepinfer-huawei-nvidia/)
> 
> 作者：Paul Sawers

DeepSeek 已经开源了用于在生产环境中提供其模型服务的推理引擎，这一举措它在去年曾表示尚不切实际。

这个名为 [DeepInfer](https://github.com/deepseek-ai/DeepInfer) 的框架旨在让开发者能够在其自己的基础设施上运行 [DeepSeek’s V4.1 Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) 模型，并享有该公司在其 API 背后使用的许多相同优化。官方还计划支持未来的 DeepSeek 模型。

> “高效运行模型完全是另一回事。”

当然，DeepSeek 长期以来一直向开发者提供其模型权重，以便他们使用第三方软件（[例如 vLLM](https://thenewstack.io/introduction-to-vllm-a-high-performance-llm-serving-engine/)）下载和运行。但*高效地*运行模型完全是另一回事。管理请求、在芯片之间分配工作以及生成响应的软件会对速度、吞吐量和计算成本产生重大影响。因此，DeepInfer 基本上让开发者能够访问 DeepSeek 应对这些挑战的独特方法。

> “我们正在分享我们的生产技术栈，以帮助社区降低计算成本、减少能耗，并使 AI 更加经济实惠。”

## “让 AI 更加经济实惠”

DeepSeek [周二在 X 上发文](https://x.com/deepseek_ai/status/2112476496283775135?s=20)表示，其正在向外部开发者开放内部推理技术，以此努力降低运行大型 AI 模型的费用。

该公司写道：“我们正在分享我们的生产技术栈，以帮助社区降低计算成本、减少能耗，并使 AI 更加经济实惠。”

DeepInfer [在 Apache 2.0 许可证下发布](https://github.com/deepseek-ai/DeepInfer?tab=Apache-2.0-1-ov-file)，其中包含优化的计算内核和通信库（包括 DeepSeek 先前开源的 [FlashMLA](https://github.com/deepseek-ai/FlashMLA)、[DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) 和 [DeepEP](https://github.com/deepseek-ai/DeepEP)），以及跨多个芯片分发推理的机制。它还支持[推测解码](https://en.wikipedia.org/wiki/Speculative_decoding)——这是一种通过一次预测和验证多个 Token 来加速响应生成的技术，以及用于减少处理器等待新工作时间的主动调度（asynchronous scheduling）。该框架还支持结构化输出，允许开发者指定模型响应的格式化方式。

除了 DeepInfer，该公司还开源了 [deepseek-recipe](https://github.com/deepseek-ai/deepseek-recipe)，这是一个配套库，用于处理 API 请求如何转换为模型输入，以及如何将产生的输出处理为响应。它提供 Rust 和 Python 版本，旨在帮助开发者在运行自己的部署时重现 DeepSeek 官方 API 的行为。该库于 [9 月悄然发布](https://github.com/deepseek-ai/deepseek-recipe/blob/main/CHANGELOG.md)，并于[周二发布了更新版本](https://github.com/deepseek-ai/deepseek-recipe/blob/main/CHANGELOG.md)。

此次发布就在 DeepSeek [发布 V4.1 Flash 更新版本](https://api-docs.deepseek.com/news/news261017)（名为 DeepSeek-V4.1-Flash-1017）几天后，该版本吹捧了在编码性能和效率方面的改进。根据 *The New Stack* 的[周一报道](https://thenewstack.io/deepseek-web-search-api/)，该版本的发布恰逢该公司通过新的 Search 和 Fetch API 向开发者提供其内部网页搜索技术。

## DeepSeek 在 2025 年为何有所保留

DeepInfer 比 DeepSeek 之前分享其推理技术的计划更为深入。早在 2025 年 4 月，该公司就[发布了一份文档](https://github.com/deepseek-ai/open-infra-index/blob/main/OpenSourcing_DeepSeek_Inference_Engine/README.md)，概述了其推理引擎的计划，解释称它曾考虑发布整个系统，随后才决定转而向现有项目贡献单个组件和改进。

当时，DeepSeek 识别出了几个障碍。其推理软件已经从早期版本的 vLLM 演变为一个高度定制的系统，该公司质疑其相对较小的研究团队是否能够维护另一个主要的开源项目。在使软件能够在 DeepSeek 自身基础设施之外使用时，也存在实际困难。

该公司当时写道：“该引擎与我们的内部基础设施（包括集群管理工具）紧密耦合，如果没有重大修改，将其用于公共部署是不切实际的。”

那么现在究竟有什么改变呢？好吧，DeepSeek *并没有*解释它是如何克服这些早期困难的，尽管新发布的范围提供了一些线索。DeepInfer [文档](https://github.com/deepseek-ai/DeepInfer#readme)清楚地表明，当前公开可用的软件支持离线推理，正如该公司所说，具备“大规模提供服务所需的核心功能”。然而，运行完整生产服务所需的几个组件仍然缺失。这些组件包括 [KV 缓存](https://huggingface.co/blog/not-lain/kv-caching)管理系统、用于跨机器分离推理不同阶段的基础设施，以及跨副本的负载均衡。

换句话说，DeepSeek 开放了负责运行其模型的大部分引擎，同时让开发者自行提供运营完整服务所需的部分周边基础设施。这种较窄范围的发布可能有助于解释为什么尽管存在去年识别出的挑战，该公司依然将其技术公之于众。

## 英伟达与华为并驾齐驱

虽然 DeepSeek 推理引擎的发布本身已经足够重大，但可以说是更有趣的花絮是第一天就受支持的硬件。

> “可以说更有趣的花絮是第一天就受支持的硬件。”

英伟达一如预期名列其中，但支持仅限于其 SM100 架构，该架构用于 Blackwell 数据中心 GPU。值得注意的是，另一个受支持的平台是华为的 [Ascend 950 NPU 系列](https://www.huawei.com/en/news/2026/9/hc-agentic-thinkpro-pto-cann)，这使得这家中国芯片制造商与英伟达一同出现在 DeepSeek 的兼容硬件列表中。较旧的英伟达架构（包括 [Hopper](https://www.nvidia.com/en-gb/data-center/technologies/hopper-architecture/)）则明显缺席。

这也与 DeepSeek 发布的 [2025 年开源计划](https://github.com/deepseek-ai/open-infra-index/blob/main/OpenSourcing_DeepSeek_Inference_Engine/README.md)息息相关。虽然该公司当时不愿发布其整个推理引擎，但它承诺在未来模型发布之前与硬件制造商合作，旨在从第一天起就跨不同芯片架构提供其模型。

美国的[出口限制](https://www.reuters.com/world/china/us-takes-step-halt-nvidia-ai-chip-shipments-chinese-firms-outside-china-2026-05-31/)使中国公司获取英伟达最先进芯片的途径变得复杂，这为 DeepSeek 与华为日益紧密的联系增添了另一个维度。今年 9 月，[彭博社报道称](https://www.bloomberg.com/news/articles/2026-09-04/deepseek-plans-big-huawei-ai-chip-order-to-power-new-data-center)，DeepSeek 计划在内蒙古的一个新数据中心部署至少 160,000 块华为昇腾 950DT 芯片，专门用于运行其模型。该公司在训练方面主要依赖英伟达，尽管 *The Information* 在 [9 月报道称](https://www.theinformation.com/articles/deepseek-bets-big-huawei-chips-bypass-u-s-export-controls/)，DeepSeek 还计划增加使用华为芯片进行训练，预计最早在第四季度交付。

同月晚些时候，[路透社报道称](https://www.reuters.com/world/asia-pacific/deepseek-partners-with-huawei-develop-chip-programming-tools-reducing-reliance-2026-09-30/)，DeepSeek 与华为正在合作开发旨在使昇腾处理器更易于编程的软件工具，进一步突显了该公司对中国 AI 硬件的投资。

华为的加入已经引起了广大开发者社区的关注。在 [Reddit 上的讨论](https://www.reddit.com/r/LocalLLaMA/comments/1xanm55/deepseek_released_deepinfer_open_source/)中，一位评论者[特别指出](https://www.reddit.com/r/LocalLLaMA/comments/1xanm55/comment/phv5agw/)这两个受支持的硬件平台是该新闻的亮点，而另一位则指出 DeepSeek [源于量化金融](https://www.reuters.com/technology/artificial-intelligence/high-flyer-ai-quant-fund-behind-chinas-deepseek-2025-01-29/)，这可能是其技术专业知识的解释。

这位评论者[写道](https://www.reddit.com/r/LocalLLaMA/comments/1xanm55/comment/phv7zpm/)：“Deepseek 再次展现了高频交易员在优化性能方面有多么出色……而且居然是在昇腾 NPU 上！！”

另一位用户似乎在戏谑 Anthropic 的 [Claude Opus 5.5](https://thenewstack.io/claude-opus-5-5-lifecycle/)，此前有[报道称](https://www.techtimes.com/articles/327994/20260924/anthropic-builds-own-ai-export-restriction-opus-55-amazons-chip-caught-too.htm)，涉及华为 AI 芯片内核编程的请求可能会触发安全保障，将某些高级 AI 开发任务重定向到旧模型。

该用户[开玩笑说](https://www.reddit.com/r/LocalLLaMA/comments/1xanm55/comment/phv5xzw/)：“别让 Opus 5.5 看到这个！它会删掉昇腾支持的。”

值得注意的是，英伟达和华为实现之间的功能支持有所不同。DeepInfer 的批处理不变推理（batch-invariant inference）和确定性采样（deterministic sampling）功能（有助于确保在指定条件下获得可重复的输出）仅在英伟达硬件上可用。DeepSeek [发布的性能测量数据](https://github.com/deepseek-ai/DeepInfer?utm_source=chatgpt.com#performance-benchmarks)也使用了英伟达 GPU（使用 4 个 SM100 GPU 用于预填充（prefill），64 个用于解码），这使得该框架在华为芯片上的性能表现如何依然是个未知数。

对于无法访问任一芯片系列的开发者来说，即时价值可能在于研究新开放的代码，并将其实际优化调整应用到其他推理引擎中。目前，DeepSeek 已经让更广泛的开源社区能够试验其更多的推理技术。