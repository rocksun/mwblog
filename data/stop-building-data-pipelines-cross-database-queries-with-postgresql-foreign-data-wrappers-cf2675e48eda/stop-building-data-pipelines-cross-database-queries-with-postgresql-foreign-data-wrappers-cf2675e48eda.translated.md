# 停止构建数据管道：使用 PostgreSQL 外部数据包装器进行跨数据库查询

想象一下，你正在运行一个复杂的应用程序，数据存储在不同的地方——用于客户数据的 Amazon RDS，用于时间序列日志的 Timescale，甚至可能还有一些本地 PostgreSQL 实例，用于你尚未迁移到云的遗留数据。听起来很熟悉，对吧？但是，如果你需要将所有这些信息整合在一起的见解呢？这时，外部数据包装器 (FDW) 就派上用场了——这个解决方案非常顺畅，你会奇怪为什么没有早点开始使用它。

FDW 是 PostgreSQL 扩展，可以非常轻松地进行跨数据库查询。[postgres_fdw](https://www.postgresql.org/docs/current/postgres-fdw.html) 扩展充当 PostgreSQL 数据库之间的桥梁，允许你的 Timescale 数据库直接与其他 PostgreSQL 数据库中的数据连接。你可以在一个地方查询所有数据，而无需进行数据迁移、管道或脆弱的 ETL（提取-转换-加载）作业。这就像从 Timescale 的 SQL 界面舒适地获得数据全景图。

让我们深入研究 FDW 发挥作用的几个场景，每个场景都针对我们作为开发人员每天在管理庞大的多数据库环境时面临的各种问题量身定制。

✨ 外部数据包装器只是我们本周推出的众多功能之一。要查看我们 10 月份的所有发布内容并及时了解即将发布的版本，[请访问我们的博客文章](请访问我们的博客文章)或查看[发布页面](发布页面)。

# 使用 FDW 跨 PostgreSQL 数据库进行查询：可能的场景

## 场景 1：驯服微服务架构中的多数据库分析

与许多其他 SaaS 产品一样，Timescale Cloud 使用微服务架构，其中每个微服务都有自己专用的 PostgreSQL 数据库。例如，我们有一个项目服务、一个用户服务、一个计费服务、一个遥测服务等。这种方法有其优点：服务整齐地分离，数据库针对特定任务进行了优化。

但是，我们经常需要运行跨多个数据库运行连接的分析查询。例如，假设我们要根据项目创建日期对总收入进行队列分析。这需要我们连接来自项目服务和计费服务的数据。

一种解决方案是启动一个专用的分析数据库，构建一个管道以从每个服务中提取数据。但是使用 FDW，我们不需要移动任何东西。我们只是设置了一个 Timescale 服务，其中包含许多 FDW，可以直接查询所有其他 Timescale 服务。那么我们如何按项目创建日期进行队列分析或收入分析呢？很简单。只需设置一个 FDW，我们就可以立即跨服务运行实时分析。

以下是它在实践中的样子：

```sql
-- Create the link to the remote server
CREATE SERVER timescale_billing
FOREIGN DATA WRAPPER postgres_fdw
OPTIONS (
host 'serviceID.projectID.tsdb.cloud.timescale.com',
dbname 'tsdb',
port '30702',
extensions 'timescaledb'
);
-- securely store the login details
CREATE USER MAPPING FOR tsdbadmin
SERVER timescale_billing
OPTIONS (
user 'tsdbadmin',
password 'mysupersecurepassword'
);
-- create a billing schema to hold the billing data
CREATE SCHEMA billing;
-- import all tables from the remote server into the billing schema
IMPORT FOREIGN SCHEMA public
FROM SERVER timescale_billing
INTO billing;
-- The project service would be added in the same way
SELECT
time_bucket('1 month', p.creation_date) AS cohort_month,
time_bucket('1 month', b.billing_date) AS billing_month,
SUM(b.revenue) AS total_revenue
FROM
projects.projects p -- this is remote!
JOIN
billing.billing b -- this is remote too!
ON p.project_id = b.project_id
GROUP BY 1,2
ORDER BY 1,2
```

现在，你有一个干净、直接的查询，可以提供可操作的见解——而无需任何 ETL 流程。

## 场景 2：Amazon RDS 满足 Timescale 以进行实时分析

我们的许多客户都从 AWS RDS 开始，并在他们的应用程序中构建了一个功能，以分析仪表板的形式向他们的客户提供见解。此类应用程序的一个示例是多租户 SaaS 平台，用于构建你自己的电子商务网站，包括产品目录、客户、订单、发货和付款。

这种平台的标准功能是分析仪表板，它可以让你了解一段时间内的订单、发货和收入。最初，每个租户的分析屏幕加载速度都非常快，但随着平台越来越受欢迎，并且建立在其上的电子商务网站也越来越受欢迎，其中一些表增长到数千万甚至数亿条记录。分析屏幕开始加载非常缓慢，你需要一个替代解决方案。
RDS 的客户采用 Timescale Cloud 是因为它的实时分析能力，这使得应用内的分析仪表板加载速度非常快。虽然许多客户完全迁移到 Timescale Cloud，但有些人发现完全迁移他们的应用程序是一个更复杂的过程。因此，他们选择只将 RDS 中性能不佳的大型表迁移到 Timescale Cloud。

在前面提到的电子商务示例中，这可能包括订单、发货和付款表。但是，对于他们在 Timescale Cloud 上运行的一些分析查询，他们需要仍然在 RDS 上的数据，例如产品目录表。以前，他们必须设置 ETL 管道才能将所需的数据从 RDS 复制到 Timescale Cloud，从而导致额外的成本和复杂性。FDW 消除了完全同步的需要。

只需几个简单的 SQL 命令，RDS 中所需的表就可以从 Timescale Cloud 中获得，从而可以在几分钟内实现跨系统查询，就像两个系统合二为一一样。想要改进分析仪表板以显示哪些客户上个月下的订单最多吗？或者确定最受欢迎的产品？有了 FDW，这些问题就变得很简单了。您将像以前一样配置 FDW，但这次是指向 RDS 服务。然后，您就可以开始编写如下查询：

```sql
-- Top 10 customers with most orders in January 2024
SELECT
c.customer_id,
c.name,
count(o.order_id) AS order_count,
sum(o.order_amount) AS total_spent
FROM rds_db.customers c -- remote table
JOIN timescale.orders o -- local table
ON c.customer_id = o.customer_id
WHERE o.timestamp BETWEEN '2024-01-01' AND '2024-01-31'
GROUP BY c.customer_id, c.name
ORDER BY order_count DESC, total_spent DESC
LIMIT 10;
```

您不仅仅是在提取数据；您还在 ETL 上节省了时间，并消除了数据重复和不一致的风险。

## 场景 3：聚合分布式数据以获得实时洞察

假设一家全球物流公司的数据分布在不同的区域。车辆数据记录在当地区域数据库中。传统上，您会被困在尝试集中所有这些数据，可能使用 ETL 管道或分析仓库。但是，如果您可以实时查询这些数据库，将数据保留在原地呢？

使用 FDW，您可以准确地做到这一点。设置您的 Timescale 实例以从每个区域的数据库中提取数据，您就可以跨区域聚合数据，而无需移动一个字节。想要查看过去一天按区域划分的车辆数量？完成了。

```sql
-- Aggregate vehicle data across regions without moving it
SELECT region, COUNT(*)
FROM (
SELECT 'North America' AS region, timestamp, location FROM na_db.vehicle_data
UNION ALL
SELECT 'Europe' AS region, timestamp, location FROM eu_db.vehicle_data
) AS vehicle_data
WHERE timestamp > NOW() - INTERVAL '1 day'
GROUP BY region;
```

此查询为您提供跨区域的车辆活动的实时快照，非常适合监控运营、优化路线或了解区域绩效——所有这些都只需最少的努力。

查看我们的文档，了解有关[如何在 Timescale Cloud 中使用 FDW](https://docs.timescale.com/use-timescale/latest/schema-management/foreign-data-wrappers/) 的更多详细信息。

# 为什么 FDW 是游戏规则改变者

FDW 不仅仅是一个工具，它们是简化、集成数据架构的捷径。对于开发人员和数据工程师来说，FDW 消除了移动和转换数据的负担，使您可以专注于构建洞察力，而不是管理基础设施。Timescale 对 FDW 的实现使这一切成为现实，从而可以统一数据以进行强大的跨数据库分析，而无需在 ETL 上浪费时间或精力。

如果您准备好打破数据孤岛，简化分析并消除中间人（看着你，ETL），那么 FDW 已经为您准备好了。[试用 Timescale Cloud](https://console.cloud.timescale.com/signup/?utm_source=blog&utm_medium=email&utm_campaign=november-abl&utm_content=timescale-cloud-signup)——立即开始跨 PostgreSQL 数据库进行查询，看看您的数据工作流程可以多么简单、无缝和强大。

*本文由 Ramon Guiu 撰写，最初于 2024 年 11 月 14 日发表在 Timescale 官方博客的**[此处](https://www.timescale.com/)**。*