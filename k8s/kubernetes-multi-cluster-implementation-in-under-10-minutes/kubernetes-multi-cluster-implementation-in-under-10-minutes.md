<!--
# 十分钟实现Kubernetes多集群
https://miro.medium.com/v2/resize:fit:828/format:webp/1*UaN5V74HnL16wY-nHcTANQ.png
-->

使用 Cilium ClusterMesh 和 KIND 在 10 分钟内搭建 Kubernetes 多集群网格

译自 [Kubernetes multi-cluster implementation in under 10 minutes](https://itnext.io/kubernetes-multi-cluster-implementation-in-under-10-minutes-2927952fb84c) 。

## 摘要

完成这个实验后，您将在本地开发机器上用容器运行一个多集群 Kubernetes 环境。

## 我们需要什么？

> **强烈**建议您在 Linux 机器上运行这个实验，我选择的是 Ubuntu，因为 MacOS 上的 Docker Desktop 没有暴露 docker 网络到主机，解决这个的不便需要的工作量和复杂度超出了本文的范围。

* [kind](https://sigs.k8s.io/kind) 是一种用于在本地运行 Kubernetes 集群的工具，它通过模拟 Docker 容器作为节点。kind 最初是为了测试 Kubernetes 本身而设计的，但也可用于本地开发或 CI 流水线:


```bash
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

* [Helm](https://helm.sh/)，Kubernetes 的标准包管理器:

```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 
chmod 700 get_helm.sh
./get_helm.sh
```

* Cilium CLI，一个用于安装、管理和排查运行Cilium CNI的Kubernetes集群的命令行工具，如其GitHub仓库中所述:

```bash
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{，.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{，.sha256sum} 
```

> 您不应该混合使用Cilium CLI的**helm模式**来启用ClusterMesh或者连接通过Cilium CLI配置的集群——后者工作在**经典模式**中——因为这两种模式是**不兼容**的。
>
> 我们将使用**Helm**而不是Cilium CLI来安装Cilium。在我们需要运行一些连接性测试时，Cilium CLI将会派上用场。


## 什么是 Cilium ClusterMesh？

**ClusterMesh** 是 Cilium 的多集群实现。它将网络数据路径扩展到多个 Kubernetes 集群。它允许不同连接集群中的端点之间进行通信，同时提供完整的策略实施。ClusterMesh 提供了(摘自官方文章“[Cilium 多集群深入解析](https://cilium.io/blog/2019/03/12/clustermesh/)”):

* **跨多个 Kubernetes 集群的 Pod IP 路由**，通过隧道或直接路由实现原生性能，无需任何网关或代理。
* **透明的服务发现**，支持标准 Kubernetes 服务和 `coredns/kube-dns`。
* **跨多个集群的网络策略实施**。策略可以指定为 Kubernetes 的 `NetworkPolicy` 资源或扩展的 `CiliumNetworkPolicy` CRD。
* **所有节点之间通信的透明加密**，无论是本地集群还是跨集群边界。

## Cilium ClusterMesh 使用案例

多集群 Kubernetes 设置的常见场景和应用包括需要高可用性、故障隔离、可扩展性和地理分布的情况:

* 高可用性是我们最常遇到的使用案例。在这种场景下，我们在多个区域或可用区中运行 Kubernetes 集群，每个服务的副本都部署在每个集群中。如果出现故障，请求可以平滑地重定向到其他集群。

> **本实验将专注于这种使用案例。** 下面提到的其他使用案例旨在让你更好地理解 ClusterMesh 解决的实际问题和应用场景，你可以跳过不看。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*kJU71Spc6aGq3gLq-NYfgw.png)

* 在多租户 Kubernetes 集群中，正确隔离租户之间是关键目标和挑战。为实现这个目标，租户集群连接到一个共享服务集群，但彼此之间不直接连接。如密码管理、日志记录或监控等常见服务通过所有租户都连接的共享集群向所有租户提供。这避免了在每个租户中单独维护这些服务的额外运维开销。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*sGgepwvMmRa4JMchPhHfIA.png)

* 与无状态服务相比，有状态服务由于其存储依赖性而表现出更高的复杂性。迁移有状态服务需要迁移它们各自的存储。通过仅针对无状态和有状态应用程序运行专用集群，我们可以将存储依赖性复杂度限制在较少数量的集群中，因为有状态集群将与无状态集群隔离。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*FOc7AWTT7-CiYn0OHc1UEw.png)

## 安装 Kubernetes 集群

如前所述，我们将模拟高可用性场景。为此，我们将在每个区域运行一个 Kubernetes 集群，假设有两个区域: **region-athens** 和 **region-hurup**。

让我们先搭建 **region-athens**。每个集群都需要一个清单，该清单将指示 kind 如何设置和配置该集群。每个集群由 1 个 master 和 3 个 worker 节点组成。我们禁用默认的 CNI `disableDefaultCNI`，因为我们希望使用 Cilium CNI 来设置这些集群，因此我们也禁用了 `kubeProxyMode`。另外，我们为每个集群的 Pod 和服务子网提供唯一的 CIDR:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
- role: worker
networking:
  disableDefaultCNI: true
  kubeProxyMode: none
  podSubnet: "10.0.0.0/16"
  serviceSubnet: "10.1.0.0/16"
```


> 将此文件保存为 `region-athens` 文件夹中的 `kind.yaml`。由于我们很快就要创建一系列集群，所以请为每个区域的构件保留一个单独的文件夹。

现在，我们可以创建 **region-athens**:

![](https://miro.medium.com/v2/resize:fit:720/0*EsrMLm4t4d10JpK_)

*图片来自 [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral) 的 [Vanessa Linzenbold](https://unsplash.com/@linziv?utm_source=medium&utm_medium=referral)*

```bash
kind create cluster --name region-athens --config=region-athens/kind.yaml
```

现在该建立 **region-hurup** 了。同样将这个文件保存为 `region-hurup` 文件夹中的 `kind.yaml`。

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker 
- role: worker
- role: worker
networking:
  disableDefaultCNI: true
  kubeProxyMode: none
  podSubnet: "10.2.0.0/16"
  serviceSubnet: "10.3.0.0/16"
```

然后让我们创建 **region-hurup**:

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*ScGRUFUU5iCb_o0SbFIGNQ.jpeg)

*图片来自 Wikipedia 的 [Claude David](https://commons.wikimedia.org/wiki/User:Bococo)*

```bash
kind create cluster --name region-hurup --config=region-hurup/kind.yaml
```

> 在部署 Cilium 之前，集群节点状态将保持 `NotReady`。


## 安装 Cilium CNI

你可能还记得，我们已经禁用了 kind 自带的默认 CNI。我们将在每个集群中安装 Cilium。首先获取我们将需要的 helm 仓库和 docker 镜像:

```bash
helm repo add cilium https://helm.cilium.io/
helm repo update 
docker pull quay.io/cilium/cilium:v1.14.2
```

对于 **region-athens** 需要:

```bash
kubectl config use-context kind-region-athens
kind load docker-image quay.io/cilium/cilium:v1.14.2 --name region-athens

helm upgrade --install cilium cilium/cilium --version 1.14.2 \
   --namespace kube-system \
   --set cluster.name=region-athens \  
   --set cluster.id=1 \
   --set image.pullPolicy=IfNotPresent \
   --set ipam.mode=kubernetes \
   --set kubeProxyReplacement=strict \
   --set nodeinit.enabled=true \
   --set hostServices.enabled=false \
   --set externalIPs.enabled=true \
   --set nodePort.enabled=true \
   --set hostPort.enabled=true \
   --set k8sServiceHost=region-athens-control-plane \
   --set k8sServicePort=6443 \
   --set hubble.enabled=true \
   --set hubble.relay.enabled=true \
   --set hubble.ui.enabled=true \
   --set hubble.ui.service.type=LoadBalancer \
   --set ipv4NativeRoutingCIDR=10.0.0.0/8
```


> 我们在每个工作节点上额外预加载 Cilium 镜像。

对于 **region-hurup** 需要:

```bash
kubectl config use-context kind-region-hurup
kind load docker-image quay.io/cilium/cilium:v1.14.2 --name region-hurup

helm upgrade --install cilium cilium/cilium --version 1.14.2 \
   --namespace kube-system \
   --set cluster.name=region-hurup \  
   --set cluster.id=2 \
   --set image.pullPolicy=IfNotPresent \
   --set ipam.mode=kubernetes \
   --set kubeProxyReplacement=strict \
   --set nodeinit.enabled=true \
   --set hostServices.enabled=false \
   --set externalIPs.enabled=true \
   --set nodePort.enabled=true \
   --set hostPort.enabled=true \
   --set k8sServiceHost=region-hurup-control-plane \
   --set k8sServicePort=6443 \
   --set hubble.enabled=true \
   --set hubble.relay.enabled=true \
   --set hubble.ui.enabled=true \
   --set hubble.ui.service.type=LoadBalancer \
   --set ipv4NativeRoutingCIDR=10.0.0.0/8 
```

> Cilium 必须在每个集群中配置一个本机路由 CIDR `ipv4NativeRoutingCIDR`，该 CIDR 覆盖**所有**连接集群的**所有** PodCIDR 范围。我们的集群 CIDR 从 `10.0.0.0/8` 私有地址空间分配。

等待所有 Cilium 相关 pod 达到 `Running` 状态，或者通过 Cilium CLI 验证 Cilium 的安装:

```bash
cilium status --wait
```

## 安装 MetalLB

首先让我们检索 kind 集群使用的 Docker 网络:

```bash
docker network inspect kind | jq -r '.[].IPAM.Config|.[0]|.Subnet'
```

在我的例子中，这将返回`172.19.0.0/16`。

> 请记住:
>
> - 所有集群中的节点必须使用每个节点配置的 InternalIP 之间有 IP 连接。通常通过在每个集群的节点的网络之间建立对等或 VPN 隧道来满足此要求。  
>
> - 集群之间的网络必须允许集群间通信。

我们将从这个 CIDR 中选择一个子网，并在每个区域的两个集群之间进行分割。对于这个实验，我选择了 `172.19.255.0/24`，并将段 `172.19.255.1–172.19.255.100` 分配给 **region-athens**，将 `172.19.255.101–172.19.255.200` 分配给 **region-hurup**。现在让我们使用这些信息并为每个区域部署负载均衡器。

对于 **region-athens**:

安装清单 `metallb-native.yaml`(见下文)中**不包含**配置文件。MetalLB 的组件虽然会启动，但在我们以 `IpAddressPool` 清单的形式在 `region-athens/ipaddresspool.yaml` 中提供所需的配置之前，它们将保持空闲状态，这是版本 0.13.7 中引入的一种新 `Kind`，取代了使用 `ConfigMap` 来配置地址池配置的旧方法。

```yaml
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: default-pool
  namespace: metallb-system
spec:
  addresses:
  - 172.19.255.1-172.19.255.100
```

我们将使用 **层 2** 配置。层 2 模式是最简单的配置，我们只需要**一系列 IP 地址**。如官方文档所述:

> Layer 2 模式不需要将 IP 绑定到工作节点的网络接口上。它通过直接响应本地网络上的 ARP 请求来实现，以向客户端提供机器的 MAC 地址。

让我们创建文件 `region-athens/l2advertisement.yaml`:


```yaml
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: default
  namespace: metallb-system
spec:
  ipAddressPools:
  - default-pool
```

现在让我们将所有这些清单打包在一起:

```bash
kubectl config use-context kind-region-athens  

kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.7/config/manifests/metallb-native.yaml
sleep 240

kubectl apply -f region-athens/ipaddresspool.yaml
kubectl apply -f region-athens/l2advertisement.yaml
```


> 提供足够的时间来配置控制器和 speakers，`sleep 240`，然后再配置。

对于 **region-hurup**，遵循相同的步骤，创建 `region-hurup/ipaddresspool.yaml`:

```yaml
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: default-pool
  namespace: metallb-system
spec:
  addresses:
  - 172.19.255.101-172.19.255.200
```

创建 `region-hurup/l2advertisement.yaml`:

```yaml
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: default
  namespace: metallb-system
spec:
  ipAddressPools:
  - default-pool
```

然后部署 MetalLB:

```bash
kubectl config use-context kind-region-hurup

kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.7/config/manifests/metallb-native.yaml
sleep 240

kubectl apply -f region-hurup/ipaddresspool.yaml
kubectl apply -f region-hurup/l2advertisement.yaml
```

有关 Kubernetes 和 MetalLB 的更多信息，你可以查看下面的文章: [Provision a Network Load Balancer on Kubernetes with MetalLB](https://akyriako.medium.com/load-balancing-with-metallb-in-bare-metal-kubernetes-271aab751fb8) 。


## 启用 Cilium ClusterMesh

每个集群必须分配一个唯一的名称**和**一个数字集群 ID(1-255)。我们在安装 Cilium 时通过 Helm 参数 `cluster.name` 和 `cluster.id` 分配了这些属性:

```bash
...
--set cluster.name=region-hurup \
--set cluster.id=2 \
...
```

> 如果我们在具有现有工作负载的集群中更改集群 ID 和/或集群名称，**所有工作负载**需要**重新启动**。集群 ID 用于生成安全标识，为了在集群之间建立访问，它需要被重新创建。

我们将使用 Cilium CLI 在两个集群上启用 ClusterMesh。将部署组件 `clustermesh-apiserver`，它将创建所有必需的证书并将它们部署为 Kubernetes secrets。它还将尝试确定哪种服务类型对于负载均衡器暴露 ClusterMesh 控制平面给其他集群将是最佳的。

```bash
cilium clustermesh enable --context kind-region-athens --service-type LoadBalancer
cilium clustermesh enable --context kind-region-hurup --service-type LoadBalancer
```

你可以像这样验证每个请求的状态:

```bash
cilium clustermesh status --context kind-region-athens --wait
```

等待 ClusterMesh 在两个集群中都启用。

## 连接集群

最后一个配置步骤是连接两个区域中的集群:

```bash
cilium clustermesh connect --context kind-region-athens --destination-context kind-region-hurup
```

> 你不需要为每个集群单独运行命令，上述命令将在两个方向上建立连接。

你可以像这样验证每个请求的状态:

```bash
cilium clustermesh status --context kind-region-athens --wait
```

等待 ClusterMesh 在两个集群中都启用，然后我们通过 Cilium CLI 运行一整套连接性测试:

```bash
cilium connectivity test --context kind-region-athens --multi-cluster kind-region-hurup
```

等待它完成，这需要一些时间。如果一切顺利，你的 mesh 应该通过所有的连接性测试:

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*yToNKraSyEqnJRF5hpRrlQ.png)

就是这样！如果你发现这些信息有用，别忘了在这篇文章下面点赞，并关注我的账号获取有关 Kubernetes 的更多内容。敬请期待......