
<!--
title: eBPF：可靠的策略设置和执行
cover: https://cdn.thenewstack.io/media/2024/04/4ffa1a23-water-sunset-1.png
-->

eBPF 的强大功能主要在于其计算效率，因为它直接与 Linux 内核相关联。

> 译自 [eBPF: Reliable Policy Setting and Enforcement](https://thenewstack.io/ebpf-reliable-policy-setting-and-enforcement/)，作者 B Cameron Gain。

巴黎 — [eBPF](https://thenewstack.io/what-is-ebpf/) 和使用 eBPF 构建的工具通常被视为提供可观察性、安全性或网络功能。但可以说，在许多情况下，所有这些因素都在发挥作用，因为 eBPF 从内核中钩入并扩展到跨环境运行的应用程序和基础设施中。

eBPF 的强大功能主要在于其计算效率，因为它直接与 [Linux 内核](https://thenewstack.io/linux-kernel-5-10-introduces-static-calls-to-prevent-speculative-execution-attacks/) 相关。然而，将 [eBPF 仅仅标记为基于 Linux](https://thenewstack.io/how-io_uring-and-ebpf-will-revolutionize-programming-in-linux/) 内核的工具具有误导性，因为它的影响遍布整个堆栈，影响到它所应用的应用程序。

eBPF 以多种方式被利用，并已成为众多成功的商业项目的基石。出于安全目的，它一直是推动力量。克服曾经阻碍 eBPF 采用的障碍为各种工具和平台铺平了道路，这些工具和平台不仅克服了这些挑战，还提高了安全性、可观察性、网络和其他应用程序的效率。

这在很大程度上是因为希望利用 eBPF 的公司或组织可能缺乏开发内部超大规模计算器或直接利用 eBPF 优势的专业知识。这就是 eBPF 工具提供商和平台提供商发挥作用的地方。他们的专业知识填补了空白，包括对 Linux（技术上是 Unix）的理解，以使用运行 eBPF 应用程序或设备所需的内核代码创建进程。此外，一些 [Linux 内核不支持 eBPF](https://thenewstack.io/how-ebpf-turns-linux-into-a-programmable-kernel/)，但工具提供商已解决了此限制。

由于可以通过单个 API 使用正确的工具正确管理策略，这意味着使用 eBPF 可以设置策略并更好地执行策略。使用 eBPF，策略的设置方式是，当事件发生时（例如攻击或在整个应用程序生命周期中违反策略时），可以发出不仅仅是警报和日志。

eBPF 的钩子深入而广泛，因此可以详细了解攻击或策略违规的严重性或其他信息。除了仅仅列出日志或发送警报之外，还可以提供有关问题的确切信息。

正如 [Liz Rice](https://uk.linkedin.com/in/lizrice)，[Isovalent](https://thenewstack.io/ciscos-strategic-move-in-the-isovalent-acquisition-ebpf/) 的首席开源官，在她的书中所描述的，[学习 eBPF：为增强可观察性、网络和安全性编程 Linux 内核](https://www.oreilly.com/library/view/learning-ebpf/9781098135119/) 中，使用 eBPF 进行策略设置的功能涉及定义什么行为是预期的，什么行为不是预期的（这包括检测到可疑错误路径时），以及在检测到异常时进行识别。但正如 Rice 所写，eBPF 的作用还远远不止这些：“调查人员获得的上下文信息越多，他们就越有可能找出事件的根本原因，并确定它是否是一次攻击，哪些组件受到影响，攻击是如何以及何时发生的，以及谁是责任人。”

![](https://cdn.thenewstack.io/media/2024/04/5cf08b1c-capture-decran-2024-04-18-201017-1024x399.png)

在 [Kubernetes](https://thenewstack.io/kubernetes/) 上为[微服务](https://thenewstack.io/microservices/)设置和执行策略是一个动态目标，因为 Kubernetes 是无状态且高度分布式的。在 KubeCon + CloudNativeCon 期间，在[我可以创建多少网络策略](https://kccnceu2024.sched.com/event/1YeMI/how-many-network-policies-can-i-create-nadia-pinaeva-red-hat-shaun-crampton-tigera)的演讲中，[Shaun Crampton](https://uk.linkedin.com/in/shaun-crampton-88633323)，[开源 Calico](https://www.tigera.io/project-calico/) 创建者 [Tigera](https://www.tigera.io/) 的杰出工程师，[Nadia Pinaeva](https://de.linkedin.com/in/npinaeva)，[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的高级软件工程师，表示云原生的网络策略可以描述为确保网络安全的 Kubernetes API。Pinaeva 说，它的结构非常简单，只有一个允许来自具有项目名称 my project 的特定命名空间的连接的入站规则。Pinaeva 说：“它的作用是允许您为一组特定的 pod 指定应该允许的连接，然后所有其他连接都将被拒绝。这是一个您可以看到的简单示例。”“这是一个在默认命名空间中创建的网络策略，它隔离了该命名空间中的所有 pod。”

从非常基础的层面来说，如果攻击者成功地重新配置了一个应用程序，使其写入到一个不同的位置，那么就会发出该警报。而且，这可能会发生，它应该在任何地方发生。因此，从策略执行的角度来看，这个方面涉及安全性，但我认为这也是可观察性，因为它提供了更多关于基于对应或不对应的设置而发生的问题的可见性。

触发事件的是确定是否满足或违反了从单个 API 设置的策略。当它被违反时，会发出警报，其中提供的信息不仅仅是一个基本的安全性工具。因此，有人可能会认为它也包含可观察性、安全性以及网络。在任何情况下，在 KubeCon+CloudNativeCon 期间，有人探讨了这个主题并展示了这一趋势如何展开。

在[CalicoCon](https://www.tigera.io/lp/calicocon-2024/)期间，这是在附近的 KubeCon + CloudNativeCon Europe 2024 期间举行的联合活动，[Jeremy Guerrand](https://ie.linkedin.com/in/j%C3%A9r%C3%A9my-guerrand-b0a74193)，Tigera 的解决方案架构师，Tigera 是开源 Calico 数据平面的领先开发商，发表了题为 [“最佳实践：使用 Calico 策略保护 Kubernetes 流量”](https://www.tigera.io/lp/calicocon-2024/#) 的演讲。他指出了 eBPF 在帮助 Calico 广泛部署以设置 Kubernetes 的网络策略中所扮演的角色。在这次演讲中，他说在“多集群、基于区域的架构”中的传统方法缺乏可见性，因此缺乏可观察性。他说，它们给出了过于宽泛的 IP 范围允许，导致了更大的攻击面。使用 Calico 策略，您可以在 Kubernetes 中定义、测试和强制执行吊舱和服务之间的严格流量规则。他说，它提供了对入站和出站流量的详细控制，有效地隔离了工作负载，增强了网络性能，并确保了符合各种安全标准。

这并不是说将 Calico 应用于解决策略设置和维护不需要大量的实践和诀窍，eBPF 功能可以简洁地描述。Guerrand 说，使用 Calico 时，它不使用标准 eBPF 钩子，而是使用可编程跟踪点和其他方式“通过创建 YAML 跟踪策略来完成这项工作”。

![](https://cdn.thenewstack.io/media/2024/04/83a63aff-capture-decran-2024-04-18-200440-1024x393.png)

在 Crampton 的演讲中展示的演示中，他在 GCP 中设置了一个集群，以便 [kube-burner](https://github.com/kube-burner/kube-burner)，一个 Kubernetes 性能和规模测试编排框架，支持任意 Kubernetes 集群，而“不以任何方式绑定到 OpenShift”。他在 Calico 中启用了 Prometheus 指标，并使用 Grafana 和 OpenSearch 提供了持久的结果服务器。当然，还使用了 Pinaeva 的包含 Calico 贡献的 YAML 文件的存储库。

![](https://cdn.thenewstack.io/media/2024/04/936f41a1-capture-decran-2024-04-18-200650-1024x531.png)

在她的演讲中，Pinaeva 展示了网络策略规模配置文件，在本例中它有七个参数。虽然适用于演讲中展示的演示，但她的评论也可以用来描述使用 eBPF 进行策略（以 Calico 为主要工具）的总体情况。“这定义了网络策略 YAML 的样子，这足以了解给定的网络策略的规模影响，”Pinaeva 说。“现在我希望在这一点上很明显，对于我可以创建多少网络策略，没有单一的或简单的答案。”
