If digital transformation defined the 2010s, the 2020s are all about digital optimization. The explosion of cloud native applications has led to mounting complexity and spiraling cloud costs. Organizations are feeling the pressure — from ballooning observability bills to the challenges of managing telemetry spread across a sea of monitoring tools.

Observability should be a built-in capability of modern infrastructure, not a bolt-on cost center. That’s where [Beyla](https://grafana.com/oss/beyla-ebpf/) came into play. Beyla was an eBPF-based auto-instrumentation agent that captures traces and metrics without requiring any application code changes. But as interest in eBPF-based observability grew across the industry, it became clear that this innovation needed to live somewhere broader than a single vendor.

To ensure that eBPF-based auto-instrumentation could benefit the entire ecosystem, Beyla was contributed to the OpenTelemetry project. Now known as [OBI (OpenTelemetry eBPF-based Instrumentation)](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation), the project continues to evolve in collaboration with the community, furthering our shared goal of making high-quality telemetry accessible to every platform team, regardless of stack or tooling.

This shift is helping redefine how observability fits into developer workflows and platform engineering strategies.

## **eBPF: Bridging the Gap Between Developers and Platforms**

The rise of platform engineering has been a response to the growing burden on developers. While developers want to ship features, the underlying infrastructure has grown more complex than ever, especially in distributed systems. Platform teams aim to tame this complexity by offering paved paths and reusable templates that enforce consistency, security and reliability.

But observability has often remained a sticking point. Developers have had to manually instrument their services, deal with inconsistent libraries across languages and make trade-offs between visibility and overhead. That’s where eBPF — and now, OBI — comes in.

With OBI, the burden of observability shifts from application teams to platform teams. eBPF works at the kernel and user-space level, collecting telemetry without needing access to source code. It observes at the protocol layer, meaning it doesn’t matter which language your services are written in — Rust, Go or Java — you get consistent, high-fidelity data either way.

## **Breaking Down the Language Barriers**

Traditional APM tooling often relies on language-specific agents and runtime hooks that struggle in modern environments, especially with compiled languages or heavily optimized microservices. These approaches often fail to connect the dots between incoming and outgoing requests, leading to fragmented or incomplete traces.

OBI, built on eBPF, sidesteps these limitations by collecting signals at the protocol level. Instead of depending on runtime reflection or code injection, eBPF attaches to system-level events and user-space functions using probes (like uprobes and kprobes). This allows it to observe request flows, track the threading model and understand when and how services communicate, independent of the application’s internal logic.

This produces end-to-end traces without requiring developers to change their code, link additional libraries or manage instrumentation overhead. With the introduction of OBI, this approach also unlocks a powerful new signal: continuous profiling.

## **The Fourth Signal**

Modern observability is often broken down into three signals: metrics, logs and traces. Each has its benefits and drawbacks.

Metrics are cheap, but not as detailed. Logs are very detailed, but expensive. Traces are critical in understanding the behavior of distributed architectures, but are difficult to instrument and costly to store. And with both logs and traces, long-term analysis becomes very pricey.

But increasingly, profiling is emerging again as the fourth signal thanks to eBPF. Because much of the same technology that powers eBPF tracing and metrics can be used to capture CPU and off-CPU profiles, eBPF is a great tool for building profiling tools. Profiling was a foundational tool in early monolithic systems, often used during performance tuning and debugging. As systems shifted to distributed architectures, continuous profiling became harder to implement until eBPF brought it back into reach.

Now, APM vendors are able to use distributed traces to create these continuous profiles, providing platform teams the information they need to optimize cloud environments and better prepare for operational issues. The result? Better decisions, faster incident resolution and clearer opportunities for optimization. When a service starts consuming too much memory, for instance, you don’t just see the spike; you understand exactly which function or thread caused it, and whether it’s tied to a recent deployment.

## **Blended Architectures, Unified Observability**

Let’s be honest, most application environments aren’t fully microservice-based or purely monolithic. They’re somewhere in between. That’s why the most effective observability strategies combine distributed tracing with continuous profiling, unlocking both breadth and depth.

Imagine clicking on a slow span in a trace and immediately seeing the corresponding CPU profile: no guesswork, no context switching. With OBI, organizations are able to move past the pain of instrumentation and into a new era where observability is automatic, integrated and actionable.

With the addition of OBI to OpenTelemetry, it’s poised to become the industry standard for platform teams providing observability to developers: language-agnostic, zero-instrumentation and built for scale. The promise of digital optimization starts with visibility. With OBI, that visibility is finally within reach.

*KubeCon + CloudNativeCon North America 2025 is taking place Nov. 10-13 in Atlanta, Georgia.* [*Register now*](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/10/cc90a365-cropped-c764bd49-screenshot-2025-10-01-at-1.01.30%E2%80%AFpm-600x600.png)

Nikola Grcevski is a principal software engineer at Grafana Labs. Nikola has worked as a software engineer for more than 20 years, mostly with compilers, managed runtimes and performance optimization. Most recently, he has been working on low-level application instrumentation...

Read more from Nikola Grcevski](https://thenewstack.io/author/nikola-grcevski/)