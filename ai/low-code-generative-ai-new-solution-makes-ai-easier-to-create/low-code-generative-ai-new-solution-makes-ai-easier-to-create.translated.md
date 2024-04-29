# 低代码生成式 AI：新解决方案让 AI 更易于创建

![低代码生成式 AI 的特色图片：新解决方案让 AI 更易于创建](https://cdn.thenewstack.io/media/2024/04/b7eccb84-mariia-shalabaieva-jryya3w2uxk-unsplash-1024x576.jpg)

并非所有生成式 AI 都是聊天机器人，也不需要是聊天机器人。

低代码开发平台 OutSystems 的 AI 产品经理 [Rodrigo Coutinho](https://www.linkedin.com/in/sousacoutinho/) 表示，生成式 AI 的作用远不止于此。

该公司最近推出了一项名为 [AI Agent Builder](https://www.outsystems.com/ai/) 的新产品，简化了组织使用 AI 代理的开发。他解释说，这些代理是一组模型连接、配置和提示。

Coutinho 告诉 The New Stack：“AI 代理背后的想法是让使用低代码的人能够访问生成式 AI 技术，因此你可以将其视为一种配置，你可以在其中建立要使用的模型。”“很酷的一点是，这不仅允许你在 [低代码环境](https://thenewstack.io/what-a-low-code-platform-offers-frontend-developers/) 中使用代理，因此无需考虑所有这些事情，你只需拥有一个执行所有这些功能的可视化元素，而且它还允许我们为人们提供一个试用代理的游乐场。”

这些代理仍然需要一些 [提示工程](https://thenewstack.io/developer-tips-in-ai-prompt-engineering/)，但他表示，开箱即用的界面允许开发人员和其他人员试用代理、对其进行调整并将其据为己有。

## 开箱即用的三个代理

OutSystems 提供三个 AI 代理：一个可以处理呼叫摘要，一个处理工单转移，还有一个私人聊天代理。

呼叫摘要简单地总结了冗长的呼叫，以便（例如）销售人员可以将完整的摘要上传到他们的销售应用程序或其他笔记中。工单转移意味着，如果有人提出通常需要支持工单的问题，代理可以根据提供给它的文档提供答案。它还可以连接到 Zendesk 等内容，以继续提交工单。他还补充说，用户界面元素也随 AI 代理一起开箱即用。

私人聊天允许组织采用类似 [ChatGPT](https://thenewstack.io/improving-chatgpts-ability-to-understand-ambiguous-prompts/) 的功能，而无需担心潜在的数据使用问题和其他生成式 AI 聊天机器人引发的合规相关问题。所有 AI 代理都旨在保证隐私并限制与公共 GPT 相关的其他组织风险。

他说：“整个架构都是考虑在我们的系统中使用它而设计的，我们的意思是，我们提供了一个公开代理的本地元素，而且很容易调用。”“如果你想从第三方应用程序使用代理或进行集成，那么它相当简单，因为你可以创建一个 OutSystem 应用程序，你只需将其公开为 REST API 即可。”

## 简化 AI 开发

Coutinho 表示，虽然开发人员倾向于将 [低代码与公民开发人员](https://thenewstack.io/pro-coders-key-to-stopping-citizen-developer-security-breach/) 联系起来，但 AI 代理也简化了程序员的开发工作。

他说：“对于任何人来说，只需进行一些配置，就可以创建一个真正有用的代理，而且会对业务产生影响，这非常容易。”“此外，在配置之后，你拥有了一个游乐场，因此你可以调整和迭代你所做的代理，直到你对结果满意为止。”

他补充说，这些代理可以在任何应用程序中使用和重复使用。

他说：“你可以使用相同的代理拥有多个界面。”“我们可以拥有更接近聊天机器人或更接近论坛的界面，所有这些都是一个可视化元素。然后在整个组织中重复使用它非常容易。”

目前，开发人员可以选择 [Azure OpenAI](https://thenewstack.io/generative-ai-cloud-services-aws-azure-or-google-cloud/) 或 [AWS](https://aws.amazon.com/?utm_content=inline+mention) [Bedrock](https://thenewstack.io/aws-goes-deep-on-ai-chip-power-and-cost-savings/) 基础模型，然后将它们与组织知识源集成，并输入自然语言指令以在应用程序中使用。OutSystems 还内置了防护措施来控制访问和性能监控，包括安全支持。

他说：“我们希望确保用户模型确保数据访问的隐私和安全性，因此通过向开发人员提供代理，而不是直接访问这些模型，你可以确保他们使用正确的模型。”
[数据](https://thenewstack.io/integrating-real-time-and-historical-data-enhances-decision-making/)，他补充道。当开发人员配置代理时，该平台确保 [数据不包含敏感](https://thenewstack.io/qa-how-verticalchange-secures-sensitive-data-using-open-source-tools/) 数据，而组织不希望这些数据被公开，他说道。它还监控令牌使用情况等内容，以便用户了解每个模型的成本以及每个模型提供的信息量，他补充道。

“代理还关联有数据，因此非常容易控制数据类型以及希望向代理提供什么数据以向客户提供响应，”他说道。“即使它不会进入模型，您也希望小心提供给客户的数据。您不希望私有 [数据泄露](https://thenewstack.io/why-unsuspecting-data-leaks-are-a-key-to-rampant-blockchain-hacks/)。”

它还可以通过简化连接到另一个模型并让其检查模型的答案是否存在可能的幻觉来简化 [打击幻觉](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/)。

“在低代码中提供这些代理的 [好处](https://thenewstack.io/adopting-low-code-for-developers-5-things-to-consider/) 是，编排这些事情非常容易，”Coutinho 说道。

例如，OutSystems 设置了其论坛从英语到日语的翻译。他表示，首先需要确保英语正确，因为该公司有很多非母语人士，“他们使用英语非常有创造力，包括我自己，”Coutinho 说道。

“因此，您需要做的第一件事是要求 AI 获取此英语句子并使其变得通顺，然后将其翻译成日语，”他解释道。“使用低代码，这非常容易使用，因为您只需几个可视元素，即可连接所有内容，并且可以通过可视方式了解正在发生的事情。检查幻觉也适用相同的方法。您可以调用模型，然后让另一个代理验证它是否符合您期望的标准。”

## 创意 AI 用例

OutSystems 计划在未来添加其他 LLM 模型，包括处理图像和视频的模型。

“我们还希望通过更多示例进行扩展，既在代理端帮助人们创造更好的产品，也在示例网站上提供灵感，”他说道。“我们知道有很多企业知道 GenAI 可以帮助他们提高生产力和效率，但他们需要一些灵感来确切了解有哪些可能性。我们将继续发展 AI 代理构建器来提供这些示例。”

Coutinho 说道，除了可预测的用例之外，客户还使用代理来帮助员工提高生产力，减少填写时间表的时间。员工描述他们在这一周所做的工作，而 AI 允许他们快速填写时间表。

客户还使用私有聊天功能从基于文本的输入中提取信息，例如姓名或电子邮件信息。然后，他表示，该信息可用于创建结构化数据集。

他补充说，一家公司正在使用代理从他们从职位发布中收到的所有求职信、简历和履历中提取信息。

“我非常好奇人们会用它做什么，”他说道。“我们的客户很有想象力。我非常期待看到由此产生的原创想法。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)