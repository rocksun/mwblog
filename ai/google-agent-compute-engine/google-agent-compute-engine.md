<!--
title: 谷歌将Gemini背后的智能体基础设施打造成云服务
cover: https://cdn.thenewstack.io/media/2026/10/30d2e7d0-google_logo-scaled.jpg
summary: 谷歌宣布将在Google Cloud推出Agent Compute Engine预览版，将Gemini背后的智能体基础设施转化为云服务。该服务为每个智能体提供硬件隔离的微虚拟机，兼具容器的速度与沙盒的安全性，同时谷歌还开源了面向Kubernetes的Agent Substrate运行环境。
-->

谷歌宣布将在Google Cloud推出Agent Compute Engine预览版，将Gemini背后的智能体基础设施转化为云服务。该服务为每个智能体提供硬件隔离的微虚拟机，兼具容器的速度与沙盒的安全性，同时谷歌还开源了面向Kubernetes的Agent Substrate运行环境。

> 译自：[Google turns the infrastructure behind Gemini’s agents into a cloud service](https://thenewstack.io/google-agent-compute-engine/)
> 
> 作者：Frederic Lardinois

Google 即将向 Google Cloud 用户提供为其 Gemini 智能体提供支持的基础设施的预览版。

在周四于圣何塞举行的 [Linux 基金会](https://thenewstack.io/agentic-ai-foundation-launch/) AGNTCon+MCPCon 大会上宣布，[Agent Compute Engine](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance) 将于今年晚些时候向 Google Cloud 用户推出预览版。它将为每个 AI 智能体提供一个硬件隔离的微虚拟机 (microVM)，结合了容器的速度与沙盒的安全性。

## 还有谁提供智能体沙盒？

当然，[智能体沙盒](https://thenewstack.io/cloud-agent-code-sandboxes/)的概念一点也不新鲜。[E2B](https://e2b.dev/) 和 [Daytona](https://www.daytona.io/) 等初创公司向开发者提供这些服务（并且在任何云上都支持它们），AWS 的 [Bedrock AgentCore](https://thenewstack.io/aws-unveils-aws-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/) 也是如此。

E2B 在 [Firecracker](https://thenewstack.io/how-firecracker-is-going-to-set-modern-infrastructure-on-fire/) 微虚拟机中运行每个沙盒，这是一种 AWS 最初为 Lambda 构建的开源虚拟化技术。它可以在保持内存和文件系统完整的情况下暂停沙盒，并在大约一秒钟内恢复它。Daytona 最初使用容器，但在 7 月份添加了微虚拟机沙盒。这些沙盒可以暂停整个机器，或者将正在运行的机器分叉为相同的副本。

AgentCore 还为每个智能体会话[提供自己的微虚拟机](https://thenewstack.io/agent-session-aware-runtime/)。当智能体等待模型或工具调用时，AWS 不对 CPU 收费，不过内存会继续计费，直到运行时回收它。这些会话最多持续八个小时。8 月份，AWS 添加了基于 EC2 的运行时实例，可以使共享会话保持长达 14 天的活跃状态。

值得注意的是，Google 对此也并不陌生。GKE 已经提供了[智能体沙盒](https://thenewstack.io/google-debuts-gke-agent-sandbox-inference-gateway-at-kubecon/)的托管版本，这是 Google 去年 11 月推出的开源 Kubernetes 项目。该公司还通过其 [Gemini 企业智能体平台](https://thenewstack.io/google-gemini-agent-platform/)销售代码执行和计算机使用沙盒。

另一方面，Agent Compute Engine 最初是作为 Gemini、[Antigravity](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/) 以及 Google 自身模型训练管道的内部基础设施。

## 谷歌的看法

很少有公司（如果有的话）运行像 Google 这样多的智能体工作负载，无论是用于其内部使用还是客户使用。据该公司称，智能体工作负载已迅速成为其整个集群中计算和存储增长最快的消耗者之一。

在此规模下，为所有这些自主智能体提供支持的基础设施服务不仅需要高效且能够扩展，而且最重要的是，它们需要安全。Google 与其一些竞争对手一样，很快意识到它需要构建一个新的专用计算服务来为所有这些智能体提供支持，类似于它过去需要构建 [Borg](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/)（后来启发了 Kubernetes）来管理其早期数据中心的计算一样。

正如 Google 的杰出工程师 Rohit Jnagal 和 Ramanathan Venkatapathy 在技术深度剖析中所指出的那样，传统的 VM 为开发者提供了大量的控制和灵活性，但代价是在启动、挂起和恢复机器时的速度。鉴于智能体启动和关闭的速度之快，这不是一个可行的选择。

他们指出，容器解决了一部分问题，“但有多个示例，如编码智能体和开发者助手，它们需要完全隔离以及智能体环境的内核级和根级控制。”

Jnagal 和 Venkatapathy 写道，借助 Agent Compute Engine，团队回归第一性原理，构建了“一个用于 Google 的统一智能体计算平台”（现在也适用于其客户）。

## 为每个智能体提供持久化的计算机

在其核心，它基本上为每个智能体提供了一个持久化的、沙盒化的计算机来协同工作。这允许智能体在可能运行数周的智能体循环中处理 shell 脚本、使用无头浏览器并编写代码（对该机器具有 root 权限）。

但该团队构建它也是为了满足大规模用例的需求，例如前沿实验室用于测试其模型的评估循环、AI 基准测试和强化学习。

此外，该团队还设计了 Agent Compute Engine，用于运行 Google 自身服务的沙盒化后端。

Jnagal 和 Venkatapathy 还指出，智能体的大部分时间都花在等待模型或用户上。因此，一旦智能体完成工具调用，主机就会对其微虚拟机进行检查点（checkpointing），然后该虚拟机在下一个调用到来之前不消耗任何活动资源。

## 沙盒内无可偷取之物

这里的关键功能除了速度之外，是能够确信智能体无法突破其沙盒。毕竟，我们已经见证了它们突破时会发生什么。

每个智能体会话都在一个单租户、内存安全的微虚拟机中运行。这些环境中没有在内存或磁盘上留下秘密，它们唯一的身份是通过每个虚拟机本地侦听器交付的短暂的、会话范围的身份。所有流量在传输过程中都是端到端加密的，快照和磁盘在静态时也是加密的。

微虚拟机也没有标准的网络接口。所有流量都通过沙盒外部的代理运行，当智能体需要访问 Google Drive 等服务时，Google 的智能体网关会在沙盒外部添加实际凭据之前，检查用户的委派和沙盒的身份。

底层主机基本上是一个具有只读文件系统的无状态设备，硬件和固件在每次启动时都经过密码验证。

所有这一切都得到了 Google 自己的 Titan 和 Titanium IPU [安全平台](https://docs.cloud.google.com/docs/security/titanium-hardware-security-architecture)的支持。微虚拟机本身在 [Cloud Hypervisor](https://thenewstack.io/rust-based-cloud-hypervisor-heads-to-linux-foundation/)（一种开源虚拟机监视器）上运行，每个虚拟机都获得自己的客体内核 (guest kernel) 和 root 访问权限。

Jnagal 和 Venkatapathy 举了一个企业智能体的例子：它管理用户的收件箱并读取包含隐藏指令的电子邮件，以查找机器上的任何 API 密钥并将其发送到外部地址。他们指出，大多数情况下，模型会忽略这一点，但并非总是如此。

“我们从一条规则开始：假设攻击者控制了沙盒内的所有内容，并确保他们在那里找不到任何可利用的东西，”团队写道。

## Agent Substrate 将相同的理念引入 Kubernetes

但并不是每个团队都希望其智能体在托管的 Google 服务中运行。对于他们，Google 还提供了 [Agent Substrate](https://github.com/agent-substrate/substrate)，这是其在 5 月份首次发布的用于 Google Kubernetes Engine (GKE) 的开源运行时。

Substrate 建立在 Google 的 Kubernetes 项目 [Agent Sandbox](https://thenewstack.io/google-cloud-a-deep-dive-into-gke-sandbox-for-agents/) 之上，并添加了一个[轻量级控制平面](https://thenewstack.io/kubernetes-ai-agent-runtime/)，Google 称该平面可以处理会压垮 Kubernetes 的数百万次短寿命工具调用。

与 Agent Compute Engine 类似，Substrate 会对空闲智能体的内存进行快照，并将机器返回到池中，直到智能体获得更多工作。

Google 表示，这意味着传统计算密度的最高 10 倍。该公司表示，在 200,000 个智能体的基准测试中，Substrate 每秒处理 500 次激活，智能体在半秒内挂起和恢复。

团队可以使用微虚拟机或 [gVisor](https://thenewstack.io/how-to-implement-secure-containers-using-googles-gvisor/) 隔离每个沙盒，并且每个智能体都获得自己的加密身份。与 Agent Compute Engine 一样，出口代理在沙盒外部附加凭据。Substrate 在任何 Kubernetes 集群上运行，Google 称它适用于任何框架，包括 Claude Code、[OpenClaw](https://thenewstack.io/openclaw-foundation-nonprofit-status/) 以及 Nous Research 的 [Hermes](https://thenewstack.io/openclaw-hermes-agent-harness/)。

“我们构建 Hermes Enterprise 是为了使客户能够在现有基础设施中进行部署，同时处理每个智能体的隔离和可扩展的访问控制，”Nous Research 首席业务官 Hervé Bizira 在公告中指出。“Agent Substrate 在平台层面上解决了这两个问题，同时也保护了宝贵的计算资源。”