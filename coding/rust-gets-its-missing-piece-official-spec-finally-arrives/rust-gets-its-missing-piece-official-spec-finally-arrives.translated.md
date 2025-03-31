# Rust 补全了缺失的一块：官方规范终于到来

![Featued image for: Rust Gets Its Missing Piece: Official Spec Finally Arrives](https://cdn.thenewstack.io/media/2025/03/7da8b55b-tanja-tepavac-cwmhxnmqvq0-unsplash-1-1024x690.jpg)

[Rust 基金会](https://rustfoundation.org/)本周宣布，Ferrous Systems 正在将其 [Ferrocene Language Specification (FLS)](https://spec.ferrocene.dev/) 捐赠给 [Rust 项目](https://thenewstack.io/rust-programming-language-guide/)。

根据该基金会的说法，此次捐赠解决了 Rust 文档生态系统中的一个关键缺口——缺少官方语言规范。

## 重要一步

Accelerant.dev 的创始人兼“[Rust In Action](https://www.manning.com/books/rust-in-action)”一书的作者 Tim McNamara 告诉 The New Stack：“这是一个重要的步骤……规范允许编写大量额外的工具，这些工具可以依赖于[语言编译器](https://thenewstack.io/programming-languages/)的可预测行为。”

虽然 [Rust 项目](https://rust-lang.org/)已经积累了大量的文档、[课程和教程](https://doc.rust-lang.org/rust-by-example/)，包括官方的 [Rust book](https://doc.rust-lang.org/book/)、[Rust Reference](https://doc.rust-lang.org/stable/reference/) 及其在线图书馆中的更多内容，但一个关键的缺失部分是官方的[语言规范](https://thenewstack.io/inside-ecmascript-javascript-standard-gets-an-extra-stage/)。

The Futurum Group 的分析师 Mitch Ashley 告诉 The New Stack：“没有 [Rust 规范](https://thenewstack.io/rusts-rapid-rise-foundation-fuels-language-growth/) 这个问题目前还不是一个大问题。Rust 没有正式规范意味着编译器实现之间可能存在行为、结果和可移植性的潜在差异。由于 '[rustc](https://doc.rust-lang.org/rustc/)' 是社区中使用的主要编译器，因此这还不是一个大问题。如果出现更多实现，或者用 Rust 创建的软件必须经过正式验证过程，那么在没有规范的情况下很难做到这一点。”

## 是时候了

Rust 最初于 2015 年发布 ([Rust 1.0](https://thenewstack.io/the-rust-c-bridge-a-new-path-forward/))，即将迎来其 10 周年纪念日，现在是制定规范的时候了。

根据 Rust 基金会的说法，2022 年 12 月，提交了一个 [RFC](https://rust-lang.github.io/rfcs/3355-rust-spec.html)，以鼓励 Rust 项目开始制定规范。该 RFC 于 2023 年 7 月获得批准，工作开始。最初，Rust 项目规范团队 ([t-spec](https://www.rust-lang.org/governance/teams/lang#team-spec)) 有兴趣从头开始创建文档，并以 Rust Reference 作为指导标记。然而，该团队知道已经有一个外部 Rust 规范被成功地用于编译器资格认证目的——FLS，该基金会说。

## 什么是 FLS？

FLS 是对 Rust 编程语言的描述，由 [Ferrous Systems](https://ferrous-systems.com/) 于 2022 年 7 月开发，作为 [Ferrocene](https://spec.ferrocene.dev/) 的一部分，Ferrocene 是一个 Rust 编译器和工具链，专为安全关键和受监管的行业而设计。

该基金会在一份声明中表示：“FLS 为 Rust 的语法、语义和行为提供了结构化和详细的参考，为验证、合规性和标准化工作奠定了基础。”

由于当时 Rust 没有官方语言规范，也没有编写规范的计划，因此 FLS 代表着朝着以符合行业要求的方式描述 Rust 迈出的重要一步，尤其是在高保证领域。

McNamara 说，该规范代表着“Rust 的另一个复选框被选中，这将产生累积效应，从而建立对该语言的信心”。“这也是一个有趣的发展，因为商业模式与创建经过认证的编译器的传统方法不同。该规范背后的公司已经捐赠了它，并使其商业编译器开源。”

## 避免混淆

Rust 基金会指出，t-spec 团队希望避免行业中出现两个高度可见的 Rust 规范可能造成的混淆，并决定尝试将 FLS 与 Rust Reference 集成，以创建官方的 Rust 项目规范。他们联系了 Ferrous Systems，后者同意将其 FLS 贡献给 Rust 项目，并允许 Rust 项目接管其开发和管理。

这也将使 Rust 项目能够监督其持续发展，为已经依赖 FLS 的公司和开发人员提供信心，并标志着 Rust 生态系统的一个重要里程碑。
[Joel Marcey](https://www.linkedin.com/in/joelmarcey/)，Rust 基金会技术总监和 t-spec 团队成员，表示 Ferrous Systems 已经为这项工作做了大量的基础工作。

他在一份声明中说：“将 FLS 正式整合到 Rust 项目中，将使 t-spec 团队能够加速我们在交付官方 Rust 规范方面的进展，该规范可供开发人员、安全关键工具供应商以及其他希望通过语言规范开展工作的人员使用。”

在 FLS 整合到 Rust 项目的过程中，会有一个过渡期。第一阶段的工作将包括将 FLS 纳入项目的工具和流程中，使其与现有的 [Rust 项目目标](https://rust-lang.github.io/rust-project-goals/2025h1/spec-fls-publish.html)保持一致。在该整合之后，Ferrous Systems 将停止其自身的规范。

展望未来，FLS 和 Rust 参考都将构成官方 Rust 规范。

## Ferrous Systems 和 Ferrocene

Ferrous Systems 的联合创始人 [Felix Gilcher](https://www.linkedin.com/in/felix-gilcher-906463283/?originalSubdomain=de) 在一份声明中说：“我们最初创建 Ferrocene 语言规范是为了提供 Rust 的结构化和可靠的描述，以便对 Ferrocene 编译器进行认证。”

Ferrous Systems 是一家位于柏林的咨询公司，专门从事 Rust 软件开发和培训。

Gilcher 说：“作为一家开源优先的公司，将 FLS 贡献给 Rust 项目是朝着促进统一的、社区驱动的规范发展的合乎逻辑的一步，该规范使所有 Rust 用户受益。我们很高兴支持这项工作，并期待这将对 Rust 在受监管和高保证领域的采用产生长期影响。”

Ferrocene 是一个开源 Rust 编译器工具链，适用于安全和任务关键型应用，例如汽车、工业和医疗开发。今年 1 月，Ferrocene 获得了医疗设备软件的 IEC 62304 C 类认证。事实上，Ferrocene 是第一个通过开源认证的 Rust 编译器工具链，适用于安全和任务关键型应用。Ferrous Systems 的总经理兼联合创始人 [Florian Gilcher](https://www.linkedin.com/in/floriangilcher/?locale=en_US) 表示，它已获得汽车（ISO 26262，ASIL-D）、工业开发（IEC 61508，SIL4）和医疗（IEC 62304，C 类）标准的认证，并且未来还将获得更多认证。

他说，Ferrocene 获得这些标准的认证“表明了我们致力于通过增强安全性和性能的工具来推进安全关键型软件开发的承诺”。

[技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，即可观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)