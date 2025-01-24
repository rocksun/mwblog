
<!--
title: 通过自动块大小推荐提升PostgreSQL性能
cover: ./cover.png
-->

我们的UI工具新增功能“Chunk Size 建议”可帮助您微调 hypertable 配置，从而提升 Postgres 性能。

> 译自 [Boost Your PostgreSQL Performance With Auto Chunk Size Recommendations](https://medium.com/timescale/boost-your-postgresql-performance-with-auto-chunk-size-recommendations-f407406174e0)，作者 Team Timescale。

作为开发者，我们相信拥有合适的工具能够更快地将应用程序推向市场，并达到用户应得的质量，这绝对至关重要。我们的使命是确保Timescale Cloud（[我们完全托管的PostgreSQL云](https://www.timescale.com/cloud)）成为您开发者工具带上的*那件*利器。因此，我们一直投入大量时间和精力进行多项改进，使您能够更快地交付产品，同时享受一流的开发体验。

这些改进包括最近推出的[数据迁移向导和Actions中心](https://www.timescale.com/blog/moving-faster-from-poc-to-prod/)以及我们的[SQL助手](https://www.timescale.com/blog/postgres-gui-sql-assistant/)，这是一个可靠的AI助手，它将帮助您编写更好的SQL代码，充满信心地进行调试等等。这些工具位于Timescale控制台中，旨在简化入门过程，让您能够快速上手并采用核心功能以获得最佳性能，轻松地从概念验证(PoC)过渡到生产环境。

今天，我们为您带来UI工具的最新补充——块大小建议，这是一项旨在消除配置超表时的猜测工作，并使您能够构建更快、更可扩展的系统的新功能。这是我们对用户提出的许多建议中的第一个，用户可以通过这些建议改进其现有的数据库配置，以从Timescale获得更好的性能。从入门到生产运行，Timescale都能为您提供最佳性能支持。

为了证明这一点，我们发布了[配套视频](https://www.timescale.com/blog/p/02a56e9e-0d38-4645-9182-8425a4dc9161/#video-how-chunk-size-recommendations-work)作为我们新的`EXPLAIN ANALYZE`系列的一部分。本系列专为开发人员设计，提供快速、可操作的技巧，以最大限度地提高Timescale应用程序的性能。敬请期待后续剧集。👀

但在分享第一集之前，让我们快速总结一下为什么块大小对PostgreSQL数据库性能至关重要。

✨ 要查看我们10月份的所有发布内容并随时了解即将发布的内容，请[访问我们的博客文章](https://timescale.ghost.io/blog/how-were-bringing-postgres-into-the-ai-era/)或查看[发布页面](https://www.timescale.com/launch/2024)。

## 为什么块大小对Postgres性能至关重要

在TimescaleDB（Timescale Cloud的核心）中，超表将数据划分为块。虽然这为时间序列数据提供了强大的功能，例如轻松的数据保留管理和快速的查询性能，但选择正确的块大小可以产生显著的影响。合适的尺寸可以优化写入和查询性能，减少元数据开销，并防止由于块太小而导致的查询规划速度变慢。

块太小意味着您的数据库必须管理更多元数据，这可能会减慢查询速度并增加规划时间，尤其是在数据量增长的情况下。相反，块过大可能会导致效率低下，在查询最新数据时可能会导致速度变慢。这就是为什么设置正确的块大小如此关键——以及为什么现在使用我们新的块大小建议工具比以往任何时候都更容易。

## 视频：块大小建议的工作原理

当您登录[Timescale控制台](https://console.cloud.timescale.com/login)时，Timescale会自动分析您的超表，并标记任何块大小不足以获得最佳性能的表。您将收到根据您的数据库使用情况量身定制的建议，这些建议以清晰、可操作的警报形式呈现。

在我们`EXPLAIN ANALYZE`系列的第一集中，[我们向您展示了此工具的工作原理](https://youtu.be/xrV6NAQnvnE)：

## 立即试用块大小建议

令人印象深刻，对吧？要立即试用块大小建议并开始使用Timescale Cloud和超表提升PostgreSQL性能，请[注册免费30天试用版](https://console.cloud.timescale.com/signup/?utm_source=blog&utm_medium=email&utm_campaign=november-abl&utm_content=timescale-cloud-signup)，无需信用卡。

此外，请关注我们`EXPLAIN ANALYZE`系列的更多视频，我们将继续分享实用建议和最佳实践，以充分利用您的Timescale数据库。与以往一样，我们欢迎您的反馈——[让我们知道](https://slack.timescale.com/)块大小建议和我们最近的其他功能如何帮助您构建更好、更快、更可扩展的应用程序。

*本文由 Grant Godeke、Ana Tavares 和 Melanie Savoia 撰写，最初于 2024 年 11 月 15 日在 Timescale 官方博客上**此处**发布，最后更新于 2024 年 11 月 28 日。*