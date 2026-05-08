Security has emerged as one of the core stumbling blocks in the AI coding space: Companies are racing to connect models to external tools, internal systems, and repositories. Meanwhile, researchers and security firms have spent the past year [warning about prompt injection attacks](https://thenewstack.io/red-teaming-enterprise-ai-agents/) and over-permissioned agents, alongside [concerns around malicious](https://thenewstack.io/ai-agent-skills-security/) third-party “skills” and tool integrations that can give AI systems broad access to files, APIs, and development environments.

The problem becomes more complicated once AI systems move beyond chat interfaces and begin taking action within developer tools. As companies build out [security models for AI agent systems](https://thenewstack.io/securing-ai-agent-systems/), MCP servers — which [connect models to services](https://thenewstack.io/build-mcp-server-tutorial/) such as GitHub, databases, and cloud platforms — are becoming another place where exposed secrets, vulnerable dependencies, and unsafe code can spread through systems before teams catch them.

This rapidly evolving environment is why GitHub is starting to push more security checks directly into the tooling layer itself, rather than waiting until code is committed or deployed.

> “MCP servers are becoming another place where exposed secrets, vulnerable dependencies, and unsafe code can spread through systems before teams catch them.”

## A growing dependency

GitHub on Tuesday [launched](https://github.blog/changelog/2026-05-05-dependency-scanning-with-github-mcp-server-is-in-public-preview/) dependency scanning for its GitHub MCP Server in public preview, while also making secret scanning for the tool [generally available](https://github.blog/changelog/2026-05-05-secret-scanning-with-github-mcp-server-is-now-generally-available/).

[MCP](https://modelcontextprotocol.io/docs/getting-started/intro), short for Model Context Protocol, is an open protocol originally developed by Anthropic that allows AI models to connect to external tools and data sources. The protocol [has become](https://thenewstack.io/why-the-model-context-protocol-won/) a key part of the growing AI agent ecosystem, with Anthropic [recently donating](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/) MCP to the Agentic AI Foundation as the industry pushes toward more standardized ways for models to interact with services and software systems.

GitHub first [launched its own MCP server](https://github.blog/changelog/2025-04-04-github-mcp-server-public-preview/) in April 2025, allowing AI tools and coding assistants to interact with GitHub repositories, issues, pull requests, and other platform features through MCP connections.

The new feature brings GitHub’s dependency scanning to MCP-connected coding environments for repositories with [Dependabot](https://docs.github.com/code-security/dependabot) alerts enabled. Dependabot is GitHub’s security tool for identifying known vulnerable or outdated software dependencies inside projects.

For instance, developers using MCP-connected coding agents such as [Claude Code](https://thenewstack.io/claude-code-and-the-rise-of-personal-software/) or Cursor could give the system a plain-English prompt asking it to review newly added packages for known security issues before code is committed. The agent can then query GitHub’s advisory database through the MCP server and return structured results that include affected dependencies, severity ratings, and suggested package versions to upgrade to.

Ultimately, the goal is to surface security problems while code is being written or modified, rather than later in the development cycle.

> “The goal is to surface security problems while code is being written or modified, rather than later in the development cycle.”

The update follows similar [community requests from developers](https://github.com/github/github-mcp-server/issues/1921) asking GitHub to expose more of its security tooling — including Dependabot and secret scanning — through the MCP server.

## Keep a secret

While dependency scanning focuses on vulnerable software packages, exposed credentials remain another major problem inside AI-assisted development environments. Just this week, *The New Stac*k reported on how a Cursor AI coding agent [wiped PocketOS’s production database](https://thenewstack.io/ai-agents-credential-crisis/) in under 10 seconds after autonomously discovering and using an over-permissioned credential.

These secrets — including API keys, passwords, and authentication tokens — are often temporarily hard-coded into projects during development, only to be later committed to repositories, logs, or shared codebases.

That problem, while not entirely new, has become more acute as developers increasingly rely on AI coding tools to generate and modify code quickly, often with less manual review. Back in March, Gitleaks creator [Zach Rice](https://www.linkedin.com/in/zricethezav/) launched [Betterleaks](https://thenewstack.io/betterleaks-open-source-secret-scanner/), a new open-source secret-scanning tool designed for what he described as the “AI agent era.”

Rice tells *The New Stack* that AI-assisted coding can create a feedback loop where developers move quickly, override warnings, and forget to properly remove credentials from generated code: “I guarantee you, most people are doing that, rather than taking the time to properly manage their secrets,” Rice says.

> “Developers can surface leaked or exposed credentials directly inside MCP-connected coding tools and agents.”

And so GitHub is seeking to address that problem from inside the development environment itself. With [secret scanning](https://thenewstack.io/github-now-enables-you-to-find-and-fix-code-for-free/) now generally available for the GitHub MCP Server, developers can surface leaked or exposed credentials directly inside MCP-connected coding tools and agents.

![Running secret scanning](https://cdn.thenewstack.io/media/2026/05/634e6331-a-1024x596.png)

***Running secret scanning***

## Shifting left

Both updates are part of a broader push to “shift security left” — catching problems at the point of development rather than after code is committed or deployed.

GitHub has been moving in this direction more broadly: its Copilot coding agent [already runs mandatory security scanning](https://github.blog/changelog/2025-10-28-copilot-coding-agent-now-automatically-validates-code-security-and-quality/), including CodeQL analysis, secret scanning, and dependency review, before a pull request reaches a human reviewer. The MCP server updates extend that same logic into the AI-assisted coding environment itself.

As agents write and modify code faster than developers can manually review it, the window between code being written and code hitting production is getting shorter. GitHub is betting the right place to close it is inside the tools themselves, where agents are continuously checked for risky behavior as they work.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)