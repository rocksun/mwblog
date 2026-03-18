Over the past year, I have spoken with dozens of engineering teams about their [observability](https://thenewstack.io/introduction-to-observability/) pipelines and analyzed their production telemetry directly. The conversations start the same way: costs are growing, leadership wants answers, and the team is under pressure to cut the bill. Names and identifying details below are changed, but the numbers and patterns are real.

A payments company with thousands of engineers spends over $200,000 a month on observability tooling. Their 18-person platform team monitors cost estimates every single day. When the estimate trends up, they investigate which team caused the spike, then chase that team down manually. They built anomaly alerts to automate this, but the alerts aren’t calibrated well enough. Sometimes they fire at the wrong team; sometimes they don’t fire at all.

To control costs, the team excludes debug logs entirely and drops 99% of unformatted logs before they reach the indexer. It also cuts certain categories of info-level logs. The company has already migrated from one observability vendor to another and is now building a secondary self-hosted stack as a cost hedge.

> “This is the cost spiral that nearly every organization with a non-trivial observability deployment recognizes.”

The bill keeps growing. The underlying instrumentation has not changed.

This is the cost spiral that nearly every [organization with a non-trivial observability](https://thenewstack.io/only-27-of-organizations-have-full-stack-observability-says-report/) deployment recognizes. The instinct is to treat it as a vendor pricing problem. Evaluate a cheaper backend. Add sampling. Route signals to a less expensive tier. Reasonable optimizations, but they treat the symptom.

## The governance gap

The real questions are different. What telemetry are we generating? Who owns each signal? Is any of it useful?

When I analyzed production telemetry from a financial institution running over 4,700 services, 82% of all data points lacked a basic *service.name* attribute. Those metrics, millions of data points per five-minute window, had no owner. Nobody could attribute them to a team, a product area, or a cost center. The organization had instrumentation guidelines. Nothing enforced them at scale.

The same analysis found 1,300 services leaking sensitive data into their observability pipeline. A framework-level Java Virtual Machine (JVM) truststore password leaked into 352 services, not because of individual developer mistakes, but because the framework set it as a system property and auto-instrumentation captured it. Kafka configuration logging exposed credentials in 479 services. Tax IDs, bank account numbers, and authorization headers appeared across hundreds more. The security team had policies. Nothing enforced them automatically.

> “These are not vendor problems. Switching backends does not fix instrumentation that captures credentials.”

At another company, Financial Operations (FinOps) reviews happen twice a month. The original trace implementation set 100% sampling on every service. Years later, nobody has reduced it because the cultural expectation is that all traces are available. Meanwhile, user IDs and offer IDs leak into metric attributes, creating high-cardinality explosions that drive cost up with every new customer.

These are not vendor problems. Switching backends does not fix instrumentation that captures credentials. Sampling does not fix a missing *service.name*. A cheaper tier does not make 75% log duplication disappear.

## Quality at the source

Pipeline-level solutions, sampling, filtering, routing, and dropping, reduce volume without improving signal quality. They operate too late. By the time telemetry reaches the pipeline, the cost of generating it has already been paid, and the sensitive information has already been serialized.

At a company running between 4,000 and 6,000 services, nearly all services rely on auto-generated instrumentation. The result: traces with over 2,000 spans, dominated by internal framework calls that answer no operational question. One engineer described it plainly: “We almost exclusively have auto-instrumentation and we see a lot of garbage and technical debt as a result.” Sampling can reduce the volume of these traces, but it cannot make them meaningful.

> “Fixing quality at the source means every metric, span, and log exists for a stated reason.”

In another production environment I analyzed, 81% of all trace data consisted of Redis PING commands and [health check endpoints](https://thenewstack.io/a-guide-to-fluent-bits-health-check-api-endpoints/). At a different organization, 75% of logs were exact duplicates: Kafka client chatter repeating every few seconds, Kubernetes events cycling through the same warnings, one service emitting nearly 2,000 identical lines in a five-minute window. Pipeline deduplication can compress this, but the question remains: why is the application generating it at all?

Fixing quality at the source means every metric, span, and log exists for a stated reason. Instrumentation follows conventions, attributes carry the metadata needed for attribution, and sensitive data never enters the pipeline. This is the difference between treating observability as something that happens to your code and treating it as something you design into your code.

## What governance actually looks like

Telemetry governance is the practice of knowing what you collect, who owns it, and whether it serves a purpose. Based on patterns I have seen across these organizations, it involves a few concrete capabilities.

Instrumentation scoring gives each service a quantitative quality baseline. Instead of asking “Is our instrumentation good?”, teams ask “Which services dropped below our threshold this week, and why?” Scoring makes quality measurable and trackable.

Automated review catches problems before they reach production. When a developer adds a span attribute that includes a user ID or introduces a metric with unbounded cardinality, the feedback loop should be immediate. Not at the next FinOps review. Not when the bill arrives.

Fleet-wide visibility into SDK versions, configuration drift, and semantic convention compliance addresses governance at scale. When 60 teams onboard to a centralized platform, each following guidelines at their own interpretation, manual enforcement does not work.

Personally Identifiable Information (PII) detection in telemetry data, not just in application logic, catches what code review misses: framework-level leaks, auto-instrumentation capturing headers, and business logic logging transaction details into span attributes.

## The productive question

The next time someone asks, “Why is our observability bill so high?”, the productive answer is not “Let’s switch vendors.” It is “let’s understand what we’re generating and why.”

That conversation shifts the focus from cost reduction to quality improvement. It moves the discussion from the pipeline to the source. And quality improvements deliver cost savings as a side effect, because when instrumentation is purposeful, there is less to collect, less to store, and less to pay for.

The organizations spending the most on observability are not the ones with the most services. They are the ones that have never asked whether their telemetry is any good.

*This guest column is being published ahead of [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/), the Cloud Native Computing Foundation’s flagship conference, which will bring together adopters and technologists from leading open-source and cloud-native communities in Amsterdam, the Netherlands, from March 23-26, 2026.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/03/1193bdff-cropped-808495cd-juraci_ollygarden-erika-hahn-600x600.png)

Juraci Paixão Kröhling is a software engineer at OllyGarden, a maintainer of the OpenTelemetry project, a member of the project's governing board and CNCF Ambassador. He has presented about distributed tracing, OpenTelemetry, and other related topics at conferences like KubeCon,...

Read more from Juraci Paixão Kröhling](https://thenewstack.io/author/juraci-paixao-krohling/)