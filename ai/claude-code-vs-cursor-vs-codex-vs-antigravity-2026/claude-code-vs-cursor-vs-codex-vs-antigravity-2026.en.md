**Six months ago, the agentic coding tool was still an argument about form**. By the start of June 2026, the argument is mostly over.

The four products that have come to define the category this year have spent the past several months quietly agreeing on what one of these things should be.

The clock starts in November. Google shipped [Antigravity](https://antigravity.google/blog/introducing-google-antigravity-2-0) in public preview on November 18, 2025, the same day Gemini 3 [arrived](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/), and that release pushed the agent-first coding surface into the mainstream. Anthropic’s [Claude Code](https://claude.com/product/claude-code), OpenAI’s Codex and Anysphere’s Cursor were already in the field.

Watching all four grow up over the same half-year tells you more than any single launch, because the interesting part came after the announcements. Think of it as the smartphone settling into a glass slab: Once everyone accepted the shape, the contest moved to the platform around it.

**Claude Code** stayed close to where it started, living in the terminal and leaning on Anthropic’s long-context reasoning, compaction, and an approval-heavy flow, which makes it strong on large-codebase work where an agent has to hold a lot in its head before touching a line. Developers who want to read every change before it lands gravitate here, and the friction is deliberate, since on a serious codebase the riskiest moment is the one just before a command runs or a file changes, and Claude Code puts a human at exactly that point.

**Cursor** went the other way and stayed model-agnostic. It runs inside a familiar VS Code surface and lets you point [Cursor](https://cursor.com) at whichever frontier model you already pay for, so a team is not tied to one vendor’s release calendar. The deeper advantage is that it asks for no workflow migration, letting developers add agency without leaving the files, tabs, diffs, and shortcuts they navigate by reflex, while the Composer agent now handles multi-file work without pulling them out of the editor.

**Codex** took the distribution route. Because [Codex](https://openai.com/codex) is packaged into ChatGPT plans for most users rather than carrying a price tag of its own, it reached scale faster than anything else in the category, even as heavier and business usage is now governed by Codex-specific limits and credits. OpenAI [reported](https://thenewstack.io/openai-codex-chatgpt-mobile/) more than 3 million weekly developers in mid-April 2026 and more than 4 million by late May, with the real money coming from enterprise rollouts within ChatGPT Business and Enterprise.

**Antigravity** traveled the furthest distance from where it began. It launched as an AI-native IDE built on a fork of VS Code, then [relaunched](https://antigravity.google/blog/introducing-google-antigravity-2-0) at Google I/O on May 19, 2026 as Antigravity 2.0, a five-surface platform spanning a standalone desktop app, a CLI, an SDK, a Managed Agents API inside the Gemini API, and an enterprise layer for Google Cloud customers.

> Think of it as the smartphone settling into a glass slab: Once everyone accepted the shape, the contest moved to the platform around it.

The rebuild was not gentle, [removing the original IDE as the default](https://thenewstack.io/ide-vs-desktop-agent/) and breaking setups overnight, after an earlier round of anger in March 2026 when Google shifted to a credit-pack model and tightened quotas. Read against Google’s other moves, the real bet is a route from a local coding agent to a managed agent runtime on Google Cloud, the same harness running in the desktop client, the CLI, the Gemini API and the enterprise platform.

## Where’s GitHub Copilot?

One name is deliberately missing from those four. GitHub [Copilot](https://github.com/features/copilot) shaped the whole category, and its coding agent now plans work, edits a branch and opens a pull request with enterprise controls attached. I kept the focus on the products that drove the agent-first conversation this year, but Copilot earns watching because GitHub already owns the place where issues, pull requests, reviews and Actions live, a home-field edge as agent-written work flows to where it gets merged.

## The blueprint they all landed on

Line the four up today, and the resemblances are hard to miss. They are converging on the same pattern: a terminal or command-line surface, explicit planning before execution, approval gates, access to external tools through the Model Context Protocol, and some form of delegated or parallel agent work. Four labs with very different cultures arrived at almost the same blueprint inside six months, which usually signals the design was less a choice than a discovery.

> Four labs with very different cultures arrived at almost the same blueprint inside six months, which usually signals the design was less a choice than a discovery.

Ask any of them to fix a failing integration test across three files and the flow looks much the same, where the agent reads the repo, proposes a plan, waits for approval, edits, runs the test, and reports back while you watch the diffs stream past. That sameness has quietly changed what one of these tools is: a coding agent now reads issues, edits branches, runs tests, calls tools, and opens pull requests, behaving like a junior teammate with commit access rather than an autocomplete.

The connector everyone points to is MCP, but the quieter standard forming inside the repository may matter more. The [`AGENTS.md`](https://agents.md) convention turns the repo itself into the agent’s onboarding guide, holding how to run tests, what style to follow, and where not to touch, and Codex, Cursor, Copilot, and Windsurf all read it natively.

OpenAI started it; Google, Cursor, and Sourcegraph joined; and since December 2025, it has sat under the Agentic AI Foundation at the Linux Foundation alongside MCP. Convergence here stops short of total, because Claude Code still reads its own `CLAUDE.md`, yet the direction points to a single instruction file that spans tools and makes an agent’s behavior portable.

What this convergence quietly did was demote the model. For most of 2025, the pitch was about whose model wrote better code. On SWE-bench Verified, the leading scores now sit within a narrow band of each other as of mid-May 2026, and Cursor will happily run any of them.

When the engine stops separating products, the difference moves to everything around it: the harness, the workflow, the approval model, and the distribution channel, and I’d argue that is the most important shift of the last six months, the reason a team’s choice now turns on fit rather than which leaderboard a model topped last week.

Benchmarks still measure whether an agent can solve an isolated task, but in real repositories the hard part is landing a change that survives local conventions, CI, and a human reviewer, so teams are starting to route work by type rather than swear loyalty to one tool.

Lock-in builds in that same layer. A team that wires its review habits, skills, hooks, and subagent patterns around one tool does not switch lightly, and Antigravity’s painful CLI migration showed how much friction there is once a workflow is in place.

## The money question splits them apart

Pricing is where the four stop rhyming, and the first thing to grasp is that an agent bills less like a seat than like a compute job, because it reads large repos, spins up sandboxes, runs tests, and loops through retries before it lands a mergeable change. The number worth comparing is the cost per accepted change, rather than the monthly sticker price, since cheap-at-the-door rarely results in cheap-at-scale once a team runs agents all day.

> An agent bills less like a seat than like a compute job… The number worth comparing is the cost per accepted change, rather than the monthly sticker price.

Codex is the outlier because it has no line item of its own and rides on top of ChatGPT plans, which drove its rapid growth, though heavier work is metered through Codex-specific credits. Cursor Pro and Claude Code’s entry tier both sit around the $20 mark as of June 2026, with usage-based costs layered on top, while Anthropic’s Max plans run well above that for power users.

Antigravity still carries preview-style access, but Google’s quota and plan changes, including a new $100 per month AI Ultra tier announced around I/O, already show how unstable free becomes once agent workloads get expensive.

| Tool | Center of gravity | Where it tends to pull ahead |
| --- | --- | --- |
| Claude Code | Terminal-native, approval-first | Deep reasoning and large-codebase work, for teams that want to read every diff |
| Cursor | Model-agnostic IDE | Editor-bound teams that want to choose their own model and avoid vendor lock-in |
| Codex | Bundled into ChatGPT | Fast reach and enterprise rollout, helped by no separate price tag |
| Antigravity | Multi-surface platform | Google Cloud and Android shops wanting managed agents, with preview risk attached |

No team should read that table as a verdict. Most shops I talk to run two of these side by side, one in the terminal for serious refactors and one in the editor for everyday edits. The trap is that all four look almost identical in a demo, and the differences that bite show up later, in where the code runs, what the agent may touch, and what it costs over a week of real work. That layer is worth poking at before committing, far more than the SWE-bench number on the launch slide.

## The next entrant is already here

The framing that Grok Build is something to watch for in the coming weeks needs a small correction, because xAI has already moved. It arrived in early beta in mid-May 2026 for the highest SuperGrok tier, and xAI [published](https://x.ai/news/grok-build-cli) its Grok Build announcement on May 25, opening access to all SuperGrok and X Premium Plus subscribers.

The tool is a terminal-native CLI backed by the grok-build-0.1A model, which xAI says it trained specifically for agentic coding, with a reported score of around 70.8 percent on SWE-bench, verified in early third-party writeups.

Two design choices stand out. Grok Build runs up to eight subagents in parallel, each isolated in its own Git worktree, the boldest architecture bet anyone in the category has made. xAI also calls it local-first, with source code and credentials staying on the machine rather than going to xAI’s servers during a session, which appeals to teams in regulated work, though its compliance paperwork is still thinner than the marketing.

> Six months of convergence has settled the shape of the agentic coding tool and turned the next phase into a contest over the harness, the price, and the habits a team builds around one product.

Local execution is not local inference, so what actually matters is which repository context is still used to reach the model. The piece still missing is Arena Mode, which would generate several candidate outputs and let you pick the best, and which has appeared in code traces but is not yet live in the beta.

The launch has happened, so the real test over the coming weeks is retention, namely whether Grok Build keeps developers in the terminal past the first week, whether Arena Mode ships and narrows the benchmark gap in practice, and whether the aggressive pricing pulls paying testers off the incumbents.

Six months of convergence has settled the shape of the agentic coding tool and turned the next phase into a contest over the harness, the price, and the habits a team builds around one product. A fifth terminal agent has now entered that contest with a large captive base inside X Premium Plus and an owner willing to spend, reason enough to watch how the incumbents answer.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)