<!--
title: Apollo：GraphQL现在可以轻松连接到REST API
cover: https://cdn.thenewstack.io/media/2025/03/9137345f-alex-shuper-2iz9r2pgjjq-unsplash-1.jpg
summary: API福音！Apollo发布REST API连接器，GraphQL轻松集成！Router 2.0性能飙升10倍，GraphOS免费计划助力云原生微服务和SaaS产品编排。告别API蔓延，拥抱声明式GraphQL，加速AI集成，标准护航，DevOps效率UP！
-->

API福音！Apollo发布REST API连接器，GraphQL轻松集成！Router 2.0性能飙升10倍，GraphOS免费计划助力云原生微服务和SaaS产品编排。告别API蔓延，拥抱声明式GraphQL，加速AI集成，标准护航，DevOps效率UP！

> 译自：[Apollo: GraphQL Now Connects to REST APIs With Little Fuss](https://thenewstack.io/apollo-graphql-now-connects-to-rest-apis-with-little-fuss/)
> 
> 作者：B Cameron Gain

许多（如果不是大多数）工程师和运维架构师都非常熟悉 API 蔓延这一不幸难题，这主要是由作为包含 [REST API](https://thenewstack.io/rest-still-outshines-graphql-for-many-api-use-cases/) 的层 BFF 驱动的。随着组织规模的扩大，支持 REST API 的后端即前端（BFF）模式可能会变得难以管理，并且肯定会耗费大量时间来单独更新代码。

[GraphQL](https://thenewstack.io/graphql-growth-explodes-but-so-do-problems-federated-graphs-solve/) 作为一种开放标准，已经证明了其在解决编排 API 这一挑战方面的价值。但是，尽管组织长期以来一直寻求将 REST API 与 GraphQL 集成，但单独集成每个 API 的过程仍然是一个普遍且持续存在的痛点。

现在，Apollo 宣布 Apollo Connectors for REST APIs 全面上市。有了它，组织可以根据组织拥有的 REST API 定义 GraphQL 模式，并仅用几行配置来编排对这些 API 的调用。

![](https://cdn.thenewstack.io/media/2025/03/7f879219-capture-decran-2025-03-04-210814.png)

“[Matt DeBergalis](https://www.linkedin.com/in/debergalis)，Apollo Labs 的 CTO 告诉我：“当团队疯狂地编写过程代码而不是通过 GraphQL 使用声明式替代方案时，会存在很多缺点。”

此外，Router 2.0 现在也已全面上市，据 Apollo 称，它为大规模 GraphQL 部署提供了超过 10 倍的性能提升。

Apollo 还为 Apollo GraphOS 引入了一项新的免费定价计划，使团队可以从小规模开始扩展，而无需前期投资。该计划包括访问试用功能和连接器，从而使团队可以更轻松地采用和扩展其 GraphQL 的使用。组织可以通过访问 [GitHub](https://github.com/apollographql/connectors-community) 并下载带有 GraphQL 的适用 Apollo 代码来免费开始使用。

![](https://cdn.thenewstack.io/media/2025/03/bfc962f6-capture-decran-2025-03-04-175749-1024x461.png)

正如 GraphQL 已成为连接 REST API 的现代、基于标准的方式一样，GraphQL 最终也不会取代 REST API。REST API 也具有 GraphQL 可能无法提供的功能。虽然两者都支持从后端系统获取数据，但它们解决了不同的问题，并从频谱的不同端点处理数据。

例如，GraphQL 提供了一种强类型的模式定义语言，用于描述存在于任意数量系统中的数据，这种方式对客户端来说是直观且有用的。相比之下，REST 鼓励一种更面向资源的方法来组织和部署服务，通常沿着域边界进行。它更侧重于对实体关系进行建模，而不是以需求驱动的方式向客户端提供数据。其想法是兼具两者的优点：更无缝（或无痛）的集成，具体取决于您如何看待 REST API 和 GraphQL 的好处。

“我们不是来取代 REST 的。我们真的不是说 GraphQL 比你拥有的 API 更好，其中可能还包括 [gRPC](https://thenewstack.io/grpc-delivers-on-the-promise-of-a-proxyless-service-mesh/) 和其他 API，”DeBergalis 说。“我们上周宣布的 REST 连接器的动机是，现在行业中存在一个巨大的痛点，我们每家公司都有 20 多年的‘80 只眼睛’。”

要管理的大多数 API 都是 REST，但也有其他的。除了上面提到的 gRPC API 之外，还有其他的，例如 [SOAP API](https://thenewstack.io/api-management-for-asynchronous-apis/)，“可以追溯到更早的过去，”DeBergalis 说。“API 是业务的构建块。它们是公司的资源或能力，”DeBergalis 说。

![](https://cdn.thenewstack.io/media/2025/03/638a0ca1-capture-decran-2025-03-04-175820.png)

*可以使用 YAML 配置和管理 GraphOS Router。*

一些组织管理着 50 多个 API，这并不罕见。“这是云原生、微服务和 [SaaS 产品](https://thenewstack.io/private-saas-is-coming-are-you-ready/) 兴起的必然结果：我们必须集成这些 API，”DeBergalis 说。“当你看到所有采用 Apollo 的公司时，他们正在解决的问题是一个编排问题：如何将所有这些 API 连接到我们想要编写的软件？这关系到如何以正确的顺序调用这些 API。如何将它们链接在一起？如何转换结果？如何在需要实时应用程序时使它们异步？”

DeBergalis 说，工程师们每次想构建一些东西时，都必须完成一长串技术任务。他们经常必须管理应用程序开发、从遗留系统切换、集成 AI 和迁移到微服务。对于具有遗留单体架构的组织，通过并购，组织必须将单独的产品集成到一致的用户体验中，DeBergalis 说。

“你知道，我猜开发人员花费的总时间中有很大一部分用于编排代码，这太疯狂了——我的意思是，如果你看看云原生堆栈的其余部分，它们都已转向这种声明式方法，我们无需编写代码即可将软件部署到云主机上，”DeBergalis 说。“编写代码是有风险的：它速度慢，会增加性能开销，并会损害安全足迹。”

## 标准的标准

GraphQL 是一个开放标准。虽然 Apollo 提供了 GraphQL 的企业版本和相关的 GraphOS 平台，但 Apollo 并不直接控制该标准。相反，治理结构是这样的，GraphQL 标准由 Linux 基金会的 [GraphQL 基金会](https://thenewstack.io/rest-vs-graphql-solving-api-challenges-in-modern-data-transfers/) 管理。这意味着该标准变成专有的风险几乎为零。

“我认为基于标准的技术至关重要，这是我们在考虑 API 战略时肯定会给任何人的建议——你必须以 10-20 年以上的眼光来考虑，”DeBergalis 说。“这意味着你必须从基于标准的方法开始，因为该战略应该长期有效。

借助 GraphQL 和 GraphOS，可以为运营创建一个核心治理和管理结构。“如果你要考虑在拥有数千个 API 的大型组织中构建编排层是什么样的，并且你有数百名开发人员协同工作，那么你需要的不仅仅是核心机制——你需要围绕它的整个产品，以解决围绕协作、治理、工作流程等方面的问题。这就是我们的产品：GraphOS，任何开发人员都可以免费使用它，因此他们可以尝试所有随之而来的东西，不仅包括核心连接器，还包括我们拥有的帮助团队扩展的工具和系统，”DeBergalis 说。“这只是我们使命的一部分——确保每位开发人员都可以尝试和体验这种方法，并最终成为每个组织的首选。”