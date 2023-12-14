<!--
title: Monokle：轻松实现Kubernetes策略管理
cover: https://cdn.thenewstack.io/media/2023/12/884e07a1-rules-1024x602.jpg
-->

Monokle使用普适实用的安全策略，迅速轻松地支撑起您的团队工作，并配备可扩展的高级功能，随着业务发展成长。

> 译自 [Monokle: Kubernetes Policies Made Easy](https://thenewstack.io/monokle-kubernetes-policies-made-easy/)，作者 Ole Lensmar 是 Kubeshop 的 CTO。Ole 在 20 世纪 90 年代后期开始构建基于 HTTP/XML 的 API，此后曾担任几家初创公司和公司的 CTO，包括 SmartBear 和大使实验室的产品架构师。他是 base8 的联合创始人，...

开始使用 Kubernetes 是一个棘手的过程。从重新学习如何针对云原生基础设施构建应用程序，到适应以声明式和主要由 YAML 驱动的应用程序配置方法，Kubernetes 的采用过程中充满了难以攻克的挑战。

也许最具挑战性，如果不是最紧迫的障碍就是，当你发现并非所有的 YAML 都具备相同的安全性或合规性。引入一种工具来帮助你和你的团队正确编写 YAML 配置，这对采用的成功至关重要。

起初，你可能会选择使用 YAML 检查工具或 IDE 插件来协助 YAML 编写，但你会意识到，仅在本地实施配置规则(或“策略”)是不够的，因为配置可以轻易地“溜过”并最终进入你的 Git 仓库或集群而没有在本地验证，这会导致另一个棘手的调试过程。

或者，你可能会开始在集群中安装专用的策略工具，如 Kyverno 或 OPA Gatekeeper。但是很快你会发现，虽然这些工具非常强大，但它们并不适合刚接触 Kubernetes 并只想启用基本安全策略的人。在启用一些基本策略之前，你最终还需要学习更多 YAML 和它们各自的“策略语言”。

您真正需要的是一个策略解决方案，它可以让您和您的团队使用常识安全策略和全生命周期最佳实践快速而直接地入门，而不需要学习新的策略语言，同时具有您在Kubernetes之旅中不断成熟时可以继续使用的高级功能。

请看 Monokle！

## Monokle是什么？

Monokle是一个全面的开源Kubernetes策略实施平台。Monokle极大地简化了以下任务：

* 定义和管理配置策略
* 在整个开发生命周期中实施策略
* 识别和修正代码和集群中的错误配置

为实现这一点，Monokle平台提供了三套工具:

1. **策略实施工具**，您可以在开发生命周期中使用它来根据定义的策略检查YAML配置。它们包括:

* Monokle VS代码扩展
* Monokle CLI
* Monokle GitHub机器人和操作
* Monokle准入控制器
* Monokle 桌面版

2. **策略管理控制台**

* 一个基于浏览器的控制台，用于管理和跟踪将在上述实施点中使用的策略。
* Monokle Cloud在云中运行控制台。 
* Monokle Enterprise是Monokle Cloud的一个内部部署，具有单点登录集成功能。

3. **配置IDE**

* 专门用于识别和修复配置和集群中的配置错误的可视化开发工具。
* Monokle Desktop
* Monokle Web IDE(Monokle Cloud的一部分)

## 80+ 配置策略规则 —— 不需要编码

Monokle 开箱即用提供了 80 多条策略规则，无需学习任何策略语言即可上手使用。包含的规则正是你对一个现代策略平台的所有期待:

- **安全规则**可以确保你的部署不会暴露可利用的攻击面，包括符合 NSA/CIS 框架的合规性。
- **资源使用**规则可以确保你的应用程序正确使用资源。
- **资源元数据**规则可以确保你的资源具有正确的元数据。
- **Kubernetes 版本兼容性**规则可以确保/验证与目标 Kubernetes 版本的兼容性。
- **资源链接**规则可以确保资源不会引用无效/未知的对等资源。

![](https://cdn.thenewstack.io/media/2023/12/e0c0c9cb-image1a.png)

如果这些规则不能满足你的验证需求，定制策略当然也是可能的(详见下文)。

## 无所不在的策略实施

Monokle 使在整个开发生命周期中实施策略变得非常容易:

- **VS Code 扩展**集成了本地开发工作流程的实时配置错误检测。
- **Monokle CLI** 允许你在本地或作为 CI/CD/GitOps 工作流程的一部分验证 YAML 配置。
- **Monokle GitHub** 应用程序/机器人将策略实施集成到你的 GitHub PR 和构建工作流中。
- **Admission Controller**在你的集群中实施 Monokle 策略，确保没有配置错误进入部署。

所有这些工具都可以单独运行，也可以与 Monokle Cloud 集成，以确保在所有团队和工作流程中实施相同的策略。

![](https://cdn.thenewstack.io/media/2023/12/0c1c192f-image2a.png)

## 集中式策略管理

虽然上述所有工具都可以单独使用，但将它们捆绑到一个连贯的策略平台 Monokle Cloud 中，是您可以实现策略在开发工作流程中的一致使用而获得重大收益的地方。Monokle Cloud 不仅允许您快速定义、管理和分发策略到项目、存储库和集群，还提供了基于浏览器的 IDE 和大量高级功能来帮助您充分利用策略。

![](https://cdn.thenewstack.io/media/2023/12/b290eb6d-image3.png)

## 配置 IDE 帮您节省时间

Monokle 包括浏览器和桌面版本的配置重点 IDE，具有大量针对配置错误检测和修复的功能，包括:

- **快速修复** - 一键操作以修复常见的配置错误(Monokle Cloud)。
- **实时策略开发** - 开发 ValidatingAdmissionPolicy 并实时查看其影响。
- **模拟运行** - 对 Kustomize 覆盖和 Helm Chart 执行模拟运行以验证其输出并与已部署的应用程序进行比较。
- **集群检查** - 检查集群中的错误配置并在需要时实时修复它们(Monokle 桌面版)。
- 其他。

## 策略功能一应俱全

虽然 Monokle 力求简化基本策略相关任务，但它也理解和接受与复杂和不断发展的应用基础设施中的策略管理相关的更高级的需求和工作流程。

### 抑制

通常需要能够抑制针对特定资源的单个规则，例如，某些 Pod 可能需要能够以 root 身份运行或访问其容器的文件系统来完成工作。Monokle Cloud 提供了一种点按式方法来抑制所需的错误配置，包括一个基于批准的工作流程，其中管理员可以确保只允许授权的抑制。

![](https://cdn.thenewstack.io/media/2023/12/251ead6a-image5a.png)

### 自定义验证器

如果内置的规则库不够用，您当然可以使用 Monokle 的插件开发工具制作自己的验证器插件。例如，如果您想要针对应用基础架构中使用的自定义资源定义(CRD)实施约定。当安装在 Monokle Cloud 中时，自定义验证插件会自动分发到所有上述实施点(VS 代码、CLI、集群)，从而可以轻松确保所有人都使用自定义验证插件及其相应规则的正确版本。

![](https://cdn.thenewstack.io/media/2023/12/194e7871-image6.png)

### 验证见解

随时间跟踪 Git 存储库中的错误配置有助于您检测到从稳定的零错误配置路径到意外偏离的情况，并跟踪您的团队在改进 YAML 配置质量方面的进步。

### 策略组合

当将策略应用于不同的运行时命名空间/集群时，通常需要在所有区域实施“基本策略”，然后覆盖命名空间/集群特定的策略。Monokle 允许您实现这一点，无论是手动还是通过 Monokle Cloud 中提供的点按界面，都可以实现高级策略实施场景而且很容易实施。

### Helm/Kustomize 模拟运行验证

使用 Helm 或 Kustomize 等工具为不同要求的不同环境生成大量 Kubernetes 资源的模板和生成是扩展应用程序配置的常见方法。就像将策略应用于纯 YAML 配置一样，Monokle 允许您在本地或 CI/CD 工作流程中验证这些工具的输出，以确保生成的清单在提交到源代码控制或部署到集群之前符合您的策略。

## 拥抱开源

所有 Monokle 实施点工具和核心验证插件框架都是开源的，采用 MIT 许可，可在 GitHub 上获得。单独使用这些工具而不使用 Monokle Cloud 提供的集中式策略管理和额外功能，是在将它们捆绑到连贯的解决方案 Monokle Cloud 中推广到整个组织之前，很好地“踢踢轮胎”来试用 Monokle 验证引擎和生态系统的方法。

## Monokle 适合您吗？

有一种方法可以找出答案：给它一个试试!

- 登录 [Monokle Cloud](https://app.monokle.com/) 以试用策略管理功能和云 IDE。
- 在 [Marketplace](https://marketplace.visualstudio.com/items?itemName=kubeshop.monokle) 上获取 VS Code 扩展。
- 从 [GitHub](https://github.com/kubeshop/monokle) 下载 Monokle 桌面版。
- 从 Monokle Cloud 内部或通过 [GitHub](https://github.com/kubeshop/monokle-admission-controller) 单独安装 Admission Controller。
- 尝试 [GitHub](https://github.com/kubeshop/monokle-cli) 上的 Monokle CLI。

感到困惑？感兴趣？请[与我们联系](https://monokle.io/contact)进行讨论或演示，了解 Monokle 如何帮助您解决 Kubernetes 策略的复杂性。
