# 开发者测试更多，JetBrains 研究发现

![开发者测试更多，JetBrains 研究发现的特色图片](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)

根据最近的[JetBrains 开发者生态系统现状报告](https://www.jetbrains.com/lp/devecosystem-2024/)，开发者正在进行更多测试。

进行测试的[开发者](https://roadmap.sh/roadmaps)比例从去年的 85% 上升到 2024 年的 95%。进行单元测试、集成测试和端到端测试的开发者比例也上升了。

然而，只有 18% 的人在使用的测试软件中使用人工智能。

该调查还考察了人工智能是否为人们提供了更多编码时间。用户普遍认为，节省时间和提高效率是使用人工智能开发工具的首要好处。

65% 的人表示他们超过一半的工作时间用于编码，高于 2023 年的 57%。使用这些工具的一半人每周至少节省 2 个小时。相比之下，4% 的人表示由于使用这些工具，他们每周没有节省任何时间，另有 46% 的人每周节省的时间不超过 2 个小时。

值得注意的是，只有 23% 的人表示使用人工智能编码工具实际上[提高了所创建代码和解决方案的质量](https://thenewstack.io/a-call-to-use-generative-ai-to-create-more-trustworthy-data/)。

GitHub Copilot 的先前估计似乎也被夸大了。

在 2024 年，JetBrains 特别询问人们是否将特定的人工智能工具用于编码和其他开发活动。当以这种方式提问（而不是询问任何用途的使用情况）时，GitHub Copilot 的使用率从 46% 下降到 26%，ChatGPT 的使用率从 70% 下降到 49%。

**以上部分由 Lawrence Hecht，TNS 分析师撰写。**

## Weaviate 为 AI 应用提供托管嵌入式服务

向量数据库公司 Weaviate 本月推出了一个新的用于 AI 应用的托管嵌入式服务。该服务名为[Weaviate Embeddings](https://www.globenewswire.com/news-release/2024/12/03/2990699/0/en/Weaviate-Launches-Flexible-Embedding-Service-for-AI-Development.html)，支持开源和专有嵌入模型。它使开发者能够完全控制其嵌入，允许他们在模型之间切换。此外，它在生产环境中没有每秒嵌入数的速率限制。

该服务托管在 Weaviate Cloud 中，并在 GPU 上运行。

## Tabnine 功能标记 AI 生成的软件中的未授权代码

[Tabnine，最初的 AI 代码助手创建者，推出了一项名为](https://www.tabnine.com/?utm_content=inline+mention)[代码来源和归属的功能，该功能检查 AI 生成的代码](https://www.tabnine.com/blog/introducing-provenance-and-attribution-minimize-ip-liability-for-genai-output/)，以查看代码是否存在潜在的知识产权或版权问题。

它会针对公开可见的 GitHub 代码检查代码，并标记任何匹配项。代码检查器会引用源代码库以及许可证类型，这使得开发者可以轻松确定是否可以根据组织的特定标准和要求使用该代码。

Tabnine 预计很快将添加一项功能，允许用户识别特定的代码库（例如竞争对手维护的代码库），然后让 Tabnine 也针对这些代码库检查生成的代码。它还计划添加审查功能，允许 Tabnine 管理员在将匹配的代码显示给开发者之前将其删除。

目前，代码来源和归属功能处于私人预览阶段，任何 Tabnine 企业客户都可以使用。它适用于所有可用的模型。

## Google 发布 Gemini 2.0 Flash 和 Javascript/Python 代码助手

[Google 已更新其 Gemini Flash 模型。](https://cloud.google.com/?utm_content=inline+mention)[Gemini Flash 2.0 的速度是 1.5 Pro 的两倍](https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/)，该公司表示。根据博文，它还推出了用于[构建具有实时音频和视频流的动态应用程序的多模式实时 API](https://thenewstack.io/how-to-build-applications-over-streaming-data-the-right-way/)。
开发者可以使用 Gemini 2.0 Flash 通过 API 调用生成包含文本、音频和图像的响应。[Gemini 2.0 Flash 可以使用 Google](https://thenewstack.io/langchain-and-google-gemini-api-for-ai-apps-a-quickstart-guide/) AI Studio 和 Vertex AI 中的 Gemini API 访问。目前它处于实验阶段，但预计明年将正式发布。

Gemini 2.0 经过训练可以使用工具，Google 指出这是构建[AI 代理](https://thenewstack.io/enhancing-ai-agents-adding-instructions-tasks-and-memory/)“体验”的基础能力。除了通过函数调用自定义第三方函数外，它还可以原生调用 Google 搜索和代码执行等工具。
文章补充道，原生使用谷歌搜索作为工具，能够带来更准确和全面的答案，并增加发布商的流量。

文章指出：“可以并行运行多个搜索，通过同时从多个来源查找更多相关事实并将它们结合起来以提高准确性，从而改进信息检索。”

谷歌还推出了一款名为Jules的实验性AI代码代理，它可以处理Python和Javascript编码任务。

文章指出：“Jules与您的GitHub工作流程异步集成，在您专注于实际构建内容的同时，处理错误修复和其他耗时任务。”“Jules创建全面的多步骤计划来解决问题，高效地修改多个文件，甚至准备pull requests，以便将修复直接提交回GitHub。”

目前，Jules仅供“特定选择的受信测试人员”使用，但计划在2025年初将其提供给其他开发者。

最后，还有一个[开发者可以加入的受信测试人员计划](https://forms.gle/UQWKGrhFqVRLmJGy5)，以试用Colab数据科学代理。它允许开发者用简单的语言描述他们的分析目标，然后它会构建一个Colab笔记本。预计它将在2025年上半年更广泛地可用。

[YOUTUBE.COM/THENEWSTACK 科技发展日新月异，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)