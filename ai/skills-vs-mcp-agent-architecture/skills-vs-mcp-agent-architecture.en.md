A venture capitalist is running his entire company on twelve Markdown files. No web application. No workflow engine. No orchestration runtime. Just structured documents in a git repo that teach [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) how to draft emails, triage support tickets, prepare board metrics, and manage product launches.

[CompanyOS](https://adventuresinclaude.ai/posts/2026-02-21-running-a-company-on-markdown-files/), which founder [Brad Feld](https://www.linkedin.com/in/bfeld/) open-sourced in February 2026, connects to eight model context protocol (MCP) servers to access APIs for Gmail, Linear, Help Scout, and other services. But the intelligence lives in the [fashionable-once-again](https://tedium.co/2026/02/17/markdown-growing-influence-cloudflare-ai/) Markdown. Each skill file encodes the workflow, guardrails, tone calibration, and decision logic. The MCP servers are plumbing. If you disconnect them, the skills still run. You just copy and paste instead of auto-sending.

Feld is not alone. Sentry’s [David Cramer](https://www.linkedin.com/in/dmcramer/), who built [Sentry](https://sentry.io/)‘s own MCP server, [writes](https://cra.mr/mcp-skills-and-agents/) bluntly that “many MCP servers don’t need to exist” because they are either poor API wrappers or can be replaced with a skill file.

The examples continue: Supabase open-sourced an [agent-skills repository](https://github.com/supabase-community/agent-skills) that separates timeless development practices from dynamic API interactions. [Microsoft’s .NET Skills Executor](https://devblogs.microsoft.com/dotnet/), which shipped three weeks ago, orchestrates SKILL.md files that invoke MCP tools as a subordinate layer. And a growing number of practitioners are discovering what Júlio Falbo documented in his widely cited post, [“Markdown is the New API.”](https://juliofalbo.medium.com/markdown-is-the-new-api-how-skill-md-and-ai-gateways-unlock-ai-native-organizations-e929d05c0470) The GitHub MCP server consumed roughly 50,000 tokens of context (later trimmed to around 23,000) to teach an agent how to interact with GitHub. A SKILL.md file saying “use the `gh` CLI for these operations” achieved the same result in about 200 tokens.

Something is shifting. Developers are ripping out MCP servers and replacing them with Markdown files. Not because MCP is broken, but because many MCP servers were built to solve the wrong kind of problem.

## The two kinds of problems

Every task an AI agent performs falls into one of two categories: It either needs to *know* something or to *do* something. The confusion between these two categories is driving most of the architectural waste in agent systems today.

When an agent needs to *know* something, you are dealing with a knowledge problem. Coding standards, deployment procedures, triage workflows, company policies, API usage patterns. This knowledge is relatively stable. It changes on the timescale of weeks or months. It can be expressed in natural language. And critically, it fits inside the context window of modern LLMs without any runtime infrastructure.

When an agent needs to *do* something, you are dealing with an execution problem. Querying a database, creating a GitHub issue, sending an email, and reading a Slack channel. Execution requires a runtime. It needs authentication, network access, error handling, and state management. This is what [MCP](https://modelcontextprotocol.io/) was designed for, and it handles it well.

The problem is that many teams built MCP servers for knowledge problems. Someone wanted their agent to understand how to interact with GitHub, so they built or installed an MCP server that exposes dozens of tools for repository management, pull request workflows, issue tracking, and CI/CD operations. The agent now has access to everything. It also has to process a massive tool schema on every invocation, consuming tens of thousands of tokens just to understand what’s available before it can decide what to do.

A skill file that says “use the `gh` CLI, prefer squash merges, always run tests before pushing, and format commit messages as conventional commits” encodes the same workflow knowledge in a fraction of the context window budget. The agent already knows how to use a CLI. It just needed the institutional knowledge about *how your team* uses it.

## The decision framework

Think of this framework as three layers that map to three distinct questions.

The first question is whether the agent needs to *know* something. If the answer involves coding standards, deployment processes, triage workflows, voice and tone guidelines, or any form of institutional knowledge, that belongs in a skill. Markdown files. Version-controlled in git. Reviewed in pull requests like any other code artifact.

The second question is whether the agent needs to *do* something. If the answer requires calling an API, querying a database, reading from a message queue, or interacting with any external system at runtime, that belongs in MCP. A running server with authentication, error handling, and proper observability.

The third question is where things get interesting. Does the agent need to *know how to do something well*? This is the hybrid case, the most common in production systems. The answer here is a skill that references MCP tools. The skill encodes the workflow, the sequencing, the edge cases, and the judgment calls. MCP provides the execution layer underneath.

Feld’s [co-support skill](https://adventuresinclaude.ai/posts/2026-02-21-running-a-company-on-markdown-files/) is a clean example of this third pattern. The skill file defines the entire support triage workflow. It knows how to categorize issues by severity, what tone to use with different customer segments, when to escalate versus resolve, and what information to include in internal notes. The Help Scout MCP server handles API calls, reads conversations, posts replies, and tags tickets. But the skill works even without the MCP server. Without API access, it still triages a pasted customer message, drafts the response in the correct tone, and formats it as copy-ready text. The thinking survives. Only the plumbing disappears.

## The 50x token tax

The cost of getting this layering wrong is not abstract. It shows up directly in your context window budget, and by extension in your API bill and your agent’s reasoning quality.

Consider a concrete example. The [GitHub MCP server](https://github.com/github/github-mcp-server), one of the most popular in the ecosystem, exposes tools for repository management, file operations, search, issues, pull requests, code review, branches, and more. When an agent loads this server’s tool schema, it consumes roughly 23,000 to 50,000 tokens of context window space, depending on the version. That is the context window capacity that the agent can no longer use to reason about your actual task.

> “A SKILL.md file that encodes your team’s GitHub workflow…typically runs 200 to 500 tokens. The agent gets the same operational knowledge with 100x less context consumption.”

A SKILL.md file that encodes your team’s GitHub workflow, including branch naming conventions, PR review requirements, CI expectations, and merge strategies, typically runs 200 to 500 tokens. The agent gets the same operational knowledge with 100x less context consumption. And because the skill is a focused, curated document rather than a raw API surface, the agent makes better decisions. It knows your team’s conventions, not just the universe of possible GitHub API calls.

This is not an argument against the GitHub MCP server. There are genuine execution tasks, creating issues, posting review comments, and merging pull requests that require API access. The argument is that loading a full MCP server to teach an agent *how your team uses GitHub* is like importing an entire database driver library to share a few configuration values. You are paying an infrastructure tax for a knowledge problem.

At scale, this tax compounds. An enterprise agent system connecting to a dozen MCP servers might consume 200,000 to 400,000 tokens in tool schemas alone. That is half or more of the available context window for most models, burned before the agent processes a single user request. Replacing the knowledge components with skill files can reclaim most of that budget for actual reasoning.

## What production systems look like

The pattern emerging across early adopters follows a consistent shape.

Feld’s CompanyOS runs 12 skill files totaling about 2,000 lines of Markdown, connected to 8 MCP servers. The skills handle everything from email voice calibration to root cause analysis using [Toyota’s Five Whys](https://en.wikipedia.org/wiki/Five_whys) method. Every skill has a “standalone mode” that works without any MCP connections. The MCP servers are strictly for API execution, sending the email, querying the database, and searching the ticket system.

[Supabase’s open-source agent-skills repository](https://github.com/supabase-community/agent-skills) takes a similar approach. Skill files encode development practices that are stable across versions, things like database migration patterns, edge function deployment conventions, and testing strategies. These are complemented by MCP servers that handle dynamic API documentation and real-time schema introspection. The boundary is clean. If the knowledge is timeless, it goes into a skill. If it requires a live connection, it goes through MCP.

Microsoft’s .NET Skills Executor, released in early February, makes the layering explicit in its architecture. SKILL.md files define workflows. The executor resolves dependencies, including MCP tool invocations, at runtime. The skill is the orchestration layer. MCP provides the function calls. This is probably the clearest signal that the industry is converging on a two-layer model rather than an MCP-for-everything approach.

Anthropic’s own [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) implementation follows this pattern internally. The skills system that ships with Claude Code uses structured Markdown files to encode best practices for document creation, code generation, and tool usage. These skill files reference MCP tools when execution is needed, but keep the workflow logic in Markdown, which can be version-controlled, reviewed, and customized by users.

## The Git Advantage

One benefit of skills that gets underappreciated is the operational model they enable. Skill files are plain text. They live in git. They go through pull requests. They have blame history and diff views and branch strategies.

This matters more than it might seem. When your agent’s behavior is encoded in an MCP server, changing that behavior means modifying server code, redeploying, and hoping you have adequate test coverage. When the behavior is encoded in a skill file, changing it means editing a Markdown document and committing the changes. The feedback loop is minutes, not hours. And the change is visible to everyone on the team in a format they can read without understanding the server’s implementation language.

Feld’s CompanyOS leans into this heavily. His email voice calibration, the rules that determine how co-comms adjusts tone for different recipients, is a section in a Markdown file. When he wants to change how the system communicates with investors versus customers, he edits a paragraph and commits. No deployment. No restart. No risk of breaking API integrations.

For platform engineering teams managing agent systems across an organization, this operational model is significantly more sustainable than maintaining a fleet of MCP servers that each encode institutional knowledge in application code.

## What to Do on Monday Morning

If you are a platform engineer or team lead evaluating your agent architecture, here is a practical starting point.

Audit your current MCP servers and ask, for each tool they expose, whether that tool solves a knowledge problem or an execution problem. If a tool exists primarily to teach the agent how to use an API rather than to call that API, it is a candidate for extraction into a skill file.

Start with the highest-token-cost servers. The ones with the largest tool schemas are likely the ones encoding the most knowledge alongside their execution capabilities. Extract the knowledge into SKILL.md files and leave the execution tools in MCP.

Adopt the standalone test that Feld uses. Every skill should produce useful output even without MCP connections. If disconnecting the MCP server makes the skill completely non-functional, you probably have an execution concern that belongs in MCP. If the skill still generates the right analysis, recommendation, or draft, you have validated that the knowledge layer is properly separated.

Version your skills in git alongside your application code. Treat them as first-class artifacts with the same review process you use for infrastructure configuration. Skill files that encode business logic, compliance requirements, or security policies deserve the same rigor as Terraform modules or Kubernetes manifests.

## The Layered Future

The skills-versus-MCP conversation is not a competition. It is an architectural clarification that the ecosystem needs.

MCP won the protocol war. Over 30,000 servers are indexed across registries. Every major cloud provider, tool vendor, and AI company supports it. That is not changing. What is changing is the recognition that MCP was designed for tool execution, and that treating it as the sole mechanism for everything an agent needs to know creates systems that are expensive, fragile, and hard to maintain.

> “The agent does not need another orchestration layer. It needs domain knowledge in a format it already understands. And for most of the knowledge problems teams are solving today, a Markdown file is better architecture than a running server.”

The emerging two-layer model is clean. Skills provide domain knowledge in a format that is cheap to process, easy to version, and accessible to every team member. MCP provides tool execution with proper authentication, error handling, and observability. The best agent systems use both, with a clear boundary between them.

Feld’s 12 Markdown files will not replace the enterprise MCP infrastructure. But they demonstrate a principle that scales beyond any individual implementation. The agent does not need another orchestration layer. It needs domain knowledge in a format it already understands. And for most of the knowledge problems teams are solving today, a Markdown file is a better architecture than a running server.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)