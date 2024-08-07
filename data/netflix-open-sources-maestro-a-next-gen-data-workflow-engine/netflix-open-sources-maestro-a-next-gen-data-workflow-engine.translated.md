# Netflix 开源 Maestro，下一代数据工作流引擎

![Featued image for: Netflix Open Sources Maestro, a Next-Gen Data Workflow Engine](https://cdn.thenewstack.io/media/2023/10/0439525e-netflix-1024x601.png)

视频和游戏流媒体服务 Netflix 已将其实用的数据科学家和分析师每天使用的工作流编排器开源，用于了解用户行为和其他大规模数据驱动的趋势。

[Maestro 工作流编排器](https://github.com/Netflix/maestro) 在 [Apache 2.0 许可证](https://thenewstack.io/a-guide-to-leveraging-open-source-licensing/) 下发布，旨在支持数十万个工作流，并且每天为这家媒体公司完成多达 200 万个作业。

## Maestro 的工作原理

据公司工程师介绍，它具有高度可扩展性、可扩展性，并且能够满足严格的服务级别目标 ([SLO](https://thenewstack.io/usenix-the-3-measures-of-successful-site-reliability-engineering/))，即使在流量高峰期间也是如此。

它建立在一系列开源技术之上，即 [Git](https://thenewstack.io/git-for-managing-small-projects/)、[Java (21)](https://thenewstack.io/java-21-is-nigh-whither-javaone/)、[Gradle](https://thenewstack.io/ai-improves-developer-workflow-says-gradle-dev-evangelist/) 和 [Docker](https://www.docker.com/?utm_content=inline+mention)。

Maestro 可以从 [cURL 命令行](https://thenewstack.io/you-too-could-have-made-curl-daniel-stenberg-at-fosdem/) 调用，它提供了创建、运行和删除工作流以及相关数据批次的功能。工作流在 [JSON](https://thenewstack.io/an-introduction-to-json/) 中定义，用户的业务逻辑可以打包到 Docker 镜像、[Jupyter 笔记本](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/)、bash 脚本、[SQL](https://thenewstack.io/using-window-functions-in-sql/)、[Python](https://thenewstack.io/what-is-python/) 和其他格式中。

在幕后，Maestro 管理工作流的整个生命周期，处理重试、排队和任务分配到计算引擎。它不仅支持 [有向无环图](https://thenewstack.io/airflow-a-workflow-orchestrator-for-big-data/) (DAG)——2024 年人工智能驱动的世界中的基本要素——而且还支持循环工作流和多个可重用模式，通过 for 循环、子工作流和条件分支。

“它支持各种工作流用例，包括 ETL 管道、ML 工作流、AB 测试管道、在不同存储之间移动数据的管道，”Netflix 工程师团队在最近发布的博客文章中 [集体写道](https://netflixtechblog.com/orchestrating-data-ml-workflows-at-scale-with-netflix-maestro-aaa2b41b800c)。“Maestro 的水平可扩展性确保它可以管理大量工作流和单个工作流中的大量作业。”

## Maestro 的诞生

Netflix 对开源软件并不陌生，[发布了](https://netflix.github.io/)许多它在内部开发的工具作为开源软件。系统压力测试工具 [Chaos Monkey](https://github.com/Netflix/chaosmonkey) 于 2011 年发布，并激发了整整一代 [混沌测试工具](https://thenewstack.io/gremlin-applies-chaos-testing-to-serverless/)。Netflix 分拆的其他开源项目包括路由网关 [Zuul](https://github.com/Netflix/zuul) 和 [微服务](https://thenewstack.io/microservices/) 路由引擎 [Conductor](https://github.com/Netflix/conductor)，现已弃用。

Netflix 在 2022 年的一篇 [博客文章](https://netflixtechblog.com/orchestrating-data-ml-workflows-at-scale-with-netflix-maestro-aaa2b41b800c) 中首次向世界介绍了 Maestro，该文章解释了它的起源。当时使用的编排器名为 Meson，它在数千个日常作业的工作负载下不堪重负，尤其是在高峰使用时间。

“Meson 基于单一领导者架构，具有高可用性。随着使用量的增加，我们不得不垂直扩展系统以跟上，并且正在接近 AWS 实例类型的限制，”工程师在 2022 年的文章中写道。

更糟糕的是，预计工作负载每年至少增长 100%，并且工作流的大小也预计会增长。

从一开始，Maestro 就被设计为高度可扩展和可扩展的。它建立在 DAG 架构之上，其中每个工作流都包含一系列步骤。每个步骤都可以具有依赖项、触发器和其他条件。每个工作流的业务逻辑在隔离中运行，保证满足 SLO。所有服务都设计为无状态的，因此可以根据需要进行扩展。

在 [亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention) 的 2023 年 Re:Invent 大会上，Netflix 工程师团队进一步详细介绍了 Maestro：

[
YOUTUBE.COM/THENEWSTACK
科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看所有播客、访谈、演示等。

[https://youtube.com/thenewstack?sub_confirmation=1](https://youtube.com/thenewstack?sub_confirmation=1)