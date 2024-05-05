# 自动为 PostgreSQL 数据库生成类型

![自动为 PostgreSQL 数据库生成类型的特色图片](https://cdn.thenewstack.io/media/2024/04/397f878b-tns-automatically-generate-types-for-your-sql-queries-featured-image-1024x538.jpg)

我最近一直在为 JavaScript 开发人员从事与 [PostgreSQL](https://thenewstack.io/from-a-fan-on-the-ascendance-of-postgresql/) 相关的大量工作，我的总体理解是 JavaScript 开发人员会不惜一切代价避免编写非 JavaScript 的代码。他们会将 [CSS 放入 JavaScript](https://thenewstack.io/tailwind-css-for-developers-style-without-using-css-code/)、[HTML 放入 Jsx](https://thenewstack.io/how-to-build-a-server-side-react-app-using-vite-and-express/)，现在还要将 SQL 放入 JavaScript！

这就是我所说的。

此语法没有官方名称，在 Supabase 的情况下，它是 [PostgREST](https://postgrest.org/en/v12/#) 之上的一个抽象。但是，我想提议我们将此语法称为 [SamQL-Jackson](https://twitter.com/PaulieScanlon/status/1783547347475067172)。

JavaScript 开发人员选择此语法而不是“原始 SQL”的原因有很多，根据我的观察，这些原因大致可分为三类：

- 我没时间学习 SQL。
- 我不想学习 SQL。
- SQL 不是类型安全的。

## 1.“我没时间学习 SQL。”

这是主观的，无法争论。如果你太忙而无法学习新事物，我完全理解。

## 2.“我不想学习 SQL。”

第 2 点也有些主观——学习你不太感兴趣的东西通常更困难。但是，我对这一点的唯一警告是 SQL 被广泛使用，因此它可能是你箭袋中的一支好箭。

## 3.“SQL 不是类型安全的。”

第 3 点有点难以解决，以下是 Jiri Cincura 的解释：

[SQL 命令的类型安全性](https://www.tabsoverspaces.com/232264-type-safety-of-sql-commands#:~:text=Summary%3F,your%20code%20and%20compiler%27s%20rules.). *“SQL 命令是类型安全的，但仅在服务器上。在你的应用程序代码中编写时，它仍然是类型安全的，但不是从你的代码和编译器规则的类型安全性的角度来看”*

归根结底，这意味着如果 SQL 查询没有类型，则代码编辑器中没有可用的类型预览。例如：

```sql
SELECT first_name, country FROM users;
```

没有可用的类型定义会让处理数据库响应变得更加困难。

除了手动检查表模式或使用 `console.log()`，没有简单的方法可以查看响应或表中包含哪些值。还需要在你的头脑中转换 Postgres 模式；例如，`VARCHAR(255)` 转换为 TypeScript 类型，例如，`string`。你也许可以在 `console.log()` 中使用 `typeof`，但这仍然不是一个很好的解决方案。

简而言之，在“JavaScript”代码库中使用 SQL 时绝对需要提供类型定义，但手动创建这些类型可能很耗时，并且可能会随着时间的推移而改变——需要进一步的手动干预和花费更多的时间。

因此，可以理解为什么许多 JavaScript 开发人员会选择使用 SamQL-Jackson 而不是“原始 SQL”，因为许多这些 JavaScript 数据库供应商在其客户端和 SDK 中内置了类型安全性。但在这些场景中，你仍然需要学习其供应商特定的语法，因为不幸的是，每个供应商处理此语法的略有不同。

以下是一个简单 SQL 查询的示例，该查询选择值 `first_name`、`country` 和 `users`。

```sql
SELECT first_name, country FROM users;
```

以下是 Supabase 和 Xata 的相同查询。

### Supabase

```sql
supabase
  .from('users')
  .select('first_name, country')
```

### Xata

```sql
xata.db.users.select(['first_name', 'country'])
```

你会注意到这两个查询彼此不同，如果你只打算使用 Supabase，这可能没问题。但是，如果你确实需要切换数据库提供商，则必须学习一种全新的语法——更不用说重写一堆查询了。

自然地，如果你编写 SQL，那么这些查询将适用于每个 PostgreSQL 解决方案，虽然我不能肯定地说，但这些原因确实在某种程度上挑战了上述第 1 点和第 2 点。

*值得注意的是，Supabase 和 Xata 都可以使用“普通”SQL 进行查询，仅供参考！*

无论如何，如果你决定采用“原始 SQL”路线并且需要类型，这里有几个选项供你选择。

## 自动类型生成

我试验了两种解决方案：

[kysely-codegen](https://github.com/RobinBlomberg/kysely-codegen) 和 [pg-to-ts](https://github.com/danvk/pg-to-ts)。两者对我来说都非常有效，以下是如何使用它们。

## 如何使用 kysely-codegen

[kysely-codegen](https://github.com/RobinBlomberg/kysely-codegen) 从你的数据库生成 Kysely 类型定义。就是这样。

### Kysely 安装

运行以下命令安装主要的 Kysely 包。还要检查
## Kysely

### 安装说明

请参阅 [安装说明](https://github.com/RobinBlomberg/kysely-codegen?tab=readme-ov-file#installation)，因为在我的情况下，我还需要安装 [pg](https://www.npmjs.com/package/pg)。

您还需要运行以下命令来安装 codegen 包。

### Kysely package.json 脚本

为了方便起见，我在 package.json 中添加了一个脚本。使用 -out-file 标志，此脚本将在我的项目的根目录中创建一个名为 kysely-db.d.ts 的文件。

### Kysely .env

Kysely 要求您在 .env 文件中有一个名为 DATABASE_URL 的环境变量。

### Kysely 生成

您现在可以运行以下脚本，您应该会在项目的根目录中看到一个新的 .d.ts 文件，其中包含数据库中所有表和列的所有类型。

以下是我测试数据库的代码片段。它只包含一个名为 *users* 的表。

### Kysely 类型化查询

以下是我在 PostgreSQL 查询中使用生成类型的示例，但这些类型定义也可以用作组件的 props 接口的一部分。

## pg-to-ts

### pg-to-ts 安装

运行以下命令来安装主要的 pg-to-ts 包。

### pg-to-ts package.json 脚本

为了方便起见，我在 package.json 中添加了一个脚本。使用 -c 标志，您可以引用 DATABASE_URL，在从终端运行脚本时可以传递该标志。此脚本将在我的项目的根目录中创建一个名为 pg-to-ts-db.d.ts 的文件。

### pg-to-ts 生成

您现在可以在 npm run 命令之前提供 DATABASE_URL 来运行以下脚本，您应该会在项目的根目录中看到一个新的 .d.ts 文件，其中包含数据库中所有表和列的所有类型。

以下是我测试数据库的代码片段。它只包含一个名为 *users* 的表。

### pg-to-ts 类型化查询

以下是我在 PostgreSQL 查询中使用生成类型的示例，但这些类型定义也可以用作组件的 props 接口的一部分。

## 完成

所以，SQL 可以是类型安全的（在 JavaScript 的意义上）。它是自动化的，因此在架构发生更改时不会出现大问题。但更重要的是，我希望您现在不再那么不愿意使用“原始 SQL”了。毕竟，它是数据库的语言。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。