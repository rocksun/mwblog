**Anthropic is giving Claude Code a new job**: Manage other Claude Code sessions.

Starting Thursday, Anthropic says select Claude Pro and Max subscribers can access the redesigned Projects in beta through cloud sessions in Claude Code, with access expanding to more users on those plans over the coming week.

The company is redesigning Claude Projects — which until now grouped chats around a shared knowledge base and instructions — with a coordinator that can take an engineering goal, break it into smaller jobs, and hand them to multiple Claude Code sessions running in parallel. This will eliminate the manual work that previously required developers to divide tasks between sessions and bring the results back together themselves.

“Claude scopes the request, delegates the work, coordinates parallel threads, reviews the outputs, and assembles the finished result,” an Anthropic rep tells *The New Stack*.

Once a developer sets a goal, Claude decides how to split the work across threads, which the developer can monitor — or open individually if they need to intervene. Each thread runs as its own Claude Code cloud session with a separate branch and copy of the repository. It can use subagents, loops, and workflows to handle smaller pieces of the job.

## More sessions use more plan

That parallel approach can also use up tokens much faster. Anthropic says Projects will hit usage limits sooner when multiple threads are running because each one counts as a full Claude Code session.

Anthropic is [facing a class-action lawsuit](https://thenewstack.io/anthropic-claude-max-lawsuit/), filed last week, from developers who pay for its Max plan. They allege that advertised usage increases came with weekly ceilings that Anthropic didn’t disclose at first.

> “Claude scopes the request, delegates the work, coordinates parallel threads, reviews the outputs, and assembles the finished result.”

## One Claude coordinates the work

A team retiring an old API endpoint, for example, could connect its API, web, and mobile repositories and have Claude create a thread for each one to update callers, run tests, and open PRs before identifying which changes need to merge first.

Developers can follow the work through the main Project chat or open an individual thread to inspect or redirect it without having to start and manage each Claude Code session themselves.

The coordinator isn’t the last layer of delegation, as each worker thread can split its assignment further using Claude Code’s existing subagents, loops, and workflows when the job calls for it. That review layer may be more than cosmetic: on the Real-SWE benchmark, which [tests coding agents against private codebases](https://thenewstack.io/real-swe-coding-benchmark/), even Anthropic’s own Fable 5.1, the top scorer, failed more than 60% of the time.

The finding suggests that coordination and output review matter as much as raw model capability when agents are dropped into unfamiliar production code.

## Parallel threads, familiar conflicts

Each thread works from its own branch, which keeps the work separate but doesn’t prevent two threads from changing the same code. When that happens, Anthropic says it handles it as a merge conflict, just like any other pull request.

> Each thread works from its own branch, which keeps the work separate but doesn’t prevent two threads from changing the same code.

## Project background carries across threads

Additionally, Anthropic is adding shared memory so information learned in one thread can be used by the others without developers repeatedly supplying the same context.

Projects can retain details such as a changed release date, the reason a feature was dropped, or who needs to approve changes to a particular service, with that information carrying forward as work continues over days or weeks.

Claude can also remember how the developer wants the project managed, including how often it should check in, when it should start new threads, and how detailed its updates should be, while a new library keeps files added by the user alongside artifacts Claude produces so future work can draw on material already created within the project.

Users can track Project-specific usage and choose the model and effort level for the coordinator and worker threads, while support for running threads locally alongside a developer’s tools and code, including resources behind a private network, is coming soon.

The beta will expand to more Claude Code users on Pro and Max plans over the coming week, with mobile support coming soon and Team and Enterprise access planned for later.

Existing subscribers who already use Projects will remain on the current version until Anthropic upgrades them. The redesign is part of a broader product consolidation: Anthropic recently [merged](https://thenewstack.io/anthropic-claude-unified-interface/) Claude chat and its Cowork interface into a single view, betting that removing the choice of mode would reduce friction rather than add it.

> Existing subscribers who already use Projects will remain on the current version until Anthropic upgrades them.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)