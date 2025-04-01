
<!--
title: 精益开发：如何应对容器税
cover: https://cdn.thenewstack.io/media/2025/04/906009dd-containers.jpg
summary: 容器化虽好，但“容器税”不容忽视！本文揭示了容器化开发中开发者面临的效率挑战，如调试难、构建慢等。新一代工具如Blackbird和Telepresence，旨在弥合本地开发与远程Kubernetes集群的差距，提升DevEx，助力企业在多云环境下实现降本增效，拥抱AI驱动的未来。
-->

容器化虽好，但“容器税”不容忽视！本文揭示了容器化开发中开发者面临的效率挑战，如调试难、构建慢等。新一代工具如Blackbird和Telepresence，旨在弥合本地开发与远程Kubernetes集群的差距，提升DevEx，助力企业在多云环境下实现降本增效，拥抱AI驱动的未来。

> 译自：[Leaner Development: How To Account for the Container Tax](https://thenewstack.io/leaner-development-how-to-account-for-the-container-tax/)
> 
> 作者：Steve Rodda

2010年，微软一则无处不在的广告，以审美上令人愉悦的办公室职员为特色，他们集体意识到一个可以解决他们所有问题的方案：

是时候“[上云了！](https://blogs.windows.com/windowsexperience/2010/12/07/to-the-cloud-an-in-depth-look-at-the-pcs-scenarios-from-our-new-tv-ad-campaign/)”

提示唱片划痕效果。许多技术驱动的公司已经上云，但他们对此并不特别兴奋。与大多数事情一样，“上云”并不像广告商让你相信的那么简单。

云架构是一个广泛的概念。它包括虚拟机（VM）、[容器化应用程序](https://www.paloaltonetworks.com/cyberpedia/containerization#:~:text=In%20recent%20years%2C%20an%20average,%2C%20test%2C%20and%20development%20environments.)和无服务器函数。其中，[容器](https://www.datadoghq.com/container-report/)是主导模型。作为[容器化](https://thenewstack.io/containers/)发展速度的一个标志，[CNCF 调查](https://www.cncf.io/reports/cncf-annual-survey-2023/)中 80% 的受访者表示使用 [Kubernetes](https://thenewstack.io/kubernetes/) 进行容器编排，这个系统现在才庆祝其 10 周年。

鉴于现在有如此多的业务在那里进行，我们是时候抛开玫瑰色的眼镜，正视容器化开发的实际情况了。通过更现实地理解其益处和挑战，我们可能会找到解决方案，重新找回“云”仍然闪亮如新时的兴奋感。

## 容器 101：是什么以及为什么

容器化在两个重要方面与客户端-服务器架构有很大的不同。

- **容器使应用程序代码完全独立于服务器和操作系统（OS）**。理论上，开发人员可以只关注应用程序代码来创建生产云应用程序。所有其他服务都是基于云的，通常由云提供商决定。这使得云计算对规模较小、专业化程度较低的团队来说更容易，并让公司能够将注意力转向其核心业务。
- **容器是不可变的、短暂的和声明式的**，这使得它们具有高度的可扩展性和稳定性。容器根据容器镜像按需启动——容器镜像是一个用于容器引擎的声明式脚本，用于构建与其它代码隔离的应用程序的单个实例。

**容器编排器有助于分配流量以保持容器的健康，并在适当的时候处理容器。您在容器镜像中所做的任何配置或代码更改都会延续到新的容器中，但是一旦您构建了一个容器，您就无法更改它。

### 容器带来巨大的好处

在很大程度上由于它们的不可变性，容器提供了显著的优势：

- **平台中立：** 由于它们不是特定于操作系统的，因此您可以在任何计算机上构建它们，并在任何服务器上运行它们，只要您安装了兼容的容器引擎。
- **快速部署：** 大多数云主机提供广泛的容器支持，因此开发人员可以在数小时内部署新的应用程序。这个过程不那么耗时，也不需要太多的知识，这使得云计算对更多的参与者来说更容易。
- **可扩展和稳定：** 容器引擎根据需要为容器提供计算资源，自动适应应用程序的复杂性或流量变化。
- **强大的安全性：** 不可变性和可处置性意味着用户渗透敏感资源的机会更少。攻击面更小，并且更容易执行最小权限原则，因为依赖项、功能和数据保持隔离。

有了所有这些优势，容器的采用正在加速也就不足为奇了——预计未来五年内[年增长率超过 30%](https://www.grandviewresearch.com/industry-analysis/application-container-market)。但是，如果您曾经使用过容器，您就会知道这种体验远非完美。

## 容器可能是一个潘多拉魔盒

容器的本质——不可变的、短暂的和声明式的——也带来了一些相当可预测的挑战。开发人员经常称容器为“黑盒”，这是一个恰当的比喻。

很难确切地知道容器内部发生了什么。它们本质上是无需干预的，这使得它们易于部署，但也促成了难以排除故障的隐藏错误。

### 容器化不是应该修复开发吗？
容器化最常被称赞的优点之一是，它大大减少了“[在我的机器上可以运行](https://medium.com/@sulthanftr/stopping-it-works-on-my-machine-once-and-for-all-containerization-and-orchestration-ac07d2ae8a22)”的问题。但这只是[影响开发者生产力的诸多问题](https://survey.stackoverflow.co/2024/professional-developers/#1-frequency-of-productivity-frictions)之一，这表明容器化并非万能药。

同样，容器也会带来自身的问题。以下几个问题往往会干扰开发人员的日常工作流程：

- **难以调试看不到的东西：** 大多数标准的故障排除工具和调试实践在代码容器化后都无法使用。如果代码没有按预期工作，很难知道应该在容器的哪个位置查找。
- **容器构建时间可能很慢且不可预测：** 当开发人员可以进行小的更改并立即看到效果时，调试通常会更好。这对于[标准容器实践](https://www.getambassador.io/docs/telepresence/latest/concepts/devloop)来说是不可能的，这会大大减慢[内部开发循环](https://www.getambassador.io/docs/telepresence/latest/concepts/devloop)。内部开发循环是单个开发人员的工作流程，这意味着单个开发人员应该能够设置和使用内部开发循环来快速编码和测试更改。
- **冲突的配置可能难以理清：** 有时很难预测安全设置、权限和其他配置如何在本地环境、容器和主机环境之间交互。更改错误的设置可能会以意想不到的方式传播问题。
- **协作可能具有挑战性：** 容器的不可变和短暂性使得在开发阶段创建共享容器变得困难。在同一个项目上工作的两个开发人员可能无法像在基于服务器的环境中那样轻松地处理相同的代码。
- **依赖项和集成可能难以测试：** 容器构建过程可能会模糊依赖项，并使其用途难以理解。许多开发人员转向内存或模拟依赖项，而不是使用实时 API 集成，从而隐藏了许多潜在问题。

解决这些挑战都有相应的方案，但全部实施起来需要大量的工作和费用，并会创建更多的工具和流程层，从而降低开发人员的速度。

容器也为 DevOps 团队带来了新的挑战：

- **跨多个主机管理容器很复杂：** 在理想情况下，您应该将所有容器放在具有相同容器引擎的单个主机上，这样您的 DevOps 团队就可以成为单个方面的专家。但现实情况是，大多数公司都有多个应用程序分布在不同主机的各种容器类型中。
- **为微服务配置服务器和数据资源可能具有挑战性：** 总的来说，容器化非常适合微服务，但构建可持续的架构需要仔细规划。
- **容器具有独特的安全风险：** 这可以追溯到它们的“黑盒”性质，这使得检测[风险](https://www.logicmonitor.com/blog/benefits-and-challenges-of-containerization-for-it-operations)更加困难。日志记录和监控作为对策尤为重要。

这些缺点并没有超过容器的优点。总的来说，容器化是一个净收益，但与任何技术一样，在实践中会更加棘手。密切关注缺点对于有效地管理它们至关重要。

## “容器税”——我们付出了什么代价？

容器的大部分好处都归于运维团队，他们不再需要担心物理基础设施和基本的维护任务。容器化使应用程序更稳定、更具成本效益和可扩展性，这意味着运维团队更加专业和积极主动。

容器化环境还允许 DevOps 和站点可靠性工程师 (SRE) 专注于服务架构、性能优化、安全改进和其他可以为公司带来实际收益的项目。

与此同时，成本主要由[开发人员](https://thenewstack.io/optimize-your-inner-dev-loop-to-increase-developer-velocity/)承担，他们被大量小的生产力消耗所困扰。您可能会认为这是一个可以接受的权衡，但速度较慢的开发人员对[整个组织来说都是一个问题](https://thenewstack.io/hello-world-what-happened-to-the-inner-dev-loop/)。

开发人员是实际构建您的产品和运行关键服务的人员。如果他们长期感到沮丧，您业务的基本功能将会落后于您的目标。“容器税”——那些持续的、小的生产力消耗的累积——是大多数公司实际上无法承受的代价。
好消息是，有一些方法可以帮助开发者更快地工作，减少冗余和障碍。提高生产力可能很困难，但改善开发者日常工作方式是一个显而易见的目标。

## 更高级别的容器管理

改进容器管理主要集中在容器编排上。如前所述，Kubernetes 的采用率非常高。[开放容器计划](https://opencontainers.org/) (OCI) 的工作等行业标准正在使 DevOps 变得更容易。

容器化正在成熟，遵循[容器引擎的最佳实践](https://docs.docker.com/build/building/best-practices)和[编排的最佳实践](https://www.getambassador.io/blog/kubernetes-best-practices)可以大大提高实现的成功率。

尽管这些都很有用，但很少能帮助改善开发者日常工作流程。我们必须找到一种方法来减轻开发者的容器负担，以便他们可以专注于创建更好的应用程序，并且我们必须以一种能够保留运营优势的方式来实现。

## 两全其美——容器走向本地

下一代开发者工具将建立在 Kubernetes 和容器管理专业知识的基础上，以提供更简化的开发者体验。开发者必须能够在熟悉的本地开发环境中独立工作，同时专注于构建高质量的应用程序。

同样，他们必须能够访问准确反映部署环境和集群架构的数据和服务，以便他们可以编写在实践中有效的代码。

基于 OCI 和 OpenAPI 等行业标准，[Blackbird](https://www.getambassador.io/products/blackbird/api-development) 等旨在提高 API 开发效率的工具正在扩展，以包括 [Telepresence](https://www.getambassador.io/products/telepresence)（现在是 Blackbird 中的 Cluster Commands）等特定于容器的功能。

这一代新工具为开发者带来了一些期待已久的可能：

*   **创建并行**，无需依赖 DevOps 团队或遗漏关键配置细节。[类似生产环境](https://www.getambassador.io/blog/prod-like-development-environments-improve-api-efficiency)
*   **将本地开发连接到实时的**，因此您可以使用真实数据和服务集成来测试和迭代代码。[远程 Kubernetes 集群](https://www.getambassador.io/blog/boost-developer-velocity-optimizing-feedback-loops)
*   **运行个人**[流量拦截](https://www.getambassador.io/blog/unlocking-power-telepresence-intercept-specification)，因此开发者可以使用真实的集群流量进行协作和测试，而不会中断服务交付。
*   **使用熟悉的、开发者友好的调试工具**来排除容器故障。
*   **在类似生产的条件下测试**
*   **集成和模拟 API**，以了解代码在部署中的性能。

解决容器“税”的方法不是放弃容器。而是寻找实用的创新，以弥合本地开发环境和远程容器集群之间的差距。这些工具需要反映 DevOps 和开发者体验 (DevEx) 的最佳实践，以便开发者可以创建按设计工作的容器应用程序。

## 多云环境：可交付成果和效率

云计算的现实与 15 年前广告宣传的不同。首先，现在很少有人在公司会议室工作，而是选择在厨房餐桌或咖啡店工作——这要归功于云计算。

其他现实则不那么自由。大多数公司都有[多云部署](https://www.newhorizons.com/resources/blog/multi-cloud-challenges)，这带来了管理挑战。将[无服务器函数](https://spectralops.io/blog/7-smart-steps-to-run-serverless-containers-on-kubernetes/)添加到图中会增加复杂性。[云安全](https://cloudsecurityalliance.org/research/guidance)是一个不断变化的目标。[成本管理](https://www.getambassador.io/blog/kubernetes-cost-optimization-strategies)是一场持续的战斗。

开发者还面临着越来越大的效率压力。科技行业仍在适应 [2024 年的收缩](https://www.forbes.com/sites/emilsayegh/2024/08/19/the-great-tech-reset-unpacking-the-layoff-surge-of-2024/)，而人工智能的影响正在改变整个行业的 [招聘计划](https://fortune.com/2025/03/13/ai-transforming-software-development-jobs-meta-ibm-anthropic/)。随着 [经济逆风](https://www.schwab.com/learn/story/future-uncertain-recession-coming) 的增长，技术领导者必须认真思考如何以更少的资源交付更多成果。
容器化无疑是开发过程中创新的一大福音，但它远非完美的解决方案。 “上云”，无论是使用虚拟机、容器还是无服务器函数，本身并不是目的。 目标应该是为您的开发人员、DevOps 和产品团队提供可持续、可维护的前进道路。

寻找实用的解决方案，帮助您实现容器的价值，而不会让容器本身变成雷区。