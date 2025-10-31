部署AI驱动的应用程序不仅仅是调用模型。开发者必须处理推理基础设施、版本化数据管道并集成外部工具，同时还要找到方法来监控或管理更可能出现幻觉的输出。当团队试图超越基本原型时，他们突然被迫在编排、合规性和AI架构方面发展专业知识。

随着AI能力在各种模态（例如：文本到图像到音频）中爆发式增长，开发者体验却未能跟上步伐。团队正在将跨云提供商、[大型语言模型 (LLM)](https://thenewstack.io/introduction-to-llms) API、向量数据库和脆弱的控制循环的解决方案拼凑在一起。即使是拥有强大工程实力的公司也难以保持开发速度。

缺少的是一种平台级解决方案，它能像传统[平台即服务 (PaaS)](https://thenewstack.io/return-to-paas-building-the-platform-of-our-dreams/) 抽象基础设施一样，抽象这些AI相关的关注点。

这正是[AI平台即服务](https://www.heroku.com/blog/introducing-the-heroku-ai-platform-as-a-service/) (AI PaaS) 旨在填补的空白。它将PaaS的简洁性、可扩展性和开发者优先工具的核心原则带入现代AI构建模块。

让我们探讨一下什么是AI PaaS，以及它如何让您无需重新发明整个技术栈即可交付生产级的AI应用程序。

## 什么是AI PaaS以及为何它是必需的？

AI PaaS正如其名：它是一个平台，帮助开发者在云端构建、部署和运行AI驱动的应用程序，而无需自行管理模型、编排、管道或基础设施。它建立在传统PaaS的基础上，但通过模型访问、检索管道、代理编排和评估工具等AI原生功能对其进行了扩展。

这些平台填补了一个关键空白，因为许多AI项目从未投入生产。Gartner预测，到2027年，多达[40%的代理AI计划将失败](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)，这通常是由于集成成本、缺乏可观测性或部署复杂性。AI PaaS通过提供有主见且可扩展的默认设置来应对这些挑战。

那么AI PaaS由什么构成？你从PaaS的基础开始，然后添加AI特定的功能。

## 现代PaaS的核心基础

无论是构建CRUD应用还是对话代理，每个PaaS都需要做好几件核心事情。它们是：

*   **可扩展性**：基础设施可以轻松扩展，以处理计算密集型AI工作负载的变化。
*   **安全性**：所有租户都通过适当的访问控制进行隔离，以确保模型、数据和代理保持安全。密钥都遵循最小权限原则并得到安全管理。
*   **容器化：** 代理和工具都在容器中，以实现一致的部署。
*   **编排：** 无需手动配置基础设施。代码自动构建和部署。
*   **数据**：数据库自动配置、可扩展并提供安全访问。这可能意味着向量数据库、客户数据或AI所需的任何其他内容。
*   **可观测性**：延迟、使用模式和错误管理通过OpenTelemetry或类似工具可见。AI工作流也需要在提示流和结果中具有可观测性，以便调试LLM结果。

这些是基本要求。但使用AI进行构建会引入一层新的复杂性。让我们看看AI PaaS所需的特定功能。

## **最小可行AI PaaS的基本功能**

要开始构建AI PaaS，所需的最少工具包括模型推理、检索管道和[模型上下文协议 (MCP)](https://thenewstack.io/mcp-a-practical-security-blueprint-for-developers) 脚手架。

### AI模型和推理选项

AI驱动的功能以LLM为中心。LLM提供对话式生成AI，自2022年ChatGPT发布以来已变得普遍。AI PaaS应提供对各种机器学习 (ML) 模型的无缝访问。所有模型都有不同的优缺点，因此访问多个模型为构建AI代理的团队提供了最大的灵活性。

这种多样性还可以用于降低成本，其中一些服务需要复杂（且昂贵）的模型，而复杂度较低的服务可以使用更小、更便宜的模型。

### AI质量和可靠性的控制循环

当LLM提供响应时，应建立一个控制循环来监控响应并验证其质量。开发者可以创建客户定义的启发式和规则，用于评估响应。这可能涉及硬编码的防护措施，或者比较多个LLM的结果以达成共识。

如果响应不符合质量标准，查询可能会被重新表述并再次查询。如果响应通过评估，控制循环将把响应传递给模型的下一步。

[![一个闭环通过将输入发送到循环中以产生输出，然后将输出作为输入返回，从而监控响应。](https://cdn.thenewstack.io/media/2025/10/147e489f-closed-loop.png)](https://cdn.thenewstack.io/media/2025/10/147e489f-closed-loop.png)

闭环如何监控响应。

### 连接数据和工具的模型上下文协议

LLM是强大的工具，可以与用户就许多不同的话题进行对话。为了支持对组织有用的生成式AI，必须不断提供额外数据，以确保及时准确的响应。

MCP是一种标准化方法，用于将外部工具连接到AI系统，以提供额外的数据或知识。MCP服务器使得安全地连接现有数据工具（内部和外部）以整合新数据变得容易。

MCP可以提供与API的连接，用于频繁变化的数据（“纽约皇后区目前的交通状况如何？”），或与包含企业数据的数据库的连接（“2021年第二季度签署了多少笔交易？”）。这些数据存储支持并增强了模型的输出。

此外，MCP还充当服务目录。当查询发送到AI时，它会根据了解数据位于*何处*以及如何检索并格式化为响应来构建其响应。这允许现有应用程序和代理连接到MCP。

[![MCP处理来自应用程序和LLM的请求，然后从外部源馈送数据。](https://cdn.thenewstack.io/media/2025/10/b194fdaa-mcp-request-processing.png)](https://cdn.thenewstack.io/media/2025/10/b194fdaa-mcp-request-processing.png)

MCP处理来自应用程序和大型语言模型的请求，然后从外部源馈送数据。（来源：[Heroku](https://www.heroku.com/ai/mcp-on-heroku/)）

MCP还可以用于将AI应用程序作为工具暴露给其他[代理系统](https://thenewstack.io/beyond-ai-models-data-platform-requirements-for-agentic-ai)使用，允许其他代理使用AI系统完成任务。

例如，[Audata](https://www.heroku.com/customers/audata/)构建了Aura（一个AI支持代理），利用Heroku Postgres的实时数据和来自[Salesforce Agentforce](https://thenewstack.io/avoiding-the-ai-agent-reliability-tax-a-developers-guide/)的企业数据来回答日常问题。如果案件升级到支持团队，则会向代表提供现有聊天的概要，从而加快工单解决速度。

## 企业级AI PaaS的期望

一个可靠的AI PaaS不仅仅是推理。它帮助团队负责任地构建、快速迭代并自信地扩展。以下是您可以从支持长期、生产级AI使用的平台中期望的功能：

### 检索增强生成

一种常用的外部知识数据存储工具是[检索增强生成 (RAG)](https://thenewstack.io/no-mcp-hasnt-killed-rag-in-fact-theyre-complementary)。RAG数据库通常是一个向量数据库，包含专门编码用于快速与LLM交互的企业数据。例如，Heroku的[Postgres pgvector](https://www.heroku.com/ai/pgvector-for-heroku-postgres/)提供了无缝的向量数据库支持，无需额外的数据库工具。

当向AI模型发出查询时，LLM会提供数据库中的相关数据来构建响应。RAG架构允许组织插入定制数据来影响LLM的响应。

例如，[1West](https://www.heroku.com/customers/1west/)的贷款处理和审批是一个缓慢的手动过程。在使用Heroku的AI PaaS训练一个机器学习模型以处理大量数据源后，贷款处理时间从几天缩短到几分钟。

[![简化的RAG架构，包括用于上下文数据的数据管道。](https://cdn.thenewstack.io/media/2025/10/8658946b-rag-architecture-model-heroku.png)](https://cdn.thenewstack.io/media/2025/10/8658946b-rag-architecture-model-heroku.png)

简化的RAG架构，包括用于上下文数据的数据管道。

### 用于更新RAG数据库的RAG数据管道

正如LLM本身可能很快过时并提供不正确或陈旧的响应一样，RAG数据库中的数据也可能发生同样的情况。为了保持AI应用程序的准确性，RAG数据库必须不断刷新以反映新的或变化的数据。这需要自动化文档处理工作流。这些工作流应与现有系统无缝集成，并高效处理所有处理步骤。

例如，在Heroku生态系统中，[Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler)可以定期运行工作流以访问文档并将处理后的数据插入到pgvector数据库中。所有处理都在安全环境中进行，保护企业数据。

## Heroku如何提供全面的AI PaaS

随着公司将AI驱动的工具集成到其技术栈中，许多开发团队缺乏在生产环境中部署AI所需的MLOps、治理和编排技能。使用Heroku的AI PaaS可以启动构建、部署、操作和扩展AI驱动应用程序的过程。

借鉴Heroku在构建云架构方面的经验和开发者优先方法意味着企业团队可以专注于构建服务，而不是管理服务器、网络、安全和构建编排工具。

[Heroku 氛围编程](https://vibes.heroku.com/new)AI代码生成允许您使用自然语言创建并部署到Heroku。Heroku的[托管推理和代理](https://elements.heroku.com/addons/heroku-inference)提供了精选的AI模型供您构建。Heroku的[MCP服务器](https://www.heroku.com/blog/introducing-official-heroku-mcp-server/)使得代理能够轻松访问Heroku资源，如日志、配置附加组件和扩展应用程序。部署在Heroku上的自定义MCP服务器可以为您的AI服务提供对现有系统的访问权限。

*   LLM支持由[Heroku托管推理和代理](https://elements.heroku.com/addons/heroku-inference)提供，可访问多个LLM推理模型。
*   [Heroku AppLink](https://devcenter.heroku.com/articles/heroku-applink)提供与Agentforce（[Salesforce](https://www.salesforce.com/?utm_content=inline+mention)平台的代理层）的安全连接，并与Salesforce Flows、Apex和[Data Cloud](https://www.salesforce.com/data/?utm_content=inline+mention)连接。
*   Heroku的[AI原生工具](https://devcenter.heroku.com/articles/heroku-inference-tools)集成使开发者能够构建新应用、增强现有应用并使用AI生成的代码创建新的AI代理。这意味着运行在Heroku上的AI代理可以安全地与敏感企业数据交互，利用最先进的AI同时确保您的数据安全。

## 赋能下一代AI开发者

部署AI应用应该像推送Web应用一样简单。凭借有主见的默认设置和托管服务，Heroku持续与开发者共同发展，提供流线型、集成的平台体验。

Heroku正将其数十年的[云端应用部署专业知识](https://www.heroku.com/heroku-gartner-magic-quadrant/)带入，以帮助开发者快速推出AI技术。要了解更多关于Heroku和AI PaaS的信息，请在[YouTube](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DQIwuBKysmxA&sa=D&source=docs&ust=1761762691618176&usg=AOvVaw2O8xHRsw-78JPt9j5a0FRo)上观看演示或在[LinkedIn](https://www.linkedin.com/company/heroku/posts/?feedView=all)上关注更新。

YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等内容。

[订阅](https://youtube.com/thenewstack?sub_confirmation=1)

由Sketch创建的分组。

[![]()

Doug是一名终身学习者和教育家，职业生涯致力于提升开发者知识和经验。作为Google Web开发者专家、O’Reilly作者、国际主题演讲者和多产博主，他乐于将复杂事物简单化。当...

[阅读Doug Sillars的更多文章](https://thenewstack.io/author/doug-sillars/)