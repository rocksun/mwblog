AI coding companies clearly agree that autonomous agents are becoming central to software development, but *how* those systems should operate — and where developers fit into the loop — is still up for debate.

[Amp](https://ampcode.com/), the AI coding startup that [spun out of Sourcegraph](https://sourcegraph.com/blog/why-sourcegraph-and-amp-are-becoming-independent-companies) in late 2025, revealed this week a rebuilt version of its CLI, dubbed [**Neo**](https://ampcode.com/news/neo), redesigned to be remote-controllable, plugin-powered, and better suited to longer-running agent workflows.

At the same time, the company has also been arguing that “[the coding agent is dead](https://ampcode.com/news/the-coding-agent-is-dead).” More precisely, Amp believes the current model of AI coding agents — systems tightly bound to one editor, one terminal, and one user session — is beginning to give way to agents that operate across environments, are more autonomous, and require less direct supervision.

> Amp believes the current model of AI coding agents — systems tightly bound to one editor, one terminal, and one user session — is beginning to give way to agents that run operate environments.

That creates an apparent contradiction: If agents are moving beyond the terminal, why rebuild the terminal at all? Amp’s view is that the terminal is becoming more of a control surface — one of many places where developers interact with agents.

“The terminal still matters and will matter,” the company writes. “There will be moments where you want the agent right next to you.”

## Rebuilding the CLI

![Neo](https://cdn.thenewstack.io/media/2026/05/6c2e1900-gif1.gif)

*Neo*

A core part of the all-new Neo is the remote control. When developers start an Amp CLI thread locally, they can now connect to and manage that same session remotely through Amp’s web interface. The system streams live updates from the terminal session into the browser, while also allowing users to send follow-up prompts, queue messages, interrupt tasks, or cancel the agent entirely from outside the command line.

![Remote control](https://cdn.thenewstack.io/media/2026/05/98bf79b3-gif2-remote-contorl.gif)

*Remote control*

Amp says the underlying architecture enabling that remote interaction was one of the main reasons it rebuilt the CLI from scratch.

Amp co-founder and CEO [Quinn Slack](https://www.linkedin.com/in/quinnslack) points to that architectural change in a [post on X](https://x.com/sqs/status/2052129216007971230?s=20), noting that he was still able to ship features over airplane wifi because the new setup sends “~95% less data to/from the server.”

According to Slack, that reduction comes from moving the agent loop itself into the cloud rather than running it directly inside the terminal session.

It’s worth noting that Amp isn’t alone in moving coding agents beyond the local terminal session.

Both [GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-remote-control?utm_source=chatgpt.com) and [Claude Code](https://code.claude.com/docs/en/remote-control?utm_source=chatgpt.com) have recently introduced remote control capabilities that allow developers to monitor and interact with long-running coding sessions from outside the terminal.

Elsewhere, Neo also introduces a [plugin system](https://ampcode.com/manual/plugin-api) for extending the CLI with additional tooling and integrations, as well as a new “compaction-first” architecture designed to better manage long-running agent sessions and large conversational histories. The updated CLI can also expose the agent’s intermediate reasoning process during execution, while token and cost tracking are now surfaced directly inside the interface during longer-running sessions.

## Beyond the IDE

Amp says it’s rolling out Neo gradually over the coming days, with users able to request early access directly from the company.

> The new CLI lands amid a growing split in how AI coding companies think software development will evolve.

The new CLI lands amid a growing split in how AI coding companies think software development will evolve. While most agree that autonomous agents will take on a larger role, there is less agreement on what becomes the primary interface around them.

In April, open source AI coding startup [Roo Code announced](https://thenewstack.io/roo-code-cloud-ides-ai-coding/) it was shutting down its VS Code extension and broader IDE-focused tooling in favor of [Roomote](https://roomote.dev/), a cloud-based autonomous coding agent designed to run tasks end-to-end across tools such as Slack, GitHub, and Linear.

[Matt Rubens](https://www.linkedin.com/in/mattrubens/), Roo Code CEO and co-founder, [writes on X](https://x.com/mattrubens/status/2046636598859559114) that his own team had already shifted toward running agents remotely in parallel cloud environments, where systems could open fixes and verify their own output.

“If the agent can create a good PR [pull request] from a single prompt, the interaction model changes completely – you let go of the IDE and focus on driving things end-to-end,” Rubens writes.

As a side point, [Atlassian this week expanded](https://thenewstack.io/atlassian-teamwork-graph-agents/) access to its Teamwork Graph — the company’s indexed enterprise graph spanning Jira, Confluence, Bitbucket, Jira Service Management, and other connected tools — through a new CLI explicitly designed *not* for developers, but for their agents.

![Teamwork Graph CLI](https://cdn.thenewstack.io/media/2026/05/81eeb1c0-gif3.gif)

*Teamwork Graph CLI*

Atlassian [describes it](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/) as “the skill layer for AI coding agents”: Install it once, and Claude Code, Codex, Gemini, or Cursor can query and act across your entire Atlassian stack on your behalf. The humans set it up; the agents do the driving. It’s a small but telling sign that incumbents are beginning to build their tooling agent-readable by default, rather than bolting agent access onto interfaces designed for people.

> Momentum is shifting away from the idea of coding agents living inside a single editor or a tightly scoped local session.

Collectively, these efforts suggest that momentum is shifting away from the idea of coding agents living inside a single editor or a tightly scoped local session. Yet at the same time, the command line itself appears to be finding a new role as a runtime, coordination layer, and control surface for those systems.

Amp is effectively trying to bridge both worlds — betting that even as agents grow more autonomous, developers will still want a place to grab the wheel. And that place might as well be the terminal.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)