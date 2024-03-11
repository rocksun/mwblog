
<!--
title: Rust势头正盛：预计新倡议将推动采用
cover: https://cdn.thenewstack.io/media/2024/03/39410597-bike-3043594_1280-1.jpg
-->

政府倡导和对更安全软件的需求推动了 Rust 开发的兴起。

> 译自 [Rust on the Rise: New Advocacy Expected to Advance Adoption](https://thenewstack.io/rust-on-the-rise-new-advocacy-expected-to-advance-adoption/)，作者 Darryl K Taft。

[Rust 编程语言](https://thenewstack.io/google-busts-confirms-common-myths-about-rust-programming/) 的使用量一直在上升，但随着更多注重安全性的组织呼吁 Rust 开发人员（亲切地称为 [Rustaceans](https://en.wiktionary.org/wiki/Rustacean)）使用更多内存安全语言，预计其势头将持续增强。

最近，本周白宫[国家网络总监办公室 (ONCD)](https://thenewstack.io/u-s-government-tackles-open-source-memory-safe-programming-security/) 发布了一项建议，要求软件开发组织开始为应用程序和系统开发使用内存安全语言，例如 Rust。

## 监管倡议

[微软](https://news.microsoft.com/?utm_content=inline-mention)和[谷歌](https://thenewstack.io/google-spends-1-million-to-make-rust-c-interoperable/)等部分公司正寻求用 Rust 重写现有 C、C++ 和 C# 系统。专家们预测此类工作将增加。

事实上，国家安全局 ([NSA](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/3608324/us-and-international-partners-issue-recommendations-to-secure-software-products/))、网络安全和基础设施安全局 ([CISA](https://www.cisa.gov/))、国家标准技术研究所 ([NIST](https://www.nist.gov/itl/ssd/software-quality-group/safer-languages)) 和国家药瘾控制所 ([ONCD](https://www.whitehouse.gov/oncd/briefing-room/2024/02/26/press-release-technical-report/)) 等机构近期的倡议和研究工作“可以作为一份有价值的证据，证明内存安全漏洞对我们的数字生态系统构成了相当大的风险”，[Rust 基金会](https://foundation.rust-lang.org/)执行董事兼首席执行官 [Rebecca Rumbul](https://www.linkedin.com/in/rebecca-rumbul-96a5441a/?originalSubdomain=uk) 告诉 The New Stack。

此外，Rumbul 表示 [Rust 基金会](https://thenewstack.io/funding-downturn-threaten-ability-to-secure-oss-projects/) 认为 Rust 编程语言是解决关键基础设施安全差距的最强大工具。“作为一个组织，我们坚定不移地致力于通过我们的 [安全倡议](https://foundation.rust-lang.org/news/second-security-initiative-report-details-rust-security-advancements/) 等计划进一步加强 Rust 的安全性，”她说。

同时，针对太空系统的软件开发，ONCD 报告称：内存安全和内存不安全编程语言都满足该组织对开发太空系统的要求。“目前，满足所有三个属性的最广泛使用的语言是 C 和 C++，它们不是内存安全编程语言，报告称。“Rust 是内存安全编程语言的一个示例，它具有上述三个必要属性，但尚未在太空系统中得到验证。”

根据 ONCD 报告，用于构建太空系统的语言的三个要求是：“首先，该语言必须允许代码接近内核，以便它可以与软件和硬件紧密交互；其次，该语言必须支持确定性，以便输出的时间保持一致；第三，该语言不得具有（或能够覆盖）‘[垃圾回收器](https://thenewstack.io/generational-shenandoah-offers-java-a-better-way-to-collect-garbage/)’，这是一个自动回收计算机程序不再使用的已分配内存的功能。”

## 2023 年 Rust 年度调查

上周发布的 [2023 年 Rust 年度调查](https://blog.rust-lang.org/2024/02/19/2023-Rust-Annual-Survey-2023-results.html) 结果显示，Rust 在工作中的使用量持续逐年上升。2023 年调查受访者中有 34% 表示他们在工作中的大部分编码中使用 Rust，比 2022 年增加了五个百分点。在这一群体中，39% 的人表示他们为大量使用 Rust 的组织工作。

调查受访者雇主投资 Rust 的首要原因是能够构建相对正确且无错误的软件，达到 86%，高于 2022 年的 82%。第二大原因是 Rust 的性能特性，达到 83%。

在技术领域方面，研究表明 Rust 特别适合创建服务器后端、Web 和网络服务以及云技术。

Rust 调查称，Rust 程序员使用他们的 Rust 程序针对各种平台，尽管到目前为止最流行的目标仍然是 Linux 机器。然而，“我们可以看到针对 [WebAssembly](https://thenewstack.io/webassembly/)、嵌入式和移动平台的用户略有增加，这说明了 Rust 的多功能性”，Rust 团队的调查博客文章称。

然而，Rumbul 告诉 The New Stack，如果没有向其全球用户群扩展，Rust 无法继续大规模地提供广泛的安全保障优势。“因此，我发现最近的 Rust 调查状态中几个数据点令人鼓舞。即，全球 Rust 专业知识的明显增长以及 Rust 在专业环境中的日益普及。”

此外，Rumbul 指出，虽然 2023 年 Rust 调查状态中描绘的许多同比变化“令人振奋”，但它们也是渐进式的；该基金会预计随着时间的推移，这些领域的增长将更加实质性。

## 监管倡导是否有帮助？

“自 2006 年成立以来，Rust 在企业自动化方面的受欢迎程度一直稳步上升，”[Holger Mueller](https://www.linkedin.com/in/holgermueller/) 说，他是 [Constellation Research](https://www.constellationr.com/) 的分析师。“它在开发者受欢迎程度排名中稳步攀升，并且语言固有的高内存安全性可能会从监管角度帮助其流行。但这绝不是让软件语言流行的可靠理由，因此，Rust 根据其优点吸引更多开发者更为重要，并且它有很多优点——比如作为一种有助于 [Linux 内核开发](https://thenewstack.io/rust-in-the-linux-kernel/) 的语言。

[Eric Newcomer](https://www.linkedin.com/in/enewcomer/) 是 [Intellyx](https://intellyx.com/) 的首席技术官兼分析师，他预计政府的呼吁将有助于推动 Rust 的进一步采用。

“白宫的认可将火上浇油，”Newcomer 告诉 The New Stack。“Rust 作为 C 和 C++ 的更安全替代品已经势头强劲。Rust 提供了与 C 和 C++ 相同级别的操作系统资源访问权限，但这样做是安全的。政府对此的认可肯定会加快采用速度。”

[Mark Russinovich](https://www.linkedin.com/in/markrussinovich/) 是 [Microsoft](https://thenewstack.io/microsoft-we-are-not-abandoning-c-for-rust/) 的 Azure 首席技术官，他一直直言不讳地表示这家软件和服务巨头将进一步采用 Rust，本周在 [X](https://x.com/markrussinovich/status/1762925751106715906?s=20)（前身为 Twitter）上发帖称，“白宫表示现在是停止 C/C++ 新项目的时候了。”

此外，Russinovich 将不愿改变的 C 和 C++ 开发者比作环保人士。

在 [另一篇 X 帖子](https://x.com/markrussinovich/status/1762985826059968545?s=20) 中，他说：“那里有一些直言不讳的 C/C++ 拥护者。我不明白他们为何抵制转向内存安全语言（传统除外）。一位专家在非常小心谨慎的情况下可以编写安全的 C/C++，但内存安全语言让任何人都不可能或很难犯内存安全错误。”

## 更多调查分析

Rust 调查的其他结果表明，人们希望有数量有限的以 Rust 为中心的职位，[Lawrence E. Hecht](https://www.linkedin.com/in/lawrence-hecht/) 指出，他是一位 IT 数据分析师和顾问，负责管理 The New Stack 的研究项目，因为只有 9% 的受访者表示他们认为合格的候选人很容易找到大多数编程都使用 Rust 的工作。虽然 27% 的人确实认为现有工作有吸引力，但如果 Rust 成为许多开发者的主要语言，这一比例可能会更高。

作为 Rust 吸引了新用户的证据，48% 的受访者在 2021 年或之后开始学习用 Rust 编程。

调查还显示 [RustRover](https://blog.rust-lang.org/images/2024-02-rust-survey-2023/what-ide-do-you-use.png) 由 [JetBrains](https://www.jetbrains.com/) 取得了初步成功。[RustRover，由 JetBrains 发布的专门的 IntelliJ Rust IDE](https://thenewstack.io/dedicated-ide-for-rust-released-by-jetbrains/)。由于之前研究中 20% 的受访者正在使用某种类型的 JetBrains IDE 或 Rust 插件，我们可以假设其中很大一部分已经切换。

Hecht 还从 2023 年的调查中检测到人们对 Rust 未来感到越来越焦虑，因为只有 18% 的人对 Rust 的未来没有担忧，而 2022 年这一比例为 30%。43% 的人认为，最大的未来担忧是 Rust 变得过于复杂。28% 的人也担心项目治理无法扩展到满足社区的规模/要求。

“Rust 社区继续经历着成长烦恼，”Hecht 说。“[去年](https://thenewstack.io/rust-foundation-focusing-on-safety-and-dev-outreach-in-2023/)，Rust 基金会执行董事担心倦怠以及跟上不断增长的用户群的能力。对项目治理扩展能力的担忧似乎是合理的。”

## Rustacean（指 Rust 语言开发者或用户） 的需求、期望和渴望

该调查的受访者还指出了麻烦功能以及他们希望在该语言中添加或增强的功能。

对于 Rust 用户希望实现、稳定或改进的功能，最想要进行改进的领域是特性（特性别名、相关类型默认值等）、const 执行（通用 const 表达式、const 特性方法等）和 async（async 闭包、协程）。

Rustacean 似乎觉得最难的部分是异步 Rust、特性和泛型系统以及借用检查器。

Rustacean 希望 Rust 的维护者主要修复编译器错误（68%）、改进 Rust 程序的运行时性能（57%）并提高编译时间（45%）。

Rust 基金会的 Rumbul 告诉 The New Stack，她认为 Rust 的维护者已经“出色”地完成两项工作：不仅构建了一门强大的编程语言，而且通过他们的调查开发了一种有用的方式来衡量 Rust 的当前状态。

“Rust 基金会的作用是与全球 Rust 社区的各个部分（包括企业用户）接触并提供支持，”她说。“通过与这些团体合作，我们将巩固 Rust 作为数字安全基石的地位。”