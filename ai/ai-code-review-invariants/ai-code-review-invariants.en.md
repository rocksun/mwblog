**Agents verify; people decide.** Most teams running AI code review today have it the other way around. They point a model at the diff, ask it whether the change is good, and leave a human to skim the result and click approve.

The model reads every line, never gets tired, and holds the same standard on every PR. What it doesn’t have is your codebase’s standards. It doesn’t know them, and no matter how well you instruct it, it doesn’t always follow the ones you write down.

> “Judgment needs intent, and accountability needs a person.”

It never saw what was decided, has no context for previous decisions, can’t tell you not to build the thing, and can’t be held accountable. A diff can’t give it any of that. Judgment needs intent, and accountability needs a person.

So what does a [code review look like](https://docs.aviator.co/verify/concepts/why-intent-driven-verification) when verification goes to agents and judgment stays with people? At Aviator, we’ve been building that review into [Aviator Verify](https://www.aviator.co/verify?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness). Below are its seven parts, in order.

## The anatomy of an intent-driven review

![](https://cdn.thenewstack.io/media/2026/10/3a16e809-image-1024x857.png)





*Click to enlarge image.*

Every change gets [checked against two layers](https://docs.aviator.co/verify/concepts/verification-layers). Acceptance criteria describe what this change should do. [Invariants](https://docs.aviator.co/verify/concepts/invariants) are the codified rules of your engineering org or team: the standards that are always true, whatever the change.

Criteria without invariants leave your standards to memory. Every engineer has to remember every standard, or someone has to catch the obvious agent mistakes in code review. Invariants without criteria give you code that follows the rules but doesn’t consider what the result should be, so the agent strays, overengineers, or solves the wrong problem.

The seven parts build both layers, verify the change against them, and hand the decision to a person:

1. **Invariants** (defined before any change): the team’s standing rules, drawn from its own code reviews.
2. **Intent and acceptance criteria** (captured from the coding session): why the change exists and how it should behave.
3. **Core decisions** (captured from the coding session): the choices made along the way, and who made them.
4. **A test plan** (built at submit): the criteria plus the invariants that apply, turned into scenarios.
5. **Evidence** (gathered at submit): proof from a running environment behind every verdict.
6. **A review** (decided by a person): intent, decisions, and evidence, approved or pushed back on. Not code.
7. **Invariants refreshed** (updated after merge): waivers and recurring comments that sharpen the invariants.

## 1. Invariants

Every review checks a change against something. In most teams, that something lives in senior engineers’ heads and comes out as review comments. Use the Money type for anything with a currency. No direct writes to the users table. Every error path emits a counter. Each of those has been typed more than once, and coding agents keep making the same mistakes because the rule was never written down anywhere an agent or a verifier could use it.

An invariant is that rule, written once and checked on every matching change. Together, your invariants become an [AI slop registry](https://www.aviator.co/blog/how-an-anti-slop-registry-stops-ai-generated-code-from-violating-your-engineering-standards/), the running list of patterns your team keeps correcting.

Agent instruction files like CLAUDE.md help, but they’re an input to generation. The same non-deterministic agent that wrote the code is asked to follow them, and nothing proves it did. Invariants sit on the verification side, checked by a deterministic script or at least a different agent that returns a verdict for each rule.

Your PR history already holds most of them. Verify reads the comments your team posts in GitHub and drafts invariants from the patterns it finds. It also drafts them from CONTRIBUTING.md and agent instruction files or on the spot when someone tags `@aviator` invariant in a PR comment or a Slack thread. Generate your team’s invariants with the [Aviator Verify free account](https://www.aviator.co/code-review?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness) and keep them even if you decide not to continue with Verify.

Three things determine whether an invariant helps or becomes noise.

* **Ownership.** Every draft goes to the team it belongs to, with the reason it was proposed, and goes live only once that team approves it. Nothing AI-drafted becomes a standing check without a human saying yes.
* **Wording.** Assert the outcome and leave the implementation open, so the rule survives renames and file moves.
* **Scope.** A rule should only run where it can break. A frontend invariant has no business checking database migrations.

## 2. Intent and acceptance criteria

The obvious way to give a reviewer intent is to write a spec up front or capture as a detailed JIRA ticket. Specs take time, get written before the work teaches anyone anything, and drift the moment implementation starts.

The most accurate intent already exists in the coding session. Every time the agent stops to ask a question and the engineer makes a call, acceptance criteria get defined in real time. There is no reason to throw all of that away when the session ends!

The intent says why the change was made. The acceptance criteria say how it should behave.

Verify captures both from the session the engineer already had. An agent skill and a hook run *verify submit* before the agent opens a pull request. The agent extracts the intent and the criteria from everything it saw in the session, and the engineer reviews and corrects them before anything is submitted.

![](https://cdn.thenewstack.io/media/2026/10/ce3429e5-acceptance-criteria-invariants-1024x562.png)





*Click to enlarge image.*

## 3. Core decisions

A decision is any point where the change could have gone another way. Where state lives, what happens when a dependency fails, whether to reuse an existing helper or write a new one. An AI-written PR is full of calls like these, and almost none of them show up in the diff.

> “An AI-written PR is full of calls like these, and almost none of them show up in the diff.”

Verify records the decisions next to the intent, with humans and agents labeled separately, so the reviewer knows who made which call and can argue with it. I wrote more about why decisions are the thing people should review in [How to review AI code without reading the code](https://thenewstack.io/review-decisions-not-code/).

## 4. A test plan

When a change is submitted, Verify reads the intent and the criteria and uses the diff to identify the invariants to apply. Both layers merge into one list of scenarios: the steps an agent takes to validate behavior, derived from the requirements rather than the code.  
  
That’s where the two layers pay off. The engineer stays focused on the change, and the registry covers the standards.

## 5. Evidence

When the same model writes and reviews the code, they share the same blind spots. Verification must be structurally separate from generation, and it must produce more than an opinion.

> “When the same model writes and reviews the code, they share the same blind spots.”

Verify spins up a preview environment and dispatches verifier agents to run the scenarios. They capture screenshots, database state, server logs, and console logs, and every verdict, for a criterion or an invariant, points at that evidence. For a UI change, the verifier actually clicks through the interface and confirms the result.

You don’t need a preview on day one. Code scans handle structural checks straight from the diff, with no infrastructure, and many invariants are converted to deterministic scripts. A preview earns its place once your criteria start asking about behavior the diff can’t show.

## 6. A review

This is where people come back in, and the work looks different. As a reviewer, you’re looking at evidence rather than reading code line by line. You read the intent, look at the hot spots where the core changes are, go through the decisions and the verdict on each criterion and invariant, and open the live preview if you want to see the change for yourself.

![](https://cdn.thenewstack.io/media/2026/10/7f022afb-verify.review-1024x552.png)





*Click to enlarge image.*

The pull request workflow barely changes. Verify adds a link to the review, the diff stays where it was, and the results are reported as a status check similar to the CI behavior.

The reviewer answers one question: does the evidence match what the team agreed to build? They approve, push back on a decision, ask for another scenario, or waive a failed invariant with a reason. That’s judgment, and someone owns it.

## 7. Invariants refreshed

Most reviews end at merge, and everything they learned leaves with them. The next PR makes the same mistake, and the same comment shows up again.

Invariants keep what each review learned. When an invariant fails on a PR, the author can waive it with a reason: maybe it doesn’t apply, maybe the invariant is incorrect, or maybe it gets fixed separately. The team that owns the Invariants sees every waiver.

![](https://cdn.thenewstack.io/media/2026/10/a8791394-invariants_waivehistory-1024x563.png)





*Click to enlarge image.*

Insights show which invariants apply most, how often each one fails, and why people waive them. An invariant that keeps getting waived is wrong, so the team rewrites or narrows it. A comment reviewers keep typing becomes the next draft. That way invariants become a set of rules that are continuously maintained over time and guard every code change.

## Where to start

Don’t switch it all on at once. Start with the invariants, because they’re the cheapest part and your PR history already holds them. Month one will feel like double work, with the team still reviewing code while the registry fills up. In month two, invariants catch enough that reviews shrink. By month three, reviewers read intent, decisions, and evidence, and open the diff only when something doesn’t add up.

The review your team already does is full of rules waiting to be written down. [Aviator Verify](https://docs.aviator.co/verify) turns them into invariants, verifies every change against them, and leaves the decisions to people.  
  
***Generate your team’s invariants with the [Aviator Verify free account](https://www.aviator.co/code-review?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness) and keep them even if you decide not to continue with Verify.***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d5d9b6e2-cropped-c9449920-ankit-jain-profile-photo-linkedin.jpeg)

Ankit Jain is a cofounder and CEO of Aviator, a developer productivity platform used by modern engineering teams to ship AI-generated code at scale. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)