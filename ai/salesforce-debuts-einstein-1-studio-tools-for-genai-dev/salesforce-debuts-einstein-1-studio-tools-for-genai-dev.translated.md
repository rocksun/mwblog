# Salesforce 推出 Einstein 1 Studio 工具，用于 GenAI 开发

![Salesforce 推出 Einstein 1 Studio 工具，用于 GenAI 开发的特色图片](https://cdn.thenewstack.io/media/2024/03/a5ddc9b7-austin-distel-mpn7xjkq_ns-unsplash-1-1024x768.jpg)

负责全球 150,000 家公司 [Salesforce](https://salesforce.com) 安装的开发人员现在拥有一套专为 GenAI 类型应用程序设计的新工具。

在 3 月 6 日和 7 日举行的 [TrailblazerDX](https://www.salesforce.com/trailblazerdx/) 开发者大会上，这家总部位于旧金山的公司推出了 [Einstein 1 Studio](https://www.salesforce.com/news/press-releases/2024/03/06/einstein-1-studio-news/)，这是一套 [低代码](https://thenewstack.io/confessions-of-a-low-code-convert/) 工具，使管理员和开发人员能够自定义 Einstein Copilot（一种用于 CRM 的会话式 AI 助手），并在需要时将 [AI 机器人](https://thenewstack.io/developers-put-ai-bots-to-the-test-of-writing-code/) 嵌入到任何应用程序中。

## 用户友好型工具

Salesforce 产品管理高级副总裁 [John Kucera](https://www.linkedin.com/in/johnkucera/) 在新闻发布会上告诉分析师，新软件包旨在使 AI 开发对用户友好，同时不损害数据安全性。现在可用的工具有：

- **Copilot Builder**，用于在 Einstein Copilot 中创建 AI 操作，以处理各种工作流的任务。管理员和开发人员可以使用他们已有的工具，例如 Apex、Flow 和 [MuleSoft API](https://thenewstack.io/mulesoft-concession-openapi-adopts-raml-different-approach-api-documentation-descriptions/)，以及 [GenAI](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/) 组件（例如提示），以使 Copilot 能够完成任务。Copilot 可以使用这些自定义操作来完成 Salesforce 应用程序或外部系统中的任务。
- **提示生成器**。这使管理员和开发人员能够创建自定义的可重复使用 [AI 提示](https://thenewstack.io/developer-tips-in-ai-prompt-engineering/)，而无需编码。它不仅将 GenAI 的使用范围扩展到会话界面之外，还允许用户设计和重新利用提示，以便在其他会话中使用。例如，可以将自定义提示嵌入到联系人记录中作为按钮，使联络中心的座席能够一键获取客户的所有升级案例的快照。
- **模型生成器**，用于从 Salesforce 或其合作伙伴中选择最合适的语言模型 (LLM)，或根据用例构建定制的预测性 AI 模型。
- **Trailhead AI 课程**，在公司的 [免费在线学习平台](https://trailhead.salesforce.com/) 上使用 Einstein Copilot 和提示生成器的说明。

Kucera 说：“与将企业限制在单个 LLM 的其他解决方案不同，Einstein 1 Studio 提供了连接到各种 AI 模型的灵活性。对于公司来说，这是一种无代码、低代码和专业代码的方式，可以构建自己的预测性 AI 模型，并根据其（Salesforce）数据云数据进行训练。”

企业可以使用 Salesforce 合作伙伴提供的预测性和生成性 AI 模型和服务，其中包括通过 [Amazon Bedrock](https://thenewstack.io/10-key-products-for-building-llm-based-apps-on-aws/) 和 Amazon SageMaker、Anthropic、Azure OpenAI、Cohere、Databricks、Google Cloud 的 Vertex AI 和 OpenAI 的 AWS，并在不移动或复制数据的情况下，根据数据云数据训练或微调选定模型。

在 [Salesforce 最近进行的一项调查](https://www.salesforce.com/news/stories/ai-it-demand-gap/) 中，90% 的 IT 专业人士声称 GenAI 迫使他们重新评估其技术策略。这种思维方式的变化影响了新应用程序和服务在其组织内被采用和使用的方式。管理员表示，他们需要更直观的用户界面，以便在工作流程中轻松与 AI 交互；更多适合其用例的 AI 模型；以及更好地访问可信的客户和业务数据，以奠定 AI 模型的基础并确保准确且相关的结果。

## 数据孤岛

Salesforce AI 首席执行官 [Clara Shih](https://www.linkedin.com/in/clarashih/) 告诉分析师：“很明显，公司拥有大量企业数据，但这些数据仍然存在于孤岛中。” “我所说的孤岛是指跨越 AWS 和 [Google Cloud](https://thenewstack.io/google-cloud-services-hit-by-outage-in-paris/) 等数据库和应用程序的数据。事实上，普通公司必须处理数千个这样的数据孤岛。不仅如此，这些不同孤岛中的数据格式也不同。其中一些以数据库和 CRM 的形式进行结构化。其中一些是无结构的，例如电子邮件、PDF 和对话记录。这些不是 AI 模型准确执行并避免出现幻觉所需的统一数据集。”
**Shih 表示，Einstein 1 Studio 直接与 Salesforce Data Cloud 集成，后者可查找并统一受困数据和 AI 模型，并利用客户数据和元数据进行智能化处理。她表示，Studio 工具箱将用户界面、各种 AI 模型和数据连接到一个单一的元数据驱动平台中。这促进了 Einstein Copilot（不要与 Microsoft 的同名 AI 工具混淆）的低代码和无代码定制，以及构建和修改连接到工作流程中 AI 模型的嵌入式提示和操作。**

**Einstein 1 Studio 还包括该公司的安全功能，[Einstein 信任层](https://www.salesforce.com/products/secure-ai/)。新增功能是客户配置的数据屏蔽，使管理员能够选择他们想要屏蔽的字段，从而提供更大的控制权。此外，从 AI 提示和响应中收集的审计跟踪和反馈数据现在存储在 Data Cloud 中，可以在其中通过 Flow 和其他 Einstein 1 Platform 工具进行报告或用于自动警报。**

**提示生成器和模型生成器现在已在全球范围内推出。Copilot Builder 已在全球范围内推出测试版。**

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

**技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等内容。**