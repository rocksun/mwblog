Vercel on Wednesday launched [eve](https://vercel.com/eve), a new open-source framework for building AI agents that treats each agent as a directory of files and bundles the infrastructure needed to run it in production.

The company describes eve as “Next.js for agents,” referring to the popular [web framework](https://nextjs.org/) Vercel created and maintains.

Eve launched at Vercel’s Ship conference in London, together with a set of related products under the [Agent Stack](https://vercel.com/blog/agent-stack) moniker.

![](https://cdn.thenewstack.io/media/2026/06/330044ef-hello-eve-more-padding.gif)

Credit: Vercel.

## An agent is a directory

One of the parallels with Next.js that Vercel stresses is that Eve defines an agent is similat to the way Next.js defines a web app.

A single directory holds all of the individual files that define what the agent does. One file sets the model the agent runs on, with Vercel’s [AI Gateway](https://vercel.com/ai-gateway) handling provider fallbacks. Another holds the system prompt, written in Markdown. The agent’s tools, meanwhile, are individual TypeScript files, where the filename becomes the tool’s name, and nothing has to be registered separately. And like every other agent framework, eve uses skill.md files, as well as [MCP servers](https://modelcontextprotocol.io/) to connect to other tools.

![](https://cdn.thenewstack.io/media/2026/06/64b07ddc-screenshot-2026-06-17-at-09.42.32-1024x484.png)

Credit: Vercel.

Eve then compiles this directory into a running agent.

Every conversation runs as a durable workflow, built on Vercel’s open-source [Workflow SDK](https://workflow-sdk.dev/), that checkpoints each step so a session can pause, survive a crash, and resume where it left off.

On the security side, each agent gets its own sandbox for the code it writes to ensure it remains isolated from the application. It’s also worth noting that every tool can be set to require human approval before it runs.

When appropriate, agents can hand off work to subagents, connect to outside services through MCP servers or [OpenAPI](https://www.openapis.org/) documents, and reach users through built-in channels for Slack, Discord, Microsoft Teams, Telegram, Twilio, GitHub, and Linear.

To allow developers and IT teams to keep tabs on what is happening, every run produces an [OpenTelemetry](https://opentelemetry.io/) trace that appears in a new Agent Runs view in Vercel’s [observability dashboard](https://vercel.com/products/observability), with the ability to export the data to specialized services like [Datadog](https://www.datadoghq.com/) and [Honeycomb](https://www.honeycomb.io/).

## Running and deploying agents

Developers start an agent locally with a single command and talk to it through a terminal interface. Deploying uses the same `vercel deploy` command as any other project, and a session that is mid-task when a new version ships finishes on the version it started on.

Eve is available in [public preview](https://vercel.com/eve) and is licensed under Apache 2.0 on [GitHub](https://github.com/vercel/eve).

![](https://cdn.thenewstack.io/media/2026/06/ef2cebba-screenshot-2026-06-17-at-09.42.44-1024x484.png)

Credit: Vercel.

## How Vercel uses it

Vercel itself says it runs more than 100 agents internally on eve, including a data-analysis agent that employees query in Slack tens of thousands of times a month and a routing agent that directs questions to whichever agent can answer them.

Agents are already a major source of Vercel’s own traffic. The company says agents now trigger around [29 percent of deployments](https://vercel.com/blog/introducing-eve) on its platform, up from less than 3 percent a year ago, and it expects that share to reach half.

## The competition

Eve enters a market that filled up quickly over the past year. Its closest TypeScript-native rival is [Mastra](https://mastra.ai/), a [Y Combinator](https://www.ycombinator.com/)-backed framework that reached version 1.0 in January and is built to run on any platform, in contrast to eve’s default to Vercel. LangChain’s [LangGraph](https://github.com/langchain-ai/langgraph), the most established agent framework, is Python-first and centers on the same durable execution eve offers. Inngest’s [AgentKit](https://agentkit.inngest.com/) is another TypeScript option with built-in durability.

The large cloud providers are coming at the same workloads from the infrastructure side. Cloudflare builds agents on its [Workers platform](https://workers.cloudflare.com/product/agents) and [Durable Objects](https://developers.cloudflare.com/durable-objects/), while Amazon’s [Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/), Google’s [Vertex AI Agent Engine](https://cloud.google.com/products/agent-builder), and Microsoft’s [Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/) offer managed runtimes that run agents from any framework. OpenAI’s [AgentKit](https://openai.com/index/introducing-agentkit/), released last year, ties its tooling to OpenAI’s own models.

Vercel says support for other platforms is coming. For now, though, eve runs only on Vercel.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)