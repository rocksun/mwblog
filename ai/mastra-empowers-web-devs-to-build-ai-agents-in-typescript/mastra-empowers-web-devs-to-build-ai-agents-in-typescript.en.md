Python dominated the early days of machine learning, but that’s changing as AI becomes more mainstream. Take, for instance, the recent release of [Mastra](https://mastra.ai/), an open source [agentic AI framework that uses TypeScript](https://github.com/mastra-ai/mastra) rather than [Python](https://thenewstack.io/what-is-python/).

Developers are less interested in what goes into a large language model and more intrigued by how to build an application on top of these models, according to [Sam Bhagwat](https://github.com/calcsam), Mastra’s co-creator and a full stack developer best known for his work as co-founder of the web framework [Gatsby](https://thenewstack.io/netlify-acquires-gatsby-its-struggling-jamstack-competitor/).

[Developers don’t have to know Python](https://roadmap.sh/python/how-long-does-it-take-to-learn) to build agents because they don’t require the same heavy computational work that work on models does, he says.

“Build agents don’t tend to need to do that kind of heavy tough work,” Bhagwat tells *The New Stack*. “It’s a lot of ‘Hey, am I providing my agent with the right context at this time? Does it have the ability to call the right tools, to perform actions on behalf to the users that are using this. Can I get the right information, which is much closer to web app development?”

And that’s the domain of [frontend developers](https://thenewstack.io/introduction-to-frontend-development), he adds.

“There’s this whole community, essentially, of full stack engineers that was being left out because we’re not really Python people. We’re JavaScript types,” he says. “We wanted to make a great tool for them.”

## Why TypeScript?

TypeScript has become a sort of default language for modern product teams, Bhagwat tells TNS.

“TypeScript tends to be better for web app development because your frontend is going to be written in JavaScript, in TypeScript, pretty much no matter what,” Bhagwat says. “When you have the backend of that written also in TypeScript, you just have a nicer integration.”

It also [opens up AI agents](https://thenewstack.io/open-responses-vs-chat-completion-a-new-era-for-ai-apps/) to a world of TypeScript-savvy developers. In fact, last year GitHub revealed that [TypeScript overtook both Python and JavaScript](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) as the most used language on its platform. The adoption shift “marks the most significant language shift in more than a decade,” the GitHub team says.

## Starting with AI agents

Agents are already changing how we interface with the internet, according to Bhagwat.

“It’s really interesting for people that are in this Dev Tools world, because we’re moving from a world where humans are writing code to where people are writing with Claude Code or Cursor. That changes a few things,” he says.

Increasingly, people are using internal documents with AI, which typically looks for markdown.

“If an agent is browsing the web and looking for a doc, because it’s a coding agent, it’s typically looking for markdown, and so it sends a request for markdown,” he explains. “Now some people are changing the content of their docs, specifically adding special instructions for agents, because they can tell who the visitors are.”

> “…we’re moving from a world where humans are writing code to where people are writing with Claude Code or Cursor.”  
> **– Sam Bhagwat, Mastra co-creator**

How important is it that web developers learn to build AI agents?

Bhagwat sees more businesspeople using AI to code solutions and even to train their own agents. Then there’s this: Frontend cloud provider Vercel CEO and creator of Next.js, Guillermo Rauch, has warned that the next evolution of frontend development will focus on building AI agents.

Right now, developers are tinkering and [learning about building AI agents](https://thenewstack.io/beyond-dx-developers-must-now-learn-agent-experience-ax/) as they usually do: Through personal side projects. For instance, Bhagwat needs to make a shopping list every week. He built an agent that understands the dietary preferences of his household. Many developers are launching similar personal projects so they can understand the technology before they have to deploy it in the enterprise, he says.

To help developers get started, Bhagwat has written an e-book, [*Principles of building AI agents*](https://mastra.ai/books/principles-of-building-ai-agents), that brings developers up to speed on what they need to know about agents and building with Mastra. It’s available for free download with email registration.

He has also written a second book, *[Patterns for building AI agents](https://mastra.ai/books/principles-of-building-ai-agents)*, also available for email registration.

## What Mastra offers out of the box

If you’ve used [Replit](https://replit.com/products/agent) to build an agent, you’ve used Mastra, according to Bhagwat. But let’s take a look at what you get with the full framework.

Mastra offers a few core framework primitives, starting with agents, which are autonomous code that use the LLMs, specific prompt instructions, and tools to complete user requests. It also supports workflows, which allow developers to orchestrate complex, multistep processes, And of course it incorporates RAG (Retrieval-Augmented Generation) functionalities, with built-in support for data syncing, web scraping, and vector database management. It offers an [MCP server](https://modelcontextprotocol.io/docs/getting-started/intro) that lets users provide a local copy of documentation to the AI.

The tool has both short-term and [long-term memory systems that allow agents](https://thenewstack.io/how-to-add-persistence-and-long-term-memory-to-ai-agents/) to remember context across threads and sessions.

Mastra users also have access to tools, specifically:

* Mastra Studio, a local developer playground where web developers can visualize, test, and debug agents and workflows in real-time.
* A [model context protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) Client, which allows developers to connect agents to pre-built tools, such as Google Sheets, GitHub, or internal databases — all without writing custom integrations;
* AI tracing and observability, so developers can see how the LLM is reasoning, as well as providing the token counts and execution steps; and
* Scorers and Evals, which are tools that measure the performance and accuracy of AI agents using model-graded or rule-based metrics. These are designed to help developers refine prompts before shipping to production.

The company also offers a fully managed cloud platform for zero-config deployments.

## Framework Support

The Mastra team has built in integrations with some frontend frameworks, including:

On the [backend, it supports](https://mastra.ai/blog/changelog-2026-01-20):

Mastra also integrates with agentic UI libraries that help web developers specifically build agentic frontend experiences, such as:

* [CopilotKit](https://mastra.ai/guides/build-your-ui/copilotkit), an open source framework that helps build Copilot experiences directly inside existing applications; and
* [Assistant UI](https://mastra.ai/guides/build-your-ui/assistant-ui), an open source TypeScript and React library that helps developers build high-quality AI chat interfaces.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)