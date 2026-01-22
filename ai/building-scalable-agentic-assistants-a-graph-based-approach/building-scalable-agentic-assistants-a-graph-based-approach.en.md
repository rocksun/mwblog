About a year back, we got pulled into what looked like a straightforward problem: Build an interface assistant that could answer questions about payments, disputes, transactions, and insights. The reality turned out to be far more complex.

Many teams already had several data sources, internal tools and domain experts working together. What we didn’t have was a way to wire all this together into something that felt coherent, reliable, and scalable. Early experiments with [single-agent chatbots](https://thenewstack.io/dont-build-chatbots-build-agents-with-jobs/) worked for demos, but they collapsed under real organizational complexity.

We needed to stop thinking in terms of [agentic systems](https://thenewstack.io/beyond-scripts-the-shift-from-automation-to-agentic-ai/) and start treating it as a coordinated system of agents, each with a narrow responsibility.

## **3 hard problems we had to solve**

Our first attempts followed a familiar pattern. One large prompt, a growing list of tools, and a lot of conditional logic. As soon as we added more capabilities, everything became brittle.

We ran into three hard problems:

* **Routing:** How do you decide which expert logic should handle a given question?
* **Context:** How do you preserve conversational and organizational context without bloating every request?
* **Scale:** How do you add new capabilities without rewriting the system?

The breakthrough came when we stopped thinking about the assistant as a single brain and started treating it as a coordinated system where each node has a clear purpose.

## **An agentic architecture that scales**

At the heart of our solution is a graph-based orchestration model. Instead of one monolithic flow, we built a system where each node in the conversation is handled by a node with a clear purpose.

![Graph-based architecture](https://cdn.thenewstack.io/media/2026/01/874cde8d-image1-1024x695.jpg)

### **Session and orchestration layer**

Every request starts with a session manager that handles state, history, and continuity. This feeds into a system orchestrator responsible for initializing agents and pushing state through the graph.

The orchestrator doesn’t make business decisions. Its job is to move data, not interpret it. That separation turned out to be critical for maintainability.

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

### **Supervisor and routing**

Each domain in our system (payments, disputes, analytics) gets its own supervisor node. These supervisors don’t process requests directly; they route to specialized worker agents based on the user’s intent.

Think of routing like a well-designed API gateway. The supervisor examines the incoming request, decides which worker is best equipped to handle it and hands off execution.

![](https://cdn.thenewstack.io/media/2026/01/fd4ec6e6-image2-1024x731.jpg)

## **Workers and tools**

Worker agents are where the actual work happens. Each worker has access to a narrow set of tools and focuses on a specific domain. One might handle payment lookups, another processes dispute filings, and a third runs analytics queries.

Because workers are narrowly scoped, they’re easier to test, easier to reason about, and easier to extend. Adding a new capability means adding a new worker node, not refactoring the entire system.

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

## **Why this architecture works**

When we moved to this model, several things improved immediately:

* **Maintainability:** Each component has a single responsibility. If something breaks, we know exactly where to look.
* **Scalability:** New features don’t require rewriting core logic. We add nodes, not complexity.
* **Testability:** We can test each worker independently before integrating it into the larger graph.
* **Context management:** Because state flows through a deliberate graph structure, we avoid the “everything everywhere all at once” problem that plagued our first attempts.

### **Before: Monolithic approach**

![](https://cdn.thenewstack.io/media/2026/01/6b9ad901-screenshot-2026-01-09-at-9.25.45-am-1024x581.png)

### **After: Graph-based approach**

![](https://cdn.thenewstack.io/media/2026/01/fd83aad6-screenshot-2026-01-09-at-9.26.09-am-1024x436.png)

This isn’t about throwing AI at a problem and hoping it works. It’s about building systems that respect the complexity of real organizations while staying maintainable as they grow.

The graph-based approach gives us something we didn’t have before: A way to coordinate multiple specialized agents without creating a tangled mess of conditionals and overloaded prompts.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/01/ec5abcc2-cropped-335ca7a4-abhishek-sant-600x600.jpeg)

Abhishek Sant is a technology leader with 15 years of experience in the software industry, including over six years building and leading high-performing engineering teams across AI/ML, scalable APIs and large-scale distributed systems. At PayPal, he has driven innovation in...

Read more from Abhishek Sant](https://thenewstack.io/author/abhishek-sant/)

[![](https://cdn.thenewstack.io/media/2026/01/990266d3-cropped-b57f50bf-hemant-murarka.jpeg)

Hemant Murarka is the head of merchant experiences engineering at PayPal, where he leads teams building scalable, customer-centric platforms for merchants worldwide. He brings over a decade of experience across data platforms and large-scale systems, with prior leadership roles at...

Read more from Hemant Murarka](https://thenewstack.io/author/hemant-murarka/)