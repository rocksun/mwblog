[OpenTelemetry](https://opentelemetry.io) (OTel) 生态系统不仅为我们提供了生成、处理和导出遥测数据的标准数据格式及传输机制，还承诺了厂商中立。但这究竟意味着什么？

这无疑是许多人在我们之前就思考过的问题，无论是在会议的走廊交流中，还是在 LinkedIn 上。而正是 Josh 的一篇 [LinkedIn 帖子](https://www.linkedin.com/posts/joshuamlee_opentelemetry-otel-activity-7303855232763998208-ccf7) 促使我们开始探索这个话题。

“我经常听到人们说：‘OpenTelemetry 是厂商中立的，所以你随时可以更换厂商。’……这就像在说，因为 vCard 格式存在，所以从 iOS 切换到 Android 非常容易一样。”

![Josh Lee 探讨厂商中立性的 LinkedIn 帖子。](https://cdn.thenewstack.io/media/2026/05/c6911c89-0.png)

这当然引起了 Adriana 的思考，并促成了[这篇博文](https://medium.com/womenintechnology/the-truth-about-opentelemetry-vendor-neutrality-d385957e2c2d)，该文对 Josh 最初的思考进行了扩展。

然而，我们意识到，在这个主题上我们还有更多内容需要探讨，具体包括：

* OpenTelemetry 社区在分布式追踪领域的根基如何引导其走向厂商中立的方向。
* 理解 OpenTelemetry 标准的设计是如何实现厂商中立的。
* 理解 OpenTelemetry 生态系统的厂商中立性在哪里止步。
* 展望未来：我们能否让 OpenTelemetry 生态系统实现完全的厂商中立，以及我们应该这样做吗？

系好安全带，孩子们！让我们开始探索吧！

了解“为什么”会很有帮助——为什么要使用 OpenTelemetry 标准？为什么要使用分布式追踪？为什么要关心厂商中立性？

让我们从开放性开始。**可观测性（和监控）迫切需要开放**。具体来说，当我们承担起监控组织所使用的所有不同系统的任务时，能够作为翻译层的开放协议就会变得无比宝贵。

> “可观测性（和监控）迫切需要开放。”

但 OpenTelemetry 生态系统还比较新，而且其他实现通用监控格式的尝试都失败了。那么，为什么 OpenTelemetry 生态系统能获得如此广泛的采用呢？

**分布式追踪是理解 OpenTelemetry 生态系统作为统一力量取得成功的关键**。在微服务出现之前，监控意味着日志和指标；这些信号拥有被广泛采用且相对开放的标准：例如用于指标的 [Prometheus](https://prometheus.io/docs/instrumenting/exposition_formats/#exposition-formats) 或 [SNMP](https://splunk.github.io/splunk-connect-for-snmp/v1.9.2/configuration/snmp-data-format/)，以及用于日志的 [syslog](https://en.wikipedia.org/wiki/Syslog) 或 ELK 栈的 JSON 格式。

在这种情况下，开放协议非常直接：如果每个被监控的实体都能以某种兼容的格式发送指标和日志，它们就可以被任意数量的工具集中接收和存储。

正如可观测性厂商不厌其烦地写道的那样，**微服务需要分布式追踪**。以前可以从单个堆栈追踪或日志中收集的信息，现在分散在数十个或数百个不同的进程中。

分布式追踪不仅仅是范围上的变化，它也是上下文的彻底转变。为了发出正确的追踪跨度（span），每个进程都需要理解调用它的进程的一小部分上下文，并将该上下文传递给下游服务。单个进程插桩（instrumentation）的边界已大大扩展。

这带来了巨大的好处。读取单个分布式追踪比根据标签拼接零散的日志要*简单得多*。但它的代价是跨越单个技术边界的复杂性增加。突然之间，[Java](https://thenewstack.io/in-the-ai-age-java-is-more-relevant-than-ever/) 开发人员必须更加关心 Python 开发人员的插桩，反之亦然。

解决这种增加的复杂性的第一个方案来自拥有专有代理（agent）和协议的厂商。每个厂商都为尽可能多的编程语言、框架和运行时创建了插桩 SDK——这造成了重复工作。在 OpenTelemetry 标准出现之前，每个厂商都在创建自己的插桩框架上投入了大量的时间、人力和资金。这也对客户造成了锁定效应，因为他们必须在发布的*每一个软件制品*中嵌入专有的 SDK。

有一个著名的[关于标准的 xkcd 漫画](https://xkcd.com/927/)，讽刺了我们如何试图通过创建一个新标准来解决竞争标准过多的问题。虽然在许多情况下确实如此，但 OpenTelemetry 标准实现了格式的精简。厂商们不再相互竞争，而是在一个共同的标准上开展合作。很快，厂商之间的区别就变成了他们能用摄取的数据做些什么，从而为客户提供价值。我们相信，之所以能做到这一点，是因为在这个领域工作的每个人都赞同一些基本事实：

* 微服务需要比传统监控更多的东西。
* 标准化是[监控与可观测性](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "监控与可观测性")的核心挑战之一。
* 开放格式使跨技术和组织边界的标准化合作成为可能。

换句话说：***可观测性迫切需要开放。***

## 是什么让 OpenTelemetry 工具具备厂商中立性？

既然我们已经确立了对 OpenTelemetry 生态系统所提供厂商中立性的需求，我们不禁要问：生态系统的厂商中立到底意味着什么？这意味着***如果你选择将可观测性数据发送给不同的厂商，你不需要更新你的插桩代码***。这非常重要，因为在过去，更换厂商意味着你必须经历更新插桩的痛苦过程，这意味着往往继续使用现有厂商比经历重新对代码进行插桩以适应新厂商的痛苦更容易。

得益于 OpenTelemetry 标准的厂商中立性，你只需更新发送遥测数据的目的地。事实上，如果你正在评估多个厂商，你甚至可以同时将相同的数据发送给不同的厂商（即“厂商对决/评估”），以帮助你确定哪家厂商最适合你组织的需求。

> “得益于 OpenTelemetry 标准的厂商中立性，你只需更新发送遥测数据的目的地。”

这一切都得益于 OpenTelemetry 生态系统的以下组件：

* API 和 SDK
* OTLP
* Collector

让我们深入探讨它们中的每一个是如何提供额外的灵活性和兼容性的。

### OpenTelemetry API 和 SDK

OpenTelemetry 规范提供了遥测数据的标准定义，并描述了如何对代码进行插桩。OpenTelemetry API 和 SDK（稍后会详细介绍）在规范中进行了定义。这确保了无论用户使用何种语言，都能获得相似的体验。

**OpenTelemetry 应用程序编程接口 (API)** 定义了对应用程序进行插桩的方法，并作为插桩的入口。OpenTelemetry 支持的每种语言都有自己的 API 实现。

**OpenTelemetry 软件开发工具包 (SDK)** 实现了 API，并决定了遥测数据的生成和关联方式。OpenTelemetry 支持的每种语言都有自己的 SDK 实现。

API 故意与 SDK（即生成遥测数据的代码）分离。这允许你插入任何你选择的 OpenTelemetry SDK，无论是官方的 OpenTelemetry SDK、厂商的 SDK 还是你自己的 SDK。（是的！你可以编写自己的 OpenTelemetry SDK！🤯）只要它们实现了 OpenTelemetry API，你选择哪一个并不重要。

这意味着库（以及你自己的代码）可以对所使用的 SDK 保持无感。这反过来又使库厂商能够提供开箱即用（OOB）的插桩，从而提供了自动插桩的所有好处，而没有其复杂性或额外开销。（当然，如果库没有提供 OOB 插桩，自动插桩也是值得一试的！）

还没准备好使用某个 SDK？没问题！因为 OpenTelemetry API 还包含一个极简的 SDK。这允许你对应用程序进行插桩，该程序仍能正常运行；但是，请记住，在插入合适的 SDK 之前，遥测数据不会发送到你的后端。

![OpenTelemetry 处于服务与后端之间的示意图。](https://cdn.thenewstack.io/media/2026/05/0d52fb5f-1-1024x284.png)

### OTLP

OpenTelemetry 协议（OTLP）是一种与厂商和工具无关的规范，用于编码、传输和交付 OpenTelemetry 数据。SDK 发出的遥测数据使用 OTLP，现在大多数可观测性后端都支持 OTLP，并强烈建议接收它。对于那些不支持的后端，可以使用将 OTLP 数据转换为特定工具格式的导出器（exporter）。OTLP 同时支持 HTTP 和 gRPC。

**OTLP 堪称某种魔法秘方。** 兼容 OTLP 的工具迎来爆发式增长，得益于共享的协议、格式和语义约定，它们都可以互操作。

### Collector

**OpenTelemetry Collector** 是一个厂商中立的二进制程序，用于接收、转换和向一个或多个可观测性解决方案导出数据。

Collector 可以被视为你将在环境中部署的与具体厂商无关的代理。

Collector 的优势：

* **解耦遥测源与其目的地。** Collector 充当某种代理。遥测数据直接发送到单一目的地——Collector，然后由其转发到一个或多个后端。
* **充当多种数据类型的单一代理。** Collector 可以从多种数据源（包括应用程序和基础设施）接收多种数据格式。
* **将遥测[数据分发到多个后端系统](https://thenewstack.io/data-intensive-applications-rewrite-2026/)**，实际上允许你进行厂商对决（或让团队结合使用多种工具）。

![OpenTelemetry Collector 与接收器、处理器和导出器交互的示意图](https://cdn.thenewstack.io/media/2026/05/77ecf221-2.png)

#### 互操作性之美

说到多播——这是 OpenTelemetry 规范最奇妙的用途之一，而且不仅限于厂商评估阶段。OpenTelemetry 生态系统的开放格式意味着可互操作的工具可以*始终*结合使用。

让我们考虑几个使用场景。

因为 Collector 允许你同时将遥测数据发送到一个或多个后端，你可以选择将每个信号发送到不同的目的地。

![显示 Collector 可以同时将遥测数据发送到多个后端的示意图。](https://cdn.thenewstack.io/media/2026/05/34a43f47-3-1024x284.png)

也许你有一个支持所有 OpenTelemetry 信号的一体化后端。在这种情况下，你可以将所有信号发送到这单个后端。

如果你在多个后端之间犹豫不决，不知道该选哪一个，你可以同时将遥测数据发送到两个一体化后端，并以对决的方式对它们进行比较。

![显示 OpenTelemetry Collector 向两个厂商发送信号的示意图。](https://cdn.thenewstack.io/media/2026/05/dbdfac62-4-1024x284.png)

出于合规性原因，许多组织需要长期的数据存储。在这种情况下，你不仅可以选择将遥测数据发送到你喜爱的后端，还可以将其发送到本地（on-premises）工具进行长期存储。

或者，假设有一家你非常喜欢的可观测性厂商，他们满足了你 95% 的需求。但他们仍然缺少一个关键工具（例如，并非所有的商业解决方案都支持 Profiling 持续分析）。OpenTelemetry 生态系统可以帮助你用其他兼容的开源或厂商工具来填补这些空白。

![显示 OpenTelemetry Collector 将信号发送到厂商后端，并将日志发送到本地长期存储的示意图。](https://cdn.thenewstack.io/media/2026/05/5de53413-5-1024x284.png)

## 使用场景 4：针对特定团队的特定流水线

假设你的公司在生产环境中使用后端 A。开发团队可能也希望使用 OpenTelemetry 信号来排查他们自己代码的问题。因此，这些团队可能会使用本地开源可观测性工具，例如 [otel-tui](https://github.com/ymtdzzz/otel-tui)、[OTel Front](https://github.com/mesaglio/otel-front) [或 OTel Viewer](https://github.com/CtrlSpice/otel-desktop-viewer) 来辅助排查故障。

或者考虑另一种场景。假设你在 A 公司工作。它与 B 公司合并。A 公司使用后端 X，而 B 公司使用后端 Y。在两个组织完全整合之前，你可能会发现合并后的组织会同时使用两个不同的后端。

![两家合并后的公司同时使用不同后端的示意图。](https://cdn.thenewstack.io/media/2026/05/0c88fac5-6-1024x284.png)

使用 OpenTelemetry 标准意味着你可以得到你想要的一切。你既可以吃掉蛋糕，也可以保留它……（只要你愿意为储存两份蛋糕买单。）

## 厂商迁移：了解你将面临什么

现在，OpenTelemetry 生态系统中那些非厂商中立的部分呢？真的存在这种东西吗？

***在数据接收方面，OpenTelemetry 协议绝对是厂商中立的。***

典型的例子：当 Adriana 从 Lightstep 跳槽到 Dynatrace 时，她能够保留其在各种演讲和课程中使用的演示代码上的现有插桩，而她所要做的就是将她的 OpenTelemetry Collector 重新指向不同的后端。轰。奇迹发生了。✨ 她能够在 Dynatrace UI 中看到她的追踪、日志和指标，就像以前在 Lightstep UI 中一样。

> “然而，没有人谈论的是，这不仅仅关乎数据接收，不是吗？”

然而，没有人谈论的是，这不*仅仅*关乎数据接收，不是吗？我们还必须考虑以下因素：

* 外观和体验（Look & feel）
* 存储与历史数据
* 查询与仪表盘
* 告警与 SLO
* 基础设施即代码 (IaC)

### 外观和体验

如果你使用厂商 X 已经有一段时间了，你已经习惯了以特定的方式做事。也就是说，形成了一套特定的工作流。无论是你个人的工作流，还是你的 SRE 团队遵循的工作流。底线是：使用新厂商意味着要习惯新的 UI 以及该厂商特定的细节。也许厂商 X 拥有厂商 Y 所没有的功能，这些功能可以让你对 OpenTelemetry 数据进行一些很酷的操作——这意味着你必须熟悉这些新功能才能充分利用它们。

### 存储与历史数据

可观测性的商业模式是数据驱动的。——几乎每个厂商都根据*接收*和*保留数据*的某种组合来收费。据我们所知，没有厂商允许导出历史遥测数据，这意味着如果你更换厂商，你将失去历史数据，除非你同时将遥测数据发送到内部管理的数据库\*。

（\*）*但得益于 OpenTelemetry 协议，你现在可以做到这一点——太酷了*

### 查询与仪表盘

大多数厂商都有自己的仪表盘和查询语言——例如，Prometheus 的 PromQL、Dynatrace 的 DQL、Splunk 的 SPL，仅举几例。这意味着当你更换厂商时，你不能简单地“平移”你的仪表盘。你必须学习新的仪表盘界面、新的查询语言，然后将旧厂商的仪表盘翻译到新厂商的仪表盘中。底线是：它们需要时间和精力来构建。

和所有事情一样，规则也有例外：

### 告警与 SLO

一些可观测性厂商提供了基于服务水平目标（SLO）进行告警的能力，这些目标本身是由 OpenTelemetry 指标驱动的。如果你选择更换厂商，你必须重新创建你的告警和 SLO。当然，前提是该厂商支持告警和 SLO。

## IaC

许多[主流可观测性厂商都有自己的 Terraform 提供商 (provider)](https://registry.terraform.io/search/providers?q=logging%20%26%20monitoring)，这对于跨可观测性厂商工具的不同方面自动化配置非常有用。不幸的是，更换可观测性厂商意味着也要更换 Terraform 提供商。此外，并非所有可观测性厂商的 Terraform 提供商都允许你配置相同的内容，这意味着，这同样不是一个“平移”的情况。

**需要指出的是，得益于智能体 AI（agentic AI），诸如创建查询和仪表盘以及编写 IaC代码之类的某些任务，在从一个厂商迁移到另一个厂商时，迁移工作量大大减少。**

## 厂商中立的未来愿景

每个可观测性平台都有其闪光点；如果它们千篇一律，就没有必要更换了。但它们也有一些共同的根本特征。我们需要一个地方来存放收集到的遥测数据（**存储**），一种探索这些数据的方法（**即时查询**），一种与我们的团队和未来的自己共享这些探索成果的方法（通常是**仪表盘**），以及一种在情况不妙时获得通知的方法（**告警**）。

![厂商中立的未来愿景示意图](https://cdn.thenewstack.io/media/2026/05/9e054d79-7-1024x284.png)

虽然 OpenTelemetry 项目本身不包含任何后端组件，本有几种开源选择，尤其是在存储、查询和可视化方面。

但正如我们已经探讨过的，互操作性不仅仅关乎更换厂商。如果我们会最喜欢的厂商让其数据存储可以通过普遍可用的 API 进行访问，从而允许我们将可观测性数据的一个副本存储为单一真理源，同时使其*可以被多个分析工具同时访问*，会怎么样？这将允许我们添加专门的分析工具、内部模型训练、定制报告等，所有这些都通过单个 API 实现——我们认为这会非常棒。

![OpenTelemetry Collector 将信号发送到厂商平台，并使其可同时被多个分析工具访问的示意图。](https://cdn.thenewstack.io/media/2026/05/08274e15-8-1024x284.png)

## 我们能实现厂商中立的承诺吗？

OpenTelemetry 社区自成立以来已经取得了长足的进步。它作为分布式追踪挑战的厂商中立解决方案出现，现已成长为生成、采集和导出可观测性数据的*事实上的*标准。

我们将 OpenTelemetry 项目的强大归功于几个关键因素：

* **可观测性是开放的这一事实。** 最终用户对此提出了要求。
* **自成立以来就支持多个厂商。** 没有哪家厂商独占鳌头。
* **CNCF 的管理和治理。** 该项目确实让人感觉像一个社区，个人和组织共同努力，实现标准遥测框架的共同目标。

而且它还在继续发展。就在几年前，OpenTelemetry 工具主要用于插桩层，厂商提供专有的导出器与他们的代理进行通信。现在，OTLP 已获得广泛支持，运行 OpenTelemetry Collector 来替代厂商代理或与其并存已非常普遍。

开源生态系统也拥抱了 OpenTelemetry 社区。Jaeger 最初是围绕其自己的（开放）追踪协议构建的。[它现在](https://opentelemetry.io/blog/2022/jaeger-native-otlp/)原生支持 OpenTelemetry 协议。广受欢迎的工具 Prometheus [现在正与 OpenTelemetry 共同演进](https://prometheus.io/docs/guides/opentelemetry/)，从而在任何地方都能享受到共享标准的好处。

我们会继续看到更多这样的变化吗？只有时间才能给出答案，但未来看起来是光明的。

在此之前，请记住：OpenTelemetry 生态系统最美妙的地方在于选择。厂商中立和[开放标准带来的作用](https://thenewstack.io/how-open-standards-enable-zero-trust-on-commodity-hardware/)远不止有一天“更换厂商”那么简单——尽管它们当然也对此有所帮助。开放格式的好处是可移植的数据和互操作的工具，允许你构建*今天*所需的可观测性解决方案。

关键在于——某个解决方案是否能让你提出有意义的问题，获得有用的答案，并根据你学到的知识采取行动？因为归根结底，如果你的应用程序和系统更加可靠，那才是最重要的。

YOUTUBE.COM/THENEWSTACK

技术瞬息万变，不容错过任何一期。订阅我们的 YouTube 频道，流式传输我们所有的播客、采访、演示等。

[订阅](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/05/261847bb-cropped-ed369392-64d6-400o400o2-94yyamxsepfa2wpkmp51hk.jpg)

Adriana Villela 是 ServiceNow Cloud Observability（前身为 Lightstep）的资深开发者倡导者（Sr. Developer Advocate）。她通过可观测性、SRE 和 DevOps 实践帮助公司实现卓越的可靠性。此前，她曾在 Tucows 管理平台工程团队和可观测性实践团队。Adriana...

阅读更多来自 Adriana Villela 的文章](https://thenewstack.io/author/adriana-villela/)

[![](https://cdn.thenewstack.io/media/2026/05/8602095d-joshlee_headshot.jpg)

Josh 是 Altinity 的开发者倡导者，他将自己的可观测性和工程背景应用于 ClickHouse 使用场景。他在跨多个行业的客户软件项目开发和领导方面拥有超过 15 年的经验。Josh 也是一位...](https://thenewstack.io/author/josh-lee/)