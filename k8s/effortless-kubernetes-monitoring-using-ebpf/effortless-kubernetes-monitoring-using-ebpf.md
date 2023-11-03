<!--
# 使用eBPF实现Kubernetes无缝监控和瓶颈检测
https://ddosify.com/assets/images/00_Effortless_Kubernetes_Monitoring_and_Bottleneck_Detection_using_eBPF-9084af8e2d2753591581dccbf6d94687.png
 -->
 
本文将介绍如何使用 eBPF 技术监控 Kubernetes 集群、检测性能瓶颈，并自动生成 K8s 服务拓扑图，无需服务重启、代码检测或 sidecar。我们将从 [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-mwvnujtgjedjy?sr=0-1&ref_=beagle&applicationId=AWSMPContessa) 一键部署 Ddosify 自托管平台。使用 [eksctl](https://eksctl.io/) 在 AWS 创建 Kubernetes 集群，并在集群中部署示例应用。我们的 [eBPF 代理 Alaz](https://github.com/ddosify/alaz) 从 Kubernetes 集群收集指标和网络流量数据，发送到 Ddosify 自托管平台。然后利用 Ddosify 平台监控集群和检测瓶颈。本文用到的所有文件可在[这里](https://github.com/ddosify/blog_examples/tree/main/006_effortless_kubernetes_monitoring_using_ebpf)找到。

译自 [Effortless Kubernetes Monitoring and Bottleneck Detection using eBPF](https://ddosify.com/blog/effortless-kubernetes-monitoring-using-ebpf/) 。作者: Fatih Baltaci ，Ddosify 项目维护者。


前提条件:

- [AWS 账号](https://aws.amazon.com/)
- [AWS CLI](https://aws.amazon.com/cli/)
- [eksctl](https://eksctl.io/) - 在 AWS 创建 Kubernetes 集群
- [kubectl](https://kubernetes.io/docs/tasks/tools/) - 管理 Kubernetes 集群
- [Ddosify 自托管平台](https://aws.amazon.com/marketplace/pp/prodview-mwvnujtgjedjy?sr=0-1&ref_=beagle&applicationId=AWSMPContessa) - 监控 Kubernetes 集群
- [Ddosify 引擎](https://github.com/ddosify/ddosify/tree/master/engine_docs)(可选) - 为 Kubernetes 集群生成负载
- [Helm](https://helm.sh/)(可选) - 将 Alaz 安装到 Kubernetes 集群

## 什么是 eBPF？

eBPF(extended Berkeley Packet Filter)是一项允许在 Linux 内核中运行沙箱化程序的技术，无需修改内核源码或加载内核模块。eBPF 程序使用限定的 C 语言编写，编译成字节码，经验证和转换后可安全在内核中执行。验证器确保程序安全运行，不会导致内核崩溃，并防止无限循环。eBPF 程序可以附加到不同内核钩子，在事件发生时运行。例如，可以将 eBPF 程序绑定到 `sys_enter_connect` 跟踪点，检测 TCP 连接。eBPF 应用场景包括跟踪、网络、安全等。更多 eBPF 信息见[这里](https://ebpf.io/)。

## Ddosify 自托管是什么?

![](https://ddosify.com/assets/images/03_ddosify_find_bottleneck-2c960ee38f325da998b4623500d92753.png)

[Ddosify 自托管](https://github.com/ddosify/ddosify/tree/master/selfhosted)是一个可观测性和性能测试平台，它能够对 Kubernetes 集群进行实时监控。使用 Ddosify 自托管，您可以在 5 分钟内 开始监测 Kubernetes 集群的瓶颈，无需额外的工作。Ddosify 自托管平台可以实时显示 Kubernetes 集群的运行状态，帮助您检测诸如慢 SQL 查询、5xx 错误、空闲 K8s 服务、慢 HTTP 请求、CPU、内存、磁盘和网络等各类瓶颈信号。它还原生集成了 Ddosify 性能测试解决方案，您可以对 Kubernetes 服务进行性能测试，找出其中的瓶颈。

## Ddosify eBPF 代理程序(Alaz)是什么?

我们的 [eBPF 代理程序 Alaz](https://github.com/ddosify/alaz) 是一个开源工具，它可以通过 eBPF 收集 Kubernetes 集群的指标和网络流量，无需代码改动或服务重启，并将数据发送到 Ddosify 自托管平台。与 sidecar 不同，它不会给集群增加额外开销。Alaz 可以轻松以 DaemonSet 形式部署，资源消耗最高只有 1 个 CPU 内核和 1Gi 内存。

在 [Alaz eBPF 目录](https://github.com/ddosify/alaz/tree/master/ebpf)下，您可以找到使用 [libbpf](https://github.com/libbpf/libbpf) 编写的 C 语言 eBPF 程序。这些程序会绑定到内核追踪点和 uprobes 上，以捕获 Kubernetes 集群上的网络流量。Alaz 的 eBPF 程序使用 [Cilium 的 bpf2go](https://github.com/cilium/ebpf/tree/main/cmd/bpf2go) 包进行编译，它会生成 Go 语言的辅助文件来与 eBPF 程序交互。我们嵌入这些辅助文件，并使用 [Cilium 的 eBPF 包](https://github.com/cilium/eBPF)将它们加载到内核中。您可以在[这里](https://github.com/ddosify/alaz/blob/master/Alaz-Architecture.md)找到关于 Alaz 架构的更多细节。

## 在 AWS 上部署 Ddosify 自托管

![](https://ddosify.com/assets/images/01_ddosify_effortless_kubernetes_monitoring_aws-10fb0afe10b8c3ef3c88c08458de8473.png)

首先，我们将使用 [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-mwvnujtgjedjy?sr=0-1&ref_=beagle&applicationId=AWSMPContessa) 在 AWS 上部署 Ddosify 自托管。您也可以在非 AWS 服务器上安装 Ddosify 自托管平台，详见[文档](https://github.com/ddosify/ddosify/blob/master/selfhosted/README.md)。

点击 `Continue to Subscribe` 按钮，然后点击 `Configure This Software` 。区域可以选择任何接近您的区域，Ddosify 支持所有 AWS 区域。这里我们使用 `US West (N. California)`。点击 `Continue to Launch` 按钮。

- **Choose Action:** 从网站启动
- **EC2 Instance Type:** c5.2xlarge(也支持 c5.xlarge 和 c5.2xlarge)
- **VPC Settings:** 保留默认 VPC
- **Subnet Settings:** 保留默认子网
- **Security Group Settings:** 点击 `Create New Based On Seller Settings`。Ddosify 使用 22 端口 SSH 访问，8014 端口 Ddosify 平台。
  - 命名安全组并添加描述
  - 点击 `Save` 按钮
- **Key Pair Settings:** 选择现有密钥对或创建新密钥对
- 点击 `Launch` 按钮

现在您可以在 [AWS Subscriptions Page](https://us-east-1.console.aws.amazon.com/marketplace/home#/subscriptions) 看到订阅。点击 `Ddosify - Effortless Kubernetes Monitoring` 的 `Manage` 按钮。点击操作按钮，然后点击查看实例。点击 `Access Software` 按钮，您就可以看到 Ddosify 自托管平台了。

![](https://ddosify.com/assets/images/02_ddosify_dashboard-83118b1a4d887d63a9c06aebbe11494e.png)

## 使用 eksctl 在 AWS 创建 Kubernetes 集群

为了测试，我们将使用 eksctl 在 AWS EKS 上创建一个 Kubernetes 集群。您也可以将 Ddosify 自托管部署到其他 K8s 平台如 GKE、AKS、minikube、k0s 等。您可以在此查看有关 eksctl 的更多信息。首先，我们创建一个 K8s 集群配置文件:

**eksctl_cluster.yaml**

```yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: ddosify-k8s-test-blog
  region: us-west-1
vpc:
  clusterEndpoints:
    publicAccess: true
    privateAccess: false

managedNodeGroups:
  - name: managed-ng-ddosify-k8s-test-blog
    amiFamily: "AmazonLinux2"
    instanceType: c5.large
    minSize: 1
    maxSize: 3
    desiredCapacity: 2
    volumeSize: 30
    iam:
      attachPolicyARNs:
        - arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy
        - arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy
        - arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
      withAddonPolicies:
        ebs: true
addons:
- name: vpc-cni
  serviceAccountRoleARN: arn:aws:iam::aws:policy/AmazonEKSCNIAccess
- name: aws-ebs-csi-driver
  serviceAccountRoleARN: arn:aws:iam::aws:policy/AmazonEKS_CSI_Driver
```

这将在 AWS 上创建一个包含两个节点的 Kubernetes 集群。现在使用 eksctl 创建集群:

```bash
eksctl create cluster -f cluster.yaml
```

> 注意: 您需要有 AWS 账户权限才能创建 Kubernetes 集群，详见 eksctl 文档。

集群创建后，更新 `KUBECONFIG` 环境变量指向新集群:

```bash
aws eks update-kubeconfig --name ddosify-k8s-test-blog --region us-west-1
```

现在检查 Kubernetes 集群节点，应该会看到两个节点:

```bash
kubectl get nodes
```

## 将示例应用程序部署到 Kubernetes 集群

我们将几个简单的微服务和 PostgreSQL 部署到 Kubernetes 集群中。

**服务:**

- `testserver` - 一个简单的 Python Django Web 应用，用于获取货币、进行汇率兑换等。它使用 PostgreSQL 作为数据库。
- `currencies` - 一个简单的 Python Flask Web 应用，返回货币汇率。`testserver` 会通过 HTTP 请求调用 `currencies` 来获取汇率。
- `postgres` - PostgreSQL 数据库。

**部署:**

运行以下命令将示例服务部署到 Kubernetes 集群中，它会创建一个 `testserver` 命名空间并在其中部署服务:


```bash
kubectl apply -f https://raw.githubusercontent.com/ddosify/blog_examples/main/006_effortless_kubernetes_monitoring_using_ebpf/sample_apps.yaml
```

几秒后就能看到所有 pod 运行起来:

```bash
kubectl get pods -n testserver
```

通过端口转发访问 `testserver` 服务:

```bash
kubectl port-forward --namespace testserver service/testserver-service 8200:8200
```

现在可以从本地访问 `testserver` 服务。获取货币汇率可以请求 `/currencies/` 端点，`testserver` 会通过 HTTP 调用 `currencies` 获取汇率:

```bash
curl http://localhost:8200/currencies/
```

获取两种货币汇率可以请求 `/exchange_rate/` 端点:

```bash
curl http://localhost:8200/exchange_rate/USD/EUR/
```

它还有一个用来测试 HTTP 状态码的端点，会返回指定的状态码:

```bash
curl http://localhost:8200/status/500/
```

## 向 Kubernetes 集群生成负载

我们将使用 [Ddosify Engine](https://github.com/ddosify/ddosify/tree/master/engine_docs) 对部署到 Kubernetes 集群的示例应用程序生成负载。Ddosify Engine 是一个开源的高性能负载测试工具。使用以下命令安装:

```bash
curl -sSfL https://raw.githubusercontent.com/ddosify/ddosify/master/scripts/install.sh | sh
```

安装后，可以运行以下命令向 `testserver` 生成负载，它会在10秒内向 `/currencies/` 端点发送 1000 个 GET 请求:

```bash
ddosify -t http://localhost:8200/currencies/ -n 1000 -d 10 -m GET
```

> 提示: 使用 `--debug` 标志可以发送单个请求并打印 curl 风格的详细输出。

在 10 秒内向 `/exchange_rate/` 端点发送 200 个 GET 请求:

```bash
ddosify -t http://localhost:8200/exchange_rate/USD/EUR/ -n 200 -d 10 -m GET
```

在 10 秒内向 `/status/` 端点发送 100 个 GET 请求，该端点会返回指定的 HTTP 状态码。Ddosify Engine 会用动态参数发送随机状态码:

```bash
ddosify -t http://localhost:8200/status/{{_randomInt}}/ -n 100 -d 10 -m GET
```

## 使用 Ddosify 自托管和 Alaz 监控 Kubernetes 集群

我们将使用 Ddosify 自托管和 Alaz 来监控 Kubernetes 集群。首先在 Ddosify 自托管的左侧菜单点击 `Observability`，然后点击 `+ Add Cluster`。命名集群并点击 `Save`。

集群创建后，您会看到 Alaz 的安装说明。

![](https://ddosify.com/assets/images/04_ddosify_alaz_instructions-b10c53a46f21bb4ae4dd84094a61cfaf.png)

我们将使用 `helm` 安装方法，您也可以用 kubectl 安装。这些命令会通过设置 `MONITORING_ID` 和 Ddosify 自托管 API 地址在集群中安装 Alaz。`MONITORING_ID` 是集群在 Ddosify 自托管上的唯一标识。Alaz 会把指标和服务流量发送到这个 API 地址。详细安装说明见 [Alaz 文档](https://github.com/ddosify/alaz#-for-ddosify-self-hosted)。

Alaz eBPF 代理以 DaemonSet 形式在集群上运行，它会收集指标和网络流量发送到 Ddosify 自托管平台，不需要改动应用代码或重启服务，也不会像 sidecar 一样增加集群开销。

几秒后就能在 Ddosify 自托管看到集群。在“指标”标签页可以看到 CPU、内存、磁盘和网络的使用情况。

![](https://ddosify.com/assets/images/05_ddosify_k8s_metrics-c1714cff3b9ad19f9984edcf9dcb9e87.png)

在 `Service Map` 标签页可以看到服务映射。可以看到服务、部署、pod 等资源及其之间的关系。资源间的线表示流量，线越粗表示流量越大，线越红表示延迟越高。鼠标移到线上可以查看资源间的延迟和每秒请求数。

![](https://ddosify.com/assets/images/06_ddosify_k8s_service_map-a990c9388104e453c5c64628e5d4d30f.png)

还可以看到资源的详细信息和各类关键指标，如慢 SQL 查询、5xx 错误、空闲服务、慢 HTTP 请求、CPU、内存、磁盘和网络等。

![](https://ddosify.com/assets/images/07_ddosify_k8s_resource_details-08e88f2c55d84c23ef4fdbdf11d206b6.png)

因此可以用 Ddosify 自托管平台和 Alaz eBPF 代理轻松地在 Kubernetes 集群上发现瓶颈，例如某个服务响应过慢导致其它服务的延迟增加，可以在 Ddosify 自托管平台上看到慢 HTTP 请求，或者看到慢 SQL 查询和 5xx 错误等。

## 总结

本文我们使用 eBPF 来监控 Kubernetes 集群和检测瓶颈。我们从 AWS Marketplace 一键部署了 Ddosify 自托管平台。我们的 eBPF 代理 Alaz 可以在不需要代码改动或重启服务的情况下从集群收集指标发送到 Ddosify 自托管平台。然后我们使用 Ddosify 自托管平台来监控集群和检测瓶颈。

如果您觉得 Ddosify 自托管平台有用，请为我们的 [GitHub 仓库](https://github.com/ddosify/ddosify)点星。欢迎查看我们的 [Ddosify eBPF 代理 Alaz](https://github.com/ddosify/alaz)。
