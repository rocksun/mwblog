
<!--
title: 是否使用SQL：这不是问题
cover: https://cdn.thenewstack.io/media/2025/05/ca3df6a7-to-sql-or-nosql.jpg
summary: SQL与NoSQL之争已成过去！多模型数据库融合，如MySQL、PostgreSQL和Oracle，集成JSON等NoSQL特性。原生JSON存储API简化开发，SQL/JSON实现混合查询。JSON-关系二元性更进一步，兼顾关系模型的效率和JSON文档的灵活性，解锁云原生AI时代数据处理新姿势！
-->

SQL与NoSQL之争已成过去！多模型数据库融合，如MySQL、PostgreSQL和Oracle，集成JSON等NoSQL特性。原生JSON存储API简化开发，SQL/JSON实现混合查询。JSON-关系二元性更进一步，兼顾关系模型的效率和JSON文档的灵活性，解锁云原生AI时代数据处理新姿势！

> 译自：[To SQL or Not To SQL: That Is Not the Question](https://thenewstack.io/to-sql-or-not-to-sql-that-is-not-the-question/)
> 
> 作者：Hermann Baer

SQL 和 NoSQL 之间持续的争论与关系数据库系统一样古老。自从 [Edgar F. Codd introduced](https://thenewstack.io/introduction-to-databases/) 在 1970 年引入关系数据库概念以来，数据库系统中结构和灵活性之间一直存在着深刻的张力。

SQL 数据库声称通过数十年来经验证的可靠性、强大的 [ACID](https://thenewstack.io/can-nosql-databases-be-acid-compliant/) 保证和强大的查询功能（非常适合复杂的关系数据模型）而具有优越性。 相比之下，NoSQL 数据库的支持者认为，僵化的模式无法跟上现代开发的步伐，因此它们提供了模式灵活性、简单的应用程序开发以及针对高速或非结构化数据的更好性能。

每个阵营都声称占据主导地位——SQL 具有一致性和完整性，NoSQL 具有速度和敏捷性——但现实世界的趋势是融合，因为双方都越来越多地致力于借鉴对方的特性。

## SQL 和 NoSQL：融合到多模型数据库中

MySQL、[PostgreSQL](https://roadmap.sh/postgresql-dba) 和 Oracle 等多模型数据库正处于将非关系功能集成到传统关系系统中的最前沿。 最近的创新包括向量处理、文档存储功能以及对 JSON 文档集合的支持。 这些新功能允许开发人员：

- 使用熟悉的文档 API 处理 JSON 文档
- 使用 SQL 查询和处理结构化和半结构化数据
- 将关系规范化与以文档为中心的开发相结合

## 多模型数据库支持原生文档存储 API

所有这些多模型数据库都引入了一种用于以原生和优化方式存储 JSON 数据的二进制格式。 这包括 Oracle 的 OSON 格式，该格式在 [research](https://www.vldb.org/pvldb/vol13/p3059-liu.pdf) 中显示出在增量更新的性能和效率方面优于 BSON 的优势。

对于寻求文档优先体验的开发人员，供应商提供公开原生 JSON 存储的 API，例如 MySQL 的 X DevAPI、基于 PostgreSQL 的 FerretDB 或 Oracle 的 [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention) 数据库 API。 这些 API 在关系基础设施之上提供了 NoSQL 开发的简单性。 开发人员可以享受模式灵活开发的简单性和敏捷性，而无需专用文档存储数据库。

但是，与 SQL 不同，文档存储 API 没有标准化，并且仍然是特定于供应商的。 定义通用标准的努力正在进行中，但仍处于早期阶段。

## 使用 SQL 查询 JSON

通过原生 JSON 支持，开发人员可以将文档集合视为数据库中的一等公民。 使用 ANSI SQL/JSON（在 SQL:2016 中引入），您可以提取值、展开数组、过滤文档并将 SQL 函数应用于 JSON 内容。 这通过统一的语言桥接了关系数据和半结构化数据，从而打开了利用 [power of SQL](https://thenewstack.io/3-foundational-principles-for-writing-efficient-sql) 进行分析和报告的大门。

这是一个查询电影的 JSON 集合、提取属性、按年份汇总总收入并计算每年收入份额的示例：

```sql
WITH revenue AS ( SELECT m.data.year , round(sum(JSON_VALUE(data,'$.gross' RETURNING NUMBER NULL ON ERROR NULL ON EMPTY ))/1000000) as millions FROM movies m WHERE m.data.gross IS NOT NULL GROUP BY m.data.year)SELECT year , millions , ROUND((RATIO_TO_REPORT(millions) OVER ())*100,2) pct_revenueFROM revenue rWHERE year > 2000ORDER BY year DESC;
```

此示例使用 ANSI SQL/JSON 运算符 `JSON_VALUE`
和 Oracle 简化的点表示法，这是一种直接的 SQL 风格的方式，用于从 JSON 文档中提取 JSON 标量值 (`m.data.year`
)。
开发人员提取并“关系化”存储在 JSON 文档中的属性，将此信息与关系表连接起来，并使用嵌套子查询或其他构造——他们使用任何可用的 SQL 运算符或函数来处理关系对象的方式相同。

## 将关系数据公开为 JSON 文档

相反，可以使用 JSON 集合视图将关系数据公开为 JSON 文档，从而使其可供以文档为中心的应用程序访问。 以下示例在 Oracle 的 EMP 表之上创建一个 JSON 集合视图，该表可能是为演示目的而创建的第一个关系表之一：

```sql
CREATE OR REPLACE JSON COLLECTION VIEW emp_collection AS SELECT JSON{'_id' : empno, 'employeName' : ename, 'jobRole' : job} FROM emp;
```

通过文档存储 API 使用此集合视图将返回类似于以下内容的数据：

```json
###
```
jason> db.emp_collection.findOne(){ _id: 7369, employeName: 'SMITH', jobRole: 'CLERK' }

这种双向灵活性模糊了 SQL 和 NoSQL 之间的界限，并将数据的处理方式与数据的存储方式分离。

## 超越双重访问：JSON-关系二元性

虽然原生二进制 JSON 存储、文档 API 和 SQL/JSON 功能代表着巨大的进步，但 [JSON-关系二元性](https://www.oracle.com/database/json-relational-duality/?source=:ex:pw:::::TNS_ToSQL_April25_A&SC=:ex:pw:::::TNS_ToSQL_April25_A&pcode=) 更进一步。这种新功能提供了关系型和 JSON 文档的最佳特性，而无需在两种模型之间进行权衡。

简而言之，二元性视图在内部使用高效的规范化格式（使用关系型和 JSON 结构）存储 JSON 文档。与此同时，开发人员与 JSON 文档进行交互。

![二元性视图：存储为行，公开为文档](https://cdn.thenewstack.io/media/2025/05/f2d163c7-json_dvs.jpeg)

二元性视图：存储为行，公开为文档

无论应用程序使用 REST 还是以文档为中心的 API，开发人员都可以从检索和处理单个应用程序层对象所需的所有数据的简单性中受益：JSON 文档。创建 JSON 二元性视图非常简单。与 JSON 集合视图一样，开发人员在数据库中将业务对象的对象文档模型定义为元数据。

这是一个简单的示例，它定义了一个二元性视图，用于使用 [GraphQL](https://roadmap.sh/graphql) 对会议日程进行建模。日程对象包括：

- 参会者信息
- 单个参会者的日程
- 一个或多个参会者计划参加的会话的日程表示
- 有关会话的详细信息，包括演讲者信息

```
create or replace JSON Duality view ScheduleV AS attendee { 
    _id : aid 
    name : aname 
    schedule : schedule @insert @update @delete { 
        scheduleId : schedule_id 
        sessions @unnest { 
            sessionId : sid 
            name : name 
            location : room 
            speaker @unnest { 
                speakerId : sid 
                speaker : name 
            } 
        } 
    } 
} ;
```

因此，JSON-关系二元性提供了关系模型的存储、一致性和 [效率优势](https://thenewstack.io/3-sql-writing-tips-and-tricks-to-enhance-productivity)，同时应用程序检索和操作深度嵌套的 JSON 结构。

## 两全其美

SQL 和 NoSQL 的融合使开发人员能够通过单个数据库从 JSON 文档开发的简单性和关系数据库的强大功能中受益。多模型数据库消除了选择一种范例而不是另一种范例的需要，从而占领了单一用途的 NoSQL 数据库系统市场。开发人员不必面对 SQL 和 NoSQL 系统之间的选择，也不必将自己锁定在一种编程范例中。他们可以灵活自由地为单个应用程序选择最佳方法，而不会牺牲功能。

Oracle 的 JSON-关系二元性视图超越了共存，将关系模型和文档模型的优势融合到统一的架构中。随着多模型系统的不断发展，这种方法树立了一个引人注目的先例，并且其他人可能会效仿。

*立即开始使用 JSON-关系二元性进行创新，无论是在本地使用 Oracle Database 23ai Free，还是在云端使用 OCI 上的 Oracle Autonomous Database。*