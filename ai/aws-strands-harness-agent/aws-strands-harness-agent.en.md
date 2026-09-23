Amazon Web Services (AWS) is [lifting the lid](https://strandsagents.com/blog/introducing-strands-harness/) on a new open source, general-purpose AI agent, designed to give developers a ready-made foundation they can run locally or deploy to the cloud.

[Strands Harness](https://strandsagents.com/docs/user-guide/harness/), as it’s called, builds on [Strands Agents](https://github.com/strands-agents/), which AWS [debuted in May 2025](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/) as an open source Python SDK for building AI agents. Strands takes what AWS calls a “model-driven approach”: developers provide the model, tools and instructions, while the model determines how to tackle the task and when to call those tools. AWS later [brought Strands to TypeScript](https://strandsagents.com/blog/strands-agents-typescript-v1/), and in February [created Strands Labs](https://thenewstack.io/aws-strands-labs-launch/) as a separate home for more experimental projects.

[Marc Brooker](https://www.linkedin.com/in/marc-brooker-b431772b/), VP and distinguished engineer at AWS, tells *The New Stack* that Strands Harness essentially sits above the [existing Strands SDK](https://github.com/strands-agents/harness-sdk), giving developers a preconfigured Strands Agent. It brings together the tools and supporting machinery an agent needs to operate over longer-running tasks, with AWS supplying its own defaults for how those pieces work together.

> “You still need to decide how to manage context, persist conversations, integrate tools, and guide the agent’s behavior.”

“An SDK like the Strands Harness SDK gives you the building blocks, but you still need to decide how to manage context, persist conversations, integrate tools, and guide the agent’s behavior,” Brooker explains.

## Unpacking Strands Harness

Out of the box, Strands Harness gives developers a working agent with file, shell and web tools, alongside built-in handling for context, memory, persistent sessions, prompt caching and delegation to other agents.

Developers can install Strands Harness as a Python or TypeScript package, using `pip install strands-harness` or `npm install @strands-agents/harness`.

AWS also provides the Strands CLI as an interactive way to prototype and configure an agent. Developers can choose a model, add prompts, tools and other capabilities, then use `/export` to generate the resulting agent as Python or TypeScript code.

![Configuring an agent with the Strands CLI.](https://cdn.thenewstack.io/media/2026/09/f7835bc7-giffy2.gif)

*Configuring an agent with the Strands CLI.*

Individual agents can be tailored to different jobs, with developers able to change their instructions, choose which model they use, control which tools and capabilities are available to them, and decide whether they can hand work off to another agent.

![Demo of Strands Harness running on a desktop](https://cdn.thenewstack.io/media/2026/09/2baca1eb-giffy.gif)

*Demo of Strands Harness running on a desktop (Credit: AWS)*

Most of Strands Harness itself doesn’t depend on AWS infrastructure. The agent loop, tools, context management, session handling and delegation are all included in the open source release, and AWS says those processes run on the machine that’s running the agent by default.

The exception is the call to the underlying model. Perhaps unsurprisingly, AWS routes model access through [Amazon Bedrock](https://thenewstack.io/mcp-summit-aws-bedrock/), its managed service for accessing and running foundation models. However, while Brooker says that this is the *only* out-of-the-box default tied specifically to AWS infrastructure, it too can be switched out.

“This is easily overrided to use a different model provider with one line,” he says.

Strands Harness can instead use Anthropic, OpenAI or Google as its model provider, or use a locally running model through [Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/). Changing provider doesn’t necessarily mean changing the underlying model, but Brooker notes that choosing a different model will obviously affect how the agent behaves.

“Different models have different strengths on reasoning, tool use, and cost,” he continues. “What doesn’t change: context management, sessions, tools, delegation all work the same regardless of provider. No features require Bedrock.”

It’s worth noting that all the other defaults can be changed, too. Developers can bring their own tools and skills, connect MCP servers, alter how context is handled, and choose where session state is stored.

> “Developers can focus on their application’s task and domain expertise, while customizing the components that need different behavior.”

“Developers can focus on their application’s task and domain expertise, while customizing the components that need different behavior,” Brooker says.

## AWS benchmarks its agent

AWS says Strands Harness is intended as a general-purpose agent rather than a coding assistant, though it takes cues from harnesses such as Claude Code and Codex. The difference, AWS says, is that developers can deploy Strands Harness to whichever cloud provider they choose — addressing what it describes as a common wish among developers using Claude Code and Codex to be able to run the same setup in the cloud.

From its own testing, AWS suggests the way a harness manages the surrounding agent machinery can materially affect cost and performance, even when the underlying model stays the same. For each harness, AWS averaged its score across six benchmarks — ALFWorld, ContextBench, GAIA, WebShop, τ³-bench and Terminal-Bench 2.1– and compared that with the average cost per task across the same tests. Against Claude Code and Codex specifically, the company says Strands Harness came out 45% cheaper, with broadly comparable accuracy.

However, that figure drops to 28% once [DeepSeek Harness](https://thenewstack.io/deepseek-harness-open-source-plugins/) — which AWS says ran around 14% cheaper than Strands Harness on matched runs — is folded into the wider comparison.

![Strands Harness benchmark results. ](https://cdn.thenewstack.io/media/2026/09/62791a1e-screenshot-2026-09-21-at-18-06-20-introducing-strands-harness-frontier-performance-with-28-lower-token-cost-strands-agents.png)

*Strands Harness benchmark results. (Credit: AWS)*

AWS points specifically to its context-management defaults as a major reason for the result. Strands Harness truncates particularly large tool outputs, compacts context once the available window passes a set threshold, and attempts to recover within the agent loop if the context overflows.

On Terminal Bench 2.1 specifically, AWS says Strands Harness running Fable 5 cost 77% less than Claude Code, at $56.29 versus $248.05 across 89 trials, while scoring 69.7 versus 61.8. DeepSeek Harness was cheaper again at $40.30, though its score was lower at 59.5.

![Terminal Bench 2.1 results.](https://cdn.thenewstack.io/media/2026/09/7e38a4c9-screenshot-2026-09-21-at-18-06-29-introducing-strands-harness-frontier-performance-with-28-lower-token-cost-strands-agents.png)

*Terminal Bench 2.1 results. (Credit: AWS)*

For AWS, those results help make the case for packaging and tuning functions such as context management, versus requiring every developer to work out those decisions independently with the SDK.

> “Getting a prototype working is one step; evaluating how those choices affect performance and cost is another.”

“Getting a prototype working is one step; evaluating how those choices affect performance and cost is another,” Brooker says. “The opportunity we saw was to package that engineering into a complete, general-purpose agent.”

## What’s in it for AWS?

AWS also has an obvious place to run the resulting agent. [Amazon Bedrock AgentCore](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/) is its managed service for deploying and operating agents, providing identity and access controls, observability and the infrastructure needed to host them.

There is, in fact, a close technical relationship between the open source project and that managed offering. AgentCore Harness and Strands Harness were built by the same team, although they live in separate codebases. Brooker says work on one can also feed improvements into the other, giving AWS a route for technology developed in the open source project to inform its managed service, and vice versa.

Brooker, again, stresses that Strands Harness can be deployed independently of AgentCore, outside of AWS altogether.

“AgentCore is an optional hosting layer for teams that want AWS to manage the infrastructure side,” he says. “However, all deployment paths are open for the developer to choose.”

Still, this arrangement gives AWS a clear commercial path: developers can adopt Strands Harness freely, while AgentCore gives the company a natural destination for teams that eventually want AWS to run the infrastructure around it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)