# Strobelight: Meta’s eBPF Profiler Framework for Massive Infra
![Featued image for: Strobelight: Meta’s eBPF Profiler Framework for Massive Infra](https://cdn.thenewstack.io/media/2025/03/f405a7c5-strobelight-1024x676.jpg)
Imagine, if you will, that you’re in charge of monitoring all of [Meta’s massive infrastructure](https://thenewstack.io/how-meta-is-reinforcing-its-global-network-for-ai-traffic/). It’s a scary thought isn’t it? Now, in a groundbreaking development, Meta’s engineering team has successfully leveraged [eBPF](https://thenewstack.io/what-is-ebpf/) technology to enhance their fleetwide profiler, [Strobelight](https://engineering.fb.com/2025/01/21/production-engineering/strobelight-a-profiling-service-built-on-open-source-technology/).

When I say “enhance,” I don’t mean some minute improvement that only a dedicated performance engineer could love. No, I mean a “[20% reduction in CPU cycles](https://ebpf.foundation/case-study-metas-strobelight-leverages-ebpf-to-reduce-cpu-cycles-and-server-demands-by-up-to-20/), equating to a 10-20% reduction in the number of required servers for Meta’s top services.” That’s a serious savings in compute, which equals a serious saving in money.

Strobelight, Meta’s fleetwide profiler framework, is designed to provide comprehensive profiling capabilities across the company’s large-scale infrastructure. It’s made up of multiple subprofilers that collect various types of performance data, including CPU, GPU, and memory profiles. The framework’s number one job is to identify performance bottlenecks and optimize resource utilization across Meta’s fleet of machines.

The key to Strobelight’s recent success lies in integrating eBPF. It enables efficient, low-overhead monitoring and system event tracing directly within the Linux kernel. By [leveraging eBPF](https://thenewstack.io/bytedance-to-network-a-million-containers-with-netkit/), Strobelight can now collect performance data with minimal impact on system resources.

To be exact, according to the [eBPF Foundation](https://ebpf.foundation/), [eBPG enables Meta to track CPU time](https://ebpf.foundation/case-study-metas-strobelight-leverages-ebpf-to-reduce-cpu-cycles-and-server-demands-by-up-to-20/) spent in function calls and execution paths; call stacks for native and non-native languages (e.g., Python, Java, and Erlang); off-CPU time and service request latency analysis; and AI/GPU profiling and memory tracking.

## eBPF for the Savings
Besides, saving compute time and cash, the use of eBPF in Strobelight has led to, the [eBPF Foundation](https://ebpf.foundation/) claims, 15,000 servers’ worth of annual capacity savings from a single one-character code change. Color me impressed. It’s also enables faster debugging and performance analysis. This allows engineers to prevent regressions before they reach production.

With eBPF, [Strobelight can now track GPU memory allocations](https://www.youtube.com/watch?v=5xAghByteYc) and detect memory leaks more efficiently. According to [Riham Selim](https://www.linkedin.com/in/riham-s/), a Meta software engineer, eBPG enables at any point of time how memory allocation is happening for each GPU,

Mind you, eBPF isn’t perfect. Selim noted. It lacks visibility into GPU internals; the sheer volume of data can be overwhelming; and it lacks application-specific understanding. So, for example, you’ll need to add observability code to a [PyTorch program](https://thenewstack.io/official-pytorch-documentary-revisits-its-past-and-its-future/) rather than relying on eBPF alone.

So, it’s important to understand that Strobelight is far more than just eBPF. According to Meta, “Strobelight is … not a single profiler but an orchestrator of many different profilers (even ad-hoc ones) that runs on all production hosts at Meta, collecting detailed information about CPU usage, memory allocations, and other performance metrics from running processes.”

Indeed, all together Strobe Light has 42 different profilers. Most, but not all of these, are based on eBPF.

## Safe Injection of Custom Code
So it is that, eBPF is vital for Strobelight. The Meta engineers note, “eBPF allows the safe injection of custom code into the kernel, which enables very low overhead collection of different types of data and unlocks so many possibilities in the observability space that it’s hard to imagine how Strobe Light would work without it.”

Don’t ask me, how you could do it. I know a thing or two about [observability](https://thenewstack.io/observability/) and, without [eBPF](https://thenewstack.io/ebpf/). I wouldn’t even know where to start. Fortunately, since we have eBPF, we needn’t worry about this.

Want to try it for yourself? You can. Most of StrobeLight was recently open sourced under the Apache 2 License. However, Meta has yet to open source Strobelight’s profilers and libraries. The company promises it will do this since by opening them up they’ll become “more robust and useful.” Be that as it may, there’s already enough open here to make Strobelight worth exploring for anyone that wants to keep a weather eye on massive infrastructure systems.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)