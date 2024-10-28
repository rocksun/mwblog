
<!--
title: 通过调整 LLM 提示定义 AI 代理角色
cover: https://cdn.thenewstack.io/media/2024/10/85a92b5b-alyssa-smith-i60ysjyl9ai-unsplashb.jpg
-->

在 AI 代理开发中，您可以使用可用于大型语言模型 (LLM) 和视觉语言模型 (VLM) 的系统提示，为代理添加角色。

> 译自 [How To Define an AI Agent Persona by Tweaking LLM Prompts](https://thenewstack.io/how-to-define-an-ai-agent-persona-by-tweaking-llm-prompts/)，作者 Janakiram MSV。

在 [AI 代理：面向开发人员的全面介绍](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 中，我通过将 AI 代理与组织中的员工进行比较，介绍了 AI 代理的关键特征。在本文中，我们将探讨如何利用 [大型语言模型](https://thenewstack.io/llm/) (LLM) 和 [视觉语言模型](https://thenewstack.io/vision-foundation-models-when-does-size-matter/) (VLM) 的系统提示来为代理添加角色。

## 了解系统提示

系统 [提示](https://thenewstack.io/prompt-engineering-get-llms-to-generate-the-content-you-want/)，也称为系统角色，是 LLM 的基础指令层。它们为模型在整个交互过程中应如何表现提供上下文和指南。与每次查询都会改变的用户提示不同，系统提示在整个对话中都保持不变——确保 AI 的行为和响应的一致性。

系统提示的关键功能包括：

- 定义 AI 的专业知识和知识领域
- 设置沟通的语气和风格
- 建立行为边界和道德准则
- 增强特定任务的性能

## 使用 Anthropic 的 Claude API 实现系统提示

[Anthropic 的 Claude API](https://www.anthropic.com/api) 允许开发人员使用请求主体中的 `system` 参数指定系统提示。此参数为整个对话设置上下文，并塑造 Claude 的响应。

以下是如何为 Claude 设置系统提示的示例：

```python
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1000,
    system="You are a knowledgeable data scientist specializing in machine learning algorithms.",
    messages=[
        {"role": "user", "content": "Explain the differences between supervised and unsupervised learning."}
    ]
)
print(response.content[0].text)
```

此处代码通过系统角色建立了知识渊博的数据科学家的语气和领域。Claude 扮演了机器学习专家数据科学家的角色。

此系统提示将影响其对相关主题的用户查询的响应，确保提供的信息与数据科学专业人士的观点相关且一致。

## OpenAI API 中的系统提示

[OpenAI 的 GPT API](https://openai.com/index/openai-api/) 同样允许指定系统提示。系统消息通常是对话中的第一条消息，并为助手设置行为。

以下是如何使用 OpenAI API 的示例：

```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant specializing in creative writing techniques."},
        {"role": "user", "content": "Can you explain the concept of 'show, don't tell' in writing?"}
    ]
)
print(response.choices[0].message.content)
```

在这种情况下，GPT 模型扮演了创意写作专家的角色，这将指导其对写作相关查询的响应。

## 编写有效的系统提示

要创建对 AI 代理设置正确角色有影响力的系统提示，请考虑以下指南：

- **具体详细**：清楚地定义代理的专业领域、背景以及任何相关的限制。
- **使用强烈的情态动词**：使用诸如“必须”或“应该”之类的指示性语言来强化重要的行为准则。
- **建立边界**：清楚地说明 AI 代理可以做什么和不能做什么，以防止它越过其预期角色。
- **融入个性特征**：定义代理的沟通风格、正式程度以及任何塑造其角色的独特特征。

## 系统提示在 AI 代理开发中的重要性

AI 代理的角色可以比作员工的职位描述或工作职能。它清楚地定义了特定工作的角色、边界和期望。系统提示为 AI 代理带来了类似的功能。

对于开发人员来说，系统提示是创建专门 AI 代理的强大工具。它们允许您：

- **创建一致的角色**：通过定义明确的角色和特征集，您可以确保您的 AI 代理在所有交互中保持一致的个性。
- **专业化领域**：您可以创建在特定领域拥有专业知识的代理，这些代理配备了该领域问题的适当知识和方法。
- **执行道德准则**：系统提示可以包含有关 AI 应该或不应该做什么的规则，有助于创建更负责任和值得信赖的 AI 代理。
- **提高响应质量**：精心设计的系统提示可以引导 AI 为用户查询提供更相关、准确和有用的响应。

## 将系统提示映射到 AI 代理

通过仔细设计系统提示，开发人员可以创建具有不同角色的 AI 代理，这些角色针对特定用例量身定制。以下是一些示例：

```
System：您是一位经验丰富的财务顾问，拥有个人理财、投资策略和退休规划方面的专业知识。提供清晰、可操作的建议，同时始终强调个人情况和风险承受能力的重要性。切勿推荐特定股票或承诺回报。始终鼓励用户咨询持牌专业人士以获取个性化建议。
```

```
System：您是主要电子商务平台的友好高效的客户支持代表。您的目标是协助客户进行订单查询、退货和一般产品信息。始终保持礼貌和耐心的态度，使用积极的语言，并努力以最令人满意的方式解决问题。如果您无法解决问题，请向客户保证您会将其升级到相应的部门。
```

```
System：您是一位经验丰富的语言导师，专门教授非母语人士英语。您的方法是耐心、鼓励和适应不同的学习风格。清楚地解释语法规则，提供相关示例，并建议实际练习。如果需要，准备好多次澄清概念，并始终赞扬学习者为他们的努力和进步。
```

## 使用系统提示定义 AI 代理的角色

为了使用系统提示实现 AI 代理，我们可以创建一个封装代理行为的 Python 类。

让我们看一下使用 OpenAI 的 GPT-4o 模型使用系统提示的 AI 代理的实际实现：

```python
import os
from openai import OpenAI

class Agent:
    def __init__(self, name: str):
        self._name = name
        self._persona = ""
        self._api_key = os.getenv('OPENAI_API_KEY', '')
        self._model = "gpt-4"

    @property
    def name(self):
        return self._name

    @property
    def persona(self):
        return self._persona

    @persona.setter
    def persona(self, value: str):
        self._persona = value

    def execute(self, task: str) -> str:
        if not self._api_key:
            return "API key not found. Please set the OPENAI_API_KEY environment variable."
        client = OpenAI(api_key=self._api_key)
        try:
            response = client.chat.completions.create(
                model=self._model,
                messages=[
                    {"role": "system", "content": self.persona},
                    {"role": "user", "content": task}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Create a financial advisor agent
    financial_advisor = Agent("FinancialAdvisorBot")
    financial_advisor.persona = """You are an experienced financial advisor with expertise in personal finance, investment strategies, and retirement planning. Provide clear, actionable advice while always emphasizing the importance of individual circumstances and risk tolerance. Never recommend specific stocks or make promises about returns. Always encourage users to consult with a licensed professional for personalized advice."""

    # Execute a task
    task = "What are some key considerations for planning retirement in your 30s?"
    response = financial_advisor.execute(task)
    print(f"Agent Name: {financial_advisor.name}")
    print(f"Agent Persona: {financial_advisor.persona}")
    print(f"\nTask: {task}")
    print(f"Agent Response:\n{response}")

    # Execute another task with the same persona
    task = "Explain the pros and cons of index fund investing for a beginner"
    response = financial_advisor.execute(task)
    print(f"\nNew Task: {task}")
    print(f"Agent Response:\n{response}")
```

在此实现中：

- `Agent` 类定义了一个 `persona` 属性，该属性表示系统提示。
- `execute` 方法接受一个任务（用户输入）并将其与系统提示一起发送到 OpenAI API。
- 然后返回 API 响应，表示代理对任务的响应。

这种结构允许轻松创建具有不同角色的各种 AI 代理，每个代理都针对特定领域或用例量身定制。

我们构建的类是为在接下来的教程中添加关键特征和属性奠定基础。本教程的重点是添加角色，同时允许用户向代理发送查询。在下一教程中，我们将探讨向代理添加指令、任务和规划策略，从而提高执行效率。
