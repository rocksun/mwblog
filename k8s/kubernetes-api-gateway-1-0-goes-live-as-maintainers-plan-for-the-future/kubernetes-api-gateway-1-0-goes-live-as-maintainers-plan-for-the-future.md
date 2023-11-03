<!-- 
# Kubernetes API网关1.0正式发布
维护者计划未来路线
https://cdn.thenewstack.io/media/2023/10/70e83b68-gateway-api-1024x604.jpg
 -->

期待已久的 Kubernetes 网关 API 现在终于准备好用于生产环境了，它带来了许多新的支持工具来帮助 Kubernetes 管理员开始使用。

译自 [Kubernetes API Gateway 1.0 Goes Live， as Maintainers Plan for the Future](https://thenewstack.io/kubernetes-api-gateway-1-0-goes-live-as-maintainers-plan-for-the-future/) 。

经过四年的努力，[Kubernetes 网关 API](https://gateway-api.sigs.k8s.io/) 最终[达到了生产可用状态](https://github.com/kubernetes-sigs/gateway-api/releases/tag/v1.0.0)，提供了管理进出 Kubernetes 集群网络流量的标准化方式。

“这代表了大量人的共同努力。我认为这可能是 Kubernetes 历史上最重要的协作 API 之一。” Kubernetes 网络负责人谷歌员工工程师 [Rob Scott](https://www.linkedin.com/in/robertjscott1/) 在[发布声明](https://twitter.com/robertjscott/status/1719419469611848071)中写道。

起初，Kubernetes 通过 Ingress 或者自定义资源来提供外部访问，但每种方式[都有局限性](https://www.haproxy.com/blog/kubernetes-gateway-ap)，不同部署之间也存在很大差异。网关 API 的[设计](https://thenewstack.io/unifying-kubernetes-service-networking-again-with-the-gateway-api/)就是为了[标准化](https://thenewstack.io/the-api-gateway-and-the-future-of-cloud-native-applications/)这些网络服务。

根据[此文档描述](https://kubernetes.io/blog/2023/10/31/gateway-api-ga/)，几个关键的 API 如 Gateway(用于配置)、GatewayClass(用于集群级操作)、HTTPRoute(用于 HTTP 流量路由)等已经成熟为通用可用(GA)状态。

![](https://cdn.thenewstack.io/media/2023/11/46323c19-api-model-1024x602.png)

## 新增实验特性

除了确定上述核心技术外，此版本还引入了一些实验特性。

**BackendTLSPolicy** 将提供网关验证证书的[方式](https://gateway-api.sigs.k8s.io/geps/gep-1897/)。**HTTPRoute** 将支持[预设超时](https://gateway-api.sigs.k8s.io/geps/gep-1742/)。还将支持更多协议: 明文 HTTP/2([https://www.rfc-editor.org/rfc/rfc7540](https://www.rfc-editor.org/rfc/rfc7540))、明文 WebSocket([https://www.rfc-editor.org/rfc/rfc6455](https://www.rfc-editor.org/rfc/rfc6455))、TLS 上的 WebSocket 等，可以通过[后端协议选择](https://gateway-api.sigs.k8s.io/geps/gep-1911/)来指定协议。

未来，所有关于网关 API 的工作将通过基本和实验两个渠道进行。

## 更多帮助和指导

此版本还带来了一个新的(Beta 版本)命令行界面工具 [gwctl](https://github.com/kubernetes-sigs/gateway-api/tree/main/gwctl) 来与网关 API 交互。gwctl 的初始功能是提供集群中可用策略的信息等，未来版本会增加更多功能。

规范文档本身现在也附带了[实施指南](https://gateway-api.sigs.k8s.io/reference/implementers-guide/)，承诺会回答“关于构建网关 API 实现你想知道但不敢问的一切”。

下周在芝加哥举行的 [KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 大会(及相关的贡献者峰会)上也有多个会议来详细讲解网关 API:

KubeCon:

* [Kubernetes 历史上最协作的 API 达到 GA](https://sched.co/1R2qM)(周三上午11:55)

贡献者峰会:

* [构建通用的符合性测试报告框架](https://sched.co/1Sp9l)(周一上午11:15)
* [使用自定义资源定义构建通用可用的 API 经验教训](https://sched.co/1Sp9u)(周一上午11:45)
* [网关 API: 走向 GA 之外](https://sched.co/1SpA9)(周一下午12:15)

最后，本周《新技术栈》杂志启动了一个六部分系列，从“[Ingress 控制器还是 Kubernetes 网关 API？](https://yylives.cc/2023/11/02/ingress-controllers-or-the-kubernetes-gateway-api-which-is-right-for-you/)”开始，介绍理解 Kubernetes 网关 API，将持续到下周。该系列由 [NGINX](https://www.nginx.com/?utm_content=inline-mention) 赞助，作者 [Robert Kimani](https://thenewstack.io/author/robertkimani/)，将涵盖使用网关 API 的主题，如微服务、多集群部署、流量管理、安全等。

