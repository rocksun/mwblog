
<!--
title: Datasette简介：表格数据的用户界面
cover: https://cdn.thenewstack.io/media/2024/09/70364e29-nat-zfx_claru9s-unsplash.jpg
-->

Datasette 是一个功能性的交互式前端，用于表格数据，无论是 CSV 文件还是数据库模式。我们对其进行了测试。

> 译自 [Introduction to Datasette, a Frontend to Tabulated Data](https://thenewstack.io/introduction-to-datasette-a-frontend-to-tabulated-data/)，作者 David Eastman。

与所有大型开源项目一样，了解[Simon Willison](https://thenewstack.io/datasette-a-developer-a-shower-and-a-data-inspired-moment/)的[Datasette](https://datasette.io/)的最佳方式是尝试一下，以了解其功能。它旨在为“数据记者、博物馆馆长、档案管理员、地方政府、科学家、研究人员”提供服务，是一个功能性的交互式表格数据前端，无论是 CSV 文件还是数据库模式。就像[Tiddlywiki](https://thenewstack.io/tiddlywiki-an-open-source-alternative-to-notion-or-obsidian/)一样，它拥有一个[生态系统](https://docs.datasette.io/en/stable/ecosystem.html#)和忠实的用户群。

我在这里想为开发者介绍这个工具，看看你是否可以在自己的组织内部使用它——在这种情况下，作为那些不太可能直接使用 SQL 查询的人员的仪表板。构建企业仪表板是大多数开发者在职业生涯中某个阶段都需要做的事情。

我将使用我上一篇文章中的数据快速演示一下，然后再用我自己的表格数据托管 Datasette。

让我们使用[Datasette lite](https://lite.datasette.io/)，它由[WebAssembly](https://thenewstack.io/webassembly/)在你的浏览器中托管。请等待几秒钟，它就会出现：

![](https://cdn.thenewstack.io/media/2024/09/355cbc5d-image-1024x567.png)

我们将使用[此链接](https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv)加载一些“按时间划分的总人口”数据，你可能在我的上一篇关于[Plotly Dash](https://thenewstack.io/introduction-to-plotly-dash-the-most-popular-ai-data-tool/)的文章中看到过这些数据；只需点击“加载 CSV”，我们就可以快速深入数据：

![](https://cdn.thenewstack.io/media/2024/09/fd9c73eb-image-1.png)

Datasette 中的一个不错的工具是使用“分面”来汇总多条目数据。在 lite 版本中，我们无法像在完整版本中那样从任何列创建分面；但我们可以使用建议的分面，例如上面的“大陆”：

![](https://cdn.thenewstack.io/media/2024/09/bf18f771-image-2.png)

（注意：“FSU”是前苏联。）

这给了我们一个非常有用的摘要。Datasette 允许你浏览数据，如果你愿意，还可以尝试使用 SQL——事实上，它可能是一个[学习 SQL](https://datasette.io/tutorials/learn-sql)的好方法，因为你始终可以在任何页面上查看和编辑 SQL。

每个页面都有一个唯一的 URL，因此你可以将其传递给其他人。它还可以以 CSV 或 JSON 格式显示给定数据。虽然 Plotly Dash 侧重于绘图，但 Datasette 主要侧重于直接处理表格数据。但是，它也提供数据可视化，如[此示例](https://congress-legislators.datasettes.com/legislators/offices)中的聚类地图所示。

现在你已经快速了解了 Datasette 如何处理 CSV 文件中的表格数据，让我们[安装它](https://docs.datasette.io/en/stable/installation.html)并将其指向一个简单的数据库。

我使用的是我的旧款 Macbook，因此可以直接使用 Homebrew：

![](https://cdn.thenewstack.io/media/2024/09/548f6d1d-image-3-1024x160.png)

像往常一样，我有很多 keg 要倒。版本检查通过：

![](https://cdn.thenewstack.io/media/2024/09/d8cb8bcf-image-4.png)

现在 Datasette 已经安装在我的 Macbook 上，我将安装我关于[AI 模式生成](https://thenewstack.io/sql-schema-generation-with-large-language-models/)的文章中提到的那个简单的[书籍模式](https://www.db-fiddle.com/f/6Fj2vw8bFhzVADG4UFUjD6/0)，尝试使用 SQLite3 方言。我将使用一个新的空“books”模式启动 SQLite3：

![](https://cdn.thenewstack.io/media/2024/09/65acbe50-image-5-1024x152.png)

有三个表：authors、publishers 和 books。

```sql
CREATE TABLE authors (
  author_id INTEGER PRIMARY KEY NOT NULL,
  name VARCHAR(255) NOT NULL,
  birthday DATE NOT NULL
);

CREATE TABLE publishers (
  publisher_id INTEGER PRIMARY KEY NOT NULL,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL
);

CREATE TABLE books (
  name VARCHAR(255) NOT NULL,
  author_id INTEGER,
  publisher_id INTEGER,
  published_date DATE NOT NULL,
  PRIMARY KEY (name, published_date),
  FOREIGN KEY (author_id) REFERENCES authors(author_id),
  FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
);
```

然后我们插入一些数据行：

```sql
INSERT INTO authors (name, birthday) VALUES ('Iain Banks', '1954-02-16');
INSERT INTO authors (name, birthday) VALUES ('Iain M Banks', '1954-02-16');
INSERT INTO publishers (name, address) VALUES ('Abacus', 'London');
INSERT INTO publishers (name, address) VALUES ('Orbit', 'New York');
INSERT INTO books (name, author_id, publisher_id, published_date) VALUES ('The Wasp Factory', 1, 1, '1984-02-16');
INSERT INTO books (name, author_id, publisher_id, published_date) VALUES ('Consider Phlebas', 2, 3, '1988-04-14');
```

你可能已经发现了最后一个插入语句中的错误——我们稍后会讨论这个问题。

现在你应该有一个 books 数据库文件：

![](https://cdn.thenewstack.io/media/2024/09/abae89e0-image-6-1024x202.png)

现在只需使用该文件名将 Datasette 指向 books 数据库：

![](https://cdn.thenewstack.io/media/2024/09/0e926ee6-image-7-1024x379.png)

你的全新 Datasette 前端位于提到的 URL 上：

![](https://cdn.thenewstack.io/media/2024/09/e0084d8a-image-8-1024x394.png)

我最初没有注意到这个错误，但现在当我们浏览书籍表时，我清楚地看到了它：

![](https://cdn.thenewstack.io/media/2024/09/c5d7bf53-image-9-1024x866.png)

我需要更改我的第一本书条目，以便将 `publisher_id` 更新为 2。我将在 SQLite3 中执行此操作：

![](https://cdn.thenewstack.io/media/2024/09/4ee89778-image-10-1024x323.png)

刷新页面后，我们看到更正：

![](https://cdn.thenewstack.io/media/2024/09/877ac4a7-image-11-1024x146.png)

请注意列上方的齿轮；这些允许您从任何列数据创建方面。

## 结论

我注意到有一个基于 Datasette 的 [SaaS 平台](https://www.datasette.cloud/) 允许使用 SQL DDL 命令。另一个有趣的补充是 [增强功能](https://simonwillison.net/2023/Dec/1/datasette-enrichments/)，它会针对行触发脚本——这感觉是扩展框架的一种明智方法。

与 Tiddlywiki 一样，Datasette 的功能性强于美观——因为它旨在使用，而不是出售。但代码是可用的，插件应该允许您根据自己的需要塑造前端。
