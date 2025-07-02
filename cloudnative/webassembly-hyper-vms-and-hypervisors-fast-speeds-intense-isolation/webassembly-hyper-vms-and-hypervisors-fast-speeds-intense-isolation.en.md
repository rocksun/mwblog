[Hypervisors](https://thenewstack.io/4-reasons-devops-engineers-still-rely-on-hypervisors/) offer substantial security through hardware-based isolation. For an additional layer of isolation within a hypervisor environment, [Hyperlight](https://thenewstack.io/microsofts-hyperlight-webassembly-for-vms-is-open-source/) — a lightweight [virtual machine manager (VMM)](https://thenewstack.io/microsoft-open-sources-openvmm-rust-powered-vm-monitor/) designed to be embedded within applications — enables safe execution of untrusted code within micro VMs with very low latency and minimal overhead. For even further isolation and improved latency, [WebAssembly](https://thenewstack.io/webassembly/) (Wasm) binaries offer substantial security via software-fault isolation (SFI).

In this article, we look at what happens when you combine WebAssembly with Hyperlight — a model that integrates not just the Wasm sandbox and not just the hypervisor sandbox, but both in congruence, providing defense in depth. The Wasm sandbox runs inside the hypervisor sandbox to execute Wasm binaries, Microsoft Engineer [Danilo (Dan) Chiarlone](https://github.com/danbugs) told me.

[![](https://cdn.thenewstack.io/media/2025/06/6bcf3e01-screenshot-2025-06-30-at-5.14.56%E2%80%AFpm-1024x453.png)](https://cdn.thenewstack.io/media/2025/06/6bcf3e01-screenshot-2025-06-30-at-5.14.56%E2%80%AFpm-1024x453.png)

At the [Cloud Native Rejekts](https://cloud-native.rejekts.io/) conference in London in March, Chiarlone and [Mikhail Krinkin](https://www.linkedin.com/in/mikhail-krinkin-57892a86/?locale=en_US) — who is also a Microsoft engineer — discussed during their talk, [“Wasm, Envoy, and Hyperlight Walk Into a Pod: No Vulnerabilities Allowed,”](http://cfp.cloud-native.rejekts.io/cloud-native-rejekts-europe-london-2025/talk/VKB9XD/) how WebAssembly works with hypervisors using Hyperlight as a micro-vm manager and a use case of it in extending [Envoy](https://thenewstack.io/envoy-gateway-offers-to-standardize-kubernetes-ingress/) network filters.

“The key difference to highlight is the difference in isolation methods. WebAssembly (Wasm), as the newer technology, provides its own sandboxing mechanism,” Chiarlone said. “In contrast, Hyperlight leverages hypervisor technologies, which have been in use for a long time and are often required for running third-party code in public cloud environments.”

## Isolation Total

[![](https://cdn.thenewstack.io/media/2025/06/64a9a2c2-screenshot-2025-06-30-at-5.15.10%E2%80%AFpm-300x283.png)](https://cdn.thenewstack.io/media/2025/06/64a9a2c2-screenshot-2025-06-30-at-5.15.10%E2%80%AFpm-300x283.png)

When creating Hyperlight applications, you have a host and a guest. Guest applications are what run inside of a Hyperlight sandbox, like the Wasm sandbox and a Wasm binary. By default, Hyperlight applications provide no functionality to a guest. For security, they are completely secluded from the outside world. Due to this, a host must explicitly provide whatever functionality a guest needs. In the talk’s example, the host provides the networking necessary for a guest to communicate data back to an Envoy.

End to end, the interaction is as follows: (1) The embedding application creates a Hyperlight Wasm sandbox prepared to execute an Envoy Network Filter guest; (2) the embedding application calls into the isolated guest to compute over data; (3) the guest calls back into the host after supposedly manipulating the data in some way.

[![](https://cdn.thenewstack.io/media/2025/06/a10eab5d-screenshot-2025-06-30-at-5.15.32%E2%80%AFpm-1024x346.png)](https://cdn.thenewstack.io/media/2025/06/a10eab5d-screenshot-2025-06-30-at-5.15.32%E2%80%AFpm-1024x346.png)

Hyperlight has a rich type system to allow communication between a guest and a host. One practical consideration is the possibility of circumventing the said type system by using vector bytes for all data, Krinkin said. Tools such as Protocol Buffers or [FlatBuffers](https://github.com/google/flatbuffers) can be employed for serialization and deserialization, allowing developers to pass data in and receive any desired interface, without delving into the specifics of the Hyperlight type system, Krinkin said.

Hyperlight is written in “pure Rust,” which introduces several considerations, Krinkin said. For instance, boilerplate code is necessary to enable interoperability between [Rust](https://thenewstack.io/rust-programming-language-guide/) and [C++](https://thenewstack.io/introduction-to-c-programming-language/), as host-guest calls occur bidirectionally. While the amount of boilerplate is not insignificant, it is also not especially complex, and therefore not a major issue, Krinkin said.

One surprising — but ultimately predictable —aspect is that a Hyperlight host is multithreaded, Krinkin said. As of version 0.5.0, Hyperlight spawns a new thread to execute a sandbox, establishing a one-to-one relationship between a thread and a micro-vm. This has posed particular challenges for Envoy, which, like many networking applications, is asynchronous and callback-based, Krinkin said. “Most processing in Envoy occurs on a single thread, minimizing the need for locking,” Krinkin said. “Consequently, accessing Envoy data structures from a different thread is problematic, as Envoy relies heavily on thread-local storage. In such cases, access attempts often return null or fail altogether.”

Additional boilerplate was introduced to reroute all callbacks to the Envoy worker thread, ensuring proper access to Envoy’s data structures, Krinkin said. “This is a crucial integration consideration,” Krinkin said.

While not directly an integration issue, Hyperlight offers a mechanism called a “call context” where multiple guest function calls can be made without resetting state between each call. With the call context, the embedding application must explicitly call “finish” to reset state.

Without a call context, when a call is made to a guest, and that guest initializes data — such as memory segments or other structures — all such state is lost when the guest call ends. Any subsequent call starts with a clean slate. This imposes limitations on the functionality that can currently be placed within Hyperlight Wasm. “This behavior is easy to overlook, but it significantly impacts design decisions,” Krinkin said.

A basic performance benchmark was presented to demonstrate the implications of these characteristics. The benchmark involved an Echo function, which performs minimal logic: sending a fixed-size payload of random data to Envoy and measuring the round-trip time for the response, Krinkin said. “This was repeated multiple times to calculate average latency and variability,” Krinkin said. “The payload size was also varied to assess its effect on performance.”

For the benchmark, several implementations were compared: Hyperlight Wasm, a native Hyperlight guest without Wasm (no WebAssembly runtime involved), and a Proxy-Wasm implementation of similar Echo functionality. “While the Proxy-Wasm variant is not a perfect apples-to-apples comparison, it provides a useful reference point,” Krinkin said. “This distinction was apparent to most viewers of the accompanying presentation, and it was explicitly acknowledged.”

[![](https://cdn.thenewstack.io/media/2025/06/59790834-screenshot-2025-06-30-at-5.16.31%E2%80%AFpm-1024x646.png)](https://cdn.thenewstack.io/media/2025/06/59790834-screenshot-2025-06-30-at-5.16.31%E2%80%AFpm-1024x646.png)

“Hyperlight’s current performance is suboptimal. However, this is recognized as a starting point, not a destination. Initial profiling led to optimizations in the Hyperlight native implementation. Specifically, while Hyperlight Wasm actively wipes out state between calls — an expensive operation — Hyperlight native can bypass this step, yielding a runtime improvement of approximately 15%,” Krinkin said. “Additional low-hanging optimization opportunities remain, and some overhead may also stem from suboptimal integration. Benchmark results showed that increasing the payload from 128 bytes to 4 kilobytes — a 30x increase — resulted in greater runtime, though the effect was marginal relative to overall system overhead.”

Meanwhile, recent development benchmarks on Hyperlight show significant improvements (upwards of 50% on guest function calls) from when these tests were run.

## The Hyperlight Sum

During the demo, Krinkin achieved what he said was  “defense in depth,” and the implementation was relatively straightforward, Krinkin said. “However, performance is currently lacking and presents a major area for improvement,” Krinkin said.

Work is underway to develop a C API for Wasm, easing integration into non-Rust codebases, Krinkin said. (Hyperlight core offers a C API, just not Hyperlight Wasm currently.) Integration of Hyperlight Wasm as an additional Proxy-Wasm engine is also planned. Proxy-Wasm is Envoy’s native framework for executing WebAssembly plugins and already supports multiple engines, such as V8. Hyperlight could become one of these supported engines, Krinkin said.

“Performance will be a key focus. Although many simple optimizations remain, deeper profiling and instrumentation will also be needed. Current tools do not readily expose performance overhead within the guest, making it difficult to analyze,” Krinkin said. Developing tooling to make Hyperlight execution more transparent will be essential. Finally, since the intended use case of Hyperlight involves sandboxing relatively small computations, the sandbox’s overhead becomes more significant as the computational workload decreases — therefore, optimizing Hyperlight’s performance is critical.”

With performance improvements underway, Hyperlight is distinguishing itself in providing an extra layer of hardware isolation on top of Wasm’s software isolation, bringing to it with a level of security that is needed for certain environments (e.g., public clouds) and providing it with tools for micro-vm life cycle management and execution while still being easily pluggable into any user application as a library. To learn more about recent developments, check out the [Hyperlight repository](https://github.com/hyperlight-dev/hyperlight).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)