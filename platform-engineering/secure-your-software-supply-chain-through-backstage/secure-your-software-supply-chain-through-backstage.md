# 通过 Backstage 确保你的软件供应链安全

一个内部开发者门户可以帮助您整合和演化您的安全策略。

翻译自 [Secure Your Software Supply Chain Through Backstage](https://thenewstack.io/secure-your-software-supply-chain-through-backstage/) 。我们的团队目前刚刚完成了 Backstage 与 ArgoCD 的集成，感觉很不错。

![](https://cdn.thenewstack.io/media/2023/08/71967b55-portal-1024x609.jpg)
*图片来自 Shutterstock 的 Alberto Andrei Rosu*

现今的软件很少从零开始编写。根据 [Forrester](https://www.forrester.com/report/the-forrester-wave-tm-software-composition-analysis-q2-2023/RES178483) 的数据，平均而言，至少有 75% 的开源代码构成了软件的组成部分。此外，团队严重依赖第三方代码。因此，您投入生产的代码来自不同的来源，并通过各种网络和参与者传输到目标地。这被称为软件供应链。

在过去几年里，由于[严重攻击](https://thenewstack.io/the-challenges-of-securing-the-open-source-supply-chain/)，软件供应链引起了极大的关注。在美国，联邦政府甚至为州立承包商发布了[软件供应链指南](https://thenewstack.io/nsa-software-supply-chain-guidance/)。

正如 [Cloud Native Computing Foundation（CNCF） 安全工作组](https://github.com/cncf/tag-security/blob/main/supply-chain-security/supply-chain-security-paper/CNCF_SSCP_v1.pdf)所述：“供应链需要多个关联的流程，供应链安全依赖于对每个流程的验证和验证。”因此，为了在开发生命周期的每个步骤中采用安全实践，公司通常[采用 DevSecOps 方法](https://thenewstack.io/5-security-principles-to-guide-your-devsecops-journey/)。

自动化是确保供应链安全的关键因素，可以减少人为错误因素，并能够处理涉及的大量参数。幸运的是，有各种工具可以帮助您通过软件开发生命周期自动化安全检查。

然而，通常您需要将不止一个工具集成到您的安全策略中。这就是内部开发者门户（如Backstage）变得至关重要的时候：

1. 您可以在 Backstage 的目录中集成单一的安全工具界面。
2. 通过 Backstage 的 Scaffolder ，您可以主动将安全供应链实践嵌入新的代码中。
3. 您可以通过 Backstage 的 Tech Insights 从您的组织安全的演变中学习。

![](https://cdn.thenewstack.io/media/2023/08/45f6a293-image3-e1691159668662.png)

## 统一的安全视图

根据 CNCF 的说法，确保供应链安全的一个关键步骤是确保“内部的、第一方的源代码仓库……通过提交签名、漏洞扫描、贡献规则和策略执行得到保护和安全”。您需要跨不同的工具（如 GitHub 、 SonarQube 和 Snyk ）实施这些措施。

![](https://cdn.thenewstack.io/media/2023/08/d9755f36-image4-e1691159730608.png)

您可以设置您的 Backstage 服务视图，集成各种工具，以便全面了解正在发生的情况，必要时可以深入了解细节。

## 主动的供应链保障

要求开发人员负责保护其自己的代码库会将更大的认知负荷推给他们，并在整个组织中创建分散的安全实践。

相反，您可以为常见的服务设置提供默认安全模板。通过 Backstage 的 Scaffolder ，您可以帮助团队以合理的默认设置和最佳实践来发布应用程序和功能。

![](https://cdn.thenewstack.io/media/2023/08/e3492be8-image2-e1691159768545.png)

Backstage 的 Scaffolder 不仅仅为新服务提供最佳实践。您还可以为现有项目提供[自助式的黄金路径](https://thenewstack.io/new-to-platform-engineering-try-a-thin-self-service-layer/)，以采用您的安全工具。例如，您可以定义一个模板，通过几次点击，在开发人员的存储库中打开一个拉取请求，以便他们在其 Spring Boot 应用程序中采用 Snyk 。

## 了解您的整体安全演变

当您通过目录进行所有权排序，并通过 Scaffolder 主动推动最佳实践时，下一步是了解您的整体软件供应链安全工具。

Roadie 的[开源 Tech Insights 插件](https://roadie.io/backstage/plugins/tech-insights/)提供了一个框架，用于实施检查和评分卡，以审核 Backstage 实例中的安全性。一些企业的 Backstage 采用者，如惠普（HP）和 Lunar Bank ，已基于此插件实施了自己的解决方案。

然而，Backstage 的开源 Tech Insights 功能要求每个团队在管理集成、安全性和数据库的基础上，设计自己的用户界面并实施自己的数据源和检查。

![](https://cdn.thenewstack.io/media/2023/08/b9e637e8-image1-e1691159830889.png)

[完整的 Tech Insights 版本](https://roadie.io/product/tech-insights/)仅提供给 Roadie 的客户使用，其中包含 100 多个事实，您可以跨 GitHub、Snyk 和 PagerDuty 等数十个数据源进行检查。

据 [SumUp](https://www.sumup.com/) 的工程副总裁 Martin Froehlich 表示，这家金融技术公司正在使用 Roadie Tech Insights 来促进和跟踪供应链安全和代码分析工具（如 Dependabot、CodeQL 等）在其所有生产服务存储库中的采用。

## 整合、推动和演化安全性

基于 Backstage 的开发者门户可以帮助您在一个集中的位置整合您的工具，以便开发人员和运维人员更容易地将安全性向左移动。您还可以通过软件模板简化流程，推动安全性倡议。您还可以跟踪您的供应链安全的演变以及实践在整个组织中的采用情况。

