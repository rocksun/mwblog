There was a further shift away from complexity in web development this year, with frontend frameworks like Astro and Svelte gaining popularity as more developers looked for solutions beyond the React ecosystem. Meanwhile, native web platform features proved they’re up to the job of building sophisticated web applications — with CSS in particular improving over 2025.

That all said, perhaps the biggest web development trend of this year was the rise of AI-assisted coding — which, it turned out, is prone to defaulting to React and the leading React framework, Next.js. Because React dominates the frontend landscape, large language models (LLMs) have had a lot of React code to train on.

Let’s look in more detail at five of the biggest web development trends of 2025.

## 1. The Rise of Native Web Features

Over 2025, a number of native web features quietly caught up to the functionality offered by JavaScript frameworks. For instance, the [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) — which enables your website to [animate smoothly](https://developer.mozilla.org/en-US/blog/view-transitions-beginner-guide/) between pages — became part of the [Baseline 2025](https://webstatus.dev/?q=baseline_date%3A2025-01-01..2025-12-31) index of cross-browser support. So it’s now widely available for web developers to use.

Baseline is a project coordinated by the WebDX Community Group at the W3C, which includes representatives from [Google](https://cloud.google.com/?utm_content=inline+mention), Mozilla, Microsoft and other organizations. It’s only been running since 2023, but [this year it really came into its own](https://thenewstack.io/interop-unites-browser-makers-to-smooth-web-inconsistencies/) as a useful resource for practicing web developers.

[![Baseline web features](https://cdn.thenewstack.io/media/2025/12/02643a08-baseline-stats-nov2025.png)](https://cdn.thenewstack.io/media/2025/12/02643a08-baseline-stats-nov2025.png)

The steady annual growth of Baseline features, via [the Web Platform Status site](https://webstatus.dev/stats).

As The New Stack’s Mary Branscombe [reported in June](https://thenewstack.io/baseline-newly-available-stay-on-top-of-new-web-features/), there are plenty of ways to keep track of what’s becoming part of baseline:

“Google’s Web.Dev has [a monthly update](https://web.dev/baseline#the-baseline-monthly-digest) on Baseline features and news, the WebDX features explorer lets you view features that are [Limited Availability](https://web-platform-dx.github.io/web-features-explorer/limited-availability/), [Newly Available](https://web-platform-dx.github.io/web-features-explorer/newly-available/) or [Widely Available](https://web-platform-dx.github.io/web-features-explorer/widely-available/); and the [monthly release notes](https://web-platform-dx.github.io/web-features-explorer/release-notes/march-2025/) cover what features have reached a new baseline status.”

From a web functionality perspective, there’s really no excuse any more to not use native web features. As long-time web developer [Jeremy Keith put it recently](https://adactio.com/journal/22235), frameworks are “limiting the possibility space of what you can do in web browsers today.” In [a follow-up post](https://adactio.com/journal/22265), Keith urged developers to especially stop using React in the browser because of the file size cost to the user. Instead, he encouraged devs to “investigate what you can do with vanilla JavaScript in the browser.”

## 2. AI Coding Assistants Default to React

This year, AI became a standard part of the web development toolchain (albeit one not always endorsed by developers, especially those who socialize on Mastodon or Bluesky instead of X or LinkedIn). Whether or not you’re an AI fan in application development, there is one big concern: the propensity of LLMs to default to React and Next.js.

When OpenAI’s [GPT-5 was released in August](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/), one of its purported strengths was coding. GPT-5 initially got [very mixed reviews from developers](https://thenewstack.io/is-gpt-5-a-coding-powerhouse-or-maintainability-nightmare/), so at that time, I reached out to OpenAI to ask them about the coding features. [Ishaan Singal](https://www.linkedin.com/in/ishaan-singal/), a researcher at OpenAI, responded by email.

I noted to Singal that in the [GPT-5 prompting guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide), there are three recommended frameworks: Next.js (TypeScript), React and HTML. Was there any collaboration with the Next.js and React project teams, I asked, to optimize GPT-5 for those frameworks?

“We picked these frameworks based on their popularity and commonality, but we did not collaborate directly with the Next.js or React teams on GPT-5,” he replied.

[![An example of "organizing code editing rules for GPT-5" from OpenAI's GPT-5 prompting guide.](https://cdn.thenewstack.io/media/2025/09/f028e3a8-screenshot-2025-09-05-at-10.55.25.png)](https://cdn.thenewstack.io/media/2025/09/f028e3a8-screenshot-2025-09-05-at-10.55.25.png)

An example of “organizing code editing rules for GPT-5” from OpenAI’s [GPT-5 prompting guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide).

We know that Vercel, the company that [shepherds the Next.js framework](https://thenewstack.io/vercels-frontend-and-the-rise-of-the-hybrid-developer/), is a fan of GPT-5. On launch day, it called GPT-5 “the best frontend AI model.” So there is a nice quid pro quo happening here — GPT-5 was able to become an expert in Next.js because of its popularity, which presumably increases its popularity even more. That helps both OpenAI and Vercel.

“At the end of the day, it is the developer’s choice,” Singal concluded, regarding which web technologies a dev wants to use. “But established repos have better support from the community. This aids developers in self-serve maintenance.”

## 3. Emergence of Web Apps in AI Agents and Chatbots

This year, we saw the emergence of mini-web applications inside AI chatbots and agents.

[MCP-UI was the first](https://thenewstack.io/mcp-ui-aims-to-replace-old-world-websites-with-ai-agent-uis/) sign that the web would be a key part of AI agents. As the name suggests, [MCP-UI](https://mcpui.dev/) uses the popular Model Context Protocol as a communication foundation. [The project](https://mcpui.dev/guide/introduction) “aims to standardize how models and tools can request the display of rich HTML interfaces within a client application.”

In [an interview in August](https://thenewstack.io/mcp-ui-creators-on-why-ai-agents-need-rich-user-interfaces/), the two founders (one of whom worked at Shopify at the time) explained that there are two types of SDKs for MCP-UI: a client SDK and a server SDK to connect to MCP servers. The server SDK is available in TypeScript, Ruby and Python.

[![MCP-UI demo](https://cdn.thenewstack.io/media/2025/07/3cf7bfe7-mcp-ui-demo.jpg)](https://cdn.thenewstack.io/media/2025/07/3cf7bfe7-mcp-ui-demo.jpg)

MCP-UI demo of a UI being inserted into a Claude 3.7 Sonnet chat.

MCP-UI sounded promising, but it was quickly overshadowed by [OpenAI’s Apps SDK](https://thenewstack.io/openai-launches-apps-sdk-for-chatgpt-a-new-app-platform/), which launched in early October. [Apps SDK](https://developers.openai.com/apps-sdk) allows third-party developers to build web-based applications that run as interactive components inside ChatGPT conversations — reminding many of us of when Apple launched its App Store in 2008.

The defining trait of Apps SDK is its web-based UI model (similar to MCP-UI). A ChatGPT app component is a web UI that runs in a sandboxed iframe inside a ChatGPT conversation. ChatGPT acts as the host of the app. You can think of a third-party ChatGPT app as a “mini web app” embedded directly into ChatGPT’s interface.

By the end of October, industry heavyweights like Vercel had figured out how to [use their JavaScript frameworks to build ChatGPT apps](https://thenewstack.io/next-js-in-chatgpt-vercel-brings-the-dynamic-web-to-ai-chat/). Vercel’s quick integration of Next.js with the ChatGPT apps platform shows that AI chatbots won’t just be limited to lightly interactive widgets — sophisticated web apps will live on these platforms, too.

## 4. Web AI and On-Device Inference in the Browser

A parallel development over 2025 was the rise in [running client-side AI in the browser](https://thenewstack.io/how-google-is-shifting-ai-from-the-cloud-to-your-browser/), which allows LLM inference to happen on-device. Google was especially prominent in this trend; and its term for it is “Web AI.” [Jason Mayes](https://www.linkedin.com/in/webai/), who leads these initiatives at Google, [defines Web AI](https://www.linkedin.com/pulse/life-edge-web-ai-history-future-smarter-digital-agentic-jason-mayes-fbqbc/) as “the art of running any machine learning model or service entirely client-side on the user’s device via the web browser.”

In November, Google held an invitation-only event called the [Google Web AI Summit](https://rsvp.withgoogle.com/events/web-ai-summit-2025). Afterwards, I spoke to Mayes, the event’s organizer and MC. He explained that a key technology is LiteRT.js, Google’s Web AI runtime that targets production web applications. It builds on [LiteRT](https://ai.google.dev/edge/litert), which is designed to run machine learning (ML) models directly on devices (mobile, embedded, or edge) rather than relying on cloud inference.

In a keynote presentation at the Web AI Summit, [Parisa Tabriz](https://www.linkedin.com/in/parisatabriz/), vice president and general manager for Chrome and the web ecosystem at Google, [highlighted the built-in AI APIs](https://thenewstack.io/googles-web-ai-playbook-the-paved-road-vs-the-open-field/) that were added to Chrome last August, along with the release of Gemini Nano — Google’s main on-device model — as a built-in feature in Chrome last June. These and other web technologies are driving the current Web AI trend.

[![Parisa Tabriz at Web AI Summit](https://cdn.thenewstack.io/media/2025/11/e857e98d-webai-tabriz1.png)](https://cdn.thenewstack.io/media/2025/11/e857e98d-webai-tabriz1.png)

Parisa Tabriz at Web AI Summit.

Another innovation that Google was involved in, alongside Microsoft, was [the release of WebMCP](https://thenewstack.io/how-webmcp-lets-developers-control-ai-agents-with-javascript/), which lets devs control how AI agents interact with websites using client-side JavaScript. In a September interview with [Kyle Pflug](https://www.linkedin.com/in/kylepflug/), group product manager for the web platform at Microsoft Edge, he explained that “the core concept is to allow web developers to define ‘tools’ for their website in JavaScript, analogous to the tools that would be provided by a traditional MCP server.”

Web AI isn’t just being promoted by commercial companies. The World Wide Web Consortium (W3C) is also exploring building blocks for “[the agentic web](https://thenewstack.io/the-agentic-web-how-ai-agents-are-shaping-the-webs-future/),” which includes using MCP-UI, WebMCP and [another emerging standard called NLWeb](https://thenewstack.io/cloudflares-balancing-act-protect-content-while-pushing-ai/) (developed at Microsoft).

## 5. The ‘Vite-ification’ of the JavaScript Ecosystem

It may sound like AI dominated web development this year — and it did, actually. But frontend tooling also saw its share of innovation. One product in particular stood out.

[Vite](https://vite.dev/), created by [Evan You](https://evanyou.me/?utm=22b03), has become the go-to build tool for modern frontend frameworks, including Vue, SvelteKit, Astro and React — with experimental support also from Remix and Angular. In [an interview with The New Stack in September](https://thenewstack.io/how-vite-became-the-backbone-of-modern-frontend-frameworks/), You told me that the key to Vite’s success was its early use of ES Modules (ESM), a standardized JavaScript module system that allows you to “break up JavaScript code into different pieces, different modules that you can load.”

[![Vite ecosystem](https://cdn.thenewstack.io/media/2025/10/d09b36d7-vite-plus-reveal.png)](https://cdn.thenewstack.io/media/2025/10/d09b36d7-vite-plus-reveal.png)

Vite ecosystem via Even You at ViteConf.

You and his company, VoidZero, are [now building Vite+](https://thenewstack.io/vite-aims-to-end-javascripts-fragmented-tooling-nightmare/), a new unified JavaScript toolchain that aims to solve JavaScript fragmentation. At this year’s ViteConf event, You [officially unveiled Vite+](https://www.youtube.com/watch?v=x7Jsmt_o9ek) and positioned it as an enterprise development toolkit. He said it includes “everything you love about Vite — plus everything you’ve been duct-taping together.”

## A Crossroads for Web Development

At the end of 2025, it feels like we’re at a crossroads in frontend development. On the one hand, there’s a way out of the React complexity conundrum: Use native web features and tools like Astro that ease the burden on users. While that was indeed a trend this year, it’s in danger of being overshadowed in 2026 by our increasing reliance on AI tools for coding — which, as noted, tend to rely on React.

The fact is, most developers now — including the hundreds of thousands of “vibe coders” who previously had not been part of the developer ecosystem — will continue to be fed React code by AI systems. That makes it even more imperative for the web development community to continue to endorse and advocate for native web code next year.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)