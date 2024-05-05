## 使用大型语言模型生成 SQL 架构

![SQL 架构生成与大型语言模型的特色图片](https://cdn.thenewstack.io/media/2024/05/834e66d0-getty-images-4aw2worpv5o-unsplash-1-1024x690.jpg)

我已查看了使用 LLM 生成的 [regex](https://thenewstack.io/using-ai-to-help-developers-work-with-regular-expressions/) 和 [JSON 持久性](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/)，但许多人认为 AI 可以很好地处理结构化查询语言 (SQL)（[https://thenewstack.io/the-future-of-sql-conversational-hands-on-problem-solving/](https://thenewstack.io/the-future-of-sql-conversational-hands-on-problem-solving/)）。为了庆祝 SQL 的 [50 岁生日](https://www.dataversity.net/sql-at-50-a-lesson-in-how-to-stay-relevant-around-data/)，让我们来讨论一下表，并在需要时引入技术术语。但是，我不想仅仅 [针对现有表测试查询](https://thenewstack.io/how-to-write-sql-queries/)。**关系数据库** 的世界始于 **架构**。

架构描述了一组表，这些表相互作用以允许 SQL 查询回答有关真实世界系统模型的问题。我们使用各种 **约束** 来控制表如何相互关联。在此示例中，我将开发一个有关书籍、作者和出版商的架构。然后，我们将看看 LLM 是否可以复制这项工作。

我们从我们事物之间的 **关系** 开始。一本书由一位作者编写，并由一位出版商出版。事实上，一本书的出版定义了作者和出版商之间的关系。

因此，具体来说，我们希望产生如下结果：

| 书籍 | 作者 | 出版商 | 发行日期 |
|---|---|---|---|
| 黄蜂工厂 | 伊恩·班克斯 | Abacus | 1984 年 2 月 16 日 |
| 考虑菲比 | 伊恩·M·班克斯 | Orbit | 1988 年 4 月 14 日 |

这很好读（我们稍后会回到它），但该表本身并不是维护更多信息的好方法。

如果出版商的名称只是一个字符串，则可能需要多次输入它——这既低效又容易出错。作者也是如此。那些有文学倾向的人会知道，这两本书的作者（伊恩·班克斯）是同一个人，但他在写科幻小说时使用了略有不同的笔名。

如果这本书后来由不同的出版商再次发行会怎样？为了确保区分这两个出版事件，我们需要同时提供书名和发行日期——因此我们的 **主键** 或唯一标识必须包括两者。我们希望系统拒绝输入标题和出版日期相同的两本书。

我们不使用一个大表，而是使用三个表并在需要时引用它们。一个用于作者，一个用于出版商，一个用于书籍。我们在 Authors 表中编写作者的详细信息，然后使用 **外键** 在 Books 表中引用它们。

因此，以下是使用数据定义语言 (**DDL**) 编写的架构表。我使用的是 MySQL 变体——令人讨厌的是，所有供应商仍然保持着略有不同的方言。

首先，是作者表。我们添加一个自动 ID 列索引作为主键。我们实际上并没有解决笔名问题（我把它留给读者）：

```
CREATE TABLE Authors (
ID int NOT NULL AUTO_INCREMENT,
Name varchar(255) not null,
Birthday date not null,
PRIMARY KEY (ID)
);
```

出版商表遵循相同的模式。“NOT NULL” 是另一个约束，可防止在没有内容的情况下添加数据。

```
CREATE TABLE Publishers (
ID int NOT NULL AUTO_INCREMENT,
Name varchar(255) not null,
Address varchar(255) not null,
PRIMARY KEY (ID)
);
```

书籍表将引用外键，这使其合乎逻辑但有点难以理解。请注意，我们尊重书名及其出版日期共同构成主键。

```
CREATE TABLE Books (
Name varchar(255) NOT NULL,
AuthorID int, PublisherID int,
PublishedDate date NOT NULL,
PRIMARY KEY (Name, PublishedDate),
FOREIGN KEY (AuthorID) REFERENCES Authors(ID),
FOREIGN KEY (PublisherID) REFERENCES Publishers(ID)
);
```

要看到顶部的一个整洁的表格，我们需要一个 **视图**。这只是将表缝合在一起的一种方式，以便我们可以挑选出需要显示的信息，同时保持架构不变。现在我们已经写下了架构，我们可以构建我们的视图：

```
CREATE VIEW ViewableBooks AS
SELECT Books.Name 'Book', Authors.Name 'Author', Publishers.Name 'Publisher', Books.PublishedDate 'Date'
FROM Books, Publishers, Authors
WHERE Books.AuthorID = Authors.ID
AND Books.PublisherID = Publishers.ID;
```

让我们看看是否可以在线游乐场中生成我们的架构，这样我们就不必安装数据库。

[DB Fiddle](https://www.db-fiddle.com/f/6Fj2vw8bFhzVADG4UFUjD6/0) 应该可以完成这项工作。

如果您输入 DDL，然后添加实际数据：

```
INSERT INTO Authors (Name, Birthday)
VALUES ('Iain Banks', '1954-02-16');
INSERT INTO Authors (Name, Birthday)
```
```
VALUES ('Iain M Banks', '1954-02-16');
INSERT INTO Publishers (Name, Address)
VALUES ('Abacus', 'London');
INSERT INTO Publishers (Name, Address)
VALUES ('Orbit', 'New York');
```

查看视图的结果在 DB Fiddle 中显示为“查询 3”，而这正是我们一直想要看到的数据：

## LLM 还能创建模式吗？

好的，现在我们想询问 LLM 关于创建模式的问题。总结一下我们希望如何指导 LLM：

- 当用英语询问模式时，我们希望它生成三个表的 DDL，包括索引和约束。
- 如果需要，我们还可以暗示需要约束（主键、外键等）。
- 我们可以要求查看。
- 如果需要，我们可以引导它使用 MySQL 语法。

我将使用 [Llama 3](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/)，但我还查看了 OpenAI 的 LLM，并得到了大致相同的结果。

我们的第一个查询：“创建一个关系数据库模式来描述书籍、出版商和作者。”

结果：

到目前为止还不错。它尚未创建 DDL，但我们可以单独询问。它在某种程度上做得更好，用英语描述了模式。我们来看看回复的其余部分：

它描述了外键约束并添加了 ISBN，这是我没想到的。此外，“PublicationDate”比我的“PublishedDate”更符合英语习惯。它还创建了一个表：

```
CREATE TABLE BookAuthors (
  BookId INT NOT NULL,
  AuthorId INT NOT NULL,
  PRIMARY KEY (BookId, AuthorId),
  FOREIGN KEY (BookId) REFERENCES Books (Id),
  FOREIGN KEY (AuthorId) REFERENCES Authors (Id)
);
```

这解决了多位作者写一本书的问题——这不是我考虑过的问题。术语 **桥表** 表示通过外键连接两个表（书籍和作者）。

我们来询问 DDL：“向我展示此模式的数据定义语言。”

```
CREATE TABLE Books (
  Id INT NOT NULL AUTO_INCREMENT,
  Title VARCHAR(255) NOT NULL,
  PublicationDate DATE NOT NULL,
  ISBN VARCHAR(13) UNIQUE NOT NULL,
  PRIMARY KEY (Id)
);

CREATE TABLE Authors (
  Id INT NOT NULL AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  PRIMARY KEY (Id)
);

CREATE TABLE Publishers (
  Id INT NOT NULL AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  PRIMARY KEY (Id)
);
```

这些都正确返回，包括 NOT NULL，以确保没有空条目。它还指出，由于现实世界中供应商 SQL 之间的差异，DDL 在某些方面是“通用的”。

最后，我们来询问一个视图：

```
CREATE VIEW BookDetails AS
SELECT
  b.Title AS BookTitle,
  a.Name AS AuthorName,
  p.Name AS PublisherName,
  b.PublicationDate
FROM
  Books AS b
JOIN
  BookAuthors AS ba ON b.Id = ba.BookId
JOIN
  Authors AS a ON ba.AuthorId = a.Id
JOIN
  Publishers AS p ON b.PublisherId = p.Id;
```

这是一个比我的复杂得多的版本；但是，当针对我的模式命名进行调整时，它在 DB Fiddle 中运行良好。表 **别名** 此处看到的命名对理解没有多大帮助。

## 结论：LLM 确实可以创建模式

我认为这对 LLM 来说是一个巨大的胜利，因为它们将我的英语描述变成了一个受限良好的模式，然后变成了可执行的 DDL，同时还提供了解释（尽管这些解释变成了更技术性的关系细节）。我甚至没有使用专门的 LLM 或服务，所以效果很好。

在某种程度上，这是将一个领域（出版界）映射到另一个领域（SQL 的特定领域语言），并且这对 LLM 的优势非常有利。每个领域都定义明确且细节丰富。

因此，祝 SQL 生日快乐，希望 LLM 能让它再保持几十年相关性！

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。
```