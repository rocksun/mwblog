<!--
title: 学以致用：语言模型在重塑教育中的作用
cover: https://cdn.thenewstack.io/media/2024/01/4019b8b3-kenny-eliason-zfso6bnzjtw-unsplash-1024x637.jpg
-->

实现动手自主学习的途径是通过大型语言模型（LLM）。Jon Udell 展示了教育科技行业如何利用人工智能。

> 译自 [Learn by Doing: How LLMs Should Reshape Education](https://thenewstack.io/learn-by-doing-how-llms-should-reshape-education/)，作者 Jon Udell。

今天，我的朋友[格雷格·威尔逊(Greg Wilson)](https://third-bit.com/)在将 tidyverse/Pandas 习语翻译成 SQL 时，问我以下问题:

好吧，我的 SQL 哪里错了?

```sql
drop table if exists person;
create table person(
 ident integer not null primary key,
 name text not null
);
 
drop table if exists job;
create table job(
 ident integer not null primary key,
 name text not null
);
 
drop table if exists did;
create table did(
 person_id integer not null,
 job_id integer not null
);
 
insert into person values (1, "Alice"), (2, "Bob");
insert into job values (20, "cook"), (30, "clean");
insert into did values(1, 20), (2, 20), (1, 30);
 
select person.name, job.name, count(*)
from person inner join did inner join job
on person.ident = did.person_id and did.job_id = job.ident
group by person.ident, job.ident
order by person.ident, job.ident;
```

结果中没有显示 (Bob, clean) 的值为 0。为什么？

我将这个问题转发给了我的首席助手 ChatGPT，它给出了以下回答:

**ChatGPT**: 您的 SQL 脚本基本没有问题，但是最后的查询语句中联结表的方式有点问题。让我详细说明一下:

表的创建和插入数据: 您正确地创建了 person、job 和 did 这三张表，并向其中插入了数据。这部分看起来没有问题。

最后的联合查询: 您试图将这些表的数据组合起来，以显示每个人做了哪些工作。然而，您使用 INNER JOIN 写的查询不会包括一个人没有工作的组合(如您示例中的 Bob 和“clean”)。这是因为 INNER JOIN 只包括两张表中都有匹配的行。

为了包括所有人和工作的组合，即使一个人没有做某项工作，您应该使用 CROSS JOIN 来创建 person 和 job 的笛卡尔积，然后与 did 表做 LEFT JOIN。这样，您可以得到所有组合，并统计出现的次数。

下面是更正后的查询:

```sql
SELECT person.name， job.name， COUNT(did.person_id) as job_count
FROM person
CROSS JOIN job
LEFT JOIN did ON person.ident = did.person_id AND job.ident = did.job_id
GROUP BY person.name， job.name
ORDER BY person.name， job.name;
```

这个查询会列出每种人和工作的组合，并统计每个人做每项工作的次数。对于 did 表中没有的组合(如您示例中的 Bob 和“clean”)，会显示 0 次。

## 准则 2: 永远不要相信，要验证

遵循准则 2(见 [7 个指导语言模型工作的原则](https://yylives.cc/2024/01/22/7-guiding-principles-for-working-with-llms/))，我下一步的行动是:

**Jon**: 听起起来不错，请写一个测试来证明它可行。

接下来发生的事情我之前提到过，在《[语言模型如何帮助一个网站改版](https://yylives.cc/2023/09/16/how-large-language-models-assisted-a-website-makeover/)》一文中: ChatGPT 编写并运行了测试。如果您还没有看到这种情况发生，那简直令人难以置信，我感觉许多人还没有看到过。

**ChatGPT**: 为了测试 SQL 查询，我将设置一个数据库环境的模拟，然后执行查询。这将演示查询在处理您的需求方面的正确性。让我们进行测试:

创建表: 我将根据您的脚本创建 person、job 和 did 表。插入数据: 我将插入您提供的数据到这些表中。执行查询: 我将运行更正后的查询，以显示它如何处理人和工作的组合，包括一个人没有工作记录的情况。

让我们从这个测试开始:

```python
import sqlite3
import pandas as pd
 
# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')
 
# Create tables
create_statements = [
    '''
    CREATE TABLE person (
        ident INTEGER NOT NULL PRIMARY KEY,
        name TEXT NOT NULL
    );
    ''',
    '''
    CREATE TABLE job (
        ident INTEGER NOT NULL PRIMARY KEY,
        name TEXT NOT NULL
    );
    ''',
    '''
    CREATE TABLE did (
        person_id INTEGER NOT NULL,
        job_id INTEGER NOT NULL
    );
    '''
]
 
for create_statement in create_statements:
    conn.execute(create_statement)
 
# Insert data
person_data = [(1, "Alice"), (2, "Bob")]
job_data = [(20, "cook"), (30, "clean")]
did_data = [(1, 20), (2, 20), (1, 30)]
 
conn.executemany('INSERT INTO person VALUES (?, ?);', person_data)
conn.executemany('INSERT INTO job VALUES (?, ?);', job_data)
conn.executemany('INSERT INTO did VALUES (?, ?);', did_data)
 
# Query to combine the tables
query = '''
SELECT person.name AS PersonName, job.name AS JobName, COUNT(did.person_id) AS JobCount
FROM person
CROSS JOIN job
LEFT JOIN did ON person.ident = did.person_id AND job.ident = did.job_id
GROUP BY person.name, job.name
ORDER BY person.name, job.name;
'''
 
# Execute the query
result = pd.read_sql_query(query, conn)
conn.close()
 
result
 
  PersonName JobName  JobCount
0      Alice   clean         1
1      Alice    cook         1
2        Bob   clean         0
3        Bob    cook         1  
```

作为跟进，我要求提供一个以CTEs（通用表达式）管道形式编写的查询版本，并仅提供查询的 `cross join` 组件的输出。

**ChatGPT**：要显示PersonJobCombos CTE的输出，我们需要仅运行查询的那部分。该CTE生成所有可能的人员和工作组合，而不考虑一个人是否实际上做过工作。让我们分别执行此CTE以查看其输出。

```python
# Reconnect to the in-memory SQLite database
conn = sqlite3.connect(':memory:')
 
# Recreate tables and insert data as before
for create_statement in create_statements:
    conn.execute(create_statement)
 
conn.executemany('INSERT INTO person VALUES (?, ?);', person_data)
conn.executemany('INSERT INTO job VALUES (?, ?);', job_data)
conn.executemany('INSERT INTO did VALUES (?, ?);', did_data)
 
# Query for PersonJobCombos CTE
person_job_combos_query = '''
WITH PersonJobCombos AS (
    SELECT person.ident AS PersonID, person.name AS PersonName, job.ident AS JobID, job.name AS JobName
    FROM person
    CROSS JOIN job
)
SELECT * FROM PersonJobCombos;
 
# Execute the PersonJobCombos CTE query
person_job_combos_result = pd.read_sql_query(person_job_combos_query, conn)
conn.close()
 
person_job_combos_result
 
PersonID PersonName  JobID JobName
0         1      Alice     20    cook
1         1      Alice     30   clean
2         2        Bob     20    cook
3         2        Bob     30   clean
```

PersonJobCombos CTE的输出显示了人员和工作的所有可能组合：

Alice与“cook”和“clean”都配对。

Bob也与“cook”和“clean”配对。

这展示了人员和工作表的笛卡尔积，创建了每个人与每个工作的组合，而不考虑他们是否实际上做过这份工作。

## 规则7：通过实践学习

现在这里有一个尴尬的坦白。在我上一份工作中，我写了很多SQL，在我当前的工作中我也写了很多。在上一份工作中，我从未发现过对 `cross join` 的需求。在使用Steampipe时，我在许多示例查询中遇到了这种习语，但从未以这种简单的形式出现过。Steampipe查询通常会将 `cross join` 与返回集的JSONB函数结合使用，以我难以想象的方式。在这些情况下，我会借助CTE管道以一系列简单的步骤构建查询，每个步骤都执行一项简单的转换。

我把规则7放在最后，因为它感觉最重要。在这里，例如，我并没有刻意去学习交叉连接，我只是想知道如何报告Bob/clean对的值为0。由于交叉连接是解决方案的有机部分，我可能会记住并能够参考这个例子。我希望在面对类似问题时会想到它。

这次练习中我可能学到的不仅仅是这些。我碰巧知道如何从Python内部使用SQLite，但如果我不知道，ChatGPT将会默默地教给我这种方法，并提供另一个有用的示例供我参考。

## 重新定义教育

我们一直需要这种按需学习的方式，现在它正在变得可能。在这个例子中，我们看到了一个tidyverse/Pandas从业者如何在SQL中展现熟悉的习语。作为SQL从业者，我可以反其道而行，了解熟悉的SQL习语在R或Python中的运用。实际上，我刚刚做到了这一点，而ChatGPT不仅能够编写代码，而且能够运行它——目前仅支持Python（尚不支持R），但似乎不可避免的是LLMs将连接到多个引擎以执行各种分析任务。

现在让我们想象一下一个可能激发Greg的模式和查询的课堂练习。老师可能会这样描述这个任务：

**老师**：这些是人们可以做的工作：cook，clean。

这些是人：Alice，Bob。

这是他们做过的工作：Alice：cook，clean；Bob：cook。

展示如何使用一个或多个SQL表对这种情况建模，并以这种格式报告数据。

```bash
PersonName  JobName JobCount
Alice       clean   1
Alice       cook    1
Bob         clean   0
Bob         cook    1
```

*你应该期望ChatGPT编写、运行并迭代一个嵌入SQLite并调用必要的SQL语句的Python脚本。当你得到一个能够报告上述数据的脚本时，自己运行以进行验证，并包含该脚本。*

现在回答这个问题：SQL输出如何包括这一行？

```bash
Bob         clean   0
```

这不在数据中，它从哪里来？

术语 `cross join` 并不在视线中！学生需要检查生成的代码，然后（在LLM的帮助下！）解释为什么需要 `cross join` 以及它是如何起作用的。

一些老师现在可能愿意并能够采用这种全新的方法。许多人可能会等到它嵌入在具有保护措施的课程中，以确保学生走上正轨。但无论如何，教育领域即将迎来一场巨大的变革。

程序员和作家[Ellen Ullman](https://jonudell.net/udell/2006-10-06-a-conversation-with-ellen-ullman-about-living-close-to-the-machine.html)喜欢说程序员按照自己的形象和愿望创建系统。我们是第一批体验到我们现在都视为理所当然的生活方式的人：异步的、机器介导的、始终在线的。现在我们将是第一批体验到LLM辅助教育的人。

对于可以用Python解决的课程练习，老师和学习者生活在一个分布不均匀的未来。通向这种更均匀分布的、实现这种实际操作性学习的路径尚未被明确指引，但我希望教育工作者正在带着头灯和手电筒走在这条道路上。
