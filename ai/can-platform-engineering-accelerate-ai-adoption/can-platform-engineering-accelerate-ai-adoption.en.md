*This article was written by the author on behalf of PlatformCon.*

Gone are the days of top-down [developer tooling](https://thenewstack.io/developer-tools/%5D%5D) mandates. About half of all companies are applying a [bottom-up approach to AI adoption](https://jellyfish.co/resources/2025-state-of-engineering-management-report/), encouraging teams to experiment with new AI dev tools. And for organizations that aren’t embracing this, [shadow AI](https://thenewstack.io/shadow-ai-isnt-a-threat-its-a-wake-up-call/) will soon force their hands.

But too much freedom brings potential for risk and waste. More than three years into this deluge of AI, only [60% of organizations](https://www.traliant.com/resources/hr-report-on-ai-insights/) have an acceptable usage [AI policy](https://thenewstack.io/how-to-create-the-generative-ai-policy-you-needed-yesterday/). [Two-thirds of organizations have adopted AI tooling in production](https://leaddev.com/the-ai-impact-report-2025), while nearly that — 60% — lack clear [metrics to measure AI’s impact](https://thenewstack.io/how-to-measure-the-roi-of-ai-coding-assistants/).

So much focus has been put on the approximately 20% of the day that developers code, which, despite thinking they are more productive, AI-generated code turns out to be [slowing down developers](https://arxiv.org/abs/2507.09089)‘ [throughput and reliability](https://arxiv.org/abs/2507.09089).

The rise of [platform engineering](https://thenewstack.io/platform-engineering/) over the last couple of years may have been in response to the [complexity of the modern tech stack](https://thenewstack.io/kubernetes-complexity-realigns-platform-engineering-strategy/). Still, today it presents a compelling solution for many of these AI adoption hurdles. Platform engineering — like AI — is best served when it [focuses on toil and other distractions that hold software developers back from delivering value to end users](https://leaddev.com/velocity/writing-code-was-never-the-bottleneck).

Unsurprisingly, much of the fourth edition of [PlatformCon](https://platformcon.com/) this June focused on platform engineering in the context of AI. As it turns out, an internal developer platform (IDP) may lay the perfect guardrails to enable AI innovation — without disastrous consequences.

“While AI is taking up all of the headlines, really platforms for AI are going to be the backbone of all of this,” Luca Galante emphasized, emphasizing platform engineering as the way to build enterprise-grade paths to production. From data science to machine learning to traditional engineering, “you need this underlying platform to sustain all of that and make it enterprise ready.”

In the Age of AI, the IDP will expand to include AI processes. This will scale proven AI use cases across software development while de-siloing data science.

By bridging these gaps, platform engineering is set to address consistency, quality, and security across [agentic AI](https://thenewstack.io/ai-agents/) and [generative AI](https://thenewstack.io/ai/) application delivery.

## Does AI Require Its Own Platform?

Until recently, AI was relegated to data science departments. Now, it’s time to follow suit of cross-organizational cloud adoption, and bring AI cross-organizationally, argued [Patrick Debois](https://youtu.be/J3QFTquSQB4?si=N_MMzLVc3zksO8kJ), as the co-author of the “DevOps Handbook” made the case at PlatformCon for why AI needs a platform team.

In the current age of AI, he said, the [AI engineer](https://thenewstack.io/what-is-an-ai-native-developer/) becomes the change agent that bridges data science’s faster path to production, consulting with the platform team for:

* Collaboration across teams.
* Enablement of both data science and application teams through the platform.
* Governance.

The AI-enabled twist on the traditional internal developer platform, Debois argues, will be reorganized to include more AI stakeholders, having the platform expand to include:

* **Large language models (LLMs)**, whether open source, proprietary or a mix.
* **Unstructured and structured data**, which will need indexing via a vector-based database.
* **RagOps** or [Retrieval-Augmented Generation as a Service](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/) is an emerging concept that brings together third-party integrations and data sources.
* **AI Agents as a Service**, including management of memory, state and access control, as well as exposure to [Model Context Protocol (MCP)](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) servers.
* **Execution sandboxes** for AI agents.
* **Access control and version control** across all mode inputs and outputs.
* **Central caching layer** to control cost.

All with the transparency and shared view that comes with the platform’s single pane of glass.

But this quickly becomes an ever-expanding toolset to maintain and monitor, which becomes another argument for an IDP to manage it all.

This new AI platform team, he said, should start with creating a prototyping, sandboxing environment that allows for safe play with new AI tooling.

Once developers get more familiar with AI experimentation, then, he said, “you pick a standardized framework that matches your environment or existing languages in your company” with “its own ecosystem for caching, for testing, for debugging as well, and that eventually leads to more golden paths.”

Debois shared four emerging [AI native developer](https://thenewstack.io/what-is-an-ai-native-developer/) patterns for how [tech roles](https://thenewstack.io/tech-culture/) are evolving:

* **From producer to manager.** The developer isn’t just producing code, but also managing code agents. [Operations](https://thenewstack.io/ai-operations/), including DevOps observability and automation, support this shift.
* **From implementation to intent.**The developer expresses intent, or the *what,* and AI takes care of implementation, or the *how.*
* **From delivery to discovery.** Similar to [vibe coding](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/), lowering the cost of experimentation, run through the existing CI/CD pipeline.
* **From content to knowledge.** Debois says AI gives teams a more compelling reason to share knowledge. As he wrote in a blog post on these [four patterns of AI native development](https://ainativedev.io/news/the-4-patterns-of-ai-native-dev-overview), “In fact, knowledge might be your company’s unique value proposition as building and delivering products increasingly becomes a commodity.”

## What Platform Features Does AI Demand?

Like with all product development, you have to consider your user base. AI has platform teams serving more than just devs.

“We wanted to allow native AI tools to expand organically and to convert organically,” said [Ina Stoyanova](https://www.youtube.com/watch?v=_NrGk8jUc6w), staff infrastructure and platform at Equilibrium Energy, on what the startup needs — or doesn’t need — from AI.

“If we had set up golden paths when we had set up a lot of the processes six months ago, we wouldn’t have been in the position that we are in today to be able to nurture the creativity that our engineers, scientist, quants [quantitative analyst] all come with, and they’re really buzzing from it.”

At a startup or scale-up — and frankly at this still early stage of AI anywhere — things can change so quickly that laying down permanent platform features too soon can be a waste.

By asking stakeholders, Equilibrium’s platform team was able to identify what both software engineering and data science teams felt were important, including:

* Cluster management.
* Computer resources.
* Data resources.
* Data tools.
* Storage.
* Query analytics.
* Observability.

But the data science and quant teams also had other considerations that were not initially on the platform engineering team’s mind.

“A platform in the context of platform engineering is really a curated set of reusable tools, workflows, APIs and documentation that enable internal users to self-service infrastructure, environments and deployment pipelines with minimal cognitive overhead,” Stoyanova said of the [definition of platform engineering](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/) that her team started questioning early on.

Platform teams, inevitably made up of engineers, always run the risk of building something that they care about more than their internal customers do. This risks increasing cognitive load — especially, at Equilibrium, for the quants and data scientists.

“We started asking our users: What are the tools that you want to use?” allowing for freedom of choice, Stoyanov said. Then, they were able to build the right thing — without investing too much and risking the startup’s ability to bootstrap and pivot.

The Series B startup Equilibrium Energy also found one AI use case that everyone — business and tech teams — cared about. The platform team built in cost tracking and metrics early on.

## Platform Prepares for AI Data Demands

Taking advantage of AI is, in part, about taking advantage of structured and unstructured data. The [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/ "internal developer platform") becomes the scaffolding on which data scientists and machine learning engineers can build a data strategy that drives AI use cases.

At PlatformCon, the Platform Engineering community [announced a new reference architecture for AI](https://youtu.be/hjg3dECHKH0?si=tHDXT1DOqe1513ow) that will be published later this year, which builds the structure around:

* Observability plane.
* Platform interfaces and version control plane.
* Integration and delivery plane.
* Data and model management plane.
* Security plane.

This new [reference architecture for AI](https://platformengineering.org/blog/ai-and-platform-engineering) (in the feature image) is a way to visualize this new machine learning plus engineering platform.

“This is not just an infrastructure diagram. This is really a structured mental model of how to think about all your different workloads and all the different bits and pieces of your setup and the interplay between them,” Galante said. “It’s really cool to see how we are evolving as a community [and] as a market to accommodate for these new needs.”

This goes beyond technical and architectural changes, he continued, as the industry evolves how it thinks about the platform engineering team itself.

The [platform engineering team](https://platformengineering.org/blog/how-to-build-your-platform-engineering-team) has always included a mix of roles:

* Head of platform engineering.
* Infrastructure platform engineers.
* Developer experience engineers.
* Platform product managers.

Serving stakeholders, including:

* Developers.
* Executives.
* Compliance and legal teams.
* Infrastructure and operation teams.
* Security teams.

[![](https://cdn.thenewstack.io/media/2025/08/8bf745e5-platform-engineering-roles-in-face-of-ai-1-1024x576.jpg)](https://cdn.thenewstack.io/media/2025/08/8bf745e5-platform-engineering-roles-in-face-of-ai-1-1024x576.jpg)

In light of AI, the platform team setup and role development have expanded to include:

* Reliability platform engineers.
* Security platform engineers.
* Data and AI platform engineers.
* Observability platform engineers.

To interact with and serve more stakeholders:

* Site reliability engineering teams.
* Architects.
* Data scientists and machine learning operations engineers.

“The platform team interfaces themselves with multiple, more stakeholders,” Galante said, with an increased granularity of specific needs,” giving rise to “an emerging behavior in this market.”

Because there is no doubt that platform teams have more to do in the face of AI.

## Scaling Generative AI Application Delivery

One of the roles of the modern platform team is to identify cross-cutting generative AI application delivery use cases and then implement them at scale. But it’s also about selecting the appropriate design patterns to implement them with. This is often the buy or build discussion, including using open or closed generative AI models.

But the most pervasive AI challenge facing platform teams, [Manjunath Bhat](https://youtu.be/w5oI1og_oe8?si=B0mk4Nyr12lMPLoH), VP analyst and fellow at Gartner, argued at PlatformCon, is security and governance requirements.

“Security, trust, and explainability concerns, but also, in many cases, governance tends to revolve around cost implications. Product teams are not necessarily the experts in these domains,” he said, which brings architects in as subject matter experts. “How can you scale applications so that you don’t just end up with a bunch of prototypes and experiments that don’t go anywhere, but you can actually productionize and operationalize these applications.”

Establish a generative AI center of excellence, or what[Team Topologies](https://thenewstack.io/how-team-topologies-supports-platform-engineering/) calls an enabling team, he recommends, to work closely with stream-aligned product teams and platform engineering experts to provide specialized expertise that can then scale.

“We don’t recommend jumping straight to building a shared platform,” Bhat said, echoing Stoyanov. “You start with enabling teams because, unless we understand what the different application needs are, it’s not appropriate for the platform team to assume that they understand what those needs are.”

This can include what Team Topologies refers to as complicated subsystem teams — like the AI experts Debois referred to — to lighten further the cognitive load on application teams and platform teams alike.

“Don’t fall into the trap of: Build it and they will come,” Bhat warned. “We start with enabling teams because it helps you discover the specific customer needs.”

## Secure Code at Developer Speed

A new paradigm is emerging in application security. On the one hand, AI-generated code means there is more code than ever to scan and protect. But agentic AI can also aid in proactive and autonomous remediation. The internal developer platform is not only a good place to roll out new AI tools cross-organizationally, but also to lay down guardrails and gates, to manage role-based access control, and to automate checks to make code more secure.

“More code. More contributors. Shorter timelines means more exposure. This is where the traditional AppSec simply cannot keep up,” said [Sónia Antão](https://www.youtube.com/watch?v=EXzszCfKL-g&ab_channel=PlatformEngineering), senior product manager at Checkmarx, at PlatformCon. “Finding issues, it’s not enough. You need to be right where the developers are, which is in the IDE [integrated developer environment],” right where they are coding and remediating, too.

To achieve this, she argues that teams need an integration of agentic AI with application security posture management (ASPM) right within the IDE for real-time code security.

“Intelligent shift left,” Antão called it, where “AppSec gets that real clear and risk-aligned big picture of what’s happening in the application landscape. This is not just about catching vulnerabilities in an early stage. It’s resolving them faster and with confidence at the speed that the business is demanding.”

Developers can then triage and prioritize errors, leveraging agents for AI-powered posture management, giving them the information they need, when they need it, all within the IDE.

By focusing on real-time code security with this agentic AI plus IDE pairing, Antão’s team has already seen a reduction in vulnerabilities ranging from 25 to 35% with response speed improvement of 69%.

## Generative AI within Developer Workflows

Generative AI can transform platform engineering into adaptive, intelligent systems that improve developer productivity, reliability, and business alignment, [Ajay Chankramath](https://www.youtube.com/watch?v=_O-trvJs_yQ), author of “[Effective Platform Engineering](https://www.manning.com/books/effective-platform-engineering),” said, kicking off his PlatformCon 2025 talk.

“Gen AI has shifted from passive assistance to autonomous, intent-aware agents today,” he said. “The rise of agentic AI enables that self-healing pipeline — so real-time feedback and personalized code suggestions.”

So far, Chankramath points to three main influences to these shifts:

* **Retrieval Augmented Generation (RAG)** — allows AI agents to ground their answers in real-time documentation that is contextual to the organization.
* **MCP** — enabling the standardization of how LLM agents communicate with external APIs, which in turn encourages adoption.
* **Generative AI within CI/CD** — allowing intelligent pipelines that can self-correct, tune and suggest improvements.

He described an evolution, from pre-platform “find-it-yourself” to more standardized internal developer platforms. Now, it’s about embedding AI agents into the developer workflow. Operations have transitioned from a ticket-based approach to semi-self-service and now to intent-based autonomous agents.

“This is not to replace anything that somebody was doing before with something else,” Chankramath said. “It’s about how you actually elevate that game so that what you’re really bringing in with the platforms are far more mature, so you as a developer [and] you as a platform engineer can actually focus on higher-value activities.”

With these goals in mind, he offered five ways to support this evolution of AI-driven platform engineering:

1. Align AI strategy with developer value streams, treating AI as flow-native components, not bolt-ons. Aim to integrate agents across coding, testing, deploying and fixing.
2. Always, he emphasized, keep human judgment in the loop. Agents design or propose actions, not approve them.
3. Make AI agents more collaborative rather than controlling, with developers able to override, retrain and recontextualize agents.
4. Observability and guardrails built in by default, including token trace logs, prompt drift detection and relevance scoring. “Just because you have a RAG doesn’t mean it’s relevant,” he emphasized. Then, the platform team must consider how to log agent actions and outputs on an observability platform, with explainable audit trails and versioning.
5. [AI impact measurement](https://thenewstack.io/how-to-measure-the-roi-of-ai-coding-assistants/), Chankramath said, must expand past accuracy and latency, including your internal customers’ Net Promoter Score.

Then share all your learnings — and those metrics — with your stakeholders and users to increase adoption via proof of benefits.

## Golden Paths With Guardrails

“The goal isn’t just using agents. It’s using them wisely,” said [Matthew Vollmer](https://www.youtube.com/watch?v=aA0Io-E2vyc), head of the Blink deep-code research agent at Coder. “By putting guardrails in place, we keep things productive and safe.”

According to him, this requires:

1. **Context provided.** “Think of them as new hires,” he said. Provide agents with access to documentation, policies and relevant codebases. Without context, agents become another bottleneck.
2. **Responsible delegation.** “We need to control who’s assigning tasks to agents and make sure those tasks are appropriate,” Vollmer said, especially in early adoption. Give these tools to senior developers first.
3. **Boundaries set.** Guardrails — like isolated, ephemeral environments with strict access controls and usage limits — help maintain security, stability and quality. Also embrace [specification-driven development](https://thenewstack.io/what-is-an-ai-native-developer/), so AI agents don’t put environments at risk or just run up costs charging tokens, but rather do exactly what they are told to do. Aim for the sweet spot, he said, of “self-contained, well-defined tasks,” like small to medium bug fixes.

All of these objectives can be achieved through an internal developer platform, where you can onboard AI agents like teammates.

“One of our engineers actually described his experience as pairing with a super fast junior dev who could write code at 100 times the speed of a human junior developer,” he said. “By assigning agents these types of jobs, you can protect your team’s innovation time so dev brains stay focused on high-value work while the AI handles some of those grunt tasks.”

Both AI and platform engineering are best served where frustration runs high. Platform engineering aims to reduce developer cognitive load. Something that, if done right, AI can help with, which doesn’t just help the developer, but your entire software organization.

According to the [Atlassian State of Developer Experience in 2025](https://www.atlassian.com/blog/developer/developer-experience-report-2025), developers are using time saved by AI to focus on improving code, developing new features, and creating documentation. When platform-driven AI adoption — or really platform engineering in general — is done right, it leads to even more time spent on value-driven activities.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/24668a31-cropped-cfb880a9-jkriggins-2019-headshot-the-new-stack.jpeg)

Jennifer Riggins is a culture side of tech storyteller, journalist, writer, and event and podcast host, helping to share the stories where culture and technology collide and to translate the impact of the tech we are building. She has been...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)