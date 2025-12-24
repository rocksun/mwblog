<!--
title: Apache Wayang：数据处理的跨平台利器
cover: https://cdn.thenewstack.io/media/2025/12/6d975e13-carlos-martinez-lyhiscxvbtm-unsplash.jpg
summary: Apache Wayang统一多个数据处理框架，通过三层抽象和跨平台优化器，智能选择并协调执行任务，简化复杂数据分析，降低成本，支持SQL和Java，已成为顶级Apache项目。
-->

Apache Wayang统一多个数据处理框架，通过三层抽象和跨平台优化器，智能选择并协调执行任务，简化复杂数据分析，降低成本，支持SQL和Java，已成为顶级Apache项目。

> 译自：[Apache Wayang Makes Data Processing a Cross-Platform Job](https://thenewstack.io/apache-wayang-makes-data-processing-a-cross-platform-job/)
> 
> 作者：Joab Jackson

大多数数据处理框架都构建在单个执行引擎之上。Apache Wayang 则不然。

上周，Apache软件基金会[首次亮相](https://news.apache.org/foundation/entry/the-apache-software-foundation-announces-new-top-level-projects-3?ref=dailydev)了[Wayang数据处理框架](https://wayang.apache.org/)，使其成为一个顶级的Apache项目。

Wayang 以印度尼西亚皮影戏命名，是一个旨在统一数据集的数据处理框架，它能够协调多个数据处理框架。

对于拥有大量数据系统的组织来说，这款软件就像一把瑞士军刀，能够根据当前需求[执行不同类型的工作](https://wayang.apache.org/docs/introduction/benchmark)。它同时支持SQL和Java。

GitHub网站[解释道](https://github.com/apache/incubator-wayang)：“在Wayang中，用户可以使用Wayang的某个API指定任何数据处理应用程序，然后Wayang可以选择最适合该应用程序的数据处理平台，例如Postgres或Apache Spark。Wayang将协调执行，从而隐藏不同的平台特定API并协调平台间的通信。”

Wayang 可用于在不同关系数据库之间运行联合[SQL查询](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/)。或者，它也可以为给定任务选择最具成本效益的处理平台，然后运行该任务。为了获得最佳结果，它甚至可以将一个任务拆分，在多个平台上运行。

“用户面临着各种专业平台来执行数据分析。他们通常以比必要更高的成本运行数据分析，因为选择正确的平台是令人望而却步的，”该技术的一些创建者在[2023年的一篇论文](https://sigmodrecord.org/publications/sigmodRecord/2309/pdfs/05_Systems_Beedkar.pdf)中写道，解释了对这项技术的需求。“此外，现代应用程序通常需要执行超出单个平台限制的数据分析，这使得平台的选择变得更加困难。”

（Wayang 的创始人 Dr. Jorge-Arnulfo Quiané-Ruiz 于2023年意外去世。）

Apache Wayang PMC 主席 Zoi Kaoudi 在一份声明中说，新的项目状态“结合强大的社区动力，使我们能够增强项目并吸引更多开发者。”

## Wayang 的三层抽象

Wayang 的三层架构在应用程序和支持数据系统之间插入了一个抽象层，该层可以根据规则决定哪些系统应该执行给定任务，然后协调这些任务。

[![diagram](https://cdn.thenewstack.io/media/2025/12/a178a58d-wayang-stack-1024x457.png)](https://cdn.thenewstack.io/media/2025/12/a178a58d-wayang-stack-1024x457.png)

数据处理发生在平台层，但平台选择是通过Wayang完成的。

在此设置中，应用程序照常持有业务逻辑，但底层核心层充当中间件，将应用程序逻辑转换为称为“Wayang计划”的中间表示。

一个跨平台优化器自动化了数据系统选择。用户不必担心用于任务的具体平台。

这允许应用程序在一个管道中利用并混合多个处理引擎。例如，[Apache Flink](https://thenewstack.io/building-real-enterprise-ai-agents-with-apache-flink/)、[Apache Spark](https://thenewstack.io/the-good-bad-and-ugly-apache-spark-for-data-science-work/) 和 [Tensorflow](https://thenewstack.io/googles-new-tensorflow-tools-and-approach-to-fine-tuning-ml/) 都可以一起用于单个任务中。Wayang 随后协调工作。

## 一个工作流，多个引擎

数据存储在一个单一的存储库中，通过选择性地将数据卸载到更强大的引擎，可以提高性能。

以一个常见的[深度学习](https://thenewstack.io/demystifying-deep-learning-and-artificial-intelligence/)任务为例：执行[随机梯度下降](https://www.geeksforgeeks.org/machine-learning/ml-stochastic-gradient-descent-sgd/)算法。这个算法基本上是一组 Map/Reduce 函数，中间穿插了一些解析工作。

Wayang 查询优化器可以确定这些任务中哪些最适合在 Apache Spark 上执行，哪些可以通过单个 Java 进程更有效地完成。

它将 Wayang 计划转换为特定的工作流，权衡操作成本和数据移动成本等因素，目标是最小化总成本。

成本可以按能耗或运行时执行的计算成本来衡量。默认情况下，Wayang 使用线性成本公式，但用户可以插入自己的优化器，例如基于机器学习（ML）的优化器。

[![Workflow diagram](https://cdn.thenewstack.io/media/2025/12/48060cd2-wayang-optimizer-1024x225.png)](https://cdn.thenewstack.io/media/2025/12/48060cd2-wayang-optimizer-1024x225.png)

Wayang优化器 (Wayang)。

Wayang 目前支持的框架有：

*   Apache Flink
*   Apache Giraph
*   GraphChi
*   Java Streams
*   JDBC-Template
*   Postgres
*   Apache Spark
*   SQLite3

## Wayang 的商业化

该项目的主要提交者之一 Kaustubh Beedkar 帮助[创立了一家公司](https://www.youtube.com/watch?v=opZdul64pt4) Scalytics，围绕这项技术开展业务。Scalytics 将 Wayang [作为基础](https://www.scalytics.io/blog/apache-wayang-more-than-a-big-data-abstraction)，在其 [Scalytics Streaming Intelligence](https://www.scalytics.io/federatedintelligence) 平台中实现联合数据处理功能，旨在将 Databricks 平台扩展到边缘平台。

根据该公司介绍，Wayang 实际上可以用来创建“虚拟数据湖”。

该公司资料[指出](https://www.scalytics.io/blog/apache-wayang-more-than-a-big-data-abstraction)：“最终目标是复制[数据库系统]在跨平台应用中的成功：用户制定平台无关的数据分析任务，而一个中间系统决定在哪个平台上执行每个子任务，目标是最小化运行时或货币成本等成本。”