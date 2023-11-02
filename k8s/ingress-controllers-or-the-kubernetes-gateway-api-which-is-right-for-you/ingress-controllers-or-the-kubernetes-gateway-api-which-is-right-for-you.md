<!--
# Ingress 控制器还是 Kubernetes Gateway API？
https://cdn.thenewstack.io/media/2023/11/44038778-arm-wrestling-567950_1280-1024x682.jpg
 -->

对这两种解决方案的优势和局限性有清晰的理解，对于制定 Kubernetes 网络策略非常关键。

译自 [Ingress Controllers or the Kubernetes Gateway API? Which Is Right for You?](https://thenewstack.io/ingress-controllers-or-the-kubernetes-gateway-api-which-is-right-for-you/) 。

在 Kubernetes 网络中，Ingress 控制器和 Kubernetes Gateway API 扮演着核心角色，充当 Kubernetes 应用程序入站流量的网关。这些组件是重要的中间层，协调 Kubernetes 集群内请求和响应的复杂交互。它们简化和优化了路由、负载均衡和流量管理等关键网络任务。

![](https://cdn.thenewstack.io/media/2023/11/289b13eb-gateway-api-logo-300x83.png)

其主要职责包括:

- **Kubernetes 应用网关**: Ingress 控制器和 Kubernetes Gateway API 作为外部流量的主要入口，将外界与容器化应用程序连接。
- **简化路由**: 提供定义入站流量路由规则的统一抽象方法，消除单个服务级路由配置需求。
- **高效负载均衡**: 自动化负载均衡，确保流量均匀分布到多个应用实例，Ingress 控制器和 Kubernetes Gateway API 能有效实现。
- **流量管理**: 提供流量管理高级功能，包括根据各种条件进行流量分流、镜像和路由，增强应用弹性和灵活性。

总之，Ingress 控制器和 [Kubernetes Gateway API](https://thenewstack.io/my-istiod-pod-cant-communicate-with-the-kubernetes-api-server/) 是连接 Kubernetes 应用和外部环境的关键组件。但该使用哪个呢？

## Ingress及其在解决网络问题方面的作用

Ingress 充当管理 [Kubernetes 集群内服务外部访问](https://thenewstack.io/aws-cdk8s-a-dev-friendly-alternative-to-yaml-for-managing-kubernetes-clusters/)的层。Ingress 的角色可以概括为:

- **路由和流量管理**: Ingress 提供了配置[外部流量到服务的路由](https://thenewstack.io/rethinking-service-mesh-with-application-traffic-management/)方式，使定义请求处理规则更简单。
- **负载均衡**: Ingress 控制器通常具有负载均衡功能，确保流量高效分发到后端服务。
- **SSL/TLS 终结**: Ingress 可以处理 SSL/TLS 终结，[实现外部客户端与集群内服务的安全通信](https://thenewstack.io/aporetos-kubernetes-security-platform-now-offers-multiregion-cluster-support-service-mesh-integration/)。
- **基于路径的路由**: Ingress 支持按路径路由，使不同服务可以通过指定路径或主机名暴露。

要掌握 Kubernetes 如何解决网络问题，理解 Ingress 及其作用至关重要。后面章节将[探讨 Ingress 控制器和 Kubernetes Gateway API](https://thenewstack.io/kubernetes-access-control-exploring-service-accounts/)，它们建立在 Ingress 基础上，提供更高级的网络解决方案。

## Ingress 控制器解密

[Ingress 控制器是 Kubernetes 网络的关键组件](https://thenewstack.io/ingress-controllers-the-swiss-army-knife-of-kubernetes/)，在管理进入 Kubernetes 集群的服务访问方面起核心作用。这些控制器扮演集群的流量管理员角色，根据规则指导外部请求到集群内具体服务和 Pod。它们通过路由、负载均衡和其他关键网络功能来实现这一目标。

Ingress 控制器的核心功能包括：

- **路由流量**: 根据预定义规则和配置指引入站流量，使请求到达集群内适当服务。
- **负载均衡**: 结合负载均衡功能，确保流量在后端服务间均匀分发，提高可用性和资源利用率。

**常见的 Ingress 控制器**

1. **Nginx Ingress 控制器**: Kubernetes 生态中使用最广泛的控制器之一。基于 Nginx Web 服务器，提供强大的流量管理功能，擅长路径路由、SSL/TLS 终结和通过注解自定义。
2. **HAProxy Ingress 控制器**: 因高性能和负载均衡功能而受欢迎。可高效处理大量连接，对路由和流量策略控制精细。适合复杂网络场景。
3. **Traefik Ingress 控制器**: 现代化、易用的 Ingress 控制器。支持[服务发现](https://thenewstack.io/how-does-service-discovery-work-in-kubernetes/)，与 Kubernetes 等编排器无缝集成。以其简单性、自动配置和支持 Let's Encrypt 的 SSL 见长。

## Ingress 控制器实践

1. **路由流量到服务**: 充当流量管理员，定义规则指引请求到特定 Kubernetes 服务。例如基于主机名或路径路由，通过不同 URL 或域名暴露服务。
2. **SSL/TLS 终结和认证**: 通过处理 SSL/TLS 终结提高安全性，确保客户端与集群内服务间加密通信。还可以管理认证授权，为应用增加安全层。

## Kubernetes Gateway API的兴起

Kubernetes Gateway API代表了Kubernetes生态系统中传统Ingress[资源](https://thenewstack.io/fairwinds-goldilocks-helps-set-kubernetes-resources-just-right/)的演进。Ingress控制器作为外部流量的入口具有价值，但在灵活性和扩展性方面存在局限。Kubernetes Gateway API作为更全面、强大的解决方案出现，解决了这些局限。

一个主要区别是，[Kubernetes Gateway API使用自定义资源定义(CRD)来定义网络资源](https://thenewstack.io/kubernetes-1-15-aims-to-extensibility-with-custom-resource-definition-features/)，提供了更结构化、可扩展的方式来定义和配置路由和流量管理规则。它利用[CRD](https://thenewstack.io/kubernetes-1-6-has-arrived-with-custom-resource-definitions/)框架扩展了Kubernetes原生API，引入了专门用于网络的新资源类型。

## Kubernetes Gateway API的关键特性

1. **路由定义**: 引入Route资源，允许定义复杂的路由配置。Route指定如何将入站流量引导到后端服务，相比Ingress资源具有更高粒度，支持更复杂的路由决策。
2. **流量分裂和镜像**: 关键特性之一是进行流量分裂和镜像。流量分裂实现从一个后端服务逐步迁移流量到另一个后端服务，方便金丝雀部署和A/B测试。流量镜像将请求复制到不同目的地用于监控和调试，不影响主流量。

## Kubernetes Gateway API如何解决Ingress的挑战

[Kubernetes Gateway API解决了](https://thenewstack.io/netflix-discovers-severe-kubernetes-http-2-vulnerabilities/)传统Ingress存在的一些挑战:

- **更灵活**: 使用CRD定义网络配置，提供高度灵活、可扩展的方式。这种灵活性让用户可以根据具体场景有效定制网络规则。
- **高级流量控制**: 通过引入Route资源，提供了管理复杂路由和流量的高级功能，超出仅通过Ingress控制器可以实现的范围。
- **更好的扩展性**: CRD提供的扩展性可以轻松集成自定义网络解决方案和第三方插件，进一步增强其功能和适应不断发展的网络需求的能力。

## 何时选择Ingress控制器

Ingress控制器非常适合以下情况:

**简单快速上手**: 设置简单，非常适合小型、不复杂的Kubernetes部署，配置简易性是优先考虑因素。

**现有部署**: 如果现有集群已配置 Ingress 控制器，且符合需求，可能不需要立即迁移到Kubernetes Gateway API。

## 何时Kubernetes Gateway API更合适

以下情况下，Kubernetes Gateway API是更好的选择:

**复杂路由和流量控制**: 需要处理复杂路由、流量分裂和高级流量管理时，Route资源提供所需的灵活性。

**自定义和扩展性**: 当需要自定义解决方案或集成第三方插件时，基于CRD的方法提供更大的可扩展性。


## Ingress 控制器与 Kubernetes Gateway API 比较

### 配置和灵活性

配置 Ingress 控制器通常需要使用注解和 ConfigMap。这种方法对简单场景较直接，但面对复杂的路由和流量管理需求时可能存在挑战，需要精心配置和更多维护工作。

相比之下，Kubernetes Gateway API 通过 CRD 提供了更结构化、可适应的配置流程。它为用户提供了一个明确定义的框架来制定自定义路由规则和流量策略等网络配置。这增强了清晰性，并使用户可以精确控制自己的网络设置。

### 性能和可伸缩性

Ingress 控制器默认仅提供基本的负载均衡功能。但在处理大量流量和动态扩展需求时可能遇到困难，扩展还会引入额外复杂性。

相反，Kubernetes Gateway API 从一开始就是专门为可伸缩性设计的。它与 Kubernetes 的伸缩机制无缝集成，非常适合大规模部署和不稳定流量模式。此外，它的流量分裂和镜像功能对编排无中断的扩展和部署也很有价值。

### 安全和认证

Ingress 控制器提供 SSL/TLS 终结确保客户端和服务间安全通信，并支持基本的认证和授权，但更高级的安全功能需要额外配置或第三方工具。

而 Kubernetes Gateway API 通过支持高级认证和策略来加强安全性。它可无缝集成 IAM 系统，开箱即用地提供强大的安全功能。

### 监控和可观测性

监控 Ingress 控制器通常需要从各种源收集日志和指标，包括控制器自身、外部负载均衡器和 Kubernetes 组件。为实现全面可观测性，可能还需要部署额外的监控工具和复杂的配置。

相反，Kubernetes Gateway API 通过原生支持监控资源和路由来优化可观测性。这种内置支持简化了监控流程，并便于与 Prometheus、Grafana等监控解决方案无缝集成。因此，获得网络流量和配置洞察更加直接。

综上所述，Ingress 控制器与 Kubernetes Gateway API 的选择取决于具体场景、配置需求、性能需求、安全考量以及对可观测性的偏好。明确理解每种解决方案的优势和局限非常重要，以便在 Kubernetes 网络策略中做出合适的选择。
