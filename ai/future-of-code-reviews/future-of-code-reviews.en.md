*Don’t kill the code reviews; just move the human checkpoint upstream to reviewing intent, specs, plans, constraints, and acceptance criteria. Code is actually the least important part of the reviews.*

Code review has become the bottleneck. AI generates [code faster than any human](https://thenewstack.io/the-new-bottleneck-ai-that-codes-faster-than-humans-can-review/) can read it, and asking another AI to do the reading doesn’t solve the underlying problem. The way out is to move the human checkpoint upstream, to the point where intent is defined, before any code is written.

## The review bottleneck

Code review as a quality gate was already showing cracks even before AI coding tools. [Microsoft research](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bosu2015useful.pdf) analyzed 1.5 million review comments across five major projects and found that as change size grows, the share of useful comments shrinks. Not fewer comments, less useful ones. We already stopped reading code for the most part.  
  
Then AI coding tools arrived and broke the model entirely. Teams with high AI adoption are now merging 98% more PRs, while [review times have climbed 91%](https://www.faros.ai/blog/ai-software-engineering).  
  
We’ve all experienced how unreliable [agents writing code](https://thenewstack.io/ai-agents-software-engineering/) can be, and no one wants to ship AI slop into production, so engineering teams keep telling themselves, “We caught AI doing dumb things once, so we must always check it.” They tell themselves that code review is the quality gate, but in reality, either PRs sit for days or engineers skim 500-line diffs and rubber-stamp approvals.

## AI code review is still a code review

There is no way we’re outreading the machines. And when humans can’t keep up, the instinct is to [use AI to review AI-generated code](https://www.aviator.co/blog/ai-code-review-is-still-a-review/). Teams are already doing this with Cursor rules files, AGENTS.md configurations, and dedicated AI review tools. A senior engineer codifies years of review standards into a rules file.

Engineers are creating their own AI-powered skill to review the code. Sometimes they also use famous personalities, asking AI to review code like [Linus Torvalds](https://thenewstack.io/torvalds-ai-programming-productivity/) or Kent Beck! The LLM reads incoming PRs against it. Developers skim the output and merge.

This approach inherits three failure modes that no amount of prompt tuning will solve.

The first is non-determinism: the same code can produce different reviews in multiple runs. That is not a quality gate.

The second is missing intent: the LLM reads a diff in isolation, pattern-matching against its training data without understanding what the code was supposed to do.

The third is duplicate blind spots: when the same model [writes the code](https://thenewstack.io/netlify-agent-experience-engineers/) and reviews the code, it misses the same things both times. You have not added a check. You have added a mirror.

> “When the same model writes the code and reviews the code, it misses the same things both times. You have not added a check. You have added a mirror.”

Teams that built these rules files did the right thing. They articulated what they cared about. The mistake was dropping those standards into a system that cannot reliably enforce them.

Three conditions have to be met for a team to get off the PR-review treadmill without losing quality. Each is a maturity step, and each needs to be in place before the next one delivers real value.

## 1: Codify code review feedback into deterministic checks

There are two types of code review comments: something about coding standards, organizational standards, or expectations; and behavior/judgment-based comments – how a particular logic should function.

The first one should be a guardrail that can be checked through AST. Behavior can also be verified through execution tests; however, we should still review this during the human checkpoint.

Most standards that teams enforce repeatedly; things like “every new endpoint must have tracing spans” or “error paths must emit metrics” or “auth failures must be logged with structured fields,” are either statically checkable through AST analysis or verifiable through execution tests.

A rule like “new endpoints must have OTel spans” becomes an AST check on route handler decorators. “Error paths emit metrics” becomes an execution test: hit the endpoint with bad input and assert that the counter increments.

When teams actually pull their last 100 PR review comments and sort them into three buckets (deterministic, execution-testable, genuine judgment), you might end with a split around 45/30/25. Three-quarters of review feedback may be codifiable. The work to codify it is real, but it is finite. Once a check is written, it never needs a reviewer again. This is where we can and should leverage AI and beat AI slop with AI.

## 2: Move the human checkpoint upstream

I’m not saying we should ‘dangerously skip reading code’ and stop reviewing AI-written code. The reviewer isn’t absent here; they’re more present than ever, just earlier.  
  
Instead of reviewing a 400-line diff after the code exists, the reviewer reads an 8-line on intentpec before it does: acceptance criteria, non-goals, blast radius. The reviewer’s job shifts from “Does this look right?” to “Are we solving the right problem with the right constraints?” which is closer to an RFC review than a line-by-line code review.

> “The reviewer’s job shifts from ‘Does this look right?’ to ‘Are we solving the right problem with the right constraints?'”

This is also where the knowledge-sharing function of review survives. When AI writes code, intent exists in a prompt that was never saved, a ticket that doesn’t capture the decision-making, or only in the engineer’s head. The implementation gets preserved. The reasoning behind it does not.

Reviewing specs in the intent-driven verification process changes that. Reviewers reading acceptance criteria are reading the decisions behind the implementation, not the implementation itself. The decisions that matter, the ones currently lost in prompt conversations with agents, become the reviewable artifact.

In practice, this does not require a formal methodology. A Jira ticket with a few sentences on scope, a short list of acceptance criteria, and a note on what is out of scope can serve as the spec. The format matters less than the discipline of defining intent before generating code.

![Summary slide of what code review used to be, and what it becomes](https://cdn.thenewstack.io/media/2026/06/4bde9091-image2-1024x576.png)

## Use LLMs where deterministic can’t reach

Some review feedback is genuine judgment: pattern recognition over context or questioning an architectural choice. This is where LLMs earn their place, not as the primary check but as a scoped fallback.

The wrong approach is one where an LLM reads a diff and produces free-form opinions. The right approach is a separate verifier agent with no shared context with the implementing agent, a scoped prompt, and structured output with file references and reasoning for each finding. Let the verifier agent capture evidence using a deterministic methodology (screenshots, API responses, server logs) to reduce the likelihood of hallucinations.

## Replace code reviews with verifying intent

This is the system we are building at Aviator. [Verify](https://www.aviator.co/verify?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness) accelerates code reviews with verified intent. Specs are written collaboratively with AI, reviewed and approved by humans, implemented with whatever coding tool the team prefers (Cursor, Copilot, Claude Code, or manual), then verified deterministically against each acceptance criterion.

Before submitting the change, your coding agent reviews the discussion and submits the intent and behavior details to Aviator. These get reviewed and approved by humans.

The difference from AI code review is fundamental. The same code always produces the same verification result. [The system checks against declared intent](https://docs.aviator.co/verify/concepts/how-verification-works?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness) rather than whatever the model notices on a given run. Verification becomes a matter of [checking the output against agreed-upon criteria](https://www.aviator.co/verify?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness), not of trying to reverse-engineer intent from the implementation.

![Workflow steps to change the shape of code reviews](https://cdn.thenewstack.io/media/2026/06/f4d062b8-image1-1024x576.png)

## How long would it take for your team?

Here’s the homework for you. Pull your team’s last 1,000 PR review comments; it should take no more than a couple of hours. Sort each one, asking, is this deterministic, is this execution-testable, or is this genuine judgment? The first two are your guardrail backlog, concrete, finite, and prioritizable. The third is what’s left for humans (and LLMs).  
  
From there, review the behavior, the intent, and the decision made while making the changes. These are the decisions the author makes while providing feedback to the agent in a terminal or IDE. Then review the evidence

Don’t kill the code reviews; “code” is actually the least important part of the reviews.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d5d9b6e2-cropped-c9449920-ankit-jain-profile-photo-linkedin.jpeg)

Ankit Jain is a cofounder and CEO of Aviator, a developer productivity platform used by modern engineering teams to ship AI-generated code at scale. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)