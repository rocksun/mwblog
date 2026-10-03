Six months ago I wrote about [how to kill the code review](https://www.latent.space/p/reviews-dead), and I was wrong. I still think line-by-line review is on its way out. I got the replacement wrong.

## What I proposed

The original essay proposed a “Swiss cheese“ model of AI code verification with five layers of trust laid out so that humans are not drowning in reading AI-generated diffs:

1. **Compare multiple options.** Several agents attempt the same change, and you rank the attempts by tests passed, diff size, and dependencies added.
2. **Deterministic guardrails.** Linters, types, and contracts. These are facts, not opinions, and an agent can’t argue with a type error.
3. **Human-defined acceptance criteria.** Someone writes down what “done” means before the code exists.
4. **Permission systems.** Scope what an agent may touch without a human.
5. **Adversarial verification.** A separate agent with no write access tries to break the implementation.

![Diagram showing code review verify layers](https://cdn.thenewstack.io/media/2026/09/66e6846b-image-1024x566.png)

Stack enough imperfect filters, and the holes stop lining up. Six months is a decade in AI time, though, and watching teams try to put this into practice showed me what the list was missing.

## Why we review code

Ask engineers why they review code, and most will say they do it to find bugs. In 2013, Alberto Bacchelli and Christian Bird [studied code review at Microsoft](https://ieeexplore.ieee.org/document/6606617/) and classified 570 review comments. 44% of developers ranked finding defects as their top reason for reviewing. Only 14% of the actual comments were about defects. Five years later, Caitlin Sadowski and her colleagues [looked at nine million reviewed changes](https://research.google/pubs/modern-code-review-a-case-study-at-google/) at Google and reached the same conclusion.

Code review is how a team builds a mental model of its system. It’s how knowledge moves around a team. Catching defects was always the smaller job.

> “We made writing cheap, and understanding stayed exactly as expensive as it has always been.”

Addy Osmani put the cost of this well in June: “We made writing cheap, and understanding stayed exactly as expensive as it has always been.” Understanding is what the review was protecting, and it’s the one cost that never came down.

## We already stopped reading

[Faros AI’s 2026 engineering report](https://www.faros.ai/research/ai-acceleration-whiplash), covering 22,000 developers across more than 4,000 teams, found incidents per PR up 242.7%, bugs per developer up 54%, and work restarts up 13.8%. PRs merged with no review at all, human or agentic, rose 31.3%. Nobody read those changes.

[DORA’s 2025 State of AI-assisted Software Development](https://dora.dev/research/2025/dora-report/) report describes the tension we’re living in. AI adoption raises delivery throughput and delivery instability at the same time. One person shows you a velocity chart; another shows you an incident chart, and both are right. Gergely [Orosz described](https://newsletter.pragmaticengineer.com/p/the-pulse-new-trend-concern-about) what this does to the engineers who are still trying:

Those devs who put the same effort and energy into code review as before feel [overloaded by AI slop](https://thenewstack.io/port-ai-builder-governance/) PRs sent their way.” That’s a team health problem as much as a quality problem.

Nobody held a meeting and voted to stop reviewing code. We just stopped. We were never that good at it either. A diff is a bad place for review. One reviewer reads it once, from memory, while context switching between five agents.

## The review theater

The obvious fix was to point AI at the diff. The agent writes, AI reviews, the agent revises, AI reviews again, and then a human skims and merges. The human is the only participant not doing the thing the loop is named after. I call that review theater.

AI code review has its place, though. It never gets tired or rushed. It reads every line, every time, and holds the same standard on every PR. It’s awake at 3 a.m. It also never saw what was decided. It was trained on the kind of code it’s reviewing. It will never tell you not to build the thing. And it can’t be held accountable.

> “Build tools for what AI does well, and protect what it can’t do.”

None of those are model quality problems. They’re all the same problem: AI review looks at the wrong artifact, at the wrong time, with no access to what was decided. A diff can’t tell you what was decided.

The principle I’d work from is simple. Build tools for what AI does well, and protect what it can’t do. We’ve been doing the exact opposite. We pointed the machine at judgment, the one thing it can’t do, and left the mechanics to people.

## The new shape of review

Looking at my five layers again, four of them answered one question: Is it right? One answered another: Is it what we meant? None of them asked whether we were building the right thing. I missed human judgment entirely, and I missed the conversation where that judgment happens.

The same concepts survive in a better order, with one addition. Each layer takes over one of the jobs code review used to do.

| Layer | Where it came from | The review job it takes over |
| --- | --- | --- |
| 1. Argue | Adversarial verification, moved to the front. Comparing multiple options folds into it | Alternative solutions |
| 2. Capture | Human-defined acceptance criteria, widened to include intent | Knowledge transfer |
| 3. Codify | Deterministic guardrails, built from an AI slop registry | Finding defects, consistency |
| 4. Debate | New. The layer that wasn’t there | Are we building the right thing? |
| 5. Own | Permission systems | Gatekeeping |

## Argue: let the agents disagree before the PR exists

Why is there a UI for two machines talking to each other? If one AI writes the code and another reviews it, a PR comment thread is a strange place for them to meet. Let them argue before the PR is created, when changing course is cheapest.

The output of this layer is a record of decisions, with no verdict attached: what was proposed, what was rejected, and why. A human facing a 4,000-line diff has very little to hold onto. A human reading what two models disagreed about has exactly what a diff never contained, and that’s where judgment belongs. Whatever the agents couldn’t settle is what the team debates.

You can do this today. Run two reviewers on different models, write a skill that captures where they disagree, and review that record as part of the PR.

Open-source tools already cover most of it:

* [PR-Agent](https://github.com/The-PR-Agent/pr-agent) (MIT) runs reviews on GPT, Claude, Gemini, DeepSeek or a local model through Ollama.
* [Aider’s architect mode](https://aider.chat/docs/usage/modes.html) (Apache 2.0) has one model propose and a different one edit, before the PR exists.
* [AutoGen](https://github.com/microsoft/autogen) (MIT) handles multi-agent conversation and group orchestration.
* [CrewAI](https://github.com/crewAIInc/crewAI) (MIT) gives you role-based agents if you want to define the arguing sides yourself.

## Capture: record intent and acceptance criteria as you work

The popular answer to agent-written code is to write the spec up front. Specs take time. They have no feedback loop, because they’re written before the work has taught anyone anything. The implementation drifts away from them almost immediately. We discarded that model 20 years ago and called it waterfall.

Two artifacts do the job a spec was trying to do. **Intent** answers why we’re making this change. **Acceptance criteria** answer how it should behave. You need both, since intent without criteria can’t be checked and criteria without intent can’t be judged. The pair works for a one-line bug fix and for a 1,000-line feature.

They already exist in your coding sessions. Every time the agent stops to ask a question, and every time an engineer pushes back or corrects it, someone makes a decision. Those are your acceptance criteria, generated live.

Don’t throw them away when the session ends. Write an agent skill that writes decisions down as they’re made and publishes them on the pull request, so the reviewer reads what you decided. Nobody has to change how they work, which is why it sticks.

Review comments come in two kinds. “Have you considered doing this differently?” needs human judgment. “Use the Money type, not float” doesn’t.

The second kind belongs in an [AI slop registry,](https://docs.aviator.co/verify/concepts/invariants) the running list of patterns your team keeps correcting. Once written down, those patterns become [invariants](https://docs.aviator.co/verify/concepts/invariants) checked on every change.

Most teams already have them, scattered across PR comments, repeated endlessly and stored in engineers’ memory:

* Money type for anything with a currency
* No direct writes to the users table
* Structured logger only, no print
* Every error path emits a counter

Every review comment your team repeats is a guardrail you haven’t written.

This is the cheapest layer and the one to start with this week. Harvest your last 1,000 review comments and turn the top 20 into invariants. Your PR history already contains the registry.

## Debate: humans on the decisions

None of my original five layers covered this one. It’s also the part [that worries me most](https://www.aviator.co/blog/ai-code-review-knowledge-sharing/).

Code review is the only scheduled moment when engineers talk about the system. Automating review costs you surprisingly little in bug-catching. It costs you that conversation, and nothing replaces it because nobody noticed it was a meeting. Automate code review carelessly and you delete shared understanding.

> “Automating review costs you surprisingly little in bug-catching. It costs you that conversation. Knowledge sharing was the product of code reviews all along.”

Peter Naur, the Turing Award winner, wrote about this in 1985 in “Programming as Theory Building”: “The death of a program happens when the programmer team possessing its theory is dissolved.” In today’s terms, that’s your reorg, attrition, and backfill. And if nobody built the understanding in the first place, you get there without a single resignation. [Knowledge sharing](https://thenewstack.io/ai-code-review-cognitive-debt/) was the product of code reviews all along.

The Debate layer keeps the same PR and the same tool and changes what the conversation is about. The team discusses the decisions the agents surfaced and couldn’t settle, and leaves the diff to the machines. This is the biggest behavioral change of the five, so start small.

## Own: decide who signs

A model has no reputation. It has no liability. It can’t be asked why.

Responsibility has already moved twice. It used to sit with the author, who wrote the code and owned it. Then it moved to the reviewer, who read it and approved it. Now it sits with the team that writes the invariants that verify the change.

That changes what ownership means. Our job becomes owning the [invariants](https://docs.aviator.co/verify/concepts/invariants) that govern the code and maintaining the mental model behind them, and line-by-line review drops out of it. Define who owns those invariants and what ownership now means, and name it before an incident names it for you.

## Kill the theater

My first essay told you to [kill the code review](https://thenewstack.io/killing-the-code-review/). Please don’t. [Kill the line-by-line review theater.](https://www.aviator.co/verify?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness)

AI is good at finding bugs. Humans are good at judgment. Tools and culture have to move together: tooling that pushes decisions onto the same PR, guardrails strong enough to earn trust, and a conversation with your team about what review is for now.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d5d9b6e2-cropped-c9449920-ankit-jain-profile-photo-linkedin.jpeg)

Ankit Jain is a cofounder and CEO of Aviator, a developer productivity platform used by modern engineering teams to ship AI-generated code at scale. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)