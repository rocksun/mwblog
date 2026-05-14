<!--
title: Red Hat 押注 AgentOps 以弥合 AI 实验与生产之间的鸿沟
cover: https://cdn.thenewstack.io/media/2026/05/69e5bd47-ruliff-andrean-0iho6quvwxk-unsplash-scaled.jpg
summary: Red Hat在峰会上发布RHAI 3.4，通过AgentOps和MaaS技术弥合AI实验与生产的鸿沟。该版本聚焦混合云环境下的智能体部署、治理与安全，助力企业实现自主系统的规模化创新。
-->

Red Hat在峰会上发布RHAI 3.4，通过AgentOps和MaaS技术弥合AI实验与生产的鸿沟。该版本聚焦混合云环境下的智能体部署、治理与安全，助力企业实现自主系统的规模化创新。

> 译自：[Red Hat is betting on AgentOps to close the gap between AI experiments and production](https://thenewstack.io/red-hat-ai-maas/)
> 
> 作者：Steven J. Vaughan-Nichols

周二，在亚特兰大举行的 [Red Hat 峰会](https://www.redhat.com/en/summit)上，Red Hat 宣布了 [Red Hat AI (RHAI) 3.4](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_ai) 的重大进展。

Red Hat 承诺提供该公司[描述](https://www.redhat.com/en/about/press-releases/red-hat-unites-builders-and-operators-agentic-future-major-advancements-red-hat-ai)为“从硬件到智能体（metal-to-agent）”的能力，旨在弥合混合云基础设施中 AI 实验与生产级运营控制之间的鸿沟。

据 [Red Hat](https://www.redhat.com/en) AI 业务副总裁 [Joe Fernandes](https://www.linkedin.com/in/joefernandes1/) 称，这意味着公司的 AI 战略“分为四个核心支柱。首先，帮助客户提供快速、灵活且高效的推理，在其环境中部署模型。其次，将他们的企业数据连接到这些模型和智能体。第三，帮助他们在混合云环境中加速智能体的部署和管理。第四，将所有这些整合到我们的集成 AI 平台上，使他们能够在任何硬件和云环境中运行任何模型和智能体。”

最后一点关于“将所有这些整合在一起”是 Red Hat 最新 AI 计划中一个全新且重要的部分。RHAI 3.4 的核心是[模型即服务](https://www.redhat.com/en/topics/ai/what-is-models-as-a-service) (MaaS)。这使你能够将预训练的 AI 和机器学习模型作为共享资源，通过 API 端点按需访问。在 Red Hat 对这一理念的实现中，MaaS 还为开发人员访问精选模型提供了一个统一的受治理接口，同时使管理人员能够跟踪消耗并执行策略。

> 在 Red Hat 对模型即服务的实现中，它还为开发人员访问精选模型提供了一个统一的受治理接口，同时使管理员能够跟踪消耗并执行策略。

此外，RHAI 3.4 构建在由 [vLLM 推理服务器](https://docs.vllm.ai/en/latest/)和 [llm-d 分布式推理引擎](https://developers.redhat.com/articles/2025/11/21/introduction-distributed-inference-llm-d)驱动的高性能分布式推理之上，以在不同环境中保持优化的模型服务。最重要的是，RHAI 推理在其分布式推理能力中增加了请求优先级排序。

这允许交互式流量和后台流量共享同一个端点，同时在负载下优先处理对延迟敏感的请求。Red Hat 还声称，[投机采样解码支持](https://docs.vllm.ai/en/latest/features/speculative_decoding/)“在对质量影响极小的情况下，将响应速度提高 2 到 3 倍，同时降低了每次交互的成本”。

> “智能体时代代表了我们平台从运行传统应用程序到驱动智能自主系统的进化。”

这非常有用，因为越来越受欢迎的智能体消耗大量资源。正如 Joe Fernandes 观察到的那样：“真正推动推理需求呈指数级增长的将是 AI 智能体。”

为了解决自主智能体的运营挑战，RHAI 3.4 引入了全面的 AgentOps 能力，包括“集成追踪、可观测性和评估，以及智能体身份和生命周期管理，从而将智能体从开发推向生产”。该平台与框架无关，可以管理“任何智能体框架”下的智能体。

Joe Fernandes 继续说道：“因此，通过我们新的 [MCP [模型上下文协议]](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 服务器目录和 MCP 网关，我们在建立这些连接时提供了对基于 MCP 服务器的工具的受控访问以及运行时的安全访问。企业客户需要我们帮助将他们的企业数据连接到模型和智能体。

“我们正在引入一个新的评估枢纽，它提供了一个集成的控制平面和一系列评估框架，以帮助评估模型和智能体性能、集成的实验跟踪，以及检索增强生成 (RAG) 和传统 ML 模型配置的自动化。再说一次，所有这些都汇聚在我们的 AI 平台中。”

为了确保这一切的安全，Red Hat 现在使用基于 SPIFFE/SPIRE 的加密身份管理。这使组织能够用短期令牌取代静态硬编码密钥，以支持“针对整个堆栈中自主智能体的最小权限操作，并帮助确认智能体行为与经验证的身份绑定。

虽然这确实有帮助，但 RHAI 还将自动对抗性扫描直接集成到了开发生命周期中。它通过利用其新收购的 Chatterbox Labs 的技术并使用 LLM 漏洞扫描工具 [Garak](https://docs.garak.ai/garak) 来实现这一点。RHAI 利用它来筛选模型和智能体系统中的风险，如越狱、提示词注入和偏见。Red Hat 还与 [Nvidia NeMo Guardrails](https://developer.nvidia.com/nemo-guardrails) 配合以实现运行时安全。”

Red Hat 还引入了集成提示词管理。这不仅将提示词视为一流的数据资产，还将驱动模型和智能体的输入存储在中央注册表中，为开发人员和管理员提供单一事实来源。

为了确保这一切尽可能高效地运行，RHAI 的评估枢纽提供了一个与框架无关的统一 AI 评估控制平面，用于评估大语言模型 (LLM)、AI 应用程序和智能体。Red Hat 称，这取代了“碎片化的测试方法，采用统一的方法来基准测试质量、准确性和风险”。这些功能由 [MLflow](https://mlflow.org/) 驱动，它“为生成式和预测式 AI 用例提供集成的实验跟踪和制品管理”。

从战略上看，Joe Fernandes 表示：“智能体时代代表了我们平台从运行传统应用程序到驱动智能自主系统的进化。我们正在定义企业执行 AI 的开放标准。通过为 AI 推理、MaaS 和 AgentOps 提供硬化的、从硬件到智能体的基础，Red Hat 提供了组织在保持严格控制的同时进行大规模创新所需的运营保障。”

这听起来很宏大。我们很快就能知道 RHAI 是否能兑现 Red Hat 的承诺。该计划尚未准备好在 Red Hat 峰会上正式揭晓，预计将在本季度的某个时间发布。我期待着看到它的实际表现，我知道我不是唯一一个对此期待的人。