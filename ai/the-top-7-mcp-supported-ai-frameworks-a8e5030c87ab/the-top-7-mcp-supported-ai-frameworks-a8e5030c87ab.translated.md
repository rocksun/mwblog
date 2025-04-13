# 支持 MCP 的 7 大 AI 框架

使用 Python 和 Typescript 框架创建 AI 应用程序，这些框架利用 MCP 服务器为 LLM 提供上下文。

[AI 代理工具包](https://getstream.io/blog/ai-agent-toolkits/) 向开发人员公开各种 API，使 AI 解决方案能够使用工具来执行任务并确保准确的结果，从而提高用户满意度。但是，将这些工具集成到 AI 应用程序中并对其进行管理可能会很麻烦。本文向您介绍使用[模型上下文协议](https://modelcontextprotocol.io/introduction) (MCP) 为 LLM 和代理提供上下文的行业标准。

# LLM 上下文配置方法和规范

默认情况下，如果不为 LLM 和 [AI 聊天机器人](https://getstream.io/chat/solutions/ai-integration/) 提供适当的上下文，它们将无法获取实时信息、执行代码、调用外部工具和 API，甚至无法代表用户使用 Web 浏览器。开发人员可以利用以下方法来解决 LLM 和代理的这一限制。

[Composio](https://composio.dev/): Composio 具有用于集成 AI 代理和 LLM 的规范和工具包库。除了 Composio 的现成工具包库之外，他们最近还宣布了 [Composio MCP](https://mcp.composio.dev/?_gl=1*1tcsvb5*_ga*MTk0ODc0NjU2OS4xNzM3MjM1ODgx*_ga_J9WD56TEBS*MTc0MjQ1NTUwMC4yMC4wLjE3NDI0NTU1MDAuMC4wLjA.*_ga_YKMWVQS9W0*MTc0MjQ1NTUwMC4yMC4wLjE3NDI0NTU1MDAuNjAuMC4xNjQwNzI1NjY1)，允许开发人员连接到 100 多个用于 IDE 的 MCP 服务器。从上面的链接查看 Composio MCP 工具类别，以将多个应用程序连接到 MCP 支持的 IDE（如 Cursor、Claude 和 Windsurf）中的项目。

[Agents.json](https://docs.wild-card.ai/agentsjson/introduction): 一种基于 OpenAI 标准构建的规范，旨在确保 [AI 代理](https://getstream.io/blog/xai-python-multi-agent/) 及其对 API 和外部工具的访问之间的无缝和增强的交互。虽然 Agent.json 是一个出色的规范，但它没有得到广泛使用和采用，这与 MCP 不同。请参阅其 [GitHub repo](https://github.com/wild-card-ai/agents-json) 以了解更多信息并开始使用。

**MCP**: MCP 为开发人员提供了向 LLM 和 AI 助手提供上下文数据以解决问题的最佳方式。例如，您可以构建一个 MCP 文档服务器，以像使用 [llms.txt file](https://llmstxt.org/) 一样，为 IDE 和代理框架提供对其文档的完全访问权限。

# 什么是 MCP？

将 MCP 视为 LLM 的第三次进化。在第一次进化中，如果 LLM 在其训练数据中找到查询，它们就能够准确地回答用户提示。在此阶段，由于他们无法访问外部工具，因此他们无法有意义地响应其训练数据之外的提示。在 LLM 的第二次进化中，我们让他们访问额外的上下文（工具），这些上下文并不容易使用。但是，它们能够帮助 LLM 准确地预测和回答用户意图。第三次进化仍然由 LLM 和工具组成，但我们实施了适当的基础设施，使他们能够访问外部应用程序并确保它们易于维护。

在构建 AI 服务时，您的数据可能位于云中，用于在企业环境中回答 [客户支持](https://getstream.io/blog/build-a-customer-support-chat-bot-with-luis-react-hooks-azure-serverless-and-stream/) 工单的 AI 助手应用程序。[MCP](https://www.anthropic.com/news/model-context-protocol) 是来自 [Anthropic](https://www.anthropic.com/) 的开源协议，您可以使用它将您的企业数据连接到 AI 系统。

它提供了一种标准方式来连接内容存储库（GitHub、Notion）、开发环境、Web 和 [业务工具](https://github.com/atharvagupta2003/mcp-stripe) 到辅助 AI 技术。MCP 的一个流行的且不断增长的用例是 AI 辅助编码。数百个与开发环境和工具（如 [Cursor](https://docs.cursor.com/context/model-context-protocol) 和 [Windsurf](https://docs.codeium.com/windsurf/mcp)）的 MCP 集成允许开发人员连接外部应用程序并与之交互以进行开发。

**注意**：本文旨在实现 MCP 与 AI 助手和代理系统开发人员使用 Python 和 TypeScript 构建的集成，而不是基于 IDE 的 MCP 集成。

# MCP 的工作原理

在 LLM 和代理的上下文中，MCP 协助他们对用户查询提供超出其内置知识的有意义的响应。例如，要求 ChatGPT 向特定的 Slack 频道发送消息、检查您日历上的可用性以及安排今天与团队成员的会议。您会对 ChatGPT 的响应感到失望，因为它无权访问这些应用程序。MCP 的实施有助于这些助手输出有用的结果。
开发者通常会问的第一个问题是 MCP 如何工作。在 MCP 的基本操作中，用户向代理发送查询。然后，代理决定调用哪个 MCP 服务器和工具来获取操作的相关信息。然后，代理使用来自特定工具的数据来响应用户。

## 为什么为 AI 代理和基于 LLM 的应用采用 MCP？

MCP 正在成为一种标准，可以帮助开发者构建 AI 系统，使这些系统能够有效地与其他外部应用程序通信。微软最近宣布在其 [Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/introducing-model-context-protocol-mcp-in-copilot-studio-simplified-integration-with-ai-apps-and-agents/) 中集成 MCP，以简化 AI 应用和代理访问工具的方式。此外，OpenAI 已经[宣布](https://x.com/sama/status/1904957253456941061)在其产品（如 [Agents SDK](https://openai.github.io/openai-agents-python/) 和 ChatGPT 的桌面应用）中支持 MCP。直接为 AI 助手配备工具并没有错。但是，对于由多个执行多项任务的多代理组成的 AI 代理系统来说，这会变得很麻烦，例如读取和回复电子邮件、进行网络抓取、财务分析、获取实时天气信息等。

## 具有工具集成的 AI 代理

在上图中，三个外部工具连接到 LLM。如果数量增加到 100+，管理和保护所有这些工具将会令人沮丧。一种改进的方法是通过 MCP 注册表访问相同的工具或超过 100+ 的工具，如下一节所示。

## 具有 MCP 集成的 AI 代理

在此图中，我们组合了代理系统所需的工具，并通过 MCP 服务器访问它们，以提供更具凝聚力的用户体验。MCP 方法使通过中心位置保护和管理这些工具变得更加容易。

## 使用 MCP 优于传统工具包集成的优势

与使用传统方式将工具与 AI 代理集成相比，MCP 具有几个关键优势。例如，没有 MCP 的工具集成的可靠性值得怀疑，因为它在由于不兼容的 AI 基础设施而对外部应用程序进行多次 API 调用时可能导致多个错误。在 MCP 之前，您想要添加到代理的每个工具都必须使用自定义代码来实现，这需要几周的时间才能实现。

**架构**：与 AI 代理的预构建工具规范不同，MCP 具有用于与工具和 API 交互的清晰灵活的架构。**改进的外部工具访问和管理**：它通过标准化接口为 AI 模型提供工具访问，以弥合 LLM 与其与第三方系统交互之间的通信差距。**解决了独立工具实现的局限性**：MCP 工具适用于单用户场景和团队。**社区驱动**：MCP 有许多开源服务器和一个开发者生态系统。它还在开发者社区中被广泛采用，用于许多用例。**身份验证**：它具有强大的内置身份验证和权限系统来控制工具访问。例如，当使用 Composio 提供的 MCP 工具时，您可以使用 Google Sheets 或 Gmail 对用户进行身份验证。**工具搜索**：与安装、配置和将工具与 AI 聊天机器人集成的传统方法不同，MCP 使搜索和查找外部工具变得更加容易。**可扩展性**：MCP 易于扩展到许多用户和应用程序。**行业标准**：您可以安装硬编码工具来为 AI 应用程序提供上下文。但是，MCP 提供了一个行业标准，为代理和 LLM 提供所需的上下文。

## MCP 服务器的种类

Anthropic 的 MCP 规范有两种服务器形式，用于向代理和 AI 项目添加工具。这些 MCP 服务器连接类型包括以下内容。

**服务器发送事件 (SSE)**：通过 HTTP 连接到远程服务。
**STDIO**：允许执行本地命令并通过标准 I/O 进行通信。
您选择构建 AI 应用程序的框架提供了连接到这些服务器所需的类。

## 访问 MCP 注册表/服务器的生态系统

有几个托管 MCP 工具的开源库可以增强 LLM 和代理，以确保它们生成的响应的可靠性。这些托管 MCP 工具的库称为注册表，提供精选的服务集合。您可以使用它们的工具将您的 AI 应用程序连接到以下注册表。此外，您可以使用不同的服务器类型，例如 `uvx`，它由基于 Python 的工具组成，无需安装要求。还有一个用于运行 MCP 工具的 Docker 选项和一个基于 `npx` 的服务器，需要安装 Node.js。
[GitHub 上的 MCP 服务器](https://github.com/modelcontextprotocol/servers)：一个由社区构建的服务器集合，包含额外的 MCP 资源。[Glama Registry](https://glama.ai/mcp/servers?attributes=category%3Abrowser-automation)：为开发者提供的生产就绪型开源 MCP 服务器。**Smithery Registry**：通过[Smithery](https://smithery.ai/)，开发者可以访问 2000 多个 MCP 服务器，以增强 AI 代理和 LLM 的能力。**OpenTools**：[OpenTools](https://opentools.com/) 为 MCP 工具的使用提供生成式 API。您可以访问数百个现成的 MCP 工具，以在您的 AI 项目中实施。使用 OpenTools API，开发者可以扩展 LLM 的网络搜索、获取实时位置数据和网络抓取功能。该 API 支持 Curl、Python 和 TypeScript。访问 OpenTools [快速入门指南](https://opentools.com/docs/quickstart) 以使用该 API。

```python
from openai import OpenAI
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
```

[PulseMCP Registry](https://www.pulsemcp.com/)：使用 PulseMCP，您可以浏览托管的 MCP 工具和 AI 项目的用例。查看 [PulseMCP 新闻](https://www.pulsemcp.com/posts)，了解最近流行的 MCP 服务器和应用程序。[mcp.run](https://www.mcp.run/)：此注册表使开发者可以访问数百个用于其业务的 MCP 应用程序。[Composio Registry](https://mcp.composio.dev/)：Composio 基于 SSE 的 MCP 服务器允许将工具与不同的 AI 框架轻松集成，以构建应用程序。[guMCP](https://www.gumloop.com/mcp)：Gumloop 的 guMCP 提供免费、开源且完全托管的 [MCP 服务器](https://github.com/gumloop/GuMCP)，可与任何 AI 应用程序无缝集成。

# 将 MCP 添加到 LLM 和 Agent 的 7 大客户端框架

虽然 MCP 已成为一个流行语，并且所有开发者社区最近都在讨论它，但要知道使用哪些 MCP 客户端框架与 AI 应用程序和代理集成并不容易。我们研究并找到了以下领先的 MCP 客户端平台，用于基于 Python 和 TypeScript 的代理工作流程和 AI 助手。

**注意**：以下部分演示了在用于构建 AI 解决方案的框架中 MCP 的实现，而不是 MCP 与 AI 代码编辑器（如 Cursor 或 Windsurf）的集成。

# 1. 使用 OpenAI Agents SDK 构建 Git MCP 代理

在使用 [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/mcp/) 构建代理时，您可以使用 SDK 的 [MCPServerSse](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerSse) 和 [MCPServerStdio](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerStdio) 类连接到这些社区构建的 MCP 服务器。以下 MCP 代理实现访问本地 Git 存储库的根目录，并响应用户关于该存储库的查询。

```python
import asyncio
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
    run_streamlit_app()
```
# 从异步实现更改为同步实现

# 由于 Streamlit 在主线程中与 asyncio 配合不佳

# 定义应用程序的同步版本
```python
def main_streamlit_app():
    st.title("本地 Git 仓库浏览器")
    st.write("此应用程序允许您查询有关 Git 仓库的信息。")
    directory_path = st.text_input("输入 git 仓库的路径：")
    if directory_path:
        # 作为按钮的常用查询
        col1, col2 = st.columns(2)
        with col1:
            if st.button("最频繁的贡献者"):
                query = "谁是最频繁的贡献者？"
                run_query(directory_path, query)
        with col2:
            if st.button("上次更改摘要"):
                query = "总结仓库中的上次更改。"
                run_query(directory_path, query)
        # 自定义查询
        custom_query = st.text_input("或输入您自己的查询：")
        if st.button("运行自定义查询") and custom_query:
            run_query(directory_path, custom_query)

# 运行同步应用程序
main_streamlit_app()
```

上面的代码将 Streamlit 与 OpenAI MCP 代理集成，允许您使用 [Git MCP 服务器](https://github.com/modelcontextprotocol/servers/tree/main/src/git) 与本地 Git 仓库聊天。要运行此示例，您应该安装以下内容。

```bash
pip install streamlit openai-agents mcp-server-git
```

然后，使用以下命令导出您的 OpenAI API 密钥

```bash
export OPENAI_API_KEY=sk-...
```

运行 Python 文件时，您应该会看到类似于此预览的结果。
您可以在 [GitHub](https://github.com/openai/openai-agents-python/tree/main/examples/mcp) 上浏览 OpenAI MCP 的其他示例。

使用 Agents SDK 的 MCP 集成的一个优势是其内置的 MCP 代理 [监控系统](https://openai.github.io/openai-agents-python/tracing/) 在 OpenAI 的仪表板上。此功能会自动捕获您代理的 MCP 操作，例如工具列表、`POST`
响应以及获取有关函数调用的数据。下图表示运行上述代码后，本节中 Git MCP 示例的跟踪。您可以从 OpenAI 的仪表板访问所有记录的信息。

# 2. 使用 Praison AI 构建 MCP AI 代理

[Praison AI](https://docs.praison.ai/) 是一个基于 Python 的 AI 框架，用于构建代理团队。它提供了以单行代码将 MCP 服务器工具添加到代理工作流程的最简单方法，就像您为代理配备传统工具一样。
以下示例将 [Airbnb MCP 服务器](https://github.com/openbnb-org/mcp-server-airbnb) 与 Praison AI 代理集成，使用 Streamlit UI 来帮助查找指定位置的公寓。您应该安装这些来使用 Praison AI 创建您的第一个 MCP 代理。

```bash
pip install praisonaiagents mcp streamlit
```

接下来，导出您的 OpenAI API 密钥

```bash
export OPENAI_API_KEY='sk-proj-qZIGbi...`
```

创建一个 Python 文件，例如 **streamlit_praison_airbnb_mcp_agent.py**，并使用此代码填充其内容。

```python
import streamlit as st
from praisonaiagents import Agent, MCP

st.title("🏠 Airbnb 预订助手")

# 创建代理
@st.cache_resource
def get_agent():
    return Agent(
        instructions="""您帮助在 Airbnb 上预订公寓。""",
        llm="gpt-4o-mini",
        tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
    )

# 初始化聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示聊天记录
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 用户输入表单
with st.form("booking_form"):
    st.subheader("输入您的预订详细信息")
    destination = st.text_input("目的地：", "Paris")
    col1, col2 = st.columns(2)
    with col1:
        check_in = st.date_input("入住日期")
    with col2:
        check_out = st.date_input("退房日期")
    adults = st.number_input("成人人数：", min_value=1, max_value=10, value=2)
    submitted = st.form_submit_button("搜索住宿")

    if submitted:
        search_agent = get_agent()
        # 格式化查询
        query = f"我想在 {destination} 预订一套公寓，从 {check_in.strftime('%m/%d/%Y')} 到 {check_out.strftime('%m/%d/%Y')}，供 {adults} 位成人入住"
        # 将用户消息添加到聊天记录
        st.session_state.messages.append({"role": "user", "content": query})
        # 显示用户消息
        with st.chat_message("user"):
            st.markdown(query)
        # 从代理获取响应
        with st.chat_message("assistant"):
            with st.spinner("正在搜索住宿..."):
                response = search_agent.start(query)
                st.markdown(response)
        # 将助手响应添加到聊天记录
        st.session_state.messages.append({"role": "assistant", "content": response})

# 允许后续问题
if st.session_state.messages:
    prompt = st.chat_input("询问有关住宿的后续问题")
    if prompt:
        search_agent = get_agent()
        # 将用户消息添加到聊天记录
        st.session_state.messages.append({"role": "user", "content": prompt})
        # 显示用户消息
        with st.chat_message("user"):
            st.markdown(prompt)
        # 从代理获取响应
        with st.chat_message("assistant"):
            with st.spinner("思考中..."):
                response = search_agent.start(prompt)
```
st.markdown(response)

# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})

运行示例代码将调用所需的 Airbnb MCP 工具，以在特定位置为您查找公寓，如下所示。

您已经注意到它通过单行代码 `tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")` 向代理添加了 MCP 支持，其中 `npx` 表示要运行以启动 MCP 服务器的命令。`-y` 是要传递给命令的命令行参数。请参阅 OpenAI Agents SDK 文档中的 [MCP Servers](https://openai.github.io/openai-agents-python/ref/mcp/server/) 以了解更多信息。

# 3. 将 MCP 用于 LangChain AI 应用

[LangChain](https://www.langchain.com/) 具有对 [MCP](https://github.com/rectalogic/langchain-mcp/tree/main) 的工具调用支持。此支持允许您设置 Python 函数以访问不同的 MCP 服务器并检索工具，以在 AI 项目中执行任务。下面的示例代码连接到安全的 MCP 文件系统服务器，使 LLM 能够准确地回答有关您提供的任何文件的问题。

```python
# Copyright (C) 2024 Andrew Wason
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
    model = ChatGroq(model_name="llama-3.1-8b-instant", stop_sequences=None)  # requires GROQ_API_KEY
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
```

在运行此 Python 脚本之前，您应该安装所需的依赖项 `langchain-core`、`langchain-groq` 和 `langchain-mcp`。

```bash
pip install langchain-core langchain-groq langchain-mcp
```

上面的 MCP 配置使用 `npx` 服务器类型。因此，您应该安装 `server-filesystem` 包。

```bash
pm install -g @modelcontextprotocol/server-filesystem
```

安装完所有必需的软件包后，如果您将文件添加到您的项目并在 Python 脚本中引用它，如示例代码 `./readme.md` 所示，您应该会看到类似于此图像的输出。

**注意**：此示例取自 LangChain 的 [GitHub repo](https://github.com/rectalogic/langchain-mcp/tree/main)。

# 4. 将 MCP 用于 Chainlit AI 应用

[Chainlit](https://docs.chainlit.io/advanced-features/mcp) 是一个用于在 Python 中构建 AI 应用程序的平台。它内置了对 MCP 服务器的支持，因此您可以配置您的应用程序以发现可用的 MCP 工具，并将工具调用集成到您的应用程序流程中，以获得更好的结果。您可以将 Chainlit 应用程序与 [server-sent events](https://modelcontextprotocol.io/docs/concepts/transports#server-sent-events-sse) (SSE) 和 [command-line](https://introcs.cs.princeton.edu/python/code/stdio.py) (stdio) 基于服务集成。在以下示例中，我们将 Chainlit 应用程序连接到 [Linear MCP server](https://github.com/ibraheem4/linear-mcp)，以允许该应用程序管理 Linear 问题、项目和团队。您可以使用此示例中提供的 Linear 工具来创建、更新、搜索和获取用户问题或向问题添加评论。

## 配置您的 Chainlit 应用程序以连接到 MCP 服务器

将您的 Chainlit 应用程序连接到 MCP 服务器以访问工具涉及两个主要步骤。

**注册 MCP 连接**：在此步骤中，您应该实现 Chainlit 的 `on_mcp_connect` 异步函数以创建成功的连接。您还可以实现 `on_mcp_disconnect` 函数来处理清理。

```python
# pip install chainlit
import chainlit as cl
from mcp import ClientSession


@cl.on_mcp_connect
async def on_mcp_connect(connection, session: ClientSession):
    """Called when an MCP connection is established"""
```
# 此处是你的连接初始化代码
# 此处理程序是 MCP 正常工作所必需的
`@cl.on_mcp_disconnect`
async def on_mcp_disconnect(name: str, session: ClientSession):
    """当 MCP 连接终止时调用"""
    # 可选处理程序：在此处清理你的代码

2. **配置 MCP 客户端 (Chainlit, LangChain, Mastra)**：为了使 MCP 服务器与 Chainlit 应用程序一起工作，客户端应通过 Chainlit 的 UI 提供连接详细信息。此配置涉及以下内容。

- 代表连接名称的唯一标识符。
**客户端类型**：你应该指定是否要使用`sse` 或`stdio`。对于`sse`，你应该添加一个 URL 端点。当使用`stdio`时，需要一个完整的命令（例如，`npx` your-tool-package 或`uvx` your-tool-package）。下面显示了一个完整的命令示例。
`npx -y linear-mcp-server --tools=all --api-key=lin_api_your_linear_API_Key`
建立 MCP 服务器连接后，你可以使用 MCP 会话执行工具。最后，你可以通过工具调用将 MCP 工具与 Chainlit 应用程序的模型/代理无缝集成。你可以在 [GitHub](https://github.com/Chainlit/cookbook/tree/main/mcp-linear) 上的 Chainlit 示例应用程序中找到此 Linear MCP 集成的完整源代码。

当你从 Chainlit 的 GitHub 仓库获取上述源代码，运行它，并通过 Chainlit 界面设置 `npx -y linear-mcp-server --tools=all --api-key=lin_api_your_linear_API_Key` 时，你将能够创建和更新 Linear 问题/项目。但是，正如本示例所示，执行这些操作需要你的 Linear 团队的 ID。

# 5. 集成 MCP 以用于 Agno AI 代理
[Agno](https://www.agno.com/) 是一个用于构建复杂代理工作流程的 Python 框架。它以其简单性、易用性以及与 MCP 服务器的无缝集成而广受欢迎。本节中的示例 MCP 实现与由四个独立贡献代理（例如 Airbnb、Google Maps、Web 搜索和天气 MCP 代理）组成的多代理团队集成。Agno 多代理协同工作以提供有关指定位置的旅行信息。

## 前提条件
要测试本节中的 Agno MCP 实现示例，

- 安装 Agno，
[DuckDuckGo](https://duckduckgo.com/) 和 [Exa](https://exa.ai/):`pip install -U openai agno duckduckgo-search exa-py`。
- 获取
[GOOGLE_MAPS_API_KEY](https://console.cloud.google.com/projectselector2/google/maps-apis/credentials) 并将其添加到你的项目的 `.env` 文件中。
- 获取
[APIFY_TOKEN](https://console.apify.com/settings/integrations) 并将其添加到你的 `.env` 中。
- 验证
[Google Address API](https://console.developers.google.com/apis/api/addressvalidation.googleapis.com)。

## 配置 Agno MCP 代理团队
对于此步骤，你应该定义你的 MCP 服务器参数，并使用 `AsyncExitStack` 管理多个上下文管理器。然后，创建代理并运行它们。

` # 定义服务器参数`
```python
airbnb_server_params = StdioServerParameters(
    command="npx",
    args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"],
    env=env,
)
maps_server_params = StdioServerParameters(
    command="npx", args=["-y", "@modelcontextprotocol/server-google-maps"], env=env
)
# 使用 contextlib.AsyncExitStack 管理多个异步上下文管理器
async with contextlib.AsyncExitStack() as stack:
    # 为每个服务器创建 stdio 客户端
    airbnb_client, _ = await stack.enter_async_context(stdio_client(airbnb_server_params))
    maps_client, _ = await stack.enter_async_context(stdio_client(maps_server_params))
    # 创建所有代理
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
```
从 Agno 的 GitHub 仓库获取完整的 [源代码](https://github.com/agno-agi/agno/blob/main/cookbook/examples/teams/coordinate/travel_planner_mcp_team.py)。安装所需的软件包，执行上述所有配置，并运行完整的 GitHub 示例代码应显示类似于此预览的输出。

# 6. 将 MCP 用于 Upsonic 代理
[Upsonic](https://docs.upsonic.ai/introduction) 是一个用于创建 AI 代理的 Python 框架。使用 Upsonic，你可以构建你的代理，定义代理的任务，并使用 [MCP 工具](https://docs.upsonic.ai/concepts/mcp_tools) 处理每个任务定义，如下面的示例代码所示。
`import os`
```python
from dotenv import load_dotenv
from upsonic import Task, Agent, Direct
from upsonic.client.tools import Search # 添加搜索作为后备工具

# 从 .env 文件加载环境变量
load_dotenv()

# 从环境变量中获取 OpenAI API 密钥
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# 为会话设置你的 OpenAI API 密钥
os.environ["OPENAI_API_KEY"] = openai_api_key

# 定义 HackerNews MCP 工具
```
## 基于 Upsonic 文档，为 HackerNews 使用正确的 MCP 设置

```python
class HackerNewsMCP:
    command = "uvx"
    args = ["mcp-hn"]
    # 此 MCP 不需要环境变量
    # 创建一个任务来分析最新的 HackerNews 故事
    # 如果 HackerNews MCP 失败，则添加搜索作为后备方案
    task = Task(
        "分析今天排名前 5 的 HackerNews 故事。提供每个故事的简短摘要，"
        "识别任何共同的主题或趋势，并突出显示哪些故事可能与对 AI 和软件开发感兴趣的人最相关。",
        tools=[HackerNewsMCP, Search]  # 包括 HackerNews MCP 和搜索工具
    )
    # 创建一个专门从事科技新闻分析的代理
    agent = Agent(
        "科技新闻分析师",
        company_url="https://news.ycombinator.com/",
        company_objective="提供对科技行业新闻和趋势的深刻分析"
    )
    # 使用代理执行任务并打印结果
    print("正在分析 HackerNews 故事...")
    agent.print_do(task)
    # 或者，如果任务很简单，您可以使用直接 LLM 调用
    # print("直接分析 HackerNews 故事...")
    # Direct.print_do(task)
    # 如果您想以编程方式访问响应：
    # agent.do(task)
    # result = task.response
    # print(result)
```

在上面的示例中，我们在 Upsonic 中创建了一个 AI 代理，该代理检索 Hackernews 中最新的五个故事。 如果您 `pip install upsonic` 并运行上面的 Python 代码，您应该会看到类似于此图像的输出。

## 7. 将 MCP 用于 Mastra 代理

[Mastra](https://mastra.ai/) 是一个 TypeScript 框架，用于构建原型和可用于生产的 AI 代理。 与 Chainlit 类似，Mastra 提供了一种标准化的方式来连接到 MCP 服务器，以通过 `stdio` 或 `sse`-based 连接访问各种工具。

要将您的 Mastra 代理连接到 MCP 服务器，您应该使用其 `MCPConfiguration` 类。 此类处理多个服务器连接，例如生命周期、命名空间和工具，在任何 Mastra 代理工作流程中。 在 Master 应用程序和 MCP 服务器之间创建连接涉及以下步骤。

- 创建 `MCPConfiguration` 类的实例并添加服务器配置。
- 使用 `getTools()` 或 `getToolsets()` 方法检索 MCP 工具。

下面的示例代码表示使用 Mastra 代理实现 MCP 服务器的基本用法。

```typescript
import { MCPConfiguration } from "@mastra/mcp";
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

// 创建一个可以访问所有工具的代理
const agent = new Agent({
    name: "Multi-tool Agent",
    instructions: "You have access to multiple tool servers.",
    model: openai("gpt-4"),
    tools: await mcp.getTools(),
});
```

请参阅 Mastra 的 [MCPConfiguration](https://mastra.ai/docs/reference/tools/mcp_configuration) 了解更多信息。

## LLM 应用和代理中 MCP 的挑战和未来发展方向

本教程向您介绍 MCP，并解释了为什么它在开发者社区中变得流行。 我们重点介绍了 MCP 与 IDE（如 Cursor 和 Windsurf）的集成。 除此之外，我们还在七个不同的 Python 和 TypeScript 框架中实现了 MCP，用于构建基于 LLM 的应用程序、AI 助手和代理。

MCP 的强大功能还带来了以下[挑战](https://x.com/tobi/status/1891137636720419191)。 在为您的项目搜索 MCP 工具时，您可能会发现检查或验证质量以及查看 AI 项目的确切应用程序具有挑战性。 这是因为它的工具搜索和发现尚未标准化。 此外，由于 MCP 服务器提供商的不同模式，其配置未提供一致的用户体验。

目前，MCP 生态系统正在[讨论](https://github.com/orgs/modelcontextprotocol/discussions/159)标准化 MCP 的各个方面。 未来可能会有一种安装基于 MCP 的应用程序的标准方法，就像我们在 Python 中 `pip install` 包一样。[PulseMCP](https://www.pulsemcp.com/) 也在尝试使浏览和发现 MCP 变得更容易。