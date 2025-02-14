# 不是我父亲的中间件：如何通过 Agentic AI 提高生产力

![Featued image for: Not My Father’s Middleware: How To Be Productive With Agentic AI](https://cdn.thenewstack.io/media/2025/02/85d1a35f-how-to-be-productive-with-agentic-ai-1024x576.jpg)

我的父亲 Nick Humble，在 IBM 工作了很长时间。在 20 世纪 90 年代初，他参与了一个全新的面向消息的中间件 [IBM](https://www.ibm.com?utm_content=inline+mention) MQ Series（现在称为 [IBM MQ](https://www.ibm.com/products/mq)）的发布团队。它于 1993 年发布，立即引起轰动。

在 21 世纪初，我与一个团队合作，使用 MQ Series 作为基础，为一个主要的英国 High Street 银行实施互联网银行系统。它保证一次（且仅一次）的消息传递在所有方面都完美运行，从运行核心银行引擎的两台大型机到网站的 Windows 服务器集群。通过将网络和数据转换问题抽象到我们不再考虑它们的程度，中间件极大地简化了构建分布式系统的过程。

快进到今天，许多企业都在想知道在哪里以及如何才能很好地利用生成式 AI (GenAI) 背后的大型语言模型 (LLM)。

GenAI 已经找到早期产品市场契合点的两个领域是软件开发和营销。[Jonathan Eyler-Werve](https://www.linkedin.com/in/eylerwerve/) 是 Broadcom 旗下 Tanzu 的 AI/ML 开发者平台战略负责人，他认为存在第三个企业特定的用例。这将解决位于自然语言处理、人员和流程交叉点的一系列企业问题。

## 企业 AI：从推理到自主系统

Eyler-Werve 认为，推理（通过训练有素的 AI 模型运行实时数据以进行预测或解决任务的过程）将成为企业应用程序的常见组成部分。这些应用程序将不是由 AI 专家构建，而是由企业开发人员构建。

“我们将使用推理模型解决组织应用程序开发中的更多问题，”他在一次采访中告诉我。“许多传统应用程序将访问推理模型来解决问题，尤其是在数据融合和翻译方面。”

企业 AI 推理的出现需要各种优秀的 AI 编程框架，例如 [AutoGen](https://microsoft.github.io/autogen/dev//index.html)、[Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/) 或 [Spring AI](https://spring.io/projects/spring-ai)，这些框架为开发人员提供了一种快速迭代的方法。Eyler-Werve 建议，它还需要一种新型的面向 AI 的中间件，就像 MQ Series 为消息传递所做的那样，解决企业推理模型的一组[横切关注点](https://thenewstack.io/vmwares-golden-path/)，包括安全性、验证、成本控制和配置。

此外，他认为，通过解决这些问题，我们将从根本上简化企业[代理系统](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)的构建；这些系统具有目标导向的行为，并且可以采取自主行动来实现这些目标，同时根据新信息不断学习和适应。

为了理解原因，让我们退后一步，依次考虑每个横切关注点。

## 企业需要什么来构建 Agentic 系统？

随着企业在其应用程序中部署推理，[强大的安全性](https://roadmap.sh/cyber-security)和[管理控制](https://thenewstack.io/kubecon-keynotes-wrestle-with-ai-governance-complexities)成为必不可少的基础设施，上述四个关注点中的三个（安全性、验证和成本控制）构成了解决方案的一部分。

对于安全性，您需要一个审计跟踪，记录应用程序和 AI 模型正在做什么。您还需要一种管理 API 密钥的方法。Broadcom 的 Tanzu 部门的杰出软件工程师 [Adib Saikali](https://www.linkedin.com/in/adibsaikali/) 在一次采访中告诉我：“我们在这里的方法是 Tanzu AI Solutions 中的 AI 中间件为您提供一个 API 密钥。”“这意味着我们向应用程序分发唯一的密钥，因此如果 API 密钥泄漏，也没什么大不了的。”

他还建议，您还需要一种管理方法，以便您的开发人员只能使用他们应该使用的模型。“在 [Tanzu AI ](https://www.vmware.com/solutions/app-platform/ai)Solutions 中，我们提供可用于组成一组用于消费的模型端点，”Saikali 说。“因此，组织可能会定义一个个人银行端点，其中包含一组适合该端点的模型，并为资本市场提供一个单独的端点，其中包含一组不同的模型。”
与安全性密切相关的是验证，它是评估传递到模型和从模型传递的消息是否安全和适当的过程。它包括许多步骤，包括记录输出。

Eyler-Werve告诉我：“在某种程度上，我们会进行真正高质量的评估，以确定模型返回的信息是否准确。但是，为了使其具有成本效益，需要考虑大量的因素。例如，记录输出需要安全地进行，因为输出中包含各种信息。鉴于此，您应该避免让每个团队都实施自己的日志记录和记录系统。”

如果您使用的是专有模型，那么成本控制就显得尤为重要，因为调用它们可能会很快变得非常昂贵。Eyler-Werve认为这是一个属于中间件的跨领域问题。

Eyler-Werve告诉我：“供应商很乐意您使用他们内置的成本控制，但这不会奏效，因为他们也希望您增加成本。您也不想让您的开发团队实施成本控制，因为如果他们做得不正确，您可能会因为一行行为不端的代码在一夜之间产生巨额账单。”

Saikali说：“我们[Tanzu]目前提供三种解决方案来帮助进行成本控制。首先，我们可以让您看到应用程序的令牌消耗；其次，我们可以让您应用速率限制；第三，我们允许您轻松切换提供商，因此您可以为您的特定用例选择具有最佳性价比的提供商。”

组织解决模型消耗控制的另一种方法是提炼模型，以加快响应速度，并降低使用LLM进行推理的财务成本和不合理的高环境成本。提炼的基本过程是，您使用较大的模型捕获一组良好的结果，然后使用存储的补全来评估较大模型和较小模型的性能，以建立基线。然后，您可以使用存储的补全的子集作为训练数据来微调较小的模型，从而改善其结果，并将其与原始基准进行比较，直到这些结果令人满意为止。

[OpenAI](https://platform.openai.com/docs/guides/distillation)和[Amazon](https://aws.amazon.com/?utm_content=inline+mention) Bedrock都提供了执行提炼的方法。[AWS claims](https://aws.amazon.com/bedrock/model-distillation/)声称，[Amazon Bedrock](https://thenewstack.io/building-llm-based-genai-applications-with-amazon-bedrock/)中提炼的模型比原始模型快500%，成本降低75%。遗憾的是，关于碳成本的数据有限，但我们可以假设较低的价格也意味着排放量的减少。

## AI Agent需要什么？
第四个关注点，即配置，涵盖了模型本身及其依赖的资源。例如，假设您的程序收到一个CSV文件中的一些数据，但它无法处理。您可以将CSV交给LLM，看看它是否可以解决问题，如果可以，则进入验证步骤，而不是抛出一个错误消息。

在这种环境中，开发团队不训练模型。Eyler-Werve说：“他们需要能够配置一个模型，将其与测量输出所需的所有监控正确连接起来，并确保它的行为符合他们的期望。”

这反过来又需要某种方式将不同的企业资源暴露给应用程序，例如位于硬盘上的电子表格。然后，这些资源形成代理可以利用的一组工具。

[Anthropic’s Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)是构建此协议的第一个真实世界的尝试。Eyler-Werve告诉我：“这意味着我们可以开始在那些原本需要整个服务和REST API的东西周围放置非常薄且快速的包装器。我们可以在一天内完成，因此如果代理知道它在哪里，被允许与之通信并且具有所有必要的连接组织，则代理可以开始与之对话。”
除了访问权限之外，代理还需要内存，以便它们可以在长时间运行的对话中保持状态和上下文。[MemGPT](https://research.memgpt.ai)是可以执行此操作的模式的一个示例。

总而言之，这些LLM增强功能（检索、工具和内存）是代理系统的构建块。根据Eyler-Werve的说法，这意味着“如果您有一个[good platform](https://thenewstack.io/how-spring-and-java-shaped-internal-developer-platforms)，它知道如何配置运行时、存储和现在的推理，还可以告诉您哪些资源可用以及它们可以做什么工作，那么您可以开始以一种非常轻量级的方式将这些代理解决方案拼接在一起。”

## LLM擅长（和不擅长）什么？
使用 LLM 的一个重大挑战是它们会编造内容。例如，一个基准测试竞赛（由 Meta 组织，基于检索增强生成 [RAG] 和复杂情况）的[获胜方案](https://arxiv.org/pdf/2410.00005) [大约有一半的时间是错误的](https://www.aicrowd.com/challenges/meta-comprehensive-rag-benchmark-kdd-cup-2024/problems/meta-kdd-cup-24-crag-knowledge-graph-and-web-retrieval/leaderboards)。这些发现与新闻和信息网站评级系统 NewsGuard 的发现类似，后者显示，10 个领先的聊天机器人 [40% 的时间会做出虚假声明](https://www.newsguardtech.com/wp-content/uploads/2025/01/December2024AIMisinformationMonitor.pdf)，并且对 22% 的问题没有给出答案。使用 RAG 和[各种其他技术可以提供帮助](https://www.nature.com/articles/d41586-025-00068-5)，但完全消除错误似乎是不可能的。

鉴于此，利用 LLM 的关键是让它们保持在最佳状态，即理解，而不是生成输出。“ChatGPT 的消费者使用是最薄弱的，”Eyler-Werve 告诉我们。“ChatGPT 的大部分世界都是基于吐出 600 个单词，其中 200 个是编造的。有了代理，我们又回到了它们最擅长的领域，即理解事物并做出最佳猜测决策。”

Eyler-Werve 还认为，LLM 的进展可能会停滞。“LLM 将在一段时间内保持现状，因为我们已经对所有可以训练的内容进行了训练。因此，虽然它们在调用函数等特定方面会变得更好，但 LLM 本身将达到瓶颈。这意味着围绕核心模型包装规则是您更快获得价值的方式。”

如果他是对的，这将意味着竞赛将不是谁拥有最好的 LLM，而是你如何以具有成本效益的方式使用它，以及你如何快速地将所有这些企业资源暴露给推理模型。

构建 AI 驱动的应用程序需要一个通用的架构，可以有效地桥接传统逻辑和 AI 驱动的逻辑。随着应用程序变得越来越复杂，这一挑战也会增加——AI 系统的不确定性意味着，更多地使用代理自主性会带来对保护措施的迫切需求。这些护栏，包括内容安全协议、使用限制和审计跟踪，在开发具有高度独立性的代理应用程序时变得尤为重要。

同样值得一提的是，有效利用 AI 需要快速迭代、实验和学习哪些有效和哪些无效的能力。在这种背景下，值得注意的是，[具有实验心态的组织](https://blog.container-solutions.com/why-run-thousands-of-failed-experiments) 并且采用了现代的、云原生的和微服务模式和架构的组织，能够很好地采用代理模型。这是一个很好的例子，说明了那些经历了所谓的“数字化转型”的公司和团队如何使自己适应未来，从而利用像代理 AI 这样的创新。

对于希望探索实际实现的读者，Anthropic 最近的[文章](https://www.anthropic.com/research/building-effective-agents) 展示了一套用于构建 LLM 代理的基础模式，并附带相应的 [cookbook](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)。在 Spring Source 博客上，Christian Tzolov 提供了一组具有相同基本模式的 [Spring AI 实现](https://spring.io/blog/2025/01/21/spring-ai-agentic-patterns)。

*有关 Tanzu AI Solutions 中包含的 AI 中间件功能的更多信息，请阅读最新的 Tanzu Platform 博客文章，什么是 AI 中间件，以及为什么你需要它来安全地大规模交付 AI 应用程序。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。