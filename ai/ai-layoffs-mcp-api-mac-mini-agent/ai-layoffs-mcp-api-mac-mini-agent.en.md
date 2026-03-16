*I’m Matt Burns, Head of Content at Insight Media Group. Each week, I round up the most important AI developments and explain what they mean for people actually putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries. This newsletter is here to help you be one of them.*

---

**This week:** Jobs are being replaced by AI, and companies are no longer making excuses. The MCP toolchain is already facing a backlash as some call for APIs to replace it. Mac Minis are becoming the default choice to host AI agents. Replit and other vibe coders raised serious funding. And Claude is adding a million users a day.

## AI is causing layoffs (obviously)

Companies aren’t hiding behind empty excuses anymore. [Atlassian cut 1,600 people this week](https://www.cnbc.com/2026/03/11/atlassian-slashes-10percent-of-workforce-to-self-fund-investments-in-ai.html) – 10% of its workforce – and pointed at AI as the cause, saying the layoffs would “self-fund further investment in AI and enterprise sales.” This is essentially a swap. Headcount out, AI in. Atlassian’s CTO is stepping down at the end of March.

Atlassian’s announcement comes weeks after [Block CEO Jack Dorsey fired 4,000 employees](https://x.com/jack/status/2027129697092731343), nearly half of its 10,000 employees at the time. Dorsey said the cuts were driven by AI automation.

*Reuters* is [reporting this morning](https://www.reuters.com/business/world-at-work/meta-planning-sweeping-layoffs-ai-costs-mount-2026-03-14/?utm_campaign=svc-beehiiv&utm_medium=referral&utm_source=newsletter.strictlyvc.com) that Meta is planning on cutting 20% of its workforce as it anticipates AI creating smaller teams.

They’re not alone. [*Bloomberg* reported that Oracle](https://www.bloomberg.com/news/articles/2026-03-05/oracle-layoffs-to-impact-thousands-in-ai-cash-crunch) is planning to cut thousands of jobs to handle a cash crunch from massive AI data center expansion, with [some estimates](https://qz.com/ai-layoffs-oracle-data-centers-costs) putting the real number as high as 30,000. Amazon’s [16,000 layoffs announced in January](https://www.cnbc.com/2026/01/28/amazon-layoffs-anti-bureaucracy-ai.html) were just “Phase One” with [internal documents pointing to another](https://americanbazaaronline.com/2026/03/12/after-16000-layoffs-amazon-may-cut-14000-more-jobs-in-second-phase-476695/) 14,000 in Q2. [March alone has seen 45,000 tech layoffs globally](https://technode.global/2026/03/09/2026-tech-layoffs-reach-45000-in-march-more-than-9200-due-to-ai-and-automation-rationalfx/), with over 9,200 explicitly attributed to AI and automation. Tech employee confidence has [hit a record low](http://v), with fewer than half of IT workers holding a positive six-month outlook.

Last week, Anthropic [pointed to tech](https://thenewstack.io/openai-gpt-5-4-ai-jobs-report-anthropic-dow-supply-chain-risk/) as the most over-exposed sector. It seems to be correct.

Layoffs are not new to tech. What’s changed is the justification. Companies aren’t citing macro headwinds anymore. They’re pointing directly at AI as both the reason for the cuts and the destination for the savings.

## The MCP vs API debate

The AI stack you just learned might already be outdated. Model Context Protocol spent 2025 as the presumed standard for connecting AI agents to the outside world, and this week, doubters are questioning its utility.

Perplexity’s cofounder and CTO Denis Yarats said internally [they’re moving away from MCPs](https://x.com/morganlinton/status/2031795683897077965) and returning to APIs and CLIs. The timing coincided with [Perplexity’s launch of a full-stack, model-agnostic API platform](https://thenewstack.io/perplexity-agent-api/) that replaces your model provider, search layer, and embeddings in one package. The company’s position is clear: APIs are the plumbing, not MCP servers.

Y Combinator president Garry Tan was even more direct. “[MCP sucks honestly](https://x.com/garrytan/status/2031910564344262988),” he posted, citing context window bloat, clunky authentication, and the need to toggle servers on and off. He got so frustrated with Claude’s MCP-based browser integration that he vibe-coded a CLI wrapper only to discover Vercel already built one.

*The New Stack* covered this architectural tension in depth. Their analysis of [Skills vs. MCP](https://thenewstack.io/skills-vs-mcp-agent-architecture/) makes the case for a two-layer model: if the knowledge is timeless, it goes into a markdown skill first; if it requires a live connection, it goes through MCP. For example, a GitHub MCP server consumed roughly 50,000 tokens of context to teach an agent how to interact with GitHub, while a [SKILL.md](http://skill.md) file achieved the same result in about 200 tokens. That’s a 250x difference. Microsoft’s .NET Skills Executor, which shipped just weeks ago, already orchestrates skill files that invoke MCP tools at a different layer.

None of this means MCP is dead. But the “MCP for everything” era appears to have ended before it even began. The industry is trying to be smarter: use the lightest tool for the job, and save the heavy protocol when it’s needed. It’s becoming increasingly clear that AI developers must remain agile and up to date on tools and best practices.

## The Mac Mini AI Agent

AI agents are starting to get their own machines now, and the Mac Mini is quickly becoming the default host for always-on AI.

Perplexity this week previewed [“Personal Computer”](https://x.com/perplexity_ai/status/2031790180521427166) – an always-on, local AI agent that runs on a Mac Mini, working across your files, apps, and sessions 24/7. This might be the best OpenClaw-like product for the average consumer. Meanwhile, [Moonshot launched a product](https://x.com/ojaskandy/status/2031801456718987765) that hacks macOS to create a separate user account for an AI agent – two users, one Mac, working side by side.

And this is happening outside of the Silicon Valley AI bubble. In China, *MIT Technology Review* reported on the OpenClaw gold rush. A Beijing software engineer who started tinkering with OpenClaw in January now runs a business with over 100 employees and 7,000 completed installation orders. Events are drawing 1,000+ attendees. Tencent held public events offering free OpenClaw installation support. China’s cybersecurity regulator [issued a warning on March 10](https://www.technologyreview.com/2026/03/11/1134179/china-openclaw-gold-rush/) about the security risks, which tells you just how mainstream agent-on-device has already become there.

The pattern is unmistakable: AI agents are moving from your browser to their own desks. They’re running background tasks, monitoring files, and executing workflows that persist across sessions. The question isn’t whether AI agents will become your coworkers – it’s whether you’ll know how to manage them when they do.

## Vibe Coding Hits $9 Billion

“Learn to code” was the career advice of the last decade. The new version: learn to describe what you want built. [Replit raised $400 million in Series D](https://techcrunch.com/2026/03/11/replit-snags-9b-valuation-6-months-after-hitting-3b/) at a $9 billion valuation, tripling its valuation in six months. Replit launched Agent 4 alongside the raise, and the company expects to hit $1 billion in run-rate revenue by year’s end. Fifty million users are now building on the platform.

The tooling layer is maturing just as fast. [Cursor introduced Automations](https://thenewstack.io/cursor-agents-developer-workflows/), always-on agents that can be triggered by codebase changes, Slack messages, or timers – turning the IDE into something closer to an autonomous engineering teammate. Together, Replit and Cursor are defining two distinct flavors of the same shift: Replit as the platform where anyone can build software by describing what they want, and Cursor as the tool where experienced engineers let agents handle the tedious parts. Different entry points, same destination.

Meanwhile, [Crafting launched with $5.5M in seed funding](https://thenewstack.io/crafting-ai-agents-platform/) to give enterprise coding agents production-like environments for testing, and [TanStack Start is positioning itself](https://thenewstack.io/tanstack-start-vibe-coding/) as the full-stack framework built specifically for vibe coders.

But vibe coding cautionary tales are popping up, too. Amazon held an [emergency engineering meeting](https://thenewstack.io/amazon-ai-assisted-errors/) after multiple outages were traced back to AI-assisted code changes. The company has now instituted a 90-day “code safety reset” requiring senior engineer approval for AI-generated deployments. The irony: Amazon laid off thousands of engineers, then discovered that the AI code replacing their work needs engineers to review it.

On *Towards Data Science*, [Reya Vir explored the same tension](https://towardsdatascience.com/the-reality-of-vibe-coding-ai-agents-and-the-security-debt-crisis/), warning about a growing security debt crisis. Vibe coding isn’t a replacement for engineering judgment. If anything, vibe coding amplifies the need for engineering judgement. If you understand what good code looks like, agents make you dramatically faster. If you don’t, agents make you dramatically more dangerous.

## Claude’s Million-a-Day moment

Claude is [adding a million users a day](https://x.com/mikeyk/status/2029662454079512598?s=20), with the trend seeming to start in early March. This is a fourfold increase from the start of 2026. Claude displaced ChatGPT as the number one free app in Apple’s App Store in 20+ countries – the first time any AI app has done that since ChatGPT launched. At this point, Anthropic is building less of a chatbot and more of a full productivity platform spanning browser, desktop, and terminal with Claude Code for developers, Cowork mode for non-technical desktop automation, and a steady update cycle on its three AI models.

Anthropic got some help from the Pentagon, too. The [company sued the DoW](https://www.axios.com/2026/03/09/anthropic-sues-pentagon-supply-chain-risk-label) over a “supply chain risk” designation imposed after the company refused to allow its AI for, among other things, mass surveillance. [Microsoft filed an amicus brief in support](https://americanbazaaronline.com/2026/03/11/microsoft-files-brief-in-support-of-anthropic-against-us-defense-476656/).

In AI, values are becoming a competitive moat and clearly a reason people choose one platform over another.

## AI Company News

* [AMI Labs](https://x.com/amilabs/status/2031234832454324639) — Yann LeCun’s startup says it’s building AI that learns from reality, not just language. It raised $1.03B in what may be Europe’s largest-ever seed round, with a $3.5 B valuation. Backed by Nvidia, Bezos Expeditions, Samsung, and Eric Schmidt.
* [Replit](https://replit.com/news/funding-announcement) — $400M Series D at $9B valuation, led by Georgian. Launched Agent 4 alongside the raise. 50M users, targeting $1B run-rate revenue by year-end.
* [Legora](https://legora.com/newsroom/legora-raises-550-million-series-d-to-fuel-us-growth) — The Swedish legal AI platform closed a $550M Series D, tripling its valuation to $5.5B. Generative AI for case law research, document review, and contract drafting.
* [Jump](https://www.businesswire.com/news/home/20260219487440/en/Jump-Raises-80-Million-Series-B-Led-by-Insight-Partners-to-Expand-AI-Operating-System-for-Financial-Advisors) — $80M Series B led by Insight Partners for an AI operating system for financial advisors. Scaled to 27,000 advisors in under two years.
* [Pasito](https://www.insightpartners.com/ideas/pasito-raises-21-million-series-a-led-by-insight-partners-to-build-ai-workspace-for-the-benefits-industry)  — $21M Series A led by Insight Partners for an AI-native workspace for group health and retirement benefits.
* [Crafting](https://www.globenewswire.com/news-release/2026/03/09/3252022/0/en/Crafting-Announces-General-Availability-of-Crafting-for-Agents-and-5-5M-Seed-Round-to-Build-Infrastructure-for-AI-Driven-Engineering.html) — $5.5M seed led by Mischief to build production-like environments for AI coding agents. Customers include Faire, Brex, and Webflow.

---

## Past Editions

> [OpenAI GPT-5.4 launches, AI gets its own jobs report, Claude surges after U.S. ban](https://thenewstack.io/openai-gpt-5-4-ai-jobs-report-anthropic-dow-supply-chain-risk/)

> [Perplexity Computer wows, Karpathy kills vibe coding, and OpenAI replaces Anthropic at the Pentagon](https://thenewstack.io/perplexity-computer-vibe-coding-openai-anthropic-pentagon/)

> [Claude Code comes to Roadmap, OpenClaw loses its head, and AI workslop](https://thenewstack.io/claude-code-comes-to-roadmap-openclaw-loses-its-head-and-ai-workslop/)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)