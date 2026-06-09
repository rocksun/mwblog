The [agentic AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/) wave has produced no shortage of impressive demos. What it has produced less of is agents that hold up in production — under real load, real data, real compliance requirements.

At the recent [Microsoft Build 2026](https://news.microsoft.com/build-2026/) conference, the company addressed that gap directly, shipping a cluster of updates to [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) that collectively add up to something closer to an enterprise runtime than a developer preview.

The company shipped a broad cluster of updates to [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) spanning hosted agent infrastructure, evaluation tooling, an open governance specification, memory, knowledge retrieval, and expanded model options. Taken piece by piece, each is a reasonable product update. Taken together, they suggest Microsoft has decided the next competitive front in enterprise AI isn’t capability — it’s reliability and governability.

> It seems that Microsoft has decided the next competitive front in enterprise AI isn’t capability — it’s reliability and governability.

“At Build 2026, Microsoft Foundry added more of the platform pieces developers need for production agents: runtime, tools, memory, grounding, models, observability, and governance,” writes [Nick Brady](https://www.linkedin.com/in/nicholasdbrady/), senior program manager for developer experience at Microsoft, in a [blog post](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026/) recapping the announcements.

## A runtime that doesn’t require a rewrite

The anchor of the infrastructure story is hosted agents in [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/overview), which Microsoft expects to reach general availability by early July 2026. The setup is a managed runtime where every session runs in its own sandbox with dedicated compute, memory, and durable filesystem access.

What makes it worth paying attention to is the framework posture. Agents built on [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), [GitHub Copilot SDK](https://github.com/github/copilot-sdk), [LangGraph](https://www.langchain.com/langgraph), or other SDKs can be deployed without rewrites. Two protocols are supported: a Responses API for OpenAI-compatible, stateful interactions, and an invocations protocol for pass-through scenarios in which developers control the request and response formats themselves. That second option is going to matter for teams that have already built custom orchestration they’re not about to discard.

The hosted runtime also supports routines, now in public preview, which let any agent run on a timer or schedule — overnight issue triage, daily reporting, that kind of workload. Long-running autonomous agents get durable state.

Alongside the runtime, [Foundry Toolkit for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) is now generally available. Brady described it as the tool that lets developers “create agents from templates or with GitHub Copilot, debug runs locally with trace visualization, connect to Toolboxes, and deploy to Foundry Agent Service from VS Code.”

As agent tool counts grow, tool governance becomes an engineering problem in its own right. Toolboxes in Foundry, now in public preview, gives an agent a single managed endpoint for every tool type. Configure once, point any MCP client to a single URL, and Foundry handles auth, lifecycle, and governance.

Skills, versioned in a project-scoped catalog and discoverable as MCP resources, are now first-class citizens in the Toolboxes model. A tool search capability, also in preview, helps select appropriate tools per task rather than dumping the entire catalog on the model. That matters both for quality and for keeping context windows from bloating.

Toolboxes also connect to [Microsoft IQ](https://www.microsoft.com/en-us/ai/microsoft-iq) — including Work IQ, Fabric IQ with the Fabric data agent, Ontology, and semantic models — so agents can tap into enterprise data without custom plumbing for each source.

## Evaluating against policy, not just benchmarks

Two governance announcements stood out. The first is [Adaptive Spec-driven Scoring for Evaluation and Regression Testing (ASSERT),](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/) Microsoft’s new open-source framework for policy-driven agent evaluation, built on Microsoft Research work. Rather than running agents against static benchmarks, ASSERT converts written policies into concrete, measurable evaluations and generates targeted scenarios to surface safety and quality defects before they reach production. It works across [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/), CrewAI, [LightLLM](https://github.com/ModelTC/lightllm), OpenAI, and other frameworks.

The second is [Agent Control Specification (ACS)](https://commandline.microsoft.com/agent-control-specification-runtime-governance/), an open industry spec for placing deterministic safety and security controls at five checkpoints in an agent’s lifecycle: input, LLM, state, tool execution, and output. ACS is expressed as a portable YAML contract — versionable, auditable, and framework-agnostic. Launch partners include Infosys, KPMG, IBM, Aviatrix, BigSpin, and CrewAI.

The combination points to a real problem. Agent failures in production tend not to be random — they cluster around predictable input types, tool misuse patterns, and output edge cases. ASSERT makes those failure modes testable. ACS makes the controls portable across frameworks and auditable across organizations.

Rounding out the evaluation stack: [Guided Guardrail Setup](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guided-set-up), a questionnaire-driven wizard in [Foundry Agent Builder](https://pnp.github.io/blog/post/copilot-studio-vs-agent-builder-vs-foundry/) that recommends PII filters, jailbreak protection, and task adherence controls without requiring security expertise; and a Rubric evaluator that auto-generates weighted quality criteria from an agent’s definition and use case.

## Memory and knowledge

Memory in Foundry Agent Service, in public preview, now covers three types. Procedural memory, new at Build, helps agents learn how to do the work across runs — not just what was said in a session. Brady cites early Tau-bench results showing +7–14% absolute success-rate gains at near-baseline cost, which is specific enough to warrant independent replication. User memory retains preferences and facts across sessions. Session memory maintains context within a thread.

On the knowledge side, Foundry IQ got a serverless option in public preview, new knowledge sources spanning Work IQ, Fabric IQ, File Search, Azure SQL, and MCP, and knowledge bases generally available with SLA-backed retrieval. Brady described the pitch as replacing custom RAG pipelines with “a dedicated knowledge layer behind your Foundry agents.” Web IQ adds sub-200ms web grounding with zero data retention for agents that need live external context.

## Models and compute

Microsoft announced four first-party MAI models entering public preview: MAI-Thinking-1 for chat and reasoning, MAI-Image-2.5 for image generation and editing, MAI-Transcribe-2 for speech-to-text with speaker diarization, and MAI-Voice-2 for multilingual text-to-speech with voice cloning.

[Fireworks AI on Foundry](https://azure.microsoft.com/en-us/blog/introducing-fireworks-ai-on-microsoft-foundry-bringing-high-performance-low-latency-open-model-inference-to-azure/) reached general availability, bringing open-model inference through a single Azure endpoint with enterprise SLAs, SOC 2 readiness, and PTU Data Zone support — enterprise access to open models without separate infrastructure or contracts.

Microsoft also claimed that Frontier Tuning is more than 10x as cost-efficient as GPT-5.5 for tasks such as producing technical Microsoft documentation. That’s specific enough to be testable and general enough to warrant skepticism until it is.

## The bigger picture

What Brady’s recap makes clear is that the Foundry announcements at Build 2026 were designed to fit together. The hosted runtime handles deployment. Toolboxes handle tool governance. ASSERT and ACS handle evaluation and control. Memory handles state. Foundry IQ handles grounding. Rubric and Agent ROI connect agent performance to business outcomes. Rubric is a new evaluator type in Microsoft Foundry, currently in public preview, that automatically generates evaluation criteria based on your agent’s specific context.

Microsoft argues that enterprise agentic AI requires platform-level infrastructure — and that the platform should be Foundry.

Whether that argument lands will depend less on what shipped at Build and more on what enterprises actually find when they try to move agents from demo to deployment.

That is the gap Microsoft says it’s closing.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)