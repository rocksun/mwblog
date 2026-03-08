*I’m Matt Burns, Director of Editorial at Insight Media Group. Each week, I round up the most important AI developments. And not just the headlines, but what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

## **OpenAI launched GPT-5.4, and Codex hit 1.6 million users**

OpenAI had a busy week. On Thursday, [it launched GPT-5.4](https://thenewstack.io/openai-launches-gpt-5-4/), the next version of its frontier model. The company calls the model its “most capable and efficient frontier model for professional work.” It combines the coding capabilities of GPT-5.3-Codex with improved support for spreadsheets, documents, and presentations. The benchmark scores impress with fewer errors, fewer false claims, and 83% score on GDPval, which tests models against real-world tasks across 44 occupations. That means it matched or exceeded industry professionals in 83% of comparisons. Anthropic’s Opus 4.6 scores 79.5% on the same test.

But GPT-5.4 is OpenAI’s most expensive per-token model yet; the company says it consumes fewer tokens per task than other models.

Earlier in the week, OpenAI [finally launched Codex](https://thenewstack.io/openais-codex-is-now-on-windows/) on Windows. The app was built for Windows developer environments and supports native sandboxing and workflows that Windows developers are already familiar with. *The New Stack* reported this week that OpenAI’s Codex now has 1.6 million weekly active users.

[@systemticls posted a good read](https://x.com/systematicls/status/2028814227004395561?s=20) on what “agentic engineering” actually looks like in practice, and it reads more like a software architectural manual than a prompting guide. Task decomposition, feedback loops, guardrails, and model selection per step. The people getting the most out of Codex (and Claude Code) aren’t writing better prompts. They’re designing better systems.

## **AI is reshaping jobs in unexpected ways**

Anthropic [published a new study](https://www.anthropic.com/research/labor-market-impacts) this week that introduces a measure called “observed exposure.” It combines theoretical LLM capability with real-world usage data. The finding? AI is far from reaching its theoretical capability. Actual task coverage remains a fraction of what’s feasible. Computer programmers are the most exposed occupation, but across the economy, the study reports no systematic increase in unemployment for other highly exposed workers since 2022. The study points to one warning sign: suggestive evidence that hiring workers aged 22 to 25 has slowed for exposed occupations. This suggests that the jobs are not vanishing, but who gets hired into them might be changing.

A new piece on [*Towards Data Science*](https://towardsdatascience.com/human-work-in-the-ai-world-how-to-remain-valuable/) makes the longer case for this shift. Favio Vazquez argues that recursive technology doesn’t equal recursive adoption. AI models improve at software speed, but the real world is constrained by infrastructure, regulation, and organizational change. Vazquez the jobs aren’t disappearing. They’re restructuring around systems design, strategy, and judgment.

[Kevin Rose got it right](https://x.com/kevinrose/status/2029376563318305202?s=20): if agents can write the code, the value shifts to knowing what to build. That’s the job now.

## **CLIs are being rebuilt for agents**

Google quietly released [gws](https://github.com/googleworkspace/cli), a unified CLI for all of Google Workspace: Gmail, Drive, Calendar, Docs, Sheets, everything. It has 40+ agent skills and MCP support. But the interesting part is the design: it’s auto-generated from Google’s Discovery Service, so it always matches the current API surface. Every command returns structured JSON. Every schema is introspectable. This isn’t a tool for humans who happen to automate things. It’s a tool for agents.

The person behind gws, Justin Poehnelt, [wrote a piece](https://justin.poehnelt.com/posts/rewrite-your-cli-for-ai-agents/) that perfectly names this shift: “Agent DX” versus “Human DX.” He argues that everything we know about good CLI design – discoverability, progressive disclosure, helpful error messages – is actively wrong for agents. Agents need predictability, structured output, explicit failures, and zero interactive prompts. He lays out seven principles, and they’re worth reading. Anthropic’s Dickson Tsai [announced](https://x.com/dickson_tsai/status/2029235808235078095) Claude Code HTTP hooks this week, too. This is another sign that developer tools are being designed with agents as first-class consumers, not an afterthought.

The pattern here matters for anyone building internal tools. If your CLI still outputs pretty tables for humans, it’s already behind.

## **Agent Orchestration is becoming a critical layer**

Individual agents can do work. But someone still has to be the manager. Two open source projects shipped this week, trying to be exactly that.

[OpenAI released Symphony](https://github.com/openai/symphony), which monitors work queues – starting with Linear boards – picks up tasks, spawns agents to execute them in isolated environments, runs tests, and submits pull requests. It’s a project manager who never sleeps. The architecture is modular: swap in different LLM providers, different project management tools, different CI pipelines. [Paperclip](https://github.com/paperclipai/paperclip) goes further. It’s a framework for managing entire organizations of agents, including org charts, budgets, spending limits, and governance rules. Each agent has a role and a set of tools. The system tracks the token cost throughout the operation.

Both are early. Both have obvious gaps. But they’re showing the future of orchestration layers for better agent management. This is an important layer to watch. The companies that figure out how to structure agent teams, define boundaries, and maintain quality control will pull ahead fast.

## **OpenAI is in damage control. Anthropic is breaking records.**

Last week, [the Pentagon kicked out Anthropic](https://thenewstack.io/perplexity-computer-vibe-coding-openai-anthropic-pentagon/) and signed with OpenAI hours later. This week, OpenAI’s chief, Sam Altman, is dealing with the public-relations fallout, and Anthropic was hit with the formal supply chain risk paperwork.

On Thursday, Anthropic CEO Dario Amodei confirmed that the Department of War designated Anthropic as a supply chain risk to national security. The company says the designation is narrow – it applies only to Claude’s use of a direct part of DOW contracts, not all use of Claude by contractors. Amodei says the company will challenge the designation in court. He also apologized for a leaked internal memo, calling the terse language within not a true reflection of his views. His tone in the released statement was conciliatory, stating that Anthropic will continue to provide models to the DoW and national security community at nominal cost during the transition. He stressed that Anthropic has “much more in common with the Department of War than we have differences.”

The broader fallout is hitting OpenAI harder. More than 300 Google and 60 OpenAI employees had [already signed an open letter](https://techcrunch.com/2026/02/27/employees-at-google-and-openai-support-anthropics-pentagon-stand-in-open-letter/) supporting Anthropic’s stance before the new deal between OpenAI and the Pentagon was announced. After it dropped, chalk messages appeared outside of OpenAI’s San Francisco office: “Where are your redlines?” [Altman admitted](https://www.cnbc.com/2026/03/03/openai-sam-altman-pentagon-deal-amended-surveillance-limits.html) the deal “looked opportunistic and sloppy” and told employees on March 4 that he “feels terrible for subjecting” them to the backlash. Within days, [OpenAI amended the contract](https://www.nbcnews.com/tech/tech-news/openai-alters-deal-pentagon-critics-sound-alarm-surveillance-rcna261357), adding explicit surveillance protections absent from the original.

The damage was already done. Roughly [2.5 million users signed up](https://quitgpt.org/) for the “QuitGPT movement.” And quickly, [Claude jumped to #1](https://techcrunch.com/2026/03/01/anthropics-claude-rises-to-no-2-in-the-app-store-following-pentagon-dispute/) on Apple’s App Store. Daily sign-ups reportedly broke records every day this week. Free users are up more than 60% since January. Paid subscribers have doubled this year.

The revenue numbers tell the same story. [*Bloomberg* reported](https://www.bloomberg.com/news/articles/2026-03-03/anthropic-nears-20-billion-revenue-run-rate-amid-pentagon-feud) that Anthropic hit a $19 billion annualized run rate – up from $9 billion at the end of 2025. Even before Anthropic lost its government contracts, Claude Code reported annualized billings ranging from $0 to $2.5 billion in nine months.

Anthropic turned getting blacklisted by the U.S. Government into a blockbuster marketing event.

---

## Past Editions

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