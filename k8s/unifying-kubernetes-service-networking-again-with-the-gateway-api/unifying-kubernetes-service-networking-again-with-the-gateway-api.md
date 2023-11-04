<!--
# 使用Gateway API统一Kubernetes服务网络(再次)
https://cdn.thenewstack.io/media/2021/04/32d3b255-gate-229024_1280-1024x768.jpg

 -->

凭借明确定义的一致性和分层API模型，Gateway API已经展现出许多前景和长远发展的可能。

译自 [Unifying Kubernetes Service Networking (Again) with the Gateway API](https://thenewstack.io/unifying-kubernetes-service-networking-again-with-the-gateway-api/) 。

[Gateway API](https://gateway-api.sigs.k8s.io/)，先前被称为Services API，再之前被称为Ingress V2，首次在2019年圣迭戈的KubeCon大会上进行了[详细](https://www.youtube.com/watch?v=cduG0FrjdJA)的面对面讨论。Ingress和Kubernetes网络API已经存在许多众所周知的和[充分记录](https://dave.cheney.net/paste/ingress-is-dead-long-live-ingressroute.pdf)的局限性。[Gateway API](https://www.youtube.com/watch?v=GiFQNevrxYA)旨在重新设计这些API，建立在对Services、Ingress和服务网格社区的经验教训之上。

> [Kubernetes API 介绍视频(Bilibili)](https://www.bilibili.com/video/BV1294y157Cv/)

与一群Ingress和Service[控制器的实现者](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)聚在一起，我们提出了希望在Kubernetes网络API 2.0版本中拥有的特性:

* **可扩展性:** 我们承认滥用了注解。复杂的路由规则结构本不应该放在注解中，但我们还有什么选择吗？Gateway API通过灵活的一致性设计，要求100%支持核心特性。它要求端口性的可选扩展特性集，最重要的是，增加了许多独特自定义特性的扩展点。这使得端口性变得明确，不会约束特定供应商的功能。
* **API组合性:** 尽管它可能全部归结为单个代理配置，但多个用户(应用和基础设施方面)必须为其角色定义服务网络的不同部分。单一的Ingress资源根本无法提供所需的面向角色的设计。一个可组合的API(与单一庞大资源相比，更多可一起工作的API资源)也允许混合匹配资源，以推动持续渐进的发展。
* **表达能力:** Ingress的简单性(主机/路径路由和TLS)使可移植性变得容易，但它也是一个最低公分母，限制了Ingress。Gateway API提升了核心路由功能，具有流量分割、流量镜像、HTTP头操作等功能。这些核心和扩展功能使更多功能真正可在实现之间移植。
* **可移植性:** 这是我们不想改变的一件事。无所不在的服务负载均衡器和Ingress实现允许网络项目和产品生态系统的存在；这直接让用户的生活更轻松。最重要的是，Gateway API旨在使行业标准的网络语义在实现之间可移植。

一年多后，有几个Gateway控制器实现正在进行中，用户可以使用这些实现。这种实现之间的压倒性一致性证明了供应商和用户对服务网络改进的需求。

# 体验Gateway API

为了理解Gateway API如何实现这些目标，让我们介绍它的两个资源:

* **Gateways** 代表一个负载均衡器或任何通用的数据平面，用于监听它所路由的流量。你可以有多个网关，或者只使用一个可能在应用程序之间共享的网关。
* **Routes** 是应用于这些网关的路由配置。这些资源针对特定协议，所以有 HTTPRoutes、TCPRoutes、UDPRoutes 等。一个或多个路由可以绑定到一个网关；它们一起定义了由网关资源表示的底层数据平面的路由配置。

> [Kubernetes API 概念视频(Bilibili)](https://www.bilibili.com/video/BV1NC4y1J76E/)

一个gateway+route在某种程度上等同于一个 Ingress 资源。因为它们是两个资源，所以它允许基础设施团队拥有网关(并将策略和配置附加到其上)，而应用程序所有者拥有自己的路由。这允许这些组之间的较少直接协调和更多的开发者自治。

![](https://cdn.thenewstack.io/media/2021/04/4f966055-image1.png)

## 面向角色和多租户设计

如果将这个概念进一步发挥，它还允许许多团队共享同一个网关。网关提供了它们与路由绑定的内置控制，甚至跨命名空间边界。这使管理员能够控制应用程序面向客户端的暴露方式。下图显示了两个不同的团队在各自的命名空间中使用相同的负载均衡器(由网关资源建模)。

![](https://cdn.thenewstack.io/media/2021/04/a5a66bdf-image2.png)

这种安排允许应用程序所有者定义流量路由、流量加权、重定向或健康检查，因为这些属性与它们的应用程序紧密相关。基础设施所有者可能希望定义应用程序可以使用哪些负载均衡器，使用哪些 TLS 证书或哪些源 IP 允许连接，因为这些是与应用程序无关的平台级属性。关注点的分离在不同的组织之间可能有所不同，API 模型还提供了灵活性来匹配不同的所有权模型。

## 使用网关实现多集群网络

Gateway API的可扩展性还支持了以前不可能实现的新用例。上周发布的来自谷歌云的 [GKE 网关控制器](https://cloud.google.com/blog/products/containers-kubernetes/new-gke-gateway-controller-implements-kubernetes-gateway-api)允许 HTTPRoutes 引用不同集群中的服务。这为像[多集群高可用性](https://cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#external-gateway)或[蓝绿部署/多集群流量分裂](https://cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#blue-green_multi-cluster_traffic_splitting_with_an_internal_gateway)等多集群网络打开了新的大门。谷歌的网关控制器能够利用其全球网络进行此多集群负载均衡，在流量进入集群之前就做出路由决策。

## 前方的道路

虽然网关 API 已经展示了统一集群入口的承诺，但已经有使用网关和路由资源对基于 Sidecar 的服务网格和 TCP/UDP 负载均衡建模的提案。这将统一路由 API，这可能会降低新服务网格用户的入门门槛，并在第4层和第7层之间提供某种融合。

网关 API 的旅程还在起步阶段，还有大量的工作要做。得益于明确定义的一致性和分层 API 模型，网关 API 已经展示了巨大的前景和漫长的前进道路。

## 尝试使用和参与

有许多资源可以查看以获取更多信息:

* 查看用户指南以了解可以解决哪些用例。
* 在谷歌云博客上了解 [Google Kubernetes Engine Gateway controller](https://cloud.google.com/blog/products/containers-kubernetes/new-gke-gateway-controller-implements-kubernetes-gateway-api)。
* 在“与谷歌一起学习 Kubernetes”视频系列中找到更多关于网关 API 的内容。
* 尝试现有的网关控制器之一。
* 或者[参与进来](https://gateway-api.sigs.k8s.io/contributing/community/)帮助设计和影响 Kubernetes 服务网络的未来!