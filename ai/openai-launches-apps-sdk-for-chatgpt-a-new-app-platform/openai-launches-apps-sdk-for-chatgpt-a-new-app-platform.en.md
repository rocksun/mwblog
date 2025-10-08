At its annual DevDay event, OpenAI announced [several initiatives for developers](https://thenewstack.io/openai-launches-a-no-code-agent-builder/) — who now number 4 million, according to the company. Of most interest was the new [Apps SDK](https://developers.openai.com/apps-sdk), which allows third-party developers to build web-based applications that run as interactive components inside ChatGPT conversations. OpenAI says it will “begin accepting app submissions for review and publication” later this year.

Yes, that’s right: it’s an application platform for ChatGPT. This has echoes of the great [smartphone app platform announcements of 2008](https://cybercultural.com/p/internet-2008/) — both iOS and Android. Arguably, given the enormous popularity of OpenAI and the chatbot user paradigm it pioneered, this is the first mainstream application platform with a genuine chance of rivaling those two smartphone app stores.

Intriguingly, the defining trait of Apps SDK is its web-based UI model. In fact, it’s quite similar to MCP-UI, which [I’ve looked at in-depth this year](https://thenewstack.io/mcp-ui-creators-on-why-ai-agents-need-rich-user-interfaces/). This makes it fundamentally different to both the iOS and Android app platforms, which are not web-based. But even though OpenAI’s App SDK sits a layer higher in the stack (ChatGPT itself has iOS, Android, and browser versions), it potentially has massive pulling power as an app-distribution platform.

Let’s make sure we understand the nuts and bolts first, before we get too carried away.

## Apps SDK: Web Components Inside a Sandbox

At its core, a ChatGPT app component is a web UI that runs in a sandboxed iframe inside a ChatGPT conversation. This is the same basic [paradigm that MCP-UI operates under](https://thenewstack.io/how-mcp-ui-powers-shopifys-new-commerce-widgets-in-agents/), except MCP-UI was designed to run inside any MCP-compliant agent — it’s [a protocol specification](https://thenewstack.io/mcp-ui-aims-to-replace-old-world-websites-with-ai-agent-uis/), not a single product. The Apps SDK, by contrast, is tightly coupled to ChatGPT itself.

[![Spotify in ChatGPT](https://cdn.thenewstack.io/media/2025/10/827023d9-openai-appssdk-spotify.jpg)](https://cdn.thenewstack.io/media/2025/10/827023d9-openai-appssdk-spotify.jpg)

Spotify in ChatGPT; via DevDay.

ChatGPT acts as the host of the app. You can think of a third-party ChatGPT app as a “mini web app” embedded directly into ChatGPT’s interface. The developer interacts with the window.openai component bridge that OpenAI [injects into the iframe](https://developers.openai.com/apps-sdk/reference/); this bridge lets the app’s frontend exchange data with the surrounding conversation and with its MCP server. To create an app using Apps SDK, you build ordinary web code — HTML, CSS, and JavaScript, which can be bundled with a modern framework like React or Vue — and ChatGPT renders it as an interactive card or panel within the chat thread.

When it [announced Apps SDK](https://developers.openai.com/apps-sdk), OpenAI noted that the system is built on the Model Context Protocol (MCP) but “extends MCP so developers can design both the logic and the interface of their apps.”

## How Does It Extend MCP?

Under the hood, Apps SDK uses the same MCP transport and tool-registration model that now powers external tool servers and aspects of [custom GPTs](https://thenewstack.io/getting-started-with-openais-gpt-builder-and-how-it-uses-rag/). MCP has become the connective tissue between all of OpenAI’s new extensibility layers, including the new Apps SDK.

The developer’s MCP server exposes tools (for server-side logic) and resources (for data endpoints or UI templates). Each tool can reference an output template — typically a URI pointing to the bundled HTML and JavaScript UI. When a user or the model triggers that tool, ChatGPT hydrates the web component with the tool’s structured output and any metadata attached.

Inside the iframe, the web app accesses this data through the host-provided window.openai interface. This creates a clean division of labor: the model reasons, the server executes, and the UI renders — a purely web-based, sandboxed, event-driven layer that ties the whole experience together.

## User Experience Guidelines

OpenAI’s [early documentation](https://developers.openai.com/apps-sdk/concepts/design-guidelines) emphasizes that embedded components should look and behave as if they’re native to ChatGPT. To achieve this, the company has introduced a set of UX guidelines and design constraints covering layout, color themes, typography, and accessibility. The aim is to make every third-party app feel cohesive within the chat environment rather than like a foreign webpage.

Developers are encouraged to respect ChatGPT’s layout boundaries, since components appear in cards with consistent margins, rounded corners, and light- or dark-theme awareness. Accessibility is also a core requirement: apps should rely on semantic HTML and ARIA attributes so that ChatGPT can maintain keyboard navigation and screen-reader compatibility.

There are other constraints, but the key is that developers build their apps with familiar web technology. The idea is to encourage an ecosystem of small, visually consistent interactive cards — maps, calendars, music playlists, document viewers, and more — that feel native to ChatGPT. Users can summon them directly by name or encounter them as contextual suggestions generated by the model. In the current preview, early partners like Spotify, Canva and Zillow demonstrate what these embedded web experiences look like in practice.

## Comparison: Apps SDK vs. MCP-UI

As noted earlier, MCP-UI is a protocol that allows developers to integrate web views inside multiple AI chat platforms, not just ChatGPT. In theory, an app developer could build a standalone browser-based application and then expose it via MCP-UI so that any compliant agent — including ChatGPT — can interact with it.

[![](https://cdn.thenewstack.io/media/2025/10/1d547a7a-devday25-webui.jpg)](https://cdn.thenewstack.io/media/2025/10/1d547a7a-devday25-webui.jpg)

Example of Coursera app inside ChatGPT; via DevDay.

The trade-offs here are familiar to anyone who followed the platform debates of the late 2000s. MCP-UI aims for cross-host portability, providing a single component specification that any agent can render using its own host-side renderer. Apps SDK, by contrast, prioritizes tight integration with ChatGPT’s product. Developers who want one consistent experience across several agent shells might gravitate toward MCP-UI, while those focused on ChatGPT’s vast user base — and who want first-party polish such as [Pulse cards](https://openai.com/index/introducing-chatgpt-pulse/), shared projects, or [Instant Checkout](https://openai.com/index/buy-it-in-chatgpt/) — will likely choose Apps SDK as the shortest path.

In some ways, this debate resembles the one from the early smartphone era: why build an app that only targets one company’s platform (say Apple’s iOS) when the web itself is supposed to be a universal platform? Facebook initially took the web’s side, [building an HTML5 web app](https://cybercultural.com/p/049-rww-mobile-summit-may2010/) it hoped both iPhone and Android users would adopt. But in the end, it capitulated and developed separate native apps, because at that time the native experience was better.

Today, ChatGPT has a gravitational pull similar to Apple and Google in 2008. Its huge user base and the growing acceptance of chat-based interfaces make it a compelling application platform. Yet in a curious inversion of history, OpenAI has flipped the paradigm: the most dynamic new app platform isn’t a native mobile OS, but an AI host rendering mini-apps built with web technology.

In other words, if you’re a third-party developer building an AI app, then you don’t necessarily need to worry about building for native platforms. Instead, you can simply build a web app that interfaces through MCP and runs inside ChatGPT. That’s certainly what OpenAI would like you to do.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)