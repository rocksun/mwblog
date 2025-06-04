# 开源 KubeVirt：使用 Kubernetes 进行 VM 管理仍在进行中

![Featued image for: Open Source KubeVirt: VM Management With Kubernetes Is a Work in Progress](https://cdn.thenewstack.io/media/2025/05/83e0f057-ibrahim-yusuf-vwjtyrfe_rw-unsplash-1024x683.jpg)

[Ibrahim Yusuf](https://unsplash.com/@its_ibrahim?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/a-man-sitting-in-front-of-a-laptop-computer-vWJtYRfE_rw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).

KubeVirt 是一个新兴且充满活力的开源项目，它通过将虚拟机管理层集成到 Kubernetes 中，使虚拟机能够与容器并行运行。KubeVirt 专为拥有虚拟机工作负载并希望采用 Kubernetes 控制面的组织而设计，它作为一个平台，允许 VM 和容器并排运行。

在[容器和 Kubernetes 上运行工作负载的组织可能会考虑使用 KubeVirt 来集成](https://thenewstack.io/the-impact-of-containerization-on-apm-strategies/)虚拟机与他们的 Kubernetes 和容器基础设施。在 Red Hat、NVIDIA 和其他科技公司的支持下，CNCF 项目与日益增长的共识保持一致，即容器不会取代 VM——许多组织已经通过惨痛的教训认识到这一点。其理念是容器和 VM 可以而且应该并排运行。但尽管这个概念是可靠的，但对于需要支持关键大规模 VM 工作负载的组织来说，仍然存在一些需要注意的地方。

借助 KubeVirt，VM 在 Kubernetes 集群内部运行，特别是 Pod 内部。这种结构适用于特定的用例，但到目前为止，它的局限性使其不太适合将 VM 大规模生产地扩展到 Kubernetes 上。采用它需要对现有的 IT 基础设施进行重大更改，包括存储、计算和网络。即使成功实施了 KubeVirt，与已建立的 VM 管理产品相比，它的功能也受到很大限制，特别是那些可以扩展到 Kubernetes 的产品，以便在单个平台上管理在容器或 VM 上运行的应用程序。

## 想要的功能

KubeVirt Kubernetes 虚拟化 API 和运行时旨在定义和管理虚拟机。但是，还需要另一个工具提供的其他功能：Libvirt 用于将 VM 与 KVM 虚拟机监控程序集成，以便可以在 Kubernetes Pod 中启动和管理它们。根据该项目的[文档](https://github.com/kubevirt/kubevirt?tab=readme-ov-file)，KubeVirt 在很大程度上仅限于声明性用法，例如：

- 创建预定义的 VM。
- 在 Kubernetes 集群上调度 VM。
- 启动 VM。
- 停止 VM。
- 删除 VM。

KubeVirt 提供的虚拟机监控程序管理功能非常基础，并且使用受限；对于集成有限数量的 VM 而言，相对缺乏功能和高级操作能力（例如存储管理集成）与 VM 管理中期望的高级功能不符。由于基于 VM 的基础设施已经使用了几十年，因此 VM 受益于广泛的行业理解和该领域管理的持续创新。理想情况下，VM 的高级功能应与容器在通用基础设施中可用。

根据 Gartner 的说法，KubeVirt 的用例包括：

- 基础设施配置，用于创建和销毁短期的非生产虚拟环境（包括开发和实验室环境）。
- 除此之外，KubeVirt 还可用于在用于托管 Kubernetes 集群时配置 VM。

根据 Gartner 副总裁兼分析师 [Michael Warrilow](https://www.gartner.com/en/experts/michael-warrilow) 的说法，“大多数企业可能会发现，至少在 2028 年之前，对现有生产虚拟工作负载进行重新虚拟化在技术上最具挑战性、风险最高且难以证明其合理性。”

与存储系统的集成不是 KubeVirt 的默认实现功能。如果没有连接到 KubeVirt 或成为 KubeVirt 标准的标准化存储元素，不同的存储供应商可能不容易与它一起工作或提供支持。

KubeVirt 是为执行 Kubernetes 的 VM 创建的，这意味着使用 KubeVirt 的组织仍然依赖于支持容器存储接口 (CSI) 的存储供应商。根据 Gartner 的数据，截至 2025 年 1 月，在列出的 CSI 驱动程序中：

- 54% 不支持快照。
- 49% 不支持对多个 Pod 进行读/写。
- 57% 不支持扩展。
这将扰乱许多使用上述常见功能的存储环境，如快照、扩展。这与虚拟环境的传统存储解决方案形成鲜明对比，无论这些解决方案是基于外部存储还是软件定义存储。经过验证的、事实上的 API 使得存储供应商能够始终如一地为虚拟工作负载卸载存储功能。示例包括克隆、迁移、配置、回收和访问控制。

虽然组织可以管理现有的虚拟机，但管理能力非常有限，仅限于基本的 hypervisor 管理。虚拟机继续存在于基础设施中，但 KubeVirt 缺乏企业级虚拟化平台提供的许多高级操作和生命周期管理功能。

## 以 Kubernetes 为中心

KubeVirt 专为 Kubernetes 环境而构建，但企业采用的要求仍然很高。该平台基于所有工作负载最终都将迁移到 Kubernetes 的假设。然而，这种转变很少是立即的；即使是 Kubernetes 版本之间的升级也可能需要几个月甚至几年的时间。因此，KubeVirt 最适合那些致力于完全容器化其工作负载并采用 Kubernetes 作为唯一控制平面的组织。一旦实施，功能的缺乏将使虚拟机管理更像是管理牲畜而不是宠物。

与传统的虚拟机平台相比，Kubernetes 引入了更多的操作复杂性。这种架构转变带来了巨大的摩擦，因为它要求组织放弃已建立的虚拟机管理实践，转而采用以 Kubernetes 为中心的方法。虽然 Kubernetes 提供了强大的编排能力，但它也需要一套全新的技能。虚拟基础设施管理员必须接受再培训，组织必须重新培训整个团队，才能通过新的控制平面管理现有的虚拟机工作负载。

对于具有大规模虚拟机部署的环境（范围从 1,000 到 100,000 台虚拟机），这种转变绝非易事。许多这些环境严重依赖于自定义脚本、高级功能和自动化，这使得迁移在技术上和操作上都具有挑战性。

Gartner 的观察结果与此观点一致，Gartner 指出，Red Hat 等供应商（及其 OpenShift 平台）已将 KubeVirt 作为进入虚拟机管理市场的战略入口。开发成熟的企业级虚拟机管理平台通常需要数年甚至数十年的持续工程和运营改进，无论解决方案是开源的还是专有的。

组织继续依赖虚拟机，因为它们提供操作简单性、经过验证的效率和更低的总拥有成本 (TCO)。此外，现有的人才库更适合虚拟机管理；在传统的虚拟机环境中招聘熟练的专业人员仍然比在容器化或 Kubernetes 原生基础设施中寻找同等专业知识容易得多。

当今的虚拟机操作由成熟的编排工具、高级功能以及强化的安全和合规性框架提供支持。将虚拟机引入 Kubernetes 原生环境将要求组织彻底改革其工具，并大幅度地重新培训技术团队——这是一项需要付出巨大成本和运营风险的努力。因此，在 Kubernetes 集群中运行虚拟机的理由仍然仅限于高度特定的用例，不建议企业普遍采用。

Warrilow 写道：“这是技能方面的一个明显差距，需要克服才能成功采用 KubeVirt，无论是否用于生产。许多现有的 I&O 人员将缺乏现代云原生工具和方法的熟练程度和经验。” “实施 DevOps 需要在技术和培训方面进行大量投资，这已被证明是广泛采用的障碍……KubeVirt 将迫使这种改变。”

## 尚不成熟的承诺

KubeVirt 在 2019 年作为沙箱项目进入 CNCF，并在 2022 年提升到孵化成熟度级别后，仍处于孵化阶段。虽然这代表着有意义的进展，但也表明该项目尚未达到 CNCF 毕业所需的成熟度水平。根据 CNCF 的说法，要实现毕业状态，还需要在开发、稳定性、采用和治理成熟度方面进行大量的额外工作。对于 CNCF 最大的项目 Kubernetes 和 OpenTelemetry 来说，这些步骤已经花费了十多年的时间才实现。
对于受监管或任务关键型行业的组织（如银行、联邦、州和地方政府、公用事业或零售业）而言，采用这种新兴技术的风险相当大。与 NVIDIA、Google 或 Meta 等拥有内部工程能力来定制和支持开源工具的技术领导者不同，大多数企业没有能力独立管理这种程度的技术复杂性。

## 结论

我们建议拥有现有 VM 基础设施的组织采用具有成熟的 VM 管理能力的平台。许多组织已经为这些成熟的平台建立了完善的安全和合规框架。将 VM 引入 Kubernetes 原生环境将需要对工具进行重大更改，并对运营团队进行广泛的技能再培训——考虑到 VM 平台的成熟度和效率，以及 KubeVirt 目前提供的 VM 功能的相对有限的规模，这些努力可能是不合理的。

虽然很少有拥有大量资源的组织能够依赖这样一个年轻的项目（KubeVirt 的 1.0 版本于 2023 年 7 月发布）将 VM 与 Kubernetes 和容器基础设施集成，但建议在可预见的未来，其使用仍然仅限于管理少量 VM——考虑为一个沙箱项目管理一百个 VM，而不是为支持关键运营管理成千上万个 VM。

Gartner 估计，到 2028 年，技术和运营限制将使 KubeVirt 的采用限制在企业环境中不到 10% 的本地生产虚拟工作负载。

Gartner 分析师 Michael Warrilow 在“KubeVirt Will Require Radical Changes to Traditional I&O”中写道：“出于错误的原因采用 KubeVirt 将会产生重大且可避免的技术风险。”“但是，仅仅将其用作重新虚拟化生产工作负载的手段不太可能产生足够的回报或提高可用性、可靠性或安全性。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，即可观看我们所有的播客、访谈、演示等。