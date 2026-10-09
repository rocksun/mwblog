<!--
title: 无需抛弃Postgres也能超越原生Postgres的限制
cover: https://cdn.thenewstack.io/media/2026/07/78b12e3d-aakash-dhage-q_d2ilpbmjg-unsplash.jpg
summary: 本文探讨了原生Postgres在处理海量实时数据和AI智能体工作负载时面临的性能瓶颈，分析了盲目迁移到专用数据库的高昂成本，并介绍了如何在不放弃Postgres的前提下，通过架构升级或使用TimescaleDB等扩展来突破规模限制。
-->

本文探讨了原生Postgres在处理海量实时数据和AI智能体工作负载时面临的性能瓶颈，分析了盲目迁移到专用数据库的高昂成本，并介绍了如何在不放弃Postgres的前提下，通过架构升级或使用TimescaleDB等扩展来突破规模限制。

> 译自：[You can outgrow vanilla Postgres without abandoning Postgres](https://thenewstack.io/postgres-at-scale-why-it-struggles/)
> 
> 作者：Kimberly Fessel

**对于许多数据爱好者来说，**Postgres是存储和管理关系型数据的*首选方式*。它高效、直接，并且能与其他工具很好地配合。但即使是Postgres也有其局限性。

当你在处理源源不断的实时数据流时，你可能会发现Postgres开始吃力：查询变慢、维护需求增加，以及大量的数据库 upkeep（维护），足以让你的自动清理（autovacuum）机制请求暂停休息。

得益于其灵活性和庞大的生态系统，开发者们[越来越倾向于将Postgres](https://thenewstack.io/why-ai-workloads-are-fueling-a-move-back-to-postgres/)作为AI应用程序的基础。但随着你在管道中加入AI智能体，你可能会更快地触及其极限。智能体工作流通常会增加数据库活动。你可能会看到更频繁的数据库请求，以及随时间推移保留更多数据的需求。

随着你的表和索引不断增长，要保持查询速度可能需要更多幕后的关注。原生 Postgres 最初可能处理你的时间序列数据得心应手；直到让 Postgres 持续运行变成了一项专门的工作。

参与对话：10月21日，我们将与 [**Tiger Data**](https://www.tigerdata.com/) 的开发者倡导与文档负责人 [**Matty Stratton**](https://www.linkedin.com/in/mattstratton/) 坐在一起，探讨规模如何将原生 Postgres 压榨到极限，以及你如何使用 TimescaleDB 来扩展它。他将通过 TimescaleDB 的现场演示，指出随着数据量和速度的增长会出现哪些 Postgres 的痛点。

立即注册本次网络研讨会

你已成功注册网络研讨会。

起初，你可能会为你的 Postgres 系统投入更多资源。你可以优化查询，或者将数据分区到更小的表中。或者你可以调整自动清理并定期重建膨胀的索引。你甚至可以为系统购买更昂贵的硬件。然而，在某个时刻，你将不得不问自己：“我到底想在当前的设置上投入多少工程精力？”

接下来，你可能会忍不住完全放弃 Postgres 以避免这么多的工程挣扎。转向专门的系统一开始可能会让人觉得不可避免，甚至很满意，但它可能会导致潜在的昂贵迁移工作。

你将有一个新的数据库要学习，这意味着你和你的团队可能需要学习一种新的查询语言或 API。在验证事情的过程中，你可能需要在 Postgres 和新设置中维护一段时间的重复数据。尽管这让人感到令人生畏，但保留 Postgres 开始看起来更具吸引力。

与其把所有东西都拆掉，不如改变 Postgres 处理数据的方式。而且重新思考 Postgres 架构的方法不止一种。例如，诸如 [Databricks Lakebase 将计算与存储分离](https://thenewstack.io/new-oltp-postgres-with-separate-compute-and-storage/)等较新方法。

这使得每个部分都可以独立扩展，同时将 Postgres 保持在核心地位。或者，如果你正感受到大规模时间序列工作负载的压力，你可以使用 Tiger Data 的 TimescaleDB 来扩展 Postgres 本身。它利用超表（hypertables）、列式压缩和连续聚合来改变 Postgres 存储、查询和总结要求苛刻的时间序列数据量的方式。

在 10 月 21 日的网络研讨会上，你将了解原生 Postgres 如何处理高摄入率，以及 TimescaleDB 如何为昂贵的数据库迁移提供替代方案。

[Tiger Data](https://www.tigerdata.com) 的 [Matty Stratton](https://www.linkedin.com/in/mattstratton/) 加入我们的直播“[Postgres 规模化：实时数据增长时什么会损坏（什么不会）](https://thenewstack.io/webinar/postgres-at-scale-when-breaks-and-what-doesnt-when-live-data-grows/)”。他将演示 TimescaleDB 并探讨如何识别你的 Postgres 系统开始出现应变的地方、哪些调整仍然可以解决问题，以及什么时候可能是考虑采用不同方法的时候。

担心你的 Postgres 系统出现磨损迹象？[**立即注册**](https://thenewstack.io/webinar/postgres-at-scale-when-breaks-and-what-doesnt-when-live-data-grows/)以了解当 Postgres 开始挣扎时要注意什么以及该做什么。