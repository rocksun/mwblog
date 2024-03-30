
<!--
title: 使用Microsoft的Retina监控Kubernetes网络
cover: https://images.techhive.com/images/article/2016/11/ethernet_cables-100694419-large.jpg?auto=webp&quality=85,70
-->

开源 Retina 使用 eBPF 为 Kubernetes 中的容器网络带来可观测性。

> 译自 [Using Microsoft’s Retina to monitor Kubernetes networks](https://www.infoworld.com/article/3714683/using-microsoft-s-retina-to-monitor-kubernetes-networks.html)，作者 Simon Bisson。


## Kubernetes 在 Microsoft 中的角色

[Kubernetes](https://www.infoworld.com/article/3268073/what-is-kubernetes-your-next-application-platform.html) 在 Microsoft 扮演着重要的角色。容器管理系统是该公司众多云服务的基础部分，从 Microsoft 365 和 Xbox 到 Azure，再到使用 Microsoft 的 Kubernetes 托管其自身服务的合作伙伴 OpenAI。

因此，Microsoft 发明了许多其 [自有的 Kubernetes 管理工具](https://www.infoworld.com/article/3714767/building-a-smarter-azure-kubernetes-for-developers.html)。其中包括用于部署 AI 推理工作负载的 [Kaito](https://github.com/Azure/kaito) 和用于大规模管理 Kubernetes 集群的 [Fleet](https://learn.microsoft.com/en-us/azure/kubernetes-fleet/overview)。Microsoft 的所有各种工具都位于其两项托管 Kubernetes 服务（Azure Kubernetes 服务和 Azure 容器服务）之下，让你能够部署和编排基于容器的应用程序，而无需构建必要的管理框架。所有这些都是免费提供的，包括 API、门户和命令行界面。

在过去，这将是全部。Microsoft 会使用这些功能来让自己区别于其竞争对手及其 Kubernetes 云。但 Microsoft 已经将 [开源模型](https://www.infoworld.com/article/3429076/what-is-open-source-software-open-source-and-foss-explained.html) 铭记于心，其 Kubernetes 计划的许多领导者都来自开源背景。Microsoft 并未将 Kubernetes 工具据为己有，而是将它们作为开源项目发布，任何人都可以使用它们，任何人都可以贡献新代码。

## 引入 Retina 可观测性平台

成为 [开源项目](https://azure.microsoft.com/en-us/blog/microsoft-open-sources-retina-a-cloud-native-container-networking-observability-platform/) 的最新 Azure 工具之一的是 Retina，这是一种网络可观测性工具，旨在帮助你了解所有集群中的网络流量，无论它们如何配置或使用什么操作系统。它也不依赖于 Azure 功能。你可以在任何 Kubernetes 实例中运行 Retina，无论是在本地还是在 AWS、Azure 或 GCP 中。

Retina 的核心，[与 Falco 安全工具](https://www.infoworld.com/article/3714269/securing-azure-kubernetes-with-falco.html) 非常相似，是 [扩展 Berkeley 数据包过滤器 (eBPF)](https://ebpf.io/)。这些过滤器让你可以在主机操作系统的内核中运行代码，在应用程序容器之外，因此你可以使用 eBPF 探针而不会显著影响你正在运行的代码。无需向容器添加代理或向代码添加监控库，一个 eBPF 探针可以监控在主机上运行的所有节点，无论它是云虚拟机还是本地物理硬件。

在内核中运行 Retina 探针简化了网络监控。你无需知道主机服务器上安装了哪些网卡，或者 Kubernetes 安装如何使用服务网格。相反，你可以了解主机操作系统的网络堆栈如何处理数据包。你可以跟踪数据包类型、延迟和数据包丢失，利用低级别的 TCP/IP 功能，这些功能在较高层可能无法访问。

通过专注于使云原生网络可观测，Retina 被设计为可以融入任何监控工具集和任何 Kubernetes 安装。它同时支持 Linux 和 Windows，这应该有助于你监控和调试混合了 Linux 和 Windows 服务的混合应用程序。由于 eBPF 探针是代码，你可以将它们视为可自定义的插件，让 Retina 能够随着新的 Kubernetes 功能而演进，并支持你监控需求所需的指标。

数据以节点级别传递到熟悉的 Prometheus 日志记录服务。收集的数据包括 DNS、第 4 层操作和数据包捕获。由于数据已标记，因此你可以在 Kubernetes 环境中构建操作映射，帮助跟踪问题，例如阻止微服务，因为 Retina 会记录 Kubernetes 实例中及周围的流模式。

## 开始使用 Retina

首先 [克隆 Retina GitHub 存储库](https://github.com/microsoft/retina)，然后使用捆绑的 Helm Chart 进行安装。你可能还需要配置 Prometheus，以确保 Retina 正在记录数据。如果你想 [使用 Retina CLI](https://retina.sh/docs/installation/cli/)，则需要在 Linux 托管的 Kubernetes 上运行。CLI 在 kubectl 中运行，因此可以轻松与其他 Kubernetes CLI 工具一起使用。或者，你可以使用 YAML 自定义资源定义来配置和运行网络捕获。

在 Linux 上，eBPF 网络捕获插件是开源 Inspektor Gadget 工具的一个版本。它最初由 Kinvolk 团队开发，现在是 Azure 的一部分，仍然专注于容器工程。[Inspektor Gadget](https://www.inspektor-gadget.io/) 是一个 Kubernetes eBPF 工具库，适用于任何规模的 Kubernetes 应用程序，从单个节点到大型集群。Retina 使用 Inspektor Gadget 跟踪小工具来观察网络系统事件。

## 观测容器网络

[Retina 网站](https://retina.sh/) 提供了使用该工具的详细说明。[Retina 提供三种不同的操作模式](https://retina.sh/docs/metrics/modes/)：按节点级别划分的基本指标，支持按源和目标 Pod 聚合的更详细的“远程上下文”指标以及允许您选择要监视哪些 Pod 的“本地上下文”选项。

需要注意的是，您默认情况下看不到所有内容，因为这可能会让人不知所措。相反，不同的指标由不同的插件启用。例如，如果您想跟踪 DNS 调用，请首先启用 DNS 插件。所有指标都包括集群和实例元数据，因此您可以使用标签进行筛选和报告，以识别特定的目标节点和 Pod。本地和远程上下文选项添加了跟踪源和目标的标签。

配置 Retina 还需要 [设置 Prometheus 目标](https://retina.sh/docs/installation/prometheus-unmanaged) 以获取数据，以及适当的 Grafana 仪表板。Microsoft 在 Retina 存储库中为 GitHub 上的这两者提供了示例配置。默认情况下会显示集群和 DNS 数据。将数据放在 Prometheus 中允许您使用其他工具处理 Retina 数据，例如将数据馈送到策略引擎以触发警报或自动执行特定操作。

在安装了 Retina 并配置了 Prometheus 和 Grafana 之后，您现在可以超越默认设置，通过 YAML 配置 Retina 代理和插件。其他指标配置通过 Kubernetes 自定义资源定义进行。

## 测量 Kubernetes 网络操作

Retina 并不是真正用于在数据包级别进行持续监视的工具，因为它会在繁忙的集群中生成大量数据，当然除非您使用基于策略的工具来识别正常操作的异常情况。在实践中，最好使用 Retina 来 [识别根本原因](https://www.infoworld.com/article/3714761/4-steps-to-improve-root-cause-analysis.html) 正在运行的集群出现的问题。也许节点无法相互通信，或者您怀疑错误可能是由于特定服务交互中的延迟造成的。在这里，您可以使用单个命令触发所需的包捕获，该命令将收集您运行诊断所需的所有数据。

持续操作通过指标报告，这些指标为您提供有关关键网络问题的统计信息。可以使用 Prometheus 管理这些指标以生成警报，并使用 Grafana 仪表板为您提供集群整体性能的概述，以及来自其他可观测性工具的数据。

Retina 提供的一个有用的指标是经常被忽略的指标：API 延迟。但是，在云原生开发中，您经常使用第三方 API。有些可能是云提供商的平台服务，而另一些可能是必不可少的业务数据源，例如 Salesforce 或 SAP Hana。在这里，您可以使用 Retina 的 API 服务器延迟来获取有助于跟踪服务器响应时间的指标。

拥有这些数据可以让您开始与 API 提供商进行诊断过程，帮助追踪任何延迟的来源。API 访问延迟可能是您的应用程序中的一个重大障碍，因此拥有这些数据可以帮助您提供更可靠、响应更快的应用程序。

### Kubernetes 生态系统的成熟

Microsoft 已发布基于 Retina 的可观测性工具的预览版本，[可用于 Azure Kubernetes 服务作为网络可观测性加载项](https://learn.microsoft.com/en-us/azure/aks/network-observability-overview)。这适用于 Azure 托管的 Prometheus 和 Grafana。您可以在其文档中找到预配置指标的列表，但它目前仅提供 Retina 功能的一个子集，仅提供节点级指标。

使用 Retina 时要考虑的一个关键点是，它建立在 Azure 在 Kubernetes 方面的经验之上。开箱即用的捕获指标是 Azure 团队认为重要的指标，并且您正在利用支持世界上最大、最活跃的 Kubernetes 环境之一的知识。如果您需要其他指标，您可以为 Retina 构建自己的 eBPF 探针，然后可以与更广泛的 Kubernetes 社区共享。
开源需要共享专业知识才能取得成功。通过开放代码库，Microsoft 鼓励 Retina 开发人员将他们的知识带到平台，并希望 AWS、GCP 和其他大规模 Kubernetes 运营商与世界分享他们学到的网络知识。随着 Kubernetes 的成熟，基于 eBPF 的工具（如 Retina 和 Falco）将变得越来越重要，提供我们大规模交付安全可靠的云原生应用程序所需的数据。
