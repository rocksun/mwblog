# Rust：故障安全软件开发的未来

![Rust：故障安全软件开发的未来特色图片](https://cdn.thenewstack.io/media/2024/06/8c5ee7d1-levi-meir-clancy-9fpm0ruywww-unsplash-1024x683.jpg)

为了彻底改变安全关键型软件领域，Rust 基金会联合了主要供应商（包括 Arm 和丰田）和专家，组建了安全关键型 Rust 联盟，为在故障不是选项的系统中采用 [Rust 编程语言](https://thenewstack.io/rust-whats-next-for-the-fast-growing-programming-language/) 铺平了道路。

Rust 不仅是 [增长最快的语言](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/) 之一，而且还因其 [内存安全性](https://thenewstack.io/out-with-c-and-c-in-with-memory-safety/) 而备受追捧，而新联盟将有助于其普及。

事实上，[Rust 基金会](https://thenewstack.io/rust-foundation-focusing-on-safety-and-dev-outreach-in-2023/)、[AdaCore](https://www.adacore.com/)、[Arm](https://arm.com/)、[Ferrous Systems](https://ferrous-systems.com/)、[HighTec EDV-Systeme GmbH](https://hightec-rt.com/en/)、[OxidOS](https://www.oxidos.io/)、[TECHFUND](https://techfund.jp/)、[TrustInSoft](https://trust-in-soft.com/)、[Veecle](https://www.veecle.io/)、[Lynx Software Technologies](https://www.lynx.com/) 和 [Woven by Toyota](https://woven.toyota/en/) 构成了致力于在 [安全关键型软件](https://thenewstack.io/bjarne-stroustrups-plan-for-bringing-safety-to-c/) 中负责任地使用 Rust 的新集团。

## 语言安全性

“编程语言安全性是指语言在编译时或运行时防止错误或未定义行为的能力。另一方面，‘安全关键型’是指系统在不造成事故或灾难性故障（将对人员、财产或环境造成伤害）的情况下运行的能力，”安全优先 Rust 联盟的创始成员提供的常见问题解答中写道。“因此，虽然安全关键型系统依赖于强调安全性和保障性的语言（例如 Rust），但编程工具只是整体策略的一个组成部分。”

## 联盟目标

该联盟旨在制定指南、工具、库和语言子集，以满足安全关键型系统的工业和法律要求。

此外，该倡议旨在吸取开源生态系统多年开发的经验教训，使 Rust 成为各个行业和严重级别安全工具包的宝贵组成部分。

“我认为安全关键型 Rust 联盟强调了业界对 Rust 满足严格安全性和可靠性标准的能力的信心，”IDC 分析师 [Arnal Dayaratna](https://www.linkedin.com/in/cloudcomputingtoday/) 告诉 The New Stack。“特别是，联盟得到丰田和 Arm 等公司的支持，说明业界认识到 Rust 的内存安全性管理和并发安全性能力如何使其区别于 [C/C++](https://thenewstack.io/google-spends-1-million-to-make-rust-c-interoperable/) 等语言。”

此外，“鉴于安全关键型行业是多么‘关键’，Rust 基金会非常有动力召集社区和行业的关键利益相关者，探讨 Rust 如何满足合规标准并为每个人贡献更好的软件，”Rust 基金会执行董事兼首席执行官 [Rebecca Rumbul](https://www.linkedin.com/in/rebecca-rumbul-96a5441a/?originalSubdomain=uk) 在一份声明中表示。

## 使用 Rust 的行业

特别关注功能安全的行业包括交通运输（例如汽车、航空、航天）、能源、生命科学等。Rust 用于许多行业的 [任务关键型和嵌入式系统](https://www.lynx.com/press-releases/rust-compiler-support)。

“安全是我们车辆软件开发的首要任务。传统上，实现最高级别的安全性是一项复杂而漫长的工作，需要使用编程语言之外的专门工具和流程，”Woven by Toyota 的杰出工程师 [JF Bastien](https://www.linkedin.com/in/jfbastien/?originalSubdomain=jp) 在一份声明中表示。“因此，我们很高兴与安全行业的领先专家合作，将 Rust 等新工具集成到我们的安全关键型系统中，”他说。

政府机构，例如
### NSA、CISA、NIST 和 ONCD 引用了内存安全语言的重要性，并引用 Rust 作为潜在示例。

## Microsoft 的影响力和关注点

此外，包括 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 在内的主要供应商也提倡使用 Rust 来确保安全性和内存安全性。早在 2019 年，Microsoft 就表示需要“[更安全的系统编程语言](https://msrc.microsoft.com/blog/2019/07/we-need-a-safer-systems-programming-language/)”，并引用 Rust 作为“由于其能够以内存安全的方式编写系统级程序，因此是业界尽可能采用的最佳选择”。

另一篇 2019 年的 Microsoft Research 帖子解释了“
[为什么 Rust 适合安全系统编程](https://msrc.microsoft.com/blog/2019/07/why-rust-for-safe-systems-programming/)”。该帖子解释了 Rust 如何代表目前可用的 C 和 C++ 的最佳替代方案。

“首先，已经有很多出色的内存安全语言可供使用，并且在 Microsoft 内部和外部广泛使用，包括 C# 或 F# 等 .NET 语言以及 Swift、
[Go](https://thenewstack.io/go-the-programming-language-of-the-cloud/) 和 [Python](https://thenewstack.io/an-introduction-to-python-a-language-for-the-ages/) 等其他语言。我们鼓励任何当前正在使用 C 或 C++ 的人考虑是否可以使用其中一种语言来代替。然而，我们正在讨论对安全的*系统*编程语言的需求（即，一种可以构建其他软件运行的系统（如操作系统内核）的语言）。此类工作负载需要 C、C++ 和 Rust 提供的速度和可预测的性能，”该帖子写道。“通过垃圾回收实现内存安全性的语言不适合系统编程，因为它们的运行时会导致不可预测的性能和不必要的开销。”

此外，Microsoft 的 Azure CTO
[Mark Russinovich](https://www.linkedin.com/in/markrussinovich) 之前 [发布在 X（前身为 Twitter）上](https://x.com/markrussinovich/status/1571995117233504257)：“说到语言，是时候停止启动任何新的 C/C++ 项目，并在需要非 GC 语言的情况下使用 Rust 了。为了安全性和可靠性。业界应该宣布这些语言已弃用。”

Microsoft 最近
[向 Rust 基金会捐赠了 100 万美元](https://thenewstack.io/microsofts-1m-vote-of-confidence-in-rusts-future/)，并且在今年早些时候决定 [用 Rust 重写一些 C# 代码](https://thenewstack.io/microsoft-we-are-not-abandoning-c-for-rust/)。

## 扩大社区，增加采用

与此同时，新财团计划与 Rust 社区紧密合作，以扩大 Rust 的用户群和适用性，而不会对现有用户和项目参与者产生不利影响。

“如果我们开始看到 Rust 在汽车或航空航天等一个或多个安全关键行业中得到更广泛的利用，Rust 基金会将认为安全关键 Rust 计划是成功的，”Rust 基金会技术总监
[Joel Marcey](https://www.linkedin.com/in/joelmarcey/) 在一份声明中说。

最后，“作为 Rust 编程语言的所在地，其主要目标是增加采用和提高质量，Rust 基金会处于有利地位，可以促进和支持跨部门和跨社区的讨论和协作，以确保 Rust 适合在安全关键行业中使用，”Rumbul 指出。

因此，“该财团可能会催化 Rust 在安全关键用例和应用程序中的采用，并加速 Rust 开发者生态系统的成熟，”Dayaratna 说。“Rust 开发者生态系统的成熟非常重要，因为其陡峭的学习曲线历来是其采用面临的主要障碍之一。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)