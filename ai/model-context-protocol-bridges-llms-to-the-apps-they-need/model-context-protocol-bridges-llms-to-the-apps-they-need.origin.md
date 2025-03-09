# Anthropic’s MCP Bridges LLMs to the Apps They Need
![Featued image for: Anthropic’s MCP Bridges LLMs to the Apps They Need](https://cdn.thenewstack.io/media/2025/03/da0fefca-tamanna-rumee-8yd0ndi1shy-unsplash-mcp-1024x683.jpg)
“This is very much like microservices, but we are bringing in intelligence,” said [Mahesh Murag](https://www.linkedin.com/in/maheshmurag/), [Anthropic](https://www.anthropic.com/company) engineer for applied AI, describing the [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP), an open source born at Anthropic to standardize how applications could provide context to LLMs and the agents that power them.

Murag was speaking at the [AI Engineer Summit](https://www.ai.engineer/summit/2025), held last month in New York, and his talk sparked a wave of interest in MCP (first released in November), as folks discussed the best way to streamline the developer process for getting agents to interact with the rest of the computing world.

## Today’s Agentic Landscape
The inspiration for MCP came from the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) (LSP), a standard for IDEs to understand all the different features of [programming languages](https://thenewstack.io/programming-languages/).

Today, agents have to interact with such resources on a one-by-one basis, accruing a lot of routine development work. Or worse, users may have to cut and paste in contextual (and configuration) data manually.

There may be plug-ins, but they are designed for each specific type of connection.

Or they may be confined to a specific platform, such as OpenAI’s [Work With Apps](https://reindeersoft.com/news/openai-launches-work-with-apps-feature-for-seamless-macos-integration) feature, which caters to [Macs](https://thenewstack.io/homebrew-for-macos-developers/) (and OpenAI).

Through MCP, agents will have a standard way to access data, tools, and prompts (pre-written templates) — if it is broadly adopted by the model makers and app vendors.

“Instead of maintaining separate connectors for each data source, developers can now build against a standard protocol,” an Anthropic [blog post explained](https://www.anthropic.com/news/model-context-protocol). “As the ecosystem matures, AI systems will maintain context as they move between different tools and datasets, replacing today’s fragmented integrations with a more sustainable architecture.”

Lots of folks feeling FOMO about MCP.

Here’s the problem it solves:

[pic.twitter.com/UszaGAsOUD]— Matt Pocock (@mattpocockuk)

[March 6, 2025]

## How the Agent Will Find the Resource
MCP wouldn’t replace[ agent frameworks](https://thenewstack.io/a-developers-guide-to-the-autogen-ai-agent-framework/), but complement them by providing pluggable connectors and adapters, and making life easier for the developer by providing a consistent way of interacting with tools, Murag said in his presentation.

MCP is defined in a set of [specification and SDKs](https://github.com/modelcontextprotocol), covering both the client and server implementations.

The documentation walks through the process of creating a “server” that [provides](https://modelcontextprotocol.io/quickstart/server) weather forecasts for an LLM using [Python](https://thenewstack.io/what-is-python/), [Node](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) or [Java](https://thenewstack.io/introduction-to-java-programming-language/). MCP servers can be installed locally or run by a third party.

The sample server has a set of “helper functions” for querying and formatting the data from the National Weather Service API. Tool execution handlers execute the logic of each tool. It can then be installed on Anthropic’s [Claude Desktop](https://claude.ai/download) AI service (or your preferred agent).

[Likewise](https://modelcontextprotocol.io/quickstart/client), the user client software, which is part of the AI application itself, initializes a session, collecting a list of available tools.
It also maintains the conversational context, executes the queries and handles the responses, and provides a command line interface for the user.

“Once your client is MCP compatible you can connect it to any server with zero additional work,” Murag explained. “If you’re a tool or API provider or someone that wants to give LLMs access to the data that matters, you can build your MCP server once and see adoption of it everywhere across all of these different AI applications.”

On the enterprise side, the team that runs the [vector database interface](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/) can turn it into a MCP server that other teams in the company build their apps from.

Presumably, service providers will all want to provide their own servers. And so just like microservices, MCP demands a registry, a place to find and discover resources. “A huge problem these days is discovery,” Murag said.

So the project also maintains an [open source repository](https://github.com/modelcontextprotocol/servers) of MCP servers, offering reference implementations for dozens of services, such as [Google Maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps), [PostgreSQL](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres), and [Slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack).

## But Will MCP Thrive?
Murag’s presentation set off a tsunami of interest in AI circles.

“In pre-MCP world, one would have to write code to connect AI tool to the external system via API. Which meant every connection had to be pre-coded,” [wrote](https://x.com/johnrushx/status/1897655569101779201) AI agent developer John Rush on X.

“MCP is a standard protocol. This means that every AI tool has to implement this once, and then it can connect to thousands of external tools via this protocol.”

By providing a “standard interface for any API to become an LLM tool plugin,” MCP is an “ultra low friction way to enrich LLM context,” agreed Julian Harris [in a X message](https://x.com/julianharris/status/1897589990382506175).

Not everyone was impressed. One observer likened it to [Zapier for AI](https://x.com/julianharris/status/1897589990382506175), noting that it was just adding extra steps to using APIs.

Another possible roadblock: Other LLM service providers, such as Grok and ChatGPT do not support it currently, and these system designers may very well try float own standards instead.

But there is nothing inherent about MCP that is tied to Anthropic’s AI service Claude, Murag pointed out

Indeed. Dagger founder Solomon Hykes [noted](https://x.com/solomonstre/status/1897784401125412896) that his[ company’s platform](https://thenewstack.io/ai-dev-tools-how-to-containerize-agents-using-dagger/) could work as an “open alternative to Claude Code,” in that is “fully open source, supports any model, and MCP native.”

Enjoy Murag’s entire presentation here:

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)