<!--
title: Pulumi推出GenAI堆栈模板:首批支持Pinecone和LangChain
cover: https://cdn.thenewstack.io/media/2024/02/1a6e838f-pulumi-1024x578.jpg
-->

缺乏运维经验的AI专业人员，可以用Python或其他编程语言来定义和编排ML堆栈。

> 译自 [Pulumi Templates for GenAI Stacks: Pinecone， LangChain First](https://thenewstack.io/pulumi-templates-for-genai-stacks-pinecone-langchain-first/)，作者 Joab Jackson。Joab Jackson 是 The New Stack 的高级编辑，负责报道云原生计算和系统操作。他报道 IT 基础设施和开发 25 年以上，包括在 IDG 和 Government Computer News 任职。

要搭建一个[生成式 AI 应用程序](https://thenewstack.io/with-chatgpt-honeycomb-users-simply-say-what-theyre-looking-for/)，通常需要至少两个起步组件，一个大型语言模型(LLM)和一个向量数据存储。您可能还需要一些前端组件，例如聊天机器人。 

[进入 GenAI 领域的](https://thenewstack.io/serverless-computing-in-2024-genai-influence-security-5g/)组织现在面临着 GenAI 的编排挑战。他们发现将这些组件从开发人员的笔记本电脑移动到生产环境中可能会导致错误并且时间消耗巨大。

为了简化部署，[基础设施即代码](https://thenewstack.io/infrastructure-as-code/)(IaC)软件提供商 [Pulumi](https://www.pulumi.com/?utm_content=inline-mention) 引入了两个基本 GenAI 工具的“提供程序”或模板，即 [Pinecone 向量数据库](https://thenewstack.io/vector-databases-are-having-a-moment-a-chat-with-pinecone/)和用于构建 LLM 的 [LangChain 框架](https://thenewstack.io/building-gpt-applications-on-open-source-stack-langchain/)。

“我们发现很多像 LangChain 这样的工具对于本地开发来说非常棒。但是当您想投入生产时，它仍然是一个 DIY 练习，”Pulumi 的首席执行官兼联合创始人 [Joe Duffy](https://www.linkedin.com/in/joejduffy/) 在接受 TNS 采访时说。“这非常具有挑战性，因为您希望对无限规模进行架构，以便随着对应用程序的成功，您能够扩展以满足需求。这并不容易做到。”

具体来说，Pulumi [支持](https://www.pulumi.com/solutions/ai-arch/) AWS 上在 1 月份发布的 [Pinecone](https://www.pinecone.io/learn/vector-embeddings-for-developers/) 的无服务器版本，LangChain 的支持是通过在 [Amazon ECS 集群](https://www.pinecone.io/blog/serverless/)上设置 [LangServe](https://www.langchain.com/langserve) 作为服务来实现的。”

这两个模板加入了一个[组合](https://www.pulumi.com/templates/)，该组合涵盖了 150 多个云和 SaaS 服务提供商，包括 GenAI 空间中使用的许多其他服务，如用于前端的 [Vercel Next.js](https://thenewstack.io/vercels-next-js-14-introduces-partial-pre-rendering/) 和 [Apache Spark](https://thenewstack.io/apple-comet-brings-fast-vector-processing-to-apache-spark/)。

除了模板本身之外，Pulumi还制定了一组使用Pinecone和LangChain的参考架构。

![缩放](https://cdn.thenewstack.io/media/2024/02/e0db1543-pulumi-pinecone.png)

## 如何使用IaC构建GenAI堆栈

这个想法是，可能没有运维经验的AI专业人员可以使用Pulumi以Python或其他语言[定义和编排ML堆栈](https://www.pulumi.com/solutions/ai/)。

作为IaC解决方案，Pulumi提供了一种声明式地定义基础设施的方法。与其他IaC方法不同，Pulumi允许开发人员使用多种编程语言(如Python、Go、Java和TypeScript)之一来构建环境。

然后[部署引擎](https://www.pulumi.com/docs/concepts/how-pulumi-works/)设置定义的环境，甚至检查以确保操作状态与定义状态保持同步。

Duffy说，AI Gen参考架构的设计遵循了最佳实践。 “很多挑战是如何使其可扩展，跨区域和跨子网可扩展，以及跨网络。所以这个蓝图是为可配置的规模而构建的。”

这不是Pulumi第一次尝试管理AI基础设施。该公司已经为[AWS SageMaker](https://www.pulumi.com/registry/packages/aws/api-docs/sagemaker/)和Microsoft的[OpenAI Azure](https://www.pulumi.com/registry/packages/azure-native/api-docs/elastic/openai/)服务开发了模块。还有一个在Docker、Azure或Runpod上部署来自[Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/)的LLM的[蓝图](https://github.com/pulumiverse/katwalk)。

当然，公司计划进一步扩大未来的名单。

“我们看到Pulumi用于这些AI工作负载的采用率很高，”Duffy说。

![缩放](https://cdn.thenewstack.io/media/2024/02/9bed338b-pulumi-langchain.png)
