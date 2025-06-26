“Every AI agent needs a web browser,” said [Paul Klein IV](https://www.linkedin.com/in/paulkleiniv), CEO of headless browser vendor Browserbase, at [this month’s AI Engineer World’s Fair](https://www.youtube.com/watch?v=YRGjll7uu5w).

What is a headless browser? [Simply put](https://en.wikipedia.org/wiki/Headless_browser), it’s a web browser without a graphical user interface. Until very recently, they’ve been used primarily for running automated web app tests and for web scraping and screenshotting. Three open source projects have emerged over the years to run these types of tasks: Puppeteer, Playwright, and Selenium. Playwright is the newest — it was launched by Microsoft in January 2020 — and also the most popular.

It’s only really over the past year that another, entirely new, use case has emerged for headless browsers. Suddenly, they’ve become a key component of what some — including [Microsoft](https://blogs.microsoft.com/blog/2025/05/19/microsoft-build-2025-the-age-of-ai-agents-and-building-the-open-agentic-web/) and browser company [Opera](https://www.operaneon.com/) — are calling the “agentic web.”

[AI agents](https://thenewstack.io/how-ai-agents-are-starting-to-automate-the-enterprise/), which are autonomous software applications, are typically tasked with going out onto the internet and gathering information — which is then either delivered to the user, or else an action is taken based on that information (such as purchasing an item on an e-commerce site). It turns out that headless browsers are ideal infrastructure for these AI agents.

> “If we want AI agents to interact with the rest of the legacy internet, they need a bridge. And I really do believe that the browser is that bridge.”  
> **– Paul Klein IV, Browserbase CEO**

Browserbase has heavily pivoted to take advantage of this new market. When the company launched in January 2024, it was promoting itself as [a browser infrastructure company](https://web.archive.org/web/20240101000000*/https://www.browserbase.com/). Its main offering was a managed service for Puppeteer, Playwright, and Selenium. Now, just eighteen months later, Browserbase describes itself as “a web browser for your AI.”

Earlier this month, Browserbase announced a massive Series B [$40 million funding round](https://www.browserbase.com/blog/series-b-and-beyond), indicating that headless browsers are now big business. In the announcement post, Klein made this observation: “The future of browsing is selective automation. Humans will still do the joyful, discovery-driven tasks. But repetitive, time-consuming work should be done by software. That’s what we’re building for.”

## How Headless Browsers Are Used in AI Agents

In his AI Engineer World’s Fair presentation, Klein emphasized that doing that automated browser work at scale is key to its value proposition. “With Browserbase, we let you run 1000s of headless browsers in the cloud for agents to control,” he said.

Browserbase has also glommed onto another huge trend this year: [MCP servers](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/). According to Klein, Browserbase has “the most popular browser automation MCP server out there.”

[![Browserbase MCP servers](https://cdn.thenewstack.io/media/2025/06/f8aeaaa1-browserbase-mcp-server-june25.jpg)](https://cdn.thenewstack.io/media/2025/06/f8aeaaa1-browserbase-mcp-server-june25.jpg)

Browserbase MCP server.

Part of the reason why developers choose Browserbase’s MCP server, he added, is because there are thousands of use cases in the “unsexy internet” (his term) where their customers don’t have custom MCP servers. So, using a headless browser with an MCP server built in — as Browserbase does — is an effective solution.

“You have AI agents and the legacy internet,” explained Klein. “You know, the DMV is not going to have an MCP server anytime soon. My barber shop is not gonna open a GraphQL API for me to schedule a haircut, as much as I keep begging John [presumably his barber] to do it. He’s got better things to do. So, if we want AI agents to interact with the rest of the legacy internet, they need a bridge. And I really do believe that the browser is that bridge between AI and the rest of the internet.”

He noted that many organizations on the “legacy internet” do not necessarily have an MCP server, but they probably have a website. (Ed: Unless they [just have a Facebook page](https://mastodon.art/@RMiddleton/114688285464490695)!)

“I think people use a lot of acronyms these days,” Klein continued. “You know, you have MCP, you have A2A, you have OpenAPI. But if those aren’t available, you can just do what could be considered the dumb thing: you just use a website. And websites are out there, there are plenty of them. There are billions of websites. And when your user is going to prompt your agent to do something, you might not always have a first-party integration available.”

[![Just use the website](https://cdn.thenewstack.io/media/2025/06/709a6edd-browserbase-just-the-website.jpg)](https://cdn.thenewstack.io/media/2025/06/709a6edd-browserbase-just-the-website.jpg)

“Just use the website.”

If AI-focused companies like Browserbase are to be believed, it will be AI agents that increasingly visit your business website, which implies that human web visits will decline accordingly. But how exactly are these agents getting the right information for their human users?

Klein reviewed the various types of AI agents currently available and how they control browsers. He started with the products that pioneered web agents over the past year or so — including WebVoyager, Adept and OpenAI’s Operator. He characterized their approach as: “Take a model and then have it generate some code to control a browser by generally parsing the DOM on the page, the HTML and the CSS.”

[![What is a web agent](https://cdn.thenewstack.io/media/2025/06/f32cefc8-browserbase-types-of-agents.jpg)](https://cdn.thenewstack.io/media/2025/06/f32cefc8-browserbase-types-of-agents.jpg)

What is a web agent?

Where we’re at now, he continued, is that there are two main types of web agents.

Vision web agents typically use headless browsers to take a screenshot “as context for the model,” and they “might do some marking up of the screenshot to indicate what box to click on,” said Klein.

Text web agents “predominantly use HTML as a context of the model” — Playwright is a popular tool in this approach.

[![Two types of agents](https://cdn.thenewstack.io/media/2025/06/7d8425b5-browserbase-two-types-of-agents.jpg)](https://cdn.thenewstack.io/media/2025/06/7d8425b5-browserbase-two-types-of-agents.jpg)

Two types of agents.

Incidentally, Browserbase has an open source framework for Playwright called Stagehand — available for Python and Node.js. In a recent [podcast interview with Brian Douglas](https://www.youtube.com/watch?v=ZHPY5QLIm0o), Klein said that Stagehand is “a superset of Playwright” and that it adds “more AI functionality on top of Playwright.”

Stagehand is key to Browserbase’s ambitions with AI agents. In another podcast interview, this time [with Latent Space](https://www.youtube.com/watch?v=YUGItptS5hI), Klein described Stagehand as “a framework for building web agents” with three API “tools” that developers can call: Act, extract, and observe.

Back to the AI Engineer World’s Fair presentation, Klein said that “computer-use” models are an emerging type of web agent. As the name suggests, it’s when an AI model is trained on UI tasks and “web trajectories” (a kind of workflow for an AI agent when it browses a website).

[![Web trajectories](https://cdn.thenewstack.io/media/2025/06/2402f5ae-web-trajectories-june25.jpg)](https://cdn.thenewstack.io/media/2025/06/2402f5ae-web-trajectories-june25.jpg)

Web trajectories.

## Conclusion

Klein noted that there is currently “a lot of innovation […] happening on teaching AI how to browse the web — and this stuff is getting good.” Certainly, if AI agents are to live up to their hype, then being able to effectively surf websites autonomously will be crucial.

You can argue whether it’s good for web publishers that their content is increasingly being browsed by AI agents rather than by humans (it’s [a big concern of mine](https://thenewstack.io/the-future-of-websites-in-the-age-of-ai-and-seo-decline/)). But it’s hard to argue against browser infrastructure being a critical piece of the [AI development stack](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/) moving forward. Browserbase seems perfectly positioned for this market.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)