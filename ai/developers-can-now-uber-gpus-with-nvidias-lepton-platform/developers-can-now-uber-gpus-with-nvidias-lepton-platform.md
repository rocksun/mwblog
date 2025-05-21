
<!--
title: 开发者现在可以借助NVIDIA的Lepton平台 “Uber” GPU
cover: https://cdn.thenewstack.io/media/2025/04/b4c49fb4-nvidia12.jpg
summary: NVIDIA推出DGX Cloud Lepton平台，开发者可按需租用全球GPU资源，类似“Uber”模式。支持Blackwell、Hopper等GPU，优化AI任务分配。Lepton对接CoreWeave等供应商，提供NVIDIA软件栈支持，简化AI开发流程。或将与云厂商竞争，加速混合云落地。
-->

NVIDIA推出DGX Cloud Lepton平台，开发者可按需租用全球GPU资源，类似“Uber”模式。支持Blackwell、Hopper等GPU，优化AI任务分配。Lepton对接CoreWeave等供应商，提供NVIDIA软件栈支持，简化AI开发流程。或将与云厂商竞争，加速混合云落地。

> 译自：[Developers Can Now ‘Uber’ GPUs With NVIDIA’s Lepton Platform](https://thenewstack.io/developers-can-now-uber-gpus-with-nvidias-lepton-platform/)
> 
> 作者：Agam Shah

你是否迫切需要 NVIDIA GPU？别着急，你很快就可以在网上订购了。

NVIDIA 已经[宣布](https://nvidianews.nvidia.com/news/nvidia-announces-dgx-cloud-lepton-to-connect-developers-to-nvidias-global-compute-ecosystem)一个名为 [DGX Cloud Lepton](https://www.nvidia.com/en-gb/data-center/dgx-cloud-lepton/) 的一站式商店，它将允许开发者租用分布在全球各地主机提供商处的 NVIDIA GPU。

开发者可以登录 Lepton，指定他们的 AI 任务，然后租用相关的 GPU。用 Uber 来类比，GPU 将会来到那些没有时间去寻找 GPU 的开发者面前。

NVIDIA 的 DGX Cloud 副总裁 [Alexis Black Bjorlin](https://www.linkedin.com/in/alexisbjorlin/) 在一次新闻发布会上说：“类似于将乘客与司机联系起来的现代打车应用，DGX Cloud Lepton 提供了一个现代化的市场，将开发者与 GPU 计算连接起来，而不仅仅是本地连接。”

GPU 的可用性并不是一个严重的问题，但是在数十个云服务或独立设施中搜索合适的服务可能会令人头疼。

大量的 NVIDIA GPU 将可供订购，包括 Blackwell，这是他们最新的 GPU。包括 Hopper（ChatGPT 运行在其上）和可能包括 Ampere 在内的旧 GPU 也将可用。

GPU 将取决于任务。如果用户需要对模型进行大规模训练，那么可能是 Blackwell。如果用户需要推理，则可能会分配 Hopper 或 Ampere。如果用户需要低延迟，那么将分配附近区域的 GPU。

## 问题：更多的 GPU 供应商

直到去年，NVIDIA GPU 一直供不应求。微软、OpenAI、亚马逊和 Meta 占据了大部分供应。甚至苹果也无法获得零件，这使得他们在 AI 领域落后了几年，根据彭博社本周的一篇[报道](https://www.bloomberg.com/news/features/2025-05-18/how-apple-intelligence-and-siri-ai-went-so-wrong)。

云提供商[最初](https://www.hpcwire.com/2023/10/16/annual-gpu-upgrades-nvidias-plan-for-faster-chips/)对访问 NVIDIA GPU 收取了高溢价。这些 GPU 仅适用于大型客户。

但是，随着供应的正常化，大量独立的 GPU 提供商涌现出来，以更便宜的价格提供 AI 计算。他们中的大多数以前都从事加密货币挖矿，但随着该市场的兴起，他们将硬件转向了 AI。像 Crusoe Energy 这样的公司，该公司[在 3 月份](https://www.cnbc.com/2025/03/25/crusoe-energy-sells-bitcoin-mining-unit-to-nydig-to-focus-on-ai.html)出售了其比特币挖矿业务，收购了新的 GPU，并开始将它们出租作为 AI 基础设施。另一个例子是 Voltage Park，该公司由一位加密货币高管创立，但现在以每小时 1.99 美元的价格提供一次性的 H100 GPU。

NVIDIA 的 Black Bjorlin 承认 GPU 容量已经增长，并补充说“在高性价比的情况下，在正确的区域找到并有效利用 AI 基础设施可能很复杂。”

## NVIDIA 类似 Uber 的想法

Lepton 提供的 GPU 将来自不太知名的 GPU 提供商，包括 CoreWeave、Crusoe、Lambda、富士康等。目前尚不清楚用户是否可以选择提供商。

Lepton 不包括前 4 大云提供商，但是用户将能够“携带他们的计算和他们当前使用的平台，因此这当然是该平台上的一个选项，”Bjorlin 说。

从字里行间可以看出，NVIDIA 可能会创建自己的云服务，并将与亚马逊、谷歌和微软等也出租 GPU 的公司竞争。

Bjorlin 还表示，Lepton 将对混合云友好，这意味着开发者可能能够将其数据或 AI 工作负载连接到较小提供商处的租赁 GPU。

## 更便宜的替代方案

Lepton 的定价尚未公布，但是该服务需要一些 NVIDIA 软件和工具，这并不便宜。

为了避免 NVIDIA 的溢价，直接从已经是 Lepton 一部分的较小服务提供商那里租用 GPU 可能会更便宜。

Crusoe Energy 的一个完全加载的 NVIDIA H200 GPU [的](https://crusoe.ai/cloud/pricing/)价格，对于为期六个月的单个实例，将使用户花费约 120,000 美元。较慢的 A100 的价格约为一半。

CoreWeave 的 H200 [价格](https://www.coreweave.com/pricing)约为每小时 50 美元。

Lepton 的优势在于其软件后端，它可以处理 [NVIDIA 软件](https://thenewstack.io/nvidia-wants-to-rewrite-the-software-development-stack/)和[硬件开发堆栈](https://thenewstack.io/nvidias-hardware-roadmap-and-its-impact-on-developers/)。开发者可以直接将他们的程序带到 GPU，并消除中间的开发和微服务复杂性。

或者，最好获得在本地运行的硬件，因为 AI 的处理要求也在降低。
NVIDIA 即将开始交付 [DGX Spark](https://thenewstack.io/after-deepseek-nvidia-puts-its-focus-on-inference-at-gtc/)，它提供 1 Petaflop 的性能，并且可以在桌面上运行推理。NVIDIA 的 CEO 黄仁勋在主题演讲中将该硬件描述为“你自己的 AI 云，就在你旁边，并且始终开启，随时等待着你”。

## Lepton 的工作方式

开发者首先需要注册成为 NVIDIA 开发者并创建一个云服务器。之后，开发者可以[申请](https://developer.nvidia.com/dgx-cloud/get-lepton)访问该服务。

我申请该服务目前正在审核中。NVIDIA 在选择用户时似乎很挑剔，仅批准那些能够充分利用其 GPU 并且有资金投入的用户。我申请 beta AI 服务的申请从未获得批准 —— 尽管如此，开发者应该尝试一下。

如果你获得访问权限，你可以从 NVIDIA Build [网站](https://build.nvidia.com/)采用 LLM 或 AI 应用程序，并将它们部署到 Lepton。可以精细地调整任务以部署到计算节点。

用户可以选择作业类型和 GPU，建立具有开发环境的容器，并将 AI 作业分派给 GPU。训练作业将转到高端 GPU，而推理将发送到低端 GPU。

开发者可以配置 GPU 并在 Lepton 界面中管理多台机器。这包括选择容器镜像、选择实例类型（CPU 或 GPU）以及建立变量。NVIDIA 提供了 MPI 和 Torchrun 的模板以帮助入门。

用户还可以在容器中运行 [Jupyter notebooks](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/)。可以通过 SSH、浏览器或其他工具访问该 Pod。Lepton 根据作业和 GPU 类型组织和管理节点。

开发者可以自带硬件以集成到 Lepton 中，从而获得更多自我管理的节点。但是，[庞大的需求清单](https://docs.nvidia.com/dgx-cloud/lepton/guides/nodes/bring-your-own-compute/requirements/)包括每个 GPU 640GB 的存储空间（推荐：20TB NVMe SSD）、高端 x86 服务器 CPU、Ubuntu 22.04 LTS 和 [CUDA](https://thenewstack.io/nvidia-making-radical-changes-to-cuda-after-nearly-20-years/) 12.4.1 或更高版本。

[技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)