
<!--
title: Apache Iceberg 3.0 版本新特性速览
cover: https://cdn.thenewstack.io/media/2025/06/3d8f2a7e-thomas-park-fqf4osws6qc-unsplash.jpg
summary: Apache Iceberg 第 3 版发布，增强了数据表格式的灵活性，包括新增数据类型、更快的删除、行沿袭和 NULL 类型的默认值。新版本将更好地支持新的用例，并着重改进流式传输和低延迟等特性。Snowflake 开源的 REST 目录 Polaris 的第一个版本也即将发布。
-->

Apache Iceberg 第 3 版发布，增强了数据表格式的灵活性，包括新增数据类型、更快的删除、行沿袭和 NULL 类型的默认值。新版本将更好地支持新的用例，并着重改进流式传输和低延迟等特性。Snowflake 开源的 REST 目录 Polaris 的第一个版本也即将发布。

> 译自：[What's New in Apache Iceberg 3.0](https://thenewstack.io/new-in-apache-iceberg-3-0-fresh-data-types-null-vals-change-capture/)
> 
> 作者：Joab Jackson

Apache Iceberg 的第 3 版已经发布。其中添加了许多功能，扩展了数据表格式的灵活性，包括一些需求量很大的数据类型、更快的删除、行沿袭以及 NULL 类型的默认值。

[Russell Spitzer](https://www.russellspitzer.com/about/index.html) 解释说，这个新版本（以及核心开发团队即将开始开发的 v4 版本）将更好地为 Iceberg 配备新的用例，他是 [Apache Iceberg](https://iceberg.apache.org/terms/) 的项目经理。

作为一种开放数据格式，Apache Iceberg 在创建 [数据湖仓](https://thenewstack.io/showdown-at-the-lakehouse-databricks-muscles-up-with-tabular/) 方面发挥了重要作用，它结合了多个结构化和非结构化数据源以进行大规模分析。它使用一套复杂的元数据来跟踪它索引的不同文件中变化的轨迹。

Iceberg 以及一个好的元数据存储，可以跟踪模式的演变，这为用户提供了更大的灵活性来更新模式，同时保持查询旧数据的能力。它可以进行时间旅行和回滚。它也可以扩展，而无需用户担心分区。

Apache Iceberg 既是一组规范，也是许多参考实现。有一个视图规范，一个 REST 规范，用于描述如何与服务器通信。它还包括一个用于存储索引、统计信息和其他无法存储在 Iceberg 清单中的数据位的 [Puffin 文件格式](https://iceberg.apache.org/puffin-spec/) 的规范。还有一系列用不同语言（Java、Python、Rust、Go、C++）编写的实现，并且基于不同的平台，例如 [Apache Spark](https://thenewstack.io/architects-guide-to-apache-iceberg/) 和 [Apache Flink](https://thenewstack.io/a-developers-guide-to-getting-started-with-apache-flink/)。

![](https://cdn.thenewstack.io/media/2025/06/fb5ec95c-iceberg-diagram.jpg)

![](https://cdn.thenewstack.io/media/2025/06/72d8f51e-iceberg-01-300x225.jpg)

Spitzer

Spritzer 与 [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) 的开发者关系高级经理 [Danica Fine](https://www.linkedin.com/in/danica-fine/) 在本月早些时候于旧金山举行的年度 [Snowflake Summit](https://thenewstack.io/snowflake-streamlines-data-analysis-for-enterprise-ai/) 上，举行了一次关于 [Iceberg 第 3 版规范](https://iceberg.apache.org/spec/#version-3-extended-types-and-capabilities) 的解释性会议。他们涵盖的新功能包括：

*   删除向量
*   变体类型
*   几何类型
*   行沿袭
*   NULL 默认值

## 删除向量

Fine 解释说，在删除数据方面，Iceberg 有两个途径：写时复制和读时合并。**写时复制**只是复制正在更改的任何文件，减去需要删除的任何行；**读时合并**保留原始文件，然后创建一个删除文件，记录要删除的内容。删除可以是某个值的所有实例（相等删除），也可以是特定位置的单个实例（位置删除）。

然而，位置删除可能会造成困境。您可以有一个文件捕获分区中的所有删除，或者为每个文件创建一个删除文件。因此，管理员面临着理解并做出适当权衡以优化访问速度的问题。

![](https://cdn.thenewstack.io/media/2025/06/b99469c5-iceberg-delete-1024x768.jpg)

对于 v3，位置删除文件将被高性能的 Puffin 文件取代。Puffin 也已被重新用于存储删除文件。每个文件都将获得其删除向量。

Fine 说：“您将会看到您这边的维护任务少了很多。您实际上不必经历并整合您的数据。”

## 新数据类型

v3.0 中有大量新的数据类型。

首先是 [变体类型](https://github.com/apache/iceberg/issues/10392)，它为存储半结构化数据（例如 [JSON](https://thenewstack.io/an-introduction-to-json/)）提供二进制支持格式。它允许您更改正在摄取的数据类型，而无需更改模式。变体可以使用多个值进行扩展。

Spitzer 说，Snowflake 本身已经支持变体类型，因此将其扩展到 Iceberg 是有意义的。

![](https://cdn.thenewstack.io/media/2025/06/3e0c2a4b-iceberg-variant-1024x768.jpg)

他说：“变体对于很多不同的事情都非常有用。”您将获得“拥有结构化类型的所有好处，同时仍然能够灵活地在每个单元格中存储您想要的任何内容。”

例如，他指出使用变体类型来捕获来自 [物联网部署](https://thenewstack.io/enterprise-challenges-for-the-internet-of-things/) 的数据。想象一下一个传感器，它提供经度和纬度值，以及错误代码。

最终用户将需要将变体类型写入引擎（和/或应用程序），将数据写入 Iceberg 列。很快，您还可以将 [变体类型分解](https://github.com/apache/parquet-format/blob/master/VariantEncoding.md) 为适当的 [Parquet 列](https://thenewstack.io/an-introduction-to-apache-parquet/) 以进行更快的分析，尽管目前尚不支持。

该版本还提供了几种新的几何数据类型。地理类型选项解锁了许多功能：Geometry 捕获二维表面，Geography 可用于三维和球形对象（此类型将在今年夏天晚些时候提供）。

Fine 警告说，地理类型仅适用于新列——您无法将数据类型反向移植到现有列。用户代码也必须进行修改才能享受新的数据类型。

## 行沿袭

Spitzer 说，行沿袭是 Snowflake 的另一个功能，实际上在 Snowflake 的许多功能中使用。

行沿袭提供了一种检查表的每一行更改的方法：数据何时更改，以及从什么更改而来（“[变更数据捕获](https://thenewstack.io/change-data-capture-for-real-time-access-to-backend-databases/)”）。基本上，行沿袭允许您审核您的数据更改。

Spitzer 说：“这是以前在 Iceberg 表中根本无法做到的事情。” “我们构建了一堆代码来尝试使用 CDC 视图来近似实现这一点，但您真的永远无法确定单个行发生了什么以及它来自哪里。”

两个新的元数据列捕获此活动：一个用于行更新，另一个用于上次更新该行的快照。

行沿袭会自动为 Iceberg v3 启用。

![](https://cdn.thenewstack.io/media/2025/06/811349ff-iceberg-row-1024x768.jpg)

## Null 默认值

NULL、NULL、NULL。开发人员讨厌 Null。Null 遍布 Iceberg 表。问题是 Iceberg 中没有 null 的默认值。在计算时间方面，您如何进行数学运算？

现在，Iceberg 提供了一种将所有缺失值更改为设定值的方法，然后再进行计算。

因此，Null 获取了两个新参数。一个是 `initial-default`。这将是在升级后，引擎首次扫描表时，将 NULL 替换为的值。这个想法是您设置一次 `initial-default` 并忘记它。

还有一个 `write-default`，它在将 NULL 写入表时添加指定的。这可以随时更改。

Spitzer 解释说：“存在两个不同的默认值的原因是，一旦您完成了该操作并且某一行被压缩或移动到另一个文件，则以前为空的值现在被写为实际值，因此您无法第二次更改它。”

## v3 之后：流式传输和低延迟

那些升级到 Apache Iceberg v3 表的人将需要一个符合 v3 标准的引擎，并且一些更新将需要更改在 Iceberg 上运行的代码。

Spitzer 说，工作组已经在启动 Iceberg 第 4 版。新功能的提案正在邮件列表中分发。

Spitzer 在接受 TNS 的后续采访时说：“我们正在研究大量的事情，试图使 Iceberg 成为一种更好的表格式，适用于目前不太擅长的用例。”

这些包括小表和具有大量更新的表。他们正在寻找更好的方法来适应流式传输应用程序，并且他们希望总体上降低延迟。这将涉及减少对元数据层的写入次数。

## Apache Polaris 也即将发布一个重要版本

虽然最初由 Netflix 开发，随后由 [Dremio](https://www.dremio.com/resources/guides/apache-iceberg/) 维护，但 Iceberg 已经从 Snowflake 获得了相当多的开源帮助——包括工程时间和甚至 Snowflake 最初为其自己的数据格式在内部开发的某些功能。

去年，Snowflake [开源发布](https://thenewstack.io/the-open-format-movement-heats-up-snowflake-embraces-apache-iceberg/) 了它为 Iceberg 开发的自己的 REST 目录，[称为 Polaris](https://thenewstack.io/snowflake-polaris-aims-for-multiquery-engine-interoperability/)。Iceberg 需要一个元数据目录来集中管理 Iceberg 表的元数据管理、治理和访问控制。

Spitzer 说，这个想法是“从客户端抽象出提交逻辑，并将它们放在一个中央服务器位置。”该目录通常依赖于数据库来获取实际的持久层。Snowflake 自己的商业 Polaris 实现 [Open Catalog](https://www.snowflake.com/en/product/features/open-catalog/) 使用 [FoundationDB](https://thenewstack.io/foundationdb-a-reliable-key-value-store-with-acid-compliance/)。

Spitzer 说，Polaris 的第一个版本将“很快”发布。正在为生产和安全保证进行最后的调整。该软件有很多需要更改的 Snowflake 特有内容。

当然，该软件必须是可扩展的。

“有些人希望将其用于他们自己的内部组织，在这种情况下，目录上每秒 20 个事务就足够了。但是我们有些人希望将其作为一项服务运行，或者为一个大型组织运行它，在这种情况下，您需要处理每秒数千个事务。这种情况可能非常罕见，但我们希望确保它可以扩展到该水平，”他说。