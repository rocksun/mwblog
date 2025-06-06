# How To Access Local MCP Servers Through a Secure Tunnel
![Featued image for: How To Access Local MCP Servers Through a Secure Tunnel](https://cdn.thenewstack.io/media/2025/06/c15aa758-getty-images-rtbjymqgjgy-unsplashb-1024x576.jpg)
MCP servers are excellent candidates for exposing data from traditional databases as [context to large language models](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (LLMs). Since these MCP servers reside on-premises closer to the data sources, we need a mechanism to expose them to remote LLMs and agents.

In this tutorial, we will explore how to utilize [Ngrok](https://ngrok.com/) to securely expose MCP servers to hosted LLMs. We will first build an MCP server based on streamable HTTP transport that returns data. We will then expose it through an [Ngrok](https://thenewstack.io/using-ngrok-in-production-not-just-for-testing-anymore/) tunnel, and finally create an [MCP client](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) based on the [Anthropic Claude API](https://www.anthropic.com/api).

The diagram below explains this approach:

## Step 1: Create an MCP Server
We will create a simple MCP server that returns employee data in JSON. This can be easily replaced with a database query to fetch the data from an existing database. Install the latest [FastMCP](https://gofastmcp.com/getting-started/welcome) Python module before proceeding.

12345678910111213141516171819202122232425 |
from fastmcp import FastMCPmcp = FastMCP("Employee Server")@mcp.tool()def get_employees() -> list: """ Returns a list of 5 employee records. Each record is a dictionary containing: - id: Unique identifier for the employee - name: Employee's name - role: Employee's job title """ #You can access any internal datasource here instead of sending dummy data return [ {"id": 1, "name": "Alice", "role": "Engineer"}, {"id": 2, "name": "Bob", "role": "Designer"}, {"id": 3, "name": "Charlie", "role": "Manager"}, {"id": 4, "name": "Diana", "role": "Analyst"}, {"id": 5, "name": "Eve", "role": "Intern"}, ]if __name__ == "__main__": mcp.run(transport="streamable-http") |
Notice that we are using streamable HTTP as the transport.
Run the MCP server and ensure it is listening for incoming requests.

## Step 2: Expose the MCP Server Through an Ngrok Tunnel
Start by installing Ngrok on your machine. This tutorial shows how to install and run it on macOS. Refer to the [Ngrok documentation](https://ngrok.com/docs/) for other environments.

1 |
brew install ngrok |
Get your Authtoken from the Ngrok dashboard and initialize the CLI.
1 |
ngrok config add-authtoken $YOUR_AUTHTOKEN |
We are now ready to open a secure tunnel to expose our MCP server.
1 |
ngrok http http://localhost:8000 |
Our MCP server is now accessible at the URL exposed by Ngrok. In my case, it is https://c45c-49-205-249-147.ngrok-free.app/mcp. We are now ready to build the MCP client that talks to this endpoint.

## Step 3: Building an MCP Client with Claude API
The Claude API, which is in [beta](https://docs.anthropic.com/en/docs/agents-and-tools/mcp), supports invoking tools exposed by an MCP server directly within the request. Refer to the [documentation](https://docs.anthropic.com/en/docs/overview) on the latest API specification.

The code below demonstrates how to access remote MCP servers from Claude’s API. It assumes you have the API key from Anthropic and have installed the required Python modules.

12345678910111213141516171819202122232425262728293031323334353637 |
import anthropicclient = anthropic.Anthropic( api_key="YOUR_ANTHROPIC_API_KEY", default_headers={ "anthropic-beta": "mcp-client-2025-04-04" })response = client.beta.messages.create( model="claude-sonnet-4-20250514", max_tokens=1000, messages=[ { "role": "user", "content": "Who is the intern within the organization?" } ], mcp_servers=[ { "type": "url", "url": "https://c45c-49-205-249-147.ngrok-free.app/mcp", "name": "emp-server", } ])blocks=response.content#print(blocks)final_output = Nonefor block in reversed(blocks): if hasattr(block, 'text'): final_output = block.text breakprint(final_output) |
The code is self-explanatory, as it points to the remote MCP server via the API. The prompt is about identifying the intern within the company, and this forces Claude to invoke the tools within the MCP server.
Claude successfully identified the intern and showed the details of the employee. This confirms that it is indeed accessing the remote MCP server.

In the upcoming tutorials of this series, we will explore how to implement OAuth to secure MCP servers. Stay tuned.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)