Two of the biggest players in the AI coding space are betting that developers want to talk to their agents while they work, with both announcing a two-way voice feature that lets users ask questions and give follow-up instructions without returning to the keyboard.

[On Friday](https://cursor.com/changelog/voice-chat), Cursor announced [Voice Chat with Agents](https://cursor.com/docs/agent/voice-chat), a [Grok Voice](https://x.ai/news/grok-voice-think-fast-1)-powered feature that lets developers call an agent and talk through a change. On the very same day, Google [announced Voice mode in Antigravity](https://antigravity.google/blog/antigravity-voice-mode), which uses [Gemini Live](https://support.google.com/gemini/answer/15274899) to bring spoken conversations to its desktop app and command-line tool.

In a [blog post](https://antigravity.google/blog/antigravity-voice-mode) announcing the feature, [Nick Van der Auwermeulen](https://www.linkedin.com/in/nickvander/), developer relations engineer at Google, contrasts the back-and-forth dynamic of human colleagues with the “rhythm” of working with coding agents.

“Some of the best engineering happens out loud,” Van der Auwermeulen writes. “You talk a bug through with a teammate, think out loud in front of a whiteboard, or say ‘*wait, try it the other way*’ halfway through a pairing session. Working with an agent has mostly had a different rhythm: you type a prompt, the agent works, you read what it did, and you type again.”

> “Some of the best engineering happens out loud.”

The longer a job runs, he adds, the more often developers need to check in. A command might be waiting for approval, or a developer might spot a requirement the original instructions missed.

“Each of those moments pulls you back to the keyboard and away from whatever you were looking at,” he continues.

And so Antigravity’s voice mode keeps a live call open while the coding agent works, so the developer can hear an update or approve a command without reaching for the keyboard.

Cursor, for its part, makes a similar pitch for keeping the conversation going.

“Describe a change out loud, ask what an agent is working on, and hear updates as the work moves forward,” the company writes.

> “Describe a change out loud, ask what an agent is working on, and hear updates as the work moves forward.”

## Look who’s talking

[Antigravity](https://antigravity.google/), for the uninitiated, is Google’s agentic software development platform. It [debuted alongside Gemini 3 last November](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/), with [version 2.0 landing in May](https://thenewstack.io/google-io-antigravity-codemender-ai-agentic/) replete with a separate desktop app. There’s also a terminal client, [Antigravity CLI](https://antigravity.google/blog/introducing-google-antigravity-cli/), and extensions [for developers who want to work from editors](https://thenewstack.io/google-antigravity-ide-extensions/) such as VS Code, JetBrains IDEs and Xcode.

Antigravity is now where Google is consolidating its various coding tools, having [moved individual Gemini CLI users to Antigravity](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) in June, while it’s also in the midst of [sunsetting Jules](https://x.com/julesagent/status/2115883717705261283), a previously launched background coding agent.

It’s worth noting that Antigravity’s [existing dictation feature](https://antigravity.google/blog/introducing-google-antigravity-2) already turns speech into a written prompt. Now, [to start a two-way call](https://antigravity.google/docs/voice-mode) in the desktop app, the user clicks the waveform button beside it and tells the agent what they want it to do.

![Starting a voice call](https://cdn.thenewstack.io/media/2026/11/98af36c0-gif1.gif)

*Starting a voice call*

Antigravity replies aloud and keeps the call open while the coding agent works, with the user able to ask how it’s going or give it further instructions. You can also interrupt the agent mid-sentence to ask a question or give it another instruction.

![Antigravity responds out loud](https://cdn.thenewstack.io/media/2026/11/5a9db8bf-gif2.gif)

*Antigravity responds out loud*

When the agent finishes, its written summary and a button to review the code changes appear in the same chat.

![Reviewing the fix mid-call](https://cdn.thenewstack.io/media/2026/11/dee44a5e-gif3.gif)

*Reviewing the fix mid-call*

Additionally, voice mode also works in the Antigravity CLI. Users run the `/voice live` command to start a call, and hear the agent reply while it works away in the terminal.

![Starting a terminal voice call](https://cdn.thenewstack.io/media/2026/11/ed88c811-cligif.gif)

*Starting a terminal voice call*

## Coding agents talk back

Cursor, which was [acquired by Elon Musk’s SpaceX](https://cursor.com/blog/joining-spacex) in August for $60 billion, has followed a similar path toward embracing voice. It added [dictation in October 2025](https://cursor.com/changelog/2-0), and in [release notes](https://prod.cursor.com/docs/release-notes) last month, the company said it had updated existing voice calls to let agents give short spoken progress updates.

One difference with Cursor’s rollout is *where* you can call from. Cursor supports voice chat on the web and iOS as well as on desktop, while Google offers it in the Antigravity desktop app and CLI. Cursor’s calls run on [Grok Voice](https://x.ai/news/grok-voice-think-fast-1), which xAI [launched through its API back in April](https://x.ai/news/grok-voice-think-fast-1).

> “The push now, it seems, is to keep the conversation going after the agent starts work.”

However, Google and Cursor aren’t the first AI companies to bring two-way voice to coding agents. OpenAI [launched](https://openai.com/index/introducing-the-codex-app/) a Codex desktop app in February with a [built-in dictation feature](https://learn.chatgpt.com/docs/whats-new#february-26-2026). And as *The New Stack* [reported in July](https://thenewstack.io/voice-ai-openai-anthropic/), the company added two-way voice to Codex in the ChatGPT desktop app, letting developers give instructions and check on tasks by speaking. The Codex CLI has offered live voice conversations [since the spring](https://github.com/openai/codex/releases/tag/rust-v0.119.0#new-features), with OpenAI enabling them by [default in September](https://github.com/openai/codex/releases/tag/rust-v0.156.0#new-features).

Anthropic, for what it’s worth, has a [voice mode](https://support.claude.com/en/articles/11101966-use-voice-mode) which offers two-way voice functionality inside the Claude app only. In Claude Code, specifically, voice still only goes one way via dictation — the `/voice` command turns developers’ vocal instructions [into prompt text](https://code.claude.com/docs/en/voice-dictation), and the agent replies in writing.

Dictation itself is useful for describing a bug or sketching out a feature aloud, and it’s showing up across the AI coding landscape, from the major AI labs to well-funded startups [such as Replit](https://docs.replit.com/updates/2026/06/19/changelog#voice-mode).

The push now, it seems, is to keep the conversation going *after* the agent starts work, so developers can follow up about a decision, clarify a requirement, or change direction before the work is finished.

[Claude Code
Step-by-Step guide to becoming a Claude Code expert in 2026

Introduction
Ways to use Claude
Understand the Basics
Using Claude Code
Claude Workflow
Usage Best Practices
CLAUDE.md
Skills
Hooks
Manage Context](https://roadmap.sh/claude-code?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=cursor-antigravity-voice-agents)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)