# Adobe 如何使用 OpenTelemetry Collector

翻译自 [How Adobe Uses OpenTelemetry Collector](https://thenewstack.io/how-adobe-uses-opentelemetry-collector/) 。

作为开源可观测性工具的一部分，它充当 Adobe 大量跟踪和指标数据的中心枢纽，也是缓解开发人员摩擦的一种方式。

![](https://cdn.thenewstack.io/media/2023/06/dc81b917-opentelemetry-stacked-color-1-1024x599.jpg)

Adobe 的 Chris Featherstone 和 Shubhanshu Surana 在[北美开源峰会](https://events.linuxfoundation.org/open-source-summit-north-america/)的演讲中称赞 OpenTelemetry Collector 是可观测性的瑞士军刀。

他们继续解释如何使用它来跟踪公司收集的大量可观测性数据，包括指标，每天 3.3 亿个独特的 series ；每天 3.6 TB 的 span 数据；每天超过 1 PB 的日志数据。


![Adobe’s Chris Featherstone and Shubhanshu Surana](https://cdn.thenewstack.io/media/2023/06/a5f933a8-adobe5-300x290.jpg)
*Adobe 的 Chris Featherstone 和 Shubhanshu Surana*

软件开发高级经理 Featherstone 解释说，并非所有这些数据都流经他的团队或 OTel collector ，但“这是一个相当不错的部分”。
分布式跟踪将他的团队带到了 OpenTelemetry 。他解释说， Adobe 主要由收购组成，随着每家新公司的引入，人们对最好的云、这个工具、那个文本编辑器等都有自己的看法。

“特别是分布式跟踪，这成为一个巨大的挑战，”他说。“想象一下，试图在云供应商之间拼接一条线索，开源。所以最终，这就是我们找到这个 collector 的原因。但我们试图建立一个基于 Jaeger 代理的分布式跟踪平台。那是在 2019 年。

于 2020 年 4 月开始推出 OTel Collector ，以取代 Jaeger 代理。最初， Collector 只是摄取跟踪，但在 2021 年 9 月，引入了指标，他们也希望引入日志。

![](https://cdn.thenewstack.io/media/2023/06/3d665717-image1.png)

团队使用 Open Telemetry 库(主要是自动 instrumentation )和主要的 Java 来 instrument 应用程序。它执行一些应用程序增强，引入 Adobe 特定的数据并在数据流向 collector 的过程中丰富其管道。它有一些自定义 extensions 和 processors，团队在可能的情况下通过 GitOps 进行配置。

Featherstone 表示:" collector 非常动态的，可以使用一组数据扩展到多个目的地，这对我们来说是巨大的。......有时我们会将收集器的数据发送到其他收集器以进行进一步处理。所以它是可观测性的瑞士军刀。"

他在 Adobe 的团队被称为开发人员生产力，其章程旨在帮助开发人员更快地编写更好的代码。

尤其对于 Java 服务，它有一个基本容器，“如果您使用 Java 镜像，您应该使用这个......它已经集成了许多提高生活质量的功能，包括 OpenTelemetry Java instrumentation 的 jar 包。[配置]来自我们的文档，这正是我们为Java配置的方式。”

他说："所以我们将 Jaeger 端点设置为本地 DaemonSet collector 。我们将指标 exporter 设置为 Prometheus ，我们设置了 propagators，我们设置了一些额外的资源属性，我们设置了 tracer ，将 exporter 设置为 Jaeger 。我们将跟踪采样设置为基于父级的总是关闭状态。"他指出这一切都融入了 Java 镜像。

因此，通过这些配置，任何在 Adobe 的 Kubernetes 中启动的 Java 服务都已经参与了跟踪。以这种方式设置的所有内容都通过 collector 。

他说:"所以每个人只要启动这个应用程序就可以参与跟踪。"他说道:" metrics ，我们努力降低摩擦，人们仍然需要以某种方式从该 exporter 中获取这些 metrics 。我们已经使这个过程变得相当简单，但它不是自动的。"他说，他们运行的大约 75% 是 Java ，但他们正试图将同样的概念应用于 Node.js 、 Python 和其他镜像。

## 管理数据

他们做了很多扩充，并确保没有 secrets 作为我们的跟踪或指标数据的一部分发送，Adobe的云运营站点可靠性工程师 Surana 说。

它使用多个进程，包括缩减处理器以及 OpenTelemetry Collector 中的自定义 processor，后者允许他们消除某些不想发送到后端的字段，这些字段可能是个人身份信息或其他敏感数据。他们还用于丰富数据，因为添加更多字段，如服务标识符、 Kubernetes 集群和地区可以改善搜索。

“ Adobe 是在积极收购的基础上建立起来的，我们在不同的生态系统中运行多种不同的产品。服务名称很有可能在不同的产品下或类似的微服务名称下发生冲突，因此我们希望确保这种情况不会发生，“他说。

它还使用 Adobe 特定的服务注册表，其中每个服务都有一个附加到服务名称的唯一 ID 。它允许 Adobe 的任何工程师在单个跟踪后端中唯一标识服务。

“它也允许工程师快速搜索事物，即使他们不知道该服务，或者他们不知道谁拥有该服务，他们也可以查看我们的服务注册表，找出该特定产品或团队的工程联系人，并打电话解决他们的问题，” Surana 说。

![](https://cdn.thenewstack.io/media/2023/06/b95e5645-image2.png)
*它们还将数据发送到多个导出目标。*

他说："这可能是最常见的用例。"在引入 OpenTelemetry Collector 之前， Adobe 的工程团队一直使用不同的流程、不同格式的不同库。他们将其发送到供应商产品、开源项目，对我们来说很难让工程团队改变他们的后端，或只在后端代码或他们的应用程序代码中进行任何小的变更，因为工程师有自己的产品特征和产品需求，他们正在努力实现。

“随着 OpenTelemetry Collector 的引入，以及 OTLP [OpenTelemetry协议] 格式，这对我们来说变得非常容易；我们能够将他们的数据发送给多个供应商，多个工具，只需进行少量更改。

去年，他们能够同时将跟踪数据发送到三个不同的后端，以测试一个特定于工程的用例。

他们现在将数据发送到边缘的另一组 OTel 收集器，在那里他们可以进行转换，包括反向采样，基于规则的采样和基于吞吐量的采样。

他说，他们一直在寻找其他方法来获得更丰富的见解，同时向后端发送更少的数据。

“整个配置由 git 管理。我们主要将 OpenTelemetry Operator Helm Chart 用于我们的基础设施用例。...它剥夺了工程师成为主题专家的责任......并使配置变得超级简单，“他说。

使用 OpenTelemetry Operator 的自动 instrumentation 允许工程师只需传入几个注释，即可自动检测所有不同信号的服务，而无需编写任何代码。

“这对我们来说是巨大的，”他说。这将开发人员的工作效率提升到一个新的水平。

![](https://cdn.thenewstack.io/media/2023/06/cd0ab508-image3.png)

他们还使用自定义身份验证器接口在 OpenTelemetry Collector 之上构建了一个自定义扩展。他们对这个身份验证系统有两个关键要求：能够使用单个系统安全地将数据发送到不同的后端，并能够为开源和供应商工具保护数据。

OpenTelemetry Collector 附带了一组丰富的流程，用于构建数据流程，包括一个属性处理器，它允许您在日志数据和矩阵数据之上添加属性。它允许您转换、丰富或修改传输中的数据，而无需应用程序工程师执行任何操作。Adobe 还使用它来改进其后端的搜索功能。

内存限制器处理器有助于确保 OTel 永远不会耗尽内存，并检查保持状态所需的存储量。他们还使用 span 到矩阵处理器和 service graph 处理器从跟踪中生成数据，并动态构建指标仪表板。

## 那么下一步是什么？

根据 Featherstone 的说法，有两件事：提高数据质量，即摆脱没有人会看的数据，以及在边缘限制 spans 。

collector 在边缘提供创建规则和删除某些数据的功能。

“对于指标，想象一下我们有能力在收集器本身中进行聚合。你知道，也许我们不需要15秒的粒度，让我们把它简化为五分钟，然后发送出去，“ Featherstone 说。

“另一个例子可能是发送一些指标进行长期存储，并将一些指标发送出去以在某个运营数据湖或类似系统中进一步处理。我们有能力在 collector 中直接调整方向，做各种各样的事情。”

第二件事是边缘的 span 速率限制。

他说："我们的边缘之一每天有大约 60 亿次点击量，我们正试图对此进行跟踪。当您谈论将所有这些数据一直传送到某个地方进行存储时，这将产生大量数据。因此，我们正试图弄清楚在哪些 collectors 中以及在什么级别实现速率限制的正确位置......只是为了防止未知的流量突发，这种情况。"

他们还试图更多地转向跟踪优先故障排除。

他说:"我们有许多东西向服务，试图通过日志来完成此操作，并试图为任何团队拉起正确的日志索引，甚至是否有权访问它或其他什么。这是如此缓慢和难以完成，以至于我们正努力改变 Adobe 内部故障排除的方式，改为像这样的方式，我们已经付出了很多努力来使这些跟踪变得相当完整。"

他们还研究了人们如何进行故障排除，以及他们拥有的工具是否提供了最好的方法。

他们期待将 OpenTelemetry 日志记录库与核心应用程序库集成，并将 OTel 收集器作为边车来发送指标，跟踪和日志。他们探索新的连接器组件，并在边缘构建跟踪采样扩展，以提高数据质量。

最后，他称赞了收集器基于插件的架构以及使用单个二进制文件将数据发送到不同目的地的能力。他说，有一组丰富的 extensions 和 processors ，可以为你的数据提供很大的灵活性。

“总的来说， OpenTelemetry 对我来说感觉很多，就像 Kubernetes 的早期一样，每个人都在谈论它，它开始就像我们现在走在曲棍球棒的道路上一样，”他说。“社区很棒。这个项目很棒。如果你还没有用 collector ，你一定要去看看。