
<!--
title: MongoDB与Couchbase：移动数据库功能对比
cover: https://cdn.thenewstack.io/media/2024/11/1d98f281-mongodb-vs-couchbase-features.jpg
-->

MongoDB 即将弃用其 Atlas 设备同步和 Atlas 设备 SDK。如果您正在考虑迁移到 Couchbase Mobile，请了解以下信息。

> 译自 [MongoDB vs. Couchbase: Comparing Mobile Database Features](https://thenewstack.io/mongodb-vs-couchbase-comparing-mobile-database-features/)，作者 Mark Gamble。

如今的[移动应用用户](https://thenewstack.io/unlock-hyper-personalization-with-ai-driven-adaptive-apps)期望始终快速、始终在线、个性化且引人入胜的体验。这对应用的采用和增长至关重要，任何未能满足这些期望的行为都几乎会导致应用被放弃。

但是，如果为应用提供支持的数据库仅在云端运行，则保证快速且始终可用的体验就会成为一项挑战。因为移动用户不断进出网络覆盖范围，如果他们失去连接，移动应用就会变慢或完全失败。

为了确保在网络连接不稳定的情况下持续快速的 用户体验，移动开发人员经常利用[移动数据库](https://thenewstack.io/why-you-need-a-mobile-database/)平台。这些平台将[云数据库](https://thenewstack.io/how-cloud-databases-have-evolved-for-the-ai-era)与在应用程序内设备上运行的嵌入式数据库相结合。嵌入式数据处理通过消除对与远程云数据库的互联网连接的需求，从而使应用程序更快、更可靠；它改为使用本地数据来为应用程序提供支持。

但是，云数据库仍然作为移动应用程序的中央数据聚合点至关重要。因此，数据同步是移动数据库平台的另一个关键组成部分，因为几乎每个应用程序都需要在用户之间和/或与云共享数据以保持一致性。

由于这些功能，移动数据库平台在移动应用程序开发人员中很受欢迎，他们希望确保他们的应用程序快速且可用，而无需依赖互联网。

## 竞争领域缩小

移动开发人员的[移动数据库平台选项](https://www.couchbase.com/content/c/how-to-choose-a-mobi?x=9xr1sL)刚刚减少了。2024年9月，[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)宣布[弃用其移动数据库平台](https://thenewstack.io/mongodb-8-goes-hard-on-time-series-data-horizontal-scaling/)Atlas Device Sync和Atlas Device SDK（以前称为Realm），这令许多移动开发人员[失望](https://www.mongodb.com/community/forums/t/device-sync-and-edge-server-are-deprecated/296035/6)。开发人员必须在2025年9月正式停止支持之前找到替代方案。

现在开发人员必须迁移到一个新的平台，让我们检查一下MongoDB的移动支持与替代移动数据库平台[Couchbase Mobile](https://www.couchbase.com/products/mobile/)相比如何。

## Couchbase Mobile 与 MongoDB Atlas 的比较

两种解决方案都提供云 NoSQL 数据库后端、移动应用程序的嵌入式数据持久性和数据同步，但相似之处也仅此而已。虽然这两个平台在细节层面存在许多差异，但以下是一些主要的差异：

### 数据库模式灵活性

- Atlas Device SDK（Realm）是面向对象的，这有一些优点，但也需要一个模式来建模关系。这会造成僵化，从而增加应用程序的复杂性。
- Couchbase Mobile 是无模式的——它是一个经典的 JSON 文档数据库，这使其更灵活。例如，添加新字段和索引不会破坏严格的模式，这可以使应用程序升级更快、更容易和更高效。

### SQL 支持

- Atlas Device SDK 需要一个[专有 API](https://roadmap.sh/api-design)和不支持联接和聚合的语法，因此开发人员必须在代码中解决这些限制。
- Couchbase Mobile 从云数据库到设备上的数据库都支持 SQL++，这意味着您可以在整个应用程序生态系统中使用相同的查询。[SQL](https://roadmap.sh/sql)支持也使 Couchbase 易于开发人员采用。

### 向量搜索

- MongoDB 仅在 Atlas 中支持向量搜索，这使其依赖于互联网访问才能工作。这意味着如果没有互联网，就没有向量搜索。
- Couchbase Mobile 支持在云数据库和设备上运行的 Couchbase Lite 中进行[向量搜索](https://thenewstack.io/the-dos-and-donts-of-implementing-effective-search)。这使得离线优先的边缘 AI 功能成为可能，有助于使应用程序面向未来并添加 AI 功能。

### 数据同步

- MongoDB 的同步解决方案不支持点对点同步。这意味着它无法在没有互联网连接到 Atlas 的情况下进行同步，并且它不支持自定义冲突解决程序。
Couchbase Mobile 提供点对点同步功能，使数据同步能够通过本地设备之间的点对点访问进行，无需互联网连接或中央云控制点。Couchbase Mobile 还允许开发者创建自己的自定义冲突解决策略。

### 设备平台支持

Atlas Device Sync 主要支持 Android、iOS、React Native 和 .NET 等移动设备平台。Couchbase Mobile 支持所有上述平台，并提供 C API，允许开发者将数据处理嵌入到 Arduino 和 Raspberry Pi 等单板计算机上的资源受限物联网 (IoT) 设备中。

## 从 MongoDB Atlas 迁移到 Couchbase Mobile

数据库迁移从未百分之百顺利。这项工作不可避免地会给最周全的计划带来意外情况。如果您正在考虑从 MongoDB Atlas Device Sync/Atlas Device SDK 迁移到 Couchbase Mobile，我们创建了一系列资源来帮助您尽可能轻松便捷地完成迁移：

- [此矩阵](https://www.couchbase.com/comparing-couchbase-vs-mongodb-mobile/) 提供了 Couchbase Mobile 与 MongoDB Atlas Device Sync/Atlas Device SDK 的逐项功能比较。
- [这篇技术博客](https://www.couchbase.com/blog/migrate-mongodb-atlas-to-couchbase/) 提供了关于迁移的考虑因素和方法的深入指南，包括数据建模、数据迁移和应用程序迁移。对于任何开始从 MongoDB Atlas Device Sync/Atlas Device SDK 迁移到 Couchbase Mobile 的人来说，这都是必读内容。
- [此点播网络研讨会](https://youtu.be/1XoIgmc3_Rs?feature=shared) 与 Couchbase 合作伙伴 MOLO17 详细介绍了 [GlueSync](https://molo17.com/gluesync/) 如何帮助轻松地将数据从 MongoDB Atlas 迁移到 [Couchbase Capella](https://www.couchbase.com/products/capella/) 以进行 Couchbase Mobile 迁移，
- 以及此 [Atlas Device SDK 与 Couchbase Lite 比较指南](https://github.com/couchbase-examples/atlas-device-sdk-cblite-compare) GitHub 上深入探讨了每个 SDK 可比功能，包括 Android、.NET、Objective-C 和 Swift。

## 结论

在 Couchbase，我们将移动功能视为战略差异化因素，我们有数百家客户使用该平台来构建其大规模移动应用程序，包括 [百事公司](https://www.couchbase.com/customers/pepsico/)、[阿联酋航空](https://www.youtube.com/watch?v=feADtbfndG4)、[Lotum](https://www.couchbase.com/customers/lotum/) 和 [AutoCrib](https://www.couchbase.com/customers/autocrib/)。我们致力于成为移动数据库应用程序领域的领导者，并将继续发展我们的功能，以支持离线优先的移动和物联网应用程序。
