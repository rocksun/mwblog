OpenAI this week announced that it is adding [plugins to Codex](https://developers.openai.com/codex/plugins). These plugins for third-party services like Box, Figma, Linear, Notion, Sentry, Slack, Gmail, and Hugging Face, package reusable workflows, MCP servers, and app integrations into installable bundles for the Codex app.

This move is reminiscent of what Anthropic has been doing with Claude Code and its desktop app, as well as Google’s Gemini CLI, both of which already offer comparable systems. But maybe more importantly, it is also a step for OpenAI to bring more tools into Codex that are not directly coding-related and will make the app more attractive to users who may be considering a move to Claude and Claude Cowork in Anthropic’s desktop app.

If Codex becomes the core of [OpenAI’s “superapp](https://www.wsj.com/tech/openai-plans-launch-of-desktop-superapp-to-refocus-simplify-user-experience-9e19931d),” it needs to go beyond coding. This feels like a first step in this direction.

![](https://cdn.thenewstack.io/media/2026/03/3e0c5bd6-directory-2-1024x671.png)

Credit: OpenAI.

Many of the new plugins, of course, are coding related, but it is noteworthy that this first new group of plugins push Codex into the planning, research, and coordination phases that happen before and after the code is written.

Instead of stitching together separate MCP servers and custom instructions, a plugin can package everything into one install that teams can then standardize on across developers without asking each person to assemble the pieces.

At their core, Codex plugins bundle skills (the usual Markdown-based workflows virtually all AI companies now support), with optional app connectors, and MCP servers for external tools. More than 20 plugins are available at launch, and users will be able to use them across the Codex app, CLI, and OpenAI’s VS Code extension.

Interestingly, OpenAI is putting these plugins front-and-center in the Codex UI, with a dedicated tab right underneath the ‘New Thread’ button. Clicking that takes you into a curated directory in the app. Self-serve publishing is not yet available, but support for additional plugins is coming soon.

In the Codex CLI, the /plugins command lets you install them from the terminal.

![](https://cdn.thenewstack.io/media/2026/03/4daf18fe-codex-local-plugin-light-1024x464.png)

Credit: OpenAI.

One of the more complex examples for a plugin that is currently available in the directory is the “build web app” plugin. It bundles the Stripe, Supabase, and Vercel MCP servers with dedicated skills to deploy to Vercel, build frontends, and best practices for web design and using these third-party services.

## What about Anthropic and Google?

Anthropic’s Claude Code has offered plugins since earlier this year, also bundling MCP servers, skills, slash commands, and hooks into single-click installs. Anthropic similarly ships a built-in marketplace with its app, and developers can also publish to repo-level or personal marketplaces, too (this feature is coming to Codex soon).

Google’s Gemini CLI and Antigravity, the company’s AI-centric IDE, call these plugins “[extensions](https://geminicli.com/extensions/),” but they are quite similar to Anthropic’s and OpenAI’s implementation: MCP servers, custom commands, agent skills, hooks, and themes, distributed via GitHub or a built-in registry. Google also [recently](https://developers.googleblog.com/making-gemini-cli-extensions-easier-to-use/) added extension settings that prompt users for configuration like API keys at install time and store them in the system keychain.

For the most part, all of the three major vendors now use the same architecture for these plugins/extensions. Switching between them and Codex is also quite easy. OpenAI explicitly notes that “if you already have a plugin from another ecosystem or a plugin you built yourself, you can add it to your local marketplace with `@plugin-creator`.”

This plugin creator, which also mimics similar features in Claude Code and Cowork, for example, lets you build new plugins — or at least create the scaffold for one — by simply describing the functionality you are looking for.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)