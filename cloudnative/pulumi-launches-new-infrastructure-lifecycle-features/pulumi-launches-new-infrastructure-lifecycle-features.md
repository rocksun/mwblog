
<!--
title: Pulumi推出新的基础设施生命周期功能
cover: https://cdn.thenewstack.io/media/2024/04/5e950cc6-walter-frehner-i2wcssuw-pi-unsplash.jpg
-->

Pulumi 为其基础设施即代码 (IaC) 平台新增了漂移检测和修复、生存时间 (TTL) 堆栈等功能。与此同时，Pulumi 首席执行官 Joe Duffy 承诺在 HashiCorp-IBM 潜在交易中继续创新。

> 译自 [Pulumi Launches New Infrastructure Lifecycle Features](https://thenewstack.io/pulumi-launches-new-infrastructure-lifecycle-features/)，作者 Darryl K Taft。

[Pulumi](https://www.pulumi.com/) 是[基础设施即代码](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/) (IaC) 领域的领导者，它为其部署工作流产品 — [Pulumi 部署](https://thenewstack.io/pulumi-introduces-one-click-deployments/) — 推出了一系列新功能，为该平台提供了新的基础设施生命周期管理功能。

这些功能包括：

- [漂移检测](https://thenewstack.io/how-drift-detection-and-iac-help-maintain-a-secure-infrastructure/)和修复
- 使用[生存时间 (TTL)](https://www.techtarget.com/searchnetworking/definition/time-to-live) 堆栈自动清理基础设施
- 计划部署

## 了解我的漂移

漂移是指组织的基础设施状态与其配置中定义的状态不同。新的漂移检测和修复功能使用户能够持续监控基础设施，以便在实际云基础设施偏离 IaC 真实来源时检测并通知团队。该公司表示，可以通过重新应用先前部署中最后一次已知良好状态的自定义策略自动修复漂移。

为了跟踪任何偏差，用户可以使用 [Slack](https://thenewstack.io/slacks-new-dev-portal-offers-ci-cd-python-javascript-aids/)、Microsoft Teams 或 [WebHook](https://thenewstack.io/new-open-source-standard-brings-consistency-to-webhooks/) 设置自定义警报，或通过 Pulumi Cloud 中的仪表板查看漂移。

## TTL 堆栈

同时，新的生存时间 (TTL) 堆栈在经过一定时间后会根据灵活的策略自动清理基础设施。这使团队能够启用自助服务，而无需担心过时的基础设施和相关成本。

Pulumi 的联合创始人兼首席执行官 [Joe Duffy](https://www.linkedin.com/in/joejduffy/) 表示，新功能是由客户高度推动的。

“漂移检测更直接、更重要，但是，TTL 堆栈获得了我的投票[作为最重要的新功能]。我们的许多客户希望为其开发人员启用自助云基础设施，尤其是在人工智能、数据科学时代，但由于担心成本高昂的浪费而不敢这样做，”Duffy 告诉 The New Stack。“有了 TTL 堆栈，这种担忧就消除了，基础设施团队现在可以完全控制以消除浪费风险。因此，虽然它比每个人都能立即理解的漂移稍微微妙一些，但我希望 TTL 堆栈成为粉丝的最爱。”

此外，计划部署功能使组织能够根据任意 [cron](https://thenewstack.io/move-your-cron-jobs-to-serverless-in-3-steps/) 计划安排部署活动，使团队能够自动化重复的工作流并使用自定义策略和操作工作流扩展系统，该公司表示。

## Day 2

这些新的基础设施生命周期管理功能旨在提高 [Day 2 运营](https://thenewstack.io/cloud-native-day-2-operations-why-this-begins-on-day-0/) 的可靠性、成本和安全性。Duffy 表示，它们使平台团队能够在保持必要护栏的同时更快地交付云供应。

事实上，Duffy 告诉 The New Stack，新功能表明 Pulumi 正在解决更多 Day 2 运营挑战 — 对于该公司最大的企业客户来说，这是一个至关重要的领域。“我们看到他们每天都在这里苦苦挣扎，我们很高兴为他们提供一个开箱即用的解决方案，以便他们可以将精力集中在解决更高价值的业务挑战上，”他说。“随着我们从基础设施即代码发展到许多产品，基础设施生命周期管理将成为一个关键主题。”

例如，“在 Oleria，我们了解解决隐私、安全和数据完整性问题的重要性。赢得并维护我们的信任不仅是一项责任，也是我们使命的一个基本方面，” [Jim Alkove](https://www.linkedin.com/in/jalkove/)，[Oleria](https://www.oleria.com/company) 的首席执行官说。“Pulumi 也了解这些属性如何影响云基础设施，”他补充说，新的功能将帮助 Oleria 帮助其客户“安全地管理对分散式 SaaS 应用程序的访问，并具有适应性和智能性”。

## 免费 Pulumi 部署

使用 Pulumi 部署，组织可以避免构建自定义的本土系统。该产品包括 [git](https://thenewstack.io/git-at-15-how-git-changed-the-way-we-code/) 推送部署、临时审查堆栈和基于 UI 的部署，并提供用于自定义工作流（例如蓝/绿和多区域部署）的 REST API。

Pulumi 宣布了 Pulumi 部署的新免费层，适用于这些新功能的使用。该公司认为，这些增强功能将通过让客户能够自信地更快地行动，帮助他们充分利用其云工作。

## 关于 IBM 和 HashiCorp：“我们将超越创新”

与此同时，Duffy 谈到了可能撼动代码基础设施领域的大问题，因为 IBM 正在谈判收购另一家 IaC 领导者 HashiCorp。

他挖苦地说：“HashiCorp 在多年前就把 IaC 的创新议程让给了我们。”“IBM 显然是一家拥有悠久历史的不可思议的公司；然而，他们最出名的是世界级的咨询和市场推广能力，我预计此次收购将为 Pulumi 继续超越创新并进一步加速获得市场份额敞开大门。”

Pulumi 通过允许用户使用通用编程语言（如 JavaScript、TypeScript、Python 和 Go）定义基础设施，采取了创新的 IaC 方法。这使开发人员能够使用熟悉的语言，并利用这些语言的力量进行抽象、测试和可重用性。

[全球基础设施即代码市场](https://www.fortunebusinessinsights.com/infrastructure-as-code-market-108777) 规模在 2022 年被评估为 7.591 亿美元，预计将从 2023 年的 9.087 亿美元增长到 2030 年的 33.049 亿美元。
