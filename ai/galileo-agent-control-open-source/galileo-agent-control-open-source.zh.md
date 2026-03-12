[Galileo](https://galileo.ai/)，一家以其AI可观测性和护栏技术闻名的公司，于周三发布了[Agent Control](https://github.com/agentcontrol/agent-control)，一个开源控制平面，旨在帮助企业大规模管理AI代理。

该平台允许组织一次性编写行为策略，并将其应用于所有代理部署。

AWS、CrewAI和Glean将成为首批提供Agent Control的合作伙伴。这将使他们的客户能够访问集中式治理框架，用于管理生产环境中的代理行为。

这项技术市场需求无疑正在增长。[IDC预测，到2027年，全球2000强企业中AI代理的使用量将增长十倍](https://www.idc.com/resource-center/blog/agent-adoption-the-it-industrys-next-great-inflection-point/)。反过来，这意味着令牌和API调用量将增加1000倍。

IDC人工智能和自动化研究总监[Tim Law](https://www.linkedin.com/in/tim-law-airesearch/)在关于此新闻的新闻稿中表示：“策略的集中管理可以帮助组织管理AI代理行为。统一的控制平面和集中式治理有助于大规模部署AI代理，同时通过评估和生命周期管理确保持续改进。”

Agent Control带来的优势是为公司提供了一种标准化的方式，可以在所有代理上应用护栏，实现：

* 一个集中式策略层，用于在运行时强制执行治理并阻止不安全行为。
* 对代理策略进行实时更新，无需停机或代码修改。

Galileo联合创始人兼首席执行官[Vikram Chatterji](https://www.linkedin.com/in/vikram-chatterji)告诉《The New Stack》，实际上，这意味着Agent Control不再使用硬编码的、脆弱的安全规则，而是“让开发人员一次性定义护栏并将其应用于任何地方。通过在Apache 2.0许可下开源，我们确保每个企业和开发人员社区都可以使用它而无需厂商锁定。”

> “Agent Control让开发人员一次性定义护栏并将其应用于任何地方。通过在Apache 2.0许可下开源，我们确保每个企业和开发人员社区都可以使用它而无需厂商锁定。”
> — [Vikram Chatterji](https://www.linkedin.com/in/vikram-chatterji)，Galileo联合创始人兼首席执行官

正如其名称所示，该公司声称Agent Control可以轻松连接到任何代理，并支持来自任何供应商或自定义内部工具的护栏评估器。策略在不同环境之间保持可移植性，使团队在发展其代理生态系统时具有灵活性。
Galileo预计，常见用例包括防止LLM幻觉、强制执行数据隐私规则、引导模型选择以控制令牌成本，以及确保面向客户的AI代理中的语气一致性。

当然，Agent Control并非市场上唯一此类产品。其他产品包括[Humanlayer Agent Control Plane](https://github.com/humanlayer/agentcontrolplane)，一个开源的Kubernetes原生AI代理编排器；[GitHub Enterprise AI Controls](https://docs.github.com/copilot/concepts/agents/enterprise-management)，GitHub的AI代理治理层；以及[Microsoft Agent 365](https://www.microsoft.com/en-us/microsoft-agent-365)，Microsoft 365在Azure中用于AI代理的控制平面。

尽管竞争激烈，数百个AI团队，包括财富50强企业，仍在使用Galileo的现有平台来测试、监控和保护处理大量流量和数据的AI应用程序。看来该公司拥有成为代理控制领域参与者所需的技术和商业实力。

> “企业代理的最大障碍不再是模型。它们每天都在进步。要将代理投入生产，行业需要透明、社区驱动的护栏。像Agent Control这样的开源项目正是行业所需的开放标准，以确保自主代理对企业来说是安全的。”
> — [Dev Rishi](https://www.linkedin.com/in/devvret-rishi-b0857684/)，[Rubrik](https://www.rubrik.com/)（一家安全云公司）AI总经理

正如[Rubrik](https://www.rubrik.com/)（一家安全云公司）AI总经理[Dev Rishi](https://www.linkedin.com/in/devvret-rishi-b0857684/)告诉《The New Stack》的那样：“企业代理的最大障碍不再是模型。它们每天都在进步。要将代理投入生产，行业需要透明、社区驱动的护栏。像Agent Control这样的开源项目正是行业所需的开放标准，以确保自主代理对企业来说是安全的。”

Agent Control现已在Apache-2.0许可下可用，其源代码、SDK和文档可在GitHub上获取。