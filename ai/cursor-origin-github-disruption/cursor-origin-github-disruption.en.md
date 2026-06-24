**The biggest news to emerge** from the AI world this week was undoubtedly that Elon Musk’s [SpaceX had agreed to acquire](https://thenewstack.io/spacex-cursor-ai-coding/) AI coding startup [Cursor](https://cursor.com/) in an all-stock deal valued at $60 billion.

But on the very same day, at an [invite-only developer conference](https://cursor.com/compile) hosted by Cursor in San Francisco, [Tomas Reimers](https://www.linkedin.com/in/tomasreimers/) took to the stage [to unveil](https://x.com/morganlinton/status/2066958434805956937) a fledgling project that could prove just as consequential for the developer tools industry.

[Origin](https://cursor.com/origin), as it’s called, [is a Git-compatible code-hosting platform](https://x.com/cursor_ai/status/2067012220832329782?s=20) designed from the ground up for a world where AI agents — rather than humans — do the bulk of the work.

Reimers, it’s worth noting, is co-founder of [Graphite](https://graphite.com/), a code-review startup that Cursor revealed it was acquiring [back in December](https://tessl.io/blog/cursor-acquires-graphite-to-bridge-code-creation-and-review/) (a deal that apparently closed in January). At the time, some commentators noted the deal’s implications for GitHub — among them was Gergely Orosz.

Orosz, author of *The Pragmatic Engineer* newsletter and an investor in Graphite, who wrote on LinkedIn: “I’m telling you: GitHub’s biggest competitor could soon be Cursor. Graphite — in my view — is the best AI code review + stacked diffs + PR workflow product out there. GitHub is already playing catch-up to Cursor/Graphite.”

Put simply, Graphite had already built workflow tools that GitHub was scrambling to replicate — and with Cursor’s resources behind it, the gap was only going to widen. And now with the might of SpaceX, a $2.5 trillion company, behind it, things could be about to get very interesting.

## The Origin origin story

On stage in San Francisco ahead of Origin’s unveiling, Reimers pointed to Graphite’s customer base — which includes Shopify, Snowflake, Notion, and Figma — as evidence of a problem already well underway before Origin existed.

> “When we were acquired by Cursor, we accelerated our most ambitious project — to rebuild that tooling from scratch.”

“Over the past few years, we noticed the trend as these companies adopt AI tooling,” Reimers said. “The tools that they relied on started to become unreliable. That’s because over the past few years, AI tooling has totally changed our industry. It’s enabled every developer to be a 10 to 100x developer, but that change has required fundamentally different tooling. That’s why, when we were acquired by Cursor, we accelerated our most ambitious project — to rebuild that tooling from scratch.”

**Amid all the hullaballoo of SpaceX** hitting the public markets, becoming one of the world’s most valuable companies overnight, and doling out a cool $60 billion for a four-year-old startup, it’s easy to appreciate why Origin might have slipped under the radar. But the infrastructure problem it’s setting out to solve is real.

> It’s easy to appreciate why Origin might have slipped under the radar. But the infrastructure problem it’s setting out to solve is real.

**GitHub, the world’s dominant code hosting platform by some distance**, is having a rough time of it. As *The New Stack* [reported in June](https://thenewstack.io/github-wants-developers-back/), the platform has logged hundreds of incidents over the past 12 months, [struggling to keep pace](https://www.theregister.com/software/2026/06/12/github-outages-persist-as-ai-coding-drives-traffic-surge/5255125) with the volume of code that AI agents are generating. The company says it’s now processing about 1.4 billion commits per month — up from 1 billion across all of 2025 — with agents alone generating more than 17 million pull requests per month.

The irony isn’t lost on anyone: GitHub helped kickstart the AI coding era with the [launch of Copilot in 2021](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/), and it’s now buckling under the weight of it. And for some, the cracks are already showing in their day-to-day habits.

[Brian Douglas](https://www.linkedin.com/in/brianldouglas/), GitHub’s former director of developer advocacy who recently [launched his own AI infrastructure startup](https://thenewstack.io/paper-compute-agent-infrastructure/) called [Paper Compute](https://papercompute.com/), tells *The New Stack* that the shift is already underway.

> “Agents are quickly killing the will for doing open source.”

“Agents are quickly killing the will for doing open source,” Douglas says. “I’d love to see what GitHub’s [monthly active user] numbers look like today, because I am sure there are a number of folks choosing to do code reviews elsewhere — or exclusively collaborating with agents to get the work to the last mile — which is at an all-time high.”

Douglas, for what it’s worth, counts himself among them, saying he now does much of his review and PR work directly in AI coding tools.

“As a GitHub power user, I find myself using it less, and relying more on Claude and Codex for review and PR interactions,” he says.

## A post-GitHub world?

Origin remains in waitlist-only mode ahead of a planned fall launch, and those present at Compile reported enough detail to sketch its ambitions. Developer advocate and independent commentator [Shawn Wang Yuexian](https://www.linkedin.com/in/shawnswyxwang/), known as swyx, [described it](https://x.com/swyx/status/2066928345246470204) as a “long-awaited Git competitor, scalable for agent workloads, extensible with API and MCP, and with built-in merge conflict and CI failure agent resolution.”

Whatever Origin looks like in its launch guise, it’s clear the appetite for an alternative to the status quo is growing. The software development world has changed considerably since GitHub popularized the pull request model back in 2008 — a feature that Douglas calls its “best ever.” But the pull request was designed for a world where humans deliberately wrote and reviewed code, one change at a time. That world is receding fast.

> “Right now, the velocity of projects being created is overwhelming GitHub, and engineers are not looking at the code.”

“Right now, the velocity of projects being created is overwhelming GitHub, and engineers are not looking at the code,” Douglas says. “So if the goal is to put it in the cloud so agents are managing the code, I think that is absolutely an opportunity for disruption.”

So, as AI agents push code at a rate no human reviewer can keep up with, the pull request risks becoming a formality — a box to tick rather than a meaningful quality gate. Which raises a deeper question about *how* the industry should measure the value of software work at all.

For Douglas, the answer lies in a different unit entirely. Commits and lines of code — the traditional proxies for developer output — tell you little in a world where an agent can generate thousands of lines in seconds. Tokens, by contrast, map directly to compute cost and, therefore, to the real effort and value generated. It’s a reframing that suits Cursor rather well.

> “Tokens are a better metric than commits.”

“Tokens are a better metric than commits,” Douglas says. “They align to a dollar spent that correlates to the effort of work. Previously, we pretended lines of code were the metric, and that was proven incorrect. But tokens plus agent sessions equals customer value — and Cursor is positioned well to own a deeper part of the collaboration stack.”

Cursor, though, isn’t alone in that conviction, and a slew of tangential efforts to rebuild that infrastructure for the agentic era are emerging.

At its [Transcend conference](https://about.gitlab.com/events/transcend/london/) in London on June 10, GitLab [announced](https://about.gitlab.com/press/releases/2026-06-10-gitlab-announces-new-capabilities-to-give-enterprises-speed-control-at-agentic-scale/) a private beta of what it calls [Next Generation Source Code Management](https://about.gitlab.com/blog/gitlab-transcend-announcements/) — known internally as Project Switch. [Unveiled on stage](https://www.youtube.com/watch?v=ekcw1yn21jQ) by GitLab chief product and marketing officer [Manav Khurana](https://www.linkedin.com/in/mkhurana/), the new backend keeps the Git protocol intact but redesigns the underlying architecture entirely, allowing agents to query repositories server-side rather than cloning them in full.

GitLab says it delivers up to 50 times faster task execution per agent, with up to 3 times fewer tokens consumed. And notably, Anthropic is a design partner on the project.

“The most popular Git platforms in the world are buckling under the load, not just because of your teams cloning, branching, and merging code, but also dozens, in some cases hundreds, of agents working simultaneously and putting a lot of pressure on those systems,” Khurana said.

The day after GitLab’s Transcend announcement, Zed co-founder [Nathan Sobo published details](https://zed.dev/blog/introducing-deltadb) of [DeltaDB](https://zed.dev/deltadb), a project the company had [first teased the previous fall](https://zed.dev/blog/sequoia-backs-zed). A more radical proposition than either Origin or Project Switch, DeltaDB replaces Git’s commit-based model entirely with a continuous stream of fine-grained deltas — every operation an agent performs, linked directly to the conversation that produced it. Sobo confirmed that a beta version is just weeks away.

HashiCorp co-founder Mitchell Hashimoto, meanwhile, has seen this coming. Back in December, he wrote on X: “The AI companies are on track to become GitHub faster than GitHub is becoming an AI company.”

When Origin was announced this week, he [retweeted himself](https://x.com/mitchellh/status/2066950461790536156?s=46) with a single line: “Cursor announced Origin today. More will come.”

Hashimoto, as it happens, [is an investor](https://x.com/mitchellh/status/2066957972992151687?s=20) in another agent-native code hosting startup called East River Source Control ([ERSC](https://ersc.io/)), which is [building](https://ersc.io/blog/ersc-availability) a Git-compatible platform designed to land thousands of commits per second.

## The model is the moat

For Douglas, the convergence of competing efforts to rebuild version control from the ground up isn’t hugely surprising. In the past year, he points out, a similar dynamic played out with developer sandboxes — the environments where code gets written and tested — as companies [like Docker](https://www.docker.com/blog/docker-sandboxes-a-new-approach-for-coding-agent-safety/), [Cloudflare](https://blog.cloudflare.com/sandbox-ga/), and [Vercel](https://vercel.com/sandbox) moved into that space because that’s where developers were spending their time.

The same gravitational pull is now acting on version control. The way developers work has changed fundamentally — where once they wrote code directly inside their editors, many now spend their time directing AI agents that do the writing for them. The IDE is no longer primarily a place to type; it’s increasingly a place to watch, review, and steer.

> “I think all the folks who are part of the story have a shot, and we need to rethink our infrastructure to prepare for this.”

“Now, IDEs are suffering from the fact that developers have evolved to foundational model harnesses writing code, and they need to position themselves as the tool you open to watch agents write the code,” Douglas says. “I think all the folks who are part of the story have a shot, and we need to rethink our infrastructure to prepare for this.”

Underpinning all of this, though, is a commercial reality. Cursor has been building toward this position for some time, having launched [its own first-party coding model](https://cursor.com/blog/composer), Composer, in 2025 and [iterating](https://thenewstack.io/cursor-composer-benchmarks/) [on Composer 2.5 in May](https://thenewstack.io/cursor-composer-benchmarks/), giving it cheaper, in-house inference rather than relying entirely on costly API calls to Anthropic and OpenAI. Composer 2.5 costs a fraction of Claude Opus at equivalent tasks — as much as a tenfold difference on output tokens. Owning the model, in other words, is what makes owning the rest of the stack viable.

“It’s clear you can’t just insert an OpenAI key and expect hyper-growth or longevity in this market anymore,” Douglas says. “Instead, you need to own the model to win.”

Whether SpaceX’s firepower accelerates that ambition or complicates it remains to be seen. But the companies placing bets on the next era of software development aren’t waiting for GitHub to catch up.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)