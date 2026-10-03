Developers have long been able to customize Claude Code to their preferences, via [settings](https://code.claude.com/docs/en/settings), persistent instructions in [`CLAUDE.md`](https://code.claude.com/docs/en/memory), [hooks](https://code.claude.com/docs/en/hooks-guide), and [MCP servers](https://code.claude.com/docs/en/mcp), alongside tweaks such as [status lines](https://code.claude.com/docs/en/statusline) and [output styles](https://code.claude.com/docs/en/output-styles). Those controls can shape the instructions Claude follows, its permissions, the tools it can use, and more — but they can’t change Claude Code’s own features or the rest of its interface.

Now, however, [Anthropic is giving developers](https://claude.com/blog/claude-code-mods) much deeper control of Claude Code via [mods](https://code.claude.com/docs/en/plugins/mods/overview), which are small JavaScript or TypeScript functions that hook into events inside Claude Code. A mod can rewrite a prompt before it reaches the model, block or rewrite a tool call, handle permission requests, replace parts of Claude Code’s interface, or add entirely new functionality.

> “Each person works differently, so there’s no reason why everyone should have an identical Claude experience.”

## Changing how Claude Code looks and behaves

Taking to X on Thursday, Claude Code creator [Boris Cherny](https://www.linkedin.com/in/bcherny/) describes mods as a way for developers to reshape Claude’s appearance and behavior via a simple prompt, with the ability to package those customizations as plugins that other users can install.

“Each person works differently, so there’s no reason why everyone should have an identical Claude experience,” Cherny [writes](https://x.com/bcherny/status/2105756563302723721)

That can include changing what Claude Code displays while it’s working. For example, a mod might want to surface live information such as the number of tool calls Claude has made, how long it has been running, and how many tokens it has consumed, then present a summary once the task is complete.

![Live agent activity](https://cdn.thenewstack.io/media/2026/10/748b9fbf-gif1.gif)

*Live agent activity*

Users were already experimenting with more specialized uses within hours of the announcement. One software developer [built a mod](https://x.com/sean_snd/status/2105965372956623126?s=20) for passing credentials to Claude without leaving the underlying secret in the conversation history.

## How Claude Code mods work

Mods have actually been in the works publicly for at least a month already. Anthropic first floated the idea on GitHub [on September 3](https://github.com/anthropics/claude-code/issues/91870) under the more technical name “function hooks,” asking developers for feedback on an API that would let JavaScript and TypeScript functions intercept events inside Claude Code. Six days later, the company said it planned to ship the feature imminently under a rebranded “Claude Mods,” while retaining function hooks as the underlying mechanism.

Mods are now enabled by default in Claude Code 2.1.287 and later. Because a mod’s code stays active throughout a session, it can remember information between events and interact with Claude Code as things happen. That makes it possible to build interface elements that update live, launch processes, add commands, or expose new tools to the model. Anthropic says that it’s already using mods for features including `AGENTS.md` support and the `/diff` pane, and has published their source in the Claude Code repository.

> “That makes mods a way to fit Claude Code to how you work.”

In a [technical blog post](https://claude.dev/blog/getting-started-with-claude-code-mods/) accompanying the launch, [Addy Osmani](https://www.linkedin.com/in/addyosmani/) a member of technical staff at Anthropic, acknowledges that developers could already customize Claude Code through various mechanisms. However, he says that mods give them control over Claude Code’s own behavior and interface, with modules that respond to events during a session and can alter or replace what Claude Code does.

“That makes mods a way to fit Claude Code to how you work,” Osmani writes.

In one example, Osmani walks through an approximately 80-line Mod called *Token Weather*, which tracks how much of Claude’s context window has been consumed and displays the result in a band above the prompt. As Claude reads more files, the display moves from “Clear” at 18% of a 200,000-token window, to “Showers” at 67%, and finally “Storm” at 81%, while also showing recent usage and how many tokens the latest turn added.

![Token Weather tracks context use](https://cdn.thenewstack.io/media/2026/10/dab94512-gif4.gif)

*Token Weather tracks context use*

Given that mods are distributed as plugins, developers can publish them through the same plugin mechanism, including from repositories on GitHub. That does, however, introduce a security consideration: mod code executes locally with access through Claude Code to the developer’s machine, so Anthropic recommends inspecting the source and installing only code from trusted publishers.

For teams, however, mods inherit Claude Code’s existing plugin controls, while Team and Enterprise users and machines with managed settings load Anthropic’s `sec-default` guard ahead of user-installed mods. By default, that prevents those mods from overriding permission-deny rules; outside those guarded environments, mods can override some permission decisions.

Mods are available now in the Claude Code CLI and desktop app, and can be installed or shared through plugin marketplaces, including GitHub repositories.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)