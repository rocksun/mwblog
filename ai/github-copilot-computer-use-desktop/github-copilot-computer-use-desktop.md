<!--
title: GitHub针对全新Copilot功能的建议：先尝试其他方法
cover: https://cdn.thenewstack.io/media/2026/10/7e392c2b-steve-a-johnson-3suqrc8-dne-unsplash-scaled.jpg
summary: GitHub推出了支持macOS和Windows的Copilot电脑使用功能，允许智能体直接操作桌面应用。尽管功能强大，但官方建议优先使用API或MCP等更稳定的工具，并对企业管控和安全性进行了规范。
-->

GitHub推出了支持macOS和Windows的Copilot电脑使用功能，允许智能体直接操作桌面应用。尽管功能强大，但官方建议优先使用API或MCP等更稳定的工具，并对企业管控和安全性进行了规范。

> 译自：[GitHub's advice for its new Copilot feature is to try something else first](https://thenewstack.io/github-copilot-computer-use-desktop/)
> 
> 作者：Amanda Caswell

**GitHub于周四推出了电脑使用功能的公开预览版**，赋予了 Copilot CLI 及其桌面应用在 macOS 和 Windows 上操作应用程序的能力。智能体可以读取应用内容并进行点击、输入、滚动和拖拽，甚至包括那些没有 API、命令行界面或 MCP 集成的老旧纯 GUI 软件。

在 Safari 中填写费用报表是 GitHub 的[演示示例](https://github.blog/changelog/2026-10-01-github-copilot-can-now-interact-with-desktop-apps/)，但该公司还描述了其他用途，包括在传统应用程序中总结信息、更新演示文稿、输入数据以及在应用程序之间移动信息。开发者可以通过终端或 Copilot 应用访问该功能，该应用运行在 Copilot CLI 之上，[作为 Claude Code 和 Codex 的竞争对手于今年早些时候发布](https://thenewstack.io/github-copilot-desktop-app/)。

GitHub 还有一些需要迎头赶上地方。OpenAI 在 [4 月将电脑使用功能添加到了 Codex 中](https://thenewstack.io/openai-codex-chrome-extension/)，而 Anthropic 则在今年早些时候为 Claude Code 和 Claude Cowork 带来了更广泛的 macOS 电脑使用功能。

> GitHub 还有一些需要迎头赶上地方。

## 电脑使用与 MCP 服务器

在 Copilot CLI 中启用电脑使用功能会激活一个[带有自身 MCP 服务器的捆绑插件](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/computer-use)。它在本地会话中工作，通过操作系统的辅助功能树读取应用程序内容，并在需要视觉上下文时截取屏幕。

该公司建议尽可能使用直接工具。因此，如果 API、MCP server、终端命令、文件系统工具或专用浏览器工具可以处理该任务，它通常比桌面交互提供更多结构化的信息和更可预测的结果。

这一建议限制了 GitHub 认为电脑使用功能的适用范围。OpenAI 总裁 [Greg Brockman](https://www.linkedin.com/in/thegdb/) [上个月](https://thenewstack.io/computer-use-agent-connectors/)提出了更广泛的观点，他认为智能体可以使用与人类相同的界面，从而免去行业为每个软件构建和维护连接器的工作。

## 保存的批准权限在其被移除后依然有效

开发者可以通过在 Copilot CLI 中输入 `/computer on` 或通过 Copilot 应用的电脑使用设置来启用该功能。macOS 还需辅助功能权限来操作控件，以及屏幕录制权限来在需要视觉上下文时检查窗口。

CLI 会话的权限模式决定了 Copilot 在访问应用之前是否会进行询问；开发者可以通过 `/permissions show` 进行检查。当出现提示时，他们可以允许当前会话访问，为将来的会话选择“始终允许”，或者拒绝。拒绝规则会覆盖自动批准和保存的批准。

保存在 CLI 中的批准权限会延续到同一台计算机上的桌面应用中。从始终允许列表中移除某个应用会清除其对未来会话的批准，但会话中已经授予的访问权限仍保持不变。

停止工作需要进行单独的操作：在 CLI 中按两次 Esc 键，或在桌面应用中点击停止或按 Esc 键。

## 对电脑使用功能的企业管控

企业策略会覆盖开发者的本地偏好。如果托管设置阻止了电脑使用功能，Copilot CLI 会报告该功能不可用。

> 企业策略会覆盖开发者的本地偏好。

通过 `managed-settings.json`，企业所有者还可以[控制开发者是否可以绕过批准提示](https://github.blog/changelog/2026-07-27-enterprise-managed-settings-now-apply-to-the-github-copilot-app/)。该限制适用于 Copilot 应用、CLI 和 VS Code。

GitHub 针对 Business 和 Enterprise 的默认启用策略并未改变此预览版的选择加入（opt-in）状态。该策略从 10 月 22 日开始适用于未配置的功能，但排除了预览功能。

## 可靠性取决于界面

时机或窗口状态的变化可能导致 Copilot 重复操作或停滞。GitHub 还警告称，智能体可能会选择错误的空间、在错误的字段中输入，或者在动态界面和复杂工作流中遇到困难。

> 应用程序窗口中可见的敏感信息也可能成为智能体的上下文。

屏幕上意外出现的内容和模棱两可的指令可能会导致影响用户设备、数据或已连接账户的操作。应用程序窗口中可见的敏感信息也可能成为智能体的上下文。