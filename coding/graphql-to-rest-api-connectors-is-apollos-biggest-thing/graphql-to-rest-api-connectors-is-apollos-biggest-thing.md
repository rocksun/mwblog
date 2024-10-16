
<!--
title: GraphQL-to-REST API Connectors是Apollo的“最伟大的成就”
cover: https://cdn.thenewstack.io/media/2024/10/af96afdf-behnam-norouzi-c-rgxbo1oiq-unsplash-1024x658-1.jpg
-->

Apollo GraphQL Connectors 提供了一种将 REST API（以及即将推出的更多 API）转换为 GraphQL 语言的方法。

> 译自 [GraphQL-to-REST API Connectors Is Apollo's ‘Biggest Thing’](https://thenewstack.io/graphql-to-rest-api-connectors-is-apollos-biggest-thing/)，作者 B Cameron Gain。

纽约——在 [Apollo GraphQL 峰会 2024](https://summit.graphql.com/) 上发布的 [Apollo GraphQL](https://www.apollographql.com/?utm_content=inline+mention) Connectors 标志着 Apollo 在简化 [API 集成](https://thenewstack.io/solving-api-integration-and-aggregation-with-supergraph/) 方面迄今为止最重要的创新之一。

随着针对 [REST API](https://thenewstack.io/the-state-of-introspection-for-rest-and-graphql-apis/) 的 Apollo Connectors 的推出，开发人员可以逐步或一次性地将 REST API 集成到 [联邦 GraphQL](https://thenewstack.io/graphql-federation-the-missing-api-for-your-platform-strategy/) 架构中。是的，您以前可以将 REST API 与 GraphQL 集成，但这涉及手动实现代码——我们可以说这是一个繁琐的过程。

> [@apollographql]´s[@debergalis]: «Connectors 真正改变了你和你的团队对[@GraphQL]的看法。这是我们做过的最伟大的事情。»[#graphqlsummit][@thenewstack][pic.twitter.com/bsa6Y8SZbB]— BC Gain (@bcamerongain)

正如 Apollo GraphQL 的首席技术官兼联合创始人 [Matt DeBergalis](https://www.linkedin.com/in/debergalis) 所描述的那样，作为“我们做过的最伟大的事情”，Connectors 提供了一种将 REST API（即将推出更多 API）转换为 [GraphQL](https://thenewstack.io/the-unlikely-journey-of-graphql/) 语言的方法。以前没有Connectors ，为了实现这一点，您需要一小段称为 GraphQL 服务器的中间件代码。“您只需为每个 API 创建一次，但它需要复杂、具体的知识才能完成，”DeBergalis 说。

## 消除复杂性

换句话说，如下所述，如果没有Connectors ，该过程将更加耗时。

“Connectors 消除了这种复杂性。它们通过消除与塑造 GraphQL 层相关的大部分前期设计工作来简化流程。Connectors 采用更务实的做法，无需再编写服务器，”DeBergalis 说。“这也摆脱了额外的网络跳转、性能成本以及与在生产环境中运行服务器相关的一切。”

Connectors 旨在减少 [DevOps](https://thenewstack.io/devops/) 团队成员可能需要编写的代码量，允许将所有 API 相对快速地组合到 Apollo 超图中。“这种方法释放了巨大的价值，因为许多企业都有 API，但它们的价值取决于它们的使用难易程度，”DeBergalis 说。“这些 API 的可用性如何？它们的开放程度如何？它们可以多快组合在一起？能够做到这一点的公司将是那些能够更快地交付和创新的公司。”

正如 GraphQL 已成为连接 REST API 的现代、基于标准的方式一样，GraphQL 最终也不会取代 REST API。REST API 还具有 GraphQL 可能无法提供的功能。虽然两者都支持从后端系统获取数据，但它们解决的是不同的问题，并且从不同的角度处理数据。

也就是说，GraphQL 提供了一种强类型的架构定义语言来描述跨任意数量系统的数据，这种方式对客户端来说既直观又实用。相比之下，REST 鼓励采用更加面向资源的方法来组织和部署服务，通常沿着域边界。它更侧重于对实体关系进行建模，而不是以需求驱动的方式向客户端提供数据。

“我们来这里不是为了取代 REST……我们真的不是说 GraphQL 比您现有的 API 更好。它不比 gRPC 好。它不比 REST 好，”DeBergalis 在其 GraphQL 峰会 2024 的主题演讲中说道。“这不是重点。它使这些东西变得更好，对吧？”

Apollo 的 Apollo Federation（用于构建联邦 GraphQL 基础设施）提供了一个带有 GraphQL 的联邦图层，以便抽象 REST 端点的复杂性。图层为所有操作公开了一个端点，而不是数百个独特的 REST 端点，并且涉及的编程更少。随着Connectors 的发布，这种抽象功能比以前集成每个 REST API 所需的编码和手动输入要少得多。

更具体地说，正如 Apollo 的 [Dylan Anthony](https://www.linkedin.com/in/dylan-anthony/) 在一篇 [博文](https://www.apollographql.com/blog/apollo-connectors-for-rest-apis) 中所说，在Connectors 发布之前，开发人员在将 REST 服务添加到联邦 GraphQL API 时必须采取许多额外的步骤：

- 确定一种编程语言和一个兼容 Apollo Federation 的 GraphQL 框架。
- 部署一个新的子图服务，包括监控、自动扩展和负载均衡，它将位于路由器和 REST API 之间。

Anthony 描述了每次更改 REST API 时的情况：

- 必须设计底层 REST 数据的子图模式。
- 必须使用所选编程语言编写与 REST API 的绑定。
- 必须编写利用这些绑定的解析器。
- 必须部署子图服务。
- 必须组合和发布用于更新路由器的模式。

Anthony 描述了使用 Apollo Connectors 如何减少每次迭代：

- 设计底层 REST 数据的子图模式。
- 组合和发布用于更新路由器的模式，以便路由器可以直接与 REST API“对话”：

![](https://cdn.thenewstack.io/media/2024/10/5ef568c3-capture-decran-2024-10-14-173838.png)

## Coinbase 的观点

然而，世界不仅仅只有 REST API。以加密货币交易平台提供商 Coinbase 为例，Connectors 未来可能会被使用，但 Coinbase 的后端服务需要的是 gRPC 而不是 REST API Connectors。

“由于我们的规模，我们需要等待一段时间才能采用 Connectors，”Coinbase 的工程经理 Stephanie Saunders 在大会期间告诉我。将任何类型的代码部署到 Coinbase 的模式中都具有挑战性，因为它需要 15 到 20 分钟才能完成部署。“如果部署的Connectors 出现问题，回滚需要很长时间——20 分钟的高容量错误是不可接受的，”Saunders 说。

Saunders 说，在考虑扩展阈值时，使用 Connectors 的方法可能是有益的。“例如，如果我们模式的某个部分没有高吞吐量，只要缓存策略足够，直接进行 API 调用可能是有意义的，”Saunders 说。“但以我们目前的吞吐量，它不一定会解决我们所有的问题——你总是需要一台服务器。”

Apollo 之所以为 REST 设计 Connectors，是因为它仍然是最流行的 API 格式。“我们的愿景是将每个 API 都引入图中，”DeBergalis 说。除了寻求涵盖 gRPC 或 Thrift 等现代替代方案外，Connectors 最终还应扩展到 SOAP 和 XML-RPC 等传统 API。“一些公司甚至在大型机上构建图，”DeBergalis 说。

> [@GraphQL] 越能自动完成 API 的编排联合，开发人员就越不需要担心管理基础设施，从而可以专注于他们的工作。这是我在 [#GraphQLSummit] 和 [@apollographql] 首席技术官 [@debergalis] 的主题演讲中获得的收获之一。[pic.twitter.com/ziqSfr5QUm]—— BC Gain (@bcamerongain)

最终目标是让开发人员能够自由地减少手动拼接 API 的时间。Connectors 允许直接实现 GraphQL 以协调 GraphQL 层下的 API，因此他们可以将更多时间花在创造性的开发工作上。DeBergalis 说，在生物研究等纯科学领域，情况也是如此，因为生物研究已经变得更加依赖计算。

“软件已经彻底改变了生物研究。这是一个有趣的类比，因为虽然电子商务公司的专业软件开发人员可能是专家，但想想研究生——他们知道如何编写软件，但他们不会整天研究最新的 API 设计模式，”DeBergalis 说。“他们还有更重要的工作要做……因此，如果我们能让更多的人编写有用的软件，我们就能发现新药，解开宇宙的奥秘——这很酷。”