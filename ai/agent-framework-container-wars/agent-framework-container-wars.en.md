As someone who had a front-row seat to the container orchestration wars, I am watching the same movie play out again with AI agent frameworks. It’s just that the cast is different, and the stakes are much higher, but the plot is almost identical.

In 2015, if you wanted to orchestrate containers, you had a plethora of choices. [Docker Swarm](https://thenewstack.io/docker-swarm-a-user-friendly-alternative-to-kubernetes/), Apache Mesos, Hashicorp Nomad, and, of course, [Kubernetes](https://thenewstack.io/kubernetes/) in its early form. Each had genuine technical merit. Smart people argued passionately for their pick. I remember sitting in conference halls watching vendors make compelling cases for why their orchestrator was the one.

By 2018, Kubernetes had absorbed the ecosystem. Not because it was technically superior in every dimension, but because it had the deepest hyperscaler backing, the strongest community gravity through [CNCF](https://thenewstack.io/cto-chris-aniszczyk-on-the-cncf-push-for-ai-interoperability/), and it became the default substrate for everything being built in the container world.

Today, I see developers facing the same bewildering choice of agent frameworks. LangGraph, CrewAI, [Google ADK](https://thenewstack.io/what-is-googles-agent-development-kit-an-architectural-tour/), [AWS Strands](https://thenewstack.io/aws-launches-its-take-on-an-open-source-ai-agents-sdk/), Microsoft Agent Framework, [OpenAI Agents SDK](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/), Mastra, Pydantic AI, and Agno. I have spent time with most of these, and I can tell you each one has something genuinely useful to offer.

But the real story is not about features. It’s about who controls what happens *after* you pick the framework.

## Free framework, paid runtime

Here is what most framework comparison articles miss. They line up features in a table and let you pick. That is like comparing container orchestrators in 2015 by listing which ones support health checks. It misses the game being played underneath.

The hyperscalers are not competing on framework features. They are giving away frameworks as on-ramps to their paid inference and deployment runtimes.

> The hyperscalers are not competing on framework features. They are giving away frameworks as on-ramps to their paid inference and deployment runtimes.

AWS released [Strands](https://strandsagents.com/latest/) as open source. It is deliberately thin. Three components: a model, tools, and a prompt. The Strands team was refreshingly honest about why. They [said](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/) their previous framework libraries “started to get in our way of fully leveraging the capabilities of newer LLMs.” But here is the part that matters. Strands is co-designed with [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/).

Strands is tightly integrated with Amazon [Bedrock AgentCore for production deployment and already underpins agentic](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/) features in Amazon Q Developer, AWS Glue, and VPC Reachability Analyzer. The Strands SDK itself is open source with no license fee, while Bedrock and Bedrock AgentCore are metered AWS services.

Google ADK follows the same playbook. It is open source on GitHub, multi-agent-native, with a genuinely impressive context-engineering architecture. Google’s engineering team [treats](https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/) context as a “compiled view over a richer stateful system.” That is serious systems engineering. But ADK is optimized for Gemini and comes with native connectors to Vertex AI, BigQuery, and AlloyDB. The framework is free. Vertex AI is not.

> “This is the GKE, EKS, AKS playbook applied to agents: Give away the orchestrator. Monetize the infrastructure underneath.”

Microsoft Agent Framework plugs into [Microsoft Foundry](https://ai.azure.com/), with [Entra Agent ID](https://www.microsoft.com/en-in/security/business/identity-access/microsoft-entra-agent-id) providing agent identity management. OpenAI’s [Agents SDK](https://openai.github.io/openai-agents-python/) is even more minimal. Three primitives: Agents, Handoffs, Guardrails. The bet is simple. If the framework is easy enough, you never leave the OpenAI API.

This is the GKE, EKS, AKS playbook applied to agents: Give away the orchestrator. Monetize the infrastructure underneath.

Then there are the independents. [LangGraph](https://www.langchain.com/langgraph) leads the pack with over 80,000 GitHub stars and the largest ecosystem. [CrewAI](https://www.crewai.com/) is popular for rapid prototyping. [Mastra](https://mastra.ai/) targets TypeScript developers. [PydanticAI](https://ai.pydantic.dev/) appeals to Python developers who want type safety. These are all model-agnostic, vendor-neutral, and genuinely useful.

But they all face the same existential question I watched Docker Swarm and Mesos face a decade ago. Can you build a sustainable business on a layer that hyperscalers are commoditizing from above?

## Smarter models, thinner frameworks

Here is where the agent framework story diverges from the container wars, and not in a way that helps the independents.

During the container orchestration era, the underlying technology (containers) did not improve dramatically in terms of self-orchestration. You always needed a scheduler. The orchestration layer was durable.

With agent frameworks, the opposite is happening. The models themselves are getting better at orchestration. AWS’s Strands team said this plainly: “We realized that we no longer needed such complex orchestration to build agents, because models now have native tool-use and reasoning capabilities.” What used to take months to make production-ready now takes days with a model-driven approach.

When [GPT-3.5 was state-of-the-art](https://thenewstack.io/donald-knuth-asked-chatgpt-20-questions-what-did-we-learn/), LangGraph’s graph-based orchestration was essential. Models could not reliably chain tool calls without explicit control flow. Today, with Claude Sonnet 4.6, Gemini 3 Pro, and Llama 4 Scout with its 10-million-token context window, models handle planning, tool selection, and self-correction on their own. The need for heavy framework orchestration shrinks with every model generation.

This means the independent frameworks are caught in a two-front squeeze. Hyperscaler runtimes commoditize the deployment and observability layers. Better models commoditize the orchestration logic from below. The framework layer is getting thinner.

## Where Value Actually Lives

If the framework layer thins out, where does the real value go? From what I have seen, building with these tools, four areas matter.

**Context engineering** is becoming the actual differentiator for production agents. Not how you orchestrate tool calls, but how you manage what the model sees. Google ADK’s [tiered context architecture](https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/) is ahead of the curve here. The team at Manus [rebuilt](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) their agent framework four times before getting context management right. This is where the hard engineering problems live now.

**Evaluation and observability** are where LangChain’s real moat lives, not in the chain abstraction, but in [LangSmith](https://smith.langchain.com/). [Langfuse](https://langfuse.com/), [Braintrust](https://www.braintrust.dev/), and [Ragas](https://www.ragas.io/) are also building in this space. AWS shipped Strands Evals with version 1.0. You cannot improve agents you cannot measure, and production agents need continuous evaluation pipelines.

**Agent security** is the emergent category nobody saw coming. A recent Gravitee report found that 88% of organizations experienced confirmed or suspected agent security incidents. Only 14% had full security approval for their agent fleet. Microsoft [published](https://www.microsoft.com/en-us/security/blog/2026/02/10/80-of-fortune-500-use-active-ai-agents-observability-governance-and-security-shape-the-new-frontier/) this week that 80% of Fortune 500 companies have active AI agents. However, most organizations still treat agents as extensions of human user accounts rather than as independent entities that require their own identities and access controls. This security layer is framework-agnostic, which means whoever owns it gains cross-framework leverage.

**Interoperability protocols** might be the most important shift of all. [MCP](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) is becoming the universal standard for tool integration. [A2A](https://a2a-protocol.org/latest/) handles agent-to-agent communication. Google’s ADK and Amazon’s Strands ship with support for both. If MCP and A2A harden into industry standards, the framework above them becomes a thinner commodity layer. This is exactly what happened when [Kubernetes standardized container orchestration](https://thenewstack.io/the-impact-of-containerization-on-apm-strategies/) while individual distributions competed on top of it.

## Where the analogy breaks

Now, here is where I have to be honest about the limits of my own analogy. The container orchestration war produced one clear winner because containers are a homogeneous abstraction. A container is a container. Workloads are portable by definition.

Agents are not like that. A coding agent, a customer service agent, and a data analysis agent have fundamentally different runtime requirements, tool chains, evaluation needs, and context patterns. This heterogeneity suggests the agent-based market framework might not consolidate into a single Kubernetes-style winner.

> “The ‘Kubernetes of agents’ might not be a framework at all. It might be the protocol layer.”

What I think happens instead is a fragmented but layered stack. Hyperscaler SDKs win for teams already committed to that cloud, because the framework-to-runtime co-design is a genuine engineering advantage. LangGraph maintains its position as a solution for complex workflows that require graph-level control and auditability. Lightweight model-driven SDKs like Strands and OpenAI’s work well for agents where the LLM handles orchestration itself. And protocols, MCP and A2A, become the unifying substrate underneath, the way TCP/IP unified networking without requiring everyone to use the same operating system.

The “Kubernetes of agents” might not be a framework at all. It might be the protocol layer.

## Pick protocols, not frameworks

If I were advising a platform engineering team today, and I do, here is what I would say.

First, bet on protocols, not frameworks. Design your tool integrations around MCP from day one. Adopt A2A for inter-agent communication. This is your hedge against framework churn, and there will be churn.

Second, invest in evaluation and observability independently of your framework choice. This layer outlasts any framework. Pick tooling that works across frameworks, not tooling that locks you into one.

Third, if you are already deep in a hyperscaler, use their SDK. The co-design between Strands and Bedrock, or ADK and Vertex, is a real engineering advantage. Do not fight that gravity. It is not worth the friction.

The container wars taught us that ecosystems, not features, win infrastructure battles. The agent framework shakeout will teach us whether that lesson still holds when the workloads themselves are as diverse as the intelligence running them.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)