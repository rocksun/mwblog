Every developer who has used an AI coding assistant has experienced the same frustration: You spend an afternoon teaching Claude Code or Codex the quirks of your codebase, the naming conventions, the deployment pipeline, and the legacy database schema nobody documented. Then you close the session. When you open a new one, most of that context is gone.

So, you have to start over. This cycle of context loss and re-explanation has become one of the most persistent friction points in AI-assisted development. Two open-source projects are now attacking it from fundamentally different directions.

The patterns here will feel familiar to anyone who has managed infrastructure. Think of session-based AI tools as stateless containers that get wiped on every restart. They are fast, disposable, and context-free. Now think of what happens when you add persistent volumes, long-running processes, and a learning loop that improves the system over time. That is the early transition that [OpenClaw](https://github.com/openclaw/openclaw) and [Hermes Agent](https://github.com/NousResearch/hermes-agent) represent. They are pushing the AI assistant from a session-bound tool toward a persistent agent runtime.

## The always-on agent is a new software category

I’d argue the AI agent landscape is splitting into two species, and most developers haven’t noticed yet. One species lives inside your terminal, your IDE, or your browser tab. You open it, use it, and close it. Tools like Claude Code, Codex, and Cursor are powerful within a session, but they carry limited context between sessions. The workarounds are manual. You write CLAUDE.md files, maintain memory directories, and build elaborate markdown-based “brain” systems. One developer [documented](https://github.com/anthropics/claude-code/issues/34556) 59 context compactions across 26 days of daily Claude Code use before building his own persistence layer from scratch.

> Tools like Claude Code, Codex, and Cursor are powerful within a session, but they carry limited context between sessions.

The other species permanently lives on your infrastructure. It runs while you sleep. It reaches you on Telegram during your commute. It remembers what it learned last month. It gets better over time. OpenClaw and Hermes Agent are the two most prominent examples of this second species, and they represent very different philosophies about how a permanent agent should work.

That said, this is not a clean binary split. Session-native tools are already adding persistence. Claude Code now has auto-memory that writes notes to disk across sessions. Cursor maintains workspace-level context. But the architectural ambitions of OpenClaw and Hermes Agent go further than incremental memory features bolted onto a session-based tool. They are designed from the ground up to run continuously, learn over time, and reach users across messaging platforms.

## OpenClaw and the ecosystem play

OpenClaw started as a weekend project by Austrian developer Peter Steinberger in late 2025. Originally called Clawdbot, it became one of the fastest-growing open-source projects on GitHub, surpassing 345,000 stars as of early April 2026. In February 2026, Steinberger [announced](https://steipete.me/posts/2026/openclaw) he was joining OpenAI and that OpenClaw would move to an independent foundation.

The growth was not accidental. OpenClaw solved a problem that developers had been waiting for someone to solve. It gave them a self-hosted AI agent that connects to the messaging apps they already use. WhatsApp, Telegram, Slack, Discord, Signal, and more than 50 other integrations. It works with every major model provider. Anthropic, OpenAI, Google, and local models through Ollama. The ecosystem grew to include [ClawHub](https://clawhub.ai/), a public skills registry with thousands of community-built skills, multiple managed hosting providers, and companion apps for macOS and iOS.

> OpenClaw solved a problem that developers had been waiting for someone to solve.

Think of OpenClaw as Android for AI agents. It has the scale, the third-party ecosystem, and the fragmentation that comparison implies. And, as with early Android, the security story is rough.

Within weeks of its explosive growth, a coordinated supply chain attack surfaced. [Koi Security](https://www.esecurityplanet.com/threats/hundreds-of-malicious-skills-found-in-openclaws-clawhub/) audited all 2,857 skills on ClawHub at the time and found 341 malicious entries, with 335 traced to a single campaign it named ClawHavoc. [SecurityScorecard](https://conscia.com/blog/the-openclaw-security-crisis/) reported tens of thousands of publicly exposed OpenClaw instances across the internet. CVE-2026-25253 (CVSS 8.8) involved unsafe automatic WebSocket connection behavior that could expose authentication tokens, contributing to one-click compromise scenarios described by multiple security researchers.

[Microsoft](https://www.microsoft.com/en-us/security/blog/2026/02/19/running-openclaw-safely-identity-isolation-runtime-risk/) advised treating the runtime as potentially influenceable by untrusted input and recommended against running it on standard personal or enterprise workstations. [Cisco](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare) called personal AI agents like OpenClaw “a security nightmare.”

The ClawHub marketplace operates like npm in its early days. Publishing a skill required only a one-week-old GitHub account. No automated static analysis, no code review, no signing requirement.

OpenClaw has since [partnered](https://openclaw.ai/blog/virustotal-partnership) with VirusTotal to scan uploaded skills and has added security guidance for operators. The trust model is improving, but remains a work in progress.

### Model-agnostic flexibility

OpenClaw supports switching between any major LLM provider without configuration changes. Model agnosticism is one of its strongest features for developers who want to avoid vendor lock-in or need to route different tasks to different models based on cost and capability.

### Always-On Presence Across Channels

The agent runs as a background service and maintains a presence across all connected messaging platforms simultaneously. A developer can start a task on their workstation, receive a completion notification on Telegram during dinner, and send follow-up instructions from their phone. This cross-channel persistence is the feature that drove OpenClaw’s viral adoption more than any other.

> Cross-channel persistence is the feature that drove OpenClaw’s viral adoption more than any other.

OpenClaw proved that developers want agents that outlive their browser tabs. The security incidents proved that the infrastructure for those agents is nowhere near ready for production.

## Hermes agent and the research play

[Hermes Agent](https://hermes-agent.nousresearch.com/) launched in February 2026 from Nous Research, the lab behind the Hermes, Nomos, and Psyche model families. At roughly 22,000 GitHub stars as of early April 2026, it is a fraction of OpenClaw’s size. The community skill library is smaller. The brand recognition is lower. What makes Hermes Agent worth watching is not its current scale. It is the architecture underneath.

Where OpenClaw focused on the breadth of integration, Hermes Agent focused on the depth of learning. The project’s tagline, “the agent that grows with you,” describes an architecture built around a closed learning loop. Three components make this loop work.

First, persistent memory. Hermes uses FTS5 full-text search over all past sessions stored in SQLite, combined with LLM-powered summarization. The agent can recall conversations from weeks ago, search its own history, and build a deeper understanding of who you are and how you work. This is not a CLAUDE.md file you maintain yourself. The agent curates its own memory with periodic nudges.

Second, autonomous skill creation. After completing complex tasks, the agent can write a structured skill document that records the procedures, pitfalls, and verification steps it discovered.

The next time a similar task arises, it loads the skill instead of solving the problem from scratch. Skills follow the open [agentskills.io](https://agentskills.io) standard, making them portable across compatible platforms.

Third, a self-training loop. Hermes integrates with [Atropos](https://github.com/nousresearch/atropos), Nous Research’s reinforcement learning framework, to generate batch trajectories and train agent behavior.

> Developers can generate thousands of tool-calling trajectories in parallel, export them, and use them to fine-tune smaller, cheaper models.

Developers can generate thousands of tool-calling trajectories in parallel, export them, and use them to fine-tune smaller, cheaper models. This research-grade infrastructure reflects Nous Research’s identity as a model training lab rather than a product company.

### Multi-instance profiles for Team Workflows

The v0.6.0 release (March 30, 2026) introduced profiles that let developers run multiple isolated Hermes instances from a single installation. Each profile gets its own configuration, memory, sessions, skills, and gateway service. This moves Hermes from “personal assistant” toward a reusable agent operating system.

### MCP server mode for IDE integration

Hermes can now expose its conversations and sessions to MCP-compatible clients via `hermes mcp serve`, as documented in the v0.6.0 release notes. Developers using Claude Desktop, Cursor, or VS Code can browse and search across sessions through the Model Context Protocol. This bridges the gap between the always-on agent and the IDE-native tools developers already use.

### Security through architectural restraint

Hermes takes a more conservative approach to its skill ecosystem. Its documentation describes container hardening with read-only root filesystems, dropped capabilities, and namespace isolation. Filesystem checkpoints create automatic snapshots before destructive operations, with a rollback command to restore the state.

The [Tirith](https://hermes-agent.nousresearch.com/docs/user-guide/security/) pre-execution scanner analyzes terminal commands before they run. No comparably prominent public supply-chain incident has surfaced in Hermes’s ecosystem so far, though the smaller attack surface and younger ecosystem make direct comparison difficult. A project with 22,000 stars will naturally attract fewer attackers than one with 345,000.

Where OpenClaw optimizes for reach and ecosystem breadth, Hermes optimizes for depth of learning. It is smaller, more opinionated, and built by a team that trains the underlying models.

## Choosing between the two approaches

The decision between OpenClaw and Hermes Agent is not a feature comparison. It maps to a deeper question about what you want your agent to become over time.

| Requirement | Recommended Option | Rationale |
| --- | --- | --- |
| Maximum messaging platform coverage | OpenClaw | 50+ integrations vs. 7 for Hermes |
| Persistent cross-session memory | Hermes Agent | FTS5 search + LLM summarization built in |
| Large pre-built skill ecosystem | OpenClaw | Thousands of ClawHub skills (vet carefully) |
| Self-improving agent over time | Hermes Agent | Closed learning loop with autonomous skill creation |
| RL training and trajectory export | Hermes Agent | Atropos integration for research workflows |
| Documented built-in safeguards | Hermes Agent | Conservative architecture; real-world hardening maturity still evolving |
| Community size and third-party support | OpenClaw | 345K+ stars, foundation governance, managed hosting |
| Running on minimal infrastructure | Hermes Agent | $5 VPS or serverless with near-zero idle cost |

Production systems will likely combine elements of both. Hermes already supports installing community skills from ClawHub, and an official migration tool exists for developers moving their configuration from OpenClaw to Hermes. The agentskills.io standard that Hermes adopted is designed to make skills portable across agent platforms, which suggests convergence rather than winner-take-all competition.

## What’s next

OpenClaw and Hermes Agent are best understood as two early, influential prototypes of persistent agent infrastructure. One is ecosystem-first. The other is learning-loop-first. Neither is a finished product, but both point toward a future where AI agents run as long-lived services rather than session-bound assistants.

> As agents become long-running processes that accumulate knowledge about your codebase, your workflows, and your decision patterns, who owns the learned knowledge?

For developers who have managed Kubernetes workloads, the direction of travel is recognizable. Stateless functions gave way to stateful services. Ephemeral containers gave way to persistent volumes. A similar transition is beginning in AI.

The bigger question emerging from this shift is one that neither project has fully answered. As agents become long-running processes that accumulate knowledge about your codebase, your workflows, and your decision patterns, who owns the learned knowledge? The user? The platform? The model provider?

OpenClaw’s move to a foundation and Hermes Agent’s local-first architecture both gesture toward user ownership, but the answer will shape the next generation of developer tooling in ways that go far beyond any single project. Stay tuned.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)