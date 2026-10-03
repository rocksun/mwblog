**GitHub launched computer use in public preview on Thursday**, giving Copilot CLI and its desktop app the ability to operate applications on macOS and Windows. Agents can read app content and click, type, scroll, and drag, including in older, GUI-only software with no API, command-line interface, or MCP integration.

An expense report in Safari was GitHub’s [launch demonstration](https://github.blog/changelog/2026-10-01-github-copilot-can-now-interact-with-desktop-apps/) but the company described other uses including summarizing information in a legacy application, updating a presentation, entering data, and moving information between apps. Developers can access the feature from the terminal or through the Copilot app, which runs on Copilot CLI and [launched earlier this year as a rival to Claude Code and Codex](https://thenewstack.io/github-copilot-desktop-app/).

GitHub has some catching up to do. OpenAI [added computer use to Codex in April](https://thenewstack.io/openai-codex-chrome-extension/), while Anthropic brought broader computer use on macOS to Claude Code and Claude Cowork earlier this year.

> GitHub has some catching up to do.

## Computer use vs. MCP servers

Enabling computer use in Copilot CLI activates a [bundled plugin with its own MCP server](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/computer-use). It works in local sessions, reading application content through the operating system’s accessibility tree and taking screenshots when it needs visual context.

The company recommends using direct tools wherever possible. So, if an API, MCP server, terminal command, filesystem tool, or dedicated browser tool can handle the task, it typically provides more structured information and more predictable results than desktop interaction.

That advice limits where GitHub thinks computer use belongs. OpenAI president [Greg Brockman](https://www.linkedin.com/in/thegdb/) made a broader case [last month](https://thenewstack.io/computer-use-agent-connectors/), arguing that agents could use the same interfaces as people and spare the industry the work of building and maintaining a connector for every piece of software.

## Saved approvals outlast their removal

Developers enable the feature with `/computer` on in Copilot CLI or through the Copilot app’s Computer Use settings. macOS also requires Accessibility permission to operate controls and Screen Recording permission to inspect windows when visual context is needed.

The CLI session’s permission mode determines whether Copilot asks before accessing an app; developers can check it with `/permissions show`. When prompted, they can allow access for the current session, choose “Always allow” for future sessions or decline. Deny rules override both automatic and saved approvals.

Approvals saved in the CLI carry over to the desktop app on the same computer. Removing an app from the always-allowed list clears its approval for future sessions but leaves access already granted in a running session intact.

Stopping work requires a separate action: press Esc twice in the CLI, or click Stop or press Esc in the desktop app.

## Enterprise controls over computer use

Enterprise policy overrides a developer’s local preference. If managed settings block computer use, Copilot CLI reports that the feature is unavailable.

> Enterprise policy overrides a developer’s local preference.

Through `managed-settings.json`, enterprise owners can also [control whether developers may bypass approval prompts](https://github.blog/changelog/2026-07-27-enterprise-managed-settings-now-apply-to-the-github-copilot-app/). That restriction applies across the Copilot app, CLI, and VS Code.

GitHub’s default-enablement policy for Business and Enterprise does not change this preview’s opt-in status. The policy starts applying to unconfigured features on October 22 but excludes preview features.

## Reliability depends on the interface

A change in timing or window state can cause Copilot to repeat an action or stall. GitHub also warns that the agent may choose the wrong control, type into the wrong field, or struggle with dynamic interfaces and complex workflows.

> Sensitive information visible in an application window may also become context for the agent.

Unexpected on-screen content and ambiguous instructions can lead to actions affecting the user’s device, data, or connected accounts. Sensitive information visible in an application window may also become context for the agent.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)