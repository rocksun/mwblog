The AI coding tool market was supposed to consolidate. One winner would emerge, developers would standardize around it, and the industry would move forward. Instead, the opposite happened. In the first week of April 2026, [Cursor shipped a rebuilt interface](https://thenewstack.io/cursor-3-demotes-ide/) for orchestrating parallel agents, OpenAI published an official plugin that runs inside Anthropic’s Claude Code, and early adopters started running all three together. Not as competitors. As layers in a stack that nobody designed but that is assembling itself anyway.

The pattern mirrors something developers already know from infrastructure. Nobody runs a single observability tool. You run Prometheus for metrics, Grafana for dashboards, and PagerDuty for alerts. Each tool does one thing well, and the value comes from how they compose. AI coding tools are following the same path, splitting into specialized layers rather than collapsing into a single product.

## Three launches, one week, one pattern

On April 2, Cursor launched version 3, codenamed Glass. The release replaced Cursor’s Composer pane with a dedicated Agents Window, a standalone interface built from scratch around managing multiple AI agents simultaneously. Developers can now run parallel agents across local machines, worktrees, and cloud sandboxes from a single sidebar. According to Cursor’s [changelog](https://cursor.com/changelog/3-0), the release also added Agent Tabs for viewing multiple conversations side by side, a `/best-of-n` command that sends the same prompt to multiple models in isolated worktrees for comparison, and Design Mode for annotating UI elements in a built-in browser. Sessions can be handed off from local to cloud to keep running overnight, then pulled back for local iteration in the morning.

Three days earlier, OpenAI [published](https://github.com/openai/codex-plugin-cc) `codex-plugin-cc` on GitHub. The plugin installs directly inside Claude Code, Anthropic’s terminal-based coding agent. It provides six slash commands. `/codex:review` runs a standard code review. `/codex:adversarial-review` pressure-tests implementation decisions around auth, data loss, and race conditions. `/codex:rescue` hands a task to Codex entirely, spinning it up as a subagent that can investigate bugs or take a second pass at a problem. An optional review gate feature lets Codex automatically review Claude’s output before it finalizes, blocking completion if issues are found.

This is OpenAI shipping an official integration into a direct competitor’s product. The Apache 2.0-licensed plugin delegates through the local Codex CLI, so it uses the developer’s existing authentication and configuration. No new runtime. No walled garden. Just Codex, invoked from inside Claude Code.

The structural insight is not that these tools launched in the same week. It is that they launched in a way that makes them composable. Cursor orchestrates agents that can use any model. Claude Code accepts plugins from rival providers. Codex runs as a subagent inside another company’s terminal. The tools are not converging. They are layering.

## A stack taking shape

What some early adopters are assembling looks less like a product choice and more like a toolchain. Three layers are forming, each with a different job.

![](https://cdn.thenewstack.io/media/2026/04/bb268e25-coding-agent-stack-1-1024x697.png)

### The orchestration layer

Cursor 3 sits here. Its Agents Window is not an editor with AI bolted on. It is a control plane for managing fleets of coding agents. The interface shows all active agents in a sidebar, whether they were kicked off from the desktop, mobile, Slack, GitHub, or Linear. Agent Tabs let developers view multiple conversations side by side in a grid. Design Mode lets them annotate UI elements in a built-in browser and point agents at specific interface problems.

The move away from VS Code is deliberate. Cursor forked VS Code in 2023 to get distribution. Now it is building away from VS Code to get differentiation. If the orchestration layer wins, the text editor becomes secondary. Cursor is betting that managing agents matters more than editing files.

Google reached a similar conclusion. [Antigravity](https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/), announced in November 2025, grew out of Google’s $2.4 billion licensing deal with Windsurf. Reuters [reported](https://www.cnbc.com/2025/07/11/google-windsurf-ceo-varun-mohan-latest-ai-talent-deal-.html) that Google paid licensing fees and hired key staff rather than acquiring the company outright. The result splits its interface into an Editor View for hands-on coding and a Manager Surface for spawning and observing multiple agents across workspaces. Two companies, two architectures, one conclusion. Developers need a surface for managing agents, not just writing code.

### The execution layer

Claude Code and OpenAI Codex live here. These are the agents that actually write, review, and debug code. They operate in terminals, cloud sandboxes, or both. They read entire codebases, run tests, commit changes, and manage pull requests.

Claude Code has emerged as the strongest contender at this layer, at least in terms of developer enthusiasm. A [survey](https://newsletter.pragmaticengineer.com/p/ai-tooling-2026) by the Pragmatic Engineer of 906 software engineers in February 2026 found it was the most-used AI coding tool with a 46% “most loved” rating. SemiAnalysis [estimates](https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point) it accounts for roughly 4% of all public GitHub commits (as of March 2026), with projections suggesting 20% by year-end. Analyst estimates from secondary reporting place Claude Code’s annualized revenue at over $2.5 billion by March 2026, though Anthropic has not confirmed that figure in an official filing. Codex recently [surpassed](https://openai.com/index/accelerating-the-next-phase-ai/) 3 million weekly active users, up from 2 million just a month earlier. Its cloud sandbox model is designed for asynchronous, long-running tasks that can proceed without developer attention.

> When you ask the same model that wrote your code to review it, you are asking someone to grade their own homework.

The execution layer is where model differences matter most. Practitioners generally report that Claude performs better on nuanced reasoning across long context windows, while Codex handles parallelizable throughput tasks more efficiently. No neutral benchmark has confirmed that division cleanly, but the perception is widespread enough to drive adoption of multi-tools. Neither dominates across every scenario, which is precisely why developers are reaching for both.

### The review layer

This is the newest layer and the one the Codex plugin specifically enables. When Claude writes code and Codex reviews it, the reviewer was not involved in writing. It does not share the same internal assumptions. It catches different classes of errors. The adversarial review command goes further by pressure-testing around auth, data loss, rollbacks, and race conditions.

Cross-provider review addresses what single-model workflows cannot. When you ask the same model that wrote your code to review it, you are asking someone to grade their own homework. The structural bias is unavoidable. A second model from a different provider, trained on different data with different optimization targets, applies genuinely independent scrutiny.

The review gate feature makes this automatic. Enable it, and Codex reviews every Claude output before it finalizes. If issues surface, Claude addresses them before proceeding. OpenAI’s documentation warns that this can create long-running loops and quickly drain usage limits, underscoring just how seriously the company expects developers to use it.

## Why interoperability, not lock-in

OpenAI building a plugin for Anthropic’s product is the most revealing strategic signal here. The conventional playbook says lock users in. Build a walled garden. Make switching costly. OpenAI is doing the opposite, and the economics explain why.

> OpenAI building a plugin for Anthropic’s product is the most revealing strategic signal here. The conventional playbook says lock users in. Build a walled garden. Make switching costly. OpenAI is doing the opposite.

Claude Code has built a large and enthusiastic installed base among professional developers. Rather than waiting for those developers to switch, OpenAI [embedded](https://techstrong.ai/features/openai-challenges-claude-code-with-cross-platform-codex-plugin-push/) Codex where they already work. Every plugin-initiated review generates usage that counts against the developer’s ChatGPT subscription or API key. Zero acquisition cost, incremental billing.

Anthropic’s open plugin architecture made this possible. Claude Code’s MCP-based plugin system is designed to support third-party integrations, including those from competitors. The platform-versus-app dynamic that usually creates tension between companies is being replaced by a composability dynamic where both sides benefit. Anthropic gets a richer plugin ecosystem. OpenAI gets distribution inside a competitor’s installed base.

This is not altruism. It is pragmatism. Both companies recognized that developers will use multiple tools regardless. The question is whether your tool is in the stack or outside it.

## What this means for developers

If this composable pattern holds, it changes three things about how developers work.

### Model choice becomes infrastructure

Cursor 3’s `/best-of-n` command sends the same task to multiple models in isolated worktrees and compares outcomes. This treats model selection the way developers already treat database selection or cloud provider selection. It is an infrastructure decision driven by workload characteristics, not brand loyalty. Claude for precision on complex refactorings. Codex for throughput on parallelizable tasks. Composer 2, Cursor’s own model built on open-source Kimi K2.5, for cost-sensitive batch work.

### The editor starts to recede

For 40 years, the code editor was the center of gravity in software development. From Emacs to VS Code, the assumption was always the same. The developer writes code, and tools help. Cursor 3’s Agents Window and Antigravity’s Manager Surface both directly challenge that assumption. The orchestration layer is beginning to compete with the editor as the primary interface. The editor is still there, still useful, but it is no longer guaranteed to be the default view.

### Review moves toward adversarial

Single-model review was always structurally limited. Cross-provider review, where one model writes and another model challenges, is the most promising mitigation strategy yet for the sycophancy problem in AI-assisted development. As this pattern matures, it could become a standard step in CI/CD pipelines, not just a developer workflow choice.

## What’s next

A coding agent stack is taking shape faster than most expected. Cursor is staking a claim on the orchestration layer. Claude Code and Codex are competing and collaborating at the execution layer. Cross-provider review is opening up a verification layer that did not exist six months ago. For developers keeping up with the tool landscape, the familiar infrastructure patterns apply. Just as you learned to compose Terraform, Docker, and Kubernetes rather than picking one tool for everything, the emerging pattern in AI coding is composition over consolidation.

The unanswered question is whether this stack stabilizes or continues to fracture. GitHub Copilot is evolving its own agent capabilities. AWS Kiro shipped an agent-first IDE. Every major cloud provider now has a position in this market. The next phase will be determined by which layers become commodities and which become the new control points. Stay tuned.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)