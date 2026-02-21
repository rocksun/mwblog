The often-misunderstood controversies regarding [Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/) and [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) arise more from technical incompatibilities that have since been resolved. Without going into the history of those controversies, it can be said that Prometheus remains the gold standard for metrics from [Kubernetes](https://thenewstack.io/kubernetes/) deployments.

OpenTelemetry acts as a conduit to Prometheus, complementing it with distributed traces and, more recently, logs. While OpenTelemetry primarily offers a push-based approach, Prometheus can continue to operate as a pull-based system when used with OpenTelemetry, or it can function as a standalone option for metrics and observability analysis. Progress continues to be made on both fronts.

Specifically, during the recently held [OTel Unplugged EU](https://opentelemetry.io/blog/2025/otel-unplugged-fosdem/) following [FOSDEM 2026](https://fosdem.org/2026/) in Brussels, there were some very fruitful discussions and descriptions of the immense improvements in the integration of OpenTelemetry and Prometheus. A key catalyst for these improvements is how Prometheus now supports UTF-8 and other [OTLP](https://thenewstack.io/search/)-native enhancements. Prometheus’ support for UTF-8 consists largely of dots, dashes, and other non-alphanumeric symbols in metric names and labels. This has remained a big hurdle for aligning OTelemetry’s semantic conventions for labels and attributes, which has been a huge challenge in the past when integrating the two.

[UTF-8](https://en.wikipedia.org/wiki/UTF-8) is structured to serve as a standard for text that covers language, symbols, and emojis. It’s been a big headache for developers and practitioners to have to fiddle around with the different nomenclatures in the past between Prometheus and OpenTelemetry.

But now, with the Unicode characters support for labels, annotations, metric names, and as well as this, it obviously, facilitates the integration between the two.

OpenTelemtry and Prometheus are now figuring out on a leadership level what it means to work together even more closely, with OTel potentially taking in some of the battle-tested specs, code, and exporters from Prometheus now that Prometheus supports UTF-8 and other OTel-induced changes,” said [Richard “RichiH” Hartmann,](https://www.linkedin.com/in/richih/?originalSubdomain=de) director of community at [Grafana Labs](https://grafana.com/). “For users, it means less friction and less tyranny of choice. There will hopefully be one single way to do some things. It would work the same on both sides, and be efficient and effective.”

## Deep background

Organizations that already rely on Prometheus for their telemetry signals often see a need to add OpenTelemetry to complement their metrics and add traces and logs to their [observability](https://thenewstack.io/introduction-to-observability/) data streams. Doing so is often considered a risk of breaking something that is not broken while potentially adding more complexity to their environment by implementing OpenTelemetry for metrics. Compatibility issues between OpenTelemetry and Prometheus have been largely resolved with the release of [Prometheus 3.0](https://prometheus.io/blog/2024/11/14/prometheus-3-0/).

Prometheus now integrates well with OpenTelemetry and remains a core part of the ecosystem. This competition was only surface-level. That said, Prometheus 2.0 introduced challenges when used as a metrics backend through OpenTelemetry, complicating adoption early on.

There have been compatibility problems that trace back well before the release of Prometheus 3.0. On a very basic level, there has been a difference in design philosophy. Compatibility problems related to data formats within Prometheus, specifically with histograms and the data forwarding protocol, are now natively supported in Prometheus 3.0 through features like Native Histograms and OTLP ingestion.

With the release of Prometheus 3.0, there are already a number of improvements that make collecting metrics through OpenTelemetry significantly better and less painful than in the past. While minor edge cases remain, as described above, work is ongoing, and with the support of the open source community, I can confirm firsthand that there is a lot of momentum to overcome these issues, which will be addressed in upcoming Prometheus releases.

This is one area where Prometheus plays a role. Current efforts involve actively translating these labels to be more compliant with conventions defined by Prometheus and Mimir to improve the structure and collatability of data.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)