<!--
title: MinIO推出MemKV：消除AI“重算税”，提升GPU利用率达95%
cover: https://cdn.thenewstack.io/media/2026/05/f30e3075-ghariza-mahavira-vyyokutbajg-unsplash-scaled.jpg
summary: MinIO发布MemKV，通过PB级分布式上下文存储解决AI“重算税”。它利用RDMA技术提升GPU利用率达95%，降低Token成本50%，助力大规模AI应用。
-->

MinIO发布MemKV，通过PB级分布式上下文存储解决AI“重算税”。它利用RDMA技术提升GPU利用率达95%，降低Token成本50%，助力大规模AI应用。

> 译自：[MinIO's MemKV promises 95% better GPU utilization by ending AI recompute tax](https://thenewstack.io/minio-memkv-recompute-tax/)
> 
> 作者：Adrian Bridgwater

聊天机器人和智能体（Copilots）展现出的智能 AI 服务光鲜亮丽，但这掩盖了目前真正的研发高地：AI 基础设施。本周二，基础数据服务公司 MinIO 推出了一种名为 MemKV 的新型上下文内存存储，旨在解决 AI 基础层中一个根深蒂固的挑战。

上下文内存存储是 AI 模型运行的核心，是一种基于软件的架构逻辑层，旨在保留与模型任务、用户偏好和交互相关的场景数据。

## TTFT（首字生成时间）

这是一个涉及多个专业术语的领域。MinIO 强调其技术能够显著提升 AI 推理负载中的 TTFT（首字生成时间）和 TPOT（每个 Token 的输出时间）。MemKV 通过提供 PB 级、原生基于闪存的上下文内存，并利用 800 [GbE RDMA](https://www.nas.nasa.gov/assets/nas/pdf/papers/NAS_Technical_Report_NAS-2014-01.pdf)（远程直接内存访问）实现端到端的访问，从而在这一领域达到了新的速度。

MemKV 与 AIStor 共同构成了 MinIO 数据基础产品组合的两大支柱。AIStor 是一个为 AI 时代构建的软件定义对象存储平台。MinIO 声称，MemKV 能够为 GPU 集群提供持久化、共享的上下文，其规模是现有内存和存储层无法企及的。

## 什么是重算税（Recompute Tax）？

随着 AI 开始执行复杂的[多步推理任务](https://thenewstack.io/system-two-ai-the-dawn-of-reasoning-agents-in-business/)，内存（或者 AI 行业现在喜欢称之为[上下文](https://www.developerway.com/posts/how-ai-remembers-and-forgets-part1)）经常会丢失，因为最靠近 GPU 的基础设施无法容纳足够的数据。当上下文丢失时，GPU 必须重复已经完成的工作，我们称之为“重算税”，这显然是对时间、能源和资源的巨大消耗。

> “任何执行重算操作的 [GPU](https://thenewstack.io/gpu-orchestration-in-kubernetes-device-plugin-or-gpu-operator/) 都不只是效率低下的问题，它是一种‘结构性拖累’。考虑到超大规模企业和新兴云厂商正在构建的 GPU 密度，这种拖累是行业无法承受的。” —— MinIO 联合创始人兼 CEO, AB Periasamy。

直接点说，MinIO 声称 MemKV “显著降低了” AI 推理负载的重算税。在公司[官方博客](https://www.min.io/blog)发布的代表性基准测试中，MemKV 在生产环境的并发条件下显著缩短了首字生成时间。核心数据包括：GPU 利用率提升 95% 以上，每个 Token 的成本降低约 50%。

MinIO 联合创始人兼 CEO AB Periasamy 表示，任何执行重算动作的 GPU 都不只是效率低下，“它是一种结构性拖累”，考虑到超大规模企业和新兴云厂商正在构建的 GPU 密度，行业无法持续承受这种负担。

## Token 经济学的新融合

HyperFRAME Research 的分析师 Don Gentile 呼吁，AI 领域的对话应从单纯的模型性能转向 Token 经济学以及大规模运营 AI 的成本。

Don Gentile 表示：“这种转变促使人们重新关注系统在推理过程中如何保留和共享上下文。MinIO 的 MemKV 解决了一个昂贵的效率问题：即当上下文无法在 GPU 之间共享时，需要重新运行之前的计算。消除这种摩擦可以提高利用率并降低企业 AI 的成本。”

深入来看，既然现在已经可以实现 PB 级规模的微秒级检索，软件工程师该如何重新思考全球分布式 GPU 集群的状态管理？MinIO CTO Ugur Tigli 告诉 *The New Stack*，开发者真的应该“停止将上下文视为随用随弃的草稿”，而应将其视为真正的“状态”，更接近于持久化存储。

## 欢迎来到上下文即服务（Context-as-a-Service）

“有了 MemKV，上下文变成了持久的、可寻址的状态，你可以保存、共享和重新加载——它更像是一个数据库行或一个对象，而不是一个缓存条目，” Ugur Tigli 说，“把它想象成一个提供‘上下文即服务’的思想模型：一个共享的大脑，每个推理副本、每个智能体、甚至每个租户都从中读取数据，而不是在每次调用时都从头开始重建相同的上下文。”

在软件开发者的实际操作层面，Ugur Tigli 解释了实践中会发生的三个变化。

首先，开发者可以使服务层实现无状态化，将会话和智能体状态放入 MemKV，而不是将其绑定到单个 GPU 上。任何副本都可以在中途接管任何对话，调度器会将请求路由到任何空闲的 GPU，然后 GPU 在微秒内从 MemKV 中提取缓存的上下文。不再需要粘性会话，没有副本亲和性，Pod 重启时也不会丢失线程。

## 不要大海捞针式处理上下文

其次，开发者可以按区域部署，而不是全球部署；他们不必尝试在各大洲之间镜像每一字节的上下文。他们可以在每个 GPU 集群本地部署一个 MemKV 实例。

“不要把 MemKV 想象成需要同步复制的持久存储，要将地理位置的选择视为一种性能选择，而不是正确性选择，” Ugur Tigli 说道。

> “开发者不再需要围绕缓存淘汰来设计架构——上下文被持久地卸载，并在微秒内（而非毫秒）即可检索。” —— MinIO CTO, Ugur Tigli

第三，他解释说，团队可以明确规定哪些数据保留，哪些数据删除。这意味着软件工程师可以固定活跃会话的键值（Keys），这样它们就不会在负载下被淘汰。他们还可以将热门前缀（长系统提示词、频繁检索的 RAG 段落）与每个用户的状态分开缓存，这样单个活跃用户就不会把共享资源挤出存储。

“这一切都意味着，在开发者的推理工作流中，重算税消失了，” Ugur Tigli 说，“对于基于文件的存储，当 GPU 内存耗尽键值（KV）缓存时，上下文要么被淘汰，要么必须重新计算——而专门的 KV 存储消除了这一点。开发者不再需要围绕缓存淘汰来设计架构——上下文被持久地卸载，并在微秒内（而非毫秒）即可检索。”

## 深入更安全的数据层？

随着我们将智能体 AI 的开发讨论深入到基础设施层，对稳健性的新责任也随之凸显。

暴露管理平台公司 ArmorCode 的首席安全与信任官 Karthik Swarnam 告诉 *The New Stack*，AI 推理对上下文内存存储的需求，代表了企业在 AI 信任持续性方面面临的另一个重大挑战。

“仅仅保护模型本身是不够的。组织还需要保护内存层，因为它决定了 AI 系统随着时间的推移保留、召回和执行哪些上下文，” Karthik Swarnam 说，“随着这些系统变得更加持久和互联，攻击面超出了提示词，扩展到了上下文数据，这些数据可能会以难以检测的方式被操纵、污染或暴露。”

从安全态势的角度来看，Karthik Swarnam 表示，这一现实引发了关于出处、访问控制、保留策略的重要问题，以及企业是否能可靠地追踪 AI 决策随时间受到的影响。他指出，行业开始意识到，内存基础设施对于 AI 治理和安全的重要性正变得与模型本身不相上下。

## 拥抱 NVMe（非易失性内存标准）

与将文件存储架构强行适配到推理数据路径的方法不同，MemKV 通过端到端的 RDMA 传输，将数据直接从 NVMe（非易失性内存标准）移动到 AI 数据路径，没有 HTTP 开销，没有文件系统转换，GPU 与其上下文之间也没有存储服务器。

CEO Periasamy 和 CTO Tigli 的核心观点是：当今智能体功能所需的 Token 使用规模，要求必须有专门为推理数据路径构建的技术，才能保证其良性的经济产出。两人表示，这就是 MemKV 设计和开发的初衷。