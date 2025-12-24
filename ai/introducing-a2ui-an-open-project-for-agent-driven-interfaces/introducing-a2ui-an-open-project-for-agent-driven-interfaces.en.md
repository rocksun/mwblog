![Train a GPT2 model with JAX on TPU for free](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/train-gpt2-model-with-jax-on-tpu-banner.original.png)

Generative AI does great at generating text, images, and code. Now, it’s time for it to be used to generate contextually relevant **interfaces**. Today we are making the [A2UI](https://github.com/google/A2UI/) project public so we can collaborate with others on this early stage *format* and *implementations*. A2UI was designed to address the specific challenges of interoperable, cross-platform, generative or template-based UI responses from agents. A2UI allows agents to generate the interface which best suits the current conversation with the agent, and send it to a front end application. We have been building A2UI for some of our products, and we would like to engage with the community to help refine the A2UI specifications, add more transports, and add more client renderers and integrations.

**A2UI** is an open-source project, complete with a format optimized for representing updateable, agent-generated UIs and an initial set of renderers**,** that allows agents to generate or populate rich user interfaces, so they can be displayed in different host applications, rendered by a range of UI frameworks such as Lit, Angular, or Flutter (with more to come). Renderers support a set of common components and/or a client advertised set of custom components which are composed into layouts. The client owns the rendering and can integrate it seamlessly into their branded UX. Orchestrator agents and remote A2A subagents can all generate UI layouts which are securely passed as messages, not as executable code.

Below are examples of A2UI rendered cards, showing a variety of UI compositions that A2UI can achieve.

![a2ui-blog-1-component-gallery (2)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/a2ui-blog-1-component-gallery_2.original.png)

## **The Problem: Agents need to** ***speak*** **UI**

Imagine an agent designed to help you book a table at a restaurant. A text-only interaction might involve a clunky back-and-forth:

**User:** (typing) "Book a table for 2."

**Agent:** "Okay, for what day?"

**User:** (typing) "Tomorrow."

**Agent:** "What time?"

**User:** (typing) "Maybe 7p"

**Agent:** "We do not have reservation availability then, any other times?

**User:** (typing) "When do you have reservations?"

**Agent:** "We have availability at 5:00, 5:30, 6:00, 8:30, 9:00, 9:30 and 10:00, Do any of those work for you?”

This can be slow and inefficient. A better experience would be for the **agent to quickly generate, or use,** a simple form with a date picker, a time selector, and a submit button. With A2UI, LLMs can compose bespoke UIs from a catalog of widgets to provide a graphical, beautiful, easy to use interface for the exact task at hand.

For example, instead of the text-based chat back and forth above, you can use A2UI to compose this reservation UI. The below is one possible rendering of an A2UI representation of the restaurant booking, with many other possibilities thanks to A2UI's design that gives the front-end host app a lot of control over the styling.

![a2ui-blog-2-reserve-table](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/a2ui-blog-2-reserve-table.original.png)

## **The challenge: Rendering across trust boundaries**

We are entering the era of the multi-agent mesh. Agents from Google are talking to agents from Cisco, IBM, SAP, and Salesforce to solve complex tasks. This is why we collectively created the [Agent-to-Agent (A2A) Protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) and donated it to the Linux Foundation: to enable agents to collaborate even when they don’t share memory, tools, or context.

However, this decentralization creates a user interface problem.

If your agent lives inside your application, it can directly manipulate the view layer (e.g. DOM). But in a multi-agent world, the agent doing the work is often remote—running in the background, on a different server, or owned by a different organization. It cannot touch your UI directly; it must send messages.

Historically, rendering UI from a remote, untrusted source meant sending HTML or JavaScript and sandboxing it inside **iframes**. This approach is heavy, can be visually disjointed (it rarely matches your app's native styling), and introduces complexity around security boundaries.

We needed a way to transmit UI that is **safe like data, but expressive like code**.

## **The solution: UI spec as a sequence of messages**

A2UI provides a standard format which can be generated on the fly as structured output, or used as a template and hydrated with values. The agent generating this response might be a remote A2A agent or the orchestrator the user is interacting with. The JSON payload can be sent to the client over A2A, AG UI, and potentially other transports. The client application renders using its own native UI components. This means **the client retains full control over styling and security**, helping to ensure the agent's output always feels native to your app.

[![


Sorry, your browser doesn't support playback for this video

](https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/wagtailvideo-xof9cc58_thumb.jpg)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/landscape-architect-demo.mp4)

In this example, the user uploads a photo, and a remote agent uses Gemini to understand it and makes a bespoke form for the specific needs of the landscaping customer

[![


Sorry, your browser doesn't support playback for this video

](https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/wagtailvideo-l_1uca6i_thumb.jpg)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/a2ui-custom-compnent.mp4)

In this example, the agent decides to respond with a custom component containing an interactive chart and a custom component containing Google Maps.

## **Core philosophy: Secure, updateable, and decoupled**

We designed A2UI around a few key principles:

* **Security first:** Running arbitrary code generated by an LLM may present a significant security risk. A2UI is a *declarative* data format, not executable code. Your client application maintains a "catalog" of trusted, pre-approved UI components (e.g., `Card`, `Button`, `TextField`), and the agent can only request to render components from that catalog. This helps you to reduce the risk of UI injection and other vulnerabilities.
* **LLM-friendly and incrementally updateable:** The UI is represented as a flat list of components with ID references which is easy for LLMs to generate incrementally, allowing for progressive rendering and a responsive user experience. An agent can efficiently make incremental changes to the UI based on new user requests as the conversation progresses.
* **Framework-agnostic and portable:** A2UI separates the UI *structure* from the UI *implementation*. The agent sends a description of the component tree and its associated data model. Your client application is responsible for mapping these abstract descriptions to its native widgets—be it web components, Flutter widgets, React components, SwiftUI views or something else entirely. The same A2UI JSON payload from an agent can be rendered on multiple different clients built on top of different frameworks.

![a2ui-blog-3-end-to-end-data-flow](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/a2ui-blog-3-end-to-end-data-flow.original.png)

## **Navigating the agentic UI ecosystem**

The space for agentic UI is evolving rapidly, with excellent tools emerging to solve different parts of the stack. We view A2UI not as a replacement for these frameworks, but as a specialized protocol that aims to solve the specific problem of **interoperable, cross-platform, generative or template-based responses.**

To help you choose the right tool, or combination of tools, here is how we map the landscape:

**1. Building the "host" application UI**

If you are building a full-stack application (the "host" UI that the user interacts with), in addition to building the actual UI, you may also utilize a framework **(AG UI, Vercel AI SDK, GenUI SDK for Flutter which already uses A2UI under the covers)** to handle the "pipes": state synchronization, chat history, and input handling.

* **Where A2UI can fit:** A2UI is complementary. If you connect your host application using AG UI, it can use A2UI as the data format for rendering responses from the host agent and also from third-party or remote agents. This gives you the best of both worlds: a rich, stateful host app that can safely render content from external agents it doesn't control.
* **A2UI with A2A:** You can send via A2A directly to a client front end.
* **A2UI with AG UI:** AG UI provides scaffolding to easily build and deploy applications that support A2UI.
* **A2UI with REST** and other transports are feasible but not yet available.

**2. UI as a "resource" (MCP apps)**

The **Model Context Protocol (MCP)** has [recently introduced **MCP Apps**](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/), a new standard consolidating work from MCP-UI and OpenAI to enable servers to provide interactive interfaces. This approach treats UI as a resource (accessed via a `ui:// URI`) that tools can return, typically rendering pre-built HTML content within a sandboxed `iframe` to ensure isolation and security.

**How A2UI is different:** A2UI takes a "native-first" approach that is distinct from the resource-fetching model of MCP Apps. Instead of retrieving an opaque payload to display in a sandbox, an A2UI agent sends a blueprint of native components. This allows the UI to inherit the host app's styling and accessibility features perfectly. In a multi-agent system, an orchestrator agent can easily understand the lightweight A2UI message content from a subagent, allowing for more fluid collaboration between agents.

**3. Platform-specific ecosystems (OpenAI ChatKit)**

Tools like **ChatKit** offer a highly integrated, optimized experience for deploying agents specifically within the OpenAI ecosystem.

**How A2UI is different:** A2UI is designed for developers building their own agentic surfaces across Web, Flutter, and native mobile, or for enterprise meshes (like **A2A**) where agents need to communicate across trust boundaries. A2UI gives the client more control over styling at the expense of the agent, in order to allow for greater visual consistency with the host client application.

## **Built for the real world**

From day one, A2UI has been developed in partnership with several teams inside and outside of Google to solve real-world problems. We're thrilled to build with support from key collaborators:

**AG UI / CopilotKit: A powerful combination**

We believe in a collaborative ecosystem. The team behind [AG UI](https://ag-ui.com/) / [CopilotKit](https://www.copilotkit.ai/) has worked with us to ensure day-zero compatibility, offering developers a powerful "better together" story.

> *"The Agent-User Interaction Protocol (AG-UI) connects agentic backends and agentic frontends. It provides developers with practical building blocks for building rich fullstack agentic applications. AG-UI fully supports the A2UI spec for rich declarative generative UIs dynamically generated by agents. AG-UI also implements a full handshake with A2A protocol, for seamless full-featured integration with any A2A system. We're excited to provide day-0 compatibility between AG-UI and A2UI."* — Atai Barkai, Founder of CopilotKit and AG UI

**Opal: Powering experimental AI mini-apps**

[Opal](http://opal.google/) lets hundreds of thousands of people build, edit, and share AI mini-apps using natural language. The Opal team at Google has been a core contributor to A2UI. In addition to helping build A2UI, the team has also been using it to **rapidly prototype** and integrate it into the core app building flow. A2UI in Opal will enable anyone to build AI mini-apps with dynamic, generative UI custom for each use case. In the next few weeks, you’ll be able to see and experience A2UI in action in Opal.

> *"A2UI is foundational to our work. It gives us the flexibility to let the AI drive the user experience in novel ways, without being constrained by a fixed front-end. Its declarative nature and focus on security allow us to experiment quickly and safely."* — Dimitri Glazkov, Principal Engineer, Opal Team

**Gemini Enterprise: Custom UIs for enterprise agents**

Gemini Enterprise enables businesses to build powerful, custom AI agents. A2UI is being integrated to allow these enterprise agents to render rich, interactive UIs within their host applications.

> *"Our customers need their agents to do more than just answer questions; they need them to guide employees through complex workflows. A2UI will allow developers building on Gemini Enterprise to have their agents generate the dynamic, custom UIs needed for any task, from data entry forms to approval dashboards, dramatically accelerating workflow automation."* — Fred Jabbour, Product Manager, Gemini Enterprise

**Flutter: Multi-platform Generative UI app experiences**

[Flutter](http://flutter.dev/) and its [GenUI SDK](https://github.com/flutter/genui) helps you generate dynamic, personalized UI with Gemini (or other LLMs) to significantly improve the usability and satisfaction of your GenAI and agent-based user experiences. These generative UIs adhere to your established brand guidelines and use your own widget catalog. A2UI is used by GenUI SDK as the UI declaration format between remote server-side agents and the app.

> *"Our developers choose Flutter because it lets them quickly create expressive, brand-rich, custom design systems that feel great on every platform. A2UI was a great fit for Flutter's GenUI SDK because it ensures that every user, on every platform, gets a high quality native feeling experience."* — Vijay Menon, Engineering Director, Dart

**AI Powered Google: Standardizing Agentic UI**

As Google adopts AI across the company, A2UI gives teams a standardized way for AI agents to exchange user interfaces, not just text. This interoperability allows agents to render on any frontend, supports workflows involving multiple agents per surface or multiple surfaces per agent, and enables internally built agents to be easily exposed externally, such as in Gemini Enterprise.

> *"Much like A2A lets any agent talk to another agent regardless of platform, A2UI standardizes the user interface layer and supports remote agent use cases through an orchestrator. This has been incredibly powerful for internal teams, allowing them to rapidly develop agents where rich user interfaces are the norm, not the exception. As Google pushes further into generative UI, A2UI provides a perfect platform for server-driven UI that renders on any client."* — James Wren, Senior Staff Engineer, AI Powered Google

## **Get started: Try out A2UI**

The best way to understand A2UI is to see it in action.

* Start by going to [a2ui.org](http://a2ui.org/) and reading the quickstart guide and documentation.
* Next go to the samples folder and try a client UI and some background sample agents, perhaps the restaurant finder.

Here’s how to launch the restaurant finder:

```
git clone https://github.com/google/A2UI.git
export GEMINI_API_KEY="your_gemini_api_key"


cd A2UI/samples/agent/adk/restaurant_finder
uv run .


cd A2UI/samples/client/lit/shell
npm install
npm run dev
```

Shell

Another way to see A2UI in action is to try the GenUI SDK for Flutter.

The GenUI SDK for Flutter uses A2UI under the covers when talking to remote or server-side agents. It's easy to get started, visit <https://docs.flutter.dev/ai/genui> or watch the [Getting started with GenUI video](https://www.youtube.com/watch?v=nWr6eZKM6no). In the GenUI SDK repo on GitHub, you can also find a [client-server sample that uses A2UI](https://github.com/flutter/genui/tree/main/examples/verdure).

CopilotKit has a public [A2UI Widget Builder](https://go.copilotkit.ai/A2UI-widget-builder) to try out as well.

## **Supported integrations**

Here are a few key integrations that the project has today, and some that we hope the project supports in the future. We welcome community contributions in these areas.

![a2ui-blog-4-checklist](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/a2ui-blog-4-checklist.original.png)

## **The future is open: Join us!**

Today marks the first public milestone of A2UI. Our format is currently at `v0.8` because we have been through many rounds of battle hardening and testing for the initial use cases, and there is more to evolve and discover. We have early, but working, client libraries for **Flutter,** **Web Components** and **Angular**.

With the project now open, we are excited to work with the ecosystem to:

* Refine and evolve the format
* Connect A2UI into your favorite client libraries
* Build more robust and useful tools in the future
* Contribute to developer onboarding and provide samples

A2UI is an Apache 2 licensed project, and we believe its success depends on the community. We invite you to explore the code, try the demos, and especially to contribute. Whether you want to build a client for your favorite UI framework, add support to an agent-building library, or build a sweet demo, we want to hear from you and collaborate with you.

Check out our public roadmap to see where we're headed and find out how you can get involved. Let's build the future of agentic user experiences together.