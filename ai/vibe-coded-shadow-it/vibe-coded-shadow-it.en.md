Shadow IT used to be a SaaS problem. Someone on the marketing team signed up for a tool, connected it to Google Workspace, and your first signal was an OAuth grant you didn’t authorize. Annoying. Detectable. Containable.

That era is over.

The new shadow IT doesn’t show up in your OAuth logs. It shows up as infrastructure running in your cloud account, built by a well-meaning engineer who asked an AI agent to stand it up in an afternoon. No ticket, no review, no security team involvement. Just someone with a good idea and a tool that removed all the friction that had slowed them down.

> “The new shadow IT doesn’t show up in your OAuth logs. It shows up as infrastructure running in your cloud account.”

That friction wasn’t just inefficiency. Some of it was doing real security work.

## The problem with good intent

Classic shadow IT had a whiff of someone knowingly going around IT. A team that didn’t want to wait for procurement. The security story was at least partially about policy enforcement.

That’s not what this is.

The engineer who vibe codes an internal tool for their team isn’t trying to circumvent anything; they’re trying to help. They have access to an AI agent that can write code, generate Pulumi programs, and stand up infrastructure faster than any review process can handle. And unless they’ve spent time thinking about cloud security, they have no reason to know that what they just shipped is a problem.

That’s what makes this harder: you can’t enforce your way out of it; you ***have*** to get ahead of it quickly.

Here’s what the bad day looks like: an engineer builds a lightweight internal app to automate something their team does manually. They ask the AI agent to handle the infrastructure. The agent provisions resources in the team’s AWS account, opens the necessary ports, and deploys the app. It works, and the team absolutely loves it. Nobody files a ticket because there’s nothing to file. Six weeks later, your CSPM flags a public-facing endpoint with an over-permissioned IAM role attached. By then the app has been running in production long enough that lateral movement is a realistic scenario, not a theoretical one.

The intent was good. The outcome has a blast radius.

## Why this is different from SaaS sprawl

When shadow IT meant unauthorized SaaS, your detection surface was defined. OAuth grants, network traffic, expense reports, SSO anomalies. The tool existed outside your infrastructure. It was external. You could find it, you could cut it off, and the damage was usually bounded.

> “This is the shift worth naming clearly: we’ve moved from SaaS sprawl to code sprawl.”

Agent-built internal tooling lives inside your infrastructure. It has IAM roles. It may have direct access to production data, internal APIs, or sensitive systems. It looks legitimate because it was built by a legitimate employee using legitimate tooling. There’s no obvious seam to detect at. The code doesn’t announce itself as ungoverned. It just runs.

This is the shift worth naming clearly: we’ve moved from SaaS sprawl to code sprawl. The detection playbook for one doesn’t translate to the other.

## A baseline worth actually using

The goal here isn’t to slow engineers down. It’s to make the safe path the easy path. The baseline we’re building toward at [Webflow](https://webflow.com/) has two layers, and that distinction matters.

**Platform controls** are things you configure once at the org or account level that make it structurally harder to do the wrong thing by accident.

*IAM least-privilege guardrails*. The permissions available to team-level AWS accounts should be scoped by default. An engineer shouldn’t be able to provision a public-facing resource with a broadly permissioned role without hitting a guardrail. The guardrail doesn’t stop the work. It stops the worst version of the work from shipping silently.

*Secrets manager enforcement.* Hardcoded credentials in vibe-coded apps are not a hypothetical. They’re a near-certainty if you don’t make the right path obvious. Enforcing secrets manager usage at the infrastructure level removes the decision entirely from the individual engineer.

> “The goal here isn’t to slow engineers down. It’s to make the safe path the easy path.”

*VPN-gated deployment targets.* Internal tooling should land behind your corporate VPN by default. If something genuinely needs to be public-facing, that should require an explicit decision, not an accidental default.

**Process controls** are what have to happen at the tool level before anything ships.

*Automated baseline check*. Before a security-informed human looks at anything, automatically run the [code and the infrastructure](https://thenewstack.io/spacelift-ai-infrastructure-code/) configuration against your baseline. Flag violations, tier them by severity, and give the engineer specific remediation guidance. This is the layer a Claude skill or similar tooling can own. The human review then focuses on what the automated check surfaced rather than starting from scratch.

*Security-informed code review with Security escalation*. Every internally built tool that touches production infrastructure needs a human with security context to look at it before it ships. For lower-risk tooling, that’s a peer engineer who understands the blast radius of what they’re reviewing. For anything with cloud infrastructure, direct data access, or novel IAM roles, it escalates to a formal Security review. Same control, tiered by risk. The key point is that the reviewer actually needs to understand the code. With vibe-coded tools, the author may not fully understand what they built. That [makes the review more important](https://thenewstack.io/move-code-review-upstream/), not a formality. It’s not just a quality gate. It’s a comprehension gate.

## The safety net

The baseline is preventive. Detection is what catches what slips through.

Your CSPM is the right tool for finding misconfigurations in what already exists. Wiz and tools like it will surface the public-facing endpoint, the over-permissioned role, the storage bucket without appropriate access controls.

But CSPM only finds what’s already deployed. The baseline and the review process are what you’re counting on to prevent that. Detection is the catch layer, not the first line.

The harder detection problem is knowing something exists in the first place. A vibe-coded tool running locally or in a team account may leave no trace in your normal visibility layer. No deployment pipeline. No change ticket. No asset inventory entry.

This is where behavioral signals in your cloud telemetry start to matter. IAM role creation outside your normal pipeline activity. New public-facing resources appearing without a corresponding change record. [API calls originating from developer](https://thenewstack.io/most-developers-call-ai-data-with-apis-and-a2a/) machines directly into production accounts rather than through your standard tooling. None of these signals are definitive on their own. In combination, they start to look like something that deserves a closer look.

Most teams aren’t looking for these signals specifically in the context of agent-built tooling. That’s the gap worth closing.

## The codified baseline

Documentation that lives in a wiki is a baseline that nobody uses when they need it. The better path is to make the baseline available within the tools engineers are already using, at the point of building.

A Claude skill or similar AI-native tooling that reviews architecture descriptions or generated infrastructure against your specific security baseline is more useful than a checklist in Confluence. The engineer gets specific, actionable feedback before a human reviewer ever sees it. The security team gets a first pass that’s already been filtered for the obvious failures. The review is better because it starts from a more complete picture.

None of this works if engineers don’t know the skill or if the review process doesn’t exist. Awareness is its own prevention layer. Introducing both during onboarding makes the safe path visible, and letting the skill’s feedback do double duty as education on why each check matters makes it stick. A guardrail that doesn’t announce itself isn’t preventive.

That’s where we’re headed internally. The blog post is the argument for why this matters. The skill is what operationalizes it.

## The takeaway

Vibe-coded internal tools are not going away. The friction that used to slow down ungoverned infrastructure is gone, and it’s not coming back. The question is whether your security baseline catches up before your CSPM does.

Platform controls make the safe path the default. Process controls make sure a human with security context sees everything before it ships. Detection gives you a catch layer for what slips through anyway.

> “Build the baseline before the CSPM finds it for you.”

None of this requires a dedicated AppSec team or a SOC. It requires a clear baseline, the tooling to enforce it, and engineers who understand what they’re reviewing. That’s a problem a small, well-structured security team can solve. Platform controls are owned at the org or SecEng level, set once and applied everywhere. Process controls are distributed: a peer engineer with security context handles lower-risk tooling, while anything touching cloud infrastructure, direct data access, or novel IAM escalates to a formal Security review. That’s distributed responsibility with a clear escalation path, not a single team reviewing everything.

Build the baseline before the CSPM finds it for you.

*This article was originally published on August 13, 2026, on* [*webflow.com*](https://webflow.com/blog/vibe-coded-apps-security-baseline)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/07/5f5aae47-andygombar.png)

Andy is a Staff Detection & Response Engineer at Webflow, where he founded and leads the detection and response program. With nearly six years at Webflow and a background spanning IT and military service, he brings a pragmatic, systems oriented...

Read more from Andy Gombar](https://thenewstack.io/author/andy-gombar/)