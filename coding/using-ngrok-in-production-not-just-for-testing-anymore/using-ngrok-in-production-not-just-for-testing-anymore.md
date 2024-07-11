
<!--
title: 生产环境中使用ngrok：不仅仅用于测试
cover: https://cdn.thenewstack.io/media/2024/07/f9dd0d0e-network-ingress-api-ngrok.jpg
-->

您已经了解 ngrok 如何为本地主机提供远程连接。现在，了解 ngrok 如何管理生产应用程序的流量。

> 译自 [Using ngrok in Production: Not Just for Testing Anymore](https://thenewstack.io/using-ngrok-in-production-not-just-for-testing-anymore/)，作者 Scott M Fulton III。


在广阔的全球网络中提供数字服务时，最大的挑战是使这些服务能够安全地相互通信。保护端点通常不像保护它们之间的路由那样令人生畏。

如果您曾经使用 ngrok 生成一个 *临时* 安全隧道，以便服务和浏览器即使在 `localhost` 上托管也能与您的应用程序联系，您可能已经问过自己是否可以以同样的无缝方式交付您的生产应用程序和 API。

如果您正在您的开发团队网络甚至您的个人笔记本电脑上为测试准备一个 API，ngrok 为您提供了一种在本地端口上 [打开 HTTPS 端点](https://ngrok.com/docs/http/) 的方法。您在笔记本电脑上启动应用程序，通过命令行调用 ngrok，现在您在另一个大陆的测试人员就可以访问了。

## 您附近的网络组件

当您在服务级别解决网络入口问题时，它一开始看起来并不容易。您很快就会意识到 [微服务架构的消息传递协议](https://thenewstack.io/securing-microservices-communication-with-mtls-in-kubernetes/) 使这个挑战成倍增加。当从网络外部联系微服务时，[API 网关使用各种 Web 协议、内部协议以及 Kafka 使用的事件流协议来路由消息](https://thenewstack.io/the-api-gateway-and-the-future-of-cloud-native-applications/)。[最优地](https://stackoverflow.com/questions/61174839/load-balancer-and-api-gateway-confusion)，一个好的 API 网关可以有效地分配消息间流量，以至于您不需要单独的负载均衡器。

在现代网络应用程序架构中，每个使服务从网络外部安全访问的重要功能（网络工程师称之为“南北流量”）都需要一个专门用于该功能的网络组件。

因此，无论您是应用程序开发人员还是网络安全工程师，用 [芝麻街的鲍勃](https://muppet.fandom.com/wiki/The_People_in_Your_Neighborhood) 的话说，这些都是您附近的单元：

- **网络地址转换 (NAT) 网关**: 使私有 IP 地址公开
- **安全 Web 网关 (SWG)**: 强制执行入站流量策略和限制
- **API 网关**: 充当您 API 与外部世界的交换机
- **负载均衡器**: 平衡地将请求分配到请求服务的活动实例
- **入口控制器**: 为微服务充当反向代理和负载均衡器的功能
- **身份和访问管理 (IAM)**: 验证服务并为它们之间的流量提供加密

单组件单功能方法的问题在于它会产生一定程度的架构复杂性，这本身就成为一个安全问题。此外，部署专门的代理来管理南北流量会增加 IT 的成本和工作量，因为每个代理都必须部署、配置和维护，包括确保及时应用安全补丁。

## “完整的门面”

部署这些大量服务的替代方案是使用一个实用程序，将活动组件的数量减少到仅提供安全入口所需的组件。这就是 ngrok 重新进入画面的地方。

您可能从未想过 ngrok 实际上可以成为您的入口控制器。也就是说，您可以将 ngrok 组件作为应用程序或 API 的全职操作员，管理对您 API 的 HTTPS 调用，并有效地将任何经过身份验证的远程应用程序与您的本地微服务应用程序在粒度级别集成。

“[Ngrok] 消除了架构在生产中通常具有的活动部件，”ngrok 的解决方案架构师 [Shub Argha](https://www.linkedin.com/in/shubcodes/) 说。“这些活动部件通常包括设置某种 Web 网关。”

Argha 说，对于传统的微服务应用程序，服务被放置在 Web 网关后面，该网关对用户进行身份验证，负载均衡器分配流量，以及一个单独的 NAT 网关（基本防火墙的主要组件）将流量路由到最终目标地址。这种网关通常通过私有子网启用对资源的访问，该子网连接一组大型的内部 IP 地址。防火墙管理的一组策略决定了如何以及何时可以访问这些资源。出站流量将通过同一个 NAT 网关从网络中路由出去。

“使用 ngrok，我们的入口控制器或 API 网关就可以替代所有这些，”Argha 说。“我们是‘完整的门面’。我们将提供负载均衡以及这两个网关，因此您无需自行设置。”

虽然 ngrok 确实提供了入口控制功能，但 Argha 解释说，一旦它集成到网络应用程序中，它还充当负载均衡器、Web 网关、NAT 网关和 API 网关的功能。因此，ngrok 还承担了安全工程师为这些组件单独生成的规则和策略的所有责任——Argha 指出，这些组件“将有额外的安全规则，所有这些规则都必须由您构建并由安全团队管理”。

Ngrok 的身份验证功能和安全策略都由一个名为 ngrok Edge 的托管服务处理，该服务位于网络之外。“您只需设置我们的入口控制器，它会建立到我们托管服务的出站连接，该服务会自动为您提供该连接。”

[将 ngrok 安装为入口控制器](https://ngrok.com/docs/using-ngrok-with/k8s/)，或“入口操作符”，可以通过 [Helm Kubernetes 包管理器](https://thenewstack.io/get-started-with-the-helm-kubernetes-package-manager/) (`helm install`) 完成，使用从 ngrok 仪表板服务获得的 [凭据](https://ngrok.com/docs/k8s/deployment-guide/credentials/)。使用它，您创建一个命名空间，然后应用一个 YAML 文件，将该命名空间分配给指定的网络端口。

相比之下，Argha 说，其他入口控制器，如 [HAProxy](https://www.haproxy.com/?utm_content=inline+mention) 和 [NGINX](https://www.nginx.com?utm_content=inline+mention)，除了设置组件、建立防火墙规则和策略、设置负载均衡器和网关以及确保 DNS 服务指向正确的端点外，还需要实施者。“在您的应用程序上线之前，您需要采取更多步骤，”他补充道。“使用 ngrok，您不需要。”

## 90 度转弯

Argha 说，这种易于实施的方式使 ngrok 能够与服务网格协调。换句话说，在网络上运行的服务，其可访问端点需要配置为与 API 网关一起运行，可以通过 ngrok 自动设置的路由访问 ngrok API 网关。

![客户端应用程序和使用 ngrok 代理构建的订阅音乐服务之间的网络交互架构](https://cdn.thenewstack.io/media/2024/07/34eb1b02-ngrok-model-1024x439.jpg)

*Scott M. Fulton 根据 Shub Argha 的图绘制的图片。*

Argha 绘制的模型代表了客户端应用程序和使用 ngrok 代理构建的订阅音乐服务之间的网络交互。Ngrok 的 API 网关管理到音乐服务的流量，代理将请求转发到应用程序中的各种服务。

此图中中心的 ngrok Edge 平台是一个托管服务，负责处理右下角黄色框中列出的所有功能，包括 [身份验证](https://roadmap.sh/guides/basics-of-authentication) 和 [授权](https://roadmap.sh/guides/oauth)。后端应用程序不再负责这些功能，这意味着应用程序不再容易受到攻击，这些攻击针对的是原本负责这些功能的组件。

同时，ngrok 代理能够将传入的远程请求转发到各种服务。结合可能存在的任何服务网格，这使远程客户端能够更直接地访问服务，就好像它们是独立的应用程序一样。对于音乐服务示例，这意味着在智能手机上运行的客户端应用程序可以向播放列表服务发出请求，以执行与播放列表相关的功能。“搜索”吊舱中的服务可以接受搜索请求，就好像它们是“搜索应用程序”一样。这改变了流量本身的性质，提升了 [Kubernetes](https://thenewstack.io/kubernetes/) 吊舱的角色，使其更像是一等公民。

“Ngrok 可以让您访问所有这些不同的 Kubernetes 服务，这些服务位于不同的吊舱中，”Argha 解释道。“Kubernetes 的优势在于，如果一个吊舱突然消失，[Kubernetes] 可以自动启动它。或者，如果一个吊舱的流量很大，它可以开始创建更多吊舱。Ngrok 的真正优势在于将流量路由到 [图中的] 搜索或播放列表。”

由于 ngrok 本身不是服务网格，因此它对服务中 Pod 的健康状况或数量，或任何时间点 Pod 之间的流量级别没有了解。您仍然需要一个服务网格。在最近由 ngrok 和 Buoyant 共同制作的 [YouTube 视频](https://www.youtube.com/watch?v=yYTKQRaOGEM) 中，Argha 和他的 Buoyant 同事 Flynn 演示了将 ngrok 与 [Linkerd](https://thenewstack.io/buoyant-revises-release-model-for-the-linkerd-service-mesh/) 集成。在演示中，Flynn 首先花了几分钟在后端安装 ngrok，只是为了展示该过程是多么简单快捷。

但 Linkerd 不是 ngrok 集成的唯一服务网格。最近，Argha 通过将 ngrok 与 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 管理的开源项目 Skupper 配对进行了实验，该项目在技术上并不将自己定义为服务网格。相反，它是一个 [第 7 层](https://thenewstack.io/the-osi-7-layer-model-can-help-define-enterprise-application-security/) 网络服务互连平面项目。在这种配对中，ngrok 管理南北路由，而 Skupper 处理东西路由。“这是 ngrok 旋转了 90 度，”Argha 评论道。然而，他补充说，“ngrok 可以与任何服务网格配对，并且效果相同。

“使用 ngrok，因为我们负责互联网层，”他继续说道，“您使用我们产品所做的其他一切事情都让您不必担心设置该互联网层。这就是我们优越的原因，”Argha 说。

*要详细了解用于生产的 ngrok，包括 Kubernetes 入口、API 网关、设备网关等，请在 ngrok.com 上免费注册，查看 ngrok 的产品文档或加入即将到来的开发者直播。*

