
<!--
title: CrewAI如何使AI代理成为协作团队成员
cover: https://cdn.thenewstack.io/media/2024/12/421f6a2c-allison-saeng-gxjay46atxo-unsplashb.jpg
-->

CrewAI 的架构远远超越了静态工作流，它支持智能、上下文感知和协作的 AI 代理。

> 译自 [How CrewAI Enables AI Agents as Collaborative Team Members](https://thenewstack.io/how-crewai-enables-ai-agents-as-collaborative-team-members/)，作者 Janakiram MSV。

在本系列的第一部分中，我们[介绍了 CrewAI](https://thenewstack.io/developer-guide-to-the-crewai-agent-framework-for-python/)，将其功能与 AI 智能体的关键属性进行了映射。现在，我们将更仔细地研究使[CrewAI](https://www.crewai.com/)真正强大的核心概念，并探讨其架构如何使开发人员能够构建复杂、智能的系统。

CrewAI 的核心是基于角色的[AI 智能体](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)的概念。每个智能体都设计用于执行特定任务，其行为由定义的角色、目标和背景故事引导。这些智能体不仅仅执行任务——它们动态协作、共享信息并适应工作流程的需求。

考虑这样一种场景：一个智能体充当市场研究分析师，负责识别市场趋势。可以如下配置此智能体：

```python
from crewai import Agent
from crewai_tools import SerperDevTool  
 
researcher = Agent(  
    role="Market Research Analyst",  
    goal="Identify emerging market trends",  
    backstory="An experienced analyst with a focus on technology and startups.",  
    llm="gpt-4o-mini",  # Specifies the language model  
    tools=[SerperDevTool()],  # Integrates a web search tool  
    memory=True,  # Retains interaction history  
    allow_delegation=False,  # Restricts task delegation  
    verbose=True  # Enables detailed logs  
) 
```

在这里，智能体配置了特定的角色、明确的目标和背景故事来解释其行为。其他属性，例如集成工具（例如，网络搜索）和内存功能，使智能体能够智能地适应工作流程。

## CrewAI 中的模块化

CrewAI 最强大的功能之一是其模块化设计，它允许开发人员将各种组件——[大型语言模型 (LLM)](https://thenewstack.io/llm/)、工具、[向量数据库](https://thenewstack.io/elasticsearch-was-great-but-vector-databases-are-the-future/)和内存——无缝地与智能体关联。这种模块化架构确保可以自定义和扩展智能体以适应各种任务和工作流程，而无需进行重大重新配置。

CrewAI 智能体与 LLM 无关，这意味着它们可以根据任务要求利用任何开源或专有语言模型。开发人员可以在智能体级别指定 LLM 提供商和模型，从而确保灵活选择符合性能、成本或隐私需求的模型。

例如，集成[OpenAI](https://thenewstack.io/beyond-chatgpt-exploring-the-openai-platform/)的[GPT-4o](https://thenewstack.io/openais-realtime-api-takes-a-bow/)-mini 或其他模型非常简单：

```python
from crewai import Agent, LLM
 
custom_llm = LLM(
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=4000
)
 
researcher = Agent(
    role="AI Researcher",
    goal="Analyze AI adoption trends",
    backstory="A data-driven analyst specializing in AI trends",
    llm=custom_llm
)
```

CrewAI 支持向量数据库集成，以启用[检索增强生成](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/) (RAG) 工作流程。通过将语言模型与[向量嵌入](https://thenewstack.io/vector-embeddings-explained-a-beginners-guide-to-powerful-ai/)相结合，智能体可以从结构化或非结构化数据源检索上下文相关的信，从而提高响应准确性和基础性。

例如，配置为搜索向量数据库以获取研究内容的智能体可以定义如下：

```python
from crewai import Agent, Task, Crew, tools
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
 
# Initialize vector database
vectorstore = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory="./research_db"
)
 
# Create a custom tool for vector search
@tools.tool('Vector Search')
def vector_search(query: str) -&gt; str:
    """Search vector database for relevant context"""
    results = vectorstore.similarity_search(query)
    return str(results)
 
# Create a research agent with vector database access
researcher = Agent(
    role='Research Specialist',
    goal='Retrieve precise information from vector database',
    backstory='I am an expert at retrieving and analyzing information from databases',
    tools=[vector_search],
    verbose=True
)
 
# Define task utilizing vector database
research_task = Task(
    description='Conduct targeted research using vector database',
    agent=researcher
)
 
# Create crew
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)
 
# Execute workflow
result = crew.kickoff()
```

## 使用 CrewAI 构建工作流程

CrewAI通过使代理在结构化工作流中协作，促进了多代理间的无缝协调。工作流可以定义为顺序的、层次的或异步的，这取决于任务的性质。

一个简单的例子说明了两个代理——市场研究员和内容策略师——如何协作以产生洞察并制定营销策略。

```python
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
 
researcher = Agent(
    role='Market Research Analyst',
    goal='Discover emerging market trends',
    backstory='Expert in identifying innovative business opportunities',
    verbose=True,
    allow_delegation=False,
    llm=ChatOpenAI(model_name="gpt-4")
)
 
writer = Agent(
    role='Content Strategist',
    goal='Create compelling marketing narratives',
    backstory='Skilled at transforming research into engaging content',
    verbose=True,
    allow_delegation=False,
    llm=ChatOpenAI(model_name="gpt-4")
)
 
research_task = Task(
    description='Analyze current market trends',
    agent=researcher,
    expected_output="A detailed analysis of current market trends"
)
 
writing_task = Task(
    description='Develop marketing strategy based on research',
    agent=writer,
    context=research_task.output,
    expected_output="A comprehensive marketing strategy document"
)
 
market_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True 
)
 
result = market_crew.kickoff()
print(result)
```

在这个例子中，任务是顺序执行的。市场研究员首先识别新出现的趋势，然后内容策略师根据这些洞察制定策略。CrewAI无缝协调代理的工作，确保任务高效执行。

## 高级工作流管理与CrewAI流程

对于更复杂的场景，CrewAI引入了Flows——一种模块化且基于事件的方法来管理AI工作流。Flows允许开发人员动态链接任务，管理状态并实现决策的逻辑条件。

考虑一个场景，我们使用Flow生成一个随机城市的名字，并检索有关它的有趣事实：

```python
from crewai.flow.flow import Flow, listen, start  
from litellm import completion  
 
class ExampleFlow(Flow):  
    model = "gpt-4o-mini"  
 
    @start()  
    def generate_city(self):  
        response = completion(  
            model=self.model,  
            messages=[  
                {"role": "user", "content": "Return the name of a random city in the world."},  
            ],  
        )  
        random_city = response["choices"][0]["message"]["content"]  
        return random_city  
 
    @listen(generate_city)  
    def generate_fun_fact(self, random_city):  
        response = completion(  
            model=self.model,  
            messages=[  
                {"role": "user", "content": f"Tell me a fun fact about {random_city}"},  
            ],  
        )  
        fun_fact = response["choices"][0]["message"]["content"]  
        return fun_fact  
 
flow = ExampleFlow()  
result = flow.kickoff()  
print(f"Generated fun fact: {result}")  
```

在这个例子中，Flow类负责协调工作流。@start()方法生成一个随机城市的名字，而@listen()装饰器触发一个后续方法，根据城市的名字检索一个有趣的事实。Flows简化了创建适应性强、事件驱动的工作流的过程，这些工作流能够动态响应状态变化或触发器。

当Flows与CrewAI的现有原语结合时，它们成为了一个强大的编排框架，用于设计和构建复杂的工作流。

## 使用CrewAI实现RAG

CrewAI的灵活性扩展到了实现RAG，这是一种通过将外部信息检索集成到生成过程中来增强AI系统的强大技术。配备有PDFSearchTool或WebSearchTool等工具的CrewAI代理可以从各种来源提取和处理数据，以产生上下文准确的结果。

这里有一个例子，一个专门的代理使用RAG从研究论文中提取关键见解：

```python
from crewai import Agent, Task, Crew  
from crewai_tools import PDFSearchTool  
 
# Define RAG tool  
rag_tool = PDFSearchTool(  
    pdf='research_paper.pdf'  
)  
 
# Define agent with RAG capabilities  
researcher = Agent(  
    role='Research Analyst',  
    goal='Extract key insights from research documents',  
    backstory='Expert at analyzing complex academic papers',  
    tools=[rag_tool]  
)  
 
# Define task for RAG  
research_task = Task(  
    description='Analyze the research paper and summarize key findings',  
    agent=researcher,  
    tools=[rag_tool],  
    expected_output='A detailed summary of the key findings from the research paper'  
)  
 
# Create Crew to coordinate workflow  
research_crew = Crew(  
    agents=[researcher],  
    tasks=[research_task],  
    process='sequential'  
)  
 
# Execute RAG workflow  
result = research_crew.kickoff()  
print(result)  
```

## 可扩展性和模块化

CrewAI 的模块化架构使其成为跨行业扩展 AI 系统的理想选择。代理、任务和工具是可重用的组件，可以组合成各种配置来解决复杂的问题。无论您是在金融领域自动化工作流程，在学术界协调研究，还是在电子商务中管理客户查询，CrewAI 都提供了一个一致且可扩展的框架。

例如，创建可重用的“研究团队”允许相同的代理分析不同的数据源，而只需最少的重新配置：

```python
from crewai import Agent, Task, Crew  
from crewai_tools import PDFSearchTool  
 
def create_research_crew(doc):  
    tool = PDFSearchTool(pdf=doc)  
    agent = Agent(
        role="Research Analyst",
        tools=[tool],
        goal="Summarize document insights",
        backstory="I am an expert research analyst who specializes in extracting and summarizing key insights from documents."
    )  
    task = Task(
        description="Analyze and summarize content", 
        agent=agent,
        expected_output="A comprehensive summary of the key insights from the document"
    )  
    return Crew(agents=[agent], tasks=[task], process="sequential")  
 
# Execute for multiple documents  
for pdf in ["doc1.pdf", "doc2.pdf"]:  
    crew = create_research_crew(pdf)  
    print(crew.kickoff())  
```

这种模块化确保了可扩展性，同时不会影响可维护性或性能。

CrewAI 的架构远远超越了静态工作流程，它支持智能的、上下文感知的和协作的代理。通过内存、规划、事件驱动的流程和 RAG 集成等高级功能，CrewAI 为开发人员提供了应对复杂现实世界挑战的工具。通过结合适应性、可扩展性和模块化，CrewAI 使团队能够设计既动态又可靠的 AI 系统，从而为自动化和智能任务执行解锁新的可能性。
