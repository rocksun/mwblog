# Vercel 的未来大计：为开发者提供 AI SDK 和加速器

Vercel 的首席执行官 Guillermo Rauch 表示，构建人工智能应用是开发者注册 Vercel 的第二大原因。因此，推出了 Vercel AI 软件开发工具包和加速器。

翻译自 [Vercel’s Next Big Thing: AI SDK and Accelerator for Devs](https://thenewstack.io/vercels-next-big-thing-ai-sdk-and-accelerator-for-devs/) 。

![](https://cdn.thenewstack.io/media/2023/08/44c86c7c-ai_sdk-1024x602.jpg)

在 2020 年代，很少有公司像 Vercel 这样对前端开发生态系统产生了如此大的影响， Vercel 是流行的 React 框架 Next.js 的管理者。当我首次写关于 Vercel 的文章时，那是[在 2020 年 7 月](https://thenewstack.io/vercels-frontend-and-the-rise-of-the-hybrid-developer/)，该公司刚刚拥抱了 Jamstack 趋势，并在其营销中广泛使用“无服务器”这个词汇。但[随着 Jamstack 趋势的下降](https://thenewstack.io/is-jamstack-toast-some-developers-say-yes-netlify-says-no/)和[无服务器](https://thenewstack.io/serverless/)不再是一个热词，Vercel [抓住了](https://vercel.com/ai)最新的“下一个大事”：生成式人工智能。

Vercel 相对较新的 [AI SDK](https://vercel.com/blog/introducing-the-vercel-ai-sdk) 在 JavaScript 开发者中迅速获得了认可，目前每周在 npm 上有 [40,000](https://twitter.com/steventey/status/1694791680262820295) 次的下载量。当然，原因在于 2023 年 AI 应用的惊人流行。Vercel 的首席执行官 Guillermo Rauch 上周在[推特](https://twitter.com/rauchg/status/1694781696657568162)上表示，“构建 AI 应用是人们现在注册 @vercel 的第二大原因，超过社交/营销和电子商务，根据注册调查。”（尽管他没有明确说明第一位是什么，但有评论者表示它是易于部署的 Next.js 项目。）

## Vercel AI SDK 是什么？

Vercel 将这个 SDK 定义为“用于基于 React 和 Svelte 构建的 AI 应用的可互操作、支持流媒体的、准备好上线的软件开发工具包”。它支持 React/Next.js 和 Svelte/SvelteKit ，对 Nuxt/Vue 的支持“即将推出” [更新：Vercel已经考虑支持 Nuxt 和 Solid.js 框架]。在 LLM 方面，SDK “包括对 OpenAI、LangChain 和 Hugging Face Inference 的一流支持”。为了补充 SDK，Vercel 还提供了一个拥有 20 多个 LLM 的 [playground](https://sdk.vercel.ai/) 。

> Vercel AI SDK 的吸引力类似于最初使 Vercel 在 JavaScript 开发者中如此受欢迎的原因：它抽象了应用程序的基础架构部分。

那么，与现有的 LLM 应用堆栈工具如 LangChain 相比，这个 SDK 如何？我向 Rauch 求证，他表示 Vercel AI SDK “专注于帮助开发者构建完整、丰富的流媒体用户界面和应用程序，并深度集成/支持前端框架”，而 “LangChain 专注于 ETL [提取、转换和加载]和提示工程”。

Rauch 补充说，AI SDK 与 LangChain 有整合。“开发者可以使用 LangChain 进行提示工程，然后使用 AI SDK 在他们的应用程序中进行流媒体和渲染输出，”他在 X/Twitter 直接消息中说道。他还给我提供了其文档中有关 [LangChain](https://sdk.vercel.ai/docs/guides/providers/langchain) 的更多参考信息。

## 示例 AI 应用程序：Memorang

为展示其新获得的 AI 技能，Vercel 本月举行了 [AI 加速器演示日](https://vercel.com/blog/vercel-ai-accelerator-demo-day)。总获胜者是一家名为 [Memorang](https://memorang.com/) 的初创公司，Vercel 描述它为“用于构建任何学科的基于 AI 的课程和学习应用程序的完整平台”。

Memorang 目前处于私人测试阶段，但在演示日的快速介绍中，我们可以看到现今基于 AI 的应用程序的样貌。创始人兼首席执行官 [Dr. Yermie Cohen](https://www.linkedin.com/in/yermie/) 解释说，Memorang 是“建立在现代和不断发展的 AI 技术堆栈上，包括 Vercel，其中大部分几个月前还不存在”。

![](https://cdn.thenewstack.io/media/2023/08/9e638497-edwrite1.jpg)
*Memorang platform*

Memorang 的第一部分是一个名为 EdWrite 的“基于 AI 的无头 CMS”，它大量使用生成式 AI 进行内容生成，这里指的是教育材料。Cohen 指出了使用 AI 进行这类内容的扩展性好处。“您的自定义工作流实际上是一个内容大炮，您可以瞄准并发射，以构建成千上万的评估，”他说道。

使用这些内容，Memorang 能够为客户（可能是教育机构）提供“基于 AI 的 Web 和移动学习应用程序，具有可组合性和白标签化”。然后，他讨论了这种方法对用户的一些好处。“当用户完成学习会话时，他们会得到关于性能行为的个性化 AI 分析和改进建议，”他指出。“然后，在回顾他们的答案时，我们的 AI 学习助手帮助他们更多地学习，深入探讨每个练习问题。”

![](https://cdn.thenewstack.io/media/2023/08/b9b73d1a-edwrite2.jpg)
*Memorang EdWrite*

## AI 工程师技术栈

虽然 Cohen 没有讨论 Memorang 用来创建其平台的技术堆栈，但您可以从查看公司当前的职位空缺中获得一些线索。具体来说，查看以下关于[全栈 AI 工程师](https://wellfound.com/jobs/2726962-full-stack-ai-engineer-langchain-serverless-vector-dbs-react)职位的要求：

- TypeScript/JavaScript 的专业知识
- 在提示工程方面的高级知识
- 使用 OpenAI +/- Langchain 完成的项目
- 具有向量数据库和语义搜索经验
- 具有 GraphQL 等无服务器堆栈的专业知识
- 深入了解 NoSQL 数据库设计和访问模式
- 前端技能包括 React（理解 hooks、组件）
- 大学学位（技术领域）

该角色的工具、库和框架列表如下：

- Langchain.js
- AWS Lambda
- Pinecone / Weaviate
- DynamoDB / MongoDB
- Neptune/Neo4j
- React + React Native
- GraphQL
- Next.js

显然，React 在构建 Memorang 的用户界面和连接到 LLM、向量数据库和 LangChain 等 [AI 堆栈组件](https://thenewstack.io/llm-app-ecosystem-whats-new-and-how-cloud-native-is-adapting/)方面起到了重要作用。

## 下一个大事

对于那些想要查看可公开使用的 AI 应用程序的开发者，Vercel 提供了一个使用以下工具的 [Pokedex 模板](https://postgres-pgvector.vercel.app/)：

- 在 Vercel 上的 Postgres
- Prisma 作为 ORM [对象关系映射]
- 用于向量相似性搜索的 pgvector
- OpenAI 嵌入
- 使用 Next.js App Router 构建

但也许最好的开始使用 Vercel AI SDK 的地方是 Vercel 的[快速入门文档](https://sdk.vercel.ai/docs/getting-started)。它提供了 Next.js 和 SvelteKit 的说明。如果您仍在寻找创意，可以查看 Vercel 的 [AI 应用程序模板](https://vercel.com/templates/ai)和示例。

最后一点说明：显然，Vercel 尚未完成其 AI 功能的推出。Vercel 开发者体验副总裁 Lee Robinson 在 X 上的最新[评论](https://twitter.com/leeerob/status/1690071476785811456)总结了这一点：“下一个大事？‘肯定是 AI，以某种形式，而且我们在这方面还有很多可以做的事情！’"

![](https://cdn.thenewstack.io/media/2023/08/35f85d58-vercel_lee.png)
