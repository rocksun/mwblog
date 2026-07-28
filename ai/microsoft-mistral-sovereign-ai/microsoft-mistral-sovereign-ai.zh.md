**Microsoft 和 Mistral 正在深化合作伙伴关系**，签署了一项价值数十亿美元的协议，专注于企业级人工智能基础设施。其目标是让各类组织能够更灵活地选择运行前沿模型的位置以及管理这些部署的方式，特别是在那些数据驻留和[主权要求](https://thenewstack.io/palantir-nvidia-sovereign-ai/)严格的地区。

根据[周二宣布](https://news.microsoft.com/source/2026/07/21/microsoft-and-mistral-expand-strategic-partnership-to-give-enterprises-and-regulated-industries-frontier-ai-they-can-control/)的协议，Microsoft 将利用 Mistral 不断扩展的欧洲计算基础设施来增加区域容量。与此同时，Mistral 计划部署数千块 NVIDIA Vera Rubin GPU，为从模型训练到多智能体工作负载的所有任务提供动力。

对于受监管行业的工程团队来说，这一公告强调了企业级 AI 的未来发展方向。许多组织不再希望公有云成为他们运行 AI 模型的唯一场所。他们要求部署方案能够适配其现有的基础设施，包括本地部署（on-premises）和气隙隔离（air-gapped）环境。

## 主权计算遇上智能体 AI

在计算层，该协议使 Microsoft 能够访问其传统的第一方数据中心和租赁设施之外的欧洲运营基础设施。此举建立在 Microsoft 于 2025 年宣布的“欧洲数字承诺”基础上，该承诺侧重于将客户数据保留在欧洲，并帮助组织满足区域监管要求。

至关重要的是，Mistral 将利用 NVIDIA 的下一代 Vera Rubin 机架级平台来驱动这一基础设施。由于主权环境支持多步骤[智能体工作流](https://thenewstack.io/agentic-ai-token-costs/)，这种硬件组合至关重要。NVIDIA 声称，与 Grace Blackwell 一代相比，该平台在大规模场景下可提供高达 10 倍的智能体吞吐量。

> “欧洲应当能够在不损害对其数据、运营或数字未来的控制权的前提下，获取世界上最强大的 AI 能力。”

尽管具体的财务条款、容量分配和推广时间表尚未公开，但该协议将 Mistral 定位为 Microsoft 企业生态系统的 AI 模型供应商和独立的欧洲计算供应商。对于担心美国《云法案》（CLOUD Act）的欧洲公司来说，其吸引力显而易见——尽管总部位于美国的供应商能否完全将数据置于其管辖范围之外，在法律上仍存在争议。

“欧洲应当能够在不损害对其数据、运营或数字未来的控制权的前提下，获取世界上最强大的 AI 能力，”[Microsoft 副董事长兼总裁 Brad Smith](https://thenewstack.io/nadella-reverse-information-paradox/) 在公告中表示。

## 模型层

在模型和 API 层，Microsoft 宣布 Mistral Medium 3.5 和 Mistral OCR 4 现已在 Microsoft Foundry 上线，其中 Medium 3.5 也已集成到 Microsoft Copilot Studio 中。

加入 Azure AI Foundry 的模型包括 Mistral Medium 3.5，这是一个拥有 1280 亿参数和 256,000 token 上下文窗口的开放权重模型，这表明它更适合需要处理长文档或持续对话的应用程序。

Microsoft 还增加了 Mistral OCR 4，该模型专为文档密集型 AI 工作流而设计。该模型可以处理 170 种语言的文档，并保留有关页面布局的信息，包括边界框、文档结构和置信度级别。

> 该模型可以处理 170 种语言的文档，并保留有关页面布局的信息，包括边界框、文档结构和置信度级别

## 气隙隔离部署成为主流

对于开发者而言，主要的各种技术获益在于架构对称性。工程师可以在 Microsoft Foundry 内部构建、测试和微调应用程序，并将这些工作负载迁移到公有 Azure、Azure Local 或由 Mistral 运营的主权基础设施上，而无需重构底层工作流。

这种混合可移植性针对的是受严格合规法规约束的行业。部署选项还包括完全气隙隔离的环境，允许组织在与公共互联网完全隔离的网络上运行 AI 工作负载。

## 部署灵活性驱动决策

此次合作表明，部署灵活性正成为[购买决策](https://thenewstack.io/ibm-earnings-ai-infrastructure/)的一部分。许多组织希望拥有在云端、本地或区域基础设施中运行 AI 的自由，[而不受单一方案的束缚](https://thenewstack.io/future-proof-ai-infrastructure/)。这正是 Microsoft 与 Mistral 扩展关系的核心价值所在。

两家公司押注，为客户提供更多部署选项的重要性将等同于提供极具竞争力的模型。如果这一策略成功，Microsoft 将成为世界上受监管最严格的行业如何运行 AI 的[控制平面](https://thenewstack.io/enterprise-ai-model-routing/)。

> 如果这一策略成功，Microsoft 将成为世界上受监管最严格的行业如何运行 AI 的[控制平面](https://thenewstack.io/enterprise-ai-model-routing/)。