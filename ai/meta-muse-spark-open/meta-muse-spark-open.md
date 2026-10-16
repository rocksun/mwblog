<!--
title: Meta推出Muse Spark Open，迎战中国最强开源模型
cover: https://cdn.thenewstack.io/media/2026/10/f47a9e53-muse-spark-open-header-animation-1024x576.gif
summary: Meta推出了拥有8160亿参数的开源模型Muse Spark Open。该模型在多步推理和智能体任务中表现优异，性能可媲美或超越部分中国顶尖开源模型，但其商业使用协议附带了一定的限制条件。
-->

Meta推出了拥有8160亿参数的开源模型Muse Spark Open。该模型在多步推理和智能体任务中表现优异，性能可媲美或超越部分中国顶尖开源模型，但其商业使用协议附带了一定的限制条件。

> 译自：[Meta ships Muse Spark Open, its answer to China’s best open-weight models](https://thenewstack.io/meta-muse-spark-open/)
> 
> 作者：Frederic Lardinois

Meta 于周四推出了 Muse Spark Open，这是一个拥有 816B 参数（其中 42B 为激活参数）的新开源模型，该公司称其为“迄今为止能力最强的美国开源权重模型”。

该[新模型已通过](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) Baseten、Fireworks AI、Groq、Modal、Nebius、OpenRouter 和 Together AI 的 API 提供。由于它是一个开源模型，你还可以从 Amazon SageMaker AI、Google Cloud Model Garden、Hugging Face 以及微软的 Foundry Model Catalog 下载权重。

## 开放权重，半开放许可证

总体而言，Muse Spark Open 具备行业标准的 100 万 Token 窗口，它看起来是一个功能极其强大的模型，根据基准测试的不同，它与一些最优秀的中国模型不相上下甚至超越了它们。不过，正如某些[较新的中国模型](https://thenewstack.io/zai-glm-weights-license/)一样，其权重虽然是开放的，但许可证却并非完全开放。

Meta 以“[Muse 模型许可证](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B/blob/main/LICENSE.md)”发布了这一新模型。Meta 表示，该许可证拥有“有限的商业条款，允许许多开发人员免费使用该模型”。

具体而言，这意味着任何在连续十二个月内总收入超过 2000 万美元的公司，在将该软件或任何衍生产品作为该模型即服务（Model as a Service）业务的一部分提供之前，必须“通知 Meta 并与 Meta 签订单独的书面协议”。

任何使用该模型的公司还必须在使用该模型或从 Muse Spark Open 创建、训练、微调或蒸馏得出的衍生模型的每个产品或服务的用户界面中，“醒目地显示‘使用 Muse Spark Open 构建（Built with Muse Spark Open）’”。

总体而言，这看起来与 Moonshot（月之暗面）用于 Kimi K3 的许可证非常相似。

内部使用以及将该模型构建到您自己的产品中是免费的，但该许可证的使用政策禁止将其用于军事和关键基础设施部署——这是 Meta 在 2024 年针对 Llama 为美国政府添加的例外条款。

不过，与 Anthropic 针对 Claude 的[新使用政策](https://www.anthropic.com/news/2026-usage-policy-update)不同，您可以随心所欲地对该模型进行各种测试。

## 基准测试

该公司表示，构建这个新模型是为了“进行编程和智能体工作，它擅长长视距任务、复杂的软件工程和多步推理”。

Muse Spark Open 竞争的两个美国模型基本上是 Thinking Machines 的 Inkling 和 Nvidia 的 Nemotron 3 Ultra。在 Meta 自己的基准测试中，其新模型全面超越了它们——通常领先 20 分或更多。

![](https://cdn.thenewstack.io/media/2026/10/a9c1bb66-eval-table_light-851x1024.png)

图片来源：Meta。

然而，更激烈的竞争是与许多开发人员今天已经在运行的中国开源模型。Spark Open 在智能体和工具调用基准测试（包括 JobBench 和 MCP-Atlas）中领先于 Kimi K3、GLM 5.3 和 Qwen3.8，并在 SciCode 上大致打成平手。

编程是它落后的领域。

在 Terminal-Bench 2.1 上，Kimi K3 的得分为 85.0，GLM 5.3 为 83.9，而 Spark Open 的得分仅为 76.4。

在 DeepSWE 1.1 上，分差为 68 对 60。这与 Meta 在 4 月份推出闭源版 Spark 时承认的差距相同，而且看起来自那时以来它并没有取得太大进展。

## 在你买不起的 Mac 上运行 Muse Spark Open

你不太可能在本地运行一个 816B 的模型，但如果你拥有两台配备 M5 Ultra 芯片和 512 GB 内存的新款 Mac Studio，Meta 表示你可以将它们连接起来并使用 MLX 在其上运行该模型。

例如，该公司正是这样做的：运行由 Muse Spark 驱动的 Muse Code，并发布 Ice Cubes Mastodon 客户端的更新。苹果目前并不向普通大众销售 512 GB 的 Mac Studio，但在几周后，你将能够以[一辆紧凑型汽车的价格](https://www.apple.com/shop/buy-mac/mac-studio)买到两台这样的机器。