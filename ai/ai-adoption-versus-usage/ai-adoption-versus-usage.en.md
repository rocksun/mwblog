Every engineering org I’ve talked to this year has some version of the same chart. Seat activations climbing. Token spend climbing. Somebody’s slide says 80% weekly active. Then you sit in that team’s planning meeting, and nothing about how they build software has changed.

That gap is the actual problem, and most of the way we measure AI adoption is designed, accidentally, to hide it.

## Everything you’re measuring is a usage metric

Token spend tells you someone typed into a box. Pull request count tells you commits landed. “Percentage of code written by AI” tells you an autocomplete got accepted. None of it tells you the work got better.

Goodhart’s Law, right on schedule. The moment a number becomes the target, it stops describing reality and starts describing the incentive.

> “The moment a number becomes the target, it stops describing reality and starts describing the incentive.”

The clearest version of this failure isn’t even AI-specific. Every engineer has watched a team clear a coverage gate with tests that assert nothing. `expect(true).toBe(true)`. Line covered, number green, nothing tested. The metric was satisfied, and the goal was abandoned, and the dashboard has no way to tell the difference.

AI usage metrics have the same shape. If I tell my team that usage is a performance signal, usage goes up inside a week, and I’ve learned nothing except that they can read incentives. Which I already knew.

Better question: if you removed these tools tomorrow, what would break? Not what people would complain about. What would break. If the honest answer is “nothing, people would be mildly annoyed,” you don’t have adoption. You have a subscription.

## Three things get called adoption. Only one lasts.

When I dig into what “we’ve adopted AI” means on a specific team, it’s one of three things, and they aren’t close in value.

Someone changes their own loop. They write commit messages with it, or use it to get oriented in unfamiliar code. Real, useful, almost entirely non-durable. First hard deadline, they revert to the way they already know works. That isn’t a discipline problem. Under pressure, people take the lowest-uncertainty path available, and a new workflow is by definition the high-uncertainty one.

Someone permanently hands off a recurring job. Not “I used AI today” but “I don’t do this anymore, a workflow does, and I check the output.” That survives deadlines, because going back would mean creating work for themselves. It also leaves when they do.

Or the team changes how it does something, on purpose. Somebody decided a step in the process now runs a certain way, wrote it down, and it holds whether or not any individual is feeling enthusiastic. Only the third one survives turnover and a bad quarter.

Most orgs celebrate the first, occasionally reach the second, and never get to the third. Because the third isn’t a tooling problem. Buying licenses is a budget conversation. Changing a norm means saying out loud that the old way was worse, then owning it when the new way breaks something in week three.

> “Changing a norm means saying out loud that the old way was worse, then owning it when the new way breaks something in week three.”

At [Webflow](https://webflow.com/), the one that stuck for us was treating prompts as shared, versioned artifacts instead of personal property. People used to keep them in scratch files, tune them privately over weeks, and lose them the next time they switched machines. Now the good ones live in the repo with an owner, a note on when to use them, and review on changes, same as any other code. It cost nothing in tooling. What it took was deciding this category of thing was worth maintaining.

It’s held because it doesn’t run on anyone’s enthusiasm. New engineers inherit the good version instead of [spending a month](https://thenewstack.io/serpapi-google-search-api/) rediscovering it. When someone finds an improvement, everybody gets it rather than one person quietly getting better at their job.

## Agents start work well and own it badly

Here’s the pattern that kills adoption before a team ever reaches that third tier.

The leverage is concentrated at the start of a task. Blank page to plausible draft is dramatically faster than it used to be. Plausible draft to correct and shippable is not faster at all, and that half is still yours.

So an engineer works out that they can start five things at once, fires them all off, and feels productive doing it. Then five things come back needing review, and review runs single-threaded inside one head, on work they didn’t write and have to reconstruct from scratch. They didn’t parallelize. They serialized on their own attention, at a queue depth nobody would have picked deliberately.

They end that week busier and less certain than the week before, which is a genuinely worse experience. Plenty of people try agentic workflows once, feel exactly that, and quietly stop. Weeks later it shows up as a usage dip and gets diagnosed as a training gap.

> “Delegating to an agent has the same ceiling as delegating to a person: the review capacity of whoever stays accountable.”

It isn’t. It’s a work-shape problem. [Delegating to an agent](https://thenewstack.io/microsoft-build-scout/) has the same ceiling as delegating to a person: the review capacity of whoever stays accountable. The teams getting real value out of this got specific about which work is safe to hand off with a light check and which isn’t, instead of treating all of it as equally delegable.

## You can’t manage adoption; you can’t score

If you can’t score the output, every argument about [whether a workflow is working](https://thenewstack.io/anthropic-claude-design-overhaul/) is a vibes argument. And vibes arguments are won by whoever is most confident in the room, which is a terrible way to run engineering.

Scoring doesn’t mean benchmarks. Benchmarks tell you a model is good in general. You need to know whether this workflow is good at the specific thing your team does, which no benchmark covers. A few dozen real cases out of your own domain, graded against a rubric you wrote down, rerun every time someone changes a prompt or swaps a model. Small is fine. The point isn’t precision, it’s having a number that moves for reasons you understand.

Without it, you can’t tell a workflow that improved from one whose failures got more fluent. In a demo, those look identical.

## What I’d actually do

Kill one recurring manual job per person, permanently. Not “try AI on it.” Take it off their week and make the workflow the owner of record. One job that stays dead beats ten experiments.

Make exactly one team norm official, in writing, this quarter. One. Small enough that you’ll actually enforce it, specific enough that somebody could break it.

Stop reporting usage upward. Report the outcome the usage was supposed to produce, including the quarters where that number looks worse than usage would have.

None of this requires a new tool, which is most of the point. Tools are the cheapest part of this, and they absorb the most attention. The expensive part is being willing to change how a team works on purpose, in public, with your name on the call.

*This article was originally published on August 5, 2026, on [webflow.com](https://webflow.com/blog/ai-adoption-vs-usage-engineering-teams).*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/08/4c6207f8-cropped-6911992f-harshal_shah-scaled-1-600x600.jpg)

Harshal Shah is an Engineering Manager at Webflow, where he leads a team building AI-powered recommendation and workflow tooling.

Read more from Harshal Shah](https://thenewstack.io/author/harshal-shah/)