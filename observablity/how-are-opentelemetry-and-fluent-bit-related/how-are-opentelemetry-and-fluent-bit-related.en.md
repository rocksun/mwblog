***Editor’s Note:** The following article is an excerpt from Chapter 1 of The Manning Book: “[Fluent Bit with Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS),” a guide to configuring Kubernetes logging, metrics and trace pipelines. This excerpt focuses on Fluent Bit’s relationship to OpenTelemetry and its evolution in capturing not only logs but also local metrics such as CPU, memory and storage use. To examine more closely how Fluent Bit and OTel perform different functions, [download the full](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS) book.*

## How OpenTelemetry Came to Life

Before OpenTelemetry (OTel), the primary specifications that informed the observability of metrics, traces and logs came from several standardization efforts within [Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/) in the form of [OpenTracing](https://opentracing.io), [OpenCensus](https://opencensus.io/?utm_source=sponsored-content&utm_id=TNS) and — implicitly, given its dominance — [Fluentd](https://chronosphere.io/learn/fluent-bit-vs-fluentd/), along with, by association, [Fluent Bit for the structure of logging](https://thenewstack.io/a-guide-to-fluent-bit-processors-for-conditional-log-processing/).

Different standards often required different tools to capture such data. [Fluent Bit](https://thenewstack.io/fluent-bit-a-specialized-event-capture-and-distribution-tool/) has always caught some metrics data; the Internet of Things (IoT) ecosystem needs to keep software footprints small, so one service capturing both logs and metrics is preferable. As a result, it made sense for Fluent Bit to capture not only logs but also local metrics such as CPU, memory and storage use.

Bringing all these data sources together has driven the simplification of operational monitoring, resulting in rapid uptake and proving to be disruptive. [Fluent Bit’s support of the OTel standards](https://chronosphere.io/learn/observability-pipeline-opentelemetry-fluent-bit/) and its ability to work within the OTel ecosystem haven’t required any radical changes, although they have driven some upgrades to parts of its implementation. In some respects, the upgrades have formalized what Fluent Bit was already doing. With this alignment, [Fluent Bit is well-equipped to support the adoption](https://thenewstack.io/whats-driving-fluent-bit-adoption/) of OTel standards without imposing them, allowing its adoption to be more incremental.

### Learnings from Later Manning Book Chapters

In future chapters, when we start digging into the input and output capabilities of Fluent Bit, we’ll look further into the relationship with OTel and leading products in the observability space, such as [Prometheus](https://prometheus.io), which has helped propel OTel further forward, and [Grafana](https://grafana.com/grafana). We’ll also look at commercial vendors that have worked to support OTel’s standards, creating a rapidly growing ecosystem of connectable monitoring tools.

**Note:** If you need a quick reference on the acronyms and terminology, you can find a handy glossary [here](https://opentelemetry.io/docs/concepts/glossary). Also, Appendix B lists several excellent resources. ([*Download the book*](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/) *to view Appendix B.*)

## How OTLP and OTel Fit Together

The heart of OTel is the [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otel/protocol/) (OTLP), which details the data structures, encoding and transmission of the telemetry data.

Currently, [OTLP supports transmission using remote procedure call (gRPC)](https://betterstack.com/community/guides/observability/otlp/) with HTTP/2 using Protocol Buffer (Protobuf) and JSON with HTTP synchronously. OTLP promotes the use of gRPC as the first-choice approach to communication and JSON as a step-down or fallback.

OTel, as a project, goes far beyond defining OTLP. It also provides implementations of the functionality described in the standard (sometimes described as a reference implementation), along with tools and libraries.

The tools and libraries are implemented in multiple languages; we can use them to help inject logic into applications and quickly get data applications producing traces. OTel also has functionality, such as log appenders, that allow logging frameworks to send the logs using the OTLP specification.

## How Fluent Bit Fits in an OpenTelemetry Solution

To understand how Fluent Bit could fit into an OTel solution, let’s look at what Fluent Bit can do using [OTel terminology](https://opentelemetry.io/docs/concepts/components):

* Given its ability to gather [monitoring and observability](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "monitoring and observability") data from different sources and transform it into the OTLP structure, Fluent Bit can fill the role of an OpenTelemetry Collector.
* Because Fluent Bit was built to work in a distributed environment and can pass data in OTLP format to any other OpenTelemetry-compliant collector (which could be a Fluent Bit node or another product), we can describe Fluent Bit as being able to perform as an OTLP Exporter.

Figure 1 shows how Fluent Bit can fit into an OpenTelemetry environment with its ability to handle logs (L), metrics (M) and traces (T) generated by an application with or without the help of OTel libraries or tools, along with its ability to interact with an OpenTelemetry Collector.

### Collector vs. Exporter: Choosing the Right Role for Fluent Bit

Because OTel provides implementations of collector and exporter capabilities, calling [Fluent Bit an OpenTelemetry Collector or OpenTelemetry Exporter can be a source of confusion](https://devopscon.io/blog/observability-monitoring/fluentbit-otel-k8s/). The standard itself is called OTLP, so referring to Fluent Bit as being OTLP-compliant is clearer, even if less obvious about the task we might [deploy Fluent Bit](https://thenewstack.io/how-to-deploy-fluent-bit-in-a-kubernetes-native-way/) to perform.

In addition, there is some sensitivity within the OpenTelemetry community about the difference between the project’s own implementation of a collector (called OpenTelemetry Collector) and other implementations of that capability. We are erring on the side of describing Fluent Bit as an OTLP Collector (after all, protocol compliance is key to the collector’s function) and reducing ambiguity among CNCF projects.

[![Fluent Bit’s relationship with OpenTelemetry with apps generating OTel logs, metrics and traces and Fluent Bit facilitating their transmission to an OTel-compliant point of aggregation or processing. Applications can send OTLP data directly or via an OTel component, and we can route data to other OTel services or analysis tools.](https://cdn.thenewstack.io/media/2025/10/a1d98481-image1.png)](https://cdn.thenewstack.io/media/2025/10/a1d98481-image1.png)

Figure 1. Fluent Bit’s relationship with OpenTelemetry, with apps generating OTel logs, metrics and traces and Fluent Bit facilitating their transmission to an OTel-compliant point of aggregation or processing. Applications can send OTLP data directly or via an OTel component, and we can route data to other OTel services or analysis tools.

### **Protocol Buffers (Protobuf)**

Protocol buffers are a key technology for gRPC, which OTel uses. Protocol buffers have a concisely defined schema, which is used with the Protobuf tooling to generate the code for sending and receiving payloads. A well-defined schema allows the tooling to create the code that creates a compressed binary payload representation. This schema is both a strength and a potential constraint.

The strength comes from the efficient payload transmission. The downside is that a schema change affects both the provider and consumer and makes realizing the tolerant reader integration pattern more challenging. Also, given that the Protobuf-generated payload is a compressed binary format, it is a lot harder to inject into any communication middleware that can accommodate transformation. Links to OTel, Protobuf and related technologies are in Appendix B.

## Looking Ahead: Explore Fluent Bit and OTel Even Further

As we progress through the “[Fluent Bit with Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/)” book, which can be downloaded in its entirety [here](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/), we’ll examine more closely how Fluent Bit and OpenTelemetry perform different functions. Note that OpenTelemetry protocol support before Fluent Bit v3 was restricted to HTTP and JSON. Version 3 brought enhancements that support HTTP/2, enabling Fluent Bit to use gRPC. This, in turn, means that [Fluent Bit can provide a fully compliant OTLP implementation](https://chronosphere.io/resource/getting-started-with-fluent-bit-and-open-source-telemetry-pipelines/) without needing to take advantage of the step down to HTTP and JSON.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/05/c3489f3d-cropped-ba30d14d-phil-wilkins.jpeg)

Writing for Chronosphere, Phil Wilkins has spent more than 30 years in the software industry, with broad experience in businesses and environments from multinationals to software startups and consumer organizations to consultancy. He started as a developer on real-time, mission-critical...

Read more from Phil Wilkins](https://thenewstack.io/author/phil-wilkins/)