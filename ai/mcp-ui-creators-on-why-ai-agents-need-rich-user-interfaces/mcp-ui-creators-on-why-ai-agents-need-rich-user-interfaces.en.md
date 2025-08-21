[MCP-UI](https://mcpui.dev/) is a new open source project that provides a way to add web-based user interface components to AI agents. It builds on the already very popular [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP), which standardizes API access for agents.

MCP-UI could become a massive deal for the internet industry. To use professional sports terminology, MCP-UI has a very high ceiling because it may even [replace the need for websites](https://thenewstack.io/mcp-ui-aims-to-replace-old-world-websites-with-ai-agent-uis/) — at least for certain categories of online companies. It’s certainly a technology that web developers and web designers need to understand and assess now.

To find out more details about MCP-UI and how to get started with it, I spoke to its two creators, [Ido Salomon](https://www.linkedin.com/in/ido-salomon/) and [Liad Yosef](https://www.linkedin.com/in/liadyosef/). The pair have recently joined the enterprise IT company Monday.com, on deals [reportedly worth](https://www.calcalistech.com/ctechnews/article/rjorfh8wel) “several million dollars each.” Previously Salomon was a senior engineer at Palo Alto Networks and Yosef a senior engineer at Shopify (where MCP-UI has already been deployed).

Note: This article will focus purely on the open source project for MCP-UI, since Monday.com isn’t ready to discuss what they might do with the technology going forward. However, there will be a follow-up post soon in which I interview two Shopify engineers about how it implemented MCP-UI — Yosef will have some input into that, too.

[![Shopify MCP-UI](https://cdn.thenewstack.io/media/2025/08/c8bd46fd-shopifyblogimage_04dab3e7-5dbf-4887-bd50-062afb3bd8ae-1-scaled.webp)](https://cdn.thenewstack.io/media/2025/08/c8bd46fd-shopifyblogimage_04dab3e7-5dbf-4887-bd50-062afb3bd8ae-1-scaled.webp)

Shopify [MCP-UI example](https://shopify.engineering/mcp-ui-breaking-the-text-wall).

## Why Is MCP-UI Needed?

MCP-UI was launched on May 16, 2025 — just a few months ago — when Salomon released v1.0.1 [onto his GitHub account](https://github.com/idosal/mcp-ui/). I asked what the inspiration was for the project.

Firstly, Salomon replied, it was that most agentic interactions at that time were text-based. He then explained the two specific motivations to build MCP-UI.

“So the first motivation was, we need something that’s different — some UI interaction [in agents] more related to what we know today from web apps, that will make it more accessible to people.”

The second factor was to enable online companies to maintain their brand and user experience — their identity — in what Salomon called “this new world of agentic consumption.”

“So MCP-UI is kind of a way to handle both,” he added. “It’s both a way to add rich user interactions into this agentic flow, and [also] allow servers or applications to really maintain their own identity within this new world.”

> MCP-UI enables “a way to add rich user interactions into [an] agentic flow, and allow servers or applications to really maintain their own identity within this new world.”  
> **– Ido Salomon, MCP-UI co-creator**

Yosef noted that they had begun to see agents like ChatGPT and Claude generate some of their own UI — for example, images of hotels in ChatGPT if you search for accommodation — but that it wasn’t extensive enough. There were aspects of a visual UI missing.

“You have very complex user interactions, or user flows — like choosing a seat in an airplane, or a seat in a venue, or even […] a complex e-commerce flow — that you can’t expect every agent to generate on their own,” Yosef explained. “So, like Ido said, we needed a way to bridge this gap.”

## Iframe and Future Mobile Considerations

Currently, MCP-UI is for browser-based UIs, although the pair hopes to add native mobile tooling in due course. For now, a core feature of MCP-UI is its use of [<iframe>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe), an HTML element that embeds another HTML page within the current one. This seems to be mainly due to security. In the MCP-UI readme file on GitHub, it states: “In all content types, the remote code is executed in a sandboxed iframe.”

“I think it was kind of the only choice that was realistic technologically wise,” said Salomon, regarding iframe. “I think MCP-UI, at its core, is fairly simple. It basically takes the building blocks of MCP [the parent protocol] — MCP has a way to respond not just with text, but with an embedded resource that can be anything. So the idea was, how do I take something like an embedded resource, get some consensus around when this embedded resource contains something. Then the host — you know, ChatGPT, whatever — can render it. And how does it run basically arbitrary code, that is unsafe, without harming the users. Iframe is kind of the only way to do that. And sandbox iframe in particular gives you an extra edge.”

He added that there are also other content types — “like remote DOM and a bunch of other stuff” — that are more complex and have their own security models.

> “MCP has a way to respond not just with text, but with an embedded resource that can be anything.”  
> **– Salomon**

I asked whether they are thinking of implementations for different mobile OS, such as iOS and Android, so that (for example) the ChatGPT app can use MCP-UI?

“There definitely will be different implementations,” said Salomon. “I think in the web, it’s much simpler, because you’re much less constrained by the operating system and the actual underlying engine. So doing stuff like saying we embed iframes and can do whatever we want with the iframe is much easier. With mobile, you have a lot of different constraints.”

But he admitted that mobile OS implementations will be something the project needs — “because a lot of the world is going in a mobile direction for agents.”

That’s not all that needs to be added to MCP-UI. The project is still very new, so things like authorisation and theming are still being worked on.

[![MCP-UI demo](https://cdn.thenewstack.io/media/2025/07/3cf7bfe7-mcp-ui-demo.jpg)](https://cdn.thenewstack.io/media/2025/07/3cf7bfe7-mcp-ui-demo.jpg)

MCP-UI demo of a UI being inserted into a Claude 3.7 Sonnet chat.

## Components: HTML and React Options

There are two types of SDKs for MCP-UI: a client SDK and a server SDK to connect to MCP servers. The server SDK is currently only available in TypeScript and Ruby, but a Python version is in the works.

The client SDK provides “a React component and Web Component for easy frontend integration.” Shopify is using Web Components in its integration, but most others — such as [Goose](https://block.github.io/goose/blog/2025/08/11/mcp-ui-post-browser-world/) and [Postman](https://www.npmjs.com/package/@postman/mcp-ui-client) — are using React, say the pair.

“Actually, most use React, because React is kind of the de facto language of vibe coding,” said Salomon. “But yeah, Web Components is just to be on the safe side of enabling everyone, because that’s kind of the goal.”

> “MCP-UI can be consumed [on] the client side using React or Web Components.”  
> **– Liad Yosef, MCP-UI co-creator**

Yosef clarified that Shopify’s use case is slightly different to others.

“So, MCP-UI can be consumed [on] the client side using React or Web Components,” he said. “Shopify uses Web Components as the actual UI content that is being shipped, and that’s something that was existing in Shopify before this project started. So Shopify was developing some sort of Web Components to be used in third-party sites, and [so] they were the natural candidates to compose Shopify’s UI.”

As noted above, we’ll explore Shopify’s implementation more in the next post.

## Will Graphical Agents Replace Websites?

So now to the bigger questions, in terms of how MCP-UI might play out. I asked whether the pair see AI agents with embedded UIs replacing the need for certain online companies — e-commerce companies, for instance — to operate websites?

“Our future vision is that complex websites and complex web apps are going to be somewhat obsolete in the future,” replied Yosef. “We already see today with textual MCP tools, that people [who] connect their agents or assistants to some sort of MCP, they don’t browse the website itself, they just use it through MCP. So the more applications or services that will expose their interfaces using these fragmented parts [via MCP-UI], yeah, it’s gonna replace the full-blown experience of websites.”

> “…complex websites and complex web apps are going to be somewhat obsolete in the future.”  
> **– Yosef**

It’s hard not to see the appeal of MCP-UI for e-commerce businesses — and indeed any business that does transactions online. But what other types of organizations would benefit from using MCP-UI?

“I think definitely productivity,” replied Yosef (perhaps giving a hint as to why Monday.com recruited them for a large sum of money). “That’s something that we can already see, that people are using agents as assistants to increase their productivity. So connecting productivity tools that will allow you these rich user interfaces and being streamlined in your own chat experience.”

Salomon added that “a lot of things that today you need […] a lot of UI overhead, maybe, to consume in a certain way, become a lot easier once you can ask the agent, and have the agent bring you just what you need to consume at that time to make your decisions.”

## Getting Started

Developers should start experimenting with MCP-UI, to get a sense for how it could fit their own use cases.

There are two types of ways developers should think about using MCP-UI, Yosef explained. One is building your own custom agent using the client SDK, so that it supports MCP-UI. The other is to have your app be integrated in external agents, via the server SDK.

In the second use case, you’re “trying to chunk it [your app] to usable chunks that people can consume through ChatGPT or Claude or their own personal assistant,” said Yosef.

In either case, prepare for an internet where a lot more interactions will happen through agents. The web isn’t going away — it’s core to MCP-UI — but the way people transact and consume online is changing.

“MCP-only apps are coming,” claimed Yosef, suggesting that some companies are already looking beyond websites and smartphone apps. “We’ve heard it from actual companies, actually starting to think this way.”

To further explore, developers should check out [the project website](https://mcpui.dev/) for technical information and [join the Discord](https://discord.gg/CEAG4KW7ZH) to connect with the community.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)