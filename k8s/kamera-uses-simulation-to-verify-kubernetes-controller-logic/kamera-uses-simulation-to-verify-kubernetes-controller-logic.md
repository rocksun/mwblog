
<!--
title: Kamera：模拟验证Kubernetes控制器逻辑
cover: https://cdn.thenewstack.io/media/2025/11/e53322bc-round-icons-ckymflj2lig-unsplash.jpg
summary: Tim Goodwin开发Kamera，模拟Kubernetes控制器行为，无需集群即可调试。它解决控制器管理和调试挑战，助力Kubernetes成为通用控制平面。
-->

Tim Goodwin开发Kamera，模拟Kubernetes控制器行为，无需集群即可调试。它解决控制器管理和调试挑战，助力Kubernetes成为通用控制平面。

> 译自：[Kamera Uses Simulation To Verify Kubernetes Controller Logic](https://thenewstack.io/kamera-uses-simulation-to-verify-kubernetes-controller-logic/)
> 
> 作者：Joab Jackson

[Tim Goodwin](https://discrete.events/)是加州大学圣克鲁兹分校的研究生，他一直在深入思考Kubernetes的未来。他看到一个超越集群的世界，在这个世界里，Kubernetes可以成为几乎任何事物的通用控制平面。

实现这一目标的关键是控制器（controllers）的魔力，它们基于[Kubernetes 控制器运行时](https://github.com/kubernetes-sigs/controller-runtime)构建。组合控制器以及将它们连接在一起的能力，正是Kubernetes强大功能的重要来源。

然而，控制器管理和调试起来非常困难。因此，Goodwin创建了一款名为[Kamera](https://github.com/tgoodwin/kamera)的控制器模拟软件，它通过模拟和模型检测，提供有针对性的工具来捕获单个控制器的行为以及它们之间的交互。

Kamera 使用真实的控制器代码，并且不需要集群即可运行——事实上，它在开发者的笔记本电脑上就能很好地运行。

Goodwin 在本月早些时候的[KubeCon + CloudNativeCon NA 2025](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) 上介绍了这项技术。

## Kubernetes 作为通用控制平面

Kubernetes [最初创建](https://thenewstack.io/how-the-kubernetes-community-celebrated-its-10th-anniversary/)是为了在集群上运行容器化应用程序，此后也已扩展到管理其他资源。

如今，数据库、[Argo CD](https://thenewstack.io/survey-argocd-leaves-flux-and-other-gitops-platforms-behind/) 等 CI/CD 系统、[Crossplane](https://thenewstack.io/kubecon-24-crossplane-a-developer-friendly-control-plane/) 等外部基础设施平台，以及最近的[机器学习 (ML) 系统](https://thenewstack.io/jumpstart-ai-workflows-with-kubernetes-ai-toolchain-operator/)都由 Kubernetes 控制。

Goodwin 说，Kubernetes 有潜力成为“我们想要的任何事物的通用控制平面”。“几乎任何可以声明性描述并持续协调的事物，我们都可以用 Kubernetes 来管理。”

在 Kubernetes 中，用户使用[声明性语言](https://thenewstack.io/kubernetes-is-getting-a-better-yaml/)，以资源的形式描述其系统的期望状态。控制器通过控制循环持续地将实际状态与期望状态进行协调。它们监控从 API 服务器发送的一系列更改事件，并向服务器响应必要的更改。

[![](https://cdn.thenewstack.io/media/2025/11/2742a54d-kubecon25-goodwin-controllers-01.png)](https://cdn.thenewstack.io/media/2025/11/2742a54d-kubecon25-goodwin-controllers-01.png)

在[自定义资源定义](https://thenewstack.io/kubernetes-crds-what-they-are-and-why-they-are-useful/) (CRD) 的帮助下，您也可以编写控制器来运行非 Kubernetes 资源以定义资源。

控制器也可以被聚合和集体控制，为尚未出现的平台铺平道路。

“正是这种组合技术使我们能够提高抽象级别，”Goodwin 说。

## 管理和调试控制器的挑战

然而，控制器很难管理，尤其是在数量众多时。它们会陷入竞态条件。它们基于过时的数据运行，如果编写不当，可能会产生非确定性结果。

Goodwin 说，对于控制循环，“业务逻辑相当简单，但您需要注意许多事情，以确保此业务逻辑在协调循环中稳健运行。”

[![代码比较](https://cdn.thenewstack.io/media/2025/11/20f5f5a1-kubecon25-goodwin-controllers-02.png)](https://cdn.thenewstack.io/media/2025/11/20f5f5a1-kubecon25-goodwin-controllers-02.png)

编写控制循环可能很困难。第一个条件可能已满足（即创建 StatefulSet），但控制器可能在后续状态初始化（启动无头服务器）之前崩溃，从而使控制器接收到应用程序正在运行的错误信号。因此，创建操作必须是独立的。(Goodwin)

Goodwin 说，除了单个控制器外，将它们聚合起来也会带来挑战，因为开发者还需要考虑多个控制器的复合逻辑。

确保每个单独的控制器按计划工作并不能保证它们在集体运行时不会造成某种损害。管理单个资源的两个控制器可能会争夺控制权，导致竞态条件。

他说：“当这些交互出现问题时，调试起来会非常令人头疼。”

这类错误可能出现在代码更改、配置更改或资源更改中。而且，如果您运气真的不好，这些竞态条件可能会一直发生，或者只是偶尔发生。

目前，几乎没有工具可以提供帮助。在许多情况下，开发者能做的最好事情就是拉出控制器的日志文件，并猜测一切出错时的集群状态。

他说：“由于这些类型的问题可能在非常特定且可能短暂的条件下重现，因此当存在可重现性挑战时，我们的整体调试过程就变得更加困难。”

欢迎来到分布式程序调试地狱。

## 使用 Kamera 探索执行空间

Goodwin 编写 Kamera 是为了帮助开发者更好地了解集群状态。

他说：“对于给定的协调过程，Kamera 将显示该过程中涉及的所有控制器操作。”“因此，如果存在一些问题，我们可以准确了解导致问题发生的原因。”

为了节省时间，Kamera 模拟一个集群。通常，控制器通过 [Kubernetes API 服务器](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/) 与系统交互；Kamera 使用模拟的 API 客户端接口模拟服务器。

Goodwin 说：“如果您有控制器运行时实现，您可以将它们连接到此工具，而无需进行任何额外的代码更改。”

该软件用 [Golang](https://thenewstack.io/introduction-to-go-programming-language/) 编写，在一个 CPU 线程上运行，可以在笔记本电脑上运行。不需要集群。

该软件的工作原理是表示集群（或更普遍地说，系统），并逐步创建 [ReplicaStates](https://www.youtube.com/watch?v=fCMPpVLWnpA) —— 遵循所有其他被调用的控制器 —— 并持续进行，直到所有控制器状态收敛且没有待处理的协调。

他解释说：“这意味着我们处于某种状态，其中每个与该状态内容相关的控制器都已观察到这些内容，并决定不需要对其进行任何更改。”

如果它有效，则意味着您的控制平面逻辑是健全的。

## 分布式程序调试困境

如果模拟陷入循环，则意味着出现问题。可能存在竞态问题，或者每次执行时都会产生不同结果的[非幂等](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent)操作。或者可能存在其他非确定性操作，导致状态不断转移到其他（ presumably）收敛状态。

如果您在真实的集群上运行这些操作，则所有控制器描述的一系列操作可能会导致集群严重崩溃。幸好这是一个模拟。

[![建模执行空间](https://cdn.thenewstack.io/media/2025/11/de1722b6-kubecon25-goodwin-controllers-03.png)](https://cdn.thenewstack.io/media/2025/11/de1722b6-kubecon25-goodwin-controllers-03.png)

Goodwin 说：“我们能在模拟中创建这些场景真是太棒了。”

## 建模执行空间

Kamera 不仅可以模拟组件的操作，它还将对整个执行空间进行建模，以验证上述任何错误都不会发生。

Goodwin 说：“我们可以使用我们的执行模型全面搜索所有可能的执行路径，并检查感兴趣的属性，如稳定收敛。”

这个过程称为模型检测，“穷尽探索系统可以进入的所有可能状态空间，以验证我们关心的某些属性始终成立。”

每个控制器的每一个执行路径都经过穷尽测试，实际上[创建了一个图](https://thenewstack.io/gql-a-new-iso-standard-for-querying-graph-databases/)，其中包含所有可能的系统状态（无论您指定多深）。每个由此产生的收敛空间都被跟踪和比较。每个收敛状态都可以通过分步操作器进行探索，以查看采用了哪些执行路径。

他说：“这让我们能够逐步完成每次协调，并以精细的方式检查集群状态是如何演变的。”

为了在真实的云原生软件上测试 Kamera，Goodwin 使用该软件来查看 [Knative](https://thenewstack.io/knative-has-finally-graduated-from-the-cncf/) 无服务器软件中的各种服务如何相互协调。不出所料，他发现该程序是健全的。

Kamera 的方法与 [SimKube](https://github.com/acrlabs/simkube) 不同，后者更像是一种在集群上已经发生的动作的[重放机制](https://thenewstack.io/simulate-kubernetes-cluster-behavior-with-simkube/)。

Kamera 是开源的，但 Goodwin 警告说，该软件目前仅处于“研究就绪”阶段，并正在寻求 Kubernetes 社区的更多反馈。

尽管存在一些粗糙之处，但这款软件对于调试 Kubernetes 集群中顽固难以捉摸的异常行为来说，可能会是一个非常有用的工具。

或者为 Kubernetes 尚未设想过的控制系统进行规划。