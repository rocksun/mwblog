*Editor’s note: This article is an excerpt from Chapter 1 of the Manning book, “[Fluent Bit with Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform).” Read also:*

Fluent Bit has emerged as the go-to telemetry pipeline for cloud native environments. It’s trusted by thousands of enterprises, integrated across all major cloud platforms and downloaded more than 15 billion times — proving its scalability and production readiness at a global scale. The burning question becomes: What’s behind Fluent Bit’s rampant adoption?

The drivers that make Fluent Bit a significant player come down to a few key factors:

* The way [Fluent Bit is implemented](https://chronosphere.io/fluent-bit/?utm_source=TNs&utm_medium=sponsored+content&utm_content=inline-mention&utm_campaign=tns+platform) perfectly addresses the cloud and cloud native industry’s drive for small size, efficiency and quick startup, making it easier to exploit the elasticity of containerized environments.
* [Fluent Bit is equipped](https://chronosphere.io/fluent-bit-academy/?utm_source=TNs&utm_medium=sponsored+content&utm_content=inline-mention&utm_campaign=tns+platform) to meet the rapid acceleration and adoption of [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry/) (often referred to as OTel), bringing together log processing, metrics and tracing to harmonize the different aspects of observing our applications. As a result, tasks such as tracking individual transactions across multiple services and servers can be standardized.
* [Fluent Bit provides](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/) out-of-the-box support for other dominant cloud native technologies, particularly those used to support monitoring and observability, such as Prometheus and Grafana’s Loki.

There are a couple of additional factors that we think are in play, but the trends are harder to isolate:

* Support for ideas and approaches to streaming and stream analytics has been seen with technologies such as Apache [Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/), Spark and Beam. Fluent Bit’s capability to support stream-processing ideas may not be influencing adoption currently, but it is likely to make a difference in the future.

Streaming is more notable in the cloud and cloud native domains, but depending on how it is addressed, it can deliver dividends for [monitoring and observability](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "monitoring and observability") across all industries and technology domains, new and old. Fluent Bit’s streaming capabilities allow it to become more dynamic and adapt to what happens.

* One of the most dominant players in the monitoring space is Fluent Bit’s older sibling, [Fluentd](https://chronosphere.io/learn/forward-protocol-fluentd-fluent-bit/?utm_source=TNs&utm_medium=sponsored+content). We could attribute its dominance to several things, such as being early in the market and part of the [Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/), or the ease with which new sources and targets can be plugged into their custom integrations.

Fluent Bit has all these benefits. In addition, Fluent Bit can communicate transparently with [Fluentd deployments](https://chronosphere.io/learn/fluent-bit-vs-fluentd/?utm_source=TNs&utm_medium=sponsored+content), removing or minimizing disruption in transitions between Fluentd and Fluent Bit, and blending deployments of both across an organization as needed.

## Small Footprint, Efficiency and Speed

Fluent Bit may have started by supporting Internet of Things (IoT) use cases, but the characteristics that IoT requires fit nicely with cloud native, particularly containers and [Kubernetes](https://chronosphere.io/learn/kubernetes-component-logs-fluent-bit/?utm_source=TNs&utm_medium=sponsored+content). There are two reasons:

1. First, maximizing the dynamic scaling of containers through orchestration engines such as Kubernetes makes the ability to go from a standstill to running quickly exceptionally easy to do when an application is designed to run with a small footprint (typically needed on IoT devices).
2. Further, with the overhead of the container itself, anything we can do to reduce the amount of CPU and memory consumed is desirable. One way is to employ precompiled native binaries (sometimes called ahead-of-time [AoT] compilation). This approach eliminates the overhead of running an interpreter layer (such as the time to start the interpreter before any application logic is loaded and the additional memory needs of the interpreter). Using a just-in-time (JIT) compiler helps with performance but still has a compilation overhead that we see with language virtual machines (VMs) such as the JVM. As Fluent Bit has been written with C, it has always compiled into a binary and, therefore, has no overhead.

## Benefits of Scaling Quickly

The value of scaling exceptionally quickly and being resource efficient and high performing means that Fluent Bit has been adopted by cloud providers such as Amazon Web Services (AWS), Azure, Google and Oracle, as well as cloud service providers such as LinkedIn and Lyft, because these characteristics translate into tens of thousands of dollars in savings.

Although Fluent Bit is very compact, it can scale to handle workloads with controls that allow inputs and outputs to run in separate threads. Separating input and output operations reduces the chance that backpressure will affect multiple inputs.

Threading control options in Fluent Bit also have the potential to increase throughput. Still, when we’re working within a containerized environment, we need to use threading with care; we no longer have an assured allocation of CPU cores, and more threads could cause the real CPU to perform more context switching than is optimal.

## Effect of OpenTelemetry and How Fluent Bit Relates to It

Before OTel, the primary specifications that informed the observability of metrics, traces and logs came from several standardization efforts within CNCF in the form of [OpenTracing](https://opentracing.io), [OpenCensus](https://opencensus.io/) and, implicitly, given its dominance, Fluentd and, by association, Fluent Bit for the structure of logging.

Different standards often require different tooling to capture such data. Fluent Bit has always captured some metrics data; the IoT ecosystem needs to keep software footprints small, so one service capturing both logs and metrics is preferable. As a result, it made sense for Fluent Bit to capture not only logs but also local metrics such as CPU, memory and storage use. Bringing all these data sources together has driven the simplification of operational monitoring, resulting in rapid uptake, and has been shown to be disruptive.

Fluent Bit’s support of the OpenTelemetry standards and its ability to work within the OTel ecosystem haven’t required any radical changes, although it has driven some upgrades of parts of its implementation.

In some respects, the upgrades have formalized what Fluent Bit was already doing. With this alignment, Fluent Bit is well-equipped to support the adoption of OpenTelemetry standards without imposing them, allowing its adoption to be more incremental.

When we start digging into the input and output capabilities of Fluent Bit, we’ll look further into the relationship with OpenTelemetry and leading products in the observability space, such as [Prometheus](https://prometheus.io), which has helped propel OTel further forward, and [Grafana](https://grafana.com/grafana). We’ll also look at commercial vendors that have worked to support OTel’s standards, creating a rapidly growing ecosystem of connectable monitoring tools.

|  |
| --- |
| **Note:** If you need a quick reference on the acronyms and terminology, you can find a handy glossary [here](https://opentelemetry.io/docs/concepts/glossary). |

## OTel: Transmitting Telemetry Data

The heart of OTel is the OpenTelemetry Protocol (OTLP), which details the data structures, encoding and transmission of the telemetry data. Currently, OTLP supports transmission using Remote Procedure Call (gRPC) with HTTP/2 using Protocol Buffer (Protobuf) and JSON with HTTP synchronously. OTLP promotes the use of gRPC as the first-choice approach to communication and JSON as a step-down or fallback.

OTel, as a project, goes far beyond defining OTLP. It also provides implementations of the functionality described in the standard (sometimes described as a reference implementation), along with tools and libraries. The tools and libraries are implemented in multiple languages. We can use them to help inject logic into applications and quickly get data applications producing traces. OTel also has functionality, such as log appenders, that allow logging frameworks to send the logs using the OTLP specification.

To understand how Fluent Bit could fit into an open telemetry solution, let’s look at what Fluent Bit can do using [OTel terminology](https://opentelemetry.io/docs/concepts/components/). Given its ability to gather monitoring and observability data from different sources and transform it into the OTLP structure, Fluent Bit can fill the role of an OpenTelemetry Collector. Because Fluent Bit was built to work in a distributed environment and can pass data in OTLP format to any other OpenTelemetry-compliant collector (which could be a Fluent Bit node or another product), we can describe Fluent Bit as being able to perform as an OTLP Exporter.

Because OTel provides implementations of collector and exporter capabilities, calling Fluent Bit an OpenTelemetry Collector or OpenTelemetry Exporter can be a source of confusion. The standard itself is called OTLP, so referring to Fluent Bit as being OTLP-compliant is clearer, even if less obvious about the task we might deploy Fluent Bit to perform.

In addition, there is some sensitivity within the OpenTelemetry community about the difference between the project’s own implementation of a collector (called OpenTelemetry Collector) and other implementations of that capability. We are erring on the side of describing Fluent Bit as an OTLP Collector (after all, protocol compliance is key to the collector’s function) and reducing ambiguity among CNCF projects.

[![Fluent Bit can fit into an OpenTelemetry environment with its ability to handle logs (L), metrics (M), and traces (T) generated by an application with or without the help of OTel libraries or tools, along with its ability to interact with an OpenTelemetry Collector.](https://cdn.thenewstack.io/media/2025/06/79c9e1ea-image1a.png)](https://cdn.thenewstack.io/media/2025/06/79c9e1ea-image1a.png)

Fluent Bit can fit into an OpenTelemetry environment with its ability to handle logs (L), metrics (M) and traces (T) generated by an application with or without the help of OTel libraries or tools, along with its ability to interact with an OpenTelemetry Collector.

|  |
| --- |
| Protocol Buffers (Protobuf) Protocol Buffers are a key technology for gRPC, which OTel uses. Protocol Buffers have a concisely defined schema, which is used with the Protobuf tooling to generate the code for sending and receiving payloads. A well-defined schema allows the tooling to create the code that creates a compressed binary payload representation. This schema is both a strength and a potential constraint. The strength comes from the efficient payload transmission. The downside is that a schema change affects both the provider and consumer, and makes realizing the tolerant reader integration pattern more challenging. Also, given that the Protobuf-generated payload is a compressed binary format, it is much harder to inject into any communication middleware that can accommodate transformation. |

## Extending Fluent Bit With C, Go, WebAssembly and Lua

The ability to extend Fluent Bit’s core capability is important. The number of third-party plugins built for Fluentd clearly demonstrates this need. In addition to source and targets, small pieces of custom logic for actions such as filtering are also needed. For inputs, outputs and filters, we can connect precompiled solutions using C, Go (also referred to as Golang) and WebAssembly (WASM). We can use these solutions to further increase our choice of languages for implementation and elevate decoupling.

As Filters often need a quicker, easier way to define small pieces of logic, using [Lua as a scripting language](https://chronosphere.io/learn/control-your-observability-logs-with-ai-lua-and-telemetry-pipeline/?utm_source=TNs&utm_medium=sponsored+content) makes sense.

### Fluent Bit and Stream Processing

The goal of implementing processing logic as events flow through a pipeline is not new. As software frameworks evolved to support that goal, we saw what we now know as stream processing or stream analytics as complex event processing (CEP). You could argue that we’ve had basic stream processing in the form of [service bus](https://www.devx.com/terms/enterprise-service-bus) products for a long time; stream processing is less about the technology and more about how the technology is applied. If you accept the argument about service buses, it is reasonable to assert that Fluentd and Fluent Bit also provide basic streaming capabilities. What has evolved is the way we look at stream processing and stream analytics. Today, we can identify a couple of distinctive characteristics of stream processing and analytics:

* The large volume of data we’re trying to push through the pipeline is a key characteristic of stream processing. Fluent Bit is no stranger to these data volumes, but the volumes we want to process demand an enormous scale for service buses to handle. Also, service buses need to address a level of complexity, such as data integrity across multiple systems, something typically not an issue for stream processing.
* As we focus on data, using SQL is the nearly universal way to work with data. If we can express the examination of the log events using SQL, we make the data a lot more accessible.

You can download the entire book, [“Fluent Bit with Kubernetes.”](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/05/c3489f3d-cropped-ba30d14d-phil-wilkins.jpeg)

Writing for Chronosphere, Phil Wilkins has spent more than 30 years in the software industry, with broad experience in businesses and environments from multinationals to software startups and consumer organizations to consultancy. He started as a developer on real-time, mission-critical...

Read more from Phil Wilkins](https://thenewstack.io/author/phil-wilkins/)