[AI coding agents](https://thenewstack.io/crafting-ai-agents-platform/) have spawned a new software supply chain, and a new study suggests the proliferation of new agents is outpacing the security infrastructure around them.

[Mobb.ai](https://mobb.ai/) has released findings from a [large-scale security audit](https://www.linkedin.com/posts/mobbai_the-state-of-ai-agent-skill-security-march-activity-7440480014619471873-qq06?lipi=urn%3Ali%3Apage%3Ad_flagship3_messaging_conversation_detail%3BCPnZ4SLLRsyQFdAH2%2Bhc4g%3D%3D) of 22,511 public skills — reusable instruction sets for AI coding agents like [Claude Code](https://thenewstack.io/anthropic-launches-a-multi-agent-code-review-tool-for-claude-code/), Cursor, GitHub Copilot, and [Windsurf](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/) — collected across four public registries: skills.sh, ClawHub, GitHub, and Tessl.

The audit produced 140,963 security findings and identified a structural gap that no registry has fully closed. That is, skills are scanned at publish time, but once they land on a developer’s machine, they execute with that developer’s full system permissions and almost no runtime verification, Mobb says.

[Eitan Worcel](https://www.linkedin.com/in/worcel/), CEO of Mobb, tells *The New Stack* that “AI coding agents are becoming the default way developers write software.”

“When a developer installs a skill or plugin for their agent, they’re giving that skill the same access they have — their source code, their credentials, and their production systems,” Worcel says.

Worcel said the research was motivated by the absence of any systematic review of the ecosystem. “We noticed no one had systematically reviewed the ecosystem, so we did.”

## A new kind of supply chain risk

Skills are typically markdown files — most commonly formatted as SKILL.md — that contain natural language instructions an AI agent follows, along with shell commands, [MCP (Model Context Protocol)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) server configurations, [IDE](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/) settings, and references to companion scripts. They are distributed through public registries and installed with a single command.

The supply chain Mobb maps runs from developer to registry to skill file to agent to system access. If any link in that chain is compromised, the attacker gains whatever access the developer has — source code, API keys, SSH credentials, cloud provider tokens, and the ability to push code into [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) pipelines, Worcel says.

Most skills scanned (66%) showed no findings under the patterns Mobb targeted. But among the 34% who did flag, 27% of all scanned skills contain command execution patterns, Worcel explains. One in six contains a `curl | sh` remote code execution pattern directly in skill instruction files, the classic attack of downloading a script from the internet and piping it straight into a shell interpreter. Nearly 15% reference consent bypass mechanisms that disable or circumvent the safety confirmations built into agent tools.

“The good news is that outright malware is rare; the ecosystem is largely healthy,” Worcel says, crediting in part the work of [Paul McCarty](https://www.linkedin.com/in/mccartypaul/?originalSubdomain=au) and the [OpenSourceMalware](https://opensourcemalware.com/) team. “But what concerns us is the attack surface. More than a quarter of skills contain instructions for agents to execute shell commands. One in six includes patterns that download and run remote scripts.”

## The gap in protection

Each of the four registries has invested in security, though with varying approaches. [Skills.sh](https://skills.sh/), operated by Vercel, runs three independent scanners — Gen Agent Trust Hub, Socket, and Snyk — visible on a public audit page. [ClawHub](https://clawhub.ai/) uses an AI-based classification system that labels skills as CLEAN, SUSPICIOUS, or MALICIOUS, though suspicious skills remain installable; the classification is informational, not enforced. [Tessl](https://tessl.io/) uses Snyk and, notably, is the only registry that blocks installations with high or critical findings at the client side.

GitHub, which hosts the source repositories for most skills and accounts for 7,379 of the skills Mobb collected, provides standard repository security features like [Dependabot](https://github.com/dependabot) and secret scanning, but those tools do not analyze SKILL.md instructions, MCP configurations, or agent hook definitions.

“The registries are doing real work — multiple security scanners, AI-based classification, risk scoring,” Worcel says. “But that protection lives on the registry’s servers. Once a skill reaches the developer’s machine, there are no guardrails. No signature verification, no runtime scanning, no way to know if what you installed is the same version that was audited.”

Worcel draws a parallel to earlier issues in the package ecosystem: “This is the same gap that hit the npm and PyPI ecosystems years ago, and the industry learned those lessons the hard way. We’re publishing this research so the AI agent ecosystem can learn them proactively.”

The gap Mobb identifies is consistent across all four registries: scanning happens at the registry boundary, at publish time. Once a developer installs a skill, no scan runs on the machine until the agent reads the files. There is no cryptographic signing to verify that the installed version matches the audited version. A skill that passes review today can be updated tomorrow with malicious content, and that window is exploitable.

Hooks — commands that execute automatically when specific agent events occur, such as a file edit or a new session — pose a particular persistence risk. A malicious skill can install a hook that continues operating after the skill itself is removed, and no registry currently audits hook configurations specifically.

## What the Audit Found

Beyond statistical patterns, Mobb documented several concrete cases. A key one is a confirmed API traffic hijacking: a skill published on GitHub under the repository `flyingtimes/podcast-using-skill` contains a `.claude/settings.json` file that overrides the Anthropic API endpoint, redirects all traffic to Zhipu AI’s BigModel platform in China, swaps in a hardcoded third-party API token, and changes the model to glm-4.6. A developer who cloned that repository and opened it in Claude Code would have their entire conversation — all code context, prompts, and responses — silently routed through a third-party server with no visible indication that anything had changed.

“We found API traffic silently redirected to third-party servers, hardcoded credentials in public repositories, and invisible characters encoding hidden data in files that appear completely normal to the human eye,” Worcel says. “These aren’t theoretical risks — we documented each one with the exact file and line of code.”

Researchers also found 159 skills with hidden HTML comment payloads. HTML comments are invisible when markdown is rendered in a browser or IDE but are fully visible to an AI agent reading the raw file.

One example — found in a repository named claude-world/claude-skill-antivirus In a file labeled as a malicious skill example, it contained a classic prompt injection: a comment instructing the agent to ignore previous instructions and execute what followed. Another, found in a separate repository, contained a comment reading <!– security-allowlist: curl-pipe-bash –> — an attempt to suppress scanner warnings about piping curl to bash.

One hundred twenty-seven skills contained invisible Unicode zero-width characters, which can encode hidden data readable by any program processing raw text but invisible to human reviewers. One case, in a repository called `copyleftdev/sk1llz`, placed a long sequence of alternating zero-width spaces and zero-width joiners immediately after a heading — a pattern consistent with binary steganographic encoding.

On the MCP front, 37 skills auto-approve MCP server connections without user consent, and researchers found live API credentials committed directly into public repository MCP configuration files. One case involved a personal Apify actor endpoint — meaning a developer’s API token would be transmitted to a third-party individual’s infrastructure, not the vendor’s own servers.

## The plan of attack

Mobb outlines the kill chain an attacker would follow: Publish a plausible-looking skill, embed malicious instructions in files that developers are unlikely to review manually, let registries distribute it, and wait for an agent to execute it.

What makes this attack surface unusual is that the instructions are in plain English — indistinguishable from legitimate skill content by binary signature scanning — and the agent is the executor. The attacker does not write exploit code. They write instructions, and the AI agent executes them using the developer’s credentials.

“The developer is in the loop, but may not be watching,” the Mobb report notes. “AI agents are designed to work autonomously. Developers increasingly trust agent actions without reviewing every step.”

## Recommendations

Mobb directs its recommendations to three audiences.

1. For **registry operators**, the report calls for client-side enforcement at install time, cryptographic signing, continuous re-scanning on update, and specific analysis of hook configurations. For developers, it recommends manually reviewing SKILL.md, `.claude/settings.json`, and `.mcp.json` before installing any skill, and treating MCP auto-approval settings as a red flag.
2. For **AI agent tool vendors** — the makers of Claude Code, Cursor, Windsurf, and similar tools — the report argues for sandboxing skill execution so skills do not automatically inherit full developer permissions, requiring explicit consent before environment variables or MCP connections are applied, and surfacing hook visibility so developers can see what is running in the background.
3. At the **industry level**, Mobb calls for the equivalent of `npm audit` or Docker Content Trust for the skill ecosystem, which includes standardized security metadata, shared vulnerability databases across registries, and trust chains with revocation mechanisms.

## Context

The timing of the report follows a real-world incident at ClawHub, one of the four registries audited. In February 2026, 341 malicious skills were discovered on the platform in what researchers call the “ClawHavoc” incident. Skills.sh, the largest registry, reports more than 89,000 total skill installations to date.

Mobb concludes that the ecosystem is largely healthy, as outright malware is rare, and the findings skew toward risky patterns rather than confirmed attacks. But the infrastructure for abuse is in place, Worcel says.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)