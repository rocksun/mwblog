# REST Still Outshines GraphQL for Many API Use Cases
![Featued image for: REST Still Outshines GraphQL for Many API Use Cases](https://cdn.thenewstack.io/media/2024/10/5e70fd80-douglas-lopes-ehyv_xoz4ia-unsplash-1024x683.jpg)
[Douglas Lopes](https://unsplash.com/@douglasamarelo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-laptop-computer-sitting-on-top-of-a-wooden-desk-ehyV_XOZ4iA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
Over the past several years, I kept hearing that [GraphQL](https://thenewstack.io/is-graphql-over-or-do-we-just-need-to-rethink-it/) — a query language for APIs that lets clients request specific data — is the future of APIs. Its hype comes from clear and compelling value props. Namely, it can help you get the exact data you need and access multiple resources from a single request, saving you time, money, and bandwidth.

But as you [begin using GraphQL](https://thenewstack.io/why-every-api-strategy-needs-graphql/), you’ll find that it creates an entirely new set of issues that overwhelm its benefits.

I’ll break down these issues so that you can better decide whether GraphQL is worth using across your integrations. I’ll also highlight why REST is a better alternative today and will continue to be the leading API standard.

## The Drawbacks of GraphQL
I can point to several fundamental issues with using GraphQL. For starters, [GraphQL often leads to complex queries that seriously](https://thenewstack.io/salt-security-finds-serious-graphql-api-security-hole/) strain backend performance. This can translate to long processing times, negating one of the promised benefits of GraphQL — a faster response time. Deeply nested queries can even cause servers to go down, further delaying responses.

In addition, GraphQL typically applies rate limiting based on the complexity of a request — such as the number of fields or objects being requested. As you increase the resources in your requests over time, understanding and following your rate limits will become more complex.

Finally, as an API matures, its GraphQL schema becomes more complex. Successfully navigating this growing complexity is not only painful from a rate-limiting perspective but can also lead to costly mistakes when your team structures requests.

## Why REST Is Better and Here to Stay
Here are a few reasons why REST is the best option for integrating SaaS applications.

- REST APIs come with standardized error codes.
These codes — which include everything from a 404 (Not Found) to a 500 (Internal Server Error) — make it easy to diagnose issues and build error-handling flows that address them automatically. For example, if you get a 429 Too Many Requests error, you can create an automated retry based on the suggested wait time in the response.

GraphQL, on the other hand, requires your engineers to account for the response provided in the errors key. And since these responses aren’t as standardized as in REST, they’re harder to plan for and handle automatically.

- Many engineers have experience building and/or maintaining REST API integrations.
Companies of all shapes and sizes primarily use REST APIs.

Case in point: [According to research from Gartner](https://www.gartner.com/en/documents/5551595), REST APIs are used by 85% of organizations — while GraphQL is only used by 19%.

Given REST’s popularity, your developers are likely experienced and comfortable with building and maintaining REST API integrations. It’s also less effort to find and hire engineering talent with experience working with REST, making it easier for your organization to scale REST API integrations over time.

In addition, while API providers will inevitably struggle to get developers to integrate with them, offering APIs in the architecture that developers are most familiar with will remove a significant barrier to adoption.

- REST’s open source ecosystem is significantly more comprehensive than GraphQL’s.
A wide range of backend frameworks and libraries for REST can auto-generate OpenAPI specifications. These tools are also available in several programming languages, allowing your [developers to work in the language](https://thenewstack.io/hey-programming-language-developer-get-over-yourself/) they’re most comfortable with.

Beyond OpenAPI, you can access diverse open source tools to [manage every facet of REST API development](https://thenewstack.io/using-a-developer-portal-for-api-management/), including validation, security, monitoring, and testing.

Postman is well suited to test REST APIs; OpenAPI lets you auto-generate API documentation; REST frameworks (e.g., Django REST Framework) are built for specific [programming languages](https://thenewstack.io/programming-languages/) and provide tools that help you build APIs efficiently, etc.

This isn’t to say that tooling doesn’t exist for GraphQL; there are simply more REST-related extensions that are better supported.

## Final Thoughts
As the API space continues to mature, I suspect that additional [API architectures](https://thenewstack.io/untangling-enterprise-api-architecture-with-graphql/) will be released and receive similar hype to GraphQL. This hype will mostly come from those who have yet to leverage them in meaningful ways, if at all.

Until a competing API architecture can exceed — let alone match — REST’s utility for both providers and consumers, REST will continue to be the preferred choice.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)