Code review is becoming the most important decision-making surface in software engineering, and it’s outgrowing the diff. The assumption was always that code review exists to catch bugs. Its real job is taste, judgment, and applying organizational processes: Is this the right thing for our product?

Now that AI writes thousands of lines of code in minutes, and there’s no way engineers can keep up with the review, engineering teams are stuck between two bad options: skip code review and risk shipping slop, or keep reviewing everything and become the bottleneck. That’s why conversations about reviewing AI code keep going in circles – everyone is arguing about a different part of code review.

## The three jobs that remain

Strip away line-by-line inspection, and code review still does three things that teams need.

First, it’s a place to collaborate. This is where teams come together to decide what belongs in the product.

The second role of code review is alignment and knowledge sharing. Every review builds shared context about the [changes happening to a code base](https://thenewstack.io/root-out-vulnerabilities-in-github-as-you-merge-code-changes/) and the underlying business needs. This context is increasingly important for both people and agents and carries the institutional knowledge and historical considerations for the product and organization.

Its third function is verification: Is the code correct? Will it work? What’s the risk?

> “Code is the medium, but the review is where we exercise judgment, and it’s still important.”

These three jobs don’t go away when AI [generates the code](https://thenewstack.io/the-ai-code-generation-problem-nobodys-talking-about/). If anything, they become more important because the volume of code demanding review is growing faster than the number of people available to review it. Code review was never strictly about reviewing code. Is this even the right name for it? Code is the medium, but the review is where we exercise judgment, and it’s still important.

## Planning and review are merging

Code review is where engineering teams conclude that they’re confident this is the right thing for their product.

As it becomes [cheaper to write and rewrite code](https://thenewstack.io/cursor-composer-benchmarks/), a lot of the things teams used to front-load, such as PRDs or architecture documents, are collapsing into the same space as code review. Teams used to do all of that in advance because writing code was expensive, making it important to catch issues earlier in the pipeline. But now they can collaborate on the genuine artifact and shape it until, as a team, they can decide this is what they want. There may be a world where there are 20 times as many PRs that don’t get merged. And maybe that’s how people build software in the future: by trying things, accepting some, rejecting others. Or, teams move the code review process left, before any code is written, by [capturing intent](https://www.aviator.co/verify) and the decision-making process from the LLM session where they happen. The decisions the engineer made while talking to the agent are already there. The discipline is in preserving them before submitting the change rather than letting them disappear.

The reviewer’s job shifts accordingly. Instead of reading a 600-line diff and asking, “Does this look right?”, they read eight lines of intent and ask whether we are solving the right problem with the right [constraints](https://docs.aviator.co/verify/concepts/invariants). That is a better use of a senior engineer’s time, and it is where the knowledge-sharing function of review survives—reviewers reading acceptance criteria are reading the decisions behind the implementation, not the implementation itself.

> “Instead of reading a 600-line diff and asking, ‘Does this look right?’, they read eight lines of intent and ask whether we are solving the right problem with the right constraints.”

That collapse puts more pressure on the code review, but it’s fundamentally the same kind of decision-making. Code review is becoming the place where product decisions get made, not just where code gets checked. Not reading code is a sliding scale

The future of code review is also the center of the debate over whether engineers should still read every line of code, but the framing is wrong.  It’s not “Do I read or not read the code?” It’s  “Does my attention get directed to where it’s actually useful?”

The question is whether reviewers can be pointed at the parts that are meaningful for them to apply their judgment and expertise, while the things that can be removed from their attention set with high confidence fall away over time.

Different organizations will find themselves at different places on that scale. It depends on the sensitivity of what you’re building, the consequences of the change, and what happens if something goes wrong. A team shipping an internal dashboard and a team shipping medical device firmware will make different choices, and both can be right.

## AI code needs AI slop register

The standards and correctness checking role of code review is the most likely candidate for AI automation, but not in the most obvious way. Pointing an LLM at a diff with a checklist does not create a quality gate. One of the most underexplored opportunities is closing the loop between review decisions and automated enforcement. Today, a senior engineer catches an API design anti-pattern in review and leaves a comment. Tomorrow, that same anti-pattern shows up in a different PR, and someone has to catch it again. This is where we can and should leverage AI and beat AI slop with AI.

> “This is where we can and should leverage AI and beat AI slop with AI.”

When teams actually pull their last 1000 PR review comments and sort them into three buckets (deterministic, execution-testable, genuine judgment), you might end with a split around 45/30/25. Three-quarters of review feedback may be codifiable. The work to codify it is real, but it is finite. Extract those decisions back into rules that become part of the institutional memory of the code base, your AI slop register. An LLM can check, at the time code gets built, with rigor that would have been extraordinarily difficult for humans to maintain—keeping an entire set of rules in your head and applying them to every API was never realistic at scale.

The tighter that loop and the closer it runs to where engineers are already iterating and collaborating, the more effective it gets.

## Stop calling it code review

Code review may not be the right name anymore, but the practice it represents isn’t going anywhere. The code is one of many artifacts we’ll use to assess a change and may become less central as a result. Engineering teams still need a place to collaborate, share knowledge, and apply judgment about what they’re building. That place is evolving, away from the diff, toward intent, toward institutional memory.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d5d9b6e2-cropped-c9449920-ankit-jain-profile-photo-linkedin.jpeg)

Ankit Jain is a cofounder and CEO of Aviator, a developer productivity platform used by modern engineering teams to ship AI-generated code at scale. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)

[![](https://thenewstack.io/wp-content/uploads/2026/08/66e4522a-david-poll-600x600.jpg)

David Poll is an engineering leader who has spent nearly two decades building the platforms and tools that developers use every day. He currently leads the GitHub Code & Review organization, working to make collaboration on building with code tractable...

Read more from David Poll](https://thenewstack.io/author/david-poll/)