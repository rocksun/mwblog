
<!--
title: 英伟达硬件路线图及其对开发者的影响
cover: https://cdn.thenewstack.io/media/2024/08/cfa6ce46-boliviainteligente-eywlm1f0vu0-unsplash.jpg
-->

英伟达修订后的 GPU 路线图对开发人员意味着什么。其中一项是 Python 将成为其 CUDA 并行编程框架的一等公民。

> 译自 [Nvidia’s Hardware Roadmap and Its Impact on Developers](https://thenewstack.io/nvidias-hardware-roadmap-and-its-impact-on-developers/)，作者 Agam Shah。

英伟达是[人工智能繁荣的最大受益者](https://thenewstack.io/nvidia-ceo-details-a-new-ai-way-of-developing-software/)，并从[GPU 销售](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/)中赚取大量现金。现在，它正在实施一项前所未有的计划，计划在 2027 年之前每年发布一款 GPU。

“我们的基本理念非常简单，”英伟达首席执行官黄仁勋在 6 月的台北电脑展上表示。“构建整个数据中心规模的解耦系统，并以一年的节奏将各个部分出售给您。我们将所有东西都推向技术极限。”

> 英伟达未来的 GPU 表明正在向混合精度计算进行多元化转变，混合精度计算将传统计算与人工智能计算结合在一起。

[微软](https://news.microsoft.com/?utm_content=inline+mention) 和 Meta 等公司正在投资数十亿美元用于建设新的数据中心，并希望获得最新、最强大的 GPU。因此，英伟达正在以前所未有的速度创新硬件技术。

金融分析师认为，该公司的股价处于不可持续的水平。就像互联网泡沫一样，人工智能泡沫也会破灭，英伟达的股价将回归现实。但英伟达 GPU 和进步的影响将永久地体现在软件开发中。

## GPU 路线图

英伟达的目标是让 GPU 成为运营中必不可少的工具，就像过去几年中的 CPU 一样。英伟达首席执行官黄仁勋认为，CPU 不够，需要 GPU 来更快地处理数据。

“软件惯性是计算机中最重要的事情。当计算机向后兼容所有已创建的软件时，你的上市速度会快得多，”黄仁勋在最近的一次活动中表示。

> 所有新的 GPU 都配备了更快的网络芯片和互连，以实现更快的服务器和芯片通信。

英伟达的旗舰 GPU 称为 Hopper，为微软、Meta 和 OpenAI 提供人工智能支持。OpenAI 和微软正在英伟达的 Hopper H100 及其前身 A100 GPU 上提供 GPT-4 和 4.0。

微软已经为下一代 GPU（称为 Blackwell）下了订单，这些 GPU 将最早于明年出现在其数据中心。

但由于英伟达在芯片制造方面遇到了技术挑战，Blackwell 的出货日期存在疑问。

“这是前所未有的计算和功率密度，考虑到所需的系统级复杂性，爬坡证明具有挑战性，”SemiAnalysis 的分析师[在一份报告中](https://www.semianalysis.com/p/nvidias-blackwell-reworked-shipment)表示。

分析师表示，Blackwell 的挑战是全面的，包括电源传输、过热、泄漏和复杂性。

Blackwell 拥有 2080 亿个晶体管，使其成为有史以来最复杂的芯片之一。最多可以将 72 个 Blackwell 集成到一个机架服务器中，英伟达正在提供连接，通过以太网连接多达 576 个 GPU。这是一种强大的 AI 能力。

英伟达正在将 Blackwell GPU 与其基于 ARM 的 Grace CPU 配对。英伟达正在用这些芯片出货自己的服务器，这些服务器可在云中使用。英伟达试图淘汰传统的编程模型，这些模型将英伟达的 GPU 与英特尔或[AMD](https://www.amd.com/en/products/processors/server/epyc/google-cloud.html?utm_content=inline+mention) 的 x86 处理器配对。

英伟达明年将出货 Blackwell Ultra，它与 Blackwell 一样，将包括 HBM3E，但容量更大。之后，英伟达将在 2026 年推出其 Rubin 平台，该平台将包括全新的 GPU 和 CPU，并支持 HBM4 内存。2027 年，英伟达将发布 Rubin Ultra GPU。

所有新的 GPU 都配备了更快的网络芯片和互连，以实现更快的服务器和芯片通信。

“这基本上是英伟达正在构建的东西，以及所有基于它的软件的丰富性，”黄仁勋说。

## 对开发者的意义

英伟达未来的 GPU 表明正在向混合精度计算进行多元化转变，混合精度计算将传统计算与人工智能计算结合在一起。

> 英伟达正在将其 CUDA 并行编程框架中的 Python 提升为一等公民。

该公司正在放弃其 GPU 对 64 位精度的关注，这对于精确计算至关重要。相反，它正在开发硬件功能来提升概率人工智能计算中使用的较低精度 4 位、8 位和 16 位数据类型。

英伟达在其 GPU 中封装了更多张量核心，用于矩阵乘法。一种名为 GEMM 的算法是英伟达 AI 模型的核心，因为它利用了张量核心，并与[CUDA](https://thenewstack.io/nvidia-hones-in-on-apple-like-approach-to-ai-with-cuda/) 中的库一起工作，供程序员与 GPU 核心交互。

首先，英伟达希望吸引更多开发者加入其阵营。开发者需要了解 [C++](https://roadmap.sh/cpp) 和 Fortran 用于 GPU 编程，但英伟达希望支持更多编程语言，包括 [Rust](https://roadmap.sh/rust) 和 [Julia](https://thenewstack.io/julia-language-gaining-in-enterprise-cred/)。

英伟达正在将其 [Python](https://roadmap.sh/python) 打造成其 CUDA 并行编程框架中的一等公民，包括扩展 SDK 和框架对 Python 的访问权限。该公司不会停止为其 C++ 库加油，这些库是解锁英伟达部分 GPU 功能所必需的。

但需要注意的是：一旦开发者陷入 CUDA，就很难摆脱。

## 能效

> 英伟达的目标是实现更高效的编码，减少循环以提供计算结果。

英伟达声称其 GPU 是绿色的，但芯片圈内人士之间一直流传着一个笑话，那就是英伟达唯一绿色的东西是它的 logo。英伟达的 Blackwell GPU 是一款耗电量高达 1200 瓦的怪兽，需要液冷。

即将推出的 GPU 将消耗巨大的电力，但也将提供最快的结果。Blackwell 将支持新的低精度数据类型——FP4 和 FP6——这些数据类型可以提高每瓦性能。

英伟达还提倡更高效的编码，减少循环以提供计算结果。即将推出的 GPU 将包含软件层，这些软件层将把任务重定向到正确的核心。这也将减轻编码人员的压力。

## AI 超级模型

英伟达的 GPU 和软件策略正在同步发展。目标是构建巨大的 GPU 集群，能够处理具有数万亿参数的 AI 模型。

与此同时，英伟达正在创建一个“AI 超级模型”框架，开发者可以在其中使用大型语言模型，并通过插入定制模型、护栏、检索增强生成 (RAG) 等工具对其进行优化。

英伟达已经针对其 AI 超级模型策略优化了开源 [Llama 3.1](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/)。开发者可以使用一系列适配器、大型语言模型的低秩自适应 (LoRA) 模型和护栏来武装 Llama 3.1 模型，以创建自己的模型。

英伟达有一个复杂的流程来创建 AI 超级模型。开发者需要弄清楚优化模型的成分、输入本地化数据并确定适配器。开发者需要实施程序来提取和推送相关数据到 [向量数据库](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/)，该数据库评估信息并向用户发送响应。

开发者需要完善 CUDA 并了解 [NIMs](https://thenewstack.io/developers-get-ready-for-nvidias-nim-based-ai-app-store/)（英伟达推理微服务），它们是英伟达网站上的云原生 AI 容器。

## 竞争
英伟达的竞争对手英特尔和 AMD 正在尽一切努力阻止开发者远离英伟达的 CUDA。

包括英特尔和富士通在内的数十家公司组成了一个名为 [UXL Foundation](https://uxlfoundation.org/) 的联盟，以开发 CUDA 的开源替代方案。

UXL 的并行编程框架建立在英特尔的 OneAPI 之上。目标很简单：代码中只需进行少量更改，程序就可以在英伟达和非英伟达 AI 加速器上运行。

当然，UXL 还提供了一个工具来剥离 CUDA 代码，以便程序可以在其他 AI 芯片上运行，包括 FPGA、ASIC 等。

AMD 有 ROCm，尽管炒作很多，但它还没有成熟。

所有竞争对手都使用开源工具，除了内部工具来创建在专有硬件上运行 AI 的神经网络。

但英伟达凭借 CUDA 比其竞争对手领先近十年，CUDA 于 2006 年开始用于高性能计算，后来成为 AI 的一股力量。
