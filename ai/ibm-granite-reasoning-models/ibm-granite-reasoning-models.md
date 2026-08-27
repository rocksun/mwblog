<!--
title: IBM推出Granite 4.2新模型：强化推理能力并坚守密集架构路线
cover: https://cdn.thenewstack.io/media/2026/08/6dbec13c-blog_art_granitev4_2_release_6e4404e908-scaled.png
summary: IBM发布了全新的Granite 4.2系列开源大模型。该系列采用密集型Transformer架构，提供3B、8B及30B版本，重点增强了推理能力、Agent代理任务支持及长文本处理，旨在为企业提供高效、高吞吐的落地AI解决方案。
-->

IBM发布了全新的Granite 4.2系列开源大模型。该系列采用密集型Transformer架构，提供3B、8B及30B版本，重点增强了推理能力、Agent代理任务支持及长文本处理，旨在为企业提供高效、高吞吐的落地AI解决方案。

> 译自：[IBM's new Granite 4.2 models add reasoning and stay dense](https://thenewstack.io/ibm-granite-reasoning-models/)
> 
> 作者：Frederic Lardinois

周二，IBM [发布了](https://huggingface.co/blog/ibm-granite/granite-4-2)其最新的开源权重 Granite 大语言模型 (LLM) 系列。该系列包含 30 亿、80 亿和 300 亿参数版本。IBM 在模型构建上采取了与部分竞争对手截然不同的策略，即通过从头开始预训练的密集型、仅解码器 (decoder-only) 推理模型。

近期许多模型已从全注意力 (all-attention) Transformer 架构转向混合 Mamba/注意力架构，包括 Nvidia 的 [Nemotron 3 系列](https://thenewstack.io/nvidia-launches-nemotron-3-super-a-120b-open-model-for-large-scale-ai-systems/)。但 IBM 在其 Granite 4.0 模型中曾尝试过这种架构。该代产品涵盖了传统的密集型、密集混合型和混合 MoE 模型。

从 Granite 4.1 开始，IBM 将主系列回归到了全注意力、密集型 Transformer 架构。当时，IBM [表示](https://research.ibm.com/blog/granite-4-1-ai-foundation-models)这些新模型超越了旧一代，“同时使用了一种更简单、因此在下游任务微调中更灵活的架构”。

## Granite 的推理能力

IBM 将 4.2 系列描述为“专注于推理的版本”。模型可以在“思考”和“非思考”模式下运行，此外还提供了一种低功耗模式，仅消耗极少的推理 token 来回答简单问题。

在推出 Granite 4.1 模型时，IBM 曾认为推理模型效率不够高，因此“对于指令遵循和工具调用等特定任务，转向成本更低、非推理且基准测试表现相似的模型对企业用户更有意义”。然而，目前团队显然认为推理是一项必要功能，即使它在 4.2 模型中仍然是可选的。

与同级别的其他模型不同（包括 [Qwen-3.8 27B](https://thenewstack.io/qwen38-27b-local-inference/)、Muse Glimmer 30B 和 Google 的 Gemma 4 31B），它是纯文本模型。其他模型大多是多模态的，尽管 IBM 也提供例如 Granite Vision 4.1 4B，未来也有可能发布该模型的 4.2 版本。

值得注意的是，IBM 周二还发布了 Granite Speech 系列中的两款新语音识别模型。

## Granite 的训练

这些采用 Apache 2.0 许可的模型是在 15 万亿 token 上进行预训练的，共分为五个阶段，其中包括一个长上下文训练阶段，目前使该系列的上下文窗口达到了 512,000 token（尽管发布的配置原生支持 128K）。

IBM 指出，模型的训练集还包括 1 万亿 token 的合成代码，这些代码由 IBM 的 [CodeAlchemy 流水线](https://research.ibm.com/blog/code-alchemy-for-synthetic-code)生成（尽管模型的整体编码表现仍然平平）。

在很大程度上，所有模型都共享同一个流水线，但 8B 和 30B 模型还经过了额外的智能体强化学习步骤，以允许它们调用工具、编辑和运行代码、在终端工作以及搜索网络。“结合来自人类反馈的强化学习 (RLHF) 对齐，这种方法使模型能够更好地胜任复杂的、多步骤的智能体工作，” IBM 写道。

3B 模型也支持工具调用。只是不要对它期望过高。

![](https://cdn.thenewstack.io/media/2026/08/e6479eae-screenshot-2026-08-25-at-11.06.07-am-1024x810.png)

## 基准测试？表现尚可。

在基准测试方面，Granite 4.2 模型并没有带来突破性的进展，但值得注意的是，小型 8B 模型往往非常接近较大 30B 模型的表现，而且它几乎可以在任何现代 Mac 以及一些相对低端的 Nvidia RTX GPU 上轻松运行。

特别是 Qwen 3.8 27B 在各方面都超过了 Granite 模型，尤其是在编码方面，IBM 模型的总体结果表现不稳定。

![](https://cdn.thenewstack.io/media/2026/08/26f7b135-blog_art_competitor_charts_granite4_2_30b_1_b808f60cde-1024x427.webp)

不过，像往常一样，基准测试只能说明部分情况。对于合适的使用场景，前沿模型往往显得大材小用，而 IBM 认为 Granite 的主要优势在于其在高吞吐量智能体任务中的表现。

“此次发布扩展了 Granite 系列，目标明确：帮助企业构建能够在现实工作流中进行推理、行动和适应的智能体，” IBM 在公告中写道。“现在，AI 系统被要求在现实世界中执行任务，我们的期望已经提高。仅仅清晰简洁地回答问题已经不够了。AI 系统必须能够以可靠和一致的方式进行计划、调用应用程序和执行复杂任务——同时保持轻量化，以便在不造成昂贵成本的情况下实际使用。”