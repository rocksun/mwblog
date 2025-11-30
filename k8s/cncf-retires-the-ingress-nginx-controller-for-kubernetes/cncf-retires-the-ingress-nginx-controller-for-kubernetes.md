<!--
title: CNCF 宣布弃用 Kubernetes Ingress Nginx 控制器
cover: https://cdn.thenewstack.io/media/2025/11/d90814fe-kubecon-haproxy-mancini-assman.jpg
summary: Ingress Nginx 控制器将于 2026 年 3 月停止支持，需迁移至 Gateway API 或其他方案。Gateway API 是 Kubernetes 网络的首选，HAProxy 等公司正提供迁移方案。
-->

Ingress Nginx 控制器将于 2026 年 3 月停止支持，需迁移至 Gateway API 或其他方案。Gateway API 是 Kubernetes 网络的首选，HAProxy 等公司正提供迁移方案。

> 译自：[CNCF Retires the Ingress Nginx Controller for Kubernetes](https://thenewstack.io/cncf-retires-the-ingress-nginx-controller-for-kubernetes/)
> 
> 作者：Joab Jackson

为您的 Kubernetes 集群运行 [Ingress Nginx 控制器](https://github.com/kubernetes/ingress-nginx/) 吗？您必须在明年 3 月前迁移到 Gateway API 或其他选项，[云原生计算基金会](https://cncf.io/?utm_content=inline+mention) 上周在 [北美 KubeCon+CloudNativeCon 大会](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) 上宣布了这一决定。

许多人预料到这一消息会发布，但仍感到惊讶，尤其是被要求[迅速的转变](https://www.kubernetes.dev/blog/2025/11/12/ingress-nginx-retirement)。

“所以今天大会上很多人都在忙着寻找替代方案，因为 Ingress 是 Kubernetes 的默认 ingress 控制器，”HAProxy 工程和运营副总裁 Frank Mancina 在活动中接受 TNS 采访时说道。

Kubernetes SIG Network 和安全响应委员会计划于 2026 年 3 月停止支持 Ingress Nginx。此后，该软件将不再受支持：没有新的发布，没有错误修复，也没有解决任何安全漏洞的更新。

代码将保留在 [GitHub](https://github.com/kubernetes/ingress-nginx) 上用于存档目的，同时支持 [Helm 运算符](https://github.com/nginx/nginx-ingress-helm-operator) 等软件。

在 3 月之后继续操作此控制器的人员，需自行承担风险。

想知道您的集群是否运行 Ingress Nginx？在具有集群管理权限的命令行中，输入以下命令：

```

kubectl get pods \--all-namespaces \--selector app.kubernetes.io/name=ingress-nginx
```

## Kubernetes 网络

Kubernetes 的网络支持姗姗来迟。CNCF 为 Gateway API 工作了四年，并于去年发布了 1.0 版本。Gateway 负责集群内外的流量路由，包括 Layer 4（TCP/IP 层）和 Layer 7（应用程序流量）流量。

Ingress 本身是一组 API 规则，用于引导访问集群的外部网络流量。Ingress Nginx 控制器作为一个 Kubernetes 项目诞生。它使用开源 Nginx 反向代理（[现由网络公司 F5 Inc. 管理](https://techcrunch.com/2019/03/11/f5-acquires-nginx-for-670m-to-move-into-open-source-multi-cloud-services/)）作为基础。[Ingress Nginx 控制器](https://github.com/kubernetes/ingress-nginx) 后来成为众多实现 Ingress API 的控制器之一。

然而，负责该项目的 Kubernetes 网络和安全组发现维护它是一个挑战。寻找人员来帮助维护代码库是一个挑战，尤其是在 Gateway API 项目启动之后。此外，添加任意 NGINX 配置指令的[功能，称为片段](https://docs.nginx.com/nginx-ingress-controller/configuration/ingress-resources/advanced-configuration-with-snippets/)，成为一个安全问题。

[Gateway API](https://thenewstack.io/kubernetes-gateway-api-nixes-future-beta-releases/) 基于一组 Kubernetes [自定义资源定义](https://thenewstack.io/kubernetes-crds-what-they-are-and-why-they-are-useful/) (CRD) 构建，于 2023 年推出，此后成为 CNCF 首选的、面向未来的 Kubernetes 入口（入站流量）和出口（出站流量）方式。

“使用 Gateway API 规范，您将拥有更多的规范和控制。这就是人们可能迁移到它的原因。而且 Kubernetes 发展非常迅速，这似乎是获得最多关注的规范，”Mancina 进一步解释道。

## 公司回应

反向代理软件提供商 [HAProxy Technologies LLC](https://www.haproxy.com/?utm_content=inline+mention) 是响应 Gateway API 倡议的公司之一。它长期提供 [HAProxy Ingress](https://github.com/haproxytech/kubernetes-ingress)，并已通过新发布的 [HAProxy Unified Gateway](https://www.haproxy.com/blog/announcing-haproxy-unified-gateway-beta) 扩展了对 Gateway API 的支持——这是一个免费的开源产品，为 Gateway API 和 Ingress 提供 Kubernetes 原生应用程序路由。

HAProxy 产品总监 Baptiste Assmann 在接受 TNS 采访时说：“我们看到的是，有些客户的工作流已经通过 Ingress 规则建立，他们不想改变它。”

Unified Gateway 旨在提供一种在时间允许的情况下轻松过渡到 Gateway API 的方式。或者两者并行运行。

Assmann 说：“我们不是为 Ingress 规则提供一个产品，为 Gateway API 提供一个产品，让人们选择其中一个，而是让新产品也支持 Ingress 规则，这样人们可以开始使用 Ingress 规则，然后在准备好时切换到 Gateway API。”

他建议，由于它们的架构不同，从一个切换到另一个可能需要一些工作。

Ingress 运行在中央控制器模型上，而 Gateway API 运行在 Kubernetes 运算符模型上。“这是一种完全不同的配置方式，”他补充道。

Mancina 进一步解释说，Gateway API 具有卓越的职责分离。例如，它区分了可以由平台团队、运营团队和应用程序团队控制的对象。

HAProxy 还在努力将选定数量的 Nginx 注解引入到统一网关中。

其他提供 Gateway API 支持的平台包括 [Nginx Gateway Fabric](https://github.com/nginx/nginx-gateway-fabric)（阅读 TNS 分析师 Janakiram MSV 的深度解读[在此](https://thenewstack.io/cncf-deprecates-the-ingress-nginx-controller/)）以及 [Envoy](https://gateway.envoyproxy.io/docs/tasks/traffic/gatewayapi-support/)、[Istio](https://istio.io/latest/docs/tasks/traffic-management/ingress/gateway-api/)、[Cilium](https://youtu.be/dqyBoqJYveQ) 和 CNCF 自己的 [KGateway](https://www.cncf.io/blog/2025/11/18/kgateway-v2-1-is-released)。