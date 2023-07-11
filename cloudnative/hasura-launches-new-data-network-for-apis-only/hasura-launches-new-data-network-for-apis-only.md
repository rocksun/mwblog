# Hasura 推出仅适用于 API 的新数据网络

Hasura DDN 是一种新的边缘网络，使用 Graph Query Language ，旨在传输实时、流式和分析数据。

翻译自 [Hasura Launches New Data Network for APIs Only](https://thenewstack.io/hasura-launches-new-data-network-for-apis-only/) 。

![](https://cdn.thenewstack.io/media/2023/06/d767c613-alina-grubnyak-ziqkhi7417a-unsplash-e1687984562708-1024x683.jpg)

数据网络通常用于文件共享、应用程序操作或互联网访问，但如果一个网络严格用于分发应用程序编程接口又如何呢？毕竟， API 相当深奥，因为它不是标准数据，而是一套定义两个软件件如何相互交互的规则。

好吧，这个与众不同的系统现在确实存在，它旨在为开发人员提供巨大的幕后支持。

总部位于班加罗尔和旧金山的 [Hasura](https://hasura.io/) 近期推出了 [Hasura DDN](https://hasura.io/ddn)，这是一个使用 [Graph Query Language](https://thenewstack.io/tigergraph-supports-graph-query-langauge-opencypher/) 的新边缘网络，旨在传输实时、流式和分析数据。它使开发人员能够在全球范围内以低延迟/高性能运行数据 API ，无需额外努力和费用，根据该公司的说法。


Hasura CEO 和联合创始人 [Tanmai Gopal](https://www.linkedin.com/in/tanmaig/) 对 The New Stack 表示，这是“世界上第一个数据 CDN(内容分发网络)”，在该网络中，所有部署在 Hasura Cloud 上的项目都会自动部署到 100 多个全球区域的边缘网络。它预先连接了所有难以建立联系的网络节点和协议，这些节点和协议需要比它们应该进行的更长时间才能建立安全连接。Hasura 会自动将客户端请求路由到最接近客户端的 Hasura 实例，以最小化延迟。

该边缘网络与 CockroachDB、Amazon Aurora、Yugabyte 等分布式数据库集成，Gopal 说。公司不害怕保证 99.99% 的正常运行时间，这是一个重要的考虑因素， Gopal 说。

“我们的服务是多云和多区域的，我们确保人们可以将他们的事实来源连接到媒体上,” Gopal 说。“ EVN (思科的产品 Easy Virtual Network 简化了第 3 层网络虚拟化)成为其他应用程序的 API ，这些应用程序是外部的，以及其他微服务或 API - 任何东西 - 都可以连接到该层并获得访问权限。所以这就是我们思考它的方式。"

Hasura 的 GraphQL 引擎为新的或现有的 Postgres 数据库提供 GraphQL API 。使用查询，它可以即时组合一个由数据库和服务支持的 GraphQL API ，这样开发团队就可以立即高效地工作， Gopal 说。

## 多样数据的兴起

“过去几年发生的一个大变化是多样数据的兴起。一种通用数据库将无法满足所有需求,” Gopal 说。 “首先，您知道为了构建下一代应用程序，您将需要多个数据库(用于各种用例)。您会希望将通用数据库与 AI 相结合，用于向量数据库。 对于实时分析解决方案，同样，您需要其他东西来升级通用数据库。 所以系统正在变得多样化，这是这个目标的重点。

“第二个变化是我们在这么多不同的技术中拥有大量的数据。 只有统一它们，我们才能提取更多的价值，并能够构建下一代应用程序，以便为我们的用户增加价值。 这就是我们现在看到的，这也解释了现在将其作为基础架构层的时机。”

Hasura DDN 得益于 Hasura 引擎的重大架构变更，该变更将其冷启动时间降低到 1 毫秒以下， Gopal 说。 因此，当 API 被调用时， Hasura 运行时可以在边缘区域上实例化，从而实现全球范围内的即时自动扩展以处理任何流量峰值。 数据人员会想知道 DDN 是一种按价值定价的经济高效方法，而不是基于基础设施定价和其他方法，比如始终打开或预热的实例，他说。

## 趋势:开发和管理 API 的新方法

“组织不应该局限于单一的 API 开发和集成方式,”企业策略集团的首席分析师 Paul Nashawaty 在接受 The New Stack 采访时表示。“组织往往没有意识到，存在更好的方法来启用在全球范围内创建和使用 API 性能。通过与分布式数据库集成， Harusa 最小化了从消费者到底层数据源的延迟。这可以与遗留和新的数据源一起实现。”

Hasura GraphQL 引擎包含了一些新功能，包括:

- **即时 GraphQL API**：该引擎可以在几秒钟内从 Postgres 数据库生成 GraphQL API ，使得启动和构建新功能变得容易。
- **内置授权**：包含一个内置的授权引擎，允许用户控制谁可以访问数据。
- **实时订阅**：支持实时订阅，允许用户随着数据的变化保持客户端的更新。
- **Webhooks**：该引擎还可以生成 webhooks ，允许用户在数据库中的某些事件发生时得到通知。这对于将 GraphQL API 与其他系统集成很有用。

Hasura 被各种公司使用，包括 Atlassian(为 Jira、Confluence 和 Bitbucket 提供GraphQL API)、GitLab(为 GitLab.com 提供 GraphQL API )和 Red Hat (为 OpenShift 提供 GraphQL API )。