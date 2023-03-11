# k8s.gcr.io 重定向到 registry.k8s.io - 你需要知道的

翻译自 [k8s.gcr.io Redirect to registry.k8s.io - What You Need to Know](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/) ，查看原文看更多链接。

作者：Authors: Bob Killen (Google), Davanum Srinivas (AWS), Chris Short (AWS), Frederico Muñoz (SAS Institute), Tim Bannister (The Scale Factory), Ricky Sadowski (AWS), Grace Nguyen (Expo), Mahamed Ali (Rackspace Technology), Mars Toktonaliev (independent), Laura Santamaria (Dell), Kat Cosgrove (Dell)

3 月 20 日星期一，k8s.gcr.io 的 registry 将重定向到社区拥有的 registry.k8s.io 。

## TL;DR：对这个变化你需要知道哪些 

* 3 月 20 日星期一，来自旧的 k8s.gcr.io 的 registry 的流量将重定向到 registry.k8s.io，最终目标是关闭 k8s.gcr.io。
* 如果您在受限环境中运行，并应用严格的域名或 IP 地址访问策略，仅限于 k8s.gcr.io，则在 k8s.gcr.io 开始重定向到新注册中心后，镜像拉取将无法运行。
* 一小部分非标准客户端不处理镜像注册表的 HTTP 重定向，需要直接指向 registry.k8s.io。
* 重定向是帮助用户进行切换的权宜之计。已弃用的 k8s.gcr.io 注册表将在某个时候被淘汰。请尽快更新您的清单以指向 registry.k8s.io。
* 如果您托管自己的镜像 registry ，您也可以在那里复制您需要的镜像，以减少到社区拥有的 registry 的流量。
* 如果您认为您可能会受到影响，或者想了解有关此更改的更多信息，请继续阅读。

## 如何检查我是否受到影响？

要测试与 registry.k8s.io 的连接并能够从那里拉取镜像，这里有一个示例命令，可以在您选择的命名空间中执行：

```bash
kubectl run hello-world -ti --rm --image=registry.k8s.io/busybox:latest --restart=Never -- date
```

当您运行上面的命令时，如果一切正常，会发生以下情况：

```bash
$ kubectl run hello-world -ti --rm --image=registry.k8s.io/busybox:latest --restart=Never -- date
Fri Feb 31 07:07:07 UTC 2023
pod "hello-world" deleted
```

## 如果我受到影响，我会看到什么样的错误？ 

错误可能取决于您使用的容器运行时类型，以及您路由到的端点，但它应该出现如 `ErrImagePull` 、 `ImagePullBackOff` 或容器无法创建并显示警告 `FailedCreatePodSandBox` 。

下面是一个示例错误消息，显示代理部署由于未知证书而无法拉取：

```bash
FailedCreatePodSandBox: Failed to create pod sandbox: rpc error: code = Unknown desc = Error response from daemon: Head “https://us-west1-docker.pkg.dev/v2/k8s-artifacts-prod/images/pause/manifests/3.8”: x509: certificate signed by unknown authority
```

## 哪些镜像会受到影响？ 

k8s.gcr.io 上的所有镜像都将受到此更改的影响。 k8s.gcr.io 托管许多 Kubernetes 版本之外的镜像。大量的 Kubernetes 子项目也在那里托管他们的镜像。例如 `dns/k8s-dns-node-cache` 、 `ingress-nginx/controller` 和 `node-problem-detector/node-problem-detector` 镜像。

## 我受到了影响。我应该怎么办？ 

对于在受限环境中运行的受影响用户，最好的选择是将所需的镜像复制到私有 registry 或在其注册表中配置 pull-through 缓存。

有几种工具可以在注册表之间复制镜像； crane 是其中一种工具，可以使用 `crane copy SRC DST` 将镜像复制到私有 registry 。还有特定于供应商的工具，例如谷歌的 gcrane ，执行类似的功能，但针对他们的平台进行了简化。

## 我如何找到哪些镜像正在使用遗留注册表并修复它们？ 

**选项 1**：请参阅我们[之前的博文](https://kubernetes.io/blog/2023/02/06/k8s-gcr-io-freeze-announcement/#what-s-next)中的一行 kubectl 命令：

```bash
kubectl get pods --all-namespaces -o jsonpath="{.items[*].spec.containers[*].image}" |\
tr -s '[[:space:]]' '\n' |\
sort |\
uniq -c
```

**选项 2**：已经开发了一个名为 community-images 的 kubectl krew 插件，它将扫描和报告使用 k8s.gcr.io 端点的所有镜像。

如果你安装了 krew，你可以安装它：

```bash
kubectl krew install community-images
```

并生成一份报告：

```bash
kubectl community-images
```

有关安装和示例输出的替代方法，请查看存储库：[kubernetes-sigs/community-images](https://github.com/kubernetes-sigs/community-image)。

**选项 3**：如果您无法直接访问集群或管理许多集群——最好的方法是在您的清单和镜像中搜索“k8s.gcr.io”。

**选项 4**：如果您希望阻止基于 k8s.gcr.io 的镜像在您的集群中运行，AWS EKS 最佳实践存储库中提供了 Gatekeeper 和 Kyverno 的示例策略，这将阻止它们被拉取。您可以将这些第三方策略用于任何 Kubernetes 集群。

**选项 5**：作为**最后**一个可能的选项，您可以使用 [Mutating Admission Webhook](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#what-are-admission-webhooks) 来动态更改镜像地址。在您的清单更新之前，这应该只被视为权宜之计。您可以在 [k8s-gcr-quickfix](https://github.com/abstractinfrastructure/k8s-gcr-quickfix) 中找到（第三方）Mutating Webhook 和 Kyverno 策略。


## 为什么 Kubernetes 更改为不同的镜像 registry ？ 

k8s.gcr.io 托管在专为 Kubernetes 项目设置的自定义 Google Container Registry (GCR) 域中。自项目启动以来，这一直运作良好，我们感谢谷歌提供这些资源，但今天，还有其他云提供商和供应商希望托管镜像，为他们平台上的人们提供更好的体验。除了谷歌去年再次承诺捐赠 300 万美元以支持该项目的基础设施外，亚马逊网络服务公司还在底特律的 Kubecon NA 2022 主题演讲中宣布了一项匹配捐赠。这将为用户提供更好的体验（更近的服务器 = 更快的下载），同时减少 GCR 的出口带宽和成本。

有关此更改的更多详细信息，请查看 [registry.k8s.io：更快、更便宜且普遍可用 (GA)](https://kubernetes.io/blog/2022/11/28/registry-k8s-io-faster-cheaper-ga/)。

## 为什么要设置重定向？ 

该项目在去年发布了 [1.25 版本后切换到了 registry.k8s.io](https://kubernetes.io/blog/2022/11/28/registry-k8s-io-faster-cheaper-ga/)；然而，大部分镜像拉取流量仍然指向旧端点 k8s.gcr.io。作为一个项目，这对我们来说是不可持续的，因为它没有利用其他供应商捐赠给该项目的资源，而且由于为该流量提供服务的成本，我们面临资金耗尽的危险。

重定向将使项目能够利用这些新资源，从而显着降低我们的出口带宽成本。我们预计此更改只会影响在受限环境中运行或使用未能正确遵守重定向的非常旧的客户端的一小部分用户。

## k8s.gcr.io 会发生什么？ 

与重定向分开，k8s.gcr.io 将被冻结，[并且在 2023 年 4 月 3 日之后不会更新新镜像](https://kubernetes.io/blog/2023/02/06/k8s-gcr-io-freeze-announcement/)。 k8s.gcr.io 将不会获得任何新版本、补丁或安全更新。它将继续保持可用以帮助人们迁移，但它将在未来完全被淘汰。

## 我还有疑问，我应该去哪里？ 

有关 registry.k8s.io 及其开发原因的更多信息，请参阅 [registry.k8s.io：更快、更便宜且普遍可用](https://kubernetes.io/blog/2022/11/28/registry-k8s-io-faster-cheaper-ga/)。

如果您想了解更多关于镜像冻结和那里可用的最后镜像的信息，请参阅博客文章：[k8s.gcr.io Image Registry Will Be Frozen From the 3rd of April 2023](https://kubernetes.io/blog/2023/02/06/k8s-gcr-io-freeze-announcement/)。

有关 registry.k8s.io 的架构及其[请求处理决策树](https://github.com/kubernetes/registry.k8s.io/blob/8408d0501a88b3d2531ff54b14eeb0e3c900a4f3/cmd/archeio/docs/request-handling.md)的信息可以在 [kubernetes/registry.k8s.io repo](https://github.com/kubernetes/registry.k8s.io) 中找到。

如果您认为您遇到了新注册表或重定向的错误，请在 [kubernetes/registry.k8s.io 存储库](https://github.com/kubernetes/registry.k8s.io/issues/new/choose)中打开一个问题。在创建新问题之前，请检查是否已经存在与您所看到的类似的问题。

