For a long time, logs lived in a strange purgatory: technically required, rarely read, and mostly forgotten until something broke.

The typical pattern looked like this: engineering teams would wire up logging because it was considered good practice, or because an auditor had it on a checklist. The logs got generated. They went somewhere — an S3 bucket, a Security Information and Event Management (SIEM) system, a flat file on a server — and then nobody looked at them. Not because teams were negligent, but because the logs weren’t built to be looked at. They were a dump. A timestamp and an event ID and a string of metadata that required real forensic patience to make sense of.

The only time anyone went digging was after an incident. And that’s exactly when you’d discover the gap: “We’re not logging what we should have been logging.” By then, it’s already too late. The attacker has moved, the blast radius is unclear, and your investigation is running on incomplete evidence.

> “The question now isn’t whether you’re generating logs; it’s whether your logs can actually tell you something when it counts.”

That world is gone. The question now isn’t whether you’re generating logs; it’s whether your logs can actually tell you something when it counts.

## The pressure didn’t come from one direction

The shift didn’t come from a single regulation or a single breach. It came from pressure building on multiple fronts simultaneously.

Regulatory frameworks started demanding demonstrable evidence, not just assertions. The SEC’s disclosure rules changed how public companies talk about security incidents. The NIS2 Directive (EU 2022/2555) raised the bar across critical infrastructure in Europe. Auditors who once accepted a screenshot of a logging policy now want to see the logs themselves, queryable and timestamped and tied to specific events.

At the same time, developers and product teams started asking harder questions about the tools they were building on. Security awareness inside engineering organizations has matured.

Teams evaluating new vendors now include security-minded engineers who want to know not just whether a product is SOC 2-certified, but also what the security logging actually looks like under the hood. Enterprise procurement followed the same pattern. Security review questionnaires got longer. Legal and compliance teams started pulling audit log samples during vendor evaluations.

A product that couldn’t produce a clean, exportable activity log was starting to lose deals it would have won two years earlier.

And then there’s the AI-powered attacker. Adversaries are moving faster than ever, and catching them in real time is increasingly difficult. What logs give you is the next best thing: a record of how they moved, what they touched, and what the attack pattern looked like. That record becomes the foundation for designing better defenses against the next one.

AI agents are already provisioning resources, making purchases, modifying account settings, and deleting data inside production environments. [Gartner projects](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) that 33% of enterprise software applications will include agentic AI by 2028, up from less than 1% in 2024. By that same year, 15% of day-to-day work decisions will be made autonomously through AI agents.

Every one of those autonomous actions is a candidate audit log entry that did not exist a year ago. The logging question is no longer just about what humans did. It now includes what agents did, who authorized them, and whether the action was within scope.

The data backs up what security teams have been feeling. [Verizon’s 2026 Data Breach Investigations Report](https://www.verizon.com/business/resources/T161/reports/2026-dbir-data-breach-investigations-report.pdf) analyzed over 22,000 confirmed breaches and found that exploitation of vulnerabilities now accounts for 31% of all initial access, overtaking credential abuse for the first time in the report’s 19-year history. Third-party involvement in breaches jumped 60% year over year, reaching 48% of all breaches.

When initial access moves that fast and spans that many external relationships, the logging infrastructure is what determines whether you can reconstruct what happened after the fact. Roughly one in three breaches starts with a vulnerability exploited before most teams can patch it, and the ones that are identified can take an average of eight months to remediate. Logging is the difference between a postmortem and a guess.

## The difference between a log and a record

Not all logging is equal, and that distinction matters more than most teams realize until they’re sitting in front of an auditor or an active incident.

Surface-level logging captures that something happened. A real audit trail captures the full context around it: who took the action, what exactly changed, when it happened, where the request originated from, and what the state of the system looked like before and after.

That difference between an event notification and a complete activity record is the difference between a log that confirms something occurred and a log that can actually reconstruct what happened.

That bar gets higher when the actor is not a human. In a human-only environment, investigators can sometimes reconstruct intent from surrounding behavior. With an [AI agent acting autonomously](https://thenewstack.io/ai-agents-database-challenge/), none of that ambient context exists. The audit trail is the only source of truth. A complete activity record in an agentic world means capturing not just the action, but the agent identity, the authorization chain that initiated it, and the scope boundaries that were supposed to constrain it.

> “In a human-only environment, investigators can sometimes reconstruct intent from surrounding behavior. With an AI agent acting autonomously, none of that ambient context exists.”

SOC 2 makes this concrete. Across several of its Common Criteria, SOC 2 Type II requires evidence that access to systems is logged, that changes to data and configurations are tracked, and that those records are tamper-evident and retained over time. A log that simply records “user logged in” doesn’t satisfy that. A log that captures the user, timestamp, IP address, session ID, and whether the authentication method was standard or elevated is getting there.

The practical test is simple: If an incident happened six months ago, could your logs reconstruct the [sequence of events](https://thenewstack.io/understanding-log-events-why-context-is-key/) clearly enough to brief a board, respond to a regulator, or hand it off to a forensic investigator? If the answer is uncertain, the logs aren’t operational yet.

Actionable security logging has a few non-negotiables. Logs need to be immutable so they can be trusted as evidence. They need to be structured so they can be queried, not just read. They need to capture the right events, which means user actions, system changes, access grants and revocations, and configuration modifications, not just authentication events.

Retention is another critical consideration. For some tools, 30 days of hot storage may be reasonable, but depending on the use case, 6 months of context might be what an investigation actually requires. Not all platforms handle this the same way. Some offer [tiered retention with cold storage](https://thenewstack.io/store-more-pay-less-welcome-to-kafka-tiered-storage/) archives. Others require a support ticket just to access logs older than the default window. The easier it is to retrieve historical logs, the more credible your tool becomes during incidents and investigations, and the better the experience for the security teams relying on it.

![Infographic showing the differences between a bad log and a good log.](https://cdn.thenewstack.io/media/2026/06/b8a2a7bb-image1-1024x576.png)

*The gap between logging something and logging the right things is where most teams find themselves when it matters most.*

## Your logging infrastructure is now a revenue asset

A well-instrumented audit trail used to be an internal asset. It lived in a SIEM, it served the security team, and it surfaced during audits. Now it’s showing up in sales cycles. Enterprise buyers are asking for it during procurement. Legal teams are reviewing it before contracts get signed. And trust centers that surface clean, structured security content are being indexed by AI-powered procurement tools that summarize vendor risk before a human even gets involved.

That puts security teams in an interesting position. The work they’ve been doing quietly for years, building reliable logging, maintaining tamper-evident records, structuring events in a way that’s actually queryable, is now directly connected to revenue. A buyer who can see a clean audit trail moves faster through the procurement process. A deal that might have stalled at the security review stage closes because the evidence was already there, accessible and credible.

The [Storm-0558 incident](https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf) in 2023 made this concrete at the highest stakes possible. A China-linked group used a stolen Microsoft signing key to forge tokens and access mailboxes belonging to U.S. State Department and Department of Commerce officials. Roughly 60,000 unclassified emails were exfiltrated.

The State Department detected the intrusion because it had paid for a higher tier of Microsoft Purview Audit logging that included mailbox access events. Other affected agencies on lower tiers did not have that visibility. After pressure from CISA and the U.S. Cyber Safety Review Board, [Microsoft made the relevant audit logs](http://bleepingcomputer.com/news/security/microsoft-extends-purview-audit-log-retention-after-july-breach) available to all customers, regardless of license tier, within months. The lesson generalized quickly across the industry. ***Logging is not a premium feature.***

This is the competitive differentiator that doesn’t get talked about enough. Sales teams can’t manufacture trust in a security review. They can only surface what’s already been built. Security teams that instrument audit trails well are handing sales something real to work with.

> “Sales teams can’t manufacture trust in a security review. They can only surface what’s already been built.”

The opportunity isn’t just about closing deals faster either. It’s about showing up differently in a market where most vendors still treat logging as an internal function. Enterprise buyers running AI-assisted workflows already need to answer their own boards and regulators when something goes sideways.

If a product in their stack can’t produce a clean record of what an agent did and who authorized it, that product becomes the weak link in their compliance story. Transparent, accessible audit trails signal maturity. They signal that a team has thought about accountability in a world where the actors are not always human. And in enterprise sales, that signal travels.

## Logging as a product, not a process

There’s a version of audit logging that operates entirely behind the scenes, and another that becomes part of your product. The gap between those two is smaller than most teams think, and the payoff for crossing it is significant.

The shift looks like this: instead of “we have logs, and we can send them to you if you need them,” it becomes “here are your logs, right inside the product, available whenever you need them.” That change in posture is what separates a compliance artifact from a product feature.

In practice, this means surfacing user activity logs directly in the product dashboard. It means giving account administrators a view of every action taken in their workspace, who made a change, what they changed, and when it happened. It means making those logs exportable, in formats that a customer’s own security team can ingest into their SIEM or hand off to an auditor without needing to file a support ticket first.

The support angle is underrated. A significant portion of “what happened to my account” tickets disappear when customers can answer that question themselves. Giving users visibility into their own activity history reduces friction, builds confidence, and quietly removes a whole category of escalations from your support queue.

![Example screenshot of an annotated event on Webflow.](https://cdn.thenewstack.io/media/2026/06/ed1d8350-image2-576x1024.png)

[Webflow](https://webflow.com/) is a good example of this done well, utilizing a [two-tiered logging approach](https://webflow.com/webflow-way/collaboration/monitoring-and-troubleshooting) that treats visibility as both a user experience and a security requirement. At the Enterprise tier, site-level activity is surfaced directly in the Designer via the [Site Activity log](https://help.webflow.com/hc/en-us/articles/33961371582995-Site-Activity-log), empowering teams to troubleshoot in real time. Every class change, component edit, CMS update, custom code modification, and publish event is logged with author, timestamp, and branch, and old entries are never rewritten when something downstream changes. This in-product visibility transforms the audit trail from a back-office compliance tax into a collaborative tool for site governance.

For high-stakes security and compliance needs, a separate [Workspace audit log API](https://help.webflow.com/hc/en-us/articles/46651794799891-Workspace-audit-log-API) exposes the granular, [security-relevant events](https://developers.webflow.com/data/reference/enterprise/workspace-audit-logs/event-types) that matter for incident response. This includes logins, access grants, permission and role changes, invitation flows, and Workspace setting changes. It was designed from the start [to flow into enterprise logging platforms](https://webflow.com/updates/audit-log-api), with one-year retention and AES-256 encryption at rest. By bifurcating these capabilities, Webflow ensures that logging supports the developer’s daily workflow while also meeting the rigorous demands of security investigators. That’s the model. Logging stops being something that happens to your product and becomes a competitive differentiator your product offers.

> “Logging stops being something that happens to your product and becomes a competitive differentiator your product offers.”

That architecture reflects a problem every security team is about to run into: how do you distinguish human action from AI-assisted action within the same audit trail?

As AI features get embedded in content workflows, generating copy, suggesting design changes, modifying CMS entries, the activity log has to answer a question it was never built to answer. Was this a person, or was this AI? Webflow’s Site Activity Log now surfaces AI attribution directly alongside human edits. Users can see not just what changed and when, but whether a human or an AI agent initiated the change. That is not a marginal improvement to logging. It is a structural change to what accountability means in a product where AI is a first-class actor.

The authorization layer completes the picture. Knowing that an AI agent took an action is only useful if you also know what permissions made that action possible, and whether those permissions matched the agent’s intended scope. This is where access control and audit logging converge. The Workspace Audit Log captures role changes and permission grants. That means you can reconstruct not just what happened, but what was enabled. For enterprise customers already fielding questions from boards and regulators about AI governance, that complete chain of evidence is what separates a vendor in the stack from a liability in the stack.

As the agentic layer grows, this kind of instrumented visibility — who acted, what they were permitted to do, whether the actor was human or AI — is what keeps a product in the stack. That is not a compliance story. That is the product story.

This article was o*riginally published on June 4, 2026, on* [*webflow.com*](https://webflow.com/blog/audit-trails-not-a-compliance-tax)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/59664e90-cropped-81692684-mohit-headshot-copy-scaled-1-600x600.jpg)

Mohit Bansal is a Senior Security Engineering Leader at Webflow, where he leads programs across security operations. With 12+ years of security engineering experience across startups and larger enterprises, he specializes in scaling security programs and supply chain defenses for...

Read more from Mohit Bansal](https://thenewstack.io/author/mohit-bansal/)