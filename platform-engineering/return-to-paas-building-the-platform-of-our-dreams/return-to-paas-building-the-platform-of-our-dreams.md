
<!--
title: 回归PaaS：构建我们梦想中的平台
cover: https://cdn.thenewstack.io/media/2025/01/e7aaa7fe-return-to-paas.jpg
-->

使用现代 PaaS 重新发现应用部署的简易性。了解 Heroku 等云原生工具如何改变生产力。

> 译自 [Return to PaaS: Building the Platform of Our Dreams](https://thenewstack.io/return-to-paas-building-the-platform-of-our-dreams/)，作者 Doug Sillars。

回想云计算时代的初期。将本地主机上运行的应用程序部署到云中的过程复杂而费力。开发人员会花费数小时创建云环境、数据库和服务器。构建部署管道来构建和启动我们的产品导致了额外的启动时间，从而减缓了创新速度和开发人员交付成品的能力。

随后出现了旨在简化应用程序部署到云中的产品，将平台即服务 (PaaS) 引入应用程序开发领域。无论您的应用程序是用什么语言编写的，您只需`git push`您的代码，平台就会完成其余工作。几分钟内，您的应用程序就会部署并上线。

例如，Heroku 的平台彻底改变了云优先部署，将您的应用程序容器化到带有内置数据库支持的 dynos 中。部署应用程序到云的复杂性消失了。开发人员的生产力提高了——他们不必担心棘手的云基础设施，而是可以回到编写应用程序的工作中。

但是现在，日益复杂的云工具正在减缓开发人员的生产力，并[掩盖了 DevOps 的最初承诺](https://thenewstack.io/the-2024-state-of-platform-engineering-fledgling-at-best/)。随着技术栈的扩展和基础设施需求的增加，开发人员失去了专注于交付应用程序价值的能力。为了解决这个问题，我们需要简化云部署的解决方案，并允许团队专注于构建优秀的应用程序。

## 复杂性和开发人员痛苦的回归

当然，自从 Heroku 首次推出以来，云计算发生了很大的变化。PaaS 和容器化的成功已推动整个行业优先部署到云中。应用程序现在默认情况下是云原生的，因此，已经构建了整个生态系统来帮助开发人员启动云原生应用程序。DevOps 的承诺导致开发人员不仅拥有应用程序代码，还负责运行应用程序的基础设施的运营和维护。

这导致了云计算领域更大的创新。[Kubernetes](https://thenewstack.io/kubernetes/) (K8s) 被称为“云的操作系统”。K8s 旨在帮助编排容器的使用——在我们的基础设施中部署、扩展和管理代码。在一个生态系统中控制所有[DevOps](https://roadmap.sh/devops) 需求的能力已导致 K8s 在全球范围内被广泛采用。

K8s 平台上的创新导致了数千种开发人员工具和产品的创建，这些工具和产品建立在 K8s 之上并改进在 K8s 之上构建平台。可以使用强大的开源云原生工具生态系统来解决无数问题。

但是：

- 无数的工具和选项会带来成本，从而减缓开发团队的速度。
- 团队面临着确定合适的工具、实施它们和维护平台的挑战。
- 技术栈呈指数级增长，增加了复杂性和认知负担。
- “你构建它，你拥有它”的 DevOps 原则分散了开发人员对交付应用程序价值的注意力。
- 团队越来越被维护复杂的解决方案所拖累，仅仅是为了启动应用程序。

![Diagram of a complex Kubernetes architecture](https://cdn.thenewstack.io/media/2025/01/7aeca3d9-kubernetes-complexity-1024x672.jpeg)

*Kubernetes 的复杂性，基于“[Navigating Kubernetes Complexity (Part I)](https://medium.com/pipedrive-engineering/navigating-kubernetes-complexity-part-i-37781d4b3ecf)”中的图表。*

请记住，我们构建的不是云部分；我们构建的是**在该云上运行的应用程序**。我们再次看到团队被用于启动应用程序的复杂解决方案的支持和维护所拖累。

## 平台工程：控制复杂性

大型组织更有可能拥有支持平台工程师团队的预算——一个在构建和部署云平台方面拥有深厚专业知识的团队。[平台工程团队](https://thenewstack.io/the-2024-state-of-platform-engineering-fledgling-at-best/) 为组织内部的 DevOps 实践提供标准化和自动化。他们创建[内部开发人员平台](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/)，允许内部开发人员简单地选择他们需要的基础设施类型，它将为他们创建。

![Triangle with K8s infrastructure at the bottom, platform engineering in the center, and developer teams at the top](https://cdn.thenewstack.io/media/2025/01/3aeb90ca-platform-engineering-standardization-automation.jpeg)

*平台工程团队的组建旨在为DevOps提供标准化和自动化。*

这通过减少DevOps领域的范围，降低开发人员的认知负荷并简化云部署来提供更好的开发人员体验。

组织可以通过引入专门的平台工程团队来减轻技术栈庞杂和简化云操作的挑战。但是，并非所有组织都拥有实施这些专业团队的资源。这加剧了对更现代化解决方案的需求。

## 现代PaaS的引入：云优先和K8s

K8s已成为在云中部署容器化应用程序的首选平台。较小的组织可能没有时间或专业知识来创建平台工程团队或构建定制的云开发平台。较大的组织可能希望简化某些应用程序，而无需与他们的平台工程团队进行内部部署讨论。在许多情况下，我们可以利用构建在现代K8s云栈之上的现有开发人员云平台。这是现代平台即服务的回归。

现代PaaS——例如Heroku最近[推出的下一代PaaS](https://blog.heroku.com/next-generation-heroku-platform)——是基于现代云部署的最佳实践构建的。您构建您的应用程序，Heroku创建容器（使用Cloud Native Buildpacks）。Heroku利用其[K8s专业知识](https://blog.heroku.com/heroku-joins-cncf-platinum-member)来管理和编排您的应用程序，并抽象掉所有复杂性。例如，无需成为容器可观察性专家，因为OpenTelemetry已内置并连接到Heroku Metrics，并可通过Heroku软件开发工具包（SDK）访问。

开发人员（甚至您的平台工程团队）不再需要一遍遍地进行相同的部署；PaaS会为您处理，使工程师能够专注于其核心职责。

## 总结

在云计算的早期，PaaS服务帮助开发人员绕过了云部署的复杂性和挫败感，以便他们可以[专注于他们的应用程序](https://thenewstack.io/open-source-drives-the-twelve-factor-modernization-project/)。随着云计算的发展和壮大，云工具生态系统的功能和复杂性呈指数级增长。虽然这些工具为开发团队提供了更多功能和灵活性，但实施所需工具的规模正在降低开发人员的生产力和交付的操作复杂性。

云原生平台即服务的回归意味着团队可以依靠行业专家来构建并从其云平台中抽象出复杂性。开发人员的生产力得到了提高，因为他们可以专注于构建和交付应用程序——知道他们的应用程序的部署和管理正在由PaaS安全地管理。
