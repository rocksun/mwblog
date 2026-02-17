With its [Visual Studio Code (VS Code)](https://thenewstack.io/visual-studio-2026-first-look-evolution-not-revolution/) [January 2026 release (v1.109)](https://aka.ms/VSCode/109), Microsoft is making the code editor “the home for multi-agent development,” introducing support for [Anthropic Claude](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/) and [OpenAI Codex](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/) agents, as well as an updated session management system that lets developers orchestrate multiple AI assistants from a single interface.

This shifts developers from a single-agent workflow to a multi-agent paradigm, allowing them to run GitHub Copilot, Claude, and Codex side by side. VS Code v1.109 (released February 4) enables developers to delegate work based on each agent’s strengths rather than being forced to use a single AI platform.

“Agents are changing how we work. You shouldn’t have to pick just one, or switch tools every time something new comes along,” the VS Code team writes in a [blog post](https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development). “With VS Code, you can run the agents you want, extend them with open standards, and manage them all from one place.”

## Biggest strength

[Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at the Futurum Group, says the change shows the influence of VS Code.

“Honestly, this move by Microsoft shows that its biggest strength isn’t any single model but instead VS Code itself, which is arguably the most popular editor in the world,” Shimmin tells *The New Stack*. “If users love Claude but have to leave VS Code to use it effectively, Microsoft loses. If they bring Claude to users, however, they can keep them in their ecosystem — and likely keep their subscription revenue.”

Moreover, “There’s no single model that can be the ‘winner’ for every developer. Microsoft knows this, and that’s why they’re moving from being an OpenAI shop to a Universal AI Interface,” he adds.

## Claude joins the party

The primary new feature is public preview support for Claude agents using Anthropic’s Claude Agent SDK. [Developers with GitHub Copilot subscriptions](https://thenewstack.io/github-agent-hq/) can now delegate tasks to Claude models directly within VS Code, using the same prompts, tools, and architecture found in other Claude implementations, the post says.

“You can now run Claude and Codex agents directly alongside GitHub Copilot,” the VS Code team writes in the post. “Start them as local agents when you need fast, interactive help, or delegate async to a cloud agent for longer-running tasks.”

Thus, GitHub Copilot Pro+ and Enterprise subscribers gain access to Claude and Codex as cloud agents, while local agent support requires the OpenAI Codex extension. Codex has been available as a local agent since November; Claude is new.

## Unified session management

VS Code v1.109 offers an updated Agent Sessions view that provides a single dashboard for tracking all agent activity across local, background, and cloud environments. Developers can kick off a cloud agent for well-defined refactoring tasks while simultaneously running a local session for exploratory work, switching contexts without losing momentum, the post says.

“The beauty of this unified approach is that all these agents show up in the same Agent Sessions view,” Microsoft explains. “You can delegate tasks between them, compare their outputs, and pick the right tool for each job.”

Agent sessions now display clear status indicators showing which sessions need attention, with improved progress tracking for long-running operations and better failure handling.

## Parallel Subagents

A significant improvement is parallel [subagent](https://code.visualstudio.com/docs/copilot/agents/subagents) execution, which enables developers to fire off multiple subagents simultaneously.

“Subagents are context-isolated agents that run independently from your main session,” the VS Code team explains. “Your main agent delegates work, and only the final result flows back. The intermediate exploration stays contained, keeping your primary context clean.”

Each subagent can have specialized behavior.

## MCP Apps arrive

Microsoft says VS Code is now the first major AI code editor with full support for [MCP Apps](https://modelcontextprotocol.io/docs/extensions/apps), the official Model Context Protocol extension that lets tool calls return interactive UI components. Instead of plain text responses, agents can now render dashboards, forms, visualizations, and multi-step workflows directly in chat.

“This creates opportunities for a richer and more effective human-agent collaboration,” Microsoft says.

The release also makes [Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills) — Anthropic’s open standard for extending AI agents — generally available.

## Further optimizations

The release also includes other optimizations, including [Copilot Memory](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-copilot-memory-a-more-productive-and-personalized-ai-for-the-way-you/4432059), which helps agents retain relevant context across interactions. The release also delivers faster code search through external indexing, improving responsiveness during large-repo development.

In addition, the release provides enhanced security with experimental terminal command sandboxing on macOS and [Linux](https://thenewstack.io/introduction-to-linux-operating-system/). Auto-approval rules reduce unnecessary prompts while maintaining control over agent-driven actions.

The chat experience is also faster and more responsive, with improved streaming, higher-quality reasoning results, and better visibility into the model’s thinking. Agents now ask clarifying questions instead of making assumptions, and a revamped inline chat makes in-context Copilot interactions feel more natural.

## Just the beginning

The company positions the latest VS Code release as just the beginning.

“A year ago, we were just introducing agent mode,” the VS Code team writes. “Now you’ve got Copilot, Claude, and Codex running side by side and SO much more.”

Microsoft will demo the new features at its [Agent Sessions Day](https://youtube.com/live/tAezuMSJuFs) on February 19.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)