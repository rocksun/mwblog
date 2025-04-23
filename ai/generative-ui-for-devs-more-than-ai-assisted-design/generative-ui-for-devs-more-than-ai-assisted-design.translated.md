# 面向开发者的生成式 UI：不仅仅是 AI 辅助设计

![Featued image for: Generative UI for Devs: More Than AI-Assisted Design](https://cdn.thenewstack.io/media/2025/04/43cc88d4-founders_thesys-c1-2-1024x576.jpg)

[生成式 AI](https://thenewstack.io/how-generative-ai-is-reshaping-the-sdlc/) 正被用于创建设计，但一种名为[生成式用户界面](https://docs.thesys.dev/guides/genui) (GenUI) 的新型 AI 驱动方法超越了静态设计，允许 [Web 开发人员](https://roadmap.sh/roadmaps?g=Web+Development) 利用 AI 和数据来实现更个性化的应用程序和分析显示。

The New Stack 采访了 [Thesys](https://www.thesys.dev/) 的联合创始人兼 CEO Rabi Shanker Guha，了解生成式 UI 对开发的意义。该公司专注于 AI 驱动的界面，并创建了 [Canvas](https://www.thesys.dev/products/canvas)，这是一款用于对话式 AI 产品的设计工具。一些工具和平台为 UI 生成或 UI 组件的代码生成提供 AI 辅助功能，例如 [GitHub Copilot](https://thenewstack.io/github-copilot-and-open-source-a-love-story-that-wont-end-well/)、[Amazon](https://aws.amazon.com/?utm_content=inline+mention) [CodeWhisperer](https://thenewstack.io/decoding-amazons-generative-ai-strategy/) 和 [Vercel’s v0](https://v0.dev/)。

周一，Thesys 推出了一款名为 [C1](https://docs.thesys.dev/guides/solutions/chat) 的新产品，该公司表示这是第一个旨在提供 GenUI 功能的 API。

Guha 说，生成式 UI 为开发人员提供了一种创建动态生成的图形用户界面的方法，该界面可以适应用户输入、上下文和偏好，从而获得更个性化的体验。

“这与 [AI 辅助设计](https://thenewstack.io/figma-redesign-shows-how-ai-can-transform-apps-adds-dev-support/) 非常不同……它基本上是将提示转换为设计。但这就像让开发人员助手为你完成工作，”Guha 说。“它可以解释意图。它可以解释数据。它可以解释……例如，你的地理位置 [和] 一天中的时间，然后实时向你呈现理想的用户界面。”

生成式 AI 擅长理解意图。你可以要求 AI 帮助你购买手表，并明确地向其提供有关你自己的信息——你的国家、你的年龄、你的性别、你想要的手表类型——它将生成推荐。

他说，C1 采用了意图的概念，并从中创建了一个界面。它将现代应用程序的可用性设计与 AI 的智商相结合——所有这些都通过 API 来实现。

“C1 API 弥合了这一差距，”Guha 说。“现在，世界上所有的 AI 代理或 AI 强大界面都可以拥有丰富的可视化 UI 的优点。”

## 全新的设计/前端开发工作流程

目前，设计师倾向于在 Figma 或类似的工具中工作，然后将设计移交给开发人员进行编码。这可能会导致转换难题。

Guha 并不认为 C1 是一款面向设计师的工具，但表示它可能会带来一个设计师和开发人员在同一解决方案中共存的世界。

“Thesys 的 C1 是我们弥合这一差距并结合 AI 和 [[大型语言模型](https://thenewstack.io/llms-can-now-trace-their-outputs-to-specific-training-data/)] 的所有智能与传统 UX 的优点的尝试，”Guha 说。“我们可以将整个过程浓缩为更多由 LLM 驱动的开发模型。”

C1 的软件开发工具包 (SDK) 可以集成到网页或应用程序中，只需 [三行 React 代码](https://docs.thesys.dev/guides/setup)，从而允许开发人员通过提示开始尝试输出。

该公司用于展示其功能的一个例子是“哈利·波特”电影演员阵容的展示。开发人员可能已将其创建为列表，但设计师可能会推荐轮播。开发人员无需对其进行编码，而是可以返回 C1 并告诉它以轮播形式显示演员阵容。

“下次你的用户提出要求时，”他说，“现在它就是一个轮播。”

![A carousel of the Harry Potter cast made by Thesys C1.](https://cdn.thenewstack.io/media/2025/04/c95e6517-harrypotter_c1_use.jpg)
Thesys C1 制作的“哈利·波特”电影演员阵容的轮播。

## C1 的生成式 UI 解决方案

C1 可以作为 LLM API 的直接替代品。例如，如果前端开发人员正在使用 [OpenAI 的 API](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/)，则开发人员可以切换 OpenAI API，将 URL 从 OpenAI 库更改为 Thesys URL，以开始通过提示实时设计。
C1 有两个部分，Guha 说。一部分是 API 本身，它被设计为与 OpenAI 兼容。这意味着开发人员可以继续使用他们喜欢的工具，例如 [模型上下文协议 (MCP) 服务器](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) 和现有的内存集成，而无需学习新的工具或解决方案。

他还补充说，还有一个 Thesys 前端 SDK，可以与开发人员现有的 [React](https://thenewstack.io/how-to-build-a-carbon-aware-website-using-react-and-next-js/) 代码库集成。Thesys 的解决方案与 React 18 以上的任何版本兼容。

他澄清说，Thesys 不会流式传输 React。它流式传输 UI 的表示形式，并使用 SDK 在消费者端转换为 React。

C1 使用 [Crayon](https://github.com/thesysdev/crayon)，这是一个 MIT 许可的 UI 工具包，用于构建 AI 代理。它由 Thesys 创建，其核心是一个基于 React 的库，可以抽象出状态管理和后端集成。根据文档，它是轻量级的，可以与任何 HTTP 服务器集成，包括 [LangChain](https://thenewstack.io/benchmark-llm-application-performance-with-langchain/)、[CrewAI](https://thenewstack.io/how-crewai-enables-ai-agents-as-collaborative-team-members/) 或一个简单的 FastAPI 服务器，该服务器为 LLM 驱动的代理提供服务。它旨在与 C1 无缝集成，但它不依赖于 Thesys。

C1 文档显示，GenUI 工具正在利用 [Anthropic](https://thenewstack.io/deno-2-0-angular-updates-anthropic-for-devs-and-more/) LLM [Claude Sonnet 3.5](https://www.anthropic.com/news/claude-3-5-sonnet)。该公司计划扩展 LLM 产品，以便开发人员可以选择使用 C1 部署哪个模型。

有一个 [开发者游乐场](https://chat.thesys.dev/) 可以探索 C1。

## 热门用例：分析和表单

C1 并非旨在创建简单的着陆页。

Guha 说：“例如，如果您正在为您的作品集构建一个着陆页，那么 Thesys 的 C1 实际上并不能为您提供太多帮助。但是，如果您正在考虑使用 AI 重新构想您的 CRM 软件，那么 Thesys 的 C1 就能真正发挥作用。”

他说，它的真正力量在于使用数据：“人们可以使用我们来构建几乎任何 AI 界面，但如果您谈论我们的经验，到目前为止，我们已经看到分析特定用例的最大胜利。分析是 AI 明显优于您必须学习 [Power BI](https://thenewstack.io/power-bi-gets-low-code-datamart-feature/) 或您必须学习如何构建 Salesforce 仪表板的地方之一。”

Thesys 的一位客户专门将 C1 用于 [销售数据](https://thenewstack.io/salesforce-officially-launches-einstein-ai-based-data-cloud/)。该客户已经创建了一个解决方案，该解决方案从软件即服务解决方案和其他来源引入数据，然后在它之上构建了一个带有 OpenAI 的层，该层可以理解查询并返回输出。用户可以询问本月管道中有多少客户，它会获取所有这些数据，进行处理并在文本中生成结果。

他说：“他们已经在构建这个了，但他们很难弄清楚如何可视化这些数据，如何以自然、直观的方式呈现它。您在文本中得到了这个响应，但文本可能不是表示这些数据的最佳方式。有时，图表可能是表示这些数据的更自然的方式。”

该公司用 Thesys API 替换了其 OpenAI 端点。现在，客户可以提出各种问题，例如“现在有多少人正在使用我们的产品？”或“我们失去了多少客户？”

Guha 说：“它在前端生成一个实时的 React 组件，带有按钮、表单和所有元素。”

另一家公司带着一款基于文本的测验的 edtech 产品找到了 Thesys：基本上，它会问一个问题，用户必须在文本字段中键入答案。C1 能够将测验变成一个带有选择题和按钮的表单。

Guha 说：“假设您正在构建一个非常简单的测验的 AI 版本。因此，您使用了 Open AI，并且您对 Open AI 说，‘给我 10 个问题，对于这 10 个问题中的每一个，给我四个选项，然后扮演一个测验的角色’。我们基本上是建立在现有 LLM 之上的，所以我们理解所有这些上下文。”

他还补充说，它也理解数据。因此，它将生成输出的 UI 表示形式，为开发人员提供这 10 个问题，但将其呈现为带有选择题、按钮选项的表单。

Guha 说：“这些是我们看到的最大用例。但是，您可以利用它做的事情是无限的。”

[YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)