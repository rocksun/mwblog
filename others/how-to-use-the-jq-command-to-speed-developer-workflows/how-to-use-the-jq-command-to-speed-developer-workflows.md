
<!--
title: 如何使用 JQ 命令加速开发者工作流
cover: https://cdn.thenewstack.io/media/2024/11/73d841f1-jq-playground-lead.png
-->

jq 命令提供了一种一致的方式来操作 JSON 数据，而无需离开命令行。通过在 jq playground 中进行练习来了解它的工作原理。

> 译自 [How to Use the JQ Command to Speed Developer Workflows](https://thenewstack.io/how-to-use-the-jq-command-to-speed-developer-workflows/)，作者 Roi Talpaz。

处理 JSON 对象对于开发者和平台工程师来说都是一项复杂且日常的任务。开发者经常需要自动化包含 JSON 数据的工作流程，例如处理 API 响应、生成配置文件或分析日志。同时，平台工程师使用 JSON 在其平台和门户中创建自动化工作流程、自助服务操作等等。

虽然 [JSON 的简洁性](https://thenewstack.io/an-introduction-to-json/) 最初吸引了工程师，但 [处理 JSON 数据](https://thenewstack.io/working-with-json-data-in-python/) 引入了一些复杂性。处理 JSON 文件，特别是处理大型数据集的困难在于难以找到和操作所需的信息。为了解决这个问题，工程师复制粘贴 JSON 文件的部分内容来计算总数或为简单的任务编写复杂的脚本，但这是一个耗时的过程，容易出错，进而影响开发者的工作流程。

`jq`，一个命令行 JSON 处理工具，应运而生。它使开发者能够轻松地操作数据，无论是从服务器的响应中提取信息，还是获取部署的可用副本数量。`jq` 将这些任务嵌入到 shell 脚本或管道中，而这些脚本或管道本身并不直接兼容 JSON。因此，`jq` 提供了一种一致的方式来处理 JSON，而无需离开命令行。并且自从 `jq` 发布以来，已经推出了交互式 `jq` playground，允许你实时地试验 JQ 命令和过滤器，提供即时反馈来帮助你学习、测试和调试复杂的 JSON 变换。

## JQ 使用案例

有多种方法可以使用 JQ 来加快开发者工作流程。在本文中，我将特别讨论在 [内部开发者门户](https://thenewstack.io/improve-developer-onboarding-with-an-internal-developer-portal) 中构建开发者工作流程。

### 1. 过滤和提取 JSON API 响应中的数据

如果你经常使用返回大型 JSON 有效负载的 API，`jq` 可以帮助你过滤并仅提取相关信息，从而更容易处理和分析数据。这在内部开发者门户中构建工作流程时尤其有用，因为你可以使用 `jq` 比使用简单的 JSON 文件更快地找到精确的字段和数据点。

例如，假设你已将 GitHub 集成到内部开发者门户中，以使待办事项列表更易于操作。你希望将评论最多的 GitHub issue 放在待办事项列表的顶部，并使用每个 GitHub issue 的标题来组织它们。

你可以使用 [GitHub API](https://docs.github.com/en/rest?apiVersion=2022-11-28) 来实现这一点。使用此 `jq` 命令传入 API 请求：

```bash
curl -L \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/jqlang/jq/issues | jq "max_by(.comments) | .title"
```

作为回应，API 输出应为：

```bash
"Add exec/2: posix_spawn"
```

### 2. 将 JSON 结构转换为其他工具的输入

在许多情况下，你需要重新格式化 JSON 数据结构以匹配另一个工具或服务所需的形式。`jq` 通过允许你快速创建新的 JSON 对象、操作数组和转换数据格式来加快此过程。

继续上面的例子，你可以清理来自 GitHub 的 `issue` 对象，只包含你认为重要的字段到你的 Slack 消息自动化中。

以下是输入：

```json
{
  "url": "https://api.github.com/repos/jqlang/jq/issues/3192",
  "id": 2599050572,
  "node_id": "PR_kwDOAE3WVc5_K9vw",
  "number": 3192,
  "title": "Adds ascii_title to string manipulation",
  "user": {
    "login": "fabiomatavelli",
    "id": 566767,
    "node_id": "MDQ6VXNlcjU2Njc2Nw==",
    "received_events_url": "https://api.github.com/users/fabiomatavelli/received_events",
    "type": "User",
    "user_view_type": "public",
    "site_admin": false
  },
  "author_association": "NONE",
  "active_lock_reason": null,
  "draft": true,
  "pull_request": {
    "merged_at": null
  },
  "body": "This introduces the `ascii_title` for string manipulation. The function is set to produce a Title like string, making all the first ASCII characters of each word uppercase.",
  "closed_by": {
    "login": "fabiomatavelli",
    "id": 566767,
    "node_id": "MDQ6VXNlcjU2Njc2Nw==",
    "avatar_url": "https://avatars.githubusercontent.com/u/566767?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/fabiomatavelli",
    "type": "User",
    "user_view_type": "public",
    "site_admin": false
  },
  "reactions": {
    "url": "https://api.github.com/repos/jqlang/jq/issues/3192/reactions",
    "total_count": 0,
    "+1": 0,
    "-1": 0,
    "laugh": 0,
    "hooray": 0,
    "confused": 0,
    "heart": 0,
    "rocket": 0,
    "eyes": 0
  },
  "timeline_url": "https://api.github.com/repos/jqlang/jq/issues/3192/timeline",
  "performed_via_github_app": null,
  "state_reason": null
}
```

转换此 JSON 有效负载的 `jq` 命令应如下所示：

```bash
curl -L \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/jqlang/jq/issues | jq '.[0] | { "title": .title, "url": .html_url, "user": .user.login, "comments": .comments }'
```

最后，输出只包含你想要在 Slack 消息中共享的字段：

```json
{
  "title": "Adds ascii_title to string manipulation",
  "url": "https://github.com/jqlang/jq/pull/3192",
  "user": "fabiomatavelli",
  "comments": 0
}
```

现在你的门户将通过发送 Slack 消息来帮助你优先处理待办事项，这些消息会提醒冲刺计划者注意需要优先处理的带有评论的 GitHub issue。

### 3. 自动化配置和环境变量

`jq` 可用于 shell 脚本中读取、修改和写入 JSON 配置文件。在需要动态调整 JSON 配置的 CI/CD 管道中，它尤其有用。

这是一个示例 `jq` 命令：

```bash
jq '.propertyName' config.json
```

你还可以修改你的配置，例如：

```bash
jq '.propertyName = "newValue"' config.json > updated_config.json
```

### 4. 验证和美化 JSON

如果你需要快速检查 JSON 文件是否格式正确，或者你知道需要使其更易读并且不想手动操作，则可以使用 `jq` 通过单个命令来验证和格式化 JSON。这在调试格式错误的 JSON 或只是查看数据时尤其有用。

## 使用 JQ Playground 快速上手

`jq` playground 是在线环境，你可以在其中测试和试验 `jq` 命令和过滤器。playground 允许你试验 `jq` 实时显示命令，帮助您快速了解不同的过滤器、管道和运算符的行为。这种动手实践、反复尝试的方法比仅仅阅读文档更有效地帮助您学习`jq`的语法和功能。

通过提供可视化环境，游乐场允许您构建和测试`jq`查询，将其分解成更小、更易于管理的部分，然后再将它们组合成更大的脚本。您还可以使用注释和空格来分解复杂的查询，从而更容易理解`jq`代码的不同部分是如何协同工作的。

游乐场环境也有助于回忆和保留，因为您可以立即看到`jq`查询的实际结果，从而更容易识别和修复错误。由于您可以迭代地测试小的更改，这种逐步反馈有助于您调试复杂的转换，而无需保存文件、运行命令和等待输出的额外开销。

游乐场环境使探索深度嵌套或不规则的JSON数据更容易。您可以即时尝试不同的路径和转换，立即查看输出并根据需要调整方法。这使得理解和导航复杂的JSON变得更容易，而无需在命令行上反复编写和重新运行脚本。

## 使用JQ游乐场

这是一个使用JQ游乐场的示例

![](https://cdn.thenewstack.io/media/2024/11/b795de42-jq-playground.png)

如果您想试验JQ命令和过滤器，请使用[此JQ游乐场](https://jq.getport.io/)。如果您想讨论其他加快开发人员工作流程的方法，请加入[Port社区](https://port-community.slack.com/ssb/redirect)。
