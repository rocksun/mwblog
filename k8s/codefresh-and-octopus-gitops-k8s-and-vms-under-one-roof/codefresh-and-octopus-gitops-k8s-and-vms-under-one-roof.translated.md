# Codefresh 和 Octopus：GitOps、K8s 和 VM 齐聚一堂

![Codefresh 和 Octopus 的特色图片：GitOps、K8s 和 VM 齐聚一堂](https://cdn.thenewstack.io/media/2024/03/4460a067-serena-repice-lentini-igomdftkf-u-unsplash-1-1024x683.jpg)

最近的 Codefresh 和 [Octopus Deploy](https://octopus.com/?utm_content=inline-mention) [合并](https://octopus.com/blog/octopus-acquires-codefresh) 远不止是关于 [Kubernetes](https://thenewstack.io/kubernetes/)。是的，Codefresh 和 Octopus 合并后的实体将在统一云原生架构的部署方面大有作为，特别是对于大型企业而言。

但它还将解决一个大问题：在部署和提供服务时，除了 Kubernetes 之外，如何管理大型公司必须适应的传统架构。合并旨在为那些需要 [GitOps](https://thenewstack.io/how-enterprises-can-benefit-from-gitops/)（[Argo CD](https://thenewstack.io/why-argo-cd-is-the-lifeline-of-gitops/)) 和 Kubernetes 并且需要管理大量现有 VM 的组织解决一个重大问题。

[Torsten Volk](https://www.linkedin.com/in/torstenvolk)，[Enterprise Management Associates (EMA)](https://www.enterprisemanagement.com/) 的分析师告诉 The New Stack：“‘绿地假设’已经打破，并且仍然通过无法适应现实环境的复杂性来打破许多高级 DevOps 软件实施。”“绝大多数企业仍然拥有并且将在很多年内拥有混乱且异构的环境，这些环境在某种程度上需要成为 CI/CD 和 GitOps 的一部分。”

具有讽刺意味的是，这种对现有基础设施的担忧的想法是基础设施即服务提供商 [Puppet](https://thenewstack.io/5-myths-about-puppet/) 在 2016 年 Kubernetes 开始获得更多采用时提出的最初论点，并且组织开始对配置管理工具的相关性表示更多担忧，Volk 说。Puppet 当时的看法是，CI/CD 和 GitOps 应该独立于底层应用程序基础设施，并提供一条通往生产的一致路径，Volk 说。

他说：“事实证明 Puppet 是正确的。”

## 管理规模

当需要大规模管理 5,000 个目标和异构环境时，需要适应大多数 VM 和 Kubernetes 集群的组织是一个关键问题，Codefresh 和 Octopus 可以共同解决， [Dan Garfield](https://www.linkedin.com/in/dan-garfield/)，[Codefresh](https://thenewstack.io/codefresh-goes-open-core-with-argo-previews-open-gitops-1-0-release/) 的联合创始人兼首席开源官，一个建立在 Argo CD 上的企业项目，告诉 The New Stack。

虽然 Codefresh 可以从 GitOps 角度帮助解决这个问题，但“实际上 Octopus 也从传统的 CD 角度对此进行了研究”，Garfield 说。

“Codefresh 一直向所有这些大型企业和电信、游戏、媒体、国防、银行和医疗保健公司销售 Kubernetes，”Garfield 说。“但是，如果你看看他们的工作负载，他们都在做 Kubernetes，并且他们为他们运行的 10% 的工作负载做 Kubernetes——而他们运行的 90% 的工作负载不是这样，他们已经运行了 20 年。”

在 [The New Stack 上的一篇文章](https://thenewstack.io/how-far-can-you-go-with-argo/) 中，Octopus 的高级产品经理 [Nikita Dergilev](https://nz.linkedin.com/in/ndergilev) 分享了这一观点。在他看来，Argo CD 非常适合集群“引导，并且易于配置，第一次部署将花费一点时间，”Dergilev 说。

“然而，他认为在团队需要跨多个环境或集群（例如云区域）部署应用程序时使用 Argo CD 会出现问题，”他说。“痛苦来自需要管理许多 [git](https://thenewstack.io/git-at-15-how-git-changed-the-way-we-code/) 存储库、分支或文件夹，并使用内部脚本或手动编排促销。它很快就会变得一团糟。”

## 投资 Argo

并不是说 Octopus 没有成功的 Kubernetes 产品。然而，Octopus 看到越来越多的客户采用 Argo。

“对于 Octopus 来说，合并具有战略意义，因为他们真的想要我们拥有的技术和专业知识。因此，他们进来并说，‘我们想收购你们所有人，我们不会带来并解雇一群人，也不会剥离产品，”Garfield 说。

“Octopus 希望 Codefresh 继续发展我们正在做的事情，并继续投资 Argo，他们真的希望加速我们一直在做的事情。有趣的是，在 DevOps 的这个阶段，我们开始解决一些在某些方面已在传统部署（如 VM）中解决的问题，而 Octopus 实际上在这方面拥有很多专业知识。”
**在合并之前，Codefresh 也开发了不仅仅是 Kubernetes 支持。**

Garfield 说，使用 Argo CD 来支持传统基础设施的“公认路径”是通过跟踪 [etcd](https://etcd.io/) 中状态的控制器，例如 Crossplane。“我们绝对有兴趣改善这些体验。请注意，GitOps 不是 Kubernetes 标准，而是一种软件交付标准。这一切都归结为如何管理状态和期望状态。”

**事实上，Volk 说他“绝对相信”Argo 贡献者和部署到虚拟机的能力是 Octopus 进行收购的重要吸引力。**

“他们有充分的理由让 Argo 贡献者满意，因为他们是可持续地提供一个一致的 DevOps 管道和跨容器和虚拟机的 GitOps 方法的关键”，Volk 说。

## 构建他们想要的任何东西

**然而，Codefresh 也没有专注于虚拟机。**

“虽然有时人们可能会将我们用于虚拟机，但他们并没有真正为此而来，但对于 Octopus，他们已经为所有使用虚拟机的公司提供服务，尤其是那些使用传统应用程序和虚拟机的公司”，Garfield 说。“所以现在我们可以通过将所有内容构建到单一体验中为他们提供解决方案。我们将采用一种方法，统一软件交付，用于传统和云原生应用程序，我们认为这将非常非常强大。”

**在软件交付领域，组织通常可以通过使用 [Jira](https://thenewstack.io/open-source-jira-alternative-plane-lands/) 跟踪器、使用任何监控工具并寻求开发持续交付来构建“他们想要的任何东西”，Garfield 指出。**

他们寻求简单性、可靠性、可预测性和弹性。目标是尽可能地减少时间支出，解决流程中固有的痛点。

**从这个意义上说，提供了一种替代方案，可以将不同的工具和选项拼凑在一起并在内部开发流程。**

“你知道我们的竞争对手是谁吗？它是影子 DevOps：一堆脚本和手动部署的人员”，Garfield 说。“那是我们的市场。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)