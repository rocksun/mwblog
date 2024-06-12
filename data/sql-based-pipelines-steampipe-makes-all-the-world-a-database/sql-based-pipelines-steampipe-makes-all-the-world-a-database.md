
<!--
title: 基于SQL的管道：Steampipe让全世界都成为数据库
cover: https://cdn.thenewstack.io/media/2024/06/9de8c55f-api-hero-image.png
-->

想为流行平台使用大量 API？想在数据库中使用 SQL 完成所有操作？Steampipe Anywhere 是您的通行证。

> 译自 [SQL-Based Pipelines: Steampipe Makes All the World a Database](https://thenewstack.io/sql-based-pipelines-steampipe-makes-all-the-world-a-database/)，作者 Andrew Brust。

许多公司都有自己的 API，用于编程访问——众多企业 SaaS 应用程序、超大规模云服务和 GitHub 等开发者服务。但所有这些 API 的工作方式都不同，并且需要使用 Python、Java 或 C# 等语言编写命令式代码。如果所有这些服务都能看起来像关系数据库，从而能够使用声明式 SQL 对它们进行检查，以及使用流行的商业智能 (BI) 工具对它们的内容进行报告和可视化，那岂不是很好？

> 普通的旧 SQL 可能会成为互联网上众多平台的特定领域语言。

使用这种方法，普通的旧 SQL 可能会成为互联网上众多平台的特定领域语言。可以通过联接交叉引用平台的不同方面，可以使用 WHERE 子句实现对特定应用程序项的精确定位，并且 SELECT 列列表允许您仅带回您感兴趣的那些项的特定属性。

## 使用基于 SQL 的管道连接互联网服务

事实上，有一个很好的开源选项可以做到这一点。它被称为 [Steampipe](https://steampipe.io/)，它运行得非常好，拥有一个生态系统，其中包含 [一百多个特定于服务的插件](https://hub.steampipe.io/#search)，适用于 Airtable、GitHub、Jira、LinkedIn 和 Kubernetes 等平台；数据库服务，包括 MongoDB Atlas 和 Snowflake（用于管理数据，而不是数据库中的数据）；以及从基于文件的源（如 CSV 文件和 Google 表格）查询数据。

> 现在，通过安装 Postgres 或 SQLite 的扩展，有了一种更简单的方法来使用 Steampipe。

让这一切正常工作就像将 Steampipe 安装到 Linux 环境（包括 [适用于 Linux 的 Windows 子系统](https://learn.microsoft.com/windows/wsl/about)）一样简单，然后拉取您感兴趣的服务的插件并交互式地运行 SQL 查询。简单的文档使您可以轻松了解每个插件支持的表模式，只需一个 SQL 查询即可了解各种在线服务的详细信息。

现在，通过安装特定于 Steampipe 插件的扩展到 [Postgres](https://www.postgresql.org/) 或 [SQLite](https://www.sqlite.org/index.html) 中，有了一种更简单的方法来使用 Steampipe。这允许您直接从这两个众所周知的数据库中查询相应服务，而无需使用传统版本的 Steampipe 实现的单独 SQL 接口。这不仅可以实现不同服务之间的数据的联合联接，还可以实现这些服务与您 *自己的* 数据之间的联合联接。

可能性是巨大的，不仅出现在 SQL 提示符中，而且出现在任何可以与 Postgres 通信的 BI 工具中（基本上，所有工具）。同时，SQLite 实现使得可以在一系列极简主义 Linux 环境中查询此数据。

## 实际应用

此处适用的用例集非常庞大。例如，想象一下获取客户列表，其中包含您在 Salesforce 中跟踪的客户 ID，然后将其加入到本地业务数据库中的客户和销售记录中。

> 当您将信息转换为表格数据时，会发生一件有趣的事情：它不仅可以被开发者和商业智能工具查询，还可以用于其他领域。

然后想象一下获取特定开发者在特定 GitHub 仓库中代码签入的统计信息，并将这些汇总数据存储在您的 HR 系统中和/或在您在 Tableau 或 Power BI 等工具中构建的仪表板中对其进行报告。

再举一个例子：搜索 Slack 对话中对内部应用程序的提及，并将其与 Zendesk 中针对同一应用程序的公开工单进行交叉引用。

## 近乎即时的 SQL 满足

想要一些技术细节？我们可以很快做到。安装独立的 Steampipe 变体就像在命令行中运行 **curl** 命令一样简单。之后，使用 **steampipe plugin install** 命令安装您选择的插件，并处理任何必要的身份验证和连接详细信息。从那里，只需键入 **steampipe query** 即可获得一个交互式提示，用于输入 SQL 查询。

如果您发现这一切都很简单（您应该这样做），请注意，在 SQLite 或 Postgres 中使用 Steampipe 甚至更容易，因为您可能已经安装了这些数据库。

[Jon Udell](https://www.linkedin.com/in/jon-udell-45915)，[Turbot](https://turbot.com/) 的布道者，该公司是 Steampipe 的幕后推手 *(编辑：他也是 The New Stack 的撰稿人，包括撰写有关 SQL 的文章)*。Udell 逐步向我介绍了该产品的功能，以及如何安装和使用它，直到我在自己的机器上运行它。如果您对详细信息感兴趣，请继续阅读，我们将探讨一个具体示例，直接从我在 Udell 的支持下成功在我的计算机上执行的步骤中复制。

## 自己动手

要使用 SQLite 或 Postgres 与 Steampipe 协同工作，您只需安装特定于插件的扩展并配置连接详细信息。然后，您可以立即从现有的数据库环境开始查询。例如，要从 SQLite 中发现 Microsoft Azure 云帐户中的资产，只需按照以下步骤操作：

1. 从 Linux shell 执行以下命令以安装特定于插件的 SQLite 扩展：

```
sudo /bin/sh -c "$(curl -fsSL https://steampipe.io/install/sqlite.sh)"
```

（以上内容可能看起来很神秘，但您可以直接从上面或从 [此处](https://steampipe.io/downloads?install=sqlite) 复制并粘贴。）

2. 当提示输入插件名称时，只需键入“azure”并点击 Enter，然后再次点击 Enter 两次以接受版本和安装位置的默认值。

3. 输入以下 Azure CLI 命令进行身份验证：

```
az login
```

接下来，在结果浏览器窗口中输入您的凭据。

4. 现在，启动 SQLite，并从其提示符中使用以下命令加载插件的扩展：

```
.load <install folder>/steampipe_sqlite_azure.so
```

（其中 <install folder> 是您在步骤 1 中所在的文件夹。）

5. 现在使用以下命令设置您的 azure 订阅：

```
SELECT steampipe_configure_azure('subscription_id="<subscription id>"');
```

将 <subscription id> 替换为您要探索的 Azure 租户中的实际订阅 ID。

6. 就是这样！您现在可以查询各种 Azure 资产。例如，要列出特定 Azure 存储帐户中的所有 Azure blob（基本上提供一个巨大的递归目录列表），请使用以下 SQL 查询：

```sql
SELECT name, container_name, storage_account_name, region, type, is_snapshot
FROM azure_storage_blob
WHERE resource_group=<resource group>
AND storage_account_name=<storage account name>
AND region=<azure region>;
```

当然，请务必将 <resource group>、<storage account name> 和 <azure region> 替换为适合您自己环境的相应字符串（如果您对这些值进行硬编码，请不要忘记引号。）

## 从这里开始更轻松

这就是全部内容。此外，步骤 1 和 2 永远不必重复，步骤 3、4 和 5 也无需再次运行，直到您进入新的 SQLite 会话。这意味着您可以自由执行一系列后续 SQL 查询，以获取有关 Azure 环境的丰富附加信息。

想要安装另一个插件扩展？只需重复上述过程，但输入不同的插件名称，然后启动 SQLite，加载相应的 **steampipe_sqlite_xxx.so** 扩展，使用相应的 **steampipe_configure_xxx** 函数对其进行配置，然后开始查询。每个 steampipe 插件都有简单的文档，列出了所有可查询的表，并提供了大量您可以复制、粘贴、编辑和运行的示例查询。

## 混搭天堂

当您将信息转换为表格数据时，会发生一件有趣的事情：它不仅可以被开发人员和商业智能工具查询，还可以用于其他领域，包括电子表格、无代码/低代码平台、工作流系统，甚至机器学习和 AI 平台。想象一下基于对公共 GitHub 存储库的观察签到或公司 Slack 频道中的讨论来构建一个关于开发人员生产力的预测模型。

一旦您让事物看起来像行和列，各种可能性就会出现。Steampipe 建立了一个不断发展的生态系统，可以优雅而稳健地实现这些场景。
