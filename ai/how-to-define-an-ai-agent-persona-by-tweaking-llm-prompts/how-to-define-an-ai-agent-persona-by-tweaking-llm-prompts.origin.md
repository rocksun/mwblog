# How To Define an AI Agent Persona by Tweaking LLM Prompts
![Featued image for: How To Define an AI Agent Persona by Tweaking LLM Prompts](https://cdn.thenewstack.io/media/2024/10/85a92b5b-alyssa-smith-i60ysjyl9ai-unsplashb-1024x576.jpg)
In [AI Agents: A Comprehensive Introduction for Developers](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/), I introduced the key traits of AI agents by comparing them to an employee working in an organization. In this article, we will explore how to add a persona to an agent by taking advantage of the system prompts available for [large language models](https://thenewstack.io/llm/) (LLM) and [vision language models](https://thenewstack.io/vision-foundation-models-when-does-size-matter/) (VLM).

## Understanding System Prompts
System [prompts](https://thenewstack.io/prompt-engineering-get-llms-to-generate-the-content-you-want/), also known as system roles, serve as a foundational layer of instruction for LLMs. They provide context and guidelines for how the model should behave throughout an interaction. Unlike user prompts, which change with each query, system prompts persist across the entire conversation — ensuring consistency in the AI’s behavior and responses.

Key functions of system prompts include:

- Defining the AI’s expertise and knowledge domain
- Setting the tone and style of communication
- Establishing behavioral boundaries and ethical guidelines
- Enhancing task-specific performance
## Implementing System Prompts With Anthropic’s Claude API
[Anthropic’s Claude API](https://www.anthropic.com/api) allows developers to specify a system prompt using the `system`
parameter in the request body. This parameter sets the context for the entire conversation and shapes Claude’s responses.
Here’s an example of how to set a system prompt for Claude:

1234567891011121314 |
import anthropicclient = anthropic.Anthropic()response = client.messages.create( model="claude-3-5-sonnet-20241022", max_tokens=1000, system="You are a knowledgeable data scientist specializing in machine learning algorithms.", messages=[ {"role": "user", "content": "Explain the differences between supervised and unsupervised learning."} ])print(response.content[0].text) |
Here the code establishes the tone and domain of a knowledgeable data scientist through the system role. Claude assumed the persona of a data scientist with expertise in machine learning.
This system prompt will influence its responses to user queries about related topics, ensuring that the information provided is relevant and aligned with the perspective of a data science professional.

## System Prompts in OpenAI’s API
[OpenAI’s GPT API](https://openai.com/index/openai-api/) similarly allows for the specification of system prompts. The system message is typically the first message in the conversation and sets the behavior for the assistant.
Here’s an example using OpenAI’s API:

12345678910111213 |
from openai import OpenAIclient = OpenAI()response = client.chat.completions.create( model="gpt-4o", messages=[ {"role": "system", "content": "You are a helpful assistant specializing in creative writing techniques."}, {"role": "user", "content": "Can you explain the concept of 'show, don't tell' in writing?"} ])print(response.choices[0].message.content) |
In this case, the GPT model takes on the persona of a creative writing expert, which will guide its responses to writing-related queries.
## Crafting Effective System Prompts
To create an impactful system prompt that sets the right persona for an AI agent, consider the following guidelines:

**Be specific and detailed:**Clearly define the agent’s area of expertise, background, and any relevant limitations.**Use strong modal verbs:**Employ instructive language like “must” or “should” to reinforce important behavioral guidelines.**Establish boundaries:**Clearly state what the AI agent can and cannot do, to prevent it from overstepping its intended role.**Incorporate personality traits:**Define the agent’s communication style, level of formality, and any unique characteristics that will shape its persona.
## The Significance of System Prompts in AI Agent Development
The persona of an AI agent can be compared to the job description or job function of an employee. It clearly defines the role, boundaries and expectations of a specific job. System prompts induce similar capabilities to an AI agent.

For developers, system prompts are a powerful tool for creating specialized AI agents. They allow you to:

**Create Consistent Personas:**By defining a clear role and set of characteristics, you ensure that your AI agent maintains a consistent personality across interactions.**Specialize in Domains:**You can create agents that are experts in specific fields, equipped with the appropriate knowledge and approach to problems in that domain.**Enforce Ethical Guidelines:**System prompts can include rules about what AI should or should not do, helping to create more responsible and trustworthy AI agents.**Improve Response Quality:**A well-crafted system prompt can guide the AI to provide more relevant, accurate, and helpful responses to user queries.
## Mapping System Prompts to AI Agents
By carefully crafting system prompts, developers can create AI agents with distinct personas tailored to specific use cases. Here are some examples:

`System: You are an experienced financial advisor with expertise in personal finance, investment strategies, and retirement planning. Provide clear, actionable advice while always emphasizing the importance of individual circumstances and risk tolerance. Never recommend specific stocks or make promises about returns. Always encourage users to consult with a licensed professional for personalized advice.`
`System: You are a friendly and efficient customer support representative for a major e-commerce platform. Your goal is to assist customers with order inquiries, returns, and general product information. Always maintain a polite and patient demeanor, use positive language, and aim to resolve issues in the most satisfactory way possible. If you cannot solve a problem, assure the customer that you will escalate it to the appropriate department.`
`System: You are an experienced language tutor specializing in teaching English to non-native speakers. Your approach is patient, encouraging, and adaptable to different learning styles. Provide clear explanations of grammar rules, offer relevant examples, and suggest practical exercises. Be prepared to clarify concepts multiple times if needed, and always praise learners for their efforts and progress.`
## Defining the Persona of AI Agents With System Prompts
To implement an AI agent using system prompts, we can create a Python class that encapsulates the agent’s behavior.

Let’s look at a practical implementation of an AI agent using system prompts with OpenAI’s GPT-4o model:

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566 |
import osfrom openai import OpenAIclass Agent: def __init__(self, name: str): self._name = name self._persona = "" self._api_key = os.getenv('OPENAI_API_KEY', '') self._model = "gpt-4" @property def name(self): return self._name @property def persona(self): return self._persona @persona.setter def persona(self, value: str): self._persona = value def execute(self, task: str) -> str: if not self._api_key: return "API key not found. Please set the OPENAI_API_KEY environment variable." client = OpenAI(api_key=self._api_key) try: response = client.chat.completions.create( model=self._model, messages=[ {"role": "system", "content": self.persona}, {"role": "user", "content": task} ] ) return response.choices[0].message.content except Exception as e: return f"An error occurred: {str(e)}"# Example usageif __name__ == "__main__": # Create a financial advisor agent financial_advisor = Agent("FinancialAdvisorBot") financial_advisor.persona = """You are an experienced financial advisor with expertise in personal finance, investment strategies, and retirement planning. Provide clear, actionable advice while always emphasizing the importance of individual circumstances and risk tolerance. Never recommend specific stocks or make promises about returns. Always encourage users to consult with a licensed professional for personalized advice.""" # Execute a task task = "What are some key considerations for planning retirement in your 30s?" response = financial_advisor.execute(task) print(f"Agent Name: {financial_advisor.name}") print(f"Agent Persona: {financial_advisor.persona}") print(f"\nTask: {task}") print(f"Agent Response:\n{response}") # Execute another task with the same persona task = "Explain the pros and cons of index fund investing for a beginner" response = financial_advisor.execute(task) print(f"\nNew Task: {task}") print(f"Agent Response:\n{response}") |
In this implementation:
- The
`Agent`
class is defined with a persona property that represents the system prompt. - The
`execute`
method takes a task (user input) and sends it to the OpenAI API along with the system prompt. - The API response is then returned, representing the agent’s response to the task.
This structure allows for the easy creation of various AI agents with different personas, each tailored to a specific domain or use case.

The`Agent`
class we built acts as the foundation for adding key traits and attributes to it in the upcoming tutorials. The focus of this tutorial is adding the persona while letting the user send a query to the agent. In the next tutorial, we will look at adding instructions, tasks and planning strategies to an agent, which improves the efficiency of the execution.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)