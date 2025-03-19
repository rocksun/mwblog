# 在 GTC 大会上，继 DeepSeek 之后，NVIDIA 将重点放在了推理上

![Featued image for: After DeepSeek, NVIDIA Puts Its Focus on Inference at GTC](https://cdn.thenewstack.io/media/2025/03/7958b117-nvidia_jensen_tshirt-cannon-1024x768.jpeg)

今年早些时候，[DeepSeek](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/) 以极低的训练成本构建了一个极具竞争力的推理模型，这一消息导致 NVIDIA 的股票暴跌，因为分析师开始怀疑大规模 AI 硬件投资的时代是否即将结束。因此，今年 NVIDIA 年度大会 GTC 的主题演讲在很大程度上是对这一事件的回应，这也许并不令人意外。NVIDIA 的 CEO 兼联合创始人 Jensen Huang 宣布了一系列新的软件和硬件，包括下一代旗舰加速器和一系列有趣的桌面级 AI 系统，供开发人员使用。但所有这些的核心信息是：下一代应用程序将基于 AI——而要实现这一点，尤其是在推理模型和代理的时代，将需要大量的计算能力，而 NVIDIA 非常乐意提供这些能力。

事实上，NVIDIA 表示，预计对 AI 计算的需求将比之前的估计增加 100 倍。有趣的是，当 Huang 想要演示新的推理模型需要多少计算能力时，他选择将 Meta 更传统的 Llama 模型与 DeepSeek R1 进行比较。这肯定不是巧合。事实证明，DeepSeek 使用了 150 倍的计算量，并生成了 20 倍的 tokens。

“大规模推理是极限计算，”Huang 说。这里总需要在延迟和计算成本之间做出权衡。Huang 认为，无论如何，生成的 tokens 数量只会继续增加。当然，主题演讲并没有完全忽略训练，但很难不认为演示文稿的很大一部分（至少是前半部分）是对 DeepSeek 的回应。

Huang 还认为，正在发生一种普遍的平台转变，从构建在通用计算机存储上的手工编码软件转变为构建在加速器和 GPU 上的机器学习软件。这也意味着——这对 NVIDIA 来说是好事——软件开发的未来意味着资本投资。Huang 指出，以前，你编写软件并运行它。现在，“计算机已经成为 tokens 的生成器，”他说，而且他认为，大多数企业很快将构建他喜欢称之为“AI 工厂”的东西，这些工厂将与其物理工厂并行运行。

对于开发人员，NVIDIA 宣布了 DGX Spark 和 [DGX Station](https://www.nvidia.com/en-gb/data-center/dgx-station/)。Spark 可以与现有的台式机或笔记本电脑并行运行，看起来有点像 Mac Studio。与此同时，DGX Station 本质上是一个功能齐全的桌面工作站，专为数据科学家设计，拥有高达 500 teraFLOPS 的计算能力。

为了加速推理并降低数据中心的成本，NVIDIA 宣布了几款新的加速器，包括 Blackwell Ultra 系列以及即将推出的 Vera Rubin、Rubin Ultra 和 Feynman 几代芯片，所有这些芯片的计算性能和内存带宽都将比各自的前代产品显著提高。

NVIDIA 显然正在采用一种类似于 Intel 的 tick-tock 节奏，每年推出一代新芯片，然后很快推出一个优化的“ultra”版本。为了强调这一点，Huang 开玩笑说他是 NVIDIA 的“首席收入破坏者”，因为现在不应该再有人购买当前一代的 Hopper 芯片了。

![](https://cdn.thenewstack.io/media/2025/03/3b604b9b-nvidia-dynamo.jpg)

NVIDIA 的 Dynamo 推理框架。

该公司今天宣布的另一个新项目是 [Dynamo](https://nvidianews.nvidia.com/news/nvidia-dynamo-open-source-library-accelerates-and-scales-ai-reasoning-models)，正如 NVIDIA 所描述的，它是一个“开源推理软件，用于加速和扩展 AI 工厂中的 AI 推理模型”。这里的想法是为在企业数据中心运行推理模型提供一个优化的框架。

“世界各地的行业都在训练 AI 模型以不同的方式思考和学习，随着时间的推移使它们变得更加复杂，”Huang 说。“为了实现定制推理 AI 的未来，NVIDIA Dynamo 帮助大规模地服务这些模型，从而在 AI 工厂中节省成本并提高效率。”

为了进一步强调其对推理的整体关注，NVIDIA 还推出了自己的推理模型系列 Llama Nemotron，该模型针对推理速度进行了优化（并且比其所基于的 Llama 模型提高了 20% 的准确性）。
总的来说，今年对GTC主题演讲的反应似乎比去年的活动更为平淡。部分原因可能是因为今年的发布内容不如往年那么多，或者它们在技术上令人印象深刻，但也有些深奥（比如其基于光子学的网络硬件）——但同时也因为这次展会感觉更像是对现状的回应，而不是对未来的展望。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等内容。