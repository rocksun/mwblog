The volume of data and noise that comes with enterprise IT complexity leaves [operations teams](https://thenewstack.io/ai-operations/) struggling to understand how to prioritize issues and improve reliability. Things are missed, teams operate in a heightened state of constant triage, and systems become harder to manage as environments grow.

Models trained on infrastructure telemetry can recognize patterns across metrics, logs, and events. Paired with large language models (LLMs), they can detect unusual behavior earlier and explain what’s happening — helping ops teams quickly identify what has changed and where to investigate.

As [AI workloads](https://thenewstack.io/ai/) expand the amount of infrastructure that organizations must operate, sysadmins, DevOps teams, and site reliability engineers (SREs) struggle to connect signals across siloed data, workflows, and tools. There are too many interlocking, time-sensitive variables — including hybrid and multi-cloud, CPU, memory, network, and disk IO metrics — for traditional monitoring and [observability](https://thenewstack.io/observability/) tooling to interpret quickly. The result is alert fatigue, slower troubleshooting, and growing pressure on teams tasked with keeping the systems running.

Time-series models trained on infrastructure telemetry can recognize patterns across metrics, logs, and events. They allow enterprise infrastructure teams to move from reactive to proactive, identifying liabilities in your stack that could bring everything down. This opens the opportunity to move toward more meaningful, time-sensitive, and context-aware alerts, and even toward autonomous, self-healing, predictive maintenance.

> “Enterprises really want to get to more proactive approaches so they can start catching especially critical issues at the symptom level, and remediate those issues before an outage happens.”

[Phanidhar Koganti](https://www.linkedin.com/in/networkleader/), senior distinguished technologist in [Hewlett Packard Enterprise (HPE) hybrid cloud](https://www.hpe.com/uk/en/home.html), tells *The New Stack*, “Enterprises really want to get to more proactive approaches so they can start catching especially critical issues at the symptom level, and remediate those issues before an outage happens.”

Koganti and HPE’s just-published whitepaper, “[Beyond the Noise: Toward a Self-Healing Autonomous IT](https://www.hpe.com/psnow/doc/a00157497enw),” explores those issues and the potential for a self-healing strategy for high-performing compute environments powered by an IT-optimized time-series foundational model (IT-TSFM).

Are enterprises ready for [AIOps](https://community.hpe.com/t5/the-cloud-experience-everywhere/beyond-generic-aiops-why-your-infrastructure-needs-hardware/ba-p/7261841)? They definitely will be if it achieves the goal of remediating risk before outages occur.

## Costly risk of unknown unknowns

While numbers vary, it’s estimated that an outage costs [at least $4,000 per minute](https://itic-corp.com/itic-reports-surveys/) — for enterprises across sectors, [that cost can be much higher](https://uptimeinstitute.com/about-ui/press-releases/uptime-announces-annual-outage-analysis-report-2025).

But it isn’t just massive outages that cost organizations money. Partial, silent degradation can add up to even higher costs overall. And that cost accumulates over time because they tend to be harder and take longer to detect.

[As dTelecom puts it](https://www.linkedin.com/posts/dtel-org_enterprise-outages-now-cost-14000-per-activity-7419385574555324417-BW52/), it’s rare that systems fully go down: “The real cost comes from uncertainty. During incidents, teams spend 20 to 40% of the time just figuring out who’s affected — which users, which regions, which services, which data paths.”

Traditional monitoring and observability dashboards surface a mix of these unknown faults, some known faults, and a lot of [alert noise](https://community.hpe.com/t5/servers-general/architecting-the-future-of-ai-infrastructure-with-hpe/m-p/7258294#M21727). But it’s the unknown unknowns or “gray failures” that keep Koganti up at night.

“These silent failures typically escape the human eye, and if those issues turn out to be a failure the next day, that directly impacts the business.” He further explains that these tend to result from the interconnected nature of distributed dependencies, which scale with the size of your enterprise and software footprint.

A gray failure isn’t something that necessarily will crash your systems today, but it may already be slowing them down or costing you extra money. And it increases the risk of things crashing down tomorrow.

So how can your ops teams find them? How could they possibly score, remediate, or even fix them all at scale?

## Specificity needed for gray failures

Generalist time-series models can’t detect these gray failures because they aren’t trained on the nuances of IT or the specific nuances of each enterprise’s infrastructure. [As the whitepaper explains](https://www.hpe.com/psnow/doc/a00157497enw), generic models are incapable of understanding nuances in seasonal behavior and the interdependent behaviors specific to IT environments.

Some IT-centric examples given include:

* A CPU spike at 9 p.m. might be a normal scheduled backup or an abnormal Distributed Denial-of-Service (DDoS) attack.
* A rise in fan speed inside a server is expected behavior, but if it occurs without a corresponding increase in temperature, it becomes an anomaly.

“Even our laptops, there are so many applications running, and some of them are not well-written. There will be small memory leak failures,” Koganti gives as another common example. “They happen so slowly that in your day-to-day usage, you will not notice them until they hit a particular threshold.”

This could be human frustration at slowness, and then a project or the whole laptop suddenly crashes without saving.

“Remediation doesn’t have to be very sophisticated,” he continues. For this, a simple reboot may be enough, “because business continuity is the primary goal. Remediation is different from permanently fixing the issue.” It usually buys you time to uncover a permanent fix.

In the enterprise space, the examples quickly become increasingly interdependent and complex.

Koganti gives the example of retail organizations that need to understand any behavioral anomalies occurring during the day and then remediate them when the store is closed, so, again, business continuity is preserved.

Right now, human operators tend to set blanket thresholds, like, for example, if CPU exceeds 90%, page someone on-call. But Koganti points out that the CPU staying between 80 and 90% on a weekday is normal, whereas staying between 70 and 80% on the weekend is anomalous. Unless, of course, it’s an e-commerce site in December, when more CPU may need to be provisioned for the whole month.

This seasonality is key.

The aim of an IT-optimized time-series foundational model or IT-TSFM, Koganti explains, is to set adaptive thresholds to “try to catch gray failures at the symptom level by doing a thorough analysis on what’s been happening across the whole day, or even across a week or across a month, to identify if there are any slow, silent failures happening that could potentially lead to an outage the next day.”

![Gemini said This image provides a workflow diagram illustrating how IT-TSFM (Time Series Forecasting Model) analytics processes metrics to generate "Gray Failure Alerts" using adaptive thresholds. Image Structure and Content Data Input (Metric): The flow begins with a Metric block, which is defined by three components: Timestamp, Dimension, and Label(s) (highlighted in green). Analytics Processing: The metric data flows into IT-TSFM Analytics, which generates three specific outputs: Correlation Score Drift Score Adaptive Threshold Alert Output: These scores feed into Gray Failure Alerts, which provide: Programmable Drift Thresholds Detailed Context Programmable Actions Visual Demonstration of Adaptive Thresholds At the bottom, a CPU Metric vs. Time graph illustrates the concept of temporal context in monitoring: Monday 9 AM: A graph shows a CPU spike highlighted in a green box, suggesting this behavior is considered "normal" or expected for a Monday morning start-of-work period. Saturday 9 AM: An identical CPU spike is highlighted in a red box, indicating that because the temporal context has changed (it is now a weekend), the same metric level may trigger an alert or be flagged as a "gray failure" by the adaptive threshold.](https://cdn.thenewstack.io/media/2026/03/82dacccc-adaptive-thresholds@2x-100-1024x571.jpg)

The characteristics of a time-series metric and the outcomes delivered by the IT-optimized time-series foundational model, or IT-TSFM.

If — or likely when — this happens, it’s as much about alerting the ops team as it is about remediating and eventually fixing it. Some common things this novel model will flag up include:

* Zombie services
* User experience degradation
* Contention between two resources, i.e., high disk IO wait + normal CPU
* Security issues
* Latency issues

The ever-evolving patterns of time-series data and the complexity of modern enterprise infrastructure make it nearly impossible for humans to detect and respond to them — especially amid the current increase in complexity driven by widespread AI adoption.

## Will AI just replace the SRE?

Over time, these IT-specific, time-series foundational models can understand your unique infrastructure patterns and begin to suggest, or even auto-fix, some of these silent failures. Eventually, enterprises can transition to some proactive, self-healing IT environments.

![A process diagram titled "Life of an Enterprise IT using IT-TSFM" illustrating an observability-to-remediation pipeline. The workflow begins with a "Customer full stack" containing various system components marked with red alert icons. The pipeline proceeds through five main stages: Observe: Collecting multivariate data like CPU, memory usage, and ambient temperature. Extract Insights: Using "Zero-shot IT-TSFM" to analyze baseline volatility and seasonality to detect anomalies. Correlate (Reduce Alert Fatigue): Generating specific alerts for failure forecasts, univariate/multivariate anomalies, and causal reasoning. Root Cause Assistance: Utilizing IT-TSFM, agentic root causing, and LLMs for diagnosis. Proactive Remediation: Employing policy-based and Copilot-driven auto-remediations. The flow concludes with the "Customer full stack" returned to a healthy state, indicated by green icons.](https://cdn.thenewstack.io/media/2026/03/6130eac1-life-of-an-enterprise-it-using-it-tsfm@2x-100-1024x322.jpg)

Observability-to-remediation pipeline using IT-TSFM and agentic AI.

But, as with all things AI in the software development lifecycle, human operators are still needed. This should enable them to [manage the vulnerability process in a more holistic way](https://www.hpe.com/us/en/opsramp.html) while also catching more advanced issues earlier.

“Let’s say the human tells the system: This week, I just installed a whole new application, and I want you to take this behavior as the normal behavior and any drift that you see across various metrics, do try to proactively analyze and alert me if you see a major deviation,” Koganti says.

Because this is a new application, even small drifts need to be detected, “to catch issues at the system level before an outage happens.”

![A concentric circular diagram illustrating the layers of an Agentic AI stack for IT operations. The Core: A light purple center circle labeled IT-TSFM (IT Optimized Time-Series Foundation Model). The Middle Layer: A medium purple ring labeled Large Language & Reasoning Model, which surrounds the core. The Outer Layer: A dark charcoal ring representing Agentic IT Operational Intelligence. The bottom of this ring includes a document icon and the text IT Knowledge Base (Augmented continuously), indicating the data source powering the intelligence.](https://cdn.thenewstack.io/media/2026/03/63425315-conclusion@2x-100-1024x988.jpg)

Agentic AI stack centered on IT-TSFM.

As its name suggests, this IT-specific time-series model is meant to sit atop the enterprise IT knowledgebase as a foundation for large language and reasoning models, and then for agentic AI moving forward.

This is likely to increase alongside the capabilities for proactive and autonomous remediation.

This time-series foundational model for IT was developed in collaboration with [HPE Labs](https://www.hpe.com/us/en/hpe-labs.html) and is being released as part of its celebration of 60 years of pioneering advancement in computing.

**Dive into the novel technology behind the IT-optimized time series foundational model and read the whitepaper now: “****[Beyond the Noise: Toward a Self-Healing Autonomous IT](https://www.hpe.com/psnow/doc/a00157497enw).”**

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)