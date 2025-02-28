# 编写高效SQL的三个基础原则

![关于编写高效SQL的三个基础原则的特色图片](https://cdn.thenewstack.io/media/2025/02/d7f3f409-sql-writing-efficient-1024x576.jpg)

[数据库](https://thenewstack.io/introduction-to-databases/)中的表构成了数据驱动应用程序的基础。处理一个混乱的模式，其中充满了令人困惑的名称和数据缺陷，是一项挑战。在名称清晰且数据干净的表上构建可以简化您的选择。

在本文中，我将通过为表命名并通过规范化和约束避免数据错误，为高效的[SQL](https://www.oracle.com/database/technologies/appdev/sql.html?source=:ex:pw:::::TNS_SQL_FEB25_A&SC=:ex:pw:::::TNS_SQL_FEB25_A&pcode=)编写奠定基础。

本系列的第二部分将介绍如何构建SQL以使其更易于阅读和调试。因此，让我们首先了解如何奠定基础。

## 选择好名称

好的表名清晰简洁。应用程序中核心表的名称将是单词名词。这些映射到相应的业务概念。例如，`customers`、`payments`和`invoices`。这些表的子表使用上下文扩展父表名称，例如`customer_addresses`和`invoice_items`。

遗憾的是，命名数据库对象是一种难得的奢侈。一旦创建表或列，其名称就固定了。虽然您可以重命名它们，但您必须同时将所有代码更改为新名称。在大型代码库中，这是不切实际的。

那么，如果您正在使用一个充满神秘名称的模式，该怎么办？您是否永远被困住了？

好消息是有一些技巧可以用来阐明令人困惑的名称：

- 使用视图进行虚拟重命名。
- 添加模式元数据。

视图是存储的查询。您可以使用它们为表或列提供更易于理解的名称。例如，此视图清楚地表明表`cust_adrs`存储客户地址及其列的目的：

```sql
create view customer_addresses as
select c_id customer_id, a_id address_id, st start_date, en end_date
from cust_adrs;
```

然后，您可以像使用常规表一样使用视图。假设您只在视图中提供新的别名——即，唯一的SQL子句是`select`和`from`，并且`select`没有表达式——访问视图与使用表相同。随着时间的推移，您可以将代码转移到使用名称更好的视图。

但这需要时间。在您仍在使用原始不透明名称的同时，将有一段较长的时期。添加元数据可以帮助为此提供上下文。

表和列注释（描述对象的自由格式文本）是一种广泛支持的方法。

[Oracle 数据库 23ai](https://www.oracle.com/database/?source=:ex:pw:::::TNS_SQL_FEB25_B&SC=:ex:pw:::::TNS_SQL_FEB25_B&pcode=)通过[模式注释](https://blogs.oracle.com/coretec/post/annotations-the-new-metadata-in-23c?source=:ex:pw:::::TNS_SQL_FEB25_C&SC=:ex:pw:::::TNS_SQL_FEB25_C&pcode=)扩展了这一概念，您可以使用[键值对](https://thenewstack.io/how-to-document-database-objects-with-annotations)来记录您的表、视图、列和索引。例如，这些语句使用描述性显示值注释表`cust_adrs`及其列`c_id`的不清晰名称：

```sql
alter table cust_adrs modify ( c_id annotations ( display 'Customer ID' ) );
alter table cust_adrs annotations ( display 'Customer Addresses' );
```

您可以通过查询`[dba|all|user]_annotations_usage`视图来查看注释：

```sql
select object_name, column_name, annotation_name, annotation_value
from user_annotations_usage
where object_name = 'CUST_ADRS';
```

| OBJECT_NAME | COLUMN_NAME | ANNOTATION_NAME | ANNOTATION_VALUE |
|---|---|---|---|
| CUST_ADRS | <null> | DISPLAY | Customer Addresses |
| CUST_ADRS | C_ID | DISPLAY | Customer ID |

使用清晰的名称是构建良好基础的第一步。下一步是有效地构建您的表。

## 规范化您的模式

数据库规范化是从表中删除冗余信息的过程。这避免了数据重复，并使某些类型的数据错误成为不可能。

使用规范化数据意味着您将花费更少的时间来处理数据质量问题，例如[查找和删除重复行](https://blogs.oracle.com/sql/post/how-to-find-and-delete-duplicate-rows-with-sql?source=:ex:pw:::::TNS_SQL_FEB25_D&SC=:ex:pw:::::TNS_SQL_FEB25_D&pcode=) 。这使您可以腾出更多时间来执行更有效率的任务，例如构建新功能。

规范化过程定义了一系列范式。这些是表必须符合才能达到该规范化级别的规则。前三种范式是：
**第一范式 (1NF):** 每一行和每一列都存储单个值，并且没有重复的行。**第二范式 (2NF):** 没有依赖于主键或唯一键一部分的列。**第三范式 (3NF):** 没有依赖于非主键或唯一键一部分的列。

虽然存在更高的范式，但这些与重叠键和多个多对多关系有关。在实践中这些很少见。确保您的表符合 3NF 将涵盖您处理的大多数情况。

一个很好的检查表是否至少规范化为 3NF 的方法是询问：

*“如果我更新表中的一列，是否意味着我必须同时更新其他列？”*

如果答案是肯定的，那么您几乎肯定违反了某种范式。要解决此问题，请将相关列拆分为新表或将其完全删除。

例如，假设您正在构建[一个答题应用程序](https://thenewstack.io/how-to-build-a-quiz-app-with-nuxt-and-xata)。当玩家提交答案时，您希望记录他们开始、完成和完成测验所用的时间，以及他们的答案。这将生成如下表：

```sql
create table quiz_answers (
  quiz_id integer,
  user_id integer,
  answer clob,
  start_time timestamp,
  end_time timestamp,
  time_taken interval day to second,
  primary key (quiz_id, user_id)
);
```

但是非键值之间存在关系：`time_taken = end_time – start_time`。更改这三列中的任何一列都意味着您还必须更改至少另外两列中的一列。通过从答案表中删除其中一列来避免这种不一致性。

请注意，更新测试存在一个例外。如果您更改表的主键或其唯一约束之一中的所有列，则会出现这种情况。在这种情况下，您正在更改行的标识符，因此其他值也可能会发生更改。

与糟糕的名称一样，未规范化的表在现有应用程序中难以更改。从一开始就规范化您的数据可以避免您处理垃圾数据。

但是，仅规范化是不够的。为了保持数据的清洁，您还应该创建约束。

## 创建适当的约束

[数据库约束](https://docs.oracle.com/en/database/oracle/oracle-database/23/sqlrf/constraint.html?source=:ex:pw:::::TNS_SQL_FEB25_E&SC=:ex:pw:::::TNS_SQL_FEB25_E&pcode=)强制执行数据规则。数据库确保所有数据都符合这些规则。如果没有约束，数据错误就会潜入，这会导致客户对您的应用程序失去信心。查找和修复这些错误非常耗时。从一开始就创建约束可以避免这种痛苦。

主要的约束包括：

**主键：** 确保值是强制性和唯一的。一个表只能有一个主键。**唯一约束：** 与主键类似，唯一约束阻止您存储重复值。与主键不同，您可以在唯一列中存储空值，并且一个表可以有多个唯一约束。**外键：** 定义父子关系。外键指向子表中的列到父表中的主键或唯一约束。有了这个，您就不能拥有孤立的行。**非空约束：** 确保您只能在列中存储非空值，即它们是强制性的。**检查约束：** 验证对于每一行，条件为真或未知。

定义这些约束有助于巩固规范化奠定的基础。例如，主键或唯一约束对于在 1NF 中强制执行“无重复行”规则是必要的。

如果您发现自己正在使用未规范化的数据，约束也可以提供帮助。在讨论规范化时，我们看到了如何存储测验答案的开始时间、结束时间和持续时间会导致不一致。虽然删除其中一列是最佳解决方案，但这在长期运行的应用程序中可能不切实际。

相反，您可以通过添加此检查约束来确保所有数据都符合公式：

```sql
alter table quiz_answers
add constraint quan_answer_time_c
check ( (end_time – start_time) = time_taken );
```

一旦到位，违反此规则的新数据将被拒绝。不幸的是，现有数据可能存在此规则为假的情况。如果是这样，添加约束将失败，您将需要花费大量时间来修复它。幸运的是，您可以使用一个技巧来阻止更多无效数据进入：

创建未验证的约束。

这些忽略现有数据，并且仅将规则应用于新数据。在 Oracle 数据库中，使用以下方法执行此操作：

```sql
alter table ... add constraint ... novalidate;
```

虽然您仍然应该清理现有数据，但您可以确保不会出现新的错误。

## 建立坚实的基础

使用命名不当的表和无效的数据意味着要花费时间来解读和纠正它们；这会降低您的生产力。
选择好的名称、规范化您的表格和创建约束，可以让您在[编写SQL](https://roadmap.sh/sql)时拥有坚实的基础。有了这些基础，您可以将注意力转向有效地构建您的SQL。敬请关注本系列的第二篇文章，其中包含一些技巧和窍门来帮助您做到这一点。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)  技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。