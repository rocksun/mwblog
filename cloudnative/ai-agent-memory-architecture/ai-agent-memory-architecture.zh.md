当你观察顶级工程团队如何实际构建代理记忆系统时，一个模式浮现：代理所看到的是文件系统接口，而持久化存储则是数据库。争论从来都不是“文件系统还是数据库”，而是在正确的层级上两者兼而有之。

文件系统是良好代理接口的观点并不新鲜。Dust.tt 在 [2025年中期将公司数据投射到合成文件系统](https://dust.tt/blog/how-we-taught-ai-agents-to-navigate-company-data-like-a-filesystem) 中。Letta 的内存基准测试显示 [文件系统工具优于其他替代方案](https://www.letta.com/blog/benchmarking-ai-agent-memory)。LangChain 的 [上下文工程工作](https://blog.langchain.com/how-agents-can-use-filesystems-for-context-engineering/) 奠定了基础。

但在2026年1月，这场讨论 intensified。Vercel 发布了 [一些评估](https://vercel.com/blog/how-to-build-agents-with-filesystems-and-bash)。Harrison Chase 分享了 [LangSmith Agent Builder 如何实现记忆](https://x.com/hwchase17/status/2011814697889316930)。Jerry Liu 宣称“文件即一切所需”。“FUSE即一切所需” [登上了Hacker News](https://www.llamaindex.ai/blog/files-are-all-you-need)。Anthropic 的 Skills 功能将 [代理能力打包成 markdown 文件文件夹](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)，默默地强化了同样的模式。

> “争论从来都不是‘文件系统还是数据库’；而是在正确的层级上两者兼而有之。”

为什么会重新受到关注？像 Cursor、Claude Code 和 Windsurf 这样的编码代理已经证明文件系统接口效果 remarkably 好——至少对于代码而言。问题是这种成功是否能推广。

这种吸引力是可理解的。一个有能力的代理可能需要与 REST API、SQL 数据库、向量存储、云控制台、文件系统、网页浏览器和人类用户互动——每个都有不同的协议和约定。需要处理的接口太多了。

但当你审视这些团队实际如何构建他们的系统时，一幅不同的画面浮现。他们在底层使用数据库——并且他们对原因 remarkably transparent。

## 文件系统接口与文件系统存储有何不同？

Harrison Chase 在他 X 上的帖子中透明地介绍了 LangSmith Agent Builder 的架构：代理看到的是文件系统接口，但实际存储是数据库。正如他在 [Agent Builder 内存系统的技术深度剖析](https://x.com/hwchase17/status/2011834318172422279) 中解释的那样：

“大型语言模型非常擅长处理文件系统，但从基础设施的角度来看，使用数据库更简单、更高效。”

这并非矛盾。这是一个深思熟虑的架构选择：

*   **接口** = 代理看到并与之交互的内容
*   **存储** = 数据实际持久化的地方

![Alt text: 一个双面板图，比较了“混淆”（文件系统与数据库作为竞争选择）与“现实”（代理访问和数据持久化作为独立层——接口根据用例选择，存储作为统一后端）。](https://cdn.thenewstack.io/media/2026/03/e538e45d-mongodb-article-slide-1.png)

争论不是“文件系统还是数据库”——而是认识到接口和存储是独立的决策。

这些是独立的决策。一旦你认识到这种区别，问题就从“文件系统还是数据库？”转变为“针对何种代理类型选择何种接口，由何种存储来支持何种要求？”

---

## 文件系统接口到底为AI代理提供了什么？

在 [MCP](https://thenewstack.io/when-is-mcp-actually-worth-it/) 和文件系统抽象之前，将代理连接到外部数据意味着为每个数据源定义自定义工具模式。每个端点都需要文档。每个模式都需要示例。正如 Arize 的 Tony Powell [观察到](https://arize.com/blog/agent-interfaces-in-2026-filesystem-vs-api-vs-database-what-actually-works/) 的：“当大型语言模型学会如何使用某个特定的 API 时，你已经耗费了大量的上下文窗口……你花费了数千个 token 用于教育而不是推理。”

文件系统接口提供了一种不同的方法：一组大型语言模型从其训练数据中已经理解的通用操作。这是 [20世纪70年代 Unix 的“一切皆文件”哲学](https://arxiv.org/html/2601.11672v1) 的重现，只是以新的规模出现。正如 Unix 将各种设备接口整合为文件操作，DevOps 将基础设施整合为代码 artifact，代理 AI 正在将各种数据源整合为文件系统操作。

核心操作：

*   **列表** — 显示位置内容 (例如 ls)
*   **读取** — 获取文件内容 (例如 cat)
*   **写入** — 创建或更新文件
*   **搜索** — 按名称或内容查找文件 (例如 find 和 grep)

实际好处是 token 效率：教育已经在预训练期间完成。正如 Turso 的 Pekka Enberg 在他 [关于 AgentFS 的文章](https://penberg.org/blog/disaggregated-agentfs.html) 中指出的：“让代理访问 grep、sed、awk、cat 和 git，它将变得非常强大和高效，无需自定义工具。”

Dust.tt 通过创建 “[合成文件系统](https://dust.tt/blog/how-we-taught-ai-agents-to-navigate-company-data-like-a-filesystem)” 扩展了这一概念——将 API 和数据库投射到文件系统般的层级结构中。Slack 频道变为目录。Notion 工作区变为文件夹。底层数据位于 API 和数据库中，但代理看到的是一个连贯的文件树。

![图表比较了 AI 代理数据接口的演变——自定义工具、MCP 和文件系统接口——突出显示通用文件系统操作与自定义模式相比如何需要零教育 token。](https://cdn.thenewstack.io/media/2026/03/c4d52158-table-screenshot-file-systems-vs-databases-2.jpg)

代理到数据接口如何从自定义工具演变为标准化文件系统操作。

---

## 文件系统接口在何处适用于 AI 代理？

文件系统模式已为 **编码代理** 展示了明确的价值。

这不足为奇。代码已经以文件形式组织在目录中。开发者以文件系统的术语思考。操作自然映射：读取文件、编辑文件、搜索代码库。像 Cursor、Claude Code 和 Windsurf 这样的工具都使用了这种模式。

Letta 团队在他们的 [基准测试分析](https://www.letta.com/blog/benchmarking-ai-agent-memory) 中提供了重要背景：“如今的代理在文件系统工具的使用上非常有效，这主要归因于针对代理编码任务的后期训练优化。”关键词是“代理编码任务”——这就是训练数据所在之处。

文件系统接口适用场景：

*   编码代理（代码已在文件中）
*   文档处理（文档映射到文件）
*   DevOps 和基础设施（配置是文件）
*   知识库导航（层级结构有效）

## 文件系统接口在AI代理中何时失效？

文件系统模式并非通用。在某些场景下，它的局限性会暴露无遗，尝试过它的实践者也坦率地承认了失败。

### 结构化数据查询

你无法通过 grep 来查询“查找所有在第三季度订购了产品 X 但未订购产品 Y 的客户”。对于涉及连接、聚合或图遍历的查询，文件系统操作会显得笨拙。

[Vercel 的基准测试](https://vercel.com/blog/testing-if-bash-is-all-you-need) 清楚地说明了这一点。当他们将文件系统操作与结构化数据的数据库查询进行测试时：

![基准测试表比较了 AI 代理方法，显示数据库查询在准确性上达到100%，同时与 Bash 和文件系统方法相比，token 使用量、成本和持续时间显著降低。](https://cdn.thenewstack.io/media/2026/03/0c8c6dbf-table-screenshot-file-systems-vs-databases.jpg)

总结：对于具有明确模式的结构化数据，专用查询语言——无论是 SQL、MongoDB 的查询 API 还是其他数据库接口——始终优于文件系统操作。

### 规模化性能

文件系统抽象隐藏了一个关键问题：每个文件操作都可能变成一个 API 调用。Hacker News 上的一位实践者 [描述了完全放弃这种方法](https://news.ycombinator.com/item?id=46582331)：“如果你通过 grep (via fuse) ，你最终会打开大量文件，这将导致对某些 API 的 fetches，而且速度会很慢……我们甚至在 Rust 中实现了这个想法来真正测试它，但最终被抛弃了，因为，嗯，它很糟糕。”

LlamaIndex 的 Jerry Liu 在“[文件即一切所需](https://www.llamaindex.ai/blog/files-are-all-you-need)”中也提出了类似的观察：“编码代理已经使用 CLI 工具作为文件搜索的主要方式，但我们注意到这种方法无法扩展到大规模文档集合（1k-1m+）。”

问题是根本性的：文件系统缺乏使数据库查询快速的索引。

### 无服务器和云原生环境

文件系统隐喻假设存在文件系统，但许多生产环境——例如无服务器函数、基于浏览器的代理和边缘计算——没有持久的本地存储。

### 非编码代理类型

客户服务代理需要结构化客户数据。分析代理需要数据库查询。使文件系统接口对编码代理强大的训练数据优势可能不会延续到这些领域。

## 为什么领先团队使用数据库存储作为代理记忆？

无论你选择哪种接口模式，领先团队在底层都已趋同于数据库存储：

![图表说明了 LangChain、Dust.tt、Turso 和 Letta 等领先 AI 团队如何使用不同的文件系统接口层，同时统一依赖底层数据库存储层作为代理记忆。](https://cdn.thenewstack.io/media/2026/03/c1977922-table-screenshot-file-systems-vs-databases-3.jpg)

**原因是一致的：**

*   **多代理协调** 需要事务。当多个代理共享状态时，你需要 ACID 保证。
*   **规模化** 需要索引。grep 适用于小型集合；生产系统需要数据库级别的查询优化。
*   **治理** 需要审计追踪。企业部署需要追踪谁在何时、为何访问了什么。
*   **混合检索** 是基本要求。生产系统 [需要向量搜索](https://thenewstack.io/why-developers-need-vector-search/)、全文搜索和结构化查询协同工作。

集成了向量搜索的文档数据库在这里特别适用。一个结合了灵活文档存储、向量嵌入和全文搜索的平台消除了拼接多个系统的需要。

## 开发者应如何为代理记忆选择接口和存储？

文件系统接口 [并非唯一选择](https://www.mongodb.com/docs/atlas/atlas-vector-search/ai-agents/)。对于某些代理类型，它也不是最佳选择。

像 MongoDB Atlas 这样的文档数据库将数据存储为 JSON 文档，其结构已经“类似文件”。凭借内置的 [原生向量搜索](https://www.mongodb.com/products/platform/atlas-vector-search)、全文搜索和 [聚合管道](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/)，代理可以直接通过 [MCP 工具](https://www.mongodb.com/docs/mcp-server/get-started/) 或 API 进行查询——无需文件系统转换层。对于分析代理、客户服务代理或任何涉及结构化数据查询的工作流，这种直接路径可能优于文件系统接口。

当代理的训练数据使得 `ls` 和 `grep` 比自定义工具更可靠时，文件系统接口会发挥作用，这主要适用于编码代理。但这种训练数据优势并非适用于所有领域。

[图 3：解耦架构]

![一个三层架构图，显示代理位于顶部，连接到接口层（包括文件系统、MCP 工具和直接 API 选项），该接口层又连接到存储层（文档数据库 + 向量搜索 + 全文搜索 + ACID）。](https://cdn.thenewstack.io/media/2026/03/56f78fd1-mongodb-article-slide-2.png)

新兴架构将接口和存储选择解耦，使团队能够独立优化每一层。

**真正要问的问题：**

*   **什么代理类型？** 编码、文档、分析、客户服务？
*   **什么接口适合该类型？** 编码代理用文件系统，结构化数据用 MCP/直接查询。
*   **有什么存储要求？** 规模、多代理协调、治理、检索模式？
*   **你需要转换层吗？** 或者代理可以直接查询数据库吗？

## 架构正在趋同。这对开发者意味着什么

“文件系统与数据库”的框架模糊了真相，多于揭示真相。构建生产级代理系统的团队已经超越了这场争论。他们将接口与存储分离，无论向代理公开哪种接口，底层都使用数据库。

> “结构化数据、非编码工作流和无服务器环境需要不同的方法。”

文件系统接口在编码代理和文档导航中运行良好，因为那里存在训练数据，且隐喻适用。但它并非通用。结构化数据、非编码工作流和无服务器环境需要不同的方法。

问题从来都不是“文件系统还是数据库？”它 [始终是两者兼而有之——在正确的层级上](https://www.mongodb.com/company/blog/technical/converged-datastore-for-agentic-ai)。