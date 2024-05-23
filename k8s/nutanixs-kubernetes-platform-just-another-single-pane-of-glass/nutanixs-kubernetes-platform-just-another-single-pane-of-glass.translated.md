## Nutanix 的 Kubernetes 平台：仅仅是另一个单一控制面板？

![Nutanix 的 Kubernetes 平台：仅仅是另一个单一控制面板？的特色图片](https://cdn.thenewstack.io/media/2024/05/06a59fb7-anne-nygard-rjtmsjld2bq-unsplash-1-1024x683.jpg)

西班牙巴塞罗那——在 [Nutanix](https://thenewstack.io/nutanix-adds-3-new-parts-to-its-multicloud-dm-platform/) 的年度用户大会 [.NEXT 2024](https://www.nutanix.com/next) 上透露，该公司的 Nutanix Kubernetes 平台 (NKP) 将提供一个全面的平台，用于跨多云管理 [Kubernetes](https://thenewstack.io/kubernetes/)，而无需为各个服务掌握通常的 Kubernetes 诀窍。人工智能将负责大部分集群编排和管理，尽管公司代表并未透露有关如何将其集成到 NKP 中的详细信息，预计它将在今年夏天作为 Nutanix 的 Kubernetes Project Beacon 的一部分提供。

[@nutanix] 首席执行官 [@RajivRamaswami]：Project Beacon 现在涵盖 [@kubernetesio] 管理、基础设施数据服务和平台服务。[#NEXTconf]2024。[pic.twitter.com/55HuxVpmIG]
— BC Gain (@bcamerongain)
[2024 年 5 月 21 日]

另一个听起来好得令人难以置信的控制面板？不提任何名字，现在有很多“墓碑”，尤其是在今天为 Kubernetes 提供单一的万能平台。也就是说，在六个月前，Nutanix 已经提供了一个经过充分测试的单一平台，使组织能够更轻松地采用多云和覆盖本地以及更多基础设施。但借助 NKP，还提供了一个完整的 Kubernetes 管理平台。

“Nutanix 运营模式一直是帮助客户使用单一平台在任何地方运行任何应用程序。借助此新产品，我们将该运营模式扩展到 Kubernetes，”

Nutanix 云原生高级总监兼总经理 [Tobi Knaup](https://www.linkedin.com/in/tobiasknaup/) 告诉 The New Stack。“适用于您的应用程序和数据的任何地方的单一平台。我们还拥有丰富的数据服务组合。”

[@nutanix] 的 Tobi Knaup（[@mesosphere] 联合创始人）让向 [@kubernetesio] 的过渡不再痛苦？Nutanix Kubernetes 平台 (NKP) 是否不仅仅是 Kubernetes 的另一个控制面板？[pic.twitter.com/66MtfDOnOS]
— BC Gain (@bcamerongain)
[2024 年 5 月 21 日]

## 降低门槛

如果 Nutanix 宣传的内容属实，它提供了一种方法来显著简化和降低 Kubernetes 采用的门槛，无论从用户还是管理方面来看。Nutanix Kubernetes 的全面云堆栈当然包括主要的云提供商，包括 [GCP](https://cloud.google.com/?utm_content=inline+mention)、[AWS](https://aws.amazon.com/?utm_content=inline+mention) 和 Azure，但现在您通过这些云提供商或其他平台（包括 OpenShift）进行 Kubernetes 管理。

此平台结合了 Nutanix 的 Kubernetes 引擎和主要功能，即 [D2IQ](https://thenewstack.io/d2iq-formerly-mesosphere-brings-enterprise-management-to-kubernetes/) 产品系列，Nutanix 于 2023 年收购了该产品系列。D2IQ 以前是 [Mesosphere](https://thenewstack.io/kubernetes-mesosphere-and-the-art-of-distributed-computing/)，由 Knaup 联合创立。

NKP 被设计为一个中央平台，允许您管理您的整个 Kubernetes 集群机群。无论是在 Nutanix 基础设施或 vSphere 上运行的 NKP 集群（一个已经支持多年并将继续支持的平台），还是像 EKS 或 AKS 这样的公共云托管 Kubernetes 服务。

NKP 管理整个集群机群，并采用并扩展这些公共云服务，其中包括 NTP 的一整套开源附加组件。生命周期管理用于从管理平面启动这些集群，然后使用开源组件将它们构建成完全生产级的解决方案。

这一点至关重要，因为它允许客户拥有在他们运行 Kubernetes 的任何地方进行操作和管理的单一方式。这也意味着，由于它非常节省空间，因此他们的应用程序仍然真正可移植。这与完全依赖一个特定的云并使用那里提供的所有工具有很大不同，这可能导致被锁定在该特定云中，从而使您的应用程序不可移植。我们提供了另一种选择。“可移植性是容器和 Kubernetes 的核心承诺之一，我们确保兑现这一承诺，”Knaup 说。

NKP 还将使用 GPT-in-a-Box 2.0，Nutanix 本周推出该产品，以扩展
## 英伟达加速计算和 LLM 支持

[英伟达](https://thenewstack.io/nvidia-ceo-details-a-new-ai-way-of-developing-software/) 宣布了其 GPT-in-a-Box 2.0 的更新，该更新将包括加速计算和 [LLM](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) 支持。此更新还将提供简化的基础模型管理以及与英伟达 NIM 微服务和 [Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) LLM 库的集成。GPT-in-a-Box 2.0 将提供 API 端点创建，涵盖基础模型和最终用户访问密钥管理。

## 堪培拉大学的云战略

这些发展引起了堪培拉大学等组织的兴趣，该大学正在重新评估其云战略。由于 Nutanix 现在提供在 AWS 和 Azure 等公共提供商上运行 Nutanix 集群的能力，因此它将其视为其混合多云战略的一部分，

澳大利亚堪培拉大学供应商和运营副总监 [贾斯汀·梅森](https://www.linkedin.com/in/justin-mason-960558122/?originalSubdomain=au) 告诉 The New Stack。“当我们谈论自助服务和云原生应用程序时，就是要将控制权交还给活跃用户，”梅森说。“这旨在为他们的学生和研究人员提供更好的用户体验和更多的授权。”

## Nutanix Calm

例如，Nutanix 提供了一个名为 Calm 的产品。它类似于公共云提供商提供的蓝图，组织可以使用这些蓝图来启动 Kubernetes 集群或其他服务。梅森说，研究人员可以进入自助服务门户，请求启动 SQL 实例，而 Nutanix Calm 可以为他们处理此事，类似于公共云提供商。

## Nutanix Kubernetes 平台 (NKP) 功能

具体来说，Nutanix 在其文档中传达了 NKP 的以下功能：

- 面向数据驱动型应用程序的 Kubernetes 平台：NKP 与业界领先的 Nutanix 数据服务产品组合集成，提供可靠的横向扩展块、文件和对象存储，以及数据库即服务。
- 通过自动化简化 Kubernetes 管理：NKP 能够通过最佳自动化和人工智能驱动的运营洞察来简化 Kubernetes 部署、安全、监控和升级，从而降低复杂性和人为错误，并建立一致性和标准化。
- 无供应商锁定的完整平台：NKP 建立在符合 CNCF 的 Kubernetes 之上，使客户能够享受开源社区的创新，同时避免与分叉的 Kubernetes 版本和单一供应商解决方案相关的可移植性、兼容性、可升级性和安全问题。此外，由于 NKP 是云原生生态系统的一部分，因此客户可以轻松利用兼容 CNCF 的合作伙伴解决方案来构建适合其特定需求的平台工程堆栈。
- 多集群舰队管理：NKP 通过集中式管理平面简化了 Kubernetes 集群的管理，该管理平面是一个用户友好的仪表板，充当对本地、公共云、边缘和气隙环境中运行的集群进行观察和控制的单一入口点。NKP 通过一整套平台服务扩展了 EKS 和 AKS 等公共云 Kubernetes 服务，为客户提供了一种管理其整个 Kubernetes 舰队的单一标准化方式。

## 订阅 The New Stack

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、采访、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)