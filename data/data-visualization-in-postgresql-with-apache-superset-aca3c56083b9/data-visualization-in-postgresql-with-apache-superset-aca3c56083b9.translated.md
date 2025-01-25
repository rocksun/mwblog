# 使用Apache Superset进行PostgreSQL数据可视化

数据可视化将数据转换为图表等图形表示，以便更快地理解复杂信息。这有助于分析师和利益相关者识别趋势、异常值和模式，从而做出明智的决策并获得洞察。

对于使用PostgreSQL进行数据可视化，既有付费工具也有开源工具可用。在这篇博文中，我们将快速介绍其中一些工具，然后向您展示如何使用Apache Superset和PostgreSQL可视化数据。

➡️ 想了解更多关于如何使用PostgreSQL/Timescale构建应用程序的信息？请务必查看以下文章——我们将带您从数据迁移到数据库监控（即将推出）。

> [如何将您的数据迁移到Timescale（三种方法）](https://timescale.ghost.io/blog/how-to-migrate-your-data-to-timescale/)
> [使用PostgreSQL和psycopg3构建Python应用程序](https://www.timescale.com/learn/building-python-apps-with-postgresql-and-psycopg3)
> 附加：[Psycopg2与Psycopg3性能基准测试](https://timescale.ghost.io/blog/psycopg2-vs-psycopg3-performance-benchmark/)

# PostgreSQL的数据可视化工具

## 开源选项

**Metabase:** 它具有简单的界面，允许非技术用户直接探索和查询数据，使其成为基本数据分析的理想选择。**Grafana:** 此数据可视化工具专注于可视化和监控时间序列数据（例如，服务器日志和基础设施指标）。它提供高级可视化、集成和插件，但不适用于传统的BI任务，例如临时查询。**Apache Superset:** 它提供与Tableau和Power BI等付费工具相当的功能，并支持数据探索、可视化和仪表板。此工具通过SQL编辑和用户定义的指标（基于Python）提供高度定制。

## 付费选项

**QlikView:**这是一个强大的引擎，擅长处理大型数据集和复杂的分析，使用内存处理来提高速度。**Power BI:** 它具有用户友好的界面，可以与Microsoft产品无缝集成，并连接到各种数据源以方便分析。**Tableau:** 此数据可视化工具可帮助您创建令人惊叹且交互式的数据透视表，非常适合清晰地呈现数据洞察。

付费工具具有更广泛的功能集、更好的可扩展性和更多支持，但需要许可证，这可能成本很高。开源工具可免费使用和修改，但可能需要技术专业知识，并且在大规模部署方面存在局限性。

出于本文的目的，我们选择**Apache Superset**来可视化PostgreSQL中的数据，因为它是一个开源的、基于Python的、可扩展的平台，具有广泛的可视化功能。它包括一个用户友好的界面和一个SQL编辑器，使其成为技术和非技术用户都非常优秀的工具。要访问数据集，请访问[Postgres-Superset-Example GitHub 仓库](https://github.com/stormatics/Postgres-Superset-Example)。

# Apache Superset

[Superset](https://superset.apache.org/)是一个快速且轻量级的开源BI平台，使用户可以轻松地探索数据，可以使用无代码可视化构建器（支持拖放）**或**SQL IDE。一些关键点包括：
- 由Apache软件基金会支持，并由Airbnb支持
- 支持40多种可视化，从简单的折线图到高度详细的地理空间图表
- 能够缓存仪表板可视化数据
- 提供具有非常详细设置（包括用户和角色权限）的管理面板
- 能够访问许多SQL和NoSQL数据库
- 简单友好的用户界面

Superset旨在处理任何大小的数据集，因为它作为数据库之上的一个薄层运行，数据库管理所有数据处理。平台的性能更多地取决于用户活动和用户数量，而不是数据大小。对于中等规模的用户群，8 GB RAM和2个vCPU的设置就足够了。

# 安装Apache Superset

安装基本库：

```bash
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev python3-pip libsasl2-dev libldap2-dev python3.8-venv
```

我们将使用虚拟环境进行Superset安装，以避免与其他Python版本冲突。

```bash
pip install virtualenv
```

您可以使用以下命令创建和激活虚拟环境：

```bash
python3 -m venv venv
source venv/bin/activate
```

一旦激活Python虚拟环境，安装或删除的任何Python包都将保留在该环境中，并且不会影响本地Python设置。要离开环境，您可以运行以下命令：

```bash
deactivate
```

升级虚拟环境中的pip版本，这样就不会出现任何依赖项错误：

```bash
pip install --upgrade pip
```

首先安装apache-superset和其他支持库：

```bash
pip install apache-superset
```
```python
pip install marshmallow
pip install Pillow
pip install psycopg2
```

设置`FLASK_APP`和`SUPERSET_SECRET_KEY`变量。Flask是一个轻量级的Python Web框架，用于Apache Superset Web服务器。

```bash
export FLASK_APP=superset
export SUPERSET_SECRET_KEY="mysecretkey"
```

创建一个管理员用户以访问Superset仪表板（使用`admin`作为用户名才能加载示例）。

```bash
superset fab create-admin
```

然后，您需要初始化数据库：

```bash
superset db upgrade
```

加载一些虚拟数据进行测试：

```bash
superset load_examples
```

创建默认角色和权限：

```bash
superset init
```

此步骤之后，是时候初始化Web服务器了。对于开发用途，使用以下命令启动Superset：

```bash
superset run -p 8500 -h 0.0.0.0 --with-threads --reload --debugger
```

-p = 端口
-h = 绑定主机

**注意**: 对于生产环境，请配置像Gunicorn、Nginx或Apache这样的Web服务器。请遵循[在WSGI HTTP服务器上运行Superset](https://superset.apache.org/docs/installation/configuring-superset/#running-on-a-wsgi-http-server)中的指南。

使用管理员凭据访问Superset仪表板：

`http://<PUBLICIP>:<PORT>`

确保端口已打开并且您可以访问Web服务器。登录后，您可以看到以下主页：

# 创建PostgreSQL数据源

选择右上角的**+**按钮，然后选择**数据 → 连接数据库**。

选择PostgreSQL作为数据库。

提供数据库的凭据。

成功连接后，单击**完成**选项。

# 创建数据集

登录后，您将进入此主屏幕，您可以在其中创建仪表板、图表和数据集。第一步是创建一个数据集，我们为可视化提供表或视图。

单击**+ 数据集**按钮以创建数据集。

这将带您进入以下屏幕，您可以在其中选择用于可视化的对象。我们使用**booking**表进行可视化。选择后，选择**创建数据集和创建图表**按钮。

# 创建可视化

## 使用Superset资源管理器UI

现在，您可以根据数据点选择任何所需的图表。我们将根据我们的要求选择**时间序列折线图**。选择**创建新图表**按钮。

在此步骤中，我们现在可以对我们的bookings表进行切片和切块。

我们的要求是按**月**获取**总预订量**。查询如下所示：

```sql
select date_trunc('month', starttime) as month, count(*)
from bookings
group by month;
```

为此，我们可以在Superset上设置以下参数：

**时间**`starttime`**时间粒度** **度量**字段包含要显示的列。在这里，我们可以提供一个聚合列，即**COUNT(*)**。- 对于可视化选项，选择**自定义**选项卡。

选择**创建/更新图表**后，它将在PostgreSQL上运行查询并可视化最终结果，如下所示。

要保存此图表，请单击**保存**按钮，提供图表名称，然后创建一个新的仪表板。

单击**保存并转到新仪表板**按钮。

## 使用SQL查询

您还可以使用SQL查询创建仪表板：

单击**SQL → SQL LAB**。

确保选择正确的数据库和模式。

在这里，您可以直接运行查询。执行此查询后，它将提供**创建图表**选项。

选择**创建图表**以可视化最终结果。

这次，我们将选择**饼图**进行表示。要求是**列出每个设施产生的总收入**。

```sql
select facs.name, sum(slots * case
when bks.memid = 0 then facs.guestcost
else facs.membercost end) as revenue
from cd.bookings bks
inner join cd.facilities facs
on bks.facid = facs.facid
group by facs.name;
```

这里，**维度字段**(一个或多个用于分组的列)将设置为**name**，**revenue**是每个设施的度量。

**注意:** 即使我们有可用于查询的原始数据，Superset也需要聚合。解决方法是进行无意义的聚合，就像我们上面所做的那样，即SUM(Revenue)。您可以在[Stack Overflow](https://stackoverflow.com/questions/48434895/visualize-raw-output-of-sql-lab-query-in-superset)上了解更多信息，或访问此[Apache Superset GitHub页面](https://github.com/apache/superset/issues/5570)。

单击**保存图表**按钮，提供查询的详细信息，并将其保存到我们之前创建的**Bookings仪表板**。

单击**保存并转到仪表板**。

**问题:** 仪表板刷新策略是什么？用户可以手动刷新仪表板或设置自动刷新间隔。

此仪表板也可以通过单击**共享**按钮来共享，因为它会创建一个查看此仪表板的URL，该URL可以复制到剪贴板或通过电子邮件发送。

# 数据可视化的最佳实践
- 在开始可视化之前，请确保您的
数据干净且准确，可获得可靠的洞察。- 选择能够体现数据重要性的可视化技术，根据受众的兴趣进行定制，并清晰地标记所有内容，以便于解读。简单为妙。
- 使用经过良好优化的 SQL 查询和索引可以减少大型数据集的可视化加载时间。
[考虑缓存结果](https://superset.apache.org/docs/installation/cache/)以提高常用可视化的性能。- 根据用户反馈定期更新您的仪表板以适应新信息。

# 使用 Timescale 增强您的仪表板
如果您需要一个数据库来存储您的数据并增强您的仪表板，请尝试 Timescale，这是一个快速、易用且可靠的 PostgreSQL 云平台，适用于时间序列、事件和分析。

通过自动分区、有效的数据压缩（90% 或更多）和[实时数据聚合](https://www.timescale.com/blog/how-we-made-real-time-data-aggregation-in-postgres-faster-by-50-000/)，Timescale 将使您的查询速度飞快，使您能够构建一个稳定而快速的应用程序，永远不会让您的用户失望。想试试吗？[创建 Timescale 帐户](https://console.cloud.timescale.com/signup)——30 天免费试用。

# Superset 常见问题 (重要)
## 如果表模式更改了怎么办？
要让 Superset 发现您的新列，您只需转到**数据 -> 数据集**，单击已更改模式的数据集旁边的编辑图标，然后从**列**选项卡中点击**从源同步列**。幕后，新列将被合并。之后，您可能需要重新编辑表/图表，以配置“列”选项卡，选中相应的复选框，然后再次保存。

## 我可以一次连接/查询多个表吗？
**在 Explore 或 Visualization UI 中不可以**。Superset SQLAlchemy 数据源只能是单个表或视图。

处理表时，解决方案是创建一个包含分析所需所有字段的表，这很可能需要一些预定的批处理过程。

视图是一个简单的逻辑层，它将任意 SQL 查询抽象为虚拟表。这允许您**连接和联合多个表**，并使用任意 SQL 表达式应用一些转换。这里的限制是您的数据库性能，因为 Superset 将有效地在您的查询（视图）之上运行查询。一个好的做法可能是将自己限制为仅将主要的大表连接到一个或多个小表，并尽可能避免使用**GROUP BY**，因为 Superset 将执行自己的**GROUP BY**，并且两次执行此操作可能会降低性能。

**无论您使用表还是视图，性能都取决于数据库向与 Superset 交互的用户提供结果的速度。**
但是，如果您使用的是 SQL Lab，则没有此类限制。您可以编写 SQL 查询来连接多个表，只要您的数据库帐户有权访问这些表即可。

*本文由 Muhammad Ali Iqbal 撰写，最初发表于 2024 年 3 月 21 日 Timescale 官方博客上的**此处**，最后更新于 2024 年 11 月 25 日。*