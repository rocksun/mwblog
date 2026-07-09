<!--
title: JetBrains 的下一步并非升级 IDE，而是为 Claude Code、Codex 和 Gemini CLI 构建治理层
cover: https://cdn.thenewstack.io/media/2026/07/c1da855a-pkseva-ov_az3xoqgo-unsplash-scaled.jpg
summary: JetBrains 推出 JetBrains Central 及相关治理能力，旨在打破不同 AI 编程工具间的壁垒。通过在 IDE 之上构建治理层，实现对 Claude Code、Gemini 等外部工具的统一管控、成本控制与协作增强，解决企业 AI 工具碎片化带来的管理难题。
-->

JetBrains 推出 JetBrains Central 及相关治理能力，旨在打破不同 AI 编程工具间的壁垒。通过在 IDE 之上构建治理层，实现对 Claude Code、Gemini 等外部工具的统一管控、成本控制与协作增强，解决企业 AI 工具碎片化带来的管理难题。

> 译自：[JetBrains' next move isn't a better IDE — it's a governance layer over Claude Code, Codex, and Gemini CLI](https://thenewstack.io/jetbrains-ai-team-governance/)
> 
> 作者：Paul Sawers

**工程团队过去几年一直都在**自主选择他们的 AI 工具——这里一个 IDE，那里一个基于终端的编码代理，再到别处一个用于代码审查的浏览器扩展——这导致工程领导者很难掌握开发人员到底在用什么工具，或者这些工具的成本是多少。

JetBrains 现在正努力缩小这一差距，而且不需要任何人放弃他们首选的工具。该公司周二宣布推出 [JetBrains AI for Teams and Organizations](https://www.jetbrains.com/agentic-software-development/)，这是一套凌驾于团队所依赖的任何 AI 工具之上的功能集合，增加了共享上下文、可重用的代理流程、全组织范围的治理以及成本控制。企业客户将在 7 月和 8 月逐步看到首批功能的推出。

> “团队不应该为了从 AI 中获益而必须标准化使用单一供应商的产品。”

在[宣布](https://blog.jetbrains.com/blog/2026/07/07/jetbrains-ai-for-teams-and-organizations-from-fragmented-ai-usage-to-coordinated-software-development/)该更新的一篇博客文章中，JetBrains 代理系统负责人 [Oleg Koverznev](https://www.linkedin.com/in/oleg-koverznev/) 指出，开发人员能够选择适合手头任务的任何工具这一能力是值得保留的，并写道这种“自由是一件好事”。

“团队不应该为了从 AI 中获益而必须标准化使用单一供应商的产品，”他写道。

这次扩张延续了 JetBrains 两年多来一直遵循的轨迹。它始于 [2023 年推出的编码助手](https://thenewstack.io/jetbrains-launches-new-ai-assistant-powered-by-multiple-llms/)，将 AI 带入了 IDE，[一年后又推出了 Junie](https://blog.jetbrains.com/junie/2025/01/meet-junie-your-coding-agent-by-jetbrains/)，将其变成了一个能够规划并执行自身任务的代理。JetBrains 在 3 月将 Junie 移出了 IDE，[推出了一个独立的 CLI](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/)，并配合 JetBrains Air——一个用于并行运行多个代理的环境；[Junie 本身在 6 月脱离了测试版](https://blog.jetbrains.com/junie/2026/06/junie-coding-agent-out-of-beta/)。

这一最新举措更进一步，在工程组织使用的每一个 AI 工具之上构建了一个治理层，而不仅仅是针对 JetBrains 自己的工具。

![在统一的 IDE 中访问编码代理。](https://cdn.thenewstack.io/media/2026/07/b19fd52a-screenshot-2026-07-08-at-13-59-28-.png)

*在统一的 IDE 中访问编码代理。*

此次发布包含四个部分。自动化功能可以根据存储库事件或预定计划触发云端代理，在托管环境中执行长期任务，并交付团队其他成员可见的结果。

![团队自动化和云端代理](https://cdn.thenewstack.io/media/2026/07/613d392f-automations-1024x666.png)

*团队自动化和云端代理*

同时，JetBrains Context 承诺让代理能更快地访问代码库自身的智能——跨存储库知识、代码示例、引用——从而减少代理的轮次、执行成本和错误。

在所有这些之上，JetBrains Central 是管理控制台：让工程领导者能够在一个地方查看其团队使用的 AI 工具，以及访问控制、模型和代理策略、分析和团队级成本归因。

事实上，JetBrains [在 3 月首次宣布了 Central](https://blog.jetbrains.com/blog/2026/03/24/introducing-jetbrains-central-an-open-system-for-agentic-software-development/)，并将其作为与一小部分设计合作伙伴共同开展的抢先体验计划运行；本周的公告将其全面推广至企业客户。

![JetBrains Central](https://cdn.thenewstack.io/media/2026/07/ae9b8858-central-1024x663.png)

*JetBrains Central*

Central 也许就是 Koverznev 所描述问题的答案——让开发人员选择自己的工具，却没有共享系统来管理它们，是有代价的。

“个人开发人员变得更高效，而组织却留下了碎片化的工作流、隔离的上下文和不断增加的成本，”他写道。“AI 不应该迫使组织在开发人员灵活性和组织控制力之间做出选择。”

> “个人开发人员变得更高效，而组织却留下了碎片化的工作流、隔离的上下文和不断增加的成本。AI 不应该迫使组织在开发人员灵活性和组织控制力之间做出选择。”

最后，配套的 JetBrains Central CLI 将像 Claude Code、Codex 和 Gemini CLI 这样的命令行工具纳入了同一个控制台，因此开发人员对竞争对手代理的使用情况与他们使用 Junie 的方式一样被追踪。JetBrains 还通过模型上下文协议 ([MCP](https://modelcontextprotocol.io/docs/getting-started/intro)) 链接到外部工具，并通过代理客户端协议 ([ACP](https://www.jetbrains.com/acp/)) 链接到外部代理，这一决定旨在避免为了获得治理优势而将团队锁定在 JetBrains 自己的代理上。

与所有这些相呼应，JetBrains 还改变了向企业客户收取 AI 费用的方式。自 [2025 年 8 月](https://blog.jetbrains.com/ai/2025/08/a-simpler-more-transparent-model-for-ai-quotas/)以来，该公司一直为个人和团队计划运行基于积分的系统，但企业客户采用的是单独的许可证结构，每月重置一次。

展望未来，企业客户将获得相同的积分模式，有效期为 12 个月，取代了每月的重置。

## 为什么 IDE 不再是中心

JetBrains 的公告与 *The New Stack* 在 2 月提出的一个更广泛的观点不谋而合：软件开发中的编排工作[正在从 IDE 转移](https://thenewstack.io/ide-vs-desktop-agent/)，转向代理控制平面，因为编码工作越来越多地发生在终端或协调多个代理的独立桌面应用程序中。该文章认为，以 IDE 为先的供应商面临一个选择——将编辑器精炼成其所谓的“最佳审查和调试界面”，或者自己构建协调层。

特别是 JetBrains Central，看起来就像是该公司选择了后者，通过在竞争对手的代理之上增加治理层，而不是试图在构建代理方面胜过它们。

该公司远非第一个拥抱这一机遇的企业。6 月，Cursor [推出了一个企业层](https://cursor.com/blog/organizations)，让公司可以从单一仪表板按部门管理预算、模型访问和代理权限。

最重要的是，拥有模型层对 IDE 制造商来说至关重要，因为这减少了他们对目前正试图治理的代理的依赖。JetBrains 在 6 月推出了[一个新的开源编码模型](https://thenewstack.io/jetbrains-mellum2-open-source-coding-model/)，旨在公司自己的基础设施上运行，而不是通过 Claude Code 或 Codex 的 API。Cursor 在[其自身的 Composer 模型](https://thenewstack.io/cursors-composer-2-beats-opus/)上也做了同样的事情，尽管在 SpaceX 进行 600 亿美元的重磅收购后，它现在有了相当雄厚的资金来追求这一目标——[预计最快本周就会推出联合构建的模型](https://finance.yahoo.com/technology/ai/articles/spacexai-plans-launch-model-cursor-210200389.html)。

这一切并不意味着 JetBrains 认为实际编码工作会移出 IDE 本身。Koverznev 认为，IDE 仍然是开发人员进行最直接工作的地方，JetBrains 只是在以此为基础向外扩展。

“围绕[这些 IDE]，我们正在构建服务，帮助团队跨存储库、终端、代理和云执行环境协调 AI 工作，”他写道。