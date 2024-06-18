
<!--
title: 如何利用Next.js通过React将Google表格用作数据库
cover: https://cdn.thenewstack.io/media/2022/10/86c3c639-shutterstock_1121158061.jpg
-->

如何通过 React 将 Google Sheets API 用作数据库。出于一个原因，选择此方法而不是更传统的数据库：数据检索。

> 译自 [How To Use Google Sheets as a Database With React via Next.js](https://thenewstack.io/how-to-use-google-sheets-as-a-database-with-react-and-ssr/)，作者 Paul Scanlon。


在本教程中，我将解释如何将 Google 表格用作数据库来存储用户投票结果。我已将此 [React](https://thenewstack.io/learn-react-start-of-a-frontend-dev-journey/) Google 表格方法用于多项营销活动。我选择此方法而不是更传统的数据库解决方案，原因只有一个：数据检索。

当然，这完全取决于你的要求，但能够简单地与团队的技术或非技术成员共享 Google 表格（以便他们可以轻松查看捕获的数据），在很多情况下已被证明非常有价值。

![](https://cdn.thenewstack.io/media/2022/10/7462cbbb-tns-google-sheets-database-app-screenshot-1024x640.jpg)

数据从浏览器发送到Server Action ，该操作安全地发布到 Google 表格，后者存储数据。要使用 [React 中的Server Action ](https://thenewstack.io/how-to-build-a-server-side-react-app-using-vite-and-express/)，我将使用 [Next.js](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations)。

在以下链接中，你将找到已完成的用户投票应用程序的实时预览和 GitHub 存储库。

- [https://nextjs-google-sheets-database.vercel.app](https://nextjs-google-sheets-database.vercel.app)
- [https://github.com/PaulieScanlon/nextjs-google-sheets-database](https://github.com/PaulieScanlon/nextjs-google-sheets-database)

我不会介绍如何开始使用 Next.js，因此如果你不熟悉如何使用 Next.js，请查阅 [文档](https://nextjs.org/docs)。

## 什么是 Server Actions？

Server Action 是在服务器上执行的异步函数。它们可以在 React 服务器和客户端组件中用于处理表单提交和 [Next.js 应用程序](https://thenewstack.io/next-js-13-debuts-a-faster-rust-based-bundler/) 中的数据突变。

使用 Server Action 允许你将数据从 [前端](https://thenewstack.io/frontend-development/) POST 到同一项目中的 [后端](https://thenewstack.io/why-backend-developers-should-fall-in-love-with-graphql-too/)。然后可以使用Server Action 将数据安全地插入到数据库中，或者在本例中插入到 Google 表格中。

使用 Next.js 实现此目标的方法是拥有一个页面来处理向Server Action 发送请求，以及一个Server Action 来处理接收请求并执行插入。

## Next.js Server Action 示例

该页面保存在 **app/some-page/page.tsx** 中，并向保存在 **app/some-page/some-action.ts** 中的操作发送请求。

你可以在以下链接中看到此简单示例的 src：

- [some-page/page.tsx](https://github.com/PaulieScanlon/nextjs-google-sheets-database/blob/main/app/some-page/page.tsx)
- [some-page/some-action.ts](https://github.com/PaulieScanlon/nextjs-google-sheets-database/blob/main/app/some-page/some-action.ts)

在此示例中，Server Action 只是返回在调用操作时传入的 id 字符串。在用户投票示例中，该操作将对 Google 表格数据库执行插入并重定向到结果页面，在该页面中使用第二个操作来检索准备显示的数据。

但在开始编写任何代码之前，你需要完成所有 Google 设置步骤。

## 如何设置 Google 表格

在开始使用 Google 表格之前，首先需要设置 Google 所称的服务帐户。你可以在 Google 文档中阅读有关服务帐户的更多信息：[了解 Google 服务帐户](https://cloud.google.com/iam/docs/service-account-overview)。

## 创建 Google Cloud 项目

第一步是创建一个项目。你将配置此项目，以便它可以通过服务帐户用户/电子邮件地址授予对 Google 表格 API 的访问权限，并使用它来生成将数据“发布”到 Google 表格所需的 API 密钥。

在以下指南中概述了创建 Google Cloud 项目的步骤：[使用 Google Cloud 控制台授予 IAM 角色](https://cloud.google.com/iam/docs/grant-role-console)

从上述链接开始，单击 **转到项目选择器** 按钮。

![](https://cdn.thenewstack.io/media/2022/10/d82aa8b7-tns-google-sheets-database-project-selector-1024x640.jpg)

现在单击 **创建项目**。

![](https://cdn.thenewstack.io/media/2022/10/6b0a31b8-tns-google-sheets-database-create-project-1024x640.jpg)

为你的项目命名，然后单击 **创建**。

![](https://cdn.thenewstack.io/media/2022/10/1c329795-tns-google-sheets-database-project-name-1024x640.jpg)

你现在应该被重定向到项目信息仪表板。单击侧边栏中的 **API 和服务** 导航项。

![](https://cdn.thenewstack.io/media/2022/10/04b16d97-tns-google-sheets-database-project-dashboard-1024x640.jpg)

要启用对 Google 表格 API 的访问，请单击 **+ 启用 API 和服务** 按钮。

![](https://cdn.thenewstack.io/media/2022/10/434324b3-tns-google-sheets-database-enable-api-1024x640.jpg)

搜索“google sheets api”，然后选择 **Google Sheets API**。

![](https://cdn.thenewstack.io/media/2022/10/ff536145-tns-google-sheets-database-google-sheets-api-1024x640.jpg)

要启用对 Google 表格 API 的访问，请单击 **启用** 按钮。

![](https://cdn.thenewstack.io/media/2022/10/769f78ac-tns-google-sheets-database-enable-google-sheets-1024x640.jpg)

要为 Google 表格 API 创建必要的凭据，请单击 **创建凭据** 按钮。

![](https://cdn.thenewstack.io/media/2022/10/d44f911e-tns-google-sheets-database-create-credentials-1024x640.jpg)

选择 **Google Sheets API** 并选中 **Application Data** 单选按钮。你可以跳过 **Your Credentials** 部分，只需单击 **DONE** 按钮。

![](https://cdn.thenewstack.io/media/2022/10/8f4486fa-tns-google-sheets-database-credentials-type-1024x640.jpg)

单击侧边栏中的 **IAM & Admin** 导航项，然后单击 **Service Accounts**。

![](https://cdn.thenewstack.io/media/2022/10/02e5ffb7-tns-google-sheets-database-service-account-1024x640.jpg)

单击 **+ CREATE SERVICE ACCOUNT** 以创建新的服务帐户。

![](https://cdn.thenewstack.io/media/2022/10/c713a9ea-tns-google-sheets-database-create-service-account-1024x640.jpg)

通过为你的项目创建一个服务帐户来创建它，方法是为其提供一个名称和一个显示名称。
**Service account name**、**Service account ID** 和 **Service account description**。准备就绪后，单击 **CREATE AND CONTINUE**。

![](https://cdn.thenewstack.io/media/2022/10/fa8f163c-tns-google-sheets-database-service-account-details-1024x640.jpg)

将 **Role** 设置为所有者，然后单击 **CONTINUE**。

您可以跳过最后一步，并在准备就绪时单击
**完成**。

检查服务帐号详细信息的权限是否正确。

在同一屏幕上，单击更多点，然后选择
**管理密钥**。

在
**密钥** 选项卡上，单击 **添加密钥** 按钮，然后单击 **创建新密钥**。

选择
**JSON** 作为密钥类型，然后单击 **创建** 按钮下载包含密钥的 .json 文件。

您刚刚下载的 .json 文件看起来有点像下面这样。您需要将作为环境变量保存的两个密钥是。
**priviate_key** 和 **client_email**。

在示例存储库中，我创建了以下环境变量。

您可以在以下链接上阅读有关为 Next.js 配置环境变量的更多信息：

## 创建 Google 表格

创建一个新的 Google 表格，复制
**id** 在 URL 地址栏中，并将其添加到您的环境变量中。

## 向 Google 表格添加列标题

您可以根据需要添加任意多个标题。值得注意的是，空格将替换为下划线。

## 共享 Google 表格

使用您的新表格创建后，将其与您的服务帐号电子邮件地址/ .json 文件中的
**client_email** 共享。确保服务帐号具有 **编辑者** 访问权限。

## 创建用户投票

要创建用户投票，投票和结果页面都有一个页面、布局和Server Action 。

在以下步骤中，我将解释如何创建每个步骤。存储库中以下分支上提供了用户投票的非样式化版本：

[example/minimal](https://github.com/PaulieScanlon/nextjs-google-sheets-database/tree/example/minimal)。这仅包含您将在以下步骤中看到的代码。

## 服务和实用工具

除了“页面”之外，您还需要配置
[google-spreadsheet](https://www.npmjs.com/package/google-spreadsheet)、[google-auth-library](https://www.npmjs.com/package/google-auth-library) 和包含界面中显示的标题的投票配置。

### 服务

安装以下依赖项：

在项目根目录创建一个新目录，并将其命名为
**services**。

创建一个名为
**google-spreadsheet.ts** 的新文件，并添加以下代码：

您可以在
[文档](https://theoephraim.github.io/node-google-spreadsheet/#/) 中阅读有关
[google-spreadsheet 的更多信息。

### 实用工具

界面中显示的标题和 id 可以更改以适应您的特定要求；只需确保它们与 Google 表格中的标题匹配即可。

在项目根目录创建一个新目录，并将其命名为
**utils**。

创建一个名为
**poll-config.ts** 的新文件，并添加以下代码。每个 id 应与 Google 表格中的列标题匹配。名称是将在用户界面中显示的内容。

## 投票

### 创建投票页面

在名为 app 的目录中创建一个新文件
**page.tsx**，并添加以下代码：

此页面包含一小部分 React
useState，以便在请求进行中时禁用按钮。要在 Next.js 中启用客户端 React，可以使用
use client 指令。

通过使用
array.map 遍历配置中的项目并返回每个项目的按钮来创建列表。向每个按钮添加
onClick 处理程序，该处理程序调用
handleClick 函数并传递
config 中的
id。

### 创建投票布局

在名为 app 的目录中创建一个新文件
**layout.tsx**，并添加以下代码：

这是投票页面的标准布局，您可以根据需要更改元数据。

### 创建投票Server Action 

在名为 app 的目录中创建一个新文件
**submit-vote.ts**，并添加以下代码：

此Server Action 负责接收页面请求中发送的 id，并使用它找到正确的单元格并将计数增加
+ 1。

如果对 Google 表格的更新成功，它将重定向到
[/results](https://nextjs-google-sheets-database.vercel.app/results)。如果出现错误，它将重定向到索引页面，但会附加一个搜索参数
error=true，该参数确定是否
[显示页面中的错误消息](https://nextjs-google-sheets-database.vercel.app/?error=true)。

## 结果

在名为 app 的目录中创建一个新目录
**results**。

### 创建结果页面

在名为 results 的目录中创建一个新文件
**page.tsx**，并添加以下代码：

此页面是服务器呈现的，不包含任何 React
useState，因此不需要使用 client 指令。与之前不同，在此组件中，我迭代 get-all-votes Server Action （我将在后面介绍）发回的结果，并为每个项目返回进度指示器、名称和百分比。

### 创建结果布局

在名为 results 的目录中创建一个新文件
**layout.tsx**，并添加以下代码：
### 这是结果页面的标准布局；您可以根据需要更改元数据。

### 创建结果Server Action 

在应用程序目录中创建一个名为 **get-all-votes.ts** 的新文件，并添加以下代码：

此Server Action 负责查询 Google 表格中的所有数据，遍历每个值以生成每个项目的总计、最大值和百分比。然后返回这些值，以便结果页面使用。

## 完成

就是这样，您现在拥有一个用户投票应用程序，它将数据存储在 Google 表格中，任何有权访问的人都可以共享和查看。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。