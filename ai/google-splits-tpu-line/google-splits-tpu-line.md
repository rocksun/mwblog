<!--
title: Google 拆分 TPU 产品线：TPU 8t 专攻训练，TPU 8i 领跑智能体推理
cover: https://cdn.thenewstack.io/media/2026/04/91c5d628-img_3656-scaled.jpg
summary: Google 推出 TPU 8t 和 8i，分别针对 AI 训练与推理。这是为了应对智能体时代下两种负载的差异。TPU 8i 侧重突破内存墙，优化推理延迟；TPU 8t 则专注于大规模训练集群的性价比。此举与 AWS 的统一策略形成对比。
-->

Google 推出 TPU 8t 和 8i，分别针对 AI 训练与推理。这是为了应对智能体时代下两种负载的差异。TPU 8i 侧重突破内存墙，优化推理延迟；TPU 8t 则专注于大规模训练集群的性价比。此举与 AWS 的统一策略形成对比。

> 译自：[Google splits its TPU line in two for the agentic era](https://thenewstack.io/google-splits-tpu-line/)
> 
> 作者：Frederic Lardinois

在 Google 的 Tensor Processing Unit（TPU）长达十年的历史中，大部分时间里 Google 每一代只发布一款芯片——有时虽然 SKU 有所不同，但都基于相同的架构。该架构既要承担前沿模型的预训练任务，又要负责这些模型的推理运行。现在，Google 认为随着这两种模式的日益分化，是时候改变这种现状了。

在周三的 Google Cloud Next 大会上，该公司推出了 TPU 8t 和 TPU 8i，这是两款分别为训练和推理量身定制的独立芯片。Google 的论点是，智能体工作负载已使得单一加速器无法在两者中都达到最优，因此在最前沿领域持续提升性价比的唯一途径就是停止这种“一刀切”的尝试。

![](https://cdn.thenewstack.io/media/2026/04/d0c7972f-tpu-8t-l-and-tpu-8i-r-with-boards-1024x421.jpg)

## 两款芯片，同属一个家族

TPU 8t 保留了 3D 环面互连（3D torus interconnect），这是一种网络拓扑结构，将芯片连接成一个三维网格，每个维度都像环一样环绕，使每块芯片都能与其最近的六个邻居直接连接。它还保留了 Google 标准的 SparseCores，用于加速嵌入查找（embedding lookups）中不规则的内存访问模式。

TPU 8i 则将这些 SparseCores 替换为全新的片上集合通信加速引擎（on-die Collectives Acceleration Engine）。Google 表示，该引擎能将全局同步操作的延迟降低高达 5 倍，而这类操作在思维链（chain-of-thought）解码和专家混合模型（Mixture-of-Experts）路由中占据主导地位。此外，网络拓扑结构也发生了变化。

![](https://cdn.thenewstack.io/media/2026/04/20bd29b5-img_3662-1024x768.jpg)

*图片来源：The New Stack。*

> Google 的论点是，智能体工作负载已使得单一加速器无法在两者中都达到最优，因此在最前沿领域持续提升性价比的唯一途径就是停止这种尝试。

TPU 8i 弃用了 3D 环面，转而采用一种受 Dragonfly 启发的新布局，称为 Boardfly：这是一种分层拓扑结构，在小组内实现芯片全互连，然后通过直接光纤长途电缆将各组相互连接，而不是通过网格路由流量。环面结构是为相邻通信而设计的，而 Dragonfly 则是为了在系统中任意两块芯片之间建立短路径。Google 表示，新布局将 1,024 块芯片组成的 pod 的最大跳数从 16 跳减少到了 7 跳。

关于 TPU 8i 最重要的一点是，Google 设计它是为了打破“内存墙”。该芯片将片上 SRAM 增加了两倍，达到 384 MB，并将 HBM 容量推高至 288 GB。Google 表示，这足以让长上下文推理模型的键值（KV）缓存完全驻留在硅片上。

对于智能体工作流，每一次片外内存访问都会导致面向用户的响应延迟，并在多个推理轮次中累积。将工作集保留在片上就是制胜的关键。

这就是为什么 TPU 8i 拥有比 TPU 8t 更高的单芯片带宽的原因。如果你仍然认为训练是更繁重的工作负载，这听起来可能有些违背直觉。事实上，训练是受计算限制的（compute-bound），而智能体推理则是受内存限制的（memory-bound）。

![](https://cdn.thenewstack.io/media/2026/04/9e253462-tpu-8i-rack-683x1024.jpg)

*TPU 8i 机架。图片来源：Google。*

## 为什么是现在？

一年前，Google 基本上还认为不需要这种拆分。当该公司发布 Ironwood（第七代 TPU，目前仍是通用市场的主力产品）时，将其定位为“首款迎接推理时代的 Google TPU”。它宣传同一款硅片可用于预训练、训练和大规模服务。

但训练和推理的需求向来有所不同。过去一年发生的变化是，推理本身改变了。早期类聊天机器人系统的传统推理——一个提示词，一个响应——属于一种工作负载。但智能体推理则完全不同：主智能体将目标分解为子任务，并分配给一组在长循环中进行推理的专门智能体。这给键值（KV）缓存大小、全对全集合通信和尾部延迟带来了巨大的压力。

模型也在发生变化，人们更加关注专家混合模型（Mixture-of-Experts）系统，这是高内存带宽受益的另一个领域。

![](https://cdn.thenewstack.io/media/2026/04/e7d047ab-tpu-8t-1024x683.jpg)

*TPU 8t 芯片。图片来源：Google。*

训练工作负载也并非停滞不前。前沿模型现在需要数十万块芯片组成的集群，才能在合理的时间内收敛。一个 TPU 8t superpod 可扩展至 9,600 块芯片，Google 表示其全新的 Virgo 数据中心网络和 Pathways 软件可以将超过一百万块 TPU 8t 芯片拼接成一个单一的逻辑训练集群。

Google 声称 TPU 8t 在训练方面的性价比比 Ironwood 提高了约 2.7 倍，而 TPU 8i 在推理方面的性价比提高了 80%。这些数据能否在客户的基准测试中站稳脚跟则是另一个问题。

![](https://cdn.thenewstack.io/media/2026/04/085d5552-img_3660-1024x768.jpg)

## 与 AWS 截然相反的赌注

与 AWS 的做法相比，这种分化读起来非常有意思。在 re:Invent 2025 上，Amazon 发布了 Trainium3，并明确表示该芯片将同时处理训练和推理任务。其 Inferentia 系列实际上已经[逐渐淡出](https://www.benzinga.com/media/24/12/42356920/amazon-halts-inferentia-ai-chip-development-to-take-on-nvidia-how-trainium-is-shaping-up-to-be-the-new-weapon-in-ai-chip-wars)。AWS 的论点是，随着模型变得更大、推理链变得更长，推理正变得越来越像训练，训练优化和推理优化硅片之间的差距正在缩小而非扩大。

Google 的第八代 TPU 则是针对这一论点的公开博弈。

Nvidia 占据了中间立场。Vera Rubin NVL72 是 Google 通过其新的 A5X 裸机实例转售的平台，它是可以在单个机架上同时进行训练和推理的系统。从单芯片来看，Nvidia 的 Rubin GPU 比任何一款 TPU 8 变体都强大得多，每块 GPU 拥有约 50 PFlops 的 NVFP4 推理能力，而每块 TPU 8i 芯片为 10.1 FP4 PFlops。但按 pod 计算，情况就反转了：一个 NVL72 机架的峰值推理性能接近 3.6 ExaFlops (NVFP4)，而一个包含 1,152 块芯片的 TPU 8i pod 的 FP8 推理性能可达 11.6 ExaFlops。

两家公司正试图实现相似的结果，但哲学不同：Nvidia 倾向于通过 NVLink 连接更少、更强悍的芯片；Google 则倾向于通过自定义网络连接大量更小的芯片。

## 客户实际上得到了什么

两款芯片都将于今年晚些时候发布，具体正式上市（GA）时间尚未指明，届时将通过 Google 的 AI Hypercomputer 架构提供。

有两个关于客户的故事比主题演讲所展示的框架更为重要。TPU 8t 和 8i 是首批提供裸机访问权限的 TPU，这意味着客户可以自行管理主机，而无需通过 Google 的虚拟机（VM）层。这是对一类特定工作负载的让步——包括底层内核开发、延迟敏感型推理、第三方独立软件供应商（ISV）——这些客户历来默认选择 Nvidia。

TPU 原生支持 PyTorch（Google 称之为 TorchTPU）目前已进入预览阶段。JAX 一直是 TPU 上的顶级框架，而自从 TPU 向外部客户销售以来，PyTorch 的支持一直略显尴尬。如果 TorchTPU 在生产环境中运行良好，它将消除开发者默认选择 GPU 基础设施的最持久理由之一。

## 是有效吞吐量，而不只是 FLOPs

在 10,000 块或更多芯片的训练规模下，峰值 FLOPs 与实际有用的 FLOPs 之间的差距可能巨大。一块芯片的卡顿就可能拖慢同步任务，而每一次检查点重启都是集群未在进行训练的时间损失。

> Google 内部的赌注似乎是，智能体时代不会像预训练时代那样垂青单一的通用加速器。

Google 表示 TPU 8t 的目标是实现 97% 的“有效吞吐量”（goodput），这是指预置计算资源中执行生产性工作的比例。“有效吞吐量”并不是一个容易让人爱上的术语，但 Google 似乎很热衷于使用它。

Google 内部的赌注似乎是，智能体时代不会像预训练时代那样垂青单一的通用加速器。

## 硬件路线图上的其他内容

第八代 TPU 虽然是重头戏，但它们只是更广泛的基础设施更新的一部分。

Google 还宣布了基于 NVIDIA Vera Rubin NVL72 的 A5X 裸机实例；Axion N4A，这是基于 Google 自研 CPU 的全新 Arm 架构 VM 家族（现在是 TPU 8t、TPU 8i 和 N4A 的主机，使 Axion 成为针对 Nvidia Grace 和 Vera 的结构性回应）；Virgo 网络架构，它能以 47 Pb/s 的对分带宽连接 134,000 块 TPU 8t 芯片；Managed Lustre，支持 10 TB/s 和 80 PB；以及 Cloud Storage 上的 Rapid Buckets，为检查点工作提供亚毫秒级延迟；具有 168 TiB 本地 SSD 的 Z4M 虚拟机，用于 ISV 构建的并行文件系统；以及 GKE 更新，包括具有机器学习驱动、延迟感知路由功能的推理网关。

所有这些组件都旨在无缝协作。Virgo 的带宽目标是根据 TPU 8t 的并行需求设定的。专用的 KV 缓存存储子系统是根据 TPU 8i 的片上占用空间设计的。Axion 的拓扑结构经过优化，旨在消除 TPU 主机的瓶颈。