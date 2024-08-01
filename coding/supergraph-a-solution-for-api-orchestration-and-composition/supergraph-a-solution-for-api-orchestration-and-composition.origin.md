# Supergraph: A Solution for API Orchestration and Composition
![Featued image for: Supergraph: A Solution for API Orchestration and Composition](https://cdn.thenewstack.io/media/2024/07/58aa37e9-screenshot-2024-07-30-at-9.46.08 am-1024x570.png)
In the [previous post in this series](https://thenewstack.io/solving-api-integration-and-aggregation-with-supergraph/), we discussed the complexities of building and consuming APIs in enterprise data landscapes. These environments involve multiple data domains managed by different teams and numerous applications, leading to challenges due to constrained resources and conflicting goals.

[The Supergraph Architecture Framework (SAF)](https://thenewstack.io/hasura-visualizes-data-api-integration-into-a-supergraph/), developed from our experience with federated data access and GraphQL federation, addresses these challenges by proposing strategies for constructing domain APIs (subgraphs) and data access API platforms (supergraphs).
This framework offers an operating model for team collaboration, acting as an API marketplace with API producers and consumers. It facilitates onboarding API producers, provides high-quality supergraph APIs for consumers and emphasizes high-quality domain APIs with capabilities like filtering, sorting and pagination.

The SAF lays the foundation for an operating model and system design that enable federated domain ownership. In enterprise data and API landscapes, this helps address challenges with [federated data access](https://thenewstack.io/the-case-for-a-federated-data-access-layer-with-graphql/) and makes use cases like API orchestration and API composition easier to tackle.

## API Orchestration
API orchestration involves managing multiple API calls and sequencing the requests and results to perform a complex task or workflow. In our reference context, an example of API orchestration might involve the following sequence:

**Restaurant API**: Check menu and availability.**Payment API**: Process the payment.**Delivery API**: Schedule the delivery.
The orchestration layer handles these steps in sequence, ensuring each step completes successfully before moving to the next, and combines their responses into a single, cohesive outcome for the user.

## Challenges With API Orchestration
Orchestration is largely driven by the API consumers based on end user requirements. It is challenging, as it typically spans multiple domains. Orchestration using traditional methods requires the same type of “glue” code/endpoints that aggregation does — only in this case, that glue is more complex, as we can see from our example. Orchestration also usually involves multiple mutations, which further compounds the challenge.

Once again, we’ve run into the challenge of ownership: Should the consumer team own orchestration code? Does that team have the necessary skills to build performant orchestration endpoints? These are all operational challenges that need to be addressed to build a powerful orchestration layer on top of domain APIs/data.

## Solving API Orchestration Challenges
A good API platform must provide the semantics for definition of complex workflows that may be interspersed with business logic functions. Similar to the way supergraph architecture allows for relationships between domain CRUD APIs and business logic, the response of API calls can be chained to functions that can act independently (or even call other CRUD APIs from the supergraph) or vice versa.

The substrate for this capability is made possible by the fact that every piece of data from any source (databases, APIs, etc.) and types in business logic code are standardized on the supergraph’s semantic layer. This enables a supergraph to provide the semantics for developers, including API consumers, to articulate a workflow using just declarative configuration.

Integrations with third-party orchestration software like Camunda, Orkus, Temporal, etc., make this experience even more seamless for developers. Read more about [API orchestration](https://supergraph.io/docs/use-cases/api-composition/#solving-api-orchestration).

Problem |
Solution |
New workflows need new orchestration endpoints. | Supergraph requires that API consumers have the ability to self-serve demand for new workflows using declarative config. |
Authoring workflows requires knowledge of backend systems engineering. | Supergraph configuration is declarative, which democratizes the ability to engineer scalable workflows. |
## API Composition
API composition, which can be thought of as a special case (or evolution) of API integration and orchestration, refers to the technique of combining multiple API responses into a single unified response with hierarchical information from the different calls. Put another way, composition fetches related data from disparate sources in a cohesive way — so, aggregation and orchestration for a read operation. An example of API composition would be the following data for a user of our food delivery application:

- The user’s past orders.
- For each order, get some information about the restaurant where the order was placed.
- For each order, get payment information.
Getting this information involves making a request to three different domains in a sequence, at each step using the response from the previous, and finally combining the overall result set into a single hierarchical response that represents the relationship between the three entities (orders, restaurants and payments).

## Challenges With API Composition and How To Solve Them
Supergraph(QL) architecture advocates for awareness of the underlying sources or domain and standardization across a set of a heterogeneous set of sources. This allows a supergraph to provide a self-service model for API composition, without requiring any custom development, by making available the following two capabilities:

**Joins**: Fetch data from A and related data from B.**Nested filters**: Fetch data from A, filtered by a property value of its related data B.
Problem |
Solution |
Every data composition permutation needs an composition endpoint. | A supergraph automates composition with declarative relationship definitions between data across sources. If the relationships from the same source can be inferred programmatically, the supergraph can automate this. |
Authoring workflows requires knowledge of backend systems engineering. | Supergraph configuration is declarative, which democratizes the ability to engineer scalable workflows. |
Read more about [API composition](https://supergraph.io/docs/use-cases/api-composition/).

## Conclusion: A Practitioner’s API Platform Design Checklist
Building on the work from the previous post on the Supergraph Architecture Framework, we can compile the following comprehensive checklist for any API platform (referred to as a supergraph) design that seeks to address the challenges of API integration, aggregation, composition and orchestration.

Guideline |
Description |
1. Integration |
Making it easy for API consumers to integrate APIs into their services |
1.1 Multiple API formats | Can the supergraph platform automatically provide output formats beyond GraphQL such as REST/OpenAPI? This is required to support the integration needs of multiple consumers. |
1.2 Documentation | Does the supergraph platform help domain or platform owners maintain API documentation? If the underlying domains (database, code or APIs) are already documented, are those automatically picked up by the supergraph platform? |
1.3 Standardization | Does the supergraph platform provide or enforce a standardized domain API design (pagination, filtering, sorting, etc.)? |
2. Aggregation |
Making it easy for API consumers to aggregate/batch multiple API calls into one |
2.1 Relationships | Does the supergraph provide a way of creating relationships between any two entities or endpoints without requiring changes from the domain owners? |
2.2 Composability | How many “join” features does the supergraph provide, given a relationship between two entities in the supergraph? |
3. Orchestration |
Making it easy for supergraph stakeholders to author custom API orchestration |
3.1 Federated mutations / decoupled orchestration business logic | Does the supergraph provide a way to author orchestration flows within or across underlying domains? |
Measuring the effectiveness of a platform’s design to meet this criteria and the time and effort investment required to build these capabilities will provide any architect with a clear indication of the likely success of their platform initiative.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)