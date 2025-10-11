
<!--
title: Kubernetes 融合现有虚机：路径探索与实践
cover: https://cdn.thenewstack.io/media/2025/10/b2cddd08-fall.jpeg
summary: Kubernetes是新应用首选，但虚拟机仍运行现有应用。为保持敏捷和效率，企业需实现Kubernetes与虚拟机共存。建议在虚拟机中运行Kubernetes，以平稳过渡，利用现有虚拟机技能。
-->

Kubernetes是新应用首选，但虚拟机仍运行现有应用。为保持敏捷和效率，企业需实现Kubernetes与虚拟机共存。建议在虚拟机中运行Kubernetes，以平稳过渡，利用现有虚拟机技能。

> 译自：[Finding the Path for Integrating Kubernetes With Existing VMs](https://thenewstack.io/finding-the-path-for-integrating-kubernetes-with-existing-vms/)
> 
> 作者：Dan Ciruli

Kubernetes 已成为部署新的企业应用（包括未来几年预计将上线的 AI 应用浪潮）的首选平台。但在可预见的未来，企业仍将在很大程度上继续在虚拟机架构上运行现有应用。找到 Kubernetes 和虚拟机共存的方法对于企业保持敏捷性和效率至关重要。

在短短 11 年间，[Kubernetes](https://thenewstack.io/kubernetes/) 已从一个开创性的、近乎实验性的[容器](https://thenewstack.io/containers/)编排平台，发展成为企业 IT 中新应用的主导部署方法。根据[云原生计算基金会 2024 年调查](https://www.cncf.io/blog/2024/06/06/the-voice-of-kubernetes-experts-report-2024-the-data-trends-driving-the-future-of-the-enterprise/)，如今五分之四的组织使用 Kubernetes。在这些自称为 Kubernetes 采用者的组织中，大约 40% 的新应用正在 Kubernetes 下运行，这一数字预计将在三年内增加到 80%。

这在企业 IT 领域中几乎是无处不在的。但无论新技术出现得多么迅速，它们仍然必须与旧技术争夺市场份额和预算。对于 Kubernetes 来说，最大的替代方案仍然是虚拟机 (VM)。

虚拟机在 21 世纪初出现，作为一种将操作系统与底层硬件分离的方式，使工作负载能够独立于硬件移动和扩展。尽管虚拟机在服务器层面为企业带来了一定的运营优势，但它们并未从根本上改变应用的开发和交付方式。开发者仍然使用三层或客户端-服务器架构开发软件，这反过来又常常需要大量的体力劳动进行测试和部署。

这就是容器化发挥作用的地方。容器化使开发者能够一次性构建一个标准环境，测试其兼容性，冻结代码更改，然后将其克隆（或容器化）以供下游重复使用，而不是单独构建每个企业环境。

这些“容器”随后可以以标准化方式部署，并在管理系统内运行。这减少了开发者艰巨的集成和测试工作，也简化了扩展应用以支持不断增长的工作负载的过程。这些优势使得 Google、Twitter 和 Airbnb 等早期 Kubernetes 采用者能够比使用虚拟机更快地创新、扩展更远。

在 [Google 开源 Kubernetes](https://thenewstack.io/kubecon-europe-how-google-will-evolve-kubernetes-in-ai-era/) 后，世界各地的开发者都采用了它。 [Kubernetes 允许开发者部署](https://thenewstack.io/a-look-at-kubernetes-deployment/)自己的工作，而不是受限于管理员向生产集群部署软件的能力，从而大大减少了他们对管理员的依赖，并使他们能够更快速、高效地工作。Kubernetes 帮助催生了已成为主导范式的云原生计算架构。

尽管云原生计算如今引领潮流，但它有时与包括虚拟机在内的现有范式存在冲突。在过去的 20 年里，企业已投入数千亿美元在虚拟机中构建和部署企业应用，他们不倾向于将其拆除并替换为更现代的云原生计算架构。

新的开发通常以云原生方式进行，但大多数现有应用仍在虚拟机中运行。因此，在可预见的未来，虚拟机和容器将需要共存。然而，这说起来容易做起来难。因此，IT 决策者面临的挑战是规划一条道路，使他们能够同时处理虚拟化和容器化应用，而不会产生额外的高昂成本。

找到 Kubernetes 和虚拟机架构之间的共同点对于企业效率至关重要。致力于同时使用 Kubernetes 和虚拟机环境的公司必须弄清楚如何将这些环境一起运行和管理。仅仅采用 Kubernetes 和云原生计算是不够的；它必须与仍在虚拟机上运行的企业应用组合的其余部分集成。

好消息是 Kubernetes 和虚拟机可以共存。首先，通过正确的平台选择，Kubernetes 和虚拟机实际上都可以运行在相同的行业标准 x86 机器上。尽管许多企业在独立的物理机上运行虚拟机和 Kubernetes，但在同一硬件上一起运行它们带来了多项好处，包括更好的硬件利用率、改进的可管理性、简化的集成、增强的安全性以及更简单的故障排除。

将[虚拟化和容器化工作负载结合在同一硬件上](https://thenewstack.io/state-of-virtualization-report-reflects-shifting-strategies/)主要有两种方式：要么在虚拟机中运行 Kubernetes，要么使用 Kubevirt 等技术在裸机上与 Kubernetes 一起运行虚拟机。

尽管运行 Kubevirt 来调度基于虚拟机的工作负载可能看起来像是在迈向未来，但它也存在一些缺点。尽管有些企业级虚拟机管理程序已经发展了十多年的生态系统、用户群和功能集，但 Kubevirt 尚未获得广泛的主流采用。它也加剧了 [Kubernetes 技能差距](https://thenewstack.io/overcoming-the-kubernetes-skills-gap-in-edge-computing/)。许多公司表示，他们很难找到足够的熟练人员来运行其云原生工作负载；如果运行任何工作负载都需要 Kubernetes 专业知识，那将使这个问题变得更加严重。

寻求共存策略的企业可能更倾向于逐步过渡，允许拥有虚拟机技能的 IT 专业人员继续管理这些环境，同时培养其内部的 Kubernetes 技能。在虚拟机中运行 Kubernetes 使公司能够为虚拟机拥有企业级解决方案，并为其容器拥有纯粹的云原生解决方案。它还提供了对所有 Kubernetes 功能的访问，包括动态大小调整和临时集群，这些概念在裸机上运行 Kubernetes 时意义不大。

Kubernetes 明确代表了企业 IT 环境的未来之路。它是一种更高层次的整体系统虚拟化，解决了早期虚拟机系统中的许多痛点。随着公司构建其 Kubernetes 环境，为企业做出正确的选择可能意味着在 Kubernetes-VM 过渡中被挤压，或者从现有集群中榨取更多效用之间的区别。