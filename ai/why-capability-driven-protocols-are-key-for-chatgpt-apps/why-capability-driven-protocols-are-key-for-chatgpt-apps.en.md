OpenAI’s [Apps SDK launched in early October](https://thenewstack.io/openai-launches-apps-sdk-for-chatgpt-a-new-app-platform/), enabling developers to build mini web apps for ChatGPT. While we haven’t yet seen the promised ChatGPT app store, third-party developers have already begun to experiment with the SDK. For instance, TELUS Digital has built a proof-of-concept ChatGPT app, “a stock and news tracker with market data, interactive visualizations and custom UI components.”

[Adam Shea](https://www.linkedin.com/in/adam-shea-a1850484/), director of engineering at TELUS Digital, shared his thoughts about ChatGPT apps via an email interview.

## Choosing React for ChatGPT App Development

To reiterate, ChatGPT apps are basically web-based applications that run inside ChatGPT conversations. Which means all the benefits of modern web development are available to developers — including the ability to use powerful JavaScript or web native techniques. As Shea noted in [a technical blog post](https://www.telusdigital.com/insights/data-and-ai/article/building-chatgpt-apps), “one of the most significant advantages of the Apps SDK is support for modern component-based development.”

In my initial post about Apps SDK in October, I noted that there are two main component approaches available: using [React](https://thenewstack.io/remix-takes-on-next-js-in-battle-of-the-react-frameworks/), or using native [Web Components](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/). In TELUS Digital’s case, they opted to use React. I asked Shea why they went that direction.

“We used React primarily due to our team’s familiarity and its robust ecosystem,” he replied. “For enterprise applications, I’d suggest React is often the pragmatic choice, especially if your team already has React expertise and existing component libraries to leverage. I think the best option really depends on your team’s skills and existing tech stack.”

## Understanding MCP and Capability-Driven Protocols

One of the insights TELUS Digital learned while building a ChatGPT app is that MCP servers aren’t just API endpoints. “MCP [Model Context Protocol] represents a shift from request-response APIs to capability-driven protocols,” wrote Shea in the blog post.

This seems like it would require a lot of testing, especially if you’re creating a ChatGPT version of an enterprise application. For example, you’d want to make sure the AI response is not a [hallucination](https://thenewstack.io/stopping-ai-hallucinations-for-enterprise-is-key-for-vectara/). I asked Shea how enterprise developers can adapt to this new “capability-driven” mindset. Do testing and observability become even more important now?

> “For enterprise-scaled applications, you would want some way that can validate the model’s output against its input…”  
> **– Adam Shea, director of engineering, TELUS Digital**

“Great question. Because the LLM is mostly restating whatever it receives from the MCP, the real focus becomes ensuring that the data you send it is accurate, complete, and structured for the experience you want to deliver,” he replied. “For enterprise-scaled applications, you would want some way that can validate the model’s output against its input so we know the data hasn’t changed.”

He mentioned [Fuel iX Fortify](https://www.fuelix.ai/products/fuel-fortify), an AI platform co-owned by TELUS Digital and its parent company, TELUS (a Canadian conglomerate). Shea said this tool provides “automated testing and vulnerability assessments” to help enterprises run AI apps.

## AI Frameworks and Alternatives to ChatGPT Apps

I recently spoke to Vercel’s Andrew Qu about its [use of Next.js to build ChatGPT apps](https://thenewstack.io/next-js-in-chatgpt-vercel-brings-the-dynamic-web-to-ai-chat/). So I asked Shea whether they have used any of the new Vercel tooling and, if so, what his initial impressions were. And if they haven’t tried it, what are his thoughts on the possible emergence of frameworks for building ChatGPT apps (or indeed any AI assistant app)?

“I haven’t had a chance to check out their ChatGPT app-based tooling yet, but as ChatGPT app adoption increases and the SDK continues to evolve, there will undoubtedly be ways to streamline the build, test, and deployment process,” he said, adding that he’s a fan of Vercel’s tooling and various integrations with other products.

Shea also noted that the review process for getting a ChatGPT app approved is largely manual and involves working with OpenAI directly. But he expects that will soon change.

“I would imagine that as the platform gains more structure, it should become possible to create tooling that automates the full build, test, and deploy workflow, just like in iOS and Android ecosystems.”

In my October post, I too compared the upcoming ChatGPT app store to iOS and Android ecosystems, but it’s worth noting that there are potential open source alternatives to ChatGPT apps. I’ve [covered MCP-UI in-depth this year](https://thenewstack.io/mcp-ui-creators-on-why-ai-agents-need-rich-user-interfaces/) (it came out before the Apps SDK), because it offers a way to embed mini web apps inside of *any* AI assistant — including ChatGPT. I asked Shea for his thoughts on [MCP-UI](https://thenewstack.io/mcp-ui-aims-to-replace-old-world-websites-with-ai-agent-uis/).

“I haven’t used it yet, but internally we’ve tried some PoCs [Proof of concepts] with it for a separate initiative. It’s an interesting parallel path to ChatGPT apps. With OpenAI putting their support behind ChatGPT apps, I think there’s going to be significant demand to support that approach. I could see the two coexisting for a while as the ecosystem matures. The comparison is less from a technical perspective and more from which platform and users you want to target.”

## What Types of Apps Are Suitable for ChatGPT?

So what types of enterprise apps does Shea think will be most suitable for putting into ChatGPT, as either a complementary app or maybe even as a full replacement of an existing smartphone app?

“The last two years have largely been about layering generative AI onto the apps people already use,” he replied. “The new ChatGPT apps flip that model by bringing apps into the generative AI environment itself. I think we’re heading toward a hybrid world where the best path really depends on where your users and customers are and what they prefer to engage with.”

He added that generative AI platforms, and particularly ChatGPT, “see exceptionally high engagement from younger generations.” So he thinks AI-based application development platforms like OpenAI’s will become increasingly important.

> “The MCP excels at integrating various types of data from different sources into an LLM like GPT.”  
> **– Shea**

As for the types of apps suitable for integrating into ChatGPT, he thinks that MCP will act as a kind of hub for data — which will in turn drive incentives to build a ChatGPT app.

“The MCP excels at integrating various types of data from different sources into an LLM like GPT,” he said. “I think the opportunity for building ChatGPT apps could be in scenarios where the use of plain text is insufficient and doesn’t offer an engaging user experience. For example, a visual experience may be needed due to more complex data or a specific layout or because an organization wants to maintain a strong brand presence and ownership within the ChatGPT interface.”

Shea added that he doesn’t necessarily see ChatGPT apps as the final form factor for OpenAI in its applications strategy.

“I have a hunch that the way we build ChatGPT apps today shares some core ideas and structure with the potential smartphone platform OpenAI has been rumored to be launching in the future.”

## The Future of ChatGPT Apps

We’re still in the very early stages of ChatGPT apps. TELUS Digital has, after all, only created a proof-of-concept app so far. So I asked Shea whether it has any ChatGPT apps in production that it has built or helped build for their customers?

“Yes, we have been working with a leading provider of financial news and market intelligence for the past month, and are in the final phase of building an authenticated experience where the user can track equities over time and use plain English to search through different stocks based on specific criteria.”

Meanwhile, some well-known tech companies are busy launching ChatGPT apps. Just in the past few days, Adobe announced ChatGPT apps [for Photoshop, Acrobat, and Adobe Express](https://www.theverge.com/news/841369/chatgpt-apps-adobe-photoshop-acrobat-express); and earlier this week, OpenAI announced an [Instacart app in ChatGPT](https://openai.com/index/instacart-partnership/). Expect a lot more of these types of apps to come into ChatGPT in 2026 — including from both enterprise and independent third-party developers.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)