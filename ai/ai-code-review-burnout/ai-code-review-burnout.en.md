Every team I talk to has the same problem. Their best engineers, the ones who care most about code quality, are drowning in review queues they can’t keep up with and don’t enjoy. Some experienced engineers complain, and some point-blank [refuse to review AI-generated code](https://www.reddit.com/r/ExperiencedDevs/comments/1towli9/today_i_announced_that_i_wont_be_reviewing_ai/).

I run a [community](https://dx.community/) of senior engineers and engineering leaders, and they all name AI code review bottlenecks among their top concerns. In [one study](https://annievella.com/posts/the-software-engineering-identity-crisis/), 77% of engineers said they spend less time writing code now. They put that time into reviewing AI output.

## The job shifted from crafting to verifying

Teams with high AI adoption are merging [98% more PRs](https://www.faros.ai/blog/how-ai-coding-tools-impact-software-engineering), and review times went up 91%. [Engineers didn’t sign up to spend their days](https://thenewstack.io/survey-engineers-want-to-code-but-spend-all-day-on-tech-debt/) reading machine-generated diffs. But that’s increasingly what the job demands.

The engineers who feel this most aren’t the ones resisting AI. They’re the ones who adopted it first, care most about code quality, and built the review culture their teams depend on. Those same people now have 15 PRs, 400 lines of code each, in their queue every day.

## Why reviewing AI-generated code is harder

When a colleague writes code, the intent travels with them through the review process. They can explain the tradeoffs they considered, the alternatives they rejected, and the constraints they worked within. Even if unwritten, that context is accessible.

> “When AI writes code, the reasoning is gone. The reviewer is left reverse-engineering intent from a diff.”

When AI writes code, the reasoning is gone. The reviewer is left reverse-engineering intent from a diff. That is a fundamentally different cognitive task. What makes it worse is that AI-generated [code passes the eye test](https://thenewstack.io/go-language-ai-agents/).

### Five shades of AI slop

**Plausible but wrong.** The code reads coherently and handles the happy path, but edge cases reveal misaligned assumptions. These bugs are difficult to catch in review because they require understanding what the code was supposed to do, not just what it does.

**Over-engineered.** AI models are trained on vast bodies of code, including enterprise patterns and production-hardened architectures. Asked to solve a problem that really needs 15 lines, a model may produce a 200-line abstraction layer that anticipates a generality nobody asked for.

**Convention-blind.** Models generate good generic code, not code that fits your system. Your repo has conventions around naming, error handling, logging patterns, module boundaries. AI frequently ignores them.

**Confidently hallucinated.** Calls APIs that don’t exist, uses deprecated methods, invents config options. Sometimes caught immediately, sometimes only in production.

**Cargo-cult patterns.** Copies structures without understanding why. Retry logic where retries make no sense. Circuit breakers for calls that are always synchronous. Error handling that looks thorough but doesn’t map to actual failure modes.

The common thread is that it looks like real code, which makes it hard to review at scale.

## How to fix the code review

The answer is not “review harder” or “add an LLM reviewer.” When the same model writes and reviews the code, it shares its own blind spots. If you add adversarial agents and multiple steps, the process becomes a theater of multi-step workflows that turns engineers into bot-sitters, spending time configuring and tuning filters instead of building.

What works is [shifting the burden off reviewers](https://www.aviator.co/verify?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness) in three places: codify repeated feedback, preserve the intent that produced the code, and measure the work that actually prevents slop.

### Create your AI slop registry

Pull your team’s last 100 PR review comments. Sort each one: Is it deterministic, something a rule can check? Is it execution-testable, something you can catch by running the code? Or is it genuine judgment?

When teams run this exercise, the rough split is 45% deterministic, 30% execution-testable, and 25% judgment. Three-quarters of review feedback is codifiable.

> “Three-quarters of review feedback is codifiable. Every recurring review comment is an invariant you haven’t written yet.”

Every recurring review comment is [an invariant](https://docs.aviator.co/verify/concepts/invariants) you haven’t written yet. “New endpoints must have OTel spans” is not a judgment call. It’s an AST check. Write it once. It never needs a reviewer again. The test for promoting something to an invariant is recurrence: if you’ve posted the same comment more than once, it should be codified.

### Preserve the reasoning trail

The prompts and agent sessions that produced your code hold the intent. Most teams throw them away. That’s like deleting the commit messages and PR descriptions and expecting reviewers to reconstruct intent from diffs alone.

At Aviator, we built [Verify](https://www.aviator.co/verify?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness) around this problem. It captures intent from prompts and agent sessions and structures it as [acceptance criteria:](https://thenewstack.io/ai-codebase-maturity-model/) what the change does, what’s out of scope, and how to tell if it worked. The decisions an engineer makes while talking to the agent, the architectural choices, the scope calls, the behavior tradeoffs, become reviewable acceptance criteria.

The reviewer reads [a list of acceptance criteria](https://docs.aviator.co/verify/concepts/how-verification-works?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness) and asks, “Are we solving the right problem with the right constraints?” That’s the high-value work for senior engineers. Not reading a 400-line diff at 4 p.m. Code is actually the [least important part of reviews](https://www.aviator.co/blog/move-code-review-before-the-code/). What matters is intent: acceptance criteria, non-goals, blast radius.

### How knowledge sharing survives

Reviewers reading specs and acceptance criteria are reading decisions, not scanning syntax. They’re debating tradeoffs, understanding how the system is evolving, seeing what constraints shaped the approach. That’s where knowledge sharing survives. If we move code review left, [knowledge sharing has to move left too](https://thenewstack.io/ai-code-review-cognitive-debt/).

### Measure and reward verification work

[31% more PRs](https://www.faros.ai/blog/ai-software-engineering) are being merged without any review at all. That’s engineers voting with their behavior.

Dashboards measuring AI adoption and productivity in lines of code will never show the work of senior engineers carrying the review burden. They will never surface the effort that goes into building the systems and guardrails that prevent slop. If you’re measuring throughput and cycle time and feeling good, you’re measuring the wrong thing.

Annie Vella has been [tracking this shift](https://annievella.com/posts/the-productivity-experience-paradox/) across 158 engineers in 28 countries. Her observation: engineers are resigning, some hoping the role will return to what it was, others leaving the profession entirely. The shift toward verification-heavy work is turning the job into something they don’t enjoy.

> “Those dashboards don’t show the senior engineer who spent her afternoon reverse-engineering intent. They show throughput. And throughput looks great right up until the people carrying the review burden walk out the door.”

The engineers who carry the review burden aren’t complaining. They’re quitting. Some leave for teams with better tooling. Some leave engineering entirely, not because they can’t keep up, but because the work stopped being the work they signed up for.

Leaders chasing lines of code generated and PRs merged will never see this coming. Those dashboards don’t show the senior engineer who spent her afternoon reverse-engineering intent from a 400-line diff. They don’t show the review that caught a cargo-cult pattern before it hit production. They show throughput. And throughput looks great right up until the people carrying the review burden walk out the door.

[Fix the code review process.](https://www.aviator.co/verify?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness) Codify what’s repetitive, preserve the reasoning trail, and measure the work that actually prevents slop. Otherwise, you watch your best engineers leave and wonder why your AI-powered team ships faster but breaks more.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d5d9b6e2-cropped-c9449920-ankit-jain-profile-photo-linkedin.jpeg)

Ankit Jain is a cofounder and CEO of Aviator, a developer productivity platform used by modern engineering teams to ship AI-generated code at scale. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)