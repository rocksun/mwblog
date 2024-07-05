# Elastic Profiling Agent Offers a 4th Pillar of Observability
![Featued image for: Elastic Profiling Agent Offers a 4th Pillar of Observability](https://cdn.thenewstack.io/media/2024/06/eda61053-ahmed-vblx61xdb2m-unsplash-1-1024x683.jpg)
The acceptance of [Elastic’s continuous profiling agent](https://github.com/open-telemetry/community/issues/1918) by the [OpenTelemetry](https://thenewstack.io/opentelemetry-gaining-traction-from-companies-and-vendors/) profiling community is arguably a formality, but it will set the stage to realize what is possible for the profiling agent. Thanks to the signaling capabilities it offers, the agent could set the stage for a so-called fourth pillar of [observability](https://thenewstack.io/observability/) alongside [traces, logs and metrics](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/).

OpenTelemetry’s profiling agent should prove to be useful for users because it provides deeper observability analysis by extending to the code level, [Austin Parker,](https://www.linkedin.com/in/austinlparker/) director of open source for [Honeycomb](https://www.honeycomb.io/?utm_content=inline+mention), explained. It instrumentalizes a deeper analysis of metrics, traces and logs by extending telemetric data pulled together in a unified stream, which extends to the code level for applications throughout the network. Code is analyzed and stored, Parker said.

“Continuous profiling with OpenTelemetry has been available to the public to some degree for over six years,” Parker said. “With the addition of the profiling agent to OpenTelemetry, we expect continuous production profiling to hit the mainstream.”

In practice, this means that when a problem arises, or when looking at certain performance aspects that an observability data stream offers — such as when a CPU is running slow or when an end user’s request for data is taking too long — the profile discerns the code at issue, Parker said. “With the right additional tools for observability, fixes should be provided faster, as users will pinpoint problem code more easily through their queries,” he said.

[Continuous profiling](https://thenewstack.io/grafana-shows-new-observability-projects-at-observabilitycon/) is a technique used to understand the behavior of a software application by collecting information about its execution over time, OpenTelemetry creators and contributors [Bahubali Shetti](https://www.linkedin.com/in/billshetti/) (Elastic), [Alexander Wert](https://www.linkedin.com/in/alexanderwert/) (Elastic), [Morgan McLean](https://www.linkedin.com/in/morganmclean/) (Splunk) and [Ryan Perry](https://www.linkedin.com/in/ryanaperry/) (Grafana) explained in a [blog post](https://opentelemetry.io/blog/2024/profiling/). In this way, continuous profiling covers tracking the duration of function calls, memory usage, CPU usage and other system resources along with associated metadata, they wrote.
“This contribution not only boosts the standardization of continuous profiling for observability but also accelerates its adoption as a key signal in OpenTelemetry,” the OpenTelemetry project creators and contributors wrote. “Customers benefit from a vendor-agnostic method of collecting profiling data correlating it with existing signals, like tracing, metrics and logs, opening new potential for observability insights and a more efficient troubleshooting experience.”

The donation is more than just a formality, [Abhishek Singh,](https://www.linkedin.com/in/abhiksingh/) general manager of observability at Elastic, said. This is because “significant code and IP is being contributed here that works in a language-agnostic way to profile the whole system. It is the most comprehensive in the market and deployed in enterprises,” Singh said.

As an example, a large Elastic customer realized that an agent deployed by its vendor was consuming more resources than expected, “resulting in millions of dollars of compute being wasted across their fleet,” Singh said. “OpenTelemetry did not have the capabilities to profile any process outside of the application where instrumentation was done and even those capabilities were limited,” Singh said.

The Elastic profiling agent is notable for being a production-ready product that we can integrate into our existing tool ecosystem, Parker said. “This accelerates our ability to get profiling in the hands of users, integrate it with existing signals and get crucial feedback on how it can improve,” Parker said.

Elastic’s donation fills in a gap that the OpenTelemetry project’s profiler was previously lacking. This is where the role of [eBPF](https://thenewstack.io/what-is-ebpf/) — which Elastic’s profiler uses — is paramount since eBPF allows for telemetrics to be scraped directly from the [Linux kernel](https://thenewstack.io/rust-in-the-linux-kernel/) and can extend throughout the network. eBPF helps to eliminate the need for third-party and proprietary code instrumentation (run-time/bytecode), recompilation or service restarts. The overhead is low, with less than 1% of CPU consumption and low memory usage in production environments, according to the project creators.

All told, the Elastic’ contribution is important because Elastic provides “whole system profiling” with eBPF, “which not only allows users to profile their applications processes but all running processes,” Singh said. “This is important because users can tie back code changes to performance degradation and see if there are other things running on the system that impact performance, such as third-party agents.”

The project’s creators highlighted specific benefits to OpenTelemetry that the continuous profiling agent offers:

**Provides detailed insights**: Continuous profiling data complements the existing signals (traces, metrics and logs) by providing detailed and code-level insights on the services’ behavior.**Improves fidelity and depth**: Seamless correlation with other OpenTelemetry signals such as traces, increasing fidelity and investigatory depth.**Anticipates environmental impact**: Combining profiling data with OpenTelemetry’s resource information (i.e., resource attributes) allows teams to derive insights into the services’ carbon footprint.
Through a detailed breakdown of services’ resource utilization, profiling data provides actionable information on performance optimization opportunities.

According to the project’s documentation, the continuous profiling agent provides support for a wide range of runtimes and languages, such as:

- C/C++
- Rust
- Zig
- Go
- Java
- Python
- Ruby
- PHP
- Node.js / V8
- Perl
- .NET
## Big Work
OpenTelemetry contributors will continue to collectively work on one of the more dynamic open source projects. Company contributors include Datadog, Grafana, Honeycomb, New Relic, Splunk and others.

“OpenTelemetry, as a project, succeeds due to the contributions of our community, regardless of their affiliation. We deeply appreciate the work that engineers from all over the world, and from many different vendors, put into the project each month,” Parker said. “Building a vendor-agnostic framework for cloud native observability is bigger than any one company, and it’s great to see that the community has responded so positively to it.”

Datadog is a main contributor to the development of the OpenTelemetry profiler and to the OpenTelemetry project. The company will continue to contribute to the profiler’s features, as well as to other aspects of the OpenTelemetry project, and to making the observability experience better for both when using Datadog.

“With this unified agent, you can then decide where the data should be sent, providing flexibility and completeness in your monitoring and observability strategy,” Datadog’s [Yrieix Garnier](https://www.linkedin.com/in/yrieixgarnier/fr), a product leader, said. “You had to run things in parallel to create collectors, then create an exporter to the data backend. Now, it’s like having one tool to push everything inside, in whatever format.”


[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)