*I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

OpenAI co-founder Andrej Karpathy [posted an essay this week](https://x.com/karpathy/status/2042334451611693415) describing a real and growing perception gap around AI. He’s right that it exists. But the reason it’s widest in software right now isn’t just about reinforcement learning and verifiable reward functions.

Developers are feeling AI’s impact first not because coding is the only domain where the tools work, and not because programmers are uniquely vulnerable. They are first because software is currently the place where frontier-model capability, AI fluency, and deep domain expertise overlap most cleanly. That overlap is what makes AI transformational. As models improve and agentic tools become more usable in law, medicine, finance, media, and operations, the same dynamic will spread outward. Developers are not the exception. They are the preview.

## Why developers feel this first

Karpathy’s essay should be required reading. His framing: one group of people tried the free tier of ChatGPT sometime last year, saw hallucinations, made some AI slop, and formed their opinion. Fair enough. A second group pays for frontier models – OpenAI’s Codex, Claude Code – and uses them professionally in technical domains. This group, Karpathy says, is experiencing “AI Psychosis” because the improvements as of this year have been “nothing short of staggering.” They’re watching these models solve programming problems that would normally take days or weeks.

His explanation for the gap is technical: reinforcement learning works best with verifiable reward functions which makes coding and math dramatically more trainable than writing or search. And because those technical domains generate the most B2B revenue, that’s where the biggest teams are focused. He’s right about that.

But there’s a simpler reason he doesn’t name. I’m not a developer. I’m a journalist and editor, and I know how to push AI forward in editorial and content work in ways that a software engineer might not. But I’m not feeling the same “AI Psychosis” that Karpathy describes, because the tools haven’t been optimized for my domain the way they’ve been optimized for code. Not yet.

The developer community is feeling this first because AI capability, AI expertise, and domain expertise all converge in the same people. The people developing AI systems tend to be leading developers. The tool was built by and for them. *The New Stack* has been tracking this shift [since Karpathy first retired](https://thenewstack.io/vibe-coding-is-passe/) his term “vibe coding” in favor of “agentic engineering,” subtly shifting the name away from a consumer term to focus on developers. And now, this narrow class of workers are the first feeling the full effects of AI in their industry.

## Why everyone else will feel it next

Anthropic [just moved Claude Cowork](https://thenewstack.io/anthropic-takes-claude-cowork-out-of-preview-and-straight-into-the-enterprise/) from research preview to general availability with full enterprise features — plugins, managed agents, connectors for Google Drive, Gmail, DocuSign, and dozens of industry-specific tools. The thesis behind the product is explicit: Claude Code transformed programming, and now Cowork is coming for the rest of the enterprise. If you work in HR, operations, finance, or design, the agentic tools that gave developers “AI Psychosis” are being built for your domain now. But let’s remember, Claude Code was available for nearly 10 months before it became an overnight hit in late December 2025, and Cowork could follow the same adoption trajectory.

A new Gallup study [released this week](https://news.gallup.com/poll/708224/gen-adoption-steady-skepticism-climbs.aspx) found that 31% of Gen Z now says AI makes them angry – up 9 percentage points from last year. Only 22% say it makes them excited, down from 36%. Hopefulness dropped 9 points to 18%. And 80% believe AI use may impede their future ability to learn. *The* *New York Times* [covered the findings](https://www.nytimes.com/2026/04/09/style/gen-z-ai-gallup-study.html) as a generational mood shift.

I get the frustration. But this is the perception gap playing out at generational scale. I have teenagers entering college and it’s hard to get them to fully embrace AI. I see Gen Z largely reacting to low-quality consumer AI experiences and institutional confusion around the technology – chatbots that hallucinate, AI-generated slop in their feeds, tools their schools simultaneously ban and require. That is a fundamentally different product than the agentic models restructuring codebases and finding generational security vulnerabilities.

The job numbers are harder to dismiss. Goldman Sachs estimates [AI is eliminating roughly 16,000 net U.S. jobs per month](https://fortune.com/2026/04/06/ai-tech-displacement-effect-gen-z-16000-jobs-per-month) — about 25,000 wiped out by automation, 9,000 added back through augmentation. Younger Gen Z workers are disproportionately concentrated in the low-paying roles AI automates first: data entry, customer service, legal support, billing. According to *Nikkei Asia* [78,557 tech workers were laid off in Q1 2026](https://asia.nikkei.com/business/technology/artificial-intelligence/nearly-80-000-tech-jobs-cut-in-q1-but-ai-s-full-impact-may-be-yet-to-come), with nearly half attributed directly to AI. Cognizant’s chief AI officer told *Nikkei* that the real impact hasn’t even materialized yet — “it could take up to a year before the real impact of the technology on the workforce becomes clear.”

You’re not going to lose your job to AI (though AI might be blamed). But you might lose it to a person who’s better at AI than you. That’s always been the thesis of this newsletter, and this week the data made it sharper.

## The evidence that this is already spreading

Anthropic released something this week that shows what happens when AI capability meets deep domain expertise. Claude Mythos Preview is a new model that the company says is “far ahead of any other AI model in cyber capabilities.” On [Anthropic’s own red team assessment](https://red.anthropic.com/2026/mythos-preview/), Mythos identified and exploited zero-day vulnerabilities in every major operating system and every major web browser. It found a 27-year-old denial-of-service bug in OpenBSD. It found a 16-year-old flaw in FFmpeg. It developed 181 working exploits for Firefox JavaScript engine vulnerabilities, compared to 2 for the previous Opus 4.6 model. The security implications are unprecedented.

The key line from the company’s writeup: “We did not explicitly train Mythos Preview to have these capabilities. Rather, they emerged as a downstream consequence of general improvements in code, reasoning, and autonomy.” Anthropic didn’t build a cybersecurity model. They built a better reasoning model, and cybersecurity capability fell out of it. That’s the mechanism by which this spreads. Improve the model on verifiable technical tasks, and downstream capabilities cascade into adjacent domains like security and infrastructure, and eventually law, medicine, and finance.

We covered [Mythos on *The New Stack* this week](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/). Anthropic isn’t releasing it publicly. Instead, [they launched Project Glasswing](https://cyberscoop.com/project-glasswing-anthropic-ai-open-source-software-vulnerabilities/) with Amazon, Apple, Microsoft, and five other major partners to use the model defensively, pledging $100 million in credits and $4 million in direct donations to open-source security. The New York Times called it “[a cybersecurity reckoning](https://www.nytimes.com/2026/04/07/technology/anthropic-claims-its-new-ai-model-mythos-is-a-cybersecurity-reckoning.html).”

And then there’s Meta. An employee built [an internal dashboard](https://fortune.com/2026/04/09/meta-killed-employee-ai-token-dashboard/) called “Claudeonomics” — named after Anthropic’s Claude — that ranked all 85,000+ employees by AI token consumption. Top users earned titles like “Token Legend.” In 30 days, total consumption hit 60 trillion tokens. The top user averaged 281 billion tokens per month. Meta’s CTO Andrew Bosworth reportedly claimed a top engineer spending their entire salary on tokens was achieving 10x productivity. Nvidia’s Jensen Huang said he’d be “[deeply alarmed](https://the-decoder.com/meta-employees-compete-for-token-consumption-on-an-internal-ai-leaderboard/)” if a $500,000-per-year engineer wasn’t consuming $250,000 worth. Nobody has put up hard numbers linking token consumption to actual business results. But 85,000 people using frontier AI models so aggressively they built a competitive leaderboard around it tells you something about where the largest companies think this is heading. Today, the token legends are engineers. As these tools mature across industries, that will change.

Developers aren’t uniquely threatened. They’re just first.

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