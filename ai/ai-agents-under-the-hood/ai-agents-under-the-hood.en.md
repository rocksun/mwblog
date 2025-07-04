## [Permalink](#heading-motivation-why-you-should-care "Permalink")Motivation: Why You Should Care

Not a day goes by without hearing the term “AI agent.” I have built multiple systems that use AI agents, like [patra.app](https://patra.app). While building those and reading through a lot of resources, I learned how AI agents actually work and what they really are under the hood. I used to think everyone understood what they are. You hear about them every day right, right? But then...

During one of our late night walks, I asked my friend, “What do you think an AI agent is, anyway?”

They gave a surprising answer that somehow included fine-tuning, chatbot, and even “MCP” 🤯. I tried asking a few more people and realized that anyone who hasn’t actually built an agent or has only seen the abstractions thinks it’s all just magic. I want to reveal that magic in this article. I don’t want you to see AI agents as something mysterious anymore. Instead, I want you to gain both an understanding and a mental model to work with them.

Well, I don’t blame them or you. There are just too many definitions for what an AI agent does, rather than what it actually is.

I promise that by the end of this, you will not only understand what an AI agent is, but also how it works, how to think about them, and why they do what they do under the hood. If you stick with this, you’ll be able to explain to your friends:

1. What an AI agent is
2. How an AI agent works
3. What the heck tools are
4. What an orchestration framework is
5. What memory is
6. What the types of AI agents are
7. The mental model for building an AI agent
8. What a multi-agent framework is

Before we begin, understand that an AI agent isn’t just any chatbot. A chatbot might simply reply with information using an LLM, or it might actually have an agent behind it that can do real tasks for you, like booking flights or checking prices using tools and APIs. Not every chatbot is an agent, but every agent can appear just like a regular chatbot on the surface. Now, let’s look at the problem with how the internet explains AI agents.

Ok, first things first, let’s understand the definition of what an AI agent is, straight from our good old friend Google search, who recently gave birth to this Search Labs thing:

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750505693141/99eb7803-dd5c-4c52-8d81-ed99522678ee.png?auto=compress,format&format=webp)

> An AI agent is a software program that utilizes artificial intelligence to perform tasks and achieve goals autonomously, often with minimal human intervention

You see the problem? Most definitions of what an AI agent is are based on what to expect as output or how it behaves, instead of focusing on what it actually is.

If I ask, "What is an LLM?" we get a much more acceptable answer:

> A Large Language Model (LLM) is **a type of AI model, specifically a deep learning model, trained on massive amounts of text data.**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750505830733/b209c299-31cf-4b19-b28e-fc47f9f227a5.png?auto=compress,format&format=webp)

Notice how this answer is not about LLMs generating the next most likely token, but more about what they are fundamentally. For AI agents, we are going to fix this problem in this article. Enough promises. Let’s get to the point.

Let’s first write an acceptable definition of an AI agent. All we have to do in this article is break that definition down into smaller pieces and understand each part of it:

Agents are **software systems** where **LLMs** use reasoning to control the flow of execution, **dynamically** choosing which **tools** to use and determining each step required to reach a **goal**.

That’s a mouthful. Let’s break down each part so we can actually understand it.

## [Permalink](#heading-agents-are-software-systems "Permalink")**Agents are Software Systems**

This is the first clarification, and it’s the easiest. When someone says “AI agent,” it should pop up in your head that it’s just software. For a simple agent, it might just be a few files of code, nothing more. The reason we also call it a system is because it contains different pieces or modules, such as:

1. LLMs
2. Working Memory or state
3. Prompts
4. Tools
5. Orchestration Layer

You already know what LLMs are. When we dive deeper into the other parts of our definition, the other modules of an AI agent will reveal themselves. Don’t worry if you can’t remember these yet. They will come up again.

In our definition, we mention a flow of execution that is dynamic. Let’s see what that means next.

## [Permalink](#heading-dynamic-flow-of-execution "Permalink")**Dynamic** Flow of Execution

To execute any task, we usually need to take one or more steps or actions. These decisions can be thought of as a workflow, or a set of rules that determine how we complete a task.

Let’s look at an example.

Suppose you want to create a customer success bot that takes a ticket as input, then responds to the creator, and either resolves the ticket or escalates it if needed.

Notice that resolving or escalating the ticket is basically an operation that needs to be performed on some external CRM software. Our LLM program should be able to handle this.

We won’t get into the details of what the code would look like right now. I’ve created a sample you can check out if you’re interested. You can use a library like “langgraph” to achieve this, and the graph or flow of execution looks something like this:

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750523331009/2478546b-8dd2-47d0-81fd-9b37556dafe9.png?auto=compress,format&format=webp)

💡

You may notice a few code examples below. If they’re not relevant to you, feel free to skip them and continue reading

Notice how we first start by classifying a ticket, which would be handled by an LLM prompt. Next, we generate the initial response, which is another LLM prompt. Then, we check if escalation is needed. This can either be done through an API call or by using a static piece of code to decide if we should escalate. Finally, depending on what’s needed, we can escalate the ticket and generate a final response to let the customer know what happened.

```

workflow = StateGraph(SupportTicketState)


workflow.add_node("classify_ticket", classify_ticket)
workflow.add_node("generate_initial_response", generate_initial_response)
workflow.add_node("check_escalation", check_escalation_needed)
workflow.add_node("escalate_ticket", escalate_ticket)
workflow.add_node("resolve_ticket", resolve_ticket)


workflow.add_edge(START, "classify_ticket")
workflow.add_edge("classify_ticket", "generate_initial_response")
workflow.add_edge("generate_initial_response", "check_escalation")


workflow.add_conditional_edges(
    "check_escalation",
    should_escalate,
    {
        "escalate": "escalate_ticket",
        "resolve": "resolve_ticket"
    }
)

workflow.add_edge("escalate_ticket", END)
workflow.add_edge("resolve_ticket", END)

```

Entire code for this is available here: <https://github.com/thesmallstar/AI-Agents-Under-the-hood-blog/blob/main/workflow.py>

This is how we can create the entire flow in langgraph. We start with a StateGraph(see the first line of the example above) and set an initial state. Then, we add multiple nodes or logical blocks. If needed, we can include a conditional block that makes decisions based on the output of the previous node.

In the example above, the value of should\_escalate, which comes from the check\_escalation node, is used to determine which part of the graph or “workflow” we go to next.

A node like "resolve ticket" will look something like this:

```
def resolve_ticket(state: SupportTicketState):
    """Resolve the ticket and generate a final customer-facing response."""
    call_resolution_api(state['ticket_id'])
    prompt = f"""
    Generate a customer-facing response to inform them their ticket is resolved.

    Ticket ID: {state['ticket_id']}
    Customer: {state['customer_name']}
    Issue: {state['issue_description']}

    The response should:
    1. State clearly that the issue has been resolved.
    2. Briefly explain the solution.
    3. Thank the customer for their patience.
    4. Ask if they need any further assistance.
    """
    response = llm.invoke(prompt)
    return {
        "final_response": response.content,
        "status": "Resolved"
    }

```

Notice how we first call the resolution API and then run the prompt to generate a response for the ticket.

You might have guessed by now that we have complete control over the flow of the program. We can specify exactly what we want and when we want it. For example, the first step will always be to classify a ticket, then generate the initial response, and then follow a fixed set of steps or a workflow. This is a workflow system and not an agent. We are missing the dynamic flow of execution here, because we have already decided what happens at each step.

Let’s try to make an agentic flow 🫣 for this. We will be using the ReAct agent flow. Don’t worry if this sounds new, we will cover it in detail soon. We will uncover it layer by layer, but first, let’s look at this along with the abstractions that exist.

**By the way, ReAct stands for "Reasoning and Acting."**  
It is a popular agent flow that lets the model reason step by step and choose when and how to act (for example, by calling tools) as part of the process.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750524956830/946ad5ed-a30f-4883-9530-73be62fd190f.png?auto=compress,format&format=webp)

In our example:

The **task** is to either resolve or escalate the ticket and give back a response.

In the **Act** stage, the agent can use a tool to classify, escalate, or resolve the ticket.

In the **Observe** stage, the agent gets new observations, which are outputs from tool calls, like what the classification of the ticket is or whether the escalation was successful.

In the **Reasoning** stage, which is basically the LLM “thinking” about what it should do next, the agent might have to decide whether to call a tool, generate a response, or check the output from the Observe stage. As you might expect, the Reasoning stage is where this loop starts.

Notice something here? We never talked about a workflow. We never decided, in the form of code or a static flow, when the LLM should use a tool, classify a ticket, or resolve a ticket.

To understand this further, let’s check out the code that can be used to do the same. Note that we are using the CrewAI library to achieve this. Remember when we defined what an agent is: Tools, LLM, Prompts, Memory, and an Orchestration Layer. CrewAI is the Orchestration Layer here. It abstracts away a lot of the details about how the agent makes a tool call, how the response gets back to the agent, and adds a lot of syntactic sugar to make creating an agent simpler. This is where all the magic of how the agent works under the hood happens. We will look at the responsibility of this Orchestration Layer in detail later, and also see what popular options exist and what features they offer.

**Now getting to the code:**

```

support_agent = Agent(
    role="Senior Customer Support Specialist",
    goal="Efficiently and accurately process customer support tickets, ensuring high customer satisfaction by providing timely and helpful responses.",
    backstory=(
        "You are a seasoned support specialist with a knack for understanding customer needs. "
        "You excel at identifying the root cause of issues, communicating clearly, and "
        "knowing precisely when a problem needs to be escalated to a senior team member. "
        "Your goal is to resolve issues on the first touch whenever possible, but never at the expense of quality."
    ),
    tools=[ClassifyTicketTool(), EscalateTicketTool(), ResolveTicketTool()],
    llm=llm,
    verbose=True,
    allow_delegation=False
)


def create_ticket_processing_task(agent, ticket_id, customer_name, issue_description):
    return Task(
        description=f"""
        Process customer support ticket with the following details:
        - Ticket ID: {ticket_id}
        - Customer Name: {customer_name}
        - Issue Description: {issue_description}

        Follow this exact workflow:
        1.  **Analyze and Classify**: Carefully read the issue description to understand the problem. Classify its 'Priority' (Low, Medium, High, Critical) and 'Category' (e.g., Technical, Billing, Feature Request).
        2.  **Draft Initial Response**: Write a professional and empathetic initial response to the customer acknowledging their issue.
        3.  **Decide to Escalate or Resolve**: Review the ticket content and its priority. You MUST decide if escalation is necessary. Escalate for 'High' or 'Critical' priority, or if the customer uses keywords like 'urgent', 'angry', 'third time', 'unacceptable', etc.
        4.  **Use a Tool**:
            - If you decide to escalate, you MUST use the 'Escalate Ticket' tool. Provide a clear reason for the escalation.
            - If you decide to resolve, you MUST use the 'Resolve Ticket' tool.
        5.  **Draft Final Response**: Based on the action you took (escalation or resolution), write a final, clear, customer-facing response. If escalated, inform them it's with a specialist. If resolved, confirm the solution and close the loop.

        Your final output must be a comprehensive report in markdown format that includes:
        - The classified priority and category.
        - The initial response.
        - The action taken with the corresponding tool.
        - The final customer-facing response.
        """,
        agent=agent,
        expected_output="A detailed markdown report with the classified ticket details, initial response, action taken, and final customer-facing response."
    )

```

Entire code for this available here: <https://github.com/thesmallstar/AI-Agents-Under-the-hood-blog/blob/main/agent.py>

Ok, the initial observations are clear. There’s no static workflow but only a dynamic one. Instead of the software dictating each step, the LLM decides what to do at every step.

**The Little Trick We Play**

But here’s a fun little trick we play: we say, “Follow this exact workflow” in the Task’s description (which is syntactic sugar in CrewAI). Wait, so what’s the point of it being an agent? Didn’t we just instruct the exact workflow, but this time in plain English?

**Isn’t That Just a Static Workflow?**

Well, yes, you did. But the point is, you can’t always do this. Not all problems are simple enough to be a five-step process where you can predict exactly what those steps will be and in what order.

For example, if you’ve used Cursor’s agent mode, can you say the agent will always do X first and then Y? No. It depends on your request. In a complex problem, it’s hard (if not impossible) to write a fixed workflow.

**Real World Example**

When I was creating [patra.app](http://patra.app)[,](https://patra.app) which is basically a Jira agent on Slack, there were endless possibilities for the kinds of queries users could ask.

Example:  
Create me a Jira ticket for this thread, assign it to ManthanSurkar, add a label Y, and set the priority to Z.

Imagine trying to do this in a static workflow. There would be multiple steps involved. First, check if a user is tagged in the Slack message. If they are, find their email, and so on. Let’s not get into the weeds.

Now imagine an action like:  
Check my Google Calendar and create a Jira ticket for the action items from the event that happened yesterday evening.

These are complex, real-world scenarios. Writing a specific workflow for each is hard. That’s why AI agents have a dynamic flow of execution.

**Don’t Overcomplicate Simple Things**

WOW, THAT’S GREAT! HOW ABOUT WE ALWAYS HAVE A DYNAMIC FLOW OF...

Stop. No. Don’t make that mistake. When you can be deterministic, why would you want to add a layer of non-determinism to your software application? Is the job not hard enough already that you want to bring in an AI model that is non-deterministic?

Agents are meant for complex problems, not the ones where you already know the solution and can jot it down as a workflow. Don’t complicate your life. Unless you just want to overengineer stuff. That’s fun, I’ll admit.

In a real-world scenario, a mix of both approaches is often used. For example, imagine you have three support agents, each dedicated to a different product. Depending on which product a ticket is linked to, you can select the appropriate agent and route the request to that agent.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750586210175/09c85433-260c-4dbf-bc87-b2ff4b356c2f.png?auto=compress,format&format=webp)

**What’s Next?**

So far, we’ve kept tools and the orchestration framework as a black box. What the heck are those? How does an LLM call a tool? What is a tool, anyway? Let’s cover the “under the hood” of all these terms in the next section.

## [Permalink](#heading-tools-amp-orchestration-framework "Permalink")**Tools &** orchestration **Framework**

LLMs predict the next token. You’ve heard this a million times by now. If that’s the case, how does it call a tool just by predicting tokens? Well, actually, it doesn’t. The LLM just indicates that it wants to use a tool, then waits for the orchestration framework to figure out what tool it should call, actually perform the call, and then let the LLM know, “Hey, the tool was called and here is the output.”

**A Simple Example**

Let’s break this down with a simple program.

Suppose we want to add or subtract two numbers based on a natural language message from a user. Since we’re dealing with natural language, we can use an LLM. But adding two numbers is a solved problem, and we should be able to do it deterministically, right? This is exactly where tools come in.

**Why Use Tools?**

Tools let the LLM communicate with other systems through APIs. They can also allow the LLM to talk to other agents (drum roll for multi-agent systems) or perform deterministic tasks, like adding two numbers.

**Defining a Tool**

Let’s define how our tool will look:

```
def add(a: int, b: int) -> int:
    """Adds two integers together."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Subtracts the second integer from the first."""
    return a - b

SYSTEM_PROMPT = """You are a helpful assistant with access to the following functions:

1. `add(a: int, b: int)`: Adds two integers together.
2. `subtract(a: int, b: int)`: Subtracts the second integer from the first.

When a user asks a question that can be answered by one of these functions, 
you MUST respond ONLY with a JSON object in the following format:
{
  "function_name": "name_of_the_function",
  "arguments": {"arg_name": "value", ...}
}

Do not include any other text, explanations, or markdown formatting. 
Your entire response must be only the JSON object.

If you can answer the question without a function, 
just provide the answer directly in plain text."""

```

Notice that we define two Python functions. They can perform the deterministic task of calculating. The prompt lets the LLM know that it can call the above functions. If the LLM wants to use any of these tools, it gives us the output in a specific format, and we can "parse" and identify which function needs to be called. Once the call is completed, we let the LLM know the answer and allow it to continue execution.

**What does "continuing the conversation" mean?**  
It’s simply adding a new message, saying that the tool call was successful and the output is X, or letting the LLM know the tool call has failed. What happens next? We let the LLM do its job of generating the next token, but now with the output of the tool call added in.

**That’s basically it.**  
This is how tool calls work under the hood. There is a parser and in our example, here’s what a parse function would look like:

```
def parse_and_execute(response_content: str) -> (str, str):
    """
    Tries to parse the LLM's text response as a JSON function call.
    If successful, it executes the function and returns the result and function name.
    Otherwise, it returns (None, None).
    """
    try:
        call_data = json.loads(response_content)
        function_name = call_data.get("function_name")
        function_args = call_data.get("arguments")

        if not all([function_name, isinstance(function_args, dict)]):
            return None, None 

        print(f"Parser is executing function: '{function_name}' with args: {function_args}")

        available_functions = {"add": add, "subtract": subtract}
        function_to_call = available_functions.get(function_name)

        if function_to_call:
            result = function_to_call(**function_args)
            return str(result), function_name
        else:
            return f"Error: Unknown function '{function_name}'.", function_name

    except (json.JSONDecodeError, TypeError):
        return None, None 

```

The entire code for this is available here: <https://github.com/thesmallstar/AI-Agents-Under-the-hood-blog/blob/main/tool.py>

And then there’s the **invoke** method. This allows you to merge the response from the tool call back into the original set of messages, so the LLM can generate the next token with this extra piece of information included.

```

def invoke(user_prompt: str):
    """
    Invokes the LLM, manually handling the function-calling loop.
    """
    print(f"\n{'='*20} Invoking for prompt: '{user_prompt}' {'='*20}")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]

    
    print("\n--- 1. Sending prompt to LLM to generate function call JSON... ---")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    response_message = response.choices[0].message
    messages.append({"role": "assistant", "content": response_message.content})

    
    print("\n--- 2. Manually parsing response for a function call... ---")
    function_output, function_name = parse_and_execute(response_message.content)

    if function_output:
        
        messages.append({
            "role": "user", 
            "content": f"I have called the function '{function_name}'. The result is: {function_output}"
        })

        
        print("\n--- 3. Sending function output back to LLM... ---")

        second_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        final_response = second_response.choices[0].message.content
    else:
        
        final_response = response_message.content

    print(f"\n--- Final Answer ---")
    print(final_response)
    return final_response

```

You know what we just did? We built a mini agent framework. This framework is an oversimplified version of how things work under the hood in more complex systems. They all have parsing layers to figure out what the next action should be. Is it a tool call? Should another agent continue the execution? And so on.

Today, OpenAI and Anthropic both support tool calling out of the box in their SDKs. You can learn more about OpenAI’s new Responses API and its support for function calls here: <https://platform.openai.com/docs/quickstart?api-mode=responses>

**Exploring Popular Agent Frameworks**

Some of the popular Agent frameworks includes -

* **CrewAI** – A Python framework for coordinating multiple agents as a team.  
   Read more: [CrewAI on Github](https://github.com/crewAIInc/crewAI)
* **OpenAI Agents SDK** – A lightweight toolkit for building and connecting agents, with built-in tracing and guardrails.  
   Read more: [OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/)
* **MetaGPT** – A multi-agent system that simulates a software team by assigning roles like product manager and developer to different agents.  
   Read more: [MetaGPT on GitHub](https://github.com/FoundationAgents/MetaGPT)

Now that you know what tools and frameworks are, it makes sense to explore the popular options. Keep in mind, each one will have its own syntactic sugar for defining a tool, setting up different aspects of an agent, or describing its goal and persona.

**Wait, Persona?**

That’s new. Why does an agent need a persona? What is a persona, anyway?

If you think about it, having a specific persona helps the agent stay focused on its goal and make better decisions about what tools to use. This becomes especially important in a multi-agent system where different agents interact with one another. A complex problem can be solved by a multi-agent system where each agent has a different persona.

**Up Next: Multi-Agent Systems**

In the next section, let’s talk more about multi-agent frameworks and why we might need multiple agents working together to get the job done.

Now that we understand what an agent is, a multi-agent system is, as you might expect, simply multiple agents working together.

**Remember, agents are just:**

* An LLM with access to tools
* A set of prompts (like persona, goal, etc.)
* Memory (which we’ll talk about later)
* All built using an orchestration framework so everything works together

But what does it actually mean to have multiple agents in a system? How do they communicate? Well, that’s up to the orchestration framework. For example, CrewAI allows two main operations in a multi-agent system.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750530783347/e075dac0-4879-4b27-9505-2d6446ff99ed.png?auto=compress,format&format=webp)

Source: [CrewAI Collaboration Concepts](https://docs.crewai.com/concepts/collaboration)

All the other agents are added as tools. The current agent can either ask a question to an expert agent or delegate the task to that agent, assuming it can take over that responsibility.

**Why Use Multi-Agent Systems?**

Multi-agent systems help organize tasks and break them into smaller problems. Each problem can be solved by an individual expert agent with access to specific tools and a particular persona, much like a team working on a project. Another advantage, as noted by Anthropic in their [blog post](https://www.anthropic.com/engineering/built-multi-agent-research-system) on multi-agent systems, is that you can use more tokens (so the system can "think more") when tackling a complex problem.

In the example above, asking a question means starting with fresh working memory (chat history), which can extend to tens of thousands of tokens and answer a specific query before the main agent continues its work.

You can read about different types of multi agent systems later [here](https://langchain-ai.github.io/langgraph/concepts/multi_agent/).

**Warning:** As you might expect, multi-agent systems are complex, hard to debug, and difficult to evaluate. I think it’s a good idea to start with a workflow. If the flow of execution becomes complex, then try building an agent. If it’s still complicated and you’re running into issues like context window limits, then consider using a multi-agent framework. Don’t use more complexity or power than you actually need.

We have touched on all the aspects of what an AI agent is, except memory. Let’s dive into this now.

In many cases, you don’t need to care much about the memory aspect of the agent until your system gets complex enough, or unless you are using an agent framework that relies on some form of memory.

There are two forms of memory that an AI agent can potentially have, much like humans do:

Short term memory lets the LLM keep track of the recent or active conversation that is happening. For example, when an agent decides to make a tool call, it doesn’t forget anything that has happened before the tool was triggered. The conversation doesn’t start over; it continues right where it left off. Simply put, whatever is in the context window of the LLM is its short term memory. Sometimes, if the context window isn’t long enough to hold everything, we can summarize the older messages and keep the most recent ones as they are.

Here’s an example. Let’s say you are doing a complex mathematical operation using an AI agent, but you only have a small context window:

M1: User: perform 10 + 20 + 30 + 40 + 50  
M2: LLM: *Tool call, 10 + 20*  
M3: User: Output 30  
M4: LLM: *Current answer is 30, let’s proceed. Tool call 30 + 30*  
M5: User: Output 60  
M6: LLM: *Current answer is 60, let’s proceed. Tool call 60 + 40*

At this point, we can summarize or even eliminate M2 to M4 into one line, like M2’:

M1: User: perform 10 + 20 + 30 + 40 + 50  
M2’: User: Output of 10 + 20 + 30 is 60, proceed further.  
M6: LLM: Current answer is 60, let’s proceed. Tool call 60 + 40

Notice how we compressed this information without losing anything important. This is a very simplified example, but in more complex situations, things can get tricky. Making sure that the right things stay in the agent’s short term memory can be a real challenge.

Sometimes, you may not even summarize, but just ignore older messages. The implementation and use of short term memory for an agent can vary, depending on the problem you are trying to solve.

We also mentioned that an agentic framework might depend on short term memory. An example is the RAISE framework, which is an extension of the ReAct framework we saw earlier.  
**RAISE stands for Reasoning and Acting through Scratchpad and Examples.** The scratchpad lives in the agent’s short term memory and is used during execution. Examples, on the other hand, are long term memory.

Read the paper that introduced RAISE framework here: <https://arxiv.org/pdf/2401.02777>

Long-term memory is what agents remember across multiple conversations. If you have used ChatGPT and tried out the memory feature, that’s like long-term memory for the system. When you have a conversation, the system stores relevant information that it can retrieve later to give you a better answer. That’s long-term memory in action.

In our previous example of a customer success bot, you could store previously answered tickets, whether answered by a human or by the agent, and then retrieve relevant examples to help answer the current ticket better. This is long-term memory being used, which is often accessed through a tool call. The tool call can be a simple database query or a RAG system that helps retrieve memory stored in persistent storage.

Notice that for long-term memory to actually be useful, it needs to appear in working memory or short-term memory, where it will be used and considered when generating the next token.

# [Permalink](#heading-mental-model-to-work-with-agents "Permalink")Mental Model to work with agents

That’s a lot of theory and under-the-hood information. I want you to leave with a practical mental model I use while developing agents, or really any LLM application. This is how I have made [patra.app](http://patra.app) work reliably, and also how I’ve shipped multiple other production systems.

**The golden model:**  
Keep yourself in the place of the agent. Imagine you are that agent.

It might sound cliché. But what does “be that agent” really mean? LLMs are not magic. If a human cannot figure out how to proceed in a particular situation, most likely an agent will not be able to either. Let’s say you are building a coding agent and you give it a task to fix a bug.

Put yourself in the shoes of the agent. Imagine facing a codebase with 1000 files. How is it supposed to know where to begin? It has no business context, and no code context. As you develop this empathy for agents, you stop believing they are some kind of magic wand. You’ll write better goals, provide more context, and add more tools. Do exactly what you or a human would do in the same situation. Does the agent have everything a human would need?

Now, don’t take this literally and overcomplicate everything. The point is to develop empathy for agents. When you do, your agent design will always improve.

Hopefully, you now see that AI agents are not magic. They are just smart systems with the right setup: LLMs, memory, tools, some orchestration, and a good mental model for solving real problems. The hype is justified, but the reality is both simpler and more practical than most people realize.

If you take away just one thing, let it be this: building effective AI agents is about clarity, empathy, and structure. Treat your agent like a new teammate. Give it context, clear goals, and the right tools. Do not expect it to read your mind.

There is still a lot evolving in this space. New frameworks are coming up, new approaches to memory are being tested, and multi-agent collaboration is getting more creative. But if you understand the basics, you are already ahead of most. So the next time someone mentions "AI agent" in conversation, you will know not only what it is but also how it thinks and works.

If you ever get stuck, just ask yourself: if I was the agent, what would I need to succeed? That is where the real magic happens.