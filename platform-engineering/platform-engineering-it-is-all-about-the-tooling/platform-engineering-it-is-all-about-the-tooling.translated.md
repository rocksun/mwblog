# 平台工程：一切皆工具

![平台工程：一切皆工具的特色图片](https://cdn.thenewstack.io/media/2024/07/328685ee-thisisengineering-f7v66rfronu-unsplash-1024x683.jpg)

[平台工程](https://thenewstack.io/platform-engineering/) 的使用和普及率持续增长，越来越多的公司发现它能够赋能软件开发人员并加速其运营效率。

通过采用平台工程，IT 系统管理员选择并组装经过验证、精心策划且定期维护的开发应用程序，并通过一体化的自助服务门户提供给公司的开发人员。该门户使开发人员能够专注于自己的工作，而不是花费宝贵的时间搜索创建和测试代码所需的应用程序。这些平台也被称为[内部开发平台 (IDP)](https://thenewstack.io/the-hidden-benefits-of-internal-developer-platforms/)，旨在为开发人员提供最佳的代码构建工具，并提供易于使用的环境，以实现自动化、标准化和灵活性，以满足繁忙的应用程序开发人员的需求。

但是，要做到这一点，IT 管理员必须首先选择并提供最适合其运营中开发团队的工具组合。

## 选择合适的平台工程工具

IT 管理员在为开发人员提供工具方面有很多选择。他们可以从零开始，根据公司的软件需求审查和选择要整合的单个工具，或者他们可以选择众多经过整理和推荐的参考架构，这些架构已经可用，并帮助他们快速开始。

“门户有不同的类型，有开源的，有不同的供应商等等，”平台工程供应商[Humanitec](https://humanitec.com/?utm_content=inline+mention) 的产品和增长副总裁[Luca Galante](https://www.linkedin.com/in/luca-galante/) 以及年度[PlatformCon 平台工程大会](https://platformcon.com/) 的主持人告诉 The New Stack。

[PlatformEngineering.org](https://platformengineering.org/) 是一个全球性的平台工程开发人员社区，它提供了一个经过整理和推荐的[平台工程工具集合](https://platformengineering.org/platform-tooling)。该工具集合由 Humanitec 于 2022 年 1 月创建，旨在建立标准并帮助行业了解这种新的软件交付方法，它被分为五个开发层。每个层——开发控制层、集成和交付层、监控和日志记录层、安全层和资源层——都包含多个应用程序选项，可用于满足这些开发工具需求。

其他可供选择的工具集合也很多，包括来自[云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention) 的[云原生景观](https://landscape.cncf.io/?view-mode=grid)，它提供了来自广泛的社区项目和供应商的大量选择。

“但最近最大的争论是‘从哪里开始？’”Galante 说。

Galante 表示，正是这种挑战促使 PlatformEngineering.org 创建了自己的推荐和经过验证的[平台工程工具集合](https://thenewstack.io/7-great-tools-for-your-platform-engineering-toolchain/)，旨在为企业提供一个易于使用的起点，将这些实践引入其运营。

“我们根据社区，并参考过去五年中超过 500 个平台工程设置，从[CNCF](https://thenewstack.io/botkube-building-bridges-across-the-cncf-landscape/) 工具景观中提炼出了一些子集，并观察了哪些最佳实践存在以及人们使用什么，”Galante 说。“所以，这基本上成为了所有正在推进或开始其平台工程之旅的人的参考架构。”

他表示，参考架构的概念正在企业中获得越来越多的认可。PlatformCon 2024 活动中约 20% 的演讲者谈到了参考架构，“所以人们现在真的在使用它来讨论如何组织他们的平台，”Galante 说。“显然，他们每个人在不同的[层]中都会有不同的应用程序池，但架构非常非常相似[它们之间]。”
构建平台工程平台最重要的部分是从后端基础开始，因为其余部分基本上都是即插即用，Galante 说。“构建平台就像盖房子，你想要从地基开始，然后在后面添加其他东西。这会给你作为平台团队带来很大的灵活性，以及很强的弹性。后端是协调一切的，前端允许开发人员自助服务，并获得他们需要的工具。这些是平台工程的核心部分。”

## 平台工程平台背后的故事
Galante 说，构成 PlatformEngineering.org 平台工具景观的五个平面包括公司可以为其平台选择的多个组件的类别。这些应用程序类别包括开发者门户、版本控制、应用程序和平台源代码、CI 管道、镜像仓库、平台编排器、CD 管道和基础设施控制平面。其他类别包括 [可观察性](https://thenewstack.io/observability/) 和分析应用程序、[密钥管理](https://thenewstack.io/the-challenges-of-secrets-management-from-code-to-cloud/)、安全、集群管理以及数据、网络和服务应用程序。

PlatformEngineering.org 景观中的这些应用程序包括 [Backstage.io](https://platformengineering.org/tools/backstage-io-spotify)，一个开发者门户；[Atlassian Compass](https://platformengineering.org/tools/compass)，另一个开发者门户；[Harbor](https://platformengineering.org/tools/harbor)，一个开源仓库；[Jaeger](https://platformengineering.org/tools/jaeger)，一个可观察性应用程序；[Helm](https://platformengineering.org/tools/helm)，一个用于 Kubernetes 的开源包维护工具；[MongoDB](https://platformengineering.org/tools/mongodb)，一个开发者数据库，[Cocalico](https://platformengineering.org/tools/project-calico-open-source)，一个用于容器的开源网络和安全应用程序；等等。

“重要的是你的前两个平面——你的开发者控制平面和你的集成交付平面，”Galante 说。“集成交付平面，它是你的平台的后端。在那里你拥有像平台编排器这样的东西。这是最关键的部分——它是平台的大脑，它使你能够真正地使其成为企业级。”

平台构建的第二重要部分是编排器，“它基本上允许开发人员访问平台的这些功能，”Galante 说。接下来是门户和其余的组件，它们帮助将正确的工具交付并呈现给开发团队。

## 将开发人员纳入平台构建方程式
本质上，平台工程就是为开发人员提供自助服务，让他们能够使用他们完成工作所需的应用程序，推动流程自动化，通过减少开发人员需要执行的手动步骤来提高他们的效率，并通过设计将流程标准化。

但是，为了实现这一点，开发人员不应该对将影响他们的平台工程过程有一些意见吗？

“100% 他们应该被包含在内，但他们并不总是被包含在内，”Galante 说。“当他们没有被包含在内时，平台工程问题可能会失败。他们在平台构建时应该有发言权。”

然而，对 Galante 来说，开发人员的参与并不包括对公司 IDP 中将包含和提供的哪些特定工具进行意见，他补充说。

Galante 说，在这一点上，公司的 IT 管理员需要有权选择和提供在公司开发环境中需要的开发工具，并能够确保它们为所有开发团队和人员服务。

“我认为，他们不应该对哪些工具 [应该被选择] 有发言权，”他说。“从开发人员的角度来看，工具是无关紧要的——工程方面的想法是‘让我来担心工具是什么，让我抽象出底层的复杂性’，”他补充说。对于平台团队和开发人员，IT 管理员应该征求意见，但将决定权留给管理员，他说。

“作为一名开发人员，告诉我你想要什么，”Galante 说。“告诉我你需要做什么才能做好你的工作，告诉我哪里有痛点，我会构建一个解决这些问题的平台，推动自动化，让我能够在后端标准化这些东西，你就不必担心所有这些东西，”他说。“这就是为什么他们尽早参与到这个过程中至关重要，并且平台团队和开发人员之间有一个非常非常紧密的反馈循环，因为你想要为他们构建金色的道路，而不是金色的笼子，对吧？”
构建这些平台的主要目标是抽象化复杂性，但不能消除太多上下文，也不能让开发人员自己感到抽象，并与流程脱节，Galante 说。

“问题是，这不是非黑即白，”Galante 解释说。“在企业中，你将拥有 [多个] 开发团队，[每个] 团队已经习惯了他们特定的工具——他们有自己的 [CI/CD](https://thenewstack.io/ci-cd/) 应用程序等等。问题是，平台团队很难 [对单独请求的工具] 进行标准化，因为每个开发团队都有自己的风格，做事方式也不同。”

这意味着平台团队只需要做他们认为对整个公司最好的事情，并为每个团队和每个开发人员提供相同的标准平台供他们使用。

“所以，这使得它成为覆盖所有人的最小公分母，”Galante 说。“显然，这不会让每个人都满意，但它应该改善每个人的整体体验。”

平台工程和迁移到 IDP 是为了使整个组织受益而做出的决定，它需要来自工程部门的某种自上而下的协调。

“你需要建立这些反馈循环……但从业务对齐的角度来看，需要有明确的执行决策来推动这一点，以便它有意义，”Galante 说。

对于大型企业来说，平台工程已经获得了青睐，因为它为开发人员提供了广泛的自由和创造力，他们不再需要等待几周才能让 IT 管理员响应票证请求，以便他们可以使用所需的工具完成工作。这就是为什么像 [AWS](https://aws.amazon.com/?utm_content=inline+mention)，[Google](https://cloud.google.com/?utm_content=inline+mention)，Facebook，Netflix 等大型公司在 2010 年左右开始开发自己的 IDP，Galante 说。

“但我们现在正处于每个保险公司、银行或任何拥有数千名开发人员的公司都处于相同境地的阶段，对吧？”Galante 说。“所以，如果你是一家企业，他们都处于相同的情况，你需要在开发人员和运营之间提供这个平台层。这就是我们现在所处的阶段。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等等。