Webpages and websites are increasingly seen as “[old world UIs](https://x.com/liadyosef/status/1949482482123817041)” to proponents of AI agents and the [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP). This week, in a presentation at Microsoft’s MCP Dev Days entitled “[The Future of User Interaction](https://www.youtube.com/watch?v=gDSIxIGYk-o),” Kent C. Dodd even went as far as to say that “we’re entering a new phase where, instead of web browsers and websites, we’re going to have Jarvis clients [a reference to AI agents] and MCP servers.”

To be clear, there’s no suggestion that web technology itself is going away. The current thinking is: AI agents will continue to use the web as the interface layer for end-users. But instead of using “old world” websites, we’ll be using [new chat-based AI browsers](https://thenewstack.io/ai-browsers-dias-chat-based-ui-and-the-future-of-the-web/) — currently in development by the likes of OpenAI and Perplexity — or other programming methods to inject a UI into an AI agent process. The latter is where a project called MCP-UI comes in.

[MCP-UI](https://mcpui.dev/) lets developers create interactive UI components for MCP. [The project](https://mcpui.dev/guide/introduction) “aims to standardize how models and tools can request the display of rich HTML interfaces within a client application.” Put that way, it’s not dissimilar to how smartphone platforms like iOS and Android allow developers to create a [WebView](https://en.wikipedia.org/wiki/WebView) inside an app.

> MCP-UI: “rich, dynamic user interfaces for your MCP applications”

More specifically, MCP-UI enables “rich, dynamic user interfaces for your MCP applications.” So far it offers SDKs for TypeScript and Ruby.

The project is still brand new and experimental, but the philosophy behind it is well aligned with the [rapid rise in popularity of MCP](https://thenewstack.io/google-embraces-mcp/) — now the default way for AI models to gather external information. “Allowing MCP servers to respond with UI snippets is a powerful way to create interactive experiences in hosts,” [states the MCP-UI project](https://mcpui.dev/guide/introduction).

In his presentation at Microsoft’s MCP event this week, Kent Dodd highlighted MCP-UI (which is how I first came across the project). Dodd showed an e-commerce demo of MCP-UI being used to display a user interface inside VS Code.

[![MCP-UI](https://cdn.thenewstack.io/media/2025/07/9abf9ce1-mcp-ui-kentdodds.jpg)](https://cdn.thenewstack.io/media/2025/07/9abf9ce1-mcp-ui-kentdodds.jpg)

Kent Dodd showing MCP-UI in action.

“This is the future of user interaction, right here,” Dodd said. “You’re no longer going to have a website that users go directly to, or anything like that. Now we are going to be interacting with a UI, still, but it’s going to be in the context of our AI agent that’s going to solve these problems for us. And I just love that.”

## More About the MCP-UI Project

MCP-UI was created by two Israeli developers, [Liad Yosef](https://www.linkedin.com/in/liadyosef/) and [Ido Salomon](https://www.linkedin.com/in/ido-salomon/), who just this week [got recruited](https://www.calcalistech.com/ctechnews/article/rjorfh8wel) by enterprise IT company Monday.com for “several million dollars each” — another sign of an extremely well-heated market for top AI talent. At the time of writing, Yosef still lists himself on LinkedIn as a senior software engineer at Shopify, while Saloman lists himself as a cloud architect at Palo Alto Networks.

MCP-UI is an open source project — it has an Apache-2.0 license according to the GitHub project page — so it doesn’t appear to be part of the Monday.com deal. But it’ll be interesting to see if it becomes more corporate-leaning now that the two creators work for the same company.

So where did MCP-UI come from? It seems to have derived from a community project called the [MCP Community Working Group](https://modelcontextprotocol-community.github.io/working-groups/index.html). The two people [leading that working group](https://github.com/orgs/modelcontextprotocol-community/people), Ola Hungerford and Tadas Antanavicius, are both [maintainers in the official MCP project](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md). So there are ties back to the main MCP project, created, of course, by Anthropic.

[![MCP-UI demo](https://cdn.thenewstack.io/media/2025/07/3cf7bfe7-mcp-ui-demo.jpg)](https://cdn.thenewstack.io/media/2025/07/3cf7bfe7-mcp-ui-demo.jpg)

MCP-UI demo of a UI being inserted into a Claude 3.7 Sonnet chat.

The “old world UIs” comment I referred to at the top of this post came from none other than Liad Yosef. To be 100% fair to him, here’s the full quote in context (pun intended):

*“In the near term we will see more and more tools like NLWeb, browser rendering and browser agents that will try to automate using the “old world” UIs, which are originally meant for humans.* *This makes sense as it immediately bridges the gap between AI capabilities and existing UI.* *The smart bet for the future will be on reversing this flow – turning these services to be MCP-first, LLM-consumable, and having a very lean human UI built \*on top\* of that.* *Services that will quickly expose themselves in this “reverse” way will benefit from an immediate and great agent compatibility, while still catering for the (gradually decreasing) traffic of human visitors.”*

NLWeb, by the way, is a Microsoft project [announced in May](https://news.microsoft.com/source/features/company-news/introducing-nlweb-bringing-conversational-interfaces-directly-to-the-web/), that aims “to be the fastest and easiest way to effectively turn your website into an AI app, allowing users to query the contents of the site by directly using natural language, just like with an AI assistant or Copilot.”

Now, when I first read this tweet by Yosef, I did cringe at the apparent dismissal of the human-centered web. Unfortunately, this is a common sentiment on X (formerly Twitter), where AI hype runs rampant. But after more consideration, I do take Yosef’s point that AI agents need a better way to present user interfaces to the end-user (we humans).

Google Chrome senior engineer Paul Kinlan has made a similar point in his recent blog posts on this topic. In a post about “super-apps,” [Kinlan posited](https://aifoc.us/super-apps/) that in the near future you could get dynamically generated UI from prompts to an LLM or chatbot. He says that web technologies are best positioned to power these new user interfaces: “HTML, CSS and JavaScript are the most expressive languages available today to render a UI and LLMs are pretty good today at generating them…”

## UIs Coming to an Agent Near You

It’s already common for AI agents to browse the web as part of their information-gathering process; so-called [headless browsers](https://thenewstack.io/why-headless-browsers-are-a-key-technology-for-ai-agents/), like Browserbase, are used for that. From my own experience as an OpenAI user, you can actually watch its o3 model “think” while it browses websites in the background — website domains flash up while you wait for your result.

[![OpenAI searching the web](https://cdn.thenewstack.io/media/2025/07/cd539bc4-openai-o3-searchweb.jpg)](https://cdn.thenewstack.io/media/2025/07/cd539bc4-openai-o3-searchweb.jpg)

OpenAI searching the web.

But having custom web UIs generated as part of an AI agent’s **output** to you is a relatively new field that the community is exploring. I agree with Dodd that MCP-UI is an exciting project to track in this regard.

Although I’m deeply concerned about [what AI technology is doing to the human web](https://thenewstack.io/is-ai-the-ultimate-version-of-google-as-larry-page-wanted/) — ravaging it, basically — I can at least rest assured that web technology is still a core part of the internet’s AI future.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)