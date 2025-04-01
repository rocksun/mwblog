<!--
title: 红帽利用AI驱动的迁移工具武装开发者
cover: https://cdn.thenewstack.io/media/2025/04/8b189415-getty-images-rofhvbj8qrc-unsplash-1.jpg
summary: 红帽 KubeCon 发布 Konveyor AI (Kai) 0.1，用 RAG 加速应用现代化，结合 LLM 和静态代码分析，无需微调模型即可生成 Kubernetes 部署工件。RHDH 1.5 增强开发者门户，提供超 60 个动态插件和 RHDH Local 本地运行版，提升开发者效率。
-->

红帽 KubeCon 发布 Konveyor AI (Kai) 0.1，用 RAG 加速应用现代化，结合 LLM 和静态代码分析，无需微调模型即可生成 Kubernetes 部署工件。RHDH 1.5 增强开发者门户，提供超 60 个动态插件和 RHDH Local 本地运行版，提升开发者效率。

> 译自：[Red Hat Arms Developers With AI-Powered Migration Tools](https://thenewstack.io/red-hat-arms-developers-with-ai-powered-migration-tools/)
> 
> 作者：Steven J Vaughan-Nichols

伦敦 — 在此举行的 [KubeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 大会上，[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 通过发布对其两个编程和 [平台工程](https://thenewstack.io/platform-engineering/) 工具的更新，展示了其开发者实力。该公司发布了 [Konveyor AI (Kai) 0.1](https://www.redhat.com/es/blog/new-updates-konveyor-ai-use-ai-driven-application-modernization-without-fine-tuning-model)，这是一个人工智能支持的开源 [应用现代化](https://thenewstack.io/application-delivery-controllers-a-key-to-app-modernization/) 工具，以及 [Red Hat Developer Hub (RHDH) 1.5](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.5/pdf/about_red_hat_developer_hub/Red_Hat_Developer_Hub-1.5-About_Red_Hat_Developer_Hub-en-US.pdf)，这是一个增强的开发者门户，旨在简化软件开发流程。

## Konveyor AI 0.1：人工智能驱动的应用现代化

[Konveyor AI 0.1](https://www.cncf.io/blog/2024/11/22/konveyor-ai-supporting-application-modernization/) 将生成式人工智能 (GenAI) 集成到传统迁移工作流程中。它的目标是简化云原生环境的应用现代化。目前还没有消息表明它将被用于将社会保障的 [COBOL](https://thenewstack.io/going-from-cobol-to-cloud-native/) 代码拖入21世纪。

Kai 使用 [检索增强生成 (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/) 方法。它通过结合公司遗留的静态代码分析和过去的迁移示例来实现这一点。借助 RAG，Kai 可以根据之前如何解决类似的迁移挑战，提供高度相关的代码建议，从而避免了大量的 AI 重新训练。

此版本将模型无关的 [大型语言模型 (LLM)](https://thenewstack.io/what-is-a-large-language-model/) 与静态代码分析相结合，使开发人员能够自动执行源代码更改并从过去的转换中获得见解，而无需进行模型微调。

最后，Konveyor 还在引入更新，以 [帮助将应用程序重新平台化到 Kubernetes](https://konveyor.io/components/konveyor-cli/)。例如，新的资产生成功能允许应用程序部署和运行时配置检索，从而创建 [Kubernetes](https://thenewstack.io/kubernetes/) 部署工件。

其他主要新功能包括：

*   **改进的静态代码分析：** 识别采用新技术时可能出现的问题。
*   **问题跟踪：** 维护已解决的现代化挑战的历史记录。
*   **增强的迁移智能：** 为不同的迁移路径提供 2,400 条预定义规则，并可以选择定义自定义规则。
*   **VS Code 扩展：** 在 IDE 中提供建议的代码更改。

## RHDH 1.5：增强的开发者门户

RHDH 1.5 是一个可定制的开发者门户，旨在提高开发者生产力并简化应用程序开发。Red Hat 开发者工具高级总监 [Balaji Sivasubramanian](https://www.linkedin.com/in/balajisiva/) 在一份声明中表示：“Red Hat Developer Hub 的最新功能旨在不仅帮助组织提高采用率和效率，还可以实现更定制化的门户，为开发者提供直接访问他们所需的工具、模板和组件，以推动创新。”

那么，这些是什么呢？首先，此版本完全关于定制。借助 [RHDH Extensions Catalog](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.5/html/installing_and_viewing_plugins_in_red_hat_developer_hub/rhdh-extensions-plugins_assembly-install-third-party-plugins-rhdh)，以开发者预览版提供，程序员可以访问社区和经过验证的 Red Hat 插件的目录视图。

扩展目录提供了超过 [60 个动态插件](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.5/html/dynamic_plugins_reference/con-preinstalled-dynamic-plugins#con-preinstalled-dynamic-plugins%7Chttps://docs.redhat.com/en/documentation/red_hat_developer_hub/1.5/html/dynamic_plugins_reference/con-preinstalled-dynamic-plugins#con-preinstalled-dynamic-plugins) 的入口。然后，您可以自定义 Developer Hub 以满足您的特定需求。此外，借助动态插件框架，您的团队可以在运行时管理任何插件（包括自定义插件），而无需重建和重新部署门户。这使得载入新工具和功能的速度更快、更容易。
开发者中心现在还提供了一个开发者预览版，即 [RHDH Local](https://github.com/redhat-developer/rhdh-local) 的本地可运行版本。这使平台工程师能够在本地机器上运行轻量级的、自包含的 RHDH 版本，从而使程序员能够更快、更轻松地更改其门户，并缩短周期时间。

借助 RHDH Local，用户可以处理模板、试用插件、验证软件目录等，而无需在 Kubernetes 集群上安装 RHDH。此外，由于它在容器化环境中运行，因此用户可以在几秒钟内启动 RHDH Local，并以同样的速度将其关闭。作为一个喜欢尽可能保持本地控制的人，我真的很喜欢 RHDH Local 的想法。

最后但并非最不重要的一点是，分析仪表板提供了关于门户使用情况的详细指标，帮助团队识别成功和需要改进的领域。

这些更新是红帽公司为支持组织开发智能应用程序并最大限度地提高开发者生产力而不断努力的一部分。红帽计划继续使用 AI 驱动的功能来增强其迁移工具包，旨在使大规模现代化更加高效。