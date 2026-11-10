On Monday, Anthropic [launched Claude Fable 5.2 and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2), the latest versions of its duo of flagship models.

Like before, Fable 5.2 will be available on all platforms today, including Amazon Web Services, Google Cloud, and Microsoft Azure, while direct access to Mythos remains limited to organizations in Anthropic’s [Cyber](https://www.anthropic.com/news/cyber-verification-program) and [Life Sciences](https://www.anthropic.com/news/life-sciences-verification-program) verification programs.

Also like before, Fabe and Mythos share the same underlying model, but Fable ships with stricter cybersecurity and biology safeguards.

It’s maybe a bit of a surprise that Anthropic didn’t designate these models as “5.5,” given that its Claude Opus, Sonnet, and Haiku models are now at that version number.

The company stresses that it continues to recommend that users go with Opus 5.5 for most coding and knowledge tasks, while Fable 5.2 is meant to help users “tackle the most daunting technical challenges.”

And while both models show improvements in coding, reasoning, and vision, according to Anthropic, one feature the company is stressing here is speed. Fable 5.2 and Mythos 5.2, the company says, generate output up to 30 percent faster than Fable 5.1 and Mythos 5.1, respectively.

![](https://cdn.thenewstack.io/media/2026/11/df96c5c9-screenshot-2026-11-09-at-11.06.08-am-800x1024.png)

Credit: Anthropic.

## Fable Fast mode

For those who want an even faster response, there is now also a Fast mode for both models, which Anthropic says speeds up token generation by up to 2.5 times.

It is available in Claude Code, on the Claude Platform, through Claude Models on Google Cloud, and through Anthropic-hosted Microsoft Foundry.

## Pricing

As for pricing, Fable still carries a premium over Opus, but Anthropic is cutting the price from $10/$50 per million input/output tokens to $8/$40. Mythos 5.2 gets the same rates.

OpenAI’s flagship [GPT-6 Astra still costs $10/$50](https://developers.openai.com/api/docs/models/gpt-6-astra) at its standard rates for prompts of up to 272,000 input tokens, putting Anthropic 20 percent below its rival on those token rates (at least for the time being).

Fast mode costs $16 per million input tokens and $80 per million output tokens for either model, twice the standard rates.

Even after the price cut, Fable’s standard input and output rates are twice [Opus 5.5’s current prices](https://platform.claude.com/docs/en/about-claude/pricing), though Anthropic’s new evaluations suggest that doesn’t necessarily translate into a higher cost per task.

## Fable 5.2 targets complex coding

On FrontierCode 2.0, Anthropic reports that Fable 5.2 scored 49.1 percent, compared with 32.4 percent for Fable 5.1, 45.5 percent for Opus 5.5, and 42.8 percent for GPT-6 Astra. On FrontierSWE v2, it scored 69.9 percent, ahead of Astra’s 65.5 percent and Opus’s 62.3 percent.

The cost comaprison with Opus may be even more interesting, though. In early FrontierCode 2.0 testing, Anthropic says Fable 5.2 at High effort performed about as well as Opus 5.5 at Max effort for roughly half the cost per task.

Medium is now the default effort level for Fable 5.2 in Claude apps and Claude Code.

It’s worth noting that the results aren’t a clean sweep for Fable 5.2, though.

Gemini 4 Carbon leads Fable on AutomationBench, which tests business workflows, at 53.9 percent versus 51.4 percent. Meanwhile, Opus still retains a small lead on the Elo measure of AA-Briefcase v1.1, a knowledge-work evaluation.

Anthropic says Fable can act as an adviser that smaller models consult on harder problems, or as an orchestrator that delegates simpler tasks to them. In one internal experiment, an engineer asked Fable 5.2 to build a prototype operating system from an empty folder.

The company says it coordinated more than 1,000 subagents over eight days and produced an OS that boots on a laptop, complete with drivers, persistent storage, a graphical interface, and an installer.

## Fable promises fewer safety blocks

Anthropic says Fable 5.2’s cyber and biology safeguards remain as robust as those in 5.1. In early testing across Claude.ai, Claude Code, and Cowork, the company observed about 55 percent fewer blocks overall, including about 60 percent fewer in cybersecurity and 40 percent fewer in biology.

That could reduce interruptions to legitimate work, though fewer blocks don’t necessarily mean broader permissions. Fable still blocks high-risk cyber activities, including penetration testing and exploit generation, as well as most research biology tasks. When a query is blocked, Anthropic says users instead receive a response from Opus 4.8 for cybersecurity or Opus 5 for biology.

Direct Mythos access remains gated, but there is another route for enterprise security work: Claude Enterprise customers can use Claude Security, which now includes Mythos 5.2, even if they aren’t members of the Cyber Verification Program.

Anthropic also says it deliberately limited improvements in certain AI-development capabilities during training, including accelerator kernel optimization and work on large language model architectures. In those areas, the models perform at about Opus 5.5’s level, according to the company. It says those limits do not affect agentic coding, hardware development, or traditional machine learning research.

For API developers, Anthropic is expanding preserved thinking to all accounts. The feature restricts changes to Claude’s prior context that could be used to extract its reasoning for distillation.

## Enterprise safeguards enter private beta

[Enterprise Frontier Safeguards](https://www.anthropic.com/news/enterprise-frontier-safeguards), which the company first announced in September, is also moving into private beta, with Bridgewater, Salesforce, and Stripe among the early customers. Automated safety monitoring runs on prompts and responses stored in customers’ own infrastructure, making it compatible with zero data retention, Anthropic says.

Eligible customers can continue using Fable 5.2 and Mythos 5.2 with zero data retention before implementing the system. For other customers, Anthropic retains data for 30 days for safety monitoring.

## Fable for physics

Anthropic argues that its models’ coding abilities also apply to scientific research because so much of that work is also based on software, including analyzing data, modeling molecules, designing parts, or controlling instruments.

The company says Fable 5.2 solved two open theoretical-physics problems involving black holes and holographic duality. One involved completing a calculation proposed in 2003 to determine whether black-hole formation remains an abrupt transition in a small-universe quantum description. The other established the limit of a technique used to rule out candidate theories of quantum gravity in a simplified universe.

The Fermat claim is more specific than the early announcement suggested. Anthropic says a team of 1,000 Fable 5.2 agents fully formalized the proof of Fermat’s Last Theorem in Lean in 30 hours, with minimal human intervention. Formalization expresses a proof in a language that a computer can check step by step; it is distinct from discovering a new proof.

The agents received a list of intermediate theorem statements to measure progress, but no mathematical references, according to Anthropic. An earlier research version of Claude took 11 days with a purpose-built harness and human guidance. The company’s comparison used a single run per model, with Opus 5.5 reaching 26 percent after 18 hours and making little additional progress by 30 hours.

Anthropic also tested Fable 5.2 on hardware design, working with circuit-board company Diode to produce a voice-assistant hub, a USB speakerphone, and a handheld virtual pet. The company says Claude selected components, designed the boards and enclosures, and wrote the software. Diode built the boards, and its engineers tested and assembled the devices with Claude’s guidance.

All three worked without electrical modifications, according to Anthropic.

[AI Engineer
Step by step guide to becoming an AI Engineer in 2026

Introduction
Working With LLMs
Context Engineering
AI Models
Embeddings & Vector Databases
Embedding Models
RAGs
AI Agents
AI Safety and Ethics
Evaluation & Observabiity](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=anthropic-fable-coding-upgrade)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)