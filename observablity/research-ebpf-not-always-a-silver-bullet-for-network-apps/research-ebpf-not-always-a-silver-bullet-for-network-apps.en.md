A research paper in the latest issue of the [Proceedings of the ACM on Networking](https://dl.acm.org/journal/pacmnet/charter) cast doubt on the performance superiority of eBPF, at least in terms of accelerating network-based workloads.

In many cases, eBPF brings no considerable performance benefit, and sometimes can even slow an application, pointed out four researchers in the paper, “[Demystifying Performance of eBPF Network Applications](https://dl.acm.org/doi/10.1145/3749216),”

“In reality many networked applications cannot benefit from eBPF, and worse the use of eBPF can limit how applications are deployed,” wrote the authors of the paper, [Farbod Shahinfar](https://dl.acm.org/author/Shahinfar%2C+Farbod) and [Sebastiano Miano](https://dl.acm.org/author/Miano%2C+Sebastiano), both from the  Politecnico di Milano, Milan, Italy; New York University’s [Aurojit Panda](https://dl.acm.org/author/Panda%2C+Aurojit); and [Gianni Antichi](https://dl.acm.org/author/Antichi%2C+Gianni) Politecnico di Milano, Milan & Queen Mary University of London.

[eBPF](https://thenewstack.io/ebpf-has-a-bright-future-in-infrastructure-development/) is a technology to [embed programming code](https://thenewstack.io/what-is-ebpf/) directly into an operating system kernel itself, via sandbox and pre-compilation, with the idea that it could run code faster than that code could run in a user-space program that communicates back and forth with the kernel. Code to run on eBPF is compiled to a platform-independent bytecode and compiled at load time.

[![chart](https://cdn.thenewstack.io/media/2025/09/6ed35240-ebpf-demystifying-01.png)](https://cdn.thenewstack.io/media/2025/09/6ed35240-ebpf-demystifying-01.png)

Lifecycle of an eBPF program (PACMNET)

eBPF has found an early home in [many networking functions](https://thenewstack.io/performant-and-programmable-telco-networking-with-ebpf/), such as load-balancing, packet-switching, and network acceleration protocols, where it is used to filter and route packets and telemetry data.

## Questioning eBPF’s Performance Claims

The researchers established a series of benchmarks to test whether eBPF’s [much-touted performance gains](https://thenewstack.io/how-ebpf-turns-linux-into-a-programmable-kernel/) were indeed realized.

In other words, the researchers wanted to know, if you embedded eBPF into your network application, would it go faster?

They found that in fact, offloading code does not always lead to performance gains.

“We found that whether or not application performance improves depends on how much of the logic can be offloaded,” they wrote.

In some cases, they found improvement, but in others, using eBPF made scant difference. And in some cases, eBPF actually made performance even more sluggish, not only for its application, but other applications around it.

## Benchmarking Different eBPF Offload Types

The researchers set up and instrumented three different types of eBPF-based application. One ran entirely within eBPF (“**full offload**“). Another offloaded just the most time-sensitive part of the code (“**fast-path offload**“) — think of [database caches](https://thenewstack.io/p99conf-how-ebpf-could-make-faster-database-systems/). And the third used eBPF to pre-process data (“**pre-processing offload**“).

The tests were run on two interconnected 24-core Intel Xeon servers interconnected with 100 Gbps links, and outfitted with 1.1MB of L1 cache, 30MB of  
L2 cache, and 36MB of L3 cache, as well as 128GB of DDR4 memory. They both ran Linux kernel version 6.8.0-rc7. [Clang](https://clang.llvm.org/index.html), v 14, compiled the bytecode, targeting [eBPF Instruction Set Architecture v. 3](https://docs.kernel.org/bpf/clang-notes.html).

With **full offload**, the results were mixed. Apps that operate on individual packets benefited, though apps that operate on streams or messages don’t appear to be improved by routing through eBPF.

It turns out the eBPF ISA does not support a lot of the processor features, such as Single-Instruction-Multiple-Data (SIMD), cryptography offloads, or floating point operations. As a result, some of the complex messaging operations actually run faster in user space.

Researchers tested the **fast-path offload** with [BMC](https://www.usenix.org/conference/nsdi21/presentation/ghigoff), an eBPF program for accelerating a Memcached key-value store.

Here, they found that benefits depend greatly on the type of workload BMC is managing. A lot of the traffic is being offloaded to BMC will indeed see faster performance times. But if most of that traffic needs to be handled by user-space code, any benefits are minimal at best.

For the **pre-processing offload**, the researchers found that an eBPF program could potentially reduce data movement by pre-processing requests. But it would not necessarily significantly improve the performance of the application itself.

[![Chart](https://cdn.thenewstack.io/media/2025/09/59bb8264-ebpf-demystifying-02.png)](https://cdn.thenewstack.io/media/2025/09/59bb8264-ebpf-demystifying-02.png)

Reducing packet size does not significantly increase throughput. (PACMNET)

## The ‘Noisy Neighbor’ Effect of eBPF Applications

The researchers found other troubling news, namely that eBPF-based applications can make for unfriendly neighbors on the server. By dominating the OS kernel, they hamper the performance of other applications running on that same server. eBPF was designed for Linux, and mostly used there, but a [Windows version](https://thenewstack.io/ebpf-is-coming-for-windows/) is afoot as well.

“Applications using eBPF might violate performance isolation,” the research team wrote.

## Recommendations for Improving eBPF Technology

There are several things that the keepers of eBPF could do to alleviate the ills of their technology, the researchers advise.

One is to refine the just-in-time compilation, which, due to the limits of the OS kernel, often produces sub-optimal code. Even common  actions such as copying to and from memory (e.g., memcpy) are done in an inefficient manner, slowing any potential optimization.

To a certain extent, the keepers of eBPF are stuck, in that this problem would not be easily fixed, “since doing so would add significant complexity into the kernel,” the researchers observed.

Still, they could refine their process for generating machine code. The eBPF ISA could be expanded, including a much-called-for increase in the number of registers supported.

Also suggested was adding schedulers and buffers, and implementing prefetching of data.

With these enhancements, eBPF can truly address a broad array of use cases that would benefit from better performance, the researchers concluded.

The [Association for Computing Machinery](https://www.acm.org/about-acm) (ACM) is a volunteer-led scientific computing society, aiming to advance computing as a science and a profession.

The [eBPF Foundation](https://thenewstack.io/ebpf-finds-a-home-with-a-new-foundation/) did not return a request for comment.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)