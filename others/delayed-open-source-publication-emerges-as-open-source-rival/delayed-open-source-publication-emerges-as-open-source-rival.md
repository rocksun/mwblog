<!--
title: 延迟开源或成开源新对手
cover: https://cdn.thenewstack.io/media/2024/01/b5f6645f-open-source-license-2-1024x576.jpg
-->

延迟开源发布（DOSP）的做法，是首先以私有许可证发布软件，然后按计划过渡到开源许可证。

> 译自 [Delayed Open Source Publication Emerges as Open Source Rival](https://thenewstack.io/delayed-open-source-publication-emerges-as-open-source-rival/)，作者 Steven J. Vaughan-Nichols。

一种混合专有和[开源](https://thenewstack.io/open-source/)许可的方式正在变得越来越受欢迎，并且对开源软件构成了威胁。

在软件行业显著的转变中，[延迟开源发布(Delayed Open Source Publication，DOSP)](https://opensource.org/delayed-open-source-publication/)作为专有许可和开源许可的灵活组合策略出现了。这种方法首先在专有许可下发布软件，然后按计划过渡到开源许可。

这些程序通常首先作为开源软件发布，然后承诺最终重新出现为开源程序而重新发布。[开源倡议组织(OSI)](https://opensource.org/)发布了一项研究，[深入探讨了 DOSP 的历史、模式和不断发展的趋势](https://blog.opensource.org/a-historic-view-of-the-practice-to-delay-releasing-open-source-software-osis-report/)。

开源专家[塞思·肖恩(Seth Schoen)](https://sethschoen.com/)、[詹姆斯·瓦西莱(James Vasile)](https://www.linkedin.com/in/jamesvasile/)和[卡尔·福格尔(Karl Fogel)](https://github.com/kfogel)的研究发现，尽管大家都知道商业源代码许可证(BSL)是 DOSP 许可证，但 DOSP 并非新事物。

最早的 DOSP 实例之一是 1998 年左右的 [Aladdin GhostScript](https://web.mit.edu/ghostscript/www/index.html)，它在“[Aladdin 免费公共许可证](https://spdx.org/licenses/Aladdin.html)”下发布，后来过渡到同时采用专有许可和 GPL 的发布模型。

另一个例子是 [KDE 的 Qt 库](https://www.qt.io/faq/tag/qt-open-source-licensing)，它将 DOSP 作为防止潜在开发中止的一种保障措施。Qt 的许可历史非常复杂，简而言之，它现在可在商业和开源 GPL 2.0、GPL 3.0 和 LGPL 3.0 许可下获得。

## 如何使用延迟开源发布

研究人员发现延迟开源发布有三种类型。

- **无条件的预定重新许可**。这种直接的方法涉及在过渡到开源许可之前预定一个时间延迟。
- **事件驱动的重新许可**。在这里，开源发布与特定事件相关联，比如发布新的专有版本，促使其前身开源。尽管这曾经很常见，但现在很少使用。
- **有条件的重新许可**。这种类型取决于某些条件，比如获得资金或找到合适的非营利组织家园，然后才过渡到开源。不用说，这个承诺可能会也可能不会实现。

延迟开源发布的一个相关变种是“可见源”或“源码可用”。在这些模式中，源代码通常是可用的，但没有[开源定义(OSD)](https://opensource.org/osd/)所保证的自由。最近一个众所周知的例子是 Meta 的大型语言模型 [Llama 2 社区许可证](https://ai.meta.com/llama/license/)，代码是可用的，但其商业使用受到限制。

在延迟开源发布的早期，OSI 的研究人员发现延迟开源发布“通常是关于垄断直接商业收入: 许可证会授予开源所需的大多数权限，但关键是不允许商业使用该软件。” 这种限制将适用于所有下游被许可方，包括用户，不仅仅是开发者。

“然而，近期，”研究人员写道，“一些延迟开源发布许可证是关于防止任何被许可方在与许可方战略上非常重要的某些特定类型软件竞争的产品或服务中使用该软件，独立于直接收入。”

例如，为[MariaDB](https://mariadb.org/)编写的[商业源代码许可证1.1](https://mariadb.com/bsl11/)不允许在生产中使用许可代码，除非许可方使用附加使用授权(AUG)机制。AUG本身没有在许可证中说明。

AUG因公司而异。例如，MariaDB将“商业使用”定义为如果您的应用程序在超过3个服务器实例上使用许可作品。换句话说，如果您打算将MariaDB用作软件即服务(SaaS)或生产的基础，则不能在没有商业许可的情况下使用它。[HashiCorp](https://www.hashicorp.com/?utm_content=inline-mention)的商业源代码许可证实施AUG确实允许生产使用...除了在与Hashicorp程序和服务竞争的产品中。

这在实践中意味着不是所有的商业源代码许可证都是相同的。由于AUG，每个商业源代码许可证实例实际上是一个实质性不同的许可证。

## 开源旧代码: 一个混乱的过程

无论如何，在商业源代码许可证下，代码的旧版本最终将在开源许可下发布。关键词是“最终”。

商业源代码许可证要求许可方指定“变更日期”和“变更许可证”。在未来的变更日期，所涵盖工件的许可证将更改为变更许可证，这是一个开源许可证。

MariaDB的变更日期是特定版本发布后的四年，其变更许可证是 GPLv2。但是，正如开源倡议组织研究人员指出的，“商业源代码许可证在概念上旨在应用于特定软件版本，以便变更日期适用于代码库的特定版本。这意味着，对于具有正在进行的延迟开源发布实践的项目，商业源代码许可证的意图是定期重新应用带有更新详细信息。

“我们看到的大多数项目尚未演示如何持续地处理此过程。然而，大多数没有明确可见和系统化的方式来应用商业源代码许可证更新到正在进行的开发。...... 对于某些项目，乍一看并不明确商业源代码许可证授权意图适用于哪个版本或哪些版本的代码库。事实上，并非所有当代软件项目都有可靠的离散“发布”事件时间表，这可能会使变更日期概念复杂化。”

很混乱，不是吗？

## 商业源代码许可证的兴起

[HashiCorp将Terraform的许可从Mozilla公共许可证2.0更改为商业源代码许可证1.1（BSL 1.1）](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/)是一个两个趋势的例子。第一个是商业源代码许可证的兴起。如今，有十多个项目使用商业源代码许可证，包括[CouchBase](https://www.couchbase.com/products/capella?utm_content=inline-mention)、DragonflyDB和ArangoDB。

此外，最近的延迟开源发布许可证及其用户越来越关注防止竞争，而不是垄断商业收入。特别是商业源代码许可证用户越来越关注防止与许可方的战略利益直接竞争。这种转变体现在这些许可证中新增的附加使用授权和具体条款中。

除延迟开源发布许可证外，几个面向云的软件项目，如[MongoDB](https://www.mongodb.com/)和[Redis](https://redis.com/?utm_content=inline-mention)，也在过去几年中抛弃了开源许可证，采用了具有非竞争条款的许可证。这些许可证，如[服务器端公共许可证(SSPL)](https://www.mongodb.com/licensing/server-side-public-license)，通常允许您查看代码，但云服务提供商不能在软件即服务中使用它。这些不是延迟开源发布兼容的许可证。

在报告发布时，开源倡议组织执行董事斯[蒂法诺·马弗利(Stefano Maffuli)](https://www.linkedin.com/in/maffulli/)赞扬了其重要发现，其中最重要的是“自开源运动初期以来的复杂性和妥协”，并提出了需要更多专门研究的新问题"。

就我个人而言，我认为延迟开源发布是开源许可和专有许可之间令人讨厌的妥协。在我看来，太多时候，它被用来利用开源程序员的工作，然后在一个项目获得足够动力为其所有者盈利后，关闭他们代码后的大门。
