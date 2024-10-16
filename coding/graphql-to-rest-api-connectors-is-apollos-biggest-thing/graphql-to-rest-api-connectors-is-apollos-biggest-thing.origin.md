# GraphQL-to-REST API Connectors Is Apollo’s ‘Biggest Thing’
![Featued image for: GraphQL-to-REST API Connectors Is Apollo’s ‘Biggest Thing’](https://cdn.thenewstack.io/media/2024/10/af96afdf-behnam-norouzi-c-rgxbo1oiq-unsplash-1024x658-1.jpg)
NEW YORK — The release of [Apollo GraphQL](https://www.apollographql.com/?utm_content=inline+mention) Connectors during [Apollo’s GraphQL Summit 2024 conference](https://summit.graphql.com/) here marks one of Apollo’s most significant innovations to date in simplifying [API integration](https://thenewstack.io/solving-api-integration-and-aggregation-with-supergraph/).

With the introduction of Apollo Connectors for [REST APIs](https://thenewstack.io/the-state-of-introspection-for-rest-and-graphql-apis/), developers can integrate REST APIs into a [federated GraphQL](https://thenewstack.io/graphql-federation-the-missing-api-for-your-platform-strategy/) schema incrementally or all at once. Yes, you could previously integrate REST APIs with GraphQL but it involved manually implementing code — and let’s just say it was a finicky process.


[@apollographql]´s[@debergalis]: «Connectors really changes the perspective of what[@GraphQL]is for you and for your teams. it’s the biggest thing we’ve ever shipped. »[#graphqlsummit][@thenewstack][pic.twitter.com/bsa6Y8SZbB]— BC Gain (@bcamerongain)

[October 9, 2024]
As “the biggest thing we’ve ever shipped,” as [Matt DeBergalis,](https://www.linkedin.com/in/debergalis) CTO and co-founder of Apollo GraphQL, described it, Connectors offers a way to translate a REST API (more APIs coming) into the [GraphQL](https://thenewstack.io/the-unlikely-journey-of-graphql/) language. Previously without a Connector, in order to achieve this, you would need a small piece of middleware code called a GraphQL Server. “You only have to create it once for each API, but it requires intricate, specific knowledge to complete,” DeBergalis said.
## Eliminate Complexity
In other words, as mentioned below, the process is otherwise a more time-consuming process without a Connector.

“Connectors eliminate this complexity. They simplify the process by removing much of the upfront design work related to shaping your GraphQL layer. Connectors take a more pragmatic approach, eliminating the need to write the server altogether,” DeBergalis said. “This also gets rid of the extra network hop, performance costs, and everything associated with running a server in production.”

Designed to reduce the amount of code that a [DevOps](https://thenewstack.io/devops/) team member might have to write, Connectors allow all APIs to be combined into an Apollo Supergraph comparatively quickly. “This approach unlocks an extraordinary amount of value, as many businesses have APIs, but their value depends on how easily they can be utilized,” DeBergalis said. “How usable are these APIs? How exposed are they? How quickly can they be combined together? The companies that can achieve this will be the ones that ship and innovate faster.”

Just as GraphQL has emerged as the modern, standards-based way to connect REST APIs, GraphQL is also not going to eventually replace REST APIs. REST APIs also have functionality that GraphQL may not be able to provide. While both support fetching data from a backend system, they solve different problems and approach data from different ends of the spectrum.

To wit, GraphQL provides a strongly typed schema definition language to describe data that lives across any number of systems in a way that is intuitive and useful to clients. By contrast, REST encourages a more resource-oriented approach to organizing and deploying services, usually along domain boundaries. It’s more focused on modeling entity relationships than it is on serving data to the client in a demand-driven way.

“We’re not here to displace REST…We’re really not here saying that GraphQL is better than the APIs that you’ve got. It’s not better than gRPC. It’s not better than REST,” DeBergalis said during his GraphQL Summit 2024 conference keynote. “That’s not the point. It makes those things better, right?”

Apollo’s Apollo Federation — used for building a federated GraphQL infrastructure — provides a federated graph layer with GraphQL in order to abstract the complexity of REST endpoints. The graph layer exposes a single endpoint for all operations instead of the otherwise hundreds of unique REST endpoints with less programming involved. With the release of Connectors, this abstraction capability involves much less coding and manual input than was previously necessary to integrate each REST API.

More specifically, there were a number of extra steps developers had to take when adding a REST service to a federated GraphQL API prior to the release of Connectors, as Apollo’s [Dylan Anthony](https://www.linkedin.com/in/dylan-anthony/) communicated in a [blog post:](https://www.apollographql.com/blog/apollo-connectors-for-rest-apis)

- Identify a programming language and an Apollo Federation-compatible GraphQL framework.
- Deploy a new subgraph service, including monitoring, auto-scaling and load-balancing, which will sit in between the router and the REST API.
And with each change to the REST API, Anthony described how:

- The subgraph schema for the underlying REST data must be designed.
- Bindings to the REST API in the chosen programming language must be written.
- Resolvers that leverage those bindings must be written.
- The subgraph service must be deployed.
- The schema to update the router must be composed and published.
With Apollo Connectors, Anthony described how each iteration is reduced to:

- Designing the subgraph schema for the underlying REST data.
- Composing and publishing the schema to update the router so the router then “speaks” directly to the REST APIs:
## Coinbase Weighs In
However, there is more to the world than REST APIs. In the case of cryptocurrency exchange platform provider Coinbase, the Connectors may be used in the future, gRPC and not REST API Connectors are what is needed for Coinbase’s backend services.

“Due to our scale, we would need to wait a while before adopting Connectors,” [Stephanie Saunders](https://graphql.org/conf/2023/speakers/stephanie.saunders2), engineering manager at [Coinbase,](https://www.coinbase.com/) told me during the conference. Deploying any kind of code into Coinbase’s schema is challenging because it takes 15 to 20 minutes to deploy. “If there’s a problem with a deployed connector, it takes a long time to roll back — 20 minutes of high-volume errors is not acceptable, Saunders said.

The approach using Connectors could be beneficial when considering a threshold for scaling, Saunders said. “For example, if there was a part of our schema that didn’t have high throughput, it might make sense for a straightforward API call as long as the caching strategy was sufficient,” Saunders said. “But with our current throughput, it’s not necessarily going to solve all our problems — you’ll always need a server.”

Apollo designed Connectors for REST because it is still the most popular API format. “Our vision is to bring every API to the graph,” DeBergalis said. In addition to looking to cover modern alternatives like gRPC or Thrift, Connectors should eventually extend to legacy APIs, such as SOAP and XML-RPC. “Some companies are even building graphs on top of mainframes,” DeBergalis said.

The more

[@GraphQL]can automate the federation of APIs for orchestration, the less developers have to worry about managing infrastructure so they can do their work. One of my takeaways from the[#GraphQLSummit]and[@apollographql]CTO[@debergalis]´s keynote.[pic.twitter.com/ziqSfr5QUm]— BC Gain (@bcamerongain)

[October 9, 2024]
At the end of the day, the goal is to allow developers the freedom to spend less time manually stitching together APIs. They can instead spend more time on the creative work of development as Connectors allows GraphQL to be directly implemented in order to orchestrate APIs underneath the GraphQL layer. In the area of pure science, such as biological research and how it has become more computational, DeBergalis said.

“Software has completely changed bioresearch. It’s an interesting analogy because, while professional software developers at an e-commerce company may be experts, think about grad students — they know how to write software, but they aren’t going to spend their days on the latest API design patterns,” DeBergalis said. “They have more important work to do… So, if we can enable many more people to write useful software, we’re going to discover new drugs and unlock the secrets of the universe — that’s cool.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)