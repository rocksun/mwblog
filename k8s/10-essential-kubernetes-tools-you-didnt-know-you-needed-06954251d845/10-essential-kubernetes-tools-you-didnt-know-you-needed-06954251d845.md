
<!--
title: 您可能不知道的10个必备Kubernetes工具
cover: ./cover.png
-->

随着 Kubernetes 迎来 10 周年庆，其采用率和生态系统呈指数级增长。在 GitHub 上拥有超过 **100,000** 个星标，Kubernetes 已成为云原生生态系统的支柱，能够实现容器化应用程序的可扩展和高效管理。最新版本 [Kubernetes 1.30](https://kubernetes.io/blog/2024/04/17/kubernetes-v1-30-release/) 引入了许多新功能和改进，进一步巩固了其作为领先的容器编排平台的地位。

> 译自 [10 Essential Kubernetes Tools You Didn’t Know You Needed](https://piotrzan.medium.com/10-essential-kubernetes-tools-you-didnt-know-you-needed-06954251d845)，作者 Piotr。

## 简介

然而，要真正发挥 Kubernetes 的强大功能，必须使用合适的工具。在本博文中，我们将探讨十个鲜为人知但非常有用的工具，它们可以增强您的 Kubernetes 体验。从配置问题检测到网络可观测性，这些工具将帮助您更有效地管理集群。无论您是经验丰富的 Kubernetes 用户还是刚入门，您都会发现宝贵的见解和实用技巧，以优化您的 Kubernetes 工作流程。

让我们深入了解这些工具，让您的 Kubernetes 技能更上一层楼！

## 工具类别

我们将要讨论的每个项目都属于一个类别。这些类别有助于在 Kubernetes 上进行设置、管理和开发。我故意避免了可观测性领域中像 Prometheus/Grafana 这样知名且成熟的项目，或网络领域的 Cilium。相反，我们将重点关注那些可能不太为人所知但能为 Kubernetes 用户带来显著益处的工具。

## 1. Popeye

**仓库链接**: [Popeye](https://github.com/derailed/popeye)

**类别**: 配置问题检测

**描述**: Popeye 是一个 Kubernetes 集群清理器。它会扫描您的 Kubernetes 资源并报告集群中潜在的问题和错误配置。Popeye 旨在主动预防，通过定期扫描和审核您的部署、配置和资源定义，确保您的集群干净且符合 Kubernetes 最佳实践。

**解决的问题**: Kubernetes 集群随着时间的推移可能会变得杂乱无章且配置错误，从而导致潜在的稳定性和性能问题。Popeye 帮助识别这些错误配置，例如已弃用的 API 版本、缺少的资源和安全漏洞。通过解决这些问题，Popeye 有助于维护集群的健康和性能，确保它们平稳高效地运行。

**示例用法**: 要在当前 Kubernetes 上下文中运行扫描并扫描所有命名空间，只需使用以下命令：

```
popeye -A -s cm
```

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SrD7f-_kWXvEkW63cPiPQQ.png)

*本地 kind 集群上关于 popeye 的结果*

## 2. KUTTL

**仓库链接**: [KUTTL](https://github.com/kudobuilder/kuttl)

**类别**: 测试

**描述**: `KUTTL` (Kubernetes 测试工具包) 是一套全面的工具集，专为测试您的 Kubernetes 应用程序而设计。它提供了一个简单且声明式的框架来编写、运行和管理测试，确保您的 Kubernetes 配置和应用程序按预期运行。

**解决的问题**: 测试 Kubernetes 配置和应用程序可能很复杂且容易出错。`KUTTL` 通过提供一个与 Kubernetes 无缝集成的声明式测试框架来简化此过程。它允许您定义测试场景和预期结果，使您更容易验证配置并在开发周期的早期发现问题。

**示例用法**: 要使用 `KUTTL` 创建和运行测试，您可以在 YAML 文件中定义测试用例。以下是一个简单测试用例的示例：

创建测试目录结构：

```
my-tests/
├── 00-setup.yaml
├── 01-verify.yaml
├── kuttl-test.yaml
```

在 `00-setup.yaml` 中定义测试步骤：

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
data:
  key: value
```

在 `01-verify.yaml` 中定义预期结果：

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
data:
  key: value
```

使用以下命令运行测试：

```
kuttl test my-tests/
```

此命令将执行测试步骤并验证您在 YAML 文件中定义的结果。

## 3. Kubescape

**仓库链接**: [Kubescape](https://github.com/kubescape/kubescape)

**类别**: 安全筛选

**描述**: `Kubescape` 是一个用于 Kubernetes 集群的安全扫描工具。它通过扫描漏洞、错误配置和对安全标准的合规性，提供对集群安全态势的全面评估。`Kubescape` 利用行业最佳实践和框架，例如 NSA Kubernetes 加固指南，以确保您的集群满足严格的安全要求。

**解决的问题**: 确保 Kubernetes 集群的安全至关重要，但由于环境的复杂性和动态性，这可能具有挑战性。`Kubescape`
通过提供自动安全扫描来简化此任务，这些扫描可以识别漏洞、错误配置和合规性问题。这有助于管理员维护安全且合规的 Kubernetes 环境，降低安全漏洞和不合规的风险。

**示例用法**: 要对您的 Kubernetes 集群执行安全扫描，请使用以下命令：

`kubescape scan framework nsa --exclude-namespaces kube-system`

此命令将根据 NSA Kubernetes 加固指南框架扫描您的集群，排除 `kube-system` 命名空间。

**示例输出**:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vqL8eh9mtE8bJxk4gc7shw.png)

了解更多关于 [Kubernetes 安全加固](https://kubernetes.io/docs/tasks/administer-cluster/securing-cluster/)

## 4. Mirrord

**仓库链接**: [mirrord](https://github.com/metalbear-co/mirrord)

**类别**: 远程开发

**描述**: `mirrord` 是一个远程开发工具，允许开发人员在 Kubernetes 集群的上下文中运行本地进程。这意味着您可以在本地开发和调试应用程序，同时它们与实时 Kubernetes 资源交互，就好像它们在集群中运行一样。`mirrord` 通过在本地和远程环境之间提供无缝桥梁来简化开发过程。

**它解决了什么问题**: 开发和调试在 Kubernetes 上运行的应用程序可能具有挑战性，因为本地环境和集群环境之间存在差异。`mirrord` 通过允许开发人员在本地运行应用程序，同时与 Kubernetes 集群无缝交互来解决此问题。这有助于更快地调试、测试和开发，因为开发人员可以使用他们熟悉的本地工具和环境，而无需将他们的应用程序部署到集群以进行每次更改。

**示例用法**: 要使用 `mirrord` 在 Kubernetes 集群的上下文中运行本地进程：

```
mirrord exec --target-namespace devops-team \
--target deployment/foo-app-deployment \
nodemon server.js
```

有关详细指南和更多示例，您可以参考 [我之前的博客文章](https://medium.com/swlh/remote-development-with-mirrord-a-guide-for-kubernetes-developers-94892122654) 关于使用 `mirrord` 进行远程开发。

## 5. Kube-linter

**仓库链接**: [Kube-linter](https://github.com/stackrox/kube-linter)

**类别**: 代码风格检查

**描述**: `Kube-linter` 是一个静态分析工具，它检查 Kubernetes YAML 文件和 Helm 图表以确保它们符合最佳实践和安全指南。它可以帮助您在部署资源之前发现潜在问题，确保您的 Kubernetes 配置安全高效。

**它解决了什么问题**: 编写 Kubernetes 配置可能很复杂，即使是微小的错误也会导致生产环境中出现重大问题。`Kube-linter` 通过分析您的 YAML 文件和 Helm 图表以查找常见错误、安全风险和与最佳实践的偏差来解决此问题。这种主动方法可以帮助您在开发周期的早期识别和解决问题，从而提高 Kubernetes 部署的整体质量和安全性。

**示例用法**: 要使用 `Kube-linter` 检查您的 Kubernetes 清单，请运行以下命令：

`kube-linter lint 1-create-deployment.yaml`

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*kttqS6RTqb2RGpvKVyqLcA.png)

## 6. k3d

**仓库链接**: [k3d](https://github.com/k3d-io/k3d)

**类别**: 配置

**描述**: `k3d` 是一个轻量级包装器，用于在 Docker 中运行 `k3s` （一个轻量级 Kubernetes 发行版）。它允许您在 Docker 容器内创建和管理 Kubernetes 集群，提供了一种简单的方法来设置和运行 `k3s` 集群，用于开发、测试和 CI/CD 目的。

**它解决了什么问题**: 为本地开发和测试设置和管理 Kubernetes 集群可能很麻烦且资源密集。`k3d` 通过使您能够在 Docker 容器内运行 `k3s` 集群来简化此过程。这种方法减少了设置完整虚拟机或物理服务器的开销，使在本地机器上创建和管理 Kubernetes 集群变得更加容易和快捷。

**示例用法**: 要使用 `k3d` 创建一个新的 `k3s` 集群，请使用以下命令：

`k3d cluster create mycluster`

## 7. Kubeshark

**仓库链接**: [Kubeshark](https://github.com/kubeshark/kubeshark)

**类别**: 网络可观测性

**描述**: `Kubeshark` 是 Kubernetes 的 API 流量分析器，提供对 Kubernetes 网络通信的深入可见性。它捕获、解析和可视化集群中的网络流量，使您能够监控和调试微服务之间的交互。

**它解决了什么问题**: 了解和调试 Kubernetes 集群中的网络通信可能具有挑战性，尤其是在复杂的微服务环境中。`Kubeshark` 通过提供对集群内 API 流量的全面视图来解决此问题。这有助于开发人员和运营人员深入了解服务交互、检测异常并更有效地解决网络问题。

**示例用法**: 要使用 `Kubeshark` 开始捕获流量，请运行以下命令：

`kubeshark tap`

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*r-3mFxPbNMCioAw06zr7aw.png)

*kubeshark web 界面*

## 8. kubectl-tree

**仓库链接**: [kubectl-tree](https://github.com/kelseyhightower/kubectl-tree)

**类别**: 插件

**描述**: `kubectl-tree` 是一个 `kubectl` 插件，它以树状结构显示 Kubernetes 资源。它提供了一种直观的方式来查看和导航您的 Kubernetes 集群，使您能够轻松地了解资源之间的关系。

**它解决了什么问题**: 使用 `kubectl get` 命令查看 Kubernetes 资源可能很麻烦，尤其是在大型集群中。`kubectl-tree` 通过以树状结构显示资源来解决此问题，使您能够更轻松地理解资源之间的关系并导航您的集群。

**示例用法**: 要使用 `kubectl-tree` 查看您的 Kubernetes 资源，请运行以下命令：

```
✗ kubectl tree deployment crossplane -n crossplane-system
NAMESPACE          NAME                                 READY  REASON  AGE
crossplane-system  Deployment/crossplane                -              49m
crossplane-system  └─ReplicaSet/crossplane-6dcbf47db4   -              49m
crossplane-system    └─Pod/crossplane-6dcbf47db4-gzzwp  True           49m
```

## 9. Flux

**仓库链接**: [Flux](https://github.com/fluxcd/flux)

**类别**: GitOps

**描述**: `Flux` 是一套用于 Kubernetes 的持续和渐进式交付解决方案。它自动化资源部署并根据 GitOps 原则将集群状态与存储在 Git 存储库中的配置同步。`Flux` 确保您的 Kubernetes 集群的期望状态（如您的版本控制配置文件中定义的那样）得到持续维护和更新。

**解决的问题**: 手动管理 Kubernetes 配置和部署可能会出现错误，并且难以审计。`Flux` 通过自动化您的 Git 存储库和 Kubernetes 集群之间的同步来解决此问题。通过将 Git 视为真相来源，`Flux` 确保您的集群状态与您的配置文件一致，从而实现可追溯性、可审计性和更轻松的更改回滚。这种方法还通过利用版本控制来促进团队成员之间的协作。

**示例用法**: 要在您的 Kubernetes 集群中安装 `Flux` 并将其连接到您的 Git 存储库，请执行以下步骤：

```
fluxctl identity --k8s-fwd-ns flux
fluxctl sync --k8s-fwd-ns flux
```

 阅读有关 [使用 Flux 和 Crossplane 进行 GitOps](https://medium.com/itnext/gitopsify-cloud-infrastructure-with-crossplane-and-flux-d605d3043452) 的更多信息

## 10. Kubecost

**仓库链接**: [Kubecost](https://github.com/kubecost/cost-model)

**类别**: 成本管理

**描述**: `Kubecost` 是用于 Kubernetes 集群的成本监控和优化工具。它提供有关 Kubernetes 工作负载的成本和资源使用情况的实时洞察。`Kubecost` 帮助您准确分配成本、优化资源利用率并通过识别效率低下和未使用的资源来降低总体云支出。此外，`Kubecost` 与 [OpenCost](https://www.opencost.io/docs/) 集成，这是一个用于 Kubernetes 的开源成本监控和管理项目。

**解决的问题**: 由于容器化工作负载的动态特性和云计费的复杂性，管理 Kubernetes 环境中的成本可能具有挑战性。`Kubecost` 通过提供详细的成本细分、使用情况报告和优化建议来解决此问题。这有助于组织了解其 Kubernetes 支出，就资源分配做出明智的决策，并确定节省成本的机会。

**示例用法**: 在您的 Kubernetes 集群中部署 `Kubecost` 后，您可以访问仪表板以查看成本报告、按命名空间、标签和部署分配成本，并接收有关优化资源使用情况的建议。与 `OpenCost` 的集成通过提供标准化的成本监控和管理功能来增强这些功能。

## 奖励回合

虽然我重点介绍了 Kubernetes 的十个基本工具，但还有许多其他工具可以极大地增强您的 Kubernetes 体验。这些附加工具提供从管理已弃用的 API 到促进远程开发等各种功能，以及更多。以下是一些您可能会发现非常有价值的附加工具列表：

工具名称|描述|代码库
---|---|---
**K9s**|用于管理 Kubernetes 集群的基于终端的用户界面|K9s
**kube-no-trouble**|检查已弃用的 API|kube-no-trouble
**kaniko**|在 Kubernetes 集群中构建容器镜像|kaniko
**arkade**|便携式 Kubernetes 应用市场|arkade
**helmfile**|管理 Kubernetes Helm Charts|helmfile
**kdash**|Kubernetes 终端仪表板|kdash
**werf**|Kubernetes 的 GitOps CI/CD 工具|werf
**kluctl**|Kubernetes 的部署工具|kluctl
**cilium**|Kubernetes 的网络、安全和可观察性解决方案|cilium
**kubeflow**|Kubernetes 的机器学习工具包|kubeflow
**k8sgpt**|GPT 驱动的 Kubernetes 助手|k8sgpt

需要我对这个翻译进行任何解释或补充说明吗？

## 结束语

我们刚刚庆祝了 Kubernetes 的 10 周年，很明显，生态系统比以往任何时候都更加强大和充满活力。Kubernetes 已发展成为云原生环境的关键组成部分，使组织能够高效可靠地大规模管理其容器化应用程序。

我们在本文中回顾的工具，从用于配置问题检测的 `Popeye` 到用于成本管理的 `Kubecost`，都证明了 Kubernetes 生态系统的广度和深度。随着 Kubernetes 继续发展，我们可以期待看到更多创新工具的出现，这些工具将进一步简化和增强我们的云原生之旅。

为了成本管理，展示了 Kubernetes 生态系统的多样性和深度。每个工具都针对特定的挑战，帮助优化或保护 Kubernetes 部署。这些工具的激增突出了 Kubernetes 生态系统的动态特性以及并非所有领域都存在完善的标准。这种多样性允许定制的解决方案，以满足不同组织和用例的独特需求。

展望未来，Kubernetes 有望为世界上更多的基础设施提供动力。随着边缘计算、无服务器架构和人工智能驱动的运营等新趋势的出现，Kubernetes 将继续适应和发展。生态系统通过广泛的工具和解决方案来促进创新的能力，对于满足未来云原生环境的需求至关重要。

您最喜欢哪些项目？您是否使用过您想分享的其他工具？请在评论中告诉我。

感谢您抽出时间阅读这篇文章。希望您觉得它有趣且信息丰富。