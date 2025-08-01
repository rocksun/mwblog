
<!--
title: 谷歌云扩大A2A协议覆盖范围
cover: https://cdn.thenewstack.io/media/2025/07/a53cdd88-img_20180723_221514-2-scaled.jpg
summary: 谷歌正增强 A2A 协议，包括在 ADK、Agentspace 和 Agent Engine 中添加原生支持，简化部署至 Cloud Run 或 GKE 的流程。规范更新至 0.3 版，支持 gRPC 框架和增强安全性。谷歌还计划推出 AI 智能体市场，并利用 Vertex GenAI 评估服务测试 A2A 智能体。A2A 旨在实现智能体间的自然语言通信，区别于 MCP 的结构化数据处理。
-->

谷歌正增强 A2A 协议，包括在 ADK、Agentspace 和 Agent Engine 中添加原生支持，简化部署至 Cloud Run 或 GKE 的流程。规范更新至 0.3 版，支持 gRPC 框架和增强安全性。谷歌还计划推出 AI 智能体市场，并利用 Vertex GenAI 评估服务测试 A2A 智能体。A2A 旨在实现智能体间的自然语言通信，区别于 MCP 的结构化数据处理。

> 译自：[Google Brings the A2A Protocol to More of Its Cloud](https://thenewstack.io/google-brings-the-a2a-protocol-to-more-of-its-cloud/)
> 
> 作者：Frederic Lardinois

今年四月初，谷歌发布了其 [Agent2Agent (A2A) 协议](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/)，旨在帮助 AI 智能体相互通信。此后，谷歌[将该协议捐赠给了](https://github.com/a2aproject/A2A?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) Linux 基金会，目前该项目已获得 150 多家公司的支持，包括 [Amazon](https://aws.amazon.com/?utm_content=inline+mention)、Microsoft、[Salesforce](https://www.salesforce.com/?utm_content=inline+mention) 和 [ServiceNow](https://www.servicenow.com/products/observability.html?utm_content=inline+mention)。

今天，谷歌正在 A2A 之路上迈出下一步，为其许多以智能体为中心以及相关的开发者工具和服务添加支持。这包括在其智能体开发工具包 (ADK) 和 Agentspace（其面向企业的无代码智能体构建器）中添加原生 A2A 支持。

谷歌还在增加新的部署选项，从而更容易将 A2A 智能体部署到 Cloud Run 或 Google Kubernetes Engine (GKE)。谷歌还在其 [Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/reasoning-engine)（该公司用于智能体的托管运行时）中添加了对 A2A 智能体的支持。

[![一张图表说明了 AI 智能体协作和 A2A 协议的原则，展示了客户端智能体和远程智能体之间的交互。该过程由四个支柱支持：安全协作、任务和状态管理、用户体验协商和能力发现。](https://cdn.thenewstack.io/media/2025/07/dad234e3-image5_vkag0kd.original.png)](https://cdn.thenewstack.io/media/2025/07/dad234e3-image5_vkag0kd.original.png)

*A2A 协议的工作原理。图片来源：Google。*

## A2A 规范更新

除了这些产品更新之外，该团队还发布了最新版本的 A2A 规范，目前版本号为 0.3。

Google Cloud 的 A2A 和业务平台副总裁 [Rao Surapaneni](https://www.linkedin.com/in/raosurapaneni/) 告诉我：“我们所做的事情之一是，我们希望在发布时就做好企业就绪的准备。安全性、身份验证、监控——我们已将所有这些都融入到规范中。当人们开始使用我们的 A2A SDK 时，我们收到了反馈，说我们需要在此处进行一些小的调整。我们需要额外的功能才能将其应用于高性能场景。”

对于这些客户，该规范现在包括对用于连接服务的高性能 [gRPC 框架](https://grpc.io/) 的支持。Surapaneni 指出，Google 的一位客户正在移动场景中，使用非常庞大的 AI 智能体群对 A2A 和 gRPC 框架进行试验。

在安全性方面，该规范现在包括有关处理未经身份验证和经过身份验证的智能体，以及具有提升和委派权限的智能体的更新。

## 部署 A2A

Surapaneni 表示，目前，Google 的许多客户正迅速从试验智能体和 A2A 转变为生产。这意味着他们正在寻找更轻松的方式来部署这些智能体，以及用于在生产中监控它们的其他工具。

“当客户开始部署到生产环境时，他们正在寻找选择。因此，我们将其纳入了我们的智能体开发工具包 ADK 中。我们使其变得非常容易——就像几行代码，甚至是一行带有默认值的代码——就可以将智能体转换为 A2A 智能体。然后，一旦你构建了它，你就会想将其部署到某个地方。”

他指出，客户希望有选择权，因此他们可以在托管智能体引擎之间进行选择，或者部署到由 Cloud Run（Google Cloud 的完全托管的无服务器平台）管理的容器中，或者部署到 GKE 服务中，以供想要完全控制其部署的用户使用。

Google 还在采用另一种部署方法，即将 A2A 智能体引入 Agentspace。不久之后，企业将能够将其智能体发布到 AgentSpace 中，以便企业可以使用该服务来访问和管理其自研智能体以及第三方智能体。

此外，Google 还在推出 [AI 智能体市场](https://console.cloud.google.com/marketplace/browse?filter=category:ai-agent)，Google Cloud 客户将能够在此处发现并购买来自 ISV、GSI 等的智能体。当然，这些智能体必须在 Google Cloud Platform 上运行，并且 Google 将审查各个智能体。

Surapaneni 表示：“我们为企业用户提供在一个界面中访问正确的内容、正确的操作和相关的智能体的能力的方式受到了极大的欢迎。”

部署完成后，Google 的 Vertex GenAI 评估服务（该服务会定期根据开发者设置的一组评估标准对应用程序进行基准测试）现在还可以测试这些 A2A 智能体，这要归功于其新添加的对该协议的支持。

## A2A 和 MCP

不过，我在对话中一直听到的一件事是，关于 A2A 和 Anthropic 的模型上下文协议 (MCP) 之间的关系仍然存在一些困惑。鉴于 Surapaneni 在创建 A2A 协议中发挥了重要作用。我问了他关于它是如何产生的，以及他对这两个协议的看法。

他解释说：“我们的洞察是，当客户和所有这些技术供应商构建自己的智能体时，你突然进入了我所说的他们提供的世界智能。但如果你从客户的角度来看，我正在部署 Salesforce、ServiceNow、Google 以及其他一些东西。如果这些智能体不能相互通信，他们只能做他们所做的事情，我无法轻松地利用它们。这就是让我思考如何让这些智能体相互通信的关键洞察？”

他还指出，MCP 和 A2A 之间的主要区别之一是，当你进行 MCP 调用时，你本质上仍然在使用代码进行 API 调用。

他说：“你错过了这些智能体拥有的自然语言能力和自主智能。因此，我想将其融入到协议中。就像人类正在与智能体打字和聊天一样，另一个智能体可以进行这种模棱两可的对话并朝着目标前进。我不想丢失正在发生的语义交换，我想将其带给智能体。”

他说，MCP 非常适合结构化数据和调用工具，“但当你想要进行人与人之间，或者在这种情况下，智能体与智能体之间的通信时，它会更加微妙、模棱两可。需要来回填补空白，对吗？所有这些都融入到了 A2A 协议中。”