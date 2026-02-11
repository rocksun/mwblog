[The Extended Berkeley Packet Filter (eBPF)](https://thenewstack.io/what-is-ebpf/)  has continued on an adoption path that extends its integral role in [observability](https://thenewstack.io/introduction-to-observability/), security, and networking functionality from the kernel to wherever applications and environments are deployed. Since its creation, it has served as a par excellence way to distribute code directly from the kernel and through a sandbox throughout the network. It enables the gathering of information and interaction with code and applications on the network, essentially covering the full scope of any code or application controlled by or connected to the kernel.

Given eBPF’s extensive coverage across environments, including Kubernetes, eBPF has been a boon for observability, [security monitoring](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/) and [networking](https://thenewstack.io/networking/). Between observability and security, there is some overlap, but the use cases with eBPF are largely distinct. For reasons we’ll explore below, eBPF has not yet reached its full potential for either case.

But all of this is largely tied to two things: Everything extends from the [Linux kernel](https://thenewstack.io/linux-6-18-all-about-the-new-long-term-support-linux-kernel/), or extends directly from the Linux kernel, and it was designed for x86 CPU configurations. Recently, it was announced — amid much ado — that eBPF would extend to Windows systems. Why anybody would want to run their servers on Windows is beyond me, but it remains a legacy system that many organizations are still content with.

## ARM and RISC-V

The project developers and maintainers of the eBPF project have also extended eBPF to ARM configurations. Meanwhile, the Mac M3 processors and the open source RISC-V processor configurations remain in development.

That was the subject of [Yuning Liang](https://archive.fosdem.org/2025/schedule/speaker/yuning_liang/), founder and CEO of DeepComputing, and my talk at [FOSDEM](https://fosdem.org/2026/) last weekend, “[eBPF Observability on RISC: What Works, What Breaks, and How to Test It](https://fosdem.org/2026/schedule/event/8SRBCB-ebpf_observability_on_risc_what_works_what_breaks_and_how_to_test_it/).” Before the talk, I canvassed the status of eBPF for ARM and RISC-V configurations.

“eBPF has been transformative, and also right that much of the ecosystem implicitly grew up in an x86\_64 world. And while designed to be architecture-agnostic, once you leave the spec and hit real kernels, real JITs, and real workloads, differences show up quickly, especially around verifier behavior, helper availability, and performance characteristics,” [Nikola Grcevski](https://ca.linkedin.com/in/nikola-grcevski-16796717), principal software engineer at Grafana Labs, tells *The New Stack*.

“Where I’d add nuance is that this doesn’t mean the eBPF promise is failing – it means it’s being stress-tested. ARM has already shown that the model can scale beyond x86 when there’s enough production pressure. RISC-V is now the clearest signal of what’s left to do,” Grcevski said. “In that sense, your framing is accurate: ‘write once, run anywhere’ isn’t a guarantee today, and RISC-based observability is precisely where the remaining gaps (and opportunities) are most visible.”

## Transition period

I agree that we are currently in a transition period where “write once, run anywhere” faces friction on RISC-V. However, characterizing it as “unpredictably incomplete” overlooks the structural work being done to close these gaps.

The eBPF Foundation and the kernel community are actively moving eBPF from being a “Linux-specific feature” to a standardized industry specification, [Bill Mulligan](https://www.linkedin.com/in/bamulligan), a [Cilium](https://cilium.io/) and eBPF community pollinator for [Isovalent](https://isovalent.com/) at [Cisco](http://cisco.com/?utm_content=inline+mention), tells *The New Stack*. With the recent standardization of the eBPF instruction set via the Internet Engineering Task Force ([RFC 9669](https://www.ietf.org/blog/bpf-rfc9669/)), there is now a formal contract for what eBPF is, independent of the underlying hardware. This suggests that the fragmentation you describe is not a fundamental flaw, but rather a temporary maturity gap that is closing rapidly as RISC-V JITs (Just-In-Time compilers) align with this new standard, Mulligan says.

“The eBPF Foundation is funding work to bring the different architectures on par with one another. It’s important not to paint all non-x86 architectures with the same brush. ARM64 has effectively graduated,” Mulligan says. “Thanks to the massive adoption of Graviton and Ampere, ARM is now a first-class citizen in the cloud native world. RISC-V is where the real frontier lies.”

An organization gets started with a sandbox project experimenting with eBPF for observability and security on a RISC-V system by treating it as a learning sandbox rather than a production experiment,” Grcevski says.

“The process begins by anchoring on a known RISC-V kernel to make its capabilities explicit. One then starts small with one observability and one security use case using libbpf and CO-RE — focusing on concrete tasks like syscall latency and execve tracking,” Grcevski tells *The New Stack*. “Finally, the loop is closed early by expecting to read kernel and JIT code, documenting gaps as they are found, and upstreaming minimal repros…I agree with this perspective because while eBPF bytecode is technically universal, the implementation is highly dependent on the host architecture’s specific JIT compiler and kernel maturity.”

Grcevski added:

* JIT Parity: The JIT compiler for x86\_64 is the gold standard; ARM64 is nearly there, but RISC-V is still catching up. If the JIT doesn’t support a specific instruction or helper, the “agnostic” nature of the code becomes irrelevant.
* Memory Models: RISC-V and ARM64 use different memory consistency models compared to x86. This can lead to subtle bugs in complex eBPF programs that rely on specific memory ordering for concurrency.
* Production Pressure: As noted by Grcevski, the ecosystem improves where the money and traffic are. As RISC-V moves into the data center, these gaps will close, but we are currently in the ‘wild west’ phase of that transition.”

Meanwhile, the differences in how JIT compilation maturity between ARM64 and RISC-V impact the CPU overhead of high-frequency profiling compared to traditional x86 deployments “is all about the ecosystem flywheel,” Mulligan says. “ARM64 is already spinning at full speed while RISC-V is just starting to spin that wheel. We aren’t seeing fundamental blockers, just the natural lag of a newer ecosystem catching up to decades of head start,” he notes.

Because ARM64 has a generous number of general-purpose registers, the performance is often indistinguishable from x86, Mulligan adds. The JIT  for RISC-V is younger which can sometimes result in more verbose instruction sequences compared to mature x86/ARM implementations. In high-frequency profiling (e.g., 10k+ events/sec), this results in slightly higher CPU usage per probe execution, Mulligan says. “This is often due to less optimized generation in the JIT compiler,” he adds.

## Primary bottleneck

Meanwhile, given the current gaps in RISC-V kernel helper support, is the primary bottleneck to eBPF adoption on new architectures is a lack of upstream development or a lack of standardized testing frameworks? “The answer is a bit of both: the eBPF Foundation is looking at making investments in bringing the RISC-V JIT compiler up to par with x86/ARM. The kernel community is also eager to support RISC-V,” Mulligan says.

The other problem is that most testing happens on the [Quick Emulator](https://www.qemu.org/), which emulates functionality but hides hardware-specific timing quirks, cache behavior, and JIT edge cases, Mulligan says. “We need a more standardized framework where eBPF patches are automatically tested on physical RISC-V silicon (not just emulators) alongside x86/ARM runners,” Mulligan notes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)