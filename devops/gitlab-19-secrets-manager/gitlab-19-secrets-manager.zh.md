**有管弦乐团……也有仅仅是由弦乐、号角或木管组成的乐部。**作为自诩的 [DevSecOps](https://thenewstack.io/devsecops-tools-that-offer-security-efficiency-and-quality/) 智能编排平台，GitLab 希望通过涵盖所有可能乐器的新型协同演奏，来呈现一场完整的演出。

该组织[在上周四发布了 GitLab 19.0](https://about.gitlab.com/press/releases/2026-05-21-gitlab-19-extends-intelligent-orchestration-to-close-the-gap-between-writing-code-and-shipping-it/)，带来了更宏大、更和谐的乐章，其中包括扩展的[机密管理](https://thenewstack.io/the-challenges-of-secrets-management-from-code-to-cloud/)、Agent化合并请求工作流、持续集成（CI）流水线可见性、对自托管开源模型的支持以及供应链可见性。

## AI 悖论的囚徒

随着 AI 驱动的代码开始在实际代码库中涌现，软件工程团队正致力于避免 [AI 悖论](https://www.linkedin.com/posts/ai-softwareengineering-developerproductivity-share-7411238038577647616-Mp-Z/)的万有引力——即更多的 AI 代码意味着需要保护更多的流水线凭证、监督更多的审查和合并变更、维护更多的流水线标准、进行更多的合规性检查等。

人们可能会觉得，智能自动化与智能基础设施编排似乎从未合奏过同一首乐曲。而 GitLab 19.0 的设计初衷就是为了对抗这种生产悖论，并减少从编写代码到交付代码之间的交接。

> “如今，将凭证放入 CI/CD 变量中，就会将该机密授予项目中的每个作业，包括那些在创建机密时还不在场的贡献者随后添加的作业。GitLab Secrets Manager 彻底改变了这一默认规则。”—— Manav Khurana，GitLab。

在这些更新中，最关键的是 [GitLab Secrets Manager](http://about.gitlab.com/blog/secrets-manager-in-public-beta/)（一种在运行代码和流水线的同一平台内存储凭证的技术）现已面向 GitLab Premium 和 Ultimate 用户进入公测阶段。该工具将每个机密的范围严格限制在获得授权使用它的作业中。访问控制和审计日志使用 GitLab 中现有的相同群组和项目结构，无需维护独立的权限模型。

如果某个凭证泄露，开发人员（在此情况下很可能是平台工程师）可以在 GitLab 审计追踪中追溯使用过该凭证的每个作业，并关联到源流水线，而无需跨独立系统关联日志。它与现有的 HashiCorp Vault、AWS Secrets Manager、Azure Key Vault 和 Google Cloud Secret Manager 集成协同工作。

## 最小特权访问原则

将机密范围限定在单个作业中，被视为在流水线构建期间对开发人员安全姿态的一次根本性改变。

GitLab 首席产品与营销官 [Manav Khurana](https://www.linkedin.com/in/mkhurana/) 告诉《The New Stack》，这一举措完全是为了践行最小特权访问原则。

“如今，将凭证放入 CI/CD 变量中，就会将该机密授予项目中的每个作业，包括那些在创建机密时还不在场的贡献者随后添加的作业，” Manav Khurana 表示，“GitLab Secrets Manager 彻底改变了这一默认规则。”

Manav Khurana 解释了现在的运行机制，并指出当开发人员创建凭证时，他们可以定义作业使用该凭证的条件：哪个分支、哪个环境，以及该分支是否受保护。任何超出该范围的作业都无法看到该机密，因此被攻破的作业也会被限制在局部范围内。

## 保持开发人员在整个生命周期中的流畅体验

GitLab 19.0 还将 Developer Flow（开发人员工作流）扩展到了整个合并请求（MR）生命周期中，以处理审查者反馈、解决冲突、拆分过大的合并请求以及在任何阶段实现功能。Developer Flow [由 GitLab 于去年推出](https://about.gitlab.com/blog/transform-mrs-to-automated-workflow/)（顾名思义，它旨在让程序员保持在“心流”状态），旨在将 Issue 转化为合并请求。

由于该工作流在提交之前会从 [AGENTS.md](https://agents.md/) 中读取特定项目的标准，因此输出结果能反映团队的上下文、工作流和防护栏，而不是泛泛的默认设置。

“Agent 是针对开发人员的项目工作的，而不是针对通用模板，” Manav Khurana 说道，“定制化程度取决于团队指定的深度。AGENTS.md 捕获了 Agent 原本无法获取的项目级上下文：惯例、架构决策、环境怪癖，以及新贡献者需要别人解释的命令。”

他进一步阐明，[agent-config.yml](https://adk.dev/agents/config/)（一个定义 Agent 行为、环境和参数的配置文件）可以用必要的依赖项和工具来设置开发环境，使 Agent 能够在提交之前运行测试和预提交钩子（pre-commit hooks）。

“关键在于给 Agent 一台准备就绪的机器，使输出符合团队的标准，而不是造成返工。同一群组中的两个项目可能会产生非常不同的 Agent 行为，因为 Developer Flow 读取的是每个项目自己的文件，而不是共享的默认设置，” Manav Khurana 说道。

## 四款全新开源模型

本版本的其他更新还包括组件分析（Components Analytics），它使平台工程团队能够直观地看到组织内正在运行哪些 CI/CD 目录组件，以及正在使用哪些版本。

此外，自托管的 GitLab Duo Agent Platform 现在可以在[另外四款开源模型](https://about.gitlab.com/blog/more-ai-models-for-duo-agent-platform-self-hosted/)上运行其 Agent：Mistral Devstral 2 123B、GLM-5.1、Kimi-K2.6 和 MiniMax-M2.7。每个模型都针对 GitLab Duo Agent Platform 的任务要求进行了评估，包括多步工具使用、代码生成质量以及跨大型代码差异的推理。它同时支持本地（on-premises）和私有云部署选项。

“引入四款全新的开源模型是为了消除在合规性与能力之间的权衡。在[物理隔离和受监管环境](https://thenewstack.io/deploying-ai-in-air-gapped-environments-what-it-really-takes/)中工作的团队现在拥有比以往更强大的本地选择，” Manav Khurana 表示。

他指出，GitLab 用户还可以设置混合部署，按功能混合使用自托管和 GitLab 托管的模型，并根据数据敏感性、基础设施成本、延迟以及本地运行模型与 GitLab 托管选项之间的能力差距来进行选择。

GitLab 19.0 还增加了安全功能，使团队在管理交付内容以及谁可以访问平台方面拥有更多控制权。结合[软件物料清单 (SBOM)](https://thenewstack.io/a-good-sbom-is-hard-to-find/)进行的依赖项扫描，可以生成可审计的第三方组件清单，并能与 GitLab 安全通告进行比对。

> “这种方法并未涵盖 Agent 是如何在团队的流水线中做出自主决策，并利用曾经授予但随后被遗忘的权限采取行动的。如果软件工程团队在启动 Agent 部署之前，没有建立好执行治理和可观测性，他们终将面对由于别人在某一天做出的决定而带来的后果——而且他们将以惨痛的方式吸取教训。”—— David Girvin，Sumo Logic。

## 不要忘记那些“被遗忘的权限”

云监测和日志管理 [SIEM](https://www.microsoft.com/en-gb/security/business/security-101/what-is-siem) 专家 [Sumo Logic](https://www.sumologic.com/) 的 AI 安全研究员 [David Girvin](https://www.linkedin.com/in/david-a-girvin/) 告诉《The New Stack》，他认同目前开展工作的这一方向。

“大多数 AI 编码工具解决的问题只占开发人员一天中大约 52 分钟的时间。而 GitLab 正在追问其余的 7 个小时里会发生什么，” David Girvin 说道，“GitLab 19 押注于跨越整个软件生命周期的 Agent化编排，而不仅仅局限于编辑器，这正是应该解决的正确问题。”

然而，David Girvin 指出，这种方法并未解决 Agent 是如何跨团队流水线做出自主决策，并利用那些曾经授予但随后被遗忘的权限采取行动的。

“如果软件工程团队在开启 Agent 部署之前没有建立起执行治理和可观测性，他们终将面对由于别人在某一天做出的决定而带来的后果——而且他们将以惨痛的方式吸取教训，” David Girvin 强调。

## 先解决 AI 基础设施，再解决代码

GitLab 已经将其工程力量投入到解决“更多 AI 代码等于更多令人头疼的问题”上，这一问题使“AI 基础设施优先”的辩论在今年成为了焦点。

正如 GitLab 的 Manav Khurana 总结的那样：“此次发布意味着开发人员花在合并请求相关的繁杂手动工作上的时间减少了，而被泄露的凭证也将仅限于使用它的作业中。安全团队则将修复重点放在真正的暴露点上，而不是清单中的每个包，仅关注你代码实际调用的那些包。”

这里的核心信息是将安全、自动化和治理置于与代码相同的平台上，以便一者可以在另一者之前启动。

正如漫画所说：[先穿裤子，再穿鞋](https://i.pinimg.com/474x/4d/6f/47/4d6f47b070a2778ed35e18e3e2428ea5.jpg)。