# 微软 IT 故障提醒：Rust 比 C/C++ 更优秀

![Featued image for: Microsoft’s IT Outage Reminder: Rust Is Better Than C/C++](https://cdn.thenewstack.io/media/2024/07/9caafb56-airport-2373727_1280-1024x682.jpg)

上周，全球范围内的 Windows 系统都出现了蓝屏死机 (BSOD)，[原因是安全供应商 CrowdStrike 提供的错误配置更新](https://thenewstack.io/7-urgent-lessons-from-the-crowdstrike-disaster/)。

这次故障被一些人称为世界上最严重的故障，它瘫痪了关键基础设施。然而，微软的一位官员在周末也提醒开发人员注意[更好的编码实践](https://thenewstack.io/infrastructure-as-code-6-best-practices-for-securing-applications/)，以提高系统可靠性，降低系统崩溃和蓝屏死机的可能性。

[微软](https://news.microsoft.com/?utm_content=inline+mention) Azure 的 CTO [Mark Russinovich](https://www.linkedin.com/in/markrussinovich/) 表示，开发人员应该逐步弃用 C/C++，转而使用[内存安全的 Rust 语言](https://thenewstack.io/rust-the-future-of-fail-safe-software-development/)，以减少系统崩溃和蓝屏死机。当然，这条推文与 CrowdStrike 的错误更新没有直接关系。

周六，Russinovich [转发了一条 2022 年的推文](https://x.com/markrussinovich/status/1814853234445722076)，内容是：“是时候停止启动任何新的 C/C++ 项目，并在需要非 GC 语言的场景中使用 Rust。为了安全性和可靠性，行业应该宣布这些语言已过时。”

## 空指针

蓝屏死机的原因有很多，包括 Windows 中的内存错误、驱动程序问题和进程问题，这些问题都依赖于用 C/C++ 编写的内核。前 Google 员工 [Zack Vorhies](https://www.linkedin.com/in/zachvorhies/) 表示，这次故障是由于 C/C++ 代码错误造成的，但这一说法被 Google 研究员 [Tavis Ormandy](https://github.com/taviso) 驳斥了。

Vorhies [将大规模故障归咎于空指针](https://x.com/Perpetualmaniac/status/1814376668095754753)，即代码中指向无效内存位置的一行代码，他将其描述为“来自内存不安全的 C++ 语言的空指针”。

Ormandy 驳斥了 Vorhies 的说法，[CrowdStrike 表示](https://www.crowdstrike.com/blog/falcon-update-for-windows-hosts-technical-details/)：“这与通道文件 291 或任何其他通道文件中包含的空字节无关。”

## 支持 Rust

微软多年来一直支持 Rust，但在内部，代码迁移仍在进行中。该公司意识到，从 C/C++ 切换不可能在一夜之间完成。

“我们正在努力。Azure 中已经有很多 Rust 代码，Windows 中也有一些 Rust 代码，”Russinovich 在[最近的一条推文](https://x.com/markrussinovich/status/1815046656469225911) 中说。

对 Rust 的采用是循序渐进的；第一步是创建原型应用程序，以证明 Rust 代码可以与 Windows 协同工作。微软还将保护系统硬件的周边应用程序迁移到 Rust。

## UEFI 固件

微软正在围绕 Rust 创建其 Surface 硬件的安全启动模块。UEFI（统一可扩展固件接口）包含将系统从启动引导到 Windows 操作系统的固件代码。UEFI 代码通常位于主板上，并在计算机开机时访问。

UEFI 固件加载到内存中，Rust 提供内存安全机制，以防止系统崩溃或被利用。许多硬件漏洞和安全问题都起源于计算机内存内部。

美国政府的主要技术安全机构 [网络安全基础设施和安全局 (CISA)](https://thenewstack.io/why-does-the-nsa-care-about-the-software-supply-chain/) 在 12 月呼吁公司[切换到内存安全技术](https://www.cisa.gov/news-events/news/urgent-need-memory-safety-software-products)。

“除了 C/C++ 之外，大多数现代编程语言已经是内存安全的。内存安全的编程语言管理计算机的内存，因此程序员无法引入内存安全漏洞，”CISA 在咨询说明中说。

## Rust 保护 PC

微软正在使用围绕 Rust 构建的安全性和固件来保护其自有硬件，微软企业和操作系统安全副总裁 [Dave Weston](https://www.linkedin.com/in/dwizzzle/) 在一次采访中说。

该公司的 Secured-core 计划包括为 Surface 和 Windows PC 提供稳定且安全的启动环境。该公司已将许多固件组件从 C 迁移到 Rust，这提高了系统稳定性，并降低了系统暴露于黑客攻击的漏洞的可能性。
微软还为其名为 Pluton 的安全处理器创建了一个完全用 Rust 编写的实时操作系统。Pluton 包含一个可信平台模块 (TPM)，用于存储生物识别数据等关键安全信息。

“微软致力于通过设计使更多事物变得安全。这是拥有我们自己的安全处理器而不是等待行业发展带来的优势之一。我们将转向 Rust……它在该领域比传统原生语言具有巨大优势，”韦斯顿说。

内存泄漏一直是 TPM 的主要问题。[QuarksLab](https://blog.quarkslab.com/vulnerabilities-in-the-tpm-20-reference-implementation-code.html) 去年指出了 TPM 2.0 代码中的两个漏洞，这些漏洞将内存暴露给越界读写，可能将关键信息暴露给虚拟化环境中黑客的攻击。像 Rust 这样的内存安全语言可以帮助防止此类问题。

## 微软与 Rust 的历史

大约十年前，Mozilla 推出了一个包含 Rust 组件的 Firefox 浏览器，现在越来越多的程序员正在采用它。其他内存安全语言包括 [Golang](https://thenewstack.io/golang-what-are-constants-in-go-and-how-do-you-use-them/), [Java](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/), [C#](https://thenewstack.io/microsoft-we-are-not-abandoning-c-for-rust/), Swift 和 [Python](https://thenewstack.io/an-introduction-to-python-for-non-programmers/).

微软进行了两次实验来检查 Rust 在可行性和性能方面的可行性。Win32K 通常是频繁攻击的常见选择，因为它提供了一种方便的特权提升攻击。

“我们从 Rust 最能提供安全价值的地方开始，”韦斯顿在 [2020 年 6 月的播客](https://azuresecuritypodcast.azurewebsites.net/) 中说。

第一个是字体解析器，它在浏览器或 Office 客户端中创建了远程攻击面。将他们的现代 Web 应用程序 SDK 字体解析器 DirectWrite 转换为 Rust 花费了 2 到 3 个月的时间。

“大约花了两个到三个月的时间，由两名开发人员完成。有趣的是，性能实际上得到了提升，”韦斯顿在播客中说。

第二个实验涉及 Win32k 中的一些图形设备接口 (GDI) 表面，Win32k 是一个最初设计于 1980 年代后期的内部图形组件。微软不想重写整个代码，因此它尝试将 Win32k 的各个组件切片出来以用 Rust 实现。实验成功完成，Rust 组件现在与 Windows 一起发布。

“这尤其重要，因为 Microsoft Windows 是用 Visual C++ 编译器或 C 编译器编译的，而 Rust 的后端实际上是 LLVM [低级虚拟机]，”韦斯顿说。

## Azure 中的 Rust

微软还在 Azure 中广泛实施 Rust。

该公司正在实施一个用 Rust 编写的虚拟机管理器，它将管理 Azure 中的 Hyper-V。

Rust 也正在 Azure Boost 中实施，韦斯顿称之为“Azure 的未来架构”。

“这就是我们将 Azure 主机的更多性能方面卸载到智能网卡和/或 FPGA 等专用卡上的地方，用于存储，”韦斯顿说。

微软在 Rust 工具上花费了大约 1000 万美元，Azure 是首要目标。该公司还希望建立一个 Rust 的长期支持版本，类似于 [Linux 操作系统](https://thenewstack.io/rust-in-the-linux-kernel/).

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以收看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)