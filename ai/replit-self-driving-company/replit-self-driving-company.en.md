**Replit CEO and co-founder Amjad Masad has spent the past year watching AI agents** absorb the routine execution inside his own company, and in a thread posted to [X on Monday,](https://x.com/amasad) he argues the same shift is bearing down on everyone else, with businesses moving toward a self-driving company where, in his words, “humans exercise judgment and agents execute most of the work.”

He rests the case on Ronald Coase’s 1937 question of why firms exist in the first place, the economist’s answer being that companies survive because coordinating work inside them beats coordinating it through open markets, and he contends AI agents are about to collapse the internal coordination costs — the management, the meetings, the reporting — that firms have swallowed as fixed for nearly a century.

In the thread, [Masad](https://www.linkedin.com/in/amjadmasad/) posted, [“The Rise of the Self-Driving Company](https://replit.com/blog/rise-of-self-driving-company),” in which he writes that “every company in the Fortune 500 will be a Self-Driving Company” by the end of 2030.

> “Every company in the Fortune 500 will be a Self-Driving Company” by the end of 2030.

## What the Agent Habitat is

Replit is moving toward that vision with [Replit for Business](https://replit.com/enterprise), which gives AI agents access to company systems, data, and workflows while keeping permissions and approvals in place.

Masad calls the underlying concept the “Agent Habitat,” a space where agents can work with employees and one another without having unrestricted access to company resources. It’s still more of a blueprint; Replit has not yet published a full technical specification explaining how those controls would work together.

## Why agent sprawl is risky

Masad is trying to solve a rising problem as companies deploy more AI agents. Many still operate through scattered chat windows, personal accounts, and custom scripts, often with whatever credentials and data employees give them. Companies have little visibility into what those agents can access or what they’ve done.

Giving agents more freedom might not be the answer, either. Recent research shows [how easily coding agents can overstep](https://thenewstack.io/coding-agents-overstep-scope/) their intended scope, even when doing legitimate work.

> Replit’s Agent Habitat aims to strike a balance by giving agents access to the tools and data they need while enforcing permissions.

Replit’s Agent Habitat aims to strike a balance by giving agents access to the tools and data they need while enforcing permissions. Masad also wants companies to benefit from what their agents learn. If an employee corrects an agent, that feedback could become part of the instructions other agents follow. One team could reuse a workflow across the company rather than building it from scratch.

## Keeping humans in control

On Tuesday, Replit [moved closer to that vision with Cloud Agents](https://replit.com/blog/anyone-can-bring-ideas-to-company-codebase), which let employees change a company’s codebase without setting up a development environment or needing to know how the application works behind the scenes.

Engineers still have the final say over what ships, but employees can bring them tested changes instead of waiting for someone to pick up a ticket.

Replit also lets administrators set up shared development environments, so employees don’t have to configure repositories, database, and services themselves. Credentials are managed centrally rather than distributed across teams, reflecting a trend that [shifts away from long-lived credentials](https://thenewstack.io/vercel-oidc-static-credentials/).

## Cloud Agents and code reviews

The company is also experimenting with agents learning from code reviews. When an engineer flags a problem, Cloud Agents can suggest updates to the team’s shared instructions, called “skills,” so future agents can avoid making the same mistake. Engineers must approve those updates, and the feature remains in early access.

Replit says the shared instructions are already helping reduce costs. In its own testing, the company reported a 51% drop in token consumption and said a routine data task that previously took 16 minutes could be completed in one, without sacrificing output quality. That’s a notable improvement, especially since [recent research has shown how much an agent’s performance depends on its harness](https://thenewstack.io/letta-frontiermemory-agent-harness-benchmark/?utm_source=chatgpt.com) and how it handles memory.

The company has also seen gains in its own engineering teams, where code output nearly tripled during the first half of 2026 without longer review times or an increase in reversions or production incidents. Agents are now being used beyond engineering, with designers building features, and support teams investigating customer issues.

> Agents are now being used beyond engineering, with designers building features, and support teams investigating customer issues.

There are limits to those numbers. Replit hasn’t shared enough detail to independently verify the gains or separate the impact of agents from other changes to how its teams work. What works at an AI-native company like Replit could also be much harder to pull off at a large enterprise with decades of existing systems and processes.

Cloud Agents are now generally available to Pro and Enterprise customers, while skills remain in early access. The broader Agent Habitat vision is still taking shape, and Replit hasn’t yet demonstrated that agents can handle the kind of company-wide work Masad describes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)