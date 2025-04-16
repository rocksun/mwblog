# 案例研究：AI Agent 将 API 连接器开发时间缩短至几分钟

![案例研究特色图片：AI Agent 将 API 连接器开发时间缩短至几分钟](https://cdn.thenewstack.io/media/2025/04/661937e6-ai_created_connectors-1024x579.jpg)

图片由 Getty Images 通过 Unsplash 提供

软件开发公司 [Fractional AI](https://www.fractional.ai/) 认为，AI 领域最大的赢家将是那些使用生成式 AI 来提高运营效率和改进产品的非 AI 公司。

为此，Fractional AI 为开源数据集成公司 [Airbyte](https://thenewstack.io/pyairbyte-airbytes-new-python-library-for-moving-data/) 创建了一个 [AI agent](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)，用于构建 [API](https://thenewstack.io/use-api-governance-tools-for-better-api-experiences/) 集成的连接器。这些由 AI 创建的连接器不再需要几天的手工编码，而只需几分钟即可完成。

Fractional AI 的 CEO [Chris Taylor](https://www.linkedin.com/in/taylorcd/) 告诉 The New Stack：“我们发展得非常快，这很有趣。在最前沿从事许多很酷的项目也很有趣。”

Airbyte 是一个 [开源数据集成引擎](https://github.com/airbytehq/airbyte)，用于将数据移动到数据仓库、[数据湖](https://thenewstack.io/observability-without-a-data-lake-might-no-longer-work/) 或数据库。它通常用于从软件即服务产品中提取数据，这当然需要与这些 SaaS API 的连接器。

例如，如果有人想将 [Shopify](https://thenewstack.io/recreating-shopifys-bfcm-globe-using-react-globe-gl/) 销售数据与 [ZenDesk](https://www.zendesk.com/) 客户支持数据结合起来，则可以使用 Airbyte 设置数据管道，从 Shopify 提取客户数据，从 Zendesk 提取客户支持工单，然后将所有数据加载到数据仓库中。

Airbyte 已经拥有一个连接器库来支持这项集成工作，但该公司设想简化创建数千个与 SaaS 产品的连接器。

Fractional AI 的 CTO [Eddie Siegel](https://www.linkedin.com/in/eddiesiegel/) 告诉 The New Stack：“他们的软件正在从第三方 [SaaS](https://thenewstack.io/goodbye-saas-hello-ai-agents/) 工具中提取数据，并将数据移动到数据仓库中。他们需要与可能存在的每种第三方 SaaS 工具类型建立集成。”

Airbyte 将该解决方案称为 [AI Assistant](https://airbyte.com/blog/hands-on-with-the-new-ai-assistant)，并且运行良好。自该工具发布以来，其库中已添加了更多的连接器。

![图表显示了在 AI Assist 之前构建的 Airbyte 连接器，以及在引入 AI Assist 后连接器数量的显著增长。](https://cdn.thenewstack.io/media/2025/04/0aad9a47-fractionalaiairbyteconnectors_built-1024x658.jpg)

图片由 Fractional AI 提供

## AI 之前的 API 构建

构建 Airbyte 的解决方案并不像将 API 文档交给 AI 工具那么简单。Airbyte 想要一种自动化解决方案，可以扫描 API 文档，因为这些文档的结构往往有些随意。

Siegel 说：“我们意识到，这些面向开发人员的 API 文档是非常复杂的网站。它们是 [Google](https://cloud.google.com/?utm_content=inline+mention) 无法很好地索引的页面类型；它们是高度动态的。它们不是由希望它被很好地索引的人设计的。”

API 文档没有标准化，而且通常是厚重且密集的阅读材料。爬取这些文档最终成为 Fractional 在涉及 AI 之前必须解决的一个出乎意料的复杂问题。

Siegel 说：“他们没有让 Web 爬虫很容易读取它们。”

由于上下文窗口大小的限制，他补充说：“调整爬取过程的难度可能比我们最初预期的 AI 方面要高出一个数量级。”

一旦文档被梳理完毕，开发人员将面临大量的手动编码。正如 [Fractional AI 网站上的案例研究](https://www.fractional.ai/case-study/api-integrations-in-minutes-how-fractional-ai-airbyte-10xd-the-speed-of-building-connectors) 指出的那样，这个耗时且复杂的过程分散了技术人才，使他们无法从事更高价值的工作。

## AI/开发人员工作流程

最终的工作流程允许用户输入他们尝试集成的 API 的 URL。AI Connector Builder 爬取这些 API 文档，然后预先填充有关连接器的所有字段，例如 API URL 基础和身份验证。

然后，AI Connector Builder 会显示该 API 的完整流列表——例如，对于 Shopify，流可能包括“订单”、“履行”和“折扣”。
用户随后选择感兴趣的流，对于选择的每个流，构建器会预先将这些流的每个字段（分页、URL 路径等）填充到 Airbyte 的连接器构建器 UI 中。然后，用户可以查看 AI 的草稿，并在最终确定连接器之前进行编辑或更正。

因此，基本上，AI 工具的最终工作流程包含五个部分：

- 抓取文档页面。
- 大型语言模型驱动的爬虫引擎查找要抓取的其他页面。
- 将 HTML 转换为 markdown 并尽可能消除噪音。
- 从抓取的页面中提取适当的部分，并将它们包含在精心制作的、专门构建的提示中。
- 将 LLM 输出转换为连接器定义的适当部分。

## AI 辅助的幕后原理

在幕后，AI 助手利用了 [GPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/)。该团队探索了 4o-mini 和 4o-mini 的微调版本，但最终只使用了 [4o-mini](https://thenewstack.io/openais-realtime-api-takes-a-bow/) 进行集成测试。[Claude](https://claude.ai/) 也被考虑过，但案例研究指出，选择 GTP-4o 是因为它具有严格的结构化输出能力。

Fractional AI 使用 [OpenAI](https://openai.com/) 的软件开发工具包 (SDK) 将提示拼接在一起。

第一步是读取 API 文档。AI 系统首先会问：“是否有 [OpenAPI](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) 规范？” 如果有，它可以直接从 OpenAPI 规范中提取身份验证参数。

但是，如果没有 OpenAPI 规范，Fractional AI 会使用 AI 搜索工具 [Jina AI](https://jina.ai/) 和 [Firecrawl](https://www.firecrawl.dev/) 抓取 API 文档，Firecrawl 是一种 API 服务，它接受 URL，对其进行抓取并将其转换为干净的 markdown 或结构化数据。

“最后，如果我们无法使用 OpenAPI 规范、Firecrawl 或 Jina 提取信息，我们会结合使用多种服务，”例如 Web 抓取工具 [Serper](https://serper.dev/) 和 AI 搜索引擎 [Perplexity](https://www.perplexity.ai/)，“作为最后的努力，以找到相关信息输入到后面的 [LLM](https://thenewstack.io/ai-agents-are-dumb-robots-calling-llms/) 中，”案例研究指出。

第二步是提取相关的 API 连接器部分。如果文档太大以至于超过了上下文窗口，Fractional AI 会使用 [OpenAI 的内置检索增强生成 (RAG)](https://thenewstack.io/openai-rag-vs-your-customized-rag-which-one-is-better/) 功能来提取文档中与身份验证相关的部分。

对于较小的文档，Fractional 构建了一个流程，首先从 HTML 中提取链接，然后询问 LLM 哪些链接看起来与身份验证相关，然后将抓取的页面的内容嵌入到未来的提示中。

最后，该过程涉及解析和提示 HTML 块中的确切细节。挑战在于将 LLM 输出强制转换为连接器构建器规范所需的精确格式。Fractional 的解决方案是“使用结构化输出进行提示，以确定特定格式的身份验证方法，从而填充连接器构建器。”

最终解决方案中使用的其他工具包括 [Langsmith](https://www.langchain.com/langsmith)，它是一个帮助开发人员构建、调试、测试和监控 LLM 应用程序的平台，用于可观测性和实验。Fractional 还利用了 OpenAI 的内置 [向量存储，在需要 RAG 的地方](https://thenewstack.io/how-to-store-embeddings-in-vector-search-and-implement-rag/)，并利用 [Redis](https://redis.com/?utm_content=inline+mention) 进行缓存和锁定。

Fractional AI 案例研究指出：“我们使用现有 [Airbyte 连接器](https://airbyte.com/connectors) 的目录作为基准来衡量 AI 驱动的连接器构建器的准确性并提高质量。”

虽然案例研究没有详细说明测试数据，但它指出准备测试数据“花费了大量精力……并且应该是任何应用 AI 项目的重点。”

在最终分析中，Fractional AI 的案例研究指出，“在许多高 ROI 的地方，正确的 AI 应用程序可以显着提高开发人员的生产力。”

“既是工程问题又是 AI 问题：这个项目很好地提醒我们，将 AI 投入生产的挑战不仅仅是来自处理 LLM 的纯粹问题，”该团队写道。“在这种情况下，高质量的爬取——一个与 [Google](https://thenewstack.io/ironwood-googles-answer-to-nvidia-in-the-ai-chip-wars/) 一样古老的挑战——提出了一个主要的挑战。”

[
[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)