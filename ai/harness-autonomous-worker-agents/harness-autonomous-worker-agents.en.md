The agentic platform Harness launched [Autonomous Worker Agents](https://www.harness.io/products/platform/worker-agents) on Tuesday, enabling enterprises to replace fixed scripts in their delivery pipelines with AI agents that reason through tasks such as deployment, testing, and security scans, all under the governance and audit controls those companies already use.

Harness’ pipelines have long run through a series of deterministic steps, like deploying code to Kubernetes or running a security scan. Now, any of those steps can run as an agent instead, which makes them far more flexible while keeping the same guardrails.

The company isn’t new to agents, of course. Harness’ expert agents, generally available since last year, advise developers and help author pipelines from a chat window or an IDE. Autonomous Worker Agents go a step further: Any step in the pipeline can now run as an agent, on infrastructure that stays within customer control.

> “Building an agent is becoming easier and easier and easier, but the harness is where the hard work is.”

But as [Harness](http://harness.io) CEO and founder [Jyoti Bansal](https://www.linkedin.com/in/jyotibansal/) tells *The New Stack*, “building an agent is becoming easier and easier and easier, but the harness is where the hard work is.”

“When I started the company, I gave the name Harness because I thought all the code that the developers are writing, it needs a safety harness around it,” Bansal says. To him, Worker Agents mark the company’s fourth phase, after reliable deployments, [the rest of the work that happens after code](https://thenewstack.io/harness-ceo-jyoti-bansal-on-why-ai-coding-doesnt-help-you-ship-faster/), and the expert agents.

He believes this fourth phase is quite different, though.

> “Running agents in production is a very different beast than running, say, coding agents that we’re all using now.”

“Running agents in production is a very different beast than running, say, coding agents that we’re all using now,” Bansal says. “If you’re using a coding agent, the worst case is you get a bad PR, and some code review agent or some human doing the code review will reject the PR, or your downstream CI/CD pipeline will catch it somewhere. But if you are the downstream CI/CD pipeline, there is no way else to catch it.”

## As simple as Markdown

Building an agent isn’t much different from writing a skill file in Markdown. An agent is defined in a single Markdown file where developers write their instructions in plain English. The release calls it an agent-file format that has “become standard across the industry.” As has become common with these tools, teams that would rather not write the file can have Harness AI generate it. Once it’s up and running, the agent draws on the Harness [Software Delivery Knowledge Graph](https://www.harness.io/blog/knowledge-graph-rag), the company’s map of a customer’s services, pipelines, deployments, incidents, and security findings.

## The safety harness

To make all of this work, Harness is building on top of core features it built over the last few years that, as it turns out, also apply to agents. Worker Agents run on [delegates](https://developer.harness.io/docs/category/delegate), the Harness components that run inside a customer’s own infrastructure, so the agents execute where the production systems live rather than inside Harness’ cloud. Each agent runs in a sandboxed container with restricted file and network access, gets its own identity and permissions, and, crucially, is governed by the same policy engine that gates human deployments.

For enterprises to deploy agents in [this part of the software lifecycle](https://thenewstack.io/ai-has-become-integral-to-the-software-delivery-lifecycle/), they must be able to verify what the agents did. Several startups already sell agent auditability as a product; Harness is baking it into the service. Bansal calls it “a massive challenge” because a pipeline that touches production has to record what triggered an agent, the prompt it ran on, how many turns it took, and what it produced. Harness has already logged all of that in its scripted steps, so an agent becomes just another action in the pipeline it already tracks.

Harness also built in cost controls that govern how many tokens an agent can spend, which Bansal says now comes up in every customer conversation. Worker Agents track token spend per agent and per pipeline, with budget caps that pause for approval before a run gets out of hand.

## An agent marketplace

Harness paired the framework with an Agent Marketplace that opens with dozens of prebuilt agents in three tiers: Harness Managed agents, the company builds and backs with an SLA, Harness Certified agents built by partners and reviewed by Harness, and community agents anyone can publish. Every agent can be forked.

The community tier is where trust gets harder. “If you take an agent that’s built by the community, you take it with a grain of salt,” Bansal says. The sandboxing, scoped credentials, and policy controls hold no matter where an agent comes from, he says, and community agents are open source, so a team can read one before it runs and fork it to fit. For large enterprises, the gate matters more than the catalog: a company can approve a handful of the managed agents for production and block the rest.

Harness is not the only one moving agents into the delivery pipeline. GitHub shipped Agentic Workflows, which run Markdown-defined agents inside GitHub Actions, in preview earlier this year, and GitLab’s Duo Agent Platform lets teams build their own agents across the software lifecycle. GitHub uses the same agent-file convention that Harness uses. The coding-agent vendors are pushing downstream, too.

Bansal doesn’t necessarily see them as competitors, though. He argues that the work that comes after code is written is a different problem, and that the agents handling it have to clear a higher bar. With more than 1,000 enterprise customers, Harness is betting that its edge is twofold: the context its knowledge graph gives its agents, and the years it spent building the mechanisms that keep a production pipeline safe.

## Phase Five: autonomous software engineering

If this is Harness’ fourth phase, the obvious question is what the next one looks like.

> “Phase five, to me, is all about autonomous software engineering.”

“Phase five, to me, is all about autonomous software engineering,” Bansal says. “Where we are going is that the entire software engineering process, from the Jira ticket all the way to production, is an autonomous process, with the set of agents that are doing all the tasks, from the coding agents to the delivery agents that we are launching, and how it’s all orchestrated. But how do you bring humans in the loop in the process, based on the risk that is there, risk of the change, what impact could it have on your production systems?”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)