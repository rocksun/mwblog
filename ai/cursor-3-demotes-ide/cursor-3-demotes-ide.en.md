Last week, the AI code editor with the fastest revenue growth in the category shipped a product that is *not* a code editor.

[Cursor 3](https://cursor.com/blog/cursor-3), built from scratch under the codename Glass, makes an agent management console the primary interface and pushes the traditional IDE to a secondary surface. Engineers can still write code in it. But the product’s design assumes they will spend most of their time dispatching agents, reviewing output, and deciding which ships. The prompt box sits where the file tree used to be.

![](https://cdn.thenewstack.io/media/2026/04/dd333462-cursor-3-1024x538.png)

For a few months now, [coding tools have become second-class citizens to AI models](https://thenewstack.io/ide-vs-desktop-agent/). Cursor 3 is what happens when a company generating $2 billion in annualized revenue agrees with that thesis and bets its entire product surface on it. The shift mirrors a transition that infrastructure engineers have already lived through.

Cloud dashboards replaced SSH terminals. Kubernetes controllers replaced manual server provisioning. Now the orchestration layer is replacing the code editor as the primary surface. The pattern is the same, but the stakes are higher, because this time the abstraction being demoted is the one developers have used for 40 years.

## What Cursor 3 ships

Cursor started in 2022 as a fork of VS Code. That fork now has a sibling built from scratch around agents. Cursor says the new interface was built “from scratch, centered around agents,” and it treats the traditional IDE as a fallback you can switch to at any time.

The workspace is multi-repo by default. Agents and humans operate across different repositories simultaneously, with every local and cloud agent visible in a unified sidebar. That sidebar pulls agents from every surface Cursor touches, including sessions kicked off from mobile, the web client, Slack, GitHub, and Linear. Cloud agents generate demos and screenshots of their work, so an engineer reviewing output doesn’t need to pull code locally to understand what changed.

The standout feature is Cloud Handoff. You can move a running agent session from your laptop to Cursor’s cloud mid-task, let it keep working while you close your machine, and pull it back to local when you’re ready to make edits and test on your desktop. The reverse also works. Start something in the cloud and bring it down when you want full control. That kind of session portability between local and cloud environments has been a gap in most competing tools.

Think of this as the shift from managing individual servers to managing a fleet through a control plane. You can still SSH into a server when you need to. But the control plane is where decisions are made, where workloads are assigned, and where you see the state of the system. Cursor 3 treats agents the same way. The IDE is SSH. Glass is the control plane.

## The pressure behind the pivot

The timing of Cursor 3 is not accidental. Cursor spent the last six weeks in what I’d describe as an accelerated product offensive. A *Fortune* [feature](https://fortune.com/2026/03/21/cursor-ceo-michael-truell-ai-coding-claude-anthropic-venture-capital/) published in late March framed the company’s situation as a textbook case of the innovator’s dilemma, and the reporting landed hard. Cursor’s annualized revenue run rate [crossed](https://www.bloomberg.com/news/articles/2026-03-02/cursor-recurring-revenue-doubles-in-three-months-to-2-billion) $2 billion in February 2026, doubling in three months, according to Bloomberg.

But Claude Code, Anthropic’s terminal-first coding agent launched barely a year ago, had reached a $2.5 billion run rate with over 300,000 business customers, according to Fortune’s reporting. Developers were publicly posting about leaving Cursor for Claude Code, and one Cursor investor told Fortune that several startups in his portfolio were decoupling from it. Reports surfaced in March that Cursor was seeking a new funding round at a valuation of roughly $50 billion, even as the narrative around its momentum was fracturing.

Cursor responded with three major moves in rapid succession. On March 5, the company [launched](https://techcrunch.com/2026/03/05/cursor-is-rolling-out-a-new-system-for-agentic-coding/) Automations, a system for triggering agents in response to GitHub events, Slack messages, and timers without human intervention.

On March 19, Cursor shipped Composer 2, its first in-house coding model built on the open-source Kimi K2.5 from Moonshot AI. Cursor claims Composer 2 scored 61.3 on its proprietary CursorBench, ahead of Claude Opus 4.6 at 58.2, at substantially lower token cost. Those benchmark numbers deserve a caveat, since CursorBench is Cursor’s own evaluation suite. Also in March, Cursor [enabled](https://thenewstack.io/cursor-self-hosted-coding-agents/) self-hosted cloud agents, allowing Fortune 500 companies to run Cursor’s agents on their own infrastructure.

Then came Cursor 3. Three product launches and a full interface rebuild in a single month. That’s the kind of cadence you see from a company that believes its category is being redefined around it.

## The structural shift

Cursor’s pivot matters because it reveals a pattern that extends far beyond one company. Every major player in AI-assisted development now agrees that agents need a dedicated orchestration surface. What they disagree on is where that surface should live. That disagreement is the most interesting architectural divergence in developer tooling right now.

Anthropic went terminal-first with Claude Code. No IDE at all. The CLI is the orchestration layer, and developers work through natural-language commands in their shells. Anthropic later added a browser-based interface at claude.ai/code and a desktop app, but the terminal remains the center of gravity. The orchestration layer lives entirely outside the editor.

OpenAI took a different path. [Codex](https://openai.com/index/introducing-the-codex-app/) now spans a standalone desktop app, a CLI, an IDE extension for VS Code and its forks, and a cloud interface at chatgpt.com/codex. The desktop app is the “command center” for managing parallel agents, reviewing diffs, and running work across projects. OpenAI’s bet is that the orchestration layer should be everywhere, available from any surface a developer happens to be using.

> “The code editor defined how software got built for four decades. Cursor 3 is a bet that supervising agents will matter more than editing files.”

Google landed closest to Cursor’s approach. After paying $2.4 billion in [licensing fees](https://www.cnbc.com/2025/07/11/google-windsurf-ceo-varun-mohan-latest-ai-talent-deal-.html) to Windsurf and hiring its CEO and key engineers into DeepMind, Google shipped [Antigravity](https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/), an agent-first IDE with two distinct modes. The Editor View gives you a traditional coding environment. The Manager Surface lets you spawn, orchestrate, and observe multiple agents working across workspaces in parallel. Agent orchestration and code editing live in the same application, but in separate views.

Cursor 3 follows this same inside-the-IDE pattern but pushes the ratio further. Glass makes the agent console the default view and the editor the fallback. Google’s Antigravity treats both views as coequal. That difference in emphasis matters because it signals where Cursor thinks the developer’s time will actually go.

The analogy to cloud infrastructure helps clarify the divergence. When AWS launched its management console, nobody stopped using SSH. But SSH stopped being the place where infrastructure decisions were made. The console became the control plane, and SSH became a debugging tool you reached for occasionally.

Anthropic and OpenAI are betting that the orchestration layer can succeed as a standalone application, separate from the IDE. Cursor and Google are betting that it needs to live alongside the editor, because developers will still want to drop into code when the agent gets something wrong. The industry agrees that agent orchestration is the new primary surface. It has not yet been agreed on the architecture.

## What this means for developers

The practical implications are split into three areas that matter right now.

### 1. Model choice becomes infrastructure

Cursor ships Composer 2 as the default model but still lets developers switch to Claude, GPT-5.4, and Gemini per conversation. The model powering your agents is now an infrastructure decision, similar to choosing a database or a cloud region. Token economics compound at scale. Cursor’s published pricing for Composer 2 standard is $0.50 per million input tokens and $2.50 per million output tokens (as of March 2026), substantially below the frontier model pricing from Anthropic and OpenAI. For teams running dozens of parallel agents, that math drives tool selection more than feature comparisons or UI preferences.

### 2. The VS Code moat dries up

Cursor forked VS Code to inherit its extension ecosystem and get immediate distribution. With Cursor 3, the company is building away from that foundation to create differentiation. If the agent-first interface wins, VS Code extensions become less relevant. Microsoft should be paying close attention. The assumption that VS Code is the center of gravity for developer tooling, an assumption that has held for nearly a decade, is weakening. JetBrains faces the same pressure. When the primary interaction surface shifts from editing files to managing agents, the traditional IDE’s competitive advantages in code intelligence and refactoring tools matter less.

### 3. Your workflow changes before your job title does

Engineers using Cursor 3 spend their time reviewing diffs generated by agents, verifying screenshots of what cloud agents produced, deciding which tasks to push to the cloud and which to keep local, and managing PR workflows. That’s a different skill set than writing code. It looks more like the work of an engineering manager or a platform operator than a traditional software developer. The role of a software engineer is converging with that of a systems operator who works at the application layer.

> “The role of a software engineer is converging with the role of a systems operator who happens to work at the application layer.”

Cursor’s own trajectory illustrates the shift. The company [acquired](https://fortune.com/2025/12/19/cursor-ai-coding-startup-graphite-competition-heats-up/) code review platform Graphite in December 2025 because, as CEO Michael Truell put it, reviewing code was becoming the bottleneck as AI accelerated writing it. Cursor 3 takes that logic further. If agents write the code and Graphite reviews it, the engineer’s job is to orchestrate both. The IDE becomes secondary.

## What’s next

The orchestration layer for AI coding agents is now a product category. Every major player has shipped one. The open question is architectural. Does the orchestration layer live inside the IDE, outside it, or across every surface simultaneously? Anthropic and OpenAI are betting on standalone tools. Cursor and Google are betting on IDE-integrated consoles. The answer will shape which company captures developer loyalty for the next decade, just as the cloud control plane wars of the early 2010s determined who owned infrastructure.

The code editor defined how software got built for four decades. Cursor 3 is a bet that supervising agents will matter more than editing files. Cursor didn’t kill the IDE. It demoted the IDE. And if that bet pays off, the last code editor anyone remembers was built by the company that made the best one. Stay tuned.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)