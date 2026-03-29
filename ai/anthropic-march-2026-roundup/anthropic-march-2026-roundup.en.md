**I’m Matt Burns, Head of Content at Insight Media Group. Each week, I round up the most important AI developments and explain what they mean for people actually putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries. This newsletter is here to help you be one of them.**

Fair warning: This weekly roundup is heavily Anthropic-focused. That’s not favoritism – it’s just where the news is. Anthropic is cooking right now, shipping faster and harder than anyone else in the industry, and most of the week’s biggest stories trace back to them.

## Anthropic’s March has been absurd

I’ve been covering technology startups and projects for 20 years, and I genuinely cannot remember a period where a company shipped as much as Anthropic did in February and March. Nearly every other day, Claude was upgraded with new features and capabilities.

These are just the major releases:

* [**Claude Opus 4.6**](https://techcrunch.com/2026/02/05/anthropic-releases-opus-4-6-with-new-agent-teams/) dropped on February 5 with a 1M-token context window and 128K-token output — Anthropic’s most capable model to date, and *The New Stack* [called it a step change for the enterprise.](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/)
* [**Claude Sonnet 4.6**](https://www.anthropic.com/news/claude-sonnet-4-6) followed on February 17 as the new default across free and Pro plans, with upgrades across coding, computer use, and agent planning at Sonnet 4.5 pricing ($3/$15 per million tokens).
* [**Interactive visualizations**](https://claude.com/blog/claude-builds-visuals) launched March 12 — Claude now builds charts, diagrams, and interactive widgets inline using HTML and SVG, rolling out to [all plan types, including free](https://thenewstack.io/anthropics-claude-interactive-visualizations).
* [**Memory for free users**](https://dataconomy.com/2026/03/04/anthropic-makes-claude-memory-feature-free-for-all-users/) arrived March 2, completing an eight-month rollout and adding a ChatGPT/Gemini import tool to make switching easier
* [**Claude Marketplace**](https://venturebeat.com/technology/anthropic-launches-claude-marketplace-giving-enterprises-access-to-claude) went live on March 6, letting enterprises apply existing Anthropic spend toward Claude-powered tools from Replit, GitLab, Harvey, Snowflake, and Lovable — with Anthropic taking zero cut
* [**Claude Code multi-agent review**](https://thenewstack.io/anthropic-launches-a-multi-agent-code-review-tool-for-claude-code/) launched March 9, dispatching parallel agents to catch bugs before human reviewers see the code — 54% of PRs now get substantive comments, up from 16%
* [**Excel and PowerPoint integrations**](https://venturebeat.com/orchestration/anthropic-gives-claude-shared-context-across-microsoft-excel-and-powerpoint/) gained shared context across both apps on March 11, with reusable Skills and LLM gateway support through Bedrock, Vertex AI, and Foundry
* [**The Claude Partner Network**](https://www.anthropic.com/news/claude-partner-network) formalized on March 12 with a $100M commitment — Accenture is training 30,000 professionals on Claude, and Cognizant opened access to its entire 350,000-person workforce
* [**1M token context**](https://blockchain.news/ainews/anthropic-claude-opus-4-6-and-sonnet-4-6-launch-1m-token-context-at-standard-pricing-business-impact-and-2026-analysis) at standard pricing went GA on March 14 for both Opus 4.6 and Sonnet 4.6, eliminating the previous 2x input surcharge beyond 200K tokens
* [**Claude Dispatch**](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork) launched March 17 as a persistent agent thread in Cowork — assign tasks from your phone, get a push notification when Claude finishes them on your Mac
* [**Claude Code hit web and mobile**](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/), letting developers kick off parallel coding workflows from Claude.ai on Anthropic-managed instances
* [**Computer use**](https://siliconangle.com/2026/03/23/anthropics-claude-gets-computer-use-capabilities-preview/) rolled out on March 23 as a research preview for Pro and Max — Claude can open apps, click, type, and navigate your Mac screen, falling back to screen control when it doesn’t have a direct integration
* [**Off-peak usage**](https://thenewstack.io/anthropic-doubles-claude-usage-outside-peak-hours/) limits doubled across Free, Pro, Max, and Team plans from March 13 through March 28, 2026
* [**Claude Code usage**](https://thenewstack.io/claude-code-user-base-grows-300-as-anthropic-launches-enterprise-analytics-dashboard/) grew 300% since the Claude 4 models launched, with run-rate revenue up 5.5x, and Anthropic shipped an enterprise analytics dashboard to track spend and code acceptance rates

Beyond the headline features, there’s been a steady stream of smaller stuff: Claude Code added PowerShell support on Windows, transcript search, MCP deduplication, and idle-return prompts across five point releases in the past week alone. Cowork picked up plugin support and improvements to file management. *The New Stack* has been all over it. I’d start with [our coverage of the multi-agent code review launch](https://thenewstack.io/anthropic-launches-a-multi-agent-code-review-tool-for-claude-code/) and Claude Code’s [expansion to the web and mobile](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/) if you’re trying to keep up.

## The servers, though

There’s a flip side to shipping this fast: Anthropic’s infrastructure seems to be struggling to keep up. Claude has gone down at least five times in March alone, including two lengthy outages this week. As I’m writing this on Friday morning, Opus 4.6 is experiencing elevated errors, though Sonnet 4.6 seems to be fine.

This isn’t unique to Anthropic. OpenAI, Google, and others have all faced similar growing pains as usage surges. But it’s more visible when you’re shipping as aggressively as Anthropic is right now. You can have the best model in the world, but if developers can’t rely on it being available, they’ll build fallback patterns, and some of those fallbacks become permanent. Reliability is a product feature, and right now it might be the one Anthropic most needs to ship.

## Claude Mythos slipped out

On Thursday, *Fortune* broke a story that [Anthropic is testing a new model](https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/) called Claude Mythos – internally codenamed “Capybara” – a next-generation model that the company describes as a “step change” in capability and “the most capable we’ve built to date.”

The reveal wasn’t planned. Anthropic accidentally left roughly 3,000 unpublished assets in a publicly accessible data cache — a draft blog post among them — due to what the company called “human error” during CMS configuration. Security researchers found it. *Fortune* reviewed it before Anthropic locked it down.

The claimed capabilities are significant: dramatically higher scores on coding, academic reasoning, and cybersecurity benchmarks compared to Opus 4.6. Anthropic said the model is “far ahead of any other AI model in cyber capabilities,” adding that it “presages an upcoming wave of models that can exploit vulnerabilities in ways that far outpace the efforts of defenders.” That’s Anthropic warning about its own model. The company says it’s testing Claude Mythos with a small group of early access customers and being “deliberate” about release.

Between the March feature blitz, the reliability problems, and now a next-generation model waiting in the wings, Anthropic’s story right now is one company trying to run at three different speeds simultaneously.

## MCP crossed 97 million installs

Anthropic’s Model Context Protocol hit [97 million monthly SDK downloads in March](https://www.digitalapplied.com/blog/mcp-97-million-downloads-model-context-protocol-mainstream). That’s up from roughly 2 million when it launched in November 2025 — 4,750% growth in 16 months. The ecosystem now includes over 5,800 community and enterprise servers spanning databases, CRMs, cloud providers, developer tools, and more. When OpenAI committed to MCP support last year, it stopped being Anthropic’s protocol and started being the industry’s. Anthropic formalized that shift in December by [donating MCP to the Agentic AI Foundation](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/) under the Linux Foundation, co-founded with Block and OpenAI.

*The New Stack* has covered the MCP story closely. Richard MacManus wrote a good piece on [why MCP won](https://thenewstack.io/why-the-model-context-protocol-won/) and our reporting on the [2026 roadmap](https://thenewstack.io/model-context-protocol-roadmap-2026/) digs into the production-readiness gaps the maintainers are now trying to close – auth, observability, server management at scale. The protocol is clearly winning adoption, but as one of our pieces put it, there’s still a [steep mountain between MCP and production.](https://thenewstack.io/model-context-protocol-evolution/) For developers building agentic workflows, MCP is the standard. The question now is whether the tooling around it can keep up with the demand.

If you want to go deeper with us, [we’ll be at the MCP Dev Summit](https://events.linuxfoundation.org/mcp-dev-summit-north-america/) April 2-3 in New York City. My good friend Alex Wilhelm, who publishes the excellent [*Cautious Optimism*](https://www.cautiousoptimism.news/) newsletter, will be there doing interviews for *The New Stack*.

## The AI Czar clocks out

David Sacks told *Bloomberg* Thursday that [he’s used up his 130 days](https://www.cnbc.com/2026/03/26/david-sacks-trump-crypto-ai-czar.html) as a special government employee and is stepping down as Trump’s AI and crypto czar. He’ll co-chair the President’s Council of Advisors on Science and Technology (PCAST) alongside Michael Kratsios. This gives Sacks a broader portfolio to oversee, but perhaps considerably less direct power.

As AI czar, Sacks had a direct line to Trump and a hand in shaping policy. As PCAST co-chair, he’ll make recommendations. [Axios reports](https://www.axios.com/2026/03/26/trump-white-house-david-sacks-ai-czar-policy-influence) the White House doesn’t plan to appoint a new AI czar, which means the most visible AI policy role in Washington is vacant with no replacement.

Before leaving, Sacks told *Bloomberg* that [Congress could pass bipartisan AI legislation](https://www.bloomberg.com/news/articles/2026-03-26/congress-could-pass-ai-standard-in-months-key-trump-aide-says) within months, with the framework pairing child safety measures with federal preemption of state AI laws. “We’ve gotten a very good reception from Capitol Hill,” Sacks said. “This is an area where I think we’re willing and happy to work with Democrats.” Whether that optimism survives his departure from the day-to-day is the question. AI policy might be one of the few genuinely bipartisan issues right now, but bipartisan momentum without a champion has a way of fading.

For organizations adopting AI, the regulatory picture matters. Federal preemption of state laws would simplify compliance significantly. A patchwork of state regulations is one of the biggest friction points for enterprises deploying AI across the U.S. If Sacks is right that a bill is months away, that’s worth paying attention to.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)