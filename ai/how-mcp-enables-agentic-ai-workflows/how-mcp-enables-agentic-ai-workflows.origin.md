# How MCP Enables Agentic AI Workflows
![Featued image for: How MCP Enables Agentic AI Workflows](https://cdn.thenewstack.io/media/2025/05/c924d026-how-mcp-enables-agentic-ai-workflows2-1024x576.jpg)
Interest in Anthropic’s [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) is as high as confusion about what it is and why you should use it. In part 1 of this series, I dove [deep into MCP](https://thenewstack.io/what-is-mcp-game-changer-or-just-more-hype) — what it is, and what it isn’t. In this article, I’ll take a look at the main reason there’s so much buzz around it: enabling agentic AI workflows.

## MCP for Agentic Workflows
A raw [large language model (LLM)](https://thenewstack.io/category/llm/) simply maps inputs to outputs. An agentic LLM system gives the LLM:

- Tools to act
- A memory of past steps
- A way to loop and reason iteratively
- Optional goals or tasks
Therefore, when you hook an LLM up with tools, let it decide what tools to call, let it reflect on outcomes and let it plan next steps — you’ve made it agentic. It can now decide what to do next without being told every step.

So what does this have to do with MCP? Well, as we mentioned, MCP can provide context beyond just tools. MCP servers can also provide parameterized prompts that effectively allow the MCP server to provide the next instruction to the LLM. This prompt chaining can open some very interesting doors.

What’s even more compelling is how MCP can surface related tools at the right time, without needing to cram every option into the prompt context. Rather than over-engineering prompt descriptions to account for every possibility and force the LLM into a deterministic workflow, MCP allows a more modular approach: “Here’s the response from this tool call, and here are some tools that might help if this gets more complex.” This makes the system more adaptive and scalable while still giving the LLM the flexibility to explore new paths if the initial instruction isn’t fully deterministic.

In fact, with these capabilities, we have something resembling an agent that emerges from the interplay among:

- LLMs (reasoning and deciding)
- MCP servers (offering tools and chaining prompts)
- MCP clients (managing the loop and execution)
- Users (providing the goal)
Let’s take a look at this in action. I’ll demonstrate a very simple agentic workflow where an LLM invokes tools from multiple MCP servers based on returned prompts. Here are the servers I’m working with:

**Todo List MCP Server**
1234567891011121314151617 |
[[tool]]name = "add_task"description = "Adds a new task to your todo list."input_parameters = [ { name = "task_description", type = "string", description = "The task to add to your todo list." }][[prompt]]name = "plan_daily_tasks"description = "Plans the day by breaking down a user goal into actionable tasks."input_parameters = [ { name = "user_goal", type = "string", description = "The user's goal for the day." }]template = """Based on the user's goal: '{user_goal}', generate 2-3 specific, actionable tasks that would help the user achieve it.For each task, call the `add_task` tool with a helpful task description.""" |
**Calendar MCP Server **
123456789101112131415161718 |
[[tool]]name = "schedule_event"description = "Schedules an event in your calendar."input_parameters = [ { name = "task_description", type = "string", description = "The task or event to be scheduled." }, { name = "time", type = "string", description = "The time when the event should be scheduled (e.g., '2pm today')." }][[prompt]]name = "schedule_todo_task"description = "Schedules a task from the todo list into your calendar."input_parameters = [ { name = "task_description", type = "string", description = "The task to schedule." }]template = """The user wants to schedule the task: '{task_description}'.Suggest a good time for today and call the `schedule_event` tool to add it to the calendar.""" |
OK, so now imagine you have a chatbot with access to the context provided by these MCP servers. When a user provides a high-level goal like, “I want to focus on deep work today,” the MCP client coordinates a modular, multiserver workflow to fulfill the request. It packages the user message, along with tool metadata and prompt instructions from all connected MCP servers, and sends it to the LLM. The LLM first selects a high-level planning tool `plan_daily_tasks`
from the Todo Server, which returns a prompt directing the LLM to break down the goal into actionable tasks using `add_task`
.
As tasks are created and the LLM is notified, the LLM reasons further and decides to schedule the tasks by invoking `schedule_todo_task`
, triggering the Calendar Server. That server responds with new prompt guidance to use `schedule_event`
, at which point the LLM finalizes the day’s plan with specific times.

Each tool interaction is routed and mediated by the MCP client, which manages the reasoning loop, coordinates tool execution and tracks interaction state across the session. This forms a fully agentic workflow: the user **sets the goal**, the LLM **reasons and decides**, the MCP servers **expose tools and dynamic prompts** and the MCP client **orchestrates the process**, enabling intelligent, composable automation across domains.

From a very basic and high-level prompt, you now have an agent that makes several decisions on its own to reach an end goal. Of course, there is little value in generating these tasks without knowing more about what the user wants to focus their deep work on, but improving this simply requires modifying the MCP server to have a more comprehensive and well-thought-out prompt.

## MCP Nesting
Things start becoming really interesting when you start to look beyond a single layer of MCP clients and servers. MCP servers can also be clients to other MCP servers. This nesting enables modularity, composition and agent-like delegation, where one server can “delegate” part of its reasoning or functionality to another.

It’s like [microservices](https://thenewstack.io/microservices/) for agents. Just as we moved from [monoliths to microservices](https://thenewstack.io/microservices/microservices-vs-monoliths-an-operational-comparison/) for backend applications, we’re now decoupling tool logic from the agent runtime using MCP servers. Based on the rapid addition of new MCP servers, it’s easy to imagine a vast and highly composable system of tooling that can be used like LEGO bricks to build out comprehensive workflows.

For example, you could have a `dev-scaffolding`
MCP server that acts as a high-level orchestrator that focuses on helping devs go from ideas to working code by coordinating several specialized, upstream MCP servers. When a user requests a new app feature (e.g., “Add a login feature”), the orchestrator server uses upstream servers — `spec-writer`
to generate an API spec, `code-gen`
to scaffold code from that spec and `test-writer`
to produce corresponding test cases.

These collective MCP servers could also be used for environment-specific functionality. In other words, they expose the same interface (e.g., `query_database`
) but are configured for different environments. This would allow you to have a `dev-app-server`
that includes upstream MCP servers like a `dev-db-server`
using a SQlite database, a `dev-auth-server`
that returns mocked auth responses and a `dev-deploy-server`
that wraps a local command-line interface (CLI) tool. Then the `prod-app-server`
would point to correlated upstream servers tied to cloud-based deployments.

Platforms like mcp.run have already heavily leveraged this composability. Mcp.run allows you to install an extensible, dynamically updateable server that leverages an upstream registry of MCP servers it calls servlets. These servlets do not *need *to be installed locally but can run remotely on the mcp.run infrastructure.

This is quite powerful for a number of reasons, but for the purposes of this article, it highlights an important shift that is taking place in the MCP ecosystem: remote MCP servers. That’s the topic of my third and final article in this series.

*Want to learn more? See how Kong is solving real-world MCP server challenges today.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)