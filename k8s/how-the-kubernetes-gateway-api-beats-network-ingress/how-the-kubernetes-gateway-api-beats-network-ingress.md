<!--
title: Kubernetes Gateway API如何战胜Ingress
cover: https://cdn.thenewstack.io/media/2024/01/c5efc0ef-nginx_kccnc-na_k8s-gateway-api_featured-1024x576.png
-->

开源 Kubernetes Gateway API 的推出，提供了一个可以替代网络Ingress管理入站流量的方案。在 The New Stack Makers 的这一集里可以了解更多相关信息。

> 译自 [How the Kubernetes Gateway API Beats Network Ingress](https://thenewstack.io/how-the-kubernetes-gateway-api-beats-network-ingress/)，作者 Heather Joslyn 是 The New Stack 的主编，对于软件开发人员和工程师相关的管理和职业问题特别感兴趣。她以前担任 Container Solutions 的首席编辑，这是一家云原生咨询公司...

芝加哥 - 想要访问你的网络和平台的入境流量可能使用的是网络的Ingress。但Ingress带来了扩展性、可用性和[安全性](https://thenewstack.io/security/)方面的问题。

例如，[NGINX](https://www.nginx.com/?utm_content=inline-mention) 高级产品经理 [Mike Stefaniak](https://www.linkedin.com/in/mike-stefaniak-8328a6249/?trk=public_profile_browsemap) 在本期 The New Stack 制造者播客节目中说，一旦你有几个团队在同一个 [Kubernetes](https://thenewstack.io/kubernetes/) 集群中的同一个Ingress上工作，"那就涉及到同一资源的许多手。这可能会在团队之间造成很多摩擦。

我确实见过，我们做了一次更新，最终以某种方式改变了它，导致现在没有流量可以进入了。哎呀，全员出动，我们遇到[一个事故](https://thenewstack.io/how-we-manage-incident-response-at-honeycomb/)了。"

网络Ingress有点像一把钝器，Stefaniak 和 NGINX 软件工程师 [Kate Osborn](https://www.nginx.com/people/kate-osborn/) 在本期 TNS 制造者节目中建议，该节目在 KubeCon + CloudNative Con 北美洲之旅中录制。

"最大的问题之一是它不可扩展，"Osborn说:"所以这是一个非常简单的资源。但是有大量复杂的路由人们想要做。为了做到这一点，他们不得不添加自定义注释。"

10月推出通用可用性的开源 [Kubernetes Gateway API](https://thenewstack.io/kubernetes-api-gateway-1-0-goes-live-as-maintainers-plan-for-the-future/) 为入站流量提供了网络Ingress的替代方案。NGINX 也推出了 [NGINX Gateway Fabric](https://github.com/nginxinc/nginx-gateway-fabric)，它为 [Kubernetes Gateway API](https://kubernetes.io/blog/2023/10/31/gateway-api-ga/) 提供了一个实现，使用 NGINX 作为数据平面。

## 可扩展性和安全性

四年前在 KubeCon 首次提出，Kubernetes Gateway API 1.0 版本相比网络Ingress具有优势。

首先，Osborn 说: "它是可扩展的。在多个网关 API 资源上的多个点上，您可以引用策略，这是一个[自定义资源定义]，这样您实际上可以得到您从注释中得不到的漂亮验证，不同的实现可以创建自己的策略。您可以在那里附加它们以使其可扩展。"

此外，每个资源都有一个相关角色，避免了 Stefaniak 提到的“同一资源的多个手”的问题。

正如 Osborn 澄清的那样:"您可以真正干净地应用[[基于角色的访问控制](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/)]策略，这使其更安全，并允许您控制您关心的内容，而不会影响可能共享基础设施的任何其他人。"

随着开发人员开始采用 Kubernetes Gateway API，Stefaniak 说他预计早期用例将是全新领域，因为网络Ingress使用非常普遍。

“Ingress 已经存在很长时间了，可能还会存在很长时间，”他说。“因为今天使用它的公司具有大量功能，大量成熟性。”

尽管如此，Osborn说: "[网关有一个独特的机会](https://thenewstack.io/kubernetes-gateway-api-nixes-future-beta-releases/)来统一南北流量和东西流量。网关组中有一个 [GAMMA 计划](https://gateway-api.sigs.k8s.io/mesh/)正致力于这一点 - 能够包含进出集群的所有类型的流量。用一个单一的、非常表达性的、面向角色的 API 来做这一点会非常酷。这里有很多可能性。"

请查看整个剧集以了解有关 Kubernetes Gateway API 的更多信息。并[与社区联系](https://gateway-api.sigs.k8s.io/contributing/)以帮助构建下一个版本。
