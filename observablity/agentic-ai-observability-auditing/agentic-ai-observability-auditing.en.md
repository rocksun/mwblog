Unknown unknowns take on a whole new meaning when AI agents are acting on our behalf. Up until now, [autonomous AI fleets inject more bugs](https://arxiv.org/abs/2603.28592) and contribute to more long-term code smell and technical debt, in less predictable, less traceable ways.

“Good enough” monitoring in your innovation lab fails to scale across enterprise silos and GPU resources. As enterprises transition autonomous, dynamic AI workloads from experimental to in-production, [observability](https://thenewstack.io/observability/) of agentic AI workloads becomes one of the most pressing problems enterprises face.

Traditional infrastructure and application performance monitoring (APM) fall short not only in their inability to keep up with this influx of code but also in their failure to peek into AI’s locked box. AI-enabled observability platforms are evolving in response, moving from simple metric monitoring to complex, actionable decision auditing.

[Gopal Vogety](https://www.linkedin.com/in/gopal-vogety/), senior director of software engineering for [HPE OpsRamp Software](https://www.hpe.com/uk/en/opsramp.html), tells *The New Stack* that there are differences in how AI workloads are managed.

> “Observability platforms are becoming auditing platforms, so that, when the humans are kept in the loop, they get the big picture, as well as the lowest-level technical details.”

“AI workloads have to be looked at, monitored, and managed differently than your regular workloads, and they deserve an AI workload-specific way of presenting the monitored data so that you help these new operational personas,” Vogety says.

“Observability platforms are becoming auditing platforms, so that, when the humans are kept in the loop, they get the big picture, as well as the lowest-level technical details.”

AI auditing platforms enable site reliability engineering (SRE) teams to enable more AI-infused applications, agents, and engineers in a provable way, giving business leadership the confidence to finally scale their AI programs. But, like all things with AI, there are a lot of people and process changes needed to support your ops teams. Here’s what you need to get your operations teams and your leadership on the same page with [agentic AI](https://community.hpe.com/t5/alliances/why-multi-tenancy-matters-for-ai-at-scale-and-how-hpe-is/ba-p/7263999).

## **Ops remit forced to expand**

It is harder than ever to work out not only *what’s* gone wrong, but *where* it occurred, *why* *which* agent did *what*, and, of course, *how* to fix it and prevent it from happening again.

Already, two-thirds of [enterprises lack confidence in real-time threat detection](https://www.fortinet.com/resources/reports/cloud-security) and response capabilities. Cloud-native, distributed environments have always been complex, so we need a new adjective to describe what SREs face with AI. There can be multiple AI apps, dependent on several large language models (LLMs), all within a single cluster.

The [2025 DORA report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report) found that higher AI adoption correlates with both increased throughput and increased instability. If developers are stuck in a [guess-and-check loop with AI](https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535), then we can only imagine the experience of ops teams, often another step away — sometimes miles —  from overseeing AI fleets.

And it’s not just engineering departments deploying swarms of AI agents. Across verticals, teams such as marketing and sales have aggressively integrated agentic AI into their workflows. Those teams demand their own vertical-specific insights.

“They really need help monitoring to understand if the reasoning and if the decisions that are being made by these agents in their verticals” are right for their business objectives, Vogety says, or if they are even accurate.

All while the operations pipeline problem persists. Across security, site reliability engineering, and DevOps roles, companies rarely had enough operations professionals, even before this influx of code and agents, to observe, monitor, and review. Not to mention the increase in sophisticated AI-generated cybersecurity attacks.

The emerging solution is what Vogety calls an “AI factory,” where enterprises use AI as a shared resource across all business units, controlling token and AI-tool sprawl while ensuring the necessary security, privacy, and quality guardrails are in place. Above this factory sits an observability AI auditing platform that enables human SREs to safely deploy AI at enterprise scale.

## **Demand for a whole new vocabulary — plus translator**

SREs and other ops teams have to adapt to a whole new AI-native vocabulary, which the AI auditing platform enables.

In order to solve what went wrong and how to fix it, Vogety says that ops teams need to answer new AI-centric questions, including:

* What parts of the LLM has the agent used?
* What reasoning has the agent gone through?
* What steps did the agent take before making that final decision?
* What data has it accessed?
* What sort of tools has it interacted with?

Many of these answers rely on a platform-centric approach to decision monitoring, balancing the need to drill down into technical metrics when necessary with the need to ensure that the most actionable signals are surfaced first.

The right AI auditing platform will “level it in such a way that an input prompt comes in and the final decision is made and try to help the enterprise customer understand what parts of the LLM and what parts of the reasoning steps the agent has gone through,” Vogety explains, “as well as what data it has accessed and what kind of tools that it interacted with and then, finally, the decision it has come to.”

Like their [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/ "internal developer platform") predecessors, an AI-centric observability platform should create a common language across business and technical stakeholders.

Operators still have to respond to their software development and infrastructure counterparts who demand new monitoring requirements to understand how AI workloads are coexisting within the already complex enterprise IT stacks.

“Monitoring the performance and the overall latency of how these LLMs are operating behind the scenes, so that it cannot just help from a cost angle, but also help the developers optimize their agentic code models that are being used for various agentic applications,” Vogety explains.

Many end users might not care about all those technical complexities, he continues. What they prioritize is: How is the quality of my AI?

Decision monitoring is particularly important for well-regulated industries and for any organization with [customers or users in the European Union](https://artificialintelligenceact.eu/assessment/eu-ai-act-compliance-checker/), which strictly requires AI auditability.

Compliance teams aren’t the only business stakeholders that will demand this level of traceability. Understanding token usage will also become increasingly important as FinOps and CloudOps meet AI at scale. With the right platform, observability teams can also help identify which workloads should remain in the cloud and which should be moved to usually more cost-efficient on-premises.

Each of these business and technical stakeholders needs its own simplified data representation within the context of both its AI workloads and domain. And it needs metrics that fit this new world.

Certainly, [DORA metrics](https://thenewstack.io/google-says-you-might-be-doing-dora-metrics-wrong/) like meantime to recovery remain essential to ops teams. Observability teams must now also examine agentic workload trends like P95, answering what is the average token usage for 95% of transactions.

An AI-native observability platform “ought to give all the pieces of information that the operator needs about the whole, applications, models, or any specific alerts that need their attention,” Vogety says. “In the world of AI, the logs play a very critical role [and drive] any decisions that are happening in the background.”

## **Tracking the lifecycle of a prompt**

Just like optimizing across the software development lifecycle has been directly tied to the success of high-performing teams, understanding and optimizing the agentic AI lifecycle will decide the next winners in the Age of AI.

Every deployer of AI agents needs to be able to access insights into:

* LLM selection
* Data access
* Tool interaction
* Final decision made

Together these steps are referred to as the AI’s trace. Tools like [HPE’s OpsRamp Software](https://www.hpe.com/uk/en/opsramp.html) bridge the gap between the agent’s reasoning pathway, the physical hardware, and the final decision and action.

Vogety gives the example of a highly important factor in whether a loan is approved or denied. “Let’s say you want to deny the loan for XYZ reasons, all the reasons to be laid out as part of the final decision.”

You want this new kind of AI operator to monitor how many of those kinds of prompts have been made over a given time period per application, and alert if there are any peaks anywhere.

> “Let’s say the time is 11:30 at night — that peak could be very odd. The model could’ve drifted to giving the wrong responses.”

“Let’s say the time is 11:30 at night — that peak could be very odd. The model could’ve drifted to giving the wrong responses.” Vogety continues, “At that time, the volume should not be so high, and these models and the GPUs are expensive, so you want to show the token usage also.”

If these GPUs are being consumed locally, that’s one thing, but if these tokens are being used on public models, that token usage directly maps to cost. This abnormal peak could also signal a heightened vulnerability. Depending on different organizational thresholds, this anomaly could be something small or you may need to wake up an SRE to investigate.

For AI observability platforms like HPE OpsRamp, you can zoom out to see this trend and drill down to the lowest granularity, per-call per LLM. Like traditional monitoring, it also shows you which AI apps are running on which clusters.

## **The risks of agentic observability**

Using AI for observability isn’t a silver bullet either.

In the face of all these bottlenecks on the ops side, engineers are using AI to review AI. This risks triggering what independent researcher and engineer Christos Zietsman calls the [homogenization trap](https://arxiv.org/abs/2603.25773) where both generating and reviewing agents share the same training distributions. This can result in correlated errors, causing the reviewing agent to miss the same edge cases that the generating agent did. This, he writes, makes bugs invisible to automated pipelines and human operators.

Recent research out of Stanford University finds that this homogenization trap sees [multi-agent systems experiencing a 37.8% performance loss](https://arxiv.org/abs/2602.01011), as agentic consensus-seeking behavior — where agents agree on a wrong answer to maintain consistency — overrides the individual engineer’s experience.

While this research, just like these AI-driven industry changes, is nascent, it does make the case for getting a second opinion. By using a third-party observability platform that doesn’t share the same underlying architecture and models as the generating agent, you can reduce this risk of correlated failures. It also helps avoid vendor lock-in, enabling a united view across a multi-vendor AI factory.

When deployed correctly, early use of [AI agents in operations has cut the time required](https://thenewstack.io/hpe-agentic-ai-ops-burnout/)[for root cause analysis in half](https://thenewstack.io/hpe-agentic-ai-ops-burnout/). As this technology evolves and self-learns, the opportunity of [self-healing ops](https://thenewstack.io/hpe-self-healing-ai-infrastructure/) also comes into view.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)