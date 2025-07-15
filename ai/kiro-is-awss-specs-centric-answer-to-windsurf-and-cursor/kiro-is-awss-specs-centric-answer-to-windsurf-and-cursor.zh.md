AWS 今天推出了 [Kiro](https://kiro.dev)，这是它对类 Cursor 和 Windsurf 这种智能 IDE 的尝试。和它最直接的竞争对手一样，AWS 使用了开源的 VS Code 项目作为 Kiro 的基础，这意味着开发者可以保留他们所有的 VS Code 设置和插件。Kiro 还支持模型上下文协议 (MCP) 来连接额外的工具。

至于底层的 LLM 模型，一位亚马逊发言人告诉我，它将使用 Clause Sonnet 4 作为默认模型，并提供 Sonnet 3.7 作为备选。对更多模型的支持即将到来。

Kiro [已发布](https://kiro.dev/blog/introducing-kiro/) Linux、Mac 和 Windows 版本，并支持大多数流行的编程语言。在预览期间，Kiro 将免费提供，之后的 Pro 计划起价为每月 19 美元，每月最多可与智能体交互 1,000 次。还将有一个 Pro+ 计划，价格为每月 39 美元，最多允许 3,000 次交互。

值得庆幸的是，AWS 不仅仅是复制类似工具的现有开发者体验，而是添加了自己的特色。具体来说，这些特色就是 Kiro 规范和钩子。

## Kiro 规范

规范几乎是不言自明的。它允许开发者通过编写项目的需求来指导工具。

乍一看，这可能听起来并不像一个新颖的想法。如果你使用过 Anthropic 的 Claude Code，你可能已经通过使用该工具的 Claude.md 文件做过类似的事情，但 AWS 是首批将此作为整体体验的一部分的代码——并且更符合企业环境中代码的编写方式。

[![](https://cdn.thenewstack.io/media/2025/07/2c687f79-kiro-specs-3.png)](https://cdn.thenewstack.io/media/2025/07/2c687f79-kiro-specs-3.png)

图片来源：Amazon。

但 AWS 在此基础上更进一步。当你使用 Kiro 启动一个项目时，它将自动生成用户故事，使用需求简单方法 (EARS) 结构来描述它们。

在下一步中，Kiro 然后通过分析你可能已经拥有的代码库和/或它创建的规范要求（开发者显然可以修改）来构建设计文档。这里有趣的是，它使用它来创建数据流图，例如，因为它列出了构建应用程序所需的 TypeScript 接口、数据库模式和 API 接口。

从那里，Kiro 生成一个任务和子任务的列表，以逐步完成，包括测试和可访问性要求。然后，开发者可以触发每个任务，并观看 Kiro 开始工作。

[![](https://cdn.thenewstack.io/media/2025/07/9fea1913-kiro-specs-1.png)](https://cdn.thenewstack.io/media/2025/07/9fea1913-kiro-specs-1.png)

图片来源：Amazon。

## Kiro 钩子

这也是 Kiro 钩子发挥作用的地方。AWS 将它们描述为事件驱动的自动化触发器，可以在保存、创建或删除文件时（或手动触发时）启动智能体以在后台执行特定任务。

**“**Kiro 钩子的作用就像一位经验丰富的开发者，可以发现你遗漏的内容或在后台完成样板任务，”AWS 的 Nikhil Swaminathan 和亚马逊开发者智能体与体验副总裁 Deepak Singh 在今天的公告中解释道。

[![](https://cdn.thenewstack.io/media/2025/07/b9b73ac3-kiro-agent-hooks-1.png)](https://cdn.thenewstack.io/media/2025/07/b9b73ac3-kiro-agent-hooks-1.png)

图片来源：Amazon。

这意味着，例如，当 API 接口被修改时，你可以触发一个钩子来更新项目的 Readme 文件，或者在提交代码之前运行扫描以查找泄露的凭据。

“钩子可以确保整个团队的一致性。每个人都可以从相同的质量检查、代码标准和安全验证修复中受益，”Swaminathan 和 Singh 写道。

[![](https://cdn.thenewstack.io/media/2025/07/9fbdc436-kiro-agent-hooks-2.png)](https://cdn.thenewstack.io/media/2025/07/9fbdc436-kiro-agent-hooks-2.png)

图片来源：Amazon。

正如 Singh 和 Swaminathan 正确地指出的那样，[氛围编码](https://thenewstack.io/from-vibe-coding-to-vibe-engineering-its-time-to-stop-riffing-with-ai/)不会很快消失，但在这一点上，也很明显，虽然现在用几个提示就能编写一个新的应用程序，但真正的工作通常是[让代码准备好](https://thenewstack.io/after-vibe-coding-comes-vibe-testing-almost/)用于实际的生产环境。

今天的公告是在一系列关于 AI 代码编辑器的新闻之后发布的。其中大多数是商业新闻，例如，Windsurf 上周宣布它不会被 OpenAI 收购，但其高管将前往 Google，并且这家搜索巨头将以 24 亿美元的价格授权一些 Windsurf 技术。

同时，我们也看到了基于命令行的编码智能体的兴起，例如 Claude Code，它似乎目前在智能编码领域占据了大部分市场份额，以及 Google 的 Gemini CLI 和亚马逊自己的 [Q Developer CLI](https://thenewstack.io/code-in-your-native-tongue-amazon-q-developer-goes-global/)。