**Kore wants to drag enterprise agent development out of the prompt-chain wilderness.** The agentic software company on Thursday released Artemis, the latest edition of its Kore Agent Platform. It’s a visual and code-based environment for building, governing, and optimizing multi-agent AI systems, built around a declarative blueprint language, a dual-brain runtime, and a machine architect that writes agents from plain-language objectives.

Somewhat quirkily defined as [multi-engine NLP](https://www.kore.ai/whitepaper/multi-engine-nlp-guide), Artemis is a multi-pronged NLP engine that employs so-called fundamental meaning (where sentences are broken down into grammar, synonyms, and concepts), machine learning, and knowledge graph technologies to form a service greater than the sum of its parts.

Described as no-code/pro-code (rather than [no-code/low-code](https://thenewstack.io/low-code-vs-no-code/)), Kore uses the term to denote its platform’s ability to allow developers to use both traditional programming languages, plus a crucial gateway connection to integrating APIs into the final multi-agent AI system.

## What makes Kore AI-native?

In an era when every software vendor is compelled to claim a level of inherent AI capability (and Kore can’t quite help itself, succumbing to using its .ai company name extension), the company claims to validate its position in this space with its trademarked Agent Blueprint Language (ABL).

Kore has explained ABL as a compiled, [declarative language](https://thenewstack.io/infrastructure-as-code-from-imperative-to-declarative-and-back-again/) that standardizes how AI agents, systems and workflows are defined, validated and governed. Six built-in orchestration patterns (supervisor, delegation, handoff, fan-out, escalation, and agent-to-agent federation) are in place to allow developers to build production-grade multi-agent systems.

Head of Products and Chief Technology Officer at Kore [Prasanna Arikala](https://www.linkedin.com/in/arikala/) tells *The New Stack* that ABL has been built for portability and governance from the get-go.

“Prompt-chain frameworks like LangChain, LlamaIndex, Semantic Kernel, and the hand-rolled orchestrator scripts most teams end up with are imperative: developers wire chains in code and discover schema drift, missing tool references, or broken handoffs only when an LLM call fails in production – ABL inverts that model,” Arikala says.

He explains that developers (or designers, via the visual editor) author a declarative blueprint consisting of agents, tools, memory, guardrails, supervisors, and topology in a typed DSL.

“Our parser and compiler statically validate the entire agent graph, surfacing contract mismatches, unresolved tools, unbound memory slots, and unreachable states *before* a single token is generated. The payoff is portability and governance,” he says.

More Kore trademarks are on offer with Arch, the organization’s agent architect. Not a person (although engineered to act like a human systems architect), this machine entity works to translate business objectives into production-ready ABL.

It supports the full agent lifecycle (i.e. design, build, train, extend, monitor and sometimes retire) and lays down the underlying agent topology, which means it is capable of continuously refining agent behavior using real-world production traces.

## The agent with two brains

Alongside the ABL language and the Arch agent architect (Archie would have been more entertaining, but we get it) Kore offers a third component in its triumvirate of AI-native tools. The company’s dual-brain architecture is a pair of two cognitive engines (combining both agentic reasoning and deterministic flows) that operate in parallel. The dual-brains work through shared memory, are authored in a unified language and governed by a single runtime.

CTO Arikala further explains what’s happening here and says that the dual-brain architecture pairs two execution engines on a shared, typed memory layer: a reasoning brain of LLM-driven agents that plan and improvise, and a deterministic brain of scripted flow agents that enforce business rules, transactions, SLAs, and compliance steps.

“The two brains never write into each other’s state unmediated,” clarifies Arikala. “Every memory slot in an ABL blueprint declares an owner, a visibility, and a write policy. Reasoning agents propose state changes; the deterministic engine commits them through the transactional store; the supervisor arbitrates conflicts using priority rules baked into the blueprint – this means deterministic logic wins on hard constraints, reasoning wins on advisory slots, and ties resolve to a human-in-the-loop step where the blueprint asks for one.”

By way of elevation, the Kore platform operates independently of the AI model in use. This separation of church and state is undertaken to keep AI systems predictable, auditable and scalable from their experimental prototyping stage all the way through to production-grade operations.

> “The architectural rigor stands out,” said Parikh. “Compiled blueprints, governance in a separate deterministic layer, and one language for every agent are the design choices enterprise AI has been missing.” – Keyur Parikh, Vanguard.

## Architectural rigor for agents

[Keyur Parikh](https://www.linkedin.com/in/keyur-parikh/) is head of workplace technology strategies and services at Pennsylvania-based financial services company Vanguard. As a Kore customer, Parikh has had early visibility into the Korei Agent Platform.

“The architectural rigor stands out,” said Parikh. “Compiled blueprints, governance in a separate deterministic layer, and one language for every agent are the design choices enterprise AI has been missing.”

CEO and founder of Kore, [Raj Koneru](https://www.linkedin.com/in/rajkonerufl/), has said that he thinks enterprise AI is entering its third wave, where governance, observability, and trust define success.

“The Kore Agent Platform reflects this shift by bringing an AI-native architecture to market that enables enterprises to build, manage, and optimise multi-agent systems with confidence,” said Koneru. “This level of depth comes from a decade of delivering AI experiences in complex, regulated environments, where scale, compliance, and reliability are non-negotiable.”

## This is AI, building, governing and optimizing AI

Koneru and team position this technology as AI, building AI. This assertion stems from the way Arch generates production-ready agents from plain-language objectives, writes them in ABL, and validates them before deployment.

It’s also AI governing AI i.e. every decision, path, and outcome is logged, traced, and analyzed by AI in real-time. Deterministic constraints and flow controls are enforced by the platform itself, not left to the agent.

Thirdly, it is said to be AI optimizing AI. The platform learns from production signals and recommends specific improvements as reviewable optimizations, with human oversight built in.

## What the CIO, CISO and CFO should think

For the third time using the power of three, Kore has a message for the CIO, CISO and CFO in relation to its release of Artemis.

For the CIO, it’s a manageability message – the platform consolidates fragmented third-party and home-grown agents into one foundation. For the CISO, AI behavior becomes predictable – governance is enforced at the platform layer, outside the model’s control.

Every agent action and policy decision is logged, timestamped, and traceable to a specific regulatory control.

Thirdly, for the third time, for the CFO, the company has suggested that AI investments are compounded – Arch, ABL and the runtime are shared infrastructure across every agent, so the marginal cost of the Nth agent approaches the cost of authoring its blueprint.

## Microsoft Azure compatibility

The Artemis edition of the Kore platform launches initially on Microsoft Azure, with a promise of “broader cloud availability” to follow. For enterprises standardized on the Microsoft stack, the Kore platform integrates with Microsoft Foundry, Microsoft Agent 365, Entra ID, and the Microsoft Graph API. It also powers a native Microsoft Teams channel through the Azure Bot Framework.

Customers deploy in public cloud, sovereign regions, private cloud, or on-premises, with data residency by region.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)