
<!--
title: SQL的未来：会话式解决问题
cover: https://cdn.thenewstack.io/media/2024/04/39c095b8-getty-images-umbdzvnab-q-unsplash.jpg
-->

借助 JSON 和 CTE 等现代 SQL 功能，大型语言模型可以成为帮助加速学习和工作的“推理伙伴”。

> 译自 [The Future of SQL: Conversational Hands-on Problem Solving](https://thenewstack.io/the-future-of-sql-conversational-hands-on-problem-solving/)，作者 Jon Udell。


如果你像我几年前一样，在长时间离开后重返 SQL，那么有[重要的变更](https://modern-sql.com/)需要了解。首先，JSON。现在，许多面向 SQL 的数据库都支持 [JSON 列](https://thenewstack.io/why-and-how-you-should-manage-json-with-sql/)，用于任意树形结构的数据。其次，[通用表表达式](https://thenewstack.io/how-to-make-sql-easier-to-understand-test-and-maintain/) (CTE)，你可以使用它将复杂查询表示为一个步骤管道，这些步骤易于理解和验证。

JSON 特性可能会令人困惑，例如，在 Steampipe 查询中，如下所示，它隐式地将表 [github_my_gist](https://hub.steampipe.io/plugins/turbot/github/tables/github_my_gist) 与其 JSON 列 files 的扩展名连接。

```sql
select
  file ->> 'language' as language,
  count(*)
from
  github_my_gist g,
  jsonb_array_elements(g.files) file
group by
  language
order by
  count desc;
```

*示例 A*

该查询按语言统计 GitHub gist，并生成如下输出。

```sql
| language    | count |
|-------------|-------|
| Python      | 15    |
| Markdown    | 34    |
| JavaScript  | 7     |
| null        | 7     |
```

以下是生成相同结果的查询的不同版本。

```sql
-- cte 1 to unnest the json
 
with expanded_files as (
    select
        g.id as gist_id,
        jsonb_array_elements(g.files) AS file
    from
        github_my_gist g
),
 
-- sample cte 1 output
 
-- | gist_id | file                         |
-- |---------|------------------------------|
-- | 1       | {"language": "Python"}       |
-- | 2       | {"language": "Markdown"}     |
-- | 3       | {"language": "JavaScript"}   |
-- | 4       | {"language": "Python"}       |
 
 
-- cte 2 to extract the language
 
languages AS (
    select
        file ->> 'language' as language
    from
        expanded_files
)
 
-- sample cte 2 output
 
-- | language    |
-- |-------------|
-- | Python      |
-- | Markdown    |
-- | JavaScript  |
-- | Python      |
 
-- final phase to count languages
 
select
    language,
    count(*) as count
from
    languages
group by
    language
order by
    count desc;
 
-- sample final output
 
-- | Python     | 2 |
-- | Markdown   | 1 |
-- | JavaScript | 1 |
```

*示例 B*


## 专业水平

如果您精通返回集的 JSON 函数（如 Postgres 的 jsonb_array_elements，它会将 JSON 列表转换成一组行），并且如果您能够想象这种转换如何与连接进行交互，您可以非常简洁地编写强大的查询，如示例 A 所示。

这种表达方式对专家来说很好，但新手可能难以在脑子里还原变换的隐藏步骤。我所说的“新手”并不是初学者，而是对于这种学科组合尚未成为专家的人（顺便说一下，虽然我在 SQL 的这个层面上已经参与了很多年了，但我依然是新手）。

从这个角度来看，你可能希望像演示 B 中那样详细说明这些步骤。创建演示 B 的版本是我在我们的支持渠道中所做的事情，并且希望更轻松地完成。所以我为此创建了一个简单的 GPT——当我说“

由于已分解为可检查步骤的管道，展示 B 更易于调试、放心地使用和安全地修改。然后可以将其折叠为展示 A，这可能更有效，但并不一定是真的。

你甚至可以提供这两个版本，以便专家和非专家都能通过他们首选的透镜观看。可以说，这是可访问性的另一种形式，以及我们对可访问性所指的一切。

以下是对此 GPT 的[提示](https://gist.github.com/judell/9341d7210d46fe269fdb024a2c3b70c4)。我用它来询问给定存储库的问题模板的名称，给定此 [schema](https://hub.steampipe.io/plugins/turbot/github/tables/github_repository#inspect) 和类似这样的 issue_templates 列：

```sql
+------------------------------------------------------------------------------------------------------------------
| issue_templates
+------------------------------------------------------------------------------------------------------------------
| [
|     {
|         "body": "**Describe the bug**\nA clear and concise description of what the bug is.\n\n**Steampipe version
|         "name": "Bug report",
|         "about": "Create a report to help us improve",
|         "title": "",
|         "filename": "bug_report.md"
|     },
|     {
|         "body": "**Is your feature request related to a problem? Please describe.**\nA clear and concise descript
|         "name": "Feature request",
|         "about": "Suggest an idea for this project",
|         "title": "",
|         "filename": "feature_request.md"
|     }
| ]
+------------------------------------------------------------------------------------------------------------------

```

在这种情况下，我从字面上仅仅请求针对特定仓库列出问题模板名称的查询（根据上述）。以下是生成的（并且经过记录的）查询的简洁版本。

```sql
SELECT
  template ->> 'name' AS template_name
FROM
  github_repository,
  jsonb_array_elements(issue_templates) AS template
WHERE
  full_name = 'your-repository-full-name';  -- Replace 'your-repository-full-name' with the actual full name of your repository
```

这是扩展版本。

```sql
-- CTE to expand the JSON array of templates
WITH expanded_templates AS (
    SELECT
        r.id AS repo_id,
        jsonb_array_elements(r.issue_templates) AS template
    FROM
        github_repository r
    WHERE
        r.full_name = 'your-repository-full-name'  -- Replace 'your-repository-full-name' with the actual full name of your repository
),
 
-- Sample data after CTE 1
-- | repo_id | template                                |
-- |---------|-----------------------------------------|
-- | 1       | {"name": "Bug report", ...}             |
-- | 1       | {"name": "Feature request", ...}        |
 
-- CTE to extract the template names
template_names AS (
    SELECT
        template -&gt;&gt; 'name' AS template_name
    FROM
        expanded_templates
)
 
-- Sample data after CTE 2
-- | template_name    |
-- |------------------|
-- | Bug report       |
-- | Feature request  |
 
-- Final selection
SELECT
    template_name
FROM
    template_names;
```

对于此类简单的案例，此方法效果很好，但对于更复杂的情况（如[本例](https://hub.steampipe.io/plugins/turbot/aws/tables/aws_s3_bucket#list-bucket-policy-statements-that-grant-external-access-for-each-bucket)）则不然，该方法查找具有授予外部访问权限的策略的 S3 存储桶。在这种情况中，您不仅仅需要 Postgres 知识：您还需要了解 AWS 策略的构建方式，然后您需要弄清楚如何使用 Postgres 联合和 JSONB 运算符对其进行查询。如果 GPT 最初未能为您完成此操作，那么故事并未结束。在提供结果说明以及表架构和必需的 JSON 列示例后，您为与已经看到比您多得多的 SQL 模式和 AWS 策略模式的实体对话设置了上下文。

## 对话式实践学习

我不断回到合唱解释的主题（[#4 在我的最佳实践列表中](https://thenewstack.io/7-guiding-principles-for-working-with-llms/))，它在 SQL 领域尤其相关，在该领域有许多编写查询的方法。

探索各种可能性曾经是艰苦的、耗时的和难以证明的。现在，证明*不*这样做变得困难；优化（有时是重大优化）可以而且确实会出现。

可以说，理解 SQL 一直需要一种外星智能，更不用说[查询计划程序(query planners)](https://blog.jonudell.net/2023/11/28/puzzling-over-the-postgres-query-planner-with-llms/)。在与 LLM 的对话中，我们现在可以快速探索可能性空间，并更轻松地评估不同方法的执行情况。我还能如何编写此查询？我为什么要这样做？数据库将如何处理它？（也许您可以流利地阅读和理解查询计划，但我不能，我非常感谢我所能获得的所有帮助。）

我经常向 LLM 提出此类问题，并收到不是理论上的答案，而是我的查询版本——使用我的数据——我可以立即尝试，并导致我可以同样廉价地探索的后续问题。

> 可以说，理解 SQL 一直需要一种外星智能，更不用说查询计划程序。

在我对最新 GPT 的一次测试中，我想到了将 Postgres 惯用法翻译成 SQLite。Postgres 和 SQLite JSON 模式截然不同。在你的脑海中同时持有这两组模式，并在它们之间进行心理映射，这仅仅是达到目的的一种手段。如果我正在考虑是否可行切换数据库，我不想深入了解最终可能永远不需要的 SQLite 模式。我只想知道什么是可能的。

GPT 名义上是关于 Postgres 的，它很乐意提供帮助。你真正用这些 GPT 所做的就是设置一个初始上下文。在任何时候，您都可以将对话引导到您希望它去的地方。

以下是统计语言中 gist 的查询的 SQLite 对应项。

```sql
select
  json_extract(value, '$.language') as language,
  count(*) as count
from
  github_my_gist,
  json_each(github_my_gist.files)
group by
  language
order by
  count desc;
```

ChatGPT 立即给出了答案，我进行了测试，它确实有效。当然，我随后想展开这个紧凑版本，以便逐步可视化查询。据我所知，事实证明你无法消除连接。以下是 ChatGPT 的解释：

> **json_each**：这是 SQLite 中与 `jsonb_array_elements` 等效的元素，但它的功能略有不同。它必须在 `FROM` 子句中使用，并且通常直接与从中提取数据的表结合使用，因为 SQLite 的查询计划程序对于复杂的 JSON 操作而言灵活性较低。

这是否完全准确？我不知道，但这与我所看到的行为相符，当然，这是 ChatGPT 使我毫不费力地设想出来的行为。这种会话式的动手学习是我用来消除围绕 AI 的噪音和炒作的信号。

最终，我不关心 SQL 或 JSON；我想提升认知能力，以便解决在数据获取和分析中出现的问题。我没有忽视体现于最强大的 LLM 中的黑暗模式，但我无法忽视它们所能提供的提升。许多类型的工作要求我们大规模地对信息进行推理，而不仅仅是对你的代码和文档进行推理，尽管这是我们这里的重点。我不想让放射科医生仅仅依赖 AI，但我确实希望他们咨询比他们见过的 X 射线和诊断结果多得多的实体。在信息技术领域，我希望代码和数据处理人员尽可能最好地利用这些新的推理合作伙伴。
