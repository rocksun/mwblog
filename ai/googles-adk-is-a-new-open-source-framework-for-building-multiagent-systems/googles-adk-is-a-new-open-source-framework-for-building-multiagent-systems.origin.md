# Google’s ADK Is a New Open Source Framework for Building Multiagent Systems
![Featued image for: Google’s ADK Is a New Open Source Framework for Building Multiagent Systems](https://cdn.thenewstack.io/media/2025/04/95ee701a-img_0679-1024x768.jpg)
LAS VEGAS — [Google](https://cloud.google.com/?utm_content=inline+mention) today launched the Agent Development Kit (ADK), a new open source framework for building [multiagent systems](https://thenewstack.io/building-autonomous-systems-in-python-with-agentic-workflows/). This is the same framework that enables [Google Agentspace](https://cloud.google.com/products/agentspace), the company’s service for building AI agents in the enterprise.

Google promises that using the ADK, developers will be able to build an AI agent in under 100 lines of code. Using the ADK, developers can orchestrate their agent systems and create guardrails for the individual agents.

One interesting aspect of this is that Google notes that developers will be able to interact with their agents “in human-like conversations with ADK’s unique bidirectional audio and video streaming capabilities.” What this looks like exactly remains to be seen. Google promises to show a demo of this capability at Next, and we will update this story once we’ve seen more details.

The ADK currently only supports Python, with more languages launching later this year. It also supports the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) to allow these agents to connect to data from third-party services.

While Google says the framework is optimized for use with its own Gemini models and Vertex AI platform, ADK also supports more than 200 models from third-party providers like Anthropic, [Meta](https://about.meta.com/?utm_content=inline+mention), Mistral AI, AI21 Labs, CAMB.AI and Qodo.

Developers also get a choice of where they want to deploy these agents. Google’s own Vertex AI is the obvious choice here, but the framework supports any containerized environment as a deployment option (including Google’s own Cloud Run).

For enterprises that want a fully managed runtime for deploying their agents in production, Google now also offers Agent Engine. Agent Engine allows developers to deploy agents using any framework, whether that’s the ADK, LangGraph, Crew.ai or others.

To help developers get started, Google is also launching the Agent Garden today. The Agent Garden features pre-built agent patterns and components to jumpstart the development process.

A lot of this may sound familiar. There’s [LangChain/LangGraph](https://www.langchain.com/), of course, which has become somewhat of a standard for building agentic systems. [Microsoft](https://news.microsoft.com/?utm_content=inline+mention), too, offers an open source framework for building multiagent systems in the form of [AutoGen](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/core-concepts/agent-and-multi-agent-application.html). It, too, supports a variety of models (including Google’s Gemini models), though Microsoft’s emphasis for AutoGen seems to be more on connecting swarms of specialized agents to solve a complex problem, while Google is aiming for what seems to be a more general toolkit. [Solo.io’s](https://solo.io?utm_content=inline+mention)[ Kagent](https://thenewstack.io/meet-kagent-open-source-framework-for-ai-agents-in-kubernetes/), a framework for building multiagent systems on top of Kubernetes, was built on top of AutoGen, for example, and launched in March.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)