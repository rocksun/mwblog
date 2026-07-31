AI agents can impress in a demo and still fumble in production. Diagrid’s Catalyst 2.0 aims to make them more resilient — and their actions tamper-evident — for high-stakes work.

With the launch of Catalyst 2.0, [Diagrid](https://www.diagrid.io) on Tuesday has added a durable execution and attestation layer to agents built with LangGraph, Microsoft Agent Framework, Google’s Agent Development Kit, OpenAI Agents SDK, and other popular frameworks.

The point here, the company notes, isn’t to get developers to adopt yet another agent framework. Instead, Catalyst runs underneath the existing frameworks and turns the agent’s model calls, tool calls, and handoffs into steps in a durable workflow. Diagrid says this allows an agent to resume from its last completed step when it’s interrupted, without having to repeat the entire run from step one.

“If the agent gets a prompt and it chooses to run 100 tools for the job and it fails at the 99th, it really needs to start back up from 99,” Diagrid co-founder and CTO [Yaron Schneider](https://www.linkedin.com/in/yaron-schneider-2130b7a3) tells *The New Stack*.

Catalyst is built on the open source [Distributed Application Runtime (Dapr)](https://dapr.io/), which the Diagrid team helped build at Microsoft, and its built-in workflow engine. For each supported agent framework, Diagrid provides a runner that intercepts the framework’s execution loop and registers its operations as workflow activities.

“We hooked into their agent runner lifecycle, and we’re essentially able to take the agentic steps that are being executed in real time and register them as workflow steps for our workflow engine in Catalyst,” Schneider says.

![](https://cdn.thenewstack.io/media/2026/07/d45f2419-catalyst-architecture-light-1024x504.png)

*Credit: Diagrid*

In a LangGraph application, for example, a developer compiles the graph as usual and passes it to Diagrid’s `DaprWorkflowGraphRunner`. Catalyst records the inputs and outputs of the model and tool calls. Dapr’s workflow runtime can then replay the orchestration after a crash, while returning the stored results of completed activities instead of executing them again.

It’s worth noting that for LangGraph users, this isn’t the first form of durable execution. [LangGraph’s own persistence layer](https://docs.langchain.com/oss/python/langgraph/persistence) saves state at superstep boundaries and supports resuming from the last successful step. Its Agent Server also provides a durable task queue and persistent checkpoints.

Diagrid’s argument is that Catalyst provides the same execution model across more than 10 frameworks and extends it to individual model and tool calls, without requiring developers to build separate recovery logic for each framework. Schneider says LangGraph is “without a doubt, hands down” the most common framework among Diagrid’s customers, with AWS Strands and Microsoft Agent Framework also showing up. All the other supported frameworks, he says, are in the long tail but easy enough to support that it makes sense for Diagrid.

## A signed record of the run

There is a second part to Catalyst 2.0, though, which may be just as important for many enterprise users. With this update, the tool now brings the workflow-history signing features introduced in [Dapr 1.18](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-history-signing/) to the supported agent frameworks.

“We keep like a ledger, like a diary,” Schneider says. “We log the input, we log the output, we log which systems we talk to.”

He describes the result as an immutable store but also notes that Catalyst doesn’t turn an arbitrary database into a blockchain. It creates a signed history that should reveal later modification.

Dapr computes a SHA-256 digest over batches of workflow-history events, links each digest to the previous signature, and signs the result with the Dapr sidecar’s [Secure Production Identity Framework for Everyone (SPIFFE)](https://spiffe.io/) identity. It stores these signatures and certificates alongside the workflow history and verifies the chain whenever it loads the workflow state. If somebody were to modify, remove, or reorder a stored event, that verification chain breaks.

Schneider says Catalyst customers can use their own certificates and retain the encrypted history so it can be inspected even if they are no longer running Catalyst. The platform can use a customer-selected database, while the hash chain supplies the tamper evidence.

## One part of the compliance problem

Diagrid is positioning that tamperproof record as useful for financial services, health care, and other regulated industries. CEO Mark Fussell says some of the financial executives the company has talked to see the lack of a verifiable record as a blocker for deploying agents in sensitive workflows.

The European Union’s AI Act is another reason Diagrid is making this argument now. [Article 12](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12) of the AI Act requires high-risk AI systems to support automatic event logging so operators can trace their behavior, identify risks, and monitor deployed systems, and a signed execution history could help with that requirement.

Fussell says Catalyst is meant to run alongside the agent services enterprises already use from the cloud providers. Teams can keep a provider’s identity, evaluation, and observability systems while using Catalyst for recovery and signed workflow history. Catalyst can run as a Diagrid-hosted service or in a customer’s environment, including air-gapped deployments.

Diagrid didn’t disclose pricing for the new release.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)