# OpenTelemetry 与 Go：eBPF 新世界

在 OpenTelemetry Go 项目的重大新闻中，必须包括通过引入 eBPF 技术，实现对使用 OpenTelemetry 的 Go 服务的自动 instrumentation 。之前，在自动为应用程序添加 instrumentation 方面，Go 存在严重的限制，这限制了 OpenTelemetry Go 项目的覆盖范围。之前所承诺的在 Go 应用程序中实现"自动 instrumentation "的指南，[最终仍然需要对应用程序代码进行一些编辑](https://utsavbatra5.medium.com/automatic-instrumentation-of-a-go-application-using-opentelemetry-4c1b0e4c98a)。

翻译自 [OpenTelemetry and Go: a whole new eBPF world](https://www.signadot.com/blog/opentelemetry-and-go-a-whole-new-ebpf-world) 。

![](https://assets.website-files.com/648776302927d2295495974a/64d2f33ebd48c4edd5358b3b_beehive.webp)

要求在新事务开始时添加一个单独的调用似乎可能微不足道。但如果你正在阅读这篇博文，你可能正在一个规模较大的团队中工作，并且在某种程度上拥有某种架构。虽然在演示应用程序或初始单体应用中手动添加 instrumentation 是有效的，但是通常负责在大规模微服务架构中添加可观测性的运维团队甚至无法访问编辑应用程序代码的权限。而且在每次启动事务时让数十个或数百个开发人员添加"一个小调用"是一场组织上的噩梦。不，理想情况是像 OpenTelemetry Kubernetes Operator 的体验一样，在这种情况下，运维人员可以向集群添加一个服务，为每个 Pod 提供一些配置，而无需涉及开发人员即可开始监视其服务。在 Java 领域，这是可能的！

为什么我们不能在 Go 中实现与 Java OpenTelemetry sdk 相同的"真正自动"过程？问题在于字节码操作。Java 代码被编译为字节码，然后被解释执行，这些字节码可以通过插入 instrumentation 调用来进行修改。这不是 Java 的"黑客"行为，而是 Java 代理规范明确支持的功能。然而，在 Go 中不支持这种字节码修补，因此在不进行至少一些 Go 代码编辑的情况下，过去几乎没有办法使用 OpenTelemetry 配合 Go 使用。

## 引入 eBPF 技术

eBPF（扩展伯克利数据包过滤器）是一项强大的技术，允许实时动态修改内核代码。通过使用 eBPF，可以监视和分析网络流量、系统调用和其他内核事件。eBPF 最重要的特性之一是通过分析堆栈和 CPU 寄存器来访问用户代码和变量的能力。这个特性使得能够开发强大而灵活的仪器化工具，用于监视和排查复杂的系统问题。同样，这不是一个"黑客"行为，eBPF 的主要应用是用于添加 instrumentation 。

eBPF 的同样用途使得像 [Falco](https://falco.org/docs/event-sources/kernel/)（安全性）、[Pixie](https://px.dev/)（针对 Kubernetes 上应用程序的 APM）和 [Cilium](https://cilium.io/)（网络监控）等项目成为可能。

## 不仅仅是原型：稳定的 instrumentation

团队为实现一个在生产环境中可用的稳定版本的仪器化工具付出了极大的努力。举一个例子： eBPF 程序需要一种方法来标识用户空间中特定数据结构和变量的位置。例如，要读取 google.golang.org/grpc.ClientConn 结构中的 target 字段的值（如 [gRPC instrumentor](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/main/instrumentation/google.golang.org/grpc/otelgrpc/interceptor.go) 中所示），eBPF 程序需要确定该字段在结构定义中的偏移量。这个偏移量由 eBPF 程序用于访问目标字段并执行必要的分析。

确定结构体字段的偏移量的一种方法是将偏移信息硬编码到 eBPF 程序中。然而，这种方法可能会导致仪器化非常不稳定。结构体内部的字段位置可能会改变，这意味着每次结构体定义更改时都必须重新编译 eBPF 程序。这个过程可能会耗费时间，而且对于庞大而复杂的代码库来说，容易出错。结果是仪器化变得脆弱，并且显著增加了构建时间。

有一种方法可以在不将偏移信息硬编码到 eBPF 程序中的情况下提取所需的偏移量。这可以通过使用 DWARF（带有属性记录格式的调试）来分析目标二进制文件来完成，DWARF 是许多编译器使用的一种调试信息格式，包括 Go 编译器。DWARF 调试信息由编译器生成并存储在二进制文件中。通过分析 DWARF 信息，可以提取 eBPF 程序所需的偏移量。

为了减小生产二进制文件的大小并提高性能，通常会从生产二进制文件中剥离 DWARF 信息。这意味着 eBPF 程序可能无法从已剥离的二进制文件中提取所需的偏移量。为了解决这个问题，团队开发了一个名为 offsets-tracker 的库。这个库跟踪不同版本中不同字段的偏移量，并将它们存储在数据库中。

offsets-tracker 库为 eBPF instrumentation 提供了稳定且灵活的解决方案，即使数据结构发生变化并且二进制文件被剥离。

## 另一个挑战：时间

相比其他后端 Web 应用程序，Golang 确实是一个非常不同的环境，这在学习即使是纪元时间也不容易获取时更加明显。从项目关于 Go 仪器化的描述中可以了解到：

eBPF 程序可以通过调用 bpf_ktime_get_ns() 来访问当前时间戳。这个函数返回的值从 CLOCK_MONOTONIC 时钟中获取，并表示自系统启动时间以来的纳秒数。

根据 OpenTelemetry 规范，起始时间和结束时间应该是时间戳，并表示确切的时间点。将单调时间转换为纪元时间戳是由这个库自动处理的。通过发现纪元启动时间并将其添加到 eBPF 程序收集的单调时间中，实现了这种转换。

## 对于Go社区意味着什么

这对于 Golang 社区来说是一个巨大的变革，因为自动仪器化意味着在微服务集群中无论何时何地都能更容易地添加 OpenTelemetry 。这很重要，因为实际上，Go 服务的问题很少是服务内部的代码缓慢，我们必须看到整个集群正在工作，并在整个集群中跟踪请求，以找出性能问题的源头。

## 结论

在 Go 中使用 eBPF 进行自动 instrumentation 是 OpenTelemetry 项目和 Go 社区的一次重大变革。它允许实现真正的自动 instrumentation ，无需手动编辑代码，并在数据结构发生变化和二进制文件被剥离时提供稳定的 instrumentation 。这将使在微服务集群中添加 OpenTelemetry 变得更加容易，从而更容易地跟踪请求并识别性能问题的源头。
