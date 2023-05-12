# GitOps 是否为 Kubernetes 的复杂性提供了关键解决方案？

翻译自 [Does GitOps Provide the Key Fix for Kubernetes’ Complexity?](https://thenewstack.io/does-gitops-provide-the-key-fix-for-kubernetes-complexity/) 。

云原生的成功很大程度上归功于 GitOps 现在和未来的成功——该框架已稳步被采用作为支持 Kubernetes 环境的一种方式。

![](https://cdn.thenewstack.io/media/2023/04/7fa47654-capture-decran-2023-04-26-221756mainphoto.png)


可以这么说，Kubernetes 仍然是复杂和困难的。即使是在最好的情况下，管理 Kubernetes 集群和在 Kubernetes 集群上部署应用程序都是一个复杂的过程，至少在解决这些复杂性问题之前还需要一段时间。对于往往没有资源进行云原生转型的中小企业来说，这个环境可能尤其令人望而却步。

但组织正在学习，最终将获得专业知识的新用户数量继续增长——云原生的成功在很大程度上归功于 GitOps。自从 Weaveworks 的创始人兼首席执行官 Alexis Richardson 首先创造了 GitOps 一词以来，该框架一直被视为一种支持 Kubernetes 环境的方式，对某些人来说是一种支持 Kubernetes 环境的方式，对其他人来说也是解决 Kubernetes 大部分问题的一种方式。

![](https://cdn.thenewstack.io/media/2023/04/668f28ef-connection_gitops_kubernetes_stackoverflow-1024x816.png)
*图片：Torsten Volk*


最近举行的 Rejekts 会议（该会议旨在为那些没有被 KubeCon 选中的优秀演讲提供第二次机会）和 KubeCon+CloudNativeCon 会议包括了许多有趣且受到广泛关注的演讲。在为期一天的 ArgoCon 会议上，礼堂座无虚席，而在 KubeCon+CloudNativeCon 期间，Flux 项目会议也吸引了众多参会者。GitOps 成为 Rejekts 和 KubeCon+CloudNativeCon 期间多个演讲的主题，人们对 GitOps 如何继续支持 Kubernetes 采用的热情和乐观情绪是显而易见的。

![](https://cdn.thenewstack.io/media/2023/04/e72f221f-complexity-1024x545.png)
*资料来源：Weaveworks*

GitOps 提供的降低 Kubernetes 集群复杂性、安全管理能力和其他好处最终成为组织在处理集群时进行扩展的驱动因素。

GitOps 使得 Kubernetes 的采用能够扩展——参与发布过程的开发人员和运维人员通过声明性代码提供其贡献，指定整个应用程序的期望状态。这确保了整个应用程序栈的一致配置，其中包含数百个参数和看似成千上万个看似无害但最终代价高昂的错误机会，通过依赖自动协调实际应用程序状态与期望状态的控制器，”企业管理协会（EMA）的分析师 Torsten Volk 说道。“如果出现问题，控制器可以快速将应用程序以及其所有依赖项回滚到之前的状态。这降低了通常伴随每次发布而带来的压力和风险，同时通过维护对应用程序堆栈的任何部分的所有更改的完整历史记录来简化安全审核。”

GitOps 使得 Kubernetes 的采用能够扩展——参与发布过程的开发人员和运维人员通过声明性代码提供其贡献，指定整个应用程序的期望状态。这确保了整个应用程序栈的一致配置，其中包含数百个参数和看似成千上万个看似无害但最终代价高昂的错误机会，通过依赖自动协调实际应用程序状态与期望状态的控制器，”企业管理协会（EMA）的分析师 Torsten Volk 说道。“如果出现问题，控制器可以快速将应用程序以及其所有依赖项回滚到之前的状态。这降低了通常伴随每次发布而带来的压力和风险，同时通过维护对应用程序堆栈的任何部分的所有更改的完整历史记录来简化安全审核。”

## 最佳实践

[OpenGitOps](https://opengitops.dev/) 是 CNCF 应用交付 SIG 下的一个 GitOps 工作组，是一组开放源代码标准、最佳实践和面向社区的教育，旨在帮助组织采用结构化、标准化的方法来实现 GitOps 。它将 [GitOps 原则](https://opengitops.dev/)描述为：

1. 声明式：由 GitOps 管理的系统必须以声明方式表达其所需状态。
2. 版本化和不可变：所需状态以强制不变性、版本控制并保留完整版本历史记录的方式存储。
3. 自动拉取：软件代理自动从源中拉取所需的状态声明。
4. 持续协调：软件代理持续观察实际系统状态并尝试应用所需状态。

通过使用 GitOps 将脚本化的应用程序发布替换为声明式的发布方式，最终结果是将应用程序栈的期望状态交给了持续交付平台的控制器来建立和保护， Volk 表示。 Volk 说：“这种方法实现了最终程度的一致性，因为部署、运行和管理应用程序所需的所有内容都安全地存储在一个通用的代码仓库中。”“新的应用程序将重用此代码的所有通用部分，并且可以在整个组织中接收相同的补丁、更新和配置更改。”

对于开发人员来说，关键的好处是很清晰的：当使用 GitOps 框架工作时，开发人员不一定需要掌握 YAML 文件和 Jenkhttps://thenewstack.io/4-power-tips-to-get-jenkins-enterprise-ready/ins 的工作原理，也不需要理解 Kubernetes 的所有不同操作基础设施和复杂工作方式，无论是节点结构、命名空间等等。在最理想的情况下，开发人员使用 GitOps 以 [Argo CD](https://thenewstack.io/why-argo-cd-is-the-lifeline-of-gitops/) 和 [Flux](https://thenewstack.io/flux-overview-react-state-management-ecosystem/) 等开源替代方案可以创建应用程序并将它们加载到 Git 上，而无需深入理解 Kubernetes 。

对于运营团队来说，GitOps 可以解决 Kubernetes 存在的许多安全问题。通过这种推拉模型和结构， GitOps 可以减轻运维团队的工作负担，因为他们几乎普遍认为 Kubernetes 的管理和安全性至少是一个挑战。

此外，通过策略即代码和其他方式，GitOps 可以用于资源节省。在处理集群时，它可以防止开发人员无意中增加云使用费用。对于运营团队，GitOps 可以帮助更好地管理云资源，避免浪费未使用的集群资源。

再次强调，GitOps 旨在使在 Kubernetes 环境中开发、部署和管理应用程序的过程变得简单。VMware 技术人员工作成员 [Unnati Mishra](https://in.linkedin.com/in/pingunnatimishra) 在她的演讲 “[Deploying with Confidence: Best Practices with Argo CD](https://cfp.cloud-native.rejekts.io/cloud-native-rejekts-eu-amsterdam-2023/talk/CVZTEA/)” 中解释了 GitOps 如何使“每个人都能轻松地参与你的项目。”“你可以在测试后部署应用程序。”

的确，GitOps 在 Kubernetes 上部署应用程序时非常强大， [Elotl](https://www.elotl.co/) 平台架构师和工程师 [Selvi Kadirvel](https://www.linkedin.com/in/selvi-kadirvel-29650812) 在她的 Rejekts 演讲“ [GitOps 管道中缺少的部分](https://cfp.cloud-native.rejekts.io/cloud-native-rejekts-eu-amsterdam-2023/talk/WZPKUH/)”中说道。组织可以进一步利用 GitOps 的“力量”通过使用多集群编排器， Kadirvel 说。她在演讲中说，这使组织可以：

* 将工作负载动态映射到集群。
* 跟踪当前集群及其资源可用性，以“做出更明智的业务决策”。
* 适用时跨集群队列迁移工作负载。

## Argo CD 和 Flux：这是 Flamingo

![](https://cdn.thenewstack.io/media/2023/04/ef1efdc3-flamingo1-1024x575.png)

两个工具 Argo CD 和 Flux 都各自有其用途和变化，这已经[被先前介绍](https://thenewstack.io/argo-cd-and-flux-are-cncf-grads-but-what-now/)过了。尽管如此，Argo CD（像 Flux 一样）利用 Git 中可用的历史记录，使得可以轻松地审计更改历史记录或在应用破坏性更改之前回滚到以前的工作版本。然而，Flux 和 Argo CD 的工作流程和扩展是不同的。

在 KubeCon + CloudNativeCon 之前不久，Weaveworks 推出了名为 [Flamingo](https://github.com/flux-subsystem-argo/flamingo) 的开源项目，它是将 Flux 集成到 Argo CD 中的子系统，从而提供了一个[“无缝”的 GitOps 体验](https://www.weave.works/blog/flamingo-expand-argo-cd-with-flux)，适用于 Kubernetes 集群。

“ Flux 具有像 Terraform 、 Pulumi 和 CloudFormation 集成等超级功能。 Flamingo 允许用户从 Argo 中访问这些 Flux 超级功能，”  Richardson 告诉The New Stack。“总体而言， Flux 是一个很棒的平台工程工具，有潜力成为一个通用的部署引擎。能够在 Flux 上使用开发工具像 Argo 是很有吸引力的。”
