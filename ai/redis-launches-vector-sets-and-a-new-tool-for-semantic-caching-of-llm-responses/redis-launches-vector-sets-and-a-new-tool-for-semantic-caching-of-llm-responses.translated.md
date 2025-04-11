# Redis发布向量集和用于LLM响应语义缓存的新工具

![Featued image for: Redis发布向量集和用于LLM响应语义缓存的新工具](https://cdn.thenewstack.io/media/2025/04/f2d42458-img_4499-edit-1024x768.jpg)

[Redis](https://redis.io/), 这家同名内存键值数据库背后的公司，近几个月来主要因其许可证变更而[见诸报端](https://thenewstack.io/redis-users-want-a-change/)，这导致了[Valkey项目](https://thenewstack.io/valkey-a-redis-fork-with-a-future/)的启动。现在，Redis希望通过在5月1日Redis 8发布之前推出两款以AI为中心的新产品来稍微改变一下话题。其中第一个是新的缓存工具[LangCache](http://redis.io/redis-for-ai/)，它允许开发人员将大型语言模型（LLM）响应缓存引入其应用程序。第二个是推出一种新的数据类型，向量集，用于存储和查询[向量](https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/)嵌入。

Redis CEO [Rowan Trollope](https://www.linkedin.com/in/rowant)在发布公告前的一次采访中告诉我：“Redis可以成为Agentic Stack的短期记忆层。” “这是公司的新战略，也是我们正在努力做的事情。”

对于Redis来说，缓存是一个显而易见的角度，它已经是许多开发人员流行的缓存解决方案。缓存LLM响应的原因与其他应用程序（降低成本和延迟）没有太大区别，但考虑到这些模型的概率性质，此处的流程与缓存SQL查询（例如）有很大不同。

Trollope说，LangCache在“底层”使用了Redis，但他强调它不是Redis数据库。它使用微调的嵌入模型来获取查询的上下文，然后创建一个嵌入来反映该上下文。

Trollope预计LangCache的主要用例将是AI代理，而不是人与聊天机器人之间的对话，后者往往更加自由，因此更难缓存。

Trollope说：“我们存在的独特理由实际上是关于性能和对开发人员来说非常容易的API。” “如果你想在数据库中存储一万亿个向量，并且你不在乎它的速度是多少，那么我们不是最好的答案。但是，如果你处于实时环境中，并且你想快速行动，并且延迟很重要——我认为在这种Agentic世界中，会有越来越多的情况变得重要。”

向量集是Redis在这里的另一个组成部分。当Redis开源项目的创始人[Salvatore “antirez” Sanfilippo](https://www.linkedin.com/in/salvatore-sanfilippo-b52b47249?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAD2STa4BUxfdShLf3CtNWdopGxyLeObb2zk&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BQR%2BjWZaqRgiVGcHe7X%2BoVg%3D%3D)去年年底重返公司时，他谈到了他对向量集的兴趣，以及为什么他认为需要一种不同的方式来考虑存储向量数据。

“Sanfilippo研究了向量数据库浪潮中发生的事情，他说，‘这太愚蠢了。’他说，‘每个人都朝着错误的方向前进。’因此，Pinecone、Milvus、Weaviate等等——它们大致都在做同样的事情，即它们正在为向量构建数据库，”总是直言不讳的Trollope说。“这些数据库的典型外观是，你添加你的数据，然后它会连接一个向量嵌入引擎，它会将数据的向量拼接在一起，然后它会创建一个索引，你可以针对它进行搜索。”

Redis认为，使用向量集（然后还将原始向量以更压缩和优化的格式存储）以及Sanfilippo开发的一种新的相似性搜索算法，应该比当前最先进的技术显着提高速度。由于数据库存储在内存中，这也意味着对昂贵内存的需求减少，或者开发人员可以在其现有服务器上存储更多的这些向量集。

Trollope说，Sanfilippo认为，Redis之所以成功，是因为它没有为开发人员做太多事情，公司应该对此采取相同的方法，并将向量集作为开发人员的新构建块提供，供他们决定如何使用它们。

在业务方面，Trollope指出，Redis仍然希望在某个时候进行IPO。他说，该公司几乎实现了盈亏平衡，并且在财务上可以为IPO流程做好准备。但他想做的是深入投资，成为AI应用程序的事实上的短期记忆（而LLM更像是长期记忆）。
我一直在和银行家们谈话，他们都希望我们进行首次公开募股（IPO）。他们就像是，‘IPO，冲，IPO。’实际上，我现在对此并不太感兴趣。我的意思是，我认为我们最终会走到那一步。我认为随着人工智能（AI）的机会，我正在对业务进行更多投资。我本可以为IPO打造公司的营收和利润，但我没有这样做，因为人工智能的机会太大了。[…]对于之前的云移动应用浪潮，Redis是一个事实上的标准，就像任何开发人员构建云移动应用一样，可能在95%的情况下都会引入Redis——然后我们会将其中一小部分货币化。现在你进入了一个新时代，每个人都将以agentic风格重写所有应用程序，而这一切都还悬而未决。

Trollope认为，随着开发人员创建这些新的用例和应用程序，他们将使用他们熟悉的工具。他认为，agentic架构本质上是使用微服务，这些微服务使用LLM，而不是在其核心中使用硬编码的规则和业务逻辑。为此，你需要一个编排层和一个会话存储，因为这些微服务/代理需要是无状态的。他认为，Redis非常适合那些想要保存这些代理状态的开发人员，因为它速度快且持久。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等。