The fastest-moving conversation in AI developer tooling this week began with a job description.

[Boris Cherny](https://www.linkedin.com/in/bcherny/), head of [Claude Code](https://www.anthropic.com/claude-code) at Anthropic, [said](https://x.com/rohanpaul_ai/status/2063289804708835412) he no longer prompts Claude directly and that “my job is to write loops.” Peter Steinberger [urged](https://x.com/steipete/status/2063697162748260627) developers to design the loops that prompt their agents, and Sunday, Google engineer Addy Osmani [published](https://addyosmani.com/blog/loop-engineering/) a post that gave the pattern a name: **loop engineering**.

The name matters less than what it exposes. Coding agents are evolving from interactive assistants into long-running execution systems, and OpenAI and Anthropic have spent months shipping the six building blocks of a loop.

## From operating the machine to designing the line

Osmani defines loop engineering as “replacing yourself as the person who prompts the agent.” At its core, it is an orchestration pattern that combines scheduled execution, isolated workspaces, verifier agents, and persistent memory to transform a coding agent into an autonomous software worker. For two years, working with a coding agent meant typing one prompt after another, with the human as both scheduler and quality gate.

> At its core, loop engineering is an orchestration pattern that combines scheduled execution, isolated workspaces, verifier agents, and persistent memory to transform a coding agent into an autonomous software worker.

A loop inverts that arrangement, and the closest parallel is moving from operating a lathe to designing the production line the lathe sits on. The loop discovers work on a schedule, verifies the result with a second agent, and writes its state to a file so that tomorrow’s run resumes where today’s left off. It sits one level above Osmani’s earlier [harness engineering](https://addyosmani.com/blog/agent-harness-engineering/) pattern.

## The same building blocks in both products

Loop engineering has moved from an informal pattern to a named practice because the building blocks now ship inside the products rather than in custom scripts.

Osmani maps six primitives to both Claude Code and Codex, and the mappings are almost identical:

| Primitive | Job in the loop | Codex | Claude Code |
| --- | --- | --- | --- |
| Automations | Scheduled discovery and triage | Automations tab with a triage inbox | Scheduled tasks, `/loop`, hooks, GitHub Actions |
| Worktrees | Isolate parallel agents | Built-in worktree per thread | `git worktree`, worktree isolation for subagents |
| Skills | Codify project knowledge | `SKILL.md` agent skills | `SKILL.md` agent skills |
| Connectors | Reach external tools | MCP connectors and plugins | MCP servers and plugins |
| Sub-agents | Separate the maker from the checker | Subagents defined in `.codex/agents/` | Subagents in `.claude/agents/`, agent teams |
| Memory | Persist state between runs | `AGENTS.md`, the Memories feature, or Linear via a connector | `CLAUDE.md`, auto memory, or Linear via MCP |

Both products expose a `/goal` command that keeps an agent working until a verifiable stopping condition holds, with Claude Code using a separate model to grade the result. With [Automations](https://developers.openai.com/codex/app/automations), OpenAI is enabling Codex users to run scheduled discovery as a first-class surface. Anthropic [launched](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/) routines for Claude Code in April, and the dynamic workflows

*The New Stack* [tested](https://thenewstack.io/claude-code-dynamic-workflows-test/) dynamic workflows by letting Claude write its own orchestration scripts and run parallel subagents. With these primitives, developers can convert recurring maintenance into scheduled autonomous workflows, and teams can run agents in parallel through isolated worktrees without corrupting the main branch. The viral moment came when the people who built the tools pointed out that the assembly was complete.

## The verifier is the part that earns trust

The most consequential design choice in a loop is splitting the agent that writes the code from the agent that checks it. A model grading its own output is too generous, so a second agent with different instructions catches the failures the first reasoned itself into, a separation Anthropic [described](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) in its harness work for long-running agents.

In Osmani’s example, a morning automation triages the previous day’s CI failures and sends one sub-agent to draft each fix in an isolated worktree while a second reviews it against the project’s tests. Ramp’s [Inspect](https://thenewstack.io/ramps-inspect-shows-closed-loop-ai-agents-are-softwares-future/) built this shape as bespoke infrastructure six months ago, and its arrival as a first-party feature in both ecosystems shows that closed-loop operation is becoming the default.

## Cost, correctness and comprehension debt

Developers went from prompt engineering to context engineering to harness engineering to loop engineering in fewer than 18 months, and the scheduling layer of a 2026 loop is a traditional scheduler such as cron. The decision logic in the middle separates the two: a cron job runs a fixed script, while a loop runs a model that reads the current state and chooses its next action.

Osmani is more cautious than the discussion he triggered, warning that token costs vary wildly and that a loop running unattended is also a loop making mistakes unattended. His sharpest warning concerns comprehension debt, the gap that widens when a system ships code you never read. Two engineers can run an identical loop and get opposite outcomes, one moving faster on work they understand, the other avoiding understanding altogether.

## The road ahead

Developers can start with a single scheduled triage automation and a verifier sub-agent, capturing most of the value at a fraction of the token spend. Cursor, Google’s [Antigravity](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/), and GitHub’s new [Copilot app](https://thenewstack.io/github-copilot-desktop-app/) all orchestrate agents, and none has yet named a loop as its unit of work.

The key difference among these platforms lies in the shift from the model to the loop around it, since scheduling, verification, and memory now determine what ships. Loop engineering is all set to become the orchestration layer for AI-assisted software development, and the vendor that makes loop definitions portable will take pole position.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)