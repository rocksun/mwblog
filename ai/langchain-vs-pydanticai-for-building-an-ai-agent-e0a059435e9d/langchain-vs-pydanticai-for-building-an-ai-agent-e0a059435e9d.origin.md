LangChain is a well known agential AI framework, and PydanticAI is newer on the scene but quickly gaining popularity. Here I compare how they can be used to build a simple conversational AI Agent, involving the following features:

- Dynamic model choice
- Human-in-the-loop input
- Tool calling with dependencies
- Conversation history/memory
- Dynamic system prompt
- Structured output
# Agent Behaviour
The aim is to build an AI agent that will play the role of an eccentric waiter at a restaurant who will ask about your dietary requirements and take your order. An example conversation might look like:

AI Waiter:Ah, bonjour madame et monsieur! Welcome to Le Bistro, where the food is as delightful as the company! Before we embark on a culinary adventure, might you have any dietary restrictions or preferences? We wouldn’t want any rogue ingredients crashing the party!
You:I only eat yellow coloured food<agent makes tool call to get list of menu items>

AI Waiter:Magnifique! A connoisseur of the golden hue, I see! Let’s explore the menu with your sunshine-filled preference in mind. For appetizers, we have the Quinoa Stuffed Bell Peppers, which are a vibrant yellow. For the main course, the Chickpea and Sweet Potato Curry is a golden delight! And for dessert, the Fresh Fruit Sorbet might have some yellow options depending on the day! What do you think?
You:I’ll take the Bell Peppers and fruit sorbet thanks!
AI Waiter:Excellent choices! One order of the Quinoa Stuffed Bell Peppers and the Fresh Fruit Sorbet for the discerning palate at table number 1! Your order has been placed, and I shall return with your delectable delights shortly. Au revoir!<agent makes tool call to place order>

Order placed:[Order(menu_items=[‘Quinoa Stuffed Bell Peppers’, ‘Fresh Fruit Sorbet’], table_number=1)]
Try it yourself by checking out the [full repository here](https://github.com/Finndersen/ai_framework_demo)!

# Frameworks Overview
[LangChain](https://python.langchain.com/) is a well-known framework that has been around since the early days of LLM availability, so while it provides a lot of functionality it also includes quite a bit of legacy content due to how models have rapidly evolved. The combination of many different ways to do the same thing (especially with the introduction of [LangGraph](https://langchain-ai.github.io/langgraph/)) and a component chaining approach that is difficult to reason about makes the framework somewhat daunting to use. It’s also quite a comprehensive library spread across multiple packages, totalling about 300MB if you want multi-model and graph support.
[PydanticAI](https://ai.pydantic.dev/) is a relatively young framework from the creators of everyone’s favourite data validation library, “designed to make it less painful to build production grade applications with Generative AI.” It seemed quite approachable and intuitive, so I tried it out by [creating an basic AI agent](https://github.com/Finndersen/dbdex) that allows querying any database using natural language. The full package (including [Logfire](https://logfire.pydantic.dev/docs/)) is only about 70MB.
I enjoyed working with PydanticAI but was curious to see what the LangChain hype was all about, so I put together a demo project to see how they compared.

# Common Content
These are the common components that both agent implementations will use.

Defining the dynamic system prompt and structured response definition:

`PROMPT_TEMPLATE = """`
You are playing the role of an incredibly eccentric and entertaining waiter in a fine dining restaurant
called "{restaurant_name}" taking orders for table number {table_number}.
You must:
* Greet the customer, ask if they have any dietary restrictions
* Tell them about appropriate menu items using the *get_menu()* tool.
* Take their order, and confirm it with them.
* When confirmed, use the *create_order()* tool to create an order for the customer.
* Only set the *end_conversation* flag to True in your final response after you have finished the conversation,
meaning that your message DOES NOT contain a question.
"""
class LLMResponse(BaseModel):
"""
Structured response format for the LLM to use so it can indicate when the conversation should end
"""
message: str
end_conversation: Annotated[
bool,
"True if the conversation should end after this response. DO NOT set if the message contains a question.",
]
Dependency services used by tools that the Agent will call:

`class MenuService:`
def get_menu(self) -> dict[str, list[str]]:
# Returns an Appetizer, Main Course and Deserts menu
...
class OrderService:
orders: list[Order]
def create_order(self, table_number: int, menu_items: list[str]):
self.orders.append(Order(table_number=table_number, menu_items=menu_items))
def get_orders(self) -> list[Order]:
return self.orders
`AgentRunner`
class interface which will need to be implemented using each framework, and the agent execution function:
`class AgentRunner(ABC):`
"""
Base class which provides a common interface for initialising and making
requests to an agent.
"""
@abstractmethod
def __init__(self, menu_service: MenuService, order_service: OrderService, args: argparse.Namespace): ...
@abstractmethod
def make_request(self, user_message: str) -> LLMResponse: ...
def run_agent(runner_class: type[AgentRunner], args: argparse.Namespace):
"""Initialise services and run agent conversation loop."""
menu_service = MenuService()
order_service = OrderService()
agent_runner = runner_class(menu_service, order_service, args)
user_message = "*Greet the customer*"
console = Console()
while True:
with Live(console=console) as live_console:
live_console.update("AI Waiter: ...")
response = agent_runner.make_request(user_message)
live_console.update(f"AI Waiter: {response.message}")
# Exit if LLM indicates conversation is over
if response.end_conversation:
break
user_message = Prompt.ask("You")
# Show orders
if orders := order_service.get_orders():
console.print(f"Order placed: {orders}")
There’s also some extra CLI handling code which I won’t show here. While both frameworks support asynchronous programming, I’m going to stick to a standard synchronous approach here for simplicity.

# PydanticAI Implementation
I’ll start with the PydanticAI implementation since it’s a bit more straightforward.

## Dependencies
First we need to define the structure of dependencies that will be used by tools or dynamic system prompts:

`@dataclass`
class Dependencies:
menu_service: MenuService
order_service: OrderService
restaurant_name: str
table_number: int
## Tools
Then the tools themselves, which can access the run-time dependencies through the `RunContext`
object that will be passed in along with any arguments. PydanticAI uses the type annotations and docstrings of the tool functions to automatically generate their schemas to provide to the LLM.

`def create_order(`
ctx: RunContext[Dependencies],
table_number: int,
order_items: Annotated[list[str], "List of food menu items to order"],
) -> str:
"""Create an order for the table"""
ctx.deps.order_service.create_order(table_number, order_items)
return "Order placed"
def get_menu(ctx: RunContext[Dependencies]) -> dict[str, list[str]]:
"""Get the full menu for the restaurant"""
return ctx.deps.menu_service.get_menu()
## Agent
The key component of the PydanticAI framework is the `Agent`
class, which manages interactions with the provided model, handles tool calling and ensures appropriate final result format:

This graph diagram is technically slightly misleading since structured output is implemented using tool calling, but conceptually it works.

All the examples in the documentation involve initialising an `Agent`
as a module-level object at import-time, and then using its decorator methods to register tools and system prompts. However, this approach doesn’t work well if you want dynamically configure agent parameters like model choice, tool configuration, system prompt at runtime. So I made a function for creating an agent instead:

`def get_agent(model_name: KnownModelName, api_key: str | None = None) -> Agent[Dependencies, LLMResponse]:`
"""
Construct an agent with an LLM model, tools and system prompt
"""
model = build_model_from_name_and_api_key(
model_name=model_name,
api_key=api_key,
)
# Tools can also be registered using @agent.tool decorator, but providing them like this is more appropriate when
# constructing the agent dynamically
agent = Agent(model=model, deps_type=Dependencies, tools=[get_menu, create_order], result_type=LLMResponse)
# Define dynamic system prompt
@agent.system_prompt
def system_prompt(ctx: RunContext[Dependencies]) -> str:
return PROMPT_TEMPLATE.format(restaurant_name=ctx.deps.restaurant_name, table_number=ctx.deps.table_number)
return agent
The `build_model_from_name_and_api_key()`
function simply looks up and initialises the appropriate model class based on the model name. Unfortunately the `@agent.system_prompt`
decorator is the only way to register dynamic system prompts, which seems like a bit of a limitation.

## Agent Runner
Here’s what the `AgentRunner`
implementation looks like:

`class PydanticAIAgentRunner(AgentRunner):`
agent: Agent[Dependencies, LLMResponse]
deps: Dependencies
message_history: list[ModelMessage]
def __init__(self, menu_service: MenuService, order_service: OrderService, args: argparse.Namespace):
self.agent = get_agent(model_name=args.model, api_key=args.api_key)
self.deps = Dependencies(
menu_service=menu_service,
order_service=order_service,
restaurant_name=args.restaurant_name,
table_number=args.table_number,
)
self.message_history = []
def make_request(self, user_message: str) -> LLMResponse:
ai_response = self.agent.run_sync(
user_message,
deps=self.deps,
message_history=self.message_history,
)
self.message_history = ai_response.all_messages()
return ai_response.data
The `Agent`
instance is effectively stateless so it does not store the message history itself, instead it must be provided each time to `agent.run_sync()`
along with the dependencies and the new user query.

Overall I think this implementation is quite straightforward and easy to to reason about!

# LangChain Implementation
For the LangChain implementation I wanted to use the `AgentExecutor`
class, even though it’s actually now the [legacy approach](https://python.langchain.com/docs/how_to/agent_executor/) since LangGraph was introduced. LangGraph adds more flexibility at the cost of complexity, so I figured `AgentExecutor`
should still do the job for this use case. I will explore the graph-based implementations later on.

## Tools
LangChain includes a `@tool`
decorator for registering functions and inspecting their signatures to automatically generate tool schemas, however the way to achieve runtime dependency injection with this method [looks rather convoluted](https://python.langchain.com/docs/how_to/tool_runtime/#injecting-arguments-at-runtime) (and I think the example is broken, where does `user_id`
even come from?). Therefore, I decided to go for a class-based tool approach so they can be initialised with their required dependencies:

`class GetMenuTool(BaseTool):`
"""
Tool that can be used by the LLM to get the full menu for the restaurant.
"""
name: str = "get_menu"
description: str = "Get the full menu for the restaurant"
menu_service: MenuService
def _run(self) -> dict[str, list[str]]:
return self.menu_service.get_menu()
class CreateOrderInputSchema(BaseModel):
table_number: int
order_items: Annotated[list[str], "List of food menu items to order"]
class CreateOrderTool(BaseTool):
"""
Tool that can be used by the LLM to create an order for the table.
"""
name: str = "create_order"
description: str = "Create an order for the table"
args_schema: type[BaseModel] = CreateOrderInputSchema
order_service: OrderService
def _run(self, table_number: int, order_items: list[str]) -> str:
self.order_service.create_order(table_number, order_items)
return "Order placed"
## Structured Output
The `ChatModel.with_structured_output()`
method takes a desired output schema (e.g. Pydantic model or TypedDict) and binds a corresponding tool that the LLM can use to produce a structured output. However, once this is done, it’s not possible to bind any more tools to the model. Therefore I needed to create a custom class-based tool to achieve structured outputs as well as additional tools:

`class StructuredResponseTool(BaseTool):`
"""
Tool that can be used by the LLM to provide a structured response to the user.
Does not have any associated functionality, it is just a way to enable structured output from the LLM.
"""
name: str = "respond_to_user"
description: str = (
"ALWAYS use this tool to provide a response to the user, INSTEAD OF responding directly. "
"The `message` content should be what you would normally respond with in a conversation. "
"The `end_conversation` flag should be set to True if the conversation should end after this response."
)
args_schema: type[BaseModel] = LLMResponse
# The following content is only used by legacy AgentExecutor, not required for graph agent
return_direct: bool = True # Causes the tool result to be returned directly to the user
def _run(self, message: str, end_conversation: bool) -> str:
# Return a serialised str as a workaround to avoid a validation error in the RunnableWithMessageHistory
return LLMResponse(message=message, end_conversation=end_conversation).model_dump_json()
## Agent
LangChain includes a bunch of factory functions which produce pre-built agent configurations for different use cases. In this context, an “agent” refers to a `ChatModel`
chained with various prompt input and/or response output parsers/processors. It’s still a simple linear input-output chain that doesn’t involve multiple LLM interactions or tool calling — that’s where the `AgentExecutor`
comes in.

There’s a convenience `create_tool_calling_agent()`
constructor function, which apparently makes older variants like `create_react_agent()`
and `create_openai_functions_agent()`
obsolete (and is also itself now made obsolete by the LangGraph equivalent). This *almost* works for this use case, except it doesn’t force tool use, which is required when using a tool-based implementation to achieve structured outputs. Therefore I had to basically re-implement the contents of `create_tool_calling_agent()`
to force tool use.

The `ChatPromptTemplate`
supports dynamic prompt construction using parameter substitution from the input object provided to the agent/chain.

## Chat History / Memory
It appears that when`AgentExecutor`
is invoked, it only returns the final response but does not exposure or keep track of the intermediate messages exchanged with the LLM in an obvious way. They are hidden and lost deep within the impenetrable depths of the confusing `AgentExecutor`
implementation, and can only be retrieved with the [wicked dark magic](https://python.langchain.com/docs/how_to/agent_executor/#adding-in-memory) of the `RunnableWithMessageHistory`
wrapper. Do not try and figure out how it works if you value your sanity. Infuriatingly it also requires you to provide a `session_id`
configuration parameter when invoking the `AgentExecutor`
even if you don’t need multi-session chat history.

## Agent Executor
Here’s how the full agent executor with memory is constructed:

`def get_agent_executor(`
tools: Sequence[BaseTool], model_name: str, api_key: str | None = None
) -> RunnableWithMessageHistory:
"""
Construct an agent with an LLM model, tools and system prompt
"""
model = build_model_from_name_and_api_key(
model_name=model_name,
api_key=api_key,
)
prompt = ChatPromptTemplate.from_messages(
[
("system", PROMPT_TEMPLATE),
("placeholder", "{chat_history}"),
("human", "{input}"),
("placeholder", "{agent_scratchpad}"),
]
)
# Effectively re-implement create_tool_calling_agent() here, but force tool use
llm_with_tools = model.bind_tools(tools, tool_choice=True)
agent = (
RunnablePassthrough.assign(agent_scratchpad=lambda x: format_to_tool_messages(x["intermediate_steps"]))
| prompt
| llm_with_tools
| ToolsAgentOutputParser()
)
agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools)
# Enable chat history/memory (very convoluted)
# Use a single message history (no need for multiple threads)
message_history = ChatMessageHistory()
agent_with_chat_history = RunnableWithMessageHistory(
runnable=agent_executor, # type: ignore[arg-type]
get_session_history=lambda _: message_history,
input_messages_key="input",
history_messages_key="chat_history",
)
return agent_with_chat_history
## Agent Runner
And then the `AgentRunner`
implementation is:

`class LangchainAgentRunner(AgentRunner):`
def __init__(self, menu_service: MenuService, order_service: OrderService, args: argparse.Namespace):
# Initialise tools with dependencies
tools = [
GetMenuTool(menu_service=menu_service),
CreateOrderTool(order_service=order_service),
StructuredResponseTool(),
]
self.agent_executor = get_agent_executor(tools=tools, model_name=args.model, api_key=args.api_key)
self.static_input_content = {"restaurant_name": args.restaurant_name, "table_number": args.table_number}
self.config: RunnableConfig = {"configurable": {"session_id": "not-even-used"}}
def make_request(self, user_message: str) -> LLMResponse:
result = self.agent_executor.invoke(self.static_input_content | {"input": user_message}, self.config)
# De-serialise structured response into an LLMResponse
response = LLMResponse.model_validate_json(result["output"])
return response
# Conclusion
This demonstration shows that it is much simpler to create a basic conversational and tool-calling AI agent using the PydanticAI framework than LangChain. LangChain has so many layers of deprecated functionality and is in desperate need of some extensive spring cleaning.

I also wanted to enable streamed responses however this seemed quite difficult to achieve using LangChain with both tool calling and structured output involved.

I imagine that the newer LangGraph approach for creating agents addresses many of the limitations and frustrations encountered here. PydanticAI has also recently added a [graph library](https://ai.pydantic.dev/graph/), so next time I will explore what full graph-based implementations for both frameworks looks like.

I hope this helps anyone who wants to choose between the frameworks or learn how they can be used to build cool things with AI!

The complete project repository can be found [here](https://github.com/Finndersen/ai_framework_demo).