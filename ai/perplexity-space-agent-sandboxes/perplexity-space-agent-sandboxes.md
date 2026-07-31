<!--
title: “有状态系统极难构建”：Perplexity 如何思考 AI 智能体沙箱架构
cover: https://cdn.thenewstack.io/media/2026/07/1362eeb5-tsd-studio-ydarxoa1usm-unsplash-scaled.jpg
summary: Perplexity 推出的 SPACE 沙箱平台旨在解决 AI 智能体长期运行中的状态管理难题。通过利用 Btrfs 文件系统实现高效的快照与分支，SPACE 大幅提升了智能体任务的持久性、可移植性及性能，为大规模 AI 智能体协作提供了基础设施保障。
-->

Perplexity 推出的 SPACE 沙箱平台旨在解决 AI 智能体长期运行中的状态管理难题。通过利用 Btrfs 文件系统实现高效的快照与分支，SPACE 大幅提升了智能体任务的持久性、可移植性及性能，为大规模 AI 智能体协作提供了基础设施保障。

> 译自：[“Stateful systems are incredibly hard to build”: How Perplexity thinks about AI agent sandboxes](https://thenewstack.io/perplexity-space-agent-sandboxes/)
> 
> 作者：Frederic Lardinois

“有状态系统极难构建”：Perplexity 如何思考 AI 智能体沙箱架构

AI 智能体的沙箱似乎已经是一个被解决的问题。毕竟，像 Firecracker 这样由 AWS 开发用于支持其 Lambda 服务的开源 microVM 技术，已经提供了现成的强隔离方案；此外，越来越多的初创公司也在销售[针对智能体工作负载的托管沙箱](https://thenewstack.io/agent-runtime-application-server/)。

尽管如此，Perplexity 还是决定推倒重来，因为团队确信隔离并不是真正的难题所在。

7 月 15 日，该公司推出了 SPACE，这是一个现正运行于其[知识工作智能体平台](https://thenewstack.io/ai-agents-knowledge-workers/) Computer 底层的沙箱平台。

![](https://cdn.thenewstack.io/media/2026/07/a3e666ae-1516431438094.jpeg)

*Perplexity 的 Nate Kupp*

在接受 *The New Stack* 采访时，Perplexity 基础设施副总裁 [Nate Kupp](https://www.linkedin.com/in/natekupp/) 表示，真正的工程挑战在于状态管理——即在 Perplexity 用户为其 [Computer](https://www.perplexity.ai/products/computer) AI 助手启动的数百万个沙箱中，实现对有时运行长达数天甚至数周的智能体会话进行暂停、恢复和分支。

“我们不断回顾并意识到，我们的需求以及我们规模下智能体系统的需求，与现有玩家所提供的方案有着很大不同，”Kupp 说道。

他表示，团队希望智能体能够“暂停、恢复并执行任务，不仅是几个小时，而是几天甚至几周”，并让这些会话作为持久、耐用的制品存续下去。

## 状态是难点

需要注意的是，SPACE 并没有试图重构技术栈的最底层。Kupp 表示，团队使用 Firecracker 作为核心构建块，并使用 Kubernetes 进行云端部署，从设计之初就将跨环境的可移植性（从云端到本地数据中心再到笔记本电脑）作为目标。

大部分工作实际上位于这些 microVM 之上的控制平面。Kupp 称，当 Computer 的智能体工具将上下文引入沙箱时，系统必须快速暂停和恢复会话，将它们迁移到其他集群，并保持它们的“可移植性和可分支性，以便我们能够分叉并在不同方向运行不同的线程”。

事实证明，这一切的基础是 [Btrfs](https://wiki.archlinux.org/title/Btrfs)，即 Linux 的写时复制（copy-on-write）文件系统，它使得快照和分支成为廉价的元数据操作，而不是全量复制。“这在很大程度上是我们取得性能突破的关键，”Kupp 说，并且对于 SPACE 构建所围绕的暂停、恢复、快照和分支操作来说，“这是一个非常自然的选择”。“我们做了一些早期原型，很快发现这非常合适，于是就沿用了下来，”他说。

在此之上，是公司发布文章所描述的包含实时内存的完整会话状态的滚动快照。这些快照每分钟进行一次，会话最多可以回溯一周。

与现有提供商相比，Kupp 说：“在我们关心的所有性能指标上，我们看到了 3 倍甚至更高的速度提升，而且成本方面也有显著改善。”他说，团队还在尾部延迟上投入了大量精力，优化了 P95 和 P99 的保障，因为沙箱性能直接处于用户的关键路径上。

“有状态系统极难构建，”Kupp 说道，他指出了 Perplexity 在运行数百万个沙箱时必须满足的耐用性和正常运行时间保障。

## 控制旋钮，而非权衡

当谈到安全性与性能之间的权衡时，Kupp 认为：“这与其说是权衡，不如说是我们必须考虑如何将控制旋钮放在正确的位置，让客户能够自主控制。”因为每个客户都会将 Computer 接入到 Salesforce、Slack、Snowflake 以及其他数据源的不同组合中，而每个数据源都有其自身的风险特征。

除了他所谓的 RBAC 和其他核心企业功能的“入场券”工作外，Kupp 表示团队正专注于 [智能体安全性](https://thenewstack.io/ai-agents-are-creating-a-new-security-nightmare-for-enterprises-and-startups/)，包括为下游系统提供即时访问权限，并在单个工具调用层面设置控制。

他说，管理员可以禁止任何写访问权限，这样智能体就完全无法写入业务系统，这是一种硬性的平台级限制，而不是留给模型行为去判断。Computer 还会标记敏感操作并提升至用户进行审批。SPACE 尚未使用的技术之一是硬件支持的机密计算，尽管 Kupp 指出公司在其技术栈中与 Nvidia 有着密切合作。

## 沙箱无处不在

目前的 SPACE 沙箱在很大程度上是同构的，即针对 Computer 的工作负载进行了统一大小的调整。Kupp 说，这种情况将会改变，因为“我们将以 [API 产品](https://thenewstack.io/perplexity-agent-api/) 的形式提供此服务”，并为更多异构的外部工作负载提供沙箱大小的灵活性。

Perplexity 此前已于 3 月宣布了一个更精简的 [Sandbox API](https://www.perplexity.ai/hub/blog/sandbox-api-isolated-code-execution-for-ai-agents)，这是一个为构建在 Kubernetes pod 而非 microVM 上的智能体提供的代码执行服务，后续将进行内测。公司还表示，Computer 很快将支持第三方沙箱，而不仅限于 SPACE。“我们已经在技术栈的每个层面考虑了这些扩展点，从沙箱层到 API 和 MCP，”Kupp 说。

Kupp 还在向下看技术栈，关注本地和混合部署。他说，Perplexity 一直在与 Nvidia 合作，利用这家芯片制造商的 RTX Spark 平台进行本地 AI 工作负载，将编排能力下沉到笔记本电脑。

公司最近发布了一个用于 Computer 的新编排器模型的研究预览版：GLM 5.2 的一个版本，即[开源中文模型](https://thenewstack.io/china-leads-open-ai-models/)，并针对其控制接口进行了后训练。

Kupp 表示，它交付的成果成本仅为“某些前沿模型的三分之一”。他解释说，最终目标是一个能根据经济效益将工作路由到任何地方的编排器。“你可以在本地运行它，也可以在云端的远程运行它。”

这个路由问题即将与一个更大的问题发生碰撞。Kupp 说，随着智能体承担更多工作，“我们真的不仅会在 GPU 上看到瓶颈，也会在 CPU 上看到瓶颈”，这改变了迄今为止几乎完全围绕 GPU 稀缺性的讨论。如果智能体会话不断从几小时延长到几周，那么[承载它们的 CPU 集群](https://thenewstack.io/cpu-agentic-ai-axion/)，以及维持这些会话存活的状态机制，看起来就不再像是管道基础设施，而更像是行业下一场容量争夺战的焦点。