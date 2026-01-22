
<!--
title: 构建可扩展的智能体助手：基于图的编排策略
cover: https://cdn.thenewstack.io/media/2026/01/37e0403e-graph.jpg
summary: 本文介绍了如何通过基于图的编排模型构建可扩展的智能体助手，以解决复杂系统中的路由、上下文管理和可扩展性问题，实现更灵活、可维护的架构。
-->

本文介绍了如何通过基于图的编排模型构建可扩展的智能体助手，以解决复杂系统中的路由、上下文管理和可扩展性问题，实现更灵活、可维护的架构。

> 译自：[Building scalable agentic assistants: A graph-based approach](https://thenewstack.io/building-scalable-agentic-assistants-a-graph-based-approach/)
> 
> 作者：Abhishek Sant, Hemant Murarka

大约一年前，我们接手了一个看似简单的问题：构建一个界面助手，能够回答关于支付、争议、交易和洞察力的问题。然而，现实远比想象的复杂。

许多团队已经拥有多个数据源、内部工具和领域专家协同工作。我们所缺乏的是一种将所有这些整合起来，使其连贯、可靠且可扩展的方法。早期对[单智能体聊天机器人](https://thenewstack.io/dont-build-chatbots-build-agents-with-jobs/)的实验在演示时效果良好，但在面对真实的组织复杂性时却崩溃了。

我们需要停止用[智能体系统](https://thenewstack.io/beyond-scripts-the-shift-from-automation-to-agentic-ai/)来思考，并开始将其视为一个由多个智能体协调运作的系统，每个智能体都肩负着狭窄的职责。

## **我们必须解决的3个难题**

我们最初的尝试遵循了熟悉的模式。一个大的提示、一个不断增长的工具列表和大量的条件逻辑。一旦我们增加更多功能，一切都变得脆弱不堪。

我们遇到了三个难题：

*   **路由：** 如何决定哪种专家逻辑应该处理给定的问题？
*   **上下文：** 如何在不使每个请求膨胀的情况下保留对话和组织上下文？
*   **扩展：** 如何在不重写系统的情况下添加新功能？

当我们停止将助手视为一个单一的大脑，并开始将其视为一个协调系统，其中每个节点都有明确的目的时，突破出现了。

## **可扩展的智能体架构**

我们解决方案的核心是基于图的编排模型。我们没有采用单一的整体流程，而是构建了一个系统，其中对话中的每个节点都由一个具有明确目的的节点处理。

![基于图的架构](https://cdn.thenewstack.io/media/2026/01/874cde8d-image1-1024x695.jpg)

### **会话和编排层**

每个请求都始于一个会话管理器，它处理状态、历史记录和连续性。这会输入到一个系统编排器中，该编排器负责初始化智能体并通过图传递状态。

编排器不做出业务决策。它的工作是移动数据，而不是解释数据。这种分离对于可维护性至关重要。

```
# Orchestrator State Management
state = {
	"user_id": "abc123",
	"conversation_history": last_3_turns,  # Not entire history
	"current_domain": "payments",
	"session_context": {
    	"merchant_id": "merch_789",
    	"date_range": "last_30_days"
	}
}
 
async def orchestrate(query: str, state: dict):
	# Initialize supervisor based on domain
	supervisor = get_supervisor(state["current_domain"])
   
	# Pass minimal context, not everything
	result = await supervisor.route_and_execute(
    	query=query,
    	context=state["session_context"]
	)
   
	# Update state for next turn
	state["conversation_history"].append(result)
	return result
```

### **主管和路由**

我们系统中的每个领域（支付、争议、分析）都有自己的主管节点。这些主管不直接处理请求；它们根据用户的意图将请求路由到专业的worker智能体。

可以将路由想象成一个精心设计的API网关。主管会检查传入的请求，决定哪个worker最适合处理它，并移交执行权。

![](https://cdn.thenewstack.io/media/2026/01/fd4ec6e6-image2-1024x731.jpg)

## **Worker和工具**

Worker智能体是实际工作发生的地方。每个worker都可以访问一组狭窄的工具，并专注于一个特定的领域。一个可能处理支付查询，另一个处理争议备案，第三个运行分析查询。

由于worker的范围很窄，它们更容易测试、更容易理解，也更容易扩展。添加新功能意味着添加新的worker节点，而不是重构整个系统。

```
class PaymentWorker:
	"""Handles payment-related queries only"""
	
    def __init__(self, tools: List[Tool]):
    	self.tools = {
        	"lookup": PaymentLookupTool(),
        	"stats": PaymentStatsTool(),
        	"export": PaymentExportTool()
    	}
	
    async def process(self, query: str, context: Context):
    	# Single responsibility: payment lookups only
    	tool_name = self._select_tool(query)
    	tool = self.tools[tool_name]
    	
        # Execute with merchant-specific context
    	result = await tool.execute(
        	query=query,
        	merchant_id=context.merchant_id,
        	filters=self._extract_filters(query)
    	)
    	
        return self._format_response(result)
	
    def _select_tool(self, query: str) -> str:
    	"""Simple keyword matching for tool selection"""
    	if "export" in query.lower():
        	return "export"
    	elif any(word in query.lower() for word in ["total", "sum", "count"]):
        	return "stats"
    	else:
        	return "lookup"
```

## **为什么这种架构有效**

当我们转向这种模型时，以下几点立即得到了改善：

*   **可维护性：** 每个组件都有单一的职责。如果出现问题，我们确切知道在哪里查找。
*   **可扩展性：** 新功能不需要重写核心逻辑。我们添加的是节点，而不是复杂性。
*   **可测试性：** 在将每个worker集成到更大的图中之前，我们可以独立测试它们。
*   **上下文管理：** 由于状态通过精心设计的图结构流动，我们避免了困扰我们最初尝试的“万物互联”问题。

### **之前：单体方法**

![](https://cdn.thenewstack.io/media/2026/01/6b9ad901-screenshot-2026-01-09-at-9.25.45-am-1024x581.png)

### **之后：基于图的方法**

![](https://cdn.thenewstack.io/media/2026/01/fd83aad6-screenshot-2026-01-09-at-9.26.09-am-1024x436.png)

这不是将人工智能应用于问题并期望它能奏效。这是关于构建尊重真实组织复杂性，同时在增长过程中保持可维护性的系统。

基于图的方法为我们提供了一些以前没有的东西：一种协调多个专业智能体的方法，而不会产生混乱的条件和过载的提示。