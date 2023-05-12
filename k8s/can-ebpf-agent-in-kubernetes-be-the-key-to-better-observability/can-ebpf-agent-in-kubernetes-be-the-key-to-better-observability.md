# Kubernetes 中的 eBPF 代理能否成为提高可观测性的关键？

翻译自 [Can eBPF Agent in Kubernetes Be the Key to Better Observability?](https://thenewstack.io/can-ebpf-agent-in-kubernetes-be-the-key-to-better-observability/)

Groundcover 自豪地宣称，他们使用一种新的 eBPF 可观测性工具取得了更好的结果，比竞争对手的工具性能提高了三倍以上。

![](https://cdn.thenewstack.io/media/2023/05/8b67ef90-frederick-marschall-bl8mdg0p_ni-unsplash-1024x683.jpg)

以色列初创公司 Groundcover 正在使用一种新的 eBPF 可观测性工具 —— 称为 [Flora](https://www.groundcover.com/blog/ebpf-observability-agent) agent —— 它声称在与 New Relic 的 Pixie 代理和 Groundcover 的 Flora 代理一起运行在 Kubernetes 节点上时，胜过了其他应用程序监视工具，如 DataDog 和 [OpenTelemetry](https://opentelemetry.io/) 。

据 Groundcover 称， Flora agent 在与 New Relic 的 Pixie agent 和 Groundcover 的 Flora agent 一起在 Kubernetes 节点上运行时，其性能优于 Datadog 等其他[应用程序监视](https://thenewstack.io/application-performance-monitoring-vs-observability-silo/)工具超过三倍。 Flora agent 对应用程序的CPU（+9％）和内存（+0％）的开销最小，几乎没有开销，而 Datadog， OpenTelemetry 和 Pixie agent 的开销分别为其 CPU 基线的 249％ ， 59％ 和 32％ ，以及其内存基线的 227％ ， 27％ 和 9％ 。

CTO [Yechezkel Rabinovich](https://www.linkedin.com/in/yechezkel-rabinovich-946794b4/?originalSubdomain=il) 在一篇[博客文章](https://www.groundcover.com/blog/ebpf-observability-agent)中表示：“除了 Flora 之外，所有其他解决方案都极大地提高了应用程序的资源消耗，并以意想不到的方式潜在地导致应用程序达到 CPU 限制，可能会降低其性能甚至在有限环境中创建内存溢出(OOM)崩溃。” “ Flora 在总资源消耗方面也被证明非常高效，使其成为高规模环境下最具成本效益的解决方案。”

当结合测试的不同代理消耗的资源和在受监控应用程序上测量的开销时，Flora 消耗的总 CPU 与 OpenTelemetry 和 Pixie 代理使用的 CPU 相似，但比 Datadog 消耗的 CPU 少 73% ，博客文章称。 “此外，Flora 消耗的内存分别比 Datadog、OpenTelemetry 和 Pixie 代理少 74%、77% 和 96%，”它补充道。

Flora Agent 于 4 月在 [KubeCon+CloudNativeConEurope 2023](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 上发布。它利用[内核中的 eBPF](https://thenewstack.io/groundcover-simplifying-observability-with-ebpf/) 来访问有关 Kubernetes 中应用程序的数据。

## 在内核中安全地运行代码

“你可以把 eBPF 看作一种修改内核的方式，而无需编译内核模块，” Rabinovich 告诉 The New Stack 。“这基本上意味着它类似于 JavaScript 对浏览器所做的事情——您可以自动适应不同的浏览器，而浏览器现在支持运行 JavaScript ，因此您可以在不需要考虑客户使用的浏览器类型的情况下运行代码。因此，在某种程度上， eBPF 也是这样的，您可以编写代码，它将在内核中安全运行，而无需测试每个内核版本。”

过去，即使不是不可能，也很难获得 eBPF 可以实现的某些数据。 Rabinovich 解释说，开发人员必须检测应用程序才能获取数据。通常，公司仍未获得 100% 的可观察性数据；他补充说，有些公司正在努力实现 10% 到 15% 的可观察性数据。

可观测性通常分为三种类型的数据：

* Logs
* Metrics
* Traces（监控交互路径，例如端到端事务和服务之间发生的事情）

[Shahar Azulay](https://www.groundcover.com/contact/shahar), Groundcover 的首席执行官表示，对于大型开发团队来说，时间就是价值。

“传统的可观测性平台需要你更改代码，”他说。“想象一下它对价值时间的影响。我们通常会遇到拥有 100 名开发人员的组织，他们已经使用不同的语言和庞大的技术堆栈来集成 OpenTelemetry （这是社区的建议）或 Datadog 。你必须通过每一个主题，每一个运行它们自己的指令，以及特定堆栈的适合性，将所有这些作为组织的领导者并将其推向生产环境。这需要几周时间。”

使用 eBPF，通常是一个 [DevOps 可靠性工程师（SRE](https://thenewstack.io/platform-engineering/sre-vs-devops-vs-platform-engineering/)）可以“只需将其立即安装在集群上，就可以恢复所有内容，”Azulay说道。

“突然之间，你可以将每个人都调整到相同的深度，因为你是从内核级别而不是应用程序级别观察的。与可观测性相比，这是一个令人兴奋的差异——可观察性供应商进入组织的大门，而不是研发团队和开发人员，他们可以去基础设施，” Azulay 说。

根据博客文章，测试应用程序是用 Golang (v1.19) 构建的基本 HTTP 服务器，它会提供可配置数量的随机 JSON 对象，并对每个接收到的请求执行预配置数量的 CPU 密集型任务，并以 Plaintext 或 Gzip 格式返回其响应。在不同的场景下对测试应用程序进行了测试，包括基线测试（未进行任何监测），根据 Datadog 和 OpenTelemetry 的相关文档进行仪表化测试，以及在 Kubernetes 节点上与 New Relic 的 Pixie 代理和 Flora 代理一起运行时进行测试。对于所有测试用例，生成了基于 Prometheus 的 CPU 和内存利用率指标，并将其抓取并存储在 VictoriaMetrics 数据库实例中。

在这个测试中，使用的基础设施是一个 Kubernetes 集群，其中包含 Node Taints，允许 Groundcover 将每个测试案例隔离开来。每个测试的应用程序版本都与监控所需的最少组件一起运行。

Groundcover 使用了 K6 operator 来生成测试负载，使用 K6 测试对象从每个单独的节点组执行。 Groundcover 使用了一个自定义的 K6 镜像，该镜像还暴露了 Prometheus 指标，以便进行合理性检查时可以从客户端获取指标。结果是通过 Grafana 进行分析的，通过一个 Prometheus 数据源集成来查询已部署的 VictoriaMetrics 实例，这些都在 Rabinovich 的博客文章中进行了说明。