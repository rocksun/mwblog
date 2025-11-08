
<!--
title: OpenTelemetry专家：攻克移动端遥测难题
cover: https://cdn.thenewstack.io/media/2025/11/d293a3ee-mobile.jpg
summary: 前端可观测性变化，OpenTelemetry增强对Web/移动支持。移动遥测挑战：数据规模、性能、平台限制、复杂生命周期。开发面临可观测性知识和指导缺乏。OTel Android/Swift SIG改进SDK，解决包大小，定义语义，推动Kotlin API。
-->

前端可观测性变化，OpenTelemetry增强对Web/移动支持。移动遥测挑战：数据规模、性能、平台限制、复杂生命周期。开发面临可观测性知识和指导缺乏。OTel Android/Swift SIG改进SDK，解决包大小，定义语义，推动Kotlin API。

> 译自：[OpenTelemetry Experts on Tough Telemetry Challenges in Mobile](https://thenewstack.io/opentelemetry-experts-on-tough-telemetry-challenges-in-mobile/)
> 
> 作者：Colin Contreary

前端可观测性的季节正在发生变化，我们看到社区积极参与改进 [OpenTelemetry 对网络应用和移动应用的支持](https://thenewstack.io/what-new-data-tells-us-about-opentelemetry-adoption-for-mobile/)。例如，OpenTelemetry 项目中成立了一个新的浏览器兴趣小组 (SIG)，他们正在努力改进 OTel 对 [浏览器运行时](https://thenewstack.io/how-to-make-opentelemetry-better-in-the-browser/) 的支持。您可以在这个 [按需小组讨论](https://get.embrace.io/web-otel-panel-typ?utm_source=the-new-stack&utm_medium=paid&utm_campaign=fall-otel-panel) 中了解更多关于他们将要开展的工作。

OTel 社区还设有专门的 Android 和 Swift 兴趣小组，用于改进在两个 [原生移动应用平台](https://thenewstack.io/how-to-instrument-a-react-native-app-to-send-otel-signals/) 上收集遥测数据的 API、插桩库和语义约定。各组织也注意到了这一点，企业管理协会 (EMA) 最近进行的一项调查显示，未来 12 到 24 个月内，[移动数据收集领域 OpenTelemetry 的采用率](https://thenewstack.io/what-new-data-tells-us-about-opentelemetry-adoption-for-mobile/) 将增加两倍。

我与 Android 和 Swift 兴趣小组的几位主要成员进行了一场 [轻松的秋季主题小组讨论](https://get.embrace.io/fall-otel-panel-typ?utm_source=the-new-stack&utm_medium=paid&utm_campaign=fall-otel-panel)，探讨了移动遥测数据收集中的主要挑战以及 OpenTelemetry 对移动设备支持的现状。小组成员包括：

* [Ari Demarco](https://www.linkedin.com/in/ariel-demarco-a4b34aa0/)，[Embrace](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=fall-otel-panel) 的 iOS 软件工程师，OTel Swift 维护者。
* [Bryce Buchanan](https://www.linkedin.com/in/brycebuchanan/)，[Elastic](https://www.elastic.co/) 的首席工程师，OTel Swift 维护者。
* [Hanson Ho](https://www.linkedin.com/in/hanson-ho/)，Embrace 的 Android 架构师，OTel 贡献者和 OTel Android 批准者。
* [Jason Plumb](https://www.linkedin.com/in/jasonplumb/)，[Splunk](https://www.splunk.com/) 的高级首席软件工程师，OTel Android 维护者和 OTel Java 批准者。
* [Nacho Bonafonte](https://www.linkedin.com/in/nachob/)，高级软件工程师，OTel Swift 维护者。

## 移动平台遥测数据收集面临的挑战

当移动开发者使用 OpenTelemetry 时，他们必须注意 [移动应用可以生成的数据规模](https://thenewstack.io/how-time-plays-a-crucial-role-in-aggregating-mobile-data/)。Buchanan 提到，虽然后端系统在严格控制的条件下运行在数千个客户端上，但移动应用可以运行在数百万个客户端上。

Demarco 插话道：“这也导致了数据量的问题，因为根据应用的不同，一个移动应用可以生成大量的遥测数据。因此，与后端可以集中控制采样不同，在移动设备上，采样决策可能应该在设备上做出，对整体情况的可见性有限。然后问题就来了，如果你过度采样，会浪费大量带宽或电量。[…] 但如果你采样不足，你可能会错过识别问题或理解行为所需的关键遥测数据。”

移动开发者还高度关注其应用的性能，而应用的性能可能会受到捕获遥测数据的运营成本的影响。Plumb 提到了开发者必须记住的几件事，包括应用必须向平台进行的 API 调用、应用在这些回调或事件处理程序中花费的时间，以及网络请求在传输中的负载大小。

“高效处理这些负载也是我认为人们在移动平台上特别面临的挑战，这在其他平台中不存在，我们没有奢侈地仅仅……横向 [扩展]，比如，再启动几个实例，” Plumb 说。

移动应用运行的平台也受到 Google 和 Apple 的严格控制。正如 Bonafonte 所说，“平台给你带来的隐私是件困难的事情。” 移动开发者需要操作系统的支持才能收集数据，因此如果系统不允许他们收集某些类型的遥测数据，他们在有效观测其应用方面就会受到限制。

与服务器不同，移动应用具有生命周期复杂性，这使得理解导致问题的条件变得异常困难。

正如 Demarco 指出的：“移动应用不是持续运行的，它们会被暂停、置于后台、终止、被操作系统杀死，可能会发生崩溃……操作系统可以预热你的应用，应用可能因为推送通知、后台获取或用户点击图标而启动。那么，你什么时候刷新你的遥测数据？……你如何跟踪应用重启后的会话连续性？当发生崩溃或操作系统杀死你的进程时，[飞行中的 Span 会怎样](https://www.cncf.io/blog/2024/06/14/why-embrace-created-span-snapshots-for-mobile-observability-with-opentelemetry/)？因此，在这些情况下你决定做什么存在一系列复杂性。这并非易事……仅仅解决其中一个问题并非你可以在代码中一行解决的事情。这是你需要真正仔细思考才能解决的问题。”

## 移动开发者在可观测性实践中面临的挑战

传统上，可观测性被视为后端团队的职权范围，因此，移动开发者常常不理解它。Ho 提到，移动开发者通常是因为被告知才与 OpenTelemetry 交互，而不是他们主动寻求的东西。

“追踪和……遥测不是移动开发者的核心能力……因为，你知道，他们面临的挑战不同。……有很多东西需要实际教给一个团队，而且架构，移动应用架构也并非为可维护的插桩而设计得非常好，” Ho 说。

产品经理可能希望获得更好的可见性来解释新功能的性能（或缺乏性能），因此他们要求移动开发者收集更多的可观测性数据。但无论是移动开发者还是产品经理都不知道要收集什么。在移动应用的可观测性插桩方面缺乏清晰度是我们讨论中的一个共同点。

Buchanan 提到，即使是像何时启动 [Span](https://thenewstack.io/spans-what-are-they-and-why-should-mobile-engineers-care/) 这样简单的事情，在移动设备上也不是微不足道的。“在后端，这非常简单。就像，‘哦，当我收到一个请求时，Span 就开始了。’ 但对于移动开发者来说，……我应该在有人点击按钮时启动吗？在网络开始时启动吗？……对此没有正确答案，比如，你该如何进行插桩？这真的取决于你的应用做什么以及你想要监控什么。”

Plumb 同意 OpenTelemetry 在围绕这些客户端用例方面没有为开发者提供很好的指导。

“我们还没有一个真正好的数据模型，或者仅仅是对会话是什么的概念性描述。”

他将这一挑战与后端可观测性工具进行了对比，后者在这一点上已经有几个定义非常明确的用例。例如，每个拥有追踪解决方案的供应商都会有追踪瀑布视图，每个 [真实用户监控 (RUM)](https://thenewstack.io/when-to-use-synthetic-monitoring-vs-real-user-monitoring/) 供应商都会有分析漏斗的方法。

正如 Ho 指出的：“当你是一个后端服务时，目标是接收请求并发出响应。你想要记录这花费了多长时间，以及中间是否有任何有趣的事情发生。目标很简单。移动应用的目标则有待定义。”

Uber Eats 团队关心的事情与 Pinterest 团队不同，也与银行应用不同。

“理解目标并将其转化为需要哪种遥测数据并非一个微不足道的飞跃。如果你没做过，这看起来很简单，但当你实际去做的时候，你会觉得，‘我关心一切。’ 你真的关心一切吗？” Ho 说。

## 改进 OpenTelemetry 对 Android 和 Swift 的支持

Android 和 Swift 兴趣小组正在改进使用 OpenTelemetry 的开发者体验。除了手动捕获日志和追踪的关键 OpenTelemetry 信号之外，这两个 SDK 还可以捕获移动设备特有的遥测数据：

* Android SDK 包含针对 [应用程序无响应 (ANR) 错误](https://embrace.io/blog/how-does-an-anr-work/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=fall-otel-panel)、崩溃报告、视图追踪和网络调用的插桩。
* Swift SDK 包含对使用 URLSession 进行的网络调用以及由应用生命周期变化触发的会话事件的插桩。

Swift 兴趣小组还解决了一个关键挑战，该挑战源于在 Apple 严格控制的移动平台中工作。Apple 的官方包管理器 Swift Package Manager 要求下载项目中所有库的所有依赖项，即使你在应用中不使用它们。因此，OpenTelemetry Swift 仓库非常庞大，这意味着移动开发者在 iOS 应用中使用 OTel 时面临着巨大的包下载大小。

正如 Bonafonte 分享的：“[OpenTelemetry Swift] 必须使用 protobuf 支持 protobuf OTLP [OpenTelemetry 行协议] 协议，这意味着你依赖于 Apple 的一个库，该库又依赖于 Apple 的另一个库，它又依赖于另一个又一个又一个的库。”

Ari 插话道：“每当你必须下载它，或编译你的应用，运行测试，在 CI 中运行，构建应用并部署它，所有这些都需要花费大量时间，而且显然，例如，在 CI 方面，时间就是金钱，所以……对于每一个 iOS 开发者来说，这将是一个痛苦。而且可能，也许他们只是想使用 API 或者我们 OpenTelemetry SDK 的实现。”

作为解决方案，Swift 兴趣小组将代码分为两个独立的仓库。官方的 OpenTelemetry Swift 仓库是主仓库，它包含使用 OTLP 所需的一切。维护者创建了另一个名为 OpenTelemetry Swift Core 的仓库，该仓库仅包含 OpenTelemetry Swift API 和 OpenTelemetry Swift SDK。这两个部分是入门、创建追踪和发出日志的最低要求。iOS 开发者现在可以插桩应用、处理数据并导出，而无需主仓库的所有开销。

Android 兴趣小组正在进行三项主要改进。第一项是更好地稳定 Android 代理的初始化 API，预计很快完成。第二项是拓宽插桩范围，其中包括增强对构建时自动插桩的支持。

正如 Plumb 所说：“第三类，我认为可能同样重要的，是语义约定。……随着每一次插桩，随着我们添加的每一种新功能，我们都试图在语义约定中反映出来，即使第一版处于开发或实验阶段，至少将其公之于众并记录下来，它意味着什么，当你看到一块标有此名称的数据时，这些附加属性意味着什么，其意图是什么。”

挑战在于在观测移动应用时要包容所有不同的意见。Ho 举了一个定义移动会话复杂性的例子，即前台与后台应用行为的问题。对于主要在后台运行的播客应用，会话应该何时开始？对于主要在前台运行，但具有后台 [活动触发内容刷新和用户界面 (UI) 更新](https://thenewstack.io/how-to-make-sense-of-ios-user-activity-with-opentelemetry/) 以便在下次应用启动时准备就绪的应用会发生什么？对于一次运行数小时且持续在前台运行的销售点 (POS) 应用，会话应该是什么？

Ho 随后分享了 Android 兴趣小组在 Embrace 的 [Kotlin API 捐赠提案](https://opentelemetry.io/blog/2025/kotlin-multiplatform-opentelemetry/) 给 OpenTelemetry 方面的发展。Kotlin 是 Android 开发的官方语言；然而，OpenTelemetry Android SDK 目前在底层利用 OpenTelemetry Java SDK 来记录遥测数据。采用 Kotlin API 和 SDK 将使移动开发者更容易使用 OpenTelemetry，因为 Kotlin 编程语言在现代移动应用开发中更熟悉、更符合惯例且更易用。