
<!--
title: 为什么JavaScript开发人员应该学习SQL？
cover: https://cdn.thenewstack.io/media/2024/05/46766d59-tns-outer-excuses-learn-postgresql-featured-image.jpg
-->

SQL 是数据库的语言，如果您是一位使用 PostgreSQL 的 JavaScript 开发人员，那么对 SQL 有一个基本的了解是有益的。

> 译自 [Outer Excuses: Why JavaScript Developers Should Learn SQL](https://thenewstack.io/outer-excuses-why-javascript-developers-should-learn-sql/)，作者 Paul Scanlon。

你好。你是 JavaScript 开发人员，对吧？我是否还可以正确地假设你不知道 SQL，并且不想学习 SQL？

在本文中，我想向你介绍 [Outerbase](https://www.outerbase.com/)，它除了其他功能外，还允许你创建、编辑、可视化和探索数据库中的数据——所有这些都不需要编写 SQL。稍后会详细介绍，但首先，让我们解决房间里的大象（双关语）

> JavaScript 开发人员不再有借口不学习 SQL。

许多 JavaScript 开发人员会做任何事情来避免 [学习 SQL](https://thenewstack.io/how-to-write-sql-queries/)，经过一番研究，我将其归结为三个关键原因：

1. 我没有时间学习 SQL。
2. 我不想学习 SQL。
3. SQL 不是类型安全的。

在之前的文章中： [自动为你的 PostgreSQL 数据库生成类型](https://thenewstack.io/automatically-generate-types-for-your-postgresql-database/)，我解决了第 3 点，所以现在是时候回过头来解决第 1 点和第 2 点了。

## 你不想学习 SQL？

我无法理解，也永远不会理解你为什么没有时间投资自己，所以让我们跳过第 1 点。

但是，第 2 点是我想解决的问题。在 JavaScript 领域，前端和后端之间的界限变得越来越模糊，我认为这实际上非常酷。前端开发人员现在可以做以前需要深入后端知识的事情。但是，这并不意味着你应该跳过基础知识。

SQL 是数据库的语言，如果你是一位使用 PostgreSQL 的 JavaScript 开发人员，那么即使你最终使用 JavaScript 客户端查询数据库，也最好对 SQL 有基本的了解。

学习 SQL 的道路可能有点坎坷，但值得庆幸的是，随着人工智能的兴起和使用它的开发工具公司，学习 SQL 可能变得容易得多。

## 开始使用 Outerbase

继续并 [注册](https://app.outerbase.com/signup/)，然后将 [Outerbase 连接到你的数据库](https://docs.outerbase.com/bases/connect-database)。连接后，你可以开始使用自然语言编写查询，Outerbase AI 会将你的“对话”转换为 SQL 查询。

我已将 Outerbase 连接到我的 PostgreSQL 数据库，我用它来捕获网站访问并将其显示在 [我网站的仪表板](https://www.paulie.dev/dashboard/) 上。我将网站访问者的地理位置数据存储在名为 analytics 的表中。表结构如下所示：

```sql
CREATE TABLE analytics (
  id            SERIAL PRIMARY KEY,          
  date          TIMESTAMP WITH TIME ZONE NOT NULL,
  slug          VARCHAR NOT NULL,
  referrer      VARCHAR,
  flag          VARCHAR,
  country       VARCHAR,
  city          VARCHAR,
  latitude      DECIMAL,
  longitude     DECIMAL
);
```

在下面的“对话”中，我要求 Outerbase 统计 analytics 表中每个国家的访问次数。

![](https://cdn.thenewstack.io/media/2024/05/7152d1f5-tns-outer-excuses-learn-postgresql-outerbase-conversation-1024x640.jpg)

而且毫不费力，Outerbase 编写了以下 SQL 查询，我已在浏览器中运行它以查看结果。

![](https://cdn.thenewstack.io/media/2024/05/1ec51287-tns-outer-excuses-learn-postgresql-outerbase-query-results-1024x640.jpg)

从这里，我可以非常轻松地将此查询复制并粘贴到我的代码中，瞧，我将拥有数据，可以在我的前端以任何我想要的方式显示。

## 在不学习 SQL 的情况下编写 SQL

通过使用 Outerbase AI，你可以使用自然语言描述你想要查询的数据，Outerbase AI 将为你编写 SQL 查询。对于希望在 PostgreSQL 池中试水（再次双关语）但又不想被不熟悉的语法困住的开发人员来说，这感觉像是一个不错的中间地带。

如果你来自 JavaScript，SQL 起初可能看起来像外星语言，但事实并非如此。例如，你能读懂这个吗？

```sql
SELECT name, country, email FROM users 
```

我想你可能可以，而且这是经过设计的。

看看这个 [Don Chamberlin 的视频](https://twitter.com/hieuSSR/status/1786270259206668643)，他是 SQL 的主要设计者之一。在视频中，Don 解释了指导 SQL 语言设计的根本目标。目标 2、3 和 4 尤其相关。

1. 我们想使用表而不是关系这个术语……
2. 我们想将语言基于普通英语单词，如 select。
3. 该语言不应该有特殊符号，并且应该易于在键盘上键入。
4. 我们希望它拥有一些我们称之为即时阅读属性的东西。这意味着，在简单的情况下，没有特殊培训的用户应该能够通过阅读来理解查询。

我认为你会同意，上面的简单 SELECT 语句满足了这些要求。即使只是在普通句子的上下文中阅读它也说得通。例如，从用户中选择姓名、国家和电子邮件。

> 有趣的事实：SQL 不必都是大写。

在 JavaScript 领域，事情有点奇怪。例如，以下是上面使用的相同查询，但使用 Supabase 和 Xata 特定的 JavaScript 语法编写。

**Supabase**

```javascript
supabase.from('users').select('name, country, email');
```

**Xata**

```javascript
xata.db['users'].select(['name', 'country', 'email']).getMany();
```


*顺便说一句，值得注意的是，Supabase 和 Xata 也可以使用“普通”SQL 进行查询！*

虽然使用 JavaScript 语法查询数据库有一些优势（[类型安全性不在其中](https://thenewstack.io/automatically-generate-types-for-your-postgresql-database/)），但我仍然想知道为什么 JavaScript 开发人员如此不愿意学习 SQL。

在大多数情况下，用 JavaScript 表达的 SQL 需要特殊知识，并且不能像普通句子（英语）那样阅读。而且，学习我所说的 [SamQL-Jackson](https://twitter.com/PaulieScanlon/status/1783547347475067172)（特定于提供商的 JavaScript 语法）是目光短浅的。为什么花时间学习只能与一个提供商一起使用的东西，而你可以投入相同的时间来培养更广泛使用的技能，这将极大地提高你对所用技术的理解，并可能提高你被录用的机会。

但是，我确实认为有一个剩余的观点是使用 SamQL-Jackson 的合理理由，那就是 **自动完成**。例如，如果你要键入 `supabase.` 在你的代码编辑器中，你会看到一个包含许多选项的列表，供你选择以构建你的查询。

![](https://cdn.thenewstack.io/media/2024/05/faad9345-tns-outer-excuses-learn-postgresql-autocomplete-preview-1024x640.jpg)

不过，如果你已经了解 SQL，则可以说你不需要自动完成。你可以非常轻松地快速编写查询，或利用约 40 年的互联网历史来帮助你理解 SQL；或者，更好的是，像 ChatGPT 这样的东西，它也有约 40 年的互联网历史可以参考。如果这两者都失败了，现在还有 Outerbase AI，它将为你编写 SQL！

这可能有点刺激，但 JavaScript 开发人员真的没有借口不学习 SQL 了。

## 最后的想法

听起来我好像对 JavaScript 和 SaaS PostgreSQL 提供商有偏见，但事实并非如此。然而，我确实对开发人员教育有既得利益。当你学习时，“[交付文化](https://thenewstack.io/say-no-to-ship-it-culture-slow-and-steady-wins-the-race/)”周围听到的“最佳实践”噪音不适用于你。当你投资自己时，速度不是一个因素。如果你花了一年时间学习 SQL，那就这样吧。SQL 是一项基础技能。学习它，甚至可能为此而苦苦挣扎，最终将帮助你理解抽象的存在原因。从那里，你可以自己决定它们是否满足你的要求。

然而，从抽象开始意味着你错过了背景故事。这就像看一部电影，直接跳到最后五分钟，只是为了说你已经看到了结尾——或者，“看看我交付了什么”。当然，观看整个过程需要更长的时间，但在此期间，你将了解角色、故事情节，并且（如果故事讲得好）你会全程参与。

对我来说，学习有点类似。我不想跳到结尾，我想体验整个故事。我不知道我是否会改变你对 SQL 的看法，但我认为通过使用 Outerbase AI，你可能会开始看到它并不像你想象的那么可怕和冗长。试试看！
