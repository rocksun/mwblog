GitHub 这一年过得并不轻松。该平台遭遇了[多次停机](https://www.infoq.com/news/2026/04/github-outages-scaling/)，影响了包括基于 Actions 的 CI/CD 流水线在内的核心服务——这是工程团队日常依赖的功能——并因此不得不发布[公开道歉](https://www.theregister.com/software/2026/04/29/github-says-sorry-and-says-it-will-do-better-as-uptime-slips/5225752)。

问题的规模令人震惊：2025 年全年 GitHub 处理了约 10 亿次提交（commits），而现在*每月*处理量就达到 14 亿次，仅 AI 智能体在同期就负责了超过 1700 万个拉取请求（pull requests）。GitHub 的 COO Kyle Daigle 在 [6 月初](https://thenewstack.io/github-wants-developers-back/)告诉 *The New Stack*，公司现在的目标是具备处理当前负载 30 倍的能力——他将这一挑战描述为远超增加更多机器的常规手段。

在这样的背景下，微软选择了这个时机，发起了迄今为止最直接的攻势，推动企业客户离开 [Azure Repos](https://azure.microsoft.com/en-us/products/devops/repos) 并转向 GitHub。Azure Repos 是微软自有的基于 Git 的源代码平台，自 2013 年起以各种形式存在，早于微软在 [2018 年以 75 亿美元收购 GitHub](https://news.microsoft.com/source/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/)。

## 迁移出口

微软用来游说客户的工具是企业在线迁移（Enterprise Live Migrations，简称 [ELM](https://learn.microsoft.com/en-gb/azure/devops/repos/enterprise-live-migrations/overview)），目前处于受限的公开预览阶段。它解决的核心问题是停机时间：以前，将大型仓库从 A 移动到 B 可能需要数天时间，导致团队无法进行活跃开发。

在一篇由 Azure DevOps 首席产品经理 [Soo Stahl](https://www.linkedin.com/in/soostahl/) 和产品经理 [Bhuvan Shah](https://www.linkedin.com/in/bhuvan-shah-8a7138171/) 共同撰写的[博客文章](https://devblogs.microsoft.com/devops/introducing-enterprise-live-migrations-migrate-azure-repos-to-github-with-minimal-downtime-azure-devops-to-github-migration-with-continuous-sync-and-fast-cutover-enterprise-live-migrations-low-downt/)中，两人解释称 ELM 的工作原理是在开发人员继续在 Azure Repos 中工作的同时，保持源仓库和目标仓库同步，最后的切换窗口通常不到 30 分钟。

> “团队可以按照自己的步调进行迁移，而无需协调复杂、高风险的‘一次性全量’迁移。”

“这意味着没有漫长的冻结期，没有持续多日的停机——只有符合您运营节奏的可控、可预测的过渡，”他们写道。“团队可以按照自己的步调进行迁移，而无需协调复杂、高风险的‘一次性全量’迁移。”

当然，这也存在不容忽视的局限性。ELM 承载了基础内容——完整的 Git 历史记录、分支、标签、拉取请求元数据（包括评论和用户历史记录），以及转换为 GitHub 规则集的分支策略——对于工作主要集中在代码上的团队来说，这可能已经覆盖了他们大部分的需求。

但是，流水线（pipelines）、工作项（work items）、维基（wikis）和测试计划（test plans）都必须分开处理。对于深度嵌入 Azure DevOps 广泛的项目管理和 CI/CD 工具的企业来说，ELM 只是一个起点，而非完整的解决方案。

对于拥有数百个仓库的大型组织而言，无论如何，这都是一项多阶段的任务。

![迁移至 GitHub](https://cdn.thenewstack.io/media/2026/06/546fc57f-azurerepos.webp)

*迁移至 GitHub*

对于微软来说，其核心考量完全在于 AI——GitHub 是 Copilot、Copilot 编程智能体以及更广泛的智能体开发套件的所在地，而 Azure Repos 并不在这个蓝图之中。

为了证明这不仅仅是对客户的推销，微软[最近发布了](https://devblogs.microsoft.com/devops/how-microsoft-is-migrating-repositories-to-github/)其自身迁移的详细信息——其 Copilot、智能体与平台（CAP）部门在六个月内迁移了 1600 多个仓库和 3100 名开发人员，而推动这一工作的团队仅由两名专职工程主管组成。

通过大规模“吃自家狗粮”（consuming its own dog food），微软试图证明这种变动是可控的，且回报意义重大。微软 1ES 及 Azure DevOps 产品管理合伙总监 [Poonam Gupta](https://www.linkedin.com/in/poonam-gupta-5155504/) 指出，AI 是此次迁移的主要驱动力。

> “软件开发正在被 AI 重塑，代码存放的位置现在直接影响到组织能够获取多少价值。”

“软件开发正在被 AI 重塑，代码存放的位置现在直接影响到组织能够获取多少价值，”Gupta 写道。“对于希望充分利用 AI 原生开发的团队来说，仓库的位置正成为一项战略决策。”

## 显而易见却被忽视的问题

关于 Azure Repos 最终会被废弃的[传言](https://www.reddit.com/r/azuredevops/comments/k9cyrl/azure_repos_deprecation/)[已在线上流传多年](https://learn.microsoft.com/en-us/answers/questions/1626498/clarification-on-azure-repos-future-and-deprecatio)，虽然微软尚未在此方面确认任何消息，但发展方向已显而易见。

[社区对 Gupta 6 月 3 日文章的反应](https://devblogs.microsoft.com/devops/how-microsoft-is-migrating-repositories-to-github/)捕捉到了企业客户的情绪：一些人质疑为什么 AI 功能不能引入 Azure Repos，而是非要更换平台；另一些人则提出了成本差异——Azure DevOps 基础版每用户每月成本为 [6 美元](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/)，而 [GitHub Enterprise 则需 21 美元](https://github.com/pricing)。

不止一位评论者将该帖子解读为“名存实亡”的废弃通知。“自从微软收购 GitHub 以来，结局就已经注定了，”一位评论者写道。“[Azure DevOps] 已经没落了，微软希望每个人都搬到 GitHub……每个人都预料到了这一点，只有微软在否认。”

也许更重要的问题是微软回避掉的：如果 GitHub 在过去的一年里一直在智能体开发流量的重压下苦苦支撑，为什么现在是企业将关键基础设施押注于它的正确时机？

上周五，这个时机显得更加尴尬：包括用于部署 Azure Functions 的 Actions 在内的 73 个微软拥有的 GitHub 仓库[在一次 Miasma 蠕虫攻击中被禁用](https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents)，导致全球开发者的 CI/CD 流水线中断。

这些都不一定会削弱向 GitHub 迁移的战略意义。AI 开发生态系统正在那里整合，迁移工具也确实在变得更好。但对于权衡决策的企业团队来说，可靠性和安全性并不是注脚——它们是核心标准。微软押注于 Copilot 和智能体工作流的吸引力足以扭转天平。

这可能是正确的，但一个 30 分钟的切换窗口仅仅是让这个论点站稳脚跟的一部分。