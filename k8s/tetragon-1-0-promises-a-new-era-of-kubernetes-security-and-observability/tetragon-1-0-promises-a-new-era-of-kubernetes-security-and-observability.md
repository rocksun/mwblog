<!-- 

# Tetragon 1.0承诺开启Kubernetes安全与可观测性新纪元
https://cdn.thenewstack.io/media/2023/11/4020e19e-tetragon-1024x768.png
 -->

基于 eBPF 的安全可观测性和运行时执行平台已经成熟并获得加速。

译自 [Tetragon 1.0 Promises a New Era of Kubernetes Security and Observability](https://thenewstack.io/tetragon-1-0-promises-a-new-era-of-kubernetes-security-and-observability/) 。


一年半前，[Isovalent](https://isovalent.com/) 公司开源了 [Tetragon](https://github.com/cilium/tetragon)，该公司将网络、安全、Kubernetes 和 [eBPF](https://ebpf.io/) 融入其方案中。如今，这个流行且实用的基于 [eBPF](https://thenewstack.io/ebpf-offers-a-new-way-to-secure-cloud-native-systems/) 的安全可观测性和运行时执行平台已经达到 1.0 里程碑。

[Tetragon 1.0](https://isovalent.com/blog/post/tetragon-release-10/) 标志着 Kubernetes 安全与可观测性的重大进展。1.0 版本的主要关注点在于性能提升。Tetragon 旨在提供全面的安全可观测性信息，同时使性能开销最小化。在不影响安全信息的前提下，保持系统效率与安全见解之间的平衡至关重要。

对不了解的人来说，Tetragon 是一种[利用 eBPF 实现深度可观测性](https://thenewstack.io/groundcover-simplifying-observability-with-ebpf/)且性能影响最小的[原生 Kubernetes 工具](https://tetragon.io/)。它可以跟踪大量活动，包括进程执行、特权提升以及网络活动。它基于 eBPF 实现的内核运行时策略可以针对未经授权的操作和时间检查-时间使用(TOCTOU)竞争条件攻击提供强大的安全防护。

虽然 Tetragon 的核心 eBPF 是 Linux 程序，但 Tetragon 意识到 Kubernetes 并作为 DaemonSet 原生运行在 Kubernetes 中。所有安全可观测性事件都会自动丰富 Kubernetes 元数据，如 Pod 名称、标签、命名空间信息和容器哈希。可观测性和执行策略可以以细粒度的方式仅应用于某些 Kubernetes 工作负载。

Isovalent 在上周在芝加哥举行的[ KubeCon+CloudNativeCon 2023](https://thenewstack.io/kubecon-2023-managing-pets-cattle-and-starfish/) 上发布了此工具的 1.0 版本。

通过使用 eBPF 作为在内核中观察和过滤事件的核心机制，Tetragon 具有高效性和微小的占用空间。通过限制传输到用户空间的只相关事件，Tetragon 减少了开销，消除了噪音，并在采取执行操作时消除了不必要的延迟和竞争条件。

使用它进行可观测性非常简单。您只需从策略库中选择策略，即可立即获得 Linux 机器和 Kubernetes 集群内部丰富的数据视图。

Tetragon 还突出的一点是它可以与其他程序透明地协同工作。例如，它不需要更改现有代码。它还可以与 Prometheus、Grafana、Splunk 和 Elasticsearch 等其他工具无缝集成，以获得增强的见解和积极的安全措施。

正如 GitHub 员工安全工程师 Jason Cetina 在声明中所说：“Tetragon 为我们的安全团队提供了丰富的数据，这些数据将重要的网络、进程和 Kubernetes 元数据连接成单个事件记录。获得这种组合视图的活动使我们能够在节点、命名空间、pod 和容器级别查询集群上的网络活动细节。此外，它的设置很快，对我们的规模来说性能开销很小，这一点非常关键。”

根据 Isovalent 的说法，随着此次发布，Tetragon 速度更快了。其性能基准测试证明了其在各种场景(包括进程执行跟踪和可扩展文件监控)中的效率。这将使其非常适合审计 [kubectl exec  usage](https://thenewstack.io/scale-applications-in-kubernetes-with-kubectl-and-the-horizontal-pod-autoscaler/) 情况、关联网络和运行时遥测以及大规模实施文件完整性监控。监控网络连接以快速检测网络攻击的能力至关重要。

随着 Tetragon 不断发展，它似乎注定要通过提供深度可观测性与最小性能影响的独特组合，成为 Kubernetes 安全的一个强大高效的工具。
