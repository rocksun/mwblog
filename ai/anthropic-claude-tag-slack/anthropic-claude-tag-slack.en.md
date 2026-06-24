Anthropic [has announced Claude Tag](https://www.anthropic.com/news/introducing-claude-tag), a new product that embeds Claude directly into Slack as a persistent, shared team member — one that accumulates institutional knowledge over time, works asynchronously, and can act without being prompted.

The product, available in beta for Enterprise and Team plan customers, replaces Anthropic’s existing Claude in Slack app, which [debuted in October 2025](https://claude.com/blog/claude-and-slack). That original integration let users DM @Claude, invoke it via an AI assistant panel, or tag it in threads for on-demand help — useful, but somewhat transactional. Then [in December](https://claude.com/blog/claude-code-and-slack), Anthropic added Claude Code to Slack, letting developers tag Claude in a conversation and have it spin up a full coding session on the web, posting a pull request back into the thread on completion.

In that sense, Claude Tag does for Slack roughly what Cowork did for knowledge workers: it takes the agent loop that originated in Claude Code and extends it to a new surface and a broader set of tasks, rather than confining it to engineering workflows.

Claude Tag, in many respects, is the next step: rather than Claude joining a conversation on request and then going quiet, it now lives in the channel full-time. Tasks can be scheduled to run over hours or days, with Claude working through them independently — accumulating context, learning the vocabulary of the work, and picking up unresolved threads that would otherwise get buried.

That context isn’t necessarily confined to a single channel, either: Where administrators grant the access, Claude can draw on information from other channels to inform the work in front of it.

![Claude Tag](https://cdn.thenewstack.io/media/2026/06/bf5c26ec-claudegif.gif)

*Claude Tag in action*

## Sense of identity

Claude Tag effectively gives Claude its own identity in the workspace — its own accounts for every connected tool, posting to Slack as the Claude app, opening pull requests under its own GitHub app, or querying a data warehouse under a dedicated service account set up by an admin. If “ambient” behavior is enabled, Claude doesn’t need to be tagged at all — it monitors conversations, flags things it thinks the team needs to know, and follows up on threads that have gone quiet, much like the “auto” mode already familiar to Claude Code users.

> Beyond scoping tool and data access, administrators can also set a ceiling on how many tokens each channel’s Claude is allowed to spend; it’s a guardrail against an autonomous agent running up costs while working unattended.

There’s one Claude per channel, shared by everyone in it, so any team member can see what’s being worked on and pick up where a colleague left off. That multiplayer dynamic is arguably one of the most significant departures from how AI assistants have hitherto worked.

For instance, a task tagged to @Claude by one person can be steered, corrected, and built upon by the rest of the team in real time.

![Multiplayer steering in action](https://cdn.thenewstack.io/media/2026/06/de0e6587-gif3claude.gif)

*Multiplayer steering in action*

Underpinning all of this is what Anthropic calls “agent identity” — the access construct that makes multiplayer AI possible without creating a security mess. [Noah Zweben](https://www.linkedin.com/in/noahzweben/), a member of technical staff on the Claude Code team, [notes in a companion blog post](https://claude.com/blog/agent-identity-access-model) that this model is a necessary foundation for the kind of autonomous, team-wide work Claude Tag is designed to handle.

> “The shift from single player to multiplayer AI in products like Claude Tag makes long-running, team-based work possible.”

“The shift from single player to multiplayer AI in products like Claude Tag makes long-running, team-based work possible,” Zweben writes. “Agent identity ensures that Claude’s access to tools is broad enough to be useful, but scoped enough to be secure at enterprise scale.”

In terms of how this works, Zweben explains why the traditional model — where an AI assistant borrows the permissions of whoever invoked it — needed to be rethought. Agents now schedule tasks and respond to events long after the person who asked has logged off, and in a shared channel with multiple people steering, there’s no single user whose credentials make sense to inherit.

Instead, administrators define what Claude can access at the workspace level, with each channel inheriting a baseline set of permissions that can be tightened or expanded depending on the work being done there.

> “Agent identity replaces the question ‘what can this user do?’ with ‘what can this agent do in this compartment?'”

An engineering channel might get read and write access to GitHub and the data warehouse; a general channel might get read-only. Crucially, because Claude operates under its own accounts rather than anyone’s personal credentials, a shared channel can never serve as a backdoor into someone’s private documents.

“Agent identity replaces the question ‘what can this user do?’ with ‘what can this agent do in this compartment?'” Zweben writes.

## Race for the Slack layer

Team messaging platforms are fast becoming the primary control layer for AI agents in the enterprise — the place where work gets assigned, monitored, and reported back on. GitHub has [brought Copilot into Microsoft Teams](https://github.blog/changelog/2025-09-19-work-with-copilot-coding-agent-in-microsoft-teams/), for instance, where OpenAI’s [Codex includes](https://openai.com/index/codex-now-generally-available/) a native Slack integration that lets teams delegate tasks directly from threads. And Cognition’s [Devin has been built around Slack](https://cognition.com/blog/devin-generally-available) from the get-go.

Block, the Jack Dorsey-led company behind Square and Cash App, [has also spent some time building something akin to this from scratch](https://thenewstack.io/how-block-manages-its-fleet-of-ai-coding-agents-from-slack/), using its open-source Goose framework to develop an agent orchestration system its engineers manage entirely from a single Slack thread.

Whichever AI ends up as the default presence in the channel where work is coordinated gains both a distribution advantage and a compounding data advantage, making it progressively harder to displace. For a company already running Claude Code in its engineering org, adding Claude Tag to its Slack channels is a natural next step — and one that deepens that dependency considerably.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)