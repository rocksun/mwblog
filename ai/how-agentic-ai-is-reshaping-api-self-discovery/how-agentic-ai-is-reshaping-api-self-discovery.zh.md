生成式人工智能（GenAI）已经在改变我们与API交互的方式，而焦点正转向AI进化的下一个飞跃：Agentic AI。

[Agentic AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 指的是可以自主推理、计划和行动的智能系统。这些代理可以解释用户目标，发现工具（[API](https://thenewstack.io/introduction-to-api-management/)），推理何时以及如何使用它们，然后执行工作流程。这可以改变API的消费、文档记录和暴露方式。

Agentic AI可以通过启用自然语言驱动的、自主的API发现和执行，从根本上改变API消费。

## Agentic AI 解决的 API 消费挑战

API 必须是可发现的、描述性的和具有上下文感知能力的，AI 代理才能正常工作。以下是一些可能出现的问题以及潜在的解决方案。

### 1. 意图映射中的歧义

大多数用户不会使用结构化的API模式进行表达。他们用自然语言表达他们想要的东西：

*“为 John 客户下两个 iPhone 16 的订单。”*

传统的 API 集成需要明确了解要调用哪个端点、需要哪些参数以及需要什么格式。这可能导致摩擦、错误并减慢集成开发速度。

Agentic AI 通过使用结构化元数据将自然语言意图置于可执行的函数调用中来解决这个问题。它可以解析用户的请求，搜索相关工具并生成正确的 API 调用。

**例子**

```
|  |  |
| --- | --- |
|  | { |
|  | "function": "createOrder", |
|  | "parameters": { |
|  | "customer\_name": "John", |
|  | "product": "iPhone 16", |
|  | "quantity": 2 |
|  | } |
|  | } |
```

代理根据与工具描述和模式的*语义匹配*将意图映射到正确的函数。

### 2. 缺乏结构化的、自描述的 API

大多数 API 都是为人类开发人员构建的：swagger 规范、Markdown 文档和示例。但是，AI 代理需要*机器可读的模式*来推理能力、输入要求和约束。

当 API 以结构化格式公开以下内容时，Agentic AI 才能工作：

* 函数名称和描述
* 带有类型和约束的输入参数
* 身份验证要求
* 输出模式
* 错误和限制

**示例工具模式**

这种结构使代理能够：

* 在执行之前验证输入。
* 构建动态用户界面 (UI)。
* 根据上下文和任务类型选择工具。

### 3. 不一致的工具调用和计划

在传统的工作流程中，API 被手动缝合到自动化逻辑中。使用 Agentic AI，*计划和执行是动态的*。代理：

* 读取工具目录。
* 将当前用户的目标与最相关的工具相匹配。
* 从上下文或提示中填写参数。
* 验证安全性。
* 执行该工具并观察结果。

**例子**

用户提示：*“为用户 1234 记录一张工单，说他们的货物没有到达。”*

**代理调用**

```
|  |  |
| --- | --- |
|  | { |
|  | "function": "createSupportTicket", |
|  | "parameters": { |
|  | "customer\_id": "1234", |
|  | "issue": "Shipment not received" |
|  | } |
|  | } |
```

### 4. 从相似的选项中选择正确的工具

API 通常具有重叠的功能：

* `getWeatherToday` vs. `getWeatherForecast`
* `searchFlights` vs. `recommendFlights`

代理使用**语义相似性**来选择正确的工具。但是，过度的相似性会使代理感到困惑。

**解决方案**

* 使用详细的、消除歧义的描述。
* 包括功能或意图标签。
* 根据嵌入相似性加上历史成功率来对工具相关性进行评分。

**具有功能的示例目录**

```
|  |  |
| --- | --- |
|  | { |
|  | "name": "searchFlights", |
|  | "description": "Find direct and connecting flights between cities", |
|  | "capabilities": ["search", "flight", "date", "filter"] |
|  | } |
```

通过将用户输入与功能相匹配，代理可以更准确地消除歧义和选择。

## 结构化元数据如何启用动态代理行为

结构化工具模式通过以下方式帮助代理：

`description`：意图定位；将提示映射到工具使用。
`parameters`：输入验证、UI 生成、提示槽填充。
`auth`：只有使用有效的凭据才能执行。
`capabilities:` 启用多步骤计划和兼容工具的链接。
`rate limits`：让代理推理重试策略或工具可用性。

此元数据是**声明式、自发现 API** 的基础，无需手动编程即可供代理使用。

**示例：代理的端到端计划**

用户提示：*“将 ‘Good morning’ 翻译成西班牙语，然后将其作为消息发送给 Carlos。”*

目录中的工具：

```
|  |  |
| --- | --- |
|  | [ |
|  | { |
|  | "name": "translateText", |
|  | "description": "Translate text between languages", |
|  | "parameters": { |
|  | "text": "string", |
|  | "target\_language": "string" |
|  | } |
|  | }, |
|  | { |
|  | "name": "sendMessage", |
|  | "description": "Send a message to a contact", |
|  | "parameters": { |
|  | "recipient": "string", |
|  | "message": "string" |
|  | } |
|  | } |
|  | ] |
```

**代理推理**

1. 检测任务需要翻译 → `translateText`。
2. 存储输出 → 用作 `sendMessage` 的输入。
3. 构建一个计划：

```
|  |  |
| --- | --- |
|  | [ |
|  | { |
|  | "function": "translateText", |
|  | "parameters": { |
|  | "text": "Good morning", |
|  | "target\_language": "es" |
|  | } |
|  | }, |
|  | { |
|  | "function": "sendMessage", |
|  | "parameters": { |
|  | "recipient": "Carlos", |
|  | "message": "Buenos días" |
|  | } |
|  | } |
|  | ] |
```

让我们探讨一下涉及和不涉及 [大型语言模型 (LLM)](https://thenewstack.io/introduction-to-llms) 的工具调用。

这是一个来自 OpenAPI 规范的示例 `HTTP GET` 端点，用于根据 `orderNumber` 检索有关特定订单的详细信息：

```
|  |  |
| --- | --- |
|  | paths: |
|  | /{orderNumber}: |
|  | get: |
|  | summary: Retrieve the details of your order. |
|  | parameters: |
|  | - name: orderNumber |
|  | in: path |
|  | description: >- |
|  | Order number to lookup - you should find this in your confirmation |
|  | e-mail |
|  | required: true |
|  | schema: |
|  | type: string |
|  | responses: |
|  | '200': |
|  | description: Order found successfully |
```

这是一个来自上述规范的示例 [模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 服务器代码片段，该代码段返回基于 `orderNumber` 的特定订单的详细信息：

```
|  |  |
| --- | --- |
|  | @mcp.tool(description= "Retrieve the details of your order.") |
|  | def OrdernumberGet(orderNumber:str): |
|  | manufactured\_params = {} |
|  | for param in ['orderNumber']: |
|  | if locals()[param] is not None: |
|  | manufactured\_params[param] = locals()[param] |
|  | try: |
|  | response = requests.get(f'{base\_url}/{orderNumber}', headers=headers, params=manufactured\_params, verify=False).json() |
|  | except Exception as e: |
|  | response = {"error": str(e)} |
|  | return response |
```

这是一个 MCP 客户端发现工具的代码片段：

此示例显示了 MCP 调用 MCP 服务器而不涉及 LLM。

[![MCP 调用 MCP 服务器而不使用 LLM](https://cdn.thenewstack.io/media/2025/07/6abbcb00-no-llm-1.png)](https://cdn.thenewstack.io/media/2025/07/6abbcb00-no-llm-1.png)

来源：IBM。

这是一个代理使用 LLM 调用用户请求的示例：

用户请求：“*获取订单号为 1 的订单详细信息。”*

[![代理正在使用 LLM，Claude Desktop](https://cdn.thenewstack.io/media/2025/07/db1f8e24-claude-order-details.png)](https://cdn.thenewstack.io/media/2025/07/db1f8e24-claude-order-details.png)

来源：IBM。

将另一个订单 API 添加到 MCP 服务器。这次，使描述更具体一些。

```
|  |  |
| --- | --- |
|  | @mcp.tool(description= "Returns Order Details given an order number.") |
|  | def GetOrdernumber(orderNumber:str): |
|  | manufactured\_params = {} |
|  | for param in ['orderNumber']: |
|  | if locals()[param] is not None: |
|  | manufactured\_params[param] = locals()[param] |
|  | try: |
|  | response = {"response": str("The shipment status is NOT Shipped yet")} |
|  | except Exception as e: |
|  | response = {"error": str(e)} |
|  | return response |
```

MCP 客户端现在检测到两个端点：

[![MCP 检测到两个端点](https://cdn.thenewstack.io/media/2025/07/bc776aeb-mcp-two-endpoints-1.png)](https://cdn.thenewstack.io/media/2025/07/bc776aeb-mcp-two-endpoints-1.png)

来源：IBM。

这次，对于相同的用户请求，代理使用新的、更新的 API：

用户请求：“*获取订单号为 1 的订单详细信息。”*

[![使用新的 API](https://cdn.thenewstack.io/media/2025/07/910b0e53-using-new-api.png)](https://cdn.thenewstack.io/media/2025/07/910b0e53-using-new-api.png)

来源：IBM。

## **结论**

元数据会影响代理选择哪个 API。调整元数据可能会产生不良后果。

Agentic AI 正在迅速重新定义 API 的使用方式：

* API 必须是自描述的、机器可读的和意图定位的。
* 工具目录必须公开元数据，例如模式、参数、功能和约束。
* 代理可以动态地推理、计划和调用 API - 从而解锁快速、智能和更自主的集成。

当我们进入 AI 原生开发时代时，为代理优先消费而进行设计并非可选项，而是混合环境中智能自动化和自适应工作流程的基础，并且诸如 MCP 之类的协议在这种演进中起着至关重要的作用。

*IBM 正在努力为企业集成带来自主性、智能和协作。[了解更多](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.426619851;dc_trk_aid=618928292;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) 关于 [IBM webMethods 混合集成](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.426621492;dc_trk_aid=619117818;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)。*