<!--
title: Kroah-Hartman：Linux内核维护者谈开源项目的影响力
cover: https://cdn.thenewstack.io/media/2025/11/42c41e50-kroah-hartman.jpg
summary: 欧盟《网络韧性法案》（CRA）旨在加强数字产品网络安全。该法案主要针对制造商，对开源个人开发者和保管者责任较轻。CRA 已生效，将于2027年强制执行。个人开发者若代码未用于商业产品则无需担忧。保管者需提供联系方式并处理漏洞。建议开源社区抵制将合规责任转嫁的行为。OpenSSF正提供指导与支持。CRA将提升整体软件安全标准。
-->

欧盟《网络韧性法案》（CRA）旨在加强数字产品网络安全。该法案主要针对制造商，对开源个人开发者和保管者责任较轻。CRA 已生效，将于2027年强制执行。个人开发者若代码未用于商业产品则无需担忧。保管者需提供联系方式并处理漏洞。建议开源社区抵制将合规责任转嫁的行为。OpenSSF正提供指导与支持。CRA将提升整体软件安全标准。

> 译自：[Kroah-Hartman: Linux Kernel Maintainer on CRA Open Source Impact](https://thenewstack.io/kroah-hartman-linux-kernel-maintainer-on-cra-open-source-impact/)
> 
> 作者：Steven J. Vaughan-Nichols

亚特兰大 — 科技公司和开发者们终于意识到，他们需要应对[欧盟（EU）的《网络韧性法案》（CRA）](https://thenewstack.io/what-the-eus-cyber-resilience-act-cra-means-for-open-source/)。幸运的是，正如[Linux 内核](https://thenewstack.io/how-ai-helps-maintain-the-linux-kernel/)稳定分支的维护者 [Greg Kroah-Hartman](https://www.linkedin.com/in/greg-kroah-hartman/?originalSubdomain=nl) 在 [KubeCon + CloudNativeCon North America 2025](https://docs.google.com/document/u/0/d/1aKlGA2jFJQHcvj3HBYSa4zv5J1kCSuqHKDHP4cWLkBw/edit) 上解释的那样，如果你是一名个人开源开发者，你并没有太多可担心的。然而，如果你的代码最终出现在欧盟市场的商业产品中，情况就不同了。

## 理解欧盟《网络韧性法案》（CRA）

不过，在深入探讨之前，让我们快速回顾一下 [CRA 是什么](https://thenewstack.io/what-the-eus-cyber-resilience-act-cra-means-for-open-source/)，因为正如 Linux 基金会在最近的一项调查中指出的那样，[62% 的开发者及其公司对 CRA 几乎一无所知](https://www.linuxfoundation.org/hubfs/Research%20Reports/lfr_cra_readiness_050125a.pdf?hsLang=en)。CRA 是一套全面的法规，旨在为在欧盟销售或使用的、具有数字元素的产品（硬件、软件和网络连接设备）建立统一的网络安全标准。

该法案旨在显著增强网络安全并减少漏洞，同时让制造商、进口商和分销商对其在整个产品生命周期中的数字产品安全性负责。这意味着从设计和开发到部署和退役的整个过程。

## CRA 利益相关者群体和责任

CRA 要求产品在设计时就应安全，定期更新，清楚披露软件依赖关系，并提供安全默认配置的机制。该立法针对的是网络安全不足和缺乏及时安全更新等问题，这些问题使数字产品容易受到攻击，用户也难以评估和保护。

根据 CRA，有三个不同的[利益相关者群体，每个群体都有独特的责任和监管义务级别](https://www.linuxfoundation.org/hubfs/Research%20Reports/lfr_cra_readiness_050125a.pdf?hsLang=en)。它们是：

*   **制造商**: 在欧盟市场上开发、组装或投放具有数字元素（硬件、软件或固件）产品的公司或组织。制造商承担 CRA 合规的主要责任，包括确保整个产品生命周期的网络安全，维护[软件物料清单（SBOM）](https://thenewstack.io/how-to-create-a-software-bill-of-materials/)，处理漏洞，并促进供应链透明度。
*   **保管者**: 组织，通常是非营利组织或基金会（如 Linux 基金会、Apache、Eclipse），负责维护供商业使用的开源软件项目。保管者在 CRA 下的义务较轻，主要侧重于建立网络安全政策，管理漏洞披露，并在其项目社区内推广安全最佳实践。
*   **非商业开发者**: 开发非商业用途开源软件的个人或团队。该群体在很大程度上免于直接的 CRA 要求，尽管贡献者之间对其适用性的混淆和不确定性仍然存在，这凸显了对更明确的指导和角色澄清的需求。

## CRA 实施时间表和指南

现在，CRA 已于 2024 年 12 月 10 日生效，但与任何此类法规一样，细节决定成败。因此，CRA 的主要义务将于 2027 年 12 月 11 日起强制执行。欧洲委员会正在制定授权法案，并与[CRA 专家组合作，以提供详细的实施和指导](https://www.sgs.com/en-gb/news/2025/09/safeguards-13125-update-on-developments-relating-to-the-eu-cyber-resilience-act)。Kroah-Hartman 作为该委员会的成员，对 CRA 了如指掌，以下是他所说的。

## CRA 对开源安全产生的积极影响

他首先向开发者保证，CRA “并非坏事”，事实上，它代表了对开源透明度和安全实践的迟来的改进。话虽如此，“欧盟的《网络韧性法案》将会[影响这里在座的每一个人](https://thenewstack.io/the-cyber-resilience-act-fear-confusion-and-reassurance/)，因为即使你不是欧盟成员……世界上的其他国家和地区也在采用相同的法规。”

此外，任何包含代码（如今几乎所有东西都包含代码）并在欧盟销售的产品，都将受到 CRA 的管辖。即使你从未离开过美国，如果你的代码在欧盟境内使用，你的程序也将受到 NDA（此处应为 CRA）的约束。

听起来很吓人，不是吗？不要惊慌。

## CRA 的目标：商业用途与非商业用途

Kroah-Hartman 强调，该法律无意针对业余爱好者、顾问或任何仅贡献于开源项目的人。“如果你在为开源项目做贡献，你无需担心，这不是问题……非商业的业余产品，不在范围内，完全不是问题。不用担心，直到你的软件被使用为止。”只有那些其工作被纳入欧盟商业产品的个人才需要特别关注合规性。

对于在 Linux 基金会、Mozilla 或 Apache 等组织 umbrella 下运作的项目维护者，Kroah-Hartmann 概述了最低限度但清晰的责任：“作为保管者，你只需要做这些：提供一个联系人，告知你关于他们发现的安全问题，然后当你修复了安全问题，向某人报告。

就是这样。你只需要做这些……如果你自己运行了一些基础设施，并且你的基础设施存在安全问题，你也必须报告。就是这样。一点也不麻烦，你只需要做这些。”

## 抵制制造商转嫁合规责任

Kroah-Harman 敦促开源项目抵制制造商试图将合规要求转嫁给维护者的企图。“如果制造商来找你，说，‘这里有一份我们希望你做的详细清单，’就顶回去。”

这是一个真正令人担忧的问题。Emerson Electric 已经试图让开源项目为他们承担法律工作。8 月份，他们要求[Debian Linux 项目](https://www.debian.org/)提供[关于 debianutils 的信息](https://lists.debian.org/debian-devel/2025/08/msg00110.html)。

## 不要害怕 CRA：提高软件安全标准

他警告说，“情况会变得更糟，因为 CRA 的截止日期很快就要到了。在开源领域，我们暂时不必担心任何事情。制造商将在明年九月开始真正关心起来。他们将在明年夏天开始恐慌，事情将开始变得棘手。”

对于这类要求，Kroah-Hartman 表示：“你没有责任去做。他们正试图让你为他们做工作。情况会变得更糟。公司正在找上门来。我会写一个简短的表格信，说：‘这是你需要做的。’”

Kroah-Hartman 解释说，[开源安全基金会（OpenSSF）](https://openssf.org/)正在努力[帮助开源社区应对和遵守 CRA](https://openssf.org/blog/2025/07/15/new-cyber-resilience-act-cra-brief-guide-for-oss-developers/)。OpenSSF 还在合作制定技术规范，开发指南和培训，并创建诸如 OSPS Baseline 之类的框架，以确保在保持开源协作本质的同时提高安全性。最终，OpenSSF 将会有一个表格信，可以用来回绝他们，并说：“不，你们自己去做。我们没有像他们那样的责任。”

Kroah-Hartman 继续说道：“我们开源保管者或贡献者在接下来的一整年里都不必做任何事。我们不承担任何责任；我们只需要在‘README 文件中提供联系方式，说明如何联系我们’。他还指出，然而，那些对 OpenSSF 感到恐慌的企业可能会为开源项目带来利润。例如，[cURL](https://curl.se/) 的维护者 [Daniel Stenberg](https://www.linkedin.com/in/danielstenberg/?originalSubdomain=se) 已经在提供[cURL CRA 支持的商业支持](https://curl.se/support.html)。

他故事的寓意是：“不要害怕。这项法律没问题。”CRA 将提高商业软件安全的标准，但拥有良好实践的开源贡献者和维护者已经在合规的道路上。