In 2025, vibe coding became more than a meme; it became a full-blown movement. Suddenly, non-developers were spinning up apps overnight, solopreneurs were grinding through 16-hour “just one more prompt” binges, and engineers were sharing “mind blown” moments at the pace of dopamine hits.

Yes, [vibe coding](https://thenewstack.io/to-vibe-or-not-to-vibe-when-and-where-to-use-vibe-coding/) was chaotic. Yes, it often produced AI-assisted spaghetti. But it also opened the gates of software creation to millions who had never touched a compiler. It [democratized](https://thenewstack.io/how-idps-and-ai-are-democratizing-platform-engineering-roles/) the joy of building and inspired a generation to imagine.

The challenge is that inspiration doesn’t equal production. At some point, you need a system.

## **Where Vibes Hit the Wall**

Studies often peg AI coding productivity gains at around 20%. That’s not because the tools are weak; it’s because most teams are sprinkling AI on top of old workflows. They’re coding the same way they did pre-AI, only with a fancier autocomplete.

There is the opposite side of the scale — people who master fleets of agents methodically chipping at their problems. For example, one of my engineers ran through 3.5 billion tokens in a month, often running four agents in parallel, and having agents review the work of other agents. When we adopted a disciplined system, our throughput doubled over the course of several months.

## **AI-First Engineering: The System**

Like agile in the early 2000s, AI-first engineering works as a system, not a menu of tricks. The key practices:

**Spec-driven development (SDD)**: Break work into three steps: Start with high-level spec → technical spec (with real interfaces, not pseudocode) → step-by-step execution plan. Let agents co-create, but keep humans in the loop. For example, if you want to add Google Calendar integration to your app, you’ll start by asking the agent to help you write product requirements. You would then review those requirements and edit them (manually or with follow-up prompting). You would then ask a different agent to read the product requirements, deeply analyze your repository and create a tech spec. You would then review the tech spec (by yourself and with the help of a different agent). And from there, you would ask the next agent to create a step-by-step plan from the spec.

The practice above allows you to reset agentic context often. The longer the agent runs, the higher the chance that the length of the context is going to start interfering with its reasoning capacity. Spec-driven development is a natural way to combine the right context with the right prompt. Metaphorically, think of it as humans working focused vs. distracted.

The next important concept is **self-verification**: That’s what made coding agents so much more powerful than the early versions of GPT. When prompted correctly, they try to test their work and correct the mistakes that they find on the way. Logging and telemetry help agents debug themselves — a huge step forward. When I jump into a new repo, before unleashing my coding agents, I first ask them to build some basic documentation for their future reference, then ask the agents to review and improve the logging and telemetry to make debugging easier.

And nowadays I rarely ask the agents to simply write the code. I prompt them to write tests first, the practice called test-driven development (TDD). This dramatically improves the agent’s self-verification capabilities.

Last, but not least, **keep it simple (KISS)**. Our main repository was getting so complex that our new hires could barely make sense of it. No AI agent would succeed in such a setup. It was time for us to refresh and simplify architecture. Cleaner repos aren’t just for humans; they make agents far more effective.

These practices together create a system strong enough to channel the vibes into real velocity.

## **The Infrastructure Layer**

Tools like [Claude Code](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/) and [Codex](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/) are revolutionizing the developer experience. But without orchestration, they can become fragmented: Duplicated configs, siloed agents, lost context.

That’s where platforms like Zencoder come in: A UI and orchestration layer on top of your existing AI subscriptions. Instead of choosing between [ChatGPT](https://thenewstack.io/openai-aims-to-make-chatgpt-the-operating-system-of-the-future/), Claude or [Gemini,](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) you can plug them all into one workflow, combine limits, run agents in parallel and get compliance, analytics and team-wide collaboration out of the box.

## **Moving Beyond the Hype Curve**

We’re still early. Today, the best teams can double throughput.

It still takes a rare combination of strong engineers, AI-first practices, frontier model access and repos that agents can digest. But that combination is growing, and so are the wins. The path to 10x lies in agent swarms with self-verification, which allows autonomous execution, which multiplies the parallel execution, supported by democratized access, where anyone can harness enterprise-grade inference through everyday subscriptions.

Vibe coding was the spark. AI-first engineering is the harness. And if history is any guide, once the system takes hold, the “we doubled our throughput” of today will feel like the warmup act.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/04/7ec426f6-andrew-filev_1000-600x600.png)

Andrew Filev is founder and CEO of Zencoder, an AI startup focused on empowering developers to code smarter, faster and with greater impact. Previously, Andrew founded Wrike, a collaborative work management platform was acquired by Vista Equity Partners in 2018...

Read more from Andrew Filev](https://thenewstack.io/author/andrew-filev/)