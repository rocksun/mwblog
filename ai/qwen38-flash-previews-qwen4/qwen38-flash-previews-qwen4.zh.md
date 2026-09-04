[阿里巴巴](https://thenewstack.io/qwen-autonomous-coding-audit/)本周发布了 [Qwen3.8-Flash](https://github.com/QwenLM/Qwen3.8-Flash-Next/blob/main/tech_report.pdf?spm=a2ty_o06.30285417.0.0.1d73c921NCrGSC&file=tech_report.pdf)，这是一款开放权重的[多模态](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/)混合专家（MoE）模型。

紧随[本月初发布](https://qwen.ai/blog?id=qwen3.8&utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)的 [Qwen 3.8 Max](https://qwen.ai/blog?id=qwen3.8&utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) 之后，这款拥有 1250 亿参数的 AI 模型作为 Qwen 4 的前奏推出。它的定位兼顾性能与性价比，据称在“编码和办公任务中具备卓越能力”，并在能力、延迟和成本之间实现了最优平衡。

“在此次发布中，我们开放了 Qwen3.8-Flash-Next 的权重，这是一款多模态 MoE 模型，同时也作为 Qwen4 所用架构的早期预览，”阿里巴巴[在其发布博客中](https://qwen.ai/blog?id=qwen3.8-flash-next)确认道。

## 阿里巴巴为何提供早期预览模型？

通过提前发布 Qwen3.8-Flash 中的架构变更，阿里巴巴希望社区能够研究其中的机制、结构和组件，并在完整的 Qwen4 模型系列构建完成之前对其进行道路测试。

通过声明 Qwen3.8-Flash 为 Qwen4 铺平了道路，阿里巴巴正在展示（并且重要地，公开共享）其后续模型将采用的设计形式，以便开发者可以提早开始构建（或至少规划）他们的下一代代码库。

具体而言，阿里巴巴表示 Qwen3.8-Flash “发挥了与 Qwen3-Next 对 Qwen3.5 相同的作用”，即 Qwen3.8-Flash 向开发者介绍了公司的混合 Gated DeltaNet + Gated Attention 设计（这些计算组件使 AI 模型能够在推理和训练过程中平衡长上下文效率与上下文聚焦和注意力），随后该设计被应用于 Qwen3.5、Qwen3.6、Qwen3.7 和 Qwen3.8 系列。

“Qwen3.8-Flash-Next 从注意力、残差、嵌入和优化四个方面对模型进行了系统性升级，在提高模型能力的同时，进一步优化了计算效率、模型容量和训练稳定性，”阿里巴巴表示。

## 与竞争模型基准测试对比

在针对智能体编码、长程智能体任务和多模态智能的基准测试中，Qwen3.8-Flash 在 SWE-bench Pro（智能体编码）、CoWorkBench（长程办公工作）、Toolathlon Verified（现实世界工具使用）、MathVision（视觉数学问题解决）、AndroidWorld（移动端智能体使用）和 ERQA（具身智能）等方面，对比包括 [DeepSeek-V4-Flash](https://thenewstack.io/deepseek-v4-flash-open-weights/) 和 [Claude-Opus-4.6](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/) 在内的模型，表现令人瞩目。

> “Qwen3.8-Flash-Next 从注意力、残差、嵌入和优化四个方面对模型进行了系统性升级，在提高模型能力的同时，进一步优化了计算效率、模型容量和训练稳定性。”

在 SWE-bench Pro 的智能体编码测试中，Qwen3.8-Flash-Next 得分为 62.5，相比之下，Qwen3.8-27B 为 61.7，Qwen3.7-Plus 为 55，DeepSeek-V4-Flash-0731 为 56.0，Claude-Opus-4.6 (Max) 为 53.4。

重要的是，Qwen3.8-Flash 仅需阿里巴巴所称的“约九分之一的训练资源”，同时提供更优的性能。公司表示，这意味着与三倍于其规模的 Qwen3.7-Plus 模型相比，Qwen3.8-Flash “显著降低”了训练和推理成本。

## Qwen3.8-Flash-Next 与 Qwen3.8-Flash 有何区别？

在命名方面，Qwen3.8-Flash-Next 是提供给开发者在 [Hugging Face](https://thenewstack.io/openai-huggingface-sandbox-breach/) AI 开发者中心和阿里巴巴 [ModelScope](https://www.alibabacloud.com/blog/alibaba-cloud-launches-modelscope-platform-and-new-solutions-to-lower-the-threshold-for-materializing-business-innovation_599467) 社区门户上使用的开放权重研究前沿模型。基于相同的底层架构，Qwen3.8-Flash 是该模型的生产版本，通过 QwenCloud API 提供，默认支持 100 万 token，并内置官方工具。

Qwen3.8-Flash-Next 拥有 125B 参数的主模型，辅以额外的 51B N-gram 嵌入，每个 token 激活 6B 参数。它原生支持 262,144 个 token 的上下文，并可通过 YaRN 扩展至 1,000,000 个 token。

## 进行了哪些架构更新？

如前所述，Qwen3.8-Flash 在注意力机制、残差连接、嵌入和优化方面进行了架构扩展。其混合注意力架构结合了压缩历史信息的 Gated DeltaNet (GDN) 与 Qwen Sparse Attention (QSA)——一种使用轻量级压缩索引器选择相关上下文的新颖设计，大大降低了长序列的注意力成本。

阿里巴巴解释说，Gated Residual (GR) 机制扩展了层间的数据路径，同时增强了跨层信息流和训练稳定性。N-gram Embedding 技术以极小的额外计算量扩展了模型容量，而 Muon Optimizer 则增强了大规模模型训练的效率。

> “如果本地 LLM 今天真的能取代远程模型，我会很高兴，我也没理由对我的经验撒谎……对于本地专业软件开发而言，它（目前）还达不到要求。”

## 开发者如何看待 Qwen3.8-Flash？

就开发者的反应而言，目前各方观点不一。

机电工程师 Alok 在 X 上发布文章，称他认为视频内存（Video RAM）障碍（即面对旨在实现更好长上下文推理的模型量化时，对物理、高速 GPU 内存进行 LLM 内存管理的需求）现已正式终结。

“我刚刚在单台 24GB RTX 4090 上运行了 Qwen3.8-Flash-Next (MoE) 125B A6B，上下文窗口为 250,000——解码速度为 21 token/秒。预填充速度 364 t/s——无需 MTP。无需 DFlash。无需 KV 缓存量化！我们正在消费级硬件上运行数据中心模型，”Alok 兴奋地说道。

多学科软件开发者 Embedding Shapes 则不那么高兴。

他们在 [Hacker News](https://news.ycombinator.com/item?id=49432317) 上发帖，用一些激烈的言辞描述了模型如何不断地把基础事物搞砸，然后说道：“如果本地 LLM 今天真的能取代远程模型，我会很高兴，我也没理由对我的经验撒谎。但我读到互联网上关于 Qwen 3.8 的言论时也曾充满希望，但对于本地专业软件开发而言，它（目前）还达不到要求。”

## 定价与访问

Qwen3.8-Flash 可通过阿里巴巴 AI 原生云平台 Model Studio 和 Qwen Cloud 访问。每百万 token 的价格为：输入 0.16 美元，输出 0.47 美元（或中国境内开发者为 3 [人民币](https://en.wikipedia.org/wiki/Renminbi)）。

该模型也可在阿里巴巴的工作场所 AI 智能体平台 QwenWork 上使用，该平台运行一种重新设计的“标准模式”，与当前模式相比，每项任务的 token 消耗量减少了 75%，并且“生成速度大致翻倍”。

阿里巴巴声称，这使旗舰级能力能够触达日常工作负载，并且开发者可以在他们可能已经拥有的硬件上运行该模型。

## 阿里巴巴的 Qwen4 预计何时发布？

阿里巴巴尚未确认 Qwen4 的确切发布日期。不过，对该主题进行的简要网页搜索显示，一系列评论员和市场观察家普遍认为它将在年底前到来，最早可能在 9 月。

这一领域的猜测探讨了下一个模型系列是否会针对高级空间建模中的复杂 3D 编码和设计任务进行优化。其他人则认为混合专家（MoE）架构将得到扩展，并可能具备更深入的原生多模态处理能力。

本刊已就此报道联系阿里巴巴以寻求更广泛的评论，但对方拒绝置评。

Qwen 在繁体中文中为[通義千問](https://zh.wikipedia.org/zh-hant/%E9%80%9A%E4%B9%89%E5%8D%83%E9%97%AE)，英文意为“a thousand questions on general meaning”。本周末你可以在当地的酒吧问答游戏中使用这个知识点。