
<!--
title: Falco已经从CNCF毕业，接下来呢？
cover: https://cdn.thenewstack.io/media/2024/03/b0777c13-clay-banks-hf8n0ruk7g0-unsplash-1.jpg
-->

Falco 提供跨分布式架构的传感器，并且它特别适用于分布式架构，尤其是 Kubernetes、容器等。

> 译自 [Falco Is a CNCF Graduate. Now What?](https://thenewstack.io/falco-is-a-cncf-graduate-now-what/)，作者 B Cameron Gain。

[Falco](https://falco.org/) 已获得 [CNCF](https://cncf.io/?utm_content=inline-mention) 的毕业身份，这一事实表明，还有很多工作要做，才能为 [eBPF](https://ebpf.io/) 铺平道路，使其充分发挥潜力，不仅在安全和 [可观测性](https://thenewstack.io/observability/) 方面，而且在不久的将来和长期内也会发挥作用。

Falco 就像许多其他安全可观测性工具或开源 CNCF 项目，因为它提供多种方法来观察或监控并跨多个运行时和基础设施绘制可观测性数据，因为它从 Linux 内核扩展到整个运行时基础设施。

不过，这就引发了一个问题，即 Falco 实际上在底层做了什么，当然，要理解 Falco，你必须理解 [什么是 eBPF](https://thenewstack.io/what-is-ebpf/)。简而言之，eBPF 通过所谓的钩子提供跨运行时的可见性、可观测性和网络功能，这些钩子再次从 [Linux 内核](https://thenewstack.io/the-linux-kernel-as-a-case-study-on-rapid-development-for-complex-software/) 扩展而来。这些钩子用于监控整个基础设施，再次从 Linux 内核扩展而来。

在 Falco 的情况下，它提供了它所谓的跨分布式架构的传感器，并且它特别针对分布式架构，尤其是 [Kubernetes](https://thenewstack.io/kubernetes/)、[容器](https://thenewstack.io/containers/) 等。它提供了扩展到 API 或通过 API 设置其工作方式规则的几项内容，并且它通过系统调用从传感器中派生，这些信息收集在集中式收集器中，而这些信息再次来自 Linux 内核本身、Kubernetes 基础设施、AWS 云跟踪等。

Falco 的整体概念很简单。你可以将 Falco 视为基础设施的安全摄像头网络。你将传感器放置在关键位置，它们观察正在发生的事情，如果它们检测到有害行为，它们会向你发出信号。

正如 Falco 在 Sysdig 的 CTO 兼创始人 [Loris Degioanni](https://www.linkedin.com/in/degio/) 和 Sysdig 开源软件工程师 [Leonardo Grasso](https://www.linkedin.com/in/leonardograsso/?originalSubdomain=it) 在 [“使用 Falco 实现实用云原生安全”](https://learning.oreilly.com/library/view/practical-cloud-native/9781098118563/) 中所写：“在最高层面上，Falco 非常简单：你通过在分布式基础设施中安装多个 *传感器* 来部署它。每个传感器收集数据（来自本地计算机或通过与某些 API 通信），针对它运行一组规则，并在发生不良事件时通知你。”

## 毕业的内核根源

Falco 最初是一个路由器数据包检查工具，它随着 eBPF 的发展而发展。Degioanni 告诉 The New Stack，eBPF 在创建后一直备受关注，直到“比如说，从 2015 年和 2016 年开始”，Falco 的项目团队开始研究该模块。“因此，这很有趣，因为从本质上讲，有不同的方法可以为 Linux 做安全性。考虑使用 eBPF 有点疯狂。到那时，它被用于编写小脚本。这需要一些工作——我们必须向 Linux 内核部分提交一些补丁，以使 eBPF 实际上能够做到这一点，但随后我们想出了一个解决方案，让整个行业大开眼界。”

此后，从沙盒到孵化再到毕业，这个过程基本上已经完成。“Falco 毕业这一事实证明了 CNCF 正在成为一个重要的项目库，这些项目或多或少是社区同意它们的项目，作为默认步骤，”Degioanni 说。“我们是下一代云原生的步骤。”

满足 [合规性标准，例如 SOC](https://thenewstack.io/macrometa-on-what-soc-ii-compliance-means-for-developers/)，并解决错误并改进 Falco 以用于大规模生产，这也是 Falco 毕业的一个重要因素。“现在世界上一些最大的公司都在生产中使用 Falco。这有点困难，对吧？”Degioanni 说。“因此，创建者需要将项目提升到成熟的水平，这需要付出很多努力。”

Falco 与 Linux 内核很好地集成在一起。虽然 eBPF 是开源的，但它的修改发生在内核中，因此贡献者会对 Linux 进行更改并提供拉取请求。为 Falco 所做的许多工作涉及依赖系统仪表驱动程序，这些驱动程序需要针对每个受支持的 Linux 发行版和内核版本进行定制，
**托斯滕·沃尔克**（[LinkedIn](https://www.linkedin.com/in/torstenvolk)）是**企业管理协会 (EMA)**（[网站](https://www.enterprisemanagement.com/)）的分析师，他告诉 The New Stack。沃尔克表示，这迫使 Falco 支持大量旧版 Linux 内核。

沃尔克表示，对旧版系统提供支持需要包含旧版编译器，进而增加了安全风险。沃尔克表示，需要通过预构建驱动程序的组合来解决这些因素，这些驱动程序可以开箱即用，而不是让客户端必须对其进行编译，才能让 Falco 准备好毕业。沃尔克表示，Falco 开发团队随后为解决这一使用需求所做的工作是创建一个新的 driverkit 工具，该工具能够编译特定于内核的检测驱动程序，并包含与旧版和新版内核版本都更广泛兼容的较新编译器。

沃尔克表示，得益于 Sysdig 和开源社区对该项目的贡献，Falco 特别适合 Kubernetes。这项工作对于帮助其跟上 Kubernetes 可观测性的挑战性方面的速度非常重要，包括其无状态、分布式特性和其他属性。“毕业来得正是时候；Kubernetes 的采用正在快速增长，而安全性从未如此关键，”Sysdig 的开源生态系统副总裁**埃德·怀尔德-詹姆斯**（[LinkedIn](https://www.linkedin.com/in/wilder-james)）告诉 The New Stack。

怀尔德-詹姆斯表示，Falco 的主要优势之一是监控系统调用，“但愿景并不止步于内核”。“现代威胁在云中的许多表面上横向移动，”他说。“Falco 基于规则的检测流式传输方法适用于整个云。”

怀尔德-詹姆斯表示，通过其插件生态系统，Falco 可以监控 Kubernetes 和主要云提供商的日志，以及为 GitHub 和[Okta](https://developer.okta.com/?utm_content=inline-mention)等平台提供检测。“这是毕业后‘下一步’的重要组成部分，”怀尔德-詹姆斯说。

与此同时，Falco 一直处于安全性和可观测性的交叉点，CNCF 首席技术官**克里斯·阿尼兹奇克**（[LinkedIn](https://www.linkedin.com/in/caniszczyk/)）告诉 The New Stack。“他们也是最早采用利用 Linux 内核中的 eBPF 来进一步改进的早期采用者，”阿尼兹奇克说。“此外，该项目不仅对云原生生态系统有益，而且对任何可能与 eBPF 兼容的系统都有益。”

然而，阿尼兹奇克表示，并没有特定的催化剂让 Falco 成为一个毕业的 CNCF 项目。阿尼兹奇克表示，Falco 的毕业“只是时间问题，该项目满足了 CNCF 毕业要求和尽职调查流程”。

阿尼兹奇克表示，“eBPF 的使用增长迅速，我们已经到了不再新奇的地步。在任何技术的生命周期中，你都会开始考虑第 1 天或第 2 天的操作。”“Falco 完全符合这些类型的需求，其采用巩固了它在毕业项目中的地位。”
