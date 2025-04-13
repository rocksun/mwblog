# The Top 7 MCP-Supported AI Frameworks
Create AI apps with Python and Typescript frameworks that leverage MCP servers to provide context to LLMs.

[Toolkits for AI agents](https://getstream.io/blog/ai-agent-toolkits/) expose developers to various APIs to equip AI solutions with tools to carry out tasks and ensure accurate results for user satisfaction. However, integrating these tools into AI apps and managing them can be messy. This article introduces you to an industry standard of providing context to LLMs and agents using [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP).
# LLM Context Provision Approaches and Specifications
By default, without giving LLMs and [AI chatbots](https://getstream.io/chat/solutions/ai-integration/) a proper context, they cannot fetch real-time information, execute code, call external tools and APIs, or even use a web browser on behalf of users. Developers can utilize the following approaches to fix this limitation of LLMs and agents.

[Composio](https://composio.dev/): Composio has specifications and a library of toolkits for integrating AI agents and LLMs. Aside from Composio’s library of ready-made toolkits, they recently announced[Composio MCP](https://mcp.composio.dev/?_gl=1*1tcsvb5*_ga*MTk0ODc0NjU2OS4xNzM3MjM1ODgx*_ga_J9WD56TEBS*MTc0MjQ1NTUwMC4yMC4wLjE3NDI0NTU1MDAuMC4wLjA.*_ga_YKMWVQS9W0*MTc0MjQ1NTUwMC4yMC4wLjE3NDI0NTU1MDAuNjAuMC4xNjQwNzI1NjY1), allowing developers to connect with 100+ MCP servers for IDEs. Check out the Composio MCP tool categories from the above link to connect several applications to your projects in MCP-supported IDEs like Cursor, Claude, and Windsurf.[Agents.json](https://docs.wild-card.ai/agentsjson/introduction): A specification built on OpenAI standards to ensure seamless and enhanced interactions between[AI agents](https://getstream.io/blog/xai-python-multi-agent/)and their access to APIs and external tools. Although Agent.json is an excellent specification, it is not widely used and has not been adopted, unlike MCP. Refer to its[GitHub repo](https://github.com/wild-card-ai/agents-json)to learn more and get started.**MCP**: MCP gives developers the best way to provide contextual data to LLMs and AI assistants to solve problems. For instance, you can build an MCP documentation server to offer complete access to your documentation to IDEs and agentic frameworks, just like using[llms.txt file](https://llmstxt.org/).
# What is MCP?
Think of MCP as a third evolution of LLMs. In the first evolution, we had LLMs capable of answering user prompts accurately if they found the queries in their training data. In this phase, they cannot meaningfully respond to prompts outside their training data since they don’t have access to external tools. In LLMs’ second evolution, we give them access to additional context (tools) that are not intuitive to work with. However, they are capable of helping the LLMs to predict and answer user intents accurately. The third evolution still consists of LLMs and tools, but we implement a proper infrastructure to give them access to external applications and ensure they are easily maintainable.

When building an AI service, your data may live in the cloud for an AI assistant app that answers [customer support](https://getstream.io/blog/build-a-customer-support-chat-bot-with-luis-react-hooks-azure-serverless-and-stream/) tickets in an enterprise setting. [MCP](https://www.anthropic.com/news/model-context-protocol) is an open-source protocol from [Anthropic](https://www.anthropic.com/) that you can use to connect your enterprise data to AI systems.

It offers a standard way to communicate and link content repositories (GitHub, Notion), development environments, web, and [business tools](https://github.com/atharvagupta2003/mcp-stripe) to assistive AI technologies. A popular and continuously growing use case of MCP is AI-assisted coding. Hundreds of MCP integrations with development environments and tools like [Cursor](https://docs.cursor.com/context/model-context-protocol) and [Windsurf](https://docs.codeium.com/windsurf/mcp) allow developers to connect and interact with external applications for development.

**Note**: This article aims to implement MCP with AI assistants and agentic systems developers built using Python and TypeScript, not IDE-based MCP integrations.
# How MCP Works
In the context of LLMs and agents, MCP assists them in providing meaningful responses to user queries outside their built-in knowledge. For instance, ask ChatGPT to message a particular Slack channel, check availability on your calendar, and schedule a meeting with a teammate today. You will be disappointed by ChatGPT’s response because it does not have access to these applications. Implementation of MCP helps these assistants output useful outcomes.

The first question developers typically ask is how MCP works. In MCP’s basic operation, a user sends a query to an agent. The agent then decides which MCP server and tool to call to get relevant information for the operation. The agent then uses the data from a specific tool to respond to the user.

# Why Adopt MCP for AI Agents and LLM-based Apps?
MCP is becoming a standard that helps developers build AI systems where these systems can effectively communicate with other external applications. Microsoft recently announced the integration of MCP in its [Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/introducing-model-context-protocol-mcp-in-copilot-studio-simplified-integration-with-ai-apps-and-agents/) to simplify how AI apps and agents access tools. Also, OpenAI has [announced](https://x.com/sama/status/1904957253456941061) the support of MCP across its products, such as the [Agents SDK](https://openai.github.io/openai-agents-python/) and the desktop app for ChatGPT. There is nothing wrong with equipping tools directly with AI assistants. However, it becomes cumbersome for an AI agent system consisting of several multi-agents performing multiple tasks, such as reading and answering emails, doing web scrapping, financial analysis, fetching real-time weather information, etc.

# An AI Agent With A Tool Integration
In the diagram above, three external tools are connected to the LLM. Managing and securing them all will be frustrating if the number increases to, for example, 100+. An improved approach will be accessing the same tools or more than 100+ of them through an MCP registry, as demonstrated in the following section.

# An AI Agent With MCP Integration
In this diagram, we combine the tools needed for the agentic system and access them through an MCP server to provide a more cohesive user experience. The MCP approach makes securing and managing these tools via a central location easier.

# Advantages of Using MCP Over Traditional Toolkits Integration
MCP has several key benefits over using the traditional way of integrating tools with AI agents. For example, the reliability of tool integration without MCP is questionable because it can result in several errors when making multiple API calls to external applications due to incompatible AI infrastructures. Before MCP, every tool you would like to add to agents must be implemented with custom code, which takes several weeks to implement.

**Architecture**: Unlike the pre-built tool specifications for AI agents, MCP has a clean and flexible architecture for interacting with tools and APIs.**Improved external tools access and management**: It provides tools access to AI models through a standardized interface to bridge the communication gap between LLMs and their interactions with third-party systems.**Addresses the limitations of a stand-alone tool implementation**: MCP tools are suitable for single-user scenarios and teams.**Community-driven**: MCP has many open-source servers and a developer ecosystem. It is also widely adopted in the developer community for many use cases.**Authentication**: It has a robust built-in authentication and permissions system to control tool access. For example, when using Composio-provided MCP tools, you can authenticate users with Google Sheets or Gmail.**Tools search**: Unlike the traditional method of installing, configuring, and integrating tools with AI chatbots, MCP makes searching for and finding external tools easier.**Scalability**: MCP is easily scalable to many users and applications.**Industry standard**: You can install hard-code tools to provide context to AI applications. However, MCP provides an industry standard to give the required context to agents and LLMs.
# Kinds of MCP Servers
The Anthropic’s specification of MCP has two forms of servers for adding tools to agents and AI projects. These MCP server connection types include the following.

**Server-Sent Events (SSE)**: Connects to a remote service via HTTP.**STDIO**: Allows execution of local commands and communication via standard I/O.
The framework you select to build your AI applications provides the necessary classes to connect to these servers.

# Access an Ecosystem of MCP Registries/Servers
There are several open-source libraries of hosted MCP tools to augment LLMs and agents to ensure the reliability of the responses they generate. These libraries of hosted MCP tools are called registries that provide curated collections of services. You can use their tools to connect your AI applications to the following registries. Also, you can use different server types, such as `uvx`
, which consists of Python-based tools without installation requirements. There is also a Docker option for running MCP tools and an `npx`
-based server that requires installing Node.js.

[MCP servers on GitHub](https://github.com/modelcontextprotocol/servers): A collection of community-built servers with additional MCP resources.[Glama Registry](https://glama.ai/mcp/servers?attributes=category%3Abrowser-automation): Production-ready and open-source MCP servers for developers.**Smithery Registry**: With[Smithery](https://smithery.ai/), developers can access 2000+ MCP servers to augment the capabilities of AI agents and LLMs.**OpenTools**:[OpenTools](https://opentools.com/)provides generative APIs for MCP tool use. You can access hundreds of ready-made MCP tools to implement with your AI projects. Using the OpenTools API, developers can extend the capabilities of LLMs’ web search, fetch real-time location data, and web scrape. The API supports Curl, Python, and TypeScript. Visit the OpenTools[quickstart guide](https://opentools.com/docs/quickstart)to use the API.
`from openai import OpenAI`
client = OpenAI(
base_url="https://api.opentools.com",
api_key="<OPENTOOLS_API_KEY>"
)
completion = client.chat.completions.create(
model="anthropic/claude-3.7-sonnet",
messages=[
{ "role": "user", "content": "Compare specs of top 5 EVs on caranddriver.com" }
],
tools=[{ "type": "mcp", "ref": "firecrawl" }]
)
[PulseMCP Registry](https://www.pulsemcp.com/): Using PulseMCP, you can browse hosted MCP tools and use cases for your AI projects. Check out[PulseMCP News](https://www.pulsemcp.com/posts)for recently trending MCP servers and apps.[mcp.run](https://www.mcp.run/): This registry gives developers access to hundreds of MCP apps for their businesses.[Composio Registry](https://mcp.composio.dev/): Composio’s SSE-based MCP servers allow easy integration of tools with different AI frameworks to build applications.[guMCP](https://www.gumloop.com/mcp): Gumloop’s guMCP provides free, open-source, and fully hosted[MCP servers](https://github.com/gumloop/GuMCP)for seamless integration with any AI app.
# Top 7 Client Frameworks to Add MCP to LLMs and Agents
Although MCP has become a buzzword, and all developer communities have recently been discussing it, it isn’t easy to know which MCP client frameworks to use for integrating with AI apps and agents. We researched and found the following leading MCP client platforms for Python and TypeScript-based agentic workflows and AI assistants.

**Note**: The following sections demonstrate the implementation of MCP in frameworks for building AI solutions and not MCP integration with AI code editors like Cursor or Windsurf.
# 1. Build a Git MCP Agent With OpenAI Agents SDK
When building agents with the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/mcp/), you connect to these community-built MCP servers using the SDK’s
and [MCPServerStdio](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerStdio)
classes. The following MCP agent implementation accesses the root directory of your local Git repo and responds to user queries about the repo.[MCPServerSse](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerSse)

`import asyncio`
import shutil
import streamlit as st
from agents import Agent, Runner, trace
from agents.mcp import MCPServer, MCPServerStdio
async def query_git_repo(mcp_server: MCPServer, directory_path: str, query: str):
agent = Agent(
name="Assistant",
instructions=f"Answer questions about the localgit repository at {directory_path}, use that for repo_path",
mcp_servers=[mcp_server],
)
with st.spinner(f"Running query: {query}"):
result = await Runner.run(starting_agent=agent, input=query)
return result.final_output
async def run_streamlit_app():
st.title("Local Git Repo Explorer")
st.write("This app allows you to query information about a local git repository.")
directory_path = st.text_input("Enter the path to the git repository:")
if directory_path:
# Common queries as buttons
col1, col2 = st.columns(2)
with col1:
if st.button("Most frequent contributor"):
query = "Who's the most frequent contributor?"
run_query(directory_path, query)
with col2:
if st.button("Last change summary"):
query = "Summarize the last change in the repository."
run_query(directory_path, query)
# Custom query
custom_query = st.text_input("Or enter your own query:")
if st.button("Run Custom Query") and custom_query:
run_query(directory_path, custom_query)
def run_query(directory_path, query):
if not shutil.which("uvx"):
st.error("uvx is not installed. Please install it with `pip install uvx`.")
return
async def execute_query():
async with MCPServerStdio(
cache_tools_list=True,
params={
"command": "python",
"args": [
"-m",
"mcp_server_git",
"--repository",
directory_path
]
},
) as server:
with trace(workflow_name="MCP Git Query"):
result = await query_git_repo(server, directory_path, query)
st.markdown("### Result")
st.write(result)
asyncio.run(execute_query())
if __name__ == "__main__":
st.set_page_config(
page_title="Local Git Repo Explorer",
page_icon="📊",
layout="centered"
)
# Change from async to synchronous implementation
# Since Streamlit doesn't work well with asyncio in the main thread
# Define a synchronous version of our app
def main_streamlit_app():
st.title("Local Git Repo Explorer")
st.write("This app allows you to query information about a Git repository.")
directory_path = st.text_input("Enter the path to the git repository:")
if directory_path:
# Common queries as buttons
col1, col2 = st.columns(2)
with col1:
if st.button("Most frequent contributor"):
query = "Who's the most frequent contributor?"
run_query(directory_path, query)
with col2:
if st.button("Last change summary"):
query = "Summarize the last change in the repository."
run_query(directory_path, query)
# Custom query
custom_query = st.text_input("Or enter your own query:")
if st.button("Run Custom Query") and custom_query:
run_query(directory_path, custom_query)
# Run the synchronous app
main_streamlit_app()
The code above integrates Streamlit with the OpenAI MCP agent, allowing you to chat with your local Git repo using the [Git MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/git). To run this example, you should install the following.

`pip install streamlit openai-agents mcp-server-git`
.- Then, export your OpenAI API keys using
`export OPENAI_API_KEY=sk-...`
. You should see a result similar to this preview when you run the Python file.
You can explore other examples of OpenAI MCP on [GitHub](https://github.com/openai/openai-agents-python/tree/main/examples/mcp).

One advantage of using the Agents SDK’s MCP integration is its built-in MCP agent [monitoring system](https://openai.github.io/openai-agents-python/tracing/) on OpenAI’s dashboard. This feature automatically captures your agents’ MCP operations, such as tool listing, `POST`
responses, and getting data about function calls. The image below represents traces of the Git MCP example in this section after running the code above. You can access all the logged information from your OpenAI's dashboard.

# 2. Build MCP AI Agents With Praison AI
[Praison AI](https://docs.praison.ai/) is a Python-based AI framework for building a team of agents. It provides the simplest way to add the MCP server tools to agentic workflows with a single line of code, just like you equip agents with traditional tooling.
The following example integrates the [Airbnb MCP server](https://github.com/openbnb-org/mcp-server-airbnb) with a Praison AI agent using a Streamlit UI to help find apartments in specified locations. You should install these to create your first MCP agent with Praison AI.

`pip install praisonaiagents mcp streamlit`
- Next, export your OpenAI API key
`export OPENAI_API_KEY='sk-proj-qZIGbi...`
.
Create a Python file, for example, **streamlit_praison_airbnb_mcp_agent.py**, and fill out its content with this code.

`import streamlit as st`
from praisonaiagents import Agent, MCP
st.title("🏠 Airbnb Booking Assistant")
# Create the agent
@st.cache_resource
def get_agent():
return Agent(
instructions="""You help book apartments on Airbnb.""",
llm="gpt-4o-mini",
tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
)
# Initialize chat history
if "messages" not in st.session_state:
st.session_state.messages = []
# Display chat history
for message in st.session_state.messages:
with st.chat_message(message["role"]):
st.markdown(message["content"])
# User input form
with st.form("booking_form"):
st.subheader("Enter your booking details")
destination = st.text_input("Destination:", "Paris")
col1, col2 = st.columns(2)
with col1:
check_in = st.date_input("Check-in date")
with col2:
check_out = st.date_input("Check-out date")
adults = st.number_input("Number of adults:", min_value=1, max_value=10, value=2)
submitted = st.form_submit_button("Search for accommodations")
if submitted:
search_agent = get_agent()
# Format the query
query = f"I want to book an apartment in {destination} from {check_in.strftime('%m/%d/%Y')} to {check_out.strftime('%m/%d/%Y')} for {adults} adults"
# Add user message to chat history
st.session_state.messages.append({"role": "user", "content": query})
# Display user message
with st.chat_message("user"):
st.markdown(query)
# Get response from the agent
with st.chat_message("assistant"):
with st.spinner("Searching for accommodations..."):
response = search_agent.start(query)
st.markdown(response)
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
# Allow for follow-up questions
if st.session_state.messages:
prompt = st.chat_input("Ask a follow-up question about the accommodations")
if prompt:
search_agent = get_agent()
# Add user message to chat history
st.session_state.messages.append({"role": "user", "content": prompt})
# Display user message
with st.chat_message("user"):
st.markdown(prompt)
# Get response from the agent
with st.chat_message("assistant"):
with st.spinner("Thinking..."):
response = search_agent.start(prompt)
st.markdown(response)
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
Running the sample code will call the required Airbnb MCP tools to look for apartments for you in a specific location, as demonstrated below.

You have noticed it adds MCP support to the agent with a single line of code `tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")`
, where `npx`
represents the command to run to start the MCP server. `-y`
is the command line argument to pass to the command. Refer [MCP Servers](https://openai.github.io/openai-agents-python/ref/mcp/server/) in the OpenAI Agents SDK documentation to learn more.

# 3. Using MCP for LangChain AI Apps
[LangChain](https://www.langchain.com/) has tool-calling support for [MCP](https://github.com/rectalogic/langchain-mcp/tree/main). This support allows you to set up Python functions to access different MCP servers and retrieve tools to perform tasks in AI projects. The sample code below connects to a secure MCP file system server, enabling an LLM to answer questions about any file you provide accurately.
`# Copyright (C) 2024 Andrew Wason`
# SPDX-License-Identifier: MIT
import asyncio
import pathlib
import sys
import typing as t
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import BaseTool
from langchain_groq import ChatGroq
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp import MCPToolkit
async def run(tools: list[BaseTool], prompt: str) -> str:
model = ChatGroq(model_name="llama-3.1-8b-instant", stop_sequences=None) # requires GROQ_API_KEY
tools_map = {tool.name: tool for tool in tools}
tools_model = model.bind_tools(tools)
messages: list[BaseMessage] = [HumanMessage(prompt)]
ai_message = t.cast(AIMessage, await tools_model.ainvoke(messages))
messages.append(ai_message)
for tool_call in ai_message.tool_calls:
selected_tool = tools_map[tool_call["name"].lower()]
tool_msg = await selected_tool.ainvoke(tool_call)
messages.append(tool_msg)
return await (tools_model | StrOutputParser()).ainvoke(messages)
async def main(prompt: str) -> None:
server_params = StdioServerParameters(
command="npx",
args=["-y", "@modelcontextprotocol/server-filesystem", str(pathlib.Path(__file__).parent.parent)],
)
async with stdio_client(server_params) as (read, write):
async with ClientSession(read, write) as session:
toolkit = MCPToolkit(session=session)
await toolkit.initialize()
response = await run(toolkit.get_tools(), prompt)
print(response)
if __name__ == "__main__":
prompt = sys.argv[1] if len(sys.argv) > 1 else "Read and summarize the file ./readme.md"
asyncio.run(main(prompt))
Before running this Python script, you should install the required dependencies, `langchain-core`
, `langchain-groq`
, and `langchain-mcp`
.

`pip install langchain-core langchain-groq langchain-mcp`
The MCP configuration above uses the `npx`
server type. So, you should install the `server-filesystem`
package.

`pm install -g @modelcontextprotocol/server-filesystem`
With all the required packages installed, if you add a file to your project and reference it in the Python script as shown in the sample code `./readme.md`
above, you should see an output similar to this image.

**Note**: This example was taken from LangChain’s [GitHub repo](https://github.com/rectalogic/langchain-mcp/tree/main).
# 4. Using MCP for Chainlit AI Apps
[Chainlit](https://docs.chainlit.io/advanced-features/mcp) is a platform for building AI applications in Python. It has built-in support for MCP servers, so you can configure your app to discover available MCP tools and integrate tool calls into your application’s flow for improved results. You can integrate Chainlit apps with [server-sent events](https://modelcontextprotocol.io/docs/concepts/transports#server-sent-events-sse) (SSE) and [command-line](https://introcs.cs.princeton.edu/python/code/stdio.py) (stdio) based services. In the following example, we will connect a Chainlit app to the [Linear MCP server](https://github.com/ibraheem4/linear-mcp) to allow the app to manage Linear issues, projects, and teams. You can use the Linear tools available in this example to create, update, search, and get user issues or add a comment to an issue.
## Configure Your Chainlit App To Connect to an MCP Server
Connecting your Chainlit app to access tools from an MCP server involves two main steps.

**Register the MCP connection**: In this step, you should implement Chainlit’s`on_mcp_connect`
async function to create a successful connection. You can also implement the`on_mcp_disconnect`
function to handle cleanup.
`# pip install chainlit`
import chainlit as cl
from mcp import ClientSession
@cl.on_mcp_connect
async def on_mcp_connect(connection, session: ClientSession):
"""Called when an MCP connection is established"""
# Your connection initialization code here
# This handler is required for MCP to work
@cl.on_mcp_disconnect
async def on_mcp_disconnect(name: str, session: ClientSession):
"""Called when an MCP connection is terminated"""
# Optional handler: Cleanup your code here
2. **Configure the MCP Client (Chainlit, LangChain, Mastra)**: For an MCP server to work with a Chainlit app, the client should provide connection details via the Chainlit’s UI. This configuration involves the following.

- A unique identifier representing the name of the connection.
**Client type**: You should specify whether you want to use`sse`
or`stdio`
. For`sse`
, you should add a URL endpoint. When using`stdio`
, a complete command (e.g.,`npx`
your-tool-package or`uvx`
your-tool-package) is required. A complete command example is shown below.
`npx -y linear-mcp-server --tools=all --api-key=lin_api_your_linear_API_Key`
After establishing an MCP server connection, you can execute tools using an MCP session. Finally, you integrate the MCP tools seamlessly with the models/agents of your Chainlit app via a tool call. You can find the complete source code for this Linear MCP integration from Chainlit’s example apps on [GitHub](https://github.com/Chainlit/cookbook/tree/main/mcp-linear).

When you get the above source code from Chainlit’s GitHub repo, run it, and set `npx -y linear-mcp-server --tools=all --api-key=lin_api_your_linear_API_Key`
through the Chainlit interface, you will then be able to create and update Linear issues/projects. However, as this example illustrates, performing these actions requires your Linear team's ID.

# 5. Integrate MCP for Agno AI Agents
[Agno](https://www.agno.com/) is a Python framework for building complex agentic workflows. It is popular for its simplicity, ease of use, and seamless integration with MCP servers. The example MCP implementation in this section integrates with a multi-agent team of four individual contributing agents, such as Airbnb, Google Maps, web search, and weather MCP agents. The Agno multi-agents collaborate to provide information about a trip in a specified location.
## Prerequisites
To test the Agno MCP implementation example in this section,

- Install Agno,
[DuckDuckGo](https://duckduckgo.com/), and[Exa](https://exa.ai/):`pip install -U openai agno duckduckgo-search exa-py`
. - Get a
[GOOGLE_MAPS_API_KEY](https://console.cloud.google.com/projectselector2/google/maps-apis/credentials)and add it to your project’s`.env`
file. - Get an
[APIFY_TOKEN](https://console.apify.com/settings/integrations)and add it to your`.env`
. - Validate the
[Google Address API](https://console.developers.google.com/apis/api/addressvalidation.googleapis.com).
## Configure the Agno MCP Team of Agents
For this step, you should define your MCP server parameters and manage multiple context managers with `AsyncExitStack`
. Then, create the agents and run them.

` # Define server parameters`
airbnb_server_params = StdioServerParameters(
command="npx",
args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"],
env=env,
)
maps_server_params = StdioServerParameters(
command="npx", args=["-y", "@modelcontextprotocol/server-google-maps"], env=env
)
# Use contextlib.AsyncExitStack to manage multiple async context managers
async with contextlib.AsyncExitStack() as stack:
# Create stdio clients for each server
airbnb_client, _ = await stack.enter_async_context(stdio_client(airbnb_server_params))
maps_client, _ = await stack.enter_async_context(stdio_client(maps_server_params))
# Create all agents
airbnb_agent = Agent(
name="Airbnb",
role="Airbnb Agent",
model=OpenAIChat("gpt-4o"),
tools=[airbnb_client],
instructions=dedent("""\
You are an agent that can find Airbnb listings for a given location.\
"""),
add_datetime_to_instructions=True,
)
Get the complete [source code](https://github.com/agno-agi/agno/blob/main/cookbook/examples/teams/coordinate/travel_planner_mcp_team.py) from Agno’s GitHub repo. Installing the required packages, performing all the above configurations, and running the complete GitHub sample code should display an output similar to this preview.

# 6. Using MCP for Upsonic Agents
[Upsonic](https://docs.upsonic.ai/introduction) is a Python framework for creating AI agents. Using Upsonic, you can build your agents, define tasks for the agents, and handle each task definition with an [MCP tool](https://docs.upsonic.ai/concepts/mcp_tools), as demonstrated in the sample code below.
`import os`
from dotenv import load_dotenv
from upsonic import Task, Agent, Direct
from upsonic.client.tools import Search # Adding Search as a fallback tool
# Load environment variables from .env file
load_dotenv()
# Get the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
raise ValueError("OPENAI_API_KEY not found in .env file")
# Set your OpenAI API key for the session
os.environ["OPENAI_API_KEY"] = openai_api_key
# Define the HackerNews MCP tool
# Using the correct MCP setup for HackerNews based on Upsonic documentation
class HackerNewsMCP:
command = "uvx"
args = ["mcp-hn"]
# No environment variables are needed for this MCP
# Create a task to analyze the latest HackerNews stories
# Adding Search as a fallback in case HackerNews MCP fails
task = Task(
"Analyze the top 5 HackerNews stories for today. Provide a brief summary of each story, "
"identify any common themes or trends, and highlight which stories might be most relevant "
"for someone interested in AI and software development.",
tools=[HackerNewsMCP, Search] # Include both HackerNews MCP and Search tools
)
# Create an agent specialized in tech news analysis
agent = Agent(
"Tech News Analyst",
company_url="https://news.ycombinator.com/",
company_objective="To provide insightful analysis of tech industry news and trends"
)
# Execute the task with the agent and print the results
print("Analyzing HackerNews stories...")
agent.print_do(task)
# Alternatively, you can use a Direct LLM call if the task is straightforward
# print("Direct analysis of HackerNews stories...")
# Direct.print_do(task)
# If you want to access the response programmatically:
# agent.do(task)
# result = task.response
# print(result)
In the example above, we create an AI agent in Upsonic that retrieves the top five most recent stories from Hackernews. If you `pip install upsonic`
and run the Python code above, you should see an output similar to this image.

# 7. Using MCP for Mastra Agents
[Mastra](https://mastra.ai/) is a TypeScript framework for building prototypes and production-ready AI agents. Like Chainlit, Mastra offers a standardized way to connect to MCP servers to access a wide range of tools with `stdio`
or `sse`
-based connections.
To connect your Mastra agent to an MCP server, you should use its `MCPConfiguration`
class. This class handles multiple server connections, such as lifecycle, namespacing, and tools, in any Mastra agentic workflow. Creating a connection between a Master app and an MCP server involves the following.

- Create an instance of the
`MCPConfiguration`
class and add server configurations. - Retrieve MCP tools using the
`getTools()`
or`getToolsets()`
method.
The sample code below represents a basic usage of implementing an MCP server with a Mastra agent.

`import { MCPConfiguration } from "@mastra/mcp";`
import { Agent } from "@mastra/core/agent";
import { openai } from "@ai-sdk/openai";
const mcp = new MCPConfiguration({
servers: {
stockPrice: {
command: "npx",
args: ["tsx", "stock-price.ts"],
env: {
API_KEY: "your-api-key",
},
},
weather: {
url: new URL("http://localhost:8080/sse"),
},
},
});
// Create an agent with access to all tools
const agent = new Agent({
name: "Multi-tool Agent",
instructions: "You have access to multiple tool servers.",
model: openai("gpt-4"),
tools: await mcp.getTools(),
});
Refer to Mastra’s [MCPConfiguration](https://mastra.ai/docs/reference/tools/mcp-configuration) to learn more.

# Challenges and What’s Next for MCP in LLM Apps and Agents
This tutorial introduces you to MCP and explains why it has become popular in the developer community. We highlight MCP integration with IDEs such as Cursor and Windsurf. In addition to the above, we implemented MCP in seven different Python and TypeScript frameworks for building LLM-based apps, AI assistants, and agents.

MCP’s awesomeness also comes with the following [challenges](https://x.com/tobi/status/1891137636720419191). When searching for MCP tools for your projects, you may find it challenging to examine or verify the quality and see the exact applications for your AI project. This is because its tool search and discovery are not yet standardized. Also, its configuration does not offer a consistent user experience due to MCP server providers’ different schemas.

Currently, the MCP ecosystem is [discussing](https://github.com/orgs/modelcontextprotocol/discussions/159) standardizing various aspects of MCP. There might be a standard way to install MCP-based apps in the future, just like how we `pip install`
packages in Python. [PulseMCP](https://www.pulsemcp.com/) also attempts to make browsing and discovering MCP easier.