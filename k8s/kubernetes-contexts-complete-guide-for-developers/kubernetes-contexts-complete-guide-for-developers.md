<!--
title: Kubernetes Context开发者指南
cover: ./cover.png
-->

介绍 Kubeconfig 和Context。终于是时候理解 kubectl 如何连接到 Kubernetes 了。

> 译自 [Kubernetes Contexts: Complete Guide for Developers](https://itnext.io/kubernetes-contexts-complete-guide-for-developers-7ea5b2fc75c7)，作者 Guilherme Oenning。

你好！我是 Guilherme，我是 Kubernetes 开发者，也是 [Aptakube](https://aptakube.com/) 的创始人 —— 一个现代化的 Kubernetes 图形用户界面。

本指南充满了每个使用 Kubernetes 的开发者都应该了解的基本信息。通过本指南的最后，你将对 kubectl 这样的客户端工具如何连接到 Kubernetes 有扎实的理解。

准备好了吗？

## 一切都始于一个 Kubeconfig 文件

当与 SQL 数据库（如 Postgres 或 MySQL）进行交互时，开发者将需要所谓的连接字符串 。**连接字符串**包含了连接到数据库所需的所有信息，包括主机名（或 IP）、端口、用户名和密码。所有这些信息通常存储在一个单独的字符串中，然后应用程序使用该字符串连接到数据库。

在 Kubernetes 的世界中，连接字符串的等价物是Context 。Context包含了连接到 Kubernetes 集群所需的所有信息，如集群主机名、端口、身份验证方法等。然而，与连接字符串不同，Context不是一个字符串，而是一个存储在名为 **Kubeconfig** 的文件中的 YAML 对象。

多个Context可以存储在一个 Kubeconfig 文件中，每个Context可用于连接到不同的集群。或者，可以将 kubeconfig 文件拆分为多个文件，每个文件包含一个或多个Context。如果您有许多集群，我建议这样做，因为这样可以使事情更有条理，更易于管理。

Kubeconfig 文件的默认存储位置是 `~/.kube/config`，这是大多数 Kubernetes 工具期望找到文件的位置，但也支持自定义位置。

如果您之前使用过 `kubectl`，您的计算机上可能已经有一个 Kubeconfig 文件。想知道其中的内容吗？如果您使用的是 macOS 或 Linux，您可以使用以下命令：

```bash
cat ~/.kube/config
```

Kubernetes Context示例：

```yaml
apiVersion: v1
kind: Config
current-context: minikube
clusters:
- cluster:
    certificate-authority: /Users/goenning/.minikube/ca.crt
    server: https://127.0.0.1:51171
  name: minikube-local
contexts:
- context:
    cluster: minikube-local
    namespace: default
    user: admin
  name: minikube
users:
- name: admin
  user:
    client-certificate: /Users/goenning/.minikube/profiles/minikube/client.crt
    client-key: /Users/goenning/.minikube/profiles/minikube/client.key
```

这是 [Minikube](https://minikube.sigs.k8s.io/docs/) 生成的一个 Kubeconfig 文件，Minikube 是一个工具，可在您的本地计算机上创建单节点的 Kubernetes 集群。这是学习 Kubernetes 和在本地开发应用程序的好工具。

如果您是 Kubernetes 的新手，我强烈推荐使用 Minikube！

每个 Kubeconfig 文件包含三个主要部分：**clusters**（集群）、**contexts**（Context）和**users**（用户）。这些部分被定义为对象数组，因为您可以在单个 kubeconfig 文件中拥有多个集群、Context和用户。然而，如前所述，我建议为每个集群使用单独的文件，或者至少根据它们共有的特性将一些集群组合在一起。

- **Cluster（集群）**：此对象定义了集群的 API 服务器位置（主机:端口）以及在 SSL 握手期间要使用的客户端证书（certificate-authority）。此部分还可能包含其他设置，例如 proxy-url，用于只能通过代理访问集群的情况。
- **User（用户）**：此对象定义了连接到集群时要使用的身份验证方法。在这种情况下，用户使用的是客户端证书，这是本地集群的常见身份验证方法。其他身份验证方法包括 token、用户名/密码 和 exec。我们将在下一节中更详细地介绍这些内容。
- **Context（Context）**：是将集群和用户联系在一起的东西。您在 Kubernetes 中执行的每个操作都是在一个Context中完成的，这就是为什么 kubectl 有一个 --context 参数，让您可以指定要与之交互的集群。这意味着您可以有多个Context指向同一个集群，但使用不同的用户，这在您在同一个集群中拥有不同角色时非常有用。

## 使用 Kubeconfig 文件与 kubectl

当使用 kubectl（或任何其他 Kubernetes 工具）时，默认情况下会在 `~/.kube/config` 路径下查找 kubeconfig 文件。但是，您可以使用 `--kubeconfig` 参数或 `KUBECONFIG` 环境变量指定不同的路径。以下是一些示例：

```bash
kubectl get pods # uses ~/.kube/config
kubectl get pods --kubeconfig /path/to/kubeconfig # uses config from /path/to/kubeconfig
KUBECONFIG=/path/to/kubeconfig kubectl get pods # same as above
```

如果您的 kubeconfig 文件中有多个集群，您可以使用 `--context` 参数指定要与之交互的集群：

```bash
kubectl get pods --context prod-europe # uses the prod-europe context from the ~/.kube/config
kubectl get pods --context prod-europe --kubeconfig /path/to/kubeconfig # uses the prod-europe context from /path/to/kubeconfig
```

在每个命令中设置 `--kubeconfig` 参数很麻烦，因此您还可以设置 `KUBECONFIG` 环境变量，指向您想要使用的 kubeconfig 文件。当您不断地与多个 kubeconfig 文件交互时，这尤其有用。

如果您使用的是 macOS 或 Linux，您可以在 shell 配置文件中（例如 `~/.bash_profile` 或 `~/.zshrc`）设置 `KUBECONFIG`，这样它将始终在将来的 shell 会话中可用，您不必每次手动设置它。

以下是一份包含一些有用的Context相关命令的速查表：

```bash
kubectl config get-contexts             # display list of contexts
kubectl config current-context          # display the current-context
kubectl config use-context prod-europe  # set the default context to my-cluster-name
```

`kubectl config use-context` 基本上会修改您的 Kubeconfig 文件，并将当前Context设置为您指定的Context。当您想要在不必每次都指定 `--context` 参数的情况下在Context之间切换时，这很有用。

大多数 Kubernetes 工具都使用 Kubeconfig 文件，这使得很容易采用和尝试新应用程序，而无需安装或配置任何额外的东西。

以下是 [Aptakube](https://aptakube.com/) 如何使用Context的示例，这也允许您同时连接多个集群，而这是使用 `kubectl` 无法实现的。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*fhJySLUd5THfTQ2e)

*Aptakube 中的Context选择器*

## 认证和安全

谈论 Kubeconfig 就不能不提及其安全性方面。这些文件可能包含诸如令牌和私钥之类的敏感信息，因此保持其安全性非常重要。

保护集群的最佳选项是不要在 Kubeconfig 文件中存储任何敏感信息。身份验证是可能变得复杂的地方。有许多方法可以对 Kubernetes 集群进行身份验证，其中一些方法比其他方法更安全。以下是最流行的几种：

- **令牌**：就安全性而言，这绝对是最糟糕的身份验证方法。如果您的 Kubeconfig 泄露了，除非您有其他网络保护措施，如 VPN/代理，否则任何人都可以使用该令牌访问您的集群。避免在任何重要的集群中使用令牌。不过，在本地集群上使用通常是可以接受的。
- **客户端证书**：这与令牌有些类似，但是它可能会更安全一些，因为证书的内容通常存储在单独的文件中。因此，即使 Kubeconfig 内容泄露，攻击者可能也无法访问证书。我们之前展示的 Kubeconfig 示例使用了客户端证书。
- **Exec 插件（推荐）**：这是大多数云提供商和托管 Kubernetes 服务建议您使用的方法。它本质上是 Kubeconfig 的扩展，用于使用外部 CLI 工具（例如 `aws`、`az` 或 `gcloud` CLI）通过云基 IAM 机制进行身份验证。这是最安全的身份验证方法，因为它不会在 Kubeconfig 文件中包含任何敏感信息。但是，设置起来也更复杂，因为它需要额外了解每个云提供商以及如何使用其 CLI 工具。

## 结论

就是这样啦！

我想鼓励您查看一下您的 Kubeconfig 文件，您会惊讶地发现您可以从简单查看中学到多少知识。大多数 Kubernetes 用户甚至都不知道其中有一个 API 服务器 URL！

如果您有任何问题或反馈，请留言。我很乐意听取您的意见！
