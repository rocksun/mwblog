# GraphQL vs. OpenAPI: Pros and Cons for Data Governance
![Featued image for: GraphQL vs. OpenAPI: Pros and Cons for Data Governance](https://cdn.thenewstack.io/media/2024/08/3c0941ef-star-wars-vs-star-trek-1024x576.jpg)
[Flickr](https://flic.kr/p/834e93))
Coke vs. Pepsi … Ali vs. Frasier … Star Wars vs. Star Trek … Mac vs. PC … GraphQL vs. OpenAPI …

OK, I’m just being dramatic. I don’t think GraphQL vs. OpenAPI is quite on the level of those other fandoms. But in the realm of API standards, [GraphQL](https://graphql.org/) and [OpenAPI](https://swagger.io/specification/) stand out as two important frameworks within the enterprise.

[APIs](https://roadmap.sh/api-design) play a critical role in data consumption and, by proxy, are essential in ensuring sound data governance. Countless articles on [data mesh](https://arxiv.org/pdf/2304.01062.pdf) architectures make the same point. Good data governance and strong API governance, combined with harvesting and using the metadata produced by APIs, are critical to getting insight into consumption, establishing feedback loops and developing self-correcting processes.
So, what is your organization’s [API strategy](https://thenewstack.io/supergraph-a-solution-for-api-orchestration-and-composition)? How do those choices impact data governance objectives? Having a target state and being intentional pay off. If you are in data governance but not in technology, you still need to get involved in API governance and make it clear you have a stake in the architecture. If you are in technology and support data governance activities, you must advocate for [choices that strengthen data governance](https://thenewstack.io/make-data-governance-automation-suck-less-with-a-supergraph/).

## OpenAI vs. GraphQL: Similarities and Differences
While there are other API standards out there — such as REST, gRPC, SOAP and JSON-RPC (or your Sierra Mists, Battlestar Galacticas or Linuxes, if you will) — I’m focusing on GraphQL and OpenAPI as a concrete way to think through these choices, but you can apply these ideas to your favorite API standard.

[GraphQL](https://roadmap.sh/graphql) and OpenAPI both define agreements between data consumers and providers, but they have significant differences in capabilities and contract specifications. Whichever you use, it’s essential to be intentional, understand your use case and design for the best outcome.
So now that the basics are out of the way, let’s compare GraphQL and OpenAPI and evaluate their relevance to data governance based on five key criteria: unified semantic layer, data access, composability, future direction and extensibility, and then look at which is better for data governance.

### Unified Semantic Layer
An API must establish and maintain a unified semantic layer (or [data access model](https://supergraph.io/?utm_campaign=the-new-stack&utm_source=the-new-stack&utm_medium=referral&utm_content=graphql-vs-opanapi)) across multiple data producers. It is a control layer that defines entities and relationships, supports a data catalog, gives consistency to data requests, provides metadata to governance activities, and helps guide and organize proper data usage.

#### GraphQL
A GraphQL endpoint includes data entities, attributes and relationships defined in platform-agnostic terms. It can be managed as a single artifact or federated through a gateway. Relationships are specified using Schema Definition Language (SDL), which includes scalars, enumerators, interfaces and unions in its type system.

#### OpenAPI
OpenAPI uses the JSON Schema standard to define data types and the data validation model for an API endpoint. As with GraphQL, you can manage OpenAPI endpoints in a federated fashion. Each endpoint expresses relationships between other OpenAPI documents through a URL scheme. Historically, maintaining and evolving a large, unified data model using JSON Schema has been challenging.

### Data Access
APIs must provide a data access approach aligned with data products. They need tech-facing self-service capabilities, enforce fine-grained (field-level) access controls, and support a variety of client transports and protocols.

#### GraphQL
GraphQL lets you specify which data elements can be directly [queried](https://www.digitalocean.com/community/tutorials/understanding-queries-in-graphql) or subscribed to. Since clients request data at the field level, you can implement fine-grained access controls within the semantic layer.

The elements that can be requested (or in GraphQL terms, the elements at the root of the query type) are akin to a “[data product](https://medium.com/data-mesh-learning/what-exactly-is-a-data-product-7f6935a17912)” and have strong correlation to an underlying data set. In its broadest definition, data products can be anything from a single data set to a 360-degree customer-reporting application. Definitions are a slippery slope, but in my opinion, GraphQL SDL does an excellent job of defining something that looks a lot like a data catalog of [data products](https://martinfowler.com/articles/data-monolith-to-mesh/data-product.png), at least in its narrow definition.

GraphQL also allows you to specify additional predicates for refining the request, such as filters or sorts. It can describe how to delete, update or create additional data (known as mutations), which is required to support operational workloads. Additionally, you can define fragments, which are similar to subroutines, for reusability and composability.

GraphQL’s query language does not incorporate other standards like HTTP or REST. It is agnostic about how the client and server communicate the request and result. A server delivers an HTTP JSON payload from an HTTP POST or persistent sockets (subscriptions). Community solutions provide file format-based payloads and gRPC clients. Commercial GraphQL JDBC drivers support requests based on SQL queries.

#### OpenAPI
OpenAPI uses [JSON Schema](https://json-schema.org/) as its foundation and relies on HTTP REST. While developers use REST verbs (GET, POST, PATCH, etc.) to define the class of an operation; their use is not enforced by OpenAPI tooling. All transactions occur over HTTP, allowing an API to define its inputs through the Uniform Resource Identifier (URI) path, query or HTTP request body.

Developers usually manage required or optional inputs using the JSON Schema standard. In this approach, you define access controls at the Remote Procedure Call (RPC) level. Response customization is proprietary since no such concept exists in the OpenAPI standard. An API can define its payload in any format, so JSON and file-format payloads are possible.

### Composability
[Composability](https://hasura.io/blog/the-future-of-api-is-composability?utm_campaign=the-new-stack&utm_source=the-new-stack&utm_medium=referral&utm_content=graphql-vs-opanapi) reduces the burden on data producers and gives additional self-service capabilities to clients. It allows producers to generate data products that are more generalized and one step removed from specific use cases; therefore, they’re more reusable. Within the context of data access, a composable system has four key features:
**Shape:**Defines the response’s structure or shape by specifying its data elements, organization and any relationships between them.**Combine:**Assembles data products (tables, views or APIs) into a cohesive whole. These data products can be reused across different operations.**Reuse:**Emphasizes reusable building blocks by defining concepts (like data products, query fragments or relationships) to create a foundation for flexible composition.**Tailor:**Customizes a data response for a specific use case or logical operation by combining components to achieve a desired outcome.
#### GraphQL
GraphQL’s query language allows the requestor to define desired data elements and traverse defined data relationships. The server handles traversing relationships and returns the request as a single result. This reusability of defined relationships is one way [GraphQL provides composability](https://thenewstack.io/supergraph-a-solution-for-api-orchestration-and-composition/) — GraphQL’s superpower.

#### OpenAPI
OpenAPI lacks a standardized approach to declaring desired data elements or reusing relationships to define a complex request. As a result, the client handles data composition, which often leads to over-fetching data and multiple calls between frontend and backend systems to stitch together a single logical request.

Unnecessary data movement incurs costs, including for data governance. Over-fetching data in a governed environment increases complexity and costs for monitoring and security, particularly in regulated environments.

### Future Focus
To assess an API standard’s viability, ask questions like: What is the probability the standard will align to data-centric use cases moving forward? How does its mission align with data-centric use cases? Are there dependencies or constraints that may complicate its evolution?

#### GraphQL
GraphQL is a self-contained, coherent, open standard focused on data-centric APIs, supported by an active standards body. The next iteration will focus on issues like federation and streaming to adapt to additional data-centric use cases and improve its alignment with [data mesh architectures](https://thenewstack.io/designing-a-data-mesh-to-reign-in-data-sprawl).

#### OpenAPI
OpenAPI relies on JSON Schema and HTTP REST. Its stated purpose is to allow humans and computers to understand an API without access to source code. This “standards mashup” creates challenges in tooling (perhaps solvable), and its stated purpose is not data-centric but more open-ended. [The next iteration of OpenAPI](https://github.com/OAI/sig-moonwalk), version 4, will focus on AI and generative AI (GenAI).

### Extensibility
A well-designed standard should incorporate extensibility in a digital-friendly, maintainable way to address unique organizational needs.

#### GraphQL
GraphQL is designed to be extensible and has features like custom directives, custom scalars and extendable types. Directives modify the behavior of operations. GraphQL defines standard directives like `@deprecated`
, which indicates that a field has a sunset. Additionally, it can define custom directives, e.g., `@source`
, which could document a data element’s expected physical address. Custom scalars can represent concepts like huge numbers, dates or geographical coordinates for specific use cases, like scientific computing.

#### OpenAPI
OpenAPI has limited extensibility based on conventions. You must add custom metadata to an OpenAPI specification by creating custom fields with an `x-<tag-name>`
type of notation. This convention effectively tells any standard tooling to ignore these fields.

### Final Assessment: Alignment to Data Governance
It’s never going to be a binary decision. However, establishing standards and providing thoughtful guidance to practitioners will make a meaningful difference in data governance outcomes. Within the limited scope I set, here is my assessment.

#### GraphQL
GraphQL SDL has a sophisticated type system, a [well-defined query language](https://hasura.io/blog/getting-started-with-react-query-and-graphql?utm_campaign=the-new-stack&utm_source=the-new-stack&utm_medium=referral&utm_content=graphql-vs-opanapi) and a flexible, structured extensibility approach. As a data-centric API standard, it can accomplish everything that OpenAPI can. Aligning to underlying data sources is more straightforward with metadata, and tooling makes it easier to support data governance requirements.

Due to its specialized focus, GraphQL can offer reference libraries implemented in multiple languages. These libraries parse GraphQL schemas and queries and connect them to code, facilitating the integration of databases and business logic into a response.

This request-handling model provides hooks that support data governance objectives. For example, it can evaluate and record data accuracy inline or track data use with rich contextual information. This well-designed, at-the-edge data-processing model is adaptable and customizable to meet data governance needs.

#### OpenAPI
OpenAPI is widely used, well-known and beloved by many developers. While you can build a data delivery platform with OpenAPI, it will be more DIY. You will need to make additional design decisions and acquire tooling to make this strategy support data governance objectives.

## Conclusion
GraphQL, as an API strategy supporting a semantic layer across a group of distributed data producers, has many advantages. It would have been hard to take GraphQL seriously five years ago, but the technology landscape has evolved. Hand-coding GraphQL resolvers is [not on my bucket list](https://thenewstack.io/is-graphql-over-or-do-we-just-need-to-rethink-it); what makes this feasible is automated GraphQL. There are credible vendors with excellent GraphQL automation capabilities that make this a viable and attractive approach.

OpenAPI, gRPC and API gateway vendors are also practical solutions. They align more with historical practices and perhaps are an easier “sell” to certain stakeholders. But they are less capable out of the box. Establishing internal standards and practices to maintain lineage back to underlying data, generating audit evidence, managing fine-grained access controls and supporting consistent experiences across multiple client protocols requires technical leadership, architecture and design across a distributed data delivery environment, and that’s hard to do.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)