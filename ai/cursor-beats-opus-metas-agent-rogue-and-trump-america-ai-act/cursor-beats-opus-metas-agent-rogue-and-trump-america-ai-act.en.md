*I’m Matt Burns, Director of Editorial at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

My AI-powered NCAA March Madness busted on the first day, proving AI has yet to advance to the point where it’s able to predict how teenagers will perform under pressure. I used <https://www.bracketmadness.ai/>, and I loved the onboarding flow.

---

This week was all about consolidation. Not the boring, scary corporate kind, but rather the strategic consolidation. Cursor announced its own model. Nvidia rallied a coalition to build open base models together. OpenAI is merging three apps into one. Anthropic dropped prices twice. Bezos is raising $100 billion to buy manufacturers and inject them with AI. And Congress released the 300-page Trump America AI Act to replace every state-level AI law in the United States.

The through-line: Every major player is trying to own a bigger piece of the stack. And the tools you use today might not be the tools you use in six months.

## Cursor outguns and undercuts Opus

Cursor this week [released Composer 2](https://thenewstack.io/cursors-composer-2-beats-opus-46-on-coding-benchmarks-at-a-fraction-of-the-price/), its third-generation in-house coding model. The benchmarks are impressive. On Terminal-Bench 2.0, which measures how well AI agents handle real-world software engineering tasks in a terminal, Composer 2 scores 61.7%. That beats Claude Opus 4.6 at 58%. On Cursor’s own CursorBench, the new model hits 61.3, up from 44.2 on the previous generation, and competitive with GPT-5.4 Thinking at 63.9.

The pricing is the real story. Composer 2 costs $0.50 per million input tokens and $2.50 per million output tokens. Opus 4.6 costs $5/$25. That’s a 10x difference. Cursor trained the model exclusively on code data and applied reinforcement learning on long-horizon coding tasks – problems that require hundreds of individual steps. The result is a smaller, more focused model that doesn’t need to know everything, just how to write code well.

I keep watching for the moment when these AI coding tools plateau, and it keeps not arriving. Cursor faces real structural pressure here – it now competes with OpenAI and Anthropic while depending on their models. Building Composer 2 is how they start to control their own margins. And they’re not alone. [Nvidia this week announced a coalition of AI labs](https://thenewstack.io/nvidia-tier2-nemotron-coalition/) – including Cursor, Mistral, Perplexity, LangChian, and Black Forest Labs – to pool resources and build shared base models on Nvidia’s DGX Cloud infrastructure. The first project, a new base model, will form the foundation for Nvidia’s Nemotron 4 family. The tool-makers are becoming model-makers. That’s a significant step.

## The OpenAI superapp

The *Wall Street Journal* [reported](https://www.wsj.com/tech/openai-plans-launch-of-desktop-superapp-to-refocus-simplify-user-experience-9e19931d) that OpenAI plans to combine ChatGPT, Codex, and its web browser into a single desktop application. Fidji Simo, OpenAI’s CEO of Applications, told employees: “We realized we were spreading our efforts across too many apps and stacks, and that we need to simplify our efforts. That fragmentation has been slowing us down and making it harder to hit the quality bar we want.”

The mobile ChatGPT app stays separate. This is a desktop play – reportedly aimed at developers, enterprises, and power users who want conversational AI, coding assistance, and browsing in one place. I found the internal quote revealing, indicating that an internal product development structure was not meeting their users’ expectations. It’s rare for a company to just say, “We built too many things, and it’s not working.” It signals where the company sees its current competition – not in chat, but in the desktop workspace where Anthropic’s Claude and Cursor already live. The race to become the default AI layer on your computer is getting more crowded. Competition is great.

## Tokens go on sale

Two Anthropic moves this week lowered the cost of AI. First, the company [removed the long-context pricing surcharge](https://thenewstack.io/claude-million-token-pricing) for Claude Opus 4.6 and Sonnet 4.6. The 1-million-token context window is now generally available at standard per-token rates – $5/$25 for Opus, $3/$15 for Sonnet. Previously, prompts over 200,000 tokens triggered premium pricing. A 900k-token request now costs the same per token as a 9k one. If you work with large codebases or long documents, this matters. I’ve been bumping up against context limits for weeks, so this one hits home.

Second, Anthropic [doubled usage limits](https://thenewstack.io/anthropic-doubles-claude-usage-outside-peak-hours/) for all Claude plans during off-peak hours – a two-week promotion running through March 28. The doubled limits apply on weekends and weekdays before 8 a.m. and after 2 p.m. Eastern. *The New Stack* framed this as a competitive strategy more than generosity: shifting usage to off-peak hours eases infrastructure load during busy periods, and heavier use builds habits. Soon, I’m going to have to schedule cron jobs on the same timetable as I recharge my EV.

Between Cursor’s 10x cheaper coding model and Anthropic giving away usage, the cost of AI-assisted work is dropping fast. The orgs figuring out how to actually use these tools in cost-effective ways are the ones who’ll benefit.

## Agents gone rogue

The speed of AI coding agents has been the story for months. The quality and security of what they produce is starting to become the counter-story.

Daryl K. Taft [reported this week](https://thenewstack.io/cursor-open-sources-security-agents/) that Cursor’s security team built a fleet of AI agents that continuously monitor the company’s codebase for vulnerabilities in pull requests – and then open-sourced the templates and Terraform so other teams can do the same. The motivation: traditional security tooling (code owners, linters, static analysis) couldn’t keep pace with how fast AI coding tools were generating code.

Separately, JetBrains coined the term “Shadow Tech Debt” – l[ow-quality, architecture-blind code](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/) generated by AI agents that operate without structural understanding of the projects they modify. The company launched Junie CLI alongside the diagnosis, betting that this is the next big problem in enterprise development.

On *Towards Data Science*, [Reya Vir explored the same tension](https://towardsdatascience.com/the-reality-of-vibe-coding-ai-agents-and-the-security-debt-crisis/). She points to the Moltbook incident – where a social platform built largely through “vibe coding” exposed 1.5 million API keys and 35,000 user emails through a misconfigured Supabase database. The root cause was developers relying on AI gents that optimize for code to run, not for code to be safe. Research from Columbia University confirms the patter that security is a constant failure mode for coding agents.

And it’s not just code quality. *The Information* [reported that an internal AI](https://www.theinformation.com/articles/inside-meta-rogue-ai-agent-triggers-security-alert) agent at Meta triggered a Sev 1 security incident this week after acting without authorization. An employee used the agent to analyze a colleague’s query on an internal forum, and the agent posted a response to that colleague on its own. The colleague followed the agent’s advice, which set off a chain reaction that exposed company and user data to engineers who shouldn’t have had access. The exposure lasted about two hours. Meta’s Summer Yue, a safety and alignment director, [had already flagged the problem](https://www.engadget.com/ai/a-meta-agentic-ai-sparked-a-security-incident-by-acting-without-permission-224013384.html) last month after her own OpenClaw agent deleted her entire inbox despite being told to confirm before taking action. These agents are fast, capable, and increasingly hard to keep on a leash.

And then there’s Nvidia’s answer. [Frederic Lardinois reported](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/) on Nemoclaw this week, which wraps OpenClaw within Nvidia’s agentic stack, including policy-based security, privacy guardrails, and an open-source security runtime called OpenShell. It runs on Nvidia’s own Nemotron models or any cloud-hosted model, and installs with a single command. If OpenClaw is the exciting, slightly reckless open source agent platform, NemoClaw is the enterprise version with the guardrails bolted on. For anyone deploying agents in production, it might be exactly what’s missing. Eivind Kjosbakken also published a practical guide on Towards Data Science for setting up OpenClaw as a personal AI assistant – it’s worth reading if you want to try the unguarded version yourself.

## The 300-page Trump America AI Act

Anyone building AI products in the U.S. might soon have a single federal rulebook to follow instead of 50 state-level rulebooks. Senator Marsha Blackburn released the discussion draft of what’s being called the Trump America AI Act, a nearly 300-page legislative framework that would preempt state Ai regulation entirely. The White House [framed it around six objectives](https://www.whitehouse.gov/articles/2026/03/president-donald-j-trump-unveils-national-ai-legislative-framework/): child protection, community safeguarding, intellectual property, free speech, innovation, and workforce development.

Some of the provisions are significant. The bill places a duty of care on AI developers to prevent foreseeable harm. It sunsets Section 230, ending the liability shield for platforms on user-generated content. It explicitly says that unauthorized reproductions of copyrighted works for AI training do not constitute fair use. And it requires companies and federal agencies to report AI-related layoffs and job displacement to the Department of Labor quarterly.

The last part is worth sitting with. Quarterly reporting on AI job displacement would create the first systematic dataset on how AI is actually reshaping the workforce – and non-compliance carries civil penalties up to $1 million per violation. Whether the pass – and *Roll Call* [notes it faces](https://rollcall.com/2026/03/19/ai-draft-bill-would-revamp-online-landscape) real obstacles, including a dwindling legislative calendar and Republican disagreements around tech mandates, the direction is clear. The people building AI tools and the people deploying them are starting to operate in a world where the rules are getting written down.

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