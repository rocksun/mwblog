
<!--
title: 为什么Red Hat必须改进边缘开发者体验
cover: https://cdn.thenewstack.io/media/2024/11/cc739340-planet-volumes-bq1nbwrwzwe-unsplash.jpg
-->

Red Hat 通过增强 AI 功能提升开发者工具，同时扩展边缘计算解决方案。

> 译自 [Why Red Hat Had To Improve the Edge Developer Experience](https://thenewstack.io/why-red-hat-had-to-improve-the-edge-developer-experience/)，作者 B Cameron Gain。


盐湖城——[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 已经认识到增强开发者体验的重要性，因为它在 OpenShift 和 [RHEL](https://thenewstack.io/configure-multiple-websites-on-a-single-rhel-based-apache-host/) 的多个方面取得进展。值得注意的是，在最近的 [KubeCon+CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 系列发布会上，该公司推出了新版本的 Red Hat Device Edge。

OpenShift AI 也支持红帽改进开发流程的努力。

Red Hat Device Edge 项目始于五年前。它被描述为 Red Hat Enterprise Linux 的一个分支，旨在满足使用 [Kubernetes](https://thenewstack.io/kubernetes/) 的各个客户的更具体需求。

最初，重点是利用 Kubernetes 进行 5G 和工业应用的电信公司。随着时间的推移，这一范围已扩大到包括构成边缘部署的各种环境中的部署。

![](https://cdn.thenewstack.io/media/2024/11/96c59fe3-capture-decran-2024-11-07-092222.png)

通过使用 Red Hat Device Edge 并将 Kubernetes 运行在边缘，红帽提供了一种解决方案，可以减少延迟并提供运营团队重视的基础设施底层功能。同时，正如本次发布所展示的那样，该公司继续增强开发者体验。

Red Hat Device Edge 最初与 RHEL 具有相同的核心组件，但也有关键区别。它没有编译数百或数千个单独的软件包来形成操作系统，而是采用了新方法：这种方法涉及创建时间点映像，它们是各个软件包的摘要，构成了 Red Hat Device Edge 面向边缘的操作系统基础，根据红帽文档。

这种方法解决了红帽与客户和合作伙伴沟通的几个关键需求：

- 镜像是不可变的，确保部署一致性并防止随着时间的推移对已部署系统进行意外更改。
- 更新以增量方式交付，最大限度地减少更新的带宽需求。
- 每个镜像都是独立可引导的，能够实现自动健康检查和标准化回滚功能。
- 减少的基础软件包集提供了一个紧凑且可移植的基础，适合低功耗设备。

## 变得边缘

[Red Hat Device Edge](https://www.redhat.com/en/technologies/device-edge) 将 RHEL 与 [MicroShift](https://www.redhat.com/en/topics/edge-computing/microshift) 相结合。红帽产品管理高级总监 [Shobhan Lakkapragada](https://www.linkedin.com/in/shobhan) 在一次简报中表示，MicroShift 充当轻量级基于 Kubernetes 的解决方案，源自 OpenShift，专为边缘环境中通常存在的最小硬件而设计。MicroShift 的特点是低 CPU 和内存需求，但仍然保留了与 OpenShift 相关的许多好处。[Ansible](https://thenewstack.io/red-hat-ansible-lightspeed-uses-ai-to-automate-infrastructure-management/) 也包含在此解决方案中，以方便边缘环境的管理。“这个集成平台以极具吸引力的价格提供边缘计算，”Lakkapragada 说。

Lakkapragada 表示，在 KubeCon+CloudNativeCon 上发布的 Red Hat Device Edge 4.17 具有两个主要更新：增强的低延迟工作负载支持和改进的边缘 AI 工作负载支持。Lakkapragada 说，还推出了一个新的 Red Hat Device Edge 版本，“针对工业控制软件进行了预调优和预配置”。此版本支持正在进行数字化转型的工业系统，允许通过此新配置对工业控制堆栈进行现代化改造，Lakkapragada 说。

因此，AI 支持在帮助改进 Red Hat Device Edge，特别是对于开发者方面发挥着关键作用。也就是说，红帽的 OpenShift AI 仍然“是一款相对较新的产品”，正如红帽 AI 产品经理 [Jeff DeMoss](https://www.linkedin.com/in/jeff-demoss/) 在简报中参考 OpenShift AI 2.15 时解释的那样。

“我们去年推出了它，并且正在大力投资它。总的来说，这是一个 AI 平台，使企业能够在混合云环境中创建和部署支持 AI 的应用程序，”DeMoss 说。

DeMoss 说，OpenShift AI 支持预测性 AI 和生成式 AI 用例，提供“AI 生命周期中的广泛功能”。这些包括模型开发、训练、服务、监控和 AI 工作流的自动化。
DeMoss解释说，利用OpenShift AI和其他Red Hat AI资产提供的功能简化了使用。一个重要方面是使开发人员能够高效地创建应用程序。DeMoss强调了确保开发人员能够找到并利用必要资产的重要性，例如提供特定模型的企业[LLM（大型语言模型）](https://thenewstack.io/llm/)。需要一个清晰的流程来在一个中央存储库中编目这些资源。

DeMoss将开发者中心描述为一个满足这一需求的平台。通过集中文档和资源，开发者中心消除了开发人员原本需要花费在搜索信息上的时间。这种编目方法加快了企业内部AI工具的采用，有助于创建应用程序，并确保开发人员能够高效地访问和使用资产。

展望未来，DeMoss表示，未来的版本将把额外的AI功能集成到产品中，通过AI驱动的解决方案提高生产力。“在2.15版本中，首先，我们引入了一个模型注册表，它连接了模型实验和生产活动。模型注册表充当中央存储库，用于管理版本、元数据和模型工件，”DeMoss说。“它通过使团队能够协同处理模型并将它们更有效地部署到生产环境中，从而增强了整体MLOps工作流程。此外，它还通过提供有关模型版本、文档、来源、使用的数据集和评估指标的信息来支持模型治理。”

作为此功能的一部分，客户可以在其组织内创建多个注册表，定义权限以控制用户或组级别的访问，并直接从注册表部署模型。此功能是在Kubeflow开源项目中开发的。

对于模型服务，用户可以访问[vLLM](https://github.com/vllm-project/vllm)服务运行时，这是一个流行的用于服务LLM的开源运行时。根据Red Hat文档，vLLM是一个高度灵活的运行时，支持Hugging Face上大多数流行的开源模型，包括Llama、Mixtrol和Mistrol。它还提供了许多功能和优化，以提高服务LLM时的性能。“在OpenShift AI中，我们集成了最新版本的vLLM，它支持最新的模型架构和多模态模型，例如视觉语言模型，”DeMoss说。

开发人员应该能够依靠AI来创建应用程序，而Red Hat Device Edge或OpenShift的其余平台则抽象掉了基础设施支持。

“开发人员无需花费时间来弄清楚使用方法细节或搜索文档。所有必要的信息都可以作为AI资产的集中目录的一部分提供，”Balaji Sivasubramanian说。“这种方法通过不仅能够创建新的应用程序，而且简化了使这些资产和应用程序可供开发人员访问的过程，从而加快了企业的转型。”


## 中心

![](https://cdn.thenewstack.io/media/2024/11/49d58591-capture-decran-2024-11-07-092613.png)

支持AI的应用程序开发构成了Red Hat开发者中心改进的重要部分。Red Hat开发者中心为组织提供了模板和资源，以开始其在Kubernetes和容器上开发边缘应用程序或其他类型部署的AI辅助之旅。

Red Hat开发者中心模板包括：

- 音频转文本应用程序：一个支持AI的音频转录应用程序，允许用户上传要转录的音频文件。
- 聊天机器人应用程序：一个支持LLM的聊天应用程序，用于创建一个使用AI生成的回复进行回复的机器人。
- 代码生成应用程序：一个支持LLM的代码生成应用程序，用于一个专门的机器人，帮助处理与代码相关的查询。
- 对象检测应用程序：使开发人员能够上传图像以识别和定位图像中的对象。
- 检索增强生成 (RAG) 聊天机器人应用程序：使开发人员能够嵌入包含相关信息的文件，以允许模型提供更准确的响应。

Red Hat开发者中心旨在汇集许多工具和对开发人员的支持。如果有一个企业LLM（大型语言模型）提供特定模型，则需要一个明确的流程来确保开发人员能够有效地访问和利用这些资源，产品管理和开发者工具高级总监[Balaji Sivasubramanian](https://www.linkedin.com/in/balajisiva)在简报中说。由于所有这些资产都需要在一个中央存储库中编目，“这就是开发者中心，一个面向开发人员的平台，被证明非常有效的地方，”Sivasubramanian说。

“开发者中心消除了开发者需要花费时间去弄清楚如何使用资源或搜索文档的需要。所有内容都可以整合起来，并作为 AI 资源的集中式目录方便访问，”Sivasubramanian 说。“这种方法显著加快了企业的进程，不仅在创建新应用程序方面，还在于确保开发者知道如何有效地使用所有这些资源和应用程序。展望未来，还有更多内容即将推出。未来的版本将把额外的 AI 功能整合到产品中，通过 AI 驱动的解决方案进一步提高生产力。”
