### Spring AI 改变 Java 以实现 GenAI 应用程序交付

![Spring AI 改变 Java 以实现 GenAI 应用程序交付的特色图片](https://cdn.thenewstack.io/media/2024/09/1e509293-spring-ai-transforms-java-genai-app-1024x576.jpg)

机器学习 (ML) 和 AI 不再是新事物，但生成式 AI (GenAI)——使用 [大型语言模型](https://thenewstack.io/llm/) (LLM) 生成图像、文本、音乐和其他媒体——在过去 18 个月中引起了相当大的关注，吸引了商业领袖和公众的想象力。

在大量语料库上训练的这些模型在给定一个简单提示时生成图像、音乐、文章和其他文本。虽然结果很少像熟练的内容创作者或艺术家制作的那样精致或创新，但它们使初学者或非艺术家能够以惊人的速度生成媒体。

## 使用 AI 创建新产品和功能

将 GenAI 模型纳入应用程序开启了开发新软件产品功能的可能性，而这些功能以前由于实用性或成本限制而无法实现。常见的用例包括在内部文档之上构建问答和聊天系统，以及在漏斗顶部的销售或招聘线索之上启用自动预审。

当我担任 InfoQ 的主编时，我们发布了大量视频——每周约 20 个——这些视频是在一些世界领先的技术会议上录制的。然而，该视频内容不可搜索，这使得网站访问者难以找到相关资料。

我考虑过创建转录本的可能性，但人工转录的成本过高，而且 ML 转录不够准确，无法使用。

四年后，随着新一代 ML 转录的到来，格局发生了变化。尽管我们仍然需要人工审阅员才能将转录本达到可发布的质量，但 ML 足够准确，我们可以以大幅降低的成本做到这一点。在这次初步尝试之后，我们能够将相同的技术扩展到新的用例，包括为我们的会议生成各种新产品创意。

## 没有 Python 的 AI？Spring AI 说“没问题”

AI/ML 也已深入渗透到软件开发领域。根据 [Docker](https://www.docker.com/?utm_content=inline+mention) 的 2024 年 [“应用程序开发状况报告”](https://www.docker.com/resources/2024-state-of-application-development-report/?key=9ae0f193aaebbedebf3bb383d50a723dcba4a1afec6b8ca3a01decf04e253b57)，64% 的受访者使用 AI 来执行编写代码、文档和研究等任务，46% 的人在某种程度上从事 ML 工作。GitHub Copilot 和 JetBrains AI 等工具允许自动编写代码，有效地充当计算机配对程序员。

对于从事生成式 AI 项目的开发人员，OpenAI 和 Mistral AI 等提供商通过 REST API 提供对 LLM 集合的访问。只要您拥有授予对这些 API 访问权限的 API 密钥，您就可以使用几乎任何 HTTP 客户端向模型提交提示，包括久经考验的命令行备用 curl。但是，如果您正在构建具有相对复杂交互的功能，则客户端抽象会使这项工作变得更加容易。

尽管 AI 历史悠久，[Java](https://thenewstack.io/java/) 在该领域的应用相对较小。对于使用数据科学最爱的 [Python](https://thenewstack.io/python/) 的开发人员来说，有很多 [功能强大的库和框架](https://winder.ai/comparison-open-source-llm-frameworks-pipelining/)，例如 [LangChain](https://docs.langchain.com/docs/) 和 [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/getting_started/concepts.html)。

但面向企业 [Java 开发人员](https://roadmap.sh/java) 的选择直到最近才出现。其中包括 [Spring AI](https://spring.io/projects/spring-ai)，它于去年 11 月宣布，并正在走向一般可用性 (GA)，但已经对其当前状态进行了评估并用于生产应用程序。

对于许多企业来说，这一点很重要。“许多客户都是从精通 Python 并用它构建前几个应用程序的专家开始他们的 AI 之旅；但在 Java 是获得生产批准的途径的情况下，如果他们使用 Python，他们将陷入许多新的管理或异常流程，” [Adib Saikali](https://www.linkedin.com/in/adibsaikali/) 说，他是 Broadcom 的杰出软件工程师。

他告诉 The New Stack：“这些客户说，‘我们希望在我们的组织中扩展 AI。我们有数千名 Java 开发人员，我们希望使用熟悉的工具，这样我们就不必重新培训。’”

此外，在企业规模上构建 AI 需要 Java 和 .NET 开发人员通常具备的软件工程技能。“企业 AI 的成功——在数百个企业应用程序中拥有数百个 AI 驱动的功能——要求您在交付软件方面非常成熟，”Saikali 说。
“说实话，我们现在正处于人工智能的实验阶段，因为这个领域发展得非常快，”他继续说道。“如果我在银行构建一个 AI 应用程序，它可能是同类中的第一个，因此没有先例。治理和最佳实践同样也没有先例，并且随着组织构建这些应用程序而不断发展。
“能够更快地迭代是关键。借助 Spring AI，我们正在利用 20 年的经验帮助开发人员采用最佳实践，因此您不必从头开始。”

## 使用 Java 构建 AI 应用程序

[Spring AI](https://docs.spring.io/spring-ai/reference/) 是 Spring 和 [Spring Boot](https://roadmap.sh/spring-boot) 的 Apache License 2.0 开源框架扩展，它提供了一个客户端抽象，用于与各种 AI 提供商合作或以多模式方法为单个应用程序工作。它 [完全集成到 Spring 生态系统](https://tanzu.vmware.com/content/blog/spring-ai-empowers-java-developers-in-the-ai-landscape) 中，允许开发人员利用该生态系统来 [快速构建 AI 驱动的应用程序](https://tanzu.vmware.com/content/blog/spring-ai-enables-quick-delivery-of-intelligent-apps-in-java)。

通过提供一致的界面，Spring AI 允许您编写可移植代码，无论您使用哪种模型。Spring AI 目前支持所有主要模型提供商，包括 OpenAI、Mistral AI、
[Microsoft](https://news.microsoft.com/?utm_content=inline+mention)、[Amazon](https://aws.amazon.com/?utm_content=inline+mention)、

“我可以更改依赖项，从 Ollama 转到 OpenAI，或从 OpenAI 转到
[Bedrock](https://thenewstack.io/building-llm-based-genai-applications-with-amazon-bedrock/)，而无需更改任何代码，”Broadcom 的研究开发软件工程师兼 Spring 开发人员倡导者 [DaShaun Carter](https://www.linkedin.com/in/dashaun/) 告诉 The New Stack。

除了支持多个模型提供商外，Spring AI 还适用于各种模型类型，包括聊天、文本转图像、音频转录和文本转语音。使用模型组合允许您构建系统，例如语音助手，它从用户那里获取语音输入，将其转录为文本，将其发送到 LLM 以获取响应，然后使用文本转语音模型将该响应读回给用户。

构建这些抽象类型时的一个问题是，如果您过早地设计 API，最终会构建错误的抽象。在某些方面，最初的 Spring 框架是对 J2EE 供应商使用对象请求代理执行此操作的响应。

然而，Carter 认为，“在这种情况下，LLM 提供商已经为我们完成了一些工作，而 Spring 团队多年来已经成功地提供了这些抽象。他们观察客户以困难的方式在做什么，并抽象掉最常用的 95%，然后他们找到一种方法，允许开发人员放弃并访问最后 5% 的功能。”

## 解决企业数据和 API 集成问题

在安全性方面，第一个选择是在本地运行模型，而 Broadcom 为此提供了
[VMware Private AI Foundation](https://www.vmware.com/explore/video-library/video/6360759360112?_gl=1*1wqfjwg*_ga*Njg2NzM1NzkzLjE3MjI4NzcxNzc.*_ga_8VJHMNGE3E*MTcyNTA0NjY2OC4xNi4xLjE3MjUwNDY2NzQuMC4wLjA.)。但是，LLM 还有两个次要问题。第一个是 [获得正确答案](https://www.youtube.com/watch?v=7S6M8H2hz6w) 取决于您编写准确提示的能力，这些提示为 AI 模型提供了所需的所有信息。第二个是 LLM 在训练后被冻结，这会导致知识陈旧。

存在解决这些问题的解决方案，例如
[检索增强生成](https://thenewstack.io/retrieval-augmented-generation-for-llms/) (RAG) 用于提示编写和函数调用以更新 LLM 的知识。Saikali 说：“在这两种情况下，Spring AI 都可以捕获复杂知识，形式为称为 [顾问](https://docs.spring.io/spring-ai/reference/api/chatclient.html#_retrieval_augmented_generation) 的可重用组件。”

顾问使通用逻辑可以应用于聊天客户端请求，以增强模型交互、提供会话状态，并在应用程序内和应用程序之间以一致的方式应用日志记录和任何其他所需的聊天客户端流程

RAG 解决了将相关数据合并到提示中以获得准确的 AI 模型响应的挑战。它分两个阶段进行。

第一个基于
[提取、转换和加载 (ETL)](https://docs.spring.io/spring-ai/reference/api/etl-pipeline.html) 管道，它使用批处理式编程从文档中读取非结构化数据，然后转换并将其写入向量数据库。向量数据库更适合此目的，因为它们擅长查找相似内容。
### 在第二阶段，RAG 会获取用户的提问，并将所有相似的文档片段添加到发送给 AI 模型的提示中。

此图表展示了其工作原理：

![RAG 如何解决将相关数据纳入提示以获得准确的 AI 模型响应的挑战的图表。](https://cdn.thenewstack.io/media/2024/09/89a6a387-spring-ai-rag-1024x567.jpg)

来源：

[Spring.io](https://docs.spring.io/spring-ai/reference/concepts.html#concept-rag)

RAG 是一种强大的技术，但成功使用它可能比看起来更困难。“需要大量尝试和错误才能正确使用它，”Saikali 说。“借助 Spring AI，我们允许公司将这些 AI 模式作为 Spring AI 顾问捕获。”

他回顾了他之前提到的为银行构建 AI 应用程序的示例。借助 Spring AI，为银行构建的每个 AI 应用程序“都将与数据清洗器和其他所需内容正确集成。”

虽然这种方法有一些限制，但 RAG 提供了一种创建特定于领域的自定义的低成本方式。由于基于 RAG 的应用程序可以引用它们使用的 data source，因此它提供了更好的透明度和来源引用。

“客户问的第一个问题之一是，‘我如何针对我的用例微调这些 LLM？’”Carter 说。“借助这些向量数据库，您可以对您拥有的任何数据进行嵌入，而无需重新训练模型。Spring AI 可以轻松地使用您的嵌入注入提示，并且您可以使用这些免费提供的 LLM 为您的应用程序提供支持。”

第二个问题，即陈旧数据，可以使用

[函数调用](https://docs.spring.io/spring-ai/reference/api/functions.html)来解决，它允许您注册自己的函数以将 LLM 连接到外部系统的 API。这些系统可以为 LLM 提供实时数据，并代表 LLM 执行数据处理操作。Spring AI 处理函数调用会话，并允许您在一个提示中定义和引用多个函数。

基本流程如下所示：

![函数调用流程的图表](https://cdn.thenewstack.io/media/2024/09/9e39b008-function-calling-basic-flow-1024x554.jpg)

来源：

[Spring.io](https://docs.spring.io/spring-ai/reference/concepts.html#concept-fc)

“这就是它变得非常有趣的地方，”Carter 说，“因为您现在可以针对特定任务调用 LLM 之外的内容。例如，如果有一个关于天气的问题，您可以告诉它调用一项服务，并将该数据用作响应的一部分。”

任何 AI 实施的最后一步都是评估输出，以帮助提高最终应用程序的准确性和实用性。然而，这种技术的相关方法仍然有些新兴。

一种方法涉及向模型展示用户的请求和 AI 模型的响应，并查询响应是否与提供的数据一致。Spring AI 项目提供了一些基本的示例，说明如何评估响应，以提示的形式，以包含在 JUnit 测试中。此功能处于早期开发阶段，但更多功能已计划在未来版本中推出。

## Spring AI 入门

启动 Spring AI 应用程序就像启动任何其他 Spring Boot 应用程序一样。您可以在 IntelliJ IDEA、Spring Tools（适用于 Eclipse 和 VS Code）、NetBeans、Spring Boot CLI 或 Spring CLI 中使用 Spring Boot 支持，或者只需将浏览器指向

[Spring Initializr](https://start.spring.io/)并填写空白。

![Spring Initialzr Web UI](https://cdn.thenewstack.io/media/2024/09/09739ec4-spring-initializr-1024x500.png)

来源：

[Spring Initializr](https://start.spring.io/)

[入门指南](https://docs.spring.io/spring-ai/reference/getting-started.html)提供了更多信息，说明您需要将哪些依赖项添加到项目构建系统中，以便使用各种模型。

## 了解更多关于 Spring AI 的信息

要了解更多关于 Spring AI 的信息，请查看 Carter 最近在拉斯维加斯探索大会上关于

[Tanzu Platform 上的 Spring AI](https://www.vmware.com/explore/video-library/video/6360758967112)的演讲。另外，务必观看拉斯维加斯探索大会上的 [SpringOne Spotlight](https://www.youtube.com/watch?v=7S6M8H2hz6w)会议，Spring 专家在那里进行了现场 Spring AI 演示。

对于那些准备开始的人，Saikali 有一个

[GitHub 示例项目](https://github.com/asaikali/spring-ai-zero-to-hero)，它将引导您完成使用 Spring AI 实现 AI 项目所需的许多步骤。还有一个 [示例 AI 驱动的航班预订服务](https://github.com/tzolov/playground-flight-booking/)，它使用 RAG、函数调用和 LLM 与用户进行交互。

如果您想直接与专家交谈，Tanzu AI Solutions 团队将于 11 月 4 日至 7 日在巴塞罗那探索大会上。

[现在开放注册](https://www.vmware.com/explore/eu)。

另外，请务必不要错过
VMware Tanzu AI 解决方案的 [最新公告](https://tanzu.vmware.com/content/blog/enterprise-ready-genai-apps-with-tanzu-ai-solutions)。Tanzu AI 解决方案是 [Tanzu Platform 10](https://thenewstack.io/broadcom-debuts-vmware-tanzu-platform-10-at-explore-2024) 中的一组功能，旨在帮助组织安全、大规模地加速交付企业级 GenAI 应用程序。