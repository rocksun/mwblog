# API Governance: Using Patterns From PayPal, Netflix and More
![Featued image for: API Governance: Using Patterns From PayPal, Netflix and More](https://cdn.thenewstack.io/media/2025/02/0c405e33-api-governance-patterns-2-1024x576.jpg)
API governance is not, I will admit, a topic that sets the pulse quickening. It might best be described as boring but important.

Done well, it can help maintain consistency and promote reuse across APIs. It should also provide a mechanism by which both internal and external customers can provide feedback and request changes. These requests can then be assessed against other competing priorities so that decisions can be made about if, how and when to implement them.

In my experience, a lot of organizations leave [API governance](https://thenewstack.io/api-management/) to chance. But, as with organizational culture, a governance process will arise whether you define it or not. It is therefore better, in my view, to be intentional.

Governance needn’t be burdensome. Many developers would welcome guidelines on how to design their APIs, because it means not having to worry so much about making choices — such as how to handle paging in a set of API results, or what a transaction ID should be called.

“At a recent conference in Germany, I asked a room of 150 developers, ‘How many of you have API guidelines in your organization?’ and very few hands went up,” [Erik Wilde](https://www.youtube.com/ErikWilde), a principal consultant at INNOQ, O’Reilly author and API-advice YouTuber, told The New Stack. “I then asked, ‘How many of you would like to have guidelines?’, and it looked to me as if the majority of hands went up. I hadn’t expected the difference to be so stark.”

If you want to establish a governance process for APIs in your organization, there are three main patterns you can apply: centralized design authority, federated governance and influenced self-governance. Each has different trade-offs and will be better suited to some situations than others.

In this article, with the aid of real-world examples, we’ll take a look at each one and examine where it might best be applied.

## Pattern 1: Centralized Design Authority
Centralized design authority (CDA) carries with it the baggage of architecture review boards and overly bureaucratic processes and is perhaps the least fashionable of the three patterns we’ll consider. But that shouldn’t blind you to the fact that it can, in certain circumstances, be effective.

For instance, it is a widely adopted approach to evolving programming languages — think of the [ISO standard for C++](https://thenewstack.io/coming-to-iso-c-26-standard-an-ai-acceleration-edge/), the [Java Community Process for Java](https://thenewstack.io/microsoft-goes-deep-on-java-with-jcp-membership/) or the [Python Enhancement Proposal (PEP)](https://thenewstack.io/guido-van-rossums-ambitious-plans-for-improving-python-performance/) process and corresponding steering council for Python.

The main role of the CDA is that of gatekeeper, which means that in order to be effective it needs to prevent low-quality or risky decisions from being made. Alongside its gatekeeping role, the authority should validate good decisions and inform teams on how to meet quality requirements through [documentation](https://thenewstack.io/poor-documentation-is-costly-heres-how-to-fix-it/) and other guidance.

Investing in good quality documentation is particularly important; without it, the number of meetings that implementing teams need to have with the CDA rapidly balloons to unmanageable levels.

Because the CDA’s primary role is gatekeeping, its success is strongly influenced by the technology group’s culture within the organization. If individual teams feel they can ignore what the CDA tells them to do, it cannot be effective. Conversely, the CDA needs to recognize that an overly heavyweight or bureaucratic process will prompt developers to seek ways to bypass it.

The main advantage of using the CDA pattern is that it drives uniformity. Using this pattern can avoid, or at least limit, the amount of duplication that can occur when developers have more autonomy. It can also ensure that security policies and other organizational protocols are correctly followed.

A significant downside is that the authority will almost inevitably become a bottleneck as a company grows, causing API projects to stall as their members wait to discuss issues with the central team.

“With this model, you often have scalability problems, where developers perceive the design authority as standing in their way,” Wilde suggested. “It’s not so much that they don’t like what the authority is doing, but rather they see it as something that slows them down, so they try to bypass it to get stuff done.”

As with other forms of software architecture authority, there is also a risk that members of the API Design Authority become too distant from the work to make good decisions about it. The phenomenon is equivalent to what [Joel Spolsky](https://www.linkedin.com/in/joelspolsky/), co-creator of Stack Overflow, refers to as “[architecture astronauts](https://www.joelonsoftware.com/2001/04/21/dont-let-architecture-astronauts-scare-you/).”

In light of this, the CDA pattern is best applied either when kickstarting a process, or when the volume of changes is relatively small. Unsurprisingly, it is generally preferred in more regulated industries.

### How PayPal Uses a Centralized Design Authority
PayPal, the online payments provider, uses a centralized design authority for governance. [Speaking at the Nordic APIs 2018 Platform Summit](https://www.youtube.com/watch?v=LuZiWas_nNw), [Jayadeba Jena](https://www.linkedin.com/in/jayadeba-jena-1a6a0020/), who was head of API Platform for the payment provider at the time, described a four-step process:

**Define (API portfolio alignment):**An API proposal with use cases and target customers is submitted to the API portfolio team. The portfolio team reviews for overlap and advises on API taxonomy, namespace and resource names. If approved, a GitHub repo is established to define an API contract and the design phase can start.**Design (API design review):**Using the[OpenAPI](https://www.openapis.org)approach for REST APIs, an API contract and samples are submitted to the central team for review via a pull request. A group of API designers review specs for compliance with design standards. Issues and comments are addressed and then, once the API spec is approved, it moves to the development phase.**Develop (APl implementation):**Implement the API meeting standards, such as service-level agreements and logging. This is an iterative process, with PRs submitted back and forth. At the end of the process, the team verifies that the implementation matches the contract definition, using tools to automatically create verification tests based on the OpenAPI specification.**Externalize (access by merchants and partners):**Provision Rate limiting, the API facade and OAuth scopes. Create external documentation. Update the SDK. Ensure the API passes the integration-readiness checklist.
To help maintain consistency, ensure adherence to the company’s security policies, backward compatibility, and life cycle management. PayPal’s CDA maintains a set of standards that define the patterns, versioning policy and style guides. This ensures that “a customer/partner gets a uniform view and the same experience across our APIs,” Jena said.

The CDA, Jena noted, became a bottleneck over time. PayPal’s solution was to train product owners to review their development team’s work against the organization-wide governance criteria. The central API design team was still responsible for developing the governance criteria, but it was no longer tasked with reviewing every API.

## Pattern 2: Federated Governance
Our second pattern, federated governance, is an internal consultancy model. Individuals from a centralized pool of experts join a team that is responsible for building an API. These experts can either advise on key decisions or be given the authority to make decisions on behalf of the implementing team.

When appropriately staffed, a federated governance team should have the necessary bandwidth to carry out research, try out options and make informed recommendations about practices, tooling and frameworks.

Federated governance has three advantages over the CDA model. The first is that important decisions can be made earlier in the process, due to the involvement of experts from the central team.

The second is that the experts themselves gain experiences that they can take back to the central team and ensure that understanding and guidance are continuously improved. Third, those overseeing the work are less likely to become “astronauts” divorced from reality, because they are directly involved in the process.

Federated governance is, however, resource intensive because a lot of experts are required to make sure that every team has the help it needs. As with a consultancy firm, you have to either scale up your employees to meet peak demand and accept that team members might not have much to do during slack periods, or you need to be prepared to lay people off when work drops away — or accept some bottlenecking.

In practice, I’ve also found that it takes considerable effort to maintain a shared understanding between the experts to avoid a loss of consistency.

### How HSBC Uses Federated Governance
HSBC moved from a centralized team to federated governance. “We have built a community of ‘API Champions’ from across HSBC to understand standards, apply them locally to their teams and escalate issues or gaps,” [John Phenix](https://www.linkedin.com/in/johnphenix), chief API architect for HSBC Wholesale Bank, [wrote in a company blog post](https://develop.hsbc.com/news/why-we-are-automating-api-governance).

HSBC did hit problems, however. “Not all API Champions were equally experienced, so we still needed a sizable central team to ensure consistency,” Phenix wrote. The company’s solution was to increase automation.

“Automated tests can form part of [DevOps](https://roadmap.sh/devops) pipelines, ensuring tests are built into the regular build, test and release cycles,” he added. “This stops people trying to game the governance process and ensures higher coverage of API reviews.”

But not all checks can be automated in this way, Phenix acknowledged: “For a relatively small investment, a large gain can be made in consistency, completeness and visibility.”

## Pattern 3: Directed Self-Governance
Perhaps the most fashionable approach to API governance is directed self-governance, a pattern that relies on influence rather than control. This pattern fits most comfortably with DevOps and cloud native approaches to building software. As such, it has been popularized by Silicon Valley companies like Netflix, and mirrored by their European counterparts such as Spotify.

The general goal is to allow a high degree of autonomy, but within that, to maintain some guardrails — a “golden path” — which makes it easy for developers to do the right thing.

“More and more we’ve seen platforms being established and API governance slotted into this,” Wilde told us. “You can use automation for some design checks in the CI/CD pipeline, to keep the process as lightweight as possible.”

Taking a leaf out of the [“Team Topologies” book](https://thenewstack.io/how-team-topologies-supports-platform-engineering/), it’s possible to combine self-governance with [enabling teams](https://teamtopologies.com/key-concepts) that help with things that the stream-aligned team is not an expert in, such as API design.

“You need to improve the effectiveness and standardization of what happens within the organization without being too heavy-handed,” Wilde told TNS. “The aim is to avoid teams having to do the same thing multiple times, or different teams picking different solutions.”

A significant advantage of this type of approach over the other two we’ve looked at is execution speed; teams can move very quickly when they are given full autonomy over the decisions they make. It also scales well without requiring a huge number of additional hires.

The main disadvantage is that a team may inadvertently make decisions that are inconsistent or that are optimized for the local context in which they are operating to the detriment of the whole. “For internal APIs, it really helps with developer productivity if they follow the same look and feel because your developers will be consuming a lot of different APIs,” Wilde told The New Stack. “That makes working on guidelines a good investment since you’ll harvest it in terms of developer productivity.”

### How the Financial Times Uses Directed Self-Governance
Amongst her many senior roles during her time at the Financial Times, [Sarah Wells](https://www.linkedin.com/in/sarahjwells1/) was the team lead for the media outlet’s content platform, which provides API access to rich versions of the FT’s content for internal and external partners.

Judging by Wells’ recollection, it seems that the FT was fairly organic in its approach to self-governance. “We didn’t have an API expert team,” she told The New Stack. “But we did have an API Gateway and some documentation standards.”

“We also had standards around what a health check would look like, and with that, we found our developers were more likely to make their APIs look like a common one,” Wells said. “We discussed what you need to think about when building an API, to make sure that it’s not completely different from all the others; that was really valuable. For example, we tried to make sure that it was discoverable through the API gateway, and that we had consistency in the way that we named things.”

## How Netflix Combines API Governance Strategies
As we’ve seen, different approaches can be combined, even within a single company. And it is often optimal to use multiple approaches in different places and at different times.

Netflix, for example, is famous for promoting a high-trust, high-autonomy culture, using a golden path and a directed self-governance approach. Nevertheless, the streaming company uses centralized governance as part of a wider adoption of [GraphQL](https://thenewstack.io/why-every-api-strategy-needs-graphql/).

[Speaking to me](https://www.infoq.com/podcasts/netflix-graphql-adoption-performance/) on the InfoQ podcast in 2021, [Kavitha Srinivasan](https://www.linkedin.com/in/kavitha-srinivasan/), a senior software engineer at Netflix, explained how the firm has a schema working group that oversees the evolution of the graph.
“It is a very people-heavy process,” she said. “Any team that wants to be part of this federated graph needs to participate in the schema working group. We have a data architect overseeing the evolution of this single unified graph. So any time somebody wants to add a new entity or field to an existing type, they have to come to the schema working group to be part of the discussion.

“We make sure that it all makes sense and folks aren’t adding pieces of schema willy-nilly to the graph on their own.”

Finally, whichever approach you choose, keep in mind that governance, like your APIs, should evolve over time. It’s important to continue considering whether your governance model is doing what you want it to.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)