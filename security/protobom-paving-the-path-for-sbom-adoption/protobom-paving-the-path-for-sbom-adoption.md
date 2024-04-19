
<!--
title: Protobom为SBOM采用铺平道路
cover: https://cdn.thenewstack.io/media/2024/04/36d606ce-lili-popper-lu15z1m_kfm-unsplash-1.jpg
-->

CISA、DHS 和 OpenSSF 正在推出 Protobom，他们表示，这是一个开源工具，将使企业更容易保护其软件供应链。

> 译自 [Protobom: Paving the Path for SBOM Adoption](https://thenewstack.io/protobom-paving-the-path-for-sbom-adoption/)，作者 Jeffrey Burt。

联邦政府和[开放源代码安全基金会 (OpenSSF)](https://openssf.org/)正在推出一个开源工具，他们希望该工具能让私营部门和政府机构更轻松地采用和使用[软件物料清单](https://thenewstack.io/one-click-sbom-for-your-kubernetes-clusters-with-palette/) (SBOM)，这是抵御不断上升的软件供应链攻击浪潮的关键组成部分。

在 2020 年备受瞩目的 [SolarWinds 黑客攻击](https://thenewstack.io/lessons-learned-from-2021-software-supply-chain-attacks/)之后，拜登政府施加压力——包括通过其 2021 年网络安全行政命令——一年后 [Apache Log4j 日志记录工具](https://thenewstack.io/log4j-why-organizations-are-failing-to-remediate-this-risk/)中的危险漏洞，以及去年 [Progress Software 的 MOVEit](https://www.cybersecuritydive.com/news/progress-software-moveit-meltdown/703659/) 文件传输工具的大规模利用，帮助加速了企业对 SBOM 的采用，根据供应链优化软件供应商 [Sonatype](https://www.sonatype.com/resources/white-paper-2023-sbom-survey-report) 的一份报告，美国和英国四分之三的组织自实施以来一直在使用 SBOM。

此外，报告发现，92% 的大型企业已采用或计划采用 SBOM。

OpenSSF、美国网络安全和基础设施安全局 (CISA) 以及国土安全部 (DHS) 内的一个办公室表示，这也推动了 IT 供应商推出无数 SBOM 数据格式和识别方案，从而造成了一个分散的市场，让组织难以对所有选项进行分类。

## 介绍 Protobom

这三个组织——包括国土安全部的科学技术局 (S&T)——本周[推出了 Protobom](https://openssf.org/press-release/2024/04/16/cisa-dhs-st-and-openssf-announce-global-launch-of-software-supply-chain-open-source-project/)，这是一个开源产品，可以集成到商业和开源应用程序中，使用户能够更轻松、更便宜地生成、读取和翻译多种数据格式的 SBOM。

组织表示，Protobom 管理各种数据格式的能力有助于推动互操作性，而集成特性意味着应用程序可以将 SBOM 信息与来自多个公共来源的有关软件安全漏洞和严重性数据的外部信息相关联，使用户能够访问有关补丁和缓解策略的实时信息。

Protobom 将由 OpenSSF 托管。

“Protobom 不仅简化了 SBOM 的创建，还使组织能够主动管理其开源依赖项的风险，” OpenSSF 总经理 [Omkhar Arasaratnam](https://www.linkedin.com/in/omkhar/) 在一份声明中表示。“开源软件的安全性需要公共部门、私营部门和社区之间的合作。”

CISA 高级顾问兼战略家 [Allan Friedman](https://www.linkedin.com/in/allanafriedman/) 称软件漏洞是恶意行为者利用的一个关键风险。

“通过利用 SBOM 作为软件安全性的关键要素，我们可以降低软件供应链的风险，并更快、更有效地应对新风险，”Friedman 在一份声明中表示。“Protobom 通过翻译广泛使用的格式来提高效率和互操作性，以便工具和组织可以专注于重要的事情。”

联邦政府和 OpenSSF 都推动了 SBOM 的采用。两年前，OpenSSF 发布了其“ [开源软件动员计划](https://8112310.fs1.hubspotusercontent-na1.net/hubfs/8112310/OpenSSF/OSS%20Mobilization%20Plan.pdf?utm_referrer=https%3A%2F%2Fopenssf.org%2F)”，“SBOM 无处不在”是其 10 项行动项目之一。该计划的核心是让 OSS 项目在每次发布其软件时向用户提供准确的 SBOM。

Protobom 诞生于 CISA 和 DHS 去年资助了包括七家初创公司在内的项目，例如 [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention)、AppCensus、Manifest Cyber 和 Scribe Security。硅谷创新计划 (SVIP) 的 SVIP 管理总监 [ Melissa Oh](https://www.linkedin.com/in/melissa-oh/) 当时表示，“DHS 正在利用初创社区开发技术，以揭示供应链中的风险并增强组织的整体网络安全。”

## 不断变化的开发空间中的风险

软件开发领域的快速发展推动了对 SBOM 和其他用于保护供应链的工具的需求。开发人员越来越多地使用开源软件和可重复使用的软件组件，并使用来自多个来源的贡献。此外，代码的发布节奏正在加快，[持续集成和持续交付 (CI/CD)](https://thenewstack.io/ci-cd/) 管道增加了软件开发的复杂性。

这些因素也使软件供应链成为威胁团体的诱人目标。根据 Sonatype 的报告，此类攻击在 2019 年至 2023 年间平均每年增长 742%。

Bambenek Consulting 总裁 [John Bambenek](https://www.linkedin.com/in/johnbambenek/) 告诉 The New Stack，在保护软件供应链方面，SBOM 是“重要的一块拼图”。如果安全团队不知道自己存在漏洞，他们就无法抵御威胁。

他说：“让组织 [使用 SBOM] 的关键是为他们提供工具，以便轻松地以标准化格式创建 SBOM，以便漏洞管理工具可以摄取它，以便安全团队可以采取适当的措施。”

然而，美国政府是 Protobom 工作背后的主要推动力，这可能会让它更难在全球范围内得到采用。

Bambenek 说：“每当美国政府推动议程时，世界其他地区往往会持怀疑态度。”“这种怀疑也不是完全没有道理。例如，很难看到对美国持敌对态度的国家愿意采用这些工具和计划。”

尽管如此，Sonatype 研究人员在他们的报告中指出，诸如涉及 SolarWinds 和 Log4j 的事件——以及拜登政府的反应——可能促使其他友好国家做出反应，注意到欧盟在 2022 年宣布其拟议的网络弹性法案，而英国在一年后发布了其“关于企业和组织的软件弹性和安全性的意见征询”。

他们写道，这两项行动都强调了 SBOM 以及其他供应链安全实践。
