<!--
title: 如何使用注释记录数据库对象
cover: https://cdn.thenewstack.io/media/2024/02/f269d59f-database-object-annotation-1024x576.png
-->

不要再试图通过使用结构化的数据库模式文档来猜测数据库列的存在原因。

> 译自 [How to Document Database Objects with Annotations](https://thenewstack.io/how-to-document-database-objects-with-annotations/)，作者 Chris Saxon 是Oracle数据库的开发者倡导者，他的工作是帮助您充分利用它并享受SQL的乐趣。您可以在Twitter上找到他，账号为@ChrisRSaxon，也可以在他的博客"All Things SQL"上找到他。

每个[数据库](https://thenewstack.io/data/)都有它们，一组列 —— 或者甚至整个表 —— 没有人能解释它们存在的原因。关于它们的任何文档（如果曾经存在过）都已经遗失在您公司的wiki中。

为了帮助您理解您的模式，最好记录在数据库内部的注释，理想情况下应该直接位于列和表旁边。这将允许您在工具中查看这些细节或通过查询数据字典来查看。

大多数数据库系统都允许您使用对象注释来实现这一点。例如，在[Oracle数据库](https://www.oracle.com/database/?source=:ex:pw:::::TheNewStack_A&SC=:ex:pw:::::TheNewStack_A&pcode=)中，您可以使用`COMMENT`命令：

```sql
create table games ( 
  game_id         int primary key,
  home_team_id    int, 
  away_team_id    int, 
  game_datetime   timestamp,
  insert_datetime timestamp
);

comment on column games.insert_datetime
  is 'Audit log of when each row was inserted';
comment on table games 
  is 'Scheduled matches between teams';
```

然后，这些信息会出现在相应对象的注释字典视图中：

```sql
select comments from user_tab_comments
where  table_name = 'GAMES';

COMMENTS                           
Scheduled matches between teams 

select column_name, comments from user_col_comments
where  table_name = 'GAMES'
and    comments is not null;

COLUMN_NAME        COMMENTS                                   
INSERT_DATETIME    Audit log of when each row was inserted
```

这是帮助其他开发人员和数据库管理员（DBA）理解您的模式的好方法。

但是注释只是一个字符串。如果要存储有关对象的许多属性，则使用它们会很麻烦。

例如，数据库表通常包括一个`INSERT_DATETIME`列。这些列应该都是：

- **系统生成的**：数据库应该使用列默认值提供值。
- **强制性的**：不允许为空。
- **仅插入**：这些值永远不应更新。

这些信息涉及您使用数据的意图：不仅仅是为什么存在这些列，而是如何与它们交互。记录这些细节有助于将来的[维护人员](https://thenewstack.io/open-source-needs-maintainers-but-how-can-they-get-paid/)理解如何在应用程序中使用这些数据。

您可以将这些属性与注释中的其他注释一起存储。问题是您要使用哪种格式？[JSON](https://thenewstack.io/why-and-how-you-should-manage-json-with-sql/)？XML？分隔键值对？

无论您选择哪种格式，您都需要所有未来的维护人员都遵循相同的格式。对于长期存活的系统来说，这变得具有挑战性。如果数据库本身对注释强制执行一些结构将会更好。

Oracle数据库23c通过[添加使用注释](https://blogs.oracle.com/coretec/post/annotations-the-new-metadata-in-23c?source=:ex:pw:::::TheNewStack_B&SC=:ex:pw:::::TheNewStack_B&pcode=)来解决了这个问题。

## 通过注释改进数据库文档

注释是带有可选值的键。您可以使用它们记录有关所讨论对象的任何元数据。

例如，下面的内容使用上述列出的属性注释了INSERT_DATETIME列：

```sql
alter table games modify (
  insert_datetime annotations ( 
    mandatory, 
    system_generated, 
    allowed_writes '["insert"]',
    description 'Audit log of when each row was inserted'
  )
);
```

你可能会想为什么allowed_writes使用了一个JSON数组，即使只有一个值。为什么不只使用字符串“insert”？

您可能希望将此注释应用于许多列。这些列可能还支持更新或删除。将它们全部设置为数组比混合使用数组和普通字符串更易于处理。

添加了注释后，您可以在`*_usage_annotations`视图中查看它们：

```sql
COLUMN_NAME        ANNOTATION_NAME     ANNOTATION_VALUE                           
INSERT_DATETIME    MANDATORY           <null>                                     
INSERT_DATETIME    SYSTEM_GENERATED    <null>                                     
INSERT_DATETIME    ALLOWED_WRITES      ["insert"]                                 
INSERT_DATETIME    DESCRIPTION         Audit log of when each row was inserted   
```

这些视图显示了所有对象类型的注释。这意味着它们都可以在一个位置访问，这样如果您想要编程访问注释以生成单独的文档，就变得非常简单。

注释的键值结构使其比注释更强大。

但是，当您将它们用于常见值时，仍然存在挑战。模式中的大多数或所有表都将具有一个`INSERT_DATETIME`列。这些列应该都具有相同的注释。随着时间的推移，试图保持所有这些同步是很困难的！

与其将注释复制到每个`INSERT_DATETIME`列中，不如在共享对象中定义一次，然后将此对象应用于所有需要的列。这确保它们都具有相同的属性。

问题是：如何做到这一点？

## 使用域标准化注释

Oracle数据库23c通过[添加使用域](https://blogs.oracle.com/coretec/post/less-coding-with-sql-domains-in-23c?source=:ex:pw:::::TheNewStack_C&SC=:ex:pw:::::TheNewStack_C&pcode=)来解决了这个问题。这些域是在[SQL标准](https://thenewstack.io/how-to-make-sql-easier-to-understand-test-and-maintain/)中构建的。它们通过可选属性扩展了现有的数据类型，包括：

- 约束
- 默认值
- 注释
- …

使用`CREATE DOMAIN`语句来创建一个。这将创建一个带有上述注释的`INSERT_DATETIME`域：

```sql
create domain insert_timestamp as 
  timestamp 
  annotations ( 
    mandatory, 
    system_generated, 
    allowed_writes '["insert"]',
    description 'Audit log of when each row was inserted'
  );
```

然后，在创建或修改表时，可以将此域应用于列。通过在数据类型之后指定域，或者使用域子句替代数据类型，来执行此操作。这将注释从域复制到表列：

```sql

alter table games
  modify ( 
    insert_datetime domain insert_timestamp 
  );

create table teams ( 
  team_id          int, 
  team_name        varchar2(100), 
  insert_datetime domain insert_timestamp
);

select object_name, column_name, annotation_name, annotation_value 
from   user_annotations_usage
where  'INSERT_TIMESTAMP' in ( object_name, domain_name );

OBJECT_NAME         COLUMN_NAME         ANNOTATION_NAME     ANNOTATION_VALUE                           
INSERT_TIMESTAMP    INSERT_TIMESTAMP    MANDATORY           <null>                                     
INSERT_TIMESTAMP    INSERT_TIMESTAMP    SYSTEM_GENERATED    <null>                                     
INSERT_TIMESTAMP    INSERT_TIMESTAMP    ALLOWED_WRITES      ["insert"]                                 
INSERT_TIMESTAMP    INSERT_TIMESTAMP    DESCRIPTION         Audit log of when each row was inserted    
GAMES               INSERT_DATETIME     MANDATORY           <null>                                     
GAMES               INSERT_DATETIME     SYSTEM_GENERATED    <null>                                     
GAMES               INSERT_DATETIME     ALLOWED_WRITES      ["insert"]                                 
GAMES               INSERT_DATETIME     DESCRIPTION         Audit log of when each row was inserted    
TEAMS               INSERT_DATETIME     MANDATORY           <null>                                     
TEAMS               INSERT_DATETIME     SYSTEM_GENERATED    <null>                                     
TEAMS               INSERT_DATETIME     ALLOWED_WRITES      ["insert"]                                 
TEAMS               INSERT_DATETIME     DESCRIPTION         Audit log of when each row was inserted
```

要将域链接到列，它们都必须具有相同的基本数据类型。您只能将`INSERT_DATETIME`域与`timestamp`列关联，不能与`date`、`number`、`varchar2`等关联。

有了这个集中的定义，您可以确信使用域的所有列都具有相同的注释。即使将来要更改它们，也适用。

例如，您可能希望指定允许在插入时间戳上执行过滤和排序操作，这意味着可以安全地在`WHERE`和`ORDER BY`子句中使用这些列。

您可以修改域以添加这些注释：

```sql
alter domain insert_timestamp 
  annotations ( allowed_reads '["where", "order by"]');
```

数据库会自动将这些应用于相应的数据库列：

```sql

select object_name, object_type, column_name, domain_name, annotation_value 
from   user_annotations_usage
where  annotation_name = 'ALLOWED_READS'
order  by object_type, object_name;

OBJECT_NAME         OBJECT_TYPE    COLUMN_NAME        DOMAIN_NAME         ANNOTATION_VALUE         
INSERT_TIMESTAMP    DOMAIN         <null>             <null>              ["where", "order by"]    
GAMES               TABLE          INSERT_DATETIME    INSERT_TIMESTAMP    ["where", "order by"]    
TEAMS               TABLE          INSERT_DATETIME    INSERT_TIMESTAMP    ["where", "order by"]
```

## 文档数据意图

数据库模式可能会很复杂。理解每个部分的目的可能会有些棘手。通过在模式本身中记录这些信息，您可以帮助所有人了解每个部分的如何和为什么。

注释是记录这些细节的常用方式。它们的非结构化性质限制了它们的有用性。[Oracle数据库23c](https://www.oracle.com/database/23c/?source=:ex:pw:::::TheNewStack_D&SC=:ex:pw:::::TheNewStack_D&pcode=)中的注释的键值结构赋予了您更大的权力。

在Oracle数据库23c中，您还可以定义域。这些为您提供了一个用于常见数据值的单一定义点，例如插入时间戳。

结合域和注释，您可以简单地描述数据。它们共同形成了一种新的SQL语句类别：数据意图语言（DIL）。

随着模式的增长，使用这些DIL语句将是帮助其他开发人员理解如何以及为什么使用它的关键。

帮助您的同行开发人员和数据库管理员：使用域和注释记录您的数据库！
