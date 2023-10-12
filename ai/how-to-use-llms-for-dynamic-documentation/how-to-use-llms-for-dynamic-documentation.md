<!-- 
# 如何利用 LLMs 动态生成文档

https://cdn.thenewstack.io/media/2023/10/cf4e813d-sigmund-vvrjjtbuuai-unsplash-1024x683.jpg
Featued image for: How to Use LLMs for Dynamic Documentation
Image via Unsplash
 -->

某些解释需要由代码作者预先编写。而其他解释或许可以由结合大型语言模型的代码阅读器实时生成。

译自[ How to Use LLMs for Dynamic Documentation](https://thenewstack.io/how-to-use-llms-for-dynamic-documentation/) 。

前几天，我重新审视了我之前编写的一个 SQL 查询，目的是将其调整适应 [GitHub 插件](https://hub.steampipe.io/plugins/turbot/github)的最新版本。尽管只做了小调整，但花费的时间比预期更长。为什么呢?因为我已经忘记该查询的工作原理了!当然，我也没有编写任何注释，写 Query 时它看起来很简单，不是吗?

下面是原始查询，它报告了一组 Steampipe 插件的最近提交(commit)。

```sql
with repos as (
  select
    name_with_owner as repo_name，
    'author-date:&gt;' || $2|| ' repo:' || name_with_owner as query
  from  
    github_search_repository
  where
    query = $1 || ' in:name'
)

select
  r.repo_name，
  c.commit -&gt; 'author' -&gt;&gt; 'name' as author，
  substring(c.commit -&gt; 'committer' -&gt;&gt; 'date' from 1 for 10) as date，
  c.commit -&gt;&gt; 'message' as message
from
  repos r
join
  github_search_commit c
on
  r.repo_name = c.repository_full_name
  and r.query = c.query
order by
  date desc
```

它的工作原理如下。如果使用参数 $1 和 $2 填入 turbot/steampipe 和 2023-10-04 的值，则 with repos CTE(公共表表达式)会运行以下查询:

```sql
select
  g.name_with_owner as repo_name，
  'turbot/steampipe in name' as query
from
  github_search_repository g 
where
  query = 'turbot/steampipe in:name'
```

[github_search_repository](https://hub.steampipe.io/plugins/turbot/github/tables/github_search_repository) 是一个由 GitHub 插件提供的表，封装了 GitHub 的[仓库搜索](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)语法。编写使用该表的 SQL 查询时，需要在 WHERE 子句中提供名为 query 的限定词，及一个表示 GitHub 仓库搜索语法的值。

目前，这个查询会返回类似下面的 208 行:

```
+---------------------------------------------------------------+-----------------------------------------------+
| repo_name                                                     | query                                         |
+---------------------------------------------------------------+-----------------------------------------------+
| turbot/steampipe-plugin-ldap                                  | author-date:&gt;2023-10-04 repo:turbot/steampipe |  
| turbot/steampipe-plugin-bitbucket                             | author-date:&gt;2023-10-04 repo:turbot/steampipe |
| turbot/steampipe-plugin-alicloud                              | author-date:&gt;2023-10-04 repo:turbot/steampipe |
...
```

`query` 列包含另一段 GitHub 搜索语法。在这里，它是另一个 Steampipe 表 [github_search_commit](https://hub.steampipe.io/plugins/turbot/github/tables/github_search_commit) 的必需限定词，该表封装了 GitHub 的[提交搜索](https://docs.github.com/search-github/searching-on-github/searching-commits)语法。下面是针对该表的独立查询示例:

```sql
select
  * 
from
  github_search_commit
where
  repository_full_name = 'steampipe-plugin-ldap'
  and query = 'author-date:&gt;2023-10-04 repo:turbot/steampipe'
```

所以，这里使用了两种不同的 query 限定词。

| 使用位置 | 表名 | 示例限定词 |
|-|-|-|  
| the with repos CTE | github_search_repository | where query = 'turbot/steampipe in name' |
| the body of the main query | github_search_commit | where query = 'author-date:>2023-10-04 repo:turbot/steampipe' |

现在让我们看主查询的主体:

```sql
select
  r.repo_name，
  c.commit -&gt; 'author' -&gt;&gt; 'name' as author，  
  substring(c.commit -&gt; 'committer' -&gt;&gt; 'date' from 1 for 10) as date，
  c.commit -&gt;&gt; 'message' as message
from
  repos r
join
  github_search_commit c
on
  r.repo_name = c.repository_full_name
  and r.query = c.query 
order by
  date desc
```

这里没有 WHERE 子句，但仍需要相同的限定词，它们也可以通过 JOIN 来提供。

所以，GitHub 搜索语法的动态构建分两层:

- 找到匹配 steampipe-plugin 的 GitHub 仓库
- 对找到的 200+ 个仓库中的每个，搜索给定日期之后的提交

现在我已经写出了解释，这看起来一点也不简单。如果只能写一个注释来帮助说明，那会是什么?

## 最重要的单个注释

当我第一次向 ChatGPT 显示这个查询时，目的不是请求文档，而是解决我在适应 GitHub 插件新版本中的某些已改列名时引入的命名冲突。尽管如此，LLM 提供了两点关键的改进，与这些列改变无关，我甚至没有要求过。

```
- 'author-date:>' || $2|| ' repo:' || g.name_with_owner as query
+ 'author-date:>' || $2|| ' repo:' || g.name_with_owner as commit_query

- and r.query = c.query
+ and r.query = c.commit_query
```

这非常正确。CTE 生成的 query 列不应与主查询体中使用的 query 限定词共享同名。这不是语法问题，但在概念上是一场灾难。将 CTE 的 query 列重命名为 commit_query 表示它与 query 限定词不同：是一种不同的用途，可以驱动 github_search_commit 查询。

这涉及到 [Learning While Coding: How LLMs Teach You Implicitly](https://thenewstack.io/learning-while-coding-how-llms-teach-you-implicitly/) 中讨论的这种隐含知识转移。这是我甚至没有要求的额外收益。

我认为下面的提示很有力量:

如果你只能为未注释的代码添加一个注释来澄清它，那会是什么?为什么?

我同时向 Copilot Chat 和 Sourcegraph Cody 提出了这个问题。

### Copilot

如果我只能为查询添加一个注释来解释它的工作原理，我会在WITH子句前面添加一个注释来解释它的作用。

```
-- This CTE retrieves the top 10 repositories that match the search query
```

**错误!**

### Cody

如果我要为此查询添加一个解释性注释，会加入在这里：

```
-- Construct dynamic commit search per repo
'author-date:&gt;' || $2|| ' repo:' || g.name_with_owner as query
```

我在这里添加注释的原因是，这行代码为每个仓库构建了一个自定义的提交搜索查询。

这是查询的关键部分——它允许在特定日期范围内针对每个仓库搜索提交记录。

如果没有这种动态构建，我们就无法对每个仓库有效过滤提交记录。

所以，添加一个快速注释来解释这行代码正在为每个仓库创建自定义的提交搜索查询，有助于阐明为何需要它，以及它如何与查询的其他部分协同工作，将仓库连接到匹配的提交记录。

**完全正确。干得好，Cody!**

## 动态文档

我理解为什么程序员经常抵制编写注释。懒惰？当然，但有时懒惰也是一种美德。计算机不care注释，它只care代码，所以如果你可以以一种对计算机和程序员都有帮助的方式编写代码，那是一个很好的开始。代码本身已经是一个维护负担;易于偏离源代码真相的注释会成为额外的负担。

尽管如此，我一直对程序文学编程的思想持同情态度。一年前，在《[Literate Programming in Go](https://www.infoworld.com/article/3677772/literate-programming-in-go.html)》一文中，我描述了一个项目，以改进[Steampipe插件SDK](https://github.com/turbot/steampipe-plugin-sdk)的文档。学习Go源代码可以嵌入类似wiki的文档这一点很有趣，我们也确实在增强否则乏味的从Go源代码生成的文档方面取得了一些进展。但我们并没有继续推进，现在我渴望在大语言模型时代再次尝试。

首先，我会重新审视我们编写的概述文档，以解释高级组件和概念。我认为Cody在索引[github.com/turbot/steampipe-plugin-sdk](https://github.com/turbot/steampipe-plugin-sdk)后会为我们提供良好服务。对这些概述文档而言，与大语言模型迭代以创建将成为代码永久组成部分并相应维护的文档，将是值得的。

但是对于函数和代码行级注释，我现在在想是否有时(或者经常!)动态方法会是最佳方案。我发现机械生成的函数级注释并不特别有用。但我们现在有新的合作伙伴。他们动态编写的注释是否足够有用，以避免固化可能偏离源代码真相的函数和代码行级文档？

这不是一种非此即彼的问题。我们正在进入两种方法共存的阶段。但我的直觉是，我们将要看到一个关于程序文学编程这个古老想法的有趣新转折。某些解释可以、将会并应该仅由代码作者单独编写，或者由作者与大语言模型合作编写。而其他解释可以、将会并应该由代码阅读器动态生成，阅读器可以即时请大语言模型提供解释。
