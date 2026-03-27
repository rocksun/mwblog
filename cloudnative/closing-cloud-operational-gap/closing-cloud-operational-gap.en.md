### Why the env zero and CloudQuery merger isn’t just a product story; It’s the thesis that the cloud operations market has been missing.

When I started CloudQuery, the problem seemed straightforward. Cloud infrastructure data was one of the most valuable and most ignored assets in any modern enterprise. Ask a platform team what they had deployed on Tuesday, and they genuinely couldn’t tell you—not because they were negligent, but because the tools they were using weren’t designed to answer that question.

So we built a normalized data layer: [SQL-queryable](https://www.cloudquery.io/docs/platform/features/sql-console?utm_source=TNS), multi-cloud, extensible. Enterprises at Fortune 100 banks and fast-moving fintechs started using it to finally get a coherent picture of what was running in their environments, across accounts, providers, and tools.

What I didn’t fully appreciate at the time was how quickly [cloud asset visibility](https://www.cloudquery.io/product/cloud-asset-inventory?utm_source=TNS) alone hits its limits. Knowing a resource exists doesn’t mean it’s governed. Knowing something is misconfigured doesn’t mean you can fix it safely, or that anyone with authority to act will see it before it becomes a problem. There’s a gap between what you can observe and what you can actually control. In most organizations, that gap is managed informally, by people writing glue scripts and relying on institutional memory.

That’s what I mean when I talk about the Operational Gap. And it’s the core reason [CloudQuery and env zero merged](https://www.env0.com/blog/env-zero-and-cloudquery-announce-merger-to-create-the-industrys-first-unified-cloud-intelligence-platform?utm_source=TNS).

## Platform engineering has always had a split-brain problem

The discipline has long been divided between Day 1 and Day 2 concerns. Day 1 is provisioning: getting infrastructure stood up safely, with the right policies, through [approved workflows](https://www.env0.com/solutions/standardized-workflows-across-teams-and-departments?utm_source=TNS). Day 2 is everything after: keeping environments compliant, catching drift, managing cost, and understanding what’s actually running versus what was intended. These two domains have historically lived in separate tooling, maintained by overlapping but distinct teams, with no shared data model connecting them.

> “The Operational Gap is the same gap it always was, but it’s compounding in a way that makes informal management untenable.”

The gap between them wasn’t zero before, but it was manageable. Teams wrote integrations. They built dashboards. They ran weekly reviews. The glue code held up, mostly because the pace of change was slow enough that humans could stay in the loop.

That’s no longer true. The acceleration in software development driven by large language models has changed the calculus. Infrastructure that used to take days to provision now takes minutes. The volume of changes moving through a cloud environment at a mid-to-large enterprise has outpaced any manual review process. The Operational Gap is the same gap it always was, but it’s compounding in a way that makes informal management untenable.

## Where env zero was strong, and where it wasn’t

Before the merger, env zero was best-in-class in governing infrastructure at the point of delivery. The policy enforcement, the approval workflows, the audit trails, and the drift detection — customers like Pismo went from two months to two days for infrastructure delivery. [Western Union moved from weeks to hours](https://www.env0.com/customers/western-union-scales-cloud-infrastructure-and-optimizes-costs?utm_source=TNS) across more than 200 applications. The core governance model was solid.

The ceiling was what happened next. Discovering an ungoverned resource and having authority over it are different things. Without a mechanism to make codification mandatory and without the ability to score risk beyond drift, discovered resources stayed discovered. Platform engineers could see the problem. They didn’t have the tooling to force the fix.

CloudQuery’s position was the inverse. We were very good at surfacing what existed across a cloud estate—normalized, queryable, contextualized across infrastructure, security, and cost data. What we didn’t have was a governed remediation path. Identifying a misconfiguration in a SQL query is useful. Having that finding flow into an approval workflow, with a full audit trail and a controlled remediation process, is a different capability entirely.

The combined [platform is designed](https://thenewstack.io/3-maxims-for-great-developer-platform-design/) to close that loop. env zero governs what gets deployed. CloudQuery provides continuous visibility into what actually exists and how it compares to declared intent. When they diverge, the platform has the context to act, not just to alert.

## Why governance is the right bet right now

I’ve watched platform teams chronically underinvest in governance tooling, and the reason is always the same: when governance works, nobody notices. The misconfiguration that didn’t cause an incident is invisible. The audit finding that didn’t materialize is invisible. The cost overrun that didn’t happen because a policy caught it at deploy time is invisible. The value is almost entirely in things that don’t occur.

That changes when AI-generated infrastructure enters the picture at scale. The volume of change becomes too high for informal controls. The blast radius of a single bad configuration gets larger as dependencies compound. The audit requirements from regulators and customers get stricter as cloud infrastructure becomes more operationally critical. At that point, governance stops being something organizations can manage through process and tribal knowledge, and has to become infrastructure itself—encoded, continuous, and automatic.

> “At that point, governance stops being something organizations can manage through process and tribal knowledge, and has to become infrastructure itself.”

The platform teams that have figured this out share a recognizable pattern. They’ve stopped treating governance as a checklist or a gate and started treating it as a layer that runs continuously under everything else. Developers don’t experience it as friction. Auditors see a complete, unambiguous record. The standards that the platform team defined once get applied consistently, whether a team is deploying to one environment or a hundred.

That’s the version of [cloud governance](https://thenewstack.io/3-steps-cloud-governance-steps-to-avoid-the-next-hack/) we’re building toward.

## What this means practically for existing customers

Both env zero and CloudQuery customers can expect their existing products to keep running. We made a deliberate decision not to collapse two platforms into one overnight and call it integration. The new combined product will have its own identity and its own roadmap, and it will be built to reflect the merged vision, not bolted together from the existing codebases.

The target customer is a [platform team](https://thenewstack.io/why-you-should-run-your-platform-team-like-a-product-team/) at a cloud-forward enterprise running production environments where the volume and velocity of infrastructure change has genuinely outpaced the ability to govern it manually. If that describes your situation — if you have significant infrastructure outside your IaC, if drift traceability is a persistent problem, if your compliance posture still depends on someone running a script and remembering to file a ticket — that’s who we’re building for.

The Operational Gap didn’t start with AI, but AI has made it the kind of problem organizations can no longer defer. The answer isn’t another point solution to add to the stack. It’s a platform that treats the full infrastructure lifecycle as a single governed system, with a complete record that doesn’t require anyone to maintain it manually. That’s what we’re building. We’re early in it, and we think we’re pointed at the right problem.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/03/bde90212-yevgenypats.jpg)

Yevgeny Pats is the CTO of env zero and co-founder & former CEO of CloudQuery and brings a decade of software engineering and startup expertise to the business. Prior to the formation of CloudQuery, Yevgeny founded other software businesses and...

Read more from Yevgeny Pats](https://thenewstack.io/author/yevgeny-pats/)