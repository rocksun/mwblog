
<!--
title: AI Agents：底层原理探秘
cover: 
summary: AI Agent 是利用 LLM 推理控制执行流程的软件系统，动态选择工具以达成目标。关键组成部分包括 LLM、记忆、提示词、工具和编排层。多Agent系统通过协作解决复杂问题，但需谨慎使用。操作Agent的心理模型是设身处地思考，提供清晰的目标和必要的工具。
-->

AI Agent 是利用 LLM 推理控制执行流程的软件系统，动态选择工具以达成目标。关键组成部分包括 LLM、记忆、提示词、工具和编排层。多Agent系统通过协作解决复杂问题，但需谨慎使用。操作Agent的心理模型是设身处地思考，提供清晰的目标和必要的工具。

> 译自：[AI Agents Under The Hood](https://blog.surkar.in/ai-agents-under-the-hood)
> 
> 作者：Manthan Surkar

### 动机：为什么你应该关心

几乎每天都能听到“AI Agent”这个词。我已经构建了多个使用 AI Agent 的系统，比如 [patra.app](https://patra.app)。在构建这些系统并阅读大量资源的过程中，我了解了 AI Agent 实际的工作原理以及它们在底层到底是什么。我曾经认为每个人都理解它们是什么。你每天都听到关于它们的消息，对吧？但是...

在一次深夜散步时，我问我的朋友：“你认为 AI Agent 到底是什么？”

他们给出了一个令人惊讶的答案，其中不知何故包含了微调、聊天机器人，甚至还有“MCP”🤯。我尝试问了更多人，意识到任何没有实际构建过 Agent 或者只看过抽象概念的人都认为这一切只是魔法。我想在这篇文章中揭示这个魔法。我不想让你再把 AI Agent 看作是神秘的东西。相反，我希望你获得对它们的理解和一个可以用来操作它们的心理模型。

好吧，我不责怪他们，也不责怪你。对于 AI Agent 的作用，而不是它实际是什么，定义实在太多了。

我保证，到本文结束时，你不仅会理解 AI Agent 是什么，还会理解它的工作原理、如何思考它们，以及它们在底层为什么会这样做。如果你坚持读完本文，你将能够向你的朋友解释：

1.  什么是 AI Agent
2.  AI Agent 如何工作
3.  工具到底是什么
4.  编排框架是什么
5.  什么是记忆
6.  AI Agent 的类型有哪些
7.  构建 AI Agent 的心理模型
8.  什么是多 Agent 框架

在我们开始之前，请理解 AI Agent 不仅仅是任何聊天机器人。聊天机器人可能只是使用 LLM 回复信息，或者它实际上可能有一个 Agent 在背后为你做实际的任务，比如预订航班或使用工具和 API 检查价格。并非每个聊天机器人都是 Agent，但每个 Agent 在表面上看起来都像一个普通的聊天机器人。现在，让我们看看互联网上解释 AI Agent 的问题。

### 问题

好的，首先，让我们从我们老朋友 Google 搜索那里了解一下 AI Agent 的定义，它最近诞生了 Search Labs 这个东西：

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750505693141/99eb7803-dd5c-4c52-8d81-ed99522678ee.png?auto=compress,format&format=webp)

> AI Agent 是一种软件程序，它利用人工智能来执行任务并自主实现目标，通常只需要最少的人工干预。

你看到问题了吗？大多数关于 AI Agent 是什么的定义都是基于对输出的期望或它的行为方式，而不是关注它实际是什么。

如果我问“什么是 LLM？”，我们会得到一个更令人接受的答案：

> 大语言模型 (LLM) 是一种 **AI 模型，具体来说是一种深度学习模型，它在大量的文本数据上进行训练。**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750505830733/b209c299-31cf-4b19-b28e-fc47f9f227a5.png?auto=compress,format&format=webp)

请注意，这个答案不是关于 LLM 生成下一个最可能的 token，而是更多关于它们从根本上是什么。对于 AI Agent，我们将在本文中解决这个问题。承诺够多了。让我们进入正题。

## 定义 AI Agent

让我们首先写一个可接受的 AI Agent 定义。我们在这篇文章中要做的就是将该定义分解成更小的部分，并理解每个部分：

Agent 是 **软件系统**，其中 **LLM** 使用推理来控制执行流程，**动态** 选择使用哪些 **工具**，并确定达到 **目标** 所需的每个步骤。

这太长了。让我们分解每个部分，以便我们真正理解它。

### Agent 是软件系统

这是第一个澄清，也是最简单的。当有人说“AI Agent”时，它应该在你脑海中浮现，它只是软件。对于一个简单的 Agent，它可能只是几个代码文件，仅此而已。我们称之为系统，是因为它包含不同的部分或模块，例如：

1.  LLM
2.  工作记忆或状态
3.  提示词 (Prompts)
4.  工具
5.  编排层

你已经知道 LLM 是什么了。当我们更深入地研究我们定义的其他部分时，AI Agent 的其他模块将自行显现。如果你还记不住这些，请不要担心。它们还会再次出现。

在我们的定义中，我们提到了动态的执行流程。让我们接下来看看这是什么意思。

### 动态执行流程

要执行任何任务，我们通常需要采取一个或多个步骤或行动。这些决策可以被认为是一个工作流程，或者是一组决定我们如何完成任务的规则。

让我们看一个例子。

假设你想创建一个客户成功机器人，它接收一个工单作为输入，然后回复创建者，并解决该工单，或者在需要时升级它。

请注意，解决或升级工单基本上是一个需要在某些外部 CRM 软件上执行的操作。我们的 LLM 程序应该能够处理这个问题。

我们现在不会深入讨论代码的具体样子。我创建了一个示例，如果你有兴趣可以查看。你可以使用像“langgraph”这样的库来实现这一点，并且图表或执行流程看起来像这样：

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750523331009/2478546b-8dd2-47d0-81fd-9b37556dafe9.png?auto=compress,format&format=webp)

> 你可能会注意到下面有一些代码示例。如果它们与你无关，请随时跳过它们并继续阅读

请注意，我们首先从对工单进行分类开始，这将由 LLM 提示词处理。接下来，我们生成初始回复，这是另一个 LLM 提示词。然后，我们检查是否需要升级。这可以通过 API 调用来完成，也可以通过使用静态代码来决定是否应该升级。最后，根据需要，我们可以升级工单并生成最终回复，让客户知道发生了什么。

```py
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

完整的代码可以在这里找到：<https://github.com/thesmallstar/AI-Agents-Under-the-hood-blog/blob/main/workflow.py>

这就是我们如何在 langgraph 中创建整个流程。我们从一个 StateGraph（参见上面示例的第一行）开始，并设置一个初始状态。然后，我们添加多个节点或逻辑块。如果需要，我们可以包含一个条件块，该块根据前一个节点的输出做出决策。

在上面的例子中，should\_escalate 的值，来自 check\_escalation 节点，用于决定我们接下来要去哪个图表或“工作流程”部分。

像“resolve ticket”这样的节点看起来像这样：

```py
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

请注意，我们首先调用 resolution API，然后运行提示词来生成工单的回复。

你可能已经猜到，我们可以完全控制程序的流程。我们可以准确地指定我们想要什么以及何时想要它。例如，第一步将始终是对工单进行分类，然后生成初始回复，然后按照一组固定的步骤或工作流程进行。这是一个工作流程系统，而不是一个 Agent。我们在这里缺少动态的执行流程，因为我们已经决定了每个步骤会发生什么。

让我们尝试为这个创建一个 Agent 式的流程 🫣。我们将使用 ReAct Agent 流程。如果这听起来很新鲜，请不要担心，我们很快会详细介绍它。我们将逐层揭开它，但首先，让我们看看它以及现有的抽象概念。

**顺便说一句，ReAct 代表“推理和行动”。**

这是一个流行的 Agent 流程，它让模型逐步推理，并选择何时以及如何行动（例如，通过调用工具）作为过程的一部分。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750524956830/946ad5ed-a30f-4883-9530-73be62fd190f.png?auto=compress,format&format=webp)

在我们的例子中：

**任务** 是解决或升级工单并给出回复。

在 **行动** 阶段，Agent 可以使用工具来分类、升级或解决工单。

在 **观察** 阶段，Agent 获得新的观察结果，这些是工具调用的输出，比如工单的分类是什么，或者升级是否成功。

在 **推理** 阶段，这基本上是 LLM“思考”它接下来应该做什么，Agent 可能必须决定是否调用工具、生成回复或检查观察阶段的输出。正如你可能预期的那样，推理阶段是这个循环开始的地方。

在这里注意到什么了吗？我们从未谈论过工作流程。我们从未以代码或静态流程的形式决定 LLM 何时应该使用工具、分类工单或解决工单。

为了进一步理解这一点，让我们看看可以用来做同样事情的代码。请注意，我们正在使用 CrewAI 库来实现这一点。还记得我们定义 Agent 是什么的时候吗：工具、LLM、提示词、记忆和一个编排层。CrewAI 是这里的编排层。它抽象掉了关于 Agent 如何进行工具调用、响应如何返回给 Agent 的大量细节，并添加了大量语法糖，使创建 Agent 变得更简单。这就是 Agent 在底层工作的所有魔法发生的地方。我们稍后将详细介绍这个编排层的职责，并看看有哪些流行的选项以及它们提供的功能。

**现在开始看代码：**

```py
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

完整的代码可以在这里找到：<https://github.com/thesmallstar/AI-Agents-Under-the-hood-blog/blob/main/agent.py>

好的，最初的观察很清楚。没有静态工作流程，只有动态工作流程。不是软件规定每个步骤，而是 LLM 决定每一步做什么。

**我们玩的小把戏**

但这里有一个有趣的小把戏：我们在 Task 的描述中说“遵循这个确切的工作流程”（这是 CrewAI 中的语法糖）。等等，那么它作为一个 Agent 的意义是什么？我们不是刚刚指示了确切的工作流程，但这次是用简单的英语？

**那不只是一个静态工作流程吗？**

嗯，是的，你做到了。但关键是，你不能总是这样做。并非所有问题都足够简单，可以成为一个五步过程，你可以准确地预测这些步骤将是什么以及按什么顺序进行。

例如，如果你使用过 Cursor 的 Agent 模式，你能说 Agent 总是先做 X 然后再做 Y 吗？不能。这取决于你的请求。在一个复杂的问题中，很难（如果不是不可能）编写一个固定的工作流程。

**真实世界的例子**

当我创建 [patra.app](http://patra.app)[,](https://patra.app) 时，它基本上是 Slack 上的一个 Jira Agent，用户可以提出的查询种类有无数种可能性。

示例：  
为这个线程创建一张 Jira 工单，将其分配给 ManthanSurkar，添加一个标签 Y，并将优先级设置为 Z。

想象一下尝试在一个静态工作流程中做这件事。将涉及多个步骤。首先，检查 Slack 消息中是否标记了用户。如果标记了，找到他们的电子邮件，等等。我们不要陷入细节。

现在想象一个像这样的动作：  
检查我的 Google 日历，并为昨天晚上发生的事件中的行动项创建一张 Jira 工单。

这些是复杂的、真实世界的场景。为每个场景编写一个特定的工作流程很难。这就是为什么 AI Agent 具有动态的执行流程。

**不要过度复杂化简单的事情**

哇，太棒了！我们总是有一个动态流程怎么样...

停。不。不要犯那个错误。当你能够确定时，为什么要向你的软件应用程序添加一层不确定性呢？这份工作还不够难吗，你还想引入一个不确定性的 AI 模型？

Agent 是为复杂的问题而设计的，而不是那些你已经知道解决方案并可以将其记为工作流程的问题。不要让你的生活复杂化。除非你只是想过度设计东西。我承认，这很有趣。

在真实世界的场景中，通常会使用两种方法的混合。例如，想象一下你有三个支持 Agent，每个 Agent 专门负责不同的产品。根据工单链接到哪个产品，你可以选择合适的 Agent 并将请求路由到该 Agent。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750586210175/09c85433-260c-4dbf-bc87-b2ff4b356c2f.png?auto=compress,format&format=webp)

**接下来是什么？**

到目前为止，我们将工具和编排框架保持为一个黑盒。那些到底是什么？LLM 如何调用工具？工具到底是什么？让我们在下一节中介绍所有这些术语的“底层”。

**工具 & 编排框架**

LLM 预测下一个 token。你现在已经听过这句话一百万次了。如果是这样，它如何仅通过预测 token 来调用工具？嗯，实际上，它并没有。LLM 只是表明它想使用一个工具，然后等待编排框架来弄清楚它应该调用哪个工具，实际执行调用，然后让 LLM 知道，“嘿，工具被调用了，这是输出。”

**一个简单的例子**

让我们用一个简单的程序来分解这一点。

假设我们想根据用户的自然语言消息来加或减两个数字。由于我们处理的是自然语言，我们可以使用 LLM。但是加两个数字是一个已经解决的问题，我们应该能够确定地做到这一点，对吗？这正是工具的用武之地。

**为什么要使用工具？**

工具让 LLM 可以通过 API 与其他系统通信。它们还可以让 LLM 与其他 Agent 通话（为多 Agent 系统敲鼓），或者执行确定性任务，比如加两个数字。

**定义一个工具**

让我们定义我们的工具的外观：

```py
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

请注意，我们定义了两个 Python 函数。它们可以执行计算的确定性任务。提示词让 LLM 知道它可以调用上面的函数。如果 LLM 想要使用这些工具中的任何一个，它会以特定的格式给我们输出，我们可以“解析”并识别需要调用哪个函数。一旦调用完成，我们会让 LLM 知道答案，并允许它继续执行。

**“继续对话”是什么意思？**

它只是添加一条新消息，说明工具调用已成功，输出为 X，或者让 LLM 知道工具调用失败了。接下来会发生什么？我们让 LLM 做它的工作，生成下一个 token，但现在加入了工具调用的输出。

**基本上就是这样。**

这就是工具调用在底层的工作方式。有一个解析器，在我们的例子中，这是一个解析函数的样子：

```py
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

完整的代码可以在这里找到：<https://github.com/thesmallstar/AI-Agents-Under-the-hood-blog/blob/main/tool.py>

然后是 **invoke** 方法。这允许你将工具调用的响应合并回原始消息集，因此 LLM 可以生成包含此额外信息的下一个 token。

```py
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

你知道我们刚刚做了什么吗？我们构建了一个迷你 Agent 框架。这个框架是更复杂系统中底层工作方式的过度简化版本。它们都有解析层来弄清楚下一个行动应该是什么。是工具调用吗？应该由另一个 Agent 继续执行吗？等等。

今天，OpenAI 和 Anthropic 都在他们的 SDK 中支持开箱即用的工具调用。你可以在这里了解更多关于 OpenAI 的新 Responses API 及其对函数调用的支持：<https://platform.openai.com/docs/quickstart?api-mode=responses>

**探索流行的 Agent 框架**

一些流行的 Agent 框架包括 -

*   **CrewAI** – 一个用于协调多个 Agent 作为团队的 Python 框架。  
    阅读更多：[Github 上的 CrewAI](https://github.com/crewAIInc/crewAI)
*   **OpenAI Agents SDK** – 一个用于构建和连接 Agent 的轻量级工具包，具有内置的跟踪和防护措施。  
    阅读更多：[OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/)
*   **MetaGPT** – 一个多 Agent 系统，通过将产品经理和开发人员等角色分配给不同的 Agent 来模拟软件团队。  
    阅读更多：[GitHub 上的 MetaGPT](https://github.com/FoundationAgents/MetaGPT)

现在你已经知道什么是工具和框架了，探索流行的选项是有意义的。请记住，每个选项都有自己的语法糖，用于定义工具、设置 Agent 的不同方面或描述其目标和角色。

**等等，角色？**

这是新的。为什么 Agent 需要一个角色？角色到底是什么？

如果你仔细想想，拥有一个特定的角色有助于 Agent 专注于其目标，并就使用哪些工具做出更好的决策。这在不同的 Agent 相互交互的多 Agent 系统中尤其重要。一个复杂的问题可以通过一个多 Agent 系统来解决，其中每个 Agent 都有不同的角色。

**接下来：多 Agent 系统**

在下一节中，让我们更多地谈谈多 Agent 框架，以及为什么我们可能需要多个 Agent 协同工作才能完成任务。

现在我们了解了什么是 Agent，正如你可能预期的那样，多 Agent 系统只是多个协同工作的 Agent。

**请记住，Agent 只是：**

*   一个可以访问工具的 LLM
*   一组提示词（如角色、目标等）
*   记忆（我们稍后会谈到）
*   所有这些都是使用编排框架构建的，以便一切协同工作

但是，在一个系统中拥有多个 Agent 实际上意味着什么？他们如何沟通？嗯，这取决于编排框架。例如，CrewAI 允许在多 Agent 系统中进行两个主要操作。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750530783347/e075dac0-4879-4b27-9505-2d6446ff99ed.png?auto=compress,format&format=webp)

*来源：[CrewAI 协作概念](https://docs.crewai.com/concepts/collaboration)*

所有其他 Agent 都作为工具添加。当前 Agent 可以向专家 Agent 提问，或者将任务委派给该 Agent，假设它可以接管该责任。

**为什么要使用多 Agent 系统？**

多 Agent 系统有助于组织任务并将它们分解成更小的问题。每个问题都可以由一个单独的专家 Agent 解决，该 Agent 可以访问特定的工具和特定的角色，就像一个团队在做一个项目一样。正如 Anthropic 在他们的关于多 Agent 系统的[博客文章](https://www.anthropic.com/engineering/built-multi-agent-research-system) 中指出的那样，另一个优点是，在处理复杂问题时，你可以使用更多的 token（因此系统可以“思考更多”）。

在上面的例子中，提问意味着从新的工作记忆（聊天历史）开始，它可以扩展到数万个 token，并在主 Agent 继续其工作之前回答一个特定的查询。

你可以在稍后[这里](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)阅读关于不同类型的多 Agent 系统。

**警告：** 正如你可能预期的那样，多 Agent 系统是复杂的，难以调试，并且难以评估。我认为从一个工作流程开始是一个好主意。如果执行流程变得复杂，那么尝试构建一个 Agent。如果它仍然很复杂，并且你遇到了诸如上下文窗口限制之类的问题，那么考虑使用一个多 Agent 框架。不要使用超过你实际需要的复杂性或能力。

我们已经接触了 AI Agent 的所有方面，除了记忆。让我们现在深入研究这个。

在许多情况下，在你的系统变得足够复杂之前，或者除非你使用的是依赖于某种形式的记忆的 Agent 框架，否则你不需要太关心 Agent 的记忆方面。

AI Agent 可能有两种形式的记忆，就像人类一样：

短期记忆让 LLM 可以跟踪正在发生的最新或活跃的对话。例如，当一个 Agent 决定进行工具调用时，它不会忘记在工具被触发之前发生的任何事情。对话不会重新开始；它会从它离开的地方继续。简而言之，LLM 的上下文窗口中的任何内容都是它的短期记忆。有时，如果上下文窗口不够长，无法容纳所有内容，我们可以总结较旧的消息，并保持最新的消息不变。

这是一个例子。假设你正在使用 AI Agent 进行复杂的数学运算，但你只有一个小的上下文窗口：

M1：用户：执行 10 + 20 + 30 + 40 + 50  
M2：LLM：*工具调用，10 + 20*  
M3：用户：输出 30  
M4：LLM：*当前答案是 30，让我们继续。工具调用 30 + 30*  
M5：用户：输出 60  
M6：LLM：*当前答案是 60，让我们继续。工具调用 60 + 40*

在这一点上，我们可以将 M2 到 M4 总结甚至消除成一行，比如 M2'：

M1：用户：执行 10 + 20 + 30 + 40 + 50  
M2'：用户：10 + 20 + 30 的输出是 60，继续。  
M6：LLM：当前答案是 60，让我们继续。工具调用 60 + 40

请注意，我们是如何压缩这些信息而没有丢失任何重要内容。这是一个非常简化的例子，但在更复杂的情况下，事情可能会变得棘手。确保正确的事情留在 Agent 的短期记忆中可能是一个真正的挑战。

有时，你甚至可能不总结，而只是忽略较旧的消息。Agent 的短期记忆的实现和使用可能会有所不同，这取决于你试图解决的问题。

我们还提到，一个 Agent 式的框架可能依赖于短期记忆。一个例子是 RAISE 框架，它是我们之前看到的 ReAct 框架的扩展。  
**RAISE 代表通过草稿纸和例子进行推理和行动。** 草稿纸存在于 Agent 的短期记忆中，并在执行期间使用。另一方面，例子是长期记忆。

在这里阅读介绍 RAISE 框架的论文：<https://arxiv.org/pdf/2401.02777>

长期记忆是 Agent 在多次对话中记住的内容。如果你使用过 ChatGPT 并尝试过记忆功能，那就像系统的长期记忆。当你进行对话时，系统会存储相关信息，以便以后检索，从而为你提供更好的答案。这就是长期记忆在起作用。

在我们之前关于客户成功机器人的例子中，你可以存储以前回答的工单，无论是人工回答还是 Agent 回答，然后检索相关的例子，以帮助更好地回答当前的工单。这是长期记忆的使用，它通常通过工具调用来访问。工具调用可以是一个简单的数据库查询，也可以是一个 RAG 系统，该系统有助于检索存储在持久存储中的记忆。

请注意，为了使长期记忆真正有用，它需要出现在工作记忆或短期记忆中，在那里它将被使用并在生成下一个 token 时被考虑。

## 用于操作 Agent 的心理模型

这有很多理论和底层信息。我希望你带着一个我在开发 Agent 或任何 LLM 应用程序时使用的实用心理模型离开。这就是我如何使 [patra.app](http://patra.app) 可靠地工作，以及我如何发布多个其他生产系统。

**黄金模型：**  
把自己放在 Agent 的位置。想象一下你就是那个 Agent。

这听起来可能很老套。但是“成为那个 Agent”到底意味着什么？LLM 不是魔法。如果一个人无法弄清楚如何在特定情况下继续进行，那么 Agent 很可能也无法做到。假设你正在构建一个编码 Agent，并且你给它一个修复错误的任务。

把自己放在 Agent 的位置。想象一下面对一个有 1000 个文件的代码库。它怎么知道从哪里开始？它没有业务上下文，也没有代码上下文。当你对 Agent 产生这种共情时，你就会停止相信它们是某种魔杖。你会写更好的目标，提供更多的上下文，并添加更多的工具。在相同的情况下，完全按照你或人类会做的那样做。Agent 是否拥有人类需要的一切？

现在，不要从字面上理解这一点并过度复杂化一切。关键是培养对 Agent 的共情。当你这样做时，你的 Agent 设计总会改进。

希望你现在明白 AI Agent 不是魔法。它们只是具有正确设置的智能系统：LLM、记忆、工具、一些编排和一个用于解决实际问题的好心理模型。炒作是合理的，但现实比大多数人意识到的更简单和更实用。

如果你只带走一件事，那就让它成为：构建有效的 AI Agent 关乎清晰性、共情和结构。像对待新队友一样对待你的 Agent。给它上下文、明确的目标和正确的工具。不要指望它读懂你的心思。

这个领域仍然有很多发展。新的框架正在出现，新的记忆方法正在测试中，并且多 Agent 协作变得更具创造性。但是，如果你理解了基础知识，你已经领先于大多数人。因此，下次有人在谈话中提到“AI Agent”时，你不仅会知道它是什么，还会知道它是如何思考和工作的。

如果你遇到任何问题，只需问自己：如果我是 Agent，我需要什么才能成功？这就是真正的魔法发生的地方。