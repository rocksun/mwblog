The argument over whether engineers should [stop reading code](https://thenewstack.io/future-of-code-reviews/) is over, because we already have.

Faros AI’s [new report](https://www.faros.ai/blog/ai-speed-trap-takeaways) shows a 76.3% increase in pull requests merged without review since their last report in April. Many companies now run AI reviews on 50% to 80% of their PRs. AI review took over bug-finding. But it didn’t take over the conversation where a team debates what it decided and why, and that is the part I missed too.

## The part AI review doesn’t solve

Most teams are stuck in one of two modes. They review every line and become [the bottleneck](https://thenewstack.io/ai-code-bottleneck-myth/), or they rubber-stamp and lose track of what changed and why. There is no middle ground yet.

> “The argument over whether engineers should stop reading code is over, because we already have.”

AI review is good at the mechanical half of the job. It never gets tired, it reads every line, and it holds the same standard on every PR. But it never saw what was decided. It won’t tell you not to build something, and it can’t be accountable for the result. A better model won’t fix that, because the tool reads the wrong artifact at the wrong time.

As I wrote in “[Kill the code review theater, keep the review](https://thenewstack.io/kill-code-review-theater/),” code review is how a team builds a mental model of its system. That has been the only scheduled moment for engineers to talk to each other about that system. Teams that hand code reviews to AI tools rarely notice they’ve also given up that moment.

I didn’t notice either. The [five layers of trust](https://www.latent.space/p/reviews-dead) I proposed in March for replacing code review all checked the code. Four asked, “Is it right?” One asked, “Is that what we meant?” None asked, “Are we building the right thing?”

## Debating decisions replaces reading the code

A decision is any point where the change could have gone another way: a token bucket or a sliding window, fail open or fail closed, one limit for every customer or one each. An AI-written PR is full of them, and almost none of them show up in the diff.

My [new framework for the review bottleneck](https://docs.aviator.co/verify/concepts/why-intent-driven-verification) also has five layers.

* **Challenge.** Before the PR exists, a second agent on a different model pushes back on the coding agent’s approach. The output records what was proposed, what was rejected and why, and which agent gave ground. Settled points stay on the record too, because two agents can also agree to look the other way.
* **Capture.** The intent (why we’re making the change) and the acceptance criteria (how it should behave) [get captured](https://docs.aviator.co/verify/how-it-works) from coding with the agent and go onto the PR. You need both: intent without criteria can’t be checked, and criteria without intent can’t be judged.
* **Codify.** Review comments your team keeps repeating, like “use the Money type, not float,” go into an [AI slop registry,](https://docs.aviator.co/verify/concepts/invariants) and become invariants, standing rules checked on every change.
* **Debate.** People discuss the decisions the agents surfaced and couldn’t settle, and leave the line-by-line checking to the machines. It’s the only layer that asks whether we’re building the right thing.
* **Own.** A model has no reputation and can’t be asked why, so a named team owns the invariants and the mental model behind them, and signs off on the change.

The first three are work for machines, and tools for them exist today. Debate and Own are work for people, and Debate is the layer that was missing.

> “The principle we designed around is simple: agents verify, people decide.”

The principle we designed around is simple: agents verify, people decide. People are better at judging whether a change is right, weighing trade-offs and risks, and owning the decision. Invariants are rules for agents. Decisions are judgment calls for people, and the calls that keep coming back become rules.

Debate also ends the argument over whether engineers should [read AI-generated code](https://www.aviator.co/blog/stop-reading-the-code/).

I recently [spoke to Robert ‘Uncle Bob’ Martin](https://www.aviator.co/podcast/uncle-bob-martin-ai-clean-code), the author of “Clean Code,” who recently said that he doesn’t read the code anymore. But he did say that humans should take responsibility for the systems, just above the code. Decisions sit at that level.

A reviewer who has debated the decisions doesn’t have to read code line by line to explain a change.

### Should we just review specs?

The obvious objection is that this just moves the reading somewhere else, and at some point that place was specs. My issue with reviewing specs is that it seems backward. A spec takes time to write, gets written before the work teaches you anything, and drifts the moment implementation starts.

Decisions come out of the work itself. They are generated live, they are short, and each one exists because the change could have gone another way. That is also why Capture pulls the intent and acceptance criteria out of the coding session after the work, instead of asking anyone to write them up front.

## How I see decision review working

Here is how I see it working, based on what we’ve been [building at Aviator](https://www.aviator.co/verify).

### Where decisions come from

Most decisions already happen on the author’s machine, and today we throw them away.

* **A capture skill** pulls intent, acceptance criteria, and decisions out of the coding agent session. Every time the agent stops to ask and the engineer makes a call, it records that call.
* **A review skill** runs an adversarial review agent that argues with the coding agent before the PR is submitted. It records what they disagreed about and how they settled it. What they couldn’t settle is what the team debates.

### What a decision looks like

This example uses a PR that adds a per-installation rate limit to webhook ingest.

![Screenshot of the Aviator decisions UI.](https://cdn.thenewstack.io/media/2026/10/39ad7164-image-1024x534.png)

The intent is one sentence: throttle webhook bursts per GitHub installation so one noisy customer can’t starve the broker, without dropping events or breaking their order.

The PR carries six decisions. The one still open is a product call, not a code one: the burst limit is one value for every customer. Two are accepted risks: a Redis outage fails open, and deferred events hold their payload in the broker. Exposing limiter metrics on the on-prem Grafana board became a follow-up with a linked ticket. The other two were argued out between the author, the reviewer, and the agents and settled.

Take one of the settled ones, “token bucket, not a sliding window.” The author’s agent explains it in the thread: one Lua call per event instead of a sorted-set scan, chosen after profiling a replay of a webhook storm. A reviewer who disagrees can push back in the same thread or ask the agent directly.

None of that is visible in the diff.

### What the reviewer does

The reviewer’s part comes down to three steps:

* Read the intent and what’s changing.
* Go through the decisions and argue where you disagree.
* Check what isn’t passing, then approve.

That is enough to understand the change, build a mental model, and argue about what matters, without reading line by line.

Each decision is its own thread, with humans and agents labeled separately, so you know who made which call. A reviewer can agree, challenge, override, or turn a decision into a tracked follow-up. The code is still there. You open it where a decision sends you, and comments on the code join the same record.

### What happens after the merge

The decisions outlive the review.

* **Your team’s week.** You see the key decisions made in your part of the codebase over the last day or week, without reading the PRs. That is what knowledge-sharing code review was always for.
* **Memory for agents.** Coding and review agents pull past decisions for the code they touch, so they don’t re-argue settled trade-offs.
* **Follow-ups that stick.** “Do it later” becomes a linked ticket, not a line in a PR description nobody reads again.
* **Rules from patterns.** When a decision keeps recurring, propose it as an invariant; it becomes a rule only after someone approves it.

Someone still has to sign. A model has no reputation and can’t be asked why, so every debated decision ends with a named person who agreed to it. That is where Debate hands off to the last layer, Own.

> “If AI already reviews most of your PRs, try one question on your team: what did we decide last week, and who agreed to it?”

If AI already reviews most of your PRs, try one question on your team: what did we decide last week, and who agreed to it?

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d5d9b6e2-cropped-c9449920-ankit-jain-profile-photo-linkedin.jpeg)

Ankit Jain is a cofounder and CEO of Aviator, a developer productivity platform used by modern engineering teams to ship AI-generated code at scale. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)