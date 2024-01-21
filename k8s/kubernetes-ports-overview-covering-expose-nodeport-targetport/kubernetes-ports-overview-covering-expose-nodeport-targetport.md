<!--
title: Kubernetes的六种端口
cover: https://journal.hexmos.com/content/images/size/w2000/2024/01/24b500f3324b07e804ee05636d3c4520addc8ee8cba9234a9e1c6961f1302535.png
-->

曾经对Kubernetes中的服务器、docker、服务、容器、目标或节点端口感到困惑过吗？本文为您逐一解析，从开发到部署，解释您工作流程中的每个端口。今天就深入探讨，简化复杂性!

> 译自 [6 Kubernetes Ports: A Definitive Look - Expose, NodePort, TargetPort, & More](https://journal.hexmos.com/kubernetes-ports-overview-covering-expose-nodeport-targetport/)。作者 Athreya aka Maneshwar 。

最近我正试图在我们的Kubernetes基础设施之上建立一个部署流水线。

我一直在寻找一份关于端口类型以及流量在它们之间的导航方式的适当指南，但找不到任何现成的解决方案。

在了解并解决这个问题之后，我写了这篇文章，以简单的方式帮助您清楚地了解端口，并促进讨论。非常适合自学和帮助朋友!

## 端口通信

在下面的方法中，我使用了 [Kubernetes](https://kubernetes.io/?ref=journal.hexmos.com) 中的 [NodePort](https://kubernetes.io/docs/concepts/services-networking/service/?ref=journal.hexmos.com#type-nodeport) [服务类型](https://kubernetes.io/docs/concepts/services-networking/service/?ref=journal.hexmos.com#publishing-services-service-types)来演示应用程序服务器和 Web 服务器之间的流量如何流动。

本文重点在于对 Kubernetes 中的端口提供概念上的清晰性。

![](https://journal.hexmos.com/content/images/2024/01/5619f7f5b86e86757d5c64b9e279f71113dd43b566d01a0f0ebad87ff3b7467d.png)

### 1. 应用程序服务器端口(`8001`)

应用程序服务器端口

![](https://journal.hexmos.com/content/images/2024/01/d9f53003464074c76efb3cbf59d29befa3727f1a7d59fb19b83608942be912e1.png)

你可能已经知道了。

你在自己选择的框架中编写代码。

无论是 Django、Node、Gin 还是其他选项。

这些框架都有自己的运行命令。

例如，在 Django 中是 `python manage.py runserver`

我们看到 Django 应用可以在 8001 端口访问

### 2. 容器端口(`8001`)

应用程序服务器端口 -> 容器端口

![](https://journal.hexmos.com/content/images/2024/01/8c561d59b80476f3f7fa0bb11c878ee246eca5b7e99da8f1a62f99a913949712.png)

你可能也已经知道了。

在 Kubernetes 中，“容器”就像一个紧凑且便携的包，其中包含应用程序运行所需的一切。可以把它想象成一个包含应用程序、依赖项甚至所需环境的虚拟盒子。

现在，让我们谈谈端口。可以把它们想象成进入应用程序的门或入口。当我们创建 Docker 镜像(应用及其环境的快照)时，我们也决定应用程序应该使用哪个端口。如果应用在 `3000` 端口上运行，Docker 会暴露相同的端口。

![](https://journal.hexmos.com/content/images/2024/01/374ca3498c4c2e981af0f942c9aeba72c8c86f01cdf68b2e78c2bc99fa9ad45a-3.png)

启动 Docker 镜像时，它会转化成一个“容器” - 应用程序的运行实例。

由于我们已经暴露了一个端口，容器已准备好接受传入的流量并将其转发到内部的应用程序。

### 3. 目标端口(8001)

应用程序服务器端口 -> 容器端口 -> 目标端口

![](https://journal.hexmos.com/content/images/2024/01/ed925a45371bafb164498e301084296ff87d7f12473c7d523c6370997a1e7884.png)

目标端口指的是 Pod 上将流量转发到容器端口的端口。

目标端口如下图所示以红色高亮。

![](https://journal.hexmos.com/content/images/2024/01/cf97fb94b79f0a903b1fec6a1531361e6bde90717b708b5e08d156702906c6bb-3.png)

服务从内部服务端口将流量转发到 Pod 上的目标端口。

应用程序服务器端口、容器端口和目标端口都很直观和易于理解，因为它们都打算是相同的。这意味着服务将重定向流量到目标端口，该端口到达应用程序服务器。

**额外内容**

你可以使用 `kubectl` 命令查看 `Pod` 的描述

```bash
kubectl get pods
kubectl describe pod <pod-name>
```

目标端口可以在 `service.yaml` 中设置

```yaml
apiVersion: v1
kind: Service
metadata:
  name: fb-backends
spec:
  type: NodePort
  ports:
  - targetPort: 8001
    protocol: TCP
  selector:
    app: fb-backends
```

### 4. 内部服务端口(5001)

应用程序服务器端口 -> 容器端口 -> 目标端口 -> 内部服务端口

![](https://journal.hexmos.com/content/images/2024/01/8888b2e60e644e8a268baa294d074068756cde87b623243655b31cbeb1a33028.png)

内部服务端口默认为 `80`，通常称为服务的端口。

```bash
ubuntu@master:~$ kubectl get svc karma-daemon
NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S)
karma-daemon NodePort 10.106.199.236 <none> 80:32488/TCP，2121:32461/TCP
```

服务使用内部服务端口将流量路由到其负责的 Pod。

![](https://journal.hexmos.com/content/images/2024/01/9a0b2431695d17f5c5649052723af97d838bd4bc24d8b0e9812eeb07659900b3.png)

在我的示例中，我在 service.yaml 中将内部服务端口指定为 ka-port，并使用 5001 以便更清楚地理解。

```yaml
apiVersion: v1
kind: Service
metadata:
  name: fb-backends
spec:
  type: NodePort
  ports:
  - name: ka-port
    port: 5001
    targetPort: 8001
    protocol: TCP
  selector:
    app: fb-backends
```

```bash
ubuntu@master:~$ kubectl get svc fb-backends  
NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S)
fb-backends NodePort 10.101.234.168 <none> 5001:30904/TCP
```

红色高亮显示了服务的内部服务端口。

![](https://journal.hexmos.com/content/images/2024/01/2c9b4ae223952cddaf0bc693ed3e9871a58af4d3c2353a67d81fa45523296e89-3.png)

内部服务端口仅在 Kubernetes 集群内可用，而不在集群外。

在节点内发出内部服务端口请求的示例 <集群 IP>:<ISP> 

```bash
ubuntu@master:~$ curl 10.101.234.168:5001
{"success": false， "message": "Please refresh the page， if the problem persists， retry login."， "error": "Couldn't find the JWT in the 'Authorization' header."}
```

如果我尝试使用目标端口或节点端口访问集群 IP，则不起作用。

```bash
ubuntu@master:~$ curl 10.101.234.168:8001
^C
ubuntu@master:~$ curl 10.101.234.168:30904
^C
```

目标端口用于在 Pod 内部重定向流量，将流量导向容器的特定端口。另一方面，节点端口充当服务的外部暴露端口，可以在集群的所有节点上访问。

直接使用目标端口或节点端口访问集群 IP 会绕过内部服务端口(5001)建立的内部路由逻辑，导致连接失败。

结论是当流量到达节点端口(30904)时，它会重定向到内部服务端口(5001)，然后再将流量重定向到目标端口(8001)。

### 5. 节点端口(30904)

应用程序服务器端口 -> 容器端口 -> 目标端口 -> 内部服务端口 -> 节点端口

![](https://journal.hexmos.com/content/images/2024/01/182bd8e857a265d1e04148b5b7fa02d40885db26b10bd43bafde6e0e53f44cbd.png)

节点端口是应用程序服务器在集群外可访问的外部端口。

对于 NodePort 类型的服务，默认情况下，Kubernetes 为每个服务分配一个从 30000-32767 范围内的唯一节点端口。

红色高亮显示了为通信开放的节点端口。

![](https://journal.hexmos.com/content/images/2024/01/8d96a621f02def968e1f5ba1f41c6a4b13fc13bbe42b9afbf16687d41b9d0b89-3.png)

节点端口对于所有节点都是常量的。你可以简单地使用公共节点 IP 访问你的应用程序。curl <节点 IP>:<服务端口>

**额外内容**

还有其他类型的服务，如 Cluster IP、Load Balancer 和 External Name，每个服务用于不同的目的。

### 6. Web 服务器或负载均衡器端口(80/443)

应用程序服务器端口 -> 容器端口 -> 目标端口 -> 内部服务端口 -> 节点端口 -> Web 服务器端口

![](https://journal.hexmos.com/content/images/2024/01/5231021af81337e2bc90db07dad4c67b5f16f8142f1b8df022a98261e60772f2.png)

这是流量到达托管服务器的端口，可以直接到达，也可以通过负载均衡器如 [Azure LB](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-overview?ref=journal.hexmos.com) 或 [AWS ELB](https://aws.amazon.com/elasticloadbalancing/?ref=journal.hexmos.com) 到达。

这是 Ingress 控制器如 NGINX Ingress 控制器监听传入流量的端口。默认情况下，这些端口是 `80(HTTP)` 和 `443(HTTPS)`。

Ingress 控制器使用这些端口根据其配置规则将传入流量路由到 Kubernetes 集群内的相应服务。

黄色高亮的是 Web 服务器端口，传入流量被重定向到节点端口 30904。

例如，如果您已经为后端购买了域名并在云提供商中设置了路由，您可以为 Kubernetes 集群创建一个[代理服务器](https://www.nginx.com/blog/setting-up-nginx/?ref=journal.hexmos.com#proxy-server)。当一个请求到达您的服务器时，您可以设置规则将其重定向到特定的节点端口。

## API 请求的流程

外部流量 -> Web 服务器端口(80/443) -> 节点端口(30904) -> 内部服务端口(5001) -> 目标端口(8001) -> 容器端口(8001) -> 应用服务器端口(8001)

**外部流量**: 旅程从针对 Web 服务器端口(80/443)的外部流量开始，API 托管在那里。

**Web 服务器端口(80/443)**: Web 服务器，通常是一个 Nginx 实例，监听 80 和 443 端口。这些端口充当传入请求的入口点。

**节点端口(30904)**: 外部流量然后被路由到节点端口(30904)。节点端口在 Kubernetes 集群中的每个节点上都是可访问的，提供一致的入口点。

**内部服务端口(5001)**: 请求通过内部服务端口进展，充当集群内的网关，将流量导向预期的服务。 

**目标端口(8001)**: 内部服务将请求转发到目标端口，指定公开应用服务的端口。

**容器端口(8001)**: 目标端口将请求重定向到 Docker 容器端口。在容器内，应用程序服务器被配置为监听此特定端口。

**应用服务器端口(8001)**: 当请求到达 Docker 容器内的应用程序服务器端口(8001)时，旅程结束，应用程序在那里处理该请求。

## 结论

文章中提到的端口是示例，用于显示端口通信是如何完成的，可以根据您的需要进行调整。

文章使用来自 [k9s](https://github.com/derailed/k9s?ref=journal.hexmos.com) 的快照，这是一个在实时查看 Kubernetes 集群的工具，以帮助您更好地理解并获得实用的见解。

想了解更多关于 Kubernetes、AI/ML 和其他有趣技术主题的信息吗？
