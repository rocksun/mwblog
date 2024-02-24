<!--
title: 介绍开源Compliance Framework
cover: ./cover.png
-->

Container Solutions 很高兴地宣布我们已经开源了一个我们研发已久的项目。

> 译自 [Introducing the Open Source Compliance Framework](https://blog.container-solutions.com/introducing-the-open-source-compliance-framework)，作者 Ian Miell。


Compliance Framework是一个开源的软件套件，旨在自动化和管理您企业的合规性任务。**您可以把它看作用于软件审计和合规的Terraform和CI。**它允许您安排、报告和定义审计评估，并为您提供了一个框架来编写自己的合规性检查“提供程序”，如果这些提供程序还不存在的话。

简而言之，它允许您实现资产的持续合规性。一旦您的安全策略被定义好了，您就可以跟踪您的应用程序是否符合规定，而不必每六个月就派人拿着夹板查看控制措施是否仍然有效。

![](https://blog.container-solutions.com/hs-fs/hubfs/image-Feb-20-2024-08-44-41-7811-AM.png?width=1839&height=919&name=image-Feb-20-2024-08-44-41-7811-AM.png)

## 为什么要开发这个工具?


平时的读者会知道，我们之前已经写过关于[合规自动化兴起](https://blog.container-solutions.com/under-control-why-governance-engineering-is-coming-to-cloud-native)的文章。自动化是驱动和统一 Container Solutions 的核心部分，而审计和合规性在历史上(相对而言)被开源世界所忽略。虽然我们通常会“自动化所有的事情”，涉及到软件交付生命周期，但我们观察到治理、风险和合规(GRC)工作中存在大量手工劳动的模式，这似乎难以实现自动化。

我们开发这个项目的直接导火索是一次云转换项目中的一个事件。一家大型金融机构的 CISO 在一次会议上举起手说:"一定有比手工检查 Confluence 表格更好的管理所有这些的方法!"，这在公司里引发了一系列的灵感。

我们觉得需要一个开源框架，让企业可以管理他们自己的合规需求，这将为他们企业 GRC 部分带来成本节省，并改善整个企业合规状态的可见性(通过实时报告)。

前端的一个截图可以看出部分想法。我们本质上不是前端工程师，所以在这方面需要帮助。

![](https://blog.container-solutions.com/hs-fs/hubfs/Screenshot%202024-02-20%20at%2008.46.40.png?width=1400&height=447&name=Screenshot%202024-02-20%20at%2008.46.40.png)

## 它是什么?

Compliance Framework由几个独立的组件组成，允许您自动检查控制措施是否在您的 IT 资产中到位和有效。

架构在[这里](https://compliance-framework.github.io/docs/architecture)有文档，简而言之，有一个“核心”和一个“评估运行时”。

![](https://blog.container-solutions.com/hs-fs/hubfs/Screenshot%202024-02-20%20at%2008.47.56.png?width=2340&height=1552&name=Screenshot%202024-02-20%20at%2008.47.56.png)

### Compliance Framework核心

核心中有一个数据库，用于跟踪“评估”、“控制”、“组件”和“证明”。这些都是 [OSCAL](https://pages.nist.gov/OSCAL/) 的概念，数据库是一个基于 JSON 文档的数据库，因为这与 OSCAL 标准的耦合度最低。

配置服务和运行时编排器管理这个数据库。前者提供了保持数据库更新的接口，后者通过事件总线与评估运行时通信，确保检查得以执行并将结果返回系统。

### 评估运行时

此组件运行框架上计划运行的“提供程序”或“插件”。例如，您可能想定期检查 AWS 中的所有磁盘是否已加密。在这种情况下，您将使用相关的提供程序，运行时将安排和执行运行，并将结果发送回核心。

进行这种分离是为了允许运行时组件在更受限的环境中运行，在那里它仍然可以仅需要与核心组件建立一个通信信道的情况下执行检查(无需从受限环境打开 ssh 以执行 VM 检查)。

综上，这些组件允许您以编程的方式对系统中您关心的任何事物运行周期性检查。然后记录结果，并可以根据这些结果进行回顾性或实时报告。这些检查可以来自通用标准“提供程序”，或者您可以为自己的定制用例构建自己的检查。

## 关键功能

Compliance Framework基于对开放标准的承诺而构建。Container Solutions 是金融行业开源基金会 [FINOS](https://www.finos.org/) 的成员，一直在帮助开发[通用的云控制](https://www.finos.org/common-cloud-controls-project)，并参与关于 O[SCAL](https://pages.nist.gov/OSCAL/)(“开放安全控制评估语言”)的开发讨论，后者是另一项新兴的行业标准。

![](https://blog.container-solutions.com/hs-fs/hubfs/Screenshot%202024-02-20%20at%2008.49.36.png?width=1126&height=1328&name=Screenshot%202024-02-20%20at%2008.49.36.png)

Compliance Framework的构建旨在支持这两项举措。它帮助将这些重要的抽象标准转化为实现的现实，从而使合规管理的效率与其他云原生软件领域一样高，使用与任何其他运营活动相同的云原生标准来提供可观察性概念(服务级指标、服务级目标、警报)。此外，它与合规生态系统中的其他 OSCAL 兼容工具间可互操作。

## 想了解更多?

如果您想了解更多信息，请通过社交媒体或本页面联系我们，或者直接联系 GitHub 项目:

https://github.com/compliance-framework/

## 想参与进来?

虽然这个项目已经花费了许多工程师的时间，但我们肯定可以从其他人那里获得帮助，以让这个项目获得更多关注。我们正在与各种金融行业公司讨论以“正确的方式”扩展和实施这个项目，并渴望获得更多反馈。

虽然从 MVP 的角度来看，后端功能已经完成，但我们当然仍然可以获得帮助来开发 API 和改进功能集。最需要帮助的领域是前端，我们坦然地说我们在这方面不是专家，这可能会对项目产生很大影响。
