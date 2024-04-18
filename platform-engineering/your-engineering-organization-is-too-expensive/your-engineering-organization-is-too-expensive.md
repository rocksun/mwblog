
<!--
title: 你的工程组织太昂贵了
cover: https://cdn.thenewstack.io/media/2024/04/a3518b26-engineering-organization-expensive.jpg
-->

如果你的工程组织过于昂贵，请考虑推出一个平台工程 MVP 来提高效率并节省成本。

> 译自 [Your Engineering Organization Is too Expensive](https://thenewstack.io/your-engineering-organization-is-too-expensive/)，作者 Luca Galante。

随着全球央行开始对通货膨胀发动一场十字军东征，全球经济状况以及价格（和成本）的未来走向仍存在许多不确定性。

工程组织在多个方面面临着不断增加的运营开支 (OpEx)。所有主要提供商的云成本都在增长，Azure 和 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 云在 2023 年同比 (YoY) [提价 15%](https://news.microsoft.com/europe/2023/01/05/consistent-global-pricing-for-the-microsoft-cloud/)。更不用说如果您的技术资产在 [VMware](https://tanzu.vmware.com?utm_content=inline+mention) 上运行，据报道，自 Broadcom 收购以来，其[价格上涨了 600% 至 1000%](https://humanitec.com/blog/escape-vmware-lock-in-with-a-modular-internal-developer-platform)。这些增长加剧了云原生工具链在过去十年中变得更加复杂、更加支离破碎和更加昂贵所造成的问题。

与此同时，薪酬数据和人才保留政策正在发出不同的信号。虽然薪酬增长不再像 2021 年那样加速，但工程薪酬待遇（尤其是高级工程师）仍超过通货膨胀， [Kubernetes 工程师的薪酬在 2023 年同比增长 10-15%](https://kube.careers/state-of-kubernetes-jobs-2023-q4)。

根据 Gartner 的说法，云行业的大多数员工估计，他们只需转换工作岗位即可赚取 11% 的额外收入，而且他们“实际上可能低估了他们增加的收入潜力”。相比之下， [Gartner 还报告](https://www.gartner.com/en/documents/4640899)（需要订阅）：

> “35% 的组织表示，他们 2024 年的绩效加薪预算将与 2023 年保持不变，而 19% 的组织计划减少或已经减少了他们的预算。只有 11% 的组织表示他们将增加 2024 年的绩效预算。另一方面，员工预计将增加 7% 以上。这可能会导致失望，因为大多数员工会期望他们的加薪幅度与通货膨胀相匹配。”

留住顶尖人才并平衡薪酬预期，同时解决工具链和云账单日益增长的复杂性（这些账单可能会迅速失控），为任何行业的管理人员描绘了一幅[具有挑战性的画面](https://thenewstack.io/want-to-be-a-tech-company-try-platform-engineering/)。

该怎么办？您是否要裁员，如果是，裁员在哪里？您是否有能力整合您的工具链，以及以什么价格？您可以在云账单上节省多少？您如何留住顶尖人才，而这些人才将对提高您的整体生产力和市场份额产生影响？

## 您是否应该考虑平台工程？

平台工程在过去两年中[席卷](https://thenewstack.io/platform-engineering-benefits-developers-and-companies-too/)了工程和云原生世界。所有主要分析师都称其为 2024 年及未来几年的关键趋势，[Gartner 预测](https://www.gartner.com/en/newsroom/press-releases/2023-11-28-gartner-hype-cycle-shows-ai-practices-and-platform-engineering-will-reach-mainstream-adoption-in-software-engineering-in-two-to-five-years)“到 2026 年，80% 的企业将实施平台工程计划”。

![Gartner 2024 年的十大战略趋势](https://cdn.thenewstack.io/media/2024/04/700e1582-top-strategic-technology-trends-2024-1.png)

*来源： [Gartner](https://www.gartner.com/en/articles/gartner-top-10-strategic-technology-trends-for-2024)*

[平台工程](https://platformengineering.org/blog/what-is-platform-engineering) 受到追捧是有充分理由的，它很可能是许多面临上述挑战的高管正在寻找的解决方案。

平台工程是整合当今企业组织的科技和工具，将其纳入优化流程，为开发人员减轻认知负担，同时实现真正的自助服务的一门学科。所有这些优化流程的总和被称为内部开发者平台 (IDP)，这是平台团队为其开发者构建的最终产品。

平台团队可以设计明确的、经过安全审查的道路，供应用程序开发人员使用基础设施和资源以及与他们的云设置进行交互。这通过设计推动整个工程组织的标准化，对前面概述的所有问题有着重要的影响。

例如，假设您决定优化流程或工作结构。在从任何流程中移除人员之前，尽可能地标准化和自动化相关工作流至关重要；否则，一切都将崩溃。推出 IDP 不仅会大幅提高您的标准化程度，而且还会加速供应商不可知论，让您避免供应商锁定并更快地整合您的工具链（并且痛苦更少）。

精心设计的 IDP 还可以提供透明度，让您深入了解云成本，从而可以在所有业务部门和技术资产中标记资源并按粒度跟踪成本。这是在不影响性能的情况下降低成本的关键。

采用平台工程的公司为开发人员和运营团队创造了一个更**健康的**（[https://thenewstack.io/devops-burnout-try-platform-engineering/](https://thenewstack.io/devops-burnout-try-platform-engineering/)) 工作环境，因为它最大程度地减少了冲突。这导致倦怠减少和更具吸引力的文化，有助于留住优秀人才。开发人员生产力的提高还意味着更短的上市时间（推出[企业级 IDP](https://humanitec.com/blog/slash-time-to-market-and-go-faster-with-platform-engineering)的团队平均下降 30%）和市场份额增长。

## 从何处开始

听起来不错，对吧？确实如此。这里的诀窍是不要迷失在过程中。许多企业已经接受了平台工程的承诺，但他们未能正确执行。

交付一个真正面向企业的 IDP，这意味着它具有一个[编排层](https://humanitec.com/products/platform-orchestrator)，该层附带所有企业功能，包括单点登录 (SSO) 和基于角色的访问控制 (RBAC)，起初可能看起来令人生畏。它需要多个利益相关者（开发人员、运营人员、高管）的参与，以及与某些工程师习惯不同的方法。许多平台团队犯的一个错误是试图一次取悦所有人。这是失去动力并拖延您的平台工程计划数月甚至数年直至其显示出任何价值的最快方式。在这一点上，需求可能会发生变化，您的 IDP 将进入失败的公司计划的坟墓。

另一方面，成功的平台计划始于[最小可行平台 (MVP)](https://humanitec.com/blog/how-to-build-a-minimum-viable-platform-mvp)，旨在快速向所有主要利益相关者展示价值。MVP 遵循一个既定的框架，该框架清楚地衡量对每个人都重要的指标的影响，然后从中进行迭代。MVP 是让企业组织中的每个人在[几周内](https://thenewstack.io/platform-engineering-dies-in-4-weeks/)（而不是几个月或几年）加入平台计划的经过验证的方法，然后扩展到可以在所有团队中推出的成熟的企业级 IDP。

采用平台工程，尤其是快速可靠地进行，是保持竞争力的公司与落后公司的关键区别因素。Humanitec 使团队能够推出面向企业的 IDP。如果您想[了解有关我们 MVP 计划的更多信息](https://humanitec.com/minimum-viable-platform-mvp)，请与我们的平台架构师交谈。