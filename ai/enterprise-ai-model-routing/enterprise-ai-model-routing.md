<!--
title: 微软承认其最大的AI战略失误，并斥资25亿美元进行补救
cover: https://cdn.thenewstack.io/media/2026/07/0c80276a-gr-stocks-iq9sajezkoe-unsplash-scaled.jpg
summary: 微软宣布投入25亿美元成立新部门，旨在帮助企业通过编排层灵活调用多模型，而非仅依赖单一模型。这一战略转型标志着企业AI部署从绑定厂商转向模型可替换的架构，强调根据任务需求优化成本、性能与合规性。
-->

微软宣布投入25亿美元成立新部门，旨在帮助企业通过编排层灵活调用多模型，而非仅依赖单一模型。这一战略转型标志着企业AI部署从绑定厂商转向模型可替换的架构，强调根据任务需求优化成本、性能与合规性。

> 译自：[Microsoft just admitted its biggest AI mistake — and spent $2.5 billion fixing it](https://thenewstack.io/enterprise-ai-model-routing/)
> 
> 作者：Amanda Caswell

微软最新的AI服务公告表明，标准化单一模型的时代可能即将终结。本周，该公司[推出了一个价值25亿美元的AI采用业务](https://www.reuters.com/business/retail-consumer/microsoft-launches-firm-help-companies-adopt-ai-with-25-billion-2026-07-02/)，旨在帮助企业定制化部署AI，并使用多种模型，而不是将自己锁定在单一提供商身上——这是向“将每个请求路由到最适合该任务的模型”这一系统转变的一部分。

简而言之，这家拥有业内最深厚单一模型合作关系的公司，现在正将“模型可替换性”作为产品进行销售。

## 豪掷25亿美元押注灵活性

据[路透社报道](https://www.reuters.com/business/retail-consumer/microsoft-launches-firm-help-companies-adopt-ai-with-25-billion-2026-07-02/)，微软周四表示，正在创建一个新的运营实体——Microsoft Frontier Company，以帮助企业客户选择真正适合其业务并能产生投资回报的AI技术。该部门成立之初便获得了微软25亿美元的资金支持，并将与包括Unilever和Novo Nordisk在内的客户展开合作。

这家新公司将帮助客户选择并整合AI工具——涵盖来自微软及其外部提供商的工具——并将其与客户各自的内部数据相结合。客户将拥有这些工作成果，而不是将其交还给微软。此举使微软与Palantir（后者正使用Nvidia的开源模型为大客户提供类似服务）以及最近启动了[10亿美元嵌入式工程部门](https://www.cnbc.com/2026/07/02/microsoft-commits-2point5-billion-6000-employees-ai-implementation-unit.html)的Amazon Web Services并驾齐驱。

最能说明问题的是其背后的原因。微软商业业务首席执行官 Judson Althoff [告诉路透社](https://www.reuters.com/business/retail-consumer/microsoft-launches-firm-help-companies-adopt-ai-with-25-billion-2026-07-02/)，这家新公司的成立部分源于微软观察到DeepSeek和Google的Gemini等模型正在追赶OpenAI的经验。在谈到最初的Copilot时，他表示：“我们犯了一个错误，那就是仅仅将其绑定在OpenAI模型上。”Althoff说，客户更关心数据与模型的结合，而不是任何特定的模型——他们需要随着技术水平的发展，能够快速切换模型的能力。

> “我们犯了一个错误，那就是仅仅将其绑定在OpenAI模型上。”

## 单一模型不再适用

考虑一个典型的客户服务应用程序，它可能需要总结支持工单、分析300页的合同、生成电子邮件、转录会议并审查源代码。这些任务并不完全相同。像Google的Gemini这样拥有百万级甚至更多token上下文窗口的模型，可能是处理合同的正确选择。而像OpenAI的GPT-5.4 mini或Anthropic的Claude Haiku这样的小型、快速模型可能以极低的成本处理工单摘要。转录任务可能会交给像Whisper这样的专用模型。如果监管机构要求客户数据必须保留在本地，那么像Meta的Llama或Mistral这样的开放权重模型通常是首选。

开发者不再选择单一的基础模型，而是越来越多地选择多种模型——由应用程序决定哪个模型处理每个请求。

## AI网关成为核心基础设施

模型只是堆栈中的一个组件，因此请求路由的决定必须在某个地方完成。这就是为什么开发者放弃将应用程序硬编码到单个模型中，而是构建可以在多个模型之间进行选择的系统。路由逻辑可能会针对一个请求优先考虑成本，针对另一个请求优先考虑速度，或者将敏感的工作负载保留在本地模型上。这样，如果某个提供商发生故障，流量可以在不改变应用程序本身的情况下路由到其他地方。

> 这家拥有业内最深厚单一模型合作关系的公司，现在正将“模型可替换性”作为产品进行销售。

## 这改变了开发者的构建方式

一旦公司不再依赖单一模型，挑战就转变为构建用于决定每个请求使用哪个模型的系统。

这意味着开发者需要工具来路由请求、比较模型性能、监控可靠性、控制成本、执行安全策略，并在某个模型宕机时切换到另一个模型。这是一个截然不同的工程问题，特别是因为“决定哪个模型响应请求”的过程发生在每次有人使用你的应用程序时。在企业规模下，这些决策每天发生数百万次，因此它们必须快速、可靠且易于管理。

## 生态系统已经在响应

像[LiteLLM](https://github.com/BerriAI/litellm)这样的开源代理和像[Portkey](https://portkey.ai/)这样的网关正在规范化各提供商之间的API。像[LangChain](https://www.langchain.com/)和[LangGraph](https://www.langchain.com/langgraph)这样的编排框架从一开始就假设存在多个模型。[模型上下文协议](https://modelcontextprotocol.io/)（MCP）正在使工具集成在不同模型间具有可移植性，而不是绑定到单一供应商。而云服务提供商本身——[Amazon Bedrock](https://aws.amazon.com/bedrock/), [Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-foundry), [Google Vertex AI](https://cloud.google.com/vertex-ai)——现在都在单个API后面展示了许多模型。

## 编排是新的护城河

核心模型将不断进步。但随着许多业务任务性能的趋同，编排成为了挑战。微软的公告表明，最大的供应商认为企业正朝着这个方向发展，并愿意投入数十亿美元来占据路由层。

> 企业不再将模型视为平台，而是将其视为编排层之后的可替换组件。

云时代教导开发者不要将应用程序与单一服务器绑定得太紧；容器化使基础设施具有可移植性。现在，同样的理念正被应用于AI。企业不再将模型视为平台，而是 consistently 将其视为编排层之后的可替换组件。