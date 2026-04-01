On Wednesday, security researcher Chaofan Shou discovered that Anthropic had shipped version 2.1.88 of Claude Code with a 59.8MB source map file attached to the npm package. Source maps are used to connect bundled production code back to the original source files during debugging, and this one connected the internet to 512,000 lines of unobfuscated TypeScript across 1,900 files.

Anthropic pulled the package within hours, confirmed it was due to a packaging issue caused by human error, but the mirrors were already on [GitHub](https://github.com/Kuberwastaken/claude-code). [*The Register*](https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/) reported the original repo was forked more than 41,500 times before the uploader replaced it with a Python port.

The coverage since then has focused on individual features. A Tamagotchi pet system. Animal codenames. Developer [Wes Bos](https://x.com/wesbos/status/2038958747200962952) posted that he went straight for the spinner verbs and found 187 of them, from “Ruminating” and “Philosophising” to “Flibbertigibbeting” and “Photosynthesizing.”



**The real story is more structural.** Independent analyses of the leaked codebase by [*VentureBeat*](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know), *The Register*, and dozens of developers reveal a production agent system that converges on the same design patterns the open-source ecosystem is also racing to build.

For developers who have worked with operating system internals, the patterns will feel familiar: Syscall interfaces with permission gates, process forking with capability-based isolation, background daemons for memory management, and compile-time feature flags for shipping strategy.

Claude Code is not a chat wrapper. The leaked source shows an agent operating system, and its architecture maps directly to patterns in [CrewAI](https://github.com/crewAIInc/crewAI), [Google ADK](https://github.com/google/adk-python), [LangGraph](https://github.com/langchain-ai/langgraph), and [AWS Strands](https://github.com/strands-agents/sdk-python) that teams are already evaluating for production deployments.

Claude Code’s tool system consists of more than 40 discrete capabilities, each implemented as a separate module with its own permission gate. File reads, bash execution, web fetches, LSP integration, and MCP server connections all live as individual tools that the agent invokes through a unified interface. The base tool definition alone spans 29,000 lines of TypeScript. Think of this as the syscall layer in a Unix kernel. The user-space program (the LLM reasoning loop) never directly touches hardware (the file system, the terminal, the network). Every interaction passes through a permission-checked gateway.

![](https://cdn.thenewstack.io/media/2026/03/0f03a531-claude-code-syscall-1024x1005.png)

This architecture solves the same problem that Kubernetes RBAC solves for pod-level API access. An agent that can read files but not execute bash commands operates under a different security profile than one with full shell access.

Claude Code enforces this at the tool level, gating each capability independently so that different contexts can grant different permission sets. Consider a scenario in which Claude Code operates within an unfamiliar repository. The tool system can restrict shell execution while allowing file reads and searches, preventing the agent from running arbitrary code in an untrusted environment without crippling its ability to understand the codebase. This is fine-grained capability security, and the leaked code shows Anthropic enforcing it through the same architectural pattern that POSIX systems have used for decades.

The 46,000-line Query Engine sitting behind the tool system handles all LLM API calls, streaming, caching, and orchestration. It is the largest single module in the codebase and acts as the kernel scheduler, deciding which tool calls to batch, which responses to cache, and how to manage the context window across long-running sessions.

## Multi-agent swarms and process orchestration

The leaked source reveals that Claude Code can spawn sub-agents with restricted toolsets, each running in an isolated context. Anthropic calls this system “swarms,” gated behind the `tengu_amber_flint` feature flag. The architecture supports both in-process teammates, using AsyncLocalStorage for context isolation, and process-based teammates that run in separate tmux or iTerm2 panes, with color-coded output for visual distinction. Team memory synchronization keeps the agents coordinated.

This is process forking with capability-based security. A parent agent identifies a parallelizable task, spawns child agents with a subset of its own permissions, and collects their results. The children cannot escalate their own access. They operate within the boundaries that the parent defined. The parallel to container orchestration is direct. In Kubernetes, a controller spawns pods with specific resource limits and RBAC bindings. In Claude Code, a coordinator spawns sub-agents with specific tool permissions and context boundaries.

CrewAI arrived at a similar pattern through its crew abstraction, where agents with defined roles collaborate on shared tasks. Google ADK uses hierarchical agent trees where root agents delegate to sub-agents. LangGraph models the same flow as nodes in a directed graph with explicit state transitions. All four systems solve the same problem. Complex tasks require multiple reasoning threads that run in parallel, share selective context, and merge their outputs. Anthropic built its version inside a closed-source CLI. The open-source ecosystem built equivalent versions using different metaphors. Convergence matters more than implementation details.

## KAIROS and the dream system as background services

The most revealing feature in the leak is [KAIROS](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know), an autonomous daemon mode referenced more than 150 times in the source. KAIROS transforms Claude Code from a request-response tool into a persistent background process. It maintains append-only daily log files, receives periodic `<tick>` prompts that let it decide whether to act proactively or stay quiet, and enforces a 15-second blocking budget so that proactive actions never interrupt the developer’s workflow for longer than a brief pause.

Think of KAIROS as a systemd service for an AI agent. It starts, persists, watches, and acts on its own schedule. When active, it uses a special output mode called “Brief” that delivers concise responses suited to a persistent assistant that should not flood the terminal.

The companion feature, autoDream, runs as a forked sub-agent in the `services/autoDream/` directory. During idle periods, it performs memory consolidation by merging observations from across sessions, removing logical contradictions, and converting tentative notes into confirmed facts. This is garbage collection for the agent state. Operating systems run background processes to defragment memory, consolidate logs, and clean caches. autoDream does the same thing for the knowledge an agent accumulates over days and weeks of continuous use.

None of the major open-source agent frameworks discussed here has shipped a comparable background autonomy feature. CrewAI, LangGraph, Google ADK, and AWS Strands all operate in request-response or workflow-trigger modes. The closest equivalent is [Hermes Agent](https://github.com/NousResearch/hermes-agent) from Nous Research, which recently added persistent multi-agent profiles with session memory, but without the proactive observation and consolidation loop that KAIROS implements. The gap between what Anthropic has built behind feature flags and what the open-source ecosystem currently offers is widest in this category.

## Compile-time feature gating as a shipping strategy

The leaked source contains 44 compile-time feature flags. At least 20 of them gate capabilities that are built and tested but do not appear in external releases. KAIROS, coordinator mode, voice mode with a full push-to-talk interface, ULTRAPLAN (a remote planning mode that offloads complex tasks to a cloud container running Opus 4.6 for up to 30 minutes), and Buddy (the Tamagotchi-style companion pet with 18 species and rarity tiers) all sit behind flags that compile to false in the external build.

This is how mature platform engineering teams ship software. Chrome, Android, and large-scale infrastructure projects at Google and Meta all use compile-time feature gating to decouple feature completion from feature release.

Engineers merge finished code into the main branch continuously. Product managers enable flags selectively for build targets, user segments, or deployment rings. The release cadence users see (a new Claude Code feature every two weeks) does not reflect the development cadence, which is much faster. The codebase also distinguishes between “Ant-only” tools that load exclusively for Anthropic employees and external tools available to all users.

Internal tools include telemetry dashboards, model-switching overrides, and the “Undercover Mode” system, which prevents Claude from revealing Anthropic’s internal codenames when contributing to public open-source repositories.

> Anthropic built an entire subsystem to prevent its AI from leaking internal details in git commits, then leaked the subsystem itself through a build configuration oversight.

The irony is sharp. Anthropic built an entire subsystem to prevent its AI from leaking internal details in git commits, then leaked the subsystem itself through a build configuration oversight.

The source also exposed internal model codenames that Undercover Mode was designed to hide. According to analyses of the leaked migrations directory, Capybara refers to a Claude 4.6 variant (the same model previously [reported](https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/) as “Mythos”), Fennec maps to Opus 4.6, and an unreleased model called Numbat remains in testing. Internal benchmarks show the latest Capybara iteration has a 29-30% false-claim rate, a regression from 16.7% in an earlier version, alongside an “assertiveness counterweight” designed to prevent the model from rewriting code too aggressively.

## What’s next

The accidental publication of Claude Code’s source provides a rare architectural benchmark. Permission-gated tool systems, multi-agent swarms, background daemons for memory management, and compile-time feature gating are not inventions unique to Anthropic. CrewAI, Google ADK, and LangGraph arrived at similar solutions for capability isolation and agent coordination through completely independent development paths. The convergence across those three layers confirms that these patterns are becoming the standard architecture for production agent systems, regardless of who builds them.

Background autonomy and memory consolidation across sessions are where Claude Code leads by the widest margin. None of the agent frameworks examined here has shipped anything comparable to KAIROS or autoDream. That gap will close faster now that thousands of developers have a concrete reference implementation to study.

The architectural details are fascinating. The security implications are immediate. The leaked source exposes Claude Code’s exact permission-enforcement logic, its hook-orchestration paths, and the trust boundaries it uses to decide when to execute code in unfamiliar repositories.

> “Your build pipeline is now part of your attack surface, and a single misconfigured ignore file can turn your most sophisticated product into an open blueprint.”

Attackers now have a roadmap for crafting repositories that exploit those specific mechanisms. The timing made it worse. A separate supply-chain attack on the widely used Axios npm package occurred within hours of the leak, injecting a remote-access trojan into versions 1.14.1 and 0.30.4. [*VentureBeat*](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know) reported that anyone who installed or updated Claude Code via npm on March 31 between 00:21 and 03:29 UTC may have pulled in the compromised dependency.

Anthropic has since designated its native installer as the recommended installation method, sidestepping the npm dependency chain entirely. Bun’s bundler generates source maps by default unless explicitly disabled, which suggests a likely mechanism for how a 59.8MB .map file ended up in the npm package, though Anthropic has not confirmed the specific build configuration that caused it.

The lesson for every team shipping AI agents through package managers is blunt. Your build pipeline is now part of your attack surface, and a single misconfigured ignore file can turn your most sophisticated product into an open blueprint.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)