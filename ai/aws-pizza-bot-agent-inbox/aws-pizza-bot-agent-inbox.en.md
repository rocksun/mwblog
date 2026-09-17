Amazon Web Services (AWS) has released a new open-source application dubbed [Pizza Bot](https://github.com/pizza-bot-app/pizza-bot), which gives developers an email-style inbox for managing AI agents that run in the background.

The problem that Pizza Bot is designed to address, ultimately, is that a chat interface is a poor fit for agents whose work continues after the (human) user has clocked off for lunch or bed.

And so Pizza Bot leans on the age-old mechanics of email: completed jobs arrive as unread threads, while anything that needs a human decision is surfaced for action. An Activity panel also exposes jobs handed off to specialist agents, including their tool use and progress.

> “Scheduled agents run autonomously in the background and surface updates directly into your inbox for review and triage.”

![Pizza Bot](https://cdn.thenewstack.io/media/2026/09/0a03e23c-whyneed-1024x683.png)

*Pizza Bot (Credit: AWS)*

Writing about the new project in a [LinkedIn post on Thursday](https://www.linkedin.com/feed/update/urn:li:activity:7503849029357940738/), co-creator [Joseph Dolivo](https://www.linkedin.com/in/josephdolivo/), principal technologist at AWS Startups, notes that Pizza Bot shifts the burden of monitoring agent work firmly away from the user.

“Instead of you having to initiate every conversation or wait on a prompt, scheduled agents run autonomously in the background and surface updates directly into your inbox for review and triage,” he writes.

As if to emphasize that point, in the accompanying [blog post](https://aws.amazon.com/blogs/opensource/introducing-pizza-bot-an-open-source-inbox-for-ai-agents-that-work-in-the-background/) for the project’s official launch on Thursday, the creators note that user absence is, in fact, a core tenet of the design brief.

> “The interface assumes you are not watching.”

“The interface assumes you are not watching,” they write. “Nothing else we’ve seen starts there, and that one assumption is what buys you pauses that outlast the session that created them, notifications worth acting on, and scheduled work that produces threads instead of logs.”

Despite its Amazon roots, Pizza Bot is in fact now a standalone community project rather than an AWS service. It lives in its [own GitHub organization](https://github.com/pizza-bot-app/), separate from Amazon, and comes with no AWS support or service-level agreement — it’s entirely self-hosted.

Pizza Bot itself is a desktop app for macOS, Windows, and Linux, with browser and terminal clients available too. By default, the app starts a local Pizza Bot server on the machine, while developers choose the model behind it — including Anthropic, Amazon Bedrock, Google Gemini, OpenAI, OpenRouter or a local model via Ollama.

It can also be extended through MCP servers and Agent Skills; the bundled browser-automation skill, for example, uses [Playwright MCP](https://playwright.dev/docs/getting-started-mcp) to navigate and interact with websites.

![Browser skill via Playwright MCP](https://cdn.thenewstack.io/media/2026/09/48cd699e-extend-1024x683.png)

*Browser skill via Playwright MCP (Credit: AWS)*

The server can also run on an always-on host or in a container, letting scheduled agents keep working while the laptop is closed and their threads be picked up later from another device.

## Under the hood: LangGraph and ambient agents

Pizza Bot’s agent runtime is built with [DeepAgents](https://www.langchain.com/deep-agents), LangChain’s open-source harness for long-running agent tasks, which itself runs on [LangGraph](https://www.langchain.com/langgraph), its runtime for stateful agent execution. The important part in all of this is persistence: LangGraph checkpoints an agent’s state as it works, allowing a run to stop for approval, survive a disconnected client and resume later without starting again from scratch. Pizza Bot stores those checkpoints, along with threads and other application data, locally in SQLite and ordinary files.

It’s worth noting that AWS has its own open source agents SDK, [Strands Agents](https://strandsagents.com/), out [since May 2025](https://thenewstack.io/aws-launches-its-take-on-an-open-source-ai-agents-sdk/) — but evidence suggests, including text in this [sample repository](https://github.com/aws-samples/langgraph-agents-with-amazon-bedrock), that AWS considers Strands as a “lighter-weight alternative to LangGraph for agents that don’t need explicit graph control flow.”

In response to a [question posted](https://www.linkedin.com/feed/update/urn:li:activity:7503849029357940738/?dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287503893780744474624%2Curn%3Ali%3Aactivity%3A7503849029357940738%29) on LinkedIn by *The New Stack*, Dolivo says that they very well could have used Strands for Pizza Bot, particularly as Strands supports [TypeScript](https://aws.amazon.com/about-aws/whats-new/2025/12/typescript-strands-agents-preview/) and [workflows](https://strandsagents.com/docs/user-guide/concepts/multi-agent/workflow/) now. But they ultimately went for LangGraph “due to the maturity of the tooling and breadth of the exosystem,” he explains.

“It’s also more familiar to many developers, and we wanted to reduce friction for community adoption since we knew we’d be open-sourcing it,” he adds.

Pizza Bot is also fairly close to an idea LangChain introduced way back in January 2025, when CEO Harrison Chase introduced the term “[ambient agents](https://www.langchain.com/blog/introducing-ambient-agents)” for agents that could respond to events, work concurrently and involve a human only when needed. LangChain’s reference implementation was an [email assistant built on LangGraph](https://github.com/langchain-ai/executive-ai-assistant). It also developed what it called an “[Agent Inbox](https://www.langchain.com/blog/introducing-ambient-agents#agent-inbox)”: a standalone interface inspired by email and customer-support software for keeping track of open interactions between people and background agents.

## From ‘JoeBot’ to Pizza Bot

The genesis of Pizza Bot can be traced back to April 2025, when Dolivo kicked off what he calls a “side-of-desk passion project” dubbed “JoeBot” that automated repetitive CRM logging. He later teamed up with colleague [Igor Fil](https://www.linkedin.com/in/igorvfil/) to turn that script into Pizza Bot, an MCP server that could execute parameterized, deterministic “recipes” across its internal systems.

The appeal soon spread beyond the engineers building it into less-technical domains. As the project evolved, Dolivo says it would eventually grow to more than 30 contributors and over 2,000 users inside Amazon, and so Pizza Bot needed a front end that people could open and use.

“An MCP server requires an MCP client, and expecting non-technical users to work out of an IDE or terminal was never going to cut it,” Dolivo adds. “We had to meet people where they actually work and own the experience end to end.”

The result was the version of Pizza Bot released this week: a desktop app built around an inbox rather than a terminal.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)