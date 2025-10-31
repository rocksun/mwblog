For Vercel’s [Andrew Qu](https://www.linkedin.com/in/andrew-qu/), OpenAI’s new [ChatGPT Apps platform](https://thenewstack.io/openai-launches-apps-sdk-for-chatgpt-a-new-app-platform/) presented a challenge.

“ChatGPT initially designed their apps to be static HTML pages, cached, so they can deliver a consistent but static experience to everyone,” Vercel’s chief of software told The New Stack. “But the web has progressed all this time to make things more dynamic… so to sort of forgo all that work and only abide by what we could have supported 10 or 20 years ago felt like a waste of progress.”

It’s not completely fair to say that ChatGPT apps are “static,” since the examples demonstrated by OpenAI on its DevDay could respond to user input, trigger backend actions and update their views dynamically. But Qu’s larger point is that ChatGPT apps are only allowed to run inside a tightly sandboxed environment, which OpenAI designed for security and consistency. So from that perspective, ChatGPT apps are certainly more limited than full single-page applications (SPAs).

In any case, Qu and his team set out to push beyond these constraints — specifically, to make [Next.js](https://roadmap.sh/nextjs), Vercel’s flagship [React](https://roadmap.sh/react) framework, [run natively](https://vercel.com/templates/ai/chatgpt-app-with-next-js) inside ChatGPT’s controlled runtime.

[![Next.js in ChatGPT](https://cdn.thenewstack.io/media/2025/10/063c780f-vercel-chatgpt.avif)](https://cdn.thenewstack.io/media/2025/10/063c780f-vercel-chatgpt.avif)

ChatGPT app with Next.js. (Source: [Vercel](https://vercel.com/templates/ai/chatgpt-app-with-next-js))

What they found was a deeply layered runtime. “Things work within like a triple-nested iframe infrastructure,” Qu said. Each layer adds restrictions on navigation and state management, meaning even basic browser functions like `pushState` and `replaceState` have been patched to prevent complex routing. Here’s how Qu illustrated this in [a blog post](https://vercel.com/blog/running-next-js-inside-chatgpt-a-deep-dive-into-native-app-integration):

```
chatgpt.com
  └── web-sandbox.oaiusercontent.com (sandbox iframe)
     └── web-sandbox.oaiusercontent.com (inner iframe)
        └── your app's HTML
```

## How Vercel Makes ChatGPT Apps Dynamic

To overcome those limits, Vercel devised a series of workarounds for asset loading, redirects and hydration. The result: a Next.js app that can render dynamically inside ChatGPT without altering the framework itself.

“There are no tweaks that need to be done at the framework level,” Qu explained. “Everything can be implemented in user land. It’s mostly just another script element you add to the layout, and a few small catches here and there.”

> “There are no tweaks that need to be done at the framework level. Everything can be implemented in user land.”  
> **– Andrew Qu, Vercel chief of software**

In other words, Vercel didn’t fork Next.js or build a special version for OpenAI’s platform — it built [a template](https://github.com/vercel-labs/chatgpt-apps-sdk-nextjs-starter) that any developer can follow. By deploying a standard Next.js project and pointing ChatGPT’s connector at the resulting URL, developers can now embed complex frontend experiences directly in chat.

“As long as you follow the guide within the blog, or you use the sample template that we published, it should just work,” Qu said.

That may sound deceptively simple, but ChatGPT’s sandbox introduces subtler constraints.

“You’re still able to make full network requests with special whitelisting of what domains are allowed,” Qu noted. “The main things that are different are when you open external links — those get intercepted… there’s a secret `window.openAI.openExternalLink()` function that they load in for you.”

## **Not Every App Belongs in a Chat**

Even though Next.js apps can be fairly easily ported to ChatGPT, not every web app belongs inside a chat interface.

Qu pointed out that even OpenAI’s own marketplace partners — such as Booking.com, DoorDash and Expedia — don’t expose their full sites. “A lot of them just render a widget […], so it sort of fits in with the conversation,” he said.

That said, Vercel wanted to make sure developers could build multiple widgets within ChatGPT.

“The thing we were trying to solve with getting Next.js to work [in ChatGPT] is that you could still declare multiple different widgets in one app, and you can do it in a familiar way, rather than trying to go and write HTML or JS by hand,” Qu explained.

[![Canva ChatGPT app](https://cdn.thenewstack.io/media/2025/10/45610109-chatgpt-app-example-canva.png)](https://cdn.thenewstack.io/media/2025/10/45610109-chatgpt-app-example-canva.png)

Canva ChatGPT app. (Source: OpenAI video)

To make that easier, Vercel is preparing a set of React “GPT hooks,” a lightweight library that will expose ChatGPT-specific window properties — including display mode, maximum height, conversation state and even real-time completions from the language model. “There’s a lot of weird hooks that AI employs on the window object,” Qu said. “We’re trying to publish a package that lets you access everything you need.”

## The Role of MCP

So how does the [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) fit into all this? OpenAI itself describes MCP as “the backbone that keeps server, model and UI in sync” in the ChatGPT app paradigm. I asked Qu what Vercel’s approach to MCP has been with the Next.js integration.

“I have a lot of controversial opinions about MCP,” Qu chuckled. “It has the promise of being this be-all, see-all integration endpoint for AI, but a lot of people misuse MCP and sort of just treat it as an API mirror.”

He recommends using MCP *only* when developers don’t control the client, such as connecting ChatGPT to Notion or GitHub — but not for internal toolchains where direct APIs make more sense.

## **Aligning With GPT-5’s Stack**

I noted that in the GPT-5 Prompting Guide, OpenAI [explicitly recommends Next.js](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/) (TypeScript), React and HTML as the preferred frontend frameworks for AI-driven development. Has that alignment with OpenAI made it easier to do this Next.js integration with ChatGPT?

“We are trying to work with any and all model labs to make Next.js better,” Qu replied. “We just want all LLMs to generate better code, across the board.”

While that didn’t directly answer my question, the implication is that Vercel wants to be a default web framework for all AI chatbots — not just ChatGPT. Qu pointed to a new [“evals” page](https://nextjs.org/evals) on the Next.js website, which shows AI model performance evaluations. An OpenAI GPT model is currently number one, but an Anthropic model isn’t far behind.

[![Next.js evals](https://cdn.thenewstack.io/media/2025/10/5c3d6177-nextjs-evals-oct25.png)](https://cdn.thenewstack.io/media/2025/10/5c3d6177-nextjs-evals-oct25.png)

Next.js evals. (Source: [Next.js](https://nextjs.org/evals))

If Anthropic or another provider launches a similar chat app store, Qu said Vercel will “spend the time to make sure that […] we can officially work with [them] to design the spec and to be the DevEx arm.” He added that the company is already experimenting with SvelteKit (which Vercel backs) as another candidate for chat-based apps, since its stricter HTML/JS output aligns closely with ChatGPT’s static assumptions.

## The Web as the Primary Interface for AI

Stepping back, Qu sees this work as evidence that the open web remains central in the age of AI interfaces.

“We’re trying to do this thing with Next.js as a proof point that even if people don’t really interact with the web in the traditional sense […] it’s still up to the people to build the experiences that will then be embedded into the chat experiences,” he said.

Rather than viewing chat clients as browser replacements, he envisions them as new distribution layers for web content — places where developers can reuse their existing frameworks and hosting workflows.

“I’m personally betting that the open web will still be a thing,” Qu continued. “We have this new medium, this new way of interacting with computers through chat clients, but we can still have the same expressiveness and the same open standards to interact with such.”

> “…even if people don’t interact with the web in the traditional sense […] it’s still up to the people to build the experiences that will then be embedded into the chat experiences.”  
> **– Andrew Qu**

One emerging area of focus is [agentic commerce](https://thenewstack.io/how-mcp-ui-powers-shopifys-new-commerce-widgets-in-agents/), where storefronts surface directly inside chat sessions. Qu argues that this could make e-commerce more open, not less.

“If you have a storefront and you can publish it, it should be no harder than sharing a link,” he said. “That’s very against the [smartphone] app store model… I think the ChatGPT Apps experience actually gets us closer to that.”

## **React and Next.js as the Default AI Stack**

As more developers — and increasingly, AI models themselves — use Next.js, Vercel has seen usage explode. “Just in the past one month alone, we’ve had more Next.js downloads than in the previous 10 years combined,” Qu said. He attributes this surge not only to professional developers but to “a bigger movement and a lower barrier of entry,” as AI-generated code lowers the friction for building web apps.

Asked whether React and Next.js might become the default stack for AI-native UIs, Qu didn’t hesitate: “Certainly think so. I think the ergonomics and the human/AI DX [developer experience] is pretty good.”

Qu also argues that React’s component model provides the right balance between machine-generated structure and human design intent. Some developers might quibble with that and respond that [React’s complexity](https://thenewstack.io/want-out-of-react-complexity-try-vues-progressive-framework/) has warped web development too far towards DevEx.

But overall, Vercel’s quick integration of Next.js with the ChatGPT apps platform shows that AI chatbots won’t just be limited to lightly interactive widgets — sophisticated web apps will live on these platforms too.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)