# FOSDEM 2025：Rust 在 Linux 中蓬勃发展，尽管面临强烈反对

![Featued image for: FOSDEM 2025: Rust Runs Riot in Linux Despite Backlash](https://cdn.thenewstack.io/media/2025/02/1d3d9a33-img_9596-1-1-1024x683.png)

[Rust](https://thenewstack.io/big-moments-in-rust-2024/) 最终应该取代 [C code](https://thenewstack.io/the-obfuscated-c-code-competition-returns/) 在 [Linux kernel](https://thenewstack.io/rust-in-the-linux-kernel/) 中。问题是，你必须等待几十年才能实现。但在短期内，预计会看到 Rust 代码激增，为 Linux 提供支持，从边缘设备到微软的 Xbox——尽管包括一些 Linux 内核维护者在内的许多人对此并不满意。

Rust 在内核中日益普及，并且早已证明其在 Linux 内核和其他领域的各种用例中优于 C，尤其是在内存安全方面。然而，Rust 并非没有相对于内核中 C 语言的风险，更不用说它非常陡峭的学习曲线。越来越多的开发人员和内核维护人员喜欢 Rust，但内核开发社区中存在着支持 Rust 和支持 C 阵营之间的争论，这种争论在本周持续进行，双方进行了激烈的交流。

[@fosdem]25：让我们这样说吧，对于[@rustlang]在[@Linux]内核中的地位，存在许多强烈的观点，正如 Rust for Linux 的 Miguel Ojeda 所描述的那样，包括细微差别和注意事项。[pic.twitter.com/qYOUzB2fBG](pic.twitter.com/qYOUzB2fBG) — BC Gain (@bcamerongain)

[February 1, 2025]

Rust 相关的动态是 [FOSDEM (Free and Open Source Developers’ European Meeting)](https://fosdem.org/) 的一个主要讨论主题，这是一个由志愿者在布鲁塞尔自由大学 (ULB) 组织的领先开源会议。在数十个与 Rust 相关的演讲中，由 [Miguel Ojeda](https://www.linkedin.com/in/ojedamiguel/?originalSubdomain=es) 做的同名演讲 [Rust for Linux](https://rust-for-linux.com/) 脱颖而出，他负责维护该项目，并且是 Linux 基金会技术咨询委员会的成员。除了讨论 Rust for Linux 项目外，他还介绍了发行工具链的状态、Rust 的稳定性，以及重要的是，你如何为内核的开发做出贡献。Rust for Linux 计划还在与 GCC 和其他组织合作，以促进在 Linux 内核中添加直接内存访问 (DMA) Rust 抽象。

Google 一直是 [将 Rust 添加到内核](https://thenewstack.io/rust-in-the-linux-kernel/) 以在 Android 手机中运行 Linux 的坚定支持者。在内核中使用 Rust 被认为是避免与 [C and C++ code](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/) 相关的内存漏洞并为 Android 操作系统增加更多稳定性的一种方式。“Google 希望用 Rust 代码替换 C 代码，这只代表内核的一小部分，但会产生巨大的影响，因为我们谈论的是数十亿部手机，”Ojeda 在他的演讲后告诉我。

除了 Google 之外，随着 Rust 获得更多的架构支持以及“维护者对它越来越满意”，Rust 的采用和热情也在增加，Ojeda 告诉我。“维护者已经告诉我，如果可以的话，他们现在就开始编写 Rust，”Ojeda 说。“如果他们可以放弃 C，他们就会这样做。”

Kernel developers:

[@Linus__Torvalds] at [#OSSummit] : « For some reason the whole [@rustlang] versus C discussion is taking almost religious overtones. » [@thenewstack] [pic.twitter.com/6TL7CaViRK](pic.twitter.com/6TL7CaViRK) — BC Gain (@bcamerongain)

[September 16, 2024]

Ojeda 在他的演讲中没有提到的是，最近那些不愿在容器中混合 C 和 Rust 代码的维护者遭到了强烈反对。9 月，Linux 的创建者 [Linus Torvalds](https://www.linkedin.com/in/linustorvalds/) 在他的 [Open Source Summit](https://events.linuxfoundation.org/open-source-summit-europe/) 主题演讲中将这场争议描述为具有“几乎宗教战争的意味”。Torvalds 随后表示，虽然这场争议涉及健康的争论，但有些争论正变得非常消极。

问题在于 C 语言和 Rust 语言在跨语言边界提交更改时存在的文化冲突。代表 Rust 人员修改 C 接口可能从 Rust 的角度来看是有意义的（反之亦然），而 C 人员则寻求 Rust 贡献来插入 C。

这场争议可以追溯到三年多前，当时有人提出 Rust 具有 C 所不具备的某些安全优势，可以成为内核的一部分并有可能取代它。尽管如此，该项目并没有停滞不前。

例如，现在著名的缓冲区溢出攻击或可以使用 C 和 CPU 生成的漏洞几乎已经过时。虽然 Rust 提供了一些安全特性和缺点，但与更容易掌握的 C 相比，它也更难学习。
在最近的 Rust 和 C 阵营之间的一次交流中，软件工程师和 Linux 内核维护者 [Christoph Hellwig](https://ostconf.com/en/materials/2307) 在 1 月初的 [一封电子邮件](https://lore.kernel.org/rust-for-linux/2b9b75d1-eb8e-494a-b05f-59f75c92e6ae@marcan.st/T/) 中写道：“kernel/dma 中不要有 Rust 代码。”他的信息是为了回应在 Linux 内核中为 DMA API 添加 Rust [补丁](https://lore.kernel.org/rust-for-linux/20250108122825.136021-3-abdiel.janulgue@gmail.com/#r) 的请求。一月份，在最近的一次来回讨论中，在周三的 FOSDEM 周边会议前夕，讨论进一步升温。

(2016 年，Hellwig 在一起针对当时的 VMware 的诉讼中败诉，声称 vSphere 侵犯了一个开源许可证。汉堡的德国法院驳回了该诉讼。)

上周，Hellwig 拒绝了 Red Hat 工程师和内核贡献者 [Danilo Krummrich](https://de.linkedin.com/in/danilo-krummrich-796885153) 对为 C API 添加 Rust 抽象的支持。

Krummrich 提出，DMA 一致性分配器的 Rust 抽象层应作为“单独的组件”进行维护。Hellwig 上周回复了 Krummrich 的提议：

“这对我没有任何帮助。另一种语言引入的每一个额外的位都会大大降低内核作为集成项目的可维护性。Linux 能够存在这么长时间的唯一原因是它没有内部边界，而添加另一种语言完全打破了这一点。你可能不喜欢我的回答，但我会尽我所能阻止这种情况。这 **不是** 因为我讨厌 Rust。

虽然不是我最喜欢的语言，但它绝对是最好的新语言之一，我鼓励人们在适合的新项目中使用它。我不希望它出现在我需要维护的庞大的 C 代码库附近。”

## Rust 浪潮

在争议中，人们一直在大声支持 Ojeda。他的大部分讨论还涵盖了内核中 Rust 倡导者发表的声明，从内核的首席开发人员（包括 Linux 创建者 Linus Torvalds 本人）到 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)、Samsung、[Google](https://cloud.google.com/?utm_content=inline+mention)、Microsoft 等公司的技术负责人。

在他的演讲中，Ojeda 重申了他之前在 2021 年给 Torvalds 的 [电子邮件](https://lore.kernel.org/lkml/20210414184604.23473-1-ojeda@kernel.org/) 中写的一句话，他说这句话至今仍然适用：

“通过在 Linux 内核中使用 Rust，我们希望：

‒ 由于下面提到的语言特性，用 Rust 编写的新代码可以降低内存安全错误、数据竞争和总体逻辑错误的风险。

‒ 由于 Rust 的安全子集，维护人员更有信心重构和接受模块的补丁。

‒ 由于基于现代语言特性且有详细文档支持的更易于推理的抽象，新的驱动程序和模块变得更容易编写。

‒ 由于使用了现代语言，更多的人参与到内核的开发中。

‒ 通过利用 Rust 工具，我们可以继续执行我们在项目中建立的文档指南。例如，我们要求所有公共 API、安全前提条件、

`unsafe`
blocks and type invariants [sic] documented.”

与此同时，使用 Rust 和 C 之间的选择不一定是二选一的问题。我认为，C 将无限期地用于许多内核层和规范中。毕竟，古老的格言适用：“如果它没有坏，那就不要修理它。”

Ojeda 告诉我：“有些维护人员不想放弃 C。但是何时不再使用 C 取决于成熟度。这取决于底层和架构的成熟度，而架构的成熟度各不相同。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.