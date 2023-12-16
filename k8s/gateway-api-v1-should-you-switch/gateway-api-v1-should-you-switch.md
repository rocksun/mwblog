<!--
title: Kubernetes Gateway API v1.0: 您应该切换吗？
cover: https://static.apiseven.com/uploads/2023/12/08/XllJX2YG_apisix-ingress.png?imageMogr2/format/webp
-->

> 译自 [Kubernetes Gateway API v1.0: Should You Switch?](https://static.apiseven.com/uploads/2023/12/08/winePDii_gateway-api.png?imageMogr2/format/webp)。作者 Navendu Pottekkat 。


距离 Kubernetes Gateway API[ 发布v1.0版本](https://kubernetes.io/blog/2023/10/31/gateway-api-ga/)已经过去一个月了，这标志着其一些关键 API 的毕业到普遍可用的状态。

去年 Gateway API 毕业到 beta 版本时，我写了[一篇关于它的文章](https://api7.ai/blog/gateway-vs-ingress-api.md)，但一年后，问题仍然存在。您应该从 Ingress API 切换到 Gateway API 吗？

我去年的答案是不应该。而且我有很强的理由。

Gateway API 及其实现仍处于起步阶段。另一方面，Ingress API 已经很稳定，涵盖了可能适用于大多数用户的一些主要用例。

对于需要更多功能的用户，我建议使用 Ingress 控制器提供的自定义资源，以牺牲可移植性(在不同的 Ingress 实现之间切换)为代价。

随着 v1.0 版本的发布，这可能会改变。Gateway API 现在功能更加强大，它的 [20 多个实现](https://gateway-api.sigs.k8s.io/implementations/)正在迅速赶上。

因此，如果您正在从头开始选择 Ingress 和 Gateway API，我建议如果您选择的 API 及其[实现](https://apisix.apache.org/docs/ingress-controller/tutorials/configure-ingress-with-gateway-api/)支持您想要的所有功能，请选择 Gateway API。

## Ingress API 有什么问题？

[Ingress API](https://kubernetes.io/docs/concepts/services-networking/ingress/) 的工作非常好，但只适用于一小部分常见用例。为了扩展其功能，Ingress 实现开始使用自定义注释。

例如，如果您选择 Nginx Ingress，您将使用它的[几十个注释](https://github.com/kubernetes/ingress-nginx/blob/main/docs/user-guide/nginx-configuration/annotations.md)。如果您决定切换到另一个 Ingress 实现(如 [Apache APISIX](https://apisix.apache.org/docs/ingress-controller/concepts/annotations/))，这些注释就是不可移植的。

这些特定于实现的注释也很难管理，并且违背了以 Kubernetes 原生方式管理 Ingress 的初衷。

最终，Ingress 控制器实现开始开发自己的 CRD，以便向 Kubernetes 用户公开更多功能。这些 CRD 特定于 Ingress 控制器。但是，如果您可以牺牲可移植性并坚持使用一个 Ingress 控制器，那么 CRD 更容易使用，并提供了更多功能。

Gateway API 旨在一次性解决这个问题，它提供了 Ingress API 的 vendor 无关性和 CRD 的灵活性。它的定位非常好，有望实现这个目标。

从长远来看，Ingress API 不会再添加新功能，所有的努力将用于与 Gateway API 保持一致。因此，采用 Ingress API 可能会在无意中达到其功能的限制时导致问题。

## 明显的好处

表达性、可扩展性和面向角色是 Gateway API 开发的关键理念。

与 Ingress API 不同，Gateway API 是一个 API 集合(HTTPRoute、Gateway、GatewayClass 等)，每个 API 都针对不同的组织角色。

例如，应用程序开发人员只需要关注 HTTPRoute 资源，在那里他们可以定义路由流量的规则。他们可以将集群级别的详细信息委托给负责管理集群并确保它满足开发人员需求的操作员，操作员使用 Gateway 资源。

![](https://yylives.cc/wp-content/uploads/2023/12/winePDii_gateway-api.png)

API 的[面向角色设计](https://gateway-api.sigs.k8s.io/#why-does-a-role-oriented-api-matter)允许不同的人使用集群而又能保持控制。

Gateway API 的功能也远胜于 Ingress API。Ingress API 中需要注释才能支持的功能在 Gateway API 中已经开箱即用。

## 官方扩展

虽然 Gateway API 是一个官方的 Kubernetes API，但它是作为一组 CRD 来实现的。

这与使用默认的 Kubernetes 资源没有什么不同。但是您只需要像安装官方扩展一样[安装这些 CRD](https://gateway-api.sigs.k8s.io/guides/#installing-gateway-api)。

![](https://yylives.cc/wp-content/uploads/2023/12/XllJX2YG_apisix-ingress.png)

与缓慢朝着长期稳定性发展的 Kubernetes 相比，这允许快速迭代。

## 会不会泛滥？

这个[著名的 XKCD 漫画](https://xkcd.com/927/)频繁地提醒我们，标准往往会泛滥。

Ingress 和 Gateway API 出现了这种标准的一个版本。它通常是这样的:

1. 出现一个标准来统一不同的项目/它们的标准(Kubernetes Ingress API)。
2. 统一的标准有限制，实现者想要克服这些限制(Ingress API 受限)。
3. 由于这些限制，实现开始偏离标准(自定义 CRD、注释)。
4. 现在，每个实现都有自己的标准(不可移植的 CRD、注释)。
5. 出现一个新标准来统一这些不同的标准(Kubernetes Gateway API)。

认为 Gateway API 可能不是这里的终点是合理的。但我相信它有足够的机会成为 Kubernetes 中的路由标准。

同样，我有很强的理由。

广泛采用对防止标准泛滥至关重要，因为实现很少有动力对应一个不同的标准工作。Gateway API 已经有 25 多个实现。

实现可以在不同级别上符合 Gateway API:

- **核心**: 所有实现都应该符合这些。
- **扩展的**: 这些可能只在某些实现中可用，但都是标准 API。
- **特定于实现的**: 特定于实现，但通过标准扩展点添加。

当更多的实现支持这些功能时，一个小众功能可以从特定于实现移动到扩展再到核心。即，API 允许自定义扩展的空间，同时确保遵循标准。

服务网格接口([Service Mesh Interface,SMI](https://smi-spec.io/))项目是对 Kubernetes 中配置服务网格进行标准化的类似尝试。但是，在最初涉及服务网格项目后，该项目几乎没有获得任何吸引力，并慢慢消亡。

SMI 没有支持用户在服务网格中期望的许多公共因子功能。它也没有足够快地支持这些功能。最终，服务网格实现在遵循 SMI 方面落后于人(我曾在 [CNCF TAG Network](https://github.com/cncf/tag-network) 的一个报告 SMI 兼容性的项目下与 SMI 密切合作)。

这些都是通用的原因，但该项目现在正在通过 Gateway API 重生。 网关 API 用于网格管理和管理(GAMMA)计划旨在扩展网关 API 以与服务网格一起使用。

SMI 项目[最近与 GAMMA initiative 合并](https://smi-spec.io/blog/announcing-smi-gateway-api-gamma/)，这对 Gateway API 来说是非常好的。无疑是最流行的服务网格 Istio 也[宣布](https://istio.io/latest/blog/2022/gateway-api-beta/) Gateway API 将是未来管理 Istio 的默认 API。这样的采用可以防止泛滥。

## 迁移指南

[Gateway API 文档](https://gateway-api.sigs.k8s.io/guides/migrating-from-ingress/)中有一份全面指南，指导如何将 Ingress 资源迁移为 Gateway 资源。而不是重述它，让我们试着使用 [ingress2gateway](https://github.com/kubernetes-sigs/ingress2gateway) 工具将我们的 Ingress 资源转换为相应的 Gateway API 资源。

您可以直接从[发行页面](https://github.com/kubernetes-sigs/ingress2gateway/releases/tag/v0.1.0)为您的操作系统下载并安装二进制文件。

让我们看一个简单的 Ingress 资源:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: httpbin-route
spec:
  ingressClassName: apisix
  rules:
  - host: local.httpbin.org
    http:
      paths:
      - backend:
          service:
            name: httpbin
            port:
              number: 80
        path: /
        pathType: Prefix
```

这将把带有提供的主机地址的所有流量路由到 httpbin 服务。要将其转换为 Gateway API 资源，我们可以运行:

```bash
ingress2gateway print --input_file=ingress.yaml
```

这个 Gateway API 资源将如下所示:

```yaml
apiVersion: gateway.networking.k8s.io/v1alpha2
kind: HTTPRoute
metadata:
  name: httpbin-route
spec:
  hostnames:
  - local.httpbin.org
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: httpbin
      port: 80
```

### 其他可行的选择

还有其他配置 Kubernetes 中网关的可行选择。

在 Apache APISIX 中，您可以以[独立模式](https://apisix.apache.org/docs/apisix/next/deployment-modes/#standalone)部署它，并在 yaml 文件中定义路由配置。您可以通过传统的工作流更新此 yaml 文件，当通过 Kubernetes API 管理网关配置不是必需时，这可能会非常有用。

如果您不打算切换到不同的解决方案，或者如果配置足够小而可以轻松迁移，那么[特定于实现的自定义 CRD](https://apisix.apache.org/docs/ingress-controller/tutorials/proxy-the-httpbin-service/) 也是可行的选择。

无论如何，Gateway API 是这里留下来的。
