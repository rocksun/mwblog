During the early phase of my career, I used to spend eight hours a day inside the Visual Studio IDE. Fast-forward to today, and developers spend more time delegating work than coding in an IDE.

That shift points us to something dramatically different – from writing and editing code to orchestrating coding agents. It is not just autocompletion bolted onto existing workflow, but a fundamental shift in how software is being built. The IDE still matters, but it is no longer on the main stage.

## The old regime of development

In the last three decades, the IDE was central to software development. From editing to navigating, refactoring, debugging, and building, the integrated development tool was the cockpit of coders and developers. Turbo C, Borland Delphi, PowerBuilder, Visual Studio, IntelliJ, Eclipse, and, more recently, VS Code dominated the IDE market. They have been the gravitational centers of professional software development.

IDEs made perfect sense based on the approach of “human writes code, tools assist”. Every feature, from syntax highlighting to debugging to integrated terminals, was designed to keep developers productive without leaving the editor. IDEs are meant to reduce the friction and optimize the loop of intent and implementation. This also meant that the developer was the bottleneck and the decision maker at every keystroke.

## Three waves of AI coding tools

The arrival of AI models targeting the developer workflow did not happen overnight. It happened in three distinct waves, each shifting the center of gravity further away from the IDE.

Wave 1 brought AI as a feature inside the IDE. Autocomplete, inline edits, and chat sidebars appeared as extensions. [GitHub Copilot](https://github.com/features/copilot) was the breakout example. The IDE remained the host, and AI was a guest. Developers stayed in the same seats. They just got a faster pair programmer sitting next to them.

Wave 2 moved AI into the terminal as an execution layer. CLI agents like [Gemini CLI](https://geminicli.com/) and [Claude Code](https://code.claude.com/docs/en/overview) brought a different model. Instead of suggesting the following line, these tools accept higher-level instructions. “Fix the failing tests across this module.” “Refactor this service to use the new API.” The terminal became a place where agents do work, not just where developers type commands. The IDE was still in the picture, but it was no longer the only place where meaningful progress happened. This marked the beginning of agents taking over the traditional job of an IDE.

Wave 3 is what we are watching emerge right now. Desktop control planes that are designed around multi-agent, long-running, parallel task management. These control planes orchestrate agents that handle various development tasks a typical developer would perform in an IDE.

![](https://cdn.thenewstack.io/media/2026/02/f4a4c263-codex-1024x801.png)

Within a few weeks, both Anthropic and OpenAI have released tools that hint at this trend. Anthropic’s new [Claude Cowork](https://claude.com/blog/cowork-research-preview) mode gives its AI assistant direct access to a local folder so that it can read, modify, and create files in a sandbox on your machine. Around the same time, OpenAI unveiled the [Codex desktop app for macOS](https://openai.com/index/introducing-the-codex-app/), a command center for running multiple AI coding agents in parallel with built-in diff review and seamless handoff to your IDE.

OpenAI’s Codex app for macOS supports managing multiple agents working simultaneously on different tasks. Anthropic’s Cowork and Code introduce a desktop experience that extends agentic capabilities beyond developer-only workflows, allowing agents to read files, run commands, and operate within explicit sandboxes.

![](https://cdn.thenewstack.io/media/2026/02/004fc339-cowork-1024x820.png)

Here’s the main idea we need to focus on. Once the UI is built around orchestration driven by the control plane, the IDE stops being the “home” and becomes just another surface.

## What is an agent control plane?

Since this may sound abstract, let me make it practical and concrete. An agent control plane is a desktop application that coordinates five things:

1. **Tasks**, meaning what needs to be done
2. **Tools** that the agent can use to accomplish a task
3. **Permissions** that explicitly allow an agent to access local resources, such as files or databases
4. **Context**, which is the crucial component of an agent that provides the knowledge about the codebase and the project
5. **Review** puts the developer in the loop for approving or rejecting the output

These functions go beyond what IDE-first workflows can do. Parallelism, where multiple agents work simultaneously in a single chat window, attempting to tackle one thread at a time. This means developers can launch multiple agents that concurrently work on backend code and frontend UI. Long-running jobs, where background tasks like test suites, large refactors, or database migrations run asynchronously, and you check the results later. And system-level actions, where agents read and modify files, run commands, and integrate with external tools within defined boundaries.

OpenAI’s Codex macOS App supports launching long-running tasks that can be offloaded to the cloud while the developer is working on local code.

In this model, the main developer interface becomes a task dashboard. Not a text editor.

## The IDE becomes a second-class citizen

I wish to clarify this assertion, as the simplified version may sound incorrect. IDEs are not optional. They are not going away. But they are being demoted from the orchestration layer.

In agent-first workflows, IDEs become diff and review surfaces where you verify what agents produced. They become debugging environments for the cases where agents get stuck or produce subtle errors. And they remain the right tool for precise editing on tricky edge cases where human judgment at the character level still matters.

The rising tension is that IDEs are also agents of absorption. The real battle is not IDE versus agent. It is about where orchestration lives. Apple just [announced](https://www.apple.com/newsroom/2026/02/xcode-26-point-3-unlocks-the-power-of-agentic-coding/) that it integrated OpenAI Codex and Anthropic’s agents directly into [Xcode](https://developer.apple.com/xcode/), showing that IDE incumbents will fight hard to keep the IDE at the center of the developer’s world.

IDEs are not dying. They are being repositioned as high-trust verification tools.

## The competitive chessboard

If orchestration moves above the IDE, the competitive landscape shifts in ways that should worry some companies and encourage others.

IDE-first companies face real pressure. If the control plane sits outside the IDE, the editor risks becoming commoditized. [JetBrains](https://www.jetbrains.com/), for instance, faces a strategic choice between becoming the best review-and-debug surface in an agent-first world or building and controlling the orchestration layer itself. Both are viable paths, but the comfortable middle ground of “IDE plus AI features” may not be defensible for long.

Microsoft sits in a particularly complex position. It owns Visual Studio, VS Code, and GitHub Copilot. Promoting a standalone desktop control plane would compete directly with its own IDE-centric stack. My hypothesis is that Microsoft will prefer to embed orchestration into its existing surfaces rather than build something that undermines them. Whether that strategy works depends on whether embedded orchestration can match the purpose-built alternatives.

Google has a different opening. It is already pushing a CLI-first agent path with [Gemini CLI](https://geminicli.com/), which means it can promote orchestration across surfaces without cannibalizing an IDE business it does not have. The caveat is that success here depends on distribution and developer trust, not model quality alone.

## What would change my mind

Three counterarguments deserve honest consideration. First, IDEs might integrate agents so deeply that they recapture the orchestration layer. Xcode’s moves suggest this is a real possibility. Second, desktop control planes might fragment attention. Developers already juggle too many tools, and adding another surface could face adoption resistance. Third, security and compliance requirements may constrain autonomous agent actions so severely that orchestration consolidates inside enterprise toolchains rather than standalone apps.

I would revise my position if IDEs become genuinely great orchestration layers with permissions management, background agent execution, task queues, and plugin ecosystems that make standalone control planes unnecessary.

## The job description changed

The IDE used to be where software happened. In an agent-first workflow, the software is verified and reviewed.

The shift from editing to orchestration is not speculative. It is playing out right now across the tools being shipped by OpenAI, Anthropic, Google, and Apple. The next battleground will not be about which surface is prettier or which model is smarter. It will be about trust. Auditing, provenance, and the ability to answer a simple question that grows more important by the month. Who did what in this codebase, and can I verify it?

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)