
<!--
title: Okta 如何通过 Argo CD 将 Kubernetes 集群从12扩展到1000
cover: https://cdn.thenewstack.io/media/2025/12/6c57c0f4-alex-shuper-knywdsncxfm-unsplash-1.jpg
summary: Okta Auth0因支持问题转向Argo CD，历时五年，成功将集群从几十个扩展到上千个。通过自定义工具和工作流编排克服了部署和同步挑战。
-->

Okta Auth0因支持问题转向Argo CD，历时五年，成功将集群从几十个扩展到上千个。通过自定义工具和工作流编排克服了部署和同步挑战。

> 译自：[How Okta Scaled From 12 to 1,000 Kubernetes Clusters With Argo CD](https://thenewstack.io/how-okta-scaled-from-12-to-1000-kubernetes-clusters-with-argo-cd/)
> 
> 作者：B. Cameron Gain

亚特兰大——可以说，[Okta 的 Auth0](https://thenewstack.io/with-auth0-purchase-okta-will-boost-access-apis-for-developers/) 私有云平台客户并没有得到他们真正想要的东西。[Okta](https://thenewstack.io/okta-wants-to-secure-your-ai-agents-too/) 的支持充其量也只是问题重重，特别是对于那些大规模的客户。

这促使他们决定在 [GitOps](https://thenewstack.io/4-core-principles-of-gitops/) 的开源领域，特别是 [CNCF](https://cncf.io/?utm_content=inline+mention) 毕业项目 [Argo CD](https://thenewstack.io/survey-argocd-leaves-flux-and-other-gitops-platforms-behind/)（以前称为 Argo Workflows）上押下重注。这并非简单的迁移；在如此广泛的运营范围内实施它需要五年多的时间。在北美的 [KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 期间，Okta 工程师 Jérémy Albuixech 和 Kahou Lei 在他们的演讲 [“从几十个到上千个集群：Argo 如何在我们扩展时保持同步。”](https://kccncna2025.sched.com/event/27FcE/one-dozen-to-one-thousand-clusters-how-argo-kept-up-as-we-scaled-jeremy-albuixech-kahou-lei-okta) 中详细阐述了他们经历的考验和磨难。

最终结果是：“我们可以肯定地说，结果显示他们现在可以扩展到一千多个集群，而几年前只有大约几十个。” Albuixech 在演讲中说道。

## 鸣谢

在深入探讨 Argo CD 以及这一切是如何发生之前，有必要先说明 Argo CD 是什么以及 GitOps 包含了什么。Argo CD 不仅仅是一个用于扩展 [Kubernetes](https://thenewstack.io/kubernetes/) 集群的软件工具或平台，它也是一个广受欢迎且社区支持日益增长的项目。同样，不能不提及平行存在的 CNCF 毕业项目 [Flux](https://thenewstack.io/why-flux-isnt-dying-after-weaveworks/)。

像 Argo CD 和 Flux 这样的 GitOps 运维工具将 Git 作为期望状态的不可变事实来源进行监控，并将该期望状态应用于实际状态。Git 的不可变结构还能在运行时发现漏洞时（这些漏洞总是会出现）自动化应用程序和集群中代码的更改。同样，如果有人直接修改运行时（例如在安全漏洞期间发生的情况），GitOps 运维工具将自动检测这些更改，并用 Git 中定义的期望状态覆盖它们。

Flux 和 Argo CD 持续监控 Git 仓库中定义的应用程序定义和配置，并将这些配置的指定状态与它们在集群上的实时状态进行比较。Argo CD 会报告任何偏离其指定状态的配置。这些报告允许管理员自动或手动将配置重新同步到定义的状态。Git 始终作为单一事实来源。

## 开源的真理

时间倒回到五年多前。Albuixech 和 Lei 描述了 Okta 的 Auth0 平台在其最初迭代时，主要是为那些希望将基础设施和配置存储在私有云账户中的客户提供服务托管。它针对的是一小部分客户，因此在设计时并未将大规模和自动化作为优先事项。它有 [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) 配置和基础设施。更新由运维人员手动完成，访问权限不如现在安全，并且它依赖于早期的云基础设施——基本上是运行在虚拟机（VM）中的代码。

“随着需求增加，我们需要一个新的平台设计。” Albuixech 说。“经过研究和概念验证，我们最终采用了大量使用 Argo 项目的云原生架构。” Albuixech 表示，Argo CD 负责服务配置，Argo Workflows 负责部署，Terraform（带有一个自定义提供商）负责基础设施即代码 (IaC)，所有这些都由控制平面服务编排，以便我们可以管理所有客户环境。

## 艰辛工作

开源项目的一个优点是社区用户会随着新闻和项目本身的增长不断提出修改意见。话虽如此，正如 Albuixech 和 Lei 在他们的演讲中详细阐述的那样，开源 Argo CD 仍然面临着一些“显著”挑战。

其中包括他们的部署管道无法使用自动同步功能，因为它无法处理 Terraform 依赖项或遵守客户特定的部署窗口，这需要使用 Argo Workflows 和控制平面进行自定义“自动同步”。

正如 Lei 所描述的，Argo CD 的自动同步确保 Kubernetes 集群中的状态始终与 Git 匹配。“然而，由于我们的发布模型，我们无法在部署管道中使用自动同步。每个发布候选版本都是一个捆绑包，包含服务镜像版本、[Terraform](https://thenewstack.io/terraform-isnt-dead/) 代码、Kubernetes 清单、插件和自定义逻辑。” Lei 说道。

Lei 表示：“自研的 application-X 插件最初导致刷新操作需要几分钟，因为 customize 会为每个插件生成一个子进程，这需要一个分叉的二进制文件。为每个客户运行不同的插件版本需要 Docker-in-Docker 方法，这进一步增加了运维复杂性。”

Lei 表示，一个发布清单对应一个 Argo 应用程序，一个 Argo 应用程序代表一个完整的客户集群。由于 Terraform 生成的基础设施会影响服务所需的配置和秘密，因此 Terraform 必须在 Argo CD 同步之前运行。自动同步无法适应这种依赖关系，也无法遵守客户特定的部署窗口。权宜之计是：“因此，我们使用 Argo Workflows 加上控制平面实现了我们自己的‘自动同步’。” Lei 说道。

其他挑战包括常见的瞬态部署失败，包括崩溃循环、同步冲突、插件故障和卡住的同步。Albuixech 和 Lei 描述说，为了管理这些问题，团队构建了一个命令行界面 (CLI) 封装器，用于对故障进行分类、强制超时和控制重试。“在大规模场景下，应用程序控制器经常在负载下崩溃，UI 变得非常慢，应用程序状态可能具有误导性，这需要控制器扩展、基础设施改进、CLI 工具和忽略资源设置。” Lei 说道。上游的 bug，例如应用程序控制器中的竞态条件和未跟踪资源导致的性能问题，必须在内部解决。

包含 50 个或更多步骤的工作流，由多个团队维护，存在冲突风险，需要动态子工作流管理。用于 Kubernetes 升级、[Postgres](https://thenewstack.io/how-distributed-postgres-solves-clouds-high-availability-problem/) 蓝绿更新、负载测试、混沌测试和 CI 验证的大型工作流可能会使 Argo UI 不堪重负，促使采用诸如启动带标签的子工作流之类的权宜之计。一些 UI 限制迫使采用不同寻常的解决方案，例如一个用于移除“终止”按钮的 Chrome 插件，它绕过了退出钩子并破坏了自动化。Lei 表示，尽管面临这些挑战，该平台仍通过广泛的自定义工具、工作流编排和精心细致的运维管理持续扩展。

## 确实令人惊叹

![](https://cdn.thenewstack.io/media/2025/12/949975ff-img_7790-2.heic)鉴于这个非常成功的开源项目的拉取请求和 GitHub 上的反馈，他们面临的这些问题非常普遍，并且协作修复方案正在提供。同样值得注意的是，这对于一个主要的开源项目在其实现方面来说是巨大的成功。这不仅仅是一个非常酷的 GitOps 平台技术，而且随着它的发展，Argo CD 继续展示其对 Kubernetes 的价值，特别是在大规模 GitOps 中。当然，也不要忘记 Flux，它也得到了经过验证的采用。

Albuixech 和 Lei 显然不是营销人员，但 Lei 这样描述成功：“尽管面临这些挑战，该平台仍通过广泛的自定义工具、工作流编排和精心细致的运维管理持续扩展。”