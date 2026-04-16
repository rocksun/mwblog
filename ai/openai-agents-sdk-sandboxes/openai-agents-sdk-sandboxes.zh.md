OpenAI 周三[宣布](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)对其 [Agents SDK](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/) 进行了重大更新，将这个与模型无关的 SDK 从一个相对简陋、无特定倾向的代理构建方式，转变为一个用于将代理投入生产的成熟工具箱。

当原始 SDK 在一年多以前发布时，OpenAI 押注模型在处理轨迹、规划以及在合理时间内保持专注任务方面的能力会不断提高。

正如 OpenAI 的 [Steve Coffey](https://www.linkedin.com/in/stevendcoffey/)（该公司 Responses API 的技术负责人）告诉 *The New Stack* 的那样，原始 SDK 基本上是为聊天机器人用例构建的。

> “现在的模型可以连续工作数小时、数天甚至数周。”

他说：“当时的模型，你可以期望它们在工作流程中采取五、六、七个步骤，但不会再多了。而现在的模型可以连续工作数小时、数天甚至数周。”

在过去的一年里，OpenAI 为 SDK 增加了许多功能，包括对 MCP、Temporal 的持久执行工具以及其他第三方工具和服务的支持。但正如 Coffey 所指出的，它仍然是一个 1.0 版本之前的项目——今天依然如此（“我们计划进一步改进它，”Coffey 说）。

## 为代理提供沙箱

这次发布的亮点功能是，开发者现在可以为他们的代理提供受控的工作空间进行操作。其核心理念是将代理控制框架（harness）与计算（compute）分离，以确保安全性和持久性，同时还使这些系统能够在需要时进行扩展。

> 这次发布的亮点功能是，开发者现在可以为他们的代理提供受控的工作空间进行操作。

这些沙箱几乎可以是任何类型的容器或虚拟机。开发者可以使用自己的容器基础设施，或使用来自 Blaxel、Cloudflare、Daytona、E2B、Modal、Runloop 和 Vercel 的工具来为其代理创建沙箱。代理可以使用单个沙箱，也可以在需要时启动额外的沙箱——或者启动在自己的沙箱环境中运行的子代理。

正因如此，SDK 可以作为 Temporal 作业运行，Coffey 解释说，代理随后将在 Model 沙箱或 Docker 容器中运行。“这样一来，这些东西就彼此非常独立了。工具调用运行在非特权环境中，而 Modal 编写的所有代码都运行在特权环境中，”他指出。

## 分离控制框架与计算

正如 Coffey 所言，团队希望确保企业能够使用现有的基础设施来运行这些工作空间。

这里也有安全方面的考虑，特别是对于大型企业。正如 Coffey 所说，从事一次性任务的个人开发者可能不会太担心安全问题，但“在光谱的另一端是这些大型企业部署，你会非常在意代理在一个完全去中心化审批的环境中运行。

“所以那个沙箱里没有 API 密钥，没有秘密。你希望它是完全隔离的——在很多情况下可能与网络隔离，并且无法进行任何形式的向外连接。”

![](https://cdn.thenewstack.io/media/2026/04/48a70f8a-codex-harness-compute-1024x563.png)

*图片来源：OpenAI。*

在这个沙箱内部，沙箱代理（现在比其前身更具规范性）可以使用 shell 和文件系统来处理文本文件、图像或 PDF 等。当然，开发者也可以定义代理可以使用的其他工具。

这些代理也需要访问数据。开发者可以挂载本地文件、AWS S3 存储桶、Google Cloud Storage、Azure Blob Storage 和 Cloudflare R2。这还允许沙箱在某种程度上具有状态性。

“如果你希望能够对容器进行快照并关闭该容器，稍后使用相同的文件系统重新启动它，我们正在增加对此的支持，”Coffey 说。

即使不使用沙箱，基于 Agent SDK 构建的代理现在也具有可配置的内存，并支持文件和文档，尽管 OpenAI 似乎期望大多数生产系统使用沙箱环境。

与以前一样，Agents SDK 没有额外收费。用户根据 OpenAI 的[标准定价](https://openai.com/api/pricing/)，为通过 API 消耗的 Token 和工具使用付费。