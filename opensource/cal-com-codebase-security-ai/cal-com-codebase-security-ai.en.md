[Cal.com](http://Cal.com), an open-source startup that builds scheduling infrastructure for developers and enterprises, [announced](https://cal.com/blog/cal-com-goes-closed-source-why) on Tuesday that it’s moving its core codebase behind closed doors, citing growing security concerns tied to advances in AI.

Much has been written about the growing [impact of AI on open-source projects](https://thenewstack.io/is-ai-killing-open-source-software/), with already time-pressed maintainers battling a barrage of machine-generated “[AI slop](https://thenewstack.io/is-ai-killing-open-source-software/)” masquerading as contributions. But the emergence of AI systems capable of systematically uncovering software vulnerabilities has pushed the conversation in a more serious, security-centric direction.

Anthropic recently unveiled [Claude Mythos](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/), an experimental system that it says can identify and exploit vulnerabilities across widely used software — including a 27-year-old flaw in [OpenBSD](https://www.openbsd.org/), a security-focused Unix-like operating system long regarded as one of the most hardened in its class.

While its capabilities are, for now, limited to select partners through [Project Glasswing](https://www.anthropic.com/glasswing), the implications are already being felt. And for companies built around open code, the trade-off between transparency and security is falling under renewed scrutiny.

> “It’s easier to perform a bank heist if you have the blueprints to the vault.”

Cal.com is among the first to act on that shift. CEO and co-founder [Bailey Pumfleet](https://www.linkedin.com/in/baileypumfleet/) tells *The New Stack* that greater visibility into code makes systems easier to attack.

“It’s easier to perform a bank heist if you have the blueprints to the vault,” Pumfleet says. “It’s a lot easier to see the inner workings of something and reverse engineer it to find a vulnerability.”

Asked whether that risk comes down to visibility or how code is maintained, Pumfleet says both are factors — but that openness materially increases exposure.

“Simply having the code open increases the risk dramatically,” he says. “It’s not closing the code or hardening it; it’s just that we’re doing both. Simply hardening it does not decrease the risk enough.”

## An “open-source Calendly”

Founded in 2021, Cal.com set out to [build an open-source alternative to Calendly](https://venturebeat.com/business/open-source-calendly-alternative-cal-com-promises-greater-data-control), offering developers a way to embed scheduling functionality directly into their own applications.

Rather than building booking systems from scratch, companies can tap Cal.com’s infrastructure to handle everything from meeting links to availability management. The idea is to treat scheduling as infrastructure — something that can be plugged into other products rather than used as a standalone tool.

![Cal.com in action](https://cdn.thenewstack.io/media/2026/04/edc7a479-giffy.gif)

***Cal.com in action***

The company has raised more than $30 million from a mix of venture and angel investors, including Reddit co-founder Alexis Ohanian’s firm Seven Seven Six and YouTube co-founder Chad Hurley.

As with most commercial open-source startups, one of the big selling points of making its source code available to poke and prod is that it allows developers to verify how the system works, adapt it to their needs, and run it on their own infrastructure.

[Available under](https://github.com/calcom/cal.com) the “copyleft” GNU Affero General Public License (AGPL), Cal.com allowed users to do just that — albeit with the proviso that anyone modifying the software and running it as a service must make those changes publicly available.

But over time, the codebase powering Cal.com’s hosted platform had begun to diverge from the publicly available codebase, with a growing set of commercial and enterprise features developed outside the open repository. Now, that separation is being made explicit.

## Split decision

Rather than removing its open source project entirely, Cal.com is carving out a distinction between what it shares publicly and what it runs in production.

Alongside the shift, the company has released [Cal.diy](http://Cal.diy), an open-source version of its platform that’s now licensed under the permissive MIT license. While it retains the core scheduling engine and booking infrastructure, a range of features tied to the commercial product have been removed, including team management, workflows, analytics, and enterprise authentication.

> Cal.com is carving out a distinction between what it shares publicly and what it runs in production.

In real terms, this leaves a self-hostable version of the platform available to hobbyist developers, while the code that powers Cal.com’s hosted service — and future development of the product — now sits in a closed repository away from the prying eyes of automated scanners.

The move formalizes a boundary that had already begun to emerge. Cal.com says it has spent recent months rewriting critical components outside of the public codebase, with the open project diverging from the system used in production.

> “We just wanted to keep Cal.diy as a way to give this out to the community for free, and share it under the most permissive license possible.”

“Cal.diy is the core part of Cal.com that handles all of the scheduling and simply has all of the enterprise features stripped out,” Pumfleet says. “That being said, our codebase has since diverged from the open-source version because we have rewritten critical security parts like authentication and data-handling. We just wanted to keep Cal.diy as a way to give this out to the community for free, and share it under the most permissive license possible.”

## Security, or something more?

Cal.com positions the move entirely as a response to a changing security landscape, arguing that advances in AI are making it easier to identify and exploit vulnerabilities in publicly available code.

The recent wave of AI-driven vulnerability research, including [Anthropic’s Mythos project](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/), has brought those concerns into sharper focus. But Cal.com co-founder and chairman Peer Richelsen tells *The New Stack* that the decision to move away from open development was already underway.

“We made this decision long before Claude Mythos and the OpenBSD vulnerability was announced, but the timing is frightening,” Richelsen says.

Pumfleet, meanwhile, says the company had already seen “a huge decrease in the cost to hack,” alongside a wave of new AI scanners that find vulnerabilities across open-source projects.

So, moving its core platform behind closed doors raises an obvious question: Given that Cal.com’s *raison d’être* was, at least initially, to be an open-source alternative to Calendly, does this risk alienating its customers?

“We have spoken to some customers internally, and they’re simply just grateful that we’re taking the steps to secure their data in the best way possible,” Pumfleet says. “I don’t think that a huge amount of customers will be put off because ultimately customers care way more about the security of their data than whether something is open source or not.”

Cal.com also confirmed that customers who are currently self-hosting will be offered access to a private, on-premise GitHub repository as part of the transition.

> “I am definitely aware of plenty of other commercial open source companies with similar backgrounds to us, reassessing open source.”

Moves like this aren’t exactly without precedent. Long before the current wave of AI-driven security concerns, companies built on open-source foundations have moved to more restrictive models — often in response to commercial pressures, ranging from limiting use by cloud providers to tightening control over monetization. This has often involved carving out enterprise features, changing licenses, or restricting access to parts of their codebases.

And so that history raises a broader question: does Cal.com’s move signal a new reality for open source, or is the company just following a familiar playbook under a different justification?

Pumfleet, for his part, rejects the idea that the move is about asserting greater control.

“The decision is entirely about security,” Pumfleet says. “We already have control over the product being open source, and we don’t really stand to gain much from being closed source. It’s really just a question about de-risking on the security side.”

Richelsen takes a broader view, arguing that the issue extends far beyond Cal.com. “We believe any open-source application is at-risk, and should take all or the sensitive parts of their app private,” he says.

Pumfleet says that others may follow: “I am definitely aware of plenty of other commercial open source companies with similar backgrounds to us, reassessing open source,” he says.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)