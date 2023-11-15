<!-- 
# 通过平台工程实现开发者的赋能，自服务工具
https://cdn.thenewstack.io/media/2023/11/569cf34a-bridge-7777586_1280-1024x574.jpg

 -->

开发团队最需要的是那些能够提高他们工作效率和自治性的工具。不仅要实现构建、测试和部署的低摩擦度，还要能够理解应用程序中的运行情况。

> 译自 [Developer Empowerment Via Platform Engineering， Self-Service Tooling](https://thenewstack.io/developer-empowerment-via-platform-engineering-self-service-tooling/) 。

随着[平台工程](https://thenewstack.io/platform-engineering/)在许多科技组织中越来越广泛地采用并不断发展，仍有大量工作有待开展。虽然它通常会导致技术和流程的变化——比如实现[内部开发者平台](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/)或门户网站——但关键的变化在于文化和交流。许多团队在掌握这方面仍在挣扎，随之而来的是平台的采用正在降低。

平台工程依赖将[平台视为产品的思维模式](https://thenewstack.io/platform-engineering-demands-a-product-mindset/)，并具有紧密的反馈循环，以激励内部开发者客户采用平台——而不是强迫他们做任何事情。 

与传统演讲不同，当[Adriana Villela](https://www.linkedin.com/in/adrianavillela/)和[Ana Margarita Medina](https://www.linkedin.com/in/anammedina/)登上[KubeCon + CloudNativeCon北美洲](https://thenewstack.io/what-will-be-hot-at-kubecon-platform-engineering-of-course/)的舞台时，这两位来自[ServiceNow Cloud Observability](https://www.servicenow.com/products/observability.html?utm_content=inline-mention)(原Lightstep)的[Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline-mention)大使和开发者倡导者进行了角色扮演。他们展示了内部开发者和平台工程师之间这种复杂关系的动态，以期找到共同点并在这枚硬币的两面之间建立同理心。

从他们这里了解如何利用同理心找到技术和交流的途径，即使该技术不断变化，需求也在不断变化。

## 同理心需要双向奔赴

![](https://cdn.thenewstack.io/media/2023/11/bf780066-what-do-developers-want-1024x576.jpeg)

“我们确实知道软件一直在变化，但我们使用软件的方式也一直在不断变化，”Medina说。“事实上，这取决于您组织或客户的规模。”

这包括[DevOps](https://thenewstack.io/devops/)的发展用于协作，[站点可靠性工程](https://thenewstack.io/observability/)(SRE)用于保证正常运行时间，现在是平台工程用于提升开发者体验。但是，她继续说道，“我们也必须记住，平台工程不仅仅关乎开发者体验。它还包含安全考虑、可靠性和其他一些事情。”

平台工程确实是一个跨职能的社会技术项目。

随着平台工程的发展，她继续说道，存在这样的设置——平台工程部门包括SRE团队，或者一个更大的SRE团队，然后有一些工程师专注于平台工程。然后还有一些组织在他们的旅程中更进一步，比如[Netflix的复杂开发者效率提升](https://thenewstack.io/developer-productivity-engineering-at-netflix/)。

“这确实打破了信息孤岛。它允许人们聚集在一起真正进行协作，” Median说。“当然，我们试图做的大部分事情都是为了将事物编码以使其更可重复和可靠。”

但是，即使信息孤岛已经消除，即使我们正在讨论所有工程师，开发人员和平台工程师真的说同一种语言吗？

“作为开发人员，我们构建、测试和部署的方式变得更加复杂，”在扮演开发人员角色时，Medina说道，在公共云、无服务器工作负载和Kubernetes的时代，她感叹她的工作自治性的丧失。

“不幸的是，这意味着作为开发人员，如果我想在需要时访问我需要的东西，我就取决于其他团队为我建立这些东西。我要看平台工程团队的脸色，我恨等待别人为我做事，”她说。

的确，一个平台工程团队的待办事项永远不会少。但他们往往陷入执行运维角色的状态，以至于无法构建那些[黄金路径](https://thenewstack.io/how-to-pave-golden-paths-that-actually-go-somewhere/)和自动化。

“好的，作为平台工程师，我们掌控着所谓的云平台，但听着，不全是为了你。不全是为了提升[开发体验](https://thenewstack.io/can-devex-metrics-drive-developer-productivity/)。我们也必须维护可靠的系统。这太多工作了，我们压力非常大。我们正处于被Jira任务淹没的状态，”Villela回答道，扮演一个平台工程师的角色。“事态已经发展到我不再享受我的工作。我想做一些很酷的事情”，比如自动化流程和使系统更可靠。

这会导致数小时甚至数天的等待时间，让开发者感到非常沮丧。“我不得不向管理层解释我被另一个团队阻塞，并且我在不断等待，”Medina反驳道。“我希望我需要的基础设施准备好了，当我需要它的时候。你在这里真的在限制我的工作。”

而且，她继续说，这些稳定和安全的环境无论在哪里看起来应该都是一样的。“我不太关心底层基础设施在运行什么。我只需要让事情起作用。”

这种充满摩擦的动态对组织来说非常不健康。再加上来自业务端加快发布速度的新压力。当团队变小时。而这些瓶颈仍在持续。

## 将交付工作进行编码

“我猜我们正在对我们交付给您的内容进行编码，但我们没有对交付进行编码，”Villela承认，当她继续扮演平台工程师的角色时。

通过以交付即代码为目标，团队可以实现以下基础设施:

- 按需提供
- 可重复使用
- 可靠
- 内置安全防护
- 在[云成本](https://thenewstack.io/devfinops-and-ai-to-provision-exactly-the-right-cloud-spend/)和[环境影响](https://thenewstack.io/want-to-save-the-world-start-by-cutting-your-cloud-costs/)方面更高效

虽然一些组织确实从头开始构建，但已经有大量关注自助交付的内部开发者平台和门户工具，包括：

- Crossplane
- Backstage
- Kratix
- [Port](https://www.getport.io/?utm_content=inline-mention)

Villela后来提到，这并不意味着非此即彼，而是这两种或多种工具可以协同工作以推动内部开发者体验——她后来演示了这一点。 Medina补充说，特别是当一切都以声明式代码完成时，价值才会出现，这增加了可重复性和可靠性。

![](https://cdn.thenewstack.io/media/2023/11/cda9e94e-kratix-crossplane-cloud-native-platform-1024x582.png)

Villela接着继续演示了典型的内部开发者平台或IDP提供，包括：

- [OpenTelemetry](https://opentelemetry.io/)：生成、摄取和转换数据以进行分析的可观测性后端。
- [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)：用于从基础设施和/或代码中摄取数据，然后使用处理器来转换数据以执行诸如屏蔽、批处理和创建样本数据之类的操作。然后它使用exporter导出到可观测性后端。
- [OpenTelemetry Operator for Kubernetes](https://github.com/open-telemetry/opentelemetry-operator)：在Kubernetes上管理和部署OTel collector。

随着角色扮演的继续，开发人员Medina说上面列出的所有东西都不是她的团队正在寻找的任何工具。因为Villela没有把她当作客户对待。我们知道，与其列出平台中使用的产品，不如使用“[平台即产品](https://thenewstack.io/how-to-host-your-own-platform-as-a-product-workshop/)”方法来展示内部开发人员痛点背景下的好处。并保持迭代小巧，闭环开发者反馈。

## Kratix的“承诺”做得更好

应用开发团队最常需要的工具是那些能够提高他们的速度和自治性的工具。不仅要以较少的摩擦来构建、测试和部署，而且要能够了解他们的应用中发生的事情，然后更容易进行调试。

![](https://cdn.thenewstack.io/media/2023/11/daf1efcd-kratix-open-source-platform-orchestrator-example-1024x587.png)

Villela的内部销售演说——包括可视化工作流程——在这一点上转为谈论她的平台团队如何使用[Kratix](https://kratix.io/)(一个开源平台编排器)在平台后面打包所有上述云原生工具，她解释说，它通过Kubernetes YAML文件以“Promise”交付功能。

这个Promise实际上是一个封装的功能，允许开发者请求利用某种功能或Promise的资源。Kratix不仅交付功能，还将其捆绑为[Kubernetes原生API即服务](https://thenewstack.io/the-flywheel-effect-of-kubernetes-apis/)。请记住，开发者希望访问内部开发者平台的首选方式是通过API的可扩展性。

平台团队拥有安装了Kratix的控制集群，然后不同的开发团队各自与他们的特定基础设施进行交互，在本例中，每个团队都提供了一个额外的Kubernetes集群。平台团队也拥有这些工作集群的所有权，因此Kratix可以为开发团队安装能力。

在现场演示中，开发人员需要提交一个简化的YAML文档作为API请求，并收到他们真正想要的——一个已经配置为在Jaeger用户界面中查看可观测性数据的Go应用程序示例——作为服务。在背后，KubeCon观众看到，平台通过在平台集群上管理cert-manager Promise和Otel operator Promise来提供这个简单的接口，然后将必要的组件安装到相关的工作集群上。

对于某些组织来说，让应用开发人员编写Kubernetes YAML本身就是在考虑开发人员体验时的一个反模式。这就是为什么使用Kratix在[Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)之上构建用户友好的开发者平台API开始带来回报的原因。就像任何API一样，平台API使消费者能够为他们使用合适的接口，无论是[内部开发者门户](https://thenewstack.io/internal-developer-portal-what-it-is-and-why-you-need-one/)(如Port或Backstage)、CLI或脚本语言，甚至是聊天机器人。

## 开发“平台即产品”组织的提示

这对专家提供了一些进一步的见解，关于如何在工程组织内培养“[平台即产品](https://thenewstack.io/platform-as-a-product-true-devops/)”的心态：

- 不要只是将DevOps团队改名为平台团队，然后不改变流程和沟通。
- 请记住，正如[Atlassian的开发者体验](https://thenewstack.io/measure-developer-joy-not-developer-productivity-atlassian-says/)所提醒我们的，每个组织都有不同的需求和不同的体验。
- 平台的成功取决于开发和平台团队之间的双向沟通和协作。
- 尽可能对许多事项进行编码。

“我们可以看到，在这种情况下，团队——像SRE、开发人员、平台工程师——都可以聚集在一起共事，使用自助服务工具使事情更令人愉快、更可靠，并具有更多的协作性。“Medina总结道。”老实说，我们越少使用Jira越好。“
