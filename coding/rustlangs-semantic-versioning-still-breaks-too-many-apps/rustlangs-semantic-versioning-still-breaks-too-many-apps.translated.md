# RustLang 的语义版本控制仍然导致太多应用程序崩溃

![RustLang 的语义版本控制仍然导致太多应用程序崩溃的特色图片](https://cdn.thenewstack.io/media/2024/07/40206855-rust-semverchecksbb-1024x682.png)

语义版本控制仍然是标记软件包新版本的最佳方式吗？[Rust 社区](https://thenewstack.io/rust-programming-language/)可能正在围绕这种行业范围的方法遇到一些挑战。

在对 1000 个最流行的 Rust 工具（打包为 [Rust crates](https://crates.io/)）进行的 [调查](https://predr.ag/blog/semver-violations-are-common-better-tooling-is-the-answer/)中，一组开发人员发现 17.2% 的软件包至少存在一个 SemVer 违规 - 在调查的所有 Rust 软件包中约有 1/6。

换句话说，在调查中基于这些 crates 运行项目的某人每 10 天就会遇到一次重大更改，Rust 开发人员 [Predrag Gruevski](https://predr.ag/) 指出，他在最近的 [Changelog 播客](https://changelog.com/podcast/597) 中讨论了 SemVer 的局限性，也是上述研究的作者之一。

“当这些重大更改发生时，它们会破坏整个生态系统，”Gruevski 说。“成千上万的人必须花时间弄清楚为什么构建突然变红了。”

正如该节目的另一位嘉宾，前端开发人员 [Chris Krycho](https://v5.chriskrycho.com/index.html) 指出的那样，正确使用 SemVer 是一个基本的沟通问题。语言维护者必须向最终用户和最终用户工具传达更新信息，以便他们可以确定是否需要在自己的应用程序中更新软件包，以及这样做是否会导致程序崩溃。

“作为 SemVer 的使用者，我不关心数字。我只想避免修复我无意破坏的东西，”Gruevski 说。

## SemVer 简化

[语义版本](https://semver.org/) 规范为迭代软件包的连续版本提供了一种（看似）简单的格式 - MAJOR.MINOR.PATCH：

**MAJOR** 版本，当您进行不兼容（API 更改）时。**MINOR** 版本，当您以向后兼容的方式添加功能时。**PATCH** 版本，当您进行向后兼容的错误修复时。
可以在编号字符串的末尾附加额外的元数据（例如“alpha 版本”。）

对于 Rust，[构成](https://doc.rust-lang.org/cargo/reference/semver.html) 主要版本的模糊性逐渐显现。

添加新特征通常被认为值得进行次要升级，尽管在某些情况下，如果 [特征](https://doc.rust-lang.org/book/ch10-02-traits.html) 或共享功能基于与其他特征的冲突，则添加可能会导致主要升级。

文档提供了其他重大或主要功能的冗长列表，包括：

- 每当公共
[项目](https://doc.rust-lang.org/reference/items.html)（例如模块）发生更改、移动或删除时 - 当所有当前字段都是公共字段时，或当没有先前的结构字段时，添加私有结构字段
- 添加新的枚举变体，或向枚举变体添加新字段
- 缩小泛型边界
- 添加或删除函数参数

对现有 Rust 应用程序的任何这些更改都可能导致编译错误或对毫无戒心的用户造成意外行为。

## 自动化 SemVer 的力量

[语义版本控制](https://www.joabj.com/Writing/Tech/Dev/1509-Software-Versioning.html) 的力量，至少在理论上，是版本控制应该统一，以便捆绑器可以识别非破坏性更改，并在下次构建中自动包含升级，而不会破坏任何东西

“当我维护一个工具时，我有几百个依赖项，我不一定想仔细查看各种不同的版本号，并思考它们都意味着什么，”Gruevski 说。“但我想要做的是在我的 Rust 项目中运行 Cargo 更新，并知道因为每个人都遵守什么是破坏性更改，所以在我执行完该命令后，我的项目仍然可以正常工作。”

Gruevski 创建了一个工具 [cargo-semver-checks](https://crates.io/crates/cargo-semver-checks)，它扫描 Rust crates 并标记 SemVer 违规。可以将其视为用于检查版本编号的 linter。它可以在构建管道中使用，以确保 Rust 中的升级不会破坏代码库中的任何依赖项（它也可以在 [GitHub 工作流程](https://github.com/obi1kenobi/cargo-semver-checks-action) 中使用）。

目前，SemverChecks 约有 80 个“lint”或规则，用于识别重大更改，这些更改可以通过测试程序产生意外行为或完全无法编译来定义。

Gruevski 承认该程序应该捕获至少 150 种其他行为，但没有捕获。（鼓励用户贡献自己的 lint）。
1 月，Gruevski 发布了一篇 [博客文章](https://predr.ag/blog/four-challenges-cargo-semver-checks-has-yet-to-tackle/)，列出了 Rust 中许多剩余的模糊之处。一方面，存在着难以置信数量的边缘情况，这些情况在事后看来似乎很明显，但几乎不可能预料到。意外的依赖关系可能会在多个依赖关系中出现。不检查类型也会导致问题。

Krycho 指出了 linter 会错过的破坏性更改类型：对数据结构的重构，使其更明智地使用内存，可能是破坏性更改，即使它没有改变相应的 API。它在可扩展性方面的变化本身就足以提醒最终用户。

[就像 YAML 一样，](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/) SemVer 规范的全部内容可能具有欺骗性地简单，尤其是在像 [Rustlang](https://thenewstack.io/rust-the-future-of-fail-safe-software-development/) 这样具有许多细微之处的语言中。
“我已经做了很多年了，每周都会发现一种新的可怕方式，会导致 Rust 项目中意外地发生破坏性更改，”Gruevski 说。

规则太多了，而且很容易在没有注意到的情况下违反其中一条规则。

“看似最无害的更改最终会因为某些原因而导致破坏，而这些原因是任何理智的人都不会想到的，”Gruevski 说。

## 海勒姆定律
Krycho 指出，多个参与项目的人员可能会进一步混淆情况。

他曾在另一种语言 [Typescript](https://thenewstack.io/TypeScript/) 中使用过 SemVer，并发现了类似的问题。

“谁来决定是错误修复还是重大破坏？你并不总是知道，”他说。“语义听起来不错，但导致破坏性更改的定义变得模糊。”

TypeScript ([目前版本 5.5](https://thenewstack.io/typescript-5-5-faster-smarter-and-more-powerful/)) 并不严格遵循语义版本控制，但由于它在 [Node.js](https://thenewstack.io/qa-tracy-hinds-bringing-node-js-people/) 生态系统中使用，因此它 [确实遵循](https://www.semver-ts.org/1-background.html) MAJOR.MINOR.PATCH 格式。

TypeScript 的方法更像是将每次更改都视为潜在的破坏性更改，即使是错误修复。

Kyrcho 指出了 [海勒姆定律](https://www.hyrumslaw.com/)，该定律以一位 Google 工程师的名字命名，他注意到，在用户数量足够多的情况下，系统的每种可观察行为都将对某些用户至关重要。即使是错误更改也可能导致破坏性更改。

“如果我的错误修复破坏了我的整个用户群，我应该称之为错误修复吗？”Krycho 问。

他说，你仍然需要人工干预，才能判断哪些更改会真正破坏用户群。

## 其他生态系统中的版本控制
需要注意的是，并非所有软件包都遵循 SemVer。Python 目前固定在 3.X 版本，并且将通过次要版本进行递增，无论是否发生破坏性更改，尽管社区正在考虑转向 [基于年份的版本控制](https://thenewstack.io/python-mulls-a-change-in-version-numbering/)，因此在 2024 年发布的 Python 版本将是 Python 3.24。

ECMAscript 和 JavaScript 只使用 [四位数的年份本身](https://thenewstack.io/ecmascript-specs-approved-and-how-google-sheets-used-wasmgc/) 作为版本号。

Canonical 为 Ubuntu 使用基于日历的版本控制 (CalVer)。最新的版本号 [24.04](https://ubuntu.com/download/server) 表示它是在 2024 年 4 月左右发布的。

因此，正如 Gruevki 指出的那样，所有这些方法的问题在于，管理员又回到了阅读发行说明以查找破坏性更改。

即使那些看起来遵循 SemVer 的软件包也有自己的怪癖。

[EmberJS](https://thenewstack.io/choose-your-own-adventure-emberjs-co-creator-tom-dale/) 某种程度上遵循 SemVer，但只升级到下一个主要版本以提醒用户弃用的代码。
有些软件项目将下一个版本升级到主要版本，仅仅是为了从主要版本获得的营销优势 ([来自贸易出版物的免费宣传](https://thenewstack.io/six-years-later-mesos-makes-version-1-0-now-real-fun-begins/))。

Krycho 建议，也许我们需要将软件的营销版本作为完全不同的东西。

即使是 [Linus Torvalds](https://thenewstack.io/linus-torvalds-on-security-ai-open-source-and-trust/)，Linux 的守护者，也 [将 Linux](https://www.makeuseof.com/how-are-linux-kernel-versions-formed/) 从 2.6 升级到版本 5，仅仅是因为次要修订的数量超过了他可以用手指和脚趾计算的范围。

您可以在此处享受完整的 Changelog 播客：

[Changelog Interviews 597: MAJOR.SEMVER.PATCH](https://changelog.com/podcast/597) – 在 [Changelog.com](https://changelog.com/) 上收听
[YOUTUBE.COM/THENEWSTACK]
科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看所有播客、访谈、演示等。

[https://youtube.com/thenewstack?sub_confirmation=1](https://youtube.com/thenewstack?sub_confirmation=1)