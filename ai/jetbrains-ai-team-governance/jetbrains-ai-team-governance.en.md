**Engineering teams have spent the past few years** picking their own AI tools — an IDE here, a terminal-based coding agent there, a browser extension for code review elsewhere — leaving engineering leaders with little visibility into what their developers actually use or what it costs.

JetBrains is now pushing to close that gap without asking anyone to give up their tool of choice. The company announced on Tuesday [JetBrains AI for Teams and Organizations](https://www.jetbrains.com/agentic-software-development/), a set of capabilities that sit above whatever AI tools a team already relies on, adding shared context, reusable agentic processes, organization-wide governance, and cost controls. Business customers will see the first pieces roll out gradually through July and August.

> “Teams shouldn’t have to standardize on a single vendor to benefit from AI.”

In a blog post [announcing](https://blog.jetbrains.com/blog/2026/07/07/jetbrains-ai-for-teams-and-organizations-from-fragmented-ai-usage-to-coordinated-software-development/) the update, [Oleg Koverznev](https://www.linkedin.com/in/oleg-koverznev/), head of agent systems at JetBrains, notes that the ability for developers to reach for whichever tool suits the task at hand is worth preserving, writing that this “freedom is a good thing.”

“Teams shouldn’t have to standardize on a single vendor to benefit from AI,” he writes.

The expansion continues a trajectory JetBrains has been running for more than two years. It started with a [coding assistant back in 2023](https://thenewstack.io/jetbrains-launches-new-ai-assistant-powered-by-multiple-llms/) that brought AI into the IDE, followed [a year later by Junie](https://blog.jetbrains.com/junie/2025/01/meet-junie-your-coding-agent-by-jetbrains/), which turned that into an agent capable of planning and executing its own tasks. JetBrains took Junie outside the IDE in March, [launching a standalone CLI](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/) alongside JetBrains Air, an environment for running multiple agents side by side; [Junie itself left beta in June](https://blog.jetbrains.com/junie/2026/06/junie-coding-agent-out-of-beta/).

This latest step goes further, building a governance layer above every AI tool an engineering org uses, not just JetBrains’ own.

![Access coding agents in a unified IDE.](https://cdn.thenewstack.io/media/2026/07/b19fd52a-screenshot-2026-07-08-at-13-59-28-.png)

*Access coding agents in a unified IDE.*

Four pieces make up the rollout. Automations can trigger cloud agents from repository events or a schedule, running long tasks in managed environments and delivering results the rest of the team can see.

![Team automations and cloud agents](https://cdn.thenewstack.io/media/2026/07/613d392f-automations-1024x666.png)

*Team automations and cloud agents*

JetBrains Context, meanwhile, promises agents faster access to a codebase’s own intelligence — cross-repository knowledge, code examples, references — cutting agent turns, execution cost, and errors.

Above all this, JetBrains Central is the management console: one place for engineering leaders to see which AI tools their teams use, along with access controls, model and agent policies, analytics, and team-level cost attribution.

JetBrains, in fact, [first announced Central in March](https://blog.jetbrains.com/blog/2026/03/24/introducing-jetbrains-central-an-open-system-for-agentic-software-development/), running it as an early access program with a small group of design partners; this week’s announcement extends it to business customers generally.

![JetBrains Central](https://cdn.thenewstack.io/media/2026/07/ae9b8858-central-1024x663.png)

*JetBrains Central*

Central, perhaps, is the answer to a problem Koverznev describes — that letting developers pick their own tools, without any shared system to manage them, has a price.

“Individual developers become more productive, while organizations are left with fragmented workflows, isolated context, and growing costs,” he writes. “AI shouldn’t force organizations to choose between developer flexibility and organizational control.”

> “Individual developers become more productive, while organizations are left with fragmented workflows, isolated context, and growing costs. AI shouldn’t force organizations to choose between developer flexibility and organizational control.”

Finally, the companion JetBrains Central CLI pulls in command-line tools like Claude Code, Codex, and Gemini CLI into that same console, so a developer’s use of a rival’s agent is tracked the same way as their use of Junie. JetBrains is also linking to external tools through the Model Context Protocol ([MCP](https://modelcontextprotocol.io/docs/getting-started/intro)) and to external agents through the Agent Client Protocol ([ACP](https://www.jetbrains.com/acp/)), a decision intended to avoid locking teams into JetBrains’ own agents to get the governance benefits.

Tying into all this, JetBrains is also changing how it bills business customers for AI. The company has run a credit-based system for individual and team plans since [August 2025](https://blog.jetbrains.com/ai/2025/08/a-simpler-more-transparent-model-for-ai-quotas/), but business customers were on a separate license structure that reset monthly.

Moving forward, business customers get the same credit model, with 12-month validity replacing that monthly reset.

## Why the IDE isn’t the center anymore

JetBrains’ announcement lines up with a broader argument *The New Stack* made back in February: Orchestration in software development [is moving away from the IDE](https://thenewstack.io/ide-vs-desktop-agent/) and toward agent control planes, as coding work increasingly happens in a terminal or in separate desktop apps that coordinate multiple agents. IDE-first vendors, the piece argued, faced a choice — refine the editor into what it called “the best review-and-debug surface,” or build the coordination layer themselves.

JetBrains Central, in particular, looks like the company choosing the latter, layering governance over rival agents rather than trying to out-build them.

The company is far from the first to embrace this opening. In June, Cursor [launched an enterprise layer](https://cursor.com/blog/organizations) that lets companies manage budgets, model access, and agent permissions by department from a single dashboard.

On top of all that, owning the model layer matters to IDE-makers because it reduces their dependence on the very agents they’re now trying to govern. JetBrains rolled out [a new open-source coding model](https://thenewstack.io/jetbrains-mellum2-open-source-coding-model/) in June, built to run on a company’s own infrastructure rather than through Claude Code or Codex’s APIs. Cursor has done the same with [its own Composer models](https://thenewstack.io/cursors-composer-2-beats-opus/), though it now has considerably deeper pockets to chase that goal following its bumper [$60 billion acquisition by SpaceX](https://thenewstack.io/spacex-cursor-ai-coding/) — with [a jointly built model expected as soon as this week](https://finance.yahoo.com/technology/ai/articles/spacexai-plans-launch-model-cursor-210200389.html).

None of this means JetBrains sees hands-on coding moving out of the IDE itself. Koverznev reckons that the IDE remains where developers do their most direct work, with JetBrains simply building outward from it.

“Around [the IDEs], we’re building the services that help teams coordinate AI work across repositories, terminals, agents, and cloud execution environments,” he writes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)