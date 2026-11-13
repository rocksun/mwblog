![全球贸易数据的未来主义数字可视化。](https://cdn.thenewstack.io/media/2025/12/8d3fb16d-network-1024x576.jpg)

**将 AI 工作负载迁移到另一个云**不仅仅是迁移模型及其数据。你的服务层、可观测性仪表盘、安全控制以及[存储系统](https://www.coreweave.com/products/storage?utm_source=coreweave.com&utm_medium=site#object-storage)必须在新基础设施上协同工作。对于平台团队来说，在真实流量下证明这些连接可能是迁移过程中最慢、风险最高的部分。

随着技术栈在供应商和云之间的扩展，每个项目都会带来更多的集成问题。兼容的规范只是一个起点。它不能保证工具在生产环境中会按预期表现，也不能保证围绕它构建的操作手册和安全工作流程能够延续。

## 让生产验证清晰可见

集成必须在你计划运行它的基础设施上、在生产流量下工作。这些工具也应该是你的团队已经在使用或要求的工具。

> “兼容的规范只是一个起点。它不能保证工具在生产环境中会按预期表现，也不能保证围绕它构建的操作手册和安全工作流程能够延续。”

我们构建了 [CoreWeave 合作伙伴网络](https://www.coreweave.com/coreweave-partner-network?utm_source=coreweave.com&utm_medium=site)来使这种验证清晰可见。它将与 CrowdStrike、VAST Data、Reflection、IBM 和其他技术供应商的关系整合到一个精心挑选的网络中，这些集成已在 [CoreWeave 云](https://www.coreweave.com/platform?utm_source=coreweave.com&utm_medium=site)的真实生产条件下进行了测试。

该网络涵盖了 AI 技术栈的四个部分，从[训练](https://www.coreweave.com/solutions/ai-model-training?utm_source=coreweave.com&utm_medium=site)和推理到数据移动、安全以及下一次迭代：

* 基础设施：计算、存储、网络、服务器和互连，合作伙伴包括 VAST Data、Dell、AMD、IBM、BackBlaze 和 Pulumi。
* 数据服务：在 AI 整个生命周期中存储、处理、移动和访问 AI 数据，合作伙伴包括 ClickHouse、Encord、LanceDB 和 Datology。
* 独立软件供应商（ISV）：编排、可观测性和模型开发，包括 Grafana、Datadog、Union、SkyPilot、IBM、Pinecone、Redis、LlamaIndex 和 Clockwork。专门的安全细分市场包括 CrowdStrike、Zscaler 和 Cranium。
* 模型、智能体和推理：用于构建、训练、服务和扩展应用程序的基础软件和服务，合作伙伴包括 Reflection、RadixArk、Inferact、OpenRouter 和 Red Hat。

这些集成共同支持运行和观察模型、策划数据、改善行为以及评估下一个版本。每个合作伙伴都必须满足相同的要求：集成必须能够在 CoreWeave 基础设施上、在生产条件下工作。合作伙伴加入该网络是因为客户运行它们或要求它们。

## 阅读工作负载证据

[IBM 在 CoreWeave 上对其 Granite 模型进行了训练](https://www.coreweave.com/resources/case-studies/ibm?utm_source=coreweave.com&utm_medium=site)，这是 Nvidia GB200 NVL72 集群最早的部署之一。[Cohere 构建了 North](https://www.coreweave.com/resources/case-studies/cohere-accelerates-training-of-north-agentic-ai-for-enterprise?utm_source=coreweave.com&utm_medium=site)，其[智能体 AI 平台](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/)基于行业首批生产级 GB200 NVL72 集群之一，据报道，其训练速度比在 Nvidia Hopper 上快三倍。

[Mistral AI 完全在 CoreWeave 上训练其模型](https://www.coreweave.com/resources/case-studies/mistral-ai?utm_source=coreweave.com&utm_medium=site)，并指出在 Nvidia GB200 NVL72 系统上训练速度快 2.5 倍。[Decart 通过与 CoreWeave 的合作，在生产规模上使用 Nvidia HGX B200](https://www.coreweave.com/resources/videos/creating-realtime-ai-experiences?utm_source=coreweave.com&utm_medium=site)，其平台包括 [Weights & Biases](https://www.coreweave.com/companies/weights-and-biases?utm_source=coreweave.com&utm_medium=site)。

底层关系早于网络公告。自开源大语言模型（LLM）和前沿模型训练浪潮之初以来，CoreWeave 和 Weights & Biases 就已经与 Encord、Pinecone 和其他合作伙伴开展了生产集成。

CoreWeave 首席营收官 [Jon Jones](https://www.linkedin.com/in/jonjones1/) 将这一变化描述为在客户构建之前使现有的合作伙伴工作清晰可见。该网络还提供了一种可重复的方法来追求更深层次的集成、联合市场开拓工作和共享创新。

合作伙伴强调了该系统的不同部分。VAST Data 联合创始人兼首席技术官 Alon Horev 描述了将 CoreWeave 的 AI 云与 VAST AI 操作系统结合起来，用于大规模训练、微调、生产推理和持续的[智能体工作负载](https://thenewstack.io/ai-cloud-taxonomy-2026/)。CrowdStrike 首席执行官兼创始人 [George Kurtz](https://www.linkedin.com/in/georgekurtz/) 强调了构建在运行 AI 的基础设施中的安全性。IBM 美洲区总经理 [Adam Lawrence](https://www.linkedin.com/in/adamelawrence/) 指出，IBM 和红帽技术是扩展选择并在部署和扩展 AI 时减少集成工作的一种方式。

## 延续你已经使用的操作

你的团队已经围绕其可观测性工具构建了操作手册。Grafana 和 Datadog 集成使你能够延续该工作。CrowdStrike、Zscaler 和 Cranium 提供安全集成，带来了现有的威胁可见性和响应工具。

[推理集成](https://www.coreweave.com/solutions/ai-inference?utm_source=coreweave.com&utm_medium=site)具有类似的目的：随着团队扩展到 CoreWeave，保持模型的可用性，而无需[重建服务层](https://thenewstack.io/5-tech-predictions-for-2026-from-ai-inference-to-kubernetes/)。我们的目标是增加容量，同时保留堆栈中已经有效的部分。

> “市场列表仍然让你的团队去验证集成。LLM 可以建议什么是流行的，但不能告诉你什么在你的基础设施上起作用。”

市场列表仍然让你的团队去验证集成。LLM 可以建议什么是流行的，但不能告诉你什么在你的基础设施上起作用。我们根据客户需求选择合作伙伴，并在所有四个细分市场测试他们的集成。

集成问题也延伸到了智能体执行内部。大多数闭源模型包括网络搜索，而大多数开源权重模型则不包括。出于成本、控制或定制而选择开源权重的团队通常不得不单独连接搜索提供商。

CoreWeave 正在将合作伙伴方法扩展到这些工具，首先从 Exa、Parallel Web Systems 和 You.com 开始。宣布的搜索层通过单个集成提供访问权限，而不是为每个提供商签订单独的合同。

团队可以通过标准推理请求上的单个设置启用它，或者从 [CoreWeave Sandbox](https://www.coreweave.com/products/coreweave-sandboxes?utm_source=coreweave.com&utm_medium=site) 内部访问它，而无需设置单独的软件开发工具包（SDK）或帐户。该安排是非排他性的，因此使用集成不会限制未来的提供商选择。

我们在 Fully Connected 上宣布了搜索合作伙伴关系，其余的集成工作计划在接下来的几周内进行。随着这些集成变得可用，它们将满足与网络其余部分相同的生产验证标准。

## 从工作负载所需的连接开始

在添加另一个云之前，请检查你的工作负载所依赖的服务、数据、可观测性和安全连接。询问哪些集成已经在生产条件下进行了测试，以及你的团队仍需验证什么。

> “在添加另一个云之前，请检查你的工作负载所依赖的服务、数据、可观测性和安全连接。”

CoreWeave 合作伙伴网络列出了经过验证的合作伙伴。CoreWeave 客户团队可以讨论特定的集成和工作负载，来自 [Fully Connected 2026](https://www.coreweave.com/fully-connected-2026?utm_source=coreweave.com&utm_medium=site) 的合作伙伴会议提供了查看使用中的集成的另一种方式。对新合作感兴趣的团队可以探索[合作伙伴计划](https://www.coreweave.com/coreweave-partner-network?utm_source=coreweave.com&utm_medium=site#partner-with-coreweave)。

这篇文章最初发布在 [The New Stack](https://thenewstack.io) 上，标题为 [CoreWeave tests AI integrations on its cloud before you migrate](https://thenewstack.io/coreweave-tests-ai-integrations/)。