# kro 的强大功能：Kubernetes 资源编排的巨大飞跃

![kro 的强大功能：Kubernetes 资源编排的巨大飞跃的特色图片](https://cdn.thenewstack.io/media/2025/03/f0c11558-kro-kubernetes-giant-leap-moon-1024x576.jpg)

[kro](https://kro.run)（我们像 Linux 命令行工具一样使用小写字母，发音像鸟类“crow”）扩展了 [Kubernetes 核心功能](https://roadmap.sh/kubernetes)，以简化相互依赖的 Kubernetes 资源的管理。[AWS](https://aws.amazon.com/?utm_content=inline+mention) 在 2024 年 11 月的 KubeCon North America 上开源了 kro。

仅仅两个月后，kro 将其字节打包并迁移到了一个供应商中立的家，[Google Cloud Platform](https://cloud.google.com/?utm_content=inline+mention) (GCP) 和 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure 加入了该项目。这种云原生协作使 kro 成为这三大云提供商[从一开始就走到一起](https://thenewstack.io/kubernetes-gets-a-new-resource-orchestrator-in-the-form-of-kro/)的第一个开源项目。

**为什么选择 kro？**

自 1.16 版本以来，Kubernetes 具有可扩展性，当时自定义资源定义 (CRD) 升级为全面可用 (GA)。虽然你可以编写任何自定义控制器（包括像订购披萨这样异想天开的控制器），但团队通常会为实际需求开发控制器：以特定顺序创建 Kubernetes 资源、在资源之间传递值以及执行逻辑操作。从头开始开发此类控制器可能既复杂又耗时，需要对编码和 Kubernetes 内部结构有深入的专业知识。

这就是 kro 的用武之地。kro 通过提供基于配置的框架来简化此过程，从而无需自定义代码。kro 没有让每个组织都构建自己的控制器，而是提供了一种标准化但灵活的方法，可以在整个社区中实现解决方案共享。其直观的设计由 Simple Schema、[通用表达式语言 (CEL](https://kubernetes.io/docs/reference/using-api/cel/)) 和强大的依赖项管理提供支持，使复杂的资源[编排变得易于访问](https://thenewstack.io/orchestrate-cloud-native-workloads-with-kro-and-kubernetes/)，只需简单的配置即可。

**哪些功能使 kro 易于使用？**

**Simple schema：**kro 提供了一种简单且人性化的方式来定义新的 CRD 规范。在底层，kro 使用 Simple Schema 定义自动生成 OpenAPIv3 模式并创建 Kubernetes CRD。这是一个重大改进，因为与 OpenAPIv3 模式相比，Simple Schema 更易于阅读和编写。

**基于 CEL 的表达式：**kro 结合了 CEL 来定义逻辑操作——Kubernetes 用于 Webhook 的相同表达式语言——因为它具有简单性和安全功能，例如[运行时成本预算](https://kubernetes.io/docs/reference/using-api/cel/#runtime-cost-budget)和[类型检查](https://kubernetes.io/docs/reference/using-api/cel/#type-checking)。借助 CEL，你可以清晰简洁地表达条件和依赖关系，并将值从一个资源传递到另一个资源。

**依赖项管理：**kro 根据指定的 CEL 表达式自动为编排的资源构建有向无环图 (DAG)。此 DAG 确定创建和删除资源的确切顺序。

这些功能使 kro 非常直观、易于适应，并且自然适合熟悉 [基础设施即代码 (IaC) 工具](https://thenewstack.io/introduction-to-infrastructure-as-code/)的人。

**kro 如何帮助管理云资源？**

kro 适用于 *任何* Kubernetes 资源，并且可以安装在 *任何* Kubernetes 集群上。kro *专门*与 Kubernetes API 交互，这意味着它不直接与任何外部 API 交互。相反，它管理和编排你的集群支持的任何资源。例如，如果安装了 Prometheus Operator，你可以使用 kro 将 Prometheus ServiceMonitor 与你的应用程序打包在一起。

同样，要配置云资源，你的集群必须包含与云提供商 API 通信的工具，例如 [AWS Controllers for Kubernetes (ACK)](https://aws-controllers-k8s.github.io/community/)、[GCP 的 Kubernetes Config Connector (KCC)](https://github.com/GoogleCloudPlatform/k8s-config-connector) 或 [Azure Service Operator (ASO)](https://github.com/Azure/azure-service-operator)。使用 **ResourceGroupDefinition (RGD)**（用于对相关资源进行分组的核心 kro 概念），你可以将应用程序、它们的云资源依赖项、所需的权限和其他必要的 Kubernetes 自定义资源打包到单个可部署单元中。

![kro 工作流程](https://cdn.thenewstack.io/media/2025/03/d69459b0-kro-architecture.png)

kro 工作流程

**kro 可以将 Kubernetes 变成一个集中式云平台**
组织经常难以管理多个分散的平台，每个团队都依赖多个不相关的工具来管理基础设施、应用程序和数据库等。将应用程序部署到 Kubernetes 的开发人员必须在多个界面之间切换——一个用于部署到 Kubernetes，另一个用于请求云基础设施资源、配置数据库和配置块存储。同时，平台团队（通常由网络、数据库和基础设施团队组成）各自维护自己的 IaC 管道。

这些管道缺乏一种标准的组合方式；一个管道的输出通常无法无缝集成到另一个管道中。更糟糕的是，它们不容易与用于将插件部署到 Kubernetes 的工具连接，从而造成进一步的低效率。数据平台团队构建他们单独的工具，通常具有重叠的功能，但很少集成。

Kubernetes 的采用已经证明了它作为集中式平台运营支柱的能力。kro 通过提供用于跨开发、平台和数据平台团队标准化资源管理的特定机制，扩展了 Kubernetes 的基础能力。通过其基于配置的自定义 API 定义方法，kro 使组织能够创建标准化的、可重用的组件，从而提供以下好处：

**提高开发人员速度：** 平台团队可以将应用程序及其云资源依赖项打包到一个可部署的单元中，嵌入组织最佳实践并确保隐式的中心治理。这种抽象降低了复杂性，使开发人员能够专注于交付功能，而不是排除基础设施管道的故障。
**改进集群管理：** kro 简化了新集群的创建，使您的业务能够扩展到新的区域、按需扩展容量以及为特定工作负载启动隔离的环境。通过将所有必需的 Kubernetes 资源打包到 RGD 中并构建 DAG，kro 确保正确的创建顺序。它还使平台运营商能够在整个集群中应用更改，从而可以轻松地更新组件以满足合规性要求。
**简化数据和 MLOps 基础设施管理：** 数据平台工程师可以将所有必需的组件打包到 kro RGD 中，包括云资源（如 GPU 节点、网络和存储），以及 Kubernetes 对象（如 StorageClasses、PersistentVolumeClaims、Services 和 Ingress）。这简化了部署过程，使数据科学家可以轻松地运行模型，而无需担心基础设施设置。例如，[此 LLM 示例](https://github.com/kro-run/kro/tree/main/examples/aws/llm) 演示了如何使用 kro 定义和编排所需的基础设施。
借助 kro，Kubernetes 可以成为平台层，从而使应用程序、基础设施和云资源的统一管理方式保持一致。

**结论**
kro 的发布标志着云原生计算的一个里程碑，它联合了 AWS、GCP 和 Azure，以解决 Kubernetes 资源管理问题。这种合作关系为跨云标准化奠定了基础，使整个生态系统受益。

加入这个变革之旅：在您的开发环境中探索 [kro](https://kro.run/)，与我们的 [GitHub](https://github.com/kro-run/kro) 社区联系，并通过 issue 或 pull request 做出贡献。无论是构建平台、应用程序还是管理数据和机器学习运营，您的贡献都可以塑造 Kubernetes 资源编排的未来，并推进可访问、标准化和高效的 [云原生开发](https://thenewstack.io/cloud-native/)。

*要了解有关 Kubernetes 和云原生生态系统的更多信息，请于 4 月 1 日至 4 日在伦敦参加 KubeCon + CloudNativeCon Europe。* 如果您要参加 KubeCon EU 2025，请在 AWS 展位 **S300 与我们会面，观看有关 kro 的演示。**
*Islam Mahgoub, Senior Solutions Architect, AWS, 也为本文做出了贡献。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。