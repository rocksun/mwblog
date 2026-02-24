Somewhere in the organization, there’s a Jenkins job that nobody wants to touch. The job is mission-critical and deploys to production every Thursday. It was written three years ago by someone who’s since left, references environment variables that may or may not still exist, and the only documentation is a Slack message that reads “Just run it. It works.”

This is automation sprawl, and it’s quietly bleeding the organization’s engineering velocity dry.

## The hidden costs nobody tracks

The thing that doesn’t show up in the infrastructure bill is the cognitive load of remembering which automation lives where. The thirty minutes it may take to figure out why the same job works in Jenkins, but fails in [GitHub Actions](https://thenewstack.io/how-to-use-github-actions-and-apis-to-surface-important-data/). The subtle drift between environments occurs because two different tools are managing overlapping resources. Teams may find [senior engineers](https://thenewstack.io/4-north-star-metrics-for-platform-engineering-teams/) spending 20% of their time simply maintaining automation and keeping existing pipelines functional, rather than building new capabilities.

That’s not velocity. That’s running to stand still.

> Teams may find senior engineers spending 20% of their time simply maintaining automation and keeping existing pipelines functional… That’s not velocity. That’s running to stand still.”

While everyone is focused on cloud spend, the real costs start to surface through the meetings to coordinate changes across platforms, the incident response, where three teams need to be on a call because nobody knows which automation modified what, and the security review that takes a month, after all, auditors need to understand five different permission models.

## What consolidation actually looks like

Successful consolidation efforts share common traits.

The smart teams start with an inventory. It’s not a spreadsheet that goes stale in a month, but an actual, maintained, living catalog of what automation exists, who owns it, and what it does. Teams can’t consolidate what they can’t see.

They establish patterns before platforms. The question isn’t “Should we use Tool X or Tool Y?” It’s “What are the three or four automation patterns we actually need, and what’s the simplest way to implement each?” Most organizations need scheduled jobs, event-triggered workflows, human-initiated runbooks, and deployment pipelines. Everything else is probably a special case that should justify its own existence.

These teams accept that migration is a longer-term strategy. The sprawl didn’t happen overnight, and it won’t be fixed overnight. The goal is to stop adding to the problem while gradually reducing the existing footprint.

## The operations-as-code evolution

With operations-as-code, teams can transition from patterns to templates. These templates serve as foundations for extending applications and for [infrastructure-as-code (IaC)](https://thenewstack.io/introduction-to-infrastructure-as-code/). The same principles that drove IaC — version control, repeatability, peer review — are now being applied to operations themselves. Not just in a manner of “How do we deploy this service?” but “How do we respond to this alert?” and “How do we onboard a new database?”

The teams doing this well aren’t treating runbooks as documentation that might be out of date, but as executable code that self-documents through its implementation. When the steps change, the automation changes. When the automation runs, it generates an audit trail.

This also matters beyond efficiency. When operational knowledge lives in people’s heads (or worse, in undocumented scripts on someone’s laptop), the organization is one resignation away from an outage.

## Practical steps forward

For organizations looking to get past this trap, here’s where to start:

**Audit before acting.** Spend a week cataloging. Talk to team leads to find out what happens when X breaks, which scripts they use, and what happens if the person who usually runs the scripts isn’t there. Grep repos for pipeline definitions. Teams may find automation they didn’t know existed, as well as automation that nobody uses anymore, but everyone’s afraid to delete

**Define ownership explicitly.** Every piece of automation should have an owner who knows they’re the owner and is tagged to a service where appropriate. The number of orphaned pipelines in most organizations suggests this isn’t as obvious as it sounds. Teams can move, but services generally don’t.

**Create a decision framework.** When someone needs new automation, where should it live? Write down the criteria, such as “If it’s CI/CD, use X. If it’s scheduled operations, use Y. If it’s incident response, use Z.” Make the default path obvious and consider creating a GitHub repo to store these artifacts.

**Measure the tax.** Track time spent maintaining existing automation separately from time building new capabilities. If maintenance consistently accounts for more than 30% of automation-related work, the organization has a consolidation problem.

## Bringing it together

The pattern that works isn’t about finding one tool to rule them all. It’s about establishing clear boundaries for what goes where.

CI/CD pipelines belong in the CI/CD system. Infrastructure provisioning belongs in [Terraform](https://thenewstack.io/how-to-scale-your-terraform-infrastructure/), Pulumi, or whatever tool the team has standardized on. But the middle layer, which includes scheduled maintenance tasks, incident response procedures, and the ad-hoc operational work that currently lives in 20 different places, is where consolidation pays off the fastest.

This is the space where runbook automation platforms like Rundeck have carved out a niche. It’s not about replacing existing tools, but providing a unified control plane for operational work. The jobs orchestrate across the organization’s infrastructure rather than duplicating it. Access controls let teams delegate execution without handing out SSH keys. Audit trails give the compliance story that scattered scripts never will.

Other tools play in this space, too. Ansible Automation Platform, various Kubernetes operators, and even well-structured GitHub Actions with proper OpenID Connect (OIDC). Operational automation deserves the same rigor as application code, which means consolidating it so teams can actually manage it.

## The uncomfortable truth

Automation sprawl persists because it’s locally optimal. Each team, solving its immediate problem with the tools they know, is making a reasonable choice. The sprawl emerges from reasonable choices compounding over time.

> “Automation sprawl persists because it’s locally optimal… The sprawl emerges from reasonable choices compounding over time.”

Fixing it requires thinking at a different level. It’s not just about choosing the best tool for the job, but also about selecting the best tool ecosystem for the organization over the next five years. It’s a harder question to answer, and one that requires the sort of buy-in most individual contributors can’t secure on their own.

However, the alternative is technical debt that doesn’t look like technical debt and appears to be business as usual. That is, until someone leaves, or an audit happens, or an incident exposes just how fragile the foundation really is.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/29ea1536-cropped-4c11b5d2-justyn-roberts-headshot-scaled-1-600x600.jpg)

Justyn Roberts is a Principal Solutions Consultant for Automation at PagerDuty, where he helps enterprises untangle automation sprawl and build sustainable operational practices.

Read more from Justyn Roberts](https://thenewstack.io/author/justyn-roberts/)