Earlier this month, [Anthropic](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/) launched [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) in public beta. Two weeks later it added persistent memory. From this and many other Claude focused launches in the recent past, it’s clear that Anthropic is selling more than a model. It’s now selling the infrastructure needed to run the model at scale.

I tested Claude’s Managed Agents and persistent memory so you don’t have to. What I found was a product built for people who are familiar with some level of development. This product was built more to fit needs that an engineering team currently has, less of a test friendly software for solo developers.

## What is Claude Managed Agents with persistent memory?

Managed Agents is a suite of APIs that developers used to have to build themselves before shipping a production AI agent. This is the infrastructure shift. Built in-house vs the APIs Claude Managed agents provide like secure sandboxing, long-running sessions, checkpointing, credential management, scoped permissions, and end-to-end tracing.

The pricing offered also mirrors an infrastructure product. On top of standard Claude API token rates, Managed Agents costs $0.08 per session hour. It was cheap to set up the test (but I did have to add $20 to my Claude balance) but can get expensive quick. For a company running hundreds of agent sessions a day it is a different calculation entirely.

## What I found during my initial testing

Getting started was exactly what I hoped everything was. Quick and simple. The console walks you through a four-step quickstart which includes create agent, configure environment, start session, integrate. Pre-built templates handle most of the setup. I had a research agent running in under five minutes with no code written. The console even asked me in plain English whether the agent needed unrestricted internet access or should be limited to specific hosts, then configured the environment automatically based on my answer.

The pre-built templates reveal what Anthropic thinks the real use cases are. There is a Deep Researcher that conducts multi-step web research and synthesizes sources. A Field Monitor that scans software blogs weekly and writes a what-changed brief. An Incident Commander that triages a Sentry alert, opens a Linear ticket, and runs the Slack war room. A Sprint Retro Facilitator that pulls a closed sprint from Linear and writes the retro doc before the meeting.

All things that could run autonomously without human intervention.

## What made testing hard

The console goes from [no-code](https://thenewstack.io/no-code-is-dead/) to code pretty quickly. When I tested the data analytics template, the second prompt asked me to call the Files API using [Python](https://thenewstack.io/python/) code. While this is great for someone who’s using an autonomous agent to read real data, it made the testing exercise less of a no-code experience quickly. Similarly to the Deep Research agent, I was unable to secure the research I was looking for in order to properly test the agent. The system timed out when I made a detailed complicated query. It returned the data I asked for from a more simplified query but the result felt too similar to the Claude chat app so I didn’t investigate further. This further proves the point that Managed Agents is real infrastructure for engineering teams shipping products at scale.

The companies Anthropic mentioned help tell the full story. [Notion](https://www.notion.com/product) uses it to run dozens of tasks in parallel while teams collaborate on the output. [Rakuten](https://www.rakuten.com/) deployed each specialist agent within a week across engineering, product, sales, and finance. [Asana](https://app.asana.com/) built AI Teammates that work alongside humans inside Asana projects. [Sentry](https://sentry.io/welcome/) went from a flagged bug to a reviewable fix in one flow. [Claude Managed Agents are already infrastructure for production deployments](http://claude.com/blog/claude-managed-agents) at scale.

Last week Anthropic added persistent memory, which lets agents learn and improve across sessions. For example, an agent handling customer documents can now remember what it learned last week without needing to be refreshed on the topic in a prompt. You can see this thorough Claude as it now offers persistent memory between chats.

## Why this matters

A common critique of AI infrastructure products is lock-in. Your agent runs on Anthropic’s cloud, processes your data through Anthropic’s infrastructure, and depends on Anthropic not changing the pricing or deprecating the API.

But the more interesting strategic question is what Anthropic is actually doing here. The company already makes the model that [Cursor](https://thenewstack.io/cursor-agents-developer-workflows/), Claude Code, and dozens of other developer tools are built on. Now it is building the infrastructure layer that sits between those models and production deployments. If that layer becomes the default way developers ship agents, Anthropic stops being a model provider and becomes something closer to [AWS](https://thenewstack.io/aws-launches-new-ai-agents-to-simplify-legacy-migrations/) for [agentic AI](https://thenewstack.io/beyond-scripts-the-shift-from-automation-to-agentic-ai/).

That is a much larger business. And judging by what it has shipped in the past three weeks, Anthropic is moving fast to own it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)