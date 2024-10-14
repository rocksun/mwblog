
<!--
title: 阿迪达斯 SRE 的平台工程意味着什么
cover: https://cdn.thenewstack.io/media/2024/10/bcdf2973-what-platform-engineering-meant-for-adidass-sres.jpg
-->

从单体架构迁移到微服务架构需要平台工程和可观测性，但这给阿迪达斯的网站可靠性工程团队带来了新的挑战。

> 译自 [What Platform Engineering Meant for Adidas’s SREs](https://thenewstack.io/what-platform-engineering-meant-for-adidass-sres/)，作者 Jennifer Riggins。

在电子商务领域，每一秒都至关重要。因此，当全球运动服饰公司阿迪达斯在去年的黑色星期五将每秒请求量从不到 3,000 个提升到 29,000 个时，这意味着订单量增长了十倍。前提是网站能够承受住这样的流量。

几个月前，网站可靠性工程 [(SRE)](https://thenewstack.io/sre-vs-platform-engineer-cant-we-all-just-get-along/) 团队与技术主管、系统架构师和业务部门合作，精心策划了一场[平台工程](https://thenewstack.io/platform-engineering/) 转型，将阿迪达斯的架构从单体架构现代化为微服务架构。这本应能够实现可扩展性。

然而，当网站处理优惠券的功能出现故障时，这种新的复杂性带来了新的挑战——这一切都发生在不断受到运动鞋机器人（专门用于购买运动鞋进行转售的机器人）威胁的情况下。在 9 月份的[DevOpsDays 伦敦](https://devopsdays.org/events/2024-london/) 大会上，SRE 团队分享了阿迪达斯在平台工程、[可观察性](https://thenewstack.io/observability/)、[安全性](https://thenewstack.io/security/) 和[微服务](https://thenewstack.io/microservices/) 方面的历程。

## 单体架构的代价

当[Andreia Otto](https://www.linkedin.com/in/andreia-otto/) 七年前加入阿迪达斯担任 SRE 和运营软件工程高级总监时，该公司软件开发人员的发布周期为六周。

“开发团队需要工作六周，然后在发布前一天，我们会召集很多人开会，讨论所有变更，审查所有即将上线的内容，”她在 DevOpsDays 大会上告诉观众。“这就像把球扔到另一边。开发和运营是完全分离的。”

此外，基础设施无法根据需求进行扩展。电子商务团队需要提高热门运动鞋发布的订单吞吐量。几年前，阿迪达斯开展了一项活动，由于需要进行大量限流才能销售抢手的库存，活动不得不延长了三天。

很明显，转向微服务对于节省时间和金钱至关重要。事实也证明了这一点。

“今年，我们开展了类似的活动，却只用了几个小时就完成了，”Otto 说。“我们动员的人员更少，时间也更短。对于公司来说，这样销售的成本更低，可以降低运营成本和供应商依赖性。”

阿迪达斯 SRE 团队还旨在通过采用平台工程方法来促进从单体架构到微服务架构的迁移，从而降低运营成本和供应商依赖性。

该团队从能够计划三天让平台每分钟处理 4,000 个订单，转变为在几个小时内推出能够每分钟处理 40,000 个订单的版本。

“我们曾经有一个庞大的单体应用，负责从前端到后端的全部功能，”Otto 说。“现在我们拥有完全的控制权——当然，复杂性也大大增加，但我们仍然拥有完全的控制权。”

## 阿迪达斯的微服务架构

阿迪达斯工程团队首先在消费者体验、网站、B2B、零售店和应用程序中实施了自上而下的 MACH 架构：

- **微服务。** 将单体应用分解为业务功能，包括购物车、促销、日志记录、B2B 和结账，每个功能至少包含一个微服务，并拥有自己的端到端 CI/CD 管道和独立的生命周期。
- **API优先。**“ 我们希望只构建一次功能，并能够在任何地方使用它，”Otto 说，这包括与渠道无关，并能够使用可重用的 API。
- **云原生。** 这包括为[Kubernetes](https://roadmap.sh/kubernetes) 集群配备专门的团队，以及采用一些[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention)。
- **无头化。** “如果你在电子商务领域工作，你会很清楚，前端需要比后端进行更多更改，”Otto 说。“如果一个团队需要更频繁地部署，他们[必须]独立于需要更少部署的团队。”

![Andreia Otto 和 Ravikanth Mogulla 在 DevOpsDays 伦敦大会上解释了阿迪达斯的 CI/CD 管道（来源：Jennifer Riggins）。](https://cdn.thenewstack.io/media/2024/10/fd756c42-adidas-cicd-pipeline-1-1024x706.jpg)

*Andreia Otto 和 Ravikanth Mogulla 在 DevOpsDays 伦敦大会上解释了阿迪达斯的 CI/CD 管道（来源：Jennifer Riggins）。*

在阿迪达斯，平台工程团队提供[内部开发者平台](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/)、[Kubernetes](https://thenewstack.io/kubernetes/)、可观察性工具和基于 Kafka 的数据平台。然后，SRE 团队位于平台和应用程序开发团队之间。
奥托表示，迁移到新平台的目标之一是通过自动化 Jenkins 中从推送到 Kubernetes 部署的所有内容来赋能开发人员。然后，所有内容都与 Microsoft Teams 集成，以提高整个工程组织的透明度。

“如果允许分支或任何已部署的代码进入生产环境，我们有一个自动化程序会在 Teams 中弹出一个消息，你可以点击按钮”来批准发布，奥托说。“有一个意识上的决定，即不要将所有内容都自动化到生产环境。有些团队比较成熟，有些团队比较不成熟。”

一个更成熟的团队可能已经采用了渐进式交付技术，例如 [金丝雀部署](https://thenewstack.io/5-deployment-strategies-the-pros-and-cons/)，但即使是他们也需要在进入生产环境之前进行最终批准。

## 新平台，新问题

演示者展示了一个 Willy Wonka 的表情包，让 DevOpsDays 的观众哈哈大笑：

![](https://cdn.thenewstack.io/media/2024/10/cc928258-willy-wonka-microservices-meme-2-1024x853.jpg)

在平台工程中，为什么往往比怎么做更容易。当 Adidas 在 2023 年 7 月转向微服务平台时，它可能提高了上市速度，但也大大增加了其在四个主要方面的复杂性：

- 服务可用性。
- 部署中的重大变更。
- 代码重复。
- 安全。

“以前，我们只有一个需要进行故障排除的单体大型服务，”奥托作为 SRE 团队说。“现在，如果出现问题，我们有所有这些东西需要弄清楚，以确保我们拥有适当的日志、适当的跟踪，并且整个 CI/CD 也是独立的。这意味着复杂性要高得多。”

![Andreia Otto 和 Adidas 的 Ravikanth Mogulla 展示了他们的系统在从单体架构迁移到微服务后变得多么复杂。](https://cdn.thenewstack.io/media/2024/10/06fc5cdf-adidas-tech-complexity-1-1024x768.jpg)
Andreia Otto 和 Adidas 的 Ravikanth Mogulla 向 DevOpsDays 伦敦的观众展示了他们的系统在从单体架构迁移到微服务后变得多么复杂。（来源：Jennifer Riggins）

在迁移之后，SRE 团队可能发现他们拥有了更多控制权，但系统的复杂性也大大增加了。

“如果我们的团队知道一件事——我认为在座的各位也都知道——那就是你可以尽可能地做好准备，但事情总会出错，我们需要为此做好准备，”奥托告诉 DevOpsDays 的观众。

她的共同演示者，[Ravikanth Mogulla](https://www.linkedin.com/in/ravikanth-mogulla-6b713026/)，Adidas 的结账和支付网站可靠性工程师主管，表示团队面临着一些经典的挑战，但“我们开始在每一次事件中不断改进。”

以下是如何 SRE 团队在 Adidas 迁移到微服务和平台工程后应对所面临挑战的更多信息：

### 挑战 1：服务可用性

第一个挑战变成了 [可观察性](https://thenewstack.io/observability/)，第一个重大事件发生在黑色星期五——他们通常会经历 10 倍的流量。负责优惠券功能的其中一个数据库开始出现一些性能问题，许多调用在 upstream 服务中堆积起来。

“我们在不同的微服务之间没有适当的超时设置，我们还发现一些微服务在跟踪方面还不成熟，”Mogulla 说。此外，团队发现“负责该问题的服务也没有集成或没有与我们的 [应用程序性能管理] 工具进行跟踪。”

在一年中最大的购物日之一，Adidas 的 [平均恢复时间 (MTTR)](https://thenewstack.io/to-improve-mttr-start-at-the-beginning/) 接近 90 分钟。作为参考，[高性能组织](https://thenewstack.io/googles-formula-for-elite-devops-performance/) 的 MTTR 低于一个小时。SRE 团队压力很大，这是可以理解的。

“我们知道优惠券服务出了问题，[但] 对我们来说最大的挑战是查明确切的问题，因为几乎所有跨所有微服务的调用都失败了。这并不简单，我们不得不联系很多团队，”Mogulla 说。“到那时，已经过去了将近 90 分钟，[而且] 我们损失了很多订单。”

### 挑战 2：部署中的重大变更

新的 Adidas 微服务架构使用 Jenkins 编排来级联来自 .com、web、桌面和移动应用程序的不同 upstream 通道的调用到不同的 downstream 服务。

有一天，当团队一起更新到新版本的 Jenkins SDK 时，其他三个服务同时顺利更新，但由于某种原因，强制同步部署导致 .com 服务停机了半小时。
“我们意识到我们已经使用了不同的版本，这导致了接近 35 分钟的平均解决时间，”Mogulla 说。“我们意识到整个架构现在有多少依赖关系。”

### 挑战 3：重复代码

在 Adidas，SRE 团队负责从平台团队获取基础设施并自动化完整的 [CI/CD](https://thenewstack.io/ci-cd/) 管道。一旦 Adidas 转移到微服务平台，每个应用程序团队都负责自己的监控、安全扫描、[密钥管理](https://thenewstack.io/the-challenges-of-secrets-management-from-code-to-cloud/)、[Helm 图表](https://thenewstack.io/what-the-helm-the-tool-we-all-love-and-sometimes-hate/) 和 [Terraform](https://thenewstack.io/terraform-isnt-dead/) 警报以及自己的 CI/CD 管道。这导致许多团队以不同的方式做着同样的事情，跨越 15 个不同的管道。

SRE 团队正在努力将 Adidas 工程师的基础建立在 DRY 原则上——不要重复自己——旨在减少冗余信息，尤其是在不断变化的领域。

SRE 希望使用 [内部开发平台](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) 来实现不同应用程序团队之间的代码重用。

### 挑战 4：安全

Adidas 平台工程团队负责基础设施和大部分安全，包括入口和密钥管理。这与运动鞋机器人之间的斗争是一场艰苦的战斗——事实上，五种影响最大的机器人中有三种针对 Adidas。

“每当我们有任何大型发布或任何炒作文章时，我们更容易受到机器人的攻击，”Mogulla 说。因此，“我们从 [内容交付网络] 做了很多事情，[这] 为我们提供了许多内置功能，我们确保我们的端点受到保护。”

然而，作为一家上市公司，Adidas 受制于许多利益相关者。他说，业务团队担心误报，而 SRE 更关心阻止漏报。随着微服务将暴露的端点呈指数级增长到 200 多个，找到这种平衡变得更加棘手。

“你无法阻止 100% 的机器人。有些机器人绕过了所有这些 [基于 CDN 的安全] 功能，”Mogulla 说。“我们要么找到独特的标准——无论是用户代理还是 TLS 指纹或哈希密钥——许多标准，比如我们用来阻止的推荐者 [或] 我们识别的直接 LAN、ASN 或 IP 子网，所以它很简单。”

但运动鞋机器人继续变得更加复杂，跨越地理位置。

除此之外，“云原生适用于所有人，包括机器人，因此他们只是在云中旋转不同的容器或集群——然后攻击就变得非常大，”他继续说道。作为回应，SRE 团队在服务之间建立了身份验证并重新组织了事件管理。

## 新的 Adidas 可观测性平台

Adidas 希望通过实施新的故障转移、可观测性和安全措施来提高其弹性。

SRE 团队开始审查所有微服务的超时以解决延迟问题，确定为每个调用、每个端点设置的正确超时。该团队还实施了断路器，以防止一个系统中的故障影响另一个系统，以及添加一个内置的 [功能标志](https://thenewstack.io/moving-to-the-cloud-presents-new-use-cases-for-feature-flags/) 工具。

“作为 Adidas 的 SRE，我们以弹性和稳定性为理念，”Mogulla 说。“每当我们将某些东西发布到生产环境中时，更大的更改，我们总是确保它位于 [功能标志](https://thenewstack.io/feature-flags-making-software-delivery-faster/) 后面，”他说，可观测性是强制性的。

“事实上，从单体架构到微服务架构的整个过渡都在一个功能标志后面。只需单击一下，我们就可以从传统架构切换到新的微服务架构。”

该团队还实施了金丝雀部署和 SDK 版本控制。并且，每当新版本准备就绪时，上游服务会独立部署。

Adidas SRE 团队切换到 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 以实现“更供应商中立”的端到端跟踪。

“在此 [转型] 之前，我们有不同应用程序的日志，但它们都隔离在不同的租户之间，”Mogulla 说。“使用微服务，我们不想在不同的租户之间切换。我们使用 [OpenSearch](https://thenewstack.io/aws-transfers-opensearch-to-the-linux-foundation/)，然后在一个租户中，但日志在不同的索引之间分开，”所有这些都在一个一站式可观测性仪表板中。
为了提高安全性，尤其是针对猖獗的抢购机器人，SRE 现在使用带有安全身份验证的 SSL/TLS 证书保护所有入口，并在所有证书上使用 Mozilla SOP（标准操作程序加密）。他们还维护包含允许列表中 IP 地址的种子代码。

“每一次失败都是我们的经验，”Mogulla 说。他补充说，当一个组织拥有如此多的团队和微服务时，“要进行适当的协调并改进每个事件”并不容易。

## 事件管理关乎稳定性

停机是不可避免的。重要的是你如何应对。

阿迪达斯的事件管理分为两个团队：

- 网站可靠性工程专注于开发和运营。
- 服务管理专注于流程创建和审计。

但奥托说，你不会从事件管理开始。相反，你从为你的组织定义稳定性开始。她说，只有这样，你才能衡量它。

阿迪达斯将稳定性衡量为三个指标：

- 平均检测时间 (MTTD)。
- 平均恢复时间 (MTTR)。
- 收入影响。

后者为电子商务平台的业务利益相关者创造了一种共同语言。

“如果我们说我们有一个共同的 KPI，那么我们就不会陷入这种争论：我应该优先考虑价值吗？我应该优先考虑稳定性吗？不。我们有一个我们都理解的指标，”奥托说。对于阿迪达斯，坦率地说，对于大多数企业来说，“这都是关于金钱的”。

根据这三个优先级指标，某些事件被认定为重大事件。然后任命一名事件经理来协调所有相关团队之间的所有沟通，包括 SRE、开发人员和营销人员。

第二天包括事件简报或根本原因分析 (RCA)。阿迪达斯遵循技术模板，其中会提出以下问题：

- 我们在技术上错过了什么？
- 可观察性是否缺失？
- 是否缺少测试？
- 从流程上来说，发生了什么？

奥托强调，这是一个有意[无责的验尸](https://thenewstack.io/top-12-best-practices-for-better-incident-management-postmortems/)，领导层尤其鼓励这样做，因为“进行事件简报的全部意义在于真正了解发生了什么并创建行动项目”。

阿迪达斯通过服务管理团队运行的问题管理来结束事件，以便优先考虑下一步行动——寻求不断收紧事件管理反馈循环。

虽然阿迪达斯在一年前就切换到了微服务架构，但 SRE 两人组最后说，可观察性和平台工程是一个持续的旅程，而不是目的地。

“那是我们的旅程，从单体架构迁移到微服务。另一个正在使用[GenAI](https://thenewstack.io/ai/)出现，”奥托总结道。“最终会弹出其他东西——这是一个持续学习的过程。”
