The [Eclipse Foundation](https://www.eclipse.org/) yesterday launched a challenge to proprietary AI platforms with the introduction of the [Agent Definition Language (ADL)](https://github.com/inference-gateway/adl), a new tool designed to make enterprise AI development more accessible, reliable and scalable.

Eclipse is positioning [ADL](https://eclipse.dev/lmos/docs/arc/adl/) as the centerpiece of [Eclipse LMOS](https://eclipse.dev/lmos/) (Language Models Operating System, now in alpha), an open source platform aimed at reshaping how large organizations build and deploy AI agents, the organization said. In doing so, it [takes direct aim at closed-source alternatives that have dominated the enterprise AI space](https://thenewstack.io/ibms-mellea-tackles-open-source-ais-hidden-weakness/).

## Born From Real-World Necessity

[Arun Joseph](https://www.linkedin.com/in/arun-joseph-ab47102a/?originalSubdomain=de), Eclipse LMOS project lead, developed the platform in 2023 while leading Deutsche Telekom’s AI program. His mission was to deploy AI across 10 European countries for sales and service operations. But he quickly hit a wall, he told The New Stack.

[![](https://cdn.thenewstack.io/media/2025/10/dd4aad9b-res-increased-1-210x300.jpg)](https://cdn.thenewstack.io/media/2025/10/dd4aad9b-res-increased-1-210x300.jpg)

Arun Joseph, Eclipse LMOS project lead

“When we started, there were emerging frameworks like [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/), but they were all in [Python](https://thenewstack.io/what-is-python/),” Joseph explained in a recent briefing. “Our entire enterprise stack at Deutsche Telekom, like most telcos and enterprises, was built on [JVM](https://thenewstack.io/how-do-javas-virtual-threads-help-your-business/) [Java Virtual Machine]. We realized we’d have to rebuild everything from scratch.”

However, the problem went deeper than just [programming languages](https://thenewstack.io/introduction-to-java-programming-language/). Deutsche Telekom’s APIs were complex, with hundreds of attributes and years of accumulated domain knowledge baked into client libraries. Starting fresh with a Python stack would mean abandoning that institutional knowledge and forcing teams to rebuild what already existed.

So, Joseph and his team took a different approach. They built their own stack using [Kotlin](https://thenewstack.io/angular-18-kotlins-new-compiler-astro-adds-react-19-support/), a JVM language that could leverage existing infrastructure, APIs and [DevOps](https://thenewstack.io/introduction-to-devops/) practices. By late 2023, they had their first agent in production for Telekom Germany.

This “looks like a real signal that agents are moving from demos to ops,” [David Mytton](https://www.linkedin.com/in/davidmytton/), CEO of AI-based dev security platform provider [Arcjet](https://thenewstack.io/arcjet-brings-ai-security-analysis-local-into-your-code/), told The New Stack. “Others have explored ‘agent definition’ ideas, but Eclipse’s governance and Java footprint matter for adoption because the JVM is widely used throughout serious enterprises.”

## The Jira Ticket Problem

But solving the technical integration challenge revealed another, more subtle problem: How do you define what an AI agent should do? Joseph asked.

“In traditional application development, a businessperson would raise a [Jira](https://thenewstack.io/open-source-jira-alternative-plane-lands/) ticket saying, ‘I want this button, and when you click it, it should add the item to the shopping cart,'” Joseph said. “But how do you describe the requirements of an agent? How do you write a ticket that explains how a bot should respond when a customer asks, ‘Why is my bill so high?'”

Indeed, “How do you write Jira tickets?” Joseph said. “Take the billing. Usually, enterprises have domain splits, right product domain, billing domain … So, if you have to write the requirements, not the engineering requirements, but rather the end user experience requirements, it is very hard for an agentic conversational system.”

The answer became ADL, a structured language that enables business domain experts to write agent behavior as standard operating procedures without becoming [prompt engineers](https://thenewstack.io/prompt-engineering-get-llms-to-generate-the-content-you-want/). Using a web-based interface, business users can define use cases, test them immediately and iterate without waiting for engineering tickets to cycle through sprints, he said.

“We wanted to make defining agent behavior as intuitive as describing a business process, while retaining the rigor engineers expect,” Joseph noted. “It eliminates the fragility of prompt-based design.”

## Three Pillars of Eclipse LMOS

Eclipse LMOS comprises three core components working together:

* **Eclipse LMOS ADL** provides a structured, model-neutral language and visual toolkit that lets domain experts define agent behavior and collaborate with engineers. It’s designed to be versionable and maintainable, addressing the chaos of traditional prompt engineering.
* **Eclipse LMOS ARC Agent Framework** offers a JVM-native framework with a Kotlin runtime for developing and testing AI agents. It includes a built-in visual interface for rapid iterations and debugging, allowing engineers to focus on integrating domain-specific APIs rather than wrestling with AI infrastructure.
* **Eclipse LMOS Platform** serves as an open orchestration layer for agent life cycle management, discovery, semantic routing and observability. Built on the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) stack, it’s currently in alpha release.

[![](https://cdn.thenewstack.io/media/2025/10/754091d2-defining_adl_lmos-1.png)](https://cdn.thenewstack.io/media/2025/10/754091d2-defining_adl_lmos-1.png)

“Bringing business context into AI workflows and applications is important for them to be able to make high-quality decisions at scale,” Mytton said. “Natural-language prompts aren’t versionable or auditable — that’s the enterprise pain, which is why programming languages exist — so this delivers for those in between.”

## A Different Philosophy

The Eclipse LMOS approach represents a philosophical departure from the current AI tooling landscape, which Joseph characterizes as problematic for enterprises.

In his presentation to The New Stack, Joseph displayed a satirical slide showing the typical enterprise AI stack: a Python codebase importing SDKs from multiple venture-backed startups, each solving one piece of the puzzle — telemetry, memory, evaluation — with a simple decorator adding entire container fleets to the infrastructure.

“I’ve seen evaluation tooling that required 25 containers just for that one function,” Joseph said. “That’s 25 containers running a custom [Kubernetes](https://thenewstack.io/kubernetes/) operator for one line of code. Enterprises can’t afford this kind of sprawl.”

Instead, Eclipse LMOS integrates with technologies enterprises already run, including Kubernetes, [Istio](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/) and JVM-based applications. The platform is designed to work with existing DevOps practices, observability tools and API libraries that organizations have spent years building.

## Already Proven at Scale

Joseph said Deutsche Telekom has deployed Eclipse LMOS in one of Europe’s largest multiagent enterprise systems, powering the [Frag Magenta OneBOT assistant](https://www.telekom.com/en/company/digital-responsibility/details/artificial-intelligence-at-deutsche-telekom-1055154) and other customer-facing AI systems. The deployment has processed millions of service and sales interactions across multiple countries.

This real-world validation matters in an industry where many AI platforms promise enterprise readiness but few have operated at telecommunications scale with the reliability requirements that come with customer-facing deployments, Joseph said.

“I believe the best way to apply AI is operations, period. There is no better area to apply AI than operations,” he said. “Your entire enterprise stack and engineers and operations are in JVM, and then you have data scientists and these new libraries and all they just keep adding and adding, but without plumbing data, you cannot move forward.”

## Standards Matter?

“Standards are important for emerging technologies as they allow reuse, interaction and investment protection,” [Holger Mueller](https://www.linkedin.com/in/holgermueller/), an analyst at [Constellation Research](https://www.constellationr.com/), told The New Stack. “Standards for agentic AI have been proposed quick and adopted faster when one considers [MCP](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) [Model Context Protocol] and [A2A](https://thenewstack.io/google-brings-the-a2a-protocol-to-more-of-its-cloud/) [Agent2Agent]. That does not mean there is no more room for standards like the Eclipse’s LMOS — but it will be an uphill battle — as agents mostly run in the cloud, the cloud standards are established, and people are building agents for them. It is going to be an uphill battle for the Eclipse Foundation.”

[Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at [The Futurum Group](https://futurumgroup.com/), tends to agree with Mueller.

Right now, there is just so much noise around agentic platforms, frameworks and tools that more traditional standardization efforts often feel too antiquated and slow to help companies solve immediate, pressing problems, he said.

“So, I worry that this extremely comprehensive ‘platform’ notion from the Eclipse Foundation might lose out to more rapidly evolving, albeit more piecemeal, architectural tools like MCP, A2A, etc.,” Shimmin said. “Likewise, every frontier model maker and hyperscaler seeks to establish itself as an agentic platform provider. In that regard, I can’t see these players handing over control to a platform that might threaten their competitive differentiation. Still, over time, I would hope that companies can look to LMOS or other such comprehensive, open and sovereignty-preserving ideas as a means of governing agentic systems that span those walled agentic platforms.”

## Market Timing

The timing of the ADL announcement aligns with explosive growth projections for agentic AI. [According to Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027), by 2028, 15% of daily business decisions will be made autonomously through agentic AI, and 33% of enterprise applications will include such capabilities — up from less than 1% in 2024.

“Agentic AI is redefining enterprise software, yet until now there has been no open source alternative to proprietary offerings,” said [Mike Milinkovich](https://www.linkedin.com/in/mikemilinkovich/?originalSubdomain=ca), executive director of the Eclipse Foundation, in a statement. “With Eclipse LMOS and ADL, we’re delivering a powerful, open platform that any organization can use to build scalable, intelligent and transparent agentic systems.”

## The Reliable AI Movement

Joseph’s work connects to a broader movement advocating for what he calls “reliable AI” in enterprise contexts. He’s a contributor to the [Reliable Agentic AI Manifesto](https://github.com/reasonable/reliable-ai/blob/main/reliable-ai-manifesto.md), alongside prominent software engineering figures like [Jonas Bonér](https://jonasboner.com/), [James Ward](https://www.linkedin.com/in/jamesward/) and [Eric Meijer](https://www.linkedin.com/in/erikmeijer1/), pushing for approaches that prioritize operational reliability over bleeding-edge experimentation.

The manifesto reflects a growing tension in the AI industry between innovation-focused startups building on Python and existing enterprises with massive investments in JVM-based infrastructure. Eclipse LMOS positions itself firmly in the latter camp, arguing that the path to reliable AI runs through existing enterprise capabilities, not around them.

## Enterprise Advantages

Compared to proprietary alternatives, Eclipse LMOS offers several architectural benefits, including an open architecture, multiagent collaboration, cloud native scalability, modularity and extensibility, and multitenant capability.

## Beyond Telecom

While Joseph has moved on from Deutsche Telekom to launch his own startup, [Masaic](https://masaic.ai/), focused on operational intelligence, Eclipse LMOS continues as an open source project under the Eclipse Foundation. The platform aims to do for agentic AI what the Eclipse IDE did for Java development: create a vendor-neutral, community-driven foundation that any organization can build upon.

Meanwhile, Joseph’s new venture positions itself as an open alternative to [Palantir](https://www.palantir.com/), focusing on operational AI. He said that the company uses Eclipse LMOS as its open core, demonstrating how the platform can serve as the foundation for commercial offerings while remaining freely available to the community, he said.

“The best way to apply AI is in operations,” Joseph said. “And the best way to make companies AI-native is to empower the engineers who already understand their systems, not bring in outside consultants to build black boxes.”

## Getting Involved

The Eclipse Foundation is inviting developers, enterprises and researchers to join the Eclipse LMOS community and contribute to the evolution of open source agentic AI. The project is part of the Eclipse Foundation’s broader AI initiatives, which include over 400 open source projects spanning cloud, edge, Internet of Things (IoT), automotive and other domains.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)