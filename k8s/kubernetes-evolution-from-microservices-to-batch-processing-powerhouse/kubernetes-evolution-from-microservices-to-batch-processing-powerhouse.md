# Kubernetes演进：从微服务到批处理的强大引擎

翻译自 [Kubernetes Evolution: From Microservices to Batch Processing Powerhouse](https://thenewstack.io/kubernetes-evolution-from-microservices-to-batch-processing-powerhouse/) 。

在早期，Kubernetes 主要专注于为基于微服务的工作负载构建功能。近年来，Kubernetes 社区已经扩展到对高性能计算工作负载的批处理支持。

![](https://cdn.thenewstack.io/media/2023/04/8170d197-dna-869109_1280-1024x768.jpg)
*图片来自 Pixabay 的 Pete Linforth。*

这篇文章是 4 月 18 日至 21 日在阿姆斯特丹举行的 KubeCon + CloudNativeCon Europe 2023 预览系列文章之一。[加入我们](https://github.com/kubernetes/community/tree/master/wg-batch)，了解更多关于云原生应用程序和开源软件的变革性质。

自 2014 年问世以来，Kubernetes 已经走过了漫长的道路。

最初专注于支持微服务工作负载的 Kubernetes 已经发展成为一个构建批处理平台的强大而灵活的工具。这种转变是由对机器学习（ML）训练能力日益增长的需求、高性能计算（HPC）系统向云端转移以及行业朝着更松散耦合的数学模型演进所驱动的。

[PGS 最近使用 Kubernetes 构建了一个计算平台，该平台相当于全球排名第七的超级计算机](https://www.pgs.com/company/newsroom/news/industry-insights--hpc-in-the-cloud/)，拥有 120 万个 vCPU ，在云端和 Spot VM 上运行。这是这一趋势的一个重要亮点。

在早期，Kubernetes 主要专注于为基于微服务的工作负载构建功能。其强大的容器编排能力使其成为管理此类应用程序复杂性的理想选择。

然而，批处理工作负载用户通常更喜欢依赖于其他框架，如 Slurm 、 Mesos 、 HTCondor 或 Nomad 。这些框架为批处理任务提供了必要的功能和可伸缩性，但它们缺乏 Kubernetes 所提供的充满活力的生态系统、社区支持和集成能力。

近年来，Kubernetes 社区已经认识到对批处理支持的需求不断增长，并在这个方向上进行了大量投资。其中一项投资是 Batch Working Group 的成立，该工作组已采取多项举措来增强 Kubernetes 的批处理能力。

批处理工作组对作业 API 进行了多项改进，使其更加强大和灵活，以支持更广泛的批处理工作负载。重新设计的 API 允许用户轻松管理批处理作业，并提供可伸缩性、性能和可靠性增强。

Kueue（https://kueue.sigs.k8s.io/） 是由 Batch Working Group 开发的新型作业调度程序，专为 Kubernetes 批处理工作负载而设计。它提供了高级功能，如作业优先级、回填、资源风格编排和抢占，确保批处理作业的高效和及时执行，同时保持您的资源使用效率最大化。

团队现在正在努力构建与各种框架（如 Kubeflow 、 Ray 、 Spark 和 Airflow ）的集成。这些集成允许用户利用 Kubernetes 的强大和灵活性，同时利用这些框架的专业能力，从而创建一个无缝高效的批处理体验。

团队还在寻求提供其他能力，包括自动缩放中的作业级别配置 API 、调度程序插件、节点级运行时改进等。

随着 Kubernetes 继续投资批处理支持，对于以前依赖其他框架的用户来说，它成为一个越来越有竞争力的选择。 Kubernetes 带来了许多优势，包括：

* **广泛的多租户功能**：Kubernetes 提供强大的安全性、审计和成本分配功能，使其成为管理多个租户和异构工作负载的组织的理想选择。
* **丰富的生态系统和社区**：Kubernetes 拥有一个蓬勃发展的开源社区，提供丰富的工具和资源来帮助用户优化他们的批处理任务。
* **受管的托管服务**：Kubernetes 在所有主要云提供商上都可以作为托管服务使用。这提供了与其计算堆栈的紧密集成，使用户能够利用独特的功能，并简化了难以使用的稀缺资源（如 Spot VM 或加速器）的编排。使用这些服务将导致更快的开发周期、更大的弹性和更低的总拥有成本。
* **计算编排标准化和可移植性**：企业可以选择单个 API 层来包装他们的计算资源，以混合他们的批处理和服务工作负载。他们可以使用 Kubernetes 减少对单一供应商的锁定，并获得充分利用当前云市场所提供的最佳资源的灵活性。

通常，用户使用 Kubernetes 的过渡还涉及到他们的批处理工作负载的容器化。容器本身已经彻底改变了软件开发过程，对于计算工作负载，它们极大地加快了发布周期，从而加快了创新速度。

容器将应用程序及其依赖项封装在一个独立的单元中，该单元可以跨不同的平台和环境一致地运行。他们消除了“它在我的机器上工作”的问题。它们支持快速原型制作和更快的迭代周期。如果与云托管相结合，它可以提供敏捷性，帮助 HPC 和面向 ML 的公司更快地进行创新。

Kubernetes 社区仍然需要解决许多挑战，包括需要对每个主机节点上的运行时进行更高级的控制，以及需要更高级的 Job API 支持。 HPC 用户习惯于对运行时有更多的控制。

在本地使用 Kubernetes 构建大规模平台仍需要相当多的技能和专业知识。目前，批处理生态系统存在一定程度的分裂，不同框架以不同方式重新实现常见概念（如作业、作业组、作业排队）。未来随着每个 Kubernetes 版本的发布，我们将看到这些问题得到解决。

Kubernetes 从一个以微服务为中心的平台演变为一个强大的批处理工具，展示了 Kubernetes 社区的适应性和弹性。通过满足对 ML 训练功能不断增长的需求，将 HPC 迁移到云端，Kubernetes 已成为批处理工作负载越来越有吸引力的选择。

Kubernetes 广泛的多租户功能、丰富的生态系统以及在主要云服务提供商上提供的托管服务，使其成为寻求优化批处理任务并利用云计算能力的组织的理想选择。如果您想加入 [Batch Working Group](https://github.com/kubernetes/community/tree/master/wg-batch) 并帮助贡献 Kubernetes ，则可以在[此处](https://github.com/kubernetes/community/blob/master/wg-batch/README.md)找到所有详细信息。我们定期召开会议，有一个 Slack 频道和一个电子邮件组可供加入。