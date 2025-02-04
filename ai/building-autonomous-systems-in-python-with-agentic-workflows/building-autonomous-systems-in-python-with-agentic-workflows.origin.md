# Building Autonomous Systems in Python with Agentic Workflows
![Featued image for: Building Autonomous Systems in Python with Agentic Workflows](https://cdn.thenewstack.io/media/2025/01/4bc6987a-flows-1024x576.jpg)
As businesses and technology push boundaries, staying ahead often means finding more innovative, faster ways to get work done. Enter [agentic workflows](https://thenewstack.io/the-architects-guide-to-understanding-agentic-ai/), a revolutionary approach to task automation that empowers systems to analyze, decide and execute tasks independently. Agentic workflows are not just another tech buzzword; they are about [enabling automation](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/) that doesn’t just follow a script but adapts in real time to handle complex challenges.

Traditional automation tools follow predefined steps. They’re effective for routine, repetitive work but falter when faced with dynamic, evolving tasks. This is where agentic workflows stand out. They combine flexibility and intelligence to manage complex operations with minimal manual input. By incorporating tools like [large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms), [APIs](https://thenewstack.io/api-management/) and other external resources, these workflows act as intelligent agents capable of solving problems, streamlining processes and driving efficiency at a higher level.

For most organizations, this is a game-changer. Agentic workflows can reduce repetitive workloads, reduce error rates and speed up decision-making. When deployed effectively, they drive innovation, allowing teams to focus on high-value tasks while autonomous systems handle the details. To put it simply, agentic workflows make your organization more agile, adaptive and future-ready.

**What Are Agentic Workflows?**
Agentic workflows are [systems composed of autonomous agents working](https://thenewstack.io/putting-ai-to-work-systems-of-intelligence-and-actionable-agency/) collaboratively to achieve specific goals. Each agent in the workflow is designed to:

- Perceive its environment or context.
- Make decisions based on predefined rules or models.
- Execute tasks, often by interacting with external APIs or systems.
**Key Benefits:**
- Automation: Reduce manual effort by delegating tasks to agents.
- Adaptability: Agents can dynamically adjust to changing requirements or input.
- Efficiency: Optimize multistep tasks by intelligently delegating subtasks.
**Common Use Cases:**
- Customer support bots with escalation workflows.
- Autonomous research assistants that retrieve, analyze and summarize information.
- Workflow orchestration for IoT devices in smart homes.
**Step 1: Setting Up the Environment**
Before you begin building your agentic workflow, ensure the required tools are installed. We’ll use OpenAI for natural language processing and Langchain for workflow orchestration.

**Install Dependencies:**
`pip install openai langchain requests`
**Configure OpenAI API Key:**
Store your API key securely using environment variables:

1234 |
import os# Set your OpenAI API keyos.environ["OPENAI_API_KEY"] = "your_openai_api_key" |
**Step 2: Designing the Workflow**
For this tutorial, we’ll build an autonomous research agent workflow. The workflow involves:

- Accepting a research topic as input.
- Retrieving relevant web articles using an external API.
- Summarizing the content.
- Storing the results in a local file.
**Step 3: Creating the Agent Framework**
Agents need a core structure to perceive, decide and act. Let’s build this framework step by step.

**Basic Agent Class**
Define a reusable `Agent`
class that all agents will inherit.

123456789101112131415 |
class Agent: def __init__(self, name): self.name = name def perceive(self, input_data): """Receive input from the environment.""" raise NotImplementedError("Perceive method must be implemented.") def decide(self): """Make decisions based on perceived input.""" raise NotImplementedError("Decide method must be implemented.") def act(self): """Perform an action based on the decision.""" raise NotImplementedError("Act method must be implemented.") |
**Step 4: Implementing Specialized Agents**
We will create three specialized agents:

- Input agent: Accepts the research topic.
- Retrieval agent: Fetches articles from an API.
- Summarization agent: Summarizes the content.
**Input Agent**
This agent takes a research topic as input.

12345678910 |
class InputAgent(Agent): def perceive(self, input_data): self.topic = input_data def decide(self): return f"Proceeding with research on: {self.topic}" def act(self): print(self.decide()) return self.topic |
**Retrieval Agent**
This agent uses an external API (such as a mock news API) to fetch articles.

123456789101112131415161718192021 |
class RetrievalAgent(Agent): def __init__(self, name, api_url): super().__init__(name) self.api_url = api_url def perceive(self, topic): self.topic = topic def decide(self): query_params = {"q": self.topic, "apiKey": "your_api_key"} return requests.get(self.api_url, params=query_params) def act(self): response = self.decide() if response.status_code == 200: articles = response.json().get("articles", []) print(f"Retrieved {len(articles)} articles.") return articles else: print("Failed to retrieve articles.") return [] |
**Summarization Agent**
This agent uses OpenAI’s API to summarize the content.

1234567891011121314151617181920212223 |
import openaiclass SummarizationAgent(Agent): def perceive(self, articles): self.articles = articles def decide(self): summaries = [] for article in self.articles: prompt = f"Summarize the following article:\n\n{article['content']}" response = openai.Completion.create( model="text-davinci-003", prompt=prompt, max_tokens=100 ) summaries.append(response.choices[0].text.strip()) return summaries def act(self): summaries = self.decide() for idx, summary in enumerate(summaries): print(f"Summary {idx + 1}: {summary}") return summaries |
**Step 5: Orchestrating the Workflow**
Now, let’s integrate the agents into an orchestrated workflow.

12345678910 |
class Workflow: def __init__(self, agents): self.agents = agents def run(self, input_data): current_data = input_data for agent in self.agents: agent.perceive(current_data) current_data = agent.act() print("Workflow completed.") |
**Instantiate Agents and Run the Workflow**
123456789101112131415 |
# Define the API URL for article retrievalapi_url = "https://newsapi.org/v2/everything"# Create agentsinput_agent = InputAgent(name="InputAgent")retrieval_agent = RetrievalAgent(name="RetrievalAgent", api_url=api_url)summarization_agent = SummarizationAgent(name="SummarizationAgent")# Orchestrate workflowagents = [input_agent, retrieval_agent, summarization_agent]research_workflow = Workflow(agents)# Run the workflowtopic = "AI in Healthcare"research_workflow.run(topic) |
**Step 6: Enhancing the Workflow**
You can extend the functionality of this workflow by:

**Adding file storage:** Save the summarized content to a text file.
123456789101112 |
class FileStorageAgent(Agent): def perceive(self, summaries): self.summaries = summaries def decide(self): return "Summaries saved to research_summaries.txt." def act(self): with open("research_summaries.txt", "w") as file: for summary in self.summaries: file.write(summary + "\n\n") print(self.decide()) |
Add this agent to the workflow:
12 |
file_storage_agent = FileStorageAgent(name="FileStorageAgent")agents.append(file_storage_agent) |
**Error handling**: Implement exception handling for API errors and empty responses.
**Parallel processing**: Use Python’s `asyncio`
to process multiple articles concurrently.
**Step 7: Testing and Debugging**
Test the workflow with various topics to ensure robustness:

- Handle topics with no articles available.
- Test with diverse inputs to verify agent adaptability.
- Log errors for easier debugging.
**Conclusion**
Agentic workflows offer a practical approach to creating smart, task-oriented systems. By breaking tasks into specialized components, you can build scalable, flexible solutions for handling complex processes.

By following this step-by-step guide, you’ve mastered the basics of designing and implementing agentic workflows with Python. From setting up individual agents to coordinating them into a unified system, you now have the tools to develop autonomous workflows that fit your specific needs.

Take the next step by experimenting with more advanced agents, integrating additional tools and APIs, and refining decision-making processes to maximize the potential of these workflows.

Revolutionize the way you work with cutting-edge AI innovation. Explore Andela’s definitive guide “[3 AI tools transforming productivity](https://www.andela.com/blog-posts/3-ai-tools-to-boost-your-productivity-4x/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack-agentic&utm_content=writers-room-sowole&utm_term=ai-tools).”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)