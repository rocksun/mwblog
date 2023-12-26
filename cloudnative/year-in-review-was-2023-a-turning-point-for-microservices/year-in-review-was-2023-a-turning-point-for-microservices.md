
<!--
title: 年终总结：微服务的转折之年
cover: https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1-1024x576.png
-->

长期以来，微服务一直被认为是云原生服务应用架构的事实标准，如今，亚马逊和谷歌等云巨头开始对其进行重构。

> 译自 [Year-in-Review: 2023 Was a Turning Point for Microservices](https://thenewstack.io/year-in-review-was-2023-a-turning-point-for-microservices/)，作者 Joab Jackson 是 The New Stack 的高级编辑，负责报道云原生计算和系统运维。他在IT基础设施和开发方面的报道已经超过25年，包括在IDG和Government Computer News的任职经历。在那之前，他...

或许我们对微服务的理解存在一些问题？

这正是“[走向云应用的现代开发](https://dl.acm.org/doi/10.1145/3593856.3595909)”（[PDF](https://mwhittaker.github.io/publications/service_weaver_HotOS2023.pdf)）一文的主旨，该文是一群谷歌工程师（由谷歌软件工程师Michael Whittaker领导）在[HOTOS '23](https://dl.acm.org/conference/hotos)（第19届操作系统热点问题研讨会）于六月展示的成果。

正如Whittaker等人指出的问题，[微服务](https://thenewstack.io/microservices/what-is-microservices-architecture/)在架构上大部分并未得到正确设置。它们混淆了逻辑边界（代码编写方式）和物理边界（代码部署方式）。问题便由此而来。

相反，谷歌工程师们提出了另一种方法。将[应用](https://thenewstack.io/open-application-model-build-the-next-generation-of-cloud-native-applications/)构建为逻辑单体，然后交由自动化运行时处理，该运行时根据应用的需求和可用资源决定在何处运行工作负载。

通过这种延迟方式，他们能够将系统的延迟降低15倍，成本降低最多9倍。

“如果人们能够从有序的模块化代码开始，我们可以将部署架构视为实现细节，” Kelsey Hightower在十月[评论](https://x.com/kelseyhightower/status/1720891958036668615?s=20)此项工作时说道。

## 微服务究竟出了什么问题？

几个月前，亚马逊Prime Video的工程团队发表了一篇[博文](https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90)，解释了至少在视频监控方面，单体架构的性能要优于[微服务和无服务器](https://thenewstack.io/monoliths-to-microservices-8-technical-debt-metrics-to-know/)的方法。

事实上，亚马逊通过放弃微服务架构，节省了90%的运营成本。

一代工程师和架构师在[微服务的优越性](https://thenewstack.io/return-of-the-monolith-amazon-dumps-microservices-for-video-monitoring/)上成长起来，这个断言确实令人震惊。

“这篇文章对亚马逊作为一家公司来说真是一种彻头彻尾的尴尬。完全无法建立内部协调或协同沟通，” 最近创办了自己的行业分析公司 [Platify](https://platifyinsights.com/) 的分析师 [Donnie Berkholz](https://twitter.com/dberkholz) [写道](https://www.linkedin.com/feed/update/urn:li:activity:7059761112958799872/)。

“这个故事的独特之处在于亚马逊曾是面向服务的架构的代表，” Ruby-on-Rails 的创作者兼 Basecamp 的联合创始人 [David Heinemeier Hansson](https://world.hey.com/dhh/even-amazon-can-t-make-sense-of-serverless-or-microservices-59625580) 表示意见，“现在所有这些理论的实际结果终于出炉了，显而易见的是，在实践中，微服务或许是最容易使系统不必要复杂化的最大警世之歌。而无服务器仅会让情况变得更糟。”

## 亚马逊视频的微服务经验

![Zoom](https://cdn.thenewstack.io/media/2023/05/6bb7cd54-prime-01.webp)

*原始的亚马逊视频传递系统。*

亚马逊工程师的任务是监控 Prime 传递给客户的数千个视频流。最初，这项工作是由一组由 [AWS Step Functions](https://aws.amazon.com/?utm_content=inline-mention) 协调的分布式组件完成的，这是一项无服务器的编排服务，使用了 AWS Lambda 无服务器服务。

理论上，使用无服务器应该允许团队独立[扩展每个服务](https://thenewstack.io/scaling-environments-with-opentelemetry-and-service-mesh/)。然而，事实证明，至少对于团队实现组件的方式而言，他们在仅达到预期负载的5%时就遇到了硬性扩展限制。由于需要在多个组件之间传输数据，扩展以监控数千个视频流的成本也将变得不划算。

最初，团队尝试优化各个组件，但这并没有带来显著的改进。因此，团队将所有组件移至单一进程，托管在亚马逊弹性计算云（Amazon EC2）和亚马逊弹性容器服务（Amazon ECS）上。

“微服务和无服务器组件是在高规模下执行工作的工具，但是否选择它们而不是单体架构必须根据具体情况做出，” 亚马逊团队得出结论。

## 微服务的缺陷

可以说，“微服务”一词最早由 Peter Rodgers 在2005年提出，尽管他称之为“微网络服务”（micro web services）。他给了这个在当时的网络服务和服务导向架构（SOA）时代引起关注的观念一个名字。

“当时‘微网络服务’背后的主要推动力是将单一的大型‘单块’设计拆分为多个独立的组件/进程，从而使代码库更粒度化和可管理，” 软件工程师Amanda Bennett在[一篇博客文章](https://medium.com/microservicegeeks/an-introduction-to-microservices-a3a7e2297ee0)中解释道。

这个概念在随后的几十年里得到了广泛应用，尤其是在云原生计算的时代，直到近年才在某些领域开始受到批评。

![Zoom](https://cdn.thenewstack.io/media/2023/12/6764bd0b-microservices-vs-monoliths-kainz.png)

*软件工程师Alexander Kainz为 TNS 贡献了一篇关于单体架构和微服务的优秀比较。*

在他们的论文中，谷歌工程师列出了微服务方法的一些缺点，包括：

- **性能**：将数据序列化并通过网络发送到远程服务会影响性能，并且如果应用程序变得足够复杂，甚至可能导致瓶颈。
- **理解**：在分布式系统中，由于微服务之间有许多交互，臭虫通常难以追踪。
- **管理问题**：认为应用程序的不同[部分](https://thenewstack.io/part-3-the-best-way-to-select-a-proxy-architecture-for-microservices-application-delivery/)可以根据自己的时间表进行更新是一种优势。但这导致开发人员必须管理大量的二进制文件，每个文件都有自己的发布计划。并且希望在本地运行的服务上运行端到端测试时可能会面临困难。
- **API变得脆弱**：微服务互操作性的关键在于一旦建立了微服务，API就不能更改，以免破坏依赖于该API的其他微服务。因此，只能通过添加更多API来扩展API，导致膨胀。
- 一种新型的微服务？

## 一种新型的微服务

当 The New Stack 首次报道亚马逊的新闻时，许多人迅速指出视频团队使用的架构也不完全是单体架构。

![Zoom](https://cdn.thenewstack.io/media/2023/05/cb5d618e-prime-02.webp)

“这绝对不是一个从微服务到单体架构的故事，” 亚马逊云计算部门前副总裁、[现任 Nubank 顾问](https://building.nubank.com.br/interview-meet-adrian-cockcroft-nubanks-new-tech-advisor/)的 [Adrian Cockcroft](https://www.linkedin.com/in/adriancockcroft/) 在接受 The New Stack 的[采访](https://thenewstack.io/amazon-prime-videos-microservices-move-doesnt-lead-to-a-monolith-after-all/)时说道，“这是一个从 Step Functions 到微服务的故事。我认为问题之一是错误的标签。”

他指出，在许多应用程序中，特别是内部应用程序，开发成本超过了运行时成本。在这些情况下，Step Functions 在节省开发时间方面具有很大意义，但在处理大量工作负载时可能会带来成本。

“如果你知道最终会在某个规模上执行它，” Cockcroft 说，“你可能会一开始就以不同的方式构建它。所以问题是，你知道如何做这件事吗，你知道将以什么规模运行吗？” Cockcroft 表示。

谷歌的论文通过简化开发人员的工作，让运行时基础设施能够找出运行这些应用程序的最具成本效益的方式来解决这个问题。

“通过将所有执行责任委托给运行时，我们的解决方案能够提供与微服务相同的好处，但性能更高，成本更低，” 谷歌研究人员写道。

## 重新审视的一年

今年进行了许多基本的架构重新审视，而微服务并不是唯一被质疑的理想。

例如，云计算也受到了审查。

在六月，[37signals](https://37signals.com/)，既经营 Basecamp 又经营 [Hey 电子邮件应用程序](https://thenewstack.io/basecamps-hey-app-attempts-to-re-invent-email/)的公司，[购置了一批戴尔服务器](https://www.delltechnologies.com/en-us/index.htm?utm_content=inline-mention)，并离开了云，打破了几十年将运营迁移到离场地更模糊定义的更大效率的传统。

“这是云营销的核心欺骗，即一切都会变得如此容易，以至于你几乎不需要任何人来操作它，” David Heinemeier Hansson在[一篇博客](https://world.hey.com/dhh/the-big-cloud-exit-faq-20274010)文章中解释道。 “我从未见过。在 37signals，也没有其他运行大型互联网应用程序的任何人。云计算有一些优势，但通常并不在减少运营人员数量方面。”

当然，DHH 是[一名赛车手](https://twitter.com/dhhracing?lang=en)，所以自然而然地他想深入挖掘硬件层面。但也有其他人愿意支持这一赌注。今年晚些时候，Oxide Computers [推出](https://thenewstack.io/in-pursuit-of-a-superior-server-oxide-computer-ships-its-first-rack/)了他们的新系统，希望以类似的情绪[为他人提供服务](https://thenewstack.io/oxide-launches-the-worlds-first-commercial-cloud-computer/)：在自己的数据中心更具成本效益地运行云计算工作负载。

这种情绪似乎至少在云账单到期时更受考虑。[FinOps 在2023年变得显眼](https://thenewstack.io/how-to-get-your-organization-started-with-finops/)，越来越多的组织[转向像 KubeCost 这样的公司来控制他们的云开支](https://thenewstack.io/kubecost-cloud-manages-k8s-costs-for-finops-teams/)。还有多少人对一名 DataDog 客户因云监控而[收到了 6500 万美元的账单](https://thenewstack.io/datadogs-65m-bill-and-why-developers-should-care/)感到吃惊呢？

可以说，对于一个创收数十亿美元的公司来说，支付 6500 万美元的可观察性账单可能是值得的。但随着首席架构师更认真地审视过去十年的工程决策，他们可能决定做一些调整。而微服务将不例外。

TNS 云原生记者 Scott M. Fulton III 对本报告做出了贡献。
