
<!--
title: 从Kubernetes和云中汲取的教训理应引导AI革命
cover: https://cdn.thenewstack.io/media/2024/05/02094dca-element5-digital-oycl7y4y0bk-unsplash-scaled.jpg
-->

人工智能技术堆栈中的错误配置会导致数据摄取管理不善、模型训练效率低下和安全漏洞不足。解决这些挑战需要不重复我们从云和 Kubernetes 经验中吸取的教训。

> 译自 [Lessons From Kubernetes and the Cloud Should Steer the AI Revolution](https://thenewstack.io/lessons-from-kubernetes-and-the-cloud-should-steer-the-ai-revolution/)，作者 Mark Hinkle。

我们之前见过这个故事……

在过去十年中，[云计算](https://thenewstack.io/Cloud-Services/) 和 [Kubernetes](https://thenewstack.io/kubernetes/) 作为革命性力量出现，承诺可扩展性、效率和运营灵活性。这些创新改变了组织部署和管理数字基础设施的方式，云服务实现了轻松的资源扩展，而 Kubernetes 提供了 [复杂的容器编排](https://thenewstack.io/kubernetes-1-30-gets-better-at-naming-things/)。

然而，这种技术采用速度带来了挑战，尤其是配置[技术债务](https://thenewstack.io/3-sources-of-tech-debt-and-how-to-manage-it/) — 一个阻碍开发人员生产力、导致系统中断并增加安全风险的复杂问题。如果组织实施主动配置 [数据管理策略](https://thenewstack.io/data-management-strategy-is-more-strategic-than-you-think/)，本可以避免这个问题。

新兴的[人工智能](https://thenewstack.io/ai/) (AI) 技术正在遵循类似的轨迹。围绕 AI 潜力的最初兴奋让我们能够避免重复过去的错误，包括累积配置技术债务。

在 AI 开发早期解决配置债务对于避免云和容器技术在快速走向主流时面临的先前配置挑战至关重要。

## 云计算的快速崛起

云计算彻底改变了 IT，强调可扩展性、灵活性及成本效益。企业迅速从昂贵的本地[数据中心转向云](https://thenewstack.io/data-center-and-cloud-environments-for-next-generation-data-stacks/)，重视敏捷性和创新。然而，这种转变带来了配置复杂性，导致配置债务，因为公司难以 [优化云服务以提高性能和成本](https://thenewstack.io/tricks-for-cloud-cost-optimization/)。

该行业通过开发云管理工具和最佳实践做出了回应，优先考虑简单性、可重复性和自动化。这些措施有助于减少配置债务，使组织能够充分利用云计算的优势，同时有效管理其挑战。

## Kubernetes：通过编排驯服云

Kubernetes 自动化了[容器化应用程序](https://thenewstack.io/containers/) 的部署、扩展和操作，使开发人员能够专注于应用程序开发，而不是基础设施。

尽管有这些好处，[Kubernetes 在配置管理中引入了复杂性](https://thenewstack.io/managing-kubernetes-complexity-in-multicloud-environments/)，由于最佳实践不一致，可能会产生大量的配置债务。

Kubernetes 社区开发了 Helm Chart 等工具和实践，用于包管理，用于自动化应用程序管理的运营商和[基础设施即代码](https://thenewstack.io/infrastructure-as-code/) (IaC) 工具，如 [Terraform](https://thenewstack.io/how-to-manage-cloud-services-with-terraform/)，以及用于高效配置的 [CI/CD 管道](https://thenewstack.io/ci-cd/)。

## 与 AI 革命的相似之处

AI 开发与云服务和 Kubernetes 的快速增长相似，有望通过增强决策制定和任务自动化等新功能彻底改变业务运营。

然而，这种快速发展可能会导致另一轮配置技术债务的积累，正如我们在云和 Kubernetes 中看到的那样。AI 系统具有巨大的配置复杂性：AI 技术堆栈、算法、数据管道和模型必须针对最佳性能、可扩展性和安全性进行正确配置。

AI 技术堆栈中的错误配置会导致[数据摄取管道](https://thenewstack.io/7-tips-for-building-fast-scalable-cost-efficient-streaming-data-pipelines/) 管理不善、模型训练效率低下和安全措施不足。解决这些挑战需要不重复我们从云和 Kubernetes 经验中吸取的教训。

## 经验教训和前进的道路

云计算和 Kubernetes 的发展为 AI 开发提供了重要的经验教训。它强调了战略规划的必要性，包括配置管理中的工具选择和最佳实践，以避免配置债务并确保系统可扩展性和安全性。

实施自动化和 IaC 将减少人为错误，使配置更可靠、更可审计。有效的治理和明确的配置管理策略对于维护系统完整性和合规性至关重要，尤其是在快速发展的 AI 创新中。

培养类似于 Kubernetes 生态系统的协作和知识共享社区至关重要。通过利用这些经验教训，AI 开发路径变得更加清晰，使技术能够实现其变革潜力，同时避免技术债务。

## 避免 AI 中配置债务的策略

为了避免 AI 开发中的配置债务，组织可以从 [云计算和 Kubernetes](https://thenewstack.io/the-status-of-cloud-native-computing-and-kubernetes-today/) 中学习，强调战略规划、自动化和持续学习的文化。

![消除错误配置：AI 配置即平台：5% 的嵌入式 AI 故障是由于错误配置造成的。资源调整复杂且手动。经过验证的“黄金配置”模板支持自动化。](https://cdn.thenewstack.io/media/2024/05/e14ee313-misconfig.jpg)

*简而言之，AI 配置即平台。*

自动化通过支持 IaC 的工具减少人为错误，并确保一致、可靠的配置。在 AI 项目中建立明确的治理策略可以简化配置管理并遵循最佳实践，从而最大程度地降低配置债务风险。

[CloudTruth](https://www.cloudtruth.com/) 的联合创始人 Greg Arnette 说，“根据对一千多位工程领导者的研究访谈，我相信新 AI 时代必备的解决方案是全面的秘密和配置数据编排解决方案，该解决方案可以管理、审计、保护和版本 AI 堆栈配置和秘密。AI 系统配置和维护复杂，并且操作成本高，因为它们消耗了大量云资源并处理敏感的公司数据。”

培养优先考虑持续改进的文化有助于团队紧跟最新技术。实施这些策略可确保有效且高效的 AI 系统管理，免受配置债务的困扰。

## 结论：用过去的智慧引领 AI 革命

一个清晰的模式出现了，将云和 Kubernetes 的兴起与人工智能技术的兴起联系起来——快速创新，然后意识到累积的配置技术债务将破坏成功的部署。

组织可以通过采用标准化工具、治理框架和协作实践来缓解配置债务，这些实践优先考虑简单性和自动化。这确保了 AI 系统的可扩展性、安全性并能够发挥其变革潜力。

请记住，配置数据是 AI 基础设施堆栈中的“承载负载”。鉴于秘密和变量至关重要，配置错误在统计上比任何其他类型的软件错误导致更多中断和违规。

每个团队都必须具备一个解决方案，该解决方案可以全面管理、审计、保护和版本此数据，而无需大量返工。
