# DataStax 旨在通过 RAGStack 简化 AI 应用构建

![Featued image for: DataStax Aims To Simplify Building AI Apps With RAGStack](https://cdn.thenewstack.io/media/2024/07/8063fcea-buildingaiapplications-1024x683.jpg)

ChatGPT 令我们所有人惊叹，但它实际上只是对 [大型语言模型 (LLM)](https://thenewstack.io/working-with-llm-apis-dev-shares-experience-building-ai-bots/) 最简单的演示，[DataStax](https://thenewstack.io/datastax-gas-data-api-for-genai-application-development/) 首席产品官 [Ed Anuff](https://www.linkedin.com/in/edanuff/) 说道，该公司提供基于开源 [Apache Cassandra](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/) 的分布式云数据库。

“它会获取之前的响应以及称为历史记录的先前交互——它会获取这些并添加您的新问题作为额外的提示，并将所有这些捆绑到一个上下文中并将其发送到 LLM，并且它会不断重复这个过程，”他谈到 ChatGPT 时说道。“当 ChatGPT 首次发布时，它所做的仅仅是这些。我们体验到的结果非常酷，但从计算机科学程序的角度来看，它实际上非常简单。”

[检索增强生成 (RAG)](https://thenewstack.io/how-rag-architecture-overcomes-llm-limitations/) 是一种补充 LLM 知识的方法。他将 RAG 比作便签卡，可以帮助你在谈论某个主题时保持专注和真实。

RagStack：这个想法是提供一组技术，类似于 LAMP 堆栈对 Web 开发所做的那样，这些技术可用于创建 AI 应用。

“让我们去检索这些非常准确的知识来源，这些来源是通过传统的数据库查找检索到的，”他说。“在某些情况下——在很多情况下——[你] 使用向量数据库查找来获取信息并将其馈送到 LLM，然后 LLM 只使用其语言功能来构建该响应。”

RAG 可以通过不同的机制工作，包括简单的搜索方法以及更 [复杂的方法，例如将问题转换为数据库查询](https://thenewstack.io/how-to-run-complex-queries-with-sql-in-vector-databases/)，他说。RAG 后的结果是“有根据的”，这意味着 LLM 结果更准确，因为 LLM 使用了与查询一起提供的特定事实信息，而不是仅仅依赖于它自己的训练数据，他解释道。他补充说，这种方法通过避免推测性或不完整的答案来提高准确性，从而导致响应更符合提供的信息，因此更可靠。

“所有这些都会导致在幕后收集大量信息，然后将这些信息与您的原始问题一起馈送到 LLM，”他说。“LLM 所做的是——而不是去依赖它自己训练的知识——它使用提供给它的信息，然后 LLM 响应。”

## 使用 RAGStack 创建 AI 应用

最近，DataStax 更新了其产品，使 RAG 应用开发速度提高了 100 倍，该公司在 [旧金山的 RAG++](https://www.datastax.com/press-release/datastax-to-launch-massive-new-ai-platform-updates-at-rag-plus-plus-event-in-san-francisco-partners-attending-langchain-microsoft-mistral-ai-nvidia-unstructured-and-more) 上宣布。为此，它正在使用它称之为 [RAGStack](https://www.datastax.com/blog/ragstack-1-dot-0-generally-available) 的东西。这个想法是提供一组技术，类似于 [LAMP](https://thenewstack.io/install-a-full-lamp-stack-on-a-debian-server/) 堆栈对 Web 开发所做的那样，这些技术可用于创建 [AI 应用](https://thenewstack.io/how-to-easily-add-ai-to-your-applications/)。

为了支持其 RagStack 愿景，该公司还在 Astra Cloud Platform 上推出了 [Langflow](https://www.datastax.com/blog/introducing-datastax-langflow-design-test-generative-ai-apps) 的托管版本。

[Langflow 是一个开源的可视化框架](https://astra.datastax.com/signup?type=langflow)，用于构建 RAG 应用。DataStax 在 4 月份收购了 Langflow。它使用拖放式 GUI 来创建数据流，并利用 [LangChain 用于 RAG 功能](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)，从而允许开发人员使用各种向量数据库、嵌入模型和大型语言模型 (LLM) 来设计、试验和测试 RAG 和 GenAI 应用。
基本上，它使 LangChain 对开发人员更容易。它通过抽象化基础设施问题并与多个 GenAI 工具（例如 OpenAI、Hugging Face 等）集成来实现这一点，根据该公司的新闻稿。
它作为 DataStax 的 Astra Cloud 平台上的托管版本提供，使开发人员更容易访问和使用。DataStax 托管的 Langflow 将允许开发人员使用任何向量数据库、嵌入模型或 LLM 设计、试验和测试 [RAG 和 GenAI 应用程序](https://thenewstack.io/develop-a-cloud-hosted-rag-app-with-an-open-source-llm/)，而无需在他们的机器上安装 Langflow。

RagStack 还利用 [LangSmith](https://www.langchain.com/langsmith)，这是一个用于管理和监控 LLM 应用程序的企业 DevOps 平台。同时，DataStax 发布了 Langflow 1.0 版本，其中包含数十个与顶级 GenAI 工具的集成，根据 [公司博客文章](https://www.datastax.com/blog/introducing-datastax-langflow-design-test-generative-ai-apps)。

根据该公司介绍，Langflow 1.0 允许开发人员利用 LangSmith 的可观察性服务来跟踪应用程序的响应，从而获得更相关、更准确的基于 LLM 的应用程序。Astra DB 环境详细信息将在 Langflow 中随时可用，用户可以通过 [Astra 门户](https://accounts.datastax.com/session-service/v1/login) 访问 Langflow。该公司补充说，使用将是免费的。

## 向量化数据和使用 Unstructured.io
DataStax 还重点介绍了 [Vectorize，最近发布的版本](https://www.datastax.com/blog/simplifying-vector-embedding-generation-with-astra-vectorize)，它直接在数据库级别处理嵌入生成。Anuff 解释说，它会将你放入数据库的任何内容都生成其向量表示。

“向量表示是我们获取这些非结构化数据的地方，这些非结构化数据可以是一段文本，可以是图像，可以是任何东西，但我们获取它并生成嵌入。该嵌入是一个非常长的数值表示，它代表了该内容的语义含义，”他说。

他解释说，这些向量进入数据库，其中彼此最接近的行具有相似的含义。从开发的角度来看，这节省了时间。

“这使我能够获取可能与你所要求的语义含义相关的，而不是精确的关键字，”他说。“在我想通过含义而不是特定关键字检索内容的这些设置中，这是一个非常强大的工具，因为你可能永远不会使用特定关键字，但含义可能非常接近。”

最后，[DataStax 宣布与](https://www.datastax.com/blog/data-ingestion-just-got-easier-unstructured-astra-db) [Unstructured.io](https://unstructured.io/) 建立合作伙伴关系，该公司提供连接器，可以访问数据源和数据格式，并提取相关内容，以正确的字节大小块的形式提供给 Astra DB Vector 数据库，Anuff 说。该公司在其新闻发布会上表示，这种合作关系将使 [开发人员能够提取和转换复杂数据](https://thenewstack.io/the-genai-data-developer-experience-performance-optimization/)，以便存储在 Astra DB Vector 中，用于为基于 LLM 的应用程序提供支持。

“用户的 GenAI 应用程序得益于闪电般的快速数据摄取，通过将大型数据集和常见文档类型快速转换为向量数据，”该公司表示。“这种新的集成然后使这些嵌入能够快速写入 Astra DB，以进行高度相关的 GenAI 相似性搜索。而且，在管理非常大的数据集时，用户能够将这些数据转换为嵌入，并在几分钟内将其写入 Astra DB。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)