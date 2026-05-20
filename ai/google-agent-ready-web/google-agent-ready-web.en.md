At its I/O developer conference on Tuesday, Google announced a number of new features and specs for how it plans to bring its Chrome browser and the web in general into this new era of agentic AI.

As Google developer advocate [Paul Kinlan](https://uk.linkedin.com/in/paulkinlan) notes in the announcement, “agents are transforming development everywhere, and nowhere is that transformation happening faster than on the web. It’s redefining what we build, how we build, and who builds. As we enter the era of the agentic web, we see a shift that bridges the gap between complex developer workflows, underlying platform capabilities, and everyday user experiences.”

Google argues that the web needs to adapt to AI agents’ needs, making it easier for them to interact with websites, while the browser needs to become more of a proactive assistant for users. Developers, meanwhile, will look for tools that help them get the most out of the web platform, with AI assisting them as needed.

## WebMCP in Chrome

At the core of how Google plans to give agents access to websites and the tools they provide is WebMCP, the emerging open standard for exposing JavaScript functions and HTML forms, for example, to agents.

“The whole point about WebMCP is that we want web experiences to be first-class citizens in agentic workflows, and WebMCP allows the web page to expose like individual functions and capabilities to those agents at this time,” Kinlan said in a press briefing ahead of the announcement.

Ideally, WebMCP allows agents to interact with a site, using the tools the website developer enabled for them. That’s much easier on the agent than trying to browse a site using screenshots or by traversing the DOM — and significantly faster, too.

Unsurprisingly, quite a few brands are interested in this as well, including Booking.com, Expedia, Instacart, Intuit, Shopify, and Redfin.

The plan is for Chrome to support WebMCP APIs soon. Google is starting with a WebMCP origin trial in Chrome 149, which is currently in beta.

For developers, Google is now letting them [bring their agents to the Chrome DevTools](https://developer.chrome.com/docs/devtools/agents). Agents can now access DevTool capabilities like console logs, network traffic, and accessibility trees directly. Gone are the days of you telling the agent what you saw in the console. They can now see what is happening directly and react accordingly.

This capability has been around for a little while, but Google now considers it a 1.0 release and ready for day-to-day usage. It’s available in Google’s own Antigravity app and for more than 20 coding agents. The tool uses either a built-in MCP server in Chrome or the Chrome DevTools CLI (because CLIs are sexy again now).

![](https://cdn.thenewstack.io/media/2026/05/9d8c565e-3_-ai_assistance_devtools.gif)

AI assistance in the Chrome DevTools. Credit: Google.

## A blueprint for coding agents building web apps

As AI tools speed up coding, the web will also change at a faster clip than before. With the [Web Platform Baseline](https://web.dev/baseline), Google and other browser vendors have defined a set of core capabilities that any web developer can expect to find in modern browsers. Google is now taking this a step further with its new [Modern Web Guidance](https://developer.chrome.com/docs/modern-web-guidance).

Available in early preview, this is essentially a set of skills for AI coding agents to teach them about the capabilities of a given Baseline target.

“We want developers to be confident that their coding agents are using features that the majority of their users will be able to use,” says Kinlan. “In the cases where they might have some browser support matrices that are outside of the baseline requirements — maybe they’re a little bit ahead of it — we’ll also have fallback strategies for when a user has a browser that doesn’t support some of the capabilities that another browser does as well.”

For developers who want to know which Baseline target they should focus on, Google is making it easy to connect to the Google Analytics API to see which browsers their users are on and which modern web features they support.

## A richer UI for the web

One major update Google is announcing at I/O is less about agents but is very much about next-gen feature: the HTML-in-Canvas API (combined with element-scoped view transitions. If your eyes glazed over reading that, you’re probably not alone, but as it turns out, this is all about eye candy.

The HTML-in-Canvas API will, as Google puts it, allow developers to “integrate real DOM elements directly into a canvas with WebGL and WebGPU to build an [immersive 3D experience](https://github.com/GoogleChromeLabs/css-web-ui-demos/blob/main/html-in-canvas/awesome-html-in-canvas.md) that is searchable, accessible, natively translatable, and interacts seamlessly with your built-in browser features.”

This is all about enabling rich graphical user interfaces that weren’t previously possible on the web. The `<canvas>` element has been around [for quite a while](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas) and allows web developers to draw graphics on a page using JavaScript. But inside of a `<canvas>` element, the browser layout engine isn’t available, meaning there’s no text wrapping, focus management, `<input>` fields, or support for copy-paste, for example.

HTML-in-Canvas brings these two worlds together. Live DOM elements from the layout engine can now be rendered inside a `<canvas>` element and, most importantly, they can be manipulated in that `<canvas>` area like any other element on a web page.

As of now, HTML-in-Canvas is a proposed standard, and Firefox and Safari haven’t adopted it yet.

“It changes the way the web feels,” Kinlan explains. “It’s going to give us the ability to change individual elements and style them in ways that we’ve never been able to style them before, all the way up to new types of experiences where you have either rich 3D graphics or 3D experiences that combine both the web and HTML.”

It’s the kind of feature you need to see in a demo (see below). It will also likely drive many a crazy experiment in what new UIs could look like on the web — with the usual excesses that come with that. But come back in a year and many web apps will likely look a bit more like a modern mobile experience than a 2005 Web 2.0 app.

![](https://cdn.thenewstack.io/media/2026/05/8ca929bb-5_-html_in_canvas_3d_in-car_demo.gif)

HTML-in-Canvas demo. Credit: Google.


[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)