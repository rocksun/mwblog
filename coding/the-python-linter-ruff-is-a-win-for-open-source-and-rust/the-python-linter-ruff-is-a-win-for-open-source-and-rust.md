
<!--
title: Python Linter Ruff是开源和Rust的胜利
cover: https://cdn.thenewstack.io/media/2024/07/3806fa61-ruff.jpg
-->

2022 年，Charlie Marsh 用 Rust 编写了一个快速开源 Python 代码检查器。如今，Ruff 每周下载量达数百万次，Marsh 也体会到了开源的力量。

> 译自 [The Python Linter Ruff Is a Win for Open Source — and Rust](https://thenewstack.io/the-python-linter-ruff-is-a-win-for-open-source-and-rust/)，作者 David Cassel。

Astral Software [描述其使命](https://astral.sh/about) 为“为 Python 生态系统提供高性能的开发人员工具，从 Ruff 开始，这是一个用 Rust 编写的极速 Python 代码检查器。”

同一页面还包含 Astral 创始人 [Charlie Marsh](https://www.linkedin.com/in/marshcharles/) 的更宏大目标声明。“对我来说，对 Ruff 的反应本身就证明了一个机会：通过构建高性能的开发人员工具来提高 Python 生态系统的生产力。”

有一点是肯定的：这是一段旋风般的旅程。去年 10 月，Marsh 在 [一篇博文中](https://astral.sh/blog/the-ruff-formatter) 指出，“一年前，我对 Ruff 做了第一个提交，这是一个用 Rust 编写的极速 Python 代码检查器。从那时起，Ruff 每周的下载量已达到数百万次，并支持数百条 lint 规则，可以作为 Flake8、isort 和 pyupgrade 等数十种工具的直接替代品。”

这是一个快速成功的案例，Ruff 为我们提供了一个很好的例子，它从编程世界的其他部分汲取灵感，然后思考开发人员真正想要什么。

在此过程中，Charlie Marsh 也从高速发展的开源开发中吸取了很多经验……

![](https://cdn.thenewstack.io/media/2024/06/0fe1dd31-screenshot-from-astral-blog-post-announcing-seed-funding-april-18-2023.png)

## 开源之旅

那篇 10 月的博文宣布了 Ruff 的 Python 格式化程序的发布——他们的第一个非代码检查器工具——强调统一的工具链是他们的最终目标。但格式化程序的发布也是一个里程碑：第一个 [由团队协作构建的工具](https://thenewstack.io/distributed-teams-distributed-applications-collaboration-in-a-cloud-native-world/)。“Ruff 代码检查器的第一个草稿是我在山洞里写的，”Marsh 开玩笑地说。（补充道，“我们现在已经发展到一个由五人组成的核心团队，拥有超过 290 名贡献者。”）

在很短的时间内，Ruff 已经成为一个真正的开源成功故事。在 [2023 年 4 月](https://astral.sh/blog/announcing-astral-the-company-behind-ruff)，Marsh 将 Ruff 称为“我第一次大规模参与开源维护的经历，我一直在有意地创建一个项目和一个环境，让新老贡献者都感到宾至如归。”

在 [最近对 Software Engineering Daily 播客的采访中](https://softwareengineeringdaily.com/2024/06/12/ruff-and-next-generation-python-tooling-with-charlie-marsh/)，Marsh 说 Ruff 现在已经建立了“一个强大且可持续的贡献者基础。实际上，你有很多贡献者，这是他们第一次编写

[Rust](https://thenewstack.io/rustlangs-semantic-versioning-still-breaks-too-many-apps/)，他们将 Ruff 视为一个有趣的切入点。”

Marsh 补充说，他们有意识地努力使其成为一个友好的社区。“所以，你知道，努力提供良好的贡献者文档，愿意并能够指导那些第一次编写 Rust 代码的人，并给他们反馈，并指导他们完成整个过程。这些都是我们努力做的事情。”

Marsh 承认，从普林斯顿大学毕业后，他“更多的是开源的消费者，而不是维护者。”因此，推出 Ruff 的经历成为“一个关于成为维护者的速成课程，”他在播客中说。

虽然最初只有少数用户，但用户群增长得如此迅速，以至于“我们发布的任何东西都会在五分钟内收到反馈并经过测试。”

Marsh 笑了起来，承认他更喜欢早期阶段，那段时期更有趣——因为他已经了解到，当你必须维护用户群的兼容性时，构建软件会更难。“就像，能力越大，责任越大。”

但他还将这个成熟阶段描述为“非常有意义”——他感谢用户不断提供的反馈。

> 问题是好事。问题意味着人们正在使用它。
>
>— Charlie Marsh (@charliermarsh)
> [2024 年 5 月 31 日]

“我认为，这是让开源变得真正有趣的一部分……你与用户之间有着直接的关系，这种关系在其他许多软件类别中并不存在。”

## 起源故事

Marsh 在 2022 年 10 月创立了 Astral，此前他在 Spring Discovery 担任软件工程师四年半，该公司拥有一个基于机器学习的临床研究工具平台。Marsh 在播客中说，在此之前，他在可汗学院担任 [高级软件工程师](https://thenewstack.io/what-it-takes-to-become-a-senior-engineer/)，在那里他负责他们的 iOS 和 Android 应用程序——以及一个基于 Python 的 Web 应用程序，以及一个使用“大量 React”的 Web 前端。

“我职业生涯中一直在不同编程生态系统之间跳跃，这有点无意为之，”Marsh 在 [2023 年](https://blog.jetbrains.com/pycharm/2023/02/ruff-python-linter-interview-with-charlie-marsh/) 告诉 JetBrains，并补充说，“在这些生态系统之间切换真正影响了我对工具的思考方式。我看到网络做得好的地方，我想把它带到 Python，反之亦然。Ruff 基于许多这样的观察……”

例如，网络生态系统显然拥有更多非 JavaScript 工具。在播客中，Marsh 说他也知道 Python 与 Rust 有很好的联系，“一个非常好的工具生态系统，以不同的方式实现 Rust-Python 桥接。”

一件事接着一件事，在 Ruff 发布五个月后，它已被采用为包括 Pandas、FastAPI、Apache Airflow 在内的顶级 Python 项目的主要 linter，根据 [Marsh 的一篇博文](https://notes.crmarsh.com/ruff-the-first-200-releases)。（这篇文章指出，Ruff 的第一个版本支持 20 个 lint 规则，但五个月后它 [支持 376 个](https://github.com/charliermarsh/ruff#supported-rules)。此外，它还添加了官方 VS Code 扩展和官方语言服务器协议……）

到 2023 年 4 月，Astral Software 宣布计划“继续为 Python 生态系统构建高性能开发工具”——从 Accel、Caffeinated Capital 甚至 Docker 创始人 Solomon Hykes 等投资者那里筹集了 [400 万美元的种子资金](https://astral.sh/blog/announcing-astral-the-company-behind-ruff)。“简而言之，我们将把 Ruff 背后的理念发挥到极致，方法是 (1) 扩展 Ruff 本身，以及 (2) 构建更多类似 Ruff 的东西。”（商业计划是“在我们的工具之上构建和销售服务”，而“工具本身将保持免费和开源。”）

到那时，Ruff 每月下载量已超过 100 万次，Marsh [在博客中](https://astral.sh/blog/announcing-astral-the-company-behind-ruff) 写道，[微软](https://news.microsoft.com/?utm_content=inline+mention)、[亚马逊](https://aws.amazon.com/?utm_content=inline+mention)、Netflix、Mozilla 和 Hugging Face 等大型公司已采用 Ruff。“许多成熟的项目和公司现在每天都依靠 Ruff 来编写代码。

“我认为这是我最大的动力来源，也是我最重要的责任。感谢您的信任。我不会让您失望。”

## 性能——以及更多

Astral 继续扩展其免费工具系列。2 月，该公司 [宣布了 uv](https://astral.sh/blog/uv)，将其描述为“一个极快的 Python 包安装程序和解析器，用 Rust 编写，旨在作为 pip 和 pip-tools 工作流程的直接替代品。”



使用热缓存，uv 安装几乎是即时的。在这里，它比 pip 和 pip-tools 快 75 倍以上。

当然，Astral 继续更新 Ruff。截至 [5 月 22 日](https://astral.sh/blog/announcing-astral-the-company-behind-ruff)，Ruff 附带了新内置语言服务器（用 Rust 编写）的 beta 版本，提供与其旧版 [ruff-lsp](https://pypi.org/project/ruff-lsp/0.0.9/) 实现相同的特性。

但在播客中被问及 Ruff 的卖点时，Marsh 已经有了答案。“旗舰功能是性能。第二是简单。”但第三个功能是他所说的“可采用性”。“我们只是非常专注于使其易于采用……从一开始，我们就基本上将我们的规则映射回现有的其他 linter，这样当人们迁移时，他们应该看到有效相同的违规集。这非常有用，因为人们在项目之间迁移——他们已经认识这些规则。他们已经熟悉它们了。他们的项目可能已经符合这些规则。”

Marsh 指出，Python 有很多不同的工具，“有点偶然……我们最终将很多工具整合到一个工具中。”因此，虽然他们的主要目标是性能，但 Marsh 认为这“对用户来说是最有影响力的东西之一……当人们迁移到 Ruff 时，他们通常会用一个工具替换 20 或 30 个工具。”

![](https://cdn.thenewstack.io/media/2024/06/ac8dffa2-screenshot-from-astral-software-home-page.png)

此外，“我们很多规则都附带自动修复……我们将进行代码转换以尝试自动修复它们。”

## 未来功能
在采访中，Marsh 还指出该工具“变化很大”，同时他们正在“积极地”开发它。然后他提供了一些关于 Ruff 未来发展的线索。Marsh 表示，他“非常感兴趣”将来支持用户自定义 linter 规则的功能，并希望看到 Ruff 对跨文件的类型推断和分析进行推断。Marsh 后来指出，能够跨文件工作“对语言服务器非常重要”，称之为“我们将在未来一年内考虑的事情……将 Ruff 发展成能够处理跨多个文件的分析、能够对 Python 进行非常智能的类型推断、能够支持非常好的编辑器体验的东西”。

Marsh 被问了一个有趣的问题：在未来 5 到 10 年，linter 会如何改变——尤其是随着 AI 增强功能进入许多开发工具。他给出了一个有趣的答案——如果机器生成代码，那么静态分析工具之类的工具变得更加重要。“如果人们生成更多代码，我认为一致、可解释且可靠的工具的价值实际上可能会上升。例如，如果你有一堆*生成的*代码，那么使用 linter 来强制执行一致性、样式和正确性，我认为实际上比今天更重要。”

Marsh 已经看到了 [大型语言模型](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/) 驱动的 linter 的“有趣探索”，其中用户输入的纯文本描述或示例将应用于整个代码库。

Marsh 甚至曾经构建了一个原型——然后得出结论：“根据我的经验，大多数人实际上并不想编写自己的 lint 规则。我认为，这实际上是 linter 的价值所在……

“你正在构建一组经过精心策划和有见地的规则……大多数人不想坐下来开发自己的规则分类法——即使这样做非常容易。”
