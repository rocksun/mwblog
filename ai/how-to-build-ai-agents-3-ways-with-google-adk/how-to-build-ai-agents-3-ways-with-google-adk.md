<!--
title: 谷歌ADK实战：3种方法打造AI智能体
cover: https://cdn.thenewstack.io/media/2025/12/c56a32a5-zhaoli-jin-xrpmmkfydnu-unsplashb.jpg
summary: Google ADK是构建AI代理的基础框架，支持Python、YAML和可视化构建器三种开发方式，提供灵活性和控制力，可用于创建多代理系统。
-->

Google ADK是构建AI代理的基础框架，支持Python、YAML和可视化构建器三种开发方式，提供灵活性和控制力，可用于创建多代理系统。

> 译自：[How To Build AI Agents 3 Ways With Google ADK](https://thenewstack.io/how-to-build-ai-agents-3-ways-with-google-adk/)
> 
> 作者：Janakiram MSV

[Google](https://cloud.google.com/?utm_content=inline+mention) 的 [Agent Development Kit](https://google.github.io/adk-docs/) (ADK) 已迅速成为构建 AI 代理的基础框架。[在 Google Cloud NEXT 2025 大会上推出](https://thenewstack.io/googles-adk-is-a-new-open-source-framework-for-building-multiagent-systems/)后，ADK 在 Google 产品（包括 [Gemini 企业版](https://cloud.google.com/gemini-enterprise?utm_source=google&utm_medium=cpc&utm_campaign=1710070-Workspace-DR-APAC-IN-en-Google-BKWS-EXA-Pollux&utm_content=c-Hybrid+%7C+BKWS+-+EXA+%7C+Txt-Pollux-Generic-435278751514&utm_term=gemini+enterprise&gclsrc=aw.ds&gad_source=1&gad_campaignid=23080541881&gclid=CjwKCAiA55rJBhByEiwAFkY1QGdZPP5s9wkpjdS3nzYfKqlrtfqicVSrvS5P13nnCq3dXyHtXPigwhoC2fkQAvD_BwE&hl=en) 和 [Google 客户互动套件](https://cloud.google.com/solutions/customer-engagement-ai?hl=en)）中为代理提供支持。ADK 对开发人员特别有吸引力的地方在于其灵活性。开发人员可以使用 Python 代码、YAML 配置文件或拖放式可视化界面构建代理——具体取决于工作流偏好和用例要求。

在本教程中，我将引导您通过这三种方法构建您的第一个“Hello World”ADK 代理。最后，您将拥有一个使用每种方法在本地运行的功能性代理，为您选择适合自己项目的方法奠定基础。

## 理解三种方法

在深入实施之前，让我们先了解每种方法提供的功能：

**命令式代理 (Python)：** 这种代码优先的方法为您提供了最大的灵活性和控制力。您直接在 Python 中定义代理逻辑、工具和编排，这使其成为需要自定义逻辑、与现有代码库集成或复杂多代理系统的复杂代理的理想选择。Python 方法还通过 LiteLLM 集成支持任何大型语言模型 (LLM)。

**声明式代理 (YAML)：** 该方法于 2025 年 8 月随 Agent Config 功能推出，允许您使用 YAML 配置文件定义代理。它减少了样板代码，使代理更易于一目了然地理解——对于更简单的代理或当您希望非开发人员理解代理行为时特别有用。

**可视化代理构建器 (GUI)：** Visual Agent Builder 在 ADK v1.18.0 中推出，是一个基于浏览器的 IDE，它结合了可视化工作流设计器、配置面板和 AI 助手。您可以通过拖放交互和自然语言对话设计多代理系统，该工具会在幕后生成正确的 YAML 配置。

## 前提条件

开始之前，请确保您具备以下条件：

* Python 3.10 或更高版本
* 代码编辑器
* 终端访问
* Google AI Studio API 密钥或已启用 Vertex AI 的 Google Cloud 项目

## 步骤 1：设置环境

首先，创建虚拟环境并安装 ADK。打开您的终端并运行：

```
python -m venv .venv
source .venv/bin/activate  
```

安装 ADK 包：

```
pip install google-adk
```

验证安装：

```
adk --version
```

您应该会看到已安装的 ADK 版本（Visual Agent Builder 需要 1.18.0 或更高版本）。

## 步骤 2：配置模型访问

ADK 需要访问 LLM。最简单的入门选项是使用带有免费 API 密钥的 [Google AI Studio](https://aistudio.google.com/)。从 Google AI Studio 获取您的 API 密钥并保持其可访问性，因为在接下来的步骤中您会用到它。

## 方法 1：使用 Python 构建命令式代理

命令式方法是最强大的方法，通过代码让您完全控制代理行为。让我们构建一个简单的问候代理，演示其核心概念。

### **创建项目结构**

为您的代理项目创建一个新目录：

```
mkdir hello_agent
cd hello_agent
```

在 `hello_agent` 目录中创建以下文件：

`__init__.py`

```
from . import agent
```

此文件将目录标记为 Python 包并导入代理模块。

`agent.py`

```
from google.adk.agents import Agent


def greet_user(name: str) -&gt; dict:
    """Greets a user by name.
    
    Args:
        name (str): The name of the user to greet.
        
    Returns:
        dict: A greeting message with status.
    """
    return {
        "status": "success",
        "message": f"Hello, {name}! Welcome to Google ADK. I'm your first AI agent!"
    }


def get_agent_info() -&gt; dict:
    """Returns information about this agent.
    
    Returns:
        dict: Information about the agent's capabilities.
    """
    return {
        "status": "success",
        "info": "I am a Hello World agent built with Google ADK using Python. "
                "I can greet users and tell them about myself."
    }


root_agent = Agent(
    name="hello_agent",
    model="gemini-2.0-flash",
    description="A friendly greeting agent that welcomes users to Google ADK.",
    instruction="""You are a friendly and helpful greeting agent. Your primary purpose is to:
    1. Greet users warmly when they provide their name using the greet_user tool
    2. Explain what you are when asked using the get_agent_info tool
    3. Be enthusiastic about introducing users to Google ADK
    
    Always use the available tools to respond appropriately to user requests.""",
    tools=[greet_user, get_agent_info],
)
```

Agent 类是 ADK 中的核心构建块。请注意我们如何将工具定义为带有类型提示和文档字符串的普通 Python 函数。ADK 使用这些信息来帮助 LLM 理解何时以及如何调用每个工具。

`.env`

```
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

将占位符值替换为您的实际凭据。

### **运行代理**

导航到您的代理文件夹的父目录：

```
cd ..
```

以终端模式运行代理：

```
adk run hello_agent
```

您应该会看到一个提示，指示代理正在运行：

`Running agent hello_agent, type exit to exit.  
[user]:  
Try these interactions:  
[user]: Hello, my name is Jani  
[user]: What can you do?  
[user]: Tell me about yourself`

代理将使用适当的工具进行响应。输入 `exit` 退出。

## 方法 2：使用 YAML 构建声明式代理

使用 YAML 配置文件的声明式方法简化了代理的创建，特别是对于简单的用例。Agent Config 功能生成相同的底层代理结构，但代码更少。

### **创建基于配置的项目**

使用 ADK CLI 生成一个基于配置的代理项目：

```
adk create yaml_hello_agent --type=config
```

接受默认值并完成步骤。

[![](https://cdn.thenewstack.io/media/2025/11/b94370f5-adk-1-0-1024x601.png)](https://cdn.thenewstack.io/media/2025/11/b94370f5-adk-1-0-1024x601.png)

### **在 YAML 中定义代理**

打开 `yaml_hello_agent/root_agent.yaml` 并将其内容替换为：

```
name: hello_yaml_agent
model: gemini-2.0-flash
description: A friendly greeting agent built with YAML configuration.
instruction: |
  You are a friendly and helpful greeting agent. Your primary purpose is to:
  1. Greet users warmly when they provide their name using the greet_user tool
  2. Explain what you are when asked using the get_agent_info tool
  3. Be enthusiastic about introducing users to Google ADK
  
  Always use the available tools to respond appropriately to user requests.
tools:
  - name: yaml_hello_agent.greet_user
  - name: yaml_hello_agent.get_agent_info
```

YAML 结构镜像了 Python Agent 类的参数，但以更易读的格式呈现。请注意工具是如何通过其模块路径引用的。

### **创建工具模块**

ADK YAML 配置的一个强大功能是您可以混合使用 Python 代码。更新 `yaml_hello_agent` 文件夹中的 `__init__.py` 文件：

```
def greet_user(name: str) -&gt; dict:
    """Greets a user by name.
    
    Args:
        name (str): The name of the user to greet.
        
    Returns:
        dict: A greeting message with status.
    """
    return {
        "status": "success",
        "message": f"Hello, {name}! Welcome to Google ADK via YAML config!"
    }


def get_agent_info() -&gt; dict:
    """Returns information about this agent.
    
    Returns:
        dict: Information about the agent's capabilities.
    """
    return {
        "status": "success", 
        "info": "I am a Hello World agent built with YAML configuration. "
                "I demonstrate the declarative approach to ADK agents."
    }
```

您的项目结构现在应该如下所示：

```
yaml_hello_agent/  
├── root_agent.yaml  
├── __init__.py  
└── .env
```

### **运行基于 YAML 的代理**

导航到父目录并运行：

```
adk run yaml_hello_agent
```

使用相同的提示进行测试：

```
[user]: Hi, I'm Jani
[user]: What are you?
```

代理的响应与 Python 版本相同，但完全通过配置定义。

## 方法 3：使用可视化代理构建器构建代理

Visual Agent Builder 在 ADK v1.18.0 中推出，是一个基于浏览器的 IDE，它改变了您构建代理的方式。它结合了可视化工作流设计器、配置面板和 AI 助手，让您可以通过拖放交互和自然语言对话设计代理。

### **启动可视化代理构建器**

从任何目录运行：

```
adk web
```

[![](https://cdn.thenewstack.io/media/2025/11/4c9ef222-adk-1-1-1024x446.png)](https://cdn.thenewstack.io/media/2025/11/4c9ef222-adk-1-1-1024x446.png)

在浏览器中打开 `http://localhost:8000/dev-ui/` 即可访问 Visual Agent Builder。

点击下拉菜单旁边的“+”按钮，输入名称 `visual_hello_agent`：

[![](https://cdn.thenewstack.io/media/2025/11/b5c12cc7-adk-1-2-1024x771.png)](https://cdn.thenewstack.io/media/2025/11/b5c12cc7-adk-1-2-1024x771.png)

与其手动配置代理，不如使用 AI 助手。在右侧面板中，输入：

`Create a simple greeting agent that can:  
1. Greet users by name when they introduce themselves  
2. Tell users about itself when asked  
Use gemini-2.5-flash as the model. Keep it simple with just two tools.`

[![](https://cdn.thenewstack.io/media/2025/11/71fbb3ba-adk-1-3-1024x563.png)](https://cdn.thenewstack.io/media/2025/11/71fbb3ba-adk-1-3-1024x563.png)

AI 助手将生成完整的代理配置，包括：

* 适当的代理名称和描述
* 模型选择
* 详细说明

[![](https://cdn.thenewstack.io/media/2025/11/fb5ddcc9-adk-1-4-1024x563.png)](https://cdn.thenewstack.io/media/2025/11/fb5ddcc9-adk-1-4-1024x563.png)

点击保存按钮，然后退出构建器模式。您现在可以与代理聊天了。

[![](https://cdn.thenewstack.io/media/2025/11/d6c47e08-adk-1-5-1024x541.png)](https://cdn.thenewstack.io/media/2025/11/d6c47e08-adk-1-5-1024x541.png)

## 比较这三种方法

使用所有三种方法构建代理后，以下是它们的比较：

| **方面**           | **命令式（Python）**   | **声明式（YAML）**     | **可视化构建器**     |
| -------------- | ---------------- | ------------------ | -------------- |
| **最适用于**         | 复杂逻辑，CI/CD       | 简单代理，协作         | 原型设计，学习      |
| **学习曲线**         | 中等             | 低                 | 最低           |
| **灵活性**         | 最高             | 中等               | 中等           |
| **模型支持**         | 所有（通过 LiteLLM） | 仅限 Gemini          | 仅限 Gemini      |
| **版本控制**         | 优秀             | 优秀               | 良好（可导出 YAML） |
| **非开发人员友好**     | 否               | 部分是             | 是             |
| **调试**           | 手动             | 手动               | 内置追踪        |

主要考虑因素：

* 当您需要最大程度的控制、自定义集成或通过 LiteLLM 支持非 Gemini 模型时，**Python 方法**是最佳选择。
* **YAML 方法**适用于简单的代理，您希望配置文件的简洁性，并能够混合使用 Python 工具。
* **可视化构建器**擅长快速原型设计、学习 ADK 概念以及与能够用自然语言描述需求的非开发人员协作。

在实践中，这些方法相辅相成。您可以使用可视化构建器进行原型设计和理解架构，然后导出 YAML 进行版本控制和 CI/CD 管道。

## 展望未来

本教程涵盖了使用 Google ADK 的三种开发方法构建您的第一个 AI 代理的基本步骤。每种方法都有其优点，并且该框架的设计旨在让您可以在它们之间流畅切换——从可视化开始，导出到 YAML，并在需要高级功能时转入 Python。

在后续教程中，我们将探讨 ADK 的高级功能，包括具有顺序、并行和循环模式的多代理系统、与模型上下文协议 (MCP) 服务器的工具集成、会话管理和内存持久化，以及部署到 Vertex AI Agent Engine。您在这里建立的基础将在我们处理日益复杂的代理工作流时为您提供很好的帮助。