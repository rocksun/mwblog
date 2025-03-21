# KubeFleet：多集群 Kubernetes 应用管理的未来

![KubeFleet：多集群 Kubernetes 应用管理的未来的特色图片](https://cdn.thenewstack.io/media/2025/03/92483285-cattle-1024x630.jpg)

如今的应用程序正变得越来越复杂，这受到了各行各业多样化和严苛的需求的驱动。电子商务网站需要处理大量数据，并在全球范围内提供流畅的购物体验。银行需要安全且始终可用的系统来服务客户。医疗保健应用程序必须保护患者信息并保证可靠性。游戏平台需要快速响应，以满足各地玩家的需求。媒体公司管理和流式传输大量内容，而电信供应商需要确保跨网络的可靠服务。物联网应用程序处理来自各个位置的众多设备的数据。

Kubernetes 处理大规模、复杂部署以及提供高可用性的能力使其成为这些现代应用程序的理想选择。在这个快速发展的环境中，跨多个 Kubernetes 集群管理和扩展应用程序已成为越来越普遍的做法，原因有很多。

**容错性**：在多个集群上运行应用程序自然会提高其容错能力。如果其中一个集群出现问题，其余集群将继续运行，从而最大限度地减少应用程序停机时间并保持服务可用性。我们观察到，许多组织都有内部策略，要求在多个集群上运行关键任务应用程序。

**性能**：对于拥有地理分布式客户群的组织来说，将应用程序放置在靠近客户的位置至关重要。因此，应用程序自然需要在多个集群或区域中运行。

**可扩展性**：某些应用程序需要大量资源才能运行（想想 ChatGPT），因此无法放入单个集群中。

多集群 Kubernetes 应用程序管理涉及跨多个集群编排和维护应用程序，以确保高可用性、性能和可扩展性。这种方法可以实现无缝更新、高效的资源利用和强大的灾难恢复，使其成为管理复杂、分布式应用程序的一种有吸引力的策略。

## 管理多集群应用程序的挑战

然而，随着组织越来越多地跨多个 Kubernetes 集群部署应用程序，它们也面临着严峻的挑战。在多个集群上管理应用程序自然会增加运营复杂性。以下是应用程序管理员需要为[部署在多个集群中](https://thenewstack.io/cluster-api-offers-a-way-to-manage-multiple-kubernetes-deployments/)的应用程序处理的一些额外事项。

**持续部署**：设置一个 CD 系统，以安全的方式升级应用程序。

**网络配置**：设置允许应用程序南北和东西向流量的网络配置。

**资源优化**：根据需求和集群/区域的资源限制，在每个单独的集群中向上和向下扩展应用程序。

**流量配置**：根据应用程序在每个集群中的部署规模，将流量分配到每个应用程序。

**部署策略**：根据资源利用率或容量，以降低风险的方式在集群/区域之间移动应用程序，而不会中断实时服务。如果需要，这还需要以无缝方式将流量与应用程序一起移动。

在多个集群上运行应用程序的复杂性需要高级解决方案，以确保容错性、性能、可扩展性和高效的资源利用。为了应对这些挑战，需要一个全面的框架来简化多集群应用程序管理。KubeFleet 是一个开源项目，它承诺通过重新定义多集群应用程序管理来应对这些挑战。

## 什么是 KubeFleet？

KubeFleet 是一种云原生多集群/多云解决方案，旨在[促进跨多个 Kubernetes 集群的应用程序的部署](https://thenewstack.io/cloud-native-deployments-bring-new-complexities-to-the-developer/)、管理和扩展。通过使用高级调度、资源优化和基于策略的管理，KubeFleet 旨在为平台运营商和应用程序所有者提供无缝且高效的体验。

## KubeFleet 解决的问题
**多集群部署**：KubeFleet 为应用程序管理员提供了一个[控制平面进行部署](https://thenewstack.io/how-a-flexible-control-plane-helps-deploy-apps-on-kubernetes/)，以便跨多个集群部署应用程序，其中包括找到最适合运行的集群以及控制每个集群上的副本数量。

**丰富的调度能力**：KubeFleet 支持许多 Kubernetes 调度操作，例如集群亲和性、拓扑分布以及首选与必需。它还引入了不同的多集群风格策略，例如选择 N 个集群（类似于 Deployment）或选择所有集群（类似于 DaemonSet）。

**基于指标的调度**：KubeFleet 还支持复杂的基于指标的放置策略，以确保根据各种指标将应用程序分配到最合适的集群，这些指标包括内部指标（GPU、CPU、内存和节点帐户）和外部/自定义指标（成本、IP 地址可用性和网络速度）。

**内置**：KubeFleet 具有内置的滚动更新策略，该策略与 Kubernetes deployment 非常相似。我们还引入了云原生阶段式 CD，在各个阶段之间具有等待和批准的[持续部署](https://thenewstack.io/ci-cd/)策略。

![KubeFleet CD process](https://cdn.thenewstack.io/media/2025/03/3fc552a8-image1a-3-1024x401.png)

加入 KubeFleet 社区

[KubeFleet](https://aka.ms/KubeFleet) 代表了 Kubernetes 社区中 Fleet 应用程序管理的重大进步。但是，我们更高兴的是，它现在是 CNCF 的一部分。我们正在寻找更多的云原生从业者参与到社区中，并帮助塑造多集群应用程序管理的未来，以确保未来的应用程序能够以高效、可靠的方式大规模部署。

*要了解有关 Kubernetes 和云原生生态系统的更多信息，请于 4 月 1 日至 4 日在伦敦加入我们的*[KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)*。*

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)