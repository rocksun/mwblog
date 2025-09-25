[Data Commons](https://datacommons.org/) may be one of the lesser-known Google initiatives, but the project, which collects [public datasets](https://datacommons.org/data/agriculture) across a broad set of topics and geographies (and the tools to query and visualize them), can come in quite handy when you’re looking for an authoritative source of data to enrich your applications or proprietary data sets. But in this new era of AI, there are also new use cases for Data Commons, including grounding large language models (LLMs) with real-world statistical information to reduce hallucinations when AI agents have to answer factual questions.

To make it easier for developers to bring this vast trove of data to their agents, Data Commons is launching its Model Context Protocol server today without having to interact with the Data Commons APIs directly.

“To compile a reliable report from traditional databases, users would need to work across datasets and manually pull data,” Google explains in today’s announcement. “Agents, however, understand complex queries and are able to fetch and compile the needed data quickly.”

## Getting Started

Google is providing tutorials for getting started with the Data Commons MCP Server for its own [Gemini CLI](https://github.com/datacommonsorg/agent-toolkit/blob/main/docs/quickstart.md) and [Agent Development Kit](https://github.com/datacommonsorg/agent-toolkit), as well as instructions for [Google Collab users](https://colab.research.google.com/github/datacommonsorg/agent-toolkit/blob/main/notebooks/datacommons_mcp_tools_with_custom_agent.ipynb). Since it’s a standard MCP server, though, there shouldn’t be any friction to integrate it into any agent workflow, though.

With this, Google says, agents will be able to answer questions like” compare the life expectancy, economic inequality, and GDP growth for BRICS nations” and “generate a concise report on income vs diabetes in US counties.”

## Data Commons MCP in Action: The ONE Campaign Partnership

To trial the MCP server, Google worked with the [ONE Campaign](https://www.one.org/us/), a non-profit that aims to “bring together grassroots activists, cutting-edge data analysis, trusted messengers, and decades of expertise to build political capital and drive policies and investments to create a more resilient, equitable future.” Together, the two organizations built the [ONE Data](https://data.one.org/) platform that combines ONE’s global development data and the public datasets in Data Commons. Google and ONE then built an agent on top of this platform that allows anyone to search through these data sources in natural language quickly.

“There is an urgent need to strengthen health systems in developing countries, but finding reliable data on health financing is a significant challenge — truly searching for the proverbial needle in a haystack,” the company notes. “The information is scattered across thousands of disparate silos, buried in different reporting formats, organized by technical jargon and stored in several isolated databases. Now, for example, if you want to identify which countries are at risk from donor cuts, you can quickly search for countries that rely most on external funding for health and are therefore most vulnerable to aid reductions or debt shocks.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)