# Kloudfuse 3.0: an All-in-One Observability Platform Emerges
![Featued image for: Kloudfuse 3.0: an All-in-One Observability Platform Emerges](https://cdn.thenewstack.io/media/2024/11/ed331c01-kloudfuse-logo-1024x576.png)
SALT LAKE CITY — The reason there are relatively few observability vendors is that the barrier to entry is very high.

Unlike the legions of single-pane-of-glass platforms for [Kubernetes](https://roadmap.sh/kubernetes), security and testing, [observability](https://thenewstack.io/observability/) requires more significant development and investment across numerous fronts. Observability platforms must extend to all aspects of a network and comprehensively cover diverse environments across all stack layers. They’ve got to meet an organization’s specific needs, especially for maintaining operational security and ensuring robust software delivery.

This comprehensive demand is one reason why a startup like [Kloudfuse](http://www.kloudfuse.com) is worth examining, as it positions its platform to compete against those of established companies like [Datadog](https://www.datadoghq.com/?utm_content=inline+mention), Grafana, [Honeycomb.io](https://www.honeycomb.io/?utm_content=inline+mention), [New Relic](http://newrelic.com/?utm_content=inline+mention) and others.

With customers including GE Healthcare, India-based online drugstore Tata 1MG, and Workday, the startup is off to a good start with its release, which it is introducing at [KubeCon+CloudNativeCon North America ](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)this week.

## What Kloudfuse Offers
More established observability platforms have certain advantages. Grafana has those beautiful panels and works wonderfully with [Prometheus](https://thenewstack.io/prometheus-at-10-whats-been-its-impact-on-observability/), the open source monitoring tool. Datadog attempts to cover it all, offering any observability functionality an organization may seek at scale. Observability platforms today must demonstrate integration with [OpenTelemetry](https://thenewstack.io/why-the-latest-advances-in-opentelemetry-are-significant/), [generative AI,](https://thenewstack.io/ai-powered-observability-picking-up-where-aiops-failed/) and, increasingly, [eBPF for observability](https://thenewstack.io/ebpf-meaner-hooks-more-webassembly-and-observability-due/) across any stack layer extending from the [Linux kernel](https://thenewstack.io/linux-kernel-6-12-prepped-for-superior-scheduling-real-time-ops/).

Kloudfuse has attempted to cover these bases in its platform and offer more.

Standout features that Kloudfuse offers include new datastreams designed to improve upon the “three pillars of observability” — [metrics, logs and traces](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/) — for when they fall short. Through Kloudfuse’s metrics, events, logs and traces (MELT) framework, [Kloudfuse 3.0](https://www.kloudfuse.com/product-launch/kloudfuse3.0) also offers frontend observability features, including real user monitoring and session replays.

Since the release of Kloudfuse 1.0 early this decade, Kloudfuse has sought to anchor its platform with an [observability data lake,](https://thenewstack.io/key-trends-shaping-the-observability-market/) recognizing the need to pull all observability telemetry data into a single location.

![Architecture of the Kloudfuse observability platform.](https://cdn.thenewstack.io/media/2024/11/73e694f1-kloudfuse-architecture-1024x474.png)
The architecture of Kloudfuse’s observability platform. (Source: Kloudfuse)

“Recognizing the fragmentation in the market and the challenges developers face with manual issue resolution, we launched our initial version to capture metrics and logs within a single platform. Our vision was to integrate additional observability streams as we continued to expand,” Kloudfuse’s [Krishna Yadappanavar](https://www.linkedin.com/in/krishnayadappanavar/), co-founder and CEO, [Pankaj Thakkar,](https://www.linkedin.com/in/pankaj-thakkar-51343719/) co-founder and CTO, and[ Ashish Hanwadikar,](https://www.linkedin.com/in/ashishh/) co-founder and chief architect, wrote in a [post on their company blog.](https://www.kloudfuse.com/blog/unveiling-kloudfuse-3-0)

“Early client feedback confirmed that this approach significantly reduced the mean time to detect issues by correlating metrics with underlying logs, streamlining the workflow for engineering and DevOps teams.”

With the release of Kloudfuse 3.0, the company has introduced a number of new features. The key capabilities, according to the company, include:

**Digital experience monitoring (DEM).**The new real user monitoring (RUM) feature (mentioned previously) provides insights into user experiences across all stacks, covering frontend to backend traces, logs and metrics.**Continuous profiling.**This profiling capability enables developers to identify otherwise hidden performance bottlenecks and enhance code quality in real time. By automatically evaluating CPU utilization, memory allocation and disk I/O, it helps to ensure optimal performance for every line of code while minimizing resource use and costs.**Data lake provided.**Since the release of Kloudfuse 1.0, Kloudfuse has sought to anchor its platform with an observability data lake, recognizing the need to pull all observability telemetry data and to capture metrics and logs within a single platform.**Advanced AI analytics capabilities.**Kloudfuse 3.0 offers the addition of[Prophet](https://github.com/facebook/prophet)for anomaly detection and forecasting to provide more accurate results, effectively managing irregular time series that include missing values, such as gaps from outages or low activity. This results in less tuning and improved forecasts, even with limited training data.**K-Lens.**Kloudfuse’s K-Lens uses outlier detection to analyze thousands of attributes, identifying those causing specific issues. It accelerates debugging and incident resolution with actionable insights and clear visualizations, such as heatmaps and multi-attribute chart series.**FuseQL language.**The introduction of a powerful log query language with advanced capabilities, multi-dimensional aggregations and filters, addresses the limitations of log-query languages such as LogQL.**Facet analytics.**Leveraging Kloudfuse’s patent-pending LogFingerprinting technology, which automatically extracts key attributes from logs for faster analysis and troubleshooting, this feature provides advanced search, filtering, bookmarking and grouping options, thus significantly boosting log analysis.
For scaling needs, Kloudfuse 3.0 includes:

**Log archival and hydration.**This feature provides immediate access to historical logs for compliance and regulatory needs, while reducing long-term storage costs. Logs are stored in cost-effective, compressed formats within the customer’s own storage.**Cardinality analysis and metrics roll-ups.**Cardinality analysis offers real-time insights into incoming metrics, logs and traces, enabling organizations to discover and reduce high-cardinality data proactively, which reduces storage and processing costs. Metrics roll-ups aggregate data, enhancing query performance and lowering mean time to resolution.
While not discussed as much as other features, Kloudfuse customers retain data sovereignty for both data storage and real-time monitoring, which not all competitors offer. It does not charge for storage because the customer provides their own.

Kloudfuse includes data shaping and transformation capabilities, and long-term storage that the customer manages; the platform is used to analyze the data without the customer having to forgo data sovereignty. A single data lake can scale infinitely, while continually training large language models for improved AI-assisted data analysis.

## Observability: Intense Competition
While Kloudfuse offers broad-ranging capabilities and some unique features, it must also contend with intense competition, as observability tools are not commodities and must clearly differentiate themselves. The established players seek to offer observability tools in their platforms to reduce costs, largely by optimizing resources.

So does Kloudfuse. It allows customers to control the data before it reaches the observability analysis — which can become very cost-intensive during troubleshooting— and a virtual private cloud (VPC) deployment model (which Grafana also offers), to control costs even further. A VPC deployment can also help avoid data transfer/egress files that companies typically pay in order to work with a Software as a Service observability vendor.

Kloudfuse will have to continually deliver new observability features that cover all of what the established players offer — and more. Ease of use and integration must be more than just as good as what the competition offers.

Thanks to the unification of telemetry data, developers using Kloudfuse do not need to manually correlate the query results from logs to traces, to metrics, etc.

Kloudfuse is set up to handle infinite scaling and volumes of data so that customers do not pay extra data when troubleshooting, for example. Customers can have the freedom to run numerous queries, which they would otherwise have to pay for if they had not deployed an observability platform under their direct control in their own VPC.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)