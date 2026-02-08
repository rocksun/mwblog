Google has [added](https://developers.googleblog.com/tailor-gemini-cli-to-your-workflow-with-hooks/) hooks to [Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/), its terminal-based competitor to Anthropic’s Claude Code.

[Hooks](https://geminicli.com/docs/hooks/) ensure that Gemini CLI runs a given script or program inside of the agentic loop and bring a larger degree of control to the agentic development loop. These could be used, for example, to run security scanners or compliance checks, log tool interactions, inject relevant information into the context window, or even adjust the model’s parameters on the fly.

As the Gemini CLI team notes in the announcement, “efficiency in the age of agents isn’t just about writing code faster; it’s about building custom tools that adapt to your specific environment.”

![](https://cdn.thenewstack.io/media/2026/01/495a80b2-gemini_cli_hooks_panel.original.png)

Hooks in Gemini CLI (Credit: Google).

While a developer could try to instruct the agent to run a specific script at certain times within the loop in the prompt or [AGENTS.md](https://agents.md/) file, given the non-deterministic nature of those agent models, there’s no guarantee that this will actually happen or that the agent won’t forget about this instruction over time.

## Claude Code did it first

If this sounds familiar, it’s likely because you already know about Claude Code Hooks, which first introduced this idea [last September](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously) (though there is also a [GitHub issue from July 2025](https://github.com/google-gemini/gemini-cli/issues/2779) that proposes this feature). Google’s implementation is not quite a one-to-one match to Anthropic’s, but it should only take a few minutes to adapt an existing Claude hook to Gemini CLI.

## Setting up hooks

Like with hooks in Claude Code, Gemini CLI also implements roughly [a dozen lifecycle events](https://geminicli.com/docs/hooks/) where a hook can fire. That may be right at the session start, after the user submits a prompt but before the agent starts planning (to add context, for example), before tools are selected (to optimize the tool selection or filter available tools), and similar moments in the agent loop.

![defining a google gemini cli hook in a JSON file.](https://cdn.thenewstack.io/media/2026/01/781ce4d0-screenshot-2026-01-29-at-10.47.25.png)

Defining a Gemini CLI hook (Credit: Google).

The hooks are defined as JSON files that describe when they are invoked and which script they should run. Those scripts are standard Bash scripts and Google notes that it is essential to keep those hooks fast because they do run synchronously and delays in the script will also delay the agent response.

Google [recommends](https://geminicli.com/docs/hooks/best-practices/) that developers use parallel operations and caching when possible to keep the operations fast.

One interesting use case for hooks is to utilize the ‘AfterAgent’ hook, which fires when the agent loop ends, to force the agent into a continuous loop to work on a difficult task — while also refreshing the context between those runs to avoid context rot.

As for security, it’s important to stress that hooks will have the user’s privileges, and Google notes that developers should review the source code of any third-party hooks.

Hooks, which are now available as part of the Gemini CLI v0.26.0 update, can also be packaged inside Gemini CLI extensions. That’s Google’s format for packaging prompts, MCP servers, sub-agents, and agent skills — and now hooks — into a single sharable package.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)