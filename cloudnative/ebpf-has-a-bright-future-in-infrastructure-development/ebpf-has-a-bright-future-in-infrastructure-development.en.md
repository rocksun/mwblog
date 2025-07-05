For the next decade, eBPF will be “a strategic platform choice for infrastructure developers,” predicted [Cisco](http://cisco.com/?utm_content=inline+mention) Distinguished Software Engineer [Daniel Borkmann](http://borkmann.ch/), in a keynote [talk](https://ossna2025.sched.com/event/23B1m/keynote-ebpf-unlocking-innovation-in-the-linux-kernel-daniel-borkmann-distinguished-software-engineer-isovalent-at-cisco-and-co-creator-of-ebpf-and-cilium) at the [Linux Open Source Summit](https://ossna2025.sched.com/) about the state of the technology he helped create, including some prognostication of how it could be used in future times.

eBPF is revolutionary because it shortens development cycles of getting new technologies into the kernel, Borkmann posited. Until now, getting some sort of extension added to the Linux kernel has taken years, with scant assurance of success. Now, eBPF allows users to [add their own kernel technologies](https://thenewstack.io/how-ebpf-turns-linux-into-a-programmable-kernel/).

“We are going from a long innovation cycle to a short innovation cycle,” said Borkmann, who has also been a 15-year Linux core committer. And more providers of infrastructure tools are taking advantage of the in-kernel technology.

eBPF is good at fine-tuning performance across the stack, from networking to the CPUs themselves, providing a better user experience. It’s also good at implementing policies.

Meta’s Facebook uses eBPF extensively in its Layer 4 load balancer, with 100 different eBPF applications doing various tasks. It is used in all Android phones for security policies and traffic control and for bridging to IPv6 networks.

## eBPF for Virtual Machines

In the realm of networking, the eBPF-based [Netkit](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/net/netkit.c) driver has [proved popular](https://thenewstack.io/bytedance-to-network-a-million-containers-with-netkit/) for identifying namespaces within the kernel itself, formerly the task of the much slower network drivers.

This work actually began in the Kubernetes community, as a way to minimize container communication latency, Borkmann said. Borkmann participated in the [Cilium project](https://thenewstack.io/supercharge-service-mesh-with-ebpf-and-cilium/), a network packet processor built on eBPF.

“As soon as we landed this in the Linux kernel, the hyperscalers also got interested, and they rolled this out into their fleet,” Borkmann said. For instance, Meta managed to shave its [P99 latency](https://thenewstack.io/p99conf-how-ebpf-could-make-faster-database-systems/) for namespace resolution from 12 seconds down to 100 milliseconds using Netkit.

The next step will be to bring eBPF to the world of [virtual machines](https://thenewstack.io/vmware-vcf-9-0-finally-unifies-container-and-vm-management/).

Many organizations now have two platforms, one based on Kubernetes and an older legacy-based one based on virtual machines (VMs). Each has its own monitoring, metrics and logging.

eBPF could help consolidate these two worlds, Borkmann said. Currently, work is underway to integrate NetKit into [KubeVirt](https://kubevirt.io/), which allows users to manage virtual machines as Kubernetes pods.

[![](https://cdn.thenewstack.io/media/2025/07/d60a6997-oss-ebpf-slide-01.png)](https://cdn.thenewstack.io/media/2025/07/d60a6997-oss-ebpf-slide-01.png)

Netkit could optimize the network throughout.

## eBPF for the Kernel

You can think of eBPF as a “universal assembly language,” Borkmann said, though it is one most developers will never see, opting for an interface to their programming language of choice.

Two major just-in-time compilers (LLVM and GCC) support a variety of front-end languages (C, Rust, etc), which they convert into eBPF bytecode. The instruction set [has been standardized](https://datatracker.ietf.org/group/bpf/about/) by the IETF Working Group (allowing for a version of [eBPF for Windows](https://thenewstack.io/ebpf-is-coming-for-windows/)). There’s a verifier to ensure user code doesn’t destabilize the system.

Another use case for eBPF has been to optimize the kernel itself.

Process scheduling is another emerging use case that benefits from a new Linux kernel utility, [sched-ext](https://github.com/sched-ext/scx/), which [enables](https://thenewstack.io/bpf-opens-a-door-to-linux-dynamic-scheduling-maybe-with-rust/) the creation of an eBPF-based kernel thread scheduler.

Hyperscalers such as Meta and Google are already using eBPF-based schedulers. Fine-grained scheduling policies have optimized these companies’ workloads by 10% or so.

SteamOS also uses an eBPF scheduling approach to optimize gaming.

eBPF could help in AI workload balancing: What part of the AI stack is chewing up resources? An eBPF-based flamegraph would show the full call graph. The longer the bar, the more cycles are being chewed up.

Finally, Borkmann suggested that eBPF could set the stage for live patching the kernel, where it would provide safety checks for the patches being applied.

[![](https://cdn.thenewstack.io/media/2025/07/95ddf2d6-oss-ebpf-slide-02.png)](https://cdn.thenewstack.io/media/2025/07/95ddf2d6-oss-ebpf-slide-02.png)

*Disclosure: The Linux Foundation paid for the reporter’s trip to the Open Source Summit.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 25 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)