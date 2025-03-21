
<!--
title: P99Conf：eBPF如何构建更快的数据库系统
cover: https://cdn.thenewstack.io/media/2024/10/0a44ad98-p99conf.png
-->

BPF-DB并非将数据复制到用户空间，而是直接在内核中执行许多常见的数据库操作。

> 译自 [P99Conf: How eBPF Could Make Faster Database Systems](https://thenewstack.io/p99conf-how-ebpf-could-make-faster-database-systems/)，作者 Joab Jackson。

未来某一天，数据库系统可能会因为新兴的 [eBPF 技术](https://thenewstack.io/ebpf/) 而获得速度提升。

虽然 [eBPF](https://ebpf.io/) 最初是为内核内数据包过滤而创建的，但研究人员正在发现该技术的其他潜在用途，它为直接在内核中运行的事件驱动程序提供了一个沙箱执行环境。

其中一个用途可能是绕过操作系统来重新路由数据库操作，而操作系统长期以来一直是数据库的瓶颈。

“在过去的 50 年里，操作系统让数据库工程师的生活非常痛苦，因为操作系统正在做出某些设计选择并将它的意志强加于任何用户空间应用程序，例如数据库系统，”卡内基梅隆大学副教授解释说，在本周早些时候 [ScyllaDB](https://www.scylladb.com/?utm_content=inline+mention) 举办的 [P99 CONF](https://www.p99conf.io/) 上发言。

在他的演讲中，介绍了 BPF-DB，这是一种内存中的键值数据存储，可以通过 eBPF 植入操作系统内核中，从而绕过操作系统的用户空间（程序通常在内存中运行的空间）的限制。

“因为我们不必将数据复制到用户空间，所以速度要快得多，”他说。

该项目背后的研究团队计划在新的一年将代码作为开源发布，并附带一篇正在发表的论文。

## 数据库与操作系统

操作系统在其管理计算机资源的角色中，必须决定如何跨多个竞争应用程序分配资源。并非每个应用程序都能始终获得其所需的内存和处理能力。

这始终是数据库设计人员的一个痛点，他们认为数据库是操作系统运行的最重要的应用程序（有时是正确的）。

> “操作系统只想打击数据库的士气，并将[其]铁腕强加于它们。”
>
> — Andy Pavlo

“底线是，许多现有系统中的操作系统服务要么太慢，要么不合适，”1991 年 [PostgreSQL](https://thenewstack.io/postgresql-17-gets-incremental-backup-sql-queries-for-json/) 创始人写道。

Pavlo 指出，操作系统人员也不太喜欢数据库人员，并提到首席 [Linux](https://thenewstack.io/Linux/page/2/) 内核维护者 [Linus Torvalds](https://thenewstack.io/linus-torvalds-on-security-ai-open-source-and-trust/) 曾经说过数据库人员“很少有品味”，抱怨他不得不做的 ASYNC I/O 内核 API 的工作，该 API 似乎只被数据库设计人员用于非阻塞数据写入。

数据库系统充斥着解决操作系统限制的变通方法，例如内存管理。

“选择你最喜欢的系统，里面可能就有类似的东西，”他说。

因此，自然而然地，构建更快数据库系统的研究方向是尽可能减少与内核的交互，尽可能减少系统调用的数量以及其他技术。

早期的一种方法是内核绕过技术，其中许多通常由内核处理的功能都在数据库系统本身中处理，通常由英特尔的 [DPDK](https://www.dpdk.org/) 和 [SPDK](https://spdk.io/) 等库处理。

然而，这种方法也有其局限性。这种方法需要大量重复的工作，并且调试可能很痛苦（[ScyllaDB](https://www.scylladb.com/) 提供 DPDK 作为选项）。

## 用户绕过

研究团队的 BPF-DB 采取了相反的方法，即将数据库系统置于操作系统本身中。

它不是将数据复制到用户空间以便由数据库系统逻辑处理，而是内核本身的数据库逻辑处理数据，从而消除了大量数据复制。

“与其将 DBMS 数据拉到用户空间，不如将 DBMS 逻辑推到内核空间，”他说。

![](https://cdn.thenewstack.io/media/2024/10/fe2f2fc2-pavlo-01.png)

eBPF 提供了实现这一目标的秘诀。

它允许用户使用 eBPF 库编写事件驱动的程序，这些程序在内核空间本身执行，并且可以通过跟踪点或中断从应用程序内部调用。

在这种方法中，最频繁的数据库操作可以由内核本身执行。

![](https://cdn.thenewstack.io/media/2024/10/086244f3-pavlo-07.png)

数据库用户无需单独连接数据库系统本身，而是可以路由到内核代理，该代理将数据库更改捆绑到数据库中。

“这减轻了数据库系统的很大一部分压力，”他说。“因为我们不必支付将数据提升到用户空间的成本，所以能够获得更好的性能。”

Pavlo说，某些操作仍然必须在用户空间中完成，例如密码身份验证。

Pavlo说，五年前还无法构建这种eBPF程序，但eBPF应用程序二进制接口（ABI）自那时以来已经变得更加丰富。


## BPF-DB简介

BPF-DB是一个完全事务性的数据存储，可以用作后端数据库（例如Redis）的前端（“可以把它想象成eBPF的[RocksDB](https://thenewstack.io/instagram-supercharges-cassandra-pluggable-rocksdb-storage-engine/)，”Pavlo说）。它带有一组数据库操作符（BEGIN、SET、GET、COMMIT），可以通过API访问，数据存储在内核驻留的哈希表中。然后将数据推送到用户空间，以便将其提交到长期存储。

![](https://cdn.thenewstack.io/media/2024/10/da1a2143-pavlo-02.png)

在早期测试中，研究团队发现BPF-DB使Redis的吞吐量（每秒操作数）翻倍，与高性能Redis克隆[Dragonfly](https://www.dragonflydb.io/)相当，同时还提供完全事务功能。延迟也低于Redis和Dragonfly。

![](https://cdn.thenewstack.io/media/2024/10/8521aa6a-pavlo-08.png)

“我们真的认为eBPF是我们摆脱操作系统问题设计选择束缚，并开始向内核注入更多复杂性以实现我们想要的功能的最终手段，”Pavlo说。
