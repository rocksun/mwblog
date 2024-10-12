
<!--
title: eBPF 即将登陆 Windows
cover: https://cdn.thenewstack.io/media/2024/10/0fd9430d-ebpf.png
-->

在 IETF 和微软的帮助下，eBPF 将很快为 Linux 和 Windows 提供跨平台的内核程序兼容性。

> 译自 [eBPF Is Coming for Windows](https://thenewstack.io/ebpf-is-coming-for-windows/)，作者 Joab Jackson。

在上个月的虚拟 [eBPF 峰会](https://youtu.be/PQNDsdP27Hw?list=PLDg_GiBbAx-m7yn_FYcc41PNrgtxlISBK) 上，[Isovalent](https://thenewstack.io/ciscos-strategic-move-in-the-isovalent-acquisition-ebpf/) 的 CTO 以及联合创始人 [Thomas Graf](https://www.linkedin.com/in/thomas-graf-73104547/?originalSubdomain=ch) [谈论了](https://www.youtube.com/watch?v=oVoW5BUBRJk&t=2s) 这个开源 [过滤器转内核引擎](https://ebpfdocumentary.com/) 的未来。他指出，未来将包括微软 Windows。

微软的研究人员已经 [着手](https://github.com/microsoft/ebpf-for-windows) 开发一个适用于 Windows 的 eBPF 版本，也就是说，为 Windows 内核提供类似的 [可编程接口](https://thenewstack.io/linux-technology-for-the-new-year-ebpf/)。

自十年前被纳入内核以来，基于 Linux 的 eBPF [得到了广泛的应用](https://thenewstack.io/ebpf-security-power-and-shortfalls/)，特别是在 [可观测性](https://thenewstack.io/how-bumblebee-eases-ebpf-observability-with-oci/)、[安全](https://thenewstack.io/crowdstrike-a-wake-up-call-for-ebpf-based-endpoint-security/) 和 [合规性](https://thenewstack.io/ebpf-reliable-policy-setting-and-enforcement/) 工具中，这些工具得益于其可编程的在线速度，能够在无需繁琐的模块或危险的内核修改的情况下分析和过滤数据包。

随着 Windows 和 Linux 之间跨平台兼容性的承诺，工具制造商可以编写在两个平台上运行的二进制文件。

## eBPF ... 适用于 Windows

与 Linux eBPF 一样，Windows eBPF 将提供一个沙箱，以便在内核本身内执行小型程序，使用一个隔离的内核内解释器来执行 [eBPF 字节码](https://github.com/microsoft/ebpf-for-windows/blob/main/docs/tutorial.md)，一旦代码 [经过验证](https://github.com/microsoft/ebpf-for-windows/blob/main/docs/debugging.md)。

微软在 GitHub 上发布的项目显示有 43 位贡献者，代码主要用 C 语言编写，[并包含少量 C++ 代码](https://thenewstack.io/can-c-be-saved-bjarne-stroustrup-on-ensuring-memory-safety/)。

Graf 表示，该软件包将带来与 Linux eBPF 的字节码兼容性，并且还将提供类似的解释器和即时编译器来执行字节码。但是，由于 Windows 系统调用存在差异，eBPF 连接到内核的挂钩点可能会有所不同。

![微软 eBPF 架构](https://cdn.thenewstack.io/media/2024/10/0caf680a-windows-ebpf-architecturediagram-1024x788.png)
微软为其适用于 Windows 内核的 eBPF（Windows）提供的架构

Graf 表示，所有为 [Linux eBPF](https://thenewstack.io/what-is-ebpf/) 开发的工具都将在“未来几年”移植到 Windows 环境中。

他警告说，这将给社区带来更多挑战。未来，工具制造商需要确保他们的产品在两种环境中都能正常工作。

因此需要标准化。

## eBPF 标准化

最初，[eBPF](https://thenewstack.io/ebpf/)（现在维护者一致认为不再代表任何意义）是作为一组代码演变而来的；它没有遵循任何预定义的规范，Graf 指出。因此，代码本身“就是标准”，工具制造商必须根据它进行编写。

[互联网工程任务组](https://thenewstack.io/internet-architecture-board-iso-future-networking-tech/) (IETF) 已经 [着手](https://datatracker.ietf.org/wg/bpf/about/) 进行一个项目，以使事情更加稳固，从而尽可能地保证 Windows 和 Linux 之间的“跨平台”兼容性，[Dave Thaler](https://github.com/dthaler) 解释说，他是该工作组的技术顾问，也是微软 eBPF 项目的主要贡献者之一，他在今年早些时候为 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) 的 [存储峰会](https://events.linuxfoundation.org/archive/2024/lsfmmbpf/) 做了 [一次演讲](https://www.youtube.com/watch?v=f2iUQSRBD_M&list=WL&index=7)。

[IETF eBPF 工作组](https://datatracker.ietf.org/wg/bpf/about/) 的首要任务是巩固运行 eBPF 程序的虚拟机的指令集架构 (ISA)。该机构已经 [基本完成](https://datatracker.ietf.org/doc/html/draft-ietf-bpf-isa) 了描述 ISA 的文档，只有一些最后的反馈意见需要处理。

在完成 ISA 工作后，该小组计划还开发一套针对验证器的预期，以保证不受信任的 eBPF 程序的安全执行。验证器应该做些什么来确保代码安全？验证器保证哪些安全属性？对于这项工作，该小组可以借鉴 Linux 内核的 [verifier.rst](https://www.kernel.org/doc/Documentation/bpf/verifier.rst) 来进行 eBPF 验证。

该小组还计划通过 ABI（应用程序二进制接口）规范创建一种用于生成可移植 eBPF 二进制文件的格式，该规范可能基于现有的规范之一。
