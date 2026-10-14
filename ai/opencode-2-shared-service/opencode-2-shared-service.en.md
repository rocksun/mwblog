[OpenCode](https://opencode.ai/) 2.0 is getting a formal unpacking today, some three months after its [public beta launch](https://web.archive.org/web/20260710181539/http://v2.opencode.ai/). The sizable architectural upgrade introduces a shared background service connecting its terminal, web and desktop interfaces, alongside a rebuilt API, a new embeddable SDK, and support for running subagents and shell commands in the background.

In a [blog post](https://anoma.ly/notes/opencode-2-0/) published on Monday, [Anomaly](https://anoma.ly/), the company behind the open-source coding agent, calls the release a “major overhaul,” adding that it drew on the experiences of “millions of daily users” to build a more adaptable system capable of supporting an expanding range of agent capabilities.

Anomaly has, in fact, been iterating on version 2.0 over the past few months, including [publishing a detailed technical account](https://anoma.ly/notes/opencode-reloaded/) of its revamped plugin architecture and hot-reloading capabilities in September. However, the drawn-out rollout has caused some confusion among developers, with [questions about whether version 2.0](https://www.reddit.com/r/opencode/comments/1wppj69/is_opencode_v2_officially_in_a_stable_release/) was officially stable yet, and [complaints about missing release notes](https://github.com/anomalyco/opencode/issues/52184), even as updates kept shipping.

Monday’s announcement, alongside the official changelog’s switch to the [2.x series](https://opencode.ai/changelog), effectively signals that version 2 is now OpenCode’s main release. In tandem, the company is also offering a broader explanation of the technical decisions behind the upgrade.

## OpenCode’s story so far

![OpenCode is an open-source coding agent.](https://cdn.thenewstack.io/media/2026/10/d69ae913-generalgif.gif)

*OpenCode is an open-source coding agent.*

By way of a brief recap, OpenCode’s origins lie in the world of serverless development. Anomaly founders [Jay V](https://www.linkedin.com/in/jayair/) and [Frank Wang](https://www.linkedin.com/in/fanjiewang/) previously created Serverless Stack ([SST](https://sst.dev/)), an open-source framework for building and deploying applications on Amazon Web Services (AWS). [Dax Raad](https://x.com/thdxr), another prominent figure in OpenCode’s development, was also part of the SST team.

Since its 2025 debut, OpenCode has gained a fervent following among developers looking for greater freedom over the AI models powering their coding tools. That became particularly pertinent in January when [Anthropic began preventing](https://venturebeat.com/technology/anthropic-cracks-down-on-unauthorized-claude-usage-by-third-party-harnesses) third-party agents from using Claude Pro and Max subscription credentials, forcing affected developers to find alternative ways of accessing Claude or switch providers.

As Janakiram MSV [reported](https://thenewstack.io/anthropic-claudecode-opencode-split/) for *The New Stack* in May, these restrictions coincided with a surge of interest in OpenCode, which allows developers to switch between competing AI models. Today, the [OpenCode GitHub repository](https://github.com/anomalyco/opencode) has accumulated north of 212,000 stars and almost 30,000 forks.

More broadly, there are signs of [growing commercial interest in this category](https://thenewstack.io/open-source-coding-agents-like-opencode-cline-and-aider-are-solving-a-huge-headache-for-developers/) of coding agents. In July, [Anaconda acquired Kilo](https://thenewstack.io/anaconda-kilo-open-source-acquisition/), another such open-source coding agent that allows developers to choose their preferred AI provider. Interestingly, Kilo had already rebuilt its command-line interface and VS Code extension using OpenCode, demonstrating how the latter was finding a role inside other developer tools.

With version 2.0, Anomaly has laid out *how* it has reworked OpenCode’s underlying architecture to accommodate a wider range of use cases. Arguably, the most significant change concerns how the coding agent runs, and how its different interfaces connect to it.

## One service, multiple interfaces

Anomaly says the plumbing for a client/server setup has been in OpenCode from the start, though few beyond power users went out of their way to use it.

With version 2.0, the server now starts automatically as a single background process on the developer’s machine, allowing OpenCode’s terminal, browser and desktop interfaces to communicate with the same underlying service.

This means developers can access and manage their coding sessions through different interfaces, while the service handles the underlying execution. Scripts built using OpenCode’s programmatic client can also automatically discover and connect to the local service, making it useful for scheduled tasks, while developers can additionally expose the service to other machines and pair it with external applications.

> “Developers can now start a session in OpenCode’s terminal interface, continue working on it through the desktop or web app, and have their own scripts connect to the same underlying service”.

The long and short of this is that developers can now start a session in OpenCode’s terminal interface, continue working on it through the desktop or web app, and have their own scripts connect to the same underlying service.

![One service, multiple interfaces](https://cdn.thenewstack.io/media/2026/10/0fd446f4-gif1.gif)

*OpenCode’s shared background service*

These architectural changes are accompanied by a ground-up redesign of OpenCode’s API, which Anomaly concedes was built piecemeal while the industry was still figuring things out.

“The old API grew haphazardly as we and the world collectively learned what agents are and should be,” the company writes in its blog post. “It was bad.”

> “The old API grew haphazardly as we and the world collectively learned what agents are and should be. It was bad.”

And so the new API gives the agent greater control over its own environment. For example, it can create a Git worktree for a new task, transfer an existing session into that worktree, or identify and interrupt another session that has become stuck. Developers can also access the API through a new `@opencode/client` package, which supports standard JavaScript and Effect.

![Agents manage their own sessions](https://cdn.thenewstack.io/media/2026/10/5a7dce35-gif2.gif)

*Agents manage their own sessions*

Another addition is an embeddable [SDK](https://opencode.ai/v2/docs/build/sdk), distributed as `@opencode/sdk`, that allows developers to incorporate OpenCode directly into their own applications. It uses the same underlying code as OpenCode’s CLI, the company notes, enabling developers to create customized versions of the agent for servers or environments such as Cloudflare Durable Objects.

These implementations can communicate with existing OpenCode clients through its standard server protocol, although Anomaly says the SDK remains under development.

## Code Mode and background execution

OpenCode 2.0 also changes *how* agents interact with external tools through the [Model Context Protocol](https://thenewstack.io/model-context-protocol-roadmap-2026/) (MCP).

A feature dubbed Code Mode allows agents to write JavaScript that calls multiple tools and processes their results within a single execution. Built around a lightweight JavaScript interpreter in the `@opencode/codemode` package, it converts MCP servers and OpenAPI endpoints into functions that agents can invoke programmatically.

For example, an agent could retrieve bug reports from GitHub, extract the relevant information and create corresponding issues in Linear, without having to make a separate model round trip for each operation.

The implications are particularly significant for developers connecting agents to large numbers of external services, where tool definitions can consume substantial portions of a model’s available context. Anomaly is making Code Mode the default for all MCP servers in version 2.0, arguing that it makes extensive integrations more practical.

“This means you can add a thousand of them with minimal context bloat and your agent will discover and compose them to get things done,” the company writes.

![Code Mode connects MCP tools](https://cdn.thenewstack.io/media/2026/10/3bfce0e7-gif3.gif)

*Code Mode connects MCP tools*

Meanwhile, OpenCode is introducing background execution for both subagents and shell commands, allowing developers to continue interacting with the primary agent while other operations are underway.

A developer could, for instance, delegate a code review to a subagent running a different AI model while continuing to work on the main task. Similarly, lengthy shell operations, such as running tests or building an application, can execute asynchronously, with the primary agent receiving a notification when they finish.

Developers can also use a keyboard shortcut to move an existing foreground task into the background if it takes longer than expected.

![Subagents and commands run concurrently](https://cdn.thenewstack.io/media/2026/10/c9bda033-gif4.gif)

*Subagents and commands run concurrently*

Rounding out the release are changes to OpenCode’s plugin architecture. Anomaly says it has implemented more than 80 internal plugins, covering most of the functionality introduced in version 2.0, as part of an effort to improve the reliability and maintainability of its plugin API.

Terminal interface plugins have also been promoted from experimental to stable, while support for hot reloading means OpenCode can create and start using a new plugin during an active session, without requiring a restart.

There are, however, some compatibility implications for existing users. Plugins developed for OpenCode 1.0 won’t work with version 2.0, while integrations built around the previous server API will need updating.

Existing OpenCode 1.x users can upgrade to version 2.0 by running `opencode upgrade --major` from the command line or entering `/update` in the terminal interface. According to the [October 11 release notes](https://github.com/anomalyco/opencode/releases/tag/v1.19.0), updates are no longer installed automatically, meaning users must initiate the upgrade themselves.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)