<!--
title: 平台工程减轻认知负荷，提升开发者生产力
cover: https://cdn.thenewstack.io/media/2023/10/51282e13-face-4776910_1280-1024x710.jpg
-->

平台工程是通过设计并构建工具链和工作流程，提供自助服务能力，以降低软件开发的复杂性。

> 译自 [Platform Engineering Reduces Cognitive Load and Raises Developer Productivity](https://thenewstack.io/platform-engineering-reduces-cognitive-load-and-raises-developer-productivity/)。作者Michel Murabito是Mia-Platform的开发者倡导者，拥有18年以上的软件开发经验。我喜欢分享自己的知识，因此在2021年至2022年期间，我以演讲者的身份在许多意大利和国际活动中发言。我管理一个YouTube频道和一个拥有700多名成员的社区，我主要在那里讨论开发者职业。

毫不意外，过去几十年来，开发者创造了无数搞笑图片，描述加入和理解公司代码库的困难。除了努力明智地选择工具、框架和方法，还要遵守DevOps“你写的代码，你运行它”的箴言，这些都导致软件开发者的认知负荷急剧增加，需要付出巨大努力和资源才能理解、创建和维护日益复杂的软件。

为了缓解过高的认知负荷挑战，采用[平台工程](https://blog.mia-platform.eu/en/the-internal-developer-platform-revolution)这种结构化的方法，通过简化流程、提供标准工具和自动化重复任务，来减轻软件开发生命周期的压力。

本文介绍了以下内容:

- 认知负荷对开发者生产力的影响。
- [平台工程如何减轻认知负荷](https://thenewstack.io/cyberark-decreases-cognitive-load-with-platform-engineering/)，提高生产力并促进软件开发。

## 理解软件开发中的认知负荷

认知负荷这个词是John Sweller在1988年的论文《解决问题期间的[认知负荷](https://github.com/Phantas0s/alexandria-library/blob/master/teaching_learning/_PAPERS/1988_cognitive_load_during_problem_solving.pdf)：对学习的影响》中首次提出的，它指执行一个任务所需的精力或信息处理量。就[软件开发](https://en.wikipedia.org/wiki/Artifact_(software_development))而言，认知负荷是处理软件工件所涉及的思考努力，这取决于任务和个人。

Robert Martin在他的书《代码整洁之道》中[指出](https://www.goodreads.com/quotes/835238-indeed-the-ratio-of-time-spent-reading-versus-writing-is)，“**开发者花在阅读和理解代码上的时间是编写代码时间的10倍以上**。” 不仅如此，如果认知负荷过高会变得普遍并[加剧](https://my.chartered.college/impact_article/%2520cognitive-load-theory-and-its-application-in-the-classroom/)，这会限制人们有效处理和记忆信息的能力，导致任务完成延迟、错误和次优解，并增加压力，可能导致职业消耗并降低工作满意度。

## 认识平台工程

[平台工程](https://blog.mia-platform.eu/en/is-platform-engineering-putting-an-end-to-devops-and-sre)是为自助服务能力设计和构建工具链和工作流程的实践，以降低云原生时代软件开发的复杂性和不确定性。[内部开发者平台](https://blog.mia-platform.eu/en/the-internal-developer-platform-revolution)(IDP)非常重要，它可以可靠地管理应用程序配置，必要时构建新的完全配置的环境，提供持续交付或部署的流水线，更重要的是保护开发项目的安全。

例如，在传统环境中，启动一个新项目需要花费几个小时手动配置开发环境。

现在，想象您有一个图形界面或命令行界面[来编排复杂的软件开发流程](https://thenewstack.io/enabling-devops-control-for-those-who-need-it-most-developers/)。如果您使用 IDP，只需通过该界面或命令行界面执行一个命令指定您的偏好，IDP 将自动管理所有配置来启动环境。

此外，平台工程等变革性方法可以自动化重复任务，减少软件工程师的精力消耗，消除人为错误。

## 重新定义开发者工作流程

近几十年来，技术的出现简化和加速了软件开发过程。最重要的是革命性的DevOps理念，它通过[促进协作、自动化、持续集成和交付催生了平台工程](https://thenewstack.io/platform-engineering-in-2023-dev-first-collaboration-and-apis/)。令人印象深刻的是，DevOps可以:

- **通过CI/CD流水线等任务的自动化来弥合开发和运维之间的鸿沟**，实现更快更可靠的软件发布。
- **通过自动化代码集成和部署来减少认知负荷**，使开发者可以专注于解决问题和创新。

## 认识平台工程对生产力的影响

根据[Puppet的报告](https://www.puppet.com/resources/state-of-platform-engineering%23top)，在组织内实施良好的平台工程实践，有37%的受访者对他们的产品交付流程的有效性“非常满意”。这种鼓舞人心的认可证明，增强的开发者体验无疑可以提高生产力。

具体来说，平台工程具有两个重要功能:

- 通过一致的工具和框架，简化开发项目的启动。
- 通过内部开发者平台[为开发者提供测试和部署代码所需的一切](https://thenewstack.io/mvp-or-tvp-why-your-internal-developer-platform-needs-both/)，最大限度地减少开发生命周期中的等待时间。这些内部平台到处都是自动化构建、测试和部署应用程序的工作流程。

一个更实际的例子可以说明这是如何工作的。想象一下您的开发团队在同一个项目的不同分支上工作。当某人提交更改并推送代码时，IDP 运行所有的流水线，检查兼容性，将代码转换为工件，并在所有选择的服务器和环境上运行它。在传统环境下，开发人员需要跟踪和监督整个过程，手动启动每个阶段。而在平台工程中，这些重复任务都是由 IDP 提供的自动化来执行，开发人员不需要采取进一步操作。

## 利用平台工程的优势

通过规定开发者负责编写、部署和维护生产环境中的代码，DevOps 的“你写的代码，你运行它”原则无意中增加了技术专业人员的认知负荷。平台工程[通过提供以下优势来解决这个问题](https://thenewstack.io/platform-engineering-benefits-developers-and-companies-too/):

- **降低复杂性**:平台工程找到并建议正确的抽象程度，使开发者可以绕过复杂的基础设施配置。
- **强大的协作和知识共享**:平台工程通过使用相同的工具、实践和方法，[促进不同团队之间的紧密协作](https://thenewstack.io/how-platform-engineering-can-improve-devops-collaboration/)，因此团队可以轻松相互学习，开发阶段之间几乎没有差距。
- **一致性和可靠性**:通过标准化的工具、流程和基础设施，平台工程通过最大限度地减少测试、部署和维护中的配置错误，确保开发流水线的[一致性和可靠性](https://thenewstack.io/platform-engineers-developers-are-your-customers/)。
- **更短的上市时间**:平台工程对开发流程、可重用组件的[自动化](https://thenewstack.io/nitric-and-the-rise-of-infrastructure-automation-in-platform-engineering/)以及跨职能协作的推广，缩短了产品交付时间。
- **平台工程是DevOps的自然演进**:在DevOps核心理念的基础上，平台工程为整个流程建立了端到端的自助服务设置。Puppet的《[2023年DevOps状态报告](https://www.faros.ai/blog/platform-engineering-the-future-of-devops-or-just-another-buzzword)》中对这种方法的认可表明，相关调查的93%的受访者认为采用平台工程是其团队朝着正确方向迈出的一步。

## 打造可行平台：为开发者铺路

[黄金路径](https://blog.mia-platform.eu/en/golden-paths-platform-engineering)意味着一种与可行平台和标准化云环境协调一致的、具有引导性且支持充分的软件开发技术，用于简化流程。专门的[内部团队策划并维护这些平台](https://thenewstack.io/cloud-control-planes-for-all-implement-internal-platforms-with-crossplane/)背后的技术栈、基础设施和云空间，使这些平台可以发挥加速器的作用，消除软件工程师在每个项目中都要从零开始的需要。

## 克服认知超载

Itrevolution的[报告](https://itrevolution.com/articles/role-of-the-platform-developer-experience/)《2022年DevOps企业论坛指南》指出，76%的被调查组织都同意，学习他们的软件架构所需的认知负载非常重，这给开发人员带来了焦虑和生产力低下。

为了战胜认知超载，开发人员应采用以下策略和技术：

- **简化**:确保代码易于理解、维护和调试，遵循良好的编码实践，即注重清晰而不是小聪明，采用描述性的命名、添加注释和编写文档。避免嵌套循环和条件判断，不必要的复杂度，过度设计和复杂逻辑。
- **抽象和模块化**:通过提高可用性来抽象代码。此外，通过将代码拆分成小的、独立的模块进行模块化，这些模块可以重用并重新组合以构建不同的应用程序。这样，开发人员可以生成易于理解、维护和扩展的解决方案。
- **向他人学习**:精通编程需要终身学习。加入开源项目和社区，研究有经验的开发人员解决问题的方案，并简化流程和程序。此外，通过参与代码审查、与同行合作项目以及寻求反馈，学习编程风格和最佳实践。
- **休息**:不间断的长时间高强度编程会导致认知超载。通过计划和休息，你可以放松身心，重新获得专注力和动力，然后更好地应对过载。可以考虑采用番茄工作法，即工作一段时间后休息一会儿以保持专注和防止耗尽。
- **转向Mia-Platform**:利用Mia-Platform及其框架的功能。熟练掌握相关工具及其功能可以显著减少所需的自定义代码量。

## 总结

随着技术的发展，开发人员在构建、测试和部署应用程序时所承受的认知负荷不可避免地越来越重，使得生产力降低，代码质量也越来越差，更不用说压力加大，甚至导致职业倦怠。

平台工程提供包含[标准化工具、框架和工作流程的自助服务平台](https://thenewstack.io/setting-kubernetes-standards-with-platform-engineering/)，抽象了许多底层复杂性并简化了软件开发和交付。这样，开发人员可以专注于设计创新解决方案，而不是处理管理部署和基础设施等琐碎任务。

同时，开发周期变得更加敏捷，因为开发人员可以快速迭代、测试和发布软件，更快地交付新功能和增强功能。此外，由此产生的更健康、更可持续的工作环境不仅可以防止职业倦怠，还可以让开发人员在满足不断发展的技术环境需求的同时发挥最佳状态。

要了解为何以及如何向平台公司转型，请阅读Mia-Platform提供的这份[白皮书](https://resources.mia-platform.eu/en/white-paper-why-and-how-to-evolve-into-a-platform-company)。

## 常见问题

**为什么平台工程是一个重大趋势？**

因为[平台工程可以优化开发者体验](https://thenewstack.io/platform-engineering-challenge-security-vs-dev-experience/)、加速软件交付过程，同时保持质量标准。

**平台工程是如何工作的？**

通过为开发团队提供构建、测试和部署应用程序的[工具](https://thenewstack.io/high-performing-devops-teams-build-self-service-platforms/)，这些工具带有简化交互的明确定义的API和服务，平台工程为加快应用程序开发建立了基础工具包、服务和框架。

**为什么平台工程很重要？**

平台工程旨在增强DevOps的价值，并为组织保持领先地位提供优势。通过平台工程，您可以:

- **提高软件质量和可靠性**:平台工程通过结合最佳实践、自动化测试和持续集成，建立一个强大的、标准化的高质量和可靠软件开发框架。其结果是用户满意度更高，对产品或服务更信任。
- **提升开发速度和敏捷性**:通过其标准化环境，平台工程缩短了启动新生态系统所需时间。
- **降低复杂性**:通过平台工程，可以抽象系统的复杂性，使软件工程师能够专注于应用程序开发，而不是底层基础设施。
- **改善开发者体验**:平台工程减少了开发者大部分认知负载和精神压力，同时消除了职业倦怠风险。

**平台工程师需要哪些技能？**

为了成功执行设计、实现和维护支持应用程序和设备基础设施的主要任务，平台工程师需要以下技能：

- **软件开发**:熟练掌握编程语言:Python、Java、C++。
- **DevOps**:熟悉部署、监控和自动化工具。
- **云计算**:了解用于构建可扩展和可靠平台的云平台和服务，以及在云上部署、监控和管理应用程序和服务。
- **安全**:深入的安全实践专业知识，以保护平台及其支持的应用程序。
- **API设计**:熟练设计、创建和记录API，以实现平台服务之间无缝交互。

**主要的认知负载类型有哪些？**

- **内在认知负载**:学习材料本身的固有难度。难度越大，负载越重。
- **外在认知负载**:劣质学习材料造成的，例如冗长难懂的术语、结构混乱的材料和不必要的干扰。
- **真正认知负载**:为了长期掌握知识并将新信息整合到现有知识中，你必须承担的负荷。

**脚手架是否可以减少认知负载？**

是的。

[脚手架](https://cloudnative.ly/scaffolding-45ec23a166a0)是通过预构建的框架快速构建应用程序的一种结构或骨架。由于它处理了初始设置，你可以直接进入需要特殊关注和自定义的部分，因此脚手架对于复杂的技术或大型项目特别有帮助。
