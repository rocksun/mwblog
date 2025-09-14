根据软件供应链安全公司 [Anchore](https://anchore.com/) 的安全副总裁 [Josh Bressers](https://www.linkedin.com/in/joshbressers/) 的说法，现在是时候更新政府关于软件物料清单 (SBOM) 最低要素的指导意见了。

最近发布的[修订草案](https://www.cisa.gov/sites/default/files/2025-08/2025_CISA_SBOM_Minimum_Elements.pdf)是对 2021 年原始版本的更新，目前正在公开征求意见，截止日期为 10 月 3 日。

“我们都非常高兴他们正在更新这份文件，因为在这个领域里，2021 年就像其他领域里的 100 年前，”Open Source Security Foundation (OpenSFF) 技术咨询委员会成员兼 [OpenSSF SBOM Everywhere](https://openssf.org/blog/2022/09/13/funding-python-spdx-development-with-the-openssf-and-sbom-everywhere/) 项目的联合负责人 Bressers 说。

[![Michael Lieberman](https://cdn.thenewstack.io/media/2025/09/fb4c3898-lieberman-150x150.png)](https://cdn.thenewstack.io/media/2025/09/fb4c3898-lieberman-150x150.png)

Michael Lieberman

[![Josh Bressers](https://cdn.thenewstack.io/media/2025/09/1e4dbe4b-bressers-150x150.png)](https://cdn.thenewstack.io/media/2025/09/1e4dbe4b-bressers-150x150.png)

Josh Bressers

在采访中，他和供应链安全供应商 [Kusari](https://www.kusari.dev/) 的联合创始人兼 CTO [Michael Lieberman](https://www.linkedin.com/in/michael-lieberman-65786ba/) 指出，SBOM 需要更多的清晰度和粒度。Lieberman 也是 OpenSFF 技术咨询委员会的成员，以及 [OpenSSF SLSA](https://openssf.org/projects/slsa/) 指导委员会的成员。

Lieberman 说，长期以来都需要更深入地了解软件的组成部分，他提到了汽车行业的 [高田气囊召回事件](https://www.nhtsa.gov/vehicle-safety/takata-recall-spotlight#:~:text=Overview,involves%20non%2Dazide%20driver%20inflators.)。

“每辆离开工厂的汽车，他们都清楚地知道汽车里装了什么，”他说。“他们确切地知道哪一批螺丝和每个螺栓，这样，如果结果证明，‘嘿，有一批螺栓有问题……这些螺栓用于这些日期之间生产的汽车。’太好了，他们知道，他们可以召回所有这些汽车。

“但医疗设备的情况并非如此，这显然很可怕，有人可能会说，‘你的起搏器里有存在漏洞的软件吗？从技术上讲，有人可能会做些什么来入侵起搏器吗？’就像，‘哦，我不知道。’”

## **深入细节**

2021 年，[关于改进国家网络安全的行政命令](https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity) 强制要求所有政府机构使用 SBOM 来消费和生产软件。SBOM 是构成软件的所有软件组件、库和依赖项的明确列表，最初仅要求联邦机构使用，但现在也已推广到软件供应商。最近，它也被倡导作为一种更好地保护任何组织运营的方式。

商务部下属的国家电信和信息管理局 (NTIA) 最初制定了 [SBOM 中应包含的最低要素](https://thenewstack.io/creating-a-minimum-elements-sbom-document-in-5-minutes/)。这项工作后来转移到了国土安全部的网络安全和基础设施安全局 (CISA)。

该修订草案引入了四个新的数据字段：组件哈希值、其唯一标识符；许可证，软件组件可用的许可证；工具名称，SBOM 作者用于创建 SBOM 的工具的名称；以及生成上下文，关于 SBOM 何时生成的精确数据。

它对五个数据字段进行了重大更新：SBOM 作者、软件生产者、组件版本、软件标识符和依赖关系。

Lieberman 认为，包含组件哈希值可能是最重要的补充。这是一种区分看似相同的版本但构建方式可能不同的方法。

“在当今的许多软件中，您的 foo 软件包版本 1 可能与我的 foo 软件包版本 1 不同，这取决于我们从哪里获得它？它是来自 Linux 发行版的一部分吗？您是从 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 获得的，还是从 Debian 获得的？这些事情最终可能导致您获得类似的东西，是的，从技术上讲，它是该软件包的 1.0 版本，但它是为您的生态系统以不同的方式构建的，这通常会导致很多混乱，”他说。

“如果我们回到 [XZ 事件](https://en.wikipedia.org/wiki/XZ_Utils_backdoor)……那件事主要影响了某些 Linux 发行版，但没有影响其他发行版。……除非您可以比较哈希值并检查以确认，‘我是否真的提取了该特定构建版本的某物？’否则您将无法知道这一点？”

他补充说，“当有人说，‘我有一个特定版本的 OpenSSL 或 log4J’时，这可能意味着很多不同的事情。它可能意味着我下载了一个 JAR 文件（如果是 Java），或者我下载了一个 Debian 软件包或一个 Red Hat 软件包或一个容器镜像，所有这些东西都略有不同。

“如果您从一个供应商处购买，或者从一个开源位置提取，或者从另一个开源位置提取，它们可能具有不同的哈希值，因为它们的构建方式略有不同。因此，您需要通过哈希值确切地知道您拥有哪一个，才能修复问题——或者知道您没有问题。”

添加生成上下文（无论是在构建前、构建期间还是构建后）也很重要。他说，在构建期间生成的 SBOM 往往是最完整的。

“您获得的作为构建过程一部分的 SBOM 是最好的，因为依赖项解析发生在构建期间。因此，当您下载这些软件包时，您可以实际捕获哈希值，即组件哈希值。您可以捕获您提取的确切版本以及所有其他信息。因为同样，根据您使用的语言，根据您所属的生态系统，说我正在下载某个东西的 1.0 版本，那么，它是否意味着带有这些补丁的 1.0 版本？没有这些补丁的 1.0 版本？我们怎么才能真正知道？”他说。

在您提取软件包时提取哈希值意味着您有一个精确的记录，如果您后来发现它是一个错误的哈希值，您可以处理它。

知道用于生成 SBOM 的工具也很重要，因为有时一个工具比另一个工具更适合特定的用例，他说。

## **监管正在推动采用**

Snyk 的 2024 年“[开源现状报告](https://view.snyk.io/the-state-of-open-source-report-2024/p/1)”发现，62.4% 的组织正在实施 SBOM 监控，而 [Anchore 的 2024 年调查](https://anchore.com/press/anchore-survey-shows-only-1-in-5-organizations-have-full-visibility-into-their-open-source-software-components) 显示，78% 的组织计划在 18 个月内增加 SBOM 的使用。

然而，早在 2025 年初，软件供应链安全公司 [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention) 的联合创始人兼 CEO [Dan Lorenc](https://www.linkedin.com/in/danlorenc/) 预测，如果没有更大的监管推动，[SBOM 将会是哑弹](https://thenewstack.io/rust-will-explode-sboms-will-be-duds-open-source-predictions/)。[Sonotype 白皮书](https://www.sonatype.com/resources/whitepapers/2023-sbom-survey-report) 认为，2021 年的行政命令是 92% 的大型企业已经实施或计划采用 SBOM 的驱动因素之一，并且 60% 的企业要求合作伙伴这样做。

根据 Bressers 的说法，推动 SBOM 采用的真正动力是欧盟的 [网络弹性法案](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) (CRA)。TNS 的 [Joab Jackson](https://thenewstack.io/author/joab/) 最近指出，除非开源开发者主动从他们的软件中赚钱，否则他们不会直接[受到 CRA 的约束](https://thenewstack.io/what-the-eus-cyber-resilience-act-cra-means-for-open-source/)。但是，使用开源组件的供应商将受到约束。

“几个月前，我在一次会议上谈到了这一点，很多观众都说，‘哦，但我们不向欧洲销售。’我说，‘你们不向欧洲销售，但你们的客户向欧洲销售。你们猜怎么着？他们会来找你们要 [SBOM]。’因此，CRA，[网络弹性法案](https://thenewstack.io/lf-europe-chief-warns-developers-on-eus-cyber-resilience-act/)，基本上是在说，如果你向欧洲市场销售，你正在销售软件，你需要 SBOM，”Bressers 说。

## OpenSSF 正在做什么

OpenSSF 在 2022 年发布了一项[动员计划](https://openssf.org/oss-security-mobilization-plan/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)，其中包括一项名为“SBOM Everywhere：改进 SBOM 工具和培训以推动采用”的倡议。Bressers 说，它刚刚开始讨论如何评论拟议的新 CISA 最低要素草案。

“因此，我们目前在 OpenSSF 所做的工作还处于早期阶段，对吧？……在大多数情况下，CISA 的新最低要素 [文档] 非常好。我认为从 OpenSSF 的角度来看，这将主要是确保我们清楚地定义术语，并确保考虑到一些可能奇怪的开源边缘情况，”他说。

“我将给您两个例子。所以在系统 RFC [征求意见稿] 中有两个部分，他们想知道 SBOM 作者。这一个感觉说得通。但是软件生产者，什么是生产者，对吧？我们不知道。我们需要研究语言，以确保我们清楚地定义这在生成 SBOM 的上下文中意味着什么。”

版本提出了其他挑战。

“不幸的是，版本不像在开源中那样简单，因为，假设您有一个软件包，某个开源项目，它现在可能是 1.6 版本。当您将其放入像 Linux 发行版这样的东西中时，它们有一种叫做 [epoch](https://antfu.me/posts/epoch-semver) 的东西，可以在开头添加一个 1。epoch 的目的是说，这个版本大于任何没有 epoch 的版本。这听起来有点复杂。……版本可能会降低。说起来很疯狂，但当它这样做时，Debian、像 Debian 和 Red Hat 以及 Ubuntu 这样的 Linux 发行版会说，‘强制此版本大于上一个版本，无论它说什么。’那么，epoch 呢？我们如何处理这些东西？”Bressers 说。

“NTIA 最低要素中有一些东西，是的，我们遵守，但实际上在这个时代已经没有任何意义了，因为……很多东西的定义方式，它只是没有意义，他们想要指向软件的原始来源。在开源世界中，这到底是什么意思？你知道，我们是在谈论 Debian 吗？我们是在谈论它来自的项目吗？我们是在谈论编写它的人吗？谁知道呢？”

虽然该文档确实在一定程度上涉及了 AI，但 Bressers 表示，他不认为它会深入研究它。

“我认为这没关系，因为整个 AI BOM 或 AI 的 SBOM 或您想以任何方式排列这些词，我认为作为一个行业，我们仍在弄清楚很多事情，所以这很好，对吧？我也不希望看到政府对这种非常新的东西的指导。”

与此同时，包括印度、日本、德国和其他国家在内的多个国家正在制定类似的指导意见。挑战将在于协调各种要求。

“我觉得对于像 SBOM 这样的技术，我们正在达到一个需要建立行业、政府和开源之间的社区的程度，因为我认为我们从未见过，我猜，像这样的问题空间，对吧？它影响了如此广泛的软件。它实际上是所有的软件。因此，我对接下来会发生什么感到兴奋和恐惧，”Bressers 说。“因此，这也是我想确保我们有像 OpenSSF 这样的组织尽最大努力帮助每个人保持一致的原因之一，而且我们了解正在发生的事情。”