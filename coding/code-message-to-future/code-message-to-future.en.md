Engineers communicate constantly. Slack messages, design docs, RFC threads, code review comments: the job is as much about sharing intent with other people as it is about solving technical problems.

But there’s one communication channel that doesn’t always get treated that way: the code itself. And everything that surrounds it must be part of that same channel.

Code is not only a set of instructions for a machine. It’s a message to the next engineer who has to read, extend, or debug it. It’s a message to your teammates in review. It’s a message to yourself six months from now, when all the original context is gone. A commit message is a Slack message that has to stand on its own. No thread. No way to ask a follow-up question. Often read years after it was written.

> “[Code] is a message to yourself six months from now, when all the original context is gone.”

Once you treat *code as communication*, the questions you should ask yourself change. Is this commit understandable on its own? Can someone review this PR in order? Does this comment explain why the code exists, or does it just repeat what the code already says?

Your local workflow is your own business. Experiment, rewrite, throw things away. The mess is part of how good ideas are found. But once something is ready to merge, the rules change. At that point, what you’re producing isn’t just a diff. It becomes part of the codebase. Someone will use it later to understand why a file changed, when a bug was introduced, or what problem the PR was trying to solve. That’s the moment to slow down and ask: does this tell a story that someone else can follow?

## A PR is a story

One mental model that helps here is thinking of a pull request as a book. Each commit is a chapter. The diff inside each commit is the prose. Nobody reads a book by jumping to random pages. You read it in order, and the story makes sense because the author was intentional about its sequence. A reviewer who reads your commits in order should be able to follow the reasoning without guessing, without needing to hold the whole diff in their head at once to understand any single part of it.

> “Nobody reads a book by jumping to random pages. You read it in order, and the story makes sense because the author was intentional.”

Here’s what that looks like in practice:

```

Add search endpoint to API
Add basic relevance ranking
Extract ranking logic into standalone module
Add unit tests for ranking
Add integration tests for search endpoint

```

Read those five commits in order, and you already know what happened. The feature was built incrementally, the ranking logic was pulled into its own module, and the behavior was covered at both unit and integration level. No PR description needed to reconstruct that. The commits tell it themselves.

For this to work, each commit needs to carry its own weight. A rename plus a behavior change is not one thing. Those are two separate changes, and they should usually be two separate commits. The titles of those chapters matter just as much as the chapters themselves. Commit messages need to carry context on their own. `Fix ABC-123` only points to context somewhere else, and [that context](https://thenewstack.io/context-is-ai-codings-real-bottleneck-in-2026/) may not be available when someone needs it.

Short, verb-first messages do it better:

* Extract validator
* Refactor: use validator in form
* Fix: [handle edge case](https://thenewstack.io/handling-edge-cases-and-exceptions-in-python/) on submit

Read them in sequence, and you already know the story.

Once review starts, avoid rewriting the commits while the conversation is active. Add new ones instead. Reviewers anchor their comments to specific lines. If you force-push and rewrite history, those anchors break, and the conversation becomes impossible to follow. The original story stays, the feedback gets addressed on top of it, and anyone reading later can see exactly how the PR evolved.

## The reader on the other side

When code is written with communication in mind, something shifts for the reviewer. Instead of trying to reconstruct intent from a set of changes, they’re following a narrative. This adds work for the author but reduces friction for everyone else, especially reviewers who haven’t been part of the exploration process. In a team setting, that tradeoff is worth it. A clear PR is easier to review. Over time, that matters. Less time spent reconstructing intent means more time spent looking at the actual change.

The reviewer is not the only reader. Someone may come back to the code years later and wonder why a line exists. A good commit history gives them a path back to the context: the commit that introduced it, the PR around it, and the tradeoffs behind it. Without that trail, it is easy to “fix” something that was intentional.

> “The code already shows what is happening. What it often can’t show is why it exists, what constraint it’s working around.”

The same instinct shows up in code comments. The code already shows what is happening. What it often can’t show is why it exists, what constraint it’s working around, what assumption it’s encoding. A comment that says `// increments the counter` adds nothing. A comment that says `// must run before the subscription is set up, or the callback fires before state is ready` is load-bearing documentation. The kind of thing that saves hours of debugging and probably prevents a bug from being introduced in the first place.

## AI-generated code makes this more important, not less

AI agents can produce a lot of code quickly, but speed does not replace context. [The cleanup cost lands further from the velocity wins than most teams expect.](https://webflow.com/blog/cleanup-cost-ai-generated-code) Left on their own, the result will be one giant commit with a message like “implement feature” and no trace of the reasoning behind any of it.

Asking an AI agent to follow the same conventions as a human engineer changes that. Atomic commits make the agent’s reasoning legible: you can see what it built first, where it [refactored the code](https://thenewstack.io/whats-missing-with-ai-generated-code-refactoring/), what it tested, and the order in which it did so. That’s not just useful for understanding the code. It’s how you catch gaps in the agent’s thinking before they make it into production. A commit that skips straight from “add endpoint” to “add integration tests” with nothing in between is a signal. A clean commit history is auditable in a way that a single dumped diff never is.

The code is still a message. It’s just that now, the author might not be human.

## Structure is part of the message

If you’ve been reading carefully, you may have noticed that each header in this article told you exactly what was inside before you read it. You didn’t need to read the whole thing to know where you were. That’s what good commit messages do. That’s what a well-structured PR does. The structure itself is the communication, and when it’s done right, the reader never has to guess.

This article was o*riginally published on June 11, 2026, on* [*webflow.com*](https://webflow.com/blog/code-as-communication)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/06/ca3c9cae-hernan.jpg)

Hernan Garchtrom is a Senior Software Engineer at Webflow, where he works on the Structure team building the foundations of the Designer and Editor platform. He specializes in frontend architecture and the complex interaction patterns that power Webflow's visual development...

Read more from Hernan Garchtrom](https://thenewstack.io/author/hernan-garchtrom/)