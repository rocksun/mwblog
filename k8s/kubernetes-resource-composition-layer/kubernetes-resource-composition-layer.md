<!--
title: 为什么Kubernetes平台总在重复构建它们本可共享的层
cover: https://cdn.thenewstack.io/media/2026/10/fe7a9f2e-steve-a-johnson-owq7lathhsc-unsplash.jpg
summary: 本文探讨了Kubernetes平台团队频繁重复编写控制器和管道逻辑的现状，分析了缺少资源组合原语的痛点，并以kro项目为例，展示了如何通过将资源依赖关系和组合逻辑转化为可复用的数据，从而简化平台构建。
-->

本文探讨了Kubernetes平台团队频繁重复编写控制器和管道逻辑的现状，分析了缺少资源组合原语的痛点，并以kro项目为例，展示了如何通过将资源依赖关系和组合逻辑转化为可复用的数据，从而简化平台构建。

> 译自：[Why Kubernetes platforms keep rebuilding a layer they could share](https://thenewstack.io/kubernetes-resource-composition-layer/)
> 
> 作者：Adam Crowder

**询问一个平台团队他们去年构建了什么，** 他们的清单很可能包括一个 Kubernetes 控制器，该控制器按顺序创建几个对象并在它们之间复制字段。没有业务逻辑，只有连线。一个 Deployment、前面的一个 Service，以及一个 ConfigMap，其中一个有趣的价值是 Service 在其状态中报告的主机名。[Kubebuilder](https://book.kubebuilder.io/) 把[构建第一个控制器](https://thenewstack.io/kubernetes-controllers-at-scale/)变成了一个愉快的下午。而第十个则带来了它自己的调和错误、升级路径和值班轮换。它是同一个控制器。每次都有点微小的差异，并且它存在于数千个组织中。

## 只有原料，没有食谱

Kubernetes 具备各种原料：CRD 定义了新类型。[控制器](https://kubernetes.io/docs/concepts/architecture/controller/)赋予了它们行为。[服务端应用 (Server-side apply)](https://kubernetes.io/docs/reference/using-api/server-side-apply/#field-management) 跟踪谁拥有每个字段。[CEL](https://kubernetes.io/docs/reference/using-api/cel/) 评估表达式，而 [OpenAPI 架构](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation)为每个字段定义了类型。Kubernetes 没有提供的是食谱。没有任何东西说明几个资源构成了单一事物，或者某一个资源中的值来自另一个资源的状态并且必须等待它。

每一个管理一组资源的工具都在自行构建这一部分，并且不断为其添砖加瓦。Helm 在渲染时这样做，Helm 4 则添加了服务端应用和等待资源状态的功能。Argo CD 拥有[同步波次、钩子 (hooks)](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/)以及[健康检查](https://argo-cd.readthedocs.io/en/stable/operator-manual/health/)，因为清单无法说明它们需要什么顺序或什么时候完成。Crossplane 拥有[组合和函数](https://docs.crossplane.io/latest/composition/compositions/)，而 v2 直接组合了原生的 Kubernetes 资源。Operator 则用 Go 语言手写。剥开它们的外表，内核是相同的：一组对象、它们之间的依赖关系、沿边缘流动的值，以及持续重新检查集群是否仍然匹配的机制。最近的每一个新增功能都在触及该工具所缺乏的部分：顺序、就绪状态、按字段的所有权、集群内部的评估。

> “Kubernetes 具备各种原料。Kubernetes 没有提供的是食谱。没有任何东西说明几个资源构成了单一事物，或者某一个资源中的值来自另一个资源的状态并且必须等待它。”

如果每个人都在构建相同的部分，问题就在于它是否应该被共享。这就是 [kro](https://kro.run/)（即 [Kube Resource Orchestrator](https://thenewstack.io/the-kro-project-giving-kubernetes-users-what-they-want/)）的立场，这也是它为什么在 2025 年 9 月进入 [Kubernetes SIG Cloud Provider](https://github.com/kubernetes/community/blob/main/sig-cloud-provider/README.md#kro) 的原因，它作为一个其他东西得以在其上构建的基础组件，而不是又一个端到端的平台。

## 拆解控制器

Kro 从拆解手写控制器开始。API 机制和生命周期在每个控制器中都是相同的；只有连线存在差异。它的答案——[ResourceGraphDefinition](https://kro.run/docs/concepts/rgd/overview/)，将连线编写为数据，并且由一个控制器来解释每个定义。CRD、OpenAPI、CEL 和服务端应用本就存在，而 kro 将它们连接了起来。

![Diagram showing parts of the glue controllers that are shared, vs those that differ.](https://cdn.thenewstack.io/media/2026/10/bbfbaa23-image.png)

ResourceGraphDefinition 包含两个可分离的部分：

1. 组合（带有每个实例背后的资源的模板，以及用于它们之间引用的 CEL 表达式）
2. API（一个架构、由此生成的 CRD，以及应用程序团队创建的实例）

## 组合

kro [从 CEL 表达式中的引用推导依赖关系图](https://kro.run/docs/concepts/rgd/dependencies-ordering/)（因此永远不需要显式声明顺序），并在实例存在之前针对 OpenAPI [对每个表达式进行类型检查](https://kro.run/docs/concepts/rgd/static-type-checking/)。开篇示例中的 ConfigMap 需要 Service 的主机名，因此其模板命名了该字段。该引用就是整个排序规则：ConfigMap 从 Service 读取，因此 Service 先生效，没有人需要手动写下顺序。显式声明的顺序是对清单已包含的关系的第二种描述，在任何重命名或重新排序之后，这两者可能会发生分歧。推导出的顺序不会产生漂移，因为它是派生出来的，而不是单独定义的。依赖关系就是引用。如果在需要它的引用之外声明顺序，就会产生两个真相来源，并带来漂移的机会。

## API

平台团队编写 ResourceGraphDefinition，而应用团队则获得与其他团队一样的 Kubernetes API，并照常使用 kubectl、RBAC 和 [GitOps](https://thenewstack.io/how-to-scale-gitops-without-hitting-the-argo-ceiling/)。十个胶水控制器变成了由一个控制器运行的十个定义。将连线作为数据使得 API 的创建成本变低，而廉价的 API 依然是一个承诺。应用程序团队将清单、RBAC 和流水线指向它，从那时起，删除字段就会破坏平台团队无法看到的东西。[kro 会拒绝](https://kro.run/docs/concepts/rgd/overview/#breaking-changes)会破坏现有实例的 ResourceGraphDefinition 架构更改，除非作者明确允许。抽象的成本从编写它转移到了拥有它：十个代码库消失了，留下了十个 API。团队应该统计 API 的数量，而不是控制器。

## 独立的原语

一旦组合变得廉价，人们就发现了更多用例，而且并非所有用例都需要自己的专用 API。在每个带标签的 Namespace 中设置默认拒绝的 NetworkPolicy。将带标签的 Services 折叠为一个 Ingress。安装一次并保持健康的 DNS 堆栈。没有什么直接请求这些；它们对已经在集群中的内容做出反应。它们是一次性定义，不需要可重复的 API。

kro 0.10 为这种情况下引入了一个原语。Graph 是纯粹的组合部分；带有命名空间，没有架构，没有 CRD，也没有实例。Ingress 案例的简写：

```

apiVersion: kro.run/v1alpha1
kind: Graph
spec:
  nodes:
    - id: services
      ref:                          # read only, never owned
        kind: Service
        metadata:
          selector: {matchLabels: {expose: "true"}}
    - id: ingress
      template:                     # created and owned
        kind: Ingress
        spec:
          rules: >-
            ${services.map(svc, {"host": svc.metadata.name + ".example.com", ...})}

```

没有人创建实例。Services 已经存在，Graph 跟踪它们：打上标签就会出现一个规则；移除标签，它就会消失。

![Architectural diagram comparing kro 0.9 and kro 0.10](https://cdn.thenewstack.io/media/2026/10/3c74120a-image.png)

在这两半中，只有一半是全新的。API 部分是一个 CRD，这是 Kubernetes 已经具备的原语。ResourceGraphDefinitions 使它们的编写成本更低，但原语已经存在。组合部分则是 Kubernetes 缺乏、而每个工具都在为自己构建的部分。Graph 就是孤立的那一部分，它独立存在时展现出了以前很容易忽视的一点：API 从来都不是输入，而只是一种输入。组合会根据集群状态进行调和，而自定义资源的新实例只是它可以做出反应的该状态的众多更改之一。无论发生什么变化，工作都是早期的内核：对象、它们之间的引用，以及使它们保持同步的持续声明式调和循环。这就是原语。ResourceGraphDefinition 则是前面带有 CRD 的相同原语。

> “剥离任何创建对象、在它们之间复制值并不断检查的事物的触发器，剩下的就是组合。”

这种拆分具有通用性。剥离任何创建对象、在它们之间复制值并不断检查的事物的触发器，剩下的就是组合。服务于一个自定义资源的 Operator 是一个前面带有 API 的组合。一个按顺序应用清单并等待它们的流水线阶段是一个前面带有提交的组合，去掉了循环。一个创建 Namespace、其配额及其角色绑定的运行手册 (runbook) 是一个前面带有工单的组合。从这个角度来看，问题不再是采用哪种工具，而是组合已经在哪里发生以及是什么在发挥作用。

## 伪装的图 (Graphs)

Kubernetes 平台已经充满了资源图；只是它们没有这样被写出来。一种命名约定使两个清单对一个字符串达成一致。将依赖关系编码为步骤顺序的同步波次或钩子。将状态字段复制到另一个对象中的脚本。每一个的存在都是因为底层的工具无法表达两个对象之间的依赖关系，或者无法看到集群当前拥有的内容，因此依赖关系存在于其他地方，例如字符串、步骤编号或脚本。组合工具将其作为对象之间的引用放回原处。在 kro 中，该引用是一个在图形内部被持续监视和评估的 CEL 表达式。

![Diagram comparing indirect resource dependency methods with direct, continuous object references.](https://cdn.thenewstack.io/media/2026/10/251ae485-image.png)

## 似曾相识的举动

Kubernetes 以前就是这样发展的。滚动更新曾是一个 [kubectl 子命令](https://github.com/kubernetes/kubernetes/pull/88057)，直到 Deployment 控制器接管了它，上面的所有东西都变得更简单了。组合看起来也该有同样的举动。kro 是 [GitHub](https://github.com/kubernetes-sigs/kro) 上的一个 Kubernetes SIG Cloud Provider 子项目，它展示了当组合机制变得可重用且关系变得声明式时会发生什么变化。这个问题比任何单个项目都大：如果组合是几乎每个平台都需要的，难道每个平台都必须自己构建它吗？组合也许就是 Kubernetes 所缺失的原语。