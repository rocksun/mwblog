Some people will tell you agents will take all our jobs. Others insist they are useless. Leadership at many companies mandates “AI usage” without explaining what that entails, leaving engineers confused.

We use coding agents at ClickHouse. They work. But they don’t work for everything, and the line between “use the agent” and “don’t bother” moved several times during 2025. Here is where we landed, and how we got there.

## The three levels of AI-assisted coding

It helps to break the space into three levels.

**Level 1: copy-pasting from a chat.** You ask a model a question in a browser tab and paste snippets into your editor. Many engineers have been doing this since 2023. It is still useful for exploration. Compared to agents, it is obsolete.

**Level 2: agents in your CLI or IDE.** The agent reads your codebase, runs commands, edits files, builds, tests, and commits. You hand-hold it for hard tasks and [let it run for routine ones](https://thenewstack.io/automate-routine-tasks-with-an-ad-hoc-ansible-script/). This is where most of our day-to-day work happens.

**Level 3: autonomous agents in isolated environments.** Multiple agents in feedback loops, spec-driven development, and orchestrated multi-agent setups. We have a few examples in production, but the tooling is still maturing, and results from long autonomous loops can be dubious.

If you tried an agent six months ago and it failed on your codebase, you probably concluded that agents are toys. That conclusion was reasonable then. It is not reasonable now.

## What changed our minds

I was skeptical about agents on the main [ClickHouse C++ codebase](https://github.com/ClickHouse/ClickHouse) for most of 2025. Early Claude Code (February 2025) was useful for JavaScript boilerplate and one-off Python scripts. It got lost in our C++ code. Even at our October 2025 engineering offsite, about half the team had never seriously used an agent. There were some sporadic wins, but no systematic ones.

> “Since Opus 4.5, agents have been usable for daily work on a large C++ codebase. 2025 was the year of the tools. 2026 should be the year of productivity gains.”

[That changed with Claude Opus 4.5](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/) in November 2025. I started giving it small, over-specified C++ tasks. Then bug investigation from CI logs. Then small features. It exceeded my expectations every time. Since Opus 4.5, agents have been usable for daily work on a large C++ codebase. 2025 was the year of the tools. 2026 should be the year of productivity gains.

## Where agents work for us today

A few scenarios where the value is now clear:

**Boilerplate and integrations.** Repetitive build-system changes, config edits across many files, JDK installation dances, Kubernetes manifests. Agents make fewer mistakes than humans on this kind of work, and they don’t get bored. This is the right place for any team starting out.

**Merge conflicts.** Agents resolve them better than humans do in nearly 100% of cases. The “agent does, you review” pattern produces higher quality code than typing it yourself, because reviewing code you just wrote is much harder than reviewing code somebody (or something) else wrote.

**Code review.** We tried integrating GitHub Copilot, Cursor’s bugbot, and others. We ended up [writing our own bot](https://github.com/ClickHouse/ClickHouse/blob/master/.claude/skills/review/SKILL.md) that invokes Copilot CLI from a script with our own review instructions. The quality continues to surprise me. Human reviewers now focus on architecture; the bot catches resource leaks, race conditions, and corner cases.

**[Fixing flaky tests.](https://thenewstack.io/how-to-fix-flaky-tests/)** ClickHouse CI runs 20 to 80 million tests across about 600 commits and 300 pull requests a day. We never mute flaky tests or retry them, so every failure must be investigated. For years, we couldn’t keep up. In January and February 2026, with help from agents, I submitted around 700 pull requests fixing tests and CI infrastructure. We went from roughly 200 findings a day to 3 to 5 per 10 million test runs. We now also have two autonomous agents opening PRs and finding edge cases. This single use case justifies the entire investment.

**Investigating bugs.** Agents are good at reading logs, forming hypotheses, and pushing back when prompted. They are also good at producing plausible-but-wrong hypotheses, which is the dangerous part. Outcomes depend heavily on the engineer’s judgment: an experienced SRE arrives at the right answer faster, while a less experienced colleague may follow a confidently sounding false lead. One [hard concurrency bug](https://github.com/ClickHouse/ClickHouse/pull/99483) that had defeated three human attempts was eventually fixed by Opus 4.6 in a one-line change, after about an hour of reasoning, with full explanation and tests.

## Recommendations

If you want one practical takeaway from a year of this, take seven.

1. **Treat AI as a tool of thought, not a replacement for thinking.** It is an extension of your editor, not your engineering judgment.
2. **It is a multiplier.** Strong engineers get sharper with agents. Weaker engineers cause more damage. There is no shortcut around understanding the problem.
3. **Start small, raise expectations gradually.** Begin with boilerplate, merge conflicts, and repetitive refactors. When those go well, push toward harder tasks. Skeptics who jump straight to large, complex tasks will only reconfirm their skepticism.
4. **Always validate.** More tests, more ways of testing, more fuzzing, more randomization. The headroom in agent-assisted work is in your CI, not in the prompt.
5. **Use the latest models, and keep at least two providers handy.** Model providers experience downtime, sometimes daily. Switch between Claude Code, Codex CLI, and others.
6. **Save guidance to CLAUDE.md or AGENTS.md, but keep it short.** Long instruction files get ignored. Avoid telling the model what *not* to do, as that often has the opposite effect of what you intended.
7. **Be specific.** Agents reward complete specifications. Saying exactly which files, which functions, and which approach gets better results than vague prompts, and it preserves your engineering skill in the process.

> “Treat AI as a tool of thought, not a replacement for thinking.”

## What’s next

We are still early. Beyond CLI agents, we are deploying agents for preliminary triage of bug reports, automatic reverts of bad changes, agentic testing of new features, and continuous analysis of problematic workloads. Level 3 (genuinely autonomous coding loops) is this year’s work.

It was reasonable to be skeptical about agentic coding in 2025. It is not reasonable anymore. The models are capable, the tools are mature, and the productivity gap between teams that use agents well and teams that don’t is widening. If you are a strong engineer who is not afraid of AI, this is a good moment to pay attention.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/05/39e0be26-alexeyheadshot.jpeg)

Alexey Milovidov is co-founder and CTO of ClickHouse, Inc. Alexey has 17 years of experience designing, developing, and operating data-intensive applications. He started work on ClickHouse in 2009 and initiated its release in open source in 2016. Before ClickHouse, he...

Read more from Alexey Milovidov](https://thenewstack.io/author/alexey-milovidov/)