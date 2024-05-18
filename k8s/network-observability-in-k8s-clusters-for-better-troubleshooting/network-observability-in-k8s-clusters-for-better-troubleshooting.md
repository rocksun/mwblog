
<!--
title: 在K8s中实施网络可观测性以实现更好的故障排除
cover: https://cdn.thenewstack.io/media/2024/05/1da65b7c-observe.jpg
-->

Calico 赋能 DevOps 和平台团队，为其容器和 Kubernetes 环境实现可观测性和高效调试。

> 译自 [Network Observability in K8s Clusters for Better Troubleshooting](https://thenewstack.io/network-observability-in-k8s-clusters-for-better-troubleshooting/)，作者 Dhiraj Sehgal。

对于使用容器和 Kubernetes 的 DevOps 和平台团队来说，减少停机时间和改善安全态势至关重要。在云原生应用程序中，需要清楚地了解网络拓扑、服务交互和工作负载依赖关系。这对于[保护和优化 Kubernetes 部署](https://thenewstack.io/build-deploy-runtime-the-3-stages-of-kubernetes-security/)以及在发生故障时最大程度地减少响应时间至关重要。

[网络](https://thenewstack.io/networking/)可观测性可以突出显示需要网络策略控制的应用程序的网络策略中的差距，从而降低因不安全的出口访问或 Kubernetes 集群内威胁的横向移动而受到攻击的风险。然而，由于 [Kubernetes 工作负载](https://roadmap.sh/kubernetes)的分布式和动态特性，可视化工作负载通信、服务依赖关系以及活动和非活动网络安全策略带来了重大挑战。

## 使用 K8s 工作负载进行网络可观测性很困难

Kubernetes 会根据实时业务需求扩展和缩减 Pod，并创建和销毁服务，从而为每个工作负载实例创建动态网络连接。为每个工作负载定义的网络访问策略会进一步影响这些连接。

在这种情况下，很难捕获准确且最新的网络流量、服务依赖关系和网络策略的表示。默认的 [Kubernetes 实现提供了有限的网络流量可见性](https://thenewstack.io/how-kubernetes-provides-networking-and-storage-to-applications/)和策略信息，这使得团队难以对连接问题进行故障排除、提高安全性并证明合规性。

## 通用可观测性工具的局限性

DevOps 和平台团队通常依赖通用可观测性工具来深入了解工作负载通信和网络策略。

### 用于安全通信的网络可观测性

在安全性方面，DevOps 和平台团队经常报告说，通用可观测性解决方案无法有效地监控工作负载之间的通信以及进出集群的通信。

**[Kubernetes 网络和安全策略](https://thenewstack.io/the-kubernetes-network-security-effect/)** 确定了集群中的访问权限。将这些策略实时映射到 Kubernetes 集群中的流量对于理解部署的行为至关重要。

由于 Kubernetes 的动态和短暂特性，传统的监控工具无法映射可以随应用程序扩展的策略和流。这给在运行时开发、实施和验证有效的网络策略带来了挑战。

### 数据聚合和关联

Kubernetes 创建了大量临时对象，这些对象会在分布式环境中生成数据。需要聚合和关联这些数据才能可视化环境中的交互和活动。此外，必须将 Kubernetes 上下文（如 Pod、服务和命名空间）添加到数据中，这需要时间以及额外的计算、内存和存储等资源。

### Kubernetes 上下文

Kubernetes 在主机和 VM 之上添加了一层抽象。虽然收集和聚合来自各个容器和主机的很重要，但必须在不同级别的 Kubernetes 抽象中关联和聚合数据。

![](https://cdn.thenewstack.io/media/2024/05/d6733046-image1-1024x382.png)

大多数通用可观测性工具会从 Kubernetes 集群导出数据，并使用大量的计算资源来聚合和关联这些数据。这既昂贵又限制了功能。对于 Kubernetes 网络可观测性来说，至关重要的是**[可观测性工具是 Kubernetes 的原生工具](https://thenewstack.io/kubernetes-observability-challenges-in-cloud-native-architecture/)**，并且在集群内部运行。

## Kubernetes 原生网络可观测性

Kubernetes 的默认设置对可见性和策略信息提供了受限的见解，通常要求用户从多个来源编译数据才能获得全面的视图。

通常，人们会执行各种 kubectl 命令来收集 Kubernetes 栈中的孤岛信息。例如，运行 `kubectl get pods` 有助于获取群集中正在运行的所有 pod 的列表，而 `kubectl get networkpolicies` 则显示定义的所有 NetworkPolicy 资源。在分布式 Kubernetes 环境中，使用 kubectl 命令获得对流量和策略的可见性明显麻烦且效率低下。

此外，可以借助 Prometheus 和 Grafana 等开源监控工具，来实现对基础架构指标（如网络流和 DNS 日志）的可见性，这些工具有助于跟踪加密和未加密数据。

通用监控解决方案通常在节点、容器或 pod 级别收集指标，这会导致形成孤立的数据孤岛。然后，这些孤岛需要在应用程序和微服务层级进行复杂的聚合和关联，才能有效监控问题（如应用程序行为、性能瓶颈和通信问题），并对它们进行故障排除。由于动态 Kubernetes 基础架构内的交互具有瞬态特性，并且会生成大量细化数据，因此，使用此方法的团队难以实现扩展。

用于更详细分析的第三方监控工具（如 Datadog、Dynatrace 和 Splunk）通常用于收集日志和指标，并构建全面的仪表板。此外，使用托管服务提供商提供的预构建仪表板，可以提供一种简化的方法，用于跟踪和分析统计数据，促进在 Kubernetes 环境中的更好的运营监督和战略规划。

## Kubernetes 网络可观测性与 Calico

Calico Cloud 为 Kubernetes 环境提供 Kubernetes 原生的、专门构建的可观测性和故障排除功能，增强了快速解决连接性问题、加强安全态势和实时了解网络拓扑的能力。

### 网络指标

Calico 能够通过堆栈自动收集 Kubernetes 集群中各种活动所产生的日志，例如 DNS 流、应用程序流、微服务信息、Kubernetes 活动、审计日志、网络流、TCP/UDP 状态、套接字统计信息和进程信息。它还会记录群集中应用的各种网络策略数据，例如应用程序级别、网络级别和 DNS 策略。Calico 在源头上整合这些数据点，这样便可以得到 Kubernetes 特定的元数据，而无需任何额外的配置，从而节省了时间和精力，同时还节约了内存、计算和网络带宽等资源。

![](https://cdn.thenewstack.io/media/2024/05/ceb2051f-image4.png)

### 可视化

Calico Cloud 提供了一个详细的仪表盘，用于轻松监控流量和网络策略，并使用动态服务威胁图对网络和网络安全问题进行故障排除。它还提供自定义仪表盘，例如 DNS 仪表盘，用于深入了解应用程序网络和安全性。此外，Calico 具有高级日志管理功能，包括自动筛选和预构建选项卡，以简化故障排除并执行更快的根本原因分析。Calico 提供了一个直接的过程来识别有问题的负载并快速访问相关日志，从而极大地简化了故障排除过程。

![](https://cdn.thenewstack.io/media/2024/05/955d58dd-image5.png)

对于寻求更深入分析（例如 DNS 分析）的用户，Calico 与 Kibana 的内置集成允许创建详细的自定义查询，以满足更高级的需求。

![](https://cdn.thenewstack.io/media/2024/05/2ba680cf-image2.png)

### 故障排除工具

Calico 提供了对网络连接问题进行故障排除的工具。考虑仪表盘警报识别出通信中断或策略拒绝流量的情况。在下图中，DevOps 和平台工程师只需点击几下即可解决“default”pod 无法与 kube-system 通信的原因。用户导航到服务图，右键单击 pod，启用具有特定时间戳和协议的数据包捕获，并捕获所有流量以进行根本原因分析。捕获的数据已经过聚合和关联，并指向故障的特定配置、依赖项或策略。通过选择受影响的工作负载，用户可以立即看到导致网络故障的原因，包括导致问题的网络策略。

![](https://cdn.thenewstack.io/media/2024/05/3685d144-image3.png)

### 使用 Calico 的好处

- **更快的故障排除**：通过提供应用程序流量和关联数据的实时视图，Calico 使 DevOps 团队能够快速缩小故障排除范围，从错误配置的网络策略到网络性能问题。这种简化的方式使团队能够有效地解决安全漏洞和工作负载通信问题，从而减少停机时间并提高运营效率。
- **改进的安全态势**：DevOps 团队现在可以使用 Calico 精确找出安全漏洞并解决缺乏细化工作负载访问控制的问题。借助基于活动的可视化和详细的流量元数据，Calico 使团队能够在执行之前预览和推荐策略。这增强了应用程序的安全态势并有效地降低了风险。

## 结论

Calico 赋能 DevOps 和平台团队，让他们能够实现可观测性，并对容器和 Kubernetes 环境进行高效故障排除。通过提供一个专门构建的解决方案来解决当前方法的局限性，Calico 使团队能够减少停机时间、改善安全态势并提高运营效率。借助 Calico，DevOps 和平台团队可以自信地驾驭容器和 Kubernetes 环境的复杂性，并安心地推动创新。
