# 数据库定价趋势：你需要了解的

![Featured image for: Database Pricing Trends: What You Need to Know](https://cdn.thenewstack.io/media/2025/03/71374e06-clouds2-1024x576.jpg)

在不断发展的数据库市场中，有一件事是不变的：价格往往会随着时间的推移而上涨。供应商会调整其定价模式，引入新的层级，并且（通常情况下）随着产品的成熟而提高成本。如果你是一名开发人员、数据工程师或架构师，了解这些趋势可以帮助你更明智地决定在哪里以及如何存储和处理数据。

## 你最喜欢的数据库又涨价了

还记得ClickHouse是快速、经济高效的分析工具吗？嗯，即使是它最近也将价格提高了30%。([阅读更多](https://quesma.com/blog-detail/clickhouse-pricing)。)

Amazon RDS遵循类似的模式。虽然EC2的价格相对稳定，但[AWS](https://aws.amazon.com/?utm_content=inline+mention)随着时间的推移增加了RDS的利润率，这意味着托管数据库服务的价格越来越高，而原始计算的价格却没有。([查看分析](https://viggy28.dev/article/rds-margin-is-ec2-opportunity/)。)

而且，我们不要忘记整个行业因Oracle激进的定价策略而产生的集体创伤后应激障碍。例如，美国国家航空航天局（NASA）由于令人困惑和掠夺性的许可结构，最终向Oracle多支付了数千万美元。([案例研究](https://www.theregister.com/2023/01/13/nasa_software_oracle_overpayment/)。)

不久前，[PlanetScale](https://planetscale.com/?utm_content=inline+mention)放弃了其廉价的Hobby计划，因为它在财务上不可行。CEO Sam Lambert解释说，虽然它吸引了大量用户，但并没有转化为以可持续的速度转变为付费客户。他还指出，云基础设施成本，尤其是出口费用，使得该计划在规模上在经济上不可行。([详情请见](https://www.theregister.com/2024/03/11/planetscale_lays_off_staff_and/)。)

这是整个行业的一种模式——免费层级和低成本计划推动了采用，但除非经过精心设计，否则通常无法转化为有意义的收入。

## 自动伸缩：方便，但预算也会自动伸缩吗？

许多现代数据库供应商现在提供基于使用量的定价模式，该模式可以根据需求自动伸缩。虽然这种灵活性很好，但也可能导致意想不到的成本。

**BigQuery成本陷阱：** BigQuery的每TB扫描5美元听起来很便宜——直到你意识到，在没有适当的成本控制的情况下查询大型数据集可能会导致高得惊人的账单。在一个著名的案例中，一位[HTTP Archive](https://httparchive.org/)用户在忘记对扫描大小应用限制后，试图查询一个大型数据集，一夜之间累积了14,000美元的费用。([阅读更多](https://www.theregister.com/2024/02/22/web_archive_user_bigquery_shock)。)

**事务性数据库，如Supabase和Neon：** 这些服务可以缩放到零，从而节省空闲工作负载的成本。但是，一旦工作负载增加，价格就会迅速上涨。例如，Neon的最低付费层级起价为0美元，但扩展计划的费用在每月69美元到870美元之间，具体取决于你使用的计算量。([Neon定价](https://neon.tech/pricing)。)

**分析数据库，如Snowflake、Databricks、ClickHouse和BigQuery：** 计算成本占主导地位。[Snowflake](https://www.snowflake.com/?utm_content=inline+mention)例如，每个信用额度收取大约2美元的费用，当运行复杂的查询时，仓库会大大增加成本。一个未经优化的查询可能会花费数百甚至数千美元。

自动伸缩本身并没有什么不好——当与正确的成本控制相结合时，它是一种强大的工具。真正的问题是，当平台在没有给用户足够的可见性或保障措施来防止失控的账单时，优先考虑灵活性。

另一个自动伸缩引起的意外账单的案例来自无服务器数据库。虽然无服务器数据库被宣传为具有成本效益和高度灵活性，但许多无服务器产品（如DynamoDB的按需模式）与预置的替代方案相比，可能会变得非常昂贵。

DynamoDB按需模式按请求收费，这使得它对于高流量应用程序来说，比预置容量贵大约五到七倍。例如，按需写入的费用为每百万次请求1.25美元，而预置写入的费用可能低至每百万次请求0.18美元。(参见[AWS定价](https://aws.amazon.com/dynamodb/pricing/)。)

虽然这种模式对于不可预测的工作负载来说是有意义的，但具有稳定流量模式的应用程序可能会不必要地累积大量成本。选择具有自动伸缩保障措施的预置容量通常是控制成本的更好选择。

## 控制自动伸缩：来自不同方法的经验教训

并非所有的自动伸缩实现都是相同的。一些供应商通过围绕存储优先原则而不是计算密集型处理来设计其架构，从而实现更高的成本可预测性。
例如，Hydrolix 是 ClickHouse 的一个分支，它专注于通过优化查询执行并与经济高效的云对象存储（如 AWS S3）紧密集成来控制计算成本。它通过更好的索引和高效的查询过滤，最大限度地减少了对按需扩展的需求，而不是不断启动昂贵的计算资源。

## 隐藏的代价：数据传输费用和供应商锁定

计算和自动扩展成本往往会引起人们的注意，但数据传输费用是意外支出的另一个主要来源。在区域、服务之间或云提供商的网络之外移动数据可能会悄无声息地增加成本，而这些成本并非总是显而易见的。

**出口费用累积迅速：**AWS 每月提供 [100 GB 的免费数据传输](https://aws.amazon.com/blogs/aws/free-data-transfer-out-to-internet-when-moving-out-of-aws/) 到互联网；超出此范围，则会收取费用。例如，将数据从 AWS 传输到互联网的费用在大多数区域按每 GB 0.09 美元计费。因此，定期移动大型数据集可能会导致巨额成本。

**区域间传输不是免费的：**即使留在同一云提供商内也并不总能保护您。AWS 对区域间传输收取每 GB 0.02 美元的费用，这意味着跨区域复制或跨多个区域的分析管道可能会悄无声息地消耗您的预算。

**供应商从锁定中获利：**一旦您开始在云生态系统中积累 PB 级的数据，数据传输成本就会成为切换提供商的障碍。您移动的越多，支付的就越多，从而形成一种昂贵的供应商锁定形式，而很少有组织尽早考虑这一点。

曾经发生过一些值得注意的事件，由于数据传输配置错误，组织面临意外且巨额的费用。例如，配置错误的 AWS S3 存储桶暴露了敏感的客户数据，导致大规模数据泄露。负责配置错误的公司不得不承担泄露的成本，并产生了 [230 万美元的数据传输和存储费用](https://www.webapper.com/aws-cost-horror-stories/)。

**如何控制数据传输成本**：

**优化数据移动：**设计您的架构以最大限度地减少不必要的数据传输。将数据处理和存储保留在同一区域内，以避免区域间费用。

**使用云成本监控工具：**AWS、[Google](https://cloud.google.com/?utm_content=inline+mention) Cloud 和 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure 提供用于跟踪数据传输成本的工具。设置警报可以帮助防止预算超支。 （查看 [NetApp BlueXP](https://bluexp.netapp.com/blog/aws-cvo-blg-aws-data-transfer-costs-solving-hidden-network-transfer-costs?utm_source=chatgpt.com) 以进行深入分析。）

**批量和压缩数据：**不要连续流式传输数据，而是批量传输并使用压缩来减少移动的数据量。

云提供商不会将数据传输费用作为定价模型中的一个明显项目，但忽略它们可能会是一个代价高昂的错误。明智的架构决策和积极的监控对于避免不必要的费用大有帮助。

## 存储与计算成本：什么才是真正驱动账单的因素？

从历史上看，数据库供应商采用了各种定价模型。在 20 世纪 80 年代，[Oracle](https://developer.oracle.com/?utm_content=inline+mention) 引入了按服务器许可模式，允许无限用户访问单个服务器上的数据库。随着多核处理器的普及，许可模式不断发展，以适应处理能力的提高，从而产生了按核心定价结构。

如今，这种方法在 Snowflake、BigQuery 和 Databricks 等主要数据平台中仍然很普遍：

**存储是经济实惠的：**将存储和计算分离的平台（如 Snowflake、BigQuery 和 Databricks）通常按接近原始云存储的价格收费，通常为每月每 TB 20 美元到 40 美元不等。但是，具有耦合存储和计算模型的供应商可能会收取更高的费用，特别是对于需要最少计算资源的大型数据集（请参阅 [Google Cloud BigQuery 存储定价](https://cloud.google.com/bigquery/pricing#storage-pricing)）。

**计算是利润驱动因素：**云数据供应商利用处理能力。例如，Snowflake 和 Databricks 根据“credits”或“DBUs”（Databricks Units）收费，而 BigQuery 按扫描的数据量收费，每 TB 5 美元。计算成本可能会迅速超过存储成本，特别是对于未优化的工作负载。 ([Databricks 定价](https://databricks.com/product/pricing), [Snowflake 定价](https://www.snowflake.com/pricing/))
**Databricks vs. Snowflake 计算成本：**

**Databricks:**

Databricks 使用 Databricks Units (DBUs) 来衡量单位时间的处理能力。每个 DBU 的成本因工作负载类型而异，从轻量级作业的约 0.07 美元到交互式分析的 0.95 美元不等。例如，运行一个消耗 10 个 DBU 一小时的作业将花费 0.70 美元到 9.50 美元之间，具体取决于工作负载类别。Spot 实例和预留容量可以节省成本，但如果没有优化，成本可能会螺旋式上升。（参见 [Databricks 定价](https://databricks.com/product/pricing)。）

**Snowflake:**

计算成本基于虚拟仓库，X-Small 实例的起价约为 2 美元/小时。成本随仓库大小呈指数级增长。选择合适的仓库大小，使用自动暂停功能并避免过度配置是控制 Snowflake 成本的关键。（参见 [Snowflake 优化技巧](https://docs.snowflake.com/en/guides-overview-performance)。）

**BigQuery：一种不同的计算定价方法：**

Google BigQuery 提供每月 2,000 美元的固定费率计划，用于 100 个 slots（大约每个 slot 每月 20 美元）。这有利于具有稳定查询负载的组织，但对于可变工作负载可能效率低下。注重成本的用户必须监控查询模式并优化数据结构，以最大限度地降低处理成本。（参见 [BigQuery 定价](https://cloud.google.com/bigquery/query-reference)。）

如果您不优化查询和工作负载，成本可能会飞涨。例如，Snowflake 的利润主要来自计算消耗，而不是存储。

## 寻找具有成本效益的数据库解决方案

鉴于分析和事务工作负载的成本不断增加，公司需要探索替代方案，在不超出预算的情况下提供相同的功能。一个主要的成本驱动因素是 Elasticsearch，许多组织依靠它进行日志和搜索分析，但它在大规模使用时可能会变得非常昂贵。

这就是 [Quesma](https://github.com/QuesmaOrg/quesma) 的用武之地。例如，如果您正在与 [Elasticsearch 不断上涨的成本](https://quesma.com/blog-detail/elastic-pricing) 作斗争，Quesma 通过其 [数据库代理](https://quesma.com/blog-detail/best-tool-for-the-job) 提供了一种替代方法。通过无缝地将 [Elastic](https://www.elastic.co/observability?utm_content=inline+mention) 查询转换为 SQL，它允许组织利用更具成本效益的数据库后端，包括 ClickHouse 和 Hydrolix。这意味着您可以保留 Elasticsearch 的灵活性，同时显着降低基础设施费用。

## 选择您的供应商，否则您的供应商会掏空您的钱包

转向基于使用量的定价意味着您需要具有战略性。主要要点：

**预计随着供应商的成熟，价格会上涨：** 今天便宜的东西明天可能就不是了。

**自动缩放定价功能强大但危险：** 设置安全措施以避免意外账单。

**计算是真正的成本：** 存储很便宜，但处理数据是供应商赚钱的地方。

**数据传输费用会迅速累积：** 尽量减少不必要的数据移动以控制成本。

**为您的工作负载选择合适的供应商：** 不要丢弃数据，而是优化您存储和处理数据的方式和位置。

选择合适的数据库不仅仅是关于性能，而是关于确保您的定价模式为您服务，而不是与您作对。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)