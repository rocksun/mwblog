At its Summit in New York today, [AWS](https://aws.amazon.com/?utm_content=inline+mention) announced a slew of updates to its AI-centric services, but the most important news was definitely Amazon Bedrock AgentCore, a new platform (now in preview) that brings together all of the services developers need to put AI agents into production and at scale, using any framework and model.

To some degree, Bedrock AgentCore is an evolution of [Bedrock Agents](https://aws.amazon.com/bedrock/agents/). But where Bedrock Agents is meant to make it easy for anyone to quickly build an agent, AgentCore is a far more comprehensive solution that was born out of the realization that getting agents to production is still too hard. AWS argues that, today, many customers are still building their own tooling or using existing tools where it’s unclear how far they can scale. The core idea behind AgentCore is to give businesses the same kind of scalability, reliability and security that they are accustomed to on AWS, but to build agentic systems, which have very specific needs and challenges.

AgentCore combines a runtime for deploying and scaling agents securely, a memory system for storing and retrieving agent memories, as well as an identity service built on top of OAuth to allow AI agents to access AWS services and third-party tools with pre-authorization.

One interesting feature of the runtime is that individual agents can run for up to eight hours, and all runtimes are checkpointed, meaning it should be fairly easy to recover from any interruptions or failures.

[![](https://cdn.thenewstack.io/media/2025/07/60b816ef-aws_ai_stack_6_2025.png)](https://cdn.thenewstack.io/media/2025/07/60b816ef-aws_ai_stack_6_2025.png)

The AWS AI Stack after today’s Bedrock AgentCore announcement. Image credit: AWS.

Developers can use the memory feature for short-term and long-term memory for their agents — and that memory can be shared between agents, as well as for different agent sessions with the same agent (but maybe another underlying model).

The entire system is model-, framework- and protocol-agnostic. Developers could use a model that runs on Amazon Bedrock or their local laptop. Enterprises that want to use their own models can also do that, with AWS stressing that these models run in isolation, guarded by [AWS’ Nitro virtualization system](https://aws.amazon.com/ec2/nitro/).

Bedrock AgentCore also includes the AgentCore Gateway for turning any resource into a Model Context Protocol (MCP)-compatible tool (think APIs, AWS Lambda functions, etc.), and a code interpreter that allows agents to write and execute JavaScript, TypeScript and Python code securely.

As AWS notes, the ability to write and execute code isn’t just useful for coding agents. This code interpreter allows agents to execute any kind of code inside this sandboxed environment, from which the agent can also then access files and the internet to bring in additional libraries or data.

For those applications that need to be able to use a web browser, there is the AgentCore Browser Tool, a cloud-based browser runtime that allows agents to interact with websites from within an isolated virtual machine (VM). As AWS stressed in a pre-briefing ahead of today’s announcement, the Browser Tool is also model-agnostic (unlike most browser-use agents).

One area that is starting to get a lot more traction these days is agent observability, so it’s maybe no surprise that AgentCore also includes an observability tool that aims to provide developers with an end-to-end view of the agent’s behavior, its reasoning, tool usage and more. With this data, developers can then diagnose performance issues, failures and audit the agent’s output. All of this data is emitted in the [OpenTelemetry](https://thenewstack.io/the-modern-observability-roundtable-ai-rising-costs-and-opentelemetry/) format.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

## Agent Marketplace

Not every AI agent will be — and needs to be — built in-house. But enterprises need a way to procure these third-party agents and secure them. To help with this, AWS is also launching a marketplace for AI agents and tools, allowing businesses to buy and deploy them directly from the AWS Marketplace.

AWS says it will curate the agents in this marketplace and scan all of these agents for vulnerabilities.

## Amazon S3 Vectors

One nifty new service — and one that will likely get a lot of attention, too — is the launch of Amazon S3 Vectors. S3 is, of course, AWS’s core object store. Vectors are key to providing models with context (and memory) in their native format, and now S3 will get built-in support for storing and querying vectors at scale.

This service will integrate natively with Amazon Bedrock Knowledge Bases and the Amazon OpenSearch Service, and the company argues that it will allow users to store their vector embedding at scale for up to 90% less cost compared to alternative services. And since it sits on top of S3, the service can handle very large data sets.

## Customizing Amazon’s Nova Models

On top of these new services, AWS is also launching a few updates to its Amazon Nova models, which launched at AWS re:Invent last December. AWS is now making it easier to customize and fine-tune these models on top of the fully managed training infrastructure of Amazon SageMaker HyperPod. This, AWS says, is something many customers have been asking for as they start to look into how to efficiently tune models to understand their specific business needs.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)