With the MCP protocol, Anthropic created the de facto standard for AI models and agents to talk to third-party applications. After donating the MCP protocol to the [Agentic AI Foundation](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/) last December, Anthropic today released a major new open extension to MCP that will allow MCP servers to serve up an interactive app-like experience right within the chat interface.

Anthropic, of course, is building this feature right into the web and desktop experiences for Claude. It’s worth stressing, however, that this is an open protocol, so any other chatbot provider can adopt this protocol, and any third-party service will be able to build these apps.

Already, support for MCP Apps is available in Goose, Visual Studio Code (for Insiders), and, later this week, ChatGPT from Anthropic competitor OpenAI.

Some of Anthropic’s early partners include the likes of Amplitude, Asana, Box, Canva, Clay, Figma, Hex, monday.com, and Slack. With the Box MCP App, for example, users will be able to search for files and preview documents inline in the chat experience — and then ask questions about those documents, too.

With the Slack app, meanwhile, users can use the AI model to write and edit message drafts and then post them to Slack. Among other things, it’s the MCP Apps framework that allows for the direct editing of these messages right in Claude.

![](https://cdn.thenewstack.io/media/2026/01/ee28fd87-slack-claude-mcp-app.gif)

The Slack MCP app (image credit: Slack).

“Enterprises need more from AI than powerful models. They also need a reliable way for those models to operate inside real business environments. By partnering with Anthropic, we are bringing Salesforce directly into our customers’ flow of work and providing the execution layer with context, data, governance, and trust,” says [Nick Johnston](https://www.linkedin.com/in/n1ckjohnston), SVP of Strategic Tech Partnerships at Salesforce in today’s announcement. “That’s what powers the Agentic Enterprise.”

Soon, Slack owner Salesforce will also bring its Agentforce, Data 360 and Customer 360 apps to Claude.

![](https://cdn.thenewstack.io/media/2026/01/3976b808-mcp-apps-asana.png)

The Asana MCP app (credit: Asana).

Some of the typical scenarios for using MCP Apps, which Anthropic first [proposed in November](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/), include interactive data exploration using dashboards, configuration wizards, document reviews and real-time monitoring.

At its core MCP Apps rely on tools that supply user interface metadata and the user interface resources (HTML and JavaScript) to render them.

## Building MCP Apps

![](https://cdn.thenewstack.io/media/2026/01/5006ec35-screenshot-2026-01-26-at-12.44.42.png)

The core primitives for defining MCP apps (credit: Anthropic).

Bringing this interactive UI experience to Claude and other chat-centric AI tools feels like a logical next step. Chat is, for better or worse, still the default way to interact with AI models, but for a while now, it has felt quite limited.

Anthropic isn’t the first one to think of this, of course. With its [Apps SDK](https://developers.openai.com/apps-sdk/), OpenAI offers a somewhat similar framework, which also uses MCP at its core. Anthropic notes that both the OpenAI Apps SDK and the open-source MCP-UI project (created by [Ido Salomon](https://github.com/idosal) and [Liad Yosef](https://github.com/liady)) pioneered many of these patterns.

“The projects proved that UI resources can and do fit naturally within the MCP ecosystem, with enterprises of all sizes adopting both the OpenAI and MCP-UI SDKs for production applications,” the Anthropic team writes.

And for the foreseeable future, developers who wrote [MCP-UI](https://mcpui.dev/) apps will be able to continue to do so.

“MCP Apps builds upon the foundations of MCP-UI and the ChatGPT Apps SDK to give people a rich, visually interactive experience,” says Nick Cooper, Member of Technical Staff, OpenAI. “We’re proud to support this new open standard and look forward to seeing what developers build with it as we grow the selection of apps available in ChatGPT.”

On the security front, Anthropic notes that it implemented a number of guardrails to ensure the third-party code you are running on your MCP host can break out of its sandbox. These include sandboxed iframes with restricted permissions, the ability of hosts to review the HTML content before rendering, auditable UI-to-host messages, and the fact that users have to give explicit approval for UI-initiated tool calls.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)