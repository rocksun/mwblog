# Honeycomb.io’s Austin Parker: OpenTelemetry In-Depth
![Featued image for: Honeycomb.io’s Austin Parker: OpenTelemetry In-Depth](https://cdn.thenewstack.io/media/2024/08/81a2400e-opentelemetry-1024x683.png)
![Headshot.](https://cdn.thenewstack.io/media/2025/01/f726e698-austin-parker-honeycomb.jpg)
Austin Parker.

OpenTelemetry is a [framework ](https://opentelemetry.io/docs/what-is-opentelemetry/)and toolkit designed to create and manage telemetry data such as [traces](https://opentelemetry.io/docs/concepts/signals/traces/), [metrics](https://opentelemetry.io/docs/concepts/signals/metrics/), and [logs](https://opentelemetry.io/docs/concepts/signals/logs/). OpenTelemetry is currently the [second most active project](https://all.devstats.cncf.io/d/1/activity-repository-groups?orgId=1) of the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention), surpassed only by [Kubernetes](https://thenewstack.io/Kubernetes/).

At [Kubecon+CloudNativeCon North America 2024](https://thenewstack.io/kubecon-keynotes-wrestle-with-ai-governance-complexities/) in Salt Lake City, we caught up with [Austin Parker](https://www.linkedin.com/in/austinlparker/), director of [open source](https://thenewstack.io/open-source-in-2025-strap-in-disruption-straight-ahead/) at [Honeycomb](https://www.honeycomb.io/?utm_content=inline+mention), to discuss the state of [observability](https://thenewstack.io/Observability/) in general and OpenTelemetry in particular.

Parker is a co-founder of the [OpenTelemetry project](https://opentelemetry.io), and a member of the OpenTelemetry Governance Committee. As a community leader for OpenTelemetry, he passionately supports and mentors people in the community to become active contributors themselves.

**Can you please introduce yourself, provide a brief background of your initial encounter with observability and its intersection with Kubernetes, and your current work in the area?**
I’ve been a part of OpenTelemetry since its inception, formerly working on OpenTracing, and currently serve as a member of the governance committee. I’ve been working in the observability space for nearly a decade now — both as an end-user, trying to implement it for my team, and now as a contributor trying to build the next generation of observability. Similarly, I’ve been in the cloud-native space for about as long, formerly working on platform-as-a-service right around the time Kubernetes started to take off, so I’ve been interested in the convergence of these things for quite some time.

**Before we dive into OpenTelemetry, can you clarify the relationship between Kubernetes Observability in general and OpenTelemetry in particular?**
Observability for Kubernetes is fully supported by OpenTelemetry (OTel). Foundational Kubernetes telemetry data, such as metrics for resource utilization to monitor the performance of Kubernetes clusters, as well as instrumentation libraries for custom application observability, are fully supported by OTel.

Also, full interoperability of the OpenTelemetry Protocol (OTLP) with the [Prometheus protocol](https://thenewstack.io/creating-a-path-for-prometheus-success/) enables users to leverage Prometheus metrics using OTel. Furthermore, the OTel Collector has a Kubernetes attribute processor to add Kubernetes metadata, which can be used to collect metrics from the Kubernetes API server. Traces and logs from Kubernetes clusters can also be easily collected and processed using OpenTelemetry.

**What challenges have you faced in integrating OpenTelemetry with Kubernetes, particularly in terms of context propagation and data collection?**
Most of the challenges in integrating OpenTelemetry with Kubernetes aren’t necessarily specific to Kubernetes, although they are exacerbated in some ways. The biggest challenge is, easily, data management. [Clusters](https://thenewstack.io/scaling-to-10000-kubernetes-clusters-without-missing-a-beat/) can be anywhere from tens to tens of thousands of nodes, and even a small cluster can produce an overwhelming amount of metrics and logs depending on your workloads. Context propagation challenges are often related to instrumentation issues, as well, which may require cooperation and coordination between multiple teams to investigate.

Often, the best way to address these challenges is developing a plan for them before you even start. Create realistic goals and objectives around what data is important to collect. Identify smaller clusters, or workloads, to deploy OpenTelemetry against rather than attempting to ‘boil the ocean’ and making sweeping changes.

**Can you discuss your approach to scaling OpenTelemetry within a large Kubernetes environment, especially regarding performance and resource usage?**
This can be a complex topic, so let’s talk about it from the top. Resource utilization is going to vary based on workload, cluster type and size, signals collected, and many other factors. Your goal is to balance these, while making tradeoffs between telemetry resolution, telemetry availability, and query performance. These tradeoffs are often influenced — directly or indirectly — by the rest of your observability stack. Let’s take a quick example, around pod logs and metrics. Are you exposing custom metrics via Prometheus, or are you turning scraped logs into metrics? What level of correlation do you need between your different signals? Are your logs solely for debugging, or do you derive customer-facing data from them?

All of these questions will influence your collection setup — for instance, if reliability of log telemetry is the most important thing, then you would want to run sidecar collectors to scrape logs, then feed those logs to a gateway for further processing. You would want to run a separate logging gateway, rather than trying to colocate log processors with metric, or trace processors. You may find that tracing provides most of the utility that metrics and logs provide you, with the tradeoff being slightly increased resource usage by a service. There aren’t hard-and-fast rules about this because much of it depends on your application architecture and your observability backend.

**How does OpenTelemetry integrate with other observability tools in your Kubernetes stack, and what benefits or challenges have you encountered?**
Generally, OpenTelemetry integrates well with other observability tooling, especially if those tools support OpenTelemetry Protocol (OTLP). You can use Collectors to act as a “central hub” in each cluster to collect and normalize data from existing Prometheus or fluentd deployments, or use OpenTelemetry metrics as inputs to autoscalers with the appropriate adapters.

One popular pattern I’ve seen is to use OpenTelemetry to create “local” cluster monitoring stacks that centralize all telemetry across a single cluster and then use the routing functionality of the Collector to emit crucial metrics, logs, and traces to a third-party solution. If you need full fidelity, you access the “local” observability stack via a proxy.

**What best practices would you recommend for instrumenting Kubernetes-native applications with OpenTelemetry?**
Given that OpenTelemetry is built on a rich, distributed context layer the key practice to ensure successful observability of your k8s-native applications is to build with this in mind. Ensure that services are built with tracing, either using instrumentation agents or through native instrumentation, in order to propagate context throughout your application.

Avoid over-reliance on custom application metrics — often, the data that you’re interested in can be captured as span attributes — this helps to control costs and ensure that your observability spend is linear rather than exponential. Be sure to take advantage of newer features in Kubernetes, like API Server and Kubelet tracing, especially if your application interacts with these APIs to scale.

**How do you handle the deployment and management of OpenTelemetry agents in a dynamic Kubernetes environment?**
Depending on the exact needs of your application, there’s a lot of different options available to you. In general, though, you want to consider two separate types of agents.

The first is the instrumentation agent that is responsible for adding and generating telemetry from your code, and the second is the collection agent that processes and exports it. In OpenTelemetry, the former is any of our zero-code instrumentation agents, and the latter is the OpenTelemetry Collector.

Instrumentation agents can be managed most easily through the OpenTelemetry Operator, which allows you to create and assign instrumentation to pods via annotations in your deployment. Helpfully, the Operator also offers a custom resource to manage Collector deployments as well, allowing you to create and define DaemonSets, StatefulSets, sidecar deployments, or others.

Typical Kubernetes workloads can use a DaemonSet that ensures a collection agent is available on each node, which is responsible for scraping local metrics and logs as well as receiving data from pods scheduled to that node. Often, for workloads with complex telemetry processing, collection sidecars will be deployed with pods to act as local receivers for data.

This is a good option for scheduled or burst services, where you want to ensure that telemetry gets out of the process as soon as possible and you don’t want to deal with the additional overhead of processing and filtering it in-process. To manage all of these instrumentation and collection agents, look to control planes that support the OpenTelemetry Agent Management Protocol ([OpAMP](https://opentelemetry.io/docs/specs/opamp/)) — this is a standard way to get or set configuration, monitor the health of your various agents, and handle updates.

**Can you share a specific case where observability in Kubernetes/OpenTelemetry helped you identify and resolve a critical issue?**
Effective alerting on Kubernetes services can dramatically reduce the amount of time needed in order to discover the contributing factors to an incident. Earlier this year, we discovered an unexpected race condition in our database involving a long-running query that happened to execute simultaneously with a migration. This race condition caused a table to lock for reads, which resulted in the connection pools exhausting across our infrastructure. Our telemetry identified the problem in multiple ways — we were able to see that the rate of failing requests increased, which triggered automatic notifications.

This led us to notice that many pods were in a crash loop (as Kubernetes was scaling to try and handle the retrying requests), which we could easily correlate with errors in the database connection pool. Thanks to OpenTelemetry, and our own observability platform, we were able to discover the relationship between the offending database cluster and our database migration, as our CI/CD is also instrumented with OpenTelemetry. All in all, we were able to detect the incident within seconds of the initial anomalous performance issue and respond within minutes, reducing downtime. Helpfully, even though this database was a critical one for our platform, we only suffered a partial degradation of service for our customers, thanks to Kubernetes.

**Can you provide details about the recent announcement that ****OpenTelemetry is expanding**** into continuous integration/continuous deployment?**
The promise of OpenTelemetry is a single standard for telemetry data, regardless of cloud, programming language, or system type. We’ve actually seen users implement it in CI/CD for several years now and are excited to see community efforts to improve semantic conventions and context propagation for these use cases. This effort should result in improved interoperability as well as increased support for OpenTelemetry in CI/CD platforms.

**Finally, can you tell us a bit about the future of OpenTelemetry in general?**
OpenTelemetry has emerged as a clear and unambiguous standard for multi-modal observability data in cloud-native systems. In the near future, the project is delivering support for continuous profiling of workloads, and introducing a new set of semantic conventions for structured events to aid in creating standard telemetry for front-end clients, generative AI systems, Kubernetes lifecycle signals, and many more.

I anticipate that the adoption of OpenTelemetry as a native part of frameworks, libraries, cloud systems, and language standard libraries will only increase as the project becomes increasingly stable and mature. In the future, I believe we’ll see OpenTelemetry further expand into new domains — user analytics, business events, developer productivity, carbon emissions and resource cost, to name a few — and allow for correlation between these and underlying performance data, in order to unlock new insights and help developers, operators, and business leaders to better understand the relationship between these factors.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)