AI 有其用武之地。

然而，重要的是将 AI 限制在其范围内，否则它将失控并被用作一切事情的捷径（尤其是在创意艺术领域）。

话虽如此，我为什么要谈论一种可以为那些没有编程经验的人构建应用程序的代理 AI 服务呢？

这绝对是一个具有挑战性的论点。为什么？因为 AI 已经开始让很多人失业。随着越来越多的开发人员发现自己被机器取代，企业将在哪里寻找新的应用程序呢？

这是一个递归的噩梦。

如果您发现自己站在业务的角度，需要构建一个应用程序来帮助您的公司蓬勃发展，并且在寻找构建者时遇到麻烦，那么总有 [Firebase Studio](https://thenewstack.io/your-ai-coding-buddy-is-always-available-at-2-am/)。

## 什么是 Firebase Studio？

Firebase Studio 是一个基于云的[代理开发环境](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/)，由 [Google](https://cloud.google.com/?utm_content=inline+mention) 创建，旨在帮助简化构建和部署 AI 驱动的应用程序。该服务为原型设计、构建和发布应用程序提供了一站式商店。这种 [无代码](https://thenewstack.io/no-code-is-dead/) 解决方案与 [Google 的 Gemini](https://thenewstack.io/qa-how-google-itself-uses-its-gemini-large-language-model/) 集成，以帮助进行代码生成、[应用程序原型设计](https://thenewstack.io/microsoft-builds-autogen-studio-for-ai-agent-prototyping/) 等。

Firebase 是一个全栈开发平台，支持前端和后端开发，甚至与身份验证、Firestore 和 Hosting 等服务集成。

使用 Firebase，您可以通过 AI 提示构建应用程序。想象一下，仅使用自然语言构建一个强大的应用程序。如果这还不够，您还可以使用传统的基于代码的开发，并使用流行的框架，例如 [Next.js](https://thenewstack.io/next-js-deployment-spec-simplifies-frontend-hosting/)。

您可以从 60 个预构建的模板开始，也可以使用 App Prototyping 代理。

我测试了 App Prototyping 代理，并且印象 *非常* 深刻。我所做的是要求 Firebase Studio 构建一个与 Google 日历集成的 [看板](https://www.atlassian.com/agile/kanban) 应用程序。在我输入我的提示后，Firebase Studio 提出了一个更详细的提示，即：

> “一个用于项目和任务管理的协作看板应用程序。主要功能包括在可自定义的看板上创建和组织任务，添加带有附件和完全可自定义的数据字段的卡片，与 Google 日历集成以获取任务截止日期，以及在列之间拖动卡片以更新状态。使用平静的蓝绿色和专业的灰色配色方案。”

接下来是应用程序蓝图（将包含的功能列表），即：

* **看板创建：** 创建和自定义多个看板，以管理不同的项目或工作流程。
* **卡片管理：** 将卡片添加到看板以表示任务；使用受让人、描述、截止日期、附件和完全可自定义的数据字段自定义每个卡片。
* **Google 日历集成：** 连接 Google 日历以同步任务截止日期，提供提醒和统一的日程视图。
* **拖放界面：** 在列之间拖放卡片以更新其状态（例如，待办事项、进行中、已完成）。
* **更改通知：** 当任何卡片发生更改时，为协作者生成通知，以确保同步的协作流程。
* **AI 资源建议：** 基于分析卡片上下文和内容，AI 工具会建议相关和相关的资源，以促进更简化的卡片开发。

到目前为止，情况看起来还不错。然后，Firebase Studio 建议了以下应用程序堆栈：

* **AI：** Gemini, Genkit
* **UI：** [TypeScript](https://thenewstack.io/what-is-typescript/), NextJS, Tailwind CSS

是时候进行原型设计了，只需单击一下即可完成。

在原型设计之后，我意识到我需要一个 Gemini API 密钥（图 1）。

[![](https://cdn.thenewstack.io/media/2025/07/059d9b8e-screenshot-2025-07-29-at-2.13.07%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/07/059d9b8e-screenshot-2025-07-29-at-2.13.07%E2%80%AFpm.png)

图 1. 如果没有 Gemini API 密钥，看板将无法按需运行。

幸运的是，有一个自动生成按钮可以实现此目的。单击自动生成后，Firebase Studio 完成了它的工作，我有了我的密钥。解决了这个问题后，我可以测试该应用程序以查看其运行情况，并且令人惊讶的是，它非常令人印象深刻。

## 如何调整应用程序？

任何创建过任何东西的人都知道，第一次尝试很少是最后一次。虽然我的看板应用程序运行良好，但可能需要进行更改。构建应用程序后，您会在窗口的右下角找到一个“编辑代码”按钮。单击该按钮，您将看到一个侧边栏，其中列出了为该应用程序创建的每个文件。展开其中一个条目，单击一个文件，它将在代码编辑器中打开（图 2）。

[![](https://cdn.thenewstack.io/media/2025/07/6ea2dc60-screenshot-2025-07-29-at-2.19.25%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/07/6ea2dc60-screenshot-2025-07-29-at-2.19.25%E2%80%AFpm.png)

图 2. Firebase Studio 代码编辑器。

如您所见，仍然需要开发人员技能，因为与所有 AI 一样，会犯错误，并且 *始终* 有改进的空间。

根据需要编辑代码，然后在完成后，单击“重建环境”按钮以应用您的更改。重建环境后，再次测试它，以查看它现在是否满足您的需求（或您客户的需求）。

## 构建后选项

一旦您对您的应用程序感到满意，您就有几个选项。

### 压缩和下载

您可以按照以下步骤创建 zip 存档并下载您的项目：

1. 在您的项目中，导航到代码视图。
2. 在文件资源管理器窗格中的空白区域单击鼠标右键，然后选择“压缩并下载”选项。
3. 出现提示时，将下载文件保存到您的本地计算机。

### Git 集成

您可以将您的项目与各种 [Git](https://thenewstack.io/linus-torvalds-reflects-on-20-years-of-git/) 提供商（例如 GitHub 和 [GitLab](https://about.gitlab.com/?utm_content=inline+mention)）集成，因此您可以将您的代码推送到您选择的存储库。推送代码后，您可以使用标准的 Git 命令和工具将其克隆到您的本地计算机。

### Firebase App Distribution（用于测试版本）

测试人员可以通过 Firebase App Distribution 下载应用程序的特定版本。当然，这是用于测试目的，并将下载完全编译的应用程序（例如，Android 的 APK 和 iOS 的 IPA）。如果您单击右上角附近的链接图标，您将获得一个可以在手机上扫描的 QR 码（图 3）。扫描后，它将在手机上打开您的应用程序，因此可以在 Android 或 iOS 上进行测试。

[![](https://cdn.thenewstack.io/media/2025/07/e796d2a3-screenshot-2025-07-29-at-2.36.54%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/07/e796d2a3-screenshot-2025-07-29-at-2.36.54%E2%80%AFpm.png)

图 3. 这是您可以在手机上尝试的我的测试看板应用程序。

Firebase Studio 还有很多功能，但这将让您对它的工作方式有一个很好的了解。我建议您在第一次浏览后阅读 [这篇 Google 文档](https://cloud.google.com/blog/products/application-development/firebase-studio-lets-you-build-full-stack-ai-apps-with-gemini) 以了解更多信息。