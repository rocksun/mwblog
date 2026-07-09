There’s a common fear about what AI could do to open source. Coding agents take over the beginner-friendly issues that help new contributors get started; the code they generate is harder to maintain, and eventually, the pipeline of new maintainers dries up. It’s a plausible scenario. But according to new research, it doesn’t appear to be what’s actually happening.

​A [study submitted to arxiv.org on July 2 out of Peking University](https://arxiv.org/abs/2607.01810) tracked 1,888 GitHub repositories that adopted AI coding agents, tools like Cursor and Claude Code, to see how those projects changed after AI entered the workflow. The researchers treated adoption as the point when a project committed its first agent configuration file, something like a .cursorrules or CLAUDE.md, and then compared those projects against a matched set that never adopted.

They used difference-in-differences, which is basically the gold standard for separating what a tool actually caused from whatever was already going on in a project before the tool showed up. And what they found was…not much. Newcomer participation held steady or crept slightly upward. Under the most conservative statistical specification, the worst they could find was a 1.5% dip that didn’t approach statistical significance.

## Complexity up, contributors steady

​​Cyclomatic complexity, which counts the number of independent paths through a function, ticked up 3% to 4% across all languages after adoption. Cognitive complexity, the trickier metric that penalizes heavily nested logic and tangled control flow, jumped by about 11% in Python projects. That sounds bad until you compare it to a [Carnegie Mellon study published last year](https://arxiv.org/abs/2511.04427), which found that Cursor adoption drove a 41% increase in the same metric. The Peking University team, working with a larger and more established set of projects and tighter statistical controls, landed at roughly a quarter of that earlier estimate.

But where the study really gets interesting is that instead of just reporting complexity and newcomer numbers as two separate findings that happen to live in the same PDF, they locked the analysis to the exact 128 Python projects where complexity actually increased.

On those same repos, newcomer entry didn’t decline, retention held steady, and the active contributor base grew. Both effects are real, but they don’t seem to be connected. AI-generated code is getting a little more complicated, yet that extra complexity doesn’t appear to be discouraging newcomers, at least at the levels this study found.

> AI-generated code is getting a little more complicated, yet that extra complexity doesn’t appear to be discouraging newcomers, at least at the levels this study found.

## What the study excluded

There are a few important caveats. The biggest issue is that the study focused on established open-source projects. Nearly two-thirds of the repositories that adopted AI coding tools did so almost as soon as they were created, leaving researchers with no meaningful pre-AI baseline for comparison. Those repositories were excluded from the main analysis, which instead focused on 603 projects with at least six months of history before AI was introduced.

The researchers also examined the full dataset, in which newcomer participation appeared to decline. But a closer look showed those projects were already losing contributors before they adopted AI, making it impossible to blame the decline on the tools themselves.

## Measuring adoption’s blind spots

There’s another limitation, too. The study measures AI adoption by looking for configuration files associated with tools like Cursor, not by tracking how often developers actually used them. That means it can tell us what happened after projects adopted AI, but not whether teams that relied heavily on AI experienced different outcomes than teams that only experimented with it.

GitHub says merged pull requests across the platform have grown from about 25 million per month in early 2023 to roughly 90 million a month today.

GitHub has started responding, too. The company recently introduced limits on the number of open pull requests that outside contributors can have at once, along with new tools to help maintainers sort through growing review queues.

> The crowding-out fear is, for now, put to rest.

## Where this leaves us

The crowding-out fear is, for now, put to rest. In established open-source projects, at current adoption levels, AI agents are not pushing newcomers out the door. However, pull request volume has nearly quadrupled. The code arriving in those PRs is a bit more complicated. The people submitting it may not fully grasp what they’re proposing. And all of that lands on maintainers whose ranks are not growing at anything like the same pace.

The researchers say future work should examine how heavily projects rely on AI coding tools and find better ways to study repositories that were effectively born with AI. Those are important next steps. But the question that feels most pressing is: Not whether AI changes who shows up to contribute, but whether it changes the effort required to maintain an open-source project over time.


> Not whether AI changes who shows up to contribute, but whether it changes the effort required to maintain an open-source project over time.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)