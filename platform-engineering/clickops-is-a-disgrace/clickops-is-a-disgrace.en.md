ClickOps is a disgrace. As a community, we should ban it. And that should be obvious to anyone who’s serious about cloud infrastructure.

Today, [data shows](https://www.firefly.ai/state-of-iac-2025) that 89% of organizations claim they’ve adopted [Infrastructure as Code (IaC)](https://thenewstack.io/introduction-to-infrastructure-as-code/), according to Firefly’s 2025 “State of Infrastructure as Code” report, but only 6% have achieved complete cloud codification. That math is brutal. It tells us that the majority of companies are embracing IaC and *believe* that they’re IaC-mature organizations, yet are still systematically using [ClickOps](https://thenewstack.io/iac-is-too-complicated-wheres-that-easy-button/) — using the cloud console/graphical interfaces instead of the command line for infrastructure management.

By and large, as cloud practitioners, we’ve normalized professional malpractice. *And it’s about to get much worse.*

## The ‘Emergency’ Rationalization

One reason why ClickOps is everywhere: every ClickOps action gets labeled as “urgent.”

Teams have perfected the art of justifying manual console changes as necessary exceptions. But when the majority of organizations are making these exceptions, they’re not exactly exceptions anymore. They’re just standard operating procedure.

The pattern is predictable:

* Label every console change as “urgent.”
* Use emergency protocols for routine changes.
* Abandon remediation work when the immediate pressure dies down.
* Repeat until ClickOps becomes standard practice.

Many treat console changes as a hot fix, and as such, they’re obliged to, at some point, go back and architect those changes correctly. But the critical word here is “obliged” — because most teams never follow through.

The hypocrisy is loud. Engineering teams demand code reviews for application changes, but then click their way through infrastructure modifications that can bring down entire environments.

The truth we don’t want to face? We stopped SSHing into Linux machines for a reason. [We should stop ClickOps](https://www.firefly.ai/blog/stop-clickops-3-steps-to-clean-up-your-cloud).

## The Staging Environment Myth We Still Believe

Teams justify ClickOps in non-production environments as necessary for agility, creating systematic drift between environments that almost guarantees production failures.

Ever found yourself saying, “Everything worked on my machine. Everything worked in staging, then we deployed to production, and suddenly — massive downtime”? It’s an issue practitioners come across more often than they’d like to admit. And often, the root cause is that production was governed by IaC, while staging remained a ClickOps free-for-all.

Reality check: The staging environment excuse isn’t pragmatism. It’s [engineering negligence](https://thenewstack.io/why-most-iac-strategies-still-fail-and-how-to-fix-them) masquerading as flexibility.

## The Cost of ClickOps-Driven Infrastructure Debt

ClickOps creates ghost infrastructure that haunts organizations for years.

Imagine: three years of unnecessary cloud spend because someone clicked a button and walked away. This isn’t an edge case. It’s the predictable outcome of treating infrastructure like it’s a debugging session instead of an engineering discipline.

And for companies like Figma, the design tool company whose initial public offering recently revealed a massive [$300,000 a day](https://www.datacenterdynamics.com/en/news/design-platform-figma-spends-300000-on-aws-daily/) cloud bill, unnecessary spending can quickly add up and cost you millions.

> The staging environment excuse isn’t pragmatism. It’s engineering negligence masquerading as flexibility.

On top of the mounting costs, what’s worse is the compounding knowledge debt. Engineers spin up environments that sit around for years, and their successors leave them untouched, lacking the courage to delete them. In those scenarios, ClickOps doesn’t just create technical debt. It creates organizational paralysis.

## The Config Drift Epidemic, Explained

Despite increasing IaC adoption, configuration drift is getting worse. The 2025 “State of Infrastructure as Code” report shows:

* Less than one-third of organizations proactively monitor drift.
* 17% have no drift detection process at all.
* Only 8% have automated drift management tooling in place.
* 40**%** of teams report drift takes days to weeks to remediate.

The root cause is obvious**:** Partial IaC adoption mixed with systematic ClickOps basically guarantees configuration divergence. This isn’t a tooling problem. It’s a discipline problem.

And the window for fixing these practices is closing quickly.

## Multiplying the Problem: Multicloud Complexity and AI

The challenge of maintaining a secure, immutable, resilient cloud intensifies in multicloud, multi-IaC environments. Today:

* 68% of organizations operate across multiple clouds.
* 57% use multiple IaC frameworks.

Different teams are using different tools, all making manual changes to interconnected resources. And that’s hard enough as it is.

But two years from now, it will be impossible to address these issues the way we can now. When we get to a place where AI agents run the cloud for us, if cloud teams don’t have a very ordered system of record and the right guardrails codified for them, they will wreak havoc. So, unsurprisingly, having a game plan as soon as possible is mission-critical.

## The Professional Gold Standard: Cloud as Code

Real emergency procedures require immediate remediation plans. When it’s 2 a.m. on a Friday night, your site reliability engineer is out of the office and you’re facing imminent downtime, manual intervention might be necessary.

But the best and most agile cloud teams:

* Track emergency interventions.
* Require immediate codification.
* Treat emergency ClickOps as technical debt that demands urgent attention.
* Reject the comfortable lie that ClickOps is an acceptable engineering practice.

And as the state of the industry continues to shift, unnecessary ClickOps activity needs to fade away to make room for more sustainable, risk-free and scalable ways of managing cloud environments.

*To learn more, download the complete “[2025 State of Infrastructure as Code” report](https://www.firefly.ai/state-of-iac-2025) and explore how ClickOps is having an impact on teams’ processes, efficiency and outlook.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/07/fbe4d2bb-idoneeman600x600-600x600.png)

Ido Neeman is CEO and co-founder of Firefly, and the former CEO and co-founder of Nuweba, the fast and secure serverless platform. To the diversity of roles he has held, he brings more than a decade's experience in the elite...

Read more from Ido Neeman](https://thenewstack.io/author/ido-neeman/)