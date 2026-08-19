Cursor has officially thrown its hat into the code-hosting ring with [Origin](https://cursor.com/docs/origin), a Git-compatible platform built for a world where AI agents generate the commits.

The [beta launch](https://cursor.com/changelog/origin-code-hosting) announced late on Monday comes two months after [Tomas Reimers](https://www.linkedin.com/in/tomasreimers/) took to the stage [at Cursor’s developer conference in San Francisco](https://thenewstack.io/cursor-origin-github-disruption/) to tease its agent-focused GitHub alternative. That happened to be on the very same day that Elon Musk’s SpaceX confirmed it had [tabled a $60 billion bid](https://thenewstack.io/spacex-cursor-ai-coding/) to acquire Cursor outright, and with that deal formally [closing on August 14](https://cursor.com/blog/joining-spacex), Origin becomes the first product Cursor has shipped as a fully owned SpaceX subsidiary.

Notably, however, Origin landed on the same day that [GitHub itself went down worldwide](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-github-is-down-worldwide/), turning what might have been a routine beta rollout into a “case in point” on why Cursor was building Origin to begin with. But while the [8-hour outage](https://www.infoworld.com/article/4210864/github-restores-services-after-nearly-8-hour-outage-disrupts-actions-apis-prs-and-copilot.html) may have seemed like fortuitous timing on the surface, GitHub going offline when it did wasn’t great for Cursor, given that Cursor needs a fully operational GitHub for new users to get the ball rolling. As SpaceXAI’s [Matt Palmer](https://www.linkedin.com/in/matt-palmer/) acknowledged [on X](https://x.com/mattyp/status/2089413216011165706): “We were going to ship this earlier, but GitHub was down. Importing your GitHub repos as a first onboarding step is non-optimal if GitHub is down.”

Still, GitHub’s troubles predate this particular blackout. As *The New Stack* [reported in June](https://thenewstack.io/github-wants-developers-back/), the platform has logged hundreds of incidents over the previous 12 months as commit volume jumped from 1 billion a year to 1.4 billion a month, with AI agents alone generating more than 17 million pull requests monthly — growth GitHub traced to infrastructure bottlenecks like MySQL contention and webhook overload.

> “Cursor has joined a slew of technology companies looking to rebuild version control for a world where agents work around the clock.”

In an interview with *The New Stack* at the time, GitHub COO Kyle Daigle discussed the scaling problem: “It’s not just about normal scaling,” he said. “It’s now making sure we can scale at 30 or 40 times” annual growth, as opposed to doubling each year, which GitHub had historically planned around.

Fast-forward to today, and Cursor has joined a slew of technology companies looking to rebuild version control for a world where agents work around the clock, querying and pushing to repositories faster than any human team ever could.

## Origin story

Origin marks a fairly significant expansion of Cursor’s ambitions. Until now, its agents have largely operated on code hosted elsewhere; with Origin, Cursor is pushing to own more of the underlying development infrastructure itself.

At launch, that starts with the basics. Users can create and host Git repositories directly inside Cursor, with the new Codebase tab acting as the home for Origin repos.

![Cursor Origin lets users create and host Git repositories directly inside Cursor.](https://cdn.thenewstack.io/media/2026/08/8784192e-gifa.gif)

*Cursor Origin lets users create and host Git repositories directly inside Cursor.*

Those repositories still behave like Git repos outside Cursor. Developers can clone them locally, add an Origin remote, and push code from the command line — essentially putting Cursor in the role normally occupied by a service such as GitHub.

![Pushing a local repo to Origin](https://cdn.thenewstack.io/media/2026/08/fd832952-gifb.gif)

*Pushing a local repo to Origin*

Cursor isn’t demanding an all-or-nothing migration, either. Existing GitHub repositories can be synced into Origin and displayed alongside Cursor-hosted repos, while GitHub remains the source of truth for projects that started there.

![Syncing GitHub](https://cdn.thenewstack.io/media/2026/08/6a652fdb-gif1.gif)

*Syncing GitHub*

Pull requests are built in too, including diffs, comments, checks and merging. Cursor’s agents sit directly alongside that code: from the browser, users can ask questions about what they’re viewing, have an agent make changes, update a PR or push a branch.

![Reviewing code / ask Cursor / merging](https://cdn.thenewstack.io/media/2026/08/d532747d-gif2.gif)

*Reviewing code / ask Cursor / merging*

That combination is arguably the more consequential part of Origin: the repository, pull request and coding agent now all live inside the same product — giving Cursor more control over the environment in which code is stored, reviewed and changed.

[Rob Whiteley](https://www.linkedin.com/in/rwhiteley/), CEO of [Coder](https://coder.com/), a cloud development platform built for enterprises, sees Origin as a “smart play” — most of the industry’s energy has gone into the tools that write code, he argues, while comparatively little has gone into what happens to that code after it’s produced.

“GitHub is starting to crack under the weight of agentic code development, and an agent-native source code forge is needed,” Whiteley tells *The New Stack*. “Everyone is integrating the ‘writing code’ stack, from editor and chat to agents, tools and LLMs. No one else is really integrating the ‘managing code’ stack, where code gets stored, versioned, reviewed and merged.”

For now, Origin’s restricted to Cursor’s Pro, Teams and Enterprise plans — nothing on the free tier, it seems — and the rollout itself is staged, so not everyone will have access to it quite yet.

## How is Origin different to GitHub?

For now, there’s no escaping the fact that there isn’t a great deal that’s different from trusty ol’ GitHub, a fact that [wasn’t entirely lost on the online community](https://news.ycombinator.com/item?id=49334209). And Origin’s own team isn’t shying away from that, either.

Tomas Reimers, the Origin engineer who co-founded Graphite, a code-review startup Cursor [acquired in early 2026,](https://cursor.com/blog/graphite) fielded questions directly from developers on Hacker News after the launch.

> “We’re intentionally releasing this as a GitHub alternative where we meet them toe-to-toe on functionality.”

[Asked](https://news.ycombinator.com/item?id=49338041) what set Origin apart from GitHub beyond uptime, Reimers concedes that it’s very “very little,” in all honesty. “We’re intentionally releasing this as a GitHub alternative where we meet them toe-to-toe on functionality,” he [writes](https://news.ycombinator.com/item?id=49338196).

He does note that more is on the way: in the coming weeks, Reimers explains, Origin should start shipping deeper agent integrations, tooling that can make sense of agent-written code, and automation that pushes pull requests toward a mergeable state on their own.

“Expect a lot more from us,” he continues. “We wanted to release a beta so people could start experimenting with our scalability and extensibility themselves. Over the next few weeks, you can expect a handful of features starting to change source control to better understand and work with agents.”

Several in the online community also highlighted the timing of Origin’s launch. [Gergely Orosz](https://www.linkedin.com/in/gergelyorosz/), author of *The Pragmatic Engineer* newsletter and an investor in Graphite, initially [took to X](https://x.com/GergelyOrosz/status/2089397495939891698?s=20) to complain about GitHub’s ongoing performance issues, despite the number of engineers it has at its disposal.

Within an hour, however, Orosz was [back](https://x.com/GergelyOrosz/status/2089414076900233647?s=20) to comment on Origin. “Cursor could not have timed their launch announcement of their hosted code service better either,” he writes. “If GitHub was stable, these alternatives would not be as interesting / popular!”

“These alternatives,” as Orosz puts it, are already [forming an orderly queue in GitHub’s shadow](https://thenewstack.io/cursor-origin-github-disruption/).

## The ‘GitHub alternative’ surge

The most direct comparison to Origin is perhaps [Entire](https://entire.io/), a distributed Git network [founded by Thomas Dohmke](https://thenewstack.io/thomas-dohmke-interview-entire/), who stepped down as GitHub’s CEO [last August](https://thenewstack.io/github-loses-its-ceo-and-independence/). Entire, essentially, [mirrors repositories across regional nodes](https://thenewstack.io/entire-git-for-agents/), with GitHub remaining the source of truth for now — though that could change once teams start creating repos natively on the platform. The company [raised a $60 million seed round in February](https://thenewstack.io/thomas-dohmke-interview-entire/), with investors including Microsoft’s venture arm, and it [formally went to market in July](https://thenewstack.io/entire-git-for-agents/).

> “Cursor could not have timed their launch announcement of their hosted code service better either. If GitHub was stable, these alternatives would not be as interesting / popular!”

GitLab, meanwhile, is also rethinking source control for an agent-heavy world, [announcing a private beta](https://about.gitlab.com/press/releases/2026-06-10-gitlab-announces-new-capabilities-to-give-enterprises-speed-control-at-agentic-scale/) of “Next Generation Source Code Management” — internally called Project Switch — back in June. Instead of agents cloning an entire repository to read or change a handful of files, the system lets them query the server for exactly what a task needs, with each agent’s visibility capped at the minimum required.

Elsewhere, code editor startup [Zed](https://zed.dev/) has [also been teasing](https://zed.dev/blog/introducing-deltadb) a new approach to version control [since last year](https://zed.dev/blog/sequoia-backs-zed), and in early August the company finally [debuted Delta](https://zed.dev/blog/introducing-delta), a “multiplayer environment for coding with agents and reviewing what they build,” as the company puts it.

“Delta keeps code and conversations connected, so developers and agents can work together with the full context of how the code came to be,” Zed co-founder and CEO Nathan Sobo wrote at the beta launch.

Underneath, Delta runs on [DeltaDB](https://zed.dev/deltadb), which keeps a live copy of conversations and in-progress work synced across a team. It sits alongside a project’s existing Git repository, and works with agent tools including Claude Code. What that changes in real terms: comments stay attached to the code they refer to as an agent keeps editing it.

Despite GitHub’s persistent reliability problems, Whiteley doesn’t see Cursor’s version becoming a major enterprise play any time soon, mostly due to the pain of switching.

“Most [enterprises] have already spent a lot of pain and money standardizing on GitHub, and moving again would mean a lot of pain for limited ROI today,” he says. “That could change as ‘vibe coding’ generates an order of magnitude more code. If Cursor commits to keeping Origin open enough for enterprises to trust and integrate with, it could become much more appealing over time.”

So while there is a clear flurry of activity in the “GitHub alternative” realm, it’s still too early to say whether any of them will cut it in the long term. GitHub has an 18-year head start: it launched in 2008, popularized the pull-request review model most of these newcomers are trying to disrupt, and was snapped up by Microsoft in 2018. It also set off the current wave of AI coding tools itself with the launch of Copilot in 2021 — the same wave now generating the volume its own infrastructure is struggling to absorb.

For now, GitHub remains the only one of these platforms actually handling this kind of developer activity at scale. However, at a lofty $2 trillion valuation, SpaceX is one of the world’s most valuable companies, which puts Cursor in a strong position when it comes to investment — not just [in its own AI models](https://thenewstack.io/cursors-composer-2-beats-opus/), but in the infrastructure underneath them.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)