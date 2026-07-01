
<!--
title: “安全守护是核心难点”：Harness押注企业可信任的生产级AI代理
cover: https://cdn.thenewstack.io/media/2026/06/42c336fe-summerizze-einevol57ps-unsplash-scaled.jpg
summary: Harness推出了Autonomous Worker Agents，允许企业用AI代理替代交付流水线中的固定脚本。该方案通过沙箱机制、成本控制和策略治理，解决了在生产环境中运行代理的风险，并将其作为公司迈向自动驾驶软件工程的重要一步。
-->

Harness推出了Autonomous Worker Agents，允许企业用AI代理替代交付流水线中的固定脚本。该方案通过沙箱机制、成本控制和策略治理，解决了在生产环境中运行代理的风险，并将其作为公司迈向自动驾驶软件工程的重要一步。

> 译自：["The harness is where the hard work is": Harness bets on agents that enterprises can trust in production](https://thenewstack.io/harness-autonomous-worker-agents/)
> 
> 作者：Frederic Lardinois

Harness 平台于周二推出了 [Autonomous Worker Agents](https://www.harness.io/products/platform/worker-agents)，使企业能够用 AI 代理替换交付流水线中的固定脚本，这些代理可以在企业现有的治理和审计控制下，推理并完成部署、测试和安全扫描等任务。

Harness 的流水线长期以来一直运行着一系列确定性步骤，例如将代码部署到 Kubernetes 或运行安全扫描。现在，任何这些步骤都可以作为代理来运行，这使得它们在保持相同护栏的同时，灵活性大大提高。

当然，该公司在代理方面并非新手。Harness 的专家代理（Expert Agents）自去年起已全面推出，旨在通过聊天窗口或 IDE 为开发人员提供建议并协助编写流水线。Autonomous Worker Agents 更进一步：流水线中的任何步骤现在都可以在客户控制的基础设施上以代理形式运行。

> “构建代理变得越来越容易，但‘安全守护（harness）’才是真正的难点所在。”

正如 Harness 首席执行官兼创始人 [Jyoti Bansal](https://www.linkedin.com/in/jyotibansal/) 在接受 *The New Stack* 采访时所说：“构建代理变得越来越容易，但‘安全守护（harness）’才是真正的难点所在。”

“当我创办这家公司时，我取名 Harness，是因为我认为开发人员编写的所有代码都需要一个安全保障，”Bansal 说。对他而言，Worker Agents 标志着公司的第四个阶段，在此之前分别是可靠的部署、[代码编写之后的后续工作](https://thenewstack.io/harness-ceo-jyoti-bansal-on-why-ai-coding-doesnt-help-you-ship-faster/)，以及专家代理。

但他认为，这第四个阶段截然不同。

> “在生产环境中运行代理，与运行我们现在都在使用的编码代理是完全不同的概念。”

“在生产环境中运行代理，与运行我们现在都在使用的编码代理是完全不同的概念，”Bansal 说。“如果你使用的是编码代理，最坏的情况是你得到一个糟糕的 PR，然后代码审查代理或人工审查员会拒绝它，或者你的下游 CI/CD 流水线会在某个地方捕获它。但如果你自己就是下游的 CI/CD 流水线，那就没有其他方法可以捕获错误了。”

## 像 Markdown 一样简单

构建代理与用 Markdown 编写技能文件并没有太大区别。代理定义在一个 Markdown 文件中，开发人员用简单的英语编写说明。此次发布称之为“已成为行业标准”的代理文件格式。正如这些工具中常见的那样，不想编写文件的团队可以让 Harness AI 来生成它。一旦运行起来，代理就会利用 Harness 的 [Software Delivery Knowledge Graph](https://www.harness.io/blog/knowledge-graph-rag)，即该公司绘制的客户服务、流水线、部署、事件和安全发现的映射图。

## 安全护栏

为了实现这一切，Harness 在过去几年构建的核心功能之上进行了扩展，事实证明这些功能也适用于代理。Worker Agents 在 [delegates](https://developer.harness.io/docs/category/delegate) 上运行，这是 Harness 在客户自有基础设施内部运行的组件，因此代理在生产系统所在的位置执行，而不是在 Harness 的云端。每个代理都在具有受限文件和网络访问权限的沙箱容器中运行，拥有自己的身份和权限，并且至关重要的是，它受制于与人类部署相同的策略引擎管理。

对于企业来说，若要在 [软件生命周期的这一环节](https://thenewstack.io/ai-has-become-integral-to-the-software-delivery-lifecycle/) 部署代理，他们必须能够验证代理的操作。几家初创公司已经在将代理的可审计性作为产品销售；而 Harness 正将其内置到服务中。Bansal 将其称为“一项巨大的挑战”，因为触及生产环境的流水线必须记录是什么触发了代理、它运行的提示词（prompt）、经历了多少轮次以及产出了什么。Harness 已经在其脚本化步骤中记录了所有这些内容，因此代理变成了流水线中它已经跟踪的另一个动作。

Harness 还内置了成本控制功能，管理代理可以消耗的 Token 数量，Bansal 表示这现在出现在每一次客户对话中。Worker Agents 会跟踪每个代理和每个流水线的 Token 消耗，并设有预算上限，在运行失控之前会暂停以等待批准。

## 代理市场

Harness 将该框架与一个代理市场（Agent Marketplace）配对，该市场首发时提供数十个预构建的代理，分为三个层级：Harness 管理的代理（由公司构建并提供 SLA 支持）、Harness 认证的代理（由合作伙伴构建并经 Harness 审核）以及任何人都可以发布的社区代理。每个代理都可以被 fork。

社区层级的信任度较难把握。“如果你使用社区构建的代理，你需要持保留意见，”Bansal 说。他表示，无论代理来自何处，沙箱、受限凭据和策略控制始终有效，而且社区代理是开源的，因此团队可以在运行前阅读代码并根据需要进行 fork。对于大型企业而言，关卡比目录更重要：公司可以批准少数受管理的代理用于生产环境，并阻止其余代理。

Harness 并不是唯一将代理引入交付流水线的公司。GitHub 在今年早些时候预览了 Agentic Workflows，它在 GitHub Actions 中运行 Markdown 定义的代理；GitLab 的 Duo Agent Platform 则允许团队在软件生命周期中构建自己的代理。GitHub 使用的代理文件约定与 Harness 相同。编码代理供应商也在向下游推进。

不过，Bansal 并不一定将他们视为竞争对手。他认为，代码编写完成后的工作是一个不同的问题，处理这些工作的代理必须达到更高的门槛。凭借超过 1,000 家企业客户，Harness 押注其优势在于两方面：知识图谱为其代理提供的上下文，以及其多年来构建的用于保持生产流水线安全的安全机制。

## 第五阶段：自动驾驶软件工程

如果这是 Harness 的第四个阶段，那么显而易见的问题是下一个阶段是什么样子。

> “在我看来，第五阶段完全是关于自动驾驶软件工程的。”

“在我看来，第五阶段完全是关于自动驾驶软件工程的，”Bansal 说。“我们的目标是整个软件工程过程，从 Jira 工单一直到生产环境，都是一个自动化的过程，由一组代理执行所有任务，从编码代理到我们正在推出的交付代理，以及这一切是如何被编排的。但是，如何在基于风险变化和对生产系统可能产生的影响的前提下，将人类引入这个流程中呢？”