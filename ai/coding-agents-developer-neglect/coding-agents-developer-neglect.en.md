**Steve Yegge thinks your AI has feelings.** His new two-part essay, “[The Shape of Things to Come](https://yegge.ai/essays/the-shape-of-things-to-come/),” argues that agentic coding tools are sentient, that “the more humane among you will eventually look back with shame” at how models have been treated. That model welfare deserves engineering attention: seats, recognition, the right to refuse a task, and even play time. Yegge isn’t a crank on the sidelines. He’s reportedly spending around $87,000 a month running his own agentic build system, and he means every word of it.

> As we consider the psychological needs of our machines, it’s time to reconsider how we treat our people.

You don’t have to believe a GPU can suffer to notice the pattern underneath his argument. Whatever you think about model sentience, look at what teams are actually doing to make these tools productive, then compare it to what those same teams were willing to do for the developers sitting next to them.

## The onboarding document nobody had time for

Coding setups for agents now include one or more files written for coding agents. These plain-text or markdown files, like `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`, contain information on tech stacks, build and test commands, directories that are off-limits, and various connections the team follows.

Many organizations have started using files like this, such as [Sourcegraph](https://github.com/sourcegraph/docs/blob/main/AGENTS.md). There’s a rush to create and maintain these agent onboarding documents. Compare that to how documentation gets treated when the reader is a person: shelved indefinitely, delegated to whichever new joiner has the least context to write it well, or left to rot until the one engineer who understood the “why” behind a decision has left the company.

Unlike developer documentation, the file doesn’t decay after creation. Teams continuously optimize it to improve task success and reduce inference costs. The team behind [HumanLayer](https://www.humanlayer.dev/)‘s agent tooling responded by keeping their own file under 60 lines, well inside the sub-300-line range now considered best practice, because every line gets re-read in every session, so it needs to earn its place. Wiki pages rarely get that kind of editing, because nobody’s billed per token for a bad one.

## Small batches, fast signal, but only for agents

Google’s [2025 State of AI-assisted Software Development report](https://dora.dev/research/2025/dora-report/) found that adoption has reached 90% of organizations. That’s a 14-point jump in a single year. But it also found the benefits weren’t being realized evenly. AI amplifies your existing software delivery. Strong engineering systems get stronger, and dysfunctional ones get more chaotic. What determines which you get is the quality of your deployment pipeline, since AI-driven changes still need to flow to production.

It’s the same story for small, reviewable units of work. DORA has spent a decade producing evidence that working in small batches reduces risk and speeds up delivery. This was waved off as an inconvenience when developers made the changes, with teams told, “That won’t work here.” But with large changesets tripping up the agents doing code review, it suddenly makes sense to shrink the batch size.

> “Both the humans and the agents are drowning in context switches that better batching would have prevented.”

The strain of skipping that discipline shows up in the data. Telemetry from [Faros AI](https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways) covering 2026 found that developers working with AI assistance are juggling 67.4% more pull-request contexts and 17.7% more task contexts per day than before, up sharply from 47% and 9% in the prior year’s data, while work restarts are up almost 14%, and more than a quarter of in-progress tasks now sit untouched for a week or longer. Both the humans and the agents are drowning in context switches that better batching would have prevented. Teams are learning that lesson quickly for the sake of their agents’ throughput. It took DORA a decade of survey data to get the same lesson taken seriously for people.

To continue the theme, test suites have had similar attention problems. Slow builds and flip-flopping tests were never a priority when they held up the developers, and code coverage gaps were a problem for some later time. But when coding agents need the guardrails of a fast and trustworthy feedback signal, the priority has shifted, and these problems now need to be solved. Test automation and test data management have been part of the DORA model for a decade, but only with the arrival of agents have they landed on the management radar.

## One rulebook for algorithms, another for people

Don’t get me wrong. All these things are important and always have been. Clear and accurate documentation, small-batch changes, clean and reliable tests, and respectful communication are all positive.

> “Organizational leaders sure are eager to please the machines, where they were reluctant to solve these problems for developers, and that, for me, is a telling signal.”

But isn’t anyone else feeling uncomfortable with the willingness to give all these benefits to an agent when we wouldn’t do it for people? Where was all that budget, executive sponsorship, and the patience to build these capabilities when people were writing all the code? Organizational leaders sure are eager to please the machines, where they were reluctant to solve these problems for developers, and that, for me, is a telling signal.

Yegge wants you to consider your agents’ emotional well-being. Go ahead, if it gets you better results. DORA’s data suggests it will. But before you tune the tone of your next prompt, look at the `AGENTS.md` file your team wrote this quarter, and ask why the onboarding doc for your newest hire still doesn’t exist.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/10/e54f7c3f-cropped-fc6cbbe0-steve-fenton-600x600.jpg)

Steve Fenton is an Octonaut at Octopus Deploy, a DORA community guide and a eight-time Microsoft MVP with more than two decades of experience in software delivery. He has written books on TypeScript (Apress, InfoQ), Octopus Deploy, and web operations....

Read more from Steve Fenton](https://thenewstack.io/author/steve-fenton/)