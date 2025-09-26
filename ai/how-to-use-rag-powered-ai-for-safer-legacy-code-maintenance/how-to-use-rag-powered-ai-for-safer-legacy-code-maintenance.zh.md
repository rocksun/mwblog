现实情况是，生成式AI（GenAI）从未被“引入”企业业务；它是在用户发现它可以将一些繁琐的任务从待办事项列表中移除时悄然渗透进来的。在任何人准备好之前，那些以编写代码为生的企业开发人员也开始使用AI了。

这让企业领导者陷入了两难境地。[氛围编程](https://thenewstack.io/to-vibe-or-not-to-vibe-when-and-where-to-use-vibe-coding/)以生产模糊的最小可行产品（MVP）尚可接受，但在其他地方使用它则存在合理的疑虑。

但当今企业的繁重工作并非全新项目。最大的挑战是维护遗留代码库。许多企业正在探索AI是否能够为开发人员减轻一些负担，同时又不让他们面临常见的AI相关风险。

## **维护遗留代码的挑战**

大型代码库，随着时间的推移精心构建，总是充满了“遗留代码”——由开发人员使用较旧的技术栈和框架编写的旧代码。随着围绕这些遗留系统开发新功能，所有这些代码都必须进行修补、更新和集成，否则企业业务将停滞不前。

所有系统都遵循一个相似的起源故事：一个MVP被一些聪明的开发人员转换为产品。接下来，随着用例的扩展，一系列技术集成被分层加入。然后，公司方法论得以实施。

与此同时，最初的开发人员转向新项目，留下了一个了解如何运行系统的运维团队。随后有人意识到该系统扩展性不佳，或者无法与新系统协同工作，或者不符合近期公司重组、收购或法规的要求。

只有少数人了解代码的一小部分以上。曾经有过一些热情的文档，但大约五年前就停止了。大部分代码在本地看来是合理的，但其上下文却很神秘。集成测试在一段时间前就坏了，但没有人确切记得是什么时候。

每个开发人员最终都会面对遗留代码。关键不在于谁被它困住，而在于我们如何更好地处理它。

## **智能体AI如何帮助现代化遗留系统**

最近，公司一直在探索[智能体AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)来解决这些问题。这些产品通常会查看您的代码库，但从“多样化”来源采样了现代代码示例的一体化[大型语言模型 (LLM)](https://thenewstack.io/introduction-to-llms)可能难以理解旧的企业遗留代码或本地策略。

为解决这个问题，包括[Tabnine](https://www.tabnine.com/?utm_content=inline+mention)在内的公司已将[检索增强生成 (RAG)](https://thenewstack.io/no-mcp-hasnt-killed-rag-in-fact-they%E2%80%99re-complementary)整合到其LLM中，以提高准确性并更仔细地查看项目代码。

Tabnine的RAG驱动的[企业上下文引擎](https://www.tabnine.com/blog/your-ai-doesnt-need-more-training-it-needs-context/)首先分析代码库。当您的代码库发生变化时，引擎可以同时更新其理解。

要了解Tabnine的RAG驱动引擎如何工作，让我们分解一个典型任务：将遗留系统连接到新的数据源。

您可以从询问Tabnine开始：“代码库中我们在哪里连接到数据库？”这不只是一个关于数据库的通用查询；企业上下文引擎必须彻底理解代码库才能正确执行此查询。接下来，您可以询问：“解释这段代码相对于其他代码的作用。”您甚至可以询问[Tabnine文档智能体](https://www.tabnine.com/blog/your-ai-doesnt-need-more-training-it-needs-context/)：“为此函数生成文档”，以帮助为下一个处理遗留代码的团队铺平道路。如果您没有时间进行测试驱动开发（TDD），您还可以通过Tabnine标准聊天框生成[单元测试](https://docs.tabnine.com/main/software-development-with-tabnine/accelerate-unit-testing)。

为了让开发人员更容易上手，他们可以从聊天框中作为内置命令（`/onboarding`）或在开始新对话时启动Tabnine的[入职智能体](https://www.tabnine.com/blog/introducing-tabnines-onboarding-agent-revolutionizing-developer-onboarding/)。触发后，该智能体返回项目关键方面的简洁摘要，使开发人员能够快速掌握其结构和功能。然后它会建议进一步相关的探索路径，而不是像某些智能体命令行工具那样生成一个看起来令人印象深刻但却信息量过大的“信息倾倒”摘要。

## **企业AI中安全、隐私和合规性的优先考量**

安全对企业而言并非次要问题。它们运行在已知基础设施上，因此可以确定组件的地理位置等信息，以确保法律合规。尽管Tabnine作为AI代码助手的插件出现，就像我最近研究过的[其他产品](https://thenewstack.io/author/david-eastman/)一样，但它更侧重于保持代码的私密性、安全性和合规性。Tabnine可以被指示只使用宽松许可的代码，并配备严格的防护措施、规则和持续审查流程，以审查受限制的许可并引导模型生成安全、合规的输出。

企业会谨慎选择供应商，很少使用小型团队，并且必须确保他们使用的每项技术都能在其整个技术栈中正常工作。为支持跨平台需求，Tabnine不强制要求任何特定的LLM甚至IDE。它作为VS Code和IntelliJ的插件工作，正如您所期望的，但也支持Eclipse和许多其他IDE。

由于其企业上下文引擎可以放置在任何地方，如果需要，Tabnine可以位于您的公司网络气隙中：

[![Enterprise Context Engine enables a Tabnine cluster to sit in a private customer environment (on prem or virtual private cloud) if needed](https://cdn.thenewstack.io/media/2025/09/5d314876-image.png)](https://cdn.thenewstack.io/media/2025/09/5d314876-image.png)

来源：Tabnine

它可以设置在企业内部、本地或私有云中。请注意，与Tabnine服务器的回传连接是可选的。否则，Tabnine将位于企业防火墙后，并保持信息机密。

Tabnine不会将用户锁定在单一的专有模型中。它支持顶级的LLM，包括Claude、GPT和开源选项，同时只允许使用宽松许可的代码。这有助于降低您的法律风险并[保护您的代码洞察](https://www.tabnine.com/code-privacy/)。

它连接到Git和其他源代码控制系统，以及本地的Jira和Confluence实例，项目知识通常存储在Confluence中。我很欣赏这一点，因为我仍然认为Atlassian的企业维基工具是团队知识捕获的最佳选择。

Tabnine的可见性工具还包括治理、风险和合规（GRC）能力，这对大多数企业来说是一个重要问题。

[![Tabnine includes GRC capabilities including auditability, setting pricing thresholds, access control to LLMs, MCP governance, and code provenance](https://cdn.thenewstack.io/media/2025/09/553f9f29-image-1.png)](https://cdn.thenewstack.io/media/2025/09/553f9f29-image-1.png)

来源：Tabnine

代码生成溯源GRC工具本身就是一个故事：就像您不希望您的“秘密配方”泄露一样，您也必须防止不可溯源的代码闯入。许多LLM都基于通用开源代码进行训练，这可能会带来问题。Tabnine可以确保在您的企业代码库中不使用非宽松许可的代码，从而避免昂贵的版权诉讼或其他知识产权侵权索赔。

## **企业开发AI工具集**

遗留系统与从头开始构建的项目存在不同的问题。Tabnine不是一个新的LLM或新的IDE，而是一个集成的平台，它利用领先的IDE和LLM进行企业开发。凭借其由企业上下文引擎领导的一系列AI工具，Tabnine帮助开发人员获得处理现代化项目所需的关键专业知识。它通过提供企业开发人员应对遗留代码库所需的AI辅助类型来实现这一点，同时关注防止常见的风险因素。

它的故事与智能体AI的前沿叙事不尽相同，但随着大型公司的技术委员会开始掌握其LLM政策，Tabnine将成为AI颠覆风暴中一个非常受欢迎的港湾。