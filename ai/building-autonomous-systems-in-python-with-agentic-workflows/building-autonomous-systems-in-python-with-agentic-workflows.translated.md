# 使用 Agentic 工作流在 Python 中构建自主系统

![Featued image for: Building Autonomous Systems in Python with Agentic Workflows](https://cdn.thenewstack.io/media/2025/01/4bc6987a-flows-1024x576.jpg)

随着企业和技术的不断发展，保持领先地位往往意味着寻找更具创新性、更快捷的工作方式。[Agentic 工作流](https://thenewstack.io/the-architects-guide-to-understanding-agentic-ai/)应运而生，这是一种革命性的任务自动化方法，使系统能够独立地分析、决策和执行任务。Agentic 工作流不仅仅是另一个技术流行语；它们关乎[实现自动化](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/)，这种自动化不仅遵循脚本，而且能够实时适应以应对复杂的挑战。

传统的自动化工具遵循预定义的步骤。它们对于常规的、重复性的工作非常有效，但在面对动态的、不断变化的任务时却力不从心。这就是 Agentic 工作流脱颖而出的地方。它们结合了灵活性和智能性，能够以最少的人工干预来管理复杂的操作。通过结合[大型语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms)、[API](https://thenewstack.io/api-management/)和其他外部资源等工具，这些工作流充当能够解决问题、简化流程和提高效率的智能代理。

对于大多数组织而言，这是一个改变游戏规则的方法。Agentic 工作流可以减少重复性工作量，降低错误率并加快决策速度。有效部署后，它们能够推动创新，使团队能够专注于高价值任务，而自主系统则负责处理细节。简而言之，Agentic 工作流使您的组织更加敏捷、适应性和面向未来。

**什么是 Agentic 工作流？**

Agentic 工作流是[由自主代理组成的系统，协同工作](https://thenewstack.io/putting-ai-to-work-systems-of-intelligence-and-actionable-agency/)以实现特定目标。工作流中的每个代理都旨在：

- 感知其环境或上下文。
- 根据预定义的规则或模型做出决策。
- 执行任务，通常是通过与外部 API 或系统交互来完成。

**主要优点：**

- 自动化：通过将任务委托给代理来减少人工工作。
- 适应性：代理可以动态调整以适应不断变化的需求或输入。
- 效率：通过智能地委托子任务来优化多步骤任务。

**常见用例：**

- 具有升级工作流的客户支持机器人。
- 能够检索、分析和总结信息的自主研究助手。
- 智能家居中物联网设备的工作流编排。

**步骤 1：设置环境**

在开始构建 Agentic 工作流之前，请确保已安装所需的工具。我们将使用 OpenAI 进行自然语言处理，并使用 Langchain 进行工作流编排。

**安装依赖项：**

```bash
pip install openai langchain requests
```

**配置 OpenAI API 密钥：**

使用环境变量安全地存储您的 API 密钥：

```python
import os
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
```

**步骤 2：设计工作流**

在本教程中，我们将构建一个自主研究代理工作流。该工作流包括：

- 接受研究主题作为输入。
- 使用外部 API 检索相关的网络文章。
- 总结内容。
- 将结果存储在本地文件中。

**步骤 3：创建代理框架**

代理需要一个核心结构来感知、决策和行动。让我们一步一步构建这个框架。

**基本代理类**

定义一个可重用的`Agent`类，所有代理都将继承该类。

```python
class Agent:
    def __init__(self, name):
        self.name = name

    def perceive(self, input_data):
        """Receive input from the environment."""
        raise NotImplementedError("Perceive method must be implemented.")

    def decide(self):
        """Make decisions based on perceived input."""
        raise NotImplementedError("Decide method must be implemented.")

    def act(self):
        """Perform an action based on the decision."""
        raise NotImplementedError("Act method must be implemented.")
```

**步骤 4：实现专用代理**

我们将创建三个专用代理：

- 输入代理：接受研究主题。
- 检索代理：从 API 获取文章。
- 摘要代理：总结内容。

**输入代理**

此代理接受研究主题作为输入。

```python
class InputAgent(Agent):
    def perceive(self, input_data):
        self.topic = input_data

    def decide(self):
        return f"Proceeding with research on: {self.topic}"

    def act(self):
        print(self.decide())
        return self.topic
```

**检索代理**

此代理使用外部 API（例如模拟新闻 API）来获取文章。

```python
# ... (Retrieval Agent code would go here)
```
```python
class RetrievalAgent(Agent):
    def __init__(self, name, api_url):
        super().__init__(name)
        self.api_url = api_url

    def perceive(self, topic):
        self.topic = topic

    def decide(self):
        query_params = {"q": self.topic, "apiKey": "your_api_key"}
        return requests.get(self.api_url, params=query_params)

    def act(self):
        response = self.decide()
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            print(f"Retrieved {len(articles)} articles.")
            return articles
        else:
            print("Failed to retrieve articles.")
            return []

```

**摘要代理**
此代理使用OpenAI的API来总结内容。

```python
import openai
class SummarizationAgent(Agent):
    def perceive(self, articles):
        self.articles = articles

    def decide(self):
        summaries = []
        for article in self.articles:
            prompt = f"Summarize the following article:\n\n{article['content']}"
            response = openai.Completion.create(
                model="text-davinci-003", prompt=prompt, max_tokens=100
            )
            summaries.append(response.choices[0].text.strip())
        return summaries

    def act(self):
        summaries = self.decide()
        for idx, summary in enumerate(summaries):
            print(f"Summary {idx + 1}: {summary}")
        return summaries

```

**步骤5：协调工作流程**
现在，让我们将代理集成到协调的工作流程中。

```python
class Workflow:
    def __init__(self, agents):
        self.agents = agents

    def run(self, input_data):
        current_data = input_data
        for agent in self.agents:
            agent.perceive(current_data)
            current_data = agent.act()
        print("Workflow completed.")

```

**实例化代理并运行工作流程**

```python
# Define the API URL for article retrieval
api_url = "https://newsapi.org/v2/everything"
# Create agents
input_agent = InputAgent(name="InputAgent")
retrieval_agent = RetrievalAgent(name="RetrievalAgent", api_url=api_url)
summarization_agent = SummarizationAgent(name="SummarizationAgent")
# Orchestrate workflow
agents = [input_agent, retrieval_agent, summarization_agent]
research_workflow = Workflow(agents)
# Run the workflow
topic = "AI in Healthcare"
research_workflow.run(topic)

```

**步骤6：增强工作流程**
您可以通过以下方式扩展此工作流程的功能：

**添加文件存储：**将总结的内容保存到文本文件。

```python
class FileStorageAgent(Agent):
    def perceive(self, summaries):
        self.summaries = summaries

    def decide(self):
        return "Summaries saved to research_summaries.txt."

    def act(self):
        with open("research_summaries.txt", "w") as file:
            for summary in self.summaries:
                file.write(summary + "\n\n")
        print(self.decide())

```
将此代理添加到工作流程中：

```python
file_storage_agent = FileStorageAgent(name="FileStorageAgent")
agents.append(file_storage_agent)
```

**错误处理：**为API错误和空响应实现异常处理。
**并行处理：**使用Python的`asyncio`同时处理多个文章。

**步骤7：测试和调试**
使用各种主题测试工作流程以确保其健壮性：

- 处理没有可用文章的主题。
- 使用不同的输入测试以验证代理的适应性。
- 记录错误以方便调试。

**结论**
代理工作流程为创建智能的、面向任务的系统提供了一种实用方法。通过将任务分解成专门的组件，您可以构建可扩展的、灵活的解决方案来处理复杂的过程。

通过遵循此分步指南，您已经掌握了使用Python设计和实现代理工作流程的基础知识。从设置单个代理到将它们协调到统一的系统中，您现在拥有开发适合您特定需求的自主工作流程的工具。

下一步是尝试更高级的代理，集成其他工具和API，并改进决策过程以最大限度地发挥这些工作流程的潜力。

彻底改变您使用尖端人工智能创新的方式。探索Andela的权威指南“[3 AI工具改变生产力](https://www.andela.com/blog-posts/3-ai-tools-to-boost-your-productivity-4x/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack-agentic&utm_content=writers-room-sowole&utm_term=ai-tools)”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。
](https://youtube.com/thenewstack?sub_confirmation=1)
```