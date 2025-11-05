Observability platforms often require highly skilled practitioners to make sense and use of those platforms. Ideally, a non-technical stakeholder would rely on monitoring, understanding problems or optimizations to make and then rely on the platform to do the rest of the work. For debugging, an AI-guided problem solver detects, updates and fixes the issue, and articulates the situation in such a way that the non-technical user can understand it.

It’s up to observability providers to offer seamless metrics that can be used to solve business goals — and thwart business disasters, [Bill Hineline,](https://www.linkedin.com/in/billhineline) field CTO for [Chronosphere](https://chronosphere.io/?utm_content=inline+mention), told me recently. No news flash there, but the need to simplify observability without dumbing it down cannot be emphasized enough.

But he also said it’s up to the non-technical stakeholders to get up to speed on how to interpret these metrics. *That’s* a refreshing take.

Another refreshing take: Defining [service-level objectives (SLOs)](https://thenewstack.io/sre-fundamentals-differences-between-sli-vs-slo-vs-sla/), often the last step in an observability strategy, should be the first.

Widespread adoption of observability tools are impossible if the tools are overly complex, yet many vendors forget that. Observability providers talk about additive features they’re offering to metrics, logs and traces, assuming that the actual users or potential adopters know what they’re talking about, which is not always the case.

Even at a CTO level, users might struggle to understand how their platforms work and how to interpret the data — and those are often the folks who approve the spending on tooling, not only for developers and operations engineers, but for all of their organization’s stakeholders.

Observability providers will often say, “We have a new way of aggregating logs or traces,” etc. But what does that mean exactly as far as solving [a system that’s gone down](https://thenewstack.io/6-scary-outage-stories-from-ctos/) and causing an organization to hemorrhage money?

## Making Observability Accessible to Non-Technical Users

A key requirement in any observability strategy should be ease of use for a broad audience, from a seasoned engineer to a non-technical product manager, Hineline said. An effective tool must provide insights “out of the box” without requiring users to build hundreds of dashboards. It should be as intuitive as a smartphone: ready to use immediately but also customizable.

This accessibility empowers non-experts to draw valuable conclusions, Hineline said.

A product manager, for example, doesn’t need to be a “master technologist” to see a correlation between a sudden drop in conversion rates, a spike in application error rates, and a new software release that occurred moments before, he said.  They can form a simple hypothesis because the platform presents clear, relevant data points without the noise of unnecessary metrics.

This principle was proven during a critical outage at United Airlines, where an application grounding the airline was instrumented in real-time, Hineline said. A sales engineer at the airline company who had only been on the account for a few days and had no “tribal knowledge” about the application’s inner workings was able to find the root cause and resolve the issue.

This experience led to a key realization: The goal is to make people experts in the tool, not experts in every interconnected part of the company’s complex systems. When the tool is powerful and intuitive enough, Hineline said, it democratizes problem-solving, breaks down knowledge silos, and ultimately delivers better, faster outcomes for the business.

The most effective observability implementations, he said, begin not by asking “What data can we collect?” but by asking “What does good look like for our business?” The purpose of observability is to ensure technology is enabling the business as intended. This means tying technical performance directly to business outcomes. For example, he said, if an e-commerce site’s user experience is slower than a competitor’s, that’s a tangible business problem.

## Start With SLOs To Limit Data Collection

This business-centric mindset naturally leads to defining SLOs, which Hineline believes should be the launching point for an organization’s observability journey.

Starting with SLOs provides “guide rails” on what data to collect. Instead of collecting everything, teams can start with a simple, powerful foundation based on signals that matter to the business, such as response time, error rate and saturation. This focused approach, Hineline said, not only provides immediate insight but also [mitigates the cost concerns](https://thenewstack.io/observability-can-get-expensive-heres-how-to-trim-costs/) that make organizations “gun-shy” about observability.

A core problem in the industry has been the business model to “collect everything.” As companies are “hyper scaling, that volume is becoming massive, and so cost is becoming a factor,” Hineline said.. This has shifted the focus, he added, to “measuring value” and understanding “the value that telemetry is giving me to make sure that I’m collecting the right things.”

One of Chronosphere’s biggest differentiators, he said, is “giving that control back to the customer, letting them understand what the value of the telemetry and the logs that they’re putting in the platform is really returning for them.”

This addresses the developer tendency to collect “everything,” Hineline said. The platform provides “the data meta, to say, ‘OK, I know you wanted 5,000 metrics. You’re using 100.'”

## Connecting Observability to Tangible Business Needs

Hineline’s observations correlate with Gartner reports on the state of observability. In [a report published this past January](https://www.gartner.com/en/documents/6064663) by Gartner analyst [Martin Caren](https://www.linkedin.com/in/mcaren), [Gregg Siegfried](https://www.linkedin.com/in/greggsiegfried/), [Matt Crossley](https://www.gartner.com/en/experts/matt-crossley) and [Mrudula Bangera](https://www.linkedin.com/in/mrudula-bangera/), the vast majority of successful-adoption use cases will hinge on meeting tangible and measurable business needs.

By 2027, 80% of organizations that successfully apply observability will achieve shorter latency for decision-making, enabling a competitive advantage for their target business or IT processes, according to Gartner.

Organizations are typically well aware of the necessity and benefit of what proper observability offers. However, they are understandably concerned about getting dinged on costs, especially when rising cloud and other costs are considered in parallel.

Log monitoring is often a starting point for organizations looking to understand the health and performance of their systems, the Gartner analysts write.

“Although logs are often in a human-readable text format, this also makes them a challenge for machines and costly to move, process and store,” the Gartner report reads. “Organizations operating at more than 1TB of logs per day will want to explore telemetry pipelines (differentiated layer) as a way to manage these issues.”

## A Practical Example: Chronosphere Logs in Action

[![](https://cdn.thenewstack.io/media/2025/09/32be332b-screenshot-2025-09-26-at-12.35.33%E2%80%AFpm-1024x581.png)](https://cdn.thenewstack.io/media/2025/09/32be332b-screenshot-2025-09-26-at-12.35.33%E2%80%AFpm-1024x581.png) Chronosphere Logs for finding what ails your virtual machines.

In June, Chronosphere introduced Logs 2.0. With it, the company claims, organizations reduce time to recovery and make it easier to optimize operations and debug.  

While my analyst firm, ReveCom, has not yet tested and analyzed this release, we have viewed a Chronosphere [demo of Chronosphere Logs.](https://www.youtube.com/watch?v=cMGPZ49vuS8) During that demo, the troubleshooting phase using the newly released logging capabilities was shown. The demo highlighted how Chronosphere solved an internal in-house problem it had identified through log data.

In the demo, [Jerome Froelich](https://www.linkedin.com/in/jerome-froelich-466730a0/), a software engineer at Chronosphere, described how the Chronosphere platform was used when a P99 latency for a metrics ingestion service increased. While the service in question looked healthy, the investigation turned to a proxy used to route edge traffic.

The metrics for one particular proxy instance were different from the others, Froelich said.  When switching to look at the logs for that proxy, it was found that the cloud provider performed a live migration on the virtual machine that instance was running on.

In this case, the VM came back in a degraded state. After it was removed from the fleet, the observed latency returned to normal, Froelich said. “Previously, debugging an issue like this would have required piecing together information from multiple disparate sources. Now, the information is available in a single pane of glass.”

## The Ongoing Challenge of Simplifying Observability

Reducing cost through reducing the size and siphoning metrics to fit the user’s needs, as opposed to just opening up this spigot of any and all data, is definitely a bad idea and a costly one. And Chronosphere at least appears to be making an earnest attempt to do that, as well as simplifying the observability process to meet the above goals as stated.

Of course, this is the mantra of other observability providers that we’ve recently covered — [Chronosphere](https://thenewstack.io/taming-ai-observability-control-is-the-key-to-success/), as well as [Grafana Labs,](https://thenewstack.io/grafanas-cto-on-the-state-of-the-observability-market/) [Kloudfuse,](https://thenewstack.io/kloudfuse-3-0-an-all-in-one-observability-platform-emerges/) [WanAware](https://thenewstack.io/wanaware-21-packets-affordable-observability-play/) and others.

As it stands now, properly instrumenting and taking advantage of observability remains a difficult process and the learning curve is steep — vendor claims aside. While the providers are obviously aware of the challenge, and it’ll be exciting to see what they come up with, don’t expect solutions that will allow the user to garner everything they need to know about their applications and network in a way that is very accessible in the near term.

But surprises do happen.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)