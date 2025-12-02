根据网络和基础设施编排供应商[Itential](https://www.itential.com/)的说法，未来基础设施管理将包括使用基于推理的代理来接管其技术栈中更大比例的确定性层。

为此，该公司已开放[FlowAI](https://www.itential.com/resource/white-papers/architecting-hybrid-ai-for-infrastructure-operations/)的客户预览，该产品允许客户构建能够推理、规划和编排的AI代理。据该公司称，结合其模型上下文协议（MCP）服务器使用，以确保严格的验证、可审计性和控制，它可以提供一个统一的模型，从而安全、可预测地大规模采用AI。

它最近在德克萨斯州奥斯汀举行的 AutoCon 4 大会上[发布了 FlowAI](https://www.itential.com/resource/demo/building-and-running-your-first-flowagent-in-the-itential-platform-with-flowai/)。

Itential 首席执行官 Chris Wade 解释说：“当人们处理基础设施时，如果你进行大量基础设施即代码（IaC）类型的讨论，你会知道一个管道是非常确定性的。它规定这 12 件事将以这个确切的顺序发生。”

“我们所说的是，AI 将在顶部提供一个推理层。因此，我们将非确定性推理与确定性推理相结合，我们认为这将是一种‘金发姑娘’式的平衡所有这些事物的情况。……如果我在管道中编写大量确定性逻辑，如果我想以任何微小的方式更改该管道，我必须去修改它、测试它并将其推送到生产环境。

“但是，如果我将该确定性层视为一系列‘食谱’，我给它小的、确定性的流程，然后让 AI 推理整个过程，那么我将拥有一个更加灵活的运营模式，基本上可以处理更多样化的任务。随着我在我们的平台中引入 AI，我可以减少技术债务。

“因此，我们正在考虑将 AI 推理置于架构的非常高的位置，这样它就可以增强人类目前所做的工作。他们正在查看中断或正在配置某些东西，他们想要检查这个，检查那个……我们发现，这些[推理模型](https://thenewstack.io/system-two-ai-the-dawn-of-reasoning-agents-in-business/)非常擅长做这些事情。”

[FlowAgent Builder](https://www.itential.com/resource/white-papers/architecting-hybrid-ai-for-infrastructure-operations/)提供了工具、模型和集成，允许用户定义代理角色、连接[大型语言模型（LLMs）](https://roadmap.sh/guides/introduction-to-llms)进行推理、分配工具访问权限并嵌入用于塑造代理操作方式的护栏。然后，[代理可以](https://www.itential.com/blog/company/ai-networking/itential-flowai-the-new-operating-model-for-infrastructure/)访问平台上的现有自动化和数据模型，从而深入了解客户的网络、云和安全系统。

[FlowMCP](https://www.itential.com/blog/itential-mcp-where-conversational-ai-meets-enterprise-automation/)作为所有代理和基础设施之间的受控接口，强制执行严格的模式、策略、权限和审计规则，而 Itential 平台则实际执行任何操作。

Wade 说：“如果我们要修改基础设施，你可能会遇到命令失败、设备繁忙或类似情况。因此，在确定性层中，你过去必须硬编码所有这些内容。你必须说，‘如果发生这种情况，请重试。如果发生这种情况，请重试。等待 10 秒，等待一分钟。’我们认为，将这些内容放在推理层中将非常有益。”

“所以，我认为，从整个行业的宏观角度来看，我们正在努力找出如何平衡推理层和确定性层，或者[管理基础设施](https://thenewstack.io/how-to-use-ai-to-design-intelligent-adaptable-infrastructure/)。显然，我们强烈认为，我们需要将这些确定性层分解成小组件，然后让 AI 推理从中发挥作用。”

Itential 期望客户构建这些代理并决定它们将暴露给哪些资产。

它们可能是模板、预检查、后检查、更新 Slack 或更新 [ServiceNow](https://thenewstack.io/servicenow-launches-a-control-tower-for-agents/) 的工作流，或者是工单创建代理。

Wade 说：“所以客户对代理的范围和它能做什么有完全的控制权，他们可以确信该代理不会随心所欲地做任何事情。它只会执行 Itential 平台暴露给该代理的功能。因此，如果我说你所能做的只是对基础设施执行读取命令并创建工单，那么这就是该代理所能做的全部。然后，客户将拥有一整套可以独立工作并在其组织内部暴露的代理。”

Futuriom Research 首席分析师 [Scott Raynovich](https://www.linkedin.com/in/scott-raynovich-9a40784/) 评论该产品时说：“随着企业努力理解如何安全地采用代理式编排和自动化，Itential 的 FlowAI 不仅提供了一个带有加速流程工具的开发平台，还提供了自信地采用代理式自动化所需的护栏和治理。”

[在此加入私人预览](https://www.itential.com/flowai/)。