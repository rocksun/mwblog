
<!--
title: 微软的 Rust 豪赌：告别蓝屏，拥抱更安全的代码
cover: https://cdn.thenewstack.io/media/2025/09/5c3fa957-philip-oroni-cnsr8wbbzpq-unsplash-1.jpg
summary: 微软正在用 Rust 修复 Windows 的安全性，并鼓励业界采用。Azure 已强制使用 Rust 于新项目，包括 Caliptra 和 Azure Boost。微软还开源了 OpenVMM 和用于 Rust 的 Azure SDK。Office 使用 Rust 重写了 DiskANN，性能提升显著。
-->

微软正在用 Rust 修复 Windows 的安全性，并鼓励业界采用。Azure 已强制使用 Rust 于新项目，包括 Caliptra 和 Azure Boost。微软还开源了 OpenVMM 和用于 Rust 的 Azure SDK。Office 使用 Rust 重写了 DiskANN，性能提升显著。

> 译自：[Microsoft's Rust Bet: From Blue Screens to Safer Code](https://thenewstack.io/microsofts-rust-bet-from-blue-screens-to-safer-code/)
> 
> 作者：Darryl K. Taft

微软公司几十年来一直在调整 Windows 的安全性。现在，该公司正试图用 [Rust](https://thenewstack.io/rust-programming-language-guide/) 修复它，并且他们希望其他人也使用它。

问题很简单：C 和 C++ 允许你编写看起来没问题，但会造成灾难性崩溃，或者更糟，被黑客入侵的代码。微软自己的内核每月都在通过 Win32k.sys（处理图形和窗口的部分）泄露权限提升漏洞。

在本周的 [RustConf 2025](https://rustconf.com/) 大会上，微软 [Azure](https://thenewstack.io/microsoft-linux-is-the-top-operating-system-on-azure-today/) 首席技术官 [Mark Russinovich](https://www.linkedin.com/in/markrussinovich/) 在题为“从蓝屏到橙色螃蟹：微软的 Rust 革命”的主题演讲中，将这种情况描述为“一个地下油库，每次泄漏几滴油，但持续不断”。

因此，他们开始用 Rust 重写部分代码。不是全部；只是部分。如果你现在深入到你的 Windows System32 文件夹，你会发现一个名为 win32kbase\_rs.sys 的文件。那是运行在你内核中的 Rust 代码。

真正重要的是：当一位安全研究人员在新 Rust 版本中发现了一个 bug 时，Russinovich 说，它导致系统崩溃，而不是让攻击者接管。

“我们认为这是一个成功，”他说。“这段用 [C++](https://thenewstack.io/introduction-to-c-programming-language/) 编写的代码，这个 bug 实际上会导致潜在的权限提升，而不是非常确定且无法利用的蓝屏崩溃。”

微软还重写了 [DirectWrite](https://learn.microsoft.com/en-us/windows/win32/directwrite/direct-write-portal)，这个字体渲染器多年来造成了无数的安全问题。两位微软开发人员在六个月内完成了它——154,000 行代码。它的运行速度比旧版本更快，并且没有相同类型的 bug。

## Azure 的强制要求

多年来，Russinovich 一直在内部推动 Rust，甚至在他有权强制执行它之前。

“实际上，甚至在那条推文之前，我就告诉我们的团队，我们应该停止 [C 和 C++](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/) 的新项目，如果我们不能容忍 [垃圾回收语言](https://thenewstack.io/does-garbage-collection-logging-affect-app-performance/)，就从 Rust 开始，”他在 RustConf 的主题演讲中说。

现在，作为 Azure 的副 CISO（兼任 CTO），他可以正式宣布：“采用或创建新的 C++ 风险太大了，你不能这样做。”

结果在 Azure 中随处可见。例如，[Caliptra](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/securing-hardware-and-firmware-supply-chains/4268815) 硬件信任根从一开始就完全用 Rust 编写。

“如果你看看 Caliptra 的 ROM，这都是开源的，”Russinovich 说。“如果你看看 Caliptra 的固件，如果你看看 Caliptra 的模拟器，它们都是用 Rust 编写的。”

[Azure Boost](https://learn.microsoft.com/en-us/azure/azure-boost/overview)，管理服务器和处理网络卸载的系统，强制要求任何接触不受信任的数据都使用 Rust，他说。

“在我们处理不受信任的输入的地方，强制要求用 Rust 重写它，并且任何新的代理都用 Rust 编写。”

甚至 [Hyper-V，微软的虚拟机监控程序](https://thenewstack.io/microsofts-hyperlight-webassembly-for-vms-is-open-source/) 和“微软有史以来创建的最安全的软件之一”，也正在接受 Rust 的处理。ARM64 模拟支持现在以 Rust 的形式发布，标志着这个关键组件的逐渐过渡的开始。

微软正式将 Rust 作为 Hyper-V 的一部分发布，这只是你将看到 Rust 在该组件中持续增长的一个地方，Russinovich 说。

“说到虚拟机监控程序，有虚拟机监控程序本身，还有 [虚拟机管理器 (VMM)](https://learn.microsoft.com/en-us/system-center/vmm/overview?view=sc-vmm-2025)。我们从一开始就用 Rust 启动了这个项目，[OpenVMM](https://thenewstack.io/microsoft-open-sources-openvmm-rust-powered-vm-monitor/)，”他说。

事实上，Windows 内核团队中有一群核心的 Rust 爱好者，他们说微软需要一个开源的虚拟机管理器，它位于 Azure 上虚拟机 (VM) 的下方，并通过主机与 Azure Boost 通信，他补充说。

“例如，我们在这里运行连接到 Azure Boost 网络适配器的模拟网络适配器。因此，为了与现有操作系统提供兼容性，该系统是一个 Linux 系统，”Russinovich 说。“该系统运行在用 Rust 编写的开放虚拟机管理器上。OpenVMM 展示了微软对开源和 Rust 以及跨平台可移植性的承诺。因此，OpenVMM 不仅与 Hyper V 兼容，不仅与 Windows 兼容，还与 Linux 和 KVM [基于内核的虚拟机] 兼容，并且这是完全开源的。”

Russinovich 还提到了 [Hyperlight 项目](https://thenewstack.io/microsofts-hyperlight-webassembly-for-vms-is-open-source/)，这是一个开源的 Rust 库，你可以使用它来执行小的、嵌入式函数，并在大规模上为每个函数调用使用基于虚拟机监控程序的保护。

此外，微软今年早些时候发布了用于 Rust 的 Azure SDK。

[![](https://cdn.thenewstack.io/media/2025/09/d90ce51f-screenshot-2025-09-03-123836-1-1.png)](https://cdn.thenewstack.io/media/2025/09/d90ce51f-screenshot-2025-09-03-123836-1-1.png)

*Mark Russinovich 在 RustConf 上。*

## Office 全力以赴

与此同时，Office 有一个不同的问题。它的语义搜索系统 [DiskANN](https://www.microsoft.com/en-us/research/project/project-akupara-approximate-nearest-neighbor-search-for-large-scale-semantic-search/)，对于 Bing 的数百个节点来说工作正常，但无法处理 Office 的数百万个文档。

“Office 想要图中数百万个节点。他们意识到 DiskANN 和 C 的实现无法提供他们想要的规模和性能，”Russinovich 说。

因此，他们用 Rust 重写了它。结果是惊人的：在相同的准确度水平下，性能更好，并且减少了内存使用。

“我们看到了巨大的胜利，”Russinovich 指出。Office 娱乐设备部门对此深信不疑，他们“全力以赴使用 Rust”，甚至超过了像 C# 这样的内存安全语言，因为它的并发处理能力。

[Azure Data Explorer](https://azure.microsoft.com/en-us/products/data-explorer) 展示了大规模迁移的样子。一位开发人员花了一年时间将数据存储层移植到 Rust，然后是查询引擎。他说，该系统现在处理着“实际上数百 PB 的数据”，其中包含 350,000 行 Rust 代码，以及 230 万行 C# 代码和不断减少的 C++ 代码。

## 向合作伙伴开放门户

现在，微软希望硬件公司和驱动程序开发人员编写他们自己的 Rust 驱动程序。根据微软 Windows 团队的 [Nate Deisinger](https://techcommunity.microsoft.com/users/nate_deisinger/3156254) 的一篇 [博文](https://techcommunity.microsoft.com/blog/windowsdriverdev/towards-rust-in-windows-drivers/4449718)，他们构建了一个名为 [windows-drivers-rs](https://github.com/microsoft/windows-drivers-rs/) 的完整框架，该框架基本上在 Rust 和 Windows 驱动程序工具包 (WDK) 之间进行转换。

“通过 [Surface 团队](https://techcommunity.microsoft.com/blog/SurfaceITPro/safer-drivers-stronger-devices/4431411) 的出色努力，我们开始了我们的旅程，使 Rust 成为全球驱动程序开发人员的一流语言，”Deisinger 在 Russinovich 在 RustConf 上发言的前一天在帖子中写道。

这些部分很简单：[wdk-build](https://github.com/microsoft/windows-drivers-rs/blob/main/crates/wdk-build) 将 [Cargo](https://thenewstack.io/how-to-write-rust-code-like-a-rustacean/) 连接到 Windows 构建系统，[wdk-sys](https://github.com/microsoft/windows-drivers-rs/blob/main/crates/wdk-sys) 提供对 Windows 驱动程序 API 的原始访问，[wdk](https://github.com/microsoft/windows-drivers-rs/blob/main/crates/wdk) 为你提供稍微安全的版本，[cargo-wdk](https://github.com/microsoft/windows-drivers-rs/tree/main/crates/cargo-wdk) 允许你像创建和构建任何其他 Rust 项目一样创建和构建驱动程序，他写道。

你可以创建内核模式驱动程序框架 (KMDF)、用户模式驱动程序框架 (UMDF) 或 Windows 驱动程序模型 (WDM) 驱动程序，这些驱动程序实际上可以在 Windows 11 上加载和运行。问题是你仍然需要编写大量不安全的 Rust 代码，因为 Windows 内核 API 不是为内存安全而设计的。

微软也在努力解决这个问题。正如 Deisinger 在博客中解释的那样，他们希望创建安全的包装器，以便“大多数驱动程序代码可以用安全的 Rust 编写”。他们有内部工作的实验版本，但尚未准备好供公众使用。

## 开发人员的真实想法

微软调查了自己的人员对 Rust 的看法。一旦开发人员克服了最初的震惊，反馈就非常积极。

“我们看到开发人员，如果他们来自 C++，尤其会感到震惊。就像，‘哇，这是一种完全不同的方式，’”Russinovich 解释说。

但在几个月后，有些事情会发生转变。“在几个月后，他们实际上已经改变了他们的想法，现在他们与 Rust 借用检查器 的思维和工作方式融为一体，并且实际上很享受它，”他说。

开发人员喜欢性能的提升。

“这非常一致。每当我们采用 C++ 代码库并将其移植到 Rust 时，我们通常会看到性能的提高，”Russinovich 说。“开发人员喜欢完全消除 bug 类型，并且他们喜欢编写一次代码，而不是调试几天，”他补充说。

他们不喜欢的是：与现有的 C++ 和 C# 代码混合使用很痛苦。异步调试很糟糕。动态链接存在问题。但他指出，“即使有这些抱怨的开发人员也不想放弃 Rust。”

## 秘密武器：AI 翻译

微软正在构建一些可能改变游戏规则的东西——AI 工具，可以自动将整个代码库从 C++ 翻译成 Rust。使用他们的 [GraphRAG](https://microsoft.github.io/graphrag/) 技术，他们可以创建大型代码库的语义表示，语言模型可以推理并逐个移植。

Russinovich 现场演示了这一点，展示了一个 Python 游戏被翻译成 Rust，同时保持了原始的项目结构和功能。

“随着时间的推移，你将看到在 [大型语言模型](https://thenewstack.io/introduction-to-llms/) [LLM] 的帮助下，从现有语言（特别是 C、C++）到 Rust 的代码进行更多这种加速。”

这可以解决 Rust 采用的最大障碍——移植现有代码库所需的大量工作。

## 更大的赌注

微软推动 Rust 的发展远远超出了赶时髦的范畴。Russinovich 将其视为未来必不可少的事情。

“我们认为像 Rust 这样的内存安全语言代表了安全软件工程的未来，”他说。“当今的安全形势要求从边缘到云的每个层面都具有可靠性和安全性保证。”

他们并不孤单。美国国家安全局 (NSA) 在 [Russinovich 2022 年发表著名推文赞扬 Rust 的优点](https://thenewstack.io/microsofts-it-outage-reminder-rust-is-better-than-c-c/) 后不久，就认可了向内存安全语言的转变。他指出，[Linux 添加了 Rust 支持](https://thenewstack.io/rust-integration-in-linux-kernel-faces-challenges-but-shows-progress/)。行业势头正在增强。

驱动程序框架代表着微软将这种理念扩展到其自身代码之外。如果硬件供应商开始编写 Rust 驱动程序，Windows 将变得更加安全，而无需微软完成所有工作。

但驱动程序开发是保守的。人们坚持使用有效的方法。微软押注于可证明的安全改进加上全面的工具，足以克服数十年的惯性。

早期结果令人鼓舞。微软已经表明，Rust 代码在 C++ 产生漏洞的地方安全地失败。他们已将其部署在他们最关键的系统中：内核、虚拟机监控程序、密码库。现在，他们希望整个生态系统都效仿。

正如 Russinovich 所说：“Rust 正在渗透到微软的核心基础设施中，并且只会继续加速。” 驱动程序框架只是更大转型的最新组成部分。