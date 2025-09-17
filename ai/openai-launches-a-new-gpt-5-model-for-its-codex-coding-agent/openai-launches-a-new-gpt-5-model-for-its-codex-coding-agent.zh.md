[Codex](https://openai.com/codex/), OpenAI 对标 GitHub Copilot、Claude Code 以及类似 AI 编码代理的答案，今天迎来重大更新。

本次发布的核心是 GPT-5-Codex，它是 OpenAI 最新的 GPT-5 模型的一个版本，该公司专门针对代理式软件工程进行了优化。虽然新模型本身就值得关注，但该团队还为 Codex 添加了大量额外功能。这些功能包括：重建的 Codex CLI，现在以代理式工作流程为中心；一个新的 IDE 扩展，将 Codex 带到 VS Code、Cursor 和其他 VS Code 分支等工具中；与 GitHub 的集成，用于代码审查；以及 Codex Web 的工作流程更新。

OpenAI 的 ChatGPT Plus、Pro、Business、Edu 和 Enterprise 计划的用户都可以使用 Codex，使用限制会根据用户订阅的计划进行调整。OpenAI 明确指出，Plus、Edu 和 Business 计划将涵盖“每周几次集中的编码会话”，而 Pro 计划的用户则可以期待“跨多个项目的完整工作周”。

随着 API 访问即将到来，Codex CLI 用户也可以使用 API 为 Codex 付费（但这可能会很快变得昂贵）。

## GPT-5-Codex

值得注意的是，虽然 GPT-5 受到了一定程度的冷遇，部分原因是它的模型路由器，有时似乎优先考虑为 OpenAI 节省推理成本，而不是改进结果，但 GPT-5-Codex 确实具有路由器。它是一个专为 Codex 设计的独立模型（尽管它也将很快在 OpenAI API 中可用）。

在今天发布之前的简报中，OpenAI 强调，为了推理复杂的问题，GPT-5-Codex 使用动态的推理量，并且在该公司自己的测试中，该模型能够在问题上自主工作超过七个小时（但这并不是一个硬性上限）。

为了帮助指导模型，GPT-5-Codex 现在使用 AGENT.md 文件，该文件已成为为模型提供编码指南和其他说明的事实行业标准。

“该模型结合了编码代理的两项基本技能：在交互式会话中与开发人员配对，以及在较长任务上进行持久、独立的执行，”该公司在其公告中写道。“这意味着 Codex 在小型、定义明确的请求或与您聊天时会感觉更快，并且可以在大型重构等复杂任务上工作更长时间。”

[![](https://cdn.thenewstack.io/media/2025/09/2039c006-gpt-5-codex-swe-bench.png)](https://cdn.thenewstack.io/media/2025/09/2039c006-gpt-5-codex-swe-bench.png)

图片来源：OpenAI。

由于该团队在 GPT-5 发布后有额外的时间来构建此模型，因此能够优化模型的编码性能。

OpenAI 的基准测试确实显示了在 [SWE-bench](https://www.swebench.com/) 基准测试中相对较小的改进，该基准测试旨在测试模型是否能够解决来自一组 GitHub pull request 的问题。74.5% 是一个非常可观的分数（由于 OpenAI 的基础设施无法运行整套任务，因此 OpenAI 之前在发布 GPT-5 时报告的一些数据存在一些差异）。

但在这个上下文中更重要的是，GPT-5-Codex 在重构代码方面表现出色，轻松超越了 GPT-5 的高推理模式。

## GitHub 中的 Codex 代码审查

这可能也是该团队认为现在是发布 GitHub 代码审查代理的合适时机的原因。“GPT-5-Codex 经过专门训练，可以进行代码审查并发现关键缺陷，”OpenAI 解释说。“在审查时，它会浏览您的代码库，推理依赖关系，并运行您的代码和测试以验证正确性。”

例如，GPT-5（高）留下的评论中有 13.7% 是不正确的，而 GPT-5-Codex 的评论中只有 4.4% 是错误的。与此同时，OpenAI 团队现在认为 52% 的 GPT-5-Codex 评论是“高影响力”的，而 GPT-5（高）只有 39%。

[![](https://cdn.thenewstack.io/media/2025/09/e50cd110-codex-comments-incorrect.png)](https://cdn.thenewstack.io/media/2025/09/e50cd110-codex-comments-incorrect.png)

图片来源：OpenAI。

在直接处理 GitHub issues 和处理代码批准时，这些数字将发挥作用。

与类似工具一样，开发人员只需在他们的 pull requests 中提及“@codex review”并告诉代理要审查什么（例如“@codex review for security vulnerabilities”）。

“在 OpenAI，Codex 现在审查我们绝大多数的 PR，每天发现数百个问题——通常在人工审查开始之前。这对于让 Codex 团队能够以更大的信心快速行动至关重要，”该公司表示。

## 与您的代理分享更多信息

至于 Codex 生态系统其余部分的更新，一个突出的功能是，开发人员现在可以在 CLI 和 Web 版本中附加和共享图像（无论是屏幕截图、线框图还是图表）与编码代理，以提供更多上下文。

在 CLI 方面，Codex 现在还使用一个待办事项列表来跟踪其进度，并且该团队表示，它改进了工具调用，以及用户界面，以便在模型调用这些工具并创建差异时进行跟踪。现在有三种明确的批准模式：只读模式，需要显式批准；自动模式，具有完整的 workspace 访问权限，但需要在该 workspace 之外进行批准；以及完全访问模式，Codex 能够读取任何地方的文件并运行具有网络访问权限的命令。

对于 Codex Web，该团队强调，它改进了服务运行的整体云基础设施，改进的缓存将新任务和后续任务的平均完成时间缩短了 90%。