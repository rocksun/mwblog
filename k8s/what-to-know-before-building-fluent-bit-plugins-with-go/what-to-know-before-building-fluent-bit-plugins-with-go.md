
<!--
title: Go 语言构建 Fluent Bit 插件：要点速览
cover: https://cdn.thenewstack.io/media/2025/11/65e41250-birds.jpeg
summary: 文章介绍了 Fluent Bit 的 Go 插件，分析了其组织和技术优势，如灵活性和原生二进制性能。同时指出了操作上的缺点，如过滤器接口缺失和额外的维护成本。推荐阅读《Fluent Bit with Kubernetes》深入了解。
-->

文章介绍了 Fluent Bit 的 Go 插件，分析了其组织和技术优势，如灵活性和原生二进制性能。同时指出了操作上的缺点，如过滤器接口缺失和额外的维护成本。推荐阅读《Fluent Bit with Kubernetes》深入了解。

> 译自：[What To Know Before Building Fluent Bit Plugins With Go](https://thenewstack.io/what-to-know-before-building-fluent-bit-plugins-with-go/)
> 
> 作者：Phil Wilkins

***编辑注：** 以下文章摘自 Manning 出版的书籍：《[Fluent Bit with Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS)》。这本书是关于优化 Kubernetes 系统的实用指南，涵盖了从基础配置到日志、指标和跟踪路由及处理的高级集成。本文摘录重点介绍了基于 Go 的 Fluent Bit 插件。通过在此处下载整本书，您可以探索如何使用类 SQL 表达式处理信号，以及何时以及如何构建自定义插件。*

[Go](https://go.dev) 是 [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) [项目](https://gloutnikov.com/post/cncf-language-stats/) 中最主要的语言，它带来了原生二进制性能的优势，同时保留了 Java 等语言的内存管理、抽象和易开发等特性。Kubernetes 的起源（Google）是 [Go 语言开发](https://thenewstack.io/introduction-to-go-programming-language/) 的推动力，这也有助于其推广。

云解决方案（尤其是超大规模解决方案）对原生二进制性能的重视，使得 C/C++ 与 Go 之间的直接集成变得很重要，因为 Linux 内核是用 C/C++ 编写的，而在 CNCF 项目使用的原生二进制语言中，Go 语言位居第一，C/C++ 位居第二。

[Go 插件通过 Fluent Bit 中的 [Goproxy 模块](https://github.com/fluent/fluent-bit/tree/master/src/proxy/go) 与 Fluent Bit [框架进行交互](https://docs.chronosphere.io/pipeline-data/plugins/source-plugins/fluent-bit?&utm_source=sponsored-content&utm_id=TNS)。在本文撰写之时，Goproxy 和相关的 Go 绑定代码仅暴露了输入和输出插件，并未暴露过滤器接口。

## 构建 Go 插件的组织和技术优势

使用 Go 并配置将 Go 插件添加到 Fluent Bit 中，可以带来一系列组织和技术优势：

* 开源项目不强制规定发布周期和开发流程。
* 由于最终结果是以原生二进制文件的形式交付的，因此可以在不暴露专有代码或知识产权的情况下提供插件。
* 针对特定组织需求或细分领域要求而设计的细分用例非常理想。这类用例通常具有一定程度的知识产权（即使在支持功能方面是间接的）。

例如，对于处理视频转码器错误的插件，使用视频转码器的组织数量相对较少，而使用特定转码器并通过自定义方式生成 [日志和事件](https://docs.chronosphere.io/ingest/logs/pipeline-logs?utm_source=c&utm_id=TNS) 的组织数量则更少。

* 可以实现插件以满足特定的内部需求，而不必过多考虑社区。如果我们的组织对命名约定有特定的标准，我们可以将其硬编码到插件中，而不必担心它是否满足更广泛的社区需求。

使用 Go 构建插件的技术优势包括：

* Go 在保留原生二进制可执行文件性能的同时，不会失去语言运行时进行的内存管理的优势。
* [Go 语言](https://chronosphere.io/learn/best-languages-for-microservices/?&utm_source=sponsored-content&utm_id=TNS) 作为标准提供了[绑定到 C 应用程序](https://pkg.go.dev/cmd/cgo) 的能力，并且 Fluent Bit 包含一个库，可以进一步[帮助实现接口](https://github.com/fluent/fluent-bit-go)。
* 开发方法，特别是对于闭源或私有解决方案的实现，可以与内部原则和实践保持一致，而不必考虑更广泛的社区。

## 基于 Go 的 Fluent Bit 插件的操作缺点

这些缺点更多是操作层面的，而不是代码开发本身。这些挑战包括：

* 在本文撰写时，过滤器接口不可用。
* 如果开发团队不使用 Go，那么在实施和维护持续集成等流程方面仍然存在额外的开销。我们需要为主要和次要版本包含回归测试。
* 如果我们打算将插件开源，它可能不会像核心 Fluent Bit 存储库那样受到同样的关注。因此，维护负担将更多地落在插件提供者身上。
* 用户在现有环境中部署我们的插件时需要额外的部署工作，如果客户使用 [OpenShift 等预打包平台](https://www.imaginarycloud.com/blog/openshift-vs-kubernetes-differences#:~:text=Developed%20by%20Red%20Hat%2C%20OpenShift%20is%20written,be%20extended%20to%20support%20other%20programming%20languages.)，这可能会带来问题。
* 付费支持服务的范围可能不明确，因为第三方支持产品通常不涵盖第三方插件。
* 即使解决方案稳定且成熟，插件也需要进行持续的定期更新，以防止出现插件过时的可能看法。
* 需要额外的开发工作才能在 C 和 Go 原生数据类型之间进行转换。我们将不得不使用其他的 Go 语言库和框架。
* 我们可能需要使用 Go 支持重新构建 Fluent Bit（`cmake -DFLB_DEBUG=On -DFLB_PROXY_GO=On`），具体取决于我们使用的 Fluent Bit 版本。请注意，Fluent Bit 项目提供的镜像默认启用了此构建标志。注意：可访问 <https://github.com/fluent/fluent-bit-go> 获取基于 Go 的开发资源，包括示例实现和用于简化 Go-C 接口的 Go 实用程序库。

如果您想更深入地了解 Fluent Bit 处理器如何[重塑指标、跟踪和日志](https://docs.chronosphere.io/ingest/metrics-traces/collector/install/kubernetes?utm_source=c&utm_id=TNS)，包括在信号上使用类 SQL 表达式，何时选择自定义插件以及如何选择不同的实现技术，请下载整本书《[Fluent Bit with Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS)》。在下一章中，您将全面了解插件生态系统，以便能够自信地在自己的环境中设计、构建和运行自定义扩展。

要了解更多关于 Fluent Bit 的信息，请阅读：

- [What Is Fluent Bit?](https://thenewstack.io/fluent-bit-core-concepts/)
- [What Are the Differences Between OTel, Fluent Bit and Fluentd?](https://thenewstack.io/what-are-the-differences-between-otel-fluent-bit-and-fluentd/)
- [What’s Driving Fluent Bit Adoption?](https://thenewstack.io/whats-driving-fluent-bit-adoption/)