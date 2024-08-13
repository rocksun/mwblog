# GraphQL 与 OpenAPI：数据治理的优缺点

![Featued image for: GraphQL vs. OpenAPI: Pros and Cons for Data Governance](https://cdn.thenewstack.io/media/2024/08/3c0941ef-star-wars-vs-star-trek-1024x576.jpg)

[Flickr](https://flic.kr/p/834e93))

可口可乐 vs. 百事可乐 … 阿里 vs. 弗雷泽 … 星球大战 vs. 星际迷航 … 苹果 vs. 微软 … GraphQL vs. OpenAPI …

好吧，我只是在夸张。我不认为 GraphQL vs. OpenAPI 能与那些其他粉丝群体相提并论。但在 API 标准领域，[GraphQL](https://graphql.org/) 和 [OpenAPI](https://swagger.io/specification/) 作为企业中两个重要的框架脱颖而出。

[API](https://roadmap.sh/api-design) 在数据消费中发挥着至关重要的作用，并且通过代理，在确保健全的数据治理方面至关重要。无数关于 [数据网格](https://arxiv.org/pdf/2304.01062.pdf) 架构的文章都表达了相同的观点。良好的数据治理和强大的 API 治理，再加上收集和使用 API 生成的元数据，对于洞察消费、建立反馈循环和开发自我纠正流程至关重要。

那么，贵组织的 [API 策略](https://thenewstack.io/supergraph-a-solution-for-api-orchestration-and-composition) 是什么？这些选择如何影响数据治理目标？拥有目标状态并有意识地付出回报。如果您从事数据治理但不在技术领域，您仍然需要参与 API 治理，并明确表明您在架构中拥有权益。如果您从事技术并支持数据治理活动，您必须倡导 [加强数据治理的选择](https://thenewstack.io/make-data-governance-automation-suck-less-with-a-supergraph/)。

## OpenAI vs. GraphQL：异同

虽然还有其他 API 标准存在——例如 REST、gRPC、SOAP 和 JSON-RPC（或者您的 Sierra Mists、Battlestar Galacticas 或 Linuxes，如果您愿意）——但我将重点关注 GraphQL 和 OpenAPI 作为一种具体的方式来思考这些选择，但您可以将这些想法应用于您最喜欢的 API 标准。

[GraphQL](https://roadmap.sh/graphql) 和 OpenAPI 都定义了数据消费者和提供者之间的协议，但它们在功能和合同规范方面存在重大差异。无论您使用哪种，都必须有意识地进行操作，了解您的用例并为最佳结果进行设计。

现在基础知识已经讲完了，让我们比较一下 GraphQL 和 OpenAPI，并根据五个关键标准评估它们与数据治理的相关性：统一语义层、数据访问、可组合性、未来方向和可扩展性，然后看看哪一个更适合数据治理。

### 统一语义层

API 必须在多个数据生产者之间建立和维护一个统一的语义层（或 [数据访问模型](https://supergraph.io/?utm_campaign=the-new-stack&utm_source=the-new-stack&utm_medium=referral&utm_content=graphql-vs-opanapi)）。它是一个控制层，定义实体和关系，支持数据目录，使数据请求保持一致，为治理活动提供元数据，并帮助指导和组织正确的数据使用。

#### GraphQL

GraphQL 端点包括以平台无关术语定义的数据实体、属性和关系。它可以作为单个工件进行管理，也可以通过网关进行联合。关系使用 Schema Definition Language (SDL) 指定，其中包括其类型系统中的标量、枚举、接口和联合。

#### OpenAPI

OpenAPI 使用 JSON Schema 标准来定义数据类型和 API 端点的數據驗證模型。与 GraphQL 一样，您也可以以联合方式管理 OpenAPI 端点。每个端点通过 URL 方案表达与其他 OpenAPI 文档之间的关系。从历史上看，使用 JSON Schema 维护和演化大型统一数据模型一直很困难。

### 数据访问

API 必须提供与数据产品一致的数据访问方法。它们需要面向技术的自助服务功能，执行细粒度（字段级）访问控制，并支持各种客户端传输和协议。

#### GraphQL

GraphQL 允许您指定哪些数据元素可以直接 [查询](https://www.digitalocean.com/community/tutorials/understanding-queries-in-graphql) 或订阅。由于客户端在字段级别请求数据，因此您可以在语义层内实现细粒度访问控制。

### EDITOR'S RESPONSE
可以请求的元素（或用 GraphQL 术语来说，查询类型根部的元素）类似于“[数据产品](https://medium.com/data-mesh-learning/what-exactly-is-a-data-product-7f6935a17912)”并且与底层数据集有很强的关联性。从最广泛的定义来看，数据产品可以是任何东西，从单个数据集到 360 度客户报告应用程序。定义是一个很滑坡的概念，但在我看来，GraphQL SDL 在定义类似于[数据产品](https://martinfowler.com/articles/data-monolith-to-mesh/data-product.png)的数据目录方面做得很好，至少在狭义的定义上是如此。

GraphQL 还允许您指定其他谓词来细化请求，例如过滤器或排序。它可以描述如何删除、更新或创建其他数据（称为变异），这是支持操作工作负载所必需的。此外，您可以定义片段，它们类似于子例程，用于可重用性和可组合性。

GraphQL 的查询语言没有包含其他标准，如 HTTP 或 REST。它对客户端和服务器如何通信请求和结果是不可知的。服务器从 HTTP POST 或持久套接字（订阅）提供 HTTP JSON 负载。社区解决方案提供基于文件格式的负载和 gRPC 客户端。商业 GraphQL JDBC 驱动程序支持基于 SQL 查询的请求。

#### OpenAPI
OpenAPI 以[JSON Schema](https://json-schema.org/)为基础，并依赖于 HTTP REST。虽然开发人员使用 REST 动词（GET、POST、PATCH 等）来定义操作的类别，但 OpenAPI 工具不会强制执行它们的用法。所有事务都通过 HTTP 进行，允许 API 通过统一资源标识符 (URI) 路径、查询或 HTTP 请求主体来定义其输入。

开发人员通常使用 JSON Schema 标准来管理必需或可选的输入。在这种方法中，您在远程过程调用 (RPC) 级别定义访问控制。响应自定义是专有的，因为 OpenAPI 标准中不存在此类概念。API 可以以任何格式定义其负载，因此 JSON 和文件格式负载都是可能的。

### 可组合性
[可组合性](https://hasura.io/blog/the-future-of-api-is-composability?utm_campaign=the-new-stack&utm_source=the-new-stack&utm_medium=referral&utm_content=graphql-vs-opanapi)减轻了数据生产者的负担，并为客户端提供了额外的自助服务功能。它允许生产者生成更通用的数据产品，这些产品比特定用例更进一步；因此，它们更具可重用性。在数据访问的背景下，可组合系统具有四个关键特征：
**形状：**通过指定其数据元素、组织以及它们之间的任何关系来定义响应的结构或形状。**组合：**将数据产品（表、视图或 API）组合成一个有凝聚力的整体。这些数据产品可以在不同的操作中重复使用。**重用：**通过定义概念（如数据产品、查询片段或关系）来强调可重用的构建块，为灵活的组合奠定基础。**定制：**通过组合组件来实现所需的结果，为特定用例或逻辑操作定制数据响应。
#### GraphQL
GraphQL 的查询语言允许请求者定义所需的数据元素并遍历定义的数据关系。服务器处理遍历关系并将请求作为单个结果返回。定义关系的可重用性是[GraphQL 提供可组合性](https://thenewstack.io/supergraph-a-solution-for-api-orchestration-and-composition/)的一种方式——GraphQL 的超能力。

#### OpenAPI
OpenAPI 缺乏一种标准化的方法来声明所需的数据元素或重用关系来定义复杂的请求。因此，客户端处理数据组合，这通常会导致过度获取数据以及前端和后端系统之间多次调用以拼接单个逻辑请求。

不必要的数据移动会产生成本，包括数据治理的成本。在受治理的环境中过度获取数据会增加监控和安全性的复杂性和成本，尤其是在受监管的环境中。

### 未来重点
为了评估 API 标准的可行性，请提出以下问题：该标准未来与以数据为中心的用例保持一致的可能性有多大？它的使命如何与以数据为中心的用例保持一致？是否存在可能使其演变复杂化的依赖关系或约束？

#### GraphQL
GraphQL 是一种自包含、连贯、开放的标准，专注于以数据为中心的 API，并得到一个活跃的标准机构的支持。下一代将专注于联邦和流式传输等问题，以适应其他以数据为中心的用例，并提高其与[数据网格架构](https://thenewstack.io/designing-a-data-mesh-to-reign-in-data-sprawl)的一致性。

#### OpenAPI
OpenAPI 缺乏一种标准化的方法来声明所需的数据元素或重用关系来定义复杂的请求。因此，客户端处理数据组合，这通常会导致过度获取数据以及前端和后端系统之间多次调用以拼接单个逻辑请求。

不必要的数据移动会产生成本，包括数据治理的成本。在受治理的环境中过度获取数据会增加监控和安全性的复杂性和成本，尤其是在受监管的环境中。

### 未来重点
为了评估 API 标准的可行性，请提出以下问题：该标准未来与以数据为中心的用例保持一致的可能性有多大？它的使命如何与以数据为中心的用例保持一致？是否存在可能使其演变复杂化的依赖关系或约束？

#### GraphQL
GraphQL 是一种自包含、连贯、开放的标准，专注于以数据为中心的 API，并得到一个活跃的标准机构的支持。下一代将专注于联邦和流式传输等问题，以适应其他以数据为中心的用例，并提高其与[数据网格架构](https://thenewstack.io/designing-a-data-mesh-to-reign-in-data-sprawl)的一致性。

#### OpenAPI
OpenAPI relies on JSON Schema and HTTP REST. Its goal is to allow humans and computers to understand APIs without access to source code. This "standard mashup" presents challenges (perhaps solvable) in terms of tooling, and its goal is not data-centric, but rather more open. [OpenAPI's next iteration](https://github.com/OAI/sig-moonwalk), version 4, will focus on AI and generative AI (GenAI).

### Extensibility
A well-designed standard should incorporate extensibility in a numerically friendly and maintainable way to meet unique organizational needs.

#### GraphQL
GraphQL is designed to be extensible and features capabilities such as custom directives, custom scalars, and extensible types. Directives modify the behavior of operations. GraphQL defines standard directives, such as `@deprecated`, which indicates that a field is obsolete. Additionally, it can define custom directives, such as `@source`, which can record the expected physical address of a data element. Custom scalars can represent concepts such as large numbers, dates, or geographic coordinates in specific use cases (e.g., scientific computing).

#### OpenAPI
OpenAPI has limited extensibility based on convention. You must add custom metadata to the OpenAPI specification by creating custom fields using the `x-<tag-name>` type of notation. This convention effectively tells any standard tool to ignore these fields.

### Final Assessment: Alignment with Data Governance
This will never be a binary decision. However, establishing standards and providing thoughtful guidance for practitioners will have a significant impact on data governance outcomes. Within the limited scope I have set, here is my assessment.

#### GraphQL
GraphQL SDL has a sophisticated type system, [a well-defined query language](https://hasura.io/blog/getting-started-with-react-query-and-graphql?utm_campaign=the-new-stack&utm_source=the-new-stack&utm_medium=referral&utm_content=graphql-vs-opanapi), and a flexible, structured approach to extensibility. As a data-centric API standard, it can do everything OpenAPI can do. Aligning metadata with underlying data sources is more direct, and tooling makes it easier to support data governance requirements.

Due to its specialized focus, GraphQL can provide reference libraries implemented in multiple languages. These libraries parse GraphQL schemas and queries and connect them to code, facilitating database and business logic integration into responses.

This request processing model provides hooks to support data governance objectives. For example, it can evaluate and record data accuracy or track data usage with rich contextual information. This well-designed edge data processing model is adaptable and customizable to meet data governance needs.

#### OpenAPI
OpenAPI is widely used, well-known, and loved by many developers. While you can build a data delivery platform using OpenAPI, it will be more DIY. You will need to make additional design decisions and acquire tooling to make this strategy support data governance objectives.

## Conclusion
GraphQL, as an API strategy that supports a semantic layer between a set of distributed data producers, has many advantages. Five years ago, it was hard to take GraphQL seriously, but the technical landscape has changed. Hand-coding GraphQL resolvers is [not on my wish list](https://thenewstack.io/is-graphql-over-or-do-we-just-need-to-rethink-it); what makes this possible is automated GraphQL. There are reputable vendors with excellent GraphQL automation capabilities, making it a viable and attractive approach.

OpenAPI, gRPC, and API gateway vendors are also practical solutions. They are more aligned with historical practices and perhaps easier for some stakeholders to "accept." But they are less capable out of the box. Establishing internal standards and practices to maintain lineage with underlying data, generate audit evidence, manage fine-grained access control, and support a consistent experience across multiple client protocols requires technical leadership, architecture, and design in a distributed data delivery environment, which is difficult to achieve.

[
YOUTUBE.COM/THENEWSTACK
Technology is moving fast, don't miss a beat. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)