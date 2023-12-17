<!--
title: Helm的五个缺陷
cover: https://cms.glasskube.eu/uploads/Goodbyehelm_7c21643ff8.png
-->

使用 Helm 多年来，这五个缺点总是让我困扰。从 CRD 更新到多命名空间部署。

> 译自 Glasskube 的 [5 shortcomings of Helm](https://glasskube.eu/en/r/knowledge/5-helm-shortcomings/)。

我们正在尝试构建下一代 Kubernetes 部署自动化的 5 个原因。您是否想要关注我们的过程？在 GitHub 上为 Glasskube 加星: [glasskube/operator](https://github.com/glasskube/operator) 。

## 介绍
s
作为一名经验丰富的 DevOps 工程师，我发现流行的 Kubernetes 部署工具 Helm 有一些令人震惊的缺陷。在这篇文章中，我想讨论其中一些在我看来需要一个更现代部署解决方案新视角的缺陷。如果您之前从未听说过 Helm，简而言之，它是:

> 一个用于将 Kubernetes 资源(应用程序)打包为chart，发布它们并通过命令行界面轻松安装的框架。

本文的目的不是讨厌构建 helm 的聪明和才华横溢的人，而是可能引发一个富有成效和健康的讨论，关于作为 DevOps 行业我们在未来几年保持相关性需要走的路。但为了完全理解下文，我认为重要的是要了解是什么发展引导我们走到了今天。所以在我们开始之前，让我们快速深入 helm 的历史。

2015 年，一家名为 Deis 的公司创造了 Helm，这是 Kubernetes 的程序包管理器。Deis 现在是 Azure Kubernetes 服务的一部分，但原来的项目仍然存在，称为 [Helm 经典版](https://github.com/helm/helm-classic)。与此同时，谷歌有一个名为 Kubernetes 部署管理器的项目，它类似于 [Google 部署管理器](https://cloud.google.com/deployment-manager/docs)，但针对的是 Kubernetes 资源而不是 GCS 资源。

在 2016 年初，这两个项目决定合并，这导致了当年稍晚发布 [Helm v2](https://v2.helm.sh/)。Helm v2 由客户端和服务器组件(分别为 Helm 和 tiller)组成，其中后者是原始 Kubernetes 部署管理器项目的延续。Tiller 旨在处理部署状态，以使多个用户更容易使用 Helm 而不会相互干扰。

2018 年，Helm [启动了](https://helm.sh/blog/intro-helm-hub/) Helm Hub 作为发现 chart 的中心站点，否则这些 chart 会分布在分布式存储库中。Helm Hub 在 2020 年[更名](https://helm.sh/blog/helm-hub-moving-to-artifact-hub/)为 [Artifact Hub](https://artifacthub.io/)。

随着 Kubernetes 1.6 的发布，其中默认启用基于角色的访问控制(RBAC)，生产环境中的 helm 部署变得更加困难，因为 tiller 所需的许多安全策略。因此，人们开始尝试一种新方法，该方法可以在不需要服务器组件的情况下完成相同的事情，这最终导致了 2019 年 Helm v3 的发布。

如您所见，helm 有非常丰富的历史。它成为了打包 Kubernetes 应用程序的黄金标准，并被世界各地的 DevOps 工程师所使用。但是仅仅因为 helm 是这个领域最大的玩家，并不意味着它没有缺陷。那么，为什么要说对 helm 说再见？

## 五个缺点:

### 1. Helm 不提供升级自定义资源定义的机制

helm 确实提供了通过将它们放置在专用 crds 目录中来打包自定义资源定义(CRD)的方法，但这些在升级期间会被忽略！这是[故意的](https://helm.sh/docs/chart_best_practices/custom_resource_definitions/#some-caveats-and-explanations)，旨在防止意外的数据丢失。因此，升级 chart 不会自动升级其关联的 CRD，这对于许多工程师来说是意想不到的，并导致更多手动参与和容易出错的升级过程和其他反模式。

为了应对这个主要设计缺陷，Chart 开发人员提出了几种策略，其中最流行的有:

- 将 CRD 放入 chart 的模板目录
- 仅用于 CRD 创建单独的子 chart

克服这一缺点的另一种方法是不直接调用 helm 命令，而是使用类似 [Flux](https://github.com/fluxcd/flux2) 的 CI/CD 解决方案。Flux 提供了在 helm 升级期间自动更新 CRD 的设置，但[默认情况下关闭](https://fluxcd.io/flux/components/helm/api/v2beta1/#helm.toolkit.fluxcd.io/v2beta1.CRDsPolicy)。


### 2. Helm 依赖关系管理

在 helm chart 中指定依赖关系的方法是将其引用为子 chart。对于可能希望单独安装或作为另一个 chart 的一部分安装的紧密耦合的依赖项，这种方法可以很好地工作，但它有一些重要的弱点：

- 子chart始终安装在**主版本相同的命名空间**中，并且无法更改此命名空间。
- **没有机制**在两个版本之间共享一个依赖项。

例如，我们的 [Glasskube Operator Helm Chart](https://github.com/glasskube/operator/tree/main/charts/glasskube-operator) 依赖于 kube-prometheus-stack、velero 和其他一些依赖项，其中一些已经安装在许多 Kubernetes 集群中。为提供尽可能简单的安装体验，该chart将所有这些依赖项引用为子chart，但使用这种方法，所有这些依赖项都捆绑在 Glasskube Operator release 中，并且无法单独更改或更新它们。此外，没有办法检查一个依赖项是否已经安装，因此用户最终可能会结束两个独立的相同 helm chart的安装！

理想的工具应该允许chart开发人员指定外部依赖项，并简单地确保那些在安装chart之前在集群中存在。通过这种方式，依赖项可以在消费者之间共享。这就是操作系统程序包管理器自始至终的工作方式。为什么 Kubernetes 需要与众不同呢？

### 3. Helm chart创建不够用户友好

到目前为止，我们讨论的问题会影响您作为chart用户。但是对于chart开发人员来说，情况如何呢？

那么，让我们从创建新chart开始。这可以通过调用 `helm create your-chart` 来实现。我邀请您快速打开一个终端，运行此命令并浏览它创建的所有文件。正如您肯定会同意的那样，这是......很多。我仍然记得我想创建我的第一个 helm chart，看到此命令的结果时的想法，“这不可能是正确的。”

```bash
.: total 8，0K
drwxr-xr-x. 2 kosmoz kosmoz 40 7. Dez 13:23 charts/
-rw-r--r--. 1 kosmoz kosmoz 1，2K 7. Dez 13:23 Chart.yaml
drwxr-xr-x. 3 kosmoz kosmoz 200 7. Dez 13:23 templates/
-rw-r--r--. 1 kosmoz kosmoz 1，9K 7. Dez 13:23 values.yaml

./charts: total 0
./templates: total 28K
-rw-r--r--. 1 kosmoz kosmoz 1，9K 7. Dez 13:23 deployment.yaml
-rw-r--r--. 1 kosmoz kosmoz 1，8K 7. Dez 13:23 _helpers.tpl
-rw-r--r--. 1 kosmoz kosmoz 925 7. Dez 13:23 hpa.yaml
-rw-r--r--. 1 kosmoz kosmoz 2，1K 7. Dez 13:23 ingress.yaml
-rw-r--r--. 1 kosmoz kosmoz 1，8K 7. Dez 13:23 NOTES.txt
-rw-r--r--. 1 kosmoz kosmoz 326 7. Dez 13:23 serviceaccount.yaml
-rw-r--r--. 1 kosmoz kosmoz 370 7. Dez 13:23 service.yaml
drwxr-xr-x. 2 kosmoz kosmoz 60 7. Dez 13:23 tests/

./templates/tests: total 4，0K
-rw-r--r--. 1 kosmoz kosmoz 388 7. Dez 13:23 test-connection.yaml
```

总共，`helm create` 生成 10 个位于不同子目录中的文件，哪些文件对于chart至关重要，哪些文件只是示例代码一开始并不明显。我曾经向已经创建了几十个chart的 DevOps 工程师抱怨过这一点，他们笑着说:

> “创建chart的第一步是运行 `helm create`。第二步是删除 90% 的结果。”


真的吗？这就是我们能做到的最好的吗？好的，我们接受它并说您已经弄清楚了新的chart的结构。现在，您可能想要添加一些资源。当然，您可以将现有的 YAML 文件直接放入chart的`templates`目录中，但您可能有兴趣在资源中使用 `values.yaml` 中的一些参数。毕竟，这本应该是创建 helm chart的重点。要查看示例，请返回终端(在之前创建 helm chart的位置)并查看 `templates/serviceaccount.yaml` 文件:


```
{{- if .Values.serviceAccount.create -}}
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{ include "your-chart.serviceAccountName" . }}
  labels:
    {{- include "your-chart.labels" . | nindent 4 }}
  {{- with .Values.serviceAccount.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
{{- end }}
```

现在，我知道您在想什么:

> 这看起来不像我熟悉的 YAML！`include`、`toYaml` 和 `nindent` 是什么，还有所有那些 - 和 {{ 和 | 是怎么回事？

没错，尽管 helm 模板文件使用 YAML 文件扩展名，但它们实际上只是模板。Helm 模板基于 Go 模板语言，该语言非常灵活和强大，但对 YAML 或 Kubernetes 一无所知。这就是为什么在模板文件中需要调用这么多转换函数的必要原因。

因此，许多流行的chart最终的模板文件包含的更多是模板语言而不是实际的 YAML。这使得它们难以阅读和维护，特别是对于没有参与其创建的人。

### 4. values.yaml 文件是一种反模式

现在，让我们回到一些更为切实的东西，您作为 helm 用户。作为编写资源为 YAML 文件 Kubernetes 应用程序开发人员，您可能习惯于在开发环境中获得丰富的支持，包括严格的模式验证和超全面的自动完成。为发布chart创建 `values.yaml` 文件有点不同。您看，对于 `values.yaml` 文件中包含什么不包含什么没有通用模式。因此，您的开发环境除了基本的 YAML 语法高亮之外无法提供帮助。验证 `values.yaml` 文件是否有效的唯一方法是通过 helm 运行它并查看会发生什么。使用 `helm template` 允许您呈现这些 helm 模板，以检测配置文件中可能的错误。

许多chart开发人员希望用户能够微调最终部署的大多数方面。因此，配置的可能性数量通常非常大且复杂，模仿它们想要创建的实际资源，但没有任何模式验证!

### 5. 无法与 Kubernetes API 交互

我们已经讨论了 helm 的 4 个缺点，但在我看来，helm 的最大缺点是：helm 版本严格是一次性操作。一旦 helm 版本成功安装，helm 的工作就完成了。但是问题是：**安装应用程序通常不是最难的部分，维护安装并保持运行才是**。不幸的是，helm 在这方面没有太大帮助。

安装版本后完成后，由于其被设计为严格的客户端应用程序，helm 无法执行任何其他更改。这种无法在版本生命周期的后期阶段与版本进行交互意味着 **helm 作为部署方法本质上是静态的**，但现代软件部署通常需要非常动态。

操作员可以做而 helm 不能做的一个简单示例是根据检测到的 Kubernetes 环境动态设置 Ingress 类和注解:

**检测云环境:**

```js
private val dynamicCloudProvider get() = when {
  kubernetesClient.configMaps().inNamespace("kube-system").withName("shoot-info")
    .get()？.data？.get("extensions")？.contains("shoot-dns-service") == true ->
      CloudProvider.gardener
  kubernetesClient.nodes().withLabel("eks.amazonaws.com/nodegroup").list().items.isNotEmpty() ->
      CloudProvider.aws
  kubernetesClient.nodes().withLabel("csi.hetzner.cloud/location").list().items.isNotEmpty() ->
      CloudProvider.hcloud
  else -> CloudProvider.generic
}

```

**基于环境应用配置:**

```js
protected val defaultIngressClassName: String？
  get() = when (configService.cloudProvider) {
    CloudProvider.aws -> "alb"
    else -> configService.ingressClassName
}

protected fun getDefaultAnnotations(primary: P， context: Context<P>): Map<String， String> =
  configService.getCommonIngressAnnotations(primary) +
  when (configService.cloudProvider) {
    CloudProvider.aws -> awsDefaultAnnotations
    CloudProvider.gardener -> gardenerDefaultAnnotations
    else -> getCertManagerDefaultAnnotations(context) + ingressNginxDefaultAnnotations
```

## 结论

尽管许多开发人员一开始有点害怕 helm，但其简单的设计使 helm 在这个空间中处于领先地位。Helm 当前是管理复杂应用程序部署的事实标准，但这并不意味着我们不应该质疑其设计并指出缺陷。应用程序的新要求将需要更动态的部署方法，我们 DevOps 工程师和应用程序开发人员必须做好准备。

这就是我们启动 Glasskube 的原因：通过我们的 [glasskube/operator](https://github.com/glasskube/operator) 在 Kubernetes 上以更简单的方式部署应用程序和基础架构。

如果您想要关注我们的进展，请确保为 [glasskube/operator](https://github.com/glasskube/operator) 加星并加入我们的 [Discord](https://discord.gg/j9A7epEeg2)。

