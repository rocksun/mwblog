# Agentic AI 是新的 Web 应用程序，您的 AI 战略必须发展

![Featued image for: Agentic AI is the New Web App, and Your AI Strategy Must Evolve](https://cdn.thenewstack.io/media/2025/03/9de63de7-phillip-glickman-2umo15jszkm-unsplash-1024x681.jpg)

[Phillip Glickman](https://unsplash.com/@phillipglickman?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)在 [Unsplash](https://unsplash.com/photos/green-and-multicolored-robot-figurine-2umO15jsZKM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)上发布。

在生成式 AI 革命两年后，为 ChatGPT 和 Claude 等工具提供支持的 LLM 变得异常强大。然而，[根据 Salesforce 首席执行官 Marc Benioff 的说法](https://www.salesforce.com/blog/the-agentic-ai-era-after-the-dawn-heres-what-to-expect/)，它们可能正在达到极限。根据 Benioff 的说法，下一个进化不一定是更智能的 LLM，而是利用 LLM 独立执行任务的自主 AI 代理。

Benioff 对 Agentic AI 非常重视，去年推出了 Agentforce，旨在为 Salesforce 客户带来数百万个 AI 代理。他并不孤单：想想前 Forrester 分析师、现任风险投资家的 Jeremiah Owyang 预测，很快就会有[比人类更多的 AI 代理](https://web-strategist.com/blog/2024/09/24/five-ai-agent-predictions/)，每人甚至可能拥有[100 个 AI 代理](https://www.linkedin.com/posts/jowyang_vid-spend-10-minutes-with-me-on-this-video-activity-7267255917669171201-eZTK)。即使这些预测只有一小部分成为现实，也会对电子商务的未来产生深远的影响。

想象一下这样一个世界：AI 代理接管客户与供应商互动的双方。面向客户的资产（如网站和 Web 应用程序）可以被广泛地替换为 — 或至少与 — [针对客户个性化的 AI 代理集成](https://thenewstack.io/evolving-from-pre-ai-to-agentic-ai-apps-a-4-step-model/)。然后，这些代理可以与客户的 AI 代理交互，通过代理之间的交易自动完成销售周期。

Salesforce 并不是唯一拥抱 Agentic AI 的公司。根据 [CapGemini](https://www.capgemini.com/insights/research-library/generative-ai-in-organizations-2024/) 对大型企业 1,100 名高管的调查，10% 的组织已经在使用 AI 代理，超过一半的组织计划在明年使用它们，82% 的组织计划在未来三年内将它们集成。64% 的高管预计 Agentic AI 将改善客户服务和满意度。[Gartner](https://www.gartner.com/en/articles/intelligent-agent-in-ai) 预测，到 2028 年，33% 的企业软件应用程序将包含 Agentic AI。

鉴于这些预测，客户期望 AI 代理向他们提供做出购买决定所需的信息，而不是自己搜索信息，这只是时间问题。

企业正在开发部署 Agentic AI 所需的架构，以期保持领先地位并将其集成到其 Web 应用程序中。具体来说，为了促进全球数千次客户互动，企业将需要在边缘部署低延迟 AI 推理的能力。

**构建支持边缘 Agentic AI 推理的架构**

开发支持边缘低延迟推理的架构是大规模 [Agentic AI 运营](https://thenewstack.io/the-rise-of-ai-agents-how-arazzo-is-defining-the-future-of-api-workflows/)的关键前提，尤其是在电子商务中，AI 代理必须与全球客户实时交互。这种向边缘的转变已经在进行中：[S&P Global Market Intelligence](https://blogs.vultr.com/New-Report-from-SP-Global-Market-Intelligence-and-Vultr-Provides-Unique-Glimpse-into-Path-to-AI-Maturity)（由 Vultr 委托）最近的一项研究发现，在接受调查的 1,000 名 AI 和 IT 专业人士中，超过 80% 的人预计未来一年将增加其 AI 边缘运营。

然而，大多数企业没有支持大规模边缘 AI 推理的基础设施，而且他们永远也不会有。GPU 和其他专用 AI 芯片非常昂贵且很快就会过时，因此内部投资这些资源是不切实际的。

从边缘环境提供的 AI 推理需要不同的技术堆栈，以使大规模 AI 具有成本效益。对于大多数企业来说，用于 AI 推理的无服务器方法在成本和性能方面都是最佳的。

**无服务器推理：成本和性能的最佳选择**

为了避免采购很快就会过时的专用 AI 芯片的资本支出，无服务器方法利用云提供商管理的资源，使每个 AI 工作负载与适合该任务的最佳计算资源相匹配。简而言之，无服务器推理允许企业将基础设施问题留给每天处理此问题的云提供商。
利用无服务器方法，企业可以充分利用云提供商的*硅多样性*——AI计算芯片的超专业化，以满足AI模型生命周期每个阶段的独特计算需求。从客户的角度来看，无服务器方法可以根据AI工作负载和用例需求自动管理适当资源的扩展，从而优化成本和性能。

通过无服务器方法来管理计算资源和优化成本，下一步是开发[支持低延迟数据流的架构](https://thenewstack.io/finding-the-right-data-architecture-for-rag-pipelines/)，并建立数据治理控制，以确保客户数据的安全。

**通过实时Agentic AI推理维护数据主权和隐私**

为了超越像ChatGPT这样的通用AI应用程序，agentic AI应用程序需要访问敏感的专有数据。在电子商务环境中尤其如此，在电子商务环境中，客户数据对于AI代理向客户提供与上下文相关的信息至关重要。当然，每当AI模型利用专有数据时，企业都必须遵守当地的数据治理要求。

向量存储和检索增强生成（RAG）是[维护数据](https://thenewstack.io/choosing-the-right-database-strategy-on-premises-or-cloud/)治理控制的有效策略，可在数据所在的任何位置为agentic AI推理提供支持。在这种方法中，敏感数据保存在受本地数据治理控制保护的向量存储中，AI代理根据需要使用[RAG访问这些数据，而不是直接在敏感数据上训练模型](https://thenewstack.io/rag-without-openai-bentoml-octoai-and-milvus/)。

向量存储和RAG可以在不将敏感数据暴露给第三方模型提供商的情况下，实现与上下文相关的洞察。无需重新训练整个模型即可补充向量存储的内容，从而降低了训练成本。这种方法还使模型更易于跨地域传输，同时遵守当地的数据主权要求。

除了数据治理之外，企业还需要低延迟的[数据流来促进实时](https://thenewstack.io/why-we-use-apache-kafka-for-real-time-data-at-scale/)agentic AI交互。[Apache Kafka](https://kafka.apache.org/)是一个开源流数据平台，非常适合将实时流数据馈送到agentic AI应用程序中。借助RAG和向量存储，Apache Kafka可以在边缘实现低延迟的agentic AI应用程序，同时保持本地治理。

**Agentic AI加剧了对正确架构方法的需求**

与传统的AI相比，[agentic AI将大大加重工程](https://thenewstack.io/making-good-on-the-promise-of-open-source-ai/)团队的负担，他们需要配置和维护复杂的基础设施，以支持分布在广阔地域和数千个边缘设备上的AI代理集群。唯一可行的方法是将无服务器推理与RAG和托管Kafka相结合，从而确保AI代理执行的任务能够准确、安全地执行，且没有明显的延迟。

通过将基础设施配置、配置和自动扩展的复杂性外包给云提供商，工程团队可以专注于构建强大的AI应用层，开发专门构建的AI代理，并优先考虑客户体验。用于AI基础设施的无服务器方法为构建客户旅程的全新agentic未来奠定了完美的基础。

[Tech moves fast, don't miss an episode. Subscribe to our YouTube channel to stream all our podcasts, interviews, demos, and more.](https://youtube.com/thenewstack?sub_confirmation=1)