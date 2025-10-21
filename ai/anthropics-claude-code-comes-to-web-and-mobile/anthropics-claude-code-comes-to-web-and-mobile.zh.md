今天，Anthropic 的 [Claude Code](https://www.claude.com/product/claude-code) 代理式编码工具正在[超越终端](https://www.anthropic.com/news/claude-code-on-the-web)，并进驻[网页和公司移动应用程序](https://claude.ai/code)。这意味着开发者现在可以直接从 Claude.ai 网页应用程序启动 Claude Code 工作流，然后 Claude Code 会在 Anthropic 管理的实例上运行这些编码任务。

公司表示，这项新功能正以“研究预览版”的形式推出，并对拥有付费 Pro 和 Max 账户的用户开放。

## 更多时间喝咖啡

Anthropic 相信，这种与 Claude Code 互动的新模式将对那些希望将多个明确定义的编码任务分配给 Claude 并行运行的开发者来说非常方便。

实际上，这意味着您将能够将 Claude Code 指向您的 GitHub 仓库，并告诉它您希望它完成什么工作。

[![网页版 Claude Code 新界面的截图](https://cdn.thenewstack.io/media/2025/10/a2913144-claude_code.png)](https://cdn.thenewstack.io/media/2025/10/a2913144-claude_code.png)

图片来源：Anthropic。

连接到 GitHub 后，您可以将当前任务提供给代理，并在新的网页界面中观看它对任务进行推理和处理代码，代理在右侧边栏运行，您的任务列表则显示在左侧。

这意味着使用 Claude Code 的开发者现在可以在手机上开始一项任务，去喝杯咖啡或参加又一次会议（唉！），然后回来继续代理未完成的工作。

## 安全性

Anthropic 强调，每个会话都将在其自己的沙盒环境中运行，并且所有 Git 交互都通过一个安全的代理服务进行，以确保 Claude Code 只能访问其被授权访问的仓库。

如果您愿意，也有一些方法可以突破这个沙盒。当您在故事中设置 Claude Code 环境时，您必须告诉 Claude Code 是否要授予它受信任的网络访问权限，以便它可以从经过验证的来源下载 npm 包。您也可以限制所有网络访问，或策划一个允许代理访问的域名列表。

总体而言，这种方法与 Anthropic 在 [Claude Agent SDK](https://thenewstack.io/anthropic-launches-claude-haiku-4-5/) 中处理安全的方式如出一辙。

## 实时引导，增强代理控制

最近，Claude Code 推出了一项新功能，允许开发者在代理处理问题时对其进行引导。这种实时引导在新平台上也可用，帮助开发者指导 Claude，而无需中断工作并可能重新开始。

Anthropic 表示：“开发者现在可以自信地监督一系列 Claude Code 实例，而不是一次管理一个单独的编码任务，确保它们安全独立地完成工作。”“这不再是看着 Claude 工作，而更像是将任务委托给整个团队——您分配工作，Claude 负责执行，并在每个任务完成后审查结果。”

[![网页版 Claude Code 新界面的截图](https://cdn.thenewstack.io/media/2025/10/013150e9-claude_code_web.png)](https://cdn.thenewstack.io/media/2025/10/013150e9-claude_code_web.png)

图片来源：Anthropic。

## 谷歌的 Jules 呢？

如果您一直在关注这些异步编码代理的开发，那么很多内容都会让您感到熟悉，并且听起来很像 [Google 的 Jules](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/)。例如，Jules 也会在新的虚拟机上创建您的 GitHub 仓库的克隆，然后为用户处理代码。

Jules 是从网页端开始，最近才转向命令行；而 Claude Code 则是从命令行转向网页端。

Anthropic 本身也已经通过 [Claude Code GitHub Actions](https://docs.claude.com/en/docs/claude-code/github-actions) 提供了 GitHub 集成，允许开发者在拉取请求中标记 Claude，以便代理开始处理解决方案。不过，这方面的计算环境是 GitHub Actions。其许多竞争对手也提供类似的 GitHub 集成。

## Claude 和 Anthropic 的底线

Anthropic 表示，其 Claude Code 代理式编码工具目前 90% 的代码是在 Claude Code 的帮助下编写的，这或许可以解释其最近的开发速度。Anthropic 称，以每位工程师每天的合并量来衡量，其工程团队的生产力提高了 67%，即使其工程组织规模翻了一番。

Claude Code 的普及在业务方面也取得了回报，Anthropic [最近表示](https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation)，Claude Code 目前已为公司创造了超过 5 亿美元的年化收入。