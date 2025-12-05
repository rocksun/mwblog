[Google](https://cloud.google.com/?utm_content=inline+mention)‘s [Agent Development Kit](https://google.github.io/adk-docs/) (ADK) has rapidly become a foundational framework for building AI agents. [Introduced at Google Cloud NEXT 2025](https://thenewstack.io/googles-adk-is-a-new-open-source-framework-for-building-multiagent-systems/), ADK powers agents across Google products, including [Gemini Enterprise](https://cloud.google.com/gemini-enterprise?utm_source=google&utm_medium=cpc&utm_campaign=1710070-Workspace-DR-APAC-IN-en-Google-BKWS-EXA-Pollux&utm_content=c-Hybrid+%7C+BKWS+-+EXA+%7C+Txt-Pollux-Generic-435278751514&utm_term=gemini+enterprise&gclsrc=aw.ds&gad_source=1&gad_campaignid=23080541881&gclid=CjwKCAiA55rJBhByEiwAFkY1QGdZPP5s9wkpjdS3nzYfKqlrtfqicVSrvS5P13nnCq3dXyHtXPigwhoC2fkQAvD_BwE&hl=en) and the [Google Customer Engagement Suite](https://cloud.google.com/solutions/customer-engagement-ai?hl=en). What makes ADK particularly compelling for developers is its flexibility. Developers can build agents using Python code, YAML configuration files or a drag-and-drop visual interface — depending on workflow preferences and use case requirements.

In this tutorial, I’ll walk you through all three approaches to building your first “Hello World” agent with ADK. By the end, you’ll have a functional agent running locally using each method, giving you a foundation to choose the right approach for your projects.

## Understanding the 3 Approaches

Before diving into implementation, let’s understand what each approach offers:

**Imperative agents (Python):** This code-first approach gives you maximum flexibility and control. You define agent logic, tools and orchestration directly in Python, making it ideal for complex agents that need custom logic, integration with existing codebases or sophisticated multiagent systems. The Python approach also supports any large language model (LLM) through LiteLLM integration.

**Declarative agents (YAML):** Introduced in August 2025 with the Agent Config feature, this approach lets you define agents using YAML configuration files. It reduces boilerplate and makes agents easier to understand at a glance — particularly useful for simpler agents or when you want non-developers to understand agent behaviour.

**Visual Agent Builder (GUI):** Launched in ADK v1.18.0, the Visual Agent Builder is a browser-based IDE that combines a visual workflow designer, configuration panels and an AI assistant. You can design multiagent systems through drag-and-drop interactions and natural language conversations, with the tool generating proper YAML configurations under the hood.

## Prerequisites

Before we begin, ensure you have the following:

* Python 3.10 or higher
* A code editor
* Terminal access
* Either a Google AI Studio API key or a Google Cloud project with Vertex AI enabled

## Step 1: Setting up the Environment

Let’s start by creating a virtual environment and installing ADK. Open your terminal and run:

```
python -m venv .venv
source .venv/bin/activate  
```

Install the ADK package:

```
pip install google-adk
```

Verify the installation:

```
adk --version
```

You should see the installed ADK version (1.18.0 or higher is required for the Visual Agent Builder).

## Step 2: Configure Model Access

ADK needs access to an LLM. The simplest option for getting started is using [Google AI Studio](https://aistudio.google.com/) with a free API key. Obtain your API key from Google AI Studio and keep it accessible, as you’ll need it for the next steps.

## Approach 1: Building an Imperative Agent With Python

The imperative approach is the most powerful method, giving you full control over agent behavior through code. Let’s build a simple greeting agent that demonstrates the core concepts.

### **Create the Project Structure**

Create a new directory for your agent project:

```
mkdir hello_agent
cd hello_agent
```

Create the following files inside the hello\_agent directory:

`__init__.py`

```
from . import agent
```

This file marks the directory as a Python package and imports the agent module.

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

The Agent class is the core building block in ADK. Notice how we define tools as regular Python functions with type hints and docstrings. ADK uses these to help the LLM understand when and how to call each tool.

`.env`

```
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

Replace the placeholder values with your actual credentials.

### **Run the Agent**

Navigate to the parent directory of your agent folder:

```
cd ..
```

Run the agent in terminal mode:

```
adk run hello_agent
```

You should see a prompt indicating the agent is running:

`Running agent hello_agent, type exit to exit.  
[user]:  
Try these interactions:  
[user]: Hello, my name is Jani  
[user]: What can you do?  
[user]: Tell me about yourself`

The agent will use the appropriate tools to respond. Type `exit` to quit.

## Approach 2: Building a Declarative Agent With YAML

The declarative approach using YAML configuration files simplifies agent creation, especially for straightforward use cases. The Agent Config feature generates the same underlying agent structure but with less code.

### **Create the Config-Based Project**

Use the ADK CLI to generate a config-based agent project:

```
adk create yaml_hello_agent --type=config
```

Accept the defaults and complete the steps.

[![](https://cdn.thenewstack.io/media/2025/11/b94370f5-adk-1-0-1024x601.png)](https://cdn.thenewstack.io/media/2025/11/b94370f5-adk-1-0-1024x601.png)

### **Define the Agent in YAML**

Open `yaml_hello_agent/root_agent.yaml` and replace its contents with:

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

The YAML structure mirrors the Python Agent class parameters, but in a more readable format. Notice how tools are referenced by their module path.

### **Create the Tools Module**

A powerful feature of ADK’s YAML config is that you can mix in Python code. Update `__init__.py` file in the `yaml_hello_agent` folder:

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

Your project structure should now look like:

`yaml_hello_agent/  
├── root_agent.yaml  
├── __init__.py  
└── .env`

### **Run the YAML-Based Agent**

Navigate to the parent directory and run:

```
adk run yaml_hello_agent
```

Test it with the same prompts:

```
[user]: Hi, I'm Jani
[user]: What are you?
```

The agent responds identically to the Python version but is defined entirely through configuration.

## Approach 3: Building an Agent With the Visual Agent Builder

The Visual Agent Builder, introduced in ADK v1.18.0, is a browser-based IDE that transforms how you build agents. It combines a visual workflow designer, configuration panels and an AI assistant that lets you design agents through drag-and-drop interactions and natural language conversations.

### **Launch the Visual Agent Builder**

From any directory, run:

```
adk web
```

[![](https://cdn.thenewstack.io/media/2025/11/4c9ef222-adk-1-1-1024x446.png)](https://cdn.thenewstack.io/media/2025/11/4c9ef222-adk-1-1-1024x446.png)

Open `http://localhost:8000/dev-ui/` in your browser to access the Visual Agent Builder.

Click the “+” button next to the dropdown and enter the name `visual_hello_agent`:

[![](https://cdn.thenewstack.io/media/2025/11/b5c12cc7-adk-1-2-1024x771.png)](https://cdn.thenewstack.io/media/2025/11/b5c12cc7-adk-1-2-1024x771.png)

Instead of manually configuring the agent, let’s use the AI Assistant. In the right panel, type:

`Create a simple greeting agent that can:  
1. Greet users by name when they introduce themselves  
2. Tell users about itself when asked  
Use gemini-2.5-flash as the model. Keep it simple with just two tools.`

[![](https://cdn.thenewstack.io/media/2025/11/71fbb3ba-adk-1-3-1024x563.png)](https://cdn.thenewstack.io/media/2025/11/71fbb3ba-adk-1-3-1024x563.png)

The AI Assistant will generate a complete agent configuration, including:

* Proper agent name and description
* Model selection
* Detailed instructions

[![](https://cdn.thenewstack.io/media/2025/11/fb5ddcc9-adk-1-4-1024x563.png)](https://cdn.thenewstack.io/media/2025/11/fb5ddcc9-adk-1-4-1024x563.png)

Click the Save button, then exit the builder mode. You can now chat with the agent.

[![](https://cdn.thenewstack.io/media/2025/11/d6c47e08-adk-1-5-1024x541.png)](https://cdn.thenewstack.io/media/2025/11/d6c47e08-adk-1-5-1024x541.png)

## Comparing the 3 Approaches

After building agents with all three methods, here’s how they compare:

| **Aspect** | **Imperative (Python)** | **Declarative (YAML)** | **Visual Builder** |
| --- | --- | --- | --- |
| **Best for** | Complex logic, CI/CD | Simple agents, collaboration | Prototyping, learning |
| **Learning curve** | Moderate | Low | Lowest |
| **Flexibility** | Highest | Medium | Medium |
| **Model support** | All (via LiteLLM) | Gemini only | Gemini only |
| **Version control** | Excellent | Excellent | Good (exports YAML) |
| **Non-developer friendly** | No | Somewhat | Yes |
| **Debugging** | Manual | Manual | Built-in tracing |

Key considerations:

* The **Python approach** is best when you need maximum control, custom integrations or support for non-Gemini models through LiteLLM.
* The **YAML approach** works well for straightforward agents where you want the simplicity of configuration files with the ability to mix in Python tools.
* The **Visual Builder** excels at rapid prototyping, learning ADK concepts and collaborating with non-developers who can describe requirements in natural language.

In practice, these approaches complement each other. You might use the Visual Builder to prototype and understand an architecture, then export the YAML for version control and CI/CD pipelines.

## Looking Ahead

This tutorial covered the essential steps to build your first AI agents using Google ADK’s three development approaches. Each method has its strengths, and the framework is designed so you can move fluidly between them — starting visually, exporting to YAML and dropping into Python when you need advanced functionality.

In subsequent tutorials, we’ll explore advanced ADK capabilities, including multiagent systems with Sequential, Parallel and Loop patterns, tool integration with Model Context Protocol (MCP) servers, session management and memory persistence, and deployment to Vertex AI Agent Engine. The foundation you’ve built here will serve you well as we tackle increasingly sophisticated agentic workflows.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)