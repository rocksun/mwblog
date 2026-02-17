微软在其 [Visual Studio Code (VS Code)](https://thenewstack.io/visual-studio-2026-first-look-evolution-not-revolution/) [2026年1月版本 (v1.109)](https://aka.ms/VSCode/109) 中，将这款代码编辑器打造成“多智能体开发之家”，引入了对 [Anthropic Claude](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/) 和 [OpenAI Codex](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/) 智能体的支持，以及一个更新的会话管理系统，让开发者能够通过单一界面协调多个AI助手。

这使得开发者从单一智能体工作流转向多智能体范式，允许他们并排运行 GitHub Copilot、Claude 和 Codex。VS Code v1.109（2月4日发布）让开发者能够根据每个智能体的优势来分配工作，而不是被迫使用单一的AI平台。

“智能体正在改变我们的工作方式。你不应该只选择一个，或者每当有新事物出现时就切换工具，”VS Code 团队在 [一篇博客文章](https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development) 中写道。“有了 VS Code，你可以运行你想要的智能体，用开放标准扩展它们，并在一处管理它们。”

## 最大优势

[Brad Shimmin](https://www.linkedin.com/in/bradshimmin/)，Futurum Group 的分析师，表示这一变化显示了 VS Code 的影响力。

“坦白说，微软的这一举动表明其最大的优势并非任何单一模型，而是 VS Code 本身，这可以说是世界上最受欢迎的编辑器，”Shimmin 告诉《*The New Stack*》。“如果用户喜欢 Claude 但必须离开 VS Code 才能有效使用它，微软就会失去用户。然而，如果他们将 Claude 带给用户，就能将他们留在自己的生态系统中——并可能保留订阅收入。”

此外，他还补充说：“没有一个单一模型能成为每个开发者的‘赢家’。微软深知这一点，这就是为什么他们正从一个 OpenAI 商店转向一个通用AI接口。”

## Claude 加入

主要的新功能是使用 Anthropic 的 Claude Agent SDK 对 Claude 智能体提供公共预览支持。文章称，[拥有 GitHub Copilot 订阅的开发者](https://thenewstack.io/github-agent-hq/) 现在可以直接在 VS Code 中将任务委托给 Claude 模型，使用与其他 Claude 实现中相同的提示、工具和架构。

“你现在可以直接在 GitHub Copilot 旁边运行 Claude 和 Codex 智能体，”VS Code 团队在文章中写道。“当你需要快速、交互式帮助时，将它们作为本地智能体启动；或者将长时间运行的任务异步委托给云智能体。”

因此，GitHub Copilot Pro+ 和企业订阅者可以访问作为云智能体的 Claude 和 Codex，而本地智能体支持则需要 OpenAI Codex 扩展。Codex 自11月起就已作为本地智能体可用；Claude 则是新加入的。

## 统一会话管理

VS Code v1.109 提供了一个更新的智能体会话视图，它提供了一个单一仪表板，用于跟踪本地、后台和云环境中所有智能体的活动。文章称，开发者可以启动一个云智能体来执行明确的重构任务，同时运行一个本地会话进行探索性工作，切换上下文而不会失去动力。

“这种统一方法的妙处在于所有这些智能体都显示在相同的智能体会话视图中，”微软解释道。“你可以在它们之间分配任务，比较它们的输出，并为每项工作选择合适的工具。”

智能体会话现在显示清晰的状态指示器，显示哪些会话需要关注，同时改进了长时间运行操作的进度跟踪和更好的故障处理。

## 并行子智能体

一个显著的改进是并行 [子智能体](https://code.visualstudio.com/docs/copilot/agents/subagents) 执行，这使得开发者能够同时启动多个子智能体。

“子智能体是上下文隔离的智能体，它们独立于你的主会话运行，”VS Code 团队解释道。“你的主智能体分配工作，只有最终结果会流回。中间的探索保持在内部，保持你的主要上下文干净。”

每个子智能体都可以有专门的行为。

## MCP 应用到来

微软表示，VS Code 现在是第一个完全支持 [MCP 应用](https://modelcontextprotocol.io/docs/extensions/apps) 的主要AI代码编辑器，MCP 应用是官方的模型上下文协议扩展，允许工具调用返回交互式UI组件。智能体现在可以直接在聊天中渲染仪表板、表单、可视化和多步骤工作流，而不是简单的文本响应。

“这为更丰富、更有效的人机智能体协作创造了机会，”微软说。

此次发布还使得 [智能体技能](https://code.visualstudio.com/docs/copilot/customization/agent-skills)——Anthropic 用于扩展 AI 智能体的开放标准——普遍可用。

## 进一步优化

此次发布还包括其他优化，例如 [Copilot 记忆](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-copilot-memory-a-more-productive-and-personalized-ai-for-the-way-you/4432059)，它有助于智能体在交互中保留相关上下文。此次发布还通过外部索引提供了更快的代码搜索，改善了大型仓库开发期间的响应能力。

此外，此次发布通过在 macOS 和 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 上进行实验性终端命令沙盒提供了增强的安全性。自动批准规则减少了不必要的提示，同时保持了对智能体驱动操作的控制。

聊天体验也更快、响应更灵敏，改进了流式传输，提供了更高质量的推理结果，并更好地了解模型的思维。智能体现在会提出澄清性问题而不是做出假设，而经过改进的内联聊天使上下文中的 Copilot 交互感觉更自然。

## 仅仅是个开始

该公司将最新的 VS Code 版本定位为仅仅是个开始。

“一年前，我们才刚刚引入智能体模式，”VS Code 团队写道。“现在你已经可以并排运行 Copilot、Claude 和 Codex，还有更多。”

微软将于2月19日在其 [智能体会话日](https://youtube.com/live/tAezuMSJuFs) 上演示新功能。