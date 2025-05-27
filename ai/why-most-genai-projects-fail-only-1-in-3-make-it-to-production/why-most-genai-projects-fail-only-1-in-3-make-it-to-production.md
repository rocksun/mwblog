
<!--
title: 为什么大多数 GenAI 项目会失败：只有三分之一能投入生产
cover: https://cdn.thenewstack.io/media/2025/05/23631ba9-seo-galaxy-yushnkbhf3q-unsplash-scaled.jpg
summary: GenAI项目落地难？数据安全成最大绊脚石！超80%企业拥抱GenAI，但仅1/3投产。数据泄露风险高，需重视LLM访问控制和RAG架构安全。授权即服务（Authorization-as-a-Service）成关键，Oso Cloud助力构建安全AI应用，Productboard案例佐证。
-->

GenAI项目落地难？数据安全成最大绊脚石！超80%企业拥抱GenAI，但仅1/3投产。数据泄露风险高，需重视LLM访问控制和RAG架构安全。授权即服务（Authorization-as-a-Service）成关键，Oso Cloud助力构建安全AI应用，Productboard案例佐证。

> 译自：[Why Most GenAI Projects Fail: Only 1 in 3 Make It to Production](https://thenewstack.io/why-most-genai-projects-fail-only-1-in-3-make-it-to-production/)
> 
> 作者：Mat Keep

人工智能正在经历科技史上最快的企业采用曲线——使用量激增，预算成倍增长，用例从生成式人工智能 (GenAI) 扩展到完全自主的、代理系统。但有一个问题：大多数 AI 应用程序永远无法投入生产。

主要问题不是模型性能、基础设施，甚至不是成本，而是数据。具体来说，[数据安全和隐私](https://thenewstack.io/building-privacy-aware-ai-software-with-vector-databases/)被反复提及为阻碍因素。如果没有强大、动态的访问控制，GenAI 系统[可能会泄露敏感数据并引入安全](https://thenewstack.io/flaw-in-r-creates-supply-chain-security-risks/)漏洞，从而可能导致声誉损害、竞争损失和法律风险。

本文探讨了 GenAI 的兴起、为什么这么多举措停滞不前，以及[授权即服务](https://www.osohq.com/cloud/authorization-service)如何帮助工程团队更快地交付 AI 应用程序，同时又不影响安全或控制。

## 史上最快的增长？GenAI 的速度、转变和支出数据

斯坦福大学的 [2025 年 AI 指数](https://hai.stanford.edu/ai-index/2025-ai-index-report) 显示，采用速度正在加快，2024 年有 78% 的组织使用 AI，高于前一年的 55%。Nutanix 的 [2025 年企业云指数](https://www.nutanix.com/enterprise-cloud-index) 发现，超过 80% 的组织已经实施了 GenAI 战略。

采用率与投资相匹配。Menlo Ventures 报告称，[企业 GenAI 支出](https://menlovc.com/2024-the-state-of-generative-ai-in-the-enterprise/)在 2024 年比前 12 个月增长了 6 倍。支出占 IT 总预算的比例只会增加：

- 波士顿咨询集团
[预测 GenAI 预算](https://www.bcg.com/publications/2024/it-spending-pulse-as-genai-investment-grows-other-it-projects-get-squeezed)在未来三年内增长 60%。[Gartner 预测](https://www.gartner.com/en/articles/2025-trends-for-tech-ceos)2023 年至 2027 年间，企业在 AI 上的支出将达到 3 万亿美元。其研究还预测，“*在未来几年内，买方组织在具有 GenAI 功能的软件上的支出将超过在没有 GenAI 功能的软件上的支出。*”
将这些预测放在上下文中来看，在 OpenAI 于 2022 年 11 月发布 ChatGPT 作为研究预览版之前，很少有企业听说过 GenAI，更不用说为其分配预算了。

## 当 AI 停止提问并开始行动时会发生什么？

如今，GenAI 的三大用例集中在内容创建、客户或员工支持自动化以及软件工程上。然而，正如 __CIO.com__ [所述](https://www.cio.com/article/3478721/top-7-generative-ai-use-cases-for-business.html)，这些只是“冰山一角”。

在 GenAI 的基础上，我们现在看到对代理 AI 的大量关注——基于 LLM 的自主系统，能够做出决策和执行任务，而无需持续的人工监督。代理 AI 的概念超越了传统的严格自动化，它使系统能够理解上下文、适应新信息和外部事件，通常（但现在并非总是）与“人在回路中”协作以解决复杂的挑战。考虑自动化业务工作流程，例如供应链管理、法律发现、会计报表、工程和设计项目、研究与战略规划等等。

随着模型复杂性的提高和特定领域的 LLM 变得更容易访问，曾经是人类认知和问题解决专属领域的活动正在被机器增强（和颠覆？）。考虑一下前面引用的斯坦福大学的研究。它发现：

- 仅在 12 个月内，针对人类表现进行基准测试的模型性能提高了高达 67%。
- 与此同时，成本正在暴跌，推理成本（通常是 AI 中最昂贵的部分）在短短两年内下降了 280 倍。如今，摩尔定律似乎“古色古香”。
我们可以从所有这些中得出的明显结论是，随着 LLM 变得更加强大且成本下降，AI 的用例的丰富性和广度只会扩大。

## 为什么 GenAI 项目未能投入生产？

采用率正在增长，用例正在扩展，资金正在流动。

可观测性对于在生产中运行的 AI 应用程序至关重要。
那么，根据 [Informatica 最近的一项调查](https://www.itpro.com/technology/artificial-intelligence/only-a-handful-of-generative-ai-projects-make-it-into-production-heres-why)，为什么只有 38% 的 AI 项目最终投入生产？[Dataiku 的一项调查](https://www.bigdatawire.com/2024/08/30/genai-adoption-by-the-numbers-2/)描绘了一幅更加黯淡的景象，目前只有 20% 的企业开发的 GenAI 应用程序投入生产。[Gartner 预测](https://www.bigdatawire.com/this-just-in/gartner-predicts-30-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025/)，到 2025 年底，30% 的 GenAI 项目将在概念验证后被放弃。

这是为什么呢？在多项调查中，我们看到了类似的结论——一切都与数据有关：

*   Nutanix 的调查发现，数据隐私和安全是 GenAI 实施中与数据相关的最重要方面。95% 的受访者表示隐私是首要任务，同样比例的人承认他们的组织可以采取更多措施来保护 GenAI 模型和应用程序。
*   [YouGov 为 BigID 开展的一项调查](https://www.agilitypr.com/pr-news/pr-tech-ai/the-top-generative-ai-concern-for-the-remainder-of-2024-is-data-security-risk-say-decision-makers-what-companies-can-do-to-protect-data/)发现，超过三分之二的组织将数据安全风险列为他们最关心的 AI 问题，50% 的组织认为这是实施过程中的最大挑战。
*   Dataiku 研究中 77% 的受访者认为，他们对 AI 的最大担忧是缺乏治理和使用控制。

在任何新技术采用浪潮的早期阶段，围绕安全和隐私的担忧通常被证明是过分的，或者可以通过新的控制和设计模式来缓解。但 Gen AI 并非如此。事实恰恰相反。随着越来越多的项目接近生产就绪，对数据隐私的担忧正在增加。[Deloitte 的一份报告](https://www.techrepublic.com/article/genai-data-privacy-concern-deloitte/)发现，2023 年只有 22% 的技术专业人士将其列为他们最关心的三个问题之一。2024 年，这一数字增加了两倍多，达到 72%。

## 当 AI 知道的太多以及 AI 堆栈中的隐藏威胁

让我们明确一点，对 AI 中[数据安全](https://thenewstack.io/how-to-put-guardrails-around-containerized-llms-on-kubernetes/)和隐私的担忧并非假设。2023 年初，三星在一名工程师无意中通过提示提交[泄露了敏感的内部源代码](https://thenewstack.io/twitters-source-code-leak-adds-to-elon-musks-social-media-mess/)后，禁止了 ChatGPT。这并非孤立的案例——BigID 报告称，近 50% 的组织已经经历了 AI 使用带来的不利业务结果，包括数据泄露。

当数据访问未得到正确控制时，LLM 会带来真正的风险。[在内部数据上训练和调整的模型](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/)或在检索增强生成 (RAG) 工作流程中使用的模型可能会在其输出中暴露个人身份信息 (PII)、知识产权 (IP) 或机密见解。这在面向客户的应用程序或模型可以访问敏感或受监管数据的内部工具中尤其令人担忧。AI 聊天机器人可能会无意中显示内部记录、合同、定价或支持历史记录。企业搜索工具可能会向未经授权的用户泄露财务或战略计划。

在软件工程中，风险被放大。AI 编码助手可能会泄露专有代码或引入漏洞——尤其是在它们跨会话保留上下文或缺乏适当的沙盒的情况下。在某些情况下，对抗性提示可能会故意提取敏感内容，从而将有用的工具变成潜在的漏洞载体。

后果是严重的：监管处罚、竞争风险、声誉损害和法律风险。

只有通过实施强大的 [LLM 访问控制](https://www.osohq.com/llm-access-control)、安全的模型架构和严格的数据治理策略，企业才能成功地提高 AI 应用程序的生产率。

## 解决权限问题并释放 AI 潜力

授权是任何软件应用程序的基础——它控制谁可以访问哪些数据、执行特定操作以及与系统的不同部分进行交互，使其对于功能和安全性都至关重要。

在 GenAI 和代理 AI 系统中，风险甚至更高。这些应用程序通常自主运行，与敏感数据交互并触发下游操作。这使得细粒度的动态授权对于防止意外行为、数据泄露或恶意滥用至关重要。

*   “我不想成为导致数据泄露的人。”
*   “我以为我正在实施 RAG，而不是开发授权系统。”
*   “如果我无法将我的 LLM 连接到我的客户数据，就不会有人使用我的聊天机器人。”
“我的安全团队阻止我将我的 Agentic AI 应用投入生产。”

在 [Oso](https://www.osohq.com/)，我们听到许多工程团队都表达了上述担忧。当他们努力构建 LLM 访问控制时，一个挑战始终突出：确保生成式和 Agentic AI 应用仅与有权查看信息的用户共享信息。

作为帮助每个人开发 AI 应用的实用指南，我们整理了[一个教程，逐步介绍如何使用 Oso Cloud 构建授权的 LLM 聊天机器人](https://www.osohq.com/post/building-an-authorized-rag-chatbot-with-oso-cloud)。它指导工程师将细粒度的授权集成到使用内部文档作为上下文的聊天机器人中，确保用户只能访问他们可以查看的信息。

本教程涵盖了设置向量数据库、使用 OpenAI 生成嵌入和响应以及使用 Oso Cloud 强制执行访问控制。随附一个包含工作代码的完整演示应用程序，工程师可以克隆该存储库并立即开始构建自己的安全、上下文感知的聊天机器人。

![](https://cdn.thenewstack.io/media/2025/05/e7a68071-image1.png)

*图 1：Agentic AI 应用中典型 RAG 架构中的数据流*

## 从缓慢的授权到流畅的授权

Productboard 是一个以客户为中心的[产品管理平台](https://thenewstack.io/a-platform-team-product-manager-determines-devops-success/)，使组织能够更快地将正确的产品推向市场。当它从为中小型企业提供服务扩展到与大型企业互动时，Productboard 遇到了授权挑战。

该公司转而向 Oso 寻求帮助，以满足新的企业需求，例如更精细和可定制的访问控制、字段级权限以及跨复杂、嵌套数据结构管理访问。此外，随着公司转向微服务架构，Oso 简化了在分布式系统中一致地强制执行权限的方式。Productboard 与 Oso 合作，通过迁移、策略设计和 AI 集成获得专家支持。

当 Productboard 通过其新的 [Productboard Pulse](https://www.productboard.com/product/voice-of-customer/) 平台引入 AI 驱动的功能时，拥有强大的授权基础被证明至关重要。

Productboard Pulse 将来自支持、CRM 和分析等工具的客户反馈聚合到一个统一的视图中，允许团队通过自然语言查询来呈现见解。它使用检索增强生成 (RAG) 架构来使用上下文数据丰富 LLM 提示，但仅限于每个用户有权查看的数据。Oso 在此工作流程中发挥着核心作用，强制执行细粒度的动态访问控制，以确保敏感反馈仅可供正确的用户访问。通过利用 Oso，Productboard 加速了开发，避免了权限逻辑的昂贵重新实现，并确保了跨分布式数据源的安全、可扩展的访问，使他们能够快速而自信地交付 AI 功能。

正如该公司该项目的首席工程师之一所说：

> “Oso 使构建 Productboard Pulse 变得更快，因为每个 API 都可以直接调用 Oso 来确定允许什么，无论数据位于何处。通过在经过验证的授权基础上构建，我们避免了许多公司在 AI 方面遇到的最大障碍。”

您可以阅读完整的 [Productboard 和 Oso 案例研究](https://www.osohq.com/customers/productboard)以了解更多信息。

## 我们何去何从？

AI 浪潮已经到来，并且发展迅速。但是，将这种势头转化为真正的商业价值取决于模型和 GPU 之外的因素。如果没有细粒度、灵活的授权，AI 项目将在概念验证阶段停滞不前，或者更糟糕的是，使您的组织面临数据泄露、安全风险和合规性失败的风险。请记住考虑授权即服务解决方案，以帮助消除访问控制作为交付 AI 应用的障碍。