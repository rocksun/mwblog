The [Model Context Protocol (MCP)](https://thenewstack.io/why-the-model-context-protocol-won/) has quickly become a well-adopted standard for connecting [large language model (LLM)](https://thenewstack.io/introduction-to-llms/)-based AI agents with external data and tools.

As a result, many developers are stacking their environments with MCP tools. Seventy percent of MCP consumers have two to seven MCP servers configured, according to a late-2025 [study by Zuplo](https://zuplo.com/mcp-report).

But every MCP added consumes memory, which is thinning as context windows must store chat histories and configuration files, while agents chain multiple MCPs together into workflows.

In an [isolated experiment](https://selfservicebi.co.uk/analytics%20edge/improve%20the%20experience/2025/11/23/the-hidden-cost-of-mcps-and-custom-instructions-on-your-context-window.html), [Mihály Kávási](https://www.linkedin.com/in/kavasimihaly/), founder of [One Day BI](https://www.onedaybi.com/), a Microsoft Power BI consultancy, calculates that this “hidden tax” accounted for 51% of a 200,000-token context window in Claude Code before running any commands, with MCP tools alone consuming over 16%.

Response sizes from [MCP servers](https://thenewstack.io/when-is-mcp-actually-worth-it/) can also be unpredictable, often flooding context windows.

“There could be thousands or hundreds of thousands of tokens in a response, and there’s no way to filter that out ahead of time,” [Patrick Kelly](https://www.linkedin.com/in/patrick-kelly-eng/), co-founder and CEO of [Sideko](https://sideko.dev/), an API documentation and tools maintenance platform, tells The New Stack.

To address this pain point, Anthropic, creator of MCP, recommends a [code execution style](https://www.anthropic.com/engineering/code-execution-with-mcp) in which agents write and execute code to call tools, rather than making direct tool calls. Anthropic claims this approach can deliver a 98.7% reduction in token usage.

Cloudflare has debuted an architecturally similar feature, [Code Mode](https://blog.cloudflare.com/code-mode/). It’s one example of a broader “code mode” architectural approach that Cloudflare describes as “the better way to use MCP.”

“Code mode is the best way to use tools and MCP servers when you’re building AI agents that are performing a complicated task,” adds Kelly.

To date, code mode has largely remained vendor-constrained. [Port of Context](https://portofcontext.com/), a project open sourced in December, aims to change that by offering a vendor-agnostic and LLM-agnostic implementation.

## What is code mode?

Code mode represents an evolution beyond direct MCP tool calling, which can lead to indeterminate outcomes if LLMs are left to run free.

Instead, code mode provides a more controlled interface between agents and MCP servers. “It deterministically generates the functions and typed inputs and outputs for each of the tools,” Kelly says.

By supplying the agent with structured context upfront, code mode empowers it to execute a script to perform tool calls, like sending an email, sharing a calendar invite, or updating a customer relationship management (CRM) table.

This approach places greater emphasis on a sandboxed execution environment, which optimizes context usage while constructing and initiating the appropriate calls.

## Introducing Port of Context

“The goal of Port of Context is to make it really easy to set up code mode, test it, and run it 100% locally with any AI model,” Kelly says. “It’s an alternative with a great local development experience.”

Port of Context, or pctx, converts MCPs and tools into typed, sandboxed code. At the time of writing, the [GitHub repository](https://github.com/portofcontext/pctx) has nearly 200 stars and over 20 forks.

The project emerged, Kelly says, from repeated conversations with agent builders who cited context-window exhaustion as a persistent issue.

Pctx is relatively easy to run. It ships as a Rust binary with no dependencies. You just install it, run it in development mode, and use a command line interface (CLI) to connect and authenticate with upstream MCP servers.

The tool then supplies a URL for agents to reference, along with a dashboard for managing tools. Code execution runs inside a secure [Deno JavaScript](https://thenewstack.io/deno-2-arrives-with-long-term-support-node-js-compatibility/) runtime that only has access to the MCP servers explicitly granted by the user.

## Benefits of an agnostic code execution layer

The primary benefit of pctx is reduced token usage. Maintainers say pctx delivers token savings comparable to those reported by Anthropic.

Another benefit is tool agnosticism. Cloudflare’s Code Mode requires execution inside Cloudflare Workers, which run code in V8 isolates. Anthropic’s approach similarly depends on a Python sandbox tied to the Claude model.

A standardized open source code mode layer allows developers to bring whatever agent or model they choose. Pctx could also replace custom code layers built to prevent MCP responses from overwhelming context windows.

“I think there’s a need for this local and model-agnostic version of code mode,” says Kelly. Yet, maintainers have added features on top of the Anthropic and Cloudflare versions to retain compatibility.

They are also creating native integrations with AI agent frameworks like [LangChain](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) and [CrewAI](https://thenewstack.io/how-crewai-enables-ai-agents-as-collaborative-team-members/). This will allow developers to write local functions and register MCP servers without leaving their framework, Kelly says.

Code mode could also unlock additional automation. “We think code mode will unlock a lot of automation in terms of being able to automatically generate your MCP servers and then use them,” says Kelly.

Without code mode, he adds, automatically generating MCP servers from [OpenAPI specifications](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) can fail if the server was not designed with context window constraints in mind. Workflows that use 10 or more MCP tools sequentially can especially clog up the context.

Lastly, since pctx introduces an additional authentication layer, it may also enable stronger governance over MCP usage in enterprise scenarios — both internal and external.

## Early usage and trade-offs

It’s still early days for Port of Context. While interest is growing, most users remain in the experimentation phase.

Select users are currently testing the tool to reduce context flooding and replace custom code for processing MCP responses, says Kelly.

One specific early adopter is the [Sentient Foundation](https://sentient.foundation/), an open source artificial general intelligence (AGI) organization. The group is testing pctx in its [Recursive Open Meta-Agent](https://github.com/sentient-agi/ROMA) (ROMA), a framework for coordinating reasoning across multiple agents, as well as their other agentic products.

Although early pctx use looks promising, a potential drawback is maintainer concentration. While pctx is open source and designed to work across platforms, it’s primarily maintained by Sideko.

The runtime customization and core code mode features will remain fully open source, Kelly says, but cloud deployment and cloud authentication components will remain closed source.

However, maintainers plan to open the roadmap to external contributors, which could lead to new extensions from AI builders.

Lastly, pctx — and code mode variants more broadly — aren’t good for simple agent scenarios involving a single tool call. “For very simple tools and simple use cases,” Kelly warns, “it’ll actually slow you down.”

## The next step: Reducing MCP tool bloat

The AI agent ecosystem is evolving rapidly. While code mode techniques currently help optimize MCP usage, other strategies and standards are likely to emerge.

Additional optimization techniques, like [semantic caching](https://thenewstack.io/what-is-semantic-caching/), reducing servers in use, or slimming in-memory state, could also deliver results.

All in all, the emergence of projects like code mode and variants like pctx stand as indications of rising MCP use and the bottlenecks in operationalizing many MCPs in practice.

Given the efficiency gains, developers should consider these sorts of architectural changes. If the benchmarks are correct, it could equate to meaningful optimizations when using MCP.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/02/96a1456d-cropped-e7e1c083-bill-doerrfeld.jpg)

Bill Doerrfeld is a tech journalist and API thought leader. He is the editor-in-chief of the Nordic APIs blog, a global API community dedicated to making the world more programmable. He is also an active contributor to a handful of...

Read more from Bill Doerrfeld](https://thenewstack.io/author/bill-doerrfeld/)