Most open source maintainers will know the feeling of opening GitHub to a growing pile of issues that can’t feasibly be maintained by a small team. AI coding tools [have made things worse](https://thenewstack.io/ai-generated-code-crisis/): a low-effort bug report, an unreviewed patch, or a speculative vulnerability write-up can all be generated in seconds now, but working out whether any of it holds up still takes a person just as long as it always did.

However, the team behind one popular open source project has reported that it’s on track to clear its issue backlog entirely, by handing the grunt work to a team of agents.

[Astro](https://github.com/withastro/astro), the JavaScript framework used to build fast, content-heavy websites, is down to [around 20 open GitHub issues](https://github.com/withastro/astro/issues) at the time of writing, from more than 200 at the start of this year — and the team expects to hit zero within the next month, which would be a first in the project’s five-year history. It’s getting there using a team of AI subagents built by its own team, and Cloudflare, which [acquired that team in January](https://thenewstack.io/cloudflare-acquires-team-behind-open-source-framework-astro/), [announced](https://blog.cloudflare.com/astro-issue-triage) on Tuesday that it’s open-sourcing the systems for other maintainers to use.

## Astro finds its fix

The tool, called [triagebot-action](https://github.com/withastro/triagebot-action), runs as a GitHub Action. When someone opens an issue, it kicks off a four-stage pipeline: reproduce the bug in a sandbox, diagnose the root cause, verify it’s an actual bug, and attempt a fix. Each stage is handled by a separate AI agent, and the whole process is driven by a state machine encoded in GitHub labels, so anyone can see exactly where a given issue sits and why.

> “‘Fix’ is always the hardest because the bar is so high.”

[Fred Schott](https://www.linkedin.com/in/fredkschott/), Astro’s co-founder and now a senior engineering manager at Cloudflare, says the “fix” step is the least essential part of the system — triaging an issue and handing the report to a human maintainer is, in his words, “still a pretty great outcome” even without it. But the fix is the hardest part to get right.

“Fix is always the hardest because the bar is so high,” Schott tells *The New Stack*. “Where all of the other tasks are just ‘*can you complete your phase* — *reproduce the bug, diagnose the cause, etc*‘. ‘Fix’ is the one where it has to write code that is of high enough quality that it can be merged.”

![Flagging a bug fix](https://cdn.thenewstack.io/media/2026/08/549bdcca-image3-1024x819.png)

*Flagging a bug fix*

That gap is exactly why triage, not fixing, came first. Schott traces it back to watching where agents kept proving reliable and where they didn’t.

“I think [it was] just the gradual realization that issue triage is something agents got very good at, without falling into some of the traps of what they were bad at re: code quality,” he says. “And issue triage is also very time-consuming for us as maintainers, so the realization that automating it, without requiring a maintainer to manually trigger it, would save us a ton of time.”

> “Issue triage is also very time-consuming for us as maintainers.”

## Astro’s home turf

By way of a brief recap, Astro launched as an open source project back in 2021, and Schott [spun up The Astro Technology Company](https://astro.build/blog/the-astro-technology-company/) the following year with $7 million in seed funding from a roster of backers that included Lightspeed Venture Partners and Google’s Gradient Ventures.

Cloudflare announced it had acquired that company in January, absorbing the team behind a framework that had come to be used by companies like IKEA, Unilever, and Visa. Astro ships pages as plain HTML by default and only loads JavaScript for the parts of a page that actually need it, unlike React-based frameworks, which tend to send a much larger JavaScript bundle for the whole page. This approach, ultimately, aligns with Cloudflare’s own business of making the web faster.

At the time, *The New Stack* [pondered what the deal meant](https://thenewstack.io/why-platform-companies-keep-buying-frontend-framework-teams/) for Astro’s future, pointing to a pattern of platform companies buying up frontend framework teams — some of which, like [Netlify’s 2023 purchase of Gatsby](https://thenewstack.io/netlify-acquires-gatsby-its-struggling-jamstack-competitor/), ended with the acquired framework slowly starved of support once its creators moved on. The question was whether Cloudflare would keep investing in Astro or let it drift into the same kind of neglect.

Six months on, Schott says little has changed. Astro still has four full-time engineers, including Schott himself, and everyone who joined through the acquisition remains on the project full time, though volunteer and Open Collective-funded contributors continue to come and go as they always have. Schott says that Astro “still operates distinctly as its own team,” replete with an open roadmap, release cadence, and so on. The team, it’s worth noting, [shipped a redesigned development server](https://thenewstack.io/astro-redesigns-its-development-server/) as part of an Astro 6 beta in January, but triagebot-action is perhaps the clearest sign yet that it has room to build new things.

Adoption of the tool beyond Astro itself is still early. Schott says Cloudflare’s [workers-sdk](https://github.com/cloudflare/workers-sdk) team is prototyping it internally, but “only Astro currently” runs it in production. The underlying agent framework behind it, [called Flue](https://flueframework.com/), sits under the Astro organization rather than Cloudflare’s, and both projects are built to run on any infrastructure, with no dependency on Cloudflare-specific tooling.

## Built for agents

Zooming out, triagebot-action is the second tool in a week that Cloudflare has open-sourced with AI agents as the primary user. At the tail end of July, [Cloudflare released pvcli](https://thenewstack.io/cloudflare-pvcli-privacy-debugger-agents/), a command-line debugger for privacy protocols used in products from the likes of Apple and Microsoft. Cloudflare systems engineer Fisher Darling said at the time that pvcli was “explicitly designed for agent-based debugging.”

Triagebot-action tackles a different problem, but the underlying idea is similar: taking work that traditionally required a person at a keyboard and packaging it into software that an AI agent can execute autonomously.

> “It’s great when it works, but it’s also always at the discretion of a maintainer for if it is correct and worth accepting, or better to go and write the fix yourself.”

Looking to the future, the next obvious progression for a tool like triagebot-action is the “fix” element itself. Schott says he doesn’t know when the system will get to the point where its fixes can be trusted close to 100% of the time, but that it’s built to evolve toward that gradually — it launched internally with no fix capability at all, then added a suggested fix left on a branch for a reviewer to look at, and only later gained the ability to open a pull request directly from that suggestion. He can picture it going further still: the agent judging its own confidence or the size of a fix, and eventually opening, or even merging, pull requests on its own.

“We are really taking this part seriously, which is why we really focus on the issue triage part first, and then ‘*write the code for me to fix this issue*‘ part is secondary and nice to have at the end,” Schott says. “It’s great when it works, but it’s also always at the discretion of a maintainer for if it is correct and worth accepting, or better to go and write the fix yourself.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)