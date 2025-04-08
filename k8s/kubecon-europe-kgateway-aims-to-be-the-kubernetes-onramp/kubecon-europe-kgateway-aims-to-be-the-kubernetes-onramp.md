
<!--
title: Kgateway旨在成为Kubernetes的入口
cover: https://cdn.thenewstack.io/media/2025/04/de9b2a5c-soloio-kubecon.jpg
summary: KubeCon爆款预定！开源Kgateway基于Envoy proxy和Kubernetes Gateway API，化身云原生Ingress控制器和AI网关！简化南北/东西向流量管理，无缝集成Istio Ambient mesh，赋能LLM应用，安全又高效！
-->

KubeCon爆款预定！开源Kgateway基于Envoy proxy和Kubernetes Gateway API，化身云原生Ingress控制器和AI网关！简化南北/东西向流量管理，无缝集成Istio Ambient mesh，赋能LLM应用，安全又高效！

> 译自：[KubeCon Europe: Kgateway Aims To Be the Kubernetes Onramp](https://thenewstack.io/kubecon-europe-kgateway-aims-to-be-the-kubernetes-onramp/)
> 
> 作者：Joab Jackson

本周在伦敦举行的 [KubeCon + CloudNativeCon EU](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/) 大会上，Kubernetes 网络管理员应该去 [Solo.io 的 S150 展位](https://x.com/soloio_inc/status/1907379381896372553) 了解一个名为 kgateway 的开源 Kubernetes API 网关实现，它可以[简化](https://www.solo.io/blog/donating-gloo-gateway-to-the-cncf-introducing-kgateway-and-advancing-cloud-connectivity) 将流量移入和移出集群的管理。

开源 [kgateway](https://kgateway.dev/) 构建于 [Envoy proxy](https://www.envoyproxy.io/docs/envoy/latest/intro/what_is_envoy) 和 [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/) 之上，是一个 Kubernetes 原生的 Ingress 控制器和下一代 API 网关。

该网关由云原生连接公司 [Solo.io](https://www.solo.io/company/about-us) 构建，之前的名称为 [Gloo Gateway](https://thenewstack.io/with-gloo-enterprise-1-0-solo-io-builds-the-stepping-stones-to-service-mesh/)。

在去年举行的 KubeCon + CloudNativeCon North America 2024 大会上，该公司宣布将把该软件捐赠给 [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) (CNCF)，并将该软件的名称更改为 kgateway。

今年 3 月，CNCF [接受](https://www.cncf.io/reports/etcd-project-journey-report/) kgateway 作为一个沙箱项目，这是早期阶段云原生软件项目的入口点。

通过转移到厂商中立的治理模式，用户和贡献者不必担心该软件会被单个厂商捐赠。

[Gloo 开源存储库](https://github.com/solo-io/gloo) 最终会被弃用。

## Kubernetes Gateway API 的重要性

2023 年，[Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/) 实现了 [1.0 版本的正式发布](https://thenewstack.io/kubernetes-gateway-api-nixes-future-beta-releases/)。API 网关是一种规范，用于控制 Kubernetes 集群的流量进出，以及如何在 Pod 之间进行内部流量传输。

Kgateway 是 Kubernetes Gateway API 的完全一致性实现。该 API 是一种规范，用于路由流量，包括“第 4 层”控制平面和“第 7 层”数据平面。

它实际上是 [Envoy proxy](https://thenewstack.io/the-envoy-proxy-finds-a-home-at-the-cncf-amazon-web-services/) 的一个接口，Envoy proxy 管理 Kubernetes 集群的 L7 数据流量。然而，直接对 Envoy 进行编程是很困难的。kgateway 所做的是为最终用户提供一个更直观的接口来编程网络流量，这些最终用户可能包括基础设施提供商、集群运营商和应用程序开发人员。

Kgateway 读取管理员设置的 Gateway API 规则，然后使用 Envoy 执行这些规则。

Solo.io 的开源主管 [Lin Sun](https://www.linkedin.com/in/lin-sun-a9b7a81/) 在接受 TNS 采访时表示：“Kgateway 支持 Kubernetes Gateway API，因此用户可以使用这个由 Gateway HTTP 路由组成的直观用户界面。”

## Kubernetes 的 AI 路线图

据 Sun 介绍，kgateway 的目标是成为所有方向 Kubernetes 流量（包括南北向和东西向内部流量）的默认网关。

该项目也在努力扩展该软件的功能。

例如，kgateway 将自己定位为“AI 网关”，以应对将应用程序与 LLM 集成时面临的独特安全和管理挑战。

项目开发人员正在参与 [Kubernetes Network Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-network)，该小组正在开发一个新项目“[Gateway API Inference extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension)”。

![](https://cdn.thenewstack.io/media/2025/04/9fbeb5d7-679bd3a099f0005407d96459_ad_4nxfojpobiqoijskybenx-y8wczlwsvsaieah_tjaxyweuqi2rhygok8sj0_sxk6juoefdr2g9wymdk7qkx85ijl4brhwnrghpyg6pprpewmqwrltjz35lv7chv54ynepldenhwcoow.webp)

这个扩展将为 Kubernetes 提供特定于推理的路由功能，允许 K8s 部署通过路由、密钥管理、备份 LLM 和其他功能更轻松地与 [生成式 AI 驱动的](https://thenewstack.io/how-generative-ai-is-reshaping-the-sdlc/) 工作负载一起工作。

Kgateway 还与 [Istio Ambient mesh](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/) 紧密集成，后者旨在完全取消 Sidecar。对于 Ambient 模式下的 Istio，kgateway 可以充当 [waypoint proxy](https://youtu.be/B8oZ1seIDIM?list=TLGGDmuUB1z53FMwMjA0MjAyNQ)，提供 Istio 本身不具备的高级 L7 功能，例如请求转换、重试、AI 工作负载的流量控制。

Sun 在这里进一步解释：[视频](https://youtu.be/Bre-w-IZU_c)。