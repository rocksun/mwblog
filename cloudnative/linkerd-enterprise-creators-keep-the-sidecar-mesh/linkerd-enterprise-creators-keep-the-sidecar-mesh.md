<!-- 
# Linkerd企业版创始人: 坚持使用sidecar服务网格

https://cdn.thenewstack.io/media/2023/10/84e59b2d-domino-bc3kjwxqu-e-unsplash-e1698754303947-1024x683.jpg

-->

Buoyant 推出了 Linkerd 的企业版，其中包含用于在 Kubernetes 集群内实现零信任安全以及用于成本优化等的安全工具。

译自 [Linkerd Enterprise Creators: Keep the Sidecar Mesh](https://thenewstack.io/linkerd-enterprise-creators-keep-the-sidecar-mesh/) 。

Buoyant 推出了 [Linkerd](https://thenewstack.io/linkerd-service-mesh-update-addresses-more-demanding-user-base/) 的首个企业版，Linkerd 是一款以轻量和易用闻名的流行[服务网格](https://thenewstack.io/service-mesh/)，适用于小型和大型组织。在此次发布中，Linkerd 继续采用[服务网格 sidecar](https://thenewstack.io/can-you-now-safely-remove-the-service-mesh-sidecar/)，这与 Linkerd 的创始人和 [Buoyant](https://buoyant.io/) 的创始人兼 CEO [William Morgan](https://www.linkedin.com/in/wmorgan/) 的主张一致。Linkerd 的开源方式以及企业版的发布，与其他开源项目创始人(如 HashiCorp)的选择形成对比，后者更倾向于将之前的开源代码闭源。但 Linkerd 仍致力于开源，正如 Morgan 所言。

Linkerd 企业版引入了潜在企业客户高度需求的特定功能。这些仅限企业版的新增功能包括基于 Linkerd 开源安全层的 Kubernetes 集群内实现零信任安全的工具。观测提供商 [Mezmo](https://urldefense.proofpoint.com/v2/url?u=https-3A__www.mezmo.com_&d=DwMFAg&c=euGZstcaTDllvimEN8b7jXrwqOf-v5A_CdpgnVfiiMM&r=rnNE9zoYZMR831eYqAxS1YEqGvEtKWyVSKXHRVHTcTc&m=zdPtVy6OEi_byNAEuDLkPSmTfzQ2ErAEoUC_r7jFKKz6DpsqlThCsAYiHanFLX4K&s=udTMvdOCjWDTSIIhqsLUrzsy6LmeGFxooe4ZuVFsEd8&e=) 和支付网络提供商 [TrueLayer](https://urldefense.proofpoint.com/v2/url?u=https-3A__truelayer.com_&d=DwMFAg&c=euGZstcaTDllvimEN8b7jXrwqOf-v5A_CdpgnVfiiMM&r=rnNE9zoYZMR831eYqAxS1YEqGvEtKWyVSKXHRVHTcTc&m=zdPtVy6OEi_byNAEuDLkPSmTfzQ2ErAEoUC_r7jFKKz6DpsqlThCsAYiHanFLX4K&s=0DHGPAbCeFLpipiWqncBsLXqz5-vW88GdoaxpLj3ko4&e=) 是早期采用者。

该版本还强调成本优化，通过自动流量控制负载均衡器实现资源管理，以降低成本。通过将端点细分为成本层，以及根据 HTTP 和 gRPC 请求路由到适当区域，Linkerd 企业版可在正常条件下将流量转移到最低成本区域，仅在系统压力大时从高成本区域添加端点。这种支持覆盖跨集群流量，使拥有多个区域跨集群复杂拓扑的企业可显著降低云端支出。此外，它解决了合规性和维护问题，以便在必要时(控制面和数据面)进行安装、升级和回滚，借助 Linkerd 企业版的生命周期自动化功能。

![](https://cdn.thenewstack.io/media/2023/10/487fecf0-capture-decran-2023-10-25-173907.png)

*Linkerd 企业版可用于停用昂贵的应用负载均衡器和减少跨区域网络支出，其创始人表示。*

尽管 Linkerd 与其他服务网格在核心功能上提供 Kubernetes 集群的全面控制具有共性，但其简单性和效率使其成为热门选择。如许多人所强调，拥有服务网格对管理云原生环境中的应用至关重要。Linkerd 用户之一微软已经认识到服务网格对其 Xbox 业务和服务的重要性。

## 是否采用 Sidecar

关于 eBPF 及其增强基于 Linux 内核运行的应用程序的数据监控能力的作用，也存在大量讨论。该技术直接在 Linux 内核内部运行，并扩展到不同环境。虽然其他服务网格(如 [Solo.io 的 Istio](https://thenewstack.io/solo-io-offers-an-enterprise-ready-istio-service-mesh-as-a-cloud-service/))已经[转向 eBPF 以提高速度](https://thenewstack.io/performant-and-programmable-telco-networking-with-ebpf/)和减少资源消耗，但 Morgan 对这种方法持怀疑态度。因此，Linkerd 无计划采用无 Sidecar 配置，特别是刚发布的企业版。因此，他声称通过此次发布，Linkerd 继续抵制利用 eBPF 作为 Sidecar 的普遍趋势。

Morgan 说，eBPF 可以帮助处理一个特定的网络领域，即在 L4 层处理 TCP 数据包。服务网格的大多数功能都是在 L7 层，而 eBPF 由于技术固有的局限无法处理。“所以，eBPF 对服务网格的效用最多也就是个工具。某个特定服务网格声称 eBPF 可提供无 Sidecar 网格纯属市场营销，因为 eBPF 可与 Sidecar 和每个主机代理一起使用，效用同样微乎其微”，Morgan说，“无 Sidecar 在此背景下意味着‘每个主机代理’，这在安全性和可靠性上都不如 Sidecar。这就是我们在 Linkerd 1.0 中抛弃它的原因。”

## 商业模式

Buoyant 出于 Linkerd 开源版本之上发布企业版，与某些高知名度的企业和组织形成对比，其中一些在通过开源项目获利方面遇到挑战。例如，HashiCorp 最近选择将其之前的开源代码(如 Vault)转为专有解决方案。然而，Linkerd 的创造者坚称对 Linkerd 开源项目的承诺与以前一样强烈。

同时，这个问题提出了如何从开源项目中获利的持续辩论的一个有趣方面，即使是非常流行的项目。一些人认为开源不应该成为商业模式的基础，在其之上添加额外的服务或企业版本。其他人主张开源项目应该将重点放在开发主要的专有产品或服务上，同时满足依赖开源项目的其他组织的需求。在这种背景下，Buoyant 选择提供扩展 Linkerd 功能的企业版。

“我认为现代开源世界与我成长过程中周末志愿军方法非常不同(这也是 Linux、Git 等项目的历史)，现代开源项目不是志愿者的工作，而是有商业利益的公司投资的项目 —— 这很好，因为 a) 维护者可以获得报酬并谋生，b) 项目不再依赖维护者的周末时间”，Morgan说。“对 Linkerd 用户来说，我确实认为我们可以提供两全其美的解决方案:一个具有健康和繁荣社区的世界级开源项目，以及一个解决企业环境特定和独特挑战的企业发行版本。”

然而，Linkerd 企业版提供了针对企业客户需求的特定功能。

尽管 Linkerd 在提供 Kubernetes 集群的全面控制方面与所有服务网格具有基本特征，但它以采用和管理的便捷性脱颖而出。许多观察者强调了在处理云原生环境中的应用程序时拥有服务网格的重要性。例如，Linkerd 开源用户微软已经认识到服务网格对其 Xbox 业务和服务提供的必要性。

在 2022 年底美国底特律举行的 KubeCon + CloudNativeCon 北美会议上，微软高级软件工程师 Christopher Voss 指出了 Linkerd 的高效资源利用率、流量分割、“大量指标”的可观测性和低延迟这些开箱即用的特性。

在微软为其 Xbox 服务尝试的所有服务网格原型中，Voss 说:“我不能说 Linkerd '获胜了'，但它更符合我们的需求。”

与此同时，许多组织正在努力整合服务网格到其运维中。是否可以接受小型和大型组织(如微软)或其他 Linkerd 用户(如 Adobe)在各种 Kubernetes 运行时环境中使用多种服务网格这一问题被提出。另一观点是在单一 API 的支持下集中运维，由跨越所有集群的统一服务网格提供支持。

“在技术层面，这不是非此即彼的选择，但在实践中，我们确实看到许多 Linkerd 用户是从“以 API 为中心”的方法迁移到服务网格的，主要是因为这种方法会导致“发夹”架构，其中内部组件之间的调用会通过公网 API 返回”，Morgan说。“这需要支付 ALB [应用负载均衡器] 和其他昂贵的云服务费用，当他们可以用网格取代这些服务时，会看到大量节省成本。”