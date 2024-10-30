# Apollo 如何利用 GraphQL 使 LLM 更可靠

![Apollo 如何利用 GraphQL 使 LLM 更可靠的特色图片](https://cdn.thenewstack.io/media/2024/10/6633051f-aakash-dhage-i5_hrkczgvk-unsplash-1024x576.jpg)

纽约 - 我们都知道 AI/ML 在 [DevOps](https://thenewstack.io/devops/) 支持和 [应用程序开发](https://thenewstack.io/the-reality-of-edge-application-development/) 方面可能成功也可能失败。然而，在 [GraphQL 搜索查询](https://thenewstack.io/graphql-to-rest-api-connectors-is-apollos-biggest-thing/) 的情况下，它似乎至少运行得相当好 - 而且还有更多东西要来。

这是 [Apollo GraphQL](https://www.apollographql.com/?utm_content=inline+mention) 本月初在这里举行的 [年度用户大会](https://summit.graphql.com/connect) 的主要收获之一。在活动中，该公司推出了一个并非仅仅是另一个 AI 产品的东西，而是在太多情况下似乎充其量只是敷衍了事，但他们声称它已经提供了切实的价值：Apollo GenAI 工具包。

“随着 Apollo GenAI 工具包的发布，Apollo 现在拥有所有必要的工具，可以为 AI 提供必要的提示和钩子，将意图转化为所需的结果，”Apollo GraphQL 的 CTO 联合创始人 [Matt DeBergalis](https://www.linkedin.com/in/debergalis) 在大会主题演讲中说道。“这种方法确保了流程保持敏捷、实验性和安全性。”

DeBergalis 说，Apollo GenAI 工具包用于在图之上构建 [大型语言模型 (LLM)](https://thenewstack.io/llm/) 和 LLM 驱动的应用程序，以及一个开源模板来帮助用户入门。

这种架构中有两个基本思想：第一个是图将用于 [编排](https://thenewstack.io/llamaindex-and-the-new-world-of-llm-orchestration-frameworks/)，DeBergalis 说。在这种设置中，LLM 的作用是将用户的自然语言请求转换为 [GraphQL](https://thenewstack.io/the-unlikely-journey-of-graphql/) 查询，该查询准确地表达了用户的意图。DeBergalis 说，图的作用是执行该查询，协调适当的 API 调用，同时对请求执行必要的安全性和规则。

第二部分解决了查询来自何处。在这种架构中，[聊天机器人](https://thenewstack.io/5-ways-chatgpt-could-supercharge-chatbots/) 被限制为从安全、预先编写的查询库中进行选择。这些查询存储在 [向量数据库](https://thenewstack.io/what-is-a-real-vector-database/) 中，例如 [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)，在那里进行相似性搜索。DeBergalis 说，这个过程允许 LLM 根据用户的请求从库中选择最相关的查询。然后，它使用用户提供的上下文 - 例如项目的名称或其他详细信息 - 将其转换为查询的特定参数。

“如果你熟悉 LLM 函数和插件，可以将这种方法视为一个‘智能函数工厂’，”DeBergalis 说。“你不需要每次想要扩展 LLM 的功能时都编写新代码 - 你只需编写一个查询。这使得这个过程既安全又高效。”

在主题演讲中的演示中，一个 LLM 被教导将最终用户的响应纳入涉及 [检索增强生成 (RAG)](https://thenewstack.io/graph-rag-how-to-squeeze-more-value-from-ai/) 数据的查询，这些数据位于 MongoDB 数据库中。它学会了如何识别持久化查询。演示中的最终用户能够实时获取有关滑雪板的信息。

## GraphQL 的正确东西
更多

[@GraphQL] 可以自动执行 API 的联合以进行编排，开发人员不必担心管理基础设施，这样他们就可以完成自己的工作。我从 [#GraphQLSummit] 和 [@apollographql] CTO [@debergalis] 的主题演讲中获得的其中一个收获。[pic.twitter.com/ziqSfr5QUm]— BC Gain (@bcamerongain)

[2024 年 10 月 9 日]
GraphQL 特别适合搜索查询的原因主要在于它对 LLM 的考虑范围有限。可以提出的特定请求数量有限，这使得它本质上比大规模 LLM 复杂得多，后者试图解决更广泛的任务范围。GraphQL 查询的集中性质与 LLM 很好地契合，因为范围更易于管理，从而导致更一致和准确的结果。


[@apollographql] 的 Ben Newman 在 [#graphqlsummit] 上的演讲“AI 驱动的超级图：从文本到查询到对话代理”中说：“LLM 在编写 GraphQL 查询方面‘有用吗’？...我有一些好消息：它们确实有用。”在 [@thenewstack] [pic.twitter.com/TFmJEpU40z]— BC Gain (@bcamerongain)

[2024 年 10 月 10 日]
在主题演讲中，软件架构师 [Benjamin Newman](https://www.linkedin.com/in/newben/) 描述了 Apollo 如何添加一个连接器子图，该子图使用 [REST API](https://thenewstack.io/rest-still-outshines-graphql-for-many-api-use-cases/) 与原始系统通信，该系统非常适合 AI。Newman 说，虽然这看起来像是连接器增加了复杂性，但真正的益处是用户拥有一个统一的查询接口，客户可以通过聊天机器人及其聊天 UI 使用该接口，开发人员也可以在幕后将其用于 IDE 中的编码系统符号。

“虽然很难预测代理改进后中间层会是什么样子，但代理最终将能够使用与人类相同的工具——即 GraphQL 查询和路由器，以及 GraphQL 附带的所有优势，”他说。“因此，无论您最终构建什么样的 AI 体验，如果它们与 API 交互，您很可能希望有一个 GraphQL 层来调解这些交互。”

对于那些对 AI 持怀疑态度的人来说，Newman 说，“建议尽早采用 GraphQL”。“归根结底，您只需要 AI 来提供一个灵活的自然语言前端，它可以接收用户请求并将它们转换为机器可执行的操作，”Newman 说。“这听起来很复杂，但所有这些技术今天都存在，并且运行得非常好。”

主要功能是 AI 如何与 GraphQL 中的持久查询配合使用。Newman 说，由于聊天机器人可以信任这些查询是安全的，因此它可以在幕后运行，而无需每次都请求许可。这使得聊天机器人能够以更对话的方式进行响应。Newman 说：“还有很多可以做的事情来使系统更智能。例如，如果持久查询不可用，它可以回退到实时生成新查询。”

## 炒作粉碎机
“我们可以使用

[#LLMs] 它们今天存在，将 [@GraphQL] 变成人类用户今天可以使用……的自我文档化……实体……然后只需等待代理赶上来，”[@apollographql] 的 Ben Newman 在今天在 [#graphqlsummit] 上的演讲中说。[@graphqlsummit][@thenewstack][pic.twitter.com/QRSpChSEoB]— BC Gain (@bcamerongain)

[2024 年 10 月 10 日]
至少到目前为止，当 AI 应用于所有开发人员和运营团队的系统时，它并不一定能达到炒作的程度。Newman 在他的主题演讲中提到了 Salesforce，称其为“准备宣布胜利”，因为它推出了新产品 [Agentforce](https://www.salesforce.com/agentforce/)。

“他们承诺这就是 AI 的本意，他们的营销团队公开声称到 2025 年底将有 10 亿个代理使用 Agentforce，”Newman 说。“这可能随着时间的推移而变得有用，而且很明显，工程师正在努力解决有趣的问题。然而，宣布这种胜利似乎为时过早。”

Newman 告诉我，在许多情况下，组织过早地依赖于 RAG 系统，而这些系统无法以使 LLM 有用的方式充分处理数据。

“很多人最终会建立这些 RAG 系统，他们只是将任何类型的文档都扔进去——比如，PDF  notoriouly 难以向量化，如果你知道要回答什么问题，这比必须做的事情要难得多，”Newman 在主题演讲结束后告诉我。

谈到 Salesforce 对 AI 的说法，Newman 告诉我：“读到这些，我的血压有点升高。我可以想象正在开发该产品的工程师可能对此感到非常自豪，但随后营销团队就带着他们的说法跑掉了。”

## RAG 为中心
随着生成式 AI 在 GraphQL 和整个计算领域中站稳脚跟，RAG 将发挥关键作用。GraphQL 用例还涵盖 MongoDB 的向量实例、聊天机器人基础设施和其他流程。正如 MongoDB 产品、搜索和 AI 总监 [Benjamin Flast](https://www.linkedin.com/in/benjamin-flast) 在主题演讲中解释的那样，RAG 将上下文带入应用程序，并支持提示 LLM 更一致。

“它的工作原理是，您使用某种检索机制，无论是数据库查询还是某种向量搜索查询，然后您去获取相关逻辑，并将它带入模型以确定它将提示的结果，”Flast 说。“这有助于应用程序，您知道，在整个领域，包括我之前提到的聊天机器人和其他应用程序，但只是使它们更可靠和一致。”

同时，其他用例正在出现。Flast 说，GraphQL 搜索查询已经成为 LLM 支持的绝佳用例，其中包括聊天机器人、知识助手、代码助手和知识管理。
“我们主要看到的是，现在有更多安全的使用案例。这些案例很适合，人们对他们正在做的事情感到满意，而且在大多数情况下，你知道，它们今天很好，”他说。“但我们已经迅速看到人们开始突破他们将这些应用程序引入生产环境的界限，以及他们使用生成式 AI 构建的各种功能。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。