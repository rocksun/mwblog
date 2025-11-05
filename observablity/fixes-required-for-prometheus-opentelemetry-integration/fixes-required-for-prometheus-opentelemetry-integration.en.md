We have covered how there have been some [conflicts between OpenTelemetry and Prometheus](https://thenewstack.io/prometheus-and-opentelemetry-just-couldnt-get-along/) compatibility for a number of reasons. Much of this has to do with how [Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/) has been — and remains — a very tried and trusted open source metrics solution that preceded what [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) has offered as an alternate way of standardization and other attributes that definitely shine for observability.

During [PromCon,](https://promcon.io/) Prometheus’s annual user conference held recently in Munich, [Julius Volz](https://www.linkedin.com/in/julius-volz/?originalSubdomain=de), a co-founder of Prometheus, offered specific insights during the opening keynote into how using OpenTelemetry with Prometheus still poses problems and what needs to be done to address those issues.

First, the bad: There is a fundamental loss of service discovery and active pull when using OpenTelemetry, as well as the complexity of OpenTelemetry’s SDKs. Performance issues abound as well. In one benchmark test — which [RevCom](https://standards.ieee.org/about/sasb/revcom/) has not verified — Volz noted there was up to a 22 times speed difference in [Go](https://thenewstack.io/introduction-to-go-programming-language/) benchmarks when OpenTelemetry instrumentation is used compared to native Prometheus instrumentation.

Obviously, improving performance is key, in particular for code meant for observability, which runs very often and is meant to help improve performance. But semantic conventions also pose problems, as we discussed in our previous articles. There is also a continued need for collaboration between the Prometheus and OpenTelemetry teams.

“I did want to point out the drawbacks of [integrating OpenTelemetry with Prometheus], and maybe make you think about, ‘OK, do we really want to go down this route if you mostly care about metrics and using them with Prometheus?’” Volz said. “Also, in terms of the service discovery and SDK slowness drawbacks, I would really like other people to think about that more and maybe improve things, to not just throw away the baby with the bath water and lose all these benefits that we built very carefully in Prometheus over a long time.”

There have been many improvements since [Richard “RichiH” Hartmann](https://www.linkedin.com/in/richih/?originalSubdomain=de) started a formal effort to improve interoperability between the two projects in 2020 (his business title is director of community at Grafana Labs).

While OpenTelemetry’s lack of service discovery will always create extra work for operators, most of the fundamental problems have been resolved, Hartmann told me post conference. OpenTelemetry has changed, arguably fixed, their histogram bucket definitions in favor of Prometheus, Hartmann said. “Prometheus then expanded support for data labels to support OpenTelemetry,” Hartmann said. “And both projects collaborated early on native histograms based on the work of [Björn “Beorn” Rabenstein](https://www.linkedin.com/in/beorn7/), leading to fully compatible releases on both sides.

Meanwhile, OpenTelemetry is “here in full force and is not going to go away, and organizations seek to use it with Prometheus, instrumenting their services with OpenTelemetry and then sending the metrics part to the Prometheus system, Volz said. “However, there are plenty of downsides in comparison to using Prometheus’ own native instrumentation client libraries,” Volz said. “It is important to be aware of these before choosing the OpenTelemetry route if one mostly cares about metrics and Prometheus.”

A quick contrast between the two systems shows that Prometheus is an entire monitoring system, focusing only on the metrics signal type. In contrast, OpenTelemetry “only cares about” generating the signals — including [logs, metrics, traces and profiles](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/) — and then passing them on to some kind of third-party backend system, Volz said. This corresponds to how OpenTelemetry’s creators’ goal is to standardize on the emission aspect and reflects the many different storage vendors represented in OpenTelemetry.

The transfer pieces present a key difference: OpenTelemetry uses [OTLP](https://thenewstack.io/why-google-clouds-otlp-support-matters-for-your-telemetry-pipeline/) to send those metrics via push, while Prometheus uses a text-based format and actively pulls them, Volz said. Sending metrics via an OpenTelemetry collector to an OTLP receiver endpoint in a Prometheus server introduces several drawbacks, Volz said.

## Losing Active Pull and Health Monitoring

The first and most unfortunate downside is the act of throwing away a lot of what makes Prometheus good and capable: the integration of service discovery with a pull-based active target monitoring, Volz said. Prometheus solves this by talking to systems like the [Kubernetes](https://thenewstack.io/kubernetes/) API server to get an always-up-to-date view. It then actively tries to pull or scrape metrics, recording an up metric with a value of zero or one, which is essential for target health alerts, Volz said.

Since OpenTelemetry doesn’t have a built-in facility for this functionality, it becomes harder to tell if a target is running but not sending metrics, or if it is down, Volz said. Conversely, security controls are bypassed when unexpected metrics are pushed. “A lot of people ignore this completely, treating their Prometheus server as a random receptacle of metrics, and then they do not know if a process that should be running is not,” Volz said. “The idea of a synthetic up metric for OTLP ingestion has been heard, but it does not exist yet.”

The second downside is the resultant changed metric names or somewhat “ugly PromQL selectors,” Volz said. OpenTelemetry introduces character set differences, allowing characters like dots and slashes that were not supported previously in Prometheus 3. “This suggests that the people standardizing OpenTelemetry did not highly prioritize how a metric would be used in a query language like [PromQL](https://docs.cloud.google.com/monitoring/promql),” Volz said.

Prometheus conventions add suffixes for both units and types of metrics to immediately clarify the meaning. OpenTelemetry, however, says “don’t put unit and type into the metric name.” As a result, the Prometheus ingestion layer adds back those suffixes during translation. With the extended character set, PromQL selectors become more complex and less easy to write and read than the native selector, Volz said.

Indeed, OpenTelemetry and its SDKs are quite complex and can be quite slow. Benchmarking in Go showed that native Prometheus client libraries are up to 22 times faster than the OpenTelemetry SDK for counter increments, as mentioned above. “Even adding two labels makes the OpenTelemetry SDK 90% slower,” Volz said. “OpenTelemetry’s complexity is baked in and is hard to remove, making it the [XML](https://thenewstack.io/xslt-debate-leads-to-bigger-questions-of-web-governance/) or [CORBA](https://thenewstack.io/the-end-of-tribalism-in-software/) of telemetry, because it attempts to solve all problems at once.”

## Roll up Sleeves

To address health checks, future work may involve a synthetic up metric for OTLP ingestion, Volz said. This feature would use service discovery and correlate expected data with incoming data to generate an up metric when data is missing, Volz said.

“On the metrics side, the Prometheus team is actively trying to improve things, including creating an experimental Delta to cumulative processor to support OpenTelemetry’s Delta temporality,” Volz said. “There is also a recognized regret for not having semantic conventions in Prometheus land from the beginning, suggesting future collaboration with OpenTelemetry people could make sense to introduce a similar standardized naming structure.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)