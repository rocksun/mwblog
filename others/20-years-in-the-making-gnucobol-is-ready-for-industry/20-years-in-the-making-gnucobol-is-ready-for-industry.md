<!--
title: 苦心20年制造的GnuCOBOL已经蓄势待发
cover: https://cdn.thenewstack.io/media/2024/03/1aba56e5-gnucobol-1024x683.png
-->

在FOSDEM的演讲中，GnuCOBOL贡献者Fabrice Le Fessant自豪地宣称，GnuCOBOL经过20年的发展，已经达到了工业级的成熟水平，可以在各种环境下与专有产品一较高下。

> 译自 [20 Years in the Making， GnuCOBOL Is Ready for Industry](https://thenewstack.io/20-years-in-the-making-gnucobol-is-ready-for-industry/)，作者 Joab Jackson 是 The New Stack 的资深编辑，报道云原生计算和系统运维。他已报道 IT 基础设施和开发领域超过 25 年，包括在 IDG 和政府计算机新闻工作。在此之前，他......阅读更多 Joab Jackson 的文章。

打孔卡片又可以使用了！

开源的 GnuCOBOL "经过 20 年的发展已经达到了工业成熟水平，可以在所有环境下与专有产品竞争"。[OCamlPro](https://ocamlpro.com/) 创始人兼 GnuCOBOL 贡献者 [Fabrice Le Fessant](https://fabrice.lefessant.net/) 在一次关于该技术的 [FOSDEM 演讲](https://ftp.heanet.ie/mirrors/fosdem-video/2024/h2215/fosdem-2024-3249-gnucobol-the-free-industrial-ready-alternative-for-cobol-.av1.webm)中这样说。

[GnuCOBOL](https://gnucobol.sourceforge.io/) 将 [COBOL 源代码](https://thenewstack.io/how-cobol-code-can-benefit-from-machine-learning-insight/)转换为可执行应用程序。它具有很强的跨平台能力，可运行在 Linux、BSD、许多专有 Unix 系统、macOS 和 Windows 系统上，甚至安卓系统。最新的 32 版已在许多商业环境中使用。

## 谁还在使用 COBOL?

COBOL (Common Business-Oriented Language) 问世于 1959 年，是一种[高级语言](https://www.techtarget.com/searchitoperations/definition/COBOL-Common-Business-Oriented-Language)，主要为大型组织的财务和人力资源部门服务。现在它是 ISO 标准，最新的 35.060 版于 [2023 年发布](https://standards.iteh.ai/catalog/standards/iso/31d28b41-4fef-4527-9083-0b65e495b32e/iso-iec-1989-2023)。

从一个关键方面来看，COBOL 是第一种现代语言:它被设计为跨平台的。资助 COBOL 开发的美国国防部希望摆脱为每个供应商的计算机品牌支持不同编程语言的做法，可移植性是 COBOL 早期成功的关键。

尽管常被视为遗留语言，但 COBOL 仍然[广受使用](https://thenewstack.io/cobol-everywhere-will-maintain/)，据估计，现有高达 800 亿行 COBOL 代码，最令人惊讶的是，它每年的[增长率为 15%](https://thenewstack.io/u-s-unemployment-surge-highlights-dire-need-for-cobol-skills/)。

GnuCOBOL 项目负责人 [Simon Sobisch](https://github.com/GitMensch) 在同一场 FOSDEM 演讲中说，当你使用 ATM 卡时，如果不是 [Java](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/)，后台发生的很多事情都可能是 COBOL。

许多组织都有庞大的 COBOL 代码库，迁移起来很困难。但是，为什么要迁移呢?COBOL 快速而可靠。

现在商业供应商主导着 COBOL 的部署。[IBM](https://www.ibm.com/?utm_content=inline-mention) 将 COBOL 捆绑在其大型机中。[Micro Focus](https://thenewstack.io/back-future-micro-focus-can-make-hpe-software-purchase/) 为 PC 提供 COBOL。[富士通的 NetCOBOL](https://www.fujitsu.com/global/products/software/developer-tool/netcobol/) 则可在 PC 和大型机上运行。

尽管如此，索比施指出，GnuCOBOL 正在获得大量商业部署，例如于银行后台应用程序，许多应用程序正从 Micro Focus 迁移过来，用户反映性能有所提高。法国联邦机构 [DGFIP](https://www.economie.gouv.fr/files/files/directions_services/dgfip/Rapport/Rapport_2011_version_anglaise.pdf) 在 Le Fessant 公司的帮助下，已从 GCOS 大型机迁移到 GnuCOBOL。

## COBOL 版的 "Hello World"

这个最初被称为 OpenCOBOL 的项目于 2002 年启动，并于 2013 年更名为 GnuCOBOL。在过去三年中，它吸引了 13 名贡献者，提交了 460 次代码。

大多数 Linux 软件包管理器都有 GnuCOBOL 程序的副本供下载。

下面是 COBOL 版的 "Hello World"。该程序分为三个部分:

```cobol
 1  IDENTIFICATION DIVISON
 2   
 3  PROGRAM-ID. prog
 4   
 5  DATA     DIVISION
 6   
 7  WORKING-STORAGE-SECTION
 8   
 9  01 var-string PIC X(20) VALUE "Hello World"
10   
11  PROCEDURE     DIVISION
12   
13  DISPLAY var-string
14   
15  END PROGRAM prog
```

标识部分确定程序的名称。数据部分存储数据("Hello World")，过程部分包含函数。  

## GnuCOBOL 为企业提供了什么

自然地，对于熟悉 [Unix 环境](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/)的人来说，GnuCOBOL 很直观。它可以编译为 C 代码(C89+)，从而使其非常可移植，从大型机到树莓派都可以运行，索比施说。

曾有实现了运行数千个处理器的 GnuCOBOL 代码，这给了项目开发人员在大型用例中调优性能和内存使用的机会。  

在合规性方面，它通过了 97% 的 COBOL 85 一致性测试，这一成功率还没有专有供应商取得，索比施自豪地说。它有 19 种方言，包括 IBM 和 Micro Focus 的扩展。

GnuCOBOL 目前还不支持对象和消息。"对象是来自 COBOL 22 的一个不常用的不错的功能，"索比施说。消息功能最近才重新实现，对于 COBOL 群体来说仍然是一个新功能需要应对，索比施说，所以 GnuCOBOL 目前还不支持。

另一个新特性是 [SuperBOL](https://get-superbol.com/)，一个由 Le Fessant 的 OCamlPro 开发的 GnuCOBOL [开发工具](https://github.com/OCamlPro/superbol-studio-oss)。它运行为 VSCode 扩展，并提供了完整的 COBOL 处理器(用 [OCaml](https://ocaml.org/) 编写)。但是，这个软件仍处于开发的早期阶段。  

最后，GnuCOBOL 将是[即将到来的 Google Summer of Code](https://gnucobol.sourceforge.io/gsoc.html) 中展示的语言之一，因此一整代新的码农将能说"这不仅仅是 COBOL，这是 GnuCOBOL。"
