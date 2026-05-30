Your AI agent has tool access. What it’s missing is the knowledge that makes those tools useful

You’ve probably connected Claude Code to your GitHub. Maybe your Jira. It worked – for you. Then someone asked, “Can we roll this out to the team?” and you realized how much was held together by context that only you have.

Scaling AI agents across your org hits three walls fast: security blocks approvals, too many MCP tools overwhelm the context window, and your agent still can’t answer basic questions like “who owns this service?”

![Diagram of an AI agent connected to multiple tools, making it confusing to answer a simple question.](https://cdn.thenewstack.io/media/2026/05/2f1795c7-1-1024x536.png)

**An AI agent connected to multiple tools, making it confusing to answer a simple question.**

## Security blocks you

The first roadblock you’re likely to encounter is security. In most organizations, MCP servers require review and legal approval of each data source before they can be used. Some customers have told us that they have AI committees for this. At best, it takes months to approve new models and MCP servers. At worst, they’re entirely blocked.

*“It took us over 9 months to get GitHub Copilot approved for internal organization usage. MCP servers are entirely blocked.”*

– Platform lead in a large financial institution

> *“It took us over 9 months to get GitHub Copilot approved for internal organization usage. MCP servers are entirely blocked.”*
>
> – Platform lead in a large financial institution

When you do get approval to introduce MCPs, you want your agents to be smarter and connected to more data, so you enable as many tools as possible. Agents then end up with 10+ MCP servers and hundreds of (MCP) tools. But if every tool definition gets loaded into the context window, you’ll end up with inflated costs and higher latency.

Anthropic’s engineering team [documented this problem](https://www.anthropic.com/engineering/code-execution-with-mcp) and estimated that agents consume 150,000 tokens just loading the MCP tool definitions. You may have even seen this yourself in Cursor or other IDEs, where they show errors and alerts about lower-quality responses.

![Screenshot of Cursor IDE showing a warning on having too many MCP tools, which can degrade performance.](https://cdn.thenewstack.io/media/2026/05/b10d59ec-2-1024x536.png)

*Cursor IDE shows a warning on having too many MCP tools, which can degrade performance.*

## Accuracy fails

Let’s say you’ve solved the previous two roadblocks of security and tool overload; your agent still won’t be able to answer basic questions.

If you try asking your agent, *“What are my open PRs?”*

* It won’t know who “me” is.
* It won’t know if “open” means draft, approved, or just not merged.
* It doesn’t know which repos or orgs to search.
* It might spend minutes querying different repositories and still miss half of them.

Or if you tried *“What’s the deployment status of this service?”, it won’t know the answers to…*

* What is a service?
* What is a deployment?
* Which pipeline represents it? All your pipelines have similar names.

So the agent resorts to guessing. Educated guesses, sure, but still guesses.

You wouldn’t hire a human and expect them to know the answers to all these questions immediately. The same goes for agents. They both need onboarding to understand your company’s terminology and ways of working.

## AGENTS.md doesn’t scale

You’ve probably tried [AGENTS.md](https://agents.md/) or similar approaches – a markdown file that explains your codebase to the agent. It works for one repo. But what about when your company has 1,000 repos? How do you keep everything in sync? Do the rules apply evenly across all teams? How do you manage context at that scale?

This is where [context engineering](https://www.port.io/glossary/context-engineering) comes in – managing, curating, and delivering the right context to AI systems at scale. If you’ve already solved these problems for developers, you can solve them for AI agents too.

What’s missing is a Context Lake – a layer of organizational knowledge your agents can query. Not just tool access, but understanding: ownership, dependencies, and what “production-ready” means here.

## What is a Context Lake?

You need a layer between your agents and your tools – one that holds the knowledge raw API access can’t provide. Who owns this? What depends on it? What does “production-ready” even mean here?

That’s what a Context Lake is: a unified layer of organizational knowledge that AI agents can query.

Your agent has GitHub access. It can list every repo. But ask it “which services does the Payments team own?” and it’s stuck – that relationship isn’t in any API. MCP gives agents tools. A Context Lake gives them understanding.

> “MCP gives agents tools. A Context Lake gives them understanding.”

Think of it as everything a new engineer learns in their first months, but structured for machines and humans alike.

You might already have a service catalog. But catalogs are built for humans to browse. A Context Lake is built for agents to query – structured for programmatic access, not just documentation.

![Screencap of a service in Port that is linked to other infra assets, building an AI agent-compatible context lake.](https://cdn.thenewstack.io/media/2026/05/137051f5-3-1024x536.png)

*A service in Port that is linked to other infra assets, building an AI agent-compatible context lake*.

## Use cases

*“Who owns this service? Who’s on-call? If something breaks at 2 a.m., who gets paged?”*

Without a Context Lake, your agent has no idea. With a Context Lake, it knows that the payment service belongs to the Payments team, that Sarah is on-call this week, and that escalations go to the #payments-incidents Slack channel.

*“What breaks if I change this? What services consume this API? What downstream systems depend on this database?”*

Your agent needs to know the blast radius before making changes. A Context Lake maps these relationships explicitly, so it can answer ‘what else breaks?’ before touching anything.

> “Your agent needs to know the blast radius before making changes. A Context Lake maps these relationships explicitly.”

*“What is a service? How does a GitHub repo become a service? What’s the difference between a deployment and a release?”*

Every organization has its own terminology. A [Context Lake translates raw data](https://thenewstack.io/better-context-will-always-beat-a-better-model/) into your company’s language. A GitHub repo isn’t just a repo. It’s mapped to a service, owned by a team, and runs in specific environments.

*“How critical is this? Who does it affect? How should I prioritize?”*

Your AI agent doesn’t understand what “production-ready” means in your organization. It doesn’t know that checkout-service handles $2M daily and requires P1 response times, while internal-tools can wait until Monday.

A Context Lake captures this [business context](https://thenewstack.io/how-precog-adds-business-context-to-make-enterprise-data-ai-ready/): revenue impact, customer tiers, SLA requirements, and compliance scope. Agents and humans can now prioritize based on what actually matters.

## What becomes possible

With a Context Lake, you stop getting different answers depending on how you phrase the question and which tools you connected. You now get consistent, deterministic answers. Ask “What are my team’s open PRs?” and you get the same reliable answer every time, because the relationships are defined, not inferred.

A developer in VS [Code uses GitHub Copilot](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/) to understand the blast radius of a change. The agent queries the Context Lake to find downstream dependencies. The same developer checks which libraries are approved for their team, or which tasks to pick up next.

![Screenshot of an agent answering a query with and without a Context Lake, showing a more reliable output with a Context Lake.](https://cdn.thenewstack.io/media/2026/05/3a357981-4-1024x536.png)

*With a Context Lake, AI agents answer reliably and accurately.*

This opens up workflows that weren’t possible before:

* PR review routing – Agent assigns reviewers based on component ownership, contributor availability, and recent activity in the codebase. No more guessing who knows this code best.
* Day planner – A new engineer asks, “What should I work on?” The agent pulls together their team’s active incidents, Jira tickets, urgent bugs, and failed monitors into a single prioritized view.
* Incident triage – Agent receives an alert, checks service criticality and SLA tier, pages the right on-call, and opens a Slack channel with relevant runbooks attached.
* AI agent delegation – When you hand off a task to an AI agent, it gets the full picture: business priority, scorecards to measure progress, historical related tasks, and the standards it needs to meet.

## How it works

As AI increasingly embeds itself in our work, we redesigned Port’s core pillars to serve both humans and AI agents.

![Diagram showing Port context lake, built of integrations, with guardrails, tools, and memory.](https://cdn.thenewstack.io/media/2026/05/5712442f-5-1024x536.png)

*Diagram showing Port context lake, built of integrations, with guardrails, tools, and memory*.

Port’s Context Lake starts with [integrations](https://docs.port.io/integrations-index). Data flows into Port from GitHub, Jira, AWS, PagerDuty, and dozens of other tools. You then map it to your business terminology: a GitHub repo becomes a service, a Jira project becomes a team’s backlog, and an AWS resource becomes part of an environment. Ties it all together. You define blueprints for services, teams, environments, and deployments, then build relationships between them. When you query a service, you get the same answer every time: who owns it, what depends on it, and whether it meets your standards.

To track your organization’s SDLC standards, we track your scorecards. You define what “production-ready” means, which services meet security requirements, and what targets to hit.

To control which agents can see or do what, we use the same access controls used by human users, so they only see what the requesting user can see.

Humans interact through dashboards and the Port UI. AI Agents interact through the [Port MCP server](https://docs.port.io/ai-interfaces/port-mcp-server/overview-and-installation) or API. Both draw from the same source of truth.

## What’s next

We’re working closely with customers to understand [what else their agents need](https://thenewstack.io/the-architects-guide-to-understanding-agentic-ai/).

Building a Context Lake still takes effort. We’re adding self-discovery capabilities – AI that finds relationships in your data and suggests how to model it. Our goal is a Context Lake that builds itself based on your feedback and usage patterns.

Also, we realize that not all data belongs in a Context Lake. Temporal data, such as logs, Slack messages, and long documents, change constantly and don’t require persistent modeling. However, this data is still useful for certain use cases. We’re experimenting with solutions like read-only actions and exploring MCP connectors to help with this kind of data as well.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/05/24f5579b-cropped-bff51576-zohar.png)

Zohar Einy is the CEO of Port, the agentic engineering platform that is helping customers like GitHub, Visa, and PwC move from manual to autonomous engineering. Zohar began his career in the Israel Defense Forces' 8200 unit as an engineer,...

Read more from Zohar Einy](https://thenewstack.io/author/zohar-einy/)