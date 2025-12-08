[AWS](https://aws.amazon.com/?utm_content=inline+mention) 的 [Kiro](https://thenewstack.io/aws-kiro-brings-automated-reasoning-to-agentic-development/) 正在帮助用户赋予智能体专业知识，而不会使其陷入上下文的海洋。

该公司新推出的[能力系统](https://kiro.dev/powers/)于本周在 [AWS re:Invent](https://reinvent.awsevents.com/) 大会上发布，它仅在开发者需要时才动态加载框架专业知识和工具。该公司表示，该系统并非预先将所有可能的工具定义都塞进 [AI 智能体](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)的上下文窗口，而是根据开发者实际正在处理的工作来激活能力。

AWS 智能体 AI 总经理兼总监 Amit Patel 在接受 The New Stack 采访时表示：“过去一年，自 MCP [模型上下文协议] 发布以来，我们一直在观察开发者，我们观察到的一件事是，许多 MCP 服务器被添加到上下文中，并且上下文变得越来越大。”“那些 MCP 工具中的并非所有工具都对开发者正在尝试完成的工作是必要的。”

## 上下文过载问题

这个问题源于 [MCP](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 服务器的传统工作方式。该公司表示，将五个 MCP 服务器连接到您的开发环境，您可能在编写第一行代码之前就加载了超过 100 个工具定义。这可能在您开始第一个提示之前就消耗了超过 50,000 个令牌——大约是一个典型上下文窗口的 40%。

AWS 自己的 MCP 服务器说明了这一挑战。它暴露了超过 150 个工具，涵盖从 Aurora 到 DynamoDB 再到 S3 的各种服务。该公司表示，加载该服务器后，这些工具定义中的每一个都将存在于您的智能体上下文中，无论您是正在处理数据库、存储还是其他完全不同的东西。

能力系统通过基于关键字的激活来解决这个问题。在您的对话中提及“数据库”或“[postgres](https://thenewstack.io/how-distributed-postgres-solves-clouds-high-availability-problem/)”，[Supabase](https://thenewstack.io/how-supabase-is-building-its-platform-engineering-strategy/) 能力就会加载其工具和最佳实践。切换到部署工作时，[Netlify](https://thenewstack.io/netlify-makes-preview-servers-available/) 能力会激活，而 Supabase 则会停用。AWS 表示，您的基线上下文使用量将保持接近于零，直到您实际需要特定工具。

## 能力的构成

每种能力都包含三个组件：一个 MCP 服务器配置、一个充当智能体入门手册的 POWER.md 指导文件，以及在 IDE 事件或斜杠命令上触发的可选钩子。

POWER.md 文件包含用于触发激活的关键字的 frontmatter、初始设置的入门步骤以及工作流特定指导文件的映射。根据 AWS 的说法，当您在 Supabase 中编写行级安全 (RLS) 策略时，智能体会加载特定于 RLS 的文档。当您切换到边缘函数时，它会加载不同的上下文。

Patel 解释说：“能力本质上是 MCP 服务器、指导文件和智能体钩子的组合，这是 Kiro 内部的三个功能。”“您可以将这三者结合起来，并将其定义为您自己可以直接使用或可以与社区共享的东西。”

The Futurum Group 分析师 Brad Shimmin 告诉 The New Stack：“正如 AWS 正确提到的，在构建复杂软件时，使用 MCP 服务器为大型语言模型（LLM）配备特定的上下文、指导方针、资源、约束等，而这些软件往往依赖于广泛而复杂的工具链，这有点像每次你想查阅某个东西时都阅读整本百科全书。”

Shimmin 说：“AWS 在这里所做的，是我们从智能代理工具提供商那里越来越常见的一种做法。[Google](https://cloud.google.com/?utm_content=inline+mention) Gemini CLI 就是一个例子，它集成了扩展；[OpenCode](https://thenewstack.io/terminal-user-interfaces-review-of-crush-ex-opencode-al/) 也通过插件实现了同样的功能。”“这一切都关乎在正确的时间‘激活’相关信息，只在适当的时候将其添加到上下文窗口……并且很可能在之后将其删除。我不确定 AWS 在 Kiro Powers 上的这个想法是否能完全取代开发者可用的所有不同技术和工具，但我确实喜欢他们通过 POWERS.md 指出的方向，将其作为一种标准化的方式来打包、激活和传输知识。”

开发者安全工具提供商 Arcjet 的首席执行官 David Mytton 指出了上下文限制的重要性。

他说：“Kiro Powers 感觉就像 [VS Code](https://thenewstack.io/5-ai-extensions-to-help-improve-your-vs-code-experience/) 的 AI 智能体扩展：您在需要时精确地投入特定领域的专业知识。”“按需加载和卸载实际上是为了避免 LLM 的上下文限制。您不必用每个工具和指令来堵塞上下文窗口，而只需为您相关的工具支付每令牌成本。”

Mytton 补充说：“很高兴看到与 Claude Skills 的竞争。”“这显然是基于 MCP 的工具的发展方向：您可以在编辑器和智能体之间移动的扩展，而不是同时加载所有可能的工具。”

## 启动合作伙伴和生态系统

Kiro 与涵盖应用程序开发生命周期的合作伙伴共同推出了能力系统：Datadog、Dynatrace、Neon、Netlify、Postman、Supabase、Strands Agents 和 Amazon Aurora。该公司将此定位为通过一键安装即可获得的“瑞士军刀般的功能”。

开发者可以在 Kiro IDE 或 kiro.dev 上浏览能力，无需编辑 [JSON](https://thenewstack.io/working-with-json-data-in-python/) 配置文件或运行命令行设置即可安装它们。如果某项能力需要 API 密钥或环境变量，它会在首次使用时提示您。

该系统还支持从 GitHub URL 导入的社区构建能力，以及来自本地目录或私有仓库的私有团队能力。Patel 表示，Kiro 强调任何人都可以使用他们的工具构建和分享能力。

尽管目前能力仅在 Kiro IDE 中运行，但该公司正在努力实现与其他 AI 开发工具的跨兼容性，包括 Kiro CLI、Cline、Cursor 和 Claude Code。目标是让公司编写一个 POWER.md 文件，使其适用于任何 AI 编码助手。

## 不仅仅是打包

Kiro 将能力定义为不仅仅是一种打包格式——他们将其定位为 AI 智能体持续学习的模型。随着框架的发展和团队构建内部工具，智能体需要扩展其能力的方法，而无需从头开始。

AWS 在一篇[博客文章](https://kiro.dev/blog/introducing-powers/)中写道：“Neo 并非只学了一次功夫就停下了。”这里指的是电影《[黑客帝国](https://en.wikipedia.org/wiki/The_Matrix)》。“在整个《黑客帝国》中，他根据需要下载了新的能力。”

愿景是当 Supabase 发布更新的 RLS 模式时，智能体会自动获取它们。公司表示，当您的团队构建了一个内部设计系统时，您可以将其打包成一项能力，每个开发者的智能体都知道如何使用它。

能力系统的推出伴随着 Kiro 发布了三款“[前沿智能体](https://thenewstack.io/aws-frontier-agents-handle-code-security-ops-without-you/)”——用于软件开发、安全和 [DevOps](https://thenewstack.io/introduction-to-devops/) 的自主智能体，它们无需人工干预即可工作。这些智能体处理大规模、耗时多天的任务，而能力系统则关注另一端：精准且注重令牌效率的、有针对性的具体开发工作。

Patel 在发布会上说：“在这个频谱的一端，您拥有这些耗时数日的大规模学习和扩展任务。”“但另一端，开发者正在从事需要有针对性和精准度的具体任务。这就是能力系统的用途。”

能力系统已在 Kiro IDE 中提供。该公司表示，与其它开发工具的跨兼容性已在计划中，但尚未可用。