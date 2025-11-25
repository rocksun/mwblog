你打开 Claude Code 或 Cursor，描述你的表，几秒钟内 AI 就会给你一个看起来……还行的 Postgres 模式。它能运行。你的测试通过了。你发布了。

你没看到的是其中潜藏着的小小灾难：用于价格的 `money` 类型，在随机数据上的 BRIN 索引，`SERIAL` 和 `UUID` 像鸡尾酒一样混用，`timestamp without time zone` 因为有些教程说它“更容易”。

快进六个月。你正在调试货币转换错误，追逐时区幽灵，重写迁移，并添加一个本应从第一天就存在的索引。AI 代理编写的代码能运行；但它不够好。它只是复制了从整个互联网上抓取到的任何示例。

这就是问题所在。它从各个地方学习 SQL：Postgres、MySQL、SQLite、SQL Server、Oracle、随机教程以及十年来的 Stack Overflow 答案。在所有这些噪音中，惯用的、高质量的 Postgres 的细微之处被好的、坏的以及 MySQL 的内容所掩盖。

所以我们构建了一些东西来解决这个问题。

## 赋予 AI 缺失的 Postgres 判断力

pg-aiguide 为 AI 编程代理提供了它们所缺失的 Postgres 特有判断力。它通过以下三者的协同工作实现：

1.  **AI 优化型“技能”**—— 精心策划、有主见的 Postgres 最佳实践，Claude Code 和其他代理可以自动应用。
2.  **官方文档的语义搜索**—— 针对 Postgres 15–18 的版本感知检索。
3.  **扩展生态系统文档**，从 TimescaleDB 开始并快速扩展

你可以通过我们的公共 **模型上下文协议 (MCP) 服务器**，或利用为支持 Claude 原生技能而构建的 **Claude Code 插件**，将其连接到任何 AI 编程代理。无需账户。没有使用限制。完全免费。

目标很简单：**让 AI 默认编写正确、生产就绪的 Postgres 代码。**

你不必粘贴文档、纠正输出或依赖提示技巧。AI 第一次就应该生成更好的 SQL。

💡

****立即试用****

你可以在不到一分钟的时间内开始使用 pg-aiguide。它适用于 Claude Code、Codex、Cursor、Gemini CLI、Visual Studio、VS Code、Windsurf 和任何其他 MCP 兼容编辑器。请参阅我们的

[快速入门指南](https://github.com/timescale/pg-aiguide/tree/main?tab=readme-ov-file#-quickstart)

获取安装说明。

## 为什么数据库代码质量如此重要

Postgres 开发者中 AI 的采用率激增：根据 [2024 年 Postgres 状况](https://www.tigerdata.com/state-of-postgres/2024) 调查，一年内从 37% 跃升至 55%。但随着 LLM 变得越来越通用，训练数据变得宽泛而非专业化，LLM 变得 *不那么* 精确。

这带来了一个令人惊讶的问题：METR 最近的一项研究发现，有经验的开发者使用 AI 完成任务实际上花费了 **19% 更长的时间**。这并非因为 AI 失败，而是因为输出“几乎正确”——那种微妙的错误需要最长的时间来发现、调试和解决。

对于数据库来说，“几乎正确”会迅速累积问题。

模式将决策编码，后期更改起来很痛苦。索引错误会一直隐藏，直到你的表增长。在开发中只需一小时修复的数据类型选择，在生产环境中可能需要数天的迁移和仔细规划。

你可以重构应用程序代码。你无法在不承担后果的情况下重构状态。

pg-aiguide 在这些错误进入生产环境之前，就在源头阻止它们。

## 通用 SQL 与引导式 SQL

当您要求编程助手设计一个简单的书店模式时，会发生以下情况。

### 未启用 pg-aiguide

```
CREATE TABLE customers (
    customer_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE INDEX idx_customers_email ON customers(email);

CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    biography TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

```

复制

这个模式可以工作，但存在经典问题：

*   混合了身份策略
*   任意的 `VARCHAR` 限制
*   区分大小写的电子邮件唯一性
*   在不同系统上行为不一致的时间戳默认值

### 启用 pg-aiguide

```
CREATE TABLE authors (
  author_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name TEXT NOT NULL,
  bio TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX ON authors (name);

CREATE TABLE users (
  user_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  phone TEXT,
  is_active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX ON users (LOWER(email));
CREATE INDEX ON users (created_at);
```

复制

此版本使用：

*   一致的身份列（`BIGINT GENERATED ALWAYS AS IDENTITY`）
*   `TEXT` 而非不必要的 `VARCHAR`
*   正确的时间戳处理（`timestamptz + now()`）
*   正确强制执行不区分大小写的唯一性

在幕后，AI 通过 [design\_postgres\_table skill](https://github.com/timescale/pg-aiguide/blob/main/skills/design-postgres-tables/SKILL.md)（通过 [view\_skill](https://github.com/timescale/pg-aiguide/blob/main/API.md#view_skill) MCP 工具或 [Claude 的原生技能框架](https://www.claude.com/blog/skills)）使用了该技能。在这两种情况下，代理都无需人工干预自动发现并应用了 Postgres 优化指南。

您不必以不同的方式提示。

您不必粘贴文档。

**pg-aiguide 自动将 AI 从“能用的 SQL”转变为“您真正在生产环境中想要的 SQL”。**

## 技能是秘密武器

如果你希望 AI 生成高质量的 SQL，仅仅让它搜索手册是不够的。手册告诉你你能做什么，而不是你应该做什么。技能弥补了这一空白。它们赋予模型判断力，而不仅仅是事实。

我们的技能并非试图重新教授 LLM 语法或能力。相反，它们为模型提供了做出更好选择所需的上下文。以下是真实技能的一个摘录。

```
## Postgres "Gotchas"

- **FK indexes**: Postgres **does not** auto-index FK columns. Add them.
- **No silent coercions**: length/precision overflows error out (no truncation). 
  Example: inserting 999 into `NUMERIC(2,0)` fails with error, unlike some 
  databases that silently truncate or round.
- **Heap storage**: no clustered PK by default (unlike SQL Server/MySQL InnoDB); 
  row order on disk is insertion order unless explicitly clustered.
```

复制

这些细节是您在 Postgres 中生活一段时间后才能了解的。它们绊倒 LLM 的原因与绊倒数据库新手（甚至一些不那么新的开发者）的原因相同。然而，正是这些细节使得模型能够生成更好的 SQL。

在我们的评估中（目前是人工“氛围驱动”，很快将由 LLM 评估），当我们比较仅使用语义搜索的系统与同时包含语义搜索和技能的系统时，模式质量持续提高：

*   更合适的数据类型
*   正确的时间戳语义
*   更强的索引策略
*   更少的迁移陷阱
*   更少的长期性能意外

这正是“AI 编程工具真正理解 Postgres”的样子。

## 我们提供给 LLM 的工具

pg-aiguide 提供了两个核心功能，它们与 AI 编程工具的运作方式紧密对应。

### 1. 技能：完整、有主见的 Postgres 指导

`view_skill` 返回完整、AI 优化的最佳实践。它们不是教程，也不是模糊的提示。它们是面向机器、密集、token 高效的指导，AI 可以可靠地使用。

例如：

*   首选 `BIGINT GENERATED ALWAYS AS IDENTITY`
*   不要使用 `money` 类型
*   不要使用不带时区的 `timestamp`
*   为外键创建索引
*   预期精度溢出时会出现错误

技能不需要分块——它们的编写方式使得每项技能都可以作为单个完整单元纳入上下文。

Claude Code 甚至原生支持技能，因此当作为插件运行时，MCP 服务器的 `view_skill` 工具会自动禁用。

### 2. 语义搜索：跨文档的版本感知向量检索

MCP 工具 `semantic_search_postgres_docs` 和 `semantic_search_tiger_docs` 允许 AI 提取您目标 Postgres 版本的**正确**文档。

这很重要，因为 Postgres 版本会发生有意义的演变：

*   Postgres 15: `UNIQUE NULLS NOT DISTINCT`
*   Postgres 16: 并行查询行为的重大变化
*   Postgres 17: COPY 错误处理的改进

如果没有版本感知能力，AI 可能会（并且确实会）虚构出在您实际环境中会破坏的功能或语法。

所有这些 Postgres 知识都被分块、嵌入并存储在 Postgres 本身中。

我们抓取官方 HTML 文档，保留标题上下文，附带源 URL，并使用带 H1→H2→H3 面包屑的字符边界分块，这样每个片段都能保留其如何融入更广泛拼图的含义。

## 帮助我们为 AI 构建全球最佳 Postgres 指南

Postgres 拥有 35 年的工程、技艺和来之不易的经验教训。没有哪个团队能独自捕获所有这些。社区构建了使 Postgres 成为其自身的模式、扩展和生产智慧。AI 编码工具应该反映这种深度，而不是吐出从过时教程和旧 Stack Overflow 帖子中提取的通用 SQL。

pg-aiguide 是我们迈出的第一步，旨在让 Postgres 有意而非偶然地成为与 AI 编码助手配合使用的最佳数据库。我们正在通过更丰富的索引指导、全文搜索技能以及 PostGIS 和 pgvector 等基本扩展的文档来扩展技能库。我们还在添加关键词 BM25 搜索，以与语义搜索配合，实现更准确的检索。**但我们需要您的帮助。**

### 您如何贡献

您可以立即产生影响：

*   为您的 Postgres 扩展添加文档
*   贡献新的技能，编码真实、经过实战检验的专业知识
*   帮助评估、完善和压力测试现有技能
*   请求功能或报告问题
*   改进语义搜索分块或提出新的索引领域
*   分享关于分区、复制、安全或性能调优的深入知识

技能最为重要。它们将多年的经验转化为 AI 可以立即使用的指导。我们的模式设计技能经过多次迭代才达到理想状态，我们在此过程中学到了很多。我们很乐意与您合作，在您的专业领域构建技能。

pg-aiguide 在 github.com/timescale/pg-aiguide 完全开源。

**帮助我们教会 AI 像专家一样编写 Postgres 代码。**