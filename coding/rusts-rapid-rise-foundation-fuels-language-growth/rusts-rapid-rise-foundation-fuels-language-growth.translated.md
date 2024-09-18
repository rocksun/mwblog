### Rust 的快速崛起：基金会推动语言发展

![Rust 的快速崛起：基金会推动语言发展](https://cdn.thenewstack.io/media/2024/09/dc25dc53-chris-luengas-nauqmbi3skw-unsplash-1-1024x683.jpg)

在上周的 [RustConf 2024](https://rustconf.com/) 中，[Rust 基金会](https://thenewstack.io/rust-foundation-focusing-on-safety-and-dev-outreach-in-2023/) 发布了其关于 Rust 编程状态的报告。

该报告涵盖了 Rust 基金会为支持 [Rust 编程语言](https://thenewstack.io/rust-whats-next-for-the-fast-growing-programming-language/) 和生态系统而做出的各种技术举措和贡献。

## 重点领域

该报告的重点领域包括 Crates.io 改进、[安全关键 Rust 联盟](https://thenewstack.io/rust-the-future-of-fail-safe-software-development/)、Rust-C++ 互操作性计划、安全计划、对基础设施支持的展望以及 Rust 语言规范。

“Rust 基金会的使命是管理 Rust 语言、社区和更广泛的生态系统。这份报告令人兴奋，因为它阐明了我们支持这一使命的工程举措，”Rust 基金会技术总监 [Joel Marcey](https://www.linkedin.com/in/joelmarcey/) 告诉 The New Stack。“我们最近围绕 Rust 语言安全性和互操作性开展的工作和合作尤其令人兴奋。”

Rust 基金会自 2021 年成立以来，其技术重点领域不断增加——随着时间的推移，该基金会已与 Rust 项目的许多成员建立了深入的合作关系，Rust 基金会执行董事兼首席执行官 [Rebecca Rumbul](https://www.linkedin.com/in/rebecca-rumbul-96a5441a/?originalSubdomain=uk) 告诉 The New Stack。

Rumbul 说：“我们还有更多全职工程师为该基金会工作，一些最具创新性的开源组织提供了关键支持，并且我们针对帮助个人维护者、新的 Rust 用户、政府和专业组织采用 Rust 并取得成功的计划和举措组合也在不断增加。”

## Crates.io

作为 Rust 编程语言的官方包注册表，[crates.io](https://crates.io/) 在 Rust 生态系统中发挥着至关重要的作用。除了 Rust 用户分享自己的库和包的地方之外，crates.io 还使其他开发人员更容易找到解决他们遇到的特定问题并扩展其自身工作的工具。

鉴于此重要性，Rust 基金会帮助资助和支持改进，以使 crates.io 更加安全、有序和高效。该基金会最近对 crates.io 的贡献得到了 Rust 基金会安全计划、[Alpha-Omega 项目](https://thenewstack.io/eclipse-plunges-into-oss-supply-chain-security/) 和 Rust 基金会白金会员 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 的财务支持。

Crates.io 改进包括管理功能、包下载更改、测试套件迁移和数据库性能优化。

该基金会最近对 crates.io 的贡献是由两名 Rust 基金会成员完成的：Rust 基金会软件工程师、Rust 项目 crates.io 团队联合负责人兼 Rust 项目长期贡献者 [Tobias Bieniek](https://www.linkedin.com/in/tobias-bieniek/?originalSubdomain=de)；以及 Rust 基金会软件工程师兼 crates.io 团队成员 [Adam Harvey](https://foundation.rust-lang.org/about/)。

4 月份，crates.io 测试套件迁移到异步测试，以便更轻松地使用仅异步。此外，在其他改进中，创建了一个新的存档版本下载后台作业，并存档了旧的、不需要的数据，最终允许 crates.io 团队大幅缩小 crates.io 数据库并提高性能。

crates.io 团队还实施了一项更改，使用户更容易安装包。

## 安全关键 Rust 联盟

6 月份，该基金会宣布成立一个新小组，致力于在安全关键软件中负责任地使用 Rust，该小组由 Rust 基金会主办。安全关键 Rust 联盟的创始参与者和基金会成员包括创始参与者和 Rust 基金会成员 [AdaCore](https://thenewstack.io/how-adacores-rust-fork-may-make-the-language-more-adoptable/)、Arm、Ferrous Systems、HighTec EDV-Systeme GmbH、Lynx Software Technologies、OxidOS、TECHFUND 和 [Veecle](https://veecle.io/)，以及 TrustInSoft 和 Woven by Toyota。

该小组的主要目标是支持在安全关键软件中使用 Rust 编程语言——其故障可能影响人类生命或造成严重的环境或财产损害的系统。

## Rust、C++ 互操作性
## Rust 基金会 2022 年中期报告

### Rust-C++ 互操作性

2 月份，Rust 基金会宣布了一项新举措，旨在改善 Rust 和 C++ 编程语言之间的互操作性，这得益于：

- 6 月份，[Jon Bauman](https://www.linkedin.com/in/jon-bauman-78b8342/) 加入 Rust 基金会，担任 Rust-C++ 互操作工程师，并开始制定互操作计划的结构和愿景。
- 目前正在制定此项初始研究的摘要和纲要，包括有关 Rust-C++ 互操作性状态的问题陈述、受影响群体和部门的纲要，以及该计划的短期和长期目标列表。

### Rust 安全计划

与此同时，安全计划专注于：

- 供应链安全
- crates.io 令牌安全
- 威胁建模
- 开发安全工具，如 [Painter](https://github.com/rustfoundation/painter) 和 [Typomania](https://docs.rs/crate/typomania/0.1.0/source/README.md)

“Rust 被公认为一种安全语言和生态系统。因此，我们希望尝试领先于未来可能出现的潜在安全问题，”Marcey 说。“基金会正在开展的一些项目，如 Painter 和 Typomania，试图正面解决这些潜在问题，我们尝试了解如果出现易受攻击的代码或人们尝试 [typosquat](https://thenewstack.io/vulnerabilities-versus-intentionally-malicious-software-components/) crates 时，潜在的途径。”

### Rust 语言规范

Rust 语言规范的进展包括：

- 任命一名团队负责人
- 聘请一名规范顾问

“Rust 项目及其出色的维护者每天都在对语言进行创新，”Marcey 说。“他们最近发布了 2024 年剩余时间和 2025 年的项目目标，其中很好地说明了语言优先级。”

### 捐赠和支持

除了 Google 捐赠的 100 万美元外，该基金会还收到了：

- [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 也捐赠了 100 万美元
- Alpha-Omega 项目为安全项目捐赠了 460,000 美元
- [Lambda Class](https://lambdaclass.com/) 捐赠了 100,000 美元

此外，AWS、Fastly、GitHub、Google Cloud 和 Microsoft Azure 等各种组织提供了基础设施支持。该报告认可了 Rust 基金会、Rust 项目团队和各种企业支持者在推进 Rust 计划方面做出的协作努力。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。