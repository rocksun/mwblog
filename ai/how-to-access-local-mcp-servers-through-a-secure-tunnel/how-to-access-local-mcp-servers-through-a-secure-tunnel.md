
<!--
title: 如何通过安全隧道访问本地MCP服务器
cover: https://cdn.thenewstack.io/media/2025/06/c15aa758-getty-images-rtbjymqgjgy-unsplashb.jpg
summary: 本地数据如何赋能 AI？用 `Ngrok` 隧道安全暴露本地 `MCP` 服务器给远程 `LLM`！三步搞定：搭建基于 `streamable-http` 的 `FastMCP` 服务器，`Ngrok` 穿透，再用 `Anthropic Claude API` 构建 `MCP` 客户端。轻松实现 AI 访问本地数据，速来体验！
-->

本地数据如何赋能 AI？用 `Ngrok` 隧道安全暴露本地 `MCP` 服务器给远程 `LLM`！三步搞定：搭建基于 `streamable-http` 的 `FastMCP` 服务器，`Ngrok` 穿透，再用 `Anthropic Claude API` 构建 `MCP` 客户端。轻松实现 AI 访问本地数据，速来体验！

> 译自：[How To Access Local MCP Servers Through a Secure Tunnel](https://thenewstack.io/how-to-access-local-mcp-servers-through-a-secure-tunnel/)
> 
> 作者：Janakiram MSV

MCP 服务器非常适合将传统数据库中的数据作为[大型语言模型上下文](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (LLM) 公开。由于这些 MCP 服务器位于更靠近数据源的本地，我们需要一种机制将它们暴露给远程 LLM 和代理。

在本教程中，我们将探讨如何利用 [Ngrok](https://ngrok.com/) 安全地将 MCP 服务器暴露给托管的 LLM。我们将首先构建一个基于可流式 HTTP 传输的 MCP 服务器，该服务器返回数据。然后，我们将通过 [Ngrok](https://thenewstack.io/using-ngrok-in-production-not-just-for-testing-anymore/) 隧道公开它，最后创建一个基于 [Anthropic Claude API](https://www.anthropic.com/api) 的 [MCP 客户端](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/)。

下图解释了这种方法：

![](https://cdn.thenewstack.io/media/2025/06/a6bf65e2-mcp-ngrok-0-1024x460.png)

## 步骤 1：创建 MCP 服务器

我们将创建一个简单的 MCP 服务器，该服务器以 JSON 格式返回员工数据。这可以很容易地替换为数据库查询，以从现有数据库中获取数据。在继续之前，请安装最新的 [FastMCP](https://gofastmcp.com/getting-started/welcome) Python 模块。

```python
from fastmcp import FastMCP
mcp = FastMCP("Employee Server")

@mcp.tool()
def get_employees() -> list:
    """
    Returns a list of 5 employee records. Each record is a dictionary containing:
        - id: Unique identifier for the employee
        - name: Employee's name
        - role: Employee's job title
    """
    #You can access any internal datasource here instead of sending dummy data
    return [
        {"id": 1, "name": "Alice", "role": "Engineer"},
        {"id": 2, "name": "Bob", "role": "Designer"},
        {"id": 3, "name": "Charlie", "role": "Manager"},
        {"id": 4, "name": "Diana", "role": "Analyst"},
        {"id": 5, "name": "Eve", "role": "Intern"},
    ]

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

请注意，我们正在使用可流式 HTTP 作为传输方式。
运行 MCP 服务器并确保它正在侦听传入的请求。

![](https://cdn.thenewstack.io/media/2025/06/b53fedd8-mcp-ngrok-1.png)

## 步骤 2：通过 Ngrok 隧道公开 MCP 服务器

首先在您的机器上安装 Ngrok。本教程展示了如何在 macOS 上安装和运行它。有关其他环境，请参阅 [Ngrok 文档](https://ngrok.com/docs/)。

```bash
brew install ngrok
```

从 Ngrok 仪表板获取您的 Authtoken 并初始化 CLI。

```bash
ngrok config add-authtoken $YOUR_AUTHTOKEN
```

我们现在准备好打开一个安全隧道来公开我们的 MCP 服务器。

```bash
ngrok http http://localhost:8000
```

![](https://cdn.thenewstack.io/media/2025/06/655309d7-mcp-ngrok-2-1024x466.png)

我们的 MCP 服务器现在可以通过 Ngrok 公开的 URL 访问。在我的例子中，它是 https://c45c-49-205-249-147.ngrok-free.app/mcp。我们现在准备好构建与此端点通信的 MCP 客户端。

## 步骤 3：使用 Claude API 构建 MCP 客户端

[beta](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) 中的 Claude API 支持直接在请求中调用 MCP 服务器公开的工具。有关最新的 API 规范，请参阅[文档](https://docs.anthropic.com/en/docs/overview)。

下面的代码演示了如何从 Claude 的 API 访问远程 MCP 服务器。它假定您拥有 Anthropic 的 API 密钥，并且已安装所需的 Python 模块。

```python
import anthropic

client = anthropic.Anthropic(
    api_key="YOUR_ANTHROPIC_API_KEY",
    default_headers={
        "anthropic-beta": "mcp-client-2025-04-04"
    }
)

response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "Who is the intern within the organization?"
        }
    ],
    mcp_servers=[
        {
            "type": "url",
            "url": "https://c45c-49-205-249-147.ngrok-free.app/mcp",
            "name": "emp-server",
        }
    ]
)

blocks=response.content
#print(blocks)
final_output = None
for block in reversed(blocks):
    if hasattr(block, 'text'):
        final_output = block.text
        break

print(final_output)
```

该代码是不言自明的，因为它通过 API 指向远程 MCP 服务器。提示是关于识别公司内的实习生，这迫使 Claude 调用 MCP 服务器中的工具。

![](https://cdn.thenewstack.io/media/2025/06/369c9f07-mcp-ngrok-3.png)

Claude 成功识别了实习生并显示了员工的详细信息。这证实了它确实正在访问远程 MCP 服务器。

在本系列的后续教程中，我们将探讨如何实施 OAuth 来保护 MCP 服务器。敬请关注。