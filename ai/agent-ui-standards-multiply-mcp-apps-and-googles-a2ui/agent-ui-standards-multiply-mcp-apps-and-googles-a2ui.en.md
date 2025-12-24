This week, [Google](https://cloud.google.com/?utm_content=inline+mention) [launched A2UI](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/), an open source project to help developers build “agentic user interfaces.” It’s the latest in what’s becoming a regular release cycle of new standards and protocols for building a [user interface in AI agents](https://thenewstack.io/web-development-in-2025-ais-react-bias-vs-native-web/) and chatbots.

First, there was [MCP-UI](https://thenewstack.io/mcp-ui-creators-on-why-ai-agents-need-rich-user-interfaces/), a Model Context Protocol (MCP) ecosystem project closely aligned with Anthropic and [used by Shopify](https://thenewstack.io/how-mcp-ui-powers-shopifys-new-commerce-widgets-in-agents/) (amongst others). Soon after, [OpenAI launched Apps SDK](https://thenewstack.io/openai-launches-apps-sdk-for-chatgpt-a-new-app-platform/), along with AgentKit and other UI tooling. Then, just last month, [MCP Apps was announced](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/) — a proposed open standard “for interactive user interfaces in the Model Context Protocol,” which is being supported by both Anthropic and OpenAI.

## What Is A2UI? A Cross-Platform, Native-First Approach

So what is Google bringing to the table with A2UI that doesn’t already exist from the flurry of other agentic UI projects? In the launch blog post, Google states that “A2UI was designed to address the specific challenges of interoperable, cross-platform, generative or template-based UI responses from agents.”

The term “cross-platform” is a big clue — this isn’t a web-centric approach, which MCP-UI and OpenAI have largely taken so far by relying on sandboxed iframes. Instead, A2UI takes what [Google’s Minko Gechev calls](https://www.linkedin.com/posts/mgechev_introducing-a2ui-an-open-project-for-agent-driven-activity-7406409944146554882-c_sq?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAAJc5gB1iiLngl5c8J7iqyPa5uC2oX1J-U) a “native-first” approach. Gechev described this as “declarative, not executable,” adding that AI agents “send a description of UI components, not code.”

Currently, A2UI has client libraries for Flutter, Web Components and Angular. But this will probably be extended to other libraries over time. The idea is for an agent to declare what it should look like on a receiving app (e.g., a chatbot), and native libraries will be used to generate the user interface. As the A2UI launch post explains:

“A2UI separates the UI structure from the UI implementation. The agent sends a description of the component tree and its associated data model. Your client application is responsible for mapping these abstract descriptions to its native widgets — be it web components, Flutter widgets, React components, SwiftUI views or something else entirely.”

Gechev also explained that A2UI is built for streaming. “Using a JSONL-based format, A2UI enables progressive rendering so users see results instantly as the agent ‘thinks,’” he wrote.

## Understanding OpenAI’s Web-Centric UI Strategy

There is some jostling for positioning going on in the emerging field of “agent development.” OpenAI, in particular, has its fingers in a bunch of pies (cue a joke about six-fingered AI-generated images).

Currently, OpenAI is putting most of its effort into trying to make ChatGPT into an application platform, where apps will be web widgets rendered in sandboxed surfaces (typically iframes). Just this week, OpenAI announced that developers can now [submit apps to ChatGPT](https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/).

However, OpenAI has also recently [entered the web browser market](https://webtechnology.news/a-new-web-browser-from-openai-initial-reactions-to-atlas/), with Atlas. And it may well get into the smartphone business — or some other hardware device — at some point, too. Earlier this month, I interviewed [Adam Shea](https://www.linkedin.com/in/adam-shea-a1850484/), director of engineering at TELUS Digital, [who told me](https://thenewstack.io/why-capability-driven-protocols-are-key-for-chatgpt-apps/), “I have a hunch that the way we build ChatGPT apps today shares some core ideas and structure with the potential smartphone platform OpenAI has been rumored to be launching in the future.”

While OpenAI seems to be covering all bases, it is focused on web technologies in its Apps SDK and (obviously) in Atlas. Which makes its approach different from Google, which is going for cross-platform reach with A2UI.

## MCP Apps vs. A2UI: Key Differences Explained

It’s also noteworthy that OpenAI is a contributor to the [MCP Apps](https://github.com/modelcontextprotocol/ext-apps?tab=readme-ov-file#readme) project, which derives from both the MCP-UI project (created by [Ido Salomon](https://www.linkedin.com/in/ido-salomon/) and [Liad Yosef](https://www.linkedin.com/in/liadyosef/), who both now work for Monday.com) and OpenAI’s Apps SDK. The company that birthed MCP, Anthropic, is also heavily involved in this project.

MCP Apps Extension (SEP-1865), to give its full name, was [launched last month](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/) on the official MCP blog. It aims to “standardize support for interactive user interfaces in the Model Context Protocol.”

Currently, MCP Apps takes an explicitly web-based approach, using the iframe sandboxing that both MCP-UI and Apps SDK support. As the launch post put it, “all UI content runs in sandboxed iframes with restricted permissions.”

In its A2UI launch post, Google emphasized that its “native-first” approach differs from MCP Apps. “Instead of retrieving an opaque payload to display in a sandbox, an A2UI agent sends a blueprint of native components,” it explained. The key point here is that the “blueprint” sent via A2UI might be used to generate web code, native mobile UI or desktop application components.

## Emerging Agent Development Frameworks

There’s been a lot of different pieces released this year to help developers build agents or connect their apps to agents. Google alluded to this in its A2UI launch post, noting that in addition to building a UI, “you may also utilize a framework (AG UI, Vercel AI SDK, GenUI SDK for Flutter, which already uses A2UI under the covers) to handle the ‘pipes.’”

As well as the plethora of acronyms, it’s also confusing sometimes as to who makes what. [AG UI](https://www.copilotkit.ai/ag-ui) (Agent-User Interaction), it turns out, is an interaction protocol from a Seattle-based company called [CopilotKit](https://www.copilotkit.ai/) — which provides tooling that implements AG UI. It also now supports A2UI.

And I haven’t even mentioned Google’s Agent2Agent Protocol (A2A) yet! A2A operates at the agent-to-agent coordination layer, rather than the UI layer.

The point is, there are a lot of different technologies developers have to wade through currently before they figure out how to build and connect an agent. Hopefully, in 2026, all of this will become clearer.

But for UI at least, there are now two fairly clear approaches: Build a mini web app (favored by OpenAI and Anthropic, and now supported by MCP Apps) or take a “native-first” approach with Google’s A2UI.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)