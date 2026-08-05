**For the final two weeks of the year**, Temporal clears its calendars. The company calls it a reading period: no meetings, just time to explore, learn, and build. Over the ‘25 holidays, co-founder and CTO [Maxim Fateev](https://www.linkedin.com/in/fateev) spent his time with coding agents. He came back describing work that once took six months, now done in less than thirty days, according to the company. Co-founder and CEO [Samar Abbas](https://www.linkedin.com/in/samar-abbas-381997/) credits that break with setting the company’s AI posture for the year. A fellow co-founder returning with numbers like that, he says, is a stronger argument than any company directive.

That shift, from a veteran engineer to a veteran engineer *with Claude Code*, led Abbas toward redirecting the company’s efforts. [Temporal](https://temporal.io/) sells durable execution, the failure-resistant plumbing that keeps long-running software alive through crashes and outages, and it sells it to companies that cannot afford downtime. Nvidia and Netflix are among the companies using its workflow technology.

In February, the [company raised $300 million](https://www.linkedin.com/posts/samar-abbas-381997_today-marks-an-incredible-milestone-for-temporal-share-7429538871408807936-HEj2/) at a $5 billion valuation on the promise that it can make agentic AI reliable for everyone else. Abbas, Temporal’s CEO who swapped roles with now-CTO Fateev in 2024, decided the company had to prove that on its own first. He calls the effort “AI for Temporal.”

## **AI adoption as a job requirement**

“We are a company of builders, which means it’s not just engineering,” Abbas tells *The New Stack*. “The entire company needs to re-evaluate how business gets done and how it uses these tools.”

At more than 500 people — 200 of them engineers — that is a lot of re-evaluating. The burden lands on every employee, he says: Examine your own daily workflow, bring some curiosity to the tools, and change how the job gets done. The expectation is not optional, and Abbas was blunt about it to me. Temporal does not mandate a single product, but it does expect people to change how they work.

> “If you are still not adopting the right tools to get better, you don’t have a role here at Temporal.”

“If you are still not adopting the right tools to get better, you don’t have a role here at Temporal,” he says. The requirement isn’t to use a specific product, but rather a mandate to adopt the work.

He frames that around growth rather than headcount. Temporal is spending to unlock new work, Abbas says, not to run the same company with fewer people. He does not rank employees on a usage leaderboard because he thinks it creates the wrong incentive. The demand also cuts against the company’s own grain.

> Abbas asking Temporal employees to turn experimental without turning reckless, and he says that cultural shift is the harder half of the work.

One of Temporal’s core values is what Abbas calls “reliable as gravity.” Temporal is conservative when it bets on a technical stack. He is asking it to turn experimental without turning reckless, and he says that cultural shift is the harder half of the work.

The AI Operators

Temporal

Samar Abbas · Co-founder & CEO








Stack
Spend
Team
The Win
The Fail
Hard Truth

Engineering

* **Claude Code:** the default coding tool, adopted on its own after the holidays
* **Cursor** plus foundation models mostly from OpenAI and Anthropic
* Open-weight models not approved internally; deemed unproven on security and privacy

Company-wide

* **Claude Desktop** puts app-building in non-technical hands
* **Notion + MCP** as the shared knowledge base; Slack AI for status
* Built in-house on Temporal: Deputy (security workflow) and model routers

Up ~5x this year, mostly coding agents

* Vendor costs tracked in Vantage, with hard spending limits
* Finance and engineering review the outliers every two weeks
* No employee token leaderboards, by design
* No absolute dollar figure on the record

A company of builders

* 500+ employees, 200+ engineers, fully remote
* Every function must rebuild its own workflows, not just engineering
* No mandated tool and no usage leaderboard
* Blunt line: adapt or “you don’t have a role here at Temporal”
* Framed as growth, not headcount cuts

20-30%
Faster feature shipping at the same-sized team, per Abbas

* BDR is the most AI-native team; outbound runs as Temporal workloads, hours to minutes
* Revenue roughly doubled this year, by Abbas’s account
* No direct correlation established between AI use and the revenue
* Recruiting prep also compressed from hours to minutes

AI slop overwhelmed the reviewers

* Cheap generation collapsed the cost of producing sloppy work
* Reviewers, not authors, became the bottleneck
* Unreviewed AI work reached slide decks and even websites
* Fix is cultural: self-review before you hand off

> “It’s not about shipping features faster. It’s about shipping value customers care about.”

Samar Abbas, Co-founder & CEO

On why faster shipping is not the same as value, a gap he says he still cannot measure.

On the engineering side, the tooling is deliberately unmandated. Temporal enables the tier-one options, Cursor and foundation models mostly from OpenAI and Anthropic, and lets engineers settle on what works. Claude Code became the dominant choice on its own after the ‘25 holidays, Abbas says.

What the company has not done is bring open weights inside. Temporal has not broadly approved open-weight models for internal use, which Abbas says remain unproven for its security and privacy requirements. There is no formal model-review process yet; a central AI team vets each new model for security before it is opened up across the company.

Abbas splits the company into two adoption problems: the technical users and everyone else, and puts the same demand on both. The most surprising adoption is happening away from the engineers. Abbas tells me a nontechnical member of Temporal’s recruiting team used Claude Desktop to build recruiting tools of their own, a job-description builder and an interview-plan builder that turned hours of scattered prep into a running start.

That project is growing into a sourcing agent that pulls and pushes candidate data across Notion and spreadsheets and ranks matches. The knowledge the sourcing agent draws on lives in Notion, wired through MCP into the company’s other systems of record. For a 500-person remote company, that wiring has done more for the non-technical side than any coding tool, letting low-code users reach systems they could not touch before, with whole workflows migrating into Notion pages as a result.

Day-to-day coordination runs through Slack, where Abbas says its AI features have replaced much of his old habit of pinging people for a status update.

Abbas smiles when he tells me the clearest payoff so far is not in engineering at all. Temporal’s business-dev reps, the team that researches prospects and drafts outbound messages, have become the most AI-native group in the company. Work that used to take hours, pulling data from a dozen places and turning it into a first outreach draft, now runs as a custom workload the team builds on Temporal and finishes in minutes. It is the AI-for-Temporal idea: a non-engineering team building on the company’s own infrastructure to turn a slow, manual process into a fast one. What excites Abbas is the loop as much as the saved hours.

## **Review bottlenecks and AI slop**

Like at other organizations, Temporal is seeing AI improve processes but also shift bottlenecks. Point AI at one workload, clear the obvious constraint, and the bottleneck jumps somewhere else. Write more code and review becomes the choke point. It’s the pattern Abbas has become an expert at, and it’s why he distrusts easy wins.

The place it bit was where a reliability company like Temporal would least tolerate it. When code got cheap to produce, reviews got expensive. “AI slop is a real thing,” Abbas says. AI, he argued, has lowered the cost of producing sloppy work so much that reviewers are being flooded with it.

On critical infrastructure, the bar has not moved: Every line still gets read by a person before it’s committed, which makes the reviewer, not the author, the new constraint. It is a squeeze other engineering leaders are feeling, too. Temporal’s fix is cultural. It has made it acceptable to send work back the moment it’s clear the author did not read it themselves first. The slop is not only in code. Abbas has seen unreviewed AI-generated competitor analysis land in slide decks, and similarly sloppy material reach websites.

The AI bill is moving fast, too. AI costs have increased roughly fivefold this year, Abbas says, and most of the increase comes from coding agents. Temporal pulls every vendor charge into Vantage, sets hard ceilings, and every two weeks, finance and engineering meet over the outliers to decide, case by case, whose limits should rise or fall based on the usage patterns. What it will not do is turn that data into a scoreboard.

> “A lot of companies created a dashboard of token consumption. We’re not big fans of that, because it creates this race where I need to become the leader in token consumption.”

“A lot of companies created a dashboard of token consumption,” Abbas says. “We’re not big fans of that, because it creates this race where I need to become the leader in token consumption.” Temporal keeps the usage data, he says, but does not expose it as an employee leaderboard or tie it to performance reviews.

Abbas recalled a runaway workflow at an earlier company that ran up $4 million in compute spending on AWS. Temporal’s answer is a value it calls “fly together”: Give people a budget, expect them to spend it like their own money, and catch the runaways with limits instead of shame.

Where the company did automate, it built the automation like software. Temporal’s security team used to file vulnerabilities as tickets and wait for engineers to prioritize them over feature work, which created constant friction between the teams. Now the team runs the whole lifecycle as one long-running durable workflow built on Temporal itself, an internal tool it calls Deputy: Find the flaw, generate the fix, open the PR, merge it, run CI, and roll it out. The security team’s role moved from filing issues to helping ship fixes.

## **Durable execution for agents**

That internal work is also the commercial argument. The problem Temporal spent years on, keeping long-running work alive across failures, is the one many teams building production agents are now encountering.

“These agents are becoming more long-lived, more asynchronous, more mission-critical,” Abbas says. “That is exactly the problem space we’ve been trying to solve with durable execution.”

He describes Temporal’s core as an open foundation model: model-, language-, and cloud-agnostic, with an open-source server companies can run themselves. Inside Temporal, that has taken a solid form. Abbas says the company built an internal platform on Temporal where a non-technical employee can describe an app to Claude Desktop and deploy it in one click.

The guardrails, identity, security, and the MCP connections are wired in, and Temporal’s own model routers keep any single provider from becoming a dependency. The company used its Replay conference in May to make the same case to customers, where it introduced serverless workers, durable streaming, and other features positioned for agent workloads.

For all the speed, Abbas is unusually willing to say he cannot prove it is worth it. Engineering is shipping features 20% to 30% faster with the same-sized team, he says, and he says revenue has roughly doubled since the start of the year, though he is careful to add that he has established no direct correlation between the two.

> “It’s not about shipping features faster. It’s about shipping value customers care about.”

He is skeptical of the tidy productivity numbers, that counts of PRs and lines of code, that are supposed to justify the bill. And he thinks the old founder playbook is part of what broke. The advice he got from investors was to do first-principles thinking on product and hire good leaders to run finance, hiring, and go-to-market the standard way. In the AI era, he says, that is backward. The functions everyone used to copy from a playbook are the ones now worth reworking from the start.

Which leaves the number he wants and does not have. “It’s not about shipping features faster. It’s about shipping value customers care about,” Abbas says. And he has yet to see a metric that directly connects the company’s AI use to that outcome.

Temporal knows what the tools cost. It knows they make the company faster. What it still cannot prove is that its customers can absorb the output. For now, that is the bottleneck no agent has cleared.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)