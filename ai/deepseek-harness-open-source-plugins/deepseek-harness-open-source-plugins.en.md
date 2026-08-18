DeepSeek on Thursday [open sourced the DeepSeek Harness](https://x.com/deepseek_ai/status/2087887408440164663), a new agent runtime for developers.

The Node.js-based harness is now available on [GitHub](https://github.com/deepseek-ai/deepseek-harness) as a developer preview and under an MIT license.

Clearly, there is some interest in the new harness. Within only a few hours, the repo picked up more than 33,000 GitHub stars, and that number is climbing quickly. Theirs is already a thriving [ecosystem of community plugins](https://github.com/topics/dsh-plugin).

What sets the DeepSeek harness apart is that “everything is a plugin,” as DeepSeek puts it. And the team takes that quite literally. The model adapter, the tool registry, the session log, and the agent loop itself are all plugins — and each one is replaceable.

![](https://cdn.thenewstack.io/media/2026/08/da2cbcb1-feat-plugin.en_-1024x640.png)

DeepSeek Harness plugins. Credit: DeepSeek.

There’s “no privileged core to patch,” the project’s documentation notes, so extending the harness simply means mounting a plugin beside the others.

The overall architecture is based on [Cordis](https://github.com/cordiverse/cordis), a “[meta-framework for spatiotemporal composability](https://github.com/cordiverse/paper).” To some degree, that sounds more complicated than it is. The core idea here is that software tools like modern AI harnesses require dynamic composition, meaning it needs to be easy to add and remove components without affecting the rest of the system — and those components need to be able to easily interact and understand how they depend on each other.

A [recent paper](https://github.com/cordiverse/paper/blob/main/paper.pdf) by three researchers from Peking University and DeepSeek explains this in more detail and forms [the basis](https://deepseek-harness.github.io/deepseek-harness/en/reference/cordis-primer) of Cordis and the DeepSeek Harness.

## Four modes, one model

The harness itself ships with four presets. *Standard* mode gives developers the full coding agent, with filesystem tools, shell access, web search capability, subagents, and a plan mode. On the other end, *Minimal* strips this down to only two tools, `bash` and `str_replace_editor`.

Then there is *Code* mode, which changes how tools reach the model. Rather than exposing those tools as individual function calls, it generates a TypeScript SDK and lets the model write a program against it, so a sequence that would otherwise take five round trips runs as a single call.

The fourth preset, Creator mode, is meant for developers who want to create custom agent presets. It inherits all of the features of the Standard mode and adds runtime inspection, plugin experiments, and preset-authoring guidance.

## Everything the model sees gets logged

Another core feature of the harness is that it keeps an append-only session log. Anything that reaches a model request has to be reconstructable from that log.

This also means that the conversation history is not just an implementation detail. Instead, core features like resume, fork, replay, transcripts, telemetry, and the web UI are all based on this single event stream. Adding any new kind of model-visible input therefore means adding a new session event.

The agent sandboxing is similarly strict — as it should be for any agent harness. The local backend wraps subprocesses in Linux [Landlock](https://landlock.io/) through a Node addon DeepSeek wrote, macOS [Seatbelt](https://sandboxicon.com/tech/seatbelt/), or a Windows ACL restricted-token runner.

![](https://cdn.thenewstack.io/media/2026/08/b0af4f5e-trajectory-real-view.en_-1024x640.png)

Agent logging. Credit: DeepSeek.

## Someone else’s model

It’s worth stressing that nothing in the harness ties it to DeepSeek’s models. Indeed, the provider catalog covers Anthropic, OpenAI, AWS Bedrock, Microsoft Azure and Google’s [Gemini Enterprise Agent Platform](https://thenewstack.io/google-gemini-agent-platform/) (though the documentation still calls it Vertex), alongside DeepSeek’s own endpoint. There is also the option to add custom OpenAI-compatible gateways for other inference providers.

What’s interesting is that the harness also ships with two subagent providers to delegate work directly to Anthropic’s [Claude Code](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/subagent/subagent-claude-code) and OpenAI’s [Codex](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/subagent/subagent-codex), resolving each product’s binary from the host PATH so the user supplies the install and the login. Both ship switched off by default.

DeepSeek also ships bridges that run a user’s existing `hooks.json` from either product against the harness’s own interception points, which the README describes as a compatibility path rather than the better design.

There’s also an MCP client, Agent Client Protocol support, and the harness can read `AGENTS.md` and `CLAUDE.md` files.

## No pull requests (yet)

As for contributing to the project, DeepSeek currently notes that “We are sorry that we cannot accept external pull requests at the moment.” Instead, it points would-be contributors to GitHub Discussions and to building plugins instead.

The company says it doesn’t consider packages in the official repository inherently more important than community ones, and that readers should treat the repo as “an idea, an official showcase, and a source of inspiration, but not a mandate from us.”

At this point, harnesses are everywhere, of course, and every major lab ships a coding agent now. Among the Chinese labs, Alibaba’s Qwen Code and ByteDance’s Trae Agent both launched in mid-2025, with Moonshot’s Kimi CLI following that October, and Zhipu’s ZCode arriving in July.

DeepSeek clearly believes that its plugin architecture is the major differentiator here, though, and while most of the competition is open source, the early reaction to the new harness shows that even though there’s plenty of competition, DeepSeek may have hit upon something here that developers are looking for.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)