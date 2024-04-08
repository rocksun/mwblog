## 数据流动性不足是云原生弊端的根源

![缺乏数据流动性是云原生弊端的根源的特色图片](https://cdn.thenewstack.io/media/2024/04/f3c382da-eilis-garvey-mskbr8vlnra-unsplash-1-1024x681.jpg)

巴黎 — 如今，很难找到不为 [云服务](https://thenewstack.io/cloud-services/) 价格上涨而苦恼的人。同样，许多人都在为如何尝试其他云提供商而苦恼，他们通过试用不同的选项来了解它们在做出重大供应商转换之前如何运作。其他人刚刚开始使用三大云提供商之一部署或转向云原生，而且许多人甚至不知道从哪里或如何开始。

一个大问题是如何保护我们的数据，特别是如何移动和访问数据，而不仅仅是停留在一个云提供商上，而这个云提供商又经常寻求涨价。我们如何根据需要按需扩展不同 [云提供商](https://thenewstack.io/how-to-evaluate-kubernetes-cloud-providers/) 和本地服务？在云原生领域，这种情况也会发生，不是如果，而是很可能在发生勒索软件攻击时发生。然后会发生什么？我们真的准备好了吗？而且，尤其是在今天，许多组织的云账单越来越高，这需要更严格的成本管理。

简单的 [虚拟化](https://thenewstack.io/virtualization-and-containers-better-together/) 工具无法提供必要的控制来管理跨各种云环境的数据和应用程序，也无法找到节省成本的方法。简单的存储快照和其他快捷方式不足以防止数据丢失和攻击。例如，移植 [虚拟机](https://thenewstack.io/containers-vs-virtual-machines-another-perspective/) 需要非常仔细的规划和远见。

[Veeam Software](https://www.veeam.com/backup-replication-virtual-physical-cloud.html) 的全球技术专家 [Michael Cade](https://uk.linkedin.com/in/michaelcade1) 在 [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 上告诉 The New Stack：“虽然可以轻松地将虚拟机从本地环境迁移到云环境，而无需精简，但这并不意味着这是正确的，并且在数据安全和保护方面不应该有更多考虑。”“迁移到云并提升和转移虚拟机是一回事，但这应该只是一个开始，否则组织会发现自己在云账单上花费巨资或遇到其他问题。目标必须是重构和重新架构为基于云原生的适当工作负载。”

“在云中使用基于云的工作负载非常容易，而无需过多担心成本和安全风险——你只需将它们提升并放入其中即可。”“但这不会奏效，因为你必须有一个计划，了解你首先要做什么。”

[Portworx](https://portworx.com/) 的产品管理和云高级总监 [Cody Hosterman](https://www.linkedin.com/in/cody-hosterman) 告诉 The New Stack，在不同云环境之间移动数据需要仔细考虑，以确保成功实施。“虽然数据传输的过程——‘提升和转移’迁移——看起来很简单，但在新云环境中取得成功会带来挑战。”Hosterman 说。

Hosterman 说，成功实现迁移涉及在管理成本和维护基本功能之间取得微妙的平衡。“避免潜在的陷阱需要对现有基础设施、应用程序和依赖项进行彻底评估，以确保与目标云环境兼容。”Hosterman 说，“例如，在新环境中配置资源是复制本地基础设施的关键步骤。”

[Matt Bator](https://www.linkedin.com/in/mattbator/) 说：“对于那些在‘今天的公共云供应商 XYZ’上运营其业务的组织来说，他们希望在未来某个时候拥有迁移到其他地方的自由，或者在对他们来说经济上最合理的地方运营。”[Veeam](https://www.kasten.io?utm_content=inline+mention) 的 [Kubernetes](https://thenewstack.io/kubernetes/) 原生解决方案负责人，在 [KubeCon + CloudNativeCon North America](https://events.linuxfoundation.org/archive/2023/kubecon-cloudnativecon-north-america/) 期间表示。

我们不妨说，备份对于在 Kubernetes 上维护安全、受保护且可访问的状态工作负载至关重要。同时，备份的效果取决于你恢复它们的能力，Bator 说。“这就是这里的关键，无论我们是就地恢复，还是出于灾难恢复的目的恢复到其他集群，或者我将其用作 Kubernetes 中的克隆例程的一部分，例如开发测试或用户验收测试。”Bator 说。

加密，
## 基于角色的访问控制、审计和不可变性

“基于角色的访问控制（[https://thenewstack.io/3-frameworks-for-role-based-access-control/](https://thenewstack.io/3-frameworks-for-role-based-access-control/)）、审计和不可变性是‘基本赌注’”，Bator 说。“这些功能确保备份数据保持可靠。我现在希望能够在不同云之间移动这些工作负载”，Bator 说。“对于无状态工作负载来说，这有点简单，对吧？容器化在工作负载的移动性方面为我们做了很多事情，但一旦我必须解决这些工作负载中的数据重力问题，并且我想定期执行此操作，也许我想启用混合云灾难恢复。

最终，将数据传输到那里很容易。使其成功并非易事。挑战在于在不影响管理和功能的情况下使迁移具有成本效益。如果没有周密的计划和执行，组织就有可能出现性能不佳和资源损失，这强调了在整个过程中进行战略决策的必要性。”

## 数据移动解决方案

“一个适当的数据移动解决方案应该能够直接与 Kubernetes 发行版交互”，Bator 说。“我不能只对工作节点进行快照，并认为分布在多个工作节点上的应用程序可以‘神奇地’恢复。因此，我需要从所有应用程序元数据开始”，他说。“我需要能够与我的底层存储基础设施集成，以便能够编排我数据的卷快照。我需要能够以一种方式打包所有这些，以便在需要时将其从集群中取出。”

确保应用程序一致性的机制也很关键。不仅是数据库，而且跨不同云和本地环境的所有工作负载都必须可以通过单个 Kubernetes API 访问，以管理和提取所有这些信息。在 Kasten 的情况下，命名空间与集群上其他应用程序一起运行，这要归功于自定义资源 API。通过蓝图等功能，可以与不同堆栈的其他组件集成，包括代码策略或集成到自动化工具中，例如 [GitOps](https://thenewstack.io/what-is-gitops-and-why-it-might-be-the-next-big-thing-for-devops/) 管道。

“我希望从我的自动化数据保护中完全消除摩擦，并确保在我每次在持续交付或持续部署管道将新代码推送到生产环境之前，对我的应用程序进行快照、对我的应用程序进行备份”，Bator 说。“因此，这些再次是成为 Kubernetes 原生的部分重大优势，而不是我将这个很酷的附加组件添加到我的 20 年备份中，它碰巧还可以与 Kubernetes 通信。”

## 勒索软件很可怕

哪种堕落邪恶的人故意策划勒索软件攻击，导致医院、学校和日托中心死亡和伤害——公共服务设施除外？此类攻击在各种类型的组织中持续发生，频率惊人。Kubernetes 当然也不例外，并且在攻击发生时做好真正恢复的准备至关重要，而且是可以做到的。

“勒索软件恶棍仍然存在于 Kubernetes 世界中。我们对任何这些攻击都无能为力，无论如何，我都希望能够利用混合多云环境”，Bator 说。“我需要能够依赖这些数据，因为这是我抵御勒索软件恶棍的最后一道防线。”

## 开始

如何开始，谁的工作是开始？好吧，这应该是开发人员、运营人员和 CTO 之间的团队合作。正如我所描述的，每个人都需要拥有或成为这种数据移动保险的一部分。这不仅仅是数据存储和应用程序，尤其是对于无状态应用程序及其权重。一旦部署，无论是在单个云提供商网络上还是在混合结构中跨不同的云原生环境中，确保数据移动、存储解决方案和灾难恢复（例如在勒索软件攻击或无意中删除数据的情况下）都至关重要。无缝工作。这不是关于单独的解决方案；它应该是一个单一的解决方案。

许多人仍然“有点困惑，不知道谁拥有 Kubernetes 的备份。是开发人员吗？是平台工程团队还是 DevOps 团队？是传统备份管理员吗？” Bator 说。“我会说，这可能更像是一个‘与’命题，而不是一个‘或’命题。这是一个‘众人拾柴火焰高’的方法。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、采访、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)