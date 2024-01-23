<!--
title: Kubernetes Operator与Helm的对比与选择
cover: https://assets-global.website-files.com/626a25d633b1b99aa0e1afa7/65ad417cdfcdbb9383d03f26_LIu3U58iMlxF4grSb-h8EqVFh_kvJrFIXXuaripoQaWATQKrCzaBA_b0KC1-nV5xf82cETQoOFDEnP8TBOAaOriLEKdPCGgQSLcdmvhlWoDR3ry0VF-I6Rn1QTOBeKbrk2HOOQLLxYb82i8y5HT10wc.jpeg
-->

了解 Kubernetes operators 和 Helm 之间的区别，并选择在 Kubernetes 中安装和配置应用程序的最佳解决方案。

> 译自 [Kubernetes Operator vs Helm: 11 Key Differences & Which One to Choose](https://www.groundcover.com/blog/kubernetes-operator-vs-helm)。作者 Steb Veksler 。

Kubernetes Helm charts 和 operators 有一点共同之处，那就是这两个术语都属于那种一听就不知所云的专业术语。即使对有编程经验的人来说，Kubernetes 环境下的 operator 这个词也可能毫无意义，因为它与编程中的运算符没有任何关系。

至于 Helm charts，你得会说希腊语，或者至少知道 Kubernetes 源自希腊语中的“舵手”这个词，并且你得对自嘲性的专业术语有所理解，才能稍微猜出为什么 Helm chart 叫这个名字。(若你还不明白，答案是 Helm chart 帮助“驾驶”Kubernetes，就像舵手驾驶船只一样。)

但除了它们共同具有那种对新手而言难以理解的术语的特点之外，Operator 和 Helm Chart 并没有太多共同之处。的确，它们都服务于在 Kubernetes 中安装和配置应用程序这个相同的基本目标。但是它们的实现方式不同。根据你想要的控制粒度和应用程序生命周期管理的重要性等因素，Operator 可能比 Helm Chart 更好，反之亦然。

考虑到这一点，请继续阅读 Operator 和 Helm Chart 的详细比较，以及在何时使用哪种解决方案的提示。

## 什么是 Kubernetes Operator?

在 Kubernetes 中，Operator 是一种可以使用 Kubernetes 自定义资源来安装和管理应用程序的控制器。为了更详细地解释这个定义，让我们解析一下定义中的两个关键词: 控制器和自定义资源。

### 控制器

Kubernetes 中的控制器是一种例程，它可以监控 Kubernetes 配置的状态以及 Kubernetes 集群资源的实际状态。当它检测到给定资源的期望状态和实际状态之间的偏差时(可能是因为管理员修改了配置，也可能是因为 Kubernetes 集群内部的某些故障)，控制器会尝试使期望状态和实际状态重新对齐。

![](https://assets-global.website-files.com/626a25d633b1b99aa0e1afa7/65ad417cdfcdbb9383d03f26_LIu3U58iMlxF4grSb-h8EqVFh_kvJrFIXXuaripoQaWATQKrCzaBA_b0KC1-nV5xf82cETQoOFDEnP8TBOAaOriLEKdPCGgQSLcdmvhlWoDR3ry0VF-I6Rn1QTOBeKbrk2HOOQLLxYb82i8y5HT10wc.jpeg)

所以，如果你部署了描述应用程序期望状态的配置，控制器将检测到该配置，然后应用它(假设考虑到 Kubernetes 集群整体状态，可以应用该配置)。

### 自定义资源

Kubernetes 中的自定义资源是对 Kubernetes API 的扩展，它使向 Kubernetes 集群添加默认情况下不可用的功能成为可能。您可以通过创建自定义资源定义(CRD)来实现这一点。

如果要使用 Kubernetes Operator 来安装或管理应用程序，您可以创建实现该应用程序所需功能的 CRD。如果您随后将 CRD 与 Operator 的控制器组合，Kubernetes 控制器例程将检测并部署它。

### Kubernetes Operator 示例

对于那些想要基本 Kubernetes Operator 示例的人，[hello-operator2](https://github.com/deepak1725/hello-operator2/commit/c87544405b8359da2007317112bb64e434330f5f) 代码(由 Deepak Sharma 提供)是一个很好的示例。我们不会在此复制全部内容，但让我们展示一些关键组件。

首先，该 Operator 定义了一些基本的上下文参数:

```go
package controllers

import (
    "context"

    appsv1 "k8s.io/api/apps/v1"
    corev1 "k8s.io/api/core/v1"
    "k8s.io/apimachinery/pkg/api/errors"
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/apimachinery/pkg/types"
    "sigs.k8s.io/controller-runtime/pkg/controller/controllerutil"
    "sigs.k8s.io/controller-runtime/pkg/reconcile"

    mydomainv1alpha1 "hello-operator2/api/v1alpha1"
)
```

然后，它实现了一个检查部署状态的函数:

```go
// ensureDeployment ensures Deployment resource presence in given namespace.
func (r *TravellerReconciler) ensureDeployment(request reconcile.Request，
    instance *mydomainv1alpha1.Traveller，
    dep *appsv1.Deployment，
) (*reconcile.Result， error) {

    // See if deployment already exists and create if it doesn't
    found := &appsv1.Deployment{}
    err := r.Get(context.TODO()， types.NamespacedName{
   	 Name:  	dep.Name，
   	 Namespace: instance.Namespace，
    }， found)
…
```

最后，它创建一个新的部署:

```go
// backendDeployment is a code for Creating Deployment
func (r *TravellerReconciler) backendDeployment(v *mydomainv1alpha1.Traveller) *appsv1.Deployment {

    labels := labels(v， "backend")
    size := int32(1)
    dep := &appsv1.Deployment{
   	 ObjectMeta: metav1.ObjectMeta{
   		 Name:  	"hello-pod"，
   		 Namespace: v.Namespace，
   	 }，
…
```

如果您想要更多 Kubernetes Operator 示例，请查看 [OperatorHub.io](https://operatorhub.io/)，它托管了数百个流行应用程序的免费 Kubernetes Operator。

## 什么是 Helm Chart？

现在我们已经完全了解了 Kubernetes Operator，让我们来谈谈 Helm 以及 Helm Chart 能实现什么。

Helm Chart 是包含使用称为 Chart 的打包格式在 Kubernetes 上部署应用程序所需资源的包。您可以使用 Helm(您猜对了！)安装 Helm Chart，Helm 是 Kubernetes 的应用程序包管理器和配置管理工具。

Helm Chart 和 Helm 包管理器类似于 Ubuntu 上的 Debian 包和 apt-get，或 Red Hat 上的 RPM 包和 DNF，只有一个关键区别: 与操作系统的应用程序包不同，Helm Chart 通常不包含应用程序二进制文件。相反，它们包含指向需要安装以部署应用程序的容器镜像或镜像的文件。

### Helm Chart 示例

您可以在 [Helm 项目的 GitHub 存储库](https://github.com/helm/examples/tree/main/charts/hello-world)中找到一个基本的 "Hello World" 应用程序的 Helm Chart 示例。该存储库包含两个关键文件。

![](https://assets-global.website-files.com/626a25d633b1b99aa0e1afa7/65ad42797a57deb0d77bc3c4_XEI3k63mxq1LuqVlAuj7LxxtXfnApD-2SG5aZO0bhL6bIMDefdZ60C3_oD3_ovGrdELmCpq_ZOkeyvH8F8_rub_jVWYwaqmMAOmZlPB94a8r-PEusEleyXs3SHYLwYb1ymbxIq4spt1Fx6jtz3lz1a0.jpeg)

首先，有 Chart.yaml，其中包含 Helm Chart 的配置数据:

```yaml
apiVersion: v2
name: hello-world
description: A Helm chart for Kubernetes

# A chart can be either an 'application' or a 'library' chart.
#
# Application charts are a collection of templates that can be packaged into versioned archives
# to be deployed.
#
# Library charts provide useful utilities or functions for the chart developer. They're included as
# a dependency of application charts to inject those utilities and functions into the rendering
# pipeline. Library charts do not define any templates and， therefore， cannot be deployed.
type: application

# This is the chart version. This version number should be incremented each time you make changes
# to the chart and its templates， including the app version.
# Versions are expected to follow Semantic Versioning (https://semver.org/)
version: 0.1.0

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"
```

然后，有 values.yaml，其中定义了应用程序本身:

```yaml
# Default values for hello-world.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.

replicaCount: 1

image:
  repository: nginx
  pullPolicy: IfNotPresent
  # Overrides the image tag whose default is the chart appVersion.
  tag: ""

nameOverride: ""
fullnameOverride: ""

serviceAccount:
  # Specifies whether a service account should be created
  create: true
  # Annotations to add to the service account
  annotations: {}
  # The name of the service account to use.
  # If not set and create is true， a name is generated using the fullname template
  name: ""

service:
  type: ClusterIP
  port: 80
```

要使用这样的 Helm Chart，您需要先在系统上[安装 helm CLI 工具](https://helm.sh/docs/intro/install/)。 然后，使用类似以下的命令添加包含要安装的 Helm Chart 的存储库:

```bash
helm repo add repo-name https://some-domain.com/path/to/repo
```

然后使用以下命令更新存储库列表:

```bash
helm repo update
```

最后，使用以下命令安装该应用程序:

```bash
helm install my-release repo-name/chart-name
```

您也可以使用 Helm 来更新和删除应用程序，但我们会在另一篇文章中全面介绍使用 Helm 的方法。

## Kubernetes Operator与Helm的11个关键区别

如果您已经阅读到这里，那么您知道 Kubernetes Operator 和 Helm Chart 都可实现相同的目标: 安装和管理应用程序。两者也都可用于部署帮助 [Kubernetes 故障排除](https://www.groundcover.com/kubernetes-troubleshooting)和[监控](https://www.groundcover.com/kubernetes-monitoring)的工具。

但是 Kubernetes Operator 和 Helm Chart 通过稍微不同的方式实现这些目标。以下是 Operator 和 Helm Chart 的主要区别。

### #1. 范围和功能

总体来说，Helm Chart 范围更窄。Helm Chart 的主要目的是安装标准应用程序，也就是那些可以根据现有容器镜像运行的应用程序。如果您需要运行依赖特殊 Kubernetes API 扩展的自定义应用程序，那么 Helm 就不是一个好的解决方案，不过您可以为此目的使用 Operator。

类似地，在配置方面 Helm 提供的灵活性更少。您可以在安装 Chart 时向 Helm 传递参数以配置应用程序，但只有在 Chart 被设计为支持这些参数时才行。

相比之下，使用 Kubernetes Operator，在定制应用程序方面，天空——或者更确切地说，您编写的代码——就是极限。

### #2. 复杂性和灵活性

与 Helm 相比，Operator 增加的灵活性所带来的代价是 Operator 也更复杂。创建 Operator 需要编写 CRD，而您可以根据一些相对简单的 YAML 代码创建 Helm Chart。

此外，从安装的角度来看，Helm 不太复杂，因为您可以用一个命令就安装它。 安装 Operator 通常需要运行长的 kubectl 命令。

### #3. 定制化

如前所述，Operator 提供了更大的定制化空间，因为您可以实现 CRD 支持的任何功能。 Helm Chart 的某些配置方面是可以定制的，但仅当创建 Helm Chart 的开发人员在构建 Chart 时实现了配置选项。

这里的区别有点像从源代码构建标准应用程序和使用包安装应用程序之间的区别。当您从源代码构建时，您可以修改源代码以自定义应用程序。 但如果您使用包进行安装，则只能修改包管理系统和环境支持的配置选项。

### #4. 云成本考量

因为 Chart 的定制性通常不如 Operator，所以它们更容易给您的环境带来冗余。 Helm Chart 可能会安装和运行您严格意义上不需要的应用程序特性，除非您重写整个 Chart，否则可能没有办法关闭这些特性。相比之下，使用 Operator，您可以精确控制哪些特性需要运行。

因此，使用 Chart 安装的应用程序更有可能消耗更多资源，从而增加云成本。总体来说，与内存泄漏或浪费 CPU 的有缺陷代码等问题相比，这对您的云端总支出的影响要小得多，但如果您想优化成本，这仍值得考虑。

### #5. 学习曲线

可以肯定，几乎每个人都会觉得学习使用 Helm 比学习 Operator 更简单。Chart 的工作方式与任何类型的软件包非常相似，所以如果您在其他上下文中使用过软件包，应该可以很快掌握 Helm。

相比之下，Operator 基于 Kubernetes 的独有概念。在您完全理解像控制器和 CRD 这样的关键 Kubernetes 概念之前，您不应该期望理解 Operator 的工作原理，更不用说创建或修改 Operator 了。

### #6. 自动化

Operator 和 Chart 都可以帮助自动执行您否则必须手动执行的应用程序安装和管理任务。但是，由于 Helm 的范围仅限于管理标准应用程序，所以它不提供太多自动化功能。

您可以使用 Helm 根据容器镜像自动安装或更新应用程序，但您无法自动执行超出 Helm 原生功能范围的定制应用程序配置更改。但是，使用 Operator，您可以自动执行 Kubernetes API 和控制器支持的任何操作。

### #7. 生命周期管理

Operator 和 Chart 在支持应用程序生命周期管理方面有共同之处，那就是您可以使用它们来安装、更新和删除应用程序。但是，使用 Helm 进行的生命周期管理有点过于简单粗暴，调整不太细致。

要使用 Helm 管理应用程序生命周期，您只能使用内置的命令，如 install、upgrade 和 uninstall。您可以使用新版本替换旧版本的应用程序，或者完全删除应用程序。但是，如果不升级整个应用程序，您就无法对现有应用程序进行细微修改，而通过修改应用程序的 Operator 就可以做到这一点。

### #8. 维护

同样，在应用程序维护方面，Operator 提供了更大的灵活性和控制能力。如果您只是想升级或删除应用程序，可以使用 Helm 来完成。但是如果您想执行其他应用程序维护任务，如修改应用程序的存储配置，除非您创建一个新的 Helm Chart 并使用它重新安装应用程序，否则 Helm 并无益处。不过，使用 Operator 就可以进行更细粒度的维护更改。

### #9. 使用案例

总的来说，Operator 支持的使用案例比 Helm 更广泛。后者只擅长应用程序的安装、升级和删除。Operator 可以做到这些，但它们还支持应用程序备份等使用案例。

### #10. 适合 GitOps

![](https://assets-global.website-files.com/626a25d633b1b99aa0e1afa7/65ad436582eee2ea375fa875_s5S7cCU29-YHqvwSV_EDhmhW5_8K6_Nb7KHhr-gvoIEtBXYrtGCGw7vmONXA2gw92oxX3LlP1BIroNJy9dz8D1jiwHOLNMGbhDXPxTWBBnUfQGuL8jWZDh6-uTVEvftlElSDnA_FTPidQR-e8nimUt6Qb6xvESvt.png)

GitOps 意味着使用存储在 Git 仓库中的代码来管理对应用程序部署和基础设施的更改。如果您在 Git 中存储应用程序和基础设施的配置数据，就可以从那里自动将配置推送到生产环境。您还可以根据 Git 中的代码版本历史记录跟踪对资源的更改。

由于您可以在 Git 中存储 Operator 和 Chart 的代码，两种解决方案都与 GitOps 方法论兼容。也就是说，可以认为当与 Operator 一起使用时，GitOps 提供更多好处，因为您可以对 Operator 进行的更改范围更广。从这个意义上说，能够以细粒度方式跟踪更改更有价值。使用 GitOps，对 Operator 中的一行代码的更改就很容易跟踪 - 如果您更改了 Operator，某些事情发生故障，并且您想找出触发问题的更改，那么这可能很有用。

### #11. 社区和生态系统

Operator 和 Helm 都拥有强大的社区和生态系统。在 OperatorHub.io 和 [Artifact Hub](https://artifacthub.io/) 等网站上可以轻松找到公开可用的 Operator 和 Helm Chart。两种解决方案的丰富文档也可以免费获得。

也就是说，就社区参与而言，Operator 和 Helm 之间的一个重要区别在于，Helm 是一个开源项目，拥有自己的一套官方资源，而 Operator 没有专门的项目(尽管 Kubernetes 项目维护着其文档)。从这个意义上说，Helm 有一个特定的“官方”社区，但 Operator 没有。

## Kubernetes Operator与Helm: 该选择哪一个？

对于“应该选择 Operator 还是 Helm？”这个问题，有两种方法。它们取决于您是要将应用程序分发给其他用户，还是仅仅想安装一个应用程序。

### 应用分发

 | 考虑因素 | 选择什么 |
|-|-|  
| 无状态应用程序 | Helm Chart |
| 需要定制的应用程序 | Operator |
| 用户的 Kubernetes 经验有限 | Helm Chart |
| 需要支持复杂的维护 | Operator |

如果您正在分发一个应用程序，当以下条件满足时，请选择 Helm Chart:

- 您的应用程序很简单。
- 配置相对简单(或者您不需要在安装时支持太多配置选项)。
- 您希望为用户提供尽可能简单的安装体验。
- 您的应用程序是无状态的，并且不需要特殊配置。

如果满足以下条件，Operator 是一个更好的选择:

- 您的应用程序需要特殊的功能或配置(如复杂的有状态存储)，这些功能或配置若不使用 CRD 就难以或无法实现。
- 您想要自动化除应用安装或生命周期管理之外的其他流程(如应用备份)。

### 应用安装

 |考虑因素|选择什么|
|-|-|
|没有可用的 Helm Chart|Operator|
|简单安装是首要任务|Helm Chart|
|您的 Kubernetes 经验有限|Helm Chart|
|您想要定制该应用|Operator|

如果您作为用户要在 Kubernetes 上安装一个应用程序，您应该首先检查该应用程序是否存在 Operator 和/或 Helm Chart。许多项目同时提供两者，但如果只有其中一个可用，那么如何安装该应用程序的问题就解决了:使用任何存在的东西。

如果您同时找到了 Operator 和 Chart，如果满足以下条件，请选择 Helm:

- 您想要简单的安装体验。
- 您不需要定制该应用。

如果您已经熟悉 Operator，并且/或者您需要以 Helm 无法实现的方式定制该应用，则 Kubernetes Operator 更具优势。

## 总结

有时，使用 Operator 而不是 Helm 并没有明确的优势，反之亦然。毕竟，两种解决方案支持大多数相同的用例。

但在底层，Operator 更复杂和可定制化，这对于高级应用程序安装或维护任务来说是一个优势。对于更简单的需求，Helm Chart 通常是更好的解决方案。
