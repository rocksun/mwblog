*By now you’re probably hearing about OpenTelemetry quite often. Maybe you’ve already read the description at **https://opentelemetry.io/docs/what-is-opentelemetry/**. Maybe you’re asking yourself, “that’s a lot of words about metrics, traces, logs, and such — but how do I actually start using this thing?” If that sounds like you, then read on…*
As a set of open standards, OpenTelemetry allows for an entire ecosystem of interoperable tools working on portable telemetry formats. But the interoperability goes beyond just the tools and frameworks that support OTLP (the network protocol used by OpenTelemetry, not to be confused with O **L** TP):

With its vast array of extensions, the **OpenTelemetry Collector** can become a universal translator between all of your telemetry, observability, and monitoring tools — in addition to its more standard role as a pipeline for gathering, processing, and forwarding telemetry.

# What is the OpenTelemetry Collector?
The OpenTelemetry Collector is a deployable binary (written in Golang) that provides an extensible framework for telemetry collection, processing, and forwarding. This is useful for a number of reasons:

- Individual services’ telemetry can be combined, batched, and filtered on the same node or cluster where the service is running, before incurring significant networking costs.
- Configuration of filtering and sampling rules for telemetry can be changed without needing to change or redeploy the services being monitored.
- Extensions can be added to support the translation between any available telemetry formats and backend destination.
With these capabilities the Collector is usually compared to a monitoring agent, but it can do much more than a vendor agent — its extensibility makes it extremely flexible as a pipeline connecting all of our data sources and sinks for telemetry data.

# Plugins
Collector plugins can come in four different forms: receivers, processors, exporters, and connectors.

These plugins are combined into a pipeline for each signal type that is being handled by the collector. The currently available signals are metrics, traces, and logs. *Profiles* as a signal type for continuous performance profiling are currently in development by the community.

**Receivers**** **gather telemetry and can be either pull- or push-based. For example, the default OTLP Receiver can be configured to provide either HTTP or gRPC endpoints where services can send OTLP data; the Prometheus Receiver is configured to scrape specific endpoints similarly to a Prometheus agent.
[ Processors](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor) can filter, mutate, or even add telemetry before it is passed to the next stage in the pipeline. The most important processor is the batch processor which prevents exporters from needing to run continuously. The transform processor is also useful for using
[OTTL](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/pkg/ottl/README.md)(OpenTelemetry Transformation Language) to filter and normalize telemetry before it is saved.
[ Exporters](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter) are the final stage in a pipeline for sending telemetry to downstream processors and databases. Multiple exporters can be combined if necessary, sending some or all telemetry to multiple destinations. Later in this post we will explore the ClickHouse exporter, which can write all telemetry to a SQL-compatible ClickHouse database.
**Connectors**** **are a way to connect the exporter from one telemetry pipeline to a receiver in another pipeline — for example the span metrics connector gathers RED (Request Throughput, Error Rate, and Duration) metrics from exported traces and forwards these metrics to the receiver of a metrics pipeline.
# The Collector as a Hub
By combining the myriad receivers and exporters that are available, we can use the OpenTelemetry Collector as a hub, seamlessly providing a compatibility layer for all of our monitoring technologies and storage and analysis destinations.

# Collector Distributions
Since the Collector is an extensible framework, it is quite common (and encouraged) for organizations to package their own distributions of the Collector. These distributions will typically include a subset of the available community plugins as well as some preset configuration. A distribution may also include unique plugins.

For example, Amazon provides the [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/) which is a Collector-distribution that is pre-configured for gathering metrics, traces, and logs from an AWS environment.

It’s also possible to create your own production-optimized distribution including only the extensions that you require for your use case.

Finally there are a number of off-the-shelf Collector container images available for convenience:

[Core](https://github.com/open-telemetry/opentelemetry-collector-releases/tree/main/distributions/otelcol): lightweight collector versions with minimal plugins[K8s](https://github.com/open-telemetry/opentelemetry-collector-releases/tree/main/distributions/otelcol-k8s): preloaded with plugins specific to Kubernetes[Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib): preloaded with over 90 vendor- and contributor-provided plugins
Which method you choose will depend on your use case. The contrib collector is excellent for proofs-of-concept, while in production a custom-built collector will offer the best performance.

# The OpenTelemetry Collector on Kubernetes
## Deploying the OpenTelemetry Collector on Kubernetes
The official [OpenTelemetry Collector Helm Chart](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-collector) includes the option to deploy the collector as a daemonset, statefulset, or deployment. In our [Kubernetes Cluster Loggging Demo](https://github.com/Altinity/demo-opentelemetry-cluster-logs) we use a `daemonset` so that each Collector instance can gather logs and metrics from its local node.

## Kubernetes Receivers — Gathering Cluster & Node Telemetry
There are a few receivers available for the OpenTelemetry Collector that can gather metrics and logs for a Kubernetes cluster. For example, the [filelog receiver](https://opentelemetry.io/docs/kubernetes/collector/components/#filelog-receiver) can be used to gather cluster logs, and there are also receivers available for [kubelet](https://opentelemetry.io/docs/kubernetes/collector/components/#kubeletstats-receiver) and [cluster](https://opentelemetry.io/docs/kubernetes/collector/components/#kubernetes-cluster-receiver) metrics.

## Resource Attributes — Identifying Application Telemetry
OpenTelemetry uses *resource attributes *to describe infrastructure entities. Telemetry coming from the kubernetes-specific receivers is already tagged with the correct resource attributes, allowing us to identify data points on a node- and pod-level. For applications running in Kubernetes, we can use the [Kubernetes Attributes Processor](https://opentelemetry.io/docs/kubernetes/collector/components/#kubernetes-attributes-processor) to automatically tag incoming application telemetry with the same node- and pod-level descriptors.

# Putting it into Practice
You’ve now got a solid handle on what the OpenTelemetry Collector is and how it could act as the observability “glue” for an environment such as a Kubernetes Cluster. We’ve covered the basics, but we’re just scratching the surface of what’s possible with the OpenTelemetry Collector.

In our next post well introduce [Kubernetes Cluster Logging with ClickHouse and OpenTelemetry](https://altinity.com/blog/kubernetes-cluster-logging-with-clickhouse-and-opentelemetry), we’ll get hands-on with using the Collector to gather logs from a Kubernetes Cluster. I’ll walk you through the setup and configuration, so you can start pulling consistent and complete logs from all of your Kubernetes-based applications and infrastructure. We’ll also introduce Grafana for visualization and ClickHouse for storage, completing an end-to-end monitoring stack based on OpenTelemetry.