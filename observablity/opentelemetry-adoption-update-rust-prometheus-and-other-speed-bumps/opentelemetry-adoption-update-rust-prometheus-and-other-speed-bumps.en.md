[OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) is arguably living up to its hype. The open source project for [observability](https://thenewstack.io/introduction-to-observability/) has evolved over the last few years to become the de facto standard of choice for a rapidly growing number of organizations in need of instrumenting applications and standardizing [telemetry data](https://thenewstack.io/unified-telemetry-observability-the-future-of-data-management/). It is designed so that the data can be understood by different observability platforms and visualization and storage systems of your choice.

The project’s contributors to this leading [CNCF](https://cncf.io/?utm_content=inline+mention) project behind [Kubernetes](https://thenewstack.io/kubernetes/) remain active in improving OpenTelemetry’s ease of use and implementation and adding new features. However, OpenTelemetry remains a work in progress, and it is still not yet universally adopted for all organizations’ needs.

Target areas for improvement continue to be OpenTelemetry support for all [programming languages](https://thenewstack.io/the-key-fundamentals-of-programming-you-should-know/) for metrics, logs and traces. [Rust](https://thenewstack.io/rust-programming-language-guide/) remains the language that is less supported by OpenTelemetry, according to the OpenTelemetry project’s documentation. [Traces, metrics and logs](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/) remain under development for Rust applications. All other major programming languages listed in OpenTelemetry’s documentation support at least metrics. This is largely due to several factors, including its relatively recent adoption at scale compared to the other commonly used languages and how metrics have worked well instead of OpenTelemetry for instrumentation.

## Complexity

Meanwhile, OpenTelemetry is often seen as complex to implement and manage, representing a significant mass adoption hurdle. Indeed, the implementation of OpenTelemetry can be challenging and complex, such as in very large and at-scale multicluster and cloud environments. (Although once the implementation work is completed, OpenTelemetry as a single instrumentation in use can go a long way in reducing complexity.)

“OpenTelemetry is complicated and hard to install,” [Ted Young](https://www.linkedin.com/in/ted-young/details/experience/), developer programs director for [Grafana Labs,](https://grafana.com/) told me during [ObservabilityCon](https://grafana.com/events/observabilitycon/) in London. That said, the core promise of standardizing observability signals — traces, metrics and logs — certainly meets real-world challenges, particularly in the domain of metrics and legacy systems, Young said. But while the project is seen as essential “to survive the future,” several key areas are driving friction, Young said.

For tracing, ensuring proper semantic conventions for labels and attributes poses challenges for developers when drawing ingress data through OpenTelemetry. Large organizations with hundreds of developers must ensure semantic conventions remain uniform. This developer-centric approach to instrumentation leads to “the weakest data quality” in tracing, as it is inherently “harder to get it right,” Young said.

The lack of established and comprehensive common conventions exacerbates this issue. While work exists for standard protocols like HTTP labeling, many “nonstandard protocols” — such as “messaging” or older “remote procedure call stuff” — lack the necessary conventions, Young said. These common conventions are essential to allow an observability backend to “automatically understand what it’s seen,” enabling advanced features like “knowledge graph” correlations.

## Prometheus Unbound

Organizations that already rely on Prometheus for their telemetry signals often see a need to add OpenTelemetry for their metrics. Doing so is often considered a risk of breaking something that is not broken while potentially adding more complexity to their environment by implementing [Prometheus](https://thenewstack.io/prometheus-and-opentelemetry-just-couldnt-get-along/) for metrics. Compatibility issues between OpenTelemetry and Prometheus remain an issue.

Prometheus now integrates well with OpenTelemetry and remains a core part of the ecosystem. This competition was only surface-level. That said, Prometheus 2.0 introduced challenges when used as a metrics backend through OpenTelemetry, complicating adoption early on.

There have been compatibility problems that trace back well before the release of Prometheus 3.0. On a very basic level, there has been a difference in design philosophy. Compatibility problems related to data formats within Prometheus, specifically with histograms and the data forwarding protocol, remain an issue with OpenTelemetry.

With the release of Prometheus 3.0, there are already a number of improvements that make collecting metrics through OpenTelemetry significantly better and less painful than in the past. Issues remain, as described above, but work is ongoing, and with the support of the open source community, I can confirm firsthand that there is a lot of momentum to overcome these issues, which will be addressed in upcoming Prometheus releases.

This is one area where Prometheus plays a role. Current efforts involve actively “refactoring these labels” to be more compliant with conventions defined by Prometheus and [Mimir](https://thenewstack.io/the-great-grafana-mimir-and-cortex-split/) to improve the structure and collatability of data.

## Rust Does Sleep

Rust is a newer programming language, and working with it is difficult compared to popular languages such as [JavaScript](https://thenewstack.io/introduction-to-javascript/) or even [Python](https://thenewstack.io/what-is-python/). But OpenTelemetry’s lateness in its compatibility with Rust is due largely to how tracing with open source [Tokio](https://thenewstack.io/using-rustlangs-async-tokio-runtime-for-cpu-bound-tasks/) works well already.

It is a good thing that Rust already has a widely adopted system, Young said. However, it also creates an “awkward situation” where the OTel community is debating whether to “just adopt Tokio tracing as the official” solution for the Rust community to gain high adoption, Young said. All this despite its limitations and the lack of momentum from its original developers.

The OpenTelemetry community faces unique integration problems with the Rust ecosystem, stemming from the language’s widely adopted native tooling. “The good thing in Rust is it has a thing called Tokio tracing,” Young said. “But the thing about Tokio tracing is it’s not distributed tracing. It’s more like, almost like, stack tracing … The problem is they work a bit differently. Tokio tracing doesn’t do distributed tracing.”

This technical gap — between OTel’s requirement for distributed tracing and Tokio’s focus on stack tracing — is compounded by issues of maintenance and momentum. “Tokio — as in the company Tokio — they’re not an observability company, and Tokio tracing is starting to look pretty unmaintained,” Young said. “It’s just an awkward situation where we’re like, maybe we’ll just adopt Tokio tracing as the official.”

The situation for future integration remains slow and uncertain. “There’s nobody home on that side, right? Because it seems like there’s not a lot of momentum,” Young said. “Now in Tokio tracing, I see like, whoa, what do we do? But that community is working it out. It’s just slow to figure out what actually is the right thing to offer.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)