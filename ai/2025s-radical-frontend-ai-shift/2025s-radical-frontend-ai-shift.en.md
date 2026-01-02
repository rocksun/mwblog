When we closed the door on 2024, there was both pearl-clutching and hype over AI — but at that time, not a lot of functionality for the frontend. That rapidly shifted in 2025, as AI use in web development evolved from code production into the creation of systems-aware components and plugins. This year also saw [developers move past the generic chatbot](https://thenewstack.io/move-beyond-chatbots-plus-5-other-lessons-for-ai-developers/) era to an approach that bakes AI directly into the frontend architecture, via a new category of generative tools that better understand UI/UX.

## The Death of the ‘Figma Gap’ and the Rise of Code-First Prototyping

At the start of the year, TNS highlighted [WebCrumbs’ Frontend AI project](https://thenewstack.io/genai-helps-frontend-developers-create-components/), a generative AI model that created a plugin or template for developers, exporting the code as CSS/Tailwind, HTML, React, Angular, Svelte or Next.js. This differentiated it from Vercel’s v0, which at first tightly coupled Next.js and Tailwind. (v0 now offers more flexible exporting of React, [Svelte, Vue, and Remix](https://v0.app/docs/faqs), as well as standard CSS code.) WebCrumbs Frontend AI also incorporated a code editor and Visual Studio.

[WebCrumbs has since shut down](https://www.webcrumbs.ai/), including Frontend AI, according to its site.  But it was a hallmark of what was to come by the end of the year, as development moved toward creation of components and more integration with frontend development work.

> We saw the “Figma gap” closing, as new tools generated code and design simultaneously.

We also saw the “Figma gap” closing, as new tools generated code and design simultaneously, ensuring that what the developer sees in the visual editor is what gets rendered in the browser.

But some, including CEO Eric Simons of [Bolt, an AI-based online web app builder](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/), foresaw an even bigger shift coming that might make it easier to create and design at the same time. Simons argued it could make the Figma gap irrelevant.

“We’ve entered a new era where it’s now faster to make working prototypes with code, than design them in Figma,” Simons said in a tweet at the time.

It’s worth noting that [Bolt](https://bolt.new/) still includes a way to upload Figma files, suggesting we’re not quite at a place where code has converged with design.

Still, instead of asking AI to rewrite a whole file for a small change, new interfaces allowed for visual tweaking — spacing, colors, fonts — that syncs instantly with the code.

## The LLM Reasoning Revolution

One thing that made that possible was a shift in Large Language Models (LLM). LLMs moved away from being general-purpose models as AI companies created models optimized for development, as well as for specialized AI developer tools.

In mid-2024, [Claude Artifacts was released](https://thenewstack.io/is-react-now-a-full-stack-framework-and-other-dev-news/), providing a preview of what was to come in 2025. It provided an AI-powered UI feature with a side-panel that allows developers to view or interact with React or HTML code in real-time, as the model writes it.

Then in April 2025, we saw the release of [OpenAI’s GPT-4.1](https://thenewstack.io/openai-releases-new-models-trained-for-developers/), which was specifically tuned for coding and instruction following, with a 1 million token context window. OpenAI also released reasoning versions with the o3 and o4 models, which introduced the ability to use images. Developers could suddenly convert whiteboard sketches or UI screenshots directly into logical reasoning chains.

In early 2025, Anthropic released [Claude 3.7 Sonnet](https://thenewstack.io/making-the-fediverse-more-accessible-with-claude-3-7-sonnet/). Its standout feature was a dual thinking mode that allowed developers to toggle between a standard fast response and an “Extended Thinking” mode. This was key for the frontend because it allowed for complex UI logic or state management issues.

Google also launched [Google Stitch](https://developers.googleblog.com/stitch-a-new-way-to-design-uis/) as experimental in May. Powered by Gemini 3, it integrates directly with Figma and can read a design file and generate high-fidelity frontend code that follows specific design system rules, such as Material Design.

## AX Over DX: Standardizing Agent-to-UI Communication With MCP

In January, Netlify CEO Matt Biilmann spoke with TNS about [AX (agentic experience)](https://thenewstack.io/beyond-dx-developers-must-now-learn-agent-experience-ax/), arguing that we must now design websites for AI agents as much as for human users. It was a warning we heard repeatedly over the course of the year in terms not just of websites, but [even APIs](https://thenewstack.io/its-time-to-start-preparing-apis-for-the-ai-agent-era/). By June, we heard it repeated by companies like PayPal, which had already began working on transitioning its [PayPal APIs to be more agentic-friendly](https://thenewstack.io/paypal-on-how-to-prepare-apis-for-agentic-ai-future/).

One way companies do this is by using the [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/). MCP servers quickly came on the scene, emerging as the industry [standard for how AI agents](https://thenewstack.io/agent-ui-standards-multiply-mcp-apps-and-googles-a2ui/) talk to application data. Extensions like MCP-UI allow these agents to not just fetch data, but to “pull” rich, branded UI components from a server and display them inside a chat interface (e.g., a flight picker appearing directly inside a Claude or ChatGPT window).

> MCP servers quickly came on the scene, emerging as the industry standard for how AI agents talk to application data.

MCP servers soon became table stakes for both companies and JavaScript frameworks that wanted to share documentation best practices with developers. [Angular and React both launched MCP Servers](https://thenewstack.io/10-mcp-servers-for-frontend-developers/) this year, and we’ve heard rumors of other frameworks following suit.

The year also saw the beginning of “self-healing UIs” that use agents embedded in the dashboard — such as [Netlify’s Agent Runners](https://thenewstack.io/new-netlify-agents-offer-ai-workflows-for-developers/) — that can scan for broken links, identify accessibility violations, or fix responsive design bugs on mobile devices and submit the Pull Request automatically.

## Generative UI: Moving Toward the Self-Assembling Interface

All of this soon led to what was arguably the most radical frontend shift in 2025: The evolution of Generative UI, where the interface is assembled by AI in response to a user’s prompt. While LLMs had been able to create interfaces since the beginning, these solutions became more complex and developer-friendly, allowing for more complex creations.

One such tool is the [Hashbrown Framework](https://thenewstack.io/run-ai-agents-in-the-browser-with-the-hashbrown-framework/), which we featured in December. This open source framework enables AI agents to run entirely in the browser. An app using Hashbrown can deploy an LLM to decide which UI components to render on the fly — filling out forms, creating custom charts, or suggesting shortcuts based on live user behavior.

It also supports, via the Skillet library, streaming, which resolves issues with LLM speeds regarding prompting. This allows the UI to start rendering and animating components the millisecond the AI begins “thinking,” making the experience feel instantaneous. By leveraging experimental browser APIs in Chrome and Edge, these tools also will also be able to run lightweight models on-device. This allows for a “private AI” that doesn’t need to send sensitive user data to a cloud server to provide a smart experience.

2025 has given us a preview of what’s possible with AI on the frontend. We look forward to finding out what sticks and what doesn’t in 2026.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)