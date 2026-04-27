#### The surprise in building KubeStellar Console with coding agents was not the extent of the model’s capabilities, but the heavy lifting the surrounding codebase had to perform.

In mid-December, I started building [KubeStellar Console](https://www.cncf.io/projects/kubestellar/) from scratch. It’s a multi-cluster management dashboard for Kubernetes, and it sits inside the KubeStellar project in the Cloud Native Computing Foundation (CNCF) Sandbox. The stack is Go on the back end, React and TypeScript on the front, and Helm for packaging. No team. Just me and two AI coding agents running in parallel terminal sessions.

The first two weeks were the honeymoon that everyone in this space seems to describe. [Code came out of the agents](https://thenewstack.io/ai-coding-agents-level-up-from-helpers-to-team-players/) faster than I could read it. Things I’d have budgeted three days for showed up in two hours. I kept a mental list of features I’d always wanted to build and just kept calling them off, one after another.

Then it struck.

Builds broke in ways that were hard to trace. Architectural choices from the day before quietly got overwritten. Scope expanded without being asked. The agent kept touching files I hadn’t pointed it toward, and the cascade problem was the worst of it—fix one thing, then three others broke. I started spending more time reverting than reviewing. The promised 10x started to feel like a net negative, and I decided to scrap the whole approach.

That arc, from euphoria to grinding frustration, is apparently universal. The usual industry advice is to hand the agent more autonomy: let it run longer, touch more files, and self-correct. In my experience, that tends to make the failure mode worse, not better. The leverage runs in the opposite direction. The intelligence in an AI-assisted codebase lives less in the model and more in the loops the codebase wraps around it. If you want the agent to do more, the surrounding code has to measure more.

Four months on, and KubeStellar Console is now in better shape. There are 63 CI/CD workflows, 32 nightly test suites, and coverage sitting at 91% across twelve shards. Across 82 days, PR acceptance settled around 81%. Community bug reports are moving to merged fixes in roughly thirty minutes. Feature requests are landing as pull requests in about an hour. None of that was the result of a better model. What changed was what the code itself had learned to measure.

Five tightening loops got me there. I think of them as the rungs of what I’ve been calling the AI Codebase Maturity Model—Assisted, Instructed, Measured, Adaptive, and Self-Sustaining. I’ll walk through them in the order they appeared, because I don’t think they can be reordered.

## 1. Write down what you keep correcting (instructed)

The cheapest intervention, and probably the highest return, is to externalize your own preferences. I started with a CLAUDE.md at the root of the repo, followed by a .github/copilot-instructions.md file for pull request conventions. Next came a card-level development guide that cataloged the top reasons I was rejecting AI-generated PRs.

That one guide wound up covering about 90% of my rejection criteria. Sessions became more consistent. The same mistakes stopped recurring across agents. I wouldn’t call this measurement — at this point, I was still running on intuition — but it filtered out enough noise for a standard measurement to become possible.

## 2. Treat tests as the trust layer, not just the correctness layer (measured)

This was the turn that mattered most. Testing for an autonomous workflow differs from testing for a human workflow. It’s the only signal the agent has to know whether it’s making the system better or worse.

Over four weeks, I added 32 nightly suites and pushed coverage to 91% across twelve parallel shards. The suites covered compliance, performance, nil safety, accessibility, internationalization, and visual regression. Alongside that, I started logging PR acceptance rates per category into auto-qa-tuning.json. That file turned out to be load-bearing for everything that followed.

Coverage volume matters. So does breadth. But the thing that nearly undid me, and that I’d flag hardest for anyone attempting this, is determinism.

> “A flaky test in a human workflow is an annoyance. In an autonomous one, it’s a slow, quiet erosion of the entire trust model.”

One [Playwright end-to-end test](https://thenewstack.io/playwright-a-time-saving-end-to-end-testing-framework/) for drag-and-drop passed about 85% of the time. In a human workflow, that’s tolerable; you re-run it, you move on. In an autonomous workflow where test results gate merges, an 85% test is a disaster. Good PRs were being blocked at random, and weak ones were being let through. I spent three days on that single test, and it turned out to be an animation-completion timing issue in CI. The lesson generalized. You can’t build automation on top of an unreliable signal. A flaky test in a human workflow is an annoyance. In an autonomous one, it’s a slow, quiet erosion of the entire trust model.

## 3. Don’t automate until you can measure (adaptive)

With acceptance rates being logged, automation became a safer proposition. Auto-QA started running four times a day across eight layers of quality checks. The rotation weights that decide which categories of work the system focuses on began adjusting themselves based on the data. Accessibility PRs were landing at 62% acceptance, so their weight went up to 0.93. Operator-category PRs were landing at 8% (11 merges against 129 closed), so that weight dropped to zero and CI cycles got redirected.

A few more loops closed around that core:

* A triage process scanned four repositories every 15 minutes.
* A PR monitor polled build status every 60 seconds.
* An error-recovery workflow used exponential backoff to handle stuck agents.
* A GA4 query ran hourly against production analytics and filed GitHub issues for error spikes before users reported them.

> “Automation without measurement isn’t maturity — it’s failure at scale.”

The pattern across all of these is the same: measurement first, automation second. Inverting the order is how autonomous systems go off the rails. Automation without measurement isn’t maturity — it’s failure at scale.

## 4. Let the codebase become the operating manual (self-sustaining)

At some point, and I can’t point to a specific day, the system stopped needing me in the loop to operate. Its behavior was being determined by its artifacts: the instruction files, the tests, the workflow rules, and the acceptance rate history. The community started opening issues at all hours, and those issues were being triaged, assigned, fixed, tested, and queued for review before I even woke up.

One case crystallized the shift. In April, a user filed a bug reporting that a cluster was marked “healthy” while pods were stuck in ImagePullBackOff. Before I looked at it, the system had already answered that cluster health reflects infrastructure health (node readiness, API reachability), which is architecturally separate from workload health. It wasn’t a bug. It was a Kubernetes mental model that didn’t quite map to what the dashboard was showing. The design decision was already encoded in the tests, in the health-check logic, and in the docs; the agent could explain it because the codebase already knew it.

That, more than any throughput number, is what “the code is the model” actually looks like in practice.

## 5. Ask “why,” not “what”

One prompting habit did disproportionate work. Instead of “fix this bug,” I started asking, “Why didn’t you catch this?” The first phrasing produces a patch. The second tends to produce a root-cause analysis and, as a side effect, a new test, instruction, or rule that blocks an entire class of similar failures.

Commanding gets you a sequence of isolated fixes. Questioning compounds. Over time, the questions are what turn the codebase into a self-improving system, and they’re what produce the instruction files in the first place if you’re starting from scratch.

## What this might mean for maintainers and leaders

If you’re leading engineering, stop optimizing for which model you’re using. The model is a commodity component, and swapping one for another is a weekend of work. Rebuilding the surrounding feedback system is a quarter of the work. The differentiation is the intelligence infrastructure: the instruction files, the test suites, the metrics, and the workflow rules.

For [open source maintainers](https://thenewstack.io/ai-generated-code-crisis/), this directly addresses the burnout problem that keeps surfacing in CNCF community conversations. If a codebase can encode enough of a maintainer’s judgment that agents can handle triage, generate pull requests, and explain design decisions to users, then the community can steer the project primarily by filing issues.

Maintainers become architects of the system rather than its daily operators. That’s not hypothetical for KubeStellar Console. It’s working now. Whether it scales beyond a solo-maintained Sandbox project is something the broader community will need to test. I’d genuinely like to know.

Most teams are still in the first loop, writing prompts and reviewing output. That’s where everyone starts. The point isn’t to race to the last loop. The point is to notice which loop is actually blocking you and close that one next.

The codebase holds what I’ve learned. The tests catch what I can’t keep in my head. What’s still mine — and I think this part stays mine — is deciding what’s worth building, what to say no to, and what good is supposed to look like.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/817e8682-cropped-613a3f65-headshot-jts-08082020_-_andy_anderson-600x600.jpg)

Andy Anderson is a Senior Platform Engineer and Architect at IBM with over two decades of experience in distributed systems, cloud-native infrastructure, and open-source community building. He is the chief maintainer of KubeStellar Console, a CNCF Sandbox project that provides...

Read more from Andy Anderson](https://thenewstack.io/author/andy-anderson/)