# eBPF Is Coming for Windows
![Featued image for: eBPF Is Coming for Windows](https://cdn.thenewstack.io/media/2024/10/0fd9430d-ebpf-1024x683.png)
At the virtual [eBPF Summit](https://youtu.be/PQNDsdP27Hw?list=PLDg_GiBbAx-m7yn_FYcc41PNrgtxlISBK) last month, [Thomas Graf](https://www.linkedin.com/in/thomas-graf-73104547/?originalSubdomain=ch), who is CTO and cofounder of [Isovalent](https://thenewstack.io/ciscos-strategic-move-in-the-isovalent-acquisition-ebpf/), [talked about the future](https://www.youtube.com/watch?v=oVoW5BUBRJk&t=2s) of the open source [filter-turned kernel engine](https://ebpfdocumentary.com/). And that future includes Microsoft Windows, he noted.

Microsoft researchers have embarked [on a project](https://github.com/microsoft/ebpf-for-windows) to make a version of eBPF for Windows, which is to say give the Windows kernel a similar [programmable interface](https://thenewstack.io/linux-technology-for-the-new-year-ebpf/).

Since its inclusion in the kernel a decade ago, the Linux-based eBPF [has found widespread adoption](https://thenewstack.io/ebpf-security-power-and-shortfalls/), particularly for [observability](https://thenewstack.io/how-bumblebee-eases-ebpf-observability-with-oci/), [security](https://thenewstack.io/crowdstrike-a-wake-up-call-for-ebpf-based-endpoint-security/) and [compliance](https://thenewstack.io/ebpf-reliable-policy-setting-and-enforcement/) tools that benefit from its programmable in-line speed to analyze and filter packets without the need for cumbersome modules or dangerous kernel modifications.

With the promised cross-platform compatibility between Windows and Linux, tool makers can write binaries that run on both platforms.

## eBPF … For Windows
Like the Linux eBPF, Windows eBPF will offer a sandbox to execute small programs within the kernel itself, using an enclaved in-kernel interpreter to execute [eBPF bytecode](https://github.com/microsoft/ebpf-for-windows/blob/main/docs/tutorial.md), once the code [is verified](https://github.com/microsoft/ebpf-for-windows/blob/main/docs/debugging.md).

The Microsoft project, captured on GitHub, shows 43 contributors, with the code mostly written in C, [with a smattering of C++](https://thenewstack.io/can-c-be-saved-bjarne-stroustrup-on-ensuring-memory-safety/).

The package will bring bytecode compatibility with Linux eBPF, Graf said, and also feature a similar interpreter and just-in-time compiler for bytecode execution. But the hook points where eBPF connects to the kernel may differ, given the differences with the Windows system calls.

![Microsoft eBPF architecture.](https://cdn.thenewstack.io/media/2024/10/0caf680a-windows-ebpf-architecturediagram-1024x788.png)
Microsoft’s architecture for its eBPF for Windows kernel (Windows)

All the tooling that has been done for the [Linux eBPF](https://thenewstack.io/what-is-ebpf/) will also be ported over to Windows environs “in the coming years,” Graf said.

He warned that this will bring more challenges to the community. Going forward, tool makers will need to ensure that their wares work in both environments.

Hence the need for standardization.

## eBPF Standardization
Originally, [eBPF](https://thenewstack.io/ebpf/) (which, the keepers now agree, no longer stands for anything) evolved as a set of code; it did not follow a pre-defined specification that it was implementing, Graf pointed out. As a result, the code itself “is the standard” that the tool makers must write to, he said.

The [Internet Engineering Task Force](https://thenewstack.io/internet-architecture-board-iso-future-networking-tech/) (IETF) has embarked on a project to solidify things a bit more, as to guarantee as much “cross-platform” compatibility between Windows and Linux as possible, explained [Dave Thaler,](https://github.com/dthaler) a technical advisor for the working group who is also one of the main contributors to the Microsoft eBPF project, in [an earlier presentation](https://www.youtube.com/watch?v=f2iUQSRBD_M&list=WL&index=7) this year for the [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)‘s [Storage Summit](https://events.linuxfoundation.org/archive/2024/lsfmmbpf/).

The first task of [IETF eBPF Working Group](https://datatracker.ietf.org/wg/bpf/about/) plans to solidify the Instruction Set Architecture (ISA) for the virtual machine that runs the eBPF programs. The body has [largely finished](https://datatracker.ietf.org/doc/html/draft-ietf-bpf-isa) the document that describes ISA, minus some last call feedback.

After the ISA work is finished, the group plans to also develop a set of expectations for the verifier, which guarantee the safe execution of untrusted eBPF programs. What should a verified do to ensure code is safe? What security properties does a verifier guarantee? For this work, the group can build from the Linux kernel’s [verifier.rst](https://www.kernel.org/doc/Documentation/bpf/verifier.rst) for eBPF.

The group also plans to create a format for producing portable eBPF binaries via an ABI (application binary interface) specification, perhaps based on one of those already existing.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)