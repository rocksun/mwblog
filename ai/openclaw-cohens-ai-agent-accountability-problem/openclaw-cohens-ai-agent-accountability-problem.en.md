*I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

**Quick Announcement!** The Forward Deployed Engineer roadmap is now live at [Roadmap.sh](http://roadmap.sh). [FDEs are becoming](https://thenewstack.io/forward-deployed-engineer-fde-openai-google/) one of the [hottest roles in tech](https://thenewstack.io/why-the-forward-deployed-engineer-is-techs-hottest-job/), and we moved fast to [produce a step-by-step guide](https://roadmap.sh/forward-deployed-engineer) designed to bring you up to speed.

**Gavriel Cohen, the developer behind the minimalist agent NanoClaw**, found his own code inside OpenClaw, used without attribution and without his consent. He walked away from the project, publicly, and [David Eastman’s story](https://thenewstack.io/nanoclaw-openclaw-agent-security/) for *The New Stack* was the most-read story across our publications this week by a wide margin.

Here’s what I see: **We gave coding agents autonomy before building the accountability that’s supposed to come with it.** And autonomy isn’t in the future. It’s here, now. Anthropic’s recursive self-improvement report, published on Thursday, says Claude now writes more than 80% of the code the company merges. Last week I argued the tokenmaxxing era could be ending and token discipline was the new skill. The cost side is at least getting tools: Paul Sawers reports [Cursor cut prices and added enterprise spend](https://thenewstack.io/cursor-pricing-token-billing/) controls the same week [GitHub’s switch to token billing](https://thenewstack.io/github-copilot-token-billing/) sent some users’ bills to the moon.

Tokens are getting spend controls. But trust isn’t built like a product feature, and users are starting to take theirs back.

## The week no one was accountable

I read the [OpenClaw/Cohen](https://thenewstack.io/nanoclaw-openclaw-agent-security/) story more like a preview than a scandal. OpenClaw’s whole appeal is that you can run it, fork it, and use any AI model with it. The same openness is how a working developer’s code ended up inside the agent with nobody able to say who put it there, when, or under what terms. Cohen’s response matters because of what it wasn’t: Not a license complaint, not a pull request, not a settlement demand. He looked at a tool he had unknowingly helped build, concluded nobody was accountable for what it absorbed, and left. **The story went viral because suddenly, thousands of developers are curious if OpenClaw is using their code too.**

And then there’s the structural point. Darryl K. Taft reported [Aikido Security’s finding that AI coding agents](https://thenewstack.io/aikido-ai-agents-security/), given the autonomy to manage their own dependencies, are installing packages that no one owns. The headline – “*There is no accountability*” – isn’t hyperbole. It’s an accurate description of the supply chain. Neither story argues the agents don’t work. The agents work fine. They’re doing exactly what they were built to do – act autonomously – inside an ecosystem that hasn’t decided yet who owns the consequences.

Linus Torvalds had the same problem this week, too. B. Cameron Gain reported the [Linux creator’s anger at hearing claims](https://thenewstack.io/torvalds-ai-programming-productivity/) that “99% of code is AI,” and the story was widely picked up. Torvalds isn’t anti-AI. He’s reacting to a number that erases the human in the loop. The trend he’s mad at is real. Anthropic reported this week that its engineers are shipping 8x the code they did two years ago, and one employee is five months past the last line they wrote by hand.

Generated isn’t the same as authored. Authorship is what creates accountability: someone who can say what the code does, why it’s there, and who fixes what breaks. Now that AI has autonomy, it needs accountability, and fast.

# The market is starting to reprice accountability

JetBrains is taking Mellum2 where Claude Code can’t go. The company [open-sourced its coding model](https://thenewstack.io/jetbrains-mellum2-open-source-coding-model/). This means open weights running locally against enterprise codebases that can’t leave the building — the code that legal, compliance, or plain common sense keeps off someone else’s cloud. Nobody at JetBrains is claiming Mellum2 out-thinks Claude. They’re selling something different: a model you can inspect, run on your own hardware, and answer for. It’s accountability as a feature, and I think it’s the right move. JetBrains sees itself as [the last independent major developer-tools company](https://thenewstack.io/jetbrains-independent-ai-coding/) in an AI coding market increasingly tied to model labs and hyperscalers.

Google moved in the other direction this week, [pushing free, Pro, and Ultra users off the open-source Gemini CLI](https://thenewstack.io/google-antigravity-cli/) and onto the closed-source Antigravity CLI. Days after OpenClaw passed 300,000 stars, [Google also launched Spark](https://thenewstack.io/gemini-spark-vs-openclaw/), a closed agent, but also a direct answer to the most popular open agent. And after the fallout from Gavriel Cohen, selling a closed agent to first adopters might be a harder sell than Google realizes.

## What Anthropic’s recursive self-improvement report actually says

Anthropic released a significant report this week. “[*When AI builds itself*](https://www.anthropic.com/institute/recursive-self-improvement)” is the company reporting on its own automation, and it includes some startling admissions.

According to this report, Claude has already climbed the first two rungs of the research job: executing tasks and designing the approach. The third is choosing the problems, and Claude is starting to work on that too. Anthropic’s benchmarks point to an astonishing, yet raw stat: Claude went from a ~3x speedup to ~52x in a year on the company’s test of making model-training code run faster. This is a task where a skilled human needs four to eight hours to reach 4x. And when Anthropic replayed real research sessions that went sideways, its best model out-picked the researcher’s next step 51% of the time in November, 64% by April. Judgment was supposed to be the durable human edge. Now that edge is eroding too.

**The quotes from inside read like a support group**: on good days, one employee admits, “I can’t help but think nothing I do matters”; on bad ones, “I realize I have no idea what I’ve been up to anymore.” Jobs are being converted from author to reviewer in real time, and it seems like the humans are suffering.

Surprisingly, the reports says Anthropic would slow down or even pause frontier development — if other labs did the same, and if it could verify they actually had. This feels like an empty offer. Verification would be impossible, and there are trillions of dollars directed at growing AI as fast as possible.

The report points to the same conclusion everything else this week has been circling. Humans will soon stop writing code and shift to reviewing it, and human review becomes the bottleneck on AI development itself. Suddenly, the scarcest resource isn’t compute. It’s the accountable human.

But how long will businesses put up with humans slowing down progress?

For me, humans have to stay in the loop for the foreseeable future. But the loop itself is going to change shape. AI will get better at review. Tooling and guardrails will improve. Companies that resent the slowdown will try to automate the review too, using agents to check agents, and some of that will work (and some won’t).

The part that won’t be automated is the person accountable for the result.

That’s the career advice hiding in all of this. Developers who win the next few years won’t be the ones who generate the most with AI. They’ll be the ones whose sign-off means something.

The agents got autonomy first. Accountability is still a human job.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)