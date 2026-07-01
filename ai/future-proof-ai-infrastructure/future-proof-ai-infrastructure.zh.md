在过去的两年里，AI基础设施竞赛一直被一个问题所主导：谁拥有最快的GPU？Jim Keller认为这正在成为一个错误的问题。

在[最近接受 *EE Times* 采访时](https://www.eetimes.com/jim-keller-on-tenstorrents-blackhole-scaling-and-ipo-ambitions)，这位 Tenstorrent 的首席执行官指出，一个组织目前能做的风险最大的举措，就是为其当前运行的模型优化其 AI 基础设施。这并不是因为这些模型不好，而是因为 18 个月后，它们将不再是该公司运行的主流模型。[Keller](https://www.linkedin.com/in/jimbkeller/) 引用了 Rent 规则和 Amdahl 定律，论证了内存、网络和系统级的平衡，现在比峰值浮点性能更重要。

> 这并不是因为这些模型不好，而是因为 18 个月后，它们将不再是该公司运行的主流模型。

这听起来像是 Keller 的产品推销词，但背后有真正的份量，因为 AI 的演进速度比其底层的基础设施更快。而那些花费数亿美元围绕一代模型进行构建的公司，现在正面临着不得不推倒重来所带来的高昂成本。

这种担忧被称为“锁定效应”，它正在重塑 AI 领域的巨头们对硬件的思考方式。

## 工作负载超越了 GPU

在 2023 年和 2024 年，AI 基础设施是一个相对简单的采购问题：训练大语言模型，将它们提供给用户，并购买尽可能多的 Nvidia 能提供的 GPU。工作负载是可以预测的，GPU 处理得很好。

随后，AI 的发展超越了它所构建的基础设施。

推理模型花费更多时间来解决问题，而不是直接跳转到答案。代理（Agent）在完成任务前会在 API、数据库和代码之间跳转。多模态模型混合了文本、图像、音频和视频。这些工作负载中没有哪一个能以同样的方式对硬件造成压力——这迫使基础设施团队重新思考两年前看来完全合理的假设。

> AI 的发展超越了它所构建的基础设施。

没有单一的芯片架构能同样出色地处理所有这些任务。构建 AI 基础设施的组织开始意识到，问题不仅在于*哪个加速器最快*，而在于*我们如何构建系统，使其不必在 AI 每一次飞跃时都被拆解？*

## Nvidia 已经在兜售一个答案

看看 Jensen Huang 一直在谈论的内容，那已经不再是单纯的 GPU 了。

在 GTC 2026 上，Nvidia [发布了 Vera Rubin 平台](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)——七款旨在作为单一系统运行的芯片：Rubin GPU、Vera CPU、NVLink 6 交换机、ConnectX-9 网络、BlueField-4 DPU 等。Vera CPU 的存在是为了处理代理式 AI（agentic AI）中繁重的 CPU 工作——工具调用、代码执行、编排。Nvidia 将这些部署称为“AI 工厂”，这种用词是有意为之的。他们销售的是完整的基础设施，而非单个加速器。

当这家占据 70% 市场份额的公司不再以 GPU 基准测试为先导，转而谈论系统级协同设计时，这就告诉你这个市场的重心正在向何处移动。

这种重构至关重要。当这家占据 70% 市场份额的公司不再以 GPU 基准测试为先导，转而谈论系统级协同设计时，这就告诉你这个市场的重心正在向何处移动。算力仍然很重要。但 Nvidia 正在通过其产品架构（如果不是通过营销的话）承认，单纯的加速器原始性能不足以应对未来的挑战。

## 超大规模企业设计自己的硅片

AMD 也看到了同样的问题，尽管它采取了不同的路径。[Helios](https://www.amd.com/en/newsroom/press-releases/2026-1-5-amd-and-its-partners-share-their-vision-for-ai-ev.html) 将 CPU、GPU 和网络集成到一个机架规模的平台中，这反映出一种更广泛的转变，即不再将 GPU 视为宇宙的中心。其主张并不是“我们的加速器更快”，而是芯片周围的基础设施与芯片本身同样重要。

超大规模企业（Hyperscalers）用它们的钱包践行这一主张的时间更长。Google 花了十年时间协同设计其 [TPU 硅片、互联和软件框架](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/)——其第七代 Ironwood 芯片现已全面上市——使其对整个技术栈拥有了不同寻常的控制力。Amazon 则走了相反的方向，为不同的工作构建了[独立的芯片](https://aws.amazon.com/ai/machine-learning/trainium/)：Trainium 用于训练，Inferentia 用于推理，目前 Trainium3 已投入生产并服务于 Anthropic 等客户。微软的 [Maia 200](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/) 旨在降低推理成本，同时该公司也在部署 Nvidia 的 Vera Rubin NVL72 用于训练和实验——这可以说是市场上最务实的双轨策略。

在它们背后是 Broadcom，其 AI 半导体收入最近在一个季度内突破了 [100 亿美元](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-first-quarter-fiscal-year-2026-financial)，这是由对定制加速器和数据中心交换机的惊人需求所驱动的。Broadcom 为 Google、Meta 等公司设计定制加速器，同时供应在数据中心规模上连接这些加速器的 Tomahawk 和 Jericho 交换机硅片。预计 2026 年定制 ASIC 的出货量将同比增长约 45%——是商用 GPU 增长率的三倍。

此外，还有一些公司认为制造更好的 GPU 并不是答案。

Cerebras 质疑是否需要数千个互连芯片，转而选择了晶圆级处理器，让更多的工作负载保持在同一块硅片上。Groq 采取了相反的方法，几乎完全针对推理进行优化。SambaNova 专注于企业 AI，构建的系统更看重高效地服务多个模型，而不是追求最快的基准测试结果。

## 适应性胜过原始速度

第一波生成式 AI 奖励的是那些能购买最多算力的人。当大多数组织都在解决同一个问题时，这很有意义。今天，AI 工作负载的变化如此之快，以至于基础设施团队开始为不同的目标进行优化：适应性。

Keller 的例子说明了这一点。Tenstorrent 的 BlackHole 架构使用标准以太网代替了专有互连，使其硬件能够与现有的 GPU 部署并列放置，而不是取而代之。Keller 告诉 [EE Times](https://www.eetimes.com/jim-keller-on-tenstorrents-blackhole-scaling-and-ipo-ambitions)，一位客户使用 Tenstorrent 的 Galaxy 服务器来增加他们已拥有的 GPU 的令牌吞吐量，而不是从零开始重建他们的基础设施。

Tenstorrent 的方法是否会成为行业标准几乎无关紧要。

更宏大的理念已经在传播。在整个行业中，公司花费在研究如何构建最快 AI 硬件上的时间变少了，而花在研究如何构建不必在 AI 每一次飞跃时都被更换的硬件上的时间变多了。

## 现在重要的问题

没有人知道三年或五年后的 AI 工作负载会是什么样子。这就是问题所在。

基础设施的更新周期以年为单位衡量。AI 模型似乎每隔几个月就会自我重塑。在今天的工作负载周围进行构建，开始看起来像是一场高风险的赌注，因为明天可能需要完全不同的东西。

> 基础设施的更新周期以年为单位衡量。AI 模型似乎每隔几个月就会自我重塑。

每家公司都在以自己的方式做出响应。他们有不同的策略，但都在问同一个问题：**你如何构建能够超越其上运行的 AI 的基础设施？**

这可能被证明是一个比构建下一个打破纪录的加速器更重要的工程挑战。正是这一挑战在驱动着从 Nvidia 和 AMD 到 Google、Amazon、Broadcom 和 Tenstorrent 的所有公司。