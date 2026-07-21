*I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: Workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

Last week I told you [the AI frontier was dropping](https://thenewstack.io/openai-spacexai-meta-price-war/) the price of intelligence toward a dollar. This week, Elon Musk took one part of the stack to zero.

On Wednesday, SpaceXAI [open-sourced Grok Build](https://github.com/xai-org/grok-build), its terminal coding agent, under an Apache 2.0 license. “Grok Build is now open source,” [Musk posted](https://x.com/elonmusk/status/2077495635687723408). The move looks like a direct attack on Claude Code and Codex: Give developers the harness for free, reset usage limits, and make competing tools defend their prices.

Then Bloomberg supplied the number that explains why SpaceXAI can afford the open source move. Anthropic, the company behind Claude Code, reportedly [pays SpaceXAI $1.25 billion a month](https://www.bloomberg.com/news/articles/2026-05-20/anthropic-to-pay-spacex-nearly-45-billion-for-computing-deal) for compute. Across Anthropic, Google, and Reflection, SpaceXAI’s compute agreements [total roughly $2.3 billion a month](https://www.bloomberg.com/news/articles/2026-07-16/spacexai-identity-crisis-at-elon-musk-s-chatbot-company).

Musk is competing with Anthropic for developers while renting Anthropic the machines it needs to compete. Grok does not have to beat Claude for SpaceXAI to benefit from Claude’s growth.

Open-sourcing the harness may [expand the market for coding agents](https://thenewstack.io/anthropic-claudecode-opencode-split/). SpaceXAI is unusually positioned to make money if that happens, even when developers choose Claude instead.

## Musk can lose the coding-agent race and still get paid

Coding agents have become more capable, more autonomous, and more token-thirsty throughout 2026. Musk has now made one of the major agent harnesses open source, even though the model powering it still costs money to run.

Grok Build is a terminal coding agent in the same category as Claude Code and OpenAI’s Codex. As our own Janakiram MSV wrote in a [six-months-in comparison,](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/) the contest stopped being about raw model quality a while ago: “Once everyone accepted the shape, the contest moved to the platform around it.” Grok Build entered the platform war in May with a local-first design and a roughly 70% score on SWE-bench. The model behind it is not a joke, either: [Artificial Analysis](https://x.com/ArtificialAnlys/status/2074942097158021371) placed the newly launched Grok 4.5 near the frontier on its independent benchmarks while measuring it as one of the cheapest models at that performance level. OpenAI noticed. Greg Brockman, its president, [replied](https://x.com/gdb/status/2077424882502263081): “If you’re able to get better price/perf on any workload, would love to hear the details,” and published his email address.

So why give the coding agent away? Because SpaceXAI can afford to fight this war differently from OpenAI and Anthropic. Musk can open-source the harness, price Grok aggressively, and still earn infrastructure revenue from Anthropic, the company behind the coding agent it’s trying to undercut.

Musk has enough compute to make this move. According to [*Bloomberg Businessweek*](https://www.bloomberg.com/news/articles/2026-07-16/spacexai-identity-crisis-at-elon-musk-s-chatbot-company), SpaceXAI’s own models were using just 11% of its available computing power in April, so it has room to spare and rarely caps its customers, even as Anthropic is reportedly scrambling through a compute crunch. SpaceX’s CFO put the strategy plainly: “Elon felt the constraint was going to be compute and power. We are already seeing that.” That is the strange shape of it. SpaceXAI can subsidize the product competing against one of its largest infrastructure customers.

## The business model is stronger than the organization running it

A second economic position is worth nothing if the company can’t run the product. This is where the story gets harder for Musk. [That same *Bloomberg* piece](https://www.bloomberg.com/news/articles/2026-07-16/spacexai-identity-crisis-at-elon-musk-s-chatbot-company) is a portrait of an operation in disarray: All eleven of xAI’s co-founders have left, and an internal survey found the most common complaint was that management “didn’t seem to know what it wanted.” The most damning detail for a company selling coding tools is that xAI’s own engineers reportedly won’t use them, reaching for Anthropic’s and OpenAI’s tools instead. If the people building Grok don’t trust it to code, it’s fair to ask why outside developers should.

That trust problem got worse the week of the open-source release. Grok Build was open-sourced the day after developers discovered it was quietly uploading entire directories to SpaceXAI’s cloud. [One user watched it](https://x.com/a_green_being/status/2076598897779020159) grab “my SSH keys, my password manager database, my documents, photos, videos, everything.” [Musk promised](https://x.com/elonmusk/status/2076739687658496209) the data would be “completely and utterly deleted.” In that context, whatever strategic value the open-source release had, it also became damage control.

Then the world read the Grok Build code. [As Simon Willison writes](https://simonwillison.net/#:~:text=xai%2Dgrok%2Dtools,how%20it%20works.), parts of Grok Build’s tooling were ported from other coding agents, including OpenAI’s Codex and the open-source OpenCode. So the tool positioned against Codex incorporates openly licensed work derived from Codex.

That is not necessarily a scandal. It is how open source is supposed to work. But opening the repository exposed two things at once: The privacy mechanism Musk had just disabled, and how quickly the coding-agent layer is becoming portable. Our own Paul Sawers made the case months ago that [the harness is where coding agents differentiate themselves](https://thenewstack.io/coding-agents-team-infrastructure/). Grok Build shows how difficult it may be to keep that differentiation proprietary.

Strip away the organizational chaos, and the economic move is narrow and smart.

Musk does not need to win developers away from Anthropic. Open-sourcing Grok Build can expand the market for coding agents, and SpaceXAI can benefit even when developers choose Claude. Anthropic pays for the compute beneath that growth.

That’s the strange shape of Musk’s position. Anthropic has to make Claude beat Grok, and Musk can get paid when it does.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)