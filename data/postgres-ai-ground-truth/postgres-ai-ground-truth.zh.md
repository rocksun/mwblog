似乎每个人都在争相[构建 AI 应用程序](https://thenewstack.io/what-developers-need-to-build-successful-ai-apps/)和智能体（agents），寻找新工具来支持从客户支持到内部文档检索的一切需求。

但是，为了可靠地工作，AI 应用程序和智能体需要访问现有的企业数据，例如客户记录或支持问题。如果没有这些信息，束手无策的智能体会自行填补空白，即产生“幻觉”。

这就是为什么 Nvidia 的联合创始人、总裁兼 [CEO Jensen Huang](https://thenewstack.io/nvidia-ceo-details-a-new-ai-way-of-developing-software/) 在他最近的 GTC 主旨演讲中，将结构化数据称为“AI 的基准事实（ground truth）”。

[Phillip Merrick](https://www.linkedin.com/in/phillipmerrick/)，[pgEdge](https://www.pgedge.com/) 的联合创始人兼首席产品官，对此表示赞同。

“企业需要他们构建的智能体和 AI 应用程序能够引用他们已有的数据，”Merrick 告诉 *The New Stack*。“因此，[结构化数据] 确实是 AI 的基准事实……这是你确保你的 LLM（大语言模型）和智能体不产生幻觉的方式；你将它们指向实际数据。

而 Postgres 是指向这些数据的最佳场所。”

## Postgres 在 AI 工作负载中脱颖而出

为什么选择 [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/)？Merrick 并不是唯一一个认为该数据库最适合构建 AI 应用程序的人。

当被问及过去一年他们在哪个数据库环境中工作过，以及下一年想在哪个环境中工作时，[Stack Overflow 2025 开发者调查](https://survey.stackoverflow.co/2025/technology#most-popular-technologies-database-database:~:text=What%20is%20it%20like%20to%20be%20the%20most%20desired%20and%20the%20most%20admired%20technology%20in%20your%20category%3F%20The%20answer%20lies%20with%20PostgreSQL%2C%20ranked%20highest%20for%20both%20since%202023!)中 66% 的受访者选择了 Postgres。

该数据库自 2023 年以来一直保持这一头衔是有充分理由的。正如 Merrick 向 *The New Stack* 描述的那样，“它很优雅；易于上手、易于使用且易于针对其进行开发，”并称其为“AI 应用程序的首选数据库”。

在列举 [Postgres 为何表现卓越](https://thenewstack.io/why-ai-workloads-are-fueling-a-move-back-to-postgres/)的一些原因时，Merrick 强调了该数据库的开源模式，并强调它是“真正”的开源：“Postgres 是一个真正的基于社区的开源项目，贡献者是作为社区的一员在运作，而不是代表他们的雇主。”

> “Postgres 是一个真正的基于社区的开源项目，贡献者是作为社区的一员在运作，而不是代表他们的雇主。”

他没有点名，但指出许多专有数据库虽然自称开源，但往往有一些商业保留手段。对于构建 AI 应用程序的开发者来说，投入这样一个专有数据库是通往可怕的供应商锁定的捷径。

可扩展性是 AI 工作负载的另一个关键基础设施关注点，Merrick 表示 Postgres 已为此做好了准备，并指出 [OpenAI 的 API](https://openai.com/index/scaling-postgresql/) 就是建立在 Postgres 之上的。

## AI 数据和工作负载的一站式商店……

在推崇其直观的开源模式和可扩展性的同时，Merrick 补充说 Postgres 不仅仅是一个关系型数据库。通过其扩展架构，它还可以吸收其他数据库模式。

特别是随着定制构建的向量数据库（如 [Pinecone](https://thenewstack.io/pinecone-revamps-vector-database-architecture-for-ai-apps/)）脱颖而出，Merrick 很快强调了选择带有向量扩展（即 pgvector）的通用数据库（即 Postgres）的优势：

“pgvector 的性能与那些独立的向量数据库一样好，但优点是它是标准的 Postgres。它是你用于所有其他数据的工具，”他解释道。“既然你可以在 Postgres 中处理所有其他事情，为什么还要为了向量而求助于那些专有的专业厂商数据库呢？”

值得注意的是，在某些情况下，开发者可能为了更快的速度而倾向于使用专有数据库。然而，Merrick 声称需要这种专门化的用例正在减少。

尽管 Jensen Huang 可能将结构化数据称为 AI 的基准事实，但非结构化数据（例如支持工单、知识库等）在构建成功的 AI 应用程序中仍发挥着关键作用。Merrick 说 Postgres 已经准备好支持两者。

他解释说，开发者可以将他们的文档和其他非结构化数据输入 Postgres，使用 pgvector 存储、索引和查询嵌入，然后使用 RAG（[检索增强生成](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/)）在顶部构建聊天机器人。

“所以 [你] 不仅将 Postgres 用于结构化数据和向量，还用于非结构化文档，”Merrick 说。“这为你构建需要处理大量非结构化数据的聊天机器人和智能体提供了一个伟大的策略。”

他指出 [针对 Postgres 的 pgEdge Agentic AI 工具包](https://www.pgedge.com/products/agentic-ai-postgres) 是企业级基于 Postgres 基础设施的一个例子，它可以帮助开发者构建 Agentic AI 应用程序，支持从文档摄取到嵌入生成再到检索的全周期。“[pgEdge] docloader 负责将你的文档导入 Postgres，”Merrick 解释道。“然后你将其与向量化器（vectorizer）配合使用，它就会自动为你获取向量。”

除了最初的摄取外，Merrick 还提醒开发者也要考虑持续的向量维护（即确保向量在内容更改时保持最新），他说这是许多人忽略的一点：

“人们没有意识到他们将不得不担心 [这一点]，因为开箱即用的 pgvector 之类的工具在底层内容发生变化时，不会为你提供向量的自动更新。”

> “人们没有意识到他们将不得不担心 [这一点]，因为开箱即用的 pgvector 之类的工具在底层内容发生变化时，不会为你提供向量的自动更新。”

这就是为什么 pgEdge 的 Agentic AI 工具包还包括 pgEdge Vectorizer（一个自动分块文本上下文并生成向量嵌入以随内容变化维护向量的 Postgres 扩展），以及一个功能齐全的 MCP（模型上下文协议）服务器，该服务器适用于大多数版本的 Postgres，并使 AI 应用程序构建者和代码生成器（例如 Claude Code）能够连接到新的和现有的 Postgres 数据库。

## ……具备任务关键型行业的安全性

无论是在各种组合中单独使用还是共同使用，Merrick 表示，这个工具包中的技术（完全开源且对所有 Postgres 用户免费）都显著降低了开发者在 Postgres 上构建 AI 应用程序的难度，无论是 Agentic AI 应用程序还是运行在知识库上的更常见的聊天机器人。

无论哪种方式，他都表示 Postgres 无疑是明智之选，因为它为企业提供了部署和扩展 AI 应用程序所需的高可用性、数据主权和安全性，特别是对于金融、医疗、电信和政府等行业的任务关键型应用。

他将这些优势部分归功于 Postgres 提供的部署灵活性，允许企业在托管云数据库、自管理云账户或本地运行应用程序。“所以你拥有了完全的灵活性，”Merrick 说。“并非所有的 Postgres 供应商实际上都提供 Postgres 的这种优势。pgEdge 做到了。”

除了这种灵活性之外，Postgres 成为开发者青睐的数据库的另一个可能原因是其久经考验的安全性，Merrick 说 pgEdge 通过其 AI 工具进一步增强了这一点：

“在我们的 [MCP 服务器](https://www.pgedge.com/download/ai-toolkit)中，我们同时拥有基于用户和基于令牌的身份验证。我们使用 TLS 运行加密流量。而且，虽然我们的 MCP 服务器同时支持只读和读写模式，但默认情况下，除非你另行说明，否则一切都是只读的。”

这些安全功能，结合支持数据主权的分布式 Postgres 能力，可帮助企业防止数据泄露并遵守 GDPR 等法规，使 Postgres 成为开发 AI 应用程序的明显领跑者。

现在轮到企业投资于正确的基础设施了。