For over 15 years, [Kin Lane](https://www.linkedin.com/in/kinlane/), co-founder and chief community officer (CCO) for open source API foundation [Naftiko](https://naftiko.io), has been building his expertise in APIs — not only the technical details but also the business angle. He believes that the growing use of copilots and [agentic AI systems](https://thenewstack.io/ai-agents-vs-agentic-ai-a-kubernetes-developers-guide/) in enterprises means we must design and [build APIs](https://thenewstack.io/api-management/) around business capabilities rather than resources. APIs should represent core business functions like “manage inventory” or ”process payments,” he says.

[He is not alone in this view](https://apievangelist.com/2025/10/07/what-is-a-capability/). Multiple other well-known API experts, including [Christian Posta](https://blog.christianposta.com/from-apis-to-capabilities-what-ai-agents-mean-for-application-architecture/), [Mike Amundsen](https://mamund.substack.com/p/focusing-on-capabilities-is-a-win) and [Daniel Kocot](https://architecturalbytes.substack.com/p/from-apis-to-capabilities), have reached similar conclusions.

Recent research documented in DORA’s [“State of AI-Assisted Software Development Report”](https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report?hl=en) provides support for this perspective, concluding that generative AI (GenAI) is an amplifier. “It magnifies the strengths of high-performing organizations and the dysfunctions of struggling ones,” the report states. Lane sees that amplification effect in organizations’ approaches to the APIs they build and consume.

“Companies will succeed or fail in their AI implementations based on their existing API investment and how far they are along their API journey,” he told me in an interview. “For example, do they have an API catalog? Do they have open APIs? Are they testing/mocking? Are their APIs properly documented? Are they invested in open source?”

The AI programs of organizations with an immature approach to APIs will, Lane believes, be a disaster. With that in mind, Lane outlined a four-step process for getting a handle on your API landscape for a more successful AI implementation.

## 1. Map Your API Landscape

The reason for this potential failure with APIs is that less-mature organizations have “a big gap between what an enterprise knows and what it is capable of,” Lane said. The average enterprise’s Software as a Service (SaaS) portfolio is around 250 to 500 services, all of which have APIs. But, according to Lane, with limited means of discovery, many end up barely used.

Introducing an AI agent into this environment will produce one of two outcomes: Either the agent can’t discover the APIs that are available to it, so it’s fairly useless. Or it can access those APIs but ends up [oversharing](https://leaddev.com/technical-direction/if-95-of-generative-ai-pilots-fail-whats-going-wrong), exposing data that should be kept private. Therefore, the first priority must be building a map of the organization’s API landscape to understand both the internal and external resources.

Building this map requires looking at the available signals. If you were building an API map of an organization from the outside, you would look at public GitHub repos, blog posts, press releases, job listings and any tech docs for published APIs. The same process can be used internally, something Lane became familiar with when he led API governance at Bloomberg for a year.

“I crawled GitHub and Confluence, looking for any existence of an API. I mapped that landscape, figured out the teams behind it and organized the data into an org chart that became like my chessboard,” Lane said.

## 2. Develop a Ubiquitous Language

With this map in place, Lane’s second priority is to look at the language used within the components of an API, such as endpoint URLs, method names and parameters.

Netscape Principal Developer [Phil Karlton famously said](https://martinfowler.com/bliki/TwoHardThings.html), “There are only two hard things in computer science: cache invalidation and naming things.” Naming things is challenging because the language choices we make really matter. While [language is primarily a tool for communication rather than thought](https://gwern.net/doc/psychology/linguistics/2024-fedorenko.pdf), language influences attention, memory and categorization, making certain cognitive distinctions easier or harder and potentially obscuring intended meaning.

Bloomberg’s APIs were mainly REST APIs. “The APIs I reviewed all had words like ‘database’ or ‘ERP’ in their names,” Lane said. “This isn’t good design.”

Lane discovered that in the vast majority of cases, Bloomberg developers build APIs at the wrong level of abstraction, mirroring backend systems rather than business processes. This manifests in [API sprawl](https://thenewstack.io/heres-how-to-tame-your-api-sprawl-and-why-you-should/) and multiple APIs that serve no real purpose.

This isn’t a limitation of REST, but using REST does shape our thinking: It encourages us to focus on the representational state transfer of resources, since that is what REST was designed to handle.

“I’d say 90% of people don’t do REST API design well,” Lane said. “They don’t think or care about REST, and they don’t take a consumer- or product-oriented approach to design.”

The way REST shapes our thinking is one example of how language choices matter. REST’s verbs — GET, PUT, PATCH, DELETE — specify an action to be performed on a particular resource (or a collection of resources). For any API, the vocabulary shapes the thinking of the developers who use it. An API is, in effect, a small language that its consumers have to learn. The names we choose [shape our mental model](https://thenewstack.io/what-are-the-core-principles-of-good-api-design/), as [Harry Richardson](https://www.linkedin.com/in/harry-richardson-007a69/), chief scientist at SoftIron, told me in 2024.

A consequence is that taxonomy is important. Taking a leaf out of Eric Evans’ book [“Domain-Driven Design,”](https://learning.oreilly.com/library/view/domain-driven-design-tackling/0321125215/) Lane suggests that developers need to start by building a common or “ubiquitous” language that’s shared between IT and the rest of the business. This is a good idea that’s rarely executed.

“Enterprises move so fast that you end up with a messy word salad of invoices, payments and messages that don’t share the same context or work together,” Lane said.

Moreover, when domain experts and developers don’t share a common language, communication breaks down in costly ways. Experts use specialized terminology from their field, whereas developers think in technical abstractions, creating a linguistic gap where both sides only vaguely understand each other. Even when a few team members bridge this divide, they become information bottlenecks, and their translations lose precision — resulting in muddled concepts, constant misinterpretation across the team and ultimately code that gets refactored in ways that undermine the original design.

## 3. Move From APIs to Business Capabilities

Having a ubiquitous language is a prerequisite for defining business-oriented APIs.

“The companies that have done the best have stitched together APIs in ways that matter to businesses,” Lane said. “The next iteration is moving from resources to ‘capabilities’ or ‘experiences.’”

Lane [defines capabilities](https://naftiko.io/blog/reframing-how-we-integrate-software-with-capabilities) as “open source, declarative, standards-based integrations aligned with business outcomes within specific domains. They provide the building blocks needed to deliver and automate integrations across countless internal, partner and third-party systems. Capabilities help rebalance how we think about and execute integrations across the sprawling ecosystems we depend on.”

Lane’s ideas around capabilities are born from a number of different disciplines but overlap with “aggregates,” which “Domain-Driven Design” defines as “a cluster of associated objects that we treat as a unit for the purpose of data changes.” Good capabilities are business-aligned, human and machine-readable, composable, declarative, governed, and executable across multiple systems.

Daniel Kocot frames [“capability thinking”](https://architecturalbytes.substack.com/p/from-apis-to-capabilities) as “placing emphasis on what a platform or system can actually do for its consumers, and how those actions can be documented, standardized and made reusable across use cases … Capability thinking reframes the unit of design. Instead of exposing granular resources, platforms describe discrete business functions such as Ship Order, Process Payment or Approve Loan.”

The term “capabilities” has found new life in describing what AI agents can do, but it also reveals gaps between what enterprises think they can do versus what their architecture actually supports. Agents need to discover what systems are capable of and decide which capabilities to use, based on goals and context. As [Mike Amundsen puts it](https://mamund.substack.com/p/focusing-on-capabilities-is-a-win), autonomous clients need “a menu of possibilities,” not just a list of endpoints.

## 4. Establish Clear Boundaries for AI

Lane contends that having a map, establishing ubiquitous language and doing the domain-driven design work means that your AI work will be better scoped. “Your MCP [Model Context Protocol] servers will have the right amount of tools for a certain set of products, customers or line of business.” Conversely, if you don’t have well-defined boundaries, you increase security exposure and risk.

With these things in place, the next steps depend on business context. Less risk-averse companies are “publishing MCP servers publicly and encouraging people to build interesting things on them,” Lane said. In more regulated industries, the focus will be on operations and developer platforms, with the goal of increasing developer velocity.

## Start With API Fundamentals for AI Success

Lane’s approach requires enterprises to start with the fundamentals: establishing a common vocabulary, mapping their API landscape and understanding what they’re capable of today before racing toward what AI might enable tomorrow. As he emphasizes, this work isn’t just about technical architecture. It’s about getting engineers, product managers and business stakeholders aligned around the same language and bounded contexts.

For executives wondering where to begin, the answer is remarkably simple: Start tagging and cataloging. Define the vocabulary for a specific domain, map the services and resources within it, and establish clear boundaries around what you’re trying to accomplish.

This foundational work may seem unglamorous compared to spinning up the latest AI agent. But this willingness to slow down and think carefully about language, design and business alignment separates the enterprises whose AI investments will amplify their strengths from those whose investments will merely magnify their dysfunction.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/09/533ec2dc-cropped-379ef74d-charles-humble-5-600x600.jpg)

Charles Humble is a former software engineer, architect and CTO who has worked as a senior leader and executive of both technology and content groups. He was InfoQ’s editor-in-chief from 2014-2020, and was chief editor for Container Solutions from 2020-2023....

Read more from Charles Humble](https://thenewstack.io/author/charles-humble/)