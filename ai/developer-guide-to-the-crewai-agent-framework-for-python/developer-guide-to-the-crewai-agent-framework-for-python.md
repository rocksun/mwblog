
<!--
title: Python版CrewAI智能体框架开发者指南
cover: https://cdn.thenewstack.io/media/2024/12/1ebdd489-getty-images-voc6uuftmqo-unsplashb.jpg
-->

与传统孤立运行的单代理系统不同，CrewAI 引入了能够协同工作的自主 AI 代理。

> 译自 [Developer Guide to the CrewAI Agent Framework for Python](https://thenewstack.io/developer-guide-to-the-crewai-agent-framework-for-python/)，作者 Janakiram MSV。

[CrewAI](https://www.crewai.com/) 是最流行的[Python](https://thenewstack.io/what-is-python/)框架之一，旨在实现智能多智能体协作——改变开发者处理复杂AI工作流程的方式。与传统上独立运行的单智能体系统不同，CrewAI引入了能够协同工作的自主AI智能体——每个智能体都承担着专门的角色，配备特定的工具，并朝着明确定义的目标努力。通过促进类似人类的协作并利用先进的工作流程管理，CrewAI为开发者提供了一个强大的工具包，用于构建智能、可扩展和适应性强的AI系统。

## CrewAI和AI智能体的构成

![](https://cdn.thenewstack.io/media/2024/12/91d73a9e-agents-1-1-1024x681-1.png)

CrewAI严格遵守上图中概述的原则，该图将AI智能体的构成分解为关键组件：[角色](https://thenewstack.io/how-to-define-an-ai-agent-persona-by-tweaking-llm-prompts/)、[指令](https://thenewstack.io/enhancing-ai-agents-adding-instructions-tasks-and-memory/)、任务、规划、[记忆](https://thenewstack.io/how-to-add-persistence-and-long-term-memory-to-ai-agents/)、[工具](https://thenewstack.io/how-to-add-tool-support-to-ai-agents-for-performing-actions/)和委托。这些元素中的每一个都是CrewAI智能体设计的基石，能够创建智能、特定角色和协作的AI系统。

有关详细解释和背景信息，请参阅我之前关于[AI智能体构成](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)的文章。

### 角色

CrewAI允许开发者通过指定每个智能体的职能和详细的背景故事来定义清晰的角色。这确保了智能体的行为一致，并与其预期角色相符。例如，一个智能体可以配置为市场研究分析师，专门研究新兴趋势。此角色有助于指导智能体在整个工作流程中的行为和决策。

```py
researcher = Agent(  
    role='Market Research Analyst',  
    goal='Identify emerging market trends',  
    backstory='An experienced analyst specializing in technology and startups'  
)
```

角色为智能体的行为创造了上下文，使其响应和行动更加量身定制和相关。

### 指令

CrewAI中的指令定义了智能体的职位描述，指定了它应该如何处理其任务。CrewAI允许开发者为每个智能体提供清晰、结构化的指令，确保其目标易于理解且可操作。

```py
research_task = Task(  
    description='Analyze industry reports to identify top emerging technologies',  
    agent=researcher  
)
```

指令直接影响任务执行过程，确保智能体在定义的工作范围内运行。

### 任务

任务是智能体执行的可操作元素。CrewAI将任务与智能体的能力无缝结合，确保角色与具体的作业分配相符。智能体独立或协作地完成其任务，具体取决于所选择的工作流程（例如，顺序或并行）。CrewAI实现了清晰的任务委托，以确保每个智能体都知道其目标。

### 规划

CrewAI支持规划，允许工作流程以顺序、分层或并行模式执行。智能体可以战略性地行动，动态地相互协调以实现共同目标。规划将单个智能体的行动与更广泛的工作流程对齐，确保效率和一致性。例如，CrewAI Flows使智能体能够链接任务、有条件地执行或响应动态事件。

```py
market_crew = Crew(  
    agents=[researcher, writer],  
    tasks=[research_task, writing_task],  
    process='sequential'  # Workflow planning  
)
```

这种方法模拟了现实世界中的团队协作，其中角色和职责是在共享策略下定义的。

### 记忆

记忆允许智能体在任务执行期间保留历史上下文。CrewAI智能体可以配置为具有记忆功能，以回忆之前的交互，确保工作流程的连续性和连贯性。这在长期运行的过程中尤其重要，在这些过程中，智能体必须根据过去的结果进行调整。

```py
researcher = Agent(  
    role='Research Analyst',  
    memory=True,  # Retains interaction history  
    goal='Analyze historical data trends for insights'  
)
```

启用记忆后，CrewAI智能体可以上下文操作，在先前结果的基础上提供更好的结果。

### 工具

CrewAI 代理通过扩展其能力的工具整合技能。无论是需要网络搜索、数据提取还是 PDF 分析的任务，代理都可以利用工具来访问和处理外部信息。CrewAI 支持多种工具，例如 PDFSearchTool 和 SerperDevTool，允许代理高效地检索和分析数据。

```python
from crewai_tools import PDFSearchTool  
 
research_tool = PDFSearchTool(pdf='industry_report.pdf')  
researcher = Agent(  
    role='Research Analyst',  
    tools=[research_tool],  
    goal='Extract insights from the industry report'  
)
```

工具使代理能够执行超出大型语言模型单独能力范围的专门任务，增强了它们整体的效能。

### 委派

委托是CrewAI的一个基本特性，它使得团队管理和代理间通信成为可能。代理可以动态分配子任务、协作和共享信息以优化工作流程。CrewAI支持在层次化工作流中的结构化委托，其中管理代理负责监督任务分配和验证。

例如，团队领导代理可以将分析任务委托给研究人员，将内容生成委托给写作者，确保工作流程顺利进行。

```python
manager = Agent(  
    role='Team Lead',  
    goal='Oversee research and content generation',  
    allow_delegation=True  
) 
```

启用委托功能后，CrewAI创建了一个协作生态系统，其中代理能够适应动态的任务需求。

## 结论

CrewAI遵循图像中描述的方法，将人物角色、指令、任务、规划、记忆、工具和委派等核心组件整合到其框架中。这种模块化和逻辑结构允许开发者设计模仿专业团队的AI代理，实现既智能又可适应的高级工作流程。通过支持基于角色的人物角色、任务执行、规划和工具集成，CrewAI为构建协作多代理系统提供了全面的解决方案。

在下一篇文章中，我们将更仔细地研究这个框架。敬请期待。