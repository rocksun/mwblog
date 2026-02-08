Python主导了机器学习的早期阶段，但随着AI变得更加主流，这种情况正在发生变化。以最近发布的[Mastra](https://mastra.ai/)为例，它是一个开源的[智能体AI框架，使用TypeScript](https://github.com/mastra-ai/mastra)而不是[Python](https://thenewstack.io/what-is-python/)。

Mastra的联合创始人兼全栈开发者Sam Bhagwat表示，开发者对大型语言模型的内部运作兴趣较小，而对如何基于这些模型构建应用程序更感兴趣。Sam Bhagwat以其作为Web框架[Gatsby](https://thenewstack.io/netlify-acquires-gatsby-its-struggling-jamstack-competitor/)联合创始人而闻名。

他说，[开发者不必了解Python](https://roadmap.sh/python/how-long-does-it-take-to-learn)也能构建智能体，因为它们不需要像模型那样繁重的计算工作。

Bhagwat告诉《The New Stack》：“构建智能体通常不需要那种繁重的工作。更多的是‘嘿，我是否在此时为我的智能体提供了正确的上下文？它是否有能力调用正确的工具，代表使用它的用户执行操作？我能否获得正确的信息？’这更接近于Web应用开发。”

他补充说，这就是[前端开发者](https://thenewstack.io/introduction-to-frontend-development)的领域。

他说：“基本上，有一整个全栈工程师社区被遗漏了，因为我们不是真正的Python使用者。我们是JavaScript类型的人。我们想为他们打造一个出色的工具。”

## 为什么选择TypeScript？

Bhagwat告诉TNS，TypeScript已经成为现代产品团队的一种默认语言。

Bhagwat说：“TypeScript往往更适合Web应用开发，因为你的前端几乎总是用JavaScript或TypeScript编写。如果后端也用TypeScript编写，你就能获得更好的集成。”

它还[向TypeScript熟练的开发者开放了AI智能体](https://thenewstack.io/open-responses-vs-chat-completion-a-new-era-for-ai-apps/)的世界。事实上，去年GitHub透露，[TypeScript在平台上超越了Python和JavaScript](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)，成为使用最多的语言。GitHub团队表示，这一采用转变“标志着十多年来最重要的语言转变”。

## 从AI智能体开始

Bhagwat表示，智能体已经改变了我们与互联网交互的方式。

他说：“对于身处Dev Tools世界的人来说，这真的很有趣，因为我们正在从人类编写代码的世界，转向人们使用Claude Code或Cursor编写代码的世界。这改变了一些事情。”

越来越多的人正在将内部文档与AI结合使用，AI通常会寻找markdown格式的内容。

他解释说：“如果一个智能体正在浏览网页并寻找文档，因为它是一个编码智能体，它通常会寻找markdown格式的内容，因此它会发送一个markdown请求。现在，一些人正在改变文档的内容，专门为智能体添加特殊指令，因为他们可以判断谁是访问者。”

> “…我们正在从人类编写代码的世界，转向人们使用Claude Code或Cursor编写代码的世界。”
> **– Mastra联合创始人 Sam Bhagwat**

Web开发者学习构建AI智能体有多重要？

Bhagwat看到越来越多的商业人士使用AI来编写解决方案，甚至训练他们自己的智能体。此外，前端云服务提供商Vercel的首席执行官兼Next.js的创建者Guillermo Rauch警告说，前端开发的下一次演进将聚焦于构建AI智能体。

目前，开发者们正在像往常一样通过个人副项目来摸索和[学习构建AI智能体](https://thenewstack.io/beyond-dx-developers-must-now-learn-agent-experience-ax/)。例如，Bhagwat每周都需要列一份购物清单。他构建了一个智能体，能够理解他家庭的饮食偏好。他说，许多开发者都在启动类似的个人项目，以便在需要将其部署到企业中之前了解这项技术。

为了帮助开发者入门，Bhagwat编写了一本电子书[*构建AI智能体原则*](https://mastra.ai/books/principles-of-building-ai-agents)，旨在让开发者快速了解关于智能体以及如何使用Mastra进行构建的知识。该书可通过电子邮件注册免费下载。

他还撰写了第二本书[*构建AI智能体模式*](https://mastra.ai/books/principles-of-building-ai-agents)，同样可通过电子邮件注册获取。

## Mastra开箱即用的功能

Bhagwat表示，如果你曾使用[Replit](https://replit.com/products/agent)构建智能体，那么你已经使用过Mastra。但让我们来看看这个完整的框架能为你提供什么。

Mastra提供了一些核心框架原语，首先是智能体，它们是使用大型语言模型、特定提示指令和工具来完成用户请求的自主代码。它还支持工作流，允许开发者编排复杂的、多步骤的过程。当然，它还整合了RAG（检索增强生成）功能，内置支持数据同步、网络抓取和向量数据库管理。它提供了一个[MCP服务器](https://modelcontextprotocol.io/docs/getting-started/intro)，允许用户向AI提供本地文档副本。

该工具兼具短期和[长期记忆系统，允许智能体](https://thenewstack.io/how-to-add-persistence-and-long-term-memory-to-ai-agents/)在不同线程和会话中记住上下文。

Mastra用户还可以访问以下工具：

* Mastra Studio，一个本地开发者平台，Web开发者可以在其中实时可视化、测试和调试智能体和工作流。
* [模型上下文协议](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) 客户端，允许开发者将智能体连接到预构建工具，如Google Sheets、GitHub或内部数据库，而无需编写自定义集成；
* AI追踪和可观测性，使开发者能够查看大型语言模型的推理过程，并提供令牌计数和执行步骤；以及
* 评分器和评估器，这些工具使用模型评级或基于规则的指标来衡量AI智能体的性能和准确性。它们旨在帮助开发者在部署到生产环境之前优化提示。

该公司还提供一个完全托管的云平台，实现零配置部署。

## 框架支持

Mastra团队已与一些前端框架进行了集成，包括：

```
* Next.js
* SvelteKit
* Astro
* Remix
* Nuxt
```

在[后端，它支持](https://mastra.ai/blog/changelog-2026-01-20)：

```
* Express
* Hono
* Elysia
* Node.js
```

Mastra还与智能体UI库集成，这些库专门帮助Web开发者构建智能体前端体验，例如：

* [CopilotKit](https://mastra.ai/guides/build-your-ui/copilotkit)，一个开源框架，帮助在现有应用程序中直接构建Copilot体验；以及
* [Assistant UI](https://mastra.ai/guides/build-your-ui/assistant-ui)，一个开源的TypeScript和React库，帮助开发者构建高质量的AI聊天界面。