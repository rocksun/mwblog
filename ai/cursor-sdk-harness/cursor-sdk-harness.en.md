*I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

Cursor has spent the past two months telling the industry, in different ways, that it’s more than an IDE company. On Wednesday, it shipped [the Cursor SDK](https://cursor.com/blog/typescript-sdk), and on Thursday, Cursor’s harness team [published a long read on the agent harness](https://cursor.com/blog/continually-improving-our-agent-harness) — together, they package years of internal orchestration work and put it in any developer’s hands. In February, CEO Michael Truell [published an essay](https://cursor.com/blog/third-era) declaring this the “third era” of AI software development. And just last week, Cursor announced [a wild partnership with SpaceX](https://cursor.com/blog/spacex-model-training) to train the next generation of its proprietary Composer models on xAI’s Colossus supercomputer.

> Cursor thinks the AI model is becoming a commodity, and the product that wins the next decade is the harness around it.

Read together, the message is unambiguous: Cursor thinks the AI model is becoming a commodity, and the product that wins the next decade is the harness around it. The strongest confirmation came entirely from outside Cursor. Google told *The New Stack* this week that it doesn’t care which coding tool developers use, be it Gemini, Claude Code, or Cursor.

## Cursor is moving past being just an IDE company

The pieces have been sliding into place for months: This week, Cursor released an SDK that made the shift explicit. When Cursor 3 shipped [earlier this month](https://thenewstack.io/cursor-3-demotes-ide/), Jani MSV covered it for *The New Stack* with blunt terms: The IDE is now a fallback. Agents spin up dedicated cloud VMs, work for hours, and return logs, video recordings, and live previews. According to Truell’s “third era” post, agent usage at Cursor has grown more than 15x in the last year.

Twelve months ago, Cursor had 2.5 times as many Tab autocomplete users as agent users. Today, it has 2x as many agent users as Tab users. Inside the Cursor itself, Truell says more than a third of internal pull requests are created by agents working in cloud VMs. He expects “the vast majority” of development work to look that way within a year.

If Truell is right (and I think he is), the IDE will matter less, and the harness will matter more. That’s why on April 29, Cursor [released the Cursor SDK](https://cursor.com/blog/typescript-sdk) in public beta. It’s a Typescript package ( `npm install @cursor/sdk` ) that lets developers build agents directly on Cursor’s harness, model-agnostic, deployable locally or on Cursor Cloud against dedicated VMs.

The harness ships with codebase indexing, MCP server support, subagents, and observability hooks. This puts Cursor in the same race as OpenAI’s Agents SDK and Anthropic’s Claude Agent SDK, but with a harness that’s used at scale on its own users. Cursor positions Composer 2 as the cheap default — priced at $0.50 per million input tokens versus Claude Opus 4.6’s $5 per million input tokens — and claims competitive benchmark performance. But the SDK supports any model you want.

Cursor positions Composer 2 as the cheap default — priced at $0.50 per million input tokens versus Claude Opus 4.6’s $5 per million input tokens — and claims competitive benchmark performance. But the SDK supports any model you want.

The SpaceX partnership lands on top of all of this. Cursor’s blog states the company has been “bottlenecked by compute” and will now “leverage xAI’s Colossus infrastructure to dramatically scale up the intelligence of our models.” The partnership became even more interesting when [*Bloomberg*](https://www.bloomberg.com/news/articles/2026-04-21/spacex-says-has-agreement-to-acquire-cursor-for-60-billion) and *[TechCrunch](https://techcrunch.com/2026/04/21/spacex-is-working-with-cursor-and-has-an-option-to-buy-the-startup-for-60-billion/)* reported that SpaceX has said it will either pay Cursor $10 billion for the companies’ work together or acquire Cursor outright for $60 billion later this year. Musk likely isn’t buying Composer 2’s weights alone. xAI already has Grok and Colossus. The more strategic asset is Cursor’s harness and its line to developers who actually use these tools every day.

## What a harness is and why it’s suddenly the most valuable AI layer

A harness is the software wrapper that turns a raw frontier model — Claude, GPT, Gemini, Composer — into something that can actually do real work inside your codebase. The model is the brain; the harness acts on its instructions and provides feedback to the brain.

A harness picks which files, docs, commits, and tool outputs the model gets to see. This is context management, and Cursor’s harness team writes that doing it well is a multi-year engineering project. The harness calls tools: the terminal, the linter, the MCP server, and the internal APIs. It spawns subagents, even using separate models with separate prompts to better plan, edit, or debug in parallel. It runs hooks for observability, and it enforces security boundaries for better access control. And it stitches all of that into a loop that the model iterates inside until the task is done.

Harness’s work looks like unglamorous engineering. Cursor’s team writes that they spend “weeks” tuning the harness model-by-model because each one has different strengths and quirks. They warn about “context rot” — the way one bad tool call can poison every decision an agent makes after it. They run continuous A/B tests on real usage, watching a metric they call Keep Rate, which measures how much agent-written code actually survives in the final commit. None of that workshops into in a benchmark headline. All of it is what makes the difference between an agent that closes a ticket and one that ships broken code.

There’s a reason this matters beyond software: The same shape will replicate everywhere agents are eventually deployed. The model is what understands the legal contract, the patient chart, or the financial model. The harness is what gives it the right context, the right tools, the right boundaries, and the right oversight. Whoever owns the harness layer in your domain owns the product.

## Google’s “we don’t care” is proof that models are commodities

The most candid quote from a hyperscaler I’ve seen came from Google Cloud’s Chief Evangelist Richard Seroter. [As Frederic Lardinois writes on *The New Stack* this week](https://thenewstack.io/google-doesnt-care/), Seroter said: “developer loyalty is at zero right now.” Google’s position is that it doesn’t matter whether developers use Cursor, Copilot, Code, or Claude Code.

> Google’s position is that it doesn’t matter whether developers use Cursor, Copilot, Code, or Claude Code.

Six months ago, Google was racing to put Gemini inside VS Code. Now it’s apparently comfortable letting the harness vendors fight it out, because Google’s moats — search, Android, Cloud, the compute under the whole stack — sit at a different layer than the IDE entirely. When a company with a frontier model is comfortable with developers using someone else’s interface, it is at least acknowledging that the interface and infrastructure layers may matter more than model loyalty. That’s the cleanest expression of model commoditization I’ve seen, said out loud, by the company best positioned to know.

It’s not just Google. Two weeks ago, Jani [wrote on our site](https://thenewstack.io/ai-agent-harness-pricing-split/) that Anthropic, OpenAI, Google, and Microsoft all agree the harness is the product — they just disagree on what to charge for it. Anthropic’s Managed Agents pricing adds a hosted-agent runtime fee on top of model usage. Cursor’s SDK launched with per-token pricing on top of Composer 2 at a fraction of the Claude Opus’s rate.

The pattern is clear: Model providers are under pressure to make intelligence cheaper and more interchangeable, while harness vendors are charging for orchestration, observability, and the integration work that actually makes agents productive. Both Anthropic’s enterprise harness and Cursor’s SDK are betting on the same future: cheap, swappable intelligence and proprietary orchestration.

What this means for the rest of us depends on where you sit. If you’re a developer, the model you use day-to-day is going to keep changing under you, and your harness is going to keep getting smarter. Worry less about which model is the popular kid this month and more about whether your tools are designed to swap models gracefully.

If you’re a CIO, your AI vendor lock-in shouldn’t sit at the model layer — it should sit at the harness, and you should be asking vendors hard questions about how theirs handles context, tools, observability, and model-swapping.

If you work outside of engineering, don’t look away. The same architecture — commodity intelligence underneath, proprietary harness on top — is what’s coming next for legal, finance, operations, design, and editorial work. The companies building those harnesses are the ones who’ll own how the work gets done.

---

## Past Editions



[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)