
<!--
title: 内部开发者平台：来自100多位专家的对话见解
cover: ./cover.png
-->

内部开发者平台是您的下一步正确选择吗？

注意：感谢您对该主题的宝贵意见。我收到了来自内部开发者平台运营商、失败公司、后悔公司、对平台感到满意的公司以及将其转变为产品或 SaaS 解决方案的公司提供的见解。我已经探索了它带来的价值，并发现最终许多解决方案都具有类似的逻辑。

> 译自 [Internal Developer Platform: Insights from Conversations with Over 100 Experts](https://itnext.io/internal-developer-platform-insights-from-conversations-with-over-100-experts-dbe332353afc)，作者 Artem Lajko。

## 我学到了什么，我对 IDP 炒作的看法是什么？

我将直接从我的对话中获得综合输出。我已经写了一篇关于 IDP 的构成及其如何组合的文章：[内部开发者平台：真实存在还是仅仅是趋势？](https://medium.com/me/stats/post/ee9c97870dcc)”

### 1. 内部开发者平台可以是任何东西，也可以什么都不是

您没有听错。关于内部开发者平台 (IDP) 的定义没有定论。许多人试图根据属性、自动化程度和它提供的价值来定义 IDP 的成熟度模型。

我会保持简单，向您展示不同的公司对 IDP 的理解。

IDP 可以简单地是提供给其他团队的带有蓝图的文档或指南。在这种情况下，公司不是在谈论 [Terraform 模块](https://www.terraform.io)、[Helm 图表](https://helm.sh) 或像 [APT](https://wiki.ubuntuusers.de/APT/) 这样的包工具。他们真正指的是：

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*28qfZE7ryhMmqM9EfTwyTg.gif)

*基于文档的内部开发者平台*

是的，您没有看错。有些公司说，如果我们提供一个带有占位符的蓝图，不同的开发人员可以使用它，那么它对我们来说就符合 IDP 的标准。我多少同意这种观点。团队 X 向一个或多个团队提供模板，并提供有关如何使用该服务作为自助服务的说明。

IDP 也可以包含 Terraform 模块，团队成员可以根据其他用户的指南在本地配置和部署这些模块。它看起来像这样：

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*s4067Pn6a2LXhDvghTt5AA.gif)

*基于 Terraform 模块的内部开发者平台*

这更符合我对 IDP 的理解。您提供基础设施即代码或配置即代码，只需要设置用户定义的配置。

IDP 也可以是一个已经实现相当高自动化程度的门户。这意味着我可以通过点击或 API 请求特定 T 恤尺寸的模板，并自动获得所有内容的部署。这指的是类似的东西：

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EqhqVledrbARt2q6v6ghpg.gif)

*基于内部开发者平台的门户*

您可以看到不同的公司对这一点有不同的理解，而且这些差异也有一些合理的理由。我将在后面讨论这个问题。

下面，我试图捕捉到我与之交谈过的公司的不同状态。

### 2. 自动化的成熟度级别

在本节中，我们将考察公司的不同状态。这与级别的质量无关，而是对一个人如何看待自己或运作的分类。

CNCF WG 平台有一份非常棒的工作，它为白皮书做出了贡献，并开发了这个名为 [平台功能](https://tag-app-delivery.cncf.io/whitepapers/platforms/) 的很棒的图形：

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*yufSDoy_wssmR07h1OruJw.png)

*[平台功能](https://itnext.io/internal-developer-platform-insights-from-conversations-with-over-100-experts-dbe332353afc)*

如果您了解平台的功能，那么您可能比许多核心业务不是软件或产品开发的中小型企业有更广阔的视野。

这就是为什么我试图抽象它来简化概念。我创建了一个堆栈，每个人都应该熟悉。在下一步中，我们将看看不同级别的自动化。

![](https://miro.medium.com/v2/resize:fit:972/format:webp/1*wurA3Fe_EO8d8EVmeyW7XQ.png)

*自动化成熟度等级。*

**级别 0：ClickOps**

仍然有许多公司更喜欢 [ClickOps](https://blog.equinix.com/blog/2022/12/01/what-is-clickops-and-how-can-you-prevent-it/)，无论是在本地还是在云中，因为他们认为它更快。我不会评判这种方法；它只是事实。

**级别 1：脚本：Bash、Python 或 PowerShell**

许多公司将自动化理解为运行脚本。由于这不是通过点击完成的，他们认为它是自动化的。同样，我不会对此进行评判。

**级别 2：基础设施即代码和配置即代码**

在我看来，脚本的下一个级别是使用像 Terraform 这样的工具来配置基础设施，以及使用像 Ansible 这样的工具来配置它。

**级别 3：流水线：IaC + CI/CD 或带有 CRD 的操作符**

更进一步，IaC 将不再从客户端设备本地执行，而是通过流水线执行，或者您将使用像 Crossplane 这样的工具，它会自动配置相应的资源。

**级别 4：Terraform 模块、Helm Chart 和 GitOps**

在专业化时，您会将基础设施的重复部分打包到 Terraform 模块中，以配置基础设施或 Kubernetes 集群，例如。随后，您将使用 GitOps 方法将基础设施作为应用程序交付到相应的集群。这里的自动化程度相当高。我所说的“相当高”是指：

1. 我可以随着项目的增长而扩展吗？
2. 我也可以扩展维护和运营以避免技术债务吗？
3. 我可以在不增加员工数量的情况下扩展设置吗？

这仍然由人执行，特别是平台团队。

**级别 5：用门户替换人工**

下一级将涉及用抽象层替换级别 4 的人工组件。这并不意味着平台团队被替换；仍然需要有人构建 Terraform 模块、Helm 图表、流水线等，以便可以通过模板推出这些模块。

我认为了解您所处的级别很重要，因为我经常将此级别与公司内的技能和资源相关联。根据我的观察，**自动化程度低**与**基础设施异构**之间似乎存在**相关性**，这反过来又与公司经常面临资源瓶颈并通过员工进行扩展有关。

这也经常反映技能水平。这并不意味着人们的技能水平很低；事实上，恰恰相反。它指的是我的公司目前在云原生路线图上的位置（我们是否使用 Git，我们是否使用容器，CI/CD，我们是否有 IaC 和 CaC 等）。

我试图对此进行映射，我相信许多人会理解它。首先，让我们看一下云原生路线图上的一些重要技能点。低不好，高好。

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*lG7xw_oTeOqSgtJ-59XmSg.png)

*技能集：云原生路线图*

现在我们试图在自动化级别识别这些点。

**命令式**是指指示某人执行特定操作或任务的命令或指令。

![](https://miro.medium.com/v2/resize:fit:1384/format:webp/1*PmVMRYGEdjQn36qKYxTzcg.png)

*命令式*

**容器化**是将应用程序及其依赖项打包到容器中的过程，使它们能够在不同的计算环境中一致地运行。

![(https://miro.medium.com/v2/resize:fit:1126/format:webp/1*EXJOukp-vkeODc9mkZ9JPw.png)]

*像 Docker 这样的容器化*

**声明式**是指一种编程方法，您在其中指定*期望的结果*，而无需明确概述实现该结果的步骤，从而允许系统自动管理实现细节。

![](https://miro.medium.com/v2/resize:fit:1156/format:webp/1*BnqQJLO3EIEL_YMpWg00bw.png)

*声明式*

**API 驱动**是指一种设计方法，它优先使用应用程序编程接口 (API) 作为不同软件组件之间交互的主要方式，从而实现跨系统无缝通信和集成。

![](https://miro.medium.com/v2/resize:fit:1130/format:webp/1*KNPscYOo4u9Goehds4d2vQ.png)

*API 驱动*

**包管理**是自动执行软件包的安装、升级、配置和删除的过程，确保软件依赖项在不同的环境中（Helm 图表、APT 等）正确管理和维护。

![](https://miro.medium.com/v2/resize:fit:1130/format:webp/1*KNPscYOo4u9Goehds4d2vQ.png)

*像 Helm 图表这样的包管理*


**编排**是指对复杂流程或工作流的自动化协调和管理，通常涉及多个服务和系统，以确保它们高效有效地协同工作（Kubernetes）。

![](https://miro.medium.com/v2/resize:fit:1200/format:webp/1*Y9VRJDVIZDTOMMCAKDGh4Q.png)

*像 Kubernetes 这样的编排*

如您所见，存在以下相关性：

- **级别 0-1**：主要采用命令式方法，没有容器化或编排。
- **级别 2-3**：在命令式和声明式之间过渡，并朝着容器化和 API 集成迈出第一步。
- **级别 4-5**：强烈关注声明式方法，广泛使用容器化、编排和 API 驱动的环境，以及包管理。

### 3. IDP 如何融入其中以及它们提供的服务

我见过的多数解决方案在逻辑上都以类似的方式构建。提供了一个门户，通常基于内部开发平台，该平台通常由一个 [操作符](https://www.redhat.com/en/topics/containers/what-is-a-kubernetes-operator) 组成。这意味着有一种方法可以将基础设施转换为模板，使其可用。换句话说，存在一个简化使用的抽象层。

因此，通常至少涉及两个方面。例如，**平台团队定义模板**，以便开发人员可以更轻松地使用它们。**然后，开发人员成为这些模板的用户，或者可以使用相同的工具来抽象他们自己的应用程序**。但在这种情况下，抽象意味着什么？

让我们看一下下面的图表：

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nt9ES_Qd2KO6GwTe31Eg5g.gif)

这里很清楚，平台团队抽象并定义了部署 Web 应用程序服务所需的一切。开发人员只需设置 2-3 个值，而不是与整个 Kubernetes 清单作斗争，并且 Web 应用程序由操作符部署。这以简化的方式呈现，但基于 IDP 的门户本质上并没有做任何不同的事情——只是更复杂。如果您用 Humanitec 的编排器替换上面的简单图表，您会看到逻辑上的某种相似性：

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*DskhFEt5HeKmqCjp2f3iQQ.png)

### 4. 使用 IDP 适合谁？

在我尝试回答这个问题之前，请您看一下下面的图表。请花点时间思考一下：

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*SPmefHrqIklEwwYovgrW6A.gif)

我认为在深入探讨内部开发者平台和门户网站之前，首先应该**评估自动化程度**。这里“自动化程度”一词不应被理解为字面意思，而应理解为理解我们目前所处的位置以及原因的同义词。如果你发现自己处于**0-1级**，我个人质疑你想将什么集成到门户网站中——脚本？如果你处于**2-3级**，你可能会考虑投入更多资金以达到**3-4级**，然后再着手处理IDP问题。最好是弥合差距，包括技能差距，为具有门户网站的IDP奠定坚实的基础。

我遇到的大多数构建IDP的公司，例如基于Backstage的，都处于**4-5级**。对他们来说，Docker、CI/CD、IaC、Kubernetes等已经**成为基本技能**，使他们能够继续进行其他主题。

当你开始学习数学时，你从基本的算术运算开始，而不是直接跳到大学的高级数学。我认为IDP+门户网站也是如此。最好在公司**建立坚实的基础**，而不是追逐你负担不起的趋势。

### 5. 自建还是购买？

我与大多数公司交谈过，特别是那些列为非提供商的公司，他们倾向于选择SaaS解决方案或自托管选项，其中SaaS是首选。许多公司不愿使用IDP，因为他们不想取代与平台工程相关的“人”的因素。

**关于“自建还是购买”的主题，我听到的大多数说法（反对自建）如下**：

- 提供商提供托管服务，他们的内部团队或外部客户团队规模较小，因此实施IDP的努力不值得。
- 然而，许多公司更愿意先将他们的各个层级专业化，然后再着手构建IDP，以确保坚实的基础。
- 一些公司表示，他们在平台工程和取代门户网站的“人”的因素方面速度更快。不需要自建或购买IDP/门户网站。
- 复杂性已经很高，添加另一层不会帮助公司前进。

**自建还是购买的个人评估**：

- 处于0-3级的公司面临的挑战与涉及IDP/门户网站的公司不同。
- 服务提供商应考虑→购买或自建（创新、新产品等）
- 拥有较少专家但处于4-5级的内部IT公司→购买。
- 拥有较少平台工程师和小型开发团队的公司应考虑→购买或进行平台工程。
- 拥有10-15名平台工程师和500-1000名开发人员的公司应→购买。

这不是一个容易的决定。我总是试图从价值的角度思考，并问自己，它能给公司带来什么附加价值？

- 创新？
- 更快的上市时间？
- 通过自助服务实现可扩展性？
- 减少平台工程师的认知负荷？
- 等等。

然而，关于所有这些主题，有一点让我深感担忧，我将在下面简要讨论。

### 6. 为什么如此关注开发者？

我不明白为什么每个人都在谈论赋能开发者；有时感觉就像把开发者当作没有训练轮的小孩一样，让他们骑自行车。IT公司真的只由开发者组成吗？说实话，公司中其他IT专业人员经常被忽视，这让我很恼火。目标是分裂文化，然后通过DevOps 3.0将它整合到组织中吗？

我们未能通过DevOps在开发者、运维和其他部门之间建立文化，现在又有了平台工程。

为了让你理解我的沮丧，让我分享一个并非由于平台工程而产生的发展，即使它可能看起来是这样，而是通过GitOps和Argo CD等工具实现的。今年，一家大型公司出现了一种新的文化，我当时就在现场，并参与其中。

过去，平台工程师/运维人员与开发人员的合作比与其他团队的合作更密切。

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*DOivzUbKWV0F_w9j1RAjIg.png)

然而，现在，一种我从未想过会发生的合作形式正在出现。

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*A6D0yMb6Nyc9UbRehO4VYA.png)

我看到服务所有者亲自动手，学习如何管理Grafana仪表板和Prometheus警报作为代码，并使用Argo CD将它们部署到不同的集群中。这提高了服务的质量，因为他们了解服务应该如何运行。它增强了与开发人员和运维人员的合作，因为他们突然之间说起了共同的语言（YAML）。此外，还有一些服务提供商在多个集群中提供服务，并且作为产品运营商，现在使用相同的GitOps（多租户分离）实践部署他们外部的自定义警报。

如果IDP继续以开发者为中心构建，我担心新兴的文化将会崩溃，我们将来需要DevOps 3.0来重建它。

您一定要看看[平台工程成熟度模型](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)！

接下来，我将向您展示最知名的门户提供商，包括 SaaS 和自托管解决方案，其中许多我都有过交流或收到过意见。

## 哪些门户存在？

以下是根据交流了解到的门户概述。

* [port](https://www.getport.io)
* [Mia](https://mia-platform.eu/)
* [Humanitec](https://humanitec.com/)(基于其自身编排器 + 评分的门户)
* [Appsmith](https://www.appsmith.com)
* [Mogenius](https://mogenius.com/)
* [Qovery](https://qovery.com/)
* [OpsVerse](https://opsverse.io)
* [OpsLevel](https://www.opslevel.com)
* [Flanksource](https://www.flanksource.com)
* [Portainer](https://www.portainer.io)
* [Kubermatic Developer Platform on KCP](https://docs.kubermatic.com/developer-platform/)
* [GiantSwarm](https://docs.giantswarm.io/vintage/platform-overview/)(基于 Backstage 的平台)
* [suXess](https://suxess-it.com)(基于 Backstage + Kargo 的平台)
* [kratix](https://www.kratix.io/)
* [Wayfinder](https://www.appvia.io/wayfinder)

如果有遗漏，请在评论中写出来！

您想对主题做出贡献吗？那就行动吧！→ [https://tag-app-delivery.cncf.io/](https://tag-app-delivery.cncf.io/)

## 联系方式

有问题、想聊天，还是想保持联系？跳过 Medium 评论，让我们在 [LinkedIn](http://www.linkedin.com/in/lajko) 上联系 🤙。别忘了订阅 [Medium 新闻](/@artem_lajko/subscribe)，这样你就不会错过任何更新！