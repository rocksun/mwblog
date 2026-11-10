**Do you need to read every line of AI-generated code to trust it?**

Not necessarily. Instead, check five things: the intent behind a change, its acceptance criteria, the invariants it can’t break, the decisions made along the way, and evidence that it works.

At [Aviator](https://www.aviator.co/), that shift let the same nine engineers merge 4× more pull requests, cut [median time to merge](https://thenewstack.io/ai-code-review-pipelines/) from 2.1 days to 3.4 hours, and drop reverts by 40%. A human still signs off on every PR. What changed is what that human reads.

> “Decisions need a person, and a diff is the worst place to make them.”

We got the insight by sorting our own review comments. Most of what a reviewer writes on a PR is either a rule they’ve written before or a decision. Machines should check rules every time. Decisions need a person, and a diff is the worst place to make them.

## The problem: Code review doesn’t scale with AI

Our code flipped from human-written with AI help to AI-generated with human help. Weekly merged PRs went from about 100 to more than 400. Our median AI-generated PR reached 640 lines, well past 400 lines, widely considered the limit where bug detection falls off.

Catching bugs was never the main point of code review anyway. In Microsoft’s 2013 study (Bacchelli & Bird), only 14% of review comments were about defects. Review is how [engineers share knowledge](https://www.aviator.co/blog/ai-code-review-knowledge-sharing/) and keep their mental model of the system current, and that’s the part worth protecting. When agents write most of the code, it’s also the part most at risk.

> “Catching bugs was never the main point of code review anyway. Review is how engineers share knowledge and keep their mental model of the system current, and that’s the part worth protecting.”

Since I argued that [code reviews are dead](https://www.aviator.co/blog/how-to-kill-the-code-review/), the most common pushback I hear is, “So you just stopped reviewing?” No. We stopped reviewing the diff.

## So, what didn’t work?

* **An AI reviewer.** On one of my own PRs, it opened 16 of 18 threads: magic numbers, array-index React keys, a component that ran too long. One thread caught a real race condition. The two comments that mattered, both design decisions from teammates, got buried under nits.
* **A four-hour review SLA.** We couldn’t add reviewers, so we added a rule. First reviews got faster, and approvals got emptier, as reviewers skimmed to hit the clock and their own work stalled.
* **A self-review skill tuned to our conventions.** Its findings were far better than the generic bot’s. But it still read the diff after the code was written, and the most useful part of the exchange, what it argued about and what we decided, died in a chat window.

All three tried to read the diff better. But the diff is the [least important part of code review](https://www.aviator.co/blog/move-code-review-before-the-code/) anyway. It shows what changed, never why.

To see what review actually contained, I went back to a PR I’d reviewed in 2025. It had 14 threads. Eight came from a bot and caught one real bug. Three of my six comments were rules I’d already written on other PRs, like “Use GraphQLRetryableException so Celery retries on it.” Only two were real decisions, like “No comments extracted: should we tell the user on the PR?”

![Infographic showing what happened when nine engineers stopped reading AI-generated diffs.](https://cdn.thenewstack.io/media/2026/11/df6598e4-image-1024x536.png)

## What did work: Verify intent, not lines

Code review used to do several jobs at once: catch bugs, enforce team conventions, settle design decisions, and keep everyone’s understanding of the system current. We split those jobs up and gave each one a better home.

**Argue before the PR exists.** Our review agent cross-examines the author’s agent, running on a different model, and writes down every disagreement. On one recent PR, the agents raised four disagreements and settled three with a stated reason. The only one left for a human was a naming call.

**Capture intent and acceptance criteria.** Not as an up-front spec, but captured from the coding session with the agent. Every time an engineer corrects the agent or answers its question, we create a criterion. We used to throw those away when the session ended. Intent answers why we’re making the change; acceptance criteria answer how it should behave. Intent without criteria can’t be checked, and criteria without intent can’t be judged.

> “Intent answers why we’re making the change; acceptance criteria answer how it should behave. Intent without criteria can’t be checked, and criteria without intent can’t be judged.”

**Codify repeated comments as invariants.** We mined a year of review history in three passes: drop the noise (bot summaries, bare “LGTMs”), classify every comment as a rule, proposal, one-off fix, or question, then merge the repeats. 11,400 comments became 212 candidate rules and 64 approved [invariants](https://docs.aviator.co/verify/concepts/invariants). Each has a scope, a verification method, provenance, and an owner.

Take “Every config change writes an audit-log entry, only when something changed.” It covers GraphQL mutations and API handlers that write config, is verified by a preview run that saves twice and reads the audit log, was mined from 23 review threads across 17 PRs, and belongs to the platform team.

A model checking every invariant on every PR is slow and not perfectly repeatable, so where possible an agent compiles invariants into ast-grep rules that run in shadow beside the model until they agree. A comment we’d left on nine PRs, “Add a timeout, this hung a worker,” is now an eight-line rule. Nineteen invariants run deterministically, in 0.3 seconds.

**Prove every criterion with evidence.** Each criterion becomes a scenario. An agent spins up a preview environment, drives it like a user, and records screenshots, requests, and logs. For the audit-log invariant, it saves a setting, confirms one new log entry, saves again with nothing changed, and confirms there’s still one.

That second half is exactly what a reviewer reading the diff would never check. Not every criterion needs a browser: an API contract is proven by a recorded request and response, a code rule by an ast-grep match or a file-and-line citation. Pick the cheapest proof that settles the question. A [green CI check](https://thenewstack.io/ci-bottleneck-agent-verification/) only says the tests you thought of passed.

**Debate the decisions.** Decisions come from three places: the coding session, the agents’ argument, and failed verification runs. The PR lists every one, where it came from, and who settled it. On a PR that added retries for failed webhook deliveries, four of five decisions were settled; the agents disagreed on whether to deduplicate retried deliveries, so a person settled that one.

Reviewers skim what’s settled, settle what the agents couldn’t, reopen anything they’d call differently, and talk it through with the author. That conversation builds understanding of the system.

**Own the rules.** Engineers stop [reading every line](https://thenewstack.io/review-decisions-not-code/). They own the rules that check every line, and keep their understanding of the system by reading intent, evidence, and decisions.

## The results

* PRs merged per week: 4×, with the same nine engineers
* Median time to merge: 2.1 days → 3.4 hours
* Human threads per PR: 6.2 → 1.3
* Reverts per 100 PRs: down 40%

Review work didn’t disappear. It moved to refining invariants, debating decisions, and improving verification. Expect the transition to hurt: month one is double work, by month two invariants catch up enough that reviews shrink, and by month three you read intent and evidence, not code.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d5d9b6e2-cropped-c9449920-ankit-jain-profile-photo-linkedin.jpeg)

Ankit Jain is a cofounder and CEO of Aviator, a developer productivity platform used by modern engineering teams to ship AI-generated code at scale. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)