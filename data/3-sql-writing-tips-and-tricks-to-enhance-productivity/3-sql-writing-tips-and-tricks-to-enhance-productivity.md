
<!--
title: 提高效率的3个SQL编写技巧
cover: https://cdn.thenewstack.io/media/2025/03/96a7ebe2-sql-writing-productive.jpg
-->

使用通用表表达式、良好的表别名以及编辑器的格式化工具，可以使 SQL 更易于阅读和调试。

> 译自：[3 SQL Writing Tips and Tricks To Enhance Productivity](https://thenewstack.io/3-sql-writing-tips-and-tricks-to-enhance-productivity/)
> 
> 作者：Chris Saxon

如果你是数据库开发人员、数据库管理员或数据分析师，编写 [SQL](https://www.oracle.com/database/technologies/appdev/sql.html?source=:ex:pw:::::TNS_SQL_FEB25_A&SC=:ex:pw:::::TNS_SQL_FEB25_A&pcode=) 以将数据导入和导出[数据库](https://thenewstack.io/introduction-to-databases/)是你工作的关键部分。快速有效地完成这项工作可以提高你的工作效率。相反，处理混乱的语句和数据会让你陷入困境。

在本系列的[第一部分](https://thenewstack.io/3-foundational-principles-for-writing-efficient-sql/)中，我演示了如何通过选择好的名称、规范化表和创建约束来为你提供一个坚实的结构，以便在编写 SQL 时提高效率。

在本文中，我将介绍如何[构造 SQL](https://roadmap.sh/sql) 以使其更易于阅读和调试。诸如公共表表达式 (CTE) 和表别名之类的技术可以将语句从难以理解的谜语转换为清晰的逻辑。

## 清晰地构造查询

大型 SQL 语句可能难以阅读和调试。CTE（也称为 `with` 子句）使你可以将它们分解为更小的部分。

CTE 是命名的子查询，位于 `select` 语句的顶部。你可以在查询后面的像访问常规表一样访问这些子查询。

这带来了一些好处：

- 你可以逐步构建查询。
- 你可以为每个 CTE 指定一个有意义的名称。
- 你可以检查每个 CTE 的结果。

例如，[Oracle Dev Gym](https://devgym.oracle.com/pls/apex/dg/class/databases-for-developers-foundations.html?source=:ex:pw:::::TNS_SQL_FEB25_F&SC=:ex:pw:::::TNS_SQL_FEB25_F&pcode=) 提供免费的测验、锻炼和课程，以帮助你学习 SQL。每个活动都有自己的表。将所有这些合并到一个查询中以报告所有活动是一项艰巨的任务。

使用 `with` 子句，你可以为每种活动类型创建一个 CTE。你可以从获取 [quiz](https://thenewstack.io/how-to-build-a-quiz-app-with-nuxt-and-xata/) 总数开始：

```sql
with quiz_totals as ( … ) 
select * from quiz_totals
```

然后添加锻炼总数并验证它们是否正确：

```sql
with quiz_totals as ( … ), 
     workout_totals as ( … ) 
select * from workout_totalss
```

对课程总数重复此操作，并将每个 CTE 的结果组合起来以获得所有总数，如下所示：

```sql
with quiz_totals as ( … ), 
     workout_totals as ( … ), 
     class_totals as ( … ), 
     all_totals as ( 
       select * from quiz_totals union all 
       select * from workout_totals union all 
       select * from class_totals 
    ) 
select * from all_totals
```

如果你需要更改任何活动类型的查询，很明显逻辑包含在相应的 CTE 中。这比在大量的嵌套子查询中搜索要简单得多。

使用 CTE 将逻辑分解为更小的问题可以使过程更易于管理。但是，每个 CTE 仍然可以引用许多表。无论何时处理多个表，都需要回答一个重要问题：哪些列属于哪个表？

通过在每列前加上其表的别名来明确这一点。

## 使用好的表别名

如果没有表别名，很难知道每列来自哪里。这使得查询更难理解和更改。

但是，未加别名的列有一个更大的问题：它们可能导致错误。

最常见的问题是当两个表具有同名的列时。如果你使用未加别名的名称，数据库将无法识别它来自哪个表，并且该语句将失败。更糟糕的是，如果你添加导致名称冲突的列，此问题可能会影响现有的 SQL。

使用表的别名限定列可以避免这些问题。从表名开头获取的单字母表别名很有吸引力，但很快会导致问题。例如，假设你编写一个查询，该查询同时访问 customers 和 contracts 表。如果你给其中一个别名“c”，你如何知道它与哪个相关，而无需滚动浏览该语句？

更好的方法是使用从表名开头获取的四个字符的别名：

- 对于单字表，别名是其前四个字符。
- 双字表采用每个单词的前两个字母。
- 三字表使用第一个单词的前两个字母和最后两个单词的第一个字母。
- 四字表使用每个单词的第一个字符。

例如：

- `customers` => `cust`
- `order_items` => `orit`
- `shipment_list_batches` => `shlb`

在极少数情况下，这会为不同的表提供相同的别名。如果发生这种情况，请为其中一个表选择一个新别名，并尽可能遵循此系统。如果你需要在查询中两次访问同一张表，请在别名中添加一个前缀，说明该表的作用。你将它们连接到的列是此信息的一个很好的来源。

例如，您可能需要将客户与其送货地址和付款地址关联起来，这两个地址都存储在 addresses 表中。添加 `deli` 或 `paym` 可以清楚地表明 address 表扮演的角色：

```sql
from customers cust
join addresses deli_addr 
on   cust.delivery_address_id = deli_addr.address_id
join addresses paym_addr
on   cust.payment_address_id = paym_addr.address_id
```

使用标准的别名系统很快就会成为第二天性，可以清楚地表明列属于哪个表，并避免错误。一个标准的结构是进一步帮助提高代码可读性的关键。

## 使用一致的风格

格式化 SQL 的最佳方式是许多争论的来源。我们都有自己偏好的子句缩进的位置和方式。关键字应该使用大写还是小写，这是一场旷日持久的争论。

最终，这些选择大多归结于个人偏好。因此，最重要的建议是：

**选择一种格式化风格并坚持下去。**

无论您喜欢如何格式化 SQL，我们都可以同意，在像这样的语句中混合和匹配风格是刺耳且难以阅读的：

```sql
SELECT Some_Columns 
    From a_table 
  JOIN another_table 
on …
```

确保标准风格的最佳方法是使用编辑器的自动格式化程序。在编写完每个语句后运行它。这比边写边格式化要快。您还可以与同事分享规则，以保持整个代码库的格式相似。

有时，自动格式化程序可能难以发现在使用小众功能的复杂 SQL 中在哪里放置换行符。这可能会导致将表达式组合成长行，从而滚动到屏幕边缘之外。

如果您遇到此问题，克服它的一个技巧是在您想要换行的地方放置一个空注释。格式化程序必须尊重这些注释，从而保证在您想要的位置精确换行。

例如：

```sql
select case -- 
  when formatted_lines_are_too_long --
  then 'Use comments to break them up' --
```

使用标准格式化程序是您的编辑器可以帮助您更快地编写 SQL 的众多方式之一，因此值得花时间学习编辑器的生产力功能。

## 了解您的编辑器

您可能已经启用了表和列名的自动完成功能，以帮助您编写 SQL。但这只是您的工具可以帮助您提高生产力的一种方式。

例如，[Oracle SQL Developer extension for VS Code](https://www.oracle.com/database/sqldeveloper/vscode/?source=:ex:pw:::::TNS_SQL_FEB25_G&SC=:ex:pw:::::TNS_SQL_FEB25_G&pcode=) 有一些可以帮助您的技巧。

您可以将表或列从模式浏览器拖到编辑器中。然后，它会询问您是否要在 `select`、`insert`、`update` 或 `delete` 语句中使用它们：

![](https://cdn.thenewstack.io/media/2025/02/fc2d8e1d-vs-code-drag-n-drop_oracle.gif)

这使您不必手动输入每一列，对于具有许多列的表来说，这是一项繁琐的任务。

您还可以在 VS Code 中配置代码片段，将短序列扩展为大型代码块。以下是我依赖的一些代码片段，可以加快编写 SQL 的过程：

- `ssf`=>`select * from`
- `ii`=>`insert into $1 values ( $2 )`
- `crt`=>`create table $1 ( c1 int );`
- `drt`=>`drop table $1 cascade constraints purge;`

花时间学习编辑器中日常任务的键盘快捷键也可以获得良好的回报。

## 结论

业务需求可能很复杂。将这些需求转换为 SQL 可能具有挑战性，如果您不小心，可能会导致巨大的怪物。

通过使用 CTE 和良好的表别名来注意清晰地构造 SQL 可以加快 SQL 的编写和维护过程。使用自动格式化程序和编辑器中的其他工具可以进一步简化任务并提高您的生产力。

然而，正如我们在本系列的第一部分中看到的那样，最重要的收获来自构建坚实的数据模型。选择好的名称、规范化您的表和创建约束可以简化对模式的理解并轻松编写 SQL。
