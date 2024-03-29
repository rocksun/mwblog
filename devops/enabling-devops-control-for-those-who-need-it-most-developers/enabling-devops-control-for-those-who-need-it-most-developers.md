
# 让最需要它的开发人员控制 DevOps

翻译自 [Enabling DevOps Control for Those Who Need It Most — Developers](https://thenewstack.io/enabling-devops-control-for-those-who-need-it-most-developers/) 。

您无法使用静态脚本语言构建开发人员自助服务平台。我们需要转向 DevOps 的系统设计方法。

![](https://cdn.thenewstack.io/media/2023/03/01899bdc-technology-2-1024x442.jpg)c

基础设施运营的演变是一段漫长的旅程，而且仍在进行中，但真正的游戏规则改变者将在开发人员控制自己的命运时到来。

表面上看，似乎 IT 需求是基础设施技术发展的催化剂。实际上，基础设施技术的根本转变是由于开发人员生产力需求所驱动的。IT 服务于开发人员生产力的意愿，而开发人员对业务结果具有更直接的影响力。无论安全性的论点是什么，如果 IT 在基础设施周围建立了一个封闭的花园，生产力就会受到影响，开发人员会离开。

## 企业计算：使用脚本和 CLI 的 IT 操作

在 90 年代末和 21 世纪初，公司离开了大型机，转向内部部署的“生产力”。微软和 Sun 分别通过 .NET 和 Java 极大地促进了开发人员的能力。应用程序变得越来越复杂。

在 20 世纪 90 年代末和 2000 年代初，公司将大型机留给了本地“生产力”。 Microsoft 和 Sun 分别在使开发人员能够使用 .NET 和 Java 方面取得了长足的进步。应用程序变得越来越奇特。

在基础设施方面，VMware 通过虚拟化技术打破了行业格局，Cisco 在网络领域占据了主导地位，EMC则在存储技术方面成为领导者。Microsoft 在 Windows 方面的垄断地位得到了 Active Directory 的支持。这些基础设施技术随着时间的推移变得越来越复杂，管理它们变成了一种利基技能。

这种日益复杂的基础设施的目的是为了更快地交付软件；这反过来又意味着开发人员需要更高的生产力。理想情况下，开发人员应该通过一个抽象层直接访问基础设施，并自动化低级别的配置细节。然而， IT 却加强了对基础设施的控制。

这种日益复杂的基础架构的目的是更快地发布软件；反过来，这意味着开发人员需要提高工作效率。理想情况下，开发人员应该可以通过一个抽象层直接访问基础设施，该抽象层可以自动处理低级别的配置细节。相反，IT 加强了控制。


## 云计算：DevOps 与基础设施即代码

公共云消除了所有物理基础设施的方面，并以显著简化的实现方式提供了基础设施即服务(IaaS)，速度成倍增长。虽然 AWS 从 IaaS 入手，但 Microsoft 则从平台即服务(PaaS)开始，这证明了它领先于其时代。随后，他们修正了路线，将重点也放在了 IaaS 上。

尽管如此，这个愿景是明确的：服务器、网络和存储管理员的孤立分工被消除了。基础设施的自动化配置已成为事实上的模式，并且比之前的模式快得多。

虽然云计算本身的基本架构实现了核心的颠覆，但基础设施运维工具的改进影响较小。Terraform、Cloud Formation、Chef 和 Puppet 开始在自动化领域取得了重大进展，但接着出现了微服务，这使得活动组件数量成倍增加。

另一方面，云编排器通过将所有云规范化为 IaaS 来专注于混合云，而将数百种本地云服务（如 DynamoDB、SQS、SNS、Kinesis 等）排除在外。充其量，他们充当门面来使用静态模板，这些模板几乎没有灵活性和自助服务，因为他们不断依赖管理员来更新它们。从根本上说，所有这些基础设施脚本工具都不是供开发人员使用的。

启动新环境需要几天或几周的时间。即使在效率最高的公司，OpEx 与 CapEx 的比率仍约为 1:1。例如，如果他们在 AWS 上花费 100 万美元，他们将需要 6 到 10 名 DevOps 工程师。 IT 及其新命名的平台工程仍然是一个很大的成本中心。

## 需要改变什么

基础设施即代码方法的根本变化是无可争辩的，但更重要的是，整个平台工程将不会来自核心受众是运营者的公司。

它将来自云供应商或开发人员，他们亲身经历过痛苦，并且明白您无法使用 Terraform 或其他静态脚本语言的安全护栏构建开发人员自助服务平台。我们需要转向 DevOps 的系统设计方法。

大多数成功的平台，如Kubernetes、可观测性和安全解决方案，甚至公共云本身都是基于系统设计架构构建的。它们都有一个具有观点的接口，通常称为策略模型，并且具有一个状态机，可以将用户的高级规范转换和实现为较低层面的细节。

它们都有一个“作为服务”的主题：基础设施即服务、容器编排服务等等。它们提供了一种可靠且一致的方式来管理和处理许多复杂的用例，无需人工干预，降低了错误的潜在风险，并提高了效率。

实际上，DevOps 自动化需要被看作是一个系统设计问题。简单地将基础设施即服务推广，可以认为 DevOps 即服务可以建立在类似的原则之上，位于基础设施即服务层之上。

为此，在 DuploCloud，我们创建了一个平台，在该平台上，所有基础设施即代码、基础设施配置（包括安全性和合规性控制）以及应用程序部署任务都在基于规则的引擎中自动化，并在第一时间正确配置时间。此外，我们还集成了所有相关的 DevOps 生命周期工具来完成该解决方案。

当用户通过以应用程序为中心的用户界面提交更高级别的部署配置时，内部基于规则的引擎会自动将配置转换为低级别的基础架构构造，同时还包含所需的合规性标准。

IaC 的基本限制在于它是一个连续运行的有人值守脚本，并假定有人在场进行监督。 DuploCloud 平台具有强大的用户友好策略模型和智能状态机，通过调用在多线程中异步工作的云原生 API，将规则引擎生成的低级配置应用到云提供商。

故障会自动恢复，重复的故障会在用户界面中主动标记为错误。该平台不断将基础设施的当前状态与期望状态进行比较，其中包括合规性标准和安全要求。这将控制权交给了开发人员，他们最需要快速有效地交付产品。