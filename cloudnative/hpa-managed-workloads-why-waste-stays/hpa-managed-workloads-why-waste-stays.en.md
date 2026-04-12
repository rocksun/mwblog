Teams running Kubernetes can usually see where they’re overprovisioned. Requests are higher than they need to be, there’s consistent headroom, and capacity sits underused.

This has been true for a while, but it is showing up more often now as more teams run burstier model-serving workloads on Kubernetes and start feeling the cost of overprovisioning more directly.

But those workloads don’t get touched.

This shows up most with HPA-managed services. The inefficiency is obvious; as the HPA scales, the waste scales with it. What’s less obvious is what happens when you change it.

These workloads already scale under real production traffic. Teams have watched how they behave during spikes, launches, and incidents. That history builds trust. And once that trust is there, inefficiency is easier to live with than unpredictability.

The biggest problem with most optimization approaches isn’t the math. It’s that they treat this as a math problem. Teams aren’t optimizing for average utilization. They’re optimizing for resilience during the worst five minutes of the quarter. Any approach that doesn’t understand that distinction is solving the wrong problem.

## **The problem isn’t finding the waste**

Most teams can spot overprovisioned workloads in minutes. I bet you every organization out there has at least a Grafana dashboard showing the stark difference between capacity allocated and capacity used. The harder question is what happens after a change gets applied.

For HPA-managed workloads, requests aren’t just a sizing input. They shape scaling behavior. HPA decisions depend on utilization ratios, so when requests change, those ratios change too. That shifts when scaling kicks in and how aggressively replicas increase.

This is what makes resource changes feel fundamentally different from code deploys. A bad deploy has a known rollback path. A bad resource change is more subtle. It shifts an invisible contract between the workload and the scheduler, and the failure mode might not surface until Friday afternoon when traffic spikes hit a threshold that didn’t exist at the old request values. By then, three other things have changed too, and proving causation is nearly impossible.

Changing requests isn’t a resource adjustment. It’s a change to how the workload scales. That’s what makes teams nervous.

## **What teams are actually protecting**

In most cases, this isn’t inertia or ignorance. It’s a deliberate choice. Teams are preserving behavior that already works:

* Predictable scale-out during spikes
* Stable latency under real traffic
* Known behavior during releases and incidents
* The ability to explain what the service will do when demand moves

Once things seem to be “working”, any change that could shift its scaling behavior looks risky. Most teams would rather tolerate the waste than introduce a new variable into a service they already depend on.

And it’s worth being honest about why: the people who set those resource values are the same people who get paged at 2am if something breaks. The risk isn’t abstract. A suggestion to downsize might be technically correct, but if it touches a service owned by a team that had an incident six months ago, that team isn’t changing anything. The savings opportunity doesn’t outweigh the personal accountability.

## **Why standard rightsizing stops here**

Most rightsizing workflows assume a simple loop: adjust requests, watch what happens, iterate. That works for stable services where changing requests doesn’t also change scaling behavior.

It breaks with HPA-managed workloads, where requests and scaling are coupled. That gets even harder with model-serving workloads, where traffic can move fast and the cost of carrying extra headroom is unusually visible.

The failure mode is especially dangerous because it’s not immediate. A service can show low average usage all week and then hit a traffic spike where the headroom that looked wasteful turns out to be the reason it stayed stable. Automation that trims too close to the line based on recent averages doesn’t account for business context: product launches, seasonal spikes, marketing events, or end-of-quarter surges that aren’t in the last two weeks of data.

That’s why these workloads sit outside routine rightsizing efforts even when the waste is obvious.

## **What would need to be true for teams to act**

If teams are going to optimize here, preserving existing scaling behavior is the bar. Changing requests can’t quietly change when the workload scales or how aggressively it responds.

The approach that works is treating requests and HPA targets as a coupled pair. Adjust both atomically, and the workload’s behavior under load stays intact even as the resource footprint shrinks.

But even the right technical approach isn’t enough on its own. Teams need to see the reasoning behind each change, not just the recommendation. They need guardrails that respect the same SLOs they’re held accountable to. And they need a path that starts with visibility, moves to approved recommendations, and only graduates to automation after trust has been earned. Flipping straight to full autonomy doesn’t build confidence. It skips the part where confidence gets built.

That trust curve shows up in the broader Kubernetes market too. In CloudBolt’s recent research on the [Kubernetes automation trust gap](https://www.cloudbolt.io/industry-research/cii-kubernetes-automation-trust-gap/), teams consistently reported that visibility and recommendations are much easier to adopt than autonomous execution.

Teams also need rollback to be straightforward. Not “file a ticket and wait.” Automatic, fast, and triggered by the same health signals the team already trusts.

Without all of that, the default answer stays simple: leave it alone.

**The most expensive inefficiencies sit inside the workloads no one feels safe changing.**

[![CloudBolt](https://cdn.thenewstack.io/media/2026/02/85d0c929-cdb-logo-dark.svg)](https://www.cloudbolt.io/solutions/kubernetes-rightsizing/?utm_content=contributor+module)

CloudBolt helps platform teams turn Kubernetes optimization insights into safe, trusted action—with the guardrails, visibility, and control needed to operate confidently in production.

Hear more from CloudBolt

Submit

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/03/ef632ec9-cropped-6af8874c-7xl80xrcanikrplucbevvxfkjuymwyrfsehjbhuxqui-600x600.png)

Yasmin Rajabi is the Chief Operating Officer at CloudBolt Software. She is a recognized leader in the FinOps and Kubernetes communities, and her background as an engineer, product leader, and operator gives her a holistic perspective on the challenges facing...

Read more from Yasmin Rajabi](https://thenewstack.io/author/yasmin-rajabi/)