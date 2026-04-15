<!--
title: Claude Code 现可实现夜间自动办公
cover: https://cdn.thenewstack.io/media/2026/03/39e0e580-004-login-1024x665.png
summary: Anthropic 为 Claude Code 推出“例行程序”功能，支持通过定时、API 或 GitHub 事件触发自动化任务。该功能在云端自主运行，可处理 Issue 分拣、文档更新和持续部署等工作。
-->

Anthropic 为 Claude Code 推出“例行程序”功能，支持通过定时、API 或 GitHub 事件触发自动化任务。该功能在云端自主运行，可处理 Issue 分拣、文档更新和持续部署等工作。

> 译自：[Claude Code can now do your job overnight](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/)
> 
> 作者：Frederic Lardinois

周二，Anthropic 为 Claude Code 发布了一个备受期待的功能：[例行程序 (routines)](https://claude.com/blog/introducing-routines-in-claude-code)。

核心理念是，你现在可以按计划运行给定的提示词，或者基于 GitHub 事件（使用 webhook）以及来自你自己代码的 API 触发。

在今年早些时候的一次更新中，Anthropic 在其命令行工具中引入了 [`/schedule` 命令](https://code.claude.com/docs/en/scheduled-tasks)，允许开发者在设定的时间或间隔运行提示词。这与之相似，但又有所不同。

“例行程序是你配置一次即可的 Claude Code 自动化——包括提示词、仓库和连接器——然后按计划、通过 API 调用或响应事件运行，”Anthropic 在其公告中解释道。

例行程序本质上是 `/schedule` 的下一代版本，通过这次更新，现有的计划任务现在会自动变成例行程序。你可以在网页版的 [claude.ai/code](https://claude.ai/code/draft_a3ce30a9-f0bb-4d18-890f-12cc6d6a6375) 或 Claude 桌面应用中将其设置为远程任务。

![](https://cdn.thenewstack.io/media/2026/04/3d6c6652-screenshot-2026-04-14-at-11.18.08-am-1024x211.png)

*图片来源：Anthropic。*

## 三种触发方式：计划、API 和 Webhook

Anthropic 指出，计划运行的例行程序对于每晚分拣新 Issue、每周扫描已合并的拉取请求以及确保项目文档保持最新状态特别有用。对于基于 API ping 触发的例行程序，公司指出这可用于持续部署工作流，例如，“Claude 对新构建进行冒烟测试，扫描错误日志以查找回归，并在发布频道发布允许或阻止发布的指令。”

> 许多团队一直利用 GitHub Actions 和处于 `-p` 无头模式的 Claude 串联类似的设置。现在 Anthropic 可以为他们管理会话生命周期。

对于这些例行程序，Claude Code 变得更像是一个后台代理，尤其是在运行具有每个拉取请求连续性的 GitHub 例行程序时。许多团队一直利用 GitHub Actions 和处于 `-p` 无头模式的 Claude 串联类似的设置。现在 Anthropic 可以为他们管理会话生命周期。

![](https://cdn.thenewstack.io/media/2026/04/d699775a-screenshot-2026-04-14-at-11.10.09-am-1006x1024.png)

*图片来源：Anthropic。*

## 云端执行，订阅限制

在某种程度上，这类似于 [Cowork](https://thenewstack.io/anthropic-takes-claude-cowork-out-of-preview-and-straight-into-the-enterprise/) 中的计划任务，Cowork 是 Anthropic 为知识工作者提供的 Claude Code 变体。

不过，除了 API 和 GitHub 触发器之外，一个主要区别在于，虽然计划好的 Cowork 任务只能在你的电脑开启时运行，但 Claude Code 例行程序运行在 Anthropic 的网页端基础设施上。这并不便宜，因此 Anthropic 每月 20 美元的 Pro 账户用户每天只能运行 5 个例行程序，而 Max 用户（每月支付 100 或 200 美元）每天将获得 15 个例行程序。Team 和 Enterprise 计划的用户每天最多可运行 25 个例行程序。这还需遵循 Anthropic 根据你的计划强制执行的常规 Token 限制——这些限制有些不透明，但似乎一天比一天严格。

> 虽然计划好的 Cowork 任务只能在你的电脑开启时运行，但 Claude Code 例行程序运行在 Anthropic 的网页端基础设施上。

这些在云端运行的例行程序的一个有趣之处在于它们是自主运行的。正如 Anthropic 所指出的，“在运行期间没有权限模式选择器，也没有批准提示词。”这些例行程序可以运行 shell 命令，访问技能（如果它们在仓库中），并调用连接器和 MCP 服务器。

同样值得注意的是，它们不会在团队之间共享，无论它们在 GitHub、Slack 和其他工具上执行什么操作，都与用户的身份绑定。

## 循环（Loops）依然是一个选项

运行长时间会话范围任务的另一个可用选项是 [`/loop` 命令](https://code.claude.com/docs/en/scheduled-tasks)。循环运行在你的本地机器上，允许你安排循环任务，但它们最多只能存活 7 天，且在重启后不会持久存在。