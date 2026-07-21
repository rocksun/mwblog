### Why we’ve stopped noticing the real improvement opportunity

Since AI arrived, many people have mentioned that the bottleneck has shifted from coding to code review. This isn’t quite right, as coding wasn’t the bottleneck in the first place, and it’s not code review now. The reason we think either of these things is constraining the flow of value is that mossy hill we all stare past when we look at the mountains.

Here’s a simple test. For the application or service you work on, how many changes have passed code review but haven’t yet been deployed and enabled for users? If the answer is none or one, accept my apologies: in your specific case, I’m wrong. But I rarely get that answer. It’s usually more than one, and that tells you the bottleneck is elsewhere.

![Bar chart showing number of changes per deployment batch.](https://cdn.thenewstack.io/media/2026/07/f8408c14-image1.png)

*Number of changes per deployment batch (Source:* [*Octopus Deploy*](https://octopus.com)*)*

We’re conducting original research in this area right now, and half of all teams have between 2 and 10 changes sitting in a batch, and a quarter have 11-50. Overall, more than 90% of teams ship in batches rather than one change at a time.

> “Coding wasn’t the bottleneck in the first place, and it’s not code review now.”

This number reveals an industry-wide visibility gap. People believe Claude Code, Cursor, and GitHub Copilot have shifted the bottleneck from coding to code review, but that ignores everything that happens after the review, and that’s not a personal failing; it’s an industry-wide misperception.

We’ve grown so used to working in batches that the practice looks like it belongs. It’s overgrown with moss, indistinguishable from the surrounding hills. When you search for ways to [speed up software delivery](https://thenewstack.io/jfrog-upgrades-ai-tooling-governance-to-speed-up-software-delivery/), you won’t see it, because it doesn’t look like a problem. It looks just as things have always been.

## What happens when AI floods a batch

Writing code is a small part of a longer value stream that starts with an opportunity and ends when a user gets the value they need. The impact across this whole value stream is lumpy. AI will help more in some areas than others, and the end-to-end benefit depends on you noticing the areas where work accumulates.

[GitLab’s 2026 AI Accountability Report](https://about.gitlab.com/resources/ai-accountability-survey-2026/) found that 85% of respondents agree AI has shifted the bottleneck from writing code to reviewing it. Yet we can see from deployment batches that 92% of these people are likely wrong, because if there’s accumulation after the code review, it means code review isn’t the bottleneck. It also means speeding up the reviews will make the real bottleneck worse.

This isn’t to say increased coding speed doesn’t put pressure on code review. [Faros AI’s research](https://www.faros.ai/blog/ai-software-engineering) across 10,000 developers found that teams with high AI adoption merge 98% more pull requests, but review time for those changes increases by 91%, and the average pull request size increases by 154%. [Cursor’s own study](https://cursor.com/blog/productivity), run with a University of Chicago economist, found companies merge 39% more pull requests once its coding agent becomes the default.

However, approving changes faster only works if the change then flows smoothly into production. In the majority of cases, it simply moves into the queue of changes awaiting further handling, such as testing and deployment. If you up the rate and size of changes passing through the review stage, pressure is simply transferred to the real bottleneck.

> “If you up the rate and size of changes passing through the review stage, pressure is simply transferred to the real bottleneck.”

Code review looks like a constraint only because it has a visible queue, while the downstream queues are hidden by their general acceptance across the industry. The job of your pipeline is to get changes to production, where they can be used, not to gather them in a “pending deployment” queue.

And as all those unreleased changes accumulate, risk increases with them.

## Batches are signposts

Ask the batch-size question, and you’ll find what’s really constraining your value stream: a manual verification step, a  [cumbersome change approval](https://thenewstack.io/stop-wasting-ai-investment-on-a-broken-change-approval-process/)  or release train process, or no easy way to deploy changes. Not coding. Not code review.

You were likely working in batches before you started your AI initiative. The introduction of AI will increase your batch sizes, which can cause problems. Increasing code review throughput doesn’t solve the problem; it simply moves changes to the bottleneck faster.

Using the true constraint to set the pace of your whole value stream will help you invest in solving the right problem. If your retrospectives keep failing to produce noticeable improvements, you’re likely missing the batch problem. It’s why some AI initiatives pay off while others flop.

## The studies miss it, too

Research on the impact of AI is useful, but, like many studies on this topic, it stops at the point where code is merged. It looks at [open pull requests](https://thenewstack.io/ai-generated-code-crisis/), merged pull requests, and hours spent reviewing. None of it asks how long changes wait after the review, or how many are bundled together before anyone sees them in production. Without that number, you can’t find the real constraint.

Having invested in AI to speed up coding, you’ll be tempted to fix code review next, or give up on code reviews altogether. If you’re shipping in batches, neither will make much difference to how quickly you remove risk or deliver value to the people using the software.

The reason your organization resists fixing the batch problem is the real problem you need to solve.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/10/e54f7c3f-cropped-fc6cbbe0-steve-fenton-600x600.jpg)

Steve Fenton is an Octonaut at Octopus Deploy, a DORA community guide and a six-time Microsoft MVP with more than two decades of experience in software delivery. He has written books on TypeScript (Apress, InfoQ), Octopus Deploy, and web operations....

Read more from Steve Fenton](https://thenewstack.io/author/steve-fenton/)