Meta 认为其新的私有 AI 大语言模型 Muse Spark 会比开源的 Llama 带来更丰厚的利润。那么，Llama 的用户该何去何从？

早在 2023 年，[Meta 发布了 Llama 2.0 并宣称其为开源模型。](https://thenewstack.io/metas-llama-2-is-not-open-source-and-thats-ok/) 尽管 [Llama 并非真正的开源](https://thenewstack.io/open-source-ai-and-the-llama-2-kerfuffle/)，但它对开发者来说听起来很不错。

事实上，在 2024 年 10 月，Meta 创始人兼 CEO Mark Zuckerberg 宣称： “[开源 AI 是前行之路。](https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/)” 去年 3 月，该公司发布了一份新闻稿，[庆祝](https://about.fb.com/news/2025/03/celebrating-1-billion-downloads-llama/) Llama 下载量达到 10 亿次。

那是过去，而现在情况变了。

从实际角度来看，Meta 已经放弃了 Llama 的开发，转而支持其在本月宣布的新私有项目 [Muse Spark](https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/)。该模型由 Meta 超级智能实验室（Meta Superintelligence Labs）开发，这是在 Mark Zuckerberg 招揽 Scale AI 的 Alexandr Wang 以启动 Meta AI 计划后，于 2025 年成立的新部门。

据[报道](https://www.bloomberg.com/news/articles/2025-06-10/zuckerberg-recruits-new-superintelligence-ai-group-at-meta)，Mark Zuckerberg 对 Llama 模型落后于 ChatGPT 和 Claude 感到不满，因此 Muse Spark 采用了全新的基础设施、架构和数据管道从零开始构建。该公司还开启了“[重金投入的抢人模式](https://www.wsj.com/tech/ai/meta-ai-hiring-freeze-fda6b3c4)”，从竞争对手那里挖掘 AI 人才。Muse Spark 在任何方面都不属于 Llama 的衍生产品。

我们并不确切知道 Meta 为何将 Llama 从其优先级名单中移除，因为该公司尚未对此做出回应。当 *The New Stack* 就 Llama 和 Muse Spark 询问 Meta 时，该公司未予置评。

![](https://cdn.thenewstack.io/media/2026/04/b1ac3a12-04_search.gif)

*展示 Meta Muse Spark AI 的截图。*

然而，从 Meta 的公开言论中我们可以看到，虽然它表示“当前的 Llama 模型将继续作为开源提供”，但这仅确认了现有模型将保持可用，而对未来的开发只字未提。AI 社区的预期是 [Llama 将仅获得增量更新和维护](https://miraflow.ai/blog/meta-ended-llama-built-muse-spark-changes-everything-2026)。你可以不用指望它能获得 Muse Spark 那样大规模的前沿投资了。

> 由于部署模型根本不同，从 Llama 到 Muse Spark 没有迁移路径。

## 没有明确的迁移路径

这对当前的 Llama 用户意味着什么？他们陷入了麻烦。由于部署模型根本不同，从 Llama 到 Muse Spark 之间没有迁移路径。Llama 提供可下载的开放权重，用于自托管和微调；而 Muse Spark 仅限云端，没有可下载的权重，没有自托管能力，目前仅提供私有 API 预览访问权限。即使 [Meta 履行承诺开源其部分新模型](https://thenewstack.io/meta-open-source-models/)，也很难想象 Llama 用户如何迁移到这些平台。

正如 [Andrew Ng](https://www.linkedin.com/in/andrewyng) 在其 AI 通讯 *[The Batch](https://www.deeplearning.ai/the-batch/issue-349/#:~:text=The%20proprietary%20release%20has%20raised%20concerns%20among%20developers%2C%20many%20of%20whom%20have%20built%20projects%20on%20open%2Dweights%20Llama%20models.)* 中所写：“闭源版本的发布引起了开发者的担忧，他们中的许多人都是基于开放权重的 Llama 模型构建项目的。”同时 Ng 写道，Meta 的转型可能有助于它“与 OpenAI、Google 和 Anthropic 一起竞争企业客户。然而，它不再担任美国开放权重的领先倡导者，这对开发者社区来说是一个重大损失。”

> Meta 不再担任美国开放权重的领先倡导者，这对开发者社区来说是一个重大损失。

顺便说一句，这涉及的开发者数量并不少。一年前，Meta 报告称 [Llama 的下载量已达 12 亿次。](https://finance.yahoo.com/news/meta-says-llama-ai-models-174133533.html) 但即便在当时，开发者就认为 [Meta 在 Llama 上的投入已不足以让其与当时领先的前沿模型竞争](https://www.businessinsider.com/meta-ai-llama-was-big-deal-developers-see-untapped-potential-2025-5)。尽管如此，成千上万的公司以及无数的开发者和个人[仍在使用 Llama](https://theirstack.com/en/technology/meta-llama/us)。他们能做什么？

## 开发者的三个选择

Llama 开发者确实有一些选择，包括：

1. 你可以继续[使用现有的 Llama 模型，这些模型在主流云服务商上依然可用](https://www.llama.com/docs/getting-the-models/405b-partners/)。然而，这些大语言模型将越来越落后于其前沿竞争对手。
2. 转向来自 Mistral、DeepSeek 或阿里巴巴 Qwen 的竞争性开源模型。
3. 迁移到主流 AI 供应商的私有 API。例如，Meta 内部的程序员在 Muse Spark 问世之前很久就已经[转向了 Claude Sonnet](https://hackernoon.com/meta-abandons-llama-in-favor-of-claude-sonnet)。

切换成本是巨大的。迁移需要重写特定供应商的 API、调整私有训练数据，并整合定制的工具和工作流。[AI 迁移既不容易，也不便宜](https://www.theregister.com/2026/04/28/locked_stocked_and_losing_budget/)。

## Llama 分支填补空白

也许最简单的出路是使用一个或多个众多的 Llama 分支（fork）。其中最重要的是 Llama 推理引擎分支 [llama.cpp](https://github.com/ggml-org/llama.cpp)。这是一个流行的 C++ 推理引擎，用于在本地运行 Llama 模型。Llama.cpp 支持广泛的大语言模型，其范围远超 Meta 的 Llama 家族。在此基础上，又涌现出了其他几个重要的分支。

其中最著名的可能是 [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp)。这是一个专注于性能的分支，承诺提供比 llama.cpp 更好的 CPU 以及 GPU/CPU 混合性能。还有一个瑞芯微（Rockchip）NPU 分支，[Rkllama](https://github.com/NotPunchnox/rkllama)。该引擎将 llama.cpp 与瑞芯微 NPU 加速相结合，适用于 RK3588 芯片等嵌入式系统，旨在与几乎所有标准的 llama.cpp 兼容模型配合使用。最后还有 [llama-rs](https://github.com/onehr/llama-rs)，这是一个 Rust 实现，被市场定位为“用于本地 AI 的极速分支”。

最后是 [OpenLLaMA](https://github.com/openlm-research/open_llama)，它是 Meta 原始 LLaMA 模型的 Apache 许可证开源复现版。它提供 3B、7B 和 13B 参数版本，全部基于 1 万亿 token 训练。它还带有 PyTorch 和 JAX 的权重。

Meta 可能会从这一转变中受益。然而，Llama 用户现在必须寻找另一条出路。祝他们好运，他们会需要的。