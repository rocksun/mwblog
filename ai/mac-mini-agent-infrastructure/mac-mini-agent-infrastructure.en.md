On April 30, Apple’s Q2 2026 earnings call did something unusual.

Tim Cook spent meaningful airtime on Mac mini and Mac Studio supply, telling analysts that both products are sold out across multiple configurations and that the supply-demand balance is “several months” away. He named the cause directly.

Cook credited agentic AI tools and workflows. CFO Kevan Parekh went further, citing Perplexity by name as a developer choosing Mac as the platform for enterprise-grade AI assistants. A week later, on May 7, Perplexity rolled out Personal Computer as a new Mac app available to all Mac users, with paid Pro, Max, and Enterprise tiers required for the full agent experience. The company’s own documentation describes Mac mini as the recommended way to run it 24/7.

This is not a product launch story. What happened over the past two weeks was the moment when three different agent runtimes were pulled toward the same answer to a question developers have been quietly asking for six months. Where should an always-on agent live? Perplexity is explicit about the Mac mini. OpenClaw recommends the Mac mini in its official hardware guide and through its community. [Hermes Agent](https://github.com/NousResearch/hermes-agent) is less Mac-specific, but its local-first Ollama path makes Apple silicon a natural fit. The pattern is difficult to ignore, and Apple’s supply data strengthens the case.

## A new substrate emerged without anyone planning it

Personal computing has always had reference hardware for new categories. The IBM PC defined the office. The Raspberry Pi defined the hobbyist server. Each became infrastructure not because a vendor declared it, but because a software ecosystem standardized on it. Mac mini is the latest entry in that lineage, and the catalyst is the persistent agent.

![](https://cdn.thenewstack.io/media/2026/05/465420a7-apple-mac-mini-thermal-architecture.gif)

A persistent agent is different from a chat session. It runs when you are not at the keyboard. It receives messages on Telegram while you sleep, drafts code at 3 a.m., monitors your inbox, and executes scheduled tasks against your calendar. It needs a host machine that stays on, runs quietly, integrates with the operating system the user already lives in, and costs less than a cloud VM over the course of a year. A Mac mini with 16 GB of unified memory and a quiet, low-power thermal design hits all four. Apple lists the 2024 M4 Mac mini at 4 watts at idle, roughly the cost of a nightlight. None of this was Apple’s design intent. Apple built the Mac mini for the small office and the home theater. The agent ecosystem repurposed it.

> Apple built the Mac mini for the small office and the home theater. The agent ecosystem repurposed it.

The clearest signal that this is no longer a niche pattern came from [Decrypt’s analysis](https://decrypt.co/366389/openclaw-apple-mac-mini-shortage-ai-2026) of the post-earnings shortage. Decrypt reported at the time that higher-RAM configurations of Mac mini and Mac Studio were carrying wait times of 16 to 18 weeks, that the 512 GB Mac Studio configuration previously offered had disappeared from the store, and that scalpers on eBay were listing base models at almost double retail. Those snapshot details will move, but the direction is consistent with what Cook said on the call.

## OpenClaw made Mac mini the default

[OpenClaw](https://thenewstack.io/persistent-ai-agents-compared/) is the clearest case of bottom-up standardization. The project surpassed 300,000 GitHub stars by early April 2026 and moved to an independent foundation backed by OpenAI after Peter Steinberger [joined](https://thenewstack.io/persistent-ai-agents-compared/) the company. The hardware story was not pitched by Steinberger or by OpenAI. It came from the community.

Setup guides written by individual developers like Dirk Paessler and Florian Darroman treat the Mac mini as the assumed deployment target. OpenClaw’s own documentation calls the Mac mini “quietly the best hardware for running OpenClaw” and lists macOS integration with iMessage, Shortcuts, Apple Notes, Reminders, and Keychain as the killer advantage no other platform delivers. That last point is the structural one. An OpenClaw agent on a Mac mini is not just running on Apple silicon. It is plugged into the same identity, calendar, and messaging surface the user already uses.

> An OpenClaw agent on a Mac mini is not just running on Apple silicon. It is plugged into the same identity, calendar, and messaging surface the user already uses.

The result is a deployment pattern that looks like infrastructure, even though no one designed it that way. A headless Mac mini in a data rack or on a shelf, running OpenClaw under a non-admin user account, reachable over Tailscale from a phone, FileVault on, skills installed deliberately. The community has converged on the same security posture and the same auto-start configuration. OpenClaw made the Mac mini the reference platform by accident.

## Hermes Agent makes Apple silicon a natural fit

[Hermes Agent](https://hermes-agent.nousresearch.com/) from [Nous Research](https://nousresearch.com/) is the least Mac-specific of the three, and that is what makes its presence in this pattern interesting. Where OpenClaw is breadth-first and ecosystem-heavy, Hermes is depth-first and learning-loop heavy. The project crossed 100,000 GitHub stars within weeks of its public release and now lists more than 800 contributors. Its tagline is “the agent that grows with you,” and its architecture pairs cross-session memory with autonomous skill creation. The agent persists what it learns, modifies its own skills when it finds a better path, and accumulates a model of the user across sessions.

Hermes is designed to run anywhere. The project’s own GitHub description calls out a $5 VPS, a GPU cluster, or serverless infrastructure as equally valid targets, and the framework supports more than 200 models through providers like OpenRouter, OpenAI, Anthropic, Nous Portal, and Google. What pulls Hermes into the Mac mini story is its [Ollama integration](https://docs.ollama.com/integrations/hermes), which routes the agent through a local OpenAI-compatible endpoint on Apple silicon.

Users who want a local-first agent with no recurring API spend gravitate toward the Mac mini for the unified memory architecture. A Mac mini with 32 GB can run quantized 30B-parameter models for inference at acceptable token rates, depending on context window and runtime, and a Mac Studio with 128 GB handles models that would have required a multi-GPU rig a year ago. The local-agent community noticed.

The two open-source projects disagree on almost everything. OpenClaw is API-key-first with a public skills registry and 50-plus messaging integrations. Hermes is provider-agnostic with a closed learning loop and a memory architecture inspired by ancient Greek loci. Where they overlap is the host. Both communities frequently tell new users that a Mac mini is the cleanest way to keep the agent running 24/7.

## Perplexity put a commercial name on the pattern

Perplexity’s product decision is what makes the convergence visible outside the open-source community. Personal Computer is a hybrid local-cloud agent that runs on the user’s Mac, with secure server execution available for connector-heavy tasks. It was [announced in March](https://www.perplexity.ai/hub/blog/perplexity-personal-computer), initially limited to Max subscribers on a waitlist, and rolled out to all Mac users via a new app on May 7.

The Pro and Enterprise tiers gained access at the same time, while the Max tier retains the heavier automation features. The Perplexity blog post that announced general availability describes the product as one that “takes Computer out of the cloud-only world and onto the device where most of your real work already takes place.” It calls out Mac mini as the deployment target for the always-on scenario, where a task can start from an iPhone, run on the Mac mini, and notify the user when it needs approval.

What makes this material is the company that shipped it. Perplexity is not an open-source community project. It is a venture-backed, model-agnostic, search-native company with a public roadmap and a sales team. Its harness, [Comet](https://comet.perplexity.ai/), already ships as a browser-native agent. Personal Computer extends that harness to local files and native Mac apps. Perplexity could have been built for any host. The company picked Mac as the substrate and was explicit enough about it that Apple’s CFO read its name out loud on the earnings call.

> Perplexity could have been built for any host. The company picked Mac as the substrate and was explicit enough about it that Apple’s CFO read its name out loud on the earnings call.

I’d argue this is the moment Mac mini stopped being a desktop and started being treated as agent infrastructure. Three runtimes with very different starting points settled on the same substrate, which is a recommended host, and Apple’s supply-side response is consistent with treating demand as durable. Apple announced in February that future Mac mini production would move to a new factory in Houston, a step consistent with treating Mac mini as a long-term category rather than a quarterly bump.

## How the three runtimes split the design space

The differences between them are sharper than the convergence on hardware suggests. They split the design space along three axes that matter for anyone choosing a runtime.

Inference strategy comes first. Perplexity is hybrid by design, running locally and reaching out to Perplexity’s secure servers when a task needs a stronger model or a cloud-based connector. OpenClaw is API-key-flexible, expecting you to bring your own model provider, with Anthropic Claude and OpenAI as the common defaults, and Ollama as the offline fallback. Hermes is provider-agnostic by design, with cloud and local paths both supported, though the Mac-mini-and-Ollama path is the one that pulls it into this story.

> OpenClaw leans heavily on macOS, with Apple Notes, iMessage, Reminders, Shortcuts, and Keychain as first-class targets.

Integration surface comes second. OpenClaw leans heavily on macOS, with Apple Notes, iMessage, Reminders, Shortcuts, and Keychain as first-class targets. Hermes leans on messaging platforms instead, where Telegram, Discord, Slack, WhatsApp, Signal, and email all reach the same agent core through a single gateway. Perplexity leans on the user’s existing workflow, opening with a keyboard shortcut, seeing the active apps, and orchestrating across local files, web tools, and 400-plus connectors.

The persistence model comes third. Perplexity persists in the task state in its secure environment. OpenClaw persists per-instance memory and skills under the user’s home directory, with manual configuration. Hermes persists everything through a closed learning loop that auto-generates skills, modifies them in place, and builds a dialectical model of the user across sessions. The same Mac mini can host any of the three, but they behave very differently after a month of running.

| Scenario | Likely fit | Why |
| --- | --- | --- |
| Hybrid local-cloud workflows with vendor support | Perplexity Personal Computer | Hybrid harness, 400-plus connectors, secure server execution |
| Messaging-heavy personal agent with deep macOS hooks | OpenClaw | Broadest integration surface, large community, BYO model |
| Local-first agent with persistent learning across sessions | Hermes Agent | Closed learning loop, cross-session memory, Ollama-native |

In practice, many developers run more than one. The Mac mini becomes the shared substrate, and the agents share the unified memory pool, the messaging clients, and the FileVault-encrypted disk.

## What’s next

Mac mini was never positioned as developer infrastructure. Apple’s marketing treated it as a starter Mac and a media server. The agent ecosystem repositioned it without permission, and the supply data is starting to reflect the new role.

> For developers, the practical takeaway is that personal AI agents are no longer browser tabs or cloud sessions. They are persistent processes on dedicated commodity Apple silicon.

For developers, the practical takeaway is that personal AI agents are no longer browser tabs or cloud sessions. They are persistent processes on dedicated commodity Apple silicon, and the cost curve favors owning the hardware over renting a VM.

The open question is what Apple does next. The Houston factory point suggests a longer commitment than a quarterly fix. High-memory Mac Studio configurations have been the hardest to find, and the high end of the lineup looks underbuilt for current demand.

The next 12 months will likely bring Windows ports, Linux variants, and competing dedicated hardware as the harness layer evolves. None of that changes the fact that three independent agent runtimes have made Apple silicon a recommended host on different principles, and Apple’s CFO named one of them on a public earnings call.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)