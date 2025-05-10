# Grafana’s eBPF Beyla Future Hinges on OpenTelemetry
![Featued image for: Grafana’s eBPF Beyla Future Hinges on OpenTelemetry](https://cdn.thenewstack.io/media/2025/05/bd7a218b-osarugue-igbinoba-t_yhxpigu78-unsplash-1024x576.jpg)
SEATTLE – [Grafana](https://thenewstack.io/why-grafana-needs-opentelemetry/) realized about six months ago that its [eBPF](https://thenewstack.io/what-ebpf-means-for-observability-vs-security/) open source Beyla project was better suited to promote auto-instrumentation through the [OpenTelemetry project](https://thenewstack.io/opentelemetry-whats-new-with-the-second-biggest-cncf-project/). As such, Grafana has decided to donate [Beyla](https://thenewstack.io/wp-admin/post.php?post=22724475&action=edit) to the OpenTelemetry project, which achieved [CNCF](https://cncf.io/?utm_content=inline+mention) Incubating status in 2021.

This donation will extend Beyla — now eBPF [OpenTelemetry](https://github.com/open-telemetry) — as the best way to advance the reach of eBPF for those types of metrics that only it can provide, while also expanding its impact through the broader community, Grafana Labs hopes.

Similar to Grafana’s stewardship and donation of [Prometheus](https://thenewstack.io/prometheus-at-10-whats-been-its-impact-on-observability/), the CNCF’s second-oldest project, eBPF OpenTelemetry is seen as playing a broader role in the proliferation of telemetry data that reaches all the way to the kernel, thanks to eBPF, and extends throughout the network.

eBPF has emerged as a secure method for gathering insights from the kernel. Its reliability has sparked widespread interest in the observability community. A robust, eBPF-based auto-instrumentation solution that integrates seamlessly with the rest of OpenTelemetry has been a longstanding goal.

Continuous profiling is a big deal for

[@opentelemetry]and open source Pyroscope but was previously a “hack version” compared to what it is today under the[@grafana]umbrella, said Ryan Perry at GrafanaCon 2025.[@thenewstack][pic.twitter.com/rBHGYx8SXT]
— BC Gain (@bcamerongain),May 9, 2025
Meanwhile, [Pyroscope](https://pyroscope.io/)‘s ability to support continuous profiling with eBPF was described during the talk, “Why you should care about continuous profiling and how to get started with Profiles Drilldown in Grafana” at [GrafanaCon](https://grafana.com/events/grafanacon/) by [Ryan Perry,](https://www.linkedin.com/in/ryanaperry/) an engineering director, who said profiling is a key element in OpenTelemetry’s development. The pyroscope.ebpf component configures an eBPF profiling job for the current host. The collected performance profiles are forwarded to the list of receivers passed in forward_to.

Accessing key profiling metrics with the Pyroscope database is becoming more integrated through OpenTelemetry, as queries become more standardized and powerful for profile details, said Perry, who was also the CEO and co-founder of continuous profiling tool provider [Pyroscope, which Grafana Labs acquired in 2023](https://grafana.com/blog/2023/03/15/pyroscope-grafana-phlare-join-for-oss-continuous-profiling/).

According to Grafana’s documentation, other Grafana eBPF projects include Grafana Alloy, a lightweight, all-in-one collector that can collect, transform and ship observability data. It supports eBPF-based profiling and auto-instrumentation through components like beyla.ebpf and pyroscope.ebpf. The beyla.ebpf component is a wrapper for Grafana Beyla that uses eBPF to automatically inspect application executables and the OS networking layer, and capture trace spans related to web transactions and RED metrics for Linux HTTP/S and gRPC services.

Grafana’s open source Beyla project offers tracing via eBPF, which is another way to collect traces for [telemetry](https://thenewstack.io/unified-telemetry-observability-the-future-of-data-management/). Its development paralleled that of the OpenTelemetry project’s profiler, the development of which Grafana Labs has been heavily involved in as a major contributor. From the outset, the profiler was useful for users because it goes deeper for observability analysis by extending to the code level. It instrumentalizes a deeper analysis of metrics, traces and logs by extending telemetrics data pulled together in a unified stream that extends to the code level for applications throughout the network. Code is analyzed and stored.

“OpenTelemetry is a pragmatic project built with a focus on efficiency and collaboration. Components are developed from scratch when necessary, but when technically challenging features — such as an eBPF-based profiler or auto-instrumentation — already exist within another organizational member’s working code, and consensus deems it a strong foundation, there is no need to reinvent the wheel,” [Ted Young](https://www.linkedin.com/in/ted-young), programs director for Grafana Labs and OpenTelemetry co-creator, told me on the sidelines of GrafanaCon, Grafana Labs’ annual user conference here. “Utilizing available shortcuts is encouraged when they serve the project’s goals. This approach can sometimes limit efforts to adopt new forms of observability, particularly when the cost of instrumentation is prohibitively high.”

No one wants to have to recompile code and applications separately for each language. As Young described, shortcuts are always sought. In certain languages, such as [Java](https://thenewstack.io/introduction-to-java-programming-language/), effective shortcuts have existed for a long time. The Java agent pattern, for instance, is highly mature, allowing OpenTelemetry’s Java agent to operate without requiring any code changes — just deployment, Young said.

However, the same cannot be said for many other languages. While some auto-instrumentation exists in [Python](https://thenewstack.io/python/), it lacks the formalization and maturity of Java’s. “In languages like JavaScript and [Go](https://thenewstack.io/introduction-to-go-programming-language/), traditional agent-based solutions are nearly nonexistent, yet the demand remains for extracting high-quality data from systems without code modifications,” Young said.

At Grafana Labs, a similar need for eBPF-based auto-instrumentation was identified about a year ago. The organization began developing such a solution independently, driven by a desire to align it with OpenTelemetry as the primary data source. From the start, the goal was to ensure compatibility with OpenTelemetry data standards. This effort led to the creation of a project named “Beyla,” the internal eBPF initiative at Grafana Labs. The solution aligned well with OpenTelemetry’s goals, leading to the idea of donating it to the community to foster vendor-neutral development and encourage broader adoption.

## Big Perception
Relying on the trusted vendor-neutral OpenTelemetry to pull metrics directly from the kernel will extend hooks to connected runtimes throughout the network with eBPF instead of through a vendor (in this case, Grafana). For OpenTelemetry’s goals, eBPF OpenTelemetry will attract more wide-scale adoption and contributions as the project expands to potentially become a de facto way to pull metrics with eBPF auto-instrumentation with eBPF.

“For example, Beyla might contain functionality for easy onboarding with Grafana Cloud or for integrating with Grafana Alloy, our OpenTelemetry Collector distribution with built-in Prometheus pipelines and support for metrics, logs, traces and profiles,” [Nikola Grcevski](https://www.linkedin.com/in/nikola-grcevski-16796717/), principal software engineer at Grafana Labs, wrote in a [blog post](https://grafana.com/blog/2025/05/07/opentelemetry-ebpf-instrumentation-beyla-donation/?utm_source=chatgpt.com).

“One of the barriers to eBPF adoption is perception. Despite being designed as a safe and efficient kernel-level technology, eBPF’s low-level nature raises concerns,” Young said. “However, when the technology is adopted and developed under the umbrella of a trusted, vendor-neutral initiative like OpenTelemetry, those concerns are mitigated by the trust established in the community.”

## eBPF for Security and Performance
Alternatives to eBPF have existed before, yet eBPF allays many security concerns, thanks largely to its isolated design compared to other code (it technically does exist within Linux kernel code, but exists in an outer layer). The concept of low-level system hooks for observability is not new. Previous attempts, however, often involved hacks that introduced risk. Despite companies’ best efforts to secure them, such solutions were inherently unsafe. The legacy of those earlier attempts lingers, contributing to skepticism. With heightened focus on security, trust-building becomes essential. Auto-instrumentation should integrate cleanly with both manual instrumentation and the broader OpenTelemetry ecosystem, producing regularized, uniform data.

Profiling presents a promising area for eBPF-based instrumentation. As a form of auto-instrumentation, profiling offers a different perspective and dataset. Integrating profiling with eBPF techniques within OpenTelemetry could yield powerful insights, particularly as OpenTelemetry’s profiling capabilities mature, Young said.

“For these reasons, it made little sense to silo the eBPF work,” Young said. “A shared, unified community approach offered far greater value than retaining a proprietary, Grafana-specific solution. Convergence around a common eBPF strategy benefits all stakeholders.”

## OpAMP Amps Up
Beyond profiling and eBPF, another area of excitement is the OpenTelemetry control plane protocol, known as [OpAMP](https://opentelemetry.io/docs/specs/opamp/), Young said. “Sampling and cost control are crucial in telemetry, especially at scale. Ideally, the tool responsible for data analysis should also govern how data is collected,” he said. “This allows smarter decisions about sampling and cost optimization to be made directly by the system that understands the analysis needs.”

Manual configuration of sampling parameters is often ineffective. Optimal values depend on system behavior, which can change over time, Young said. Therefore, enabling backend systems to dynamically manage collectors and SDKs offers a nuanced and adaptive approach. OpAMP was developed to support this capability, he said.

“At Grafana Labs, solutions like fleet management and adaptive telemetry within Grafana Cloud demonstrate this principle,” Young said. “The next step is to extend adaptive telemetry to environments like Alloy and integrate it more deeply through fleet management using protocols such as OpAMP.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)