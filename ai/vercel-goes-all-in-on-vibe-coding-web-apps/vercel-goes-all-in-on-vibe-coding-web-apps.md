
<!--
title: Vercel All in 氛围编程Web应用
cover: https://cdn.thenewstack.io/media/2025/08/a0bba8c6-pokemon_awesome_vercel.jpg
summary: Vercel 将 v0.dev 更名为 v0.app，旨在吸引非开发者用户。该工具通过 AI 代理将任务分解为子任务，简化 Web 应用构建。底层使用 Next.js、TypeScript 和 Tailwind，并支持自定义和集成第三方 API。Next.js 也在不断更新，以更好地与 LLM 和 AI 代理配合使用。
-->

Vercel 将 v0.dev 更名为 v0.app，旨在吸引非开发者用户。该工具通过 AI 代理将任务分解为子任务，简化 Web 应用构建。底层使用 Next.js、TypeScript 和 Tailwind，并支持自定义和集成第三方 API。Next.js 也在不断更新，以更好地与 LLM 和 AI 代理配合使用。

> 译自：[Vercel Goes All In on Vibe Coding Web Apps](https://thenewstack.io/vercel-goes-all-in-on-vibe-coding-web-apps/)
> 
> 作者：Loraine Lawson

[Vercel](https://thenewstack.io/creators-of-nuxt-js-and-nitro-join-vercel/) 今天推出了其 [v0 AI 驱动产品](https://vercel.com/blog/v0-app) 的新版本，将其名称从 .dev 更改为 .app，以反映其新的受众：最终用户。

“[Vercel 的 v0.app](https://v0.app/) 产品经理 Aryaman Khandelwal 在接受 The New Stack 采访时表示：“我们最初推出 v0 的想法是让开发人员的开发工作流程更轻松，但在构建 v0 的过程中，我们意识到，实际上，v0 更适合所有人。” “从 [v0.dev](https://thenewstack.io/frontend-ai-vercel-abstracts-model-chaos-in-one-interface/) 到 v0.app 的转变，实际上是我们推动 v0 更易于完全非技术人员使用的举措。”

他告诉 The New Stack，到目前为止，v0 拥有 300 万用户，并且每秒生成 6 个半应用程序，这意味着每天都在构建数十万个 Web 应用程序。

## Vercel 对 AI 工具的更新

Khandelwal 说，Vercel 做的第一个改变是更新用户界面，使其对不是“超级开发人员”的人们更易于访问。

第二个变化是，v0 可以为开发人员和最终用户执行操作，例如搜索互联网或添加集成，而不仅仅是生成代码。 它可以创建一个完整的堆栈应用程序，包括用于前端的反应式 UI 和后端连接（例如数据库）。

“基本上，我们认为 v0 涵盖了您在构建 Web 应用程序时想要做的所有事情，”他说。“我不建议使用 v0 来构建没有 UI 的纯后端框架。”

尽管它可以做一些这样的事情，但他补充说。 他说，人们已经使用它来编写“非常酷的 API”，但 v0.app 的超能力实际上是构建网站和应用程序。

新的 v0.app 可以执行：

* **Web 搜索：** 它搜索 Web，处理故障并返回带有引用的结果。
* **文件读取：** 它读取文件并返回其内容。
* **站点检查：** 它检查实时站点，拍摄屏幕截图并总结发现。
* **设计灵感：** 它根据提示生成带有描述的图像概念。 例如，我只是要求它在我的待办事项站点中添加一个以时间为主题的图像，它就弹出了一个。 但它还允许上传徽标、产品信息甚至品牌指南，并且计划在未来推出更多功能，使品牌推广更加容易，他说。
* **待办事项管理：** 它跟踪任务，更新计划并输出技术细分。
* **工作检查：** 它发现错误，比较实现并通过结果进行推理。
* **集成：** 它支持集成，包括从 Vercel 的托管选项列表中添加数据库的选项。 它还可以添加其他工具，包括 AI 工具，例如 Vercel 市场目前提供的 [Grok](https://grok.com/)。 它还支持第三方 API 集成，因此企业可以选择连接到他们自己的后端系统。

## 为什么 Vercel 要争取非开发人员

显然，这不是 Vercel 在推出 v0.dev 时最初的目标，v0.dev 的目标是前端和 [Web 开发人员](https://roadmap.sh/roadmaps?g=Web+Development)。 第一个版本侧重于创建代码。

“我们了解开发人员。 我们的市场一直是面向开发人员的，”Khandelwal 说。“我们最初将其构建为开发人员工具。 我们使其非常技术性。”

但他说，自部署以来的过去两年中，Vercel 看到的是，开发人员周围的人员（设计师、营销人员、销售工程师、产品经理）使用该工具的次数超出了 Vercel 的预期。

他补充说，这种转变主要来自客户。

“我们实际上发现，有更多的用户来自那些开发人员相邻的角色，他们从 v0 中获得了很大的价值，”Khandelwal 说。“我们并没有真正很好地为他们服务，这就是这种转变的动力来源。”

## 从 LLM 到 Agentic AI，或从瀑布到敏捷

[大型语言模型 (LLM)](https://thenewstack.io/introduction-to-llms/) 主要使用更瀑布式的方法进行开发：您输入一个命令，它会尝试一次性完成某些操作，或者直接失败。 为了使 v0 更加用户友好，该工具现在调用 [AI 代理](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)，而不仅仅是一个 LLM。

这种代理方法使其能够采用更 [敏捷](https://thenewstack.io/ai-in-agile-managing-the-unpredictable-in-iterative-development/) 的方法，将命令分解为子任务，因此它可以非常快速地迭代应用程序。 Khandelwal 说，这使得它对非技术用户来说既简单又强大。

“它会说，‘嘿，我首先需要创建 UI，然后我需要添加数据库，然后我需要添加关闭，然后我需要进行润色’，事实证明，像真人一样逐步执行操作，实际上会大大降低错误率，”他说。

它还允许 v0 迭代您正在部署的任何 Web 应用程序。 我只用了几次尝试，几秒钟到几分钟的时间，就开发了一个带有图像的基本待办事项列表。 如果您对更复杂的应用程序感到好奇，请查看 [Pokémon Awesome!](https://pokemon-awesome.vercel.app/)，这是一个 v0 部署的应用程序。 在 [v0.app 的主页](https://v0.app/) 上有更多。

[![使用 Vercel v0.app 制作的每日计划器](https://cdn.thenewstack.io/media/2025/08/bebe9721-easy_vercel_app.jpg)](https://cdn.thenewstack.io/media/2025/08/bebe9721-easy_vercel_app.jpg)

*我的每日计划器，使用 Vercel v0.app 制作。*

我大部分的工作时间实际上都花在了尝试让 [GitHub](https://thenewstack.io/github-launches-its-coding-agent/) 保存我网站的新迭代上，我觉得这更多的是一个“我的问题”，而不是 Vercel 的问题。 AI 最终能够识别问题（或用户错误）并告诉我如何纠正它。

“现在发生了两件事，用户在第一次或第二次提示时会发现，”Khandelwal 说。

他说，第一件事是 v0.app 犯的错误更少，尤其是在非常非常复杂的提示下。 他补充说，第二件事是它实际上比 v0.dev 的代码创建方法更快。

以前，Vercel 必须“限制”原始 v0，以使其不会一次做太多事情。 它被告知执行用户要求的最低限度的操作，以免破坏应用程序。

“通常，发生的情况是 v0 会尝试一次性完成所有操作，并且当它尝试一次性完成所有操作时，错误率会更高，”他说。 现在，v0 将自动分解这些较小的步骤。

## 在 AI 的底层：让我们谈谈框架

我问 Khandelwal v0.app 在底层做了什么：例如，它是否默认为 [Next.js](https://thenewstack.io/next-js-deployment-spec-simplifies-frontend-hosting/)，这是由 Vercel 开发和部署的微框架？ 如果您不要求使用特定的框架，他承认，它确实使用 Next.js。

“我们尽量只在必要时才公开复杂性，”他说。“因此，如果您不要求使用特定的技术堆栈或任何东西，我们将 [为您构建一个 Web 应用程序](https://thenewstack.io/web-devs-meet-the-ai-apps-youll-build-next/)。 它将使用 Next.js，它将用 [TypeScript](https://thenewstack.io/typescript-5-9-brings-less-friction-more-features/) 编写，并且它将使用 [Tailwind](https://thenewstack.io/astro-5-2-brings-tailwind-4-support-and-new-features/) 进行样式设置。”

他补充说，这些是可用于 Web 开发的“最现代的技术”。

“今天，该行业正在朝着标准化这些技术方向发展，我们使用此堆栈中每个部分的最新版本，”他说。“如果您什么都不要求，您是一个非技术人员，您真的不在乎它是用什么构建的。 我们将为您提供最先进的技术并为您构建它。”

但是，如果您更精通技术，则可以自定义代码。 例如，您可以要求使用原始 CSS 而不是 Tailwind。 它可以生成静态 HTML 和 CSS 站点。 他说，它甚至可以生成原始 React。

> “我们尽量只在必要时才公开复杂性。 因此，如果您不要求使用特定的技术堆栈或任何东西，我们将为您构建一个 Web 应用程序。 它将使用 Next.js，它将用 TypeScript 编写，并且它将使用 Tailwind 进行样式设置。”
>
> **— Aryaman Khandelwal, Vercel**

该工具还支持其他微框架。 最近，Vercel 推出了对 [Svelte](https://thenewstack.io/svelte-adds-asynchronous-sync-inside-components/) 的改进支持，允许 **氛围编程** 人员生成 Svelte 应用程序并使用许多通常适用于 Next.js 的工具。

“我们并没有非常专注于改进对 Vue 和 Angular 以及其他一些元 JavaScript 框架的支持，但总的来说，我们可以使用它们生成代码，”Khandelwal 说。“我们尽量做到为您挑选真正、真正好的默认设置，如果您不知道并且您真的不在乎。 但是如果您愿意，您始终可以对其进行更多自定义。”

该工具还包含一个代码编辑器选项卡，因此开发人员仍然可以进入并更改或修复代码（如果需要）。 它还允许您将代码发送到您的 IDE，并且正如我之前提到的，它可以与 GitHub 存储库同步。

“您始终可以执行推送到 git 的操作，并且 v0 实际上会更新您正在处理的应用程序，”他说。“因此，您实际上可以在 IDE 中访问完整的开发工作流程。”

## v0.app 正在改变 Next.js 框架

Vercel 内部还有另一个有趣的动态：Next.js 团队正在 [更新框架](https://thenewstack.io/what-developers-told-us-about-vercels-next-js-update/)，以便它可以更好地与 LLM 和代理 AI 配合使用，Khandelwal 说。

“我们与 Next.js 团队的合作非常密切，”他说。“事实上，我们是 Next.js 的非常好的客户——我们向他们提供了很多关于好例子或诸如‘LLM 似乎不理解此语法’或‘似乎不理解框架中的此模式’之类的反馈。”

该团队将要求提供更好的文档，或者是否可以简化或更改情况。

例如，有客户端日志和服务器端日志。 通常，客户端日志位于浏览器控制台中，而服务器端日志显示在终端中。 但是，LLM 通常只能访问终端。

因此，v0 团队告知 Next.js 团队，他们需要在两个位置都提供日志以支持代理 AI 开发。

Khandelwal 说：“实际上，我们可以与 Vercel 和 Next.js 建立一种非常酷的共生关系，我们可以向他们提供非常好的反馈，说明我们如何使这些工具更好用，并适用于像这样的**氛围编程**平台。”