<!-- 
# LangStream: 面向LLM应用的基于事件驱动的开发者平台
https://cdn.thenewstack.io/media/2023/10/a31a5057-langstream-1024x679.webp
Image via DataStax
 -->

译自 [LangStream: an Event-Driven Developer Platform for LLM Apps](https://thenewstack.io/langstream-an-event-driven-developer-platform-for-llm-apps/) 。

LangStream开源框架将数据流技术与生成式AI相结合。我们采访了DataStax公司的项目负责人Chris Bartholomew，聊到了这一开发者平台。

DataStax最近发布了一个名为[LangStream](https://langstream.ai/)的新开源项目，将数据流技术与生成式AI相结合。我们采访了这个项目的负责人、流处理工程师[Chris Bartholomew](https://www.linkedin.com/in/chris-bartholomew/)，讨论了LangStream为新兴的AI应用生态系统带来了什么，以及它与当前较为热门的[LangChain项目](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)是否有任何相似之处。

[DataStax](https://www.datastax.com/company)至今已有10多年历史，最初是凭借在开源NoSQL数据库Apache Cassandra上构建的一个数据管理产品在云原生社区崭露头角。如今，DataStax自称为“实时AI公司”，因此其最新产品已经强烈地向生成式AI转型。

在其主页上，LangStream被描述为一个用于“构建和运行基于事件驱动的AI应用”的平台。Bartholomew进一步解释说，LangStream针对的是事件驱动和流式架构，这与现有的AI应用开发系统不同。他认为这些架构对于生成式AI应用特别有益，因为它们能够处理海量数据并优先考虑最新和最相关的数据。

他说：“数据越新越相关，在构建提示和向LLM发送提示时就越好。”

## LangStream和向量数据库

Bartholomew表示LangStream是一个中立的开源供应商中立项目，尽管开箱即用它支持DataStax的向量数据库Astra DB。它还支持开源向量数据库Milvus和[Pinecone](https://thenewstack.io/vector-databases-are-having-a-moment-a-chat-with-pinecone/)。

我问开发者如何将LangStream与向量数据库一起使用？

他回答说，工作流程有两个主要组成部分。首先，数据(通常是非结构化的)通过管道进行向量化处理。这需要部署专门的代理程序，可以爬取网站或从存储源(如S3存储桶)访问文档，然后分割这些数据并使用来自OpenAI或Hugging Face等平台的嵌入模型。结果数据然后与向量数据库同步。

下一步是在应用中使用这些数据，比如生成式AI聊天机器人。Bartholomew解释说，在收到用户查询时，LangStream会查询数据库获取相关数据(使用RAG模型:检索增强生成)，将该数据转化为LLM的提示，然后调用语言模型。

这听起来确实是在应用中使用向量数据库的一种有用方法，那么实时数据的处理在哪呢?

Bartholomew指出，特别是向量格式的数据具有动态变化的特点，不断更新演化而不是静态的。他说，定期重新评估LLM应用中使用的数据非常关键。

例如，如果从网站(内部网站聊天机器人)提取数据，就需要重新评估有没有新数据，因为数据会持续产生。”

他补充说，LangStream具有自动管道，可以持续评估新数据。

## 如何在LangStream中构建应用

关于开发者如何使用LangStream作为平台来创建LLM应用，我请Bartholomew解释这在实践中是如何工作的。

他回复说，LangStream作为一个开发框架运行，提供无代码方法，用户可以通过配置和组合各种“代理”来编排流水线。但对于更高级的用例，开发者可以用Python编写自定义代理。

“所以你可以编写任何定制代码。我们还会把LangChain、LlamaIndex等流行Python库预装到运行时环境中。”

他补充说，运行时环境基于Kubernetes和Apache Kafka。“我们本可以只写一个库来把这些东西粘合在一起，但我们真的想要一个可靠的LangStream应用运行时环境。”

![](https://cdn.thenewstack.io/media/2023/10/de2a257f-langstream-screen-shot.png)
*LangStream 接口*

提到LangChain让我问LangStream是否与这个较知名的“Lang”产品有任何相似之处。

他回答说，LangStream与LangChain是互补的。他举了一个用LangChain创建的原型应用的例子。

“所以你可以把它转化并在LangStream中运行。LangStream是一个运行时环境，而不仅仅是一个开发环境。”

他补充说，你还可以考虑将LangChain应用“分解”或“重新组合”为基于事件的架构，也就是说转换为基于微服务的分布式应用。

“这样你可以获得可扩展性优势，这种模式众所周知，易于理解如何扩展。你也获得健壮性。”

## LangStream vs JavaScript构建LLM应用

我提到今年我看到的许多AI应用似乎都是在JavaScript框架(如[Vercel的](https://thenewstack.io/vercels-next-big-thing-ai-sdk-and-accelerator-for-devs/)Next.js)中开发的。所以我问LangStream的方法与这种方法有何不同。

他回答说，必须小心在浏览器前端与OpenAI等LLM系统交互，因为可能会暴露私钥。他认为更安全的架构是前端与后端通信。

“你会有一些认证，但不会暴露密钥来调用昂贵的LLM。”

根据Bartholomew的说法，最佳实践是编写前端应用与后端应用交互，这就是DataStax配置LangStream的方式。他指出，它使用WebSocket网关进行通信。

这种方法(基于事件驱动，前后端分离)的一个用例是Bartholomew提到的“多谈多谈聊天机器人”。这种聊天机器人不仅回答问题，还可以在需要时主动发起对话并提问。

他解释说:“现在聊天机器人是请求-回复的。我问它问题然后它回答。它等待我提问。而我们基于事件驱动，可以异步发送消息，所以聊天机器人可以主动发起对话，发送消息说‘你好，我是聊天机器人，我能做xxx’。如果你有段时间没有提问，它还可以试图继续对话。”

## 总结

LangStream为[AI应用领域](https://thenewstack.io/llm-app-ecosystem-whats-new-and-how-cloud-native-is-adapting/)带来了一些新思路，具有基于事件驱动的架构，并让AI工程师可以使用Kubernetes和Kafka。所以它在开发者特别是偏爱Python而不是JavaScript的开发者中获得采用，将会很有趣。
