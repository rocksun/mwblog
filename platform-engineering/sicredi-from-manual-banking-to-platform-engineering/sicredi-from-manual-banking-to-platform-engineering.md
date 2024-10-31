
<!--
title: Sicredi：从人工银行到平台工程
cover: https://cdn.thenewstack.io/media/2024/10/3f7ec36b-getty-images-38hnyyzyvok-unsplash-1.jpg
-->

巴西信用合作社的客户对新金融科技功能的需求，意味着西克雷迪必须大幅提升其软件开发水平。

> 译自 [Sicredi: From Manual Banking to Platform Engineering](https://thenewstack.io/sicredi-from-manual-banking-to-platform-engineering/)，作者 Todd R Weiss。

随着越来越多的银行客户开始要求扩大现代[金融科技服务](https://thenewstack.io/overcoming-the-challenges-of-working-with-a-mobile-fintech-api/)的范围，例如数字钱包和加密货币，在 2017 年，这家拥有 102 年历史的巴西信用合作社 [Sicredi](https://ri.sicredi.com.br/en/) 的开发人员看到了摆在他们面前的诱人可能性。

但是，当他们开始试验并致力于构想、构建和交付这些面向客户的新的银行创新时，他们受到了其他日常业务运营需求、缓慢的内部[软件开发周期](https://thenewstack.io/why-we-shift-testing-left-a-software-dev-cycle-that-doesnt-scale/)和其他机构挑战的阻碍。Sicredi 悠久的银行历史使其开发系统发展成为庞大、难以管理的遗留系统和基础设施，这些系统和基础设施笨拙且效率低下。

“新产品和功能的交付需要很长时间才能到达我们的客户，”Sicredi 的平台工程经理 [Eduardo Abe](https://www.linkedin.com/in/eduardolopesabe/) 告诉 The New Stack。“软件开发周期非常缓慢，因为在运营需求上浪费了大量时间，增加了整个开发周期中的等待时间以及业务产品的上市时间。”

Abe 说，随着客户开始关注 2017 年市场上出现的创新金融服务，变革的时机到来了。当时 Sicredi 的官员们并没有意识到，但在公司内部创建[平台工程](https://thenewstack.io/platform-engineering/)战略的道路才刚刚开始。其旧的开发基础设施已无法满足客户和技术日益增长的需求。竞赛现在开始了。

“为了[加快在我们的业务产品中使用这些新技术](https://www.youtube.com/watch?v=eDbQ18Fx0qU)的速度，我们决定采用使用[敏捷方法](https://thenewstack.io/agile-reinvented-a-look-into-the-future/)原则的组织形式，开始使用公共云和新的微服务架构模型来指导云原生应用程序的开发，”他说。“在这种情况下，开发团队呈指数级增长，给技术团队带来了巨大的挑战。”

## Sicredi 从 DevOps 向平台工程的转变

Abe 于 2022 年 1 月加入 Sicredi 担任 SRE（站点可靠性工程师）和 DevOps 经理，后来于 2024 年 3 月成为平台工程经理，他说，Sicredi 在 2016 年采用了 [DevOps](https://thenewstack.io/devops/) 实践，因为该信用合作社致力于简化和更好地管理其开发系统。

2017 年，Sicredi 实施了 [基础设施即代码](https://aws.amazon.com/what-is/iac/) 战略，为该信用合作社提供了使用代码而不是手动流程和设置来配置和支持其计算基础设施的新工具。此举旨在提高效率并节省管理系统的时间，帮助该组织走上了最终转向平台工程的轨道。随着最终平台概念的建立，Sicredi 自建的 [独立开发者平台 (IDP)](https://thenewstack.io/the-hidden-costs-of-free-internal-developer-portals/) 正朝着平台工程的未来迈进。

为了进一步完善其企业 DevOps 战略，DevOps 团队在 2019 年被拆分为软件工程团队和敏捷基础设施团队，目的是更好地控制仍然笨重的基础设施，Abe 说。2019 年底，Sicredi 的 IDP 正式投入生产。

但工作仍未完成。到 2021 年，Sicredi 开始组建团队，以全面整合平台工程方法来开展运营。

到 2024 年初，Sicredi 将其 IDP 的技术从 [Java](https://thenewstack.io/oracle-unveils-java-23-simplicity-meets-enterprise-power/) 迁移到 Go，以加速技术插件。

Abe 说，构建自己的 IDP 用于平台工程并非一项轻松的任务。

“我们的平台抽象了各种技术供开发人员使用，从而加快了基础设施资源的配置，包括软件开发周期中的存储库、数据库、消息服务和 Amazon S3 存储桶，”他说。“它还抽象了我们所有的 [CI/CD](https://thenewstack.io/ci-cd/) 工具，包括 [Jenkins](https://thenewstack.io/cloudbees-scales-jenkins-redefines-devsecops/) 和 [GitLab](https://about.gitlab.com/?utm_content=inline+mention)，并充当协调器，部署到我们的容器解决方案。”

Sicredi 的 IDP，他们称之为 DevConsole，为公司的工作流程等带来了巨大的改进，Abe 说。

“基础设施平台工程模型和 IDP 解决方案使 Sicredi 复杂的混合基础设施运营变得简单且可扩展，”他说。“数据显示，例如在 2021 年至 2023 年期间，开发团队增长了 45%，而无需扩大基础设施团队，”同时，由于用户新产品和功能的加速开发，业务成果也得到了增长，他补充道。

## Sicredi IDP 的更多细节

据 Abe 称，DevConsole 目前被 Sicredi 的大约 240 个开发团队和 1000 多名开发人员使用。它已被用于创建 4000 多个应用程序，用于与不同的业务合作伙伴合作，例如 Pix（巴西的即时支付服务）。

该信用合作社的开发人员使用该平台构建各种数字渠道的应用程序，以及满足 45,000 名信用合作社员工及其 800 万客户在巴西约 2,700 个分支机构的核心银行、客户互动和支付需求的应用程序。

为了保持 IDP 的最新状态，一个由 23 名平台工程师组成的团队会每季度对其进行审查，他们负责监控和维护该平台以供公司开发人员使用，Abe 说。该团队包括负责 IDP、容器、流媒体和 CI/CD 任务的工程师。

Sicredi 在使用 Canonical OpenStack 的私有云上的 47 个不同的 Kubernetes 集群上运行着 6,900 多个应用程序。

## 回顾 Sicredi 的平台工程战略

“平台工程的概念在关键操作和复杂系统中至关重要，”Abe 说。“该平台支持可扩展性、自主性、自助服务和弹性。”

他说，他们吸取了几个重要的教训。

“我认为理解 IDP 是一种技术产品有助于我们构建旨在加速软件开发生命周期的目标，”Abe 说。“使用平台指标也很重要。如今，我们可能不会从头开始开发 IDP。但当我们在 2017 年开始我们的旅程时，平台和 IDP 的概念甚至还不存在。”

Abe 说，应用程序开发和业务运营的改进对信用合作社的业务仍然意义重大。“过去，流程是手动和被动地完成的，现在有了平台，我们主动工作并且以自助服务为导向。”

Abe 说，Sicredi 在 2015 年就开始使用 Jenkins 和 [Python](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/) 对小型自动化项目进行试验，从而开始了这些流程。

## 其他成功标志

那么，使用平台工程为信用合作社带来的最大的运营收益是什么？

“在 Sicredi 采用我们的 IDP 最重要的是拥有自主权和责任，”Abe 说。“在整个平台中，我们实施了防护措施，以防止我们的开发人员错误地使用 IDP。开发人员可以为其应用程序分配 CPU 和内存资源，但只能达到一定限度。超出此限度，他们需要说明原因。另一个超级重要的因素是我们的 DevOps 团队，他们帮助在开发团队中推广平台的使用。”

Abe 说，他仍然对 Sicredi 的平台工程之旅感到惊讶，这段旅程最终促成了其 IDP 的创建。“在我们找到理想的解决方案之前，经历了许多起起伏伏，”他说。“我无法从一开始就参与其中，但在过去的三年里，我一直直接在我们的平台上工作，我们对结果感到满意。”
