[Google Cloud’s](https://cloud.google.com/?utm_content=inline+mention) engineers have enabled Google Cloud Observability, and specifically [Cloud Trace](https://cloud.google.com/trace/docs/overview), to support the [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otel/protocol/) ingest for near-direct and more vendor-neutral ingestion of trace data.

Now that users can send their trace data using OTLP via the Telemetry (OTLP) API, Google Cloud recommends this approach in many cases, including for users who anticipate high volumes of trace data when paired with the [OpenTelemetry Collector](https://thenewstack.io/why-the-latest-advances-in-opentelemetry-are-significant/). Google’s adoption and integration of the protocol has involved significant engineering work, and metrics and logs have separate OTLP support paths and availability that vary by product and region.

In the meantime, Google’s approach is similar to those of [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure and [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention). Without requiring third-party tools or vendors, Azure and AWS support OTLP as well, covering Azure Monitor OTel support, AWS Distro for OpenTelemetry and X-Ray OTLP ingest.

## Key Benefits of Native OTLP Integration

Defined as a data exchange protocol designed to transport telemetry from a source to a destination in a vendor-agnostic fashion, OTLP support for Google Cloud Observability reduces the prior requirement for developers to integrate vendor-specific exporters in many cases, according to [Google documentation](https://cloud.google.com/learn/what-is-opentelemetry). This helps ensure that the core telemetry pipeline remains standardized and readily interoperable across OTLP-supporting observability backends when appropriately configured.

The core relationship is defined by Google as eliminating a necessary conversion step, shifting complexity from the client side (the Collector) to the cloud backend, according to Google.

[![Diagram showing how Google cloud observability itegrates with the OpenTelemetry Protocol.](https://cdn.thenewstack.io/media/2025/10/047495d8-google-cloud-otlp-1024x576.png)](https://cdn.thenewstack.io/media/2025/10/047495d8-google-cloud-otlp-1024x576.png)

This diagram shows how both in-process and collector-based configurations can use native OpenTelemetry Protocol exporters to communicate telemetry data. (Source: Google Cloud)

[A Google Cloud blog post](https://cloud.google.com/blog/products/management-tools/opentelemetry-now-in-google-cloud-observability/) published in September, authored by company product managers [Sujay Solomon](https://www.linkedin.com/in/sujay-solomon/) and [Keith Chen](https://www.linkedin.com/in/keith-chen-a4640679/), noted the benefits of the OTLP integration to send tracing data. Those benefits include:

* **Vendor-neutral telemetry pipelines:** The use of native OTLP exporters from in-process or collectors eliminates the need to use vendor-specific exporters in your telemetry pipelines, according to the Google post.
* **Telemetry data integrity:** Assurances that telemetry data maintains the OpenTelemetry data model during transmission and storage without transformations into proprietary formats.
* **Interoperability with your choice of observability tooling:** The ability to send telemetry to one or more observability backends that support native OTLP without additional OTel exporters.
* **Reduced client-side complexity and resource usage:** The ability to shift telemetry processing logic, such as applying filters to the observability backend, reducing the need for custom rules and thus client-side processing overhead with Google Cloud Observability.

## A New Role for the OTel Collector in Google Cloud Observability

[![Screenshot from the trace explore page in Cloud Trace.](https://cdn.thenewstack.io/media/2025/10/e7da2810-google-cloud-trace-explorer-1024x576.png)](https://cdn.thenewstack.io/media/2025/10/e7da2810-google-cloud-trace-explorer-1024x576.png)

The trace explore page in Cloud Trace, with the fields that use OpenTelemetry semantics highlighted. (Source: Google Cloud)

The recent addition of native OTLP ingestion in Google Cloud Observability is directly, critically related to the [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/), as it fundamentally changes the Collector’s primary role and configuration for Google Cloud Observability. The obvious benefit described above is the removal of the conversion step, so there is comparatively minimal configuration involved for the Collector to ingest tracing data from Google Cloud Observability backend.

OpenTelemetry Collector is used to serve as a filter to monitor telemetrics. It is applicable for whenever multiple applications or [microservices](https://thenewstack.io/introduction-to-microservices/) are involved, particularly for security considerations. As such, an OpenTelemetry Collector falls under the category of an observability agent. Prior to this announcement, users might use observability agents, such as [Fluent Bit](https://thenewstack.io/fluent-bit-core-concepts/), Vector and others to ingest tracing data with Google Cloud Observability.

## The Role of Observability Agents and Data Collection

Observability agents play a critical role in the nuts and bolts workings of [observability](https://thenewstack.io/introduction-to-observability/). They handle data transport to ensure telemetry data is transmitted accurately. Agents typically offer data collection, data processing and data transport, playing a critical role in monitoring system performance. They help in identifying unknown unknowns to troubleshoot and mitigate performance issues before they become problems. That’s the golden standard of observability functionality.

In this way, an observability agent, when used for data collection, collects data sent to it from one or many sources. In addition to receiving data, it sends data to an endpoint, such as for visualization with a [Grafana](https://thenewstack.io/grafanas-cto-on-the-state-of-the-observability-market/) panel. An agent can be configured to collect certain types of logs, traces and metrics for observability.

Initially, you can opt not to use an observability agent, if you’re already deploying an application that is instrumented to send telemetry data directly to the observability platform. The collectors can be useful when monitoring an application that can’t be instrumented.

Without observability collector functionality, configuring each backend or user monitoring separately for those is required, which can be cumbersome. On the contrary, an observability collector serves as a single endpoint for all microservices, streamlining access to applications and microservices through a unified point facilitated by the collector. Utilizing an observability agent to serve as a collector, you can view and manage microservices collectively, offering a consolidated view on a platform like Grafana. While Grafana provides certain alternatives without an OpenTelemetry collector, the collector significantly simplifies this process.

## The Status of OTLP Support for Logs and Metrics

It should be noted that Google Cloud’s announcement is about [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) for tracing. Logs and metrics, and especially logs, remain a work in progress due to a number of potential hurdles, including implementation of role-based access controls (RBAC), compliance concerns and the engineering work required.

At this time, Azure and Google Cloud, among the top three cloud vendors and hyperscalers, directly support metrics ingest through OpenTelemetry over the OTLP protocol. AWS commonly uses the AWS Distro for OpenTelemetry (ADOT) Collector. AWS and Google Cloud do not have broadly available direct OTLP logs ingest, while Azure’s logs ingest through OTLP remains largely limited.

## Google’s Strategy for a Simplified Telemetry Pipeline

Again, this is part of ongoing development in the race to integrate and improve observability data ingest among the hyperscalers, as Google’s Solomon and Chen wrote in their company blog post.

Google Cloud Observability’s recent move, they wrote, “is a cornerstone of our strategy to simplify telemetry management and foster an open cloud environment. We understand that in today’s complex cloud environments, managing telemetry data across disparate systems, inconsistent data formats, and vast volumes of information can lead to observability gaps and increased operational overhead.

“We are dedicated to streamlining your telemetry pipeline, starting with focusing on native OTLP ingestion for all telemetry types so you can seamlessly send your data to Google Cloud Observability. This will help foster true vendor neutrality and interoperability, eliminating the need for complex conversions or vendor-specific agents.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)