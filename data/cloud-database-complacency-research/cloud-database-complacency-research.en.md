A database is like a water heater. When all is well, it just does its job in the background. You don’t fantasize about replacing it or envy the one your friend just got. Really, you don’t even think about it — until something goes awry.

But new research reveals a key difference: With databases, the problems don’t blindside you. Some 38% of technology leaders worry that their current database won’t meet their needs in the near future. However, they aren’t acting on it. They wait until some compelling event (e.g., a production incident, usage spike, budget cut, or cloud strategy pivot) pushes the database to the top of the priority list.

That’s just one of the interesting findings from the [Futurum Group](https://futurumgroup.com/)’s latest research study, commissioned by ScyllaDB, which explores the latest trends in cloud database cost pressures, performance risks, and migration motivations. Respondents include technical decision-makers who shape cloud database strategy as well as team members directly responsible for the database.

![Responses to poll about level of influence of cloud database strategy](https://cdn.thenewstack.io/media/2026/04/29f1cb07-1-1024x576.png)

Guy Currier, Futurum Group Chief Analyst, summarizes the findings this way: “Those technology leaders expressed complacency with their cloud databases at the same time as concern and caution. This combination suggests that although they would prefer not to take immediate action, they know they will have to move when compelling events force a change.”

The full report, [*Is Cloud Database Complacency Affecting Your Business Objectives?*](https://lp.scylladb.com/report-techstrong-cloud-database-offer), is available now. Here are some key takeaways.

## Comfort masks concern

A third of the leaders surveyed report satisfaction with the performance of their current cloud databases. Yet, 38% worry that their database isn’t fit to support future AI/ML workloads and the resulting explosion in data volume.

The prime characteristic of these workloads is their unpredictability; past database performance is a poor indicator of future behavior as the technology evolves and as volumes increase. “Organizations experience what we might call ‘good enough for now’ syndrome,” Currier noted. “Their databases handle today’s workloads adequately, but leaders doubt these solutions will scale to meet tomorrow’s demands.”

> “Organizations experience what we might call ‘good enough for now’ syndrome. Their databases handle today’s workloads adequately, but leaders doubt these solutions will scale to meet tomorrow’s demands.”

![Chart showing opinions on the performance of cloud databases supporting organizational applications](https://cdn.thenewstack.io/media/2026/04/dd0141a5-2-1024x576.png)

Cloud database costs are also a major concern. The research found that 35% of leaders want to improve performance but feel constrained by budget. Another 35% are concerned about rising costs despite being satisfied with performance.

The top cloud database cost drivers include:

* Unexpected loads (40%)
* New or strict technical requirements (38%)
* Networking bandwidth growth (38%)
* Storage growth (38%)

![Poll results around the factors which have driven up database costs](https://cdn.thenewstack.io/media/2026/04/58fe80a1-3-1024x576.png)

## The 10% cost-savings tipping point

Nearly 40% of organizations are meeting their cloud database budgets, but just as many consider their predictable costs too high.

As Currier explains, “Organizations might tolerate high costs when they can plan for them. However, this tolerance creates an opening for solutions that can deliver similar predictability at lower price points.”

![Pie chart showing poll responses on costs associated with key cloud databases](https://cdn.thenewstack.io/media/2026/04/d5cfaa55-4-1024x576.png)

That opening is quite specific: A 10% cost reduction is all it would take for many tech leaders to consider migrating their cloud database. Why so low? Likely, the answer lies in scale. When database costs climb into the millions annually – which is not unusual for platforms like DynamoDB, according to the research – even a modest 10% translates to substantial savings.

## Event-driven database migration triggers

Still, technical leaders don’t proactively seek alternatives that are more cost-efficient or better prepared for the technical needs of current/future AI/ML workloads. They wait for trigger events that force them into a crisis-driven decision.

Leadership changes (36%) and major production incidents (32%) emerged as the primary catalysts. Other significant triggers include:

* Load spikes (32%)
* Cost reductions of 10% or more (31%)
* Maintenance burdens (31%)
* Performance issues (29%)
* Volatile costs (28%)

Most of these triggers highlight the reactive nature of these migrations, rather than proactive, strategic changes.

![Poll responses on factors most likely to cause respondents' organization to switch to/from cloud databases](https://cdn.thenewstack.io/media/2026/04/90f9d423-5-1024x576.png)

Note that *volatile* database costs drive 28% of switching decisions, suggesting that sheer unpredictability can be nearly as disruptive as high costs.

> “Database decisions are rarely made in a vacuum. Even when teams identify performance or cost inefficiencies, acting on them competes with feature delivery, roadmap commitments, limited operational bandwidth, and against their familiar tech stack.”

“Database decisions are rarely made in a vacuum,” the research report notes. “Even when teams identify performance or cost inefficiencies, acting on them competes with feature delivery, roadmap commitments, limited operational bandwidth, and against their familiar tech stack.”

## Early warning signs

While water heater issues tend to surface without warning, database issues can usually be anticipated. There are several early warning signs that a database is starting to become a constraint:

* **Cost is growing faster than throughput.** When database spend rises faster than the throughput it’s handling, the system may not be as scalable as it appears. Teams patch their way forward (e.g., with caches) to sustain performance. But the [cost per query keeps](https://thenewstack.io/why-kubernetes-cost-optimization-keeps-failing/) climbing.
* **Rising tail latency. When P95 or [P99 latency](https://thenewstack.io/if-p99-latency-is-bs-whats-the-alternative/)** starts to climb during peak periods or background operations, it indicates the system is nearing its breaking point. These changes might be dismissed if they don’t immediately violate SLAs, but they’re canaries in the coal mine.
* **Increasing operational friction.** More manual tuning, more frequent capacity adjustments, more time spent managing the database to maintain the same level of performance…all these signal diminishing returns from the current architecture.
* **Disproportionate complexity for organic growth.** When routine [scaling or new workload](https://thenewstack.io/kubernetes-vpa-inplace-resize/) support requires outsized engineering effort, it’s a sign that the database has become a constraint rather than an enabler.

## From reactive to strategic

Recognizing these signals is one thing, but actually acting on them before a crisis forces your hand is another. Some due diligence now will help you stay ahead of it.

* Get a general sense of what options are available for your use cases
* Define vendor-neutral evaluation criteria
* Stress test your existing database to understand its breaking point – before production traffic exposes it for you
* Set clear decision triggers (e.g., specific performance thresholds, cost targets, and capability gaps)
* Map your database capabilities against your 12–24 month strategic roadmap, not just your current workloads

As Currier concludes: “Your database might be ‘good enough for now,’ but if that isn’t aligned with where your business needs to go, complacency is already costing you.”

Download [the full report here](https://lp.scylladb.com/report-techstrong-cloud-database-offer); you’ll also get access to an expert panel discussing the research findings.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/01/14adf317-cynthiadunlop.jpeg)

Cynthia Dunlop has been writing about software development and testing for much longer than she cares to admit. She's currently senior director of content strategy at ScyllaDB.

Read more from Cynthia Dunlop](https://thenewstack.io/author/cynthiadunlop/)