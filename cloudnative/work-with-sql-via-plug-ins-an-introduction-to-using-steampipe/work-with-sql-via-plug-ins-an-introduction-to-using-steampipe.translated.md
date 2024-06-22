SQL 一直是数据**通用语言**，允许从不同域中提取硬数据。这就是我特别感兴趣 [Steampipe 可通过 SQL 读取应用数据](https://thenewstack.io/sql-based-pipelines-steampipe-makes-all-the-world-a-database/) 的原因。它有许多插件，可将内部应用数据转换为漂亮的 SQL 表。

在这篇文章中，我将介绍 [Slack 插件](https://hub.steampipe.io/plugins/turbot/slack)，我将连接它，然后在实时工作区中使用它。但是，我们从一开始就知道，从 Slack 的角度来看，准备访问第三方应用需要做很多工作。这是尝试开放应用程序数据的缺点。

我喜欢 Steampipe 的一点是，你可以在将其附加到系统之前准备一个明智的查询。这对访问系统权限有限的顾问来说很有用，因此他们需要随身携带相当广泛的工具集。

有一个 [可用的 CLI](https://steampipe.io/downloads) 适用于我的 macOS 版本，我很乐意使用它的界面。像往常一样，我使用 [Warp](https://www.warp.dev/) 作为我的 shell，尽管 Steampipe 有自己的 CLI，稍后会优先使用。在更新 Homebrew 三分钟后，我直接安装了 Steampipe：

```
brew install steampipe
```

然后，快速检查版本以确保安装成功：

```
steampipe --version
```

然后，我安装了 Slack 插件：

```
steampipe plugin install slack
```

## 准备审问 Slack

你可能想要调查组织的 Slack 有几个原因，特别是如果你加入了一个团队，需要建立一个 [实践社区 (CoP)](https://thenewstack.io/developers-need-a-community-of-practice-and-wikis-still-work/)，或者只是想了解哪些用户最活跃，或者是否讨论了某些问题（或工单号）。

但首先，我们如何连接到它？幸运的是，Slack 有一种方法可以在范围内授予令牌以供应用使用。我很久以前就使用了这种方法，当时我研究了 [Dark，无服务器后端工具](https://thenewstack.io/how-to-get-started-building-serverless-backends-with-dark/)。当时有点棘手，所以我希望它变得简单一些。然而，这个过程只是稍微顺利一些。

我尝试使用 Slack 应用的 Mac 版本来执行此操作，但无法执行。但是，从网站上执行此操作很简单。签入你的目标 Slack 工作区，然后转到 [api.slack.com/apps](https://api.slack.com/apps)。

从这里，我们可以创建一个新应用，选择“从头开始”，然后给它一个名称。“应用”是 Slack 指 Steampipe 的第三方访问服务：

然后，我们可以选择权限并获得范围令牌访问权限。我避免任何与管理员相关的范围，并确保包括“团队”、“用户”、“组”等：

你始终可以返回此部分，添加任何缺少的范围并重新安装应用。

这将允许应用从 Slack 检索基本信息。最后，我们将把我们的新工具及其 OAuth 令牌安装到工作区。务必复制你的长用户 OAuth 令牌：

像往常一样，Slack 会向你显示警告，表示它正在请求访问（或无法访问的原因）。

确保在进度列表中看到“安装你的应用”旁边的勾号：

现在返回你的 shell，并将该令牌添加到 Steampipe 的 Slack 配置文件中：

```
steampipe config set slack.token <YOUR_OAUTH_TOKEN>
```

## 查询数据

现在我们终于准备好查看我们可以在 Steampipe 本身中做什么了。耶！

我们将访问 CLI 的查询模式，并立即查看可用表列表（请注意提供了自动完成建议）：

（在空白行中按 Ctrl+D，或使用 `.exit` 命令。）

结果如下：

| 表 | 描述 |
|---|---|
| `slack_access_log` | 按用户、IP 和用户代理分组的 Slack 登录。 |
| `slack_connection` | 有关与 Slack 工作区连接的信息。 |
| `slack_conversation` | 类似于所有对话的统一界面。 |
| `slack_conversation_member` | 检索对话的成员。 |
| `slack_emoji` | 工作区中安装的 Slack 表情符号。 |
| `slack_group` | Slack 工作区用户组。 |
| `slack_search` | 使用查询搜索 Slack 中的任何内容。 |
| `slack_user` | Slack 工作区用户。 |

要获取有关表中列的信息，请运行 `.inspect {connection}.{table}`。

在继续之前，尝试此命令以确认你是否已连接：

```
select * from slack_user;
```
### 确保您获得一些有用的数据。

如果没有，请检查安装是否完成或访问令牌是否足够。

在我们愤怒地查询之前，让我们快速查看一下

`slack_user` 表：

```
.inspect slack_user
```

首先，我想看看哪些用户不是机器人，没有被删除，以及谁更新了他们的帐户以使用双因素身份验证：

出于某种原因，Slackbot 不是机器人！但我可以看到，如果这是我的担忧，两个人可能需要安全提醒。

现在让我们看看 `slack_search` 表，它可以更准确地放大信息：

请注意 `channel` 是一个 JSON 类型，乍一看似乎有点问题。但是，您可以使用 `->>` 运算符来提取文本。您必须在 `where` 子句中指定查询才能查询此表。

以下是快速搜索工作区频道中提到的“ChatGPT”：

但我们可能想要更多有关何时提及的信息：

使用 `slack_conversation` 表，我们可以通过计算成员数量来了解热门频道：

```
select name,num_members from slack_conversation where
num_members is not null
order by num_members desc
limit 5;
```

因为我们正在使用 SQL，所以我们当然可以根据需要查找的信息在表之间获得更多集中的查询。

希望您能看到 Steampipe 是一个检索有价值数据的有用工具，并且这个 Slack 插件很好地展示了我们可以得到什么。如果您对系统的访问权限有限，那么准备一份有用的 SQL 查询列表可以节省您的时间——这是一种以您选择的灵活格式获取所需数据的好方法。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、采访、演示等。