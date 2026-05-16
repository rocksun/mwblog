As one of the stalwarts of the modern developer tooling industry, GitLab needs little introduction. The company helped popularize the idea of a single platform for managing the software development lifecycle, spanning source control, CI/CD, security scanning, collaboration, and deployment within a single system.

But now, GitLab is restructuring itself for a whole new paradigm: that AI agents will increase the amount of software being built — and developers will spend their time supervising, reviewing, and coordinating machine-generated code rather than writing every line themselves.

[Bill Staples](https://www.linkedin.com/in/williamstaples/), who has served as GitLab’s CEO since co-founder [Sid Sijbrandij](https://www.linkedin.com/in/sijbrandij/) stepped down [in 2024](https://www.linkedin.com/posts/sijbrandij_on-todays-earnings-call-i-am-announcing-activity-7270548131891556352-eBU5/), announced a slew of changes at the company this week, including layoffs, executive changes, product consolidation, and a renewed focus on AI-driven software development.

The overhaul comes during a difficult stretch for GitLab. The company’s market capitalization has dropped roughly 66% to around $3.7 billion over the past 15 months, as investors question how AI will reshape software development and developer tooling more broadly.

Staples, for his part, thinks he has an answer to quell this decline. In [an open letter published on Monday](https://about.gitlab.com/blog/gitlab-act-2/), Staples argues that AI won’t shrink the software industry — it will expand it. Making software cheaper to produce, the thinking goes, will only create demand for more of it. Economists call that [Jevons’ paradox](https://en.wikipedia.org/wiki/Jevons_paradox) — a nineteenth-century economic theory, named for the same [effect that saw](https://cssh.northeastern.edu/what-is-jevons-paradox-and-why-it-may-or-may-not-predict-ais-future/) more efficient steam engines drive coal consumption up, not down — and GitLab is betting its future on it.

> “As the cost of producing software collapses, demand for it will expand.”

“Software has been the force multiplier behind nearly every business transformation of the last two decades,” Staples writes. “The constraint was the cost and time of producing and managing it. That constraint is collapsing. As the cost of producing software collapses, demand for it will expand.”

## A “machine-scale” rebuild for the agentic era

Digging into the details of the letter, Staples points to several large architectural and organizational bets built around what GitLab calls the “agentic era” of software development.

“Software will be built by machines, directed by people,” Staples writes. “Agents will plan, code, review, deploy, and repair.”

Crucially, Staples argues that this won’t reduce the importance of engineers, though it does change where their value exists. Developers will focus on higher-level system design, architecture, governance, reasoning through failures, and coordinating fleets of AI systems operating across the software lifecycle.

That framing also helps explain why GitLab is putting such heavy emphasis on orchestration. In Staples’ telling, the new challenge is coordinating large numbers of agents operating simultaneously across repositories, pipelines, approvals, deployments, and enterprise policy systems.

> “Enterprises don’t need agent activity. They need running software that moves the business forward. Orchestration is the layer that gets you there.”

“Enterprises don’t need agent activity,” Staples notes. “They need running software that moves the business forward. Orchestration is the layer that gets you there.”

To support that shift, GitLab is rebuilding large parts of its underlying platform for what it describes as “machine-scale” requirements. Staples argues that existing developer infrastructure was largely designed around human-paced workflows — individual developers opening pull requests, triggering pipelines, and committing code at relatively predictable rates. AI agents change that dynamic entirely.

“Agents open merge requests in parallel, trigger pipelines around the clock, and push commits at a rate no human team ever did,” Staples writes.

GitLab has already been laying the foundation for this new direction, including its Duo Agent Platform, [which](https://ir.gitlab.com/news/news-details/2026/GitLab-Announces-the-General-Availability-of-GitLab-Duo-Agent-Platform/default.aspx) [launched in January](https://ir.gitlab.com/news/news-details/2026/GitLab-Announces-the-General-Availability-of-GitLab-Duo-Agent-Platform/default.aspx). Speaking to *The New Stack* in February, [Staples argued](https://thenewstack.io/gitlab-ceo-on-why-ai-isnt-helping-enterprise-ship-code-faster/) that coding was never really the bottleneck — developers spend only 10 to 20% of their day writing code, with the rest consumed by reviews, pipeline runs, security scans, and compliance checks. “That code being generated even faster just gets stuck in the queues that follow on the coding,” he said. The Duo Agent Platform is GitLab’s attempt to automate across that entire lifecycle, not just the coding part.”

## Leaning on its legacy

Among the company’s bigger bets are rebuilding GitLab into more API-first, composable services, developing agent-specific APIs, and redesigning orchestration systems capable of coordinating autonomous software agents across the full development lifecycle.

But GitLab also believes its biggest advantage in the AI era may come from something older and vaster: the amount of enterprise context already flowing through its platform.

> “Every dev tool vendor is converging on similar code generation capabilities. What doesn’t commoditize is the unique context the model gets to work with.”

“Every dev tool vendor is converging on similar code generation capabilities,” Staples writes. “What doesn’t commoditize is the unique context the model gets to work with: a data model that connects planning, code, review, security, deployment, and operations across every project and repository, accumulated over years of a team’s work.”

The argument is that while code generation models are converging across the industry, the organizational context is harder to reproduce. The company is effectively betting that agents operating inside GitLab’s existing ecosystem will make better decisions because they can draw from years of accumulated customer workflow data spanning repositories, CI/CD pipelines, deployments, approvals, and operational history.

That also helps explain why governance remains such a large part of the company’s positioning toward enterprise customers. Staples presents governance as the mechanism that allows companies to safely deploy larger numbers of autonomous agents inside production systems.

“Like a race car, it doesn’t matter how fast you can go if you can’t maintain control,” he writes.

The timing, though, is perhaps somewhat awkward for GitLab. The company originally emerged as one of GitHub’s most credible competitors before repositioning itself around the broader software lifecycle and enterprise DevOps tooling. Yet even as [frustration with GitHub has bubbled up](https://leaddev.com/software-quality/whats-gone-wrong-at-github) across parts of the developer community [in recent months](https://medium.com/@NMitchem/github-is-dying-and-developers-dont-even-know-it-yet-cca14b732ae5) — ranging from [reliability complaints](https://www.reddit.com/r/ExperiencedDevs/comments/1r0cytn/has_github_just_become_a_dumpster_fire/) to criticism of the platform’s direction under Microsoft — GitLab hasn’t emerged as a major beneficiary.

One likely reason is switching costs: teams deeply embedded in GitHub’s CI/CD workflows, integrations, and tooling don’t migrate easily, even if they’re frustrated. Ironically, that same dynamic — platform stickiness as a competitive moat — is precisely what GitLab is now betting on with its own enterprise customers in the AI era. As one community member on X [put it](https://x.com/tekbog/status/2053986174822457666): “*It’s crazy GitLab isn’t getting bigger during this GitHub fiasco era*.”

> “It’s crazy GitLab isn’t getting bigger during this GitHub fiasco era.”

## Jevons’ paradox, a recurring theme

Much of the traditional developer tooling market has historically depended on charging per developer seat. AI agents complicate that equation: they can do the work of many developers, but they don’t need seats.

If software can be produced at far greater volume and speed, it raises questions about how traditional developer tooling businesses capture value in that world. GitLab’s answer is that AI will increase overall software demand faster than it reduces the need for engineers — and that platforms capable of coordinating agents at machine speed will be worth more, not less, as a result.

It’s a [familiar argument in AI circles](https://www.npr.org/sections/planet-money/2025/02/04/g-s1-46018/ai-deepseek-economics-jevons-paradox), and one that has found vocal support among executives such as Box CEO Aaron Levie, [who has made a similar case](https://www.linkedin.com/pulse/jevons-paradox-knowledge-work-aaron-levie-qalmc/) that software demand will expand as production costs fall.

Blogger and open-source developer [Simon Willison](https://www.linkedin.com/in/simonwillison/) writes that “Jevons-paradox-inspired hope” for AI is largely consistent with his own thinking, though he cautions that GitLab’s position is also shaped by its business incentives — particularly at a moment when investors appear uncertain about how AI agents will affect the long-term economics of developer tooling companies.

“If your entire business depends on software engineering growing as a field and producing larger volumes of more lucrative seats, you have a strong incentive to believe that agents will have that effect,” Willison [writes](https://simonwillison.net/tags/jevons-paradox/).

For GitLab, the bet is that Jevons’ theory holds true for the agentic AI era — the alternative is too bleak to consider.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)