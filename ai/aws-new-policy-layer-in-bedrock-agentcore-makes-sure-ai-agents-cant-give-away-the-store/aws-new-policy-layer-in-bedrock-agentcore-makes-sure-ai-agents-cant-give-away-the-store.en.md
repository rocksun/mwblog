LAS VEGAS — At its re:Invent conference in Las Vegas, [AWS](https://aws.amazon.com/?utm_content=inline+mention) today announced a number of updates to [Amazon Bedrock AgentCore](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/) that will make it easier for businesses to build and deploy AI agents on the AWS platform.

Amazon Bedrock AgentCore is AWS’ developer-oriented platform for building, deploying and managing AI agents. When it [launched this summer](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/), it featured many of the core tools needed to build production-ready agents, including the ability to use any popular agent framework and large language model (LLM) to build those agents, authentication services, features to provide memory to these agents and more.

Now, at re:Invent, AWS is introducing three core new features that address some of the issues that still hold some companies back from adopting agents.

“In the usual AWS style, we have a handful of primitives,” [David Richardson](https://www.linkedin.com/in/davidrr/), the VP of Amazon Bedrock AgentCore at AWS, told me. “The intent is that they can work well together. Actually, we’re trying even harder to have that be true than is always the case with AWS. I know sometimes we show our seams, but we’re really trying to have it be a whole set of things that are likely going to be needed across a wide range of agents.”

## Policy

The first of these new services is a security and policy enforcement capability that addresses the need for additional guardrails that many companies have found when putting agents into production. For many companies, after all, it’s the nondeterministic nature of these models that makes them hesitant to go beyond the pilot phase — and that’s especially true when it comes to customer-facing products. Prompt injection attacks are, after all, very hard to protect against.

With this new feature, called Policy, Richardson explained that what’s interesting here is that it sits outside of the agentic loop and is rules-based. A company can use this to create guardrails (in natural language), to, for example, ensure that if the AI agent wants to offer a user a credit that is worth more than $100, a human agent has to step in and validate this request.

[![](https://cdn.thenewstack.io/media/2025/12/1cb23905-screenshot-2025-12-02-at-09.05.07.png)](https://cdn.thenewstack.io/media/2025/12/1cb23905-screenshot-2025-12-02-at-09.05.07.png)

Credit: AWS.

“The way I think about it … is it controls what the agent is allowed to ask the tool to do. At the low level, you’ve got [identity access management], which says these are the tools that can be used. With Policy, you’ve got what you can ask the tool to do — and then with our existing Bedrock Guardrails, you can control what the LLM will say back to the end user,” Richardson explained.

He also noted that the intent here is for Policy to be part of a layered security story that starts with the agent runtime sitting on top of micro virtual machines (VMs) that provide session-level isolation, on top of all of the usual security features that AWS offers.

In the end, Richardson argues, businesses need to be able to trust their agents if they want to get any real value out of them. And ideally, this additional safety net will get them there and allow them to rely on the agent’s reasoning capabilities more because it will be there when something doesn’t quite work as planned.

## Evals

The second new feature addition is custom Evaluations. Bedrock AgentCore already supported traditional observability tools — both those inside of the AWS ecosystem, like CloudWatch and the distributed X-Ray tracing system, or industry standards like OpenTelemetry.

The new evaluation tools will come with 13 prebuilt evaluations that cover a lot of the basics (correctness, faithfulness, helpfulness, response relevance, conciseness, coherence, instruction following, refusal, goal success rate, tool selection accuracy, tool parameter accuracy, context relevance, harmfulness, stereotyping).

Developers can also create their own custom evaluations, too. These will use an LLM as a judge.

[![](https://cdn.thenewstack.io/media/2025/12/48a2a2fb-screenshot-2025-12-02-at-09.07.49.png)](https://cdn.thenewstack.io/media/2025/12/48a2a2fb-screenshot-2025-12-02-at-09.07.49.png)

Credit: AWS.

“I’m kind of envisioning there will wind up — at least early on — being two ways it gets used. One will probably be by the agent developer at development and refinement time, while they’re going through and maybe testing it on their own or testing it with some precanned traces, and looking at the evals,” Richardson said. “And then the other will be more long-term by an Ops team, sort of analogous to how they manage a nonagentic application, where, in that world, you might have a latency- and error metrics-related set of metrics, now you might have a user sentiment or an accuracy metric that is calculated by the evaluators.”

## Memory

The third announcement isn’t so much a new feature as an addition to Bedrock AgentCore’s existing memory tool. The memory tool already provides short- and long-term memory features, but it now also offers episodic memory.

“The idea there is to have it be aligned with an individual user, so that you can record things like their preferences — like they prefer a window seat versus an aisle seat, or they prefer hotels that are sub-$500 or things like that,” Richardson said. “We think different memory disciplines, memory regimes, are going to be one of the keys to creating effective agents. And so we want to start to offer a few different memory type capabilities that customers can use.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)