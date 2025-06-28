[Qodo](https://www.qodo.ai/)，这个让开发者能够生成代码，同时也能帮助他们审查和测试代码的 Agentic 编码平台，今天发布了 [Qodo Gen CLI](https://docs.qodo.ai/qodo-documentation/qodo-gen/qodo-gen-cli)，这是一个新的 Agent 框架，它允许开发者基于他们独特的工作流程和代码库轻松创建自己的 AI 编码 Agent。本质上，这意味着开发者将能够编写自己的配置文件和提示，以指导这些 Agent 的行为，从而完成复杂的工作流程并与外部工具交互。

正如 Qodo 联合创始人兼 CEO [Itamar Friedman](https://www.linkedin.com/in/itamarf/) 告诉我的那样，团队始终认为，虽然 [vibe coding 可能很有趣](https://thenewstack.io/vibe-coding-in-a-post-ide-world-why-agentic-ai-is-the-real-disruption/)，但对于企业来说，要从他们在 AI 和 [编码 Agent](https://thenewstack.io/ai-coding-agents-level-up-from-helpers-to-team-players/) 方面的投资中获得真正的价值，AI 必须集成到软件开发生命周期的各个环节，并将代码审查和测试作为核心。他还强调了 Qodo 的一个独特功能——也是它能够处理大型代码库的原因——是它的上下文引擎。（如果这听起来很熟悉，那可能是因为 Qodo 的竞争对手 [Augment Code](https://thenewstack.io/augment-codes-remote-agents-code-in-the-cloud/) 也非常重视其上下文引擎。）

[![一个文本片段，展示了如何定义一个 Qodo 编码 Agent。](https://cdn.thenewstack.io/media/2025/06/2809f91c-qg-cli-custom-agent.png)](https://cdn.thenewstack.io/media/2025/06/2809f91c-qg-cli-custom-agent.png)

图片来源：Qodo。

Friedman 解释说：“在 [软件开发生命周期] 中要完成的大部分工作都需要 [...] 引入正确的上下文并检查生成的代码的质量。例如，如果你正在进行根本原因分析，那么你需要引入正确的上下文来完成这项工作，并且你需要检查代码中有什么不对劲，并在 QA 中对其进行调试等等。”

Qodo 团队认为，要将 Agentic AI 应用于软件开发过程的所有部分，意味着你必须将 Agent 从 IDE 中解放出来，并将其引入命令行。然而，对于大多数以 Agent 为中心的命令行工具来说，自定义的开始和结束都是添加模型上下文协议 (MCP) 工具，以使 Agent 能够使用第三方工具并访问其他数据。

“大多数 Agent 的行为方式都相同。例如，对于大多数 Agent，你给他们一些规则，他们基本上将其用作系统提示的一部分，然后你可以自定义该规则。这是一个文件，你只是希望它能按你期望的方式工作。我们使用了一种我们努力开发的基于图的 Agent，它具有内部基准等等，以使该图严格遵循一组特定的指令，”Friedman 说。

[![](https://cdn.thenewstack.io/media/2025/06/22598a09-screenshot-2025-06-24-at-15.25.02.png)](https://cdn.thenewstack.io/media/2025/06/22598a09-screenshot-2025-06-24-at-15.25.02.png)

图片来源：Qodo。

例如，如果一个开发团队通常使用观察、定位、决策和行动 (OODA) 循环，他们现在可以在配置文件中指定这一点，Agent 将严格遵守这些准则来解决问题。

Friedman 说，在这个配置文件中，开发者可以定义 Agent 的一般行为，但他们也可以使用它来定义 MCP 权限，并设置 Agent 应该尝试实现的总体目标，包括退出规则。由于这些 Agent 基于大型语言模型 (LLM) 并且不是确定性的，因此 Agent 遵循这些退出规则，并且开发者可以强制它提供非常具体的输出尤为重要。Friedman 说，Qodo 的系统 99.99% 的时间都会遵循这些规则。

Qodo 还在其 CLI 工具中添加了一个名为“create agent”的新命令，该命令允许开发者按照公司的最佳实践逐步完成创建新 Agent 的过程。如果开发者的意图不够明确，该工具还会根据需要提出澄清问题。

默认情况下，Qodo Gen CLI 将附带一些预构建的 Agent，用于执行代码审查、测试覆盖率分析和发布说明生成等任务。这些预构建的 Agent 还与流行的 CI/CD 工具集成。

目前，Qodo Gen CLI 支持 OpenAI 的 o3 和 Anthropic 的 Claude Sonnet 4 等模型。

展望未来，Qodo 团队也在思考如何最好地与这些 Agent 交互——以及在哪里进行交互是最好的。“ADEs [Agentic 开发环境] 是下一件事，”Friedman 说，并指出如果像 Lovable 这样的公司可以动态构建用户界面，“为什么我们需要这种如此苛刻的 IDE？我需要界面来适应我的任务。”