*I’m Matt Burns, Director of Editorial at Insight Media Group. Each week, I round up the most important AI developments. And not just the headlines, but what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

**Quick brag**: [Roadmap](https://roadmap.sh/dashboard) hit a significant milestone this week. It’s now [the 6th-most-starred project](https://github.com/kamranahmedse/developer-roadmap?tab=readme-ov-file) on GitHub, with its founder, [Kamran Ahmed](https://github.com/kamranahmedse), now the 2nd-most-starred person on GitHub. I have amazing coworkers.

## **The Multi-Agent Desktop Arrives for Everyone**

Workers need to start getting comfortable with agents. They’re becoming more than features inside software. Agents are becoming the interface itself.

This was the week AI agents stopped being a developer tool and started becoming something for non-technical users. [Perplexity launched Computer](https://www.perplexity.ai/products/computer) – not a chatbot, not a smarter research engine, but what the company calls a “general-purpose digital worker.” You describe the outcome, and Computer deploys subagents that browse, research, create, and connect your tools automatically in the background. It connects to Gmail, Slack, Notion, Calendar, and hundreds of other apps and can run for hours or *even months* ([according to the release notes](https://www.perplexity.ai/hub/blog/introducing-perplexity-computer#:~:text=Perplexity%20Computer%20is%20a%20system%20that%20creates%20and%20executes%20entire%20workflows%2C%20capable%20of%20running%20for%20hours%20or%20even%20months.%C2%A0)). The tagline makes the value proposition clear: “Chat answers. Agents do tasks. Computer works.” There are [dozens of examples](https://www.perplexity.ai/computer/live/) on the product page to see how it works.

Perplexity Computer is similar to OpenClaw, but for normal people. OpenClaw runs on your local machine and requires significant setup. Computer runs in a browser and just works.

Meanwhile, Anthropic expanded [Claude Cowork with 13 new enterprise plugins](https://thenewstack.io/anthropic-accelerates-its-cowork-enterprise-play/) covering Google Workspace, DocuSign, FactSet, LegalZoom, and more. The company also shipped [Remote Control for Claude Code](https://code.claude.com/docs/en/remote-control), finally enabling mobile access to the desktop app, and [a scheduling tool](https://x.com/claudeai/status/2026720870631354429?s=20) that brings Claude closer to OpenClaw. Notion released Custom Agents that run workflows on a schedule or in response to specific requests in a workspace. To support this product, Notion quietly released an early-alpha toolkit on GitHub for building custom tool calls. [Eric Goldman from Notion announced it](https://x.com/goldmanem/status/2026392066222354785) as a programmable partner for custom agents: “Build your agents the exact tools they need to do work across your business.”

## **The Agent Standards Race Heats Up**

The New Stack has been covering [the agent framework wars](https://thenewstack.io/agent-framework-container-wars/) closely, and the parallel to the container wars is hard to ignore – different cast, higher stakes, nearly identical plog. This week, Anthropic pushed the story forward by [releasing its Skills repository on GitHub](https://github.com/anthropics/skills), making the full collection of Agent Skills available to anyone. This includes folders of instructions, scripts, and resources that teach AI agents repeatable workflows. The repo already has 76,000+ stars. As TNS reported in its deep dive, Agent Skills is [Anthropic’s next bid to define AI standards](https://thenewstack.io/agent-skills-anthropics-next-bid-to-define-ai-standards/), following the same playbook that turned MCP into the de facto protocol for how agents use tools.

The move matters because adoption has already spread well past Anthropic. Microsoft adopted Agent Skills inside VS Code and GitHub. Cursor, Goose, Amp, and OpenCode have all picked up as well. OpenAI quietly adopted a structurally identical architecture in ChatGPT and Codex. The spec is now at v0.9 under the newly formed Agentic AI Foundation, a Linux Foundation-backed alliance. Whether you’re building agents or just using them, this is the plumbing layer worth watching.

## **Vibe Coding is 2025. Agentic Engineering is now.**

One year ago this month, Andrej Karpathy coined the term “vibe coding.” [He’s now calling it obsolete](https://thenewstack.io/vibe-coding-agentic-engineering/). His replacement term sits better with me: “[agentic engineering](https://thenewstack.io/vibe-coding-is-passe/).” His [post on X went viral](https://x.com/karpathy/status/2026731645169185220?s=20) (3 million views and counting), Karpathy described setting up a home video analysis dashboard by giving an agent a single English-language prompt – “log into my DGX Spark, set up vLLM, download and benchmark Qwen3-VL, build a web UI, test everything, configure systemd services, and write me a report. He says the agent ran for 30 minutes, hit multiple issues, researched solutions online, debugged, and came back with the finished product.” 

His process is how I’m working now, and over the last couple of weeks, I’ve seen countless examples of others doing the same, producing vastly improved results compared to similar attempts on past models.

Karpathy’s broader claim echoes [Matt Shumer’s](https://x.com/mattshumer_/status/2021256989876109403): coding agents didn’t work before December ‘25 and do now. The models crossed a threshold of coherence and tenacity that makes the old workflow – typing code into an editor – feel like a relic. Product strategist Aakash Gupta picked up [on a related Karpathy thread](https://x.com/aakashgupta/status/2026367615602667784) and noted that the new distribution channel for software is agents. “Agents don’t browse your marketing site or watch your demo video. They call your CLI, hit your MCP server, and read your docs programmatically. If none of those surface areas exist, your product is invisible to them….MCP went from zero to 97 million monthly SDK downloads in twelve months.”

Benjamin Lee [published a piece on TDS](https://towardsdatascience.com/the-missing-curriculum-essential-concepts-for-data-scientists-in-the-age-of-ai-coding-agents/) relaying the missing curriculum for data scientists in the age of AI coding agents. He argues that code smells, architecture intuition, and systems thinking matter more than ever when the agent writes the code, but you own the consequences. It’s a great practical read and worth your time if you’re navigating this shift yourself. The people who thrive in the agentic engineering era won’t be the fastest typists. They’ll be the ones who know what good code looks like and can steer an agent toward it. 

## **Cloudflare Builds the Plumbing for Agent-Friendly Websites**

[Cloudflare launched Markdown for Agents](https://thenewstack.io/cloudflares-markdown-for-agents-automatically-make-websites-more-aifriendly/) earlier this month. The concept is straightforward: When an AI agent requests a webpage, Cloudflare’s edge converts the HTML to clean markdown before returning it. The token savings are impressive. When used on Cloudflare’s own blog post, it shows the amount of tokens drops from 16,180 in HTML to 3,150 in Markdown, an 80% reduction.

Agents like Claude Code and OpenCode already send the Accept headers that trigger this conversion. The feature is in beta for Pro, Business, and Enterprise Cloudflare customers at no additional cost. It’s infrastructure-level plumbing that makes every website behind Cloudflare instantly more accessible to AI agents (without modifying any code).

## **The Pentagon Drops Anthropic, OpenAI Steps In**

President Trump on Friday [directed all federal agencies to immediately stop using](https://truthsocial.com/@realDonaldTrump/posts/116144552969293195) Anthropic’s products, calling it a “radical left, woke company.” Secretary Hegseth followed, [declaring in a tweet](https://x.com/SecWar/status/2027507717469049070?s=20) Anthropic is a supply chain risk – a label typically reserved for foreign adversaries. This designation, if made official, would have serious implications, perhaps limiting Anthropic from doing business with other DoW vendors such as AWS, Nvidia, and Microsoft. [Anthropic responded](https://www.anthropic.com/news/statement-comments-secretary-war), questioning Hegseth’s implications of the order and saying it would challenge the designation in court. 

Hours later, [Sam Altman announced on X](https://x.com/sama/status/2027578652477821175?s=20) that OpenAI had struck a deal to deploy its models on the Pentagon’s classified network. The details matter. Altman said the agreement includes prohibitions on domestic mass surveillance and “human responsibility for the use of force, including for autonomous weapon systems.” On the surface, that sounds like what Anthropic was asking for. But the language isn’t the same. Anthropic wanted human oversight before the trigger pull – a human in the kill chain sequence of an AI-powered weapon. OpenAI’s deal requires human responsibility – which can mean accountability after the fact. Anthropic wanted surveillance protections beyond the current law, because Dario Amodei argued current law hasn’t caught up with what AI makes possible. OpenAI’s deal appears to defer to existing law and policy, which is the exact framework Anthropic said was insufficient.

This isn’t over. The Pentagon’s own position is that mass surveillance and autonomous weapons are already illegal under current law – which raises the obvious question: if you’d never do it anyway, why not put it in writing? Anthropic forced the Pentagon to answer that question and got blacklisted. OpenAI got a deal with language that looks similar but commits to less. The precedent this sets for every AI company doing business with the government is worth watching closely. 

---

## Past Editions

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