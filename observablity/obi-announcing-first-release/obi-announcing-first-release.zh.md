# OpenTelemetry eBPF Instrumentation 发布第一个版本

作者

**[Nikola Grcevski](https://github.com/grcevski) (Grafana Labs)，[Tyler Yahn](https://github.com/MrAlias) (Splunk)**

|

2025年11月3日，星期一

在Grafana Labs、Splunk、Coralogix、Odigos和许多其他社区成员的重大合作之后，我们非常高兴地宣布[OpenTelemetry eBPF Instrumentation](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation)（简称OBI）的第一个Alpha版本发布。

这一事件标志着该项目（最初名为Grafana Beyla）在今年早些时候由Grafana Labs捐赠后的一个重要里程碑。在项目由OpenTelemetry管理后，eBPF instrumentation 的开发速度显著加快。许多新协议已被添加，质量得到提升——尤其是在大规模部署时，并且测试运行速度快了10倍。这真实地证明了OpenTelemetry社区的价值。

## 什么是OpenTelemetry eBPF Instrumentation，为什么你应该关注它？

与许多其他OpenTelemetry instrumentation 方法不同，OpenTelemetry eBPF instrumentation（OBI）是进程外运行的，并在协议层面而非库层面进行instrumentation。它利用了eBPF技术的深度内核集成、进程隔离、运行时安全和性能优势。

由于OBI在协议层面进行instrumentation，这意味着你基本上可以通过一个简单的命令，以零成本对所有应用程序（所有编程语言、所有库）进行instrumentation，并且始终能得到一致的视图。让我们将之前的声明细化为对最终用户而言的实际含义：

1.  无需重启，无需代码更改，无需应用程序配置更改！仅凭OBI就能提供指标和跟踪的完全自动化捕获。eBPF的优点在于你可以将其部署到运行环境中，并确信它不会破坏你的系统/集群/应用程序的稳定性。
2.  没有新的应用程序依赖——没有新的安全漏洞。由于OBI是进程外运行的，我们不会向你的应用程序添加任何内容。你无需升级或添加OpenTelemetry SDK依赖项，如果已添加的OpenTelemetry SDK依赖项存在漏洞，也无需修补你的应用程序。你可以独立地保护OBI在系统上的访问，这不会影响你安装的任何其他内容。
3.  添加遥测数据不会使你的应用程序变慢。由于你的应用程序无需添加任何内容或执行任何工作来导出遥测数据，因此应用程序的性能不会受到遥测捕获的影响。OBI大部分工作在内核级别完成，并且经过高度优化以提高性能。即使在非常高的请求速率下，它也具有最小的CPU和内存占用。
4.  你的遥测数据在所有编程语言和库中始终保持一致。OBI将使你的遥测数据在所有服务中保持最新的OpenTelemetry稳定规范，而无需你费力处理合规性问题。
5.  支持广泛的协议instrumentation，包括HTTP/HTTPS、HTTP/2、gRPC、SQL、Redis、MongoDB、Kafka、GraphQL、Elasticsearch/OpenSearch、AWS S3。所有编程语言的自动跟踪上下文传播。

## 我应该对所有事物都使用OpenTelemetry eBPF Instrumentation 吗？

是的，但…

OpenTelemetry eBPF Instrumentation（OBI）在某些方面表现出色，但与其他OpenTelemetry技术结合使用时会变得更好。让我们看看这在实践中意味着什么。

OpenTelemetry eBPF Instrumentation 是开始使用OpenTelemetry的绝佳工具。它可以快速为你提供基本的信号，如RED（请求错误持续时间）指标、服务图和某些类型应用程序的跟踪。然而，由于数据捕获是在内核级别完成的，其他类型的OpenTelemetry instrumentation 可以提供的某些详细程度将不会存在。让我们详细看看这意味着什么：

1.  如果你根本没有遥测数据，或者只有部分遥测数据，那么尝试使用OBI，它是一种轻松实现所有内容自动instrumentation（特别是编译后的二进制文件）的方法。OBI会检测应用程序是否已通过另一个OpenTelemetry SDK 进行instrumentation，并且不会重复信号。因此，将其部署到已instrumentation和未instrumentation的应用程序混合环境中既简单又安全。
2.  如果你的应用程序正在使用没有OpenTelemetry支持的库，例如比官方支持库更旧的库，或者没有人为其提供instrumentation的库，请尝试使用OBI。
3.  保留已成功通过OpenTelemetry SDK或代理进行instrumentation的服务。很少有理由放弃其他类型的OpenTelemetry instrumentation，除非你遇到显著的性能或成本问题。在这种情况下，OBI可能会有所帮助。
4.  虽然OBI是收集指标和服务图的优秀工具，但它对某些语言和技术而言，在分布式跟踪支持方面表现不佳。例如，它目前不处理响应式编程框架、Java虚拟线程或复杂线程池的分布式跟踪。通常，OBI的分布式跟踪对于Go（HTTP和gRPC）、Node.js（HTTP）、Python（HTTP）、NGINX（HTTP）、PHP（HTTP/FPM）运行良好，而对于其他编程语言，支持程度会因应用程序内部管理线程和连接的方式而大相径庭。我们正在寻求帮助，以更广泛地扩展分布式跟踪支持。分布式跟踪的限制已在我们的文档的[使用OBI的分布式跟踪](/docs/zero-code/obi/distributed-traces/)部分中说明。

## 总结

我们认为，**可观测性**应该是现代基础设施的内置功能，而不是附加的成本中心。OpenTelemetry eBPF Instrumentation 允许你通过一个简单的命令行将必要的遥测捕获添加到你的环境中。现在，你再也没有理由不使用OpenTelemetry了。无需付出努力，无需停机，无需代码或配置更改，有充分的理由尝试一下。

## 开始使用OpenTelemetry eBPF Instrumentation

开始使用OpenTelemetry eBPF Instrumentation（OBI）非常简单！你可以将其独立部署，作为Docker镜像，或作为Kubernetes Daemonset（或Pod Sidecar）。有关安装、配置以及使用OBI运行应用程序的详细说明，请查阅[入门指南](/docs/zero-code/obi/setup/)。

有关如何在docker环境中安装OBI的完整示例，你可以查看我们的许多[集成测试示例](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/tree/main/internal/test/integration)，这些示例结合了多种编程语言、数据库后端和云服务。在我们的Kubernetes [测试仓库](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/tree/main/internal/test/integration/k8s/manifests)中也有一些Kubernetes示例。

## 后续步骤

如果你想与我们取得联系，建议我们应该开发的功能，或者关注我们的工作并及时了解我们的发布，你随时可以在GitHub的[OpenTelemetry eBPF Instrumentation 仓库](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation)找到我们。我们每周还会定期举行非常活跃的[特别兴趣小组 (SIG) 社区电话会议](https://github.com/open-telemetry/community?tab=readme-ov-file#sig-ebpf-instrumentation)，你可以在此加入并成为我们社区的一部分。如果你无法参加我们的社区电话会议，你也可以在CNCF Community Slack频道[#otel-ebpf-instrumentation](https://cloud-native.slack.com/archives/C08P9L4FPKJ)上轻松异步找到我们。

## 致谢

本次Alpha版本的发布是世界各地贡献者无数小时工作的结果。感谢所有为实现这一里程碑贡献代码、文档、反馈和热情的每一个人。