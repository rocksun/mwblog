# Apollo: GraphQL Now Connects to REST APIs With Little Fuss
![Featued image for: Apollo: GraphQL Now Connects to REST APIs With Little Fuss](https://cdn.thenewstack.io/media/2025/03/9137345f-alex-shuper-2iz9r2pgjjq-unsplash-1-1024x576.jpg)
Many, if not most, engineers and operations architects are well acquainted with the unfortunate conundrum of API sprawl, largely driven by BFF as a layer consisting of [REST APIs](https://thenewstack.io/rest-still-outshines-graphql-for-many-api-use-cases/). As the organization scales, the backend-for-frontend (BFF) pattern supporting the REST APIs can become unmanageable and certainly time consuming to separately update with code.

[GraphQL](https://thenewstack.io/graphql-growth-explodes-but-so-do-problems-federated-graphs-solve/), as an open standard, has demonstrated its merit in addressing this challenge to orchestrate APIs. But while organizations have long sought to integrate REST APIs with GraphQL, the process of separately integrating each API has remained a widespread and persistent pain point.
Now, Apollo has announced the general availability of Apollo Connectors for REST APIs. With it, organizations can define a GraphQL schema in terms of the REST APIs an organization has and orchestrate calls to those APIs with just a few lines of configuration.

“There are a lot of disadvantages when you’ve got teams frantically writing procedural code instead of using declarative alternatives through GraphQL,” [Matt DeBergalis,](https://www.linkedin.com/in/debergalis) CTO of [Apollo Labs](https://www.apollographql.com/events/new-innovations-from-apollo-dont-miss-out?utm_campaign=2025-01-29_new-innovations-from-apollo-dont-miss-out&utm_medium=newsletter&utm_source=tns&utm_content=inline-mention), told me.

Additionally, Router 2.0 is now generally available, and according to Apollo, it offers over a 10x performance boost for large-scale GraphQL deployments.

Apollo has also introduced a new free pricing plan for Apollo GraphOS, allowing teams to start small and scale without upfront investment. This plan includes access to trial features and connectors, making it easier for teams to adopt and expand their use of GraphQL. Organizations can get started free of charge by accessing [GitHub](https://github.com/apollographql/connectors-community) and downloading the applicable Apollo code with GraphQL.

Just as GraphQL has emerged as the modern, standards-based way to connect REST APIs, GraphQL is also not going to eventually replace REST APIs. REST APIs also have functionality that GraphQL may not be able to provide. While both support fetching data from a backend system, they solve different problems and approach data from different ends of the spectrum.

To wit, GraphQL provides a strongly typed schema definition language to describe data that lives across any number of systems in a way that is intuitive and useful to clients. By contrast, REST encourages a more resource-oriented approach to organizing and deploying services, usually along domain boundaries. It’s more focused on modeling entity relationships than it is on serving data to the client in a demand-driven way. The idea is to have the best of both worlds: more seamless — or pain free — integration depending on how you look at and the benefits of both REST APIs and GraphQL.

“We’re not here to displace REST. We’re really not here saying that GraphQL is better than the APIs that you’ve got, which might also include [gRPC](https://thenewstack.io/grpc-delivers-on-the-promise-of-a-proxyless-service-mesh/) and others,” DeBergalis said. “The motivation behind what we’ve done with REST connectors that we announced last week is that there’s an enormous pain point in the industry now that we’ve got 20-plus years of ‘80 eyes’ at every company.”

The majority of the APIs to manage are REST, but there are others as well. In addition to the above-mentioned gRPC APIs, there are others, such as [SOAP APIs](https://thenewstack.io/api-management-for-asynchronous-apis/) that “go back even further in the past,” DeBergalis said. “APIs are the building blocks of the business. They’re the resources, or the capabilities, of a company,” DeBergalis said.

![](https://cdn.thenewstack.io/media/2025/03/638a0ca1-capture-decran-2025-03-04-175820.png)
It is possible to configure and manage GraphOS Router with YAML.

It is not uncommon for some organizations to have 50 or more APIs to manage. “That’s the consequence of cloud native, microservices and the rise of [SaaS products](https://thenewstack.io/private-saas-is-coming-are-you-ready/): having APIs that we have to integrate with,” DeBergalis said. “When you look at all the companies that have adopted Apollo, the problem you’re solving is an orchestration problem: How do you connect all those APIs to the software we want to write? And that’s about how you call those APIs in the right order. How do you chain them together? How do you transform the results? How do you make them asynchronous when you need them for real-time applications?”

There’s a long list of technical tasks that engineers have to do anytime they want to build something, DeBergalis said. They often must manage app development, switching from legacy systems, integrating AI and moving to microservices. For an organization with a legacy monolithic architecture, with M&As, organizations must integrate separate products into a consistent user experience, DeBergalis said.

“You know, my guess is that a healthy fraction of the total time developers spend is on orchestration code, and it’s nuts — I mean if you look at the rest of the cloud native stack, it’s all moved to this declarative approach where we don’t write code in order to deploy software onto cloud hosts,” DeBergalis said. “Code is risky to write: it’s slow, it increases performance overhead and it harms the security footprint.”

## Standard Standards
GraphQL is an open standard. While Apollo offers an enterprise version of GraphQL and the associated GraphOS platform, Apollo does not directly control the standard. Instead, the governance structure is such that GraphQL standard is managed by the Linux Foundation’s [GraphQL Foundation](https://thenewstack.io/rest-vs-graphql-solving-api-challenges-in-modern-data-transfers/). This means the risks of the standard becoming proprietary are virtually nil.

“I think standards-based technologies are critical, and it’s the advice that we certainly give anybody when you think about your API strategy — you’ve got to think in terms of 10-20+ years,” DeBergalis said. “That means you’ve got to start with a standards-based approach, because the strategy should remain in place for a long time.

With GraphQL and GraphOS, it is possible to create a core governance and management structure for operation. “If you’re going to think about what it’s like to build an orchestration tier in a large organization with thousands of APIs and you’ve got hundreds of developers collaborating together, you need more than just the core machinery — you need a whole product around that that addresses questions around collaboration, governance, workflows and so on. That’s our product: GraphOS, which any developer can use for free so they can try everything that comes along with not just the core Connectors, but also the tools and the systems that we have to help teams scale,” DeBergalis said. “That’s just part of our mission — to make sure that this approach is something every developer can try and experience and ultimately becomes the preferred choice in every organization.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)