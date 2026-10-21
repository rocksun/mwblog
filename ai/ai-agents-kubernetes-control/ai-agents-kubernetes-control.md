<!--
title: AI智能体与Kubernetes：控制循环中各自的职责定位
cover: https://cdn.thenewstack.io/media/2026/10/7d96e1b7-sara-canonici-ztnx3xxzyvc-unsplash.jpg
summary: 本文探讨了AI智能体与Kubernetes在控制循环中的分工协作。智能体擅长推理、分析复杂环境并提出优化方案，而Kubernetes及其Operator则负责基于规则的确定性执行与状态调谐。将两者结合并设置安全边界，能够实现更高效、可靠的云原生集群管理。
-->

本文探讨了AI智能体与Kubernetes在控制循环中的分工协作。智能体擅长推理、分析复杂环境并提出优化方案，而Kubernetes及其Operator则负责基于规则的确定性执行与状态调谐。将两者结合并设置安全边界，能够实现更高效、可靠的云原生集群管理。

> 译自：[AI agents vs. Kubernetes: where each belongs in the control loop](https://thenewstack.io/ai-agents-kubernetes-control/)
> 
> 作者：Vikram Seshadri

**Kubernetes一直依赖智能体**，只不过不是今天AI对话中主导的那类。控制器观察当前状态，将其与声明的目标状态进行比较，并采取行动缩小差距。这种相似性使得[AI智能体和Kubernetes](https://thenewstack.io/agentic-ai-kubernetes-management/) Operator听起来似乎可以互换。但事实并非如此。

这个问题已经不再是理论探讨。在过去的18个月里，智能体工具已经从副业演变为云原生技术栈的一部分。CNCF已将智能体框架纳其Sandbox（沙箱），Kubernetes SIG Apps也将Agent Sandbox纳为子项目，用于[安全运行智能体工作负载](https://thenewstack.io/securing-kubernetes-ai-agents/)。

平台团队已经在决定智能体可以在生产集群中更改什么，通常是一次一个拉取请求（Pull Request），且没有书面策略。默认情况下，推理和执行之间的边界是由惯例而非设计设定的。

---

***KubeCon + CloudNativeCon将于11月9日至12日在犹他州盐湖城举行。*[立即注册](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)*!***

---

Kubernetes Operator的设计初衷是具有可预测性。它根据编码规则协调资源，重试失败的操作，并收敛到声明的状态。而当期望的结果明确但路径未知时，AI智能体就派上用场了。它可以调查不熟悉的情况，从多个系统收集上下文，权衡利弊，并提出行动方案。

一种更安全的架构模式结合了这些优势。智能体提供推理和上下文。Operator、策略引擎和其他确定性系统则保留对执行的控制权。

## Kubernetes的推理层

![工作流程图，说明了智能体如何增加推理能力，同时Kubernetes Operator保持对集群外部的控制。](https://cdn.thenewstack.io/media/2026/10/8319c569-figure1-shelby-brittain.png)





*点击放大图片。*

[kagent是一个开源的CNCF Sandbox项目](https://kagent.dev/docs/kagent/introduction/what-is-kagent/)，它提供了一个这种模式的具体示例。它将AI智能体作为Kubernetes资源运行，并将它们连接到Kubernetes、Helm、可观测性和自定义工具。智能体可以检查资源、检索日志和事件、查询指标、查阅文档并协调专门的智能体。

但这并不意味着每个工具都可以被自由执行。非敏感的读取操作可以自动运行，而诸如应用、修补或删除资源等更改则[需要明确批准](https://kagent.dev/docs/kagent/examples/human-in-the-loop/)。这种分离使得智能体能够进行广泛的调查，而不会赋予不确定的推理过程对集群的无限制权限。

> “这种分离使得智能体能够进行广泛的调查，而不会赋予不确定的推理过程对集群的无限制权限。”

由此产生的运维循环如下：观察、诊断、提出建议、批准、调谐和验证。前三个步骤受益于智能体推理。Kubernetes及其Operator处理调谐步骤。验证则闭环了整个过程，而不假设成功接受的更改产生了预期的结果。

## Karpenter展示了区别

考虑这样一个集群：[Karpenter成功配置了容量](https://thenewstack.io/self-healing-gpu-nodes/)，但平台团队仍然看到利用率不足的节点、缓慢的整合、Spot实例的频繁更替（churn）或挂起的Pod。Karpenter本身已经是一个Operator。它评估调度约束并协调NodePool和NodeClaims。用大语言模型（LLM）替换该逻辑会使原本可靠的控制循环变得不可预测。

基于kagent的运维智能体应该在Karpenter之上工作。它可以检查NodePool和EC2NodeClass（针对EKS集群）的配置、挂起的Pod、Kubernetes事件、Pod Disruption Budget（Pod中断预算）、Karpenter日志以及相关的Prometheus指标。然后，它可以询问为什么观察到的行为与团队的目标不同。

![说明受限的 Karpenter 改进循环的图表。](https://cdn.thenewstack.io/media/2026/10/57718106-figure2-shelby-brittain.png)





*点击放大图片。*

调查可能会发现，[Pod Disruption Budget正在阻碍整合](https://karpenter.sh/docs/concepts/disruption/)，一个do-not-disrupt（禁止中断）注解将节点固定在原地，或者中断预算正在阻止驱逐。它可能还会发现，对于突发性工作负载而言，consolidateAfter（整合延迟）设置得过于激进，从而产生了不必要的中断。它还可以识别出实例约束，导致Karpenter在选择Spot容量时灵活性过低。

> “Karpenter本身已经是一个Operator。用大语言模型替换该逻辑会使原本可靠的控制循环变得不可预测。”

智能体的输出不应是诸如“优化NodePool”之类的模糊建议。它应该呈现证据、识别权衡，并生成一个精简的配置补丁（Patch）。对NodePool中断预算的更改应说明可能受影响的最大节点数。整合更改应说明团队将观察工作负载稳定性的多长时间。实例选择的扩展应保留架构、可用区和工作负载的约束。

然后，补丁通过批准或策略门控。一旦批准，Karpenter就会使用其现有的调度和中断逻辑进行调谐。智能体在一段确定的时间内观察结果，并检查整合是否有所改善，同时没有增加挂起Pod的延迟或有害的中断。如果不符合验收标准，系统可以通过相同的受控路径建议或启动回滚。

## Argo CD应用升级，智能体构建依据

考虑一个平台团队升级由Argo CD管理的Helm Chart。在Git中更改Chart版本很简单。了解该更改将如何影响正在运行的应用程序则需要更多的工作。Argo CD可以显示哪些资源发生了变化；而智能体可以帮助解释这些变化对工作负载意味着什么。

例如，新版本的Chart可能会重命名团队用于配置其就绪探针（readiness probe）的值。智能体可以比较发行说明、现有值和渲染后的清单，以确定升级是否会静默回退到默认值。它应该将这一发现转化为一个聚焦的拉取请求，更新Chart版本和受影响的值，解释运维风险，并定义上线前所需的检查。

一旦拉取请求通过审查并合并，Argo CD就会渲染Chart，并在应用程序配置的同步策略下同步生成的清单。然后，智能体将检查Argo CD的同步和健康状态以及应用程序指标。仅凭成功的同步并不能确定升级是否保持了延迟、错误率或可用性。

如果这些检查失败，智能体可以通过相同的审批流程提出Git回滚或恢复计划，并考虑回滚无法撤销的任何数据或架构更改。责任分工保持清晰：智能体进行调查、提出建议和验证；Argo CD负责调谐已批准的目标状态。

## 自主性需要靠实力争取

团队可以逐步引入这种模式。从只读调查员开始。接下来，允许智能体生成补丁或拉取请求。然后允许经过批准的、具有明确范围和回滚条件的低风险更改。只有结果可衡量且被充分理解的操作才能实现自主。

> “重要的边界不在于智能体是否可以调用 kubectl、Helm 或云 API。而在于每个操作是否都经过授权、受到限制、具备可观测性且可回滚。”

重要的边界不在于智能体是否可以调用 kubectl、Helm 或云 API。而在于每个操作是否都经过授权、受到限制、具备可观测性且可回滚。

Kubernetes可以运行帮助管理Kubernetes的智能体，但前提是每个组件都坚守其最擅长的工作岗位。智能体负责推理不确定的情况，Operator负责调谐声明的状态，而策略则为两者设定限制。人类仍然对系统从推荐走向自主的速度负有责任。