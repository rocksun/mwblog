
<!--
title: FerretDB 2.0：使用PostgreSQL能力的开源MongoDB
cover: https://cdn.thenewstack.io/media/2025/03/5e5b11c1-ferretdb.png
-->

> 译自：[FerretDB 2.0: Open Source MongoDB With PostgreSQL Power](https://thenewstack.io/ferretdb-2-0-open-source-mongodb-alternative-with-postgresql-power/)
> 
> 作者：Joab Jackson

FerretDB，一个基于 PostgreSQL 的开源 MongoDB 代理，发布 v2.0 版本，提升速度并采用厂商中立的 NoSQL 标准。

[Percona](https://www.percona.com/?utm_content=inline+mention) 创始人的一个新项目 [FerretDB](https://www.ferretdb.com/) 旨在为 MongoDB NoSQL 文档导向数据库系统提供一个开源替代方案。

FerretDB 不是一个分支，也不是 [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention) 的重写。相反，它是一个代理，将 MongoDB 5.0+ wire protocol 查询转换为 SQL。它运行在 [PostGreSQL](https://thenewstack.io/postgresql-17-gets-incremental-backup-sql-queries-for-json/) 的 stock 版本上。

FerretDB 系统还可以作为 MongoDB 兼容云服务的本地替代方案，特别是 [Microsoft CosmosDB](https://thenewstack.io/microsoft-introduces-cosmo-db-globally-distributed-multi-mode-azure-database-service/) 和 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 的 [DynamoDB](https://thenewstack.io/dynamodb-when-to-move-out/)（[Google Cloud](https://cloud.google.com/?utm_content=inline+mention) 本身提供 [MongoDB Atlas](https://thenewstack.io/mongodb-atlas-finally-gets-a-command-line-interface/)，MongoDB 的商业云版本）。

周二，该公司发布了 2.0 版本的 [开源软件](https://github.com/FerretDB/FerretDB)，由于包含了 [DocumentDB extension](https://github.com/microsoft/documentdb) for PostgreSQL（由 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 提供）作为数据库引擎，因此性能得到了显着提升。

此外，DocumentDB 扩展提供了对 [BSON (Binary JSON) data type](https://www.mongodb.com/resources/basics/json-and-bson#:~:text=BSON%20stands%20for%20%E2%80%9CBinary%20JSON,more%20quickly%20compared%20to%20JSON.) 的支持，从而能够通过 SQL 查询文档数据。

实际上，FerretDB 可以将任何 Postgres 数据库系统变成 MongoDB 服务提供商。

## 开源很重要

FerretDB 并非旨在作为所有 [MongoDB 实例](https://thenewstack.io/5-reasons-to-run-mongodb-on-kubernetes/) 的直接替代品，尤其是不适用于那些利用 [高级专有功能](https://thenewstack.io/mongodb-unveils-managed-graphql-for-mongodb-atlas/) 的实例，但在接受 TNS 采访时，FerretDB 联合创始人兼 CEO Peter Farkas 估计，它应该适用于大约 80% 的工作负载。

它还可以与大多数第三方 MongoDB 工具和驱动程序一起使用。

Farkas 与 Peter Zaitsev 和 Alexey Palazhchenko 共同创立了 FerretDB。Zaitsev 是 Percona 的创始人之一，该公司专门为 [MySQL](https://thenewstack.io/upgraded-mysql-crashes-on-restart-percona/)、MongoDB 和 ValKey 等数据库提供 [高性能支持](https://thenewstack.io/percona-backs-valkey-with-enterprise-grade-support/)。Palazhchenko 和 Farkas 也是 Percona 的早期员工。

最初，MongoDB 作为一种简单、高度可扩展的数据存储方式，在 Web 开发人员中找到了归宿。Mongo 使用更友好的 [JSON format](https://thenewstack.io/working-with-json-data-in-python/) 以文档导向模型存储数据，这比 SQL 模式定义的列和行更容易使用，尤其是在处理复杂的嵌套数据时。

2018 年，MongoDB 将其同名文档存储的许可证更改为更严格的 [SSPL license](https://www.mongodb.com/legal/licensing/server-side-public-license)（[从 GPLv3](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)），这主要是为了阻止云提供商在不回报项目的情况下提供 MongoDB 功能（[Reddis](https://redis.com/?utm_content=inline+mention) 几年后也遇到了类似的情况）。

这三位 Percona 资深人士于 2021 年启动了这个项目，他们怀疑许多 MongoDB 用户需要一个开源许可的版本。Farkas 解释说，他们可能为一家完全在其 [open source software](https://thenewstack.io/open-source/) 上构建软件堆栈的组织工作。或者他们可能想要一个用于云提供商的开源本地备份。

## OpenDocDB 标准

许多用户可能不希望在由一家公司控制的开源项目上运行关键系统。认识到这一点，该公司启动了 [OpenDocDB](https://opendocdb.org/about) 计划，希望围绕 FerretDB 吸引一个开发社区。
这个想法是，正如 SQL 已经成为查询结构化数据的供应商中立标准一样，OpenDocDB 也可以基于 [MongoDB API](https://www.mongodb.com/products/tools/mongodb-query-api) 成为查询面向文档的数据库的标准。

按照 [Percona 手册](https://www.percona.com/about)，FerretDB 本身计划通过提供工具和高级企业功能、云服务以及对高可用性关键任务部署的优质支持来赚钱。
