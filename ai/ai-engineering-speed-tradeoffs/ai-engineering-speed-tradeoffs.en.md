I use AI every day, and I would not want to go back.

That is probably the simplest way to start. AI has made me faster, helped me learn faster, and made entire areas of engineering feel more approachable than they used to. It has changed how I start work, how I find context, how I write code, how I test, and how I move through parts of the stack that once felt unfamiliar.

At Webflow, we have been thinking a lot about where AI fits in the engineering workflow. Not just as a code generator, and not as a shortcut around judgment, but as a way to help people move through real product work with more context and less friction.

That distinction matters to me because the most useful AI workflows are rarely just about writing code faster. They are about connecting the assistant to the right context, systems, and constraints so the work starts closer to reality.

But AI has not made engineering magically easy.

The annoying work did not disappear. In some cases, it just changed outfits and came back with a better résumé.

For me, the biggest shift is this:

AI made starting and executing work much faster.

The slower part is everything that happens after: reviewing the output, understanding the assumptions, keeping PRs small enough to review, merging things in the right order, and making sure I can still explain the code two weeks later.

That is where the real tradeoff lives.

## Before the first draft

Before AI became part of my daily workflow, much of my [engineering involved context](https://thenewstack.io/context-engineering-going-beyond-prompt-engineering-and-rag/) hunting.

A normal day started in familiar places. Slack. Jira. Assigned tasks. Confluence. Internal documentation. Tool documentation. Framework documentation. Then, depending on how quickly things went sideways, Google, Stack Overflow, Reddit, GitHub Issues, and eventually a teammate who might have seen the same thing before.

Sometimes that became pair programming. Sometimes it became a debugging session. Sometimes it became two hours of trying different things and later describing the process as “investigation,” which is technically true and emotionally generous.

That was especially true earlier in my career, when I was mostly focused on frontend engineering. Moving from frontend into backend, databases, and full-stack work took real time. I had to learn new systems, new frameworks, new failure modes, and new kinds of context.

React changed. Tooling changed. Libraries changed. NPM packages failed to install for reasons that felt personal.

A lot of the work was not just writing code. It was getting enough context to [write the right code](https://thenewstack.io/netlify-agent-experience-engineers/).

And sometimes the slowest part of the task was everything that happened before the first real line of code.

## The speed of starting

AI changed that first step dramatically.

Today, with MCP and connected tools, I can get relevant context much faster. Instead of manually jumping between Slack, Confluence, Jira, internal docs, web documentation, and the codebase, I can ask AI to help gather and synthesize that information.

This is also why MCP is interesting [beyond the “AI writes code” use case](https://thenewstack.io/vibe-coding-spec-driven/). MCP gives assistants a more structured way to work with the tools and systems where real work already happens. For example, [Webflow’s developer platform supports MCP](https://developers.webflow.com/#mcp), so agents can work with Webflow workflows using tools like Claude, Cursor, Postman, and other MCP-compatible clients.

That is a much more useful version of AI to me than a blank chat box. It is not just an outside observer guessing. It is an assistant that can operate closer to the actual workflow, with clearer context and more relevant actions.

If I am starting a new feature, I can ask for the context around the ticket, related conversations, similar implementations, relevant files, prior decisions, and the constraints I should know about before touching the code.

That does not remove the need to think.

It removes much of the manual searching before thinking can begin.

That difference matters. There is a lot of invisible time in engineering that is not exactly coding, but also not exactly planning. It is the time spent trying to understand what already happened, what someone meant in a ticket, why a system works a certain way, or whether the thing you are about to build already exists under a different name.

AI is very good at reducing that friction.

> “I still need to check the map. But at least I am not starting in the wilderness with a Jira ticket and a dream.”

It can summarize long threads. It can explain unfamiliar code paths. It can compare approaches. It can help turn scattered context into a first usable map.

I still need to check the map. But at least I am not starting in the wilderness with a Jira ticket and a dream.

## When execution gets easier

The next major shift is execution.

AI made it much easier to go from “I have no idea where to start” to “I have a working first draft.”

That first draft might be a feature implementation, a test, a database query, a script, a migration, a Splunk dashboard, or an AWS-related change. It might be frontend, backend, infrastructure, observability, or some awkward combination of all of them, because software has a sense of humor.

This has changed the kind of work I can take on.

Full-stack work feels more approachable. Infrastructure work feels less intimidating. Migrations feel easier to reason about. Dashboards, queries, and unfamiliar systems no longer feel like walls I need to climb before I can make progress.

AI does not magically give you expertise. But it can shorten the distance between being blocked and being useful.

That has been especially valuable for me as someone who started in frontend and grew into broader full-stack work. Before, moving into a new area often meant spending a long time just learning the vocabulary of the problem. Now I can ask better questions earlier. I can get examples faster. I can generate a first version, inspect it, challenge it, and learn from it.

The learning curve is still there.

AI just makes it less lonely.

Testing is a good example. I do not want this article to become a love letter to testing, because that would be suspicious behavior. But AI has made tests faster to write and easier to debug. It can generate mocks, suggest cases I might not have considered, update existing tests, and help reason through failures.

I still need to make sure the tests are meaningful. A passing test suite is only useful if it is testing the right behavior. But AI has made the mechanics faster, which gives me more room to think about coverage instead of fighting the shape of a mock object for half an afternoon.

A small victory, but a real one.

## After the first draft

The problem is that software engineering does not end at the first draft.

That is usually where the interesting problems begin, quietly waiting behind a passing test suite and a very confident assistant.

This is where AI starts to slow me down.

A generated solution can look correct. It can compile. It can pass tests. It can even be cleanly written. But that does not automatically mean it is the right solution for the codebase, the product, or the team.

The model may make assumptions. It may miss a constraint. It may choose a pattern that looks reasonable in isolation but does not match how the system actually works. It may solve a larger problem than the one I had. It may introduce an abstraction that feels elegant today and unnecessary by Thursday.

Before AI, much of my time went into creating the first version: searching, reading, asking, trying, debugging, rewriting.

Now, AI can dramatically compress that first version.

But then I need to verify it.

I need to read the generated code like I would review someone else’s work. I need to understand why it made certain choices. I need to check the edge cases. I need to make sure the tests are not just passing, but useful. I need to confirm the implementation fits the existing architecture. I need to remove unnecessary changes.

I need to ask whether this is the smallest reasonable solution, or whether the assistant tried to remodel the kitchen because I asked it to change a lightbulb.

That review work matters.

If I skip it, AI does not save me time. It creates future work with better formatting.

## The new bottleneck

AI moves time from creation to verification.

That can be a good tradeoff. In many cases, it is. I would rather spend more time evaluating a solution than staring at a blank page or searching through six tabs trying to remember which GitHub issue matched my error message.

But verification is still work.

It requires judgment, context, and discipline. It requires knowing what good looks like. It requires understanding the system well enough to decide whether the generated solution belongs there.

> “AI moves time from creation to verification. The fastest code to generate is not always the fastest code to own.”

The fastest code to generate is not always the fastest code to own.

That has become one of the most important lessons for me. If I cannot explain the code, I do not really own it. If I cannot defend the tradeoff, I should not ship it. If I cannot debug it later, then AI did not save me time. It borrowed time from the future, and future me is rarely impressed by that arrangement.

This is the part of AI-assisted engineering that feels less glamorous than the demos.

The demo ends when the code appears.

The work continues when someone has to maintain it.

## Starting too much

There is another bottleneck I did not expect: work in progress.

AI makes it easier to start work. Much easier. I can explore an idea, generate a first implementation, create tests, and open a PR faster than before.

That is powerful.

But starting work is not the same as finishing work.

When creating work gets cheaper, it becomes easier to create too much of it. Suddenly, there are more branches, more PRs, more review requests, and more changes that depend on other changes. Some PRs need to land in a specific order. Some need context that lives in another branch. Some are small enough on their own, but together they create a queue that the team still has to review, understand, and merge.

The bottleneck moves from “Can I build this?” to “Can we safely absorb this?”

> “The bottleneck moves from ‘Can I build this?’ to ‘Can we safely absorb this?'”

AI can speed up individual execution, but software still ships through teams.

That means coordination still matters. Review still matters. Sequencing still matters. Keeping PRs small still matters. In fact, it may matter more now because the cost of generating too much work has gone down.

This is one of the stranger effects of AI. It can make me feel more productive while also creating more unfinished work around me.

More motion is not always more progress.

Sometimes progress is smaller PRs, clearer sequencing, fewer parallel branches, and enough discipline to finish the thing I already started before asking AI to help me start three more.

## What has actually changed

AI saves me time by helping me find context, synthesize information, scaffold a solution, or execute the first version of the work.

That is also the version of AI that feels most aligned with what we are building toward at Webflow: AI connected to real workflows, real product surfaces, and real publishing systems. The value is not just that an assistant can generate something quickly. The value is that it can help people move from context to creation to shipping with less manual overhead, while still leaving room for human judgment and ownership.

It slows me down when the hard part is no longer producing code, but verifying it, sequencing it, reviewing it, and owning it.

That tradeoff is worth it.

I am much faster with AI than without it. I can work across more areas of the stack. I can get unstuck faster. I can build things that would have taken me much longer before. I spend less time hunting for context and more time making decisions.

But AI did not remove the hard parts of engineering.

It moved them.

The work is less about starting from a blank page and more about knowing what good looks like. It is less about manually assembling every piece of context and more about validating whether the assembled picture is correct. It is less about typing every line yourself and more about owning every line you ship.

That is the version of AI in engineering that feels real to me.

Not magic. Not a replacement. Not a shortcut around judgment.

A very fast assistant that saves me a lot of time, as long as I remember that I am still the engineer responsible for the result.

*This article was originally published on July 9, 2026, on* [*webflow.com*](https://webflow.com/blog/ai-saves-time)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/07/00dc5030-cropped-74138d5a-laureanogonzalez46-scaled-1-600x600.jpeg)

Laureano Gonzalez is a Senior Software Engineer at Webflow, where he works on bringing AI-powered features into the product experience. With experience across frontend, backend, and full-stack development, he focuses on building reliable, maintainable systems that support real product workflows....

Read more from Laureano Gonzalez](https://thenewstack.io/author/laureano-gonzalez/)