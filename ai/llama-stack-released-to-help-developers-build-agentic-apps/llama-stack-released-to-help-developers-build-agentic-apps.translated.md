# Llama Stack 发布，帮助开发者构建“代理应用程序”

![Llama Stack 发布，帮助开发者构建“代理应用程序”的特色图片](https://cdn.thenewstack.io/media/2024/10/eb6497fd-llama-stack-feature-1024x576.jpg)

在 2024 年的 Facebook Connect 大会上，Meta 的年度开发者大会，该公司发布了 [Llama 3.2](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/)，其最新的大型语言模型。Meta 表示其 [Llama LLM 是开源的](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/)，尽管其他人 [并不完全同意](https://thenewstack.io/why-open-source-ai-has-no-meaning/)。无论如何，Meta 的首席产品官 [Chris Cox](https://www.linkedin.com/in/chris-cox-2896b841/) 将 Llama 3.2 称为“我们迄今为止最以开发者为中心的版本”，并在其 [开发者主题演讲](https://developers.facebook.com/m/meta-connect-developer-sessions/developer-keynote) 中解释了这句话的含义。

“过去——Llama 1、Llama 2、Llama 3 和 3.1——我们一直非常关注模型性能，努力打造最智能的、最先进的模型，并将其开放给消费者和你们，”Cox 说。“对于这个版本，我们一直在努力解决我们从你们所有人那里听到的意见，[即]你们需要什么来改进你们的工具，并将行业提升到下一个水平。”

“Llama Stack 是一组参考 API，用于现代 LLM 系统部署的每个组件。”

– Chris Cox，Meta

尽管 Llama 3.2 的新图像生成功能在活动期间和之后吸引了最多的社交媒体关注，但对于开发者来说，最重要的公告是 Cox 的最后一条。他解释了人们是如何向他抱怨使用 Llama 模型作为开发者太难了。

“你们就像把这些模型扔过墙，每个人都在做同样的事情，每个人都在做批次推理、合成数据，”他说，总结了一些抱怨。“每个人都在蒸馏模型，每个人都在做评估。拜托，让入门变得非常简单，也让这些东西模块化。”

为了回应这些批评，Meta 发布了“Llama Stack”，帮助开发者更轻松地开始使用其 Llama 模型。

“Llama Stack 是一组参考 API，用于现代 LLM 系统部署的每个组件，”Cox 说。“它也是一堆 PyTorch 和其他开发环境的库，可以帮助你立即开始。”

## 细枝末节

该堆栈包含一系列“构建块”，开发者可以使用这些构建块来构建 LLM 应用程序，从实际意义上讲，这意味着以下 API 集：

- 推理
- 安全
- 内存
- 代理系统
- 评估
- 训练后
- 合成数据生成
- 奖励评分

Meta 在 [相关的 GitHub 存储库](https://github.com/meta-llama/llama-stack) 中指出，每个 API 都是一组 REST 端点。API 提供者实际上可以是任何人——“云提供商或专门的推理提供商可以提供这些 API。”

为了让开发者更容易使用，Meta 组织了一系列“发行版”，它表示这是“API 和提供商组合在一起，为最终应用程序开发者提供一致的整体”。目前，Docker 上有三个发行版可用：本地 GPU、本地 CPU 和本地 TGI + Chroma。

正如 [Ahmad Al-Dahle](https://www.linkedin.com/in/ahmad-al-dahle-63a963a0/)，Meta 生成式 AI 的负责人，[在 X 上所说](https://x.com/Ahmad_Al_Dahle/status/1839384436703666309)，“我们的 Llama Stack 发行版是我们在如何通过单个端点支持开发者的道路上迈出的巨大一步。我们现在与社区分享简化且一致的体验，这将使他们能够在多种环境中使用 Llama 模型，包括本地、云、单节点和设备上。”

在 LinkedIn 上，[Prashant Ratanchandani](https://www.linkedin.com/in/prashantratanchandani/)，Meta 生成式 AI 的工程副总裁，[分享了他的想法](https://www.linkedin.com/posts/prashantratanchandani_in-pursuit-of-our-goal-of-open-innovation-activity-7245551523517104128-SqmE?utm_source=share&utm_medium=member_desktop)。“Llama Stack 是我们试图定义和标准化所有构建块，以将 AI 应用程序带给用户的尝试。如今，要做到这一点，开发者需要考虑并选择多个构建块，而 LlamaStack 将这些构建块整合到一个简洁的包中——涵盖模型训练和微调、评估，以及最终构建和部署应用程序。”
同样有趣的是，看看 Meta 的企业合作伙伴如何实施 Llama Stack。例如，戴尔显然优先考虑代理应用程序 [在其产品中](https://www.dell.com/en-us/blog/redefining-ai-integration-in-the-llama-ecosystem-with-dell-ai-solutions/)。“通过将 Llama Stack 与戴尔的 AI 工厂相结合，组织可以获得企业级基础设施，使他们能够轻松地使用 Llama 模型原型化和构建基于代理的 AI 应用程序，”该公司声称。

## 代理系统 API
在当前可用的 API 中，“代理系统” API 显然是关键，因为 [AI 代理的热潮](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) 在 AI 开发者社区中。它恰好位于堆栈的顶部——对于 Meta 和戴尔来说——因此它很可能成为 AI 工程师想要定期使用的 API。

当 Llama Stack 最初在 7 月份作为 RFC 提出时，[早期评论员](https://www.youtube.com/watch?v=A0UCOek8Yc0) 建议这是 Meta 的“代理框架”。Meta 本身使用“代理应用程序”一词来表示它设想使用 Llama Stack 构建的应用程序类型。

在 Llama Stack 正式发布之前，Meta [在 GitHub 上发布了一个仓库](https://github.com/meta-llama/llama-stack-apps)，“展示了在 Llama Stack 之上构建的应用程序示例”。从 Llama 3.1 开始，它表示，您可以构建能够执行以下操作的代理应用程序：

- 将任务分解并执行多步推理。
- 使用工具执行某些操作：
    - 内置：模型内置了对搜索或代码解释器等工具的了解。
    - 零样本：模型可以学习使用以前从未见过的上下文工具定义来调用工具。
    - 使用 Llama Guard 等模型提供系统级安全保护。
## 结论
现在确定开发人员想要使用 Llama Stack 构建哪些类型的应用程序还为时过早，但这只是 AI 开发工具标准化的另一个例子。使用 Llama Stack 以及 Meta 的 LLM 是使用独立 AI 工具（如 [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) 或 [LlamaIndex](https://thenewstack.io/a-developers-guide-to-getting-started-with-llamaindex/)）并寻找 [Hugging Face 目录](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) 中合适的 LLM 的替代方案。使用 Llama Stack，尤其是在用作分发时，所有这些选择都会为您做出。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)