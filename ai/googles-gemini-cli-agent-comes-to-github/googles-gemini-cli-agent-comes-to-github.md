
<!--
title: 谷歌 Gemini CLI Agent 登陆 GitHub
cover: https://cdn.thenewstack.io/media/2025/04/c90e05a8-img_3909-edit.jpg
summary: Google的开源AI代理Gemini CLI推出GitHub Actions，允许开发者在GitHub问题中标记该代理，以自动化代码审查、问题分类等任务。该工具免费使用，但API调用和GitHub Actions可能收费。它与GitHub和Anthropic的类似工具有竞争，并侧重于团队协作。
-->

Google的开源AI代理Gemini CLI推出GitHub Actions，允许开发者在GitHub问题中标记该代理，以自动化代码审查、问题分类等任务。该工具免费使用，但API调用和GitHub Actions可能收费。它与GitHub和Anthropic的类似工具有竞争，并侧重于团队协作。

> 译自：[Google's Gemini CLI Agent Comes to GitHub](https://thenewstack.io/googles-gemini-cli-agent-comes-to-github/)
> 
> 作者：Frederic Lardinois

[Gemini CLI](https://cloud.google.com/gemini/docs/codeassist/gemini-cli)，[Google](https://cloud.google.com/?utm_content=inline+mention) 的开源 AI 代理，开发者可以通过终端访问，并与 [Claude Code](https://thenewstack.io/claude-code-user-base-grows-300-as-anthropic-launches-enterprise-analytics-dashboard/) 等工具竞争。现在，Gemini CLI 正通过推出 [Gemini CLI GitHub Actions](http://google-github-actions/run-gemini-cli) 走出命令行，进入 GitHub。开发者将能够在他们的 GitHub 问题中标记该代理，Gemini 将开始异步处理该问题，无论是错误修复还是向现有应用程序添加新功能。该工具使用 GitHub 的 CI/CD 平台 GitHub Actions 作为其计算服务。

[Ryan J. Salva](https://www.linkedin.com/in/ryanjsalva/)，Google 负责开发者体验的产品高级主管指出，Google 启动这个项目是因为在 Gemini CLI 发布后收到了太多的贡献和功能请求，以至于团队开始自动化他们在 GitHub 中所做的很多事情。

“社区碰巧注意到了。他们碰巧看到了我们正在做的事情，并希望自己也使用这些相同的工具，”他在 Google Cloud Next Tokyo 大会今日发布前的记者招待会上说。“它是一个自主代理，可以处理你在 GitHub 内部必须执行的所有常见的日常任务，无论是问题分类、执行代码审查，或者坦率地说，打开各种限制，使其成为你可以委托的各种任务的通用按需协作者。”

该代理将允许开发者设置自动化，以便在新问题提交、拉取请求提交，甚至问题获得新标签时调用该代理。

“通过自动化这些 SDLC [软件开发生命周期] 事件，你可以有效地将管理该 SDLC 的所有工作委托给 CLI，”Salva 说。

要开始使用，用户需要安装 Gemini CLI 工具并运行“/setup-github”。

该代理本身的使用将是免费的，但是你需要提供你的 Google API Studio API 密钥，并且一旦你用完免费套餐，你将需要为 API 使用付费。GitHub Actions 是该代理工作的地方，一旦你用完免费套餐，它也会按分钟收费。Vertex AI 用户以及 Gemini Code Assist 的标准版和企业版用户也将可以访问该服务。

免费版 Code Assist 的个人用户也将很快可以使用该新工具。

Salva 指出，使用 GitHub Actions 的优势还在于，每当打开 Gemini CLI 的实例时，GitHub Actions 都会启动一个新的容器，将该进程与平台上发生的其他一切隔离开来。

在安全方面，该服务使用 Google Cloud 的工作负载身份联合，从而无需长期存在的 API 密钥，并允许细粒度的访问控制，因此开发者可以确保该代理仅可以访问特定分支，例如。

“锁定它并赋予其最小权限可确保你在以自主方式使用 Gemini CLI 时，不会危及任何数据泄露或自动销毁，”Salva 说。

现在，如果所有这些听起来有点熟悉，那可能是因为你听说过 [GitHub 自己的编码代理](https://thenewstack.io/github-launches-its-coding-agent/)，该代理于 5 月份发布。GitHub 代理也是一个软件工程 (SWE) 代理，可以在 GitHub 生态系统内部异步工作。

同样，Anthropic 最近也演示了其 Claude Code 代理如何与 GitHub Actions 一起工作。[Claude Code GitHub Actions 工具](https://docs.anthropic.com/en/docs/claude-code/github-actions) 目前处于 Beta 版。Augment Code 最近也推出了一个异步代理（或者该公司称之为“[远程代理](https://thenewstack.io/augment-codes-remote-agents-code-in-the-cloud/)”）。

GitHub 正在为其代理使用 Anthropic 的 Claude Sonnet 模型，而 Google 显然正在使用自己的 Gemini 模型。

与 GitHub 一样，Google 还指出，它的工具侧重于团队协作，因为 GitHub 是软件开发团队聚集的地方。但是，没有理由独奏开发者不想尝试它。

由于它在 GitHub 中运行，因此它可以与给定项目的完整上下文一起使用。

在一个演示中，Google 展示了开发者如何在问题中标记该代理，然后该代理会回复一个完成该任务的计划。获得批准后，该代理会在后台工作（尽管开发者始终可以完全了解该代理所做的事情），并检查该计划中的待办事项。

值得注意的是，这并不是 Google 首次尝试将代理引入 GitHub 生态系统。[Gemini Code Assist for GitHub](https://blog.google/technology/developers/gemini-code-assist-free/) 毕竟是在 2 月份发布的。但是正如 Salva 指出的那样，该项目仅侧重于代码审查，没有任何其他功能。

“开发者正在寻找一种更通用的工具，该工具可以用于各种用例，不仅限于代码审查，还可以用于各种 SDLC 中的自动化事件，”他说。“因此，Gemini CLI 通过提供一个可推广的代理来打开更多可能的用例。碰巧的是，构建现有代码审查代理和 Gemini CLI 的团队是同一个团队。它们都在我的组织内，因此我们正在考虑长期融合。”

> [GitHub 发布其编码代理](https://thenewstack.io/github-launches-its-coding-agent/)