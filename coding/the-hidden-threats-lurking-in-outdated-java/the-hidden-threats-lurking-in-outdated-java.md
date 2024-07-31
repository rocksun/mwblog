
<!--
title: 隐藏在过时Java中的威胁
cover: https://cdn.thenewstack.io/media/2024/07/2606d764-java.jpg
-->

为什么即时安全更新对于您的关键企业 Java 应用程序至关重要。

> 译自 [The Hidden Threats Lurking in Outdated Java](https://thenewstack.io/the-hidden-threats-lurking-in-outdated-java/)，作者 Simon Ritter。

保持企业系统尽可能安全应该是显而易见的，不是吗？不幸的是，由于需要考虑如此多的安全方面，这在一些最重要的领域经常被忽视。

例如，[Java](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/) 运行时。

直到 2019 年，保持 JDK 更新到最新的安全补丁都是直截了当的，并且没有直接成本。当 Sun Microsystems 发布 Java 时，您可以免费下载 Java 开发工具包，除非您将其用于某种嵌入式或[单用途应用程序](https://www.oracle.com/java/technologies/javase-embedded/embedded-faq.html)（例如使用嵌入式 PC 的售票亭）。即使发布了新版本的 Java——这每两、三甚至四年才发生一次——与持续的免费更新仍然有相当大的重叠，以确保平稳过渡。

Oracle 在 2010 年收购 Sun 后，继续以相同的方式交付其 JDK，直到 2019 年。它的第一个变化是转向基于时间的发布计划，而不是基于功能的发布计划。现在，就像时钟一样，我们每年都有两个新版本的 Java：一个在 3 月，一个在 9 月。

这种更快的发布节奏导致了 Oracle JDK 长期支持 (LTS) 版本的引入，因为为所有版本提供扩展维护和支持是不切实际的。最初，每三年发布一个新的 LTS 版本，但现在已经缩短到两年。

当前的 LTS 版本是 JDK 8、11、17 和 21。Oracle 不再支持（即使是商业上）旧的开源版本的 Java，JDK 6 和 7。

[安全更新](https://thenewstack.io/the-great-security-debate-is-patching-useless/) 有多重要？毕竟，Java 现在已经近 30 年了；我们现在难道还没有消除所有漏洞吗？可悲的是，没有，现实地说，这永远不会发生。OpenJDK 包含 750 万行代码，并依赖于许多外部库，所有这些都可能存在未发现的漏洞。

让我们用一些硬数据来解释这一点。

假设您在 JDK 6 上运行您的应用程序，并且自 Oracle 免费公开更新结束（2013 年 4 月）以来一直没有更新它。在这种情况下，您的应用程序会暴露于总共 425 个漏洞，其中 89 个是严重的。

[及时更新您的系统](https://thenewstack.io/security-of-software-update-systems-in-2023/) 的能力至关重要。

Oracle 为每个更新提供两个版本，分别称为关键补丁更新 (CPU) 和补丁集更新 (PSU)。CPU 仅包含与安全相关的更改；PSU 包含与安全相关的更改、错误修复、性能改进以及任何其他代码更改。大小差异很大。一个大型 CPU 可能包含 15 个更改，但通常少于 10 个。另一方面，PSU 可以包含 200 到 400 个更改。

更新中包含的更改越多，其中一个更改可能影响应用程序功能的可能性就越大。由于更新之间只有三个月的时间，因此只能对应用程序进行如此多的测试。这会导致 PSU 产生重大影响的情况。例如，2022 年 7 月的 PSU 包含一个修复程序，该修复程序阻止了基于 Hadoop Cluster、Solr 和 Lucene 的应用程序正常工作。

自从 Oracle 更改其分发和许可以来，已经发布了 22 个更新。其中，6 个 PSU 需要修改和新版本来解决引入的回归。创建新更新的时间从不到两周到超过五周不等。CPU 从未受到过这种影响。访问 CPU 对于维护应用程序的最高安全级别至关重要。

由于所有免费的 OpenJDK 二进制分发版仅提供 PSU 版本，因此一些用户可能认为在能够部署之前等待几周是可以接受的风险。

这非常危险。

当发布 JDK 更新时，所有已解决的漏洞都会在发行说明中披露。恶意行为者现在拥有信息，使他们能够尝试找到利用未修补应用程序的方法。

让我们以常用的 Java 库 Apache Struts 为例，来说明这有多危险。

2023 年 12 月 7 日，发布了有关 Struts 中漏洞的详细信息。该漏洞的通用漏洞评分系统 (CVSS) 为 9.8，使其成为严重漏洞。此外，它有可能允许[远程代码执行](https://thenewstack.io/github-actions-design-flaw-leaves-security-hole-for-remote-code-execution/) (RCE)，这是一种比可用于拒绝服务 (DOS) 的漏洞更糟糕的漏洞。
仅仅四天后，概念验证代码就被发布，展示了如何利用此漏洞。在代码发布后的 24 小时内，就观察到对未修补系统的攻击。在可用的 Java 更新发布之前等待两周或更长时间，将使您的应用程序暴露在风险之中。您是否愿意承担这种风险？

Azul 的 Platform Core 提供了经过 TCK（技术兼容性工具包）测试的 Zulu 版本的 OpenJDK，每个季度都包含 CPU 和 PSU。它还支持 JDK 6 和 7。这为您的关键任务企业 Java 应用程序提供了最大的安全性和稳定性，而无需您将旧版应用程序升级到更新的版本。

[了解更多关于 Java 和 OpenJDK 的信息](https://www.azul.com/products/core/)。
