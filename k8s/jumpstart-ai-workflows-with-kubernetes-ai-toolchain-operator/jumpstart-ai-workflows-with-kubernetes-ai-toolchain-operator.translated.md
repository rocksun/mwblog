# 使用 Kubernetes AI 工具链操作员快速启动 AI 工作流

![使用 Kubernetes AI 工具链操作员快速启动 AI 工作流的特色图片](https://cdn.thenewstack.io/media/2024/07/c4574198-tools-1024x576.jpg)

随着各行各业和创新者寻求将数字体验转型的方法，生成式 AI 正在蓬勃发展。从 AI 聊天机器人到语言翻译工具，人们在日常场景中与一组通用的 AI/ML 模型（称为语言模型）进行交互。因此，近年来，新的语言模型在规模、性能和用例方面迅速发展。

作为应用程序开发人员，您可能希望通过简单地进行 REST 调用并将您的应用程序指向推理端点来集成高性能模型，以选择 Falcon、Mistral、Phi 和其他模型。就这样，您打开了 AI 王国的大门，以及各种智能应用程序。

开源语言模型是[使用 AI 进行实验](https://thenewstack.io/ai/) 的经济高效方式，而[Kubernetes](https://thenewstack.io/primer-how-kubernetes-came-to-be-what-it-is-and-why-you-should-care/) 已成为最适合扩展和自动化 AI/ML 应用程序的开源平台，同时不会影响用户和公司数据的安全性。

“让我们让 Kubernetes 成为 AI 转型的引擎，”微软首席产品经理主管 Jorge Palma 说。他在 2024 年欧洲 KubeCon 大会上发表了主题演讲，会上到处都在讨论 AI 用例。Palma 谈到了他遇到的许多开发人员，他们都在自己的基础设施中本地部署模型，将它们放入容器中，并使用 Kubernetes 集群来托管它们。

“容器映像是模型的绝佳格式。它们易于分发，”Palma 在 KubeCon 大会上说。“然后，您可以将它们部署到 Kubernetes，并利用它提供的所有不错的原语和抽象——例如，管理异构基础设施，并且可以大规模扩展。”

[容器](https://thenewstack.io/containers/) 还可以帮助您避免恼人的“但在我的机器上运行良好”问题。它们是可移植的，因此您的模型可以在各种环境中一致地运行。它们简化了版本控制，以便在您微调以提高性能时更好地维护模型的迭代。容器提供资源隔离，因此您可以运行不同的 AI 项目，而不会混淆组件。当然，在 Kubernetes 集群中运行容器可以轻松地进行扩展——这是处理大型模型时的一个关键因素。

“如果您不打算使用 Kubernetes，您打算做什么？”微软软件工程师 Ishaan Sehgal 问道。他是 Kubernetes AI 工具链操作员 (KAITO) 项目的贡献者，并帮助开发了其主要组件，以简化在给定集群上部署 AI。KAITO 是一个 Kubernetes 操作员，也是微软开发的开源项目，它在您的集群中运行，并自动部署大型 AI 模型。

正如 Sehgal 指出的那样，[Kubernetes 为您提供了运行 AI 工作负载所需的规模和弹性](https://thenewstack.io/why-kubernetes-needs-to-be-dumbed-down-for-devops/)。否则，如果虚拟机 (VM) 出现故障或您的推理端点出现故障，您必须附加另一个节点并重新设置所有内容。“弹性方面，数据管理——Kubernetes 非常适合运行 AI 工作负载，原因就在于此，”他说。

## Kubernetes 使其更轻松，KAITO 进一步提升

Kubernetes 使扩展 AI 模型变得更加容易，但它并不完全容易。在我的文章“[将您的 AI/ML 工作负载带到 Kubernetes 并利用 KAITO](https://vmblog.com/archive/2024/03/05/bring-your-ai-ml-workloads-to-kubernetes-and-leverage-the-kubernetes-ai-toolchain-operator-kaito.aspx)”中，我重点介绍了开发人员在此过程中面临的一些障碍。例如，仅仅开始就非常复杂。如果没有先前的经验，您可能需要几周才能正确设置您的环境。下载和存储大型模型权重（大小超过 200 GB）仅仅是开始。模型文件存在存储和加载时间要求。然后，您需要有效地将模型容器化并托管它们——在考虑成本的同时选择适合您模型的 GPU 大小。此外，还需要解决计算硬件上令人讨厌的配额限制问题。

使用 KAITO，以前可能需要几周才能完成的工作流现在只需几分钟即可完成。此工具简化了在 Kubernetes 上部署、扩展和管理 AI 工作负载的繁琐细节，因此您可以专注于 ML 生命周期中的其他方面。您可以从各种流行的开源模型中进行选择，或加入您的自定义选项，KAITO 会调整部署参数并自动为您配置 GPU 节点。如今，KAITO 支持[五个模型系列和十多个容器化模型](https://github.com/Azure/kaito/tree/main/presets)，从小型到大型语言模型不等。
## KAITO 的工作原理

使用 KAITO 是一个两步过程。首先，在您的集群上安装 KAITO，然后选择一个预设，该预设封装了使用您的模型进行推理所需的所有要求。在关联的工作区自定义资源定义 (CRD) 中，建议使用最小 GPU 大小，这样您就不必搜索理想的硬件。您始终可以根据需要自定义 CRD。部署工作区后，KAITO 使用节点供应器控制器来自动执行其余操作。

“KAITO 基本上会为您配置 GPU 节点并将它们添加到您的集群中，”微软高级云布道师 Paul Yu 解释道。“作为用户，我只需要将我的工作区部署到 AKS 集群中，这就会创建额外的 CR。”

如以下 KAITO 架构所示，工作区调用供应器为您创建和配置合适大小的基础设施，甚至将您的工作负载分布到更小的 GPU 节点以降低成本。该项目使用开源 [Karpenter](https://karpenter.sh/) API 来根据您请求的大小配置 VM，安装适用于 Kubernetes 的正确驱动程序和设备插件。

对于具有合规性要求的应用程序，KAITO 提供对数据安全性和隐私的细粒度控制。您可以确保模型在您组织的网络中被隔离，并且您的数据永远不会离开 Kubernetes 集群。

查看此教程，了解如何 [将您自己的 AI 模型引入 Azure Kubernetes 服务上的智能应用程序](https://aka.ms/kaito-live)，Sehgal 和 Yu 在几分钟内将 KAITO 集成到一个常见的电子商务应用程序中。

## 使用托管 Kubernetes

目前，您可以使用 KAITO 在 Azure 上配置 GPU，但该项目正在快速发展。[路线图](https://github.com/orgs/Azure/projects/669) 包括对其他托管 Kubernetes 提供商的支持。当您使用托管 Kubernetes 服务时，您可以更轻松地与该云平台中的其他服务交互，以向您的工作流或应用程序添加功能。

今年早些时候，[在 Microsoft Build 2024 上，宝马谈到了其在生成式 AI 中的使用](https://build.microsoft.com/sessions/812d376f-56fe-411b-a10c-1faa3c1d80c9?source=sessions) 以及 Azure OpenAI 服务在其运行在 AKS 上的联网汽车应用程序 My BMW 中的使用。

Kubernetes [开源项目](https://thenewstack.io/open-source-project-momentum-what-it-takes/) 的联合创始人 Brendan Burns 介绍了演示。“我们看到的是，随着人们使用 Azure OpenAI 服务，他们正在 AKS 之上构建应用程序的其余部分，”他告诉观众。“但是，当然，仅仅使用 OpenAI 服务并不是您可能想要使用的唯一东西。有很多原因可能导致您想要使用开源大型语言模型，包括数据和安全合规性以及微调您想要做的事情等情况。也许那里有一个更适合您任务的模型。但在 AKS 内部执行此操作可能很棘手，因此我们将 Kubernetes AI 工具链操作员集成到一个开源项目中。”

## 使用 KAITO 使您的语言模型更智能

开源语言模型是在来自各种来源的大量文本上训练的，因此针对特定领域的提示的输出可能并不总是满足您的需求。例如，以宠物店应用程序为例。如果客户向集成的预训练模型询问狗粮推荐，它可能会给出几种流行犬种的几种不同价格选项。这很有信息量，但不一定有用，因为客户正在购物。在 [使用宠物店的历史数据微调模型](https://thenewstack.io/automating-context-in-structured-data-for-llms/) 之后，推荐可以改为针对商店中评价良好、价格合理的选项进行定制。

作为机器学习生命周期中的一个步骤，微调有助于将开源模型定制到您自己的数据和用例中。KAITO 的最新版本 v0.3.0 支持微调，以及使用适配器和更广泛的模型进行推理。您只需在 KAITO 工作区 CR 中定义您的调整方法和数据源，即可看到您的智能应用程序变得更加上下文感知，同时在您的集群中维护数据安全性和合规性要求。

要了解项目的最新路线图并测试这些新功能，请查看 [GitHub 上的 KAITO](https://github.com/Azure/kaito)。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)