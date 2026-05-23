n8n 是目前最强大的工作流自动化平台之一，而学习它最快的方法就是亲手构建一个真实的案例。

在本文中，你将构建一个完整的端到端 AI 工作流。我们将以内容发布管道为例，但你在此学到的概念：触发器、AI 代理、条件路由、人工审批和 API 调用，同样适用于你随后构建的任何工作流。

没有枯燥的理论堆砌。你将边读边练。

## 你将学到什么

你将构建一个真实的自动化项目。在此过程中掌握的技能将为你开启通往无限自动化可能的大门。

> “没有枯燥的理论堆砌。你将边读边练。”

到最后，你将学会如何：

* 安装并设置 n8n
* 选择正确的触发器来启动工作流
* 从外部服务获取数据并处理故障
* 将 AI 集成到你的工作流中，使其成为智能工作流
* 使用条件和逻辑路由数据
* 在 Gmail、Slack 或 Teams 等任何平台上发送通知
* 以专业的方式测试、调试和扩展工作流

这些是每个严肃的 n8n 工作流的构建基石。一旦学会，你就可以反复使用它们。

## 项目：文章提交工作流

我们将[构建一个真实的内容自动化工作流](https://thenewstack.io/building-multiagent-systems-for-workflow-automation-with-crewai/)。

**问题：** 发布一篇博文需要大量的后台手动协调。作者提交草稿；审稿人阅读并发送反馈；另一个人在 CMS 上发布；最后，财务团队处理付款。这需要四次交接，以及通过电子邮件进行的大量反复沟通。

我们将使用 n8n 自动化整个工作流。

该流程分为六个阶段。每一个都教授一个核心概念。

1. **提交：** 作者在 Google Docs 中起草文章，并通表单提交。
2. **文档获取：** n8n 获取 Google Docs 内容并验证链接是否有效且可访问。
3. **AI 评审：** AI 代理根据一系列规则对草稿进行评审。未通过的草稿将通过电子邮件退回给作者，并附上具体反馈。
4. **编辑审批：** 编辑在 Slack 中批准或拒绝草稿。
5. **发布：** 批准的草稿将发布到 CMS（Hashnode、WordPress 等）。

**成功邮件和付款提醒：** 作者收到确认邮件。财务团队收到 Slack 提醒以发放款项。

## 开始之前：运行 n8n

在构建之前，你需要运行 n8n。

### 方案 1：云端版（启动最快）

在 <https://n8n.io/> 注册。免费试用涵盖了本教程中的所有内容。

### 方案 2：自托管（免费且无限制）

这是免费且无限制的，但你需要安装 Docker。如果你还没有，请从 [Docker 官方网站](https://www.docker.com/products/docker-desktop/)下载，然后运行：

```
docker volume create n8n_data

docker run -d --restart unless-stopped \
  --name n8n -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

现在，打开 <http://localhost:5678>。创建你的账户，大功告成。

**注意：** 如果你采用自托管，你的 n8n 实例必须能从互联网访问，基于 webhook 的步骤才能正常工作。可以使用 ngrok 或 Cloudflare Tunnel 等隧道工具，并将 WEBHOOK\_URL 环境变量设置为你的公共 URL。

本教程建议使用方案 1。一旦一切运行正常，你可以免费迁移到自托管实例。

n8n 运行后，让我们开始构建。

## 第 1 阶段：触发器

每个工作流都从触发器开始。它定义了什么会启动工作流。n8n 提供了许多触发器：定时触发器按固定间隔运行，电子邮件触发器在收到新邮件时触发，webhook 触发器响应 HTTP 请求，等等。

对于我们的工作流，我们将使用 **Form Trigger**（表单触发器）。作者填写包含其 Google Docs 链接的表单。当他们提交时，工作流启动。

在你的 n8n 中，点击“Create Workflow”按钮创建一个新工作流。

这将在画布上创建一个空的工作流。

![n8n 空画布截图，中心显示 "Add first step" 提示，左侧边栏显示工作流设置。](https://cdn.thenewstack.io/media/2026/05/0e6fe844-1-1024x487.png)

*截图：n8n 空画布，中心显示“Add first step”提示，左侧边栏显示工作流设置。*

现在，在左上角点击“+”图标并搜索“Form Trigger”。在触发器部分选择“On form submission”。

![截图：节点选择器打开，显示 "Form Trigger" 搜索结果。突出显示 "On form submission" 事件。](https://cdn.thenewstack.io/media/2026/05/e7c7b90c-2.png)

*截图：节点选择器打开，显示“Form Trigger”搜索结果。突出显示“On form submission”事件。*

向你的表单添加以下字段：

* 姓名 (text, 必填)
* 邮箱 (email, 必填)
* 标题 (text, 必填)
* Google Docs 链接 (text, 必填)

你还可以添加 HTML 块来配置表单，但这在本教程中是可选的。

点击底部的“Execute workflow”。表单将在新标签页中打开。

![截图：在浏览器新标签页中呈现的表单，显示姓名、邮箱、标题和 Google Docs 链接字段。](https://cdn.thenewstack.io/media/2026/05/391414d7-3.png)

*截图：在浏览器新标签页中呈现的表单，显示姓名、邮箱、标题和 Google Docs 链接字段。*

你的第一个触发器已经准备就绪。

你可以与作者分享工作流的公共 URL，以便他们提交文章草稿进行评审。

## 第 2 阶段：验证 Google Docs 链接

你已经收集了作者的详细信息及其 Google Docs 链接，但请记住，链接可能是断开的，或者文档可能没有共享。在将其传递给 AI 之前，你需要对其进行验证。

点击触发器节点后的“+”图标，搜索“Google Docs”。

选择“Get a document”操作。根据提示使用你的 Google 账户进行身份验证。

在“Document URL”字段中，从 Form Trigger 节点拖入“Google Docs link”字段。n8n 会为你插入表达式。

现在，打开该节点的 Settings 选项卡，将 **On Error** 切换为 **Continue (using error output)**。这会在 Google Docs 节点上添加第二个输出，用于处理错误路径。如果文档是私有的或链接断开，数据将流向错误分支，而不是中止工作流。

接下来，在 Google Docs 节点的主（成功）输出后添加一个 **IF** 节点。IF 节点根据条件路由你的工作流。在这里，我们确认确实收到了文档。

在 IF 节点中，添加此条件：

* Value 1: {{ $json.content }}
* Operation: Exists (或 “Is Not Empty”)

如果 Google Docs 节点成功，content 字段将被填充，TRUE 分支触发。失败时，节点会将数据发送到其错误输出，你将其连接到 Gmail 拒绝节点。

创建此条件后，你的工作流应如下所示：

![截图：画布显示四个按顺序连接的节点 - Form Trigger、Google Docs 节点、IF 节点，且 IF 节点的 TRUE 和 FALSE 分支可见。](https://cdn.thenewstack.io/media/2026/05/440f8fbc-4-1024x337.png)

*截图：画布显示四个按顺序连接的节点——Form Trigger、Google Docs 节点、IF 节点，且 IF 节点的 TRUE 和 FALSE 分支可见。*

如果文档加载成功，工作流将继续沿 TRUE 分支运行。

将 Google Docs 节点的错误输出直接连接到一个 Gmail 节点，以向作者发送邮件告知其链接失效。（你也可以使用 IF 节点的 FALSE 分支作为边缘案例的备选路径，即文档加载了但内容为空的情况。）

添加一个 Gmail 节点。选择“Send an email”操作并使用你的 Google 账户进行身份验证。

在“To”字段中，从 Form Trigger 拖入 Email 字段。添加主题行并粘贴以下正文：

|  |
| --- |
| 你好 {{ $(‘Article Submission Form’).item.json.Name }}，我们无法访问你提交的 Google Doc。请检查文档共享设置是否为“任何拥有链接的人”（查看者）或已共享给我们的评审账户，然后重新提交。顺颂商祺，工作流团队 |

注意，{{ $(‘Article Submission Form’).item.json.Name }} 是引用之前节点数据的方式。你会经常用到这种模式。

Gmail 节点看起来是这样的：

![截图：Gmail "Send Email" 节点配置面板，显示填充了表达式的 To 字段、主题行和正文文本。](https://cdn.thenewstack.io/media/2026/05/ab11017c-5-1024x478.png)

*截图：Gmail “Send Email” 节点配置面板，显示填充了表达式的 To 字段、主题行和正文文本。*

目前的工作流如下所示：

![截图：画布上现在连接了五个节点，包括 IF 节点失败分支上的 Gmail 节点。](https://cdn.thenewstack.io/media/2026/05/e2c9a715-6-1024x388.png)

*截图：画布上现在连接了五个节点，包括 IF 节点失败分支上的 Gmail 节点。*

## 第 3 阶段：AI 评审

这是工作流的核心，也是将普通自动化转变为 AI 驱动自动化的关键步骤。

> “这是工作流的核心，也是将普通自动化转变为 AI 驱动自动化的关键步骤。”

放置一个 **AI Agent** 节点。将其连接到 IF 节点的 TRUE 输出。

![截图：在 TRUE 分支上添加了 AI Agent 节点的画布。尚未连接聊天模型或输出解析器。](https://cdn.thenewstack.io/media/2026/05/5d1d92b8-7.png)

*截图：在 TRUE 分支上添加了 AI Agent 节点的画布。尚未连接聊天模型或输出解析器。*

### 连接聊天模型

代理需要大脑才能运行。点击“Chat Model”选项并连接到 **OpenAI Chat Model**。你可以将此模型更改为你选择的任何其他模型，如 Anthropic 的 Claude 或 Gemini。在本教程中，我们将使用 OpenAI 模型。

你需要一个 OpenAI API 密钥。从你的 OpenAI 控制台获取一个，并在提示时将其粘贴到 n8n 的凭据面板中。

选择你的账户有权访问的任何模型。对于本教程，一个小型且便宜的模型效果很好（例如 *gpt-4o-mini* 或你账户中当前的任何小型模型）。你以后可以随时更换它。

### 提示词

这就是我们告诉 AI 代理我们想让它做什么的方式。我们希望我们的代理根据一套规则审查提交的文章。以下是你可以为此项目复制并粘贴的提示词。

|  |
| --- |
| 你是一位严格的、基于规则的文章评审员。仅根据以下规则进行评估。不要重写。如果不确定，标记为 PASS。仅输出有效的 JSON。规则：1. 字数：500 到 2000 字 2. 标题：句首大写，不得全大写，不得重复 3. 段落不超过 120 字 4. 句子不超过 30 字 5. 禁用词汇：“game-changing”, “revolutionary”, “next-gen”, “cutting-edge”, “leverage” 6. 代码安全：无硬编码密钥，无 SQL 拼接，无 eval() 7. 结构：3 个以上标题，首个标题前有引言，最后一个标题后有结论。如果全部通过，status = SUCCESS 且 message = 友好的成功邮件。如果有任何不通过，status = FAIL 且 message = 列出每个未通过规则及原因的邮件。待评审文章内容：””” {{ $(‘Get a document’).item.json.content }} |

现在根据需要调整这些规则。

### 连接结构化输出解析器

默认情况下，AI 会以消息风格进行回复，但我们只想要 JSON 结构，以便在工作流中使用。点击 AI 节点中的输出解析器，选择“Structured Output Parser”。在该部分中，选择“Define using JSON Schema”。在正文中添加该模式：

```
{
  "type": "object",
  "required": ["status", "message"],
  "properties": {
    "status": {
      "type": "string",
      "enum": ["SUCCESS", "FAIL"]
    },
    "message": {
      "type": "string",
      "description": "解释评审结果并列出问题（如有）的邮件风格草稿"
    }
  },
  "additionalProperties": false
}
```

现在，每个 AI 响应都有一个状态（SUCCESS 或 FAIL）和一个消息体。

就是这样。现在代理将评审工作流并给出裁决。

现在，工作流应该看起来像这样：

![截图：包含 Form Trigger、Google Docs、IF、Gmail（失败）、附带 Chat Model 和 Output Parser 子节点的 AI Agent 的完整画布。](https://cdn.thenewstack.io/media/2026/05/8d1aa96b-8.png)

*截图：包含 Form Trigger、Google Docs、IF、Gmail（失败）、附带 Chat Model 和 Output Parser 子节点的 AI Agent 的完整画布。*

在继续下一阶段之前，运行你的工作流以确保到目前为止的一切都运行顺畅。

## 第 4 阶段：编辑审批（发送并等待）

到目前为止，AI 已经评审了草稿并给出了裁决。现在我们需要[人工编辑](https://thenewstack.io/github-ceo-on-why-well-still-need-human-programmers/)在内容上线前签字。这种模式被称为“人机回环”。

在画布中放入一个 IF 节点。添加一个条件：Value 1 设置为 {{ $json.output.status }}，Operation 设置为 “Equals” (String)，Value 2 设置为 SUCCESS。

如果为 false，则添加 Gmail 节点以通知作者进行修改。

主题：需要采取行动：你的文章未通过评审检查

正文：{{ $json.output.message }}

以下是失败消息的样子。

![截图：邮件客户端收到的拒绝邮件，显示主题为 "需要采取行动：你的文章未通过评审检查"，正文列出了未通过的规则。](https://cdn.thenewstack.io/media/2026/05/954593d2-9-1024x435.png)

*截图：邮件客户端收到的拒绝邮件，显示主题为“需要采取行动：你的文章未通过评审检查”，正文列出了未通过的规则。*

如果文章通过了 AI 评审，我们将使用 Slack 让编辑进行最终审核。

在画布中放入一个 **Slack** 节点。将 Operation 设置为 **Send and Wait for Response**。该节点会将消息发布到 Slack，并暂停工作流，直到有人点击按钮。当编辑点击“Approve”（批准）或“Reject”（拒绝）时，n8n 会恢复工作流，并在下一个节点提供响应。

现在，你必须首先验证你的 Slack 凭据。点击“Connect to Slack”按钮进入 Slack 设置。

请注意，你必须拥有足够的权限才能为 n8n 提供 Slack 访问权限。

接下来，配置你的 Slack 选项。将 Resource 选择为“Message”。从频道下拉菜单中添加你的频道。在消息中粘贴格式化后的消息。

|  |
| --- |
| \*📄 文章已准备好进行最终评审\* \*标题：\* {{ $(‘Article Submission Form’).item.json.Title }} \*作者：\* {{ $(‘Article Submission Form’).item.json.Name }} \*草稿：\* {{ $(‘Article Submission Form’).item.json[‘Google docs link’] }} 请评审并确认是否可以发布。 |

请将响应类型选择为“Approval”，并同时选择“Approve”和“Reject”选项。这将允许 Slack 频道中的成员批准或拒绝该文章。

![截图：Slack 节点配置，选择了 "Send and Wait for Response" 操作，挑选了频道，并启用了 "Approve" 和 "Reject" 响应选项。](https://cdn.thenewstack.io/media/2026/05/c39b858e-10-1024x459.png)

*截图：Slack 节点配置，选择了“Send and Wait for Response”操作，挑选了频道，并启用了“Approve”和“Reject”响应选项。*

现在，你的工作流应该看起来像这样。

![截图：完整画布显示新的 IF 分支拆分为 Gmail（拒绝）和 Slack Send-and-Wait。](https://cdn.thenewstack.io/media/2026/05/a813deff-11.png)

*截图：完整画布显示新的 IF 分支拆分为 Gmail（拒绝）和 Slack Send-and-Wait。*

在继续下一步之前，请确保运行你的工作流。

你应该会看到一条 Slack 消息，类似于这样。

![截图：频道中实际的 Slack 消息，显示标题、作者、草稿链接以及 Approve/Reject 按钮。](https://cdn.thenewstack.io/media/2026/05/42aa0e98-12-1024x388.png)

*截图：频道中实际的 Slack 消息，显示标题、作者、草稿链接以及 Approve/Reject 按钮。*

## 第 5 阶段：发布到 CMS (Hashnode)

根据编辑的反馈，我们可以向作者发送拒绝邮件。如果文章获得批准，我们可以将其发布到 CMS。

到目前为止，你已经了解了 IF 节点。是时候测试这些知识了。在画布中放入 IF 节点，并检查文章是被批准还是被拒绝。

以下是条件：

* Value 1: {{ $json.approval\_status }},
* Operation: Equals (String),
* Value 2: approved

Slack 的 Send-and-Wait 节点会根据编辑点击的按钮返回一个 data.approved 布尔值。如果你的 n8n 版本中的数据结构看起来不同，请打开前一个节点的输出面板并从中复制正确的路径。

在 false 分支中，放入 Gmail 节点以发送拒绝邮件。以下是你可以使用的失败消息。

|  |
| --- |
| 你好 {{ $(‘Article Submission Form’).item.json.Name }}，感谢你提交标题为“{{ $(‘Article Submission Form’).item.json.Title }}”的文章。你的作品通过了我们的自动评审并送达编辑团队，这本身就是一项显著的成就。经过慎重考虑，我们的编辑决定暂不发布该作品。这并不代表你的努力或技能有问题。编辑决策取决于许多因素，包括当前的内容排期、受众契合度和话题时机。今天不适合的作品往往在其他地方能找到归宿，或者在以后以不同的角度呈现效果更好。我们非常感谢你与我们分享你的作品，并希望你将来考虑再次提交。顺颂商祺，工作流团队 |

如果文章获得批准，我们需要将其发布到 CMS。

对于此工作流，我们将使用 Hashnode 平台，但你可以使用任何你喜欢的 CMS。

在画布上添加一个 **HTTP Request** 节点。该节点用于调用外部 API。

首先，以正确的方式设置凭据。在 n8n 中，转到 Credentials > New > Header Auth 并创建一个凭据：

* Name: Authorization
* Value: Bearer YOUR\_HASHNODE\_TOKEN

现在配置 HTTP Request 节点：

* Method: POST
* URL: <https://gql.hashnode.com>
* Authentication: Generic Credential Type > Header Auth > (选择你刚刚创建的凭据)
* Send Headers: ON, 添加 Content-Type: application/json
* Send Body: ON
* Body Content Type: JSON
* Specify Body: Using JSON

将以下内容粘贴到 JSON 字段中：

```
{
"query": "mutation PublishPost($input: PublishPostInput!) { publishPost(input: $input) { post { url title } } }",
"variables": {
"input": {
"title": "{{ $('Article Submission Form').item.json.Title }}",
"contentMarkdown": "{{ $('Get a document').item.json.content }}",
"publicationId": "YOUR_PUBLICATION_ID"
}
}
}
```

将 YOUR\_PUBLICATION\_ID 替换为你的 Hashnode 发布 ID（你可以在 Hashnode 仪表板 URL 中找到它）。

使用 n8n 凭据而不是在请求头中硬编码令牌，意味着在你导出或共享工作流时，令牌永远不会泄露。

现在工作流应该看起来像这样：

![截图：完整画布，HTTP Request 节点添加到批准分支，连接在批准 IF 之后。](https://cdn.thenewstack.io/media/2026/05/f961eb35-13-1024x447.png)

*截图：完整画布，HTTP Request 节点添加到批准分支，连接在批准 IF 之后。*

现在，当你的工作流运行时，如果所有审批到位，它将发布到 Hashnode 平台。

我们快完成了——只需设置最后两个通知。

## 第 6 阶段：成功邮件和付款提醒

核心工作流已经完成。还剩两件事：告诉作者他们的文章已经上线，并提醒财务团队发放款项。

再放置一个 Gmail 节点并将其连接到 HTTP Request 节点。

在 Gmail 节点中使用以下正文：

|  |
| --- |
| 恭喜！你的文章“{{ $(‘Article Submission Form’).item.json.Title }}”已上线。在此阅读：{{ $json.data.publishPost.post.url }}。你将收到另一封包含付款详情的邮件。 |

![截图：在邮件客户端收到的成功邮件。](https://cdn.thenewstack.io/media/2026/05/87d8b821-1231-1024x415.png)

*截图：在邮件客户端收到的成功邮件*

放置一个 Slack 节点并将其连接到 HTTP Request 节点。

在这里，你需要选择财务团队的频道。

你可以使用以下消息：

|  |
| --- |
| :newspaper: \*新文章已发布 – 待付款\* \*作者：\* {{ $(‘Article Submission Form’).item.json.Name }} \*邮箱：\* {{ $(‘Article Submission Form’).item.json.Email }} \*URL：\* {{ $json.data.publishPost.post.url }} 请处理款项。 |

Slack 消息看起来会像这样：

![截图：财务频道中的 Slack 消息，显示报纸表情符号、作者姓名、邮箱和文章 URL。](https://cdn.thenewstack.io/media/2026/05/21cc4e93-14-1024x324.png)

*截图：财务频道中的 Slack 消息，显示报纸表情符号、作者姓名、邮箱和文章 URL。*

就是这样！这是你最终的 AI 工作流的样子：

![截图：完整的画布显示所有节点 - Form Trigger, Google Docs, IF (验证), Gmail (无效链接), AI Agent, IF (AI 裁决), Gmail (AI 拒绝), Slack Send-and-Wait, IF (编辑决定), Gmail (编辑拒绝), HTTP Request, Gmail (成功), Slack (财务提醒)。](https://cdn.thenewstack.io/media/2026/05/4fc32a26-15-1024x495.png)

*截图：完整的画布显示所有节点——Form Trigger, Google Docs, IF (验证), Gmail (无效链接), AI Agent, IF (AI 裁决), Gmail (AI 拒绝), Slack Send-and-Wait, IF (编辑决定), Gmail (编辑拒绝), HTTP Request, Gmail (成功), Slack (财务提醒)。*

恭喜，你刚刚构建了一个完整的内容自动化 AI 工作流。

## 还有一件事：错误处理

你的工作流将无人值守地运行。事情总会出错。API 可能会挂掉，令牌会过期，Slack 可能会触发速率限制。

> “你的工作流将无人值守地运行。事情总会出错。”

在将其投入生产之前，请设置 **Error Workflow**（错误工作流）。在 n8n 中，转到工作流的 Settings，滚动到 Error Workflow，然后选择（或创建一个）每当此工作流失败时就会启动的工作流。一个简单的错误工作流，只需将失败详情发布到 Slack 频道，就能在以后为你节省数小时的调试时间。

## 接下来该做什么

这只是构建一个完整的端到端 AI 工作流的一个例子。你几乎可以自动化任何领域的任何工作流。

在这个项目中，我们选择了 Gmail，但你也可以选择 Outlook。我们选择 Slack 作为即时通讯平台，但你也可以改用 Microsoft Teams。你可以利用手头所有的工具。

接下来可以尝试构建的一些想法：

1. [**GitHub PR**](https://thenewstack.io/what-github-pull-requests-reveal-about-your-teams-dev-habits/) **评审员：** 在拉取请求时触发，将 diff 发送给 AI 代理，并发布包含安全、漏洞和最佳实践发现的评审评论。
2. **潜在客户评分管道：** 从表单中获取潜在客户，使用 Clearbit 或 Apollo 进行富集，根据你的 ICP 使用 AI 进行评分，并将合格的客户推送到你的 CRM。
3. **会议行动项提取：** 在 Zoom 或 Fireflies 转录稿上触发，使用 AI 提取行动项，并将其发布到相关的 Slack 频道。

挑一个。在这个周末把它做出来。这才是你真正掌握 n8n 的方式。