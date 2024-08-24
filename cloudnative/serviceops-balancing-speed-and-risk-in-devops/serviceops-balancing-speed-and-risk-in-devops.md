
<!--
title: ServiceOps：在DevOps中平衡速度和风险
cover: https://cdn.thenewstack.io/media/2024/08/4555232b-serviceops_balancing-speed-risk-devops.jpg
-->

使团队能够主动分析风险，避免进行可能导致事件的更改。

> 译自 [ServiceOps: Balancing Speed and Risk in DevOps](https://thenewstack.io/serviceops-balancing-speed-and-risk-in-devops/)，作者 Margaret Lee。

[CrowdStrike](https://www.bmc.com/blogs/resolvingcrowdstrike/) 的停机事件突出了当今业务运营的互联性，其中单个错误可能会影响许多组织和人员。[CrowdStrike发生的事件](https://thenewstack.io/5-agile-techniques-to-help-avoid-a-crowdstrike-like-issue/) 可能会发生在任何公司，即使是那些拥有良好变更控制和发布实践的公司，尤其是在组织中不同的开发团队采用不同的发布实践来加速软件交付时。缺乏统一的软件发布方法会增加引入错误或性能问题的风险。

[ServiceOps](https://www.bmc.com/documents/white-papers/serviceops-redefining-it-excellence.html) 为加速变更同时预测和管理风险提供了一种新的运营模式。通过连接 IT 服务管理 (ITSM)、IT 运营 (ITOps) 和 [DevOps](https://roadmap.sh/devops)，ServiceOps 使组织能够标准化变更控制和发布实践，提升监控和自动化修复，并防止类似 CrowdStrike 的事件发生。

## ServiceOps 支持变更风险评估

管理变更及其影响的最有效方法是主动分析风险，以避免进行可能导致事件的变更。ServiceOps 将 ITSM 的配置管理数据库 (CMDB)、发布管理和 [变更管理](https://thenewstack.io/the-chickens-have-flown-the-coop-change-management-is-back/) 功能与 [可观察性](https://thenewstack.io/observability/) 和 AIOps 解决方案相结合，使软件交付更安全、更具协作性。通过集成 ITSM 和可观察性之间的工作流程，并使用 AIOps 工具进行变更风险评估，组织可以减少与变更相关的停机时间和成本。

ITSM 和 AIOps 工具之间的集成通过分析来自服务历史记录和运营数据的风险信息，在单一视图中自动识别风险变更。AI 模型关联过去的变更并确定它们对服务可用性和健康状况等运营变量的影响。此信息通过使用 AIOps 工具的 [强大的服务依赖关系图](https://thenewstack.io/ai-powered-service-models-speed-troubleshooting/)，帮助团队快速了解风险因素和影响范围，从而减少变更请求的处理时间。这种 AI 驱动的评估还为 DevOps 和 SRE 团队提供了宝贵的反馈，使他们能够更快、更自信地部署。

这在实践中是什么样子的？以下是一个数据库升级请求的示例。根据使用过去情况和当前服务健康状况进行的风险评估，您将了解在您的环境中部署此变更或升级的风险。

![](https://cdn.thenewstack.io/media/2024/08/f9027958-database-upgrade-request-serviceops.png)

这种对变更窗口内实时部署情况、运营指标等的可见性，帮助 DevOps 团队了解正在进行的变更、哪些内容将受到影响、是否存在任何冲突，以及是否需要安排这些冲突以避免同时更改问题。

对服务和运营数据的可见性提供了自动化部分决策的机会。例如，如果变更没有风险，并且没有同时进行基础设施变更，您可以让开发人员发布它，以避免减慢他们的速度。如果存在风险，请让某人查看它。

## 下一步？释放 GenAI 在 ServiceOps 中的潜力

生成式 AI (GenAI) 在 ServiceOps 中发挥着重要作用。例如，使用预测性和因果性 AI 可以补充其他形式的 AI 来预测变更的风险，而对话式用户界面可以实现共享评估。

在变更风险评估期间使用 GenAI 作为界面层提供了许多好处，例如：

- 它使复杂的风险洞察力对不同的跨职能团队成员（包括 [站点可靠性工程师 (SRE)](https://thenewstack.io/sre-vs-platform-engineer-cant-we-all-just-get-along/)、DevOps、开发人员、服务经理和变更经理）变得易于理解，他们对运营环境的熟悉程度不同。
- 它通过让人们能够提出和回答问题来帮助做出明智的决策，从而加速变更风险评估过程。
- 它通过为 DevOps 团队提供风险缓解建议，增强组织对 DevOps 的信心。

用于变更风险评估的对话式界面可以使风险洞察力对负责快速交付高质量软件的团队变得易于理解和可操作。

想象一下，让负责审批软件变更的团队能够使用基于聊天的界面来提问并获得针对其软件将要部署的特定环境的答案。他们可以得到诸如“哪些是风险变更？”和“我可以查看变更冲突吗？”之类问题的答案。

DevOps 推动的快速变化给 IT 服务和 IT 运维团队带来了重大挑战。两者都需要加速变更，而不会冒停机风险。无论在章程、范围和技能方面存在什么差异，越来越多的服务和运维团队正在走到一起，重新定义服务卓越和业务一致性。

[ServiceOps](https://www.bmc.com/info/serviceops.html) 是一种让团队协同工作以实现服务交付卓越的智能方式。ServiceOps 由自动化和 AI 支持，是一种新的服务交付运营模式，可以降低成本，减少停机风险，并提高 IT 生产力和效率。
