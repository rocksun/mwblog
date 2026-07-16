OpenAI announced [ChatGPT Work](https://thenewstack.io/openai-codex-work-atlas/) on July 9 and began rolling it out to Pro, Enterprise, and Edu users. It runs on the new GPT-5.6, opens a user’s local files, edits Google Workspace and Microsoft 365 documents, and carries a multi-step task through to a finished deliverable.

Reuters placed it directly against Anthropic’s [Claude Cowork](https://thenewstack.io/claude-cowork-cloud-mobile/), and both target the same person — a non-coder who wants the power of a coding agent without the terminal. Counting Anthropic, Microsoft, Perplexity, and Amazon, five leading labs have now released an agent of this kind. The batch shows that the newest agents are organized more by their intended users than by their functions.

Based on the target user persona, four archetypes appear: the knowledge worker, the power user who self-hosts, the developer, and the enterprise. The personas often overlap since one individual can embody all three roles. Additionally, a product like [Claude Code](https://thenewstack.io/claude-code-and-the-rise-of-personal-software/) caters to both solo developers and platform teams.

Therefore, consider these deployment archetypes categorized by the main buyer, rather than strict separations. The archetype only represents what marketing promotes. Behind the scenes, each lab has almost consistently decided who owns the runtime, persists memory, manages credentials, and enforces policy.

## Four archetypes, based on the user persona

Let’s analyze each of the four archetypes individually, as each differs in the level of control available to users.

The first archetype serves the knowledge worker. A vendor operates the runtime and sells the agent as a delegation to someone who lives in documents rather than code.

ChatGPT Work is the newest, alongside Claude Cowork, which now runs cloud sessions on web and mobile while keeping local-file access on the desktop; Microsoft’s Copilot Cowork, a cloud-hosted agent that executes long-running tasks inside the Microsoft 365 trust boundary; [Perplexity Computer](https://thenewstack.io/perplexity-computer-vibe-coding-openai-anthropic-pentagon/), which works across local files and Microsoft apps; and Amazon Quick, the successor to Q Business as that product closes to new customers at the end of July. The user grants access and supervises the result. In most cases, the vendor manages the runtime and persisted state, except for Perplexity’s local option.

A second archetype belongs to the power user who self-hosts. The provider controls the persistent agent process and chooses where to store the state and credentials, often on a [Mac mini that has become a piece of personal infrastructure](https://thenewstack.io/mac-mini-agent-infrastructure/) in its own right.

[OpenClaw](https://thenewstack.io/openclaw-foundation-nonprofit-status/) and [Hermes](https://thenewstack.io/persistent-ai-agents-compared/) are the reference examples, open source, and run on the operator’s own machine. Self-hosting involves managing the control plane rather than full local custody, since both options still allow access to a hosted model and the storage of credentials for external services.

**Related reads:**

“Microsoft has proved it can survive major changes in the tides of technology… Today, it faces another evolution in one of its core cash cows, as late-stage unicorns and AI labs alike push deeper into Office territory.”

[→  *Read more in Cautious Optimism*](https://www.cautiousoptimism.news/the-ai-agents-are-coming-for-microsoft-office/?utm_source=The+New+Stack&utm_medium=referral&utm_campaign=Article+Quote+Box)

The developer gets the third archetype, whose runtime spans the IDE, the terminal, the repository, and a cloud sandbox. Claude Code, [OpenAI Codex](https://openai.com/codex/), [GitHub Copilot](https://github.com/features/copilot) in agent mode, and the open-source [OpenCode](https://opencode.ai/) all live here, and Amazon’s developer agent is folding into its Kiro tool. Coding-agent execution is extending from the local IDE to vendor-managed sandboxes and asynchronous cloud workers, making this the most challenging archetype to categorize clearly.

The fourth archetype is built for enterprise workflows and integration with business processes. They run an open agent framework, such as LangGraph or CrewAI, on a managed, governed runtime. ADK on the Gemini Enterprise Agent Platform, Strands on the [Bedrock AgentCore](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/), Microsoft Agent Framework on Foundry Agent Service, and Claude Managed Agents belong to this category. [OpenAI’s Agents SDK](https://thenewstack.io/openai-agents-sdk-sandboxes/) can be hosted on some of these runtimes, including AgentCore, which AWS lists as one of its supported frameworks. The vendor operates the infrastructure, and the customer configures identity, policy, and retention on top of it.

| Persona | Representative products | Runtime ownership | State and credentials | Platform type |
| --- | --- | --- | --- | --- |
| Knowledge worker | [ChatGPT Work](https://chatgpt.com//), [Claude Cowork](https://www.anthropic.com/product/claude-cowork), [Copilot Cowork](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/), [Perplexity Computer](https://www.perplexity.ai/hub/blog/everything-is-computer), [Amazon Quick](https://aws.amazon.com/quick/) | Vendor cloud for most, with per-folder local access on some | Vendor persists session state, user grants scoped credentials | Packaged experience |
| Power user, self-host | [OpenClaw](https://github.com/openclaw/openclaw), [Hermes](https://github.com/NousResearch/hermes-agent) | The operator’s own machine | Operator chooses where state and tokens live, though inference is often external | Packaged experience, self-operated |
| Developer | [Claude Code](https://www.anthropic.com/claude-code), [OpenAI Codex](https://github.com/openai/codex), [GitHub Copilot](https://github.com/features/copilot), [OpenCode](https://opencode.ai/) | Split across the IDE, the laptop, and a cloud sandbox | Repo and local for now, drifting into hosted sandboxes | Swing, moving toward platform |
| Enterprise, workflow-driven | [ADK](https://adk.dev/) on [Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform), [Strands](https://strandsagents.com/) on [AgentCore](https://aws.amazon.com/bedrock/agentcore/), [MAF](https://learn.microsoft.com/en-us/agent-framework/) on [Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/overview), [Claude Managed Agents](https://www.anthropic.com/engineering/managed-agents) | Managed vendor runtime, customer-configurable | Customer defines identity, policy, and retention; platform brokers | Programmable platform |

## The line below the personas

The persona-based approach abstracts four things: where execution runs, where state is persisted, how authority is delegated, and where policy is enforced.

Anthropic describes its design as decoupling the brain from the hands. The harness that calls Claude runs separately from the sandbox where code executes, and a session, an append-only log of every model call, tool call, and result, connects the two. Because the sandbox is kept separate from the brain, the agent can start reasoning before any container exists, and the code it runs remains far from the developer’s credentials.

The same four planes show up at the other vendors. AgentCore Runtime gives each session a dedicated microVM with an isolated CPU, memory, and filesystem, and meters compute usage. [Google can route governed traffic through its Agent Gateway](https://thenewstack.io/google-debuts-gke-agent-sandbox-inference-gateway-at-kubecon/), where Model Armor policies inspect configured ingress and egress flows, while Agent Identity and an Agent Registry track the fleet. Microsoft assigns each hosted agent a dedicated Entra Agent ID and runs it in a per-session sandbox whose filesystem survives idle periods.

> Deploying agents on a managed runtime is more like leasing a workshop than purchasing a tool… a long-term tenant installs their own locks, maintains their records, and takes their tools when the lease ends.

Deploying agents on a managed runtime is more like leasing a workshop than purchasing a tool. The landlord manages the building and supplies the power, but a long-term tenant installs their own locks, maintains their records, and takes their tools when the lease ends. The personas often conceal this difference. Currently, the vendor typically operates the runtime, so the key question is how much control the customer can still exert and what they can take away across the four planes.

## Where the line falls

What differentiates each offering is not the compute operator, since vendors handle nearly all of it. It is how much of those four planes a product leaves the customer to configure and export. A packaged experience hands nearly all four to the vendor and returns supervision and a finished outcome. A programmable platform operates the infrastructure but lets the customer define identity, policy, and retention and move the code elsewhere.

Copilot Cowork shows that the two axes are separate. It is a packaged knowledge-worker experience, yet it runs on a governed enterprise platform and inherits Microsoft’s identity, compliance, and audit controls.

> The persona sells the product, but the four planes decide the lock-in.

A product can be packaged on the surface and programmable underneath, which is why the personas and the control planes have to be read as different questions. ChatGPT Work makes the same point from the developer side, since [OpenAI’s new desktop app](https://thenewstack.io/openais-codex-desktop-app-is-all-about-managing-agents/) folds Chat, Work, and Codex into a single surface, though OpenAI has not detailed how far the runtime or credential store are shared beneath it. The persona sells the product, but the four planes decide the lock-in.

| Usecase | Agent Type | Tradeoff |
| --- | --- | --- |
| Delegate a knowledge task to an agent you supervise | A knowledge-worker agent such as ChatGPT Work, Copilot Cowork, or Amazon Quick | The vendor typically operates the runtime and persists state, and you configure little below the surface beyond access and approval |
| Keep state and credentials on hardware you control | A self-hosted agent such as OpenClaw or Hermes, in a local configuration | You control the persistent process, though model inference and some tools may still be remote |
| Ship code changes across the IDE, repo, and CI | A developer coding agent such as Claude Code, Codex, or Copilot | Execution spans your tools and a cloud sandbox, so ownership is split and worth mapping before you commit |
| Run many governed agents with audit and identity | An enterprise runtime platform such as AgentCore, Agent Platform, Foundry, or Managed Agents | The vendor operates the infrastructure while you define identity, policy, and retention, in exchange for coupling workflow logic to one cloud |

Real deployments combine the rows rather than picking one. Teams on Foundry Agent Service commonly run open-source orchestration, such as LangGraph, for agent logic while leaning on the platform for governed execution, and Microsoft’s own hosted runtime now supports long-running personal agents like OpenClaw and Hermes with durable state. The boundary between experience and platform is not a thick, well-defined boundary, but a thin line a single system can cross, bridging rival camps.

> The agent market is not being decided by open against closed. Open frameworks like Strands, ADK, and [Microsoft Agent Framework are precisely what the governed runtimes](https://thenewstack.io/microsoft-scout-openclaw-runtime/) are built to host.

The agent market is not being decided by open against closed. Open frameworks like Strands, ADK, and Microsoft Agent Framework are precisely what the governed runtimes are built to host. Vendors now manage the runtime across nearly all archetypes, shifting the competition to who can most effectively configure and export state, identity, and underlying policy.

If coding agents enter managed sandboxes alongside knowledge-worker agents, the developer archetype will be established on the platform side. The map will then transform into what the vendors are already outlining. When enterprise teams assess agents, their most important question should be how much of execution, state, identity, and policy they can configure and extract from the product. They should not focus on which persona it presents or whether its framework is open, as the framework no longer determines the product’s value or locking-in capabilities.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)