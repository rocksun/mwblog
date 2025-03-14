# MCP: The Missing Link Between AI Agents and APIs
![Featued image for: MCP: The Missing Link Between AI Agents and APIs](https://cdn.thenewstack.io/media/2025/03/fb998efb-missing-link-2001-1024x576.jpg)
[via YouTube](https://www.youtube.com/watch?v=VABNA_an2A0).
Last November Anthropic launched the [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP), an open source standard designed to streamline how AI models interact with APIs. As [we explained earlier this month](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/), the vision is to make MCP the universal method for AI agents to trigger external actions.

MCP has drawn a lot of interest in its first few months, including from API management companies like [Speakeasy](https://www.speakeasy.com/). API companies see MCP as a linking mechanism to the [rich ecosystem of LLMs](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/) and agentic frameworks. To find out more, I spoke to Speakeasy CEO [Sagar Batchu](https://www.linkedin.com/in/sagar-batchu-981b3738/).

**What Is Model Context Protocol (MCP)?**
As explained in its documentation, MCP “follows a client-server architecture where a host application can connect to multiple servers.”

Essentially, MCP standardizes API access for AI agents. You can also think of it as a meta-API, as this diagram [from Matt Pocock](https://x.com/mattpocockuk/status/1897742389592440970/photo/2) illustrates:

“So MCP is a protocol and really a very thin layer above an API that says, here is the definition that this API needs to expose for the LLM or agent to be able to query and find out more about […] whatever that data might be,” Batchu explained.

An [MCP client](https://modelcontextprotocol.io/clients) can be an LLM like Claude, IDEs like Cursor and Windsurf, and various other tools (such as SpinAI, a TypeScript framework for building AI agents).

As for an MCP server — the orange-colored block in the above diagram — you can either build your own or use a pre-built MCP server. In its [introductory blog post](https://www.anthropic.com/news/model-context-protocol), Anthropic mentioned there are pre-built MCP servers “for popular enterprise systems like Google Drive, Slack, GitHub, Git, Postgres, and Puppeteer.”

## Speakeasy’s Role in an MCP Architecture
Building your own MCP server is where Speakeasy comes in. Recently the company launched [MCP Server Generation](https://www.speakeasy.com/post/release-model-context-protocol), a tool that automates the creation of MCP-compatible servers.

Currently, Speakeasy’s MCP Server Generation supports TypeScript-based SDKs. However, given Python’s dominance in the AI ecosystem, the company plans to add Python support soon.

Batchu noted that because MCP operates as a client-server model, AI agents interacting with an MCP server can use any programming language. He explained that, unlike traditional SDKs — which are language-specific and require developers to write integration code — MCP servers expose endpoints that AI agents can access directly.

**How Does MCP Compare to OpenAPI?**
[OpenAPI](https://www.openapis.org/) is a widely adopted standard for defining APIs, so at first glance it too is a kind of layer above APIs. But according to Batchu, MCP builds upon OpenAPI rather than replaces it.
“The jump from an OpenAPI spec into MCP is very small,” he said. “OpenAPI is somewhat of a superset of all information that MCP needs, and then you package it up with the specific examples and descriptions [for] an LLM, and you run it as a server.”

Put another way: while OpenAPI provides a structured definition of an API’s capabilities, it is primarily a static specification. MCP, by contrast, introduces a client-server interaction model. An MCP server is a live, running instance that AI agents can query in real time. This means an MCP server can dynamically respond to AI-generated requests, making APIs more accessible to [agentic workflows](https://thenewstack.io/llama-stack-released-to-help-developers-build-agentic-apps/).

“The jump from an OpenAPI spec into MCP is very small.”

– Sagar Batchu, Speakeasy CEO
As Batchu put it, “the difference is [that] an OpenAPI spec is just a definition, and MCP server is actually a server-client experience.”

Until MCP arrived, integrating an API with an AI model had been challenging. Many AI-based API integrations failed because models lacked the necessary schema information to make sense of API responses, Batchu noted. MCP solves this by structuring API interactions in a way that AI can understand, making integrations more reliable.

**Real-World Use Cases For MCP Servers**
Speakeasy already has several customers using its MCP feature set, Batchu said. Companies like Vercel, Dub, and others are leveraging MCP servers to enhance their API-driven workflows.

On Dub, a link-sharing platform, marketing teams frequently create short links for tracking article performance. Instead of manually searching analytics dashboards, they can now ask an AI assistant to retrieve their most-clicked links over the past week. The AI queries Dub’s MCP server, fetches the relevant data, and even generates a visualization — all without the user leaving their chat interface.

I asked about potential e-commerce applications, since this is an area seemingly well suited to AI agents. Imagine such a company using MCP to power AI-driven business intelligence, Batchu suggested. An AI assistant could query an MCP server for sales data, generate reports, and even suggest marketing strategies based on real-time insights. This would lessen the need for manual data extraction and analysis.

**Competing Standards Ahead?**
Anthropic developed MCP, but so far there’s been no sign that the other big dogs in AI will adopt it — the likes of OpenAI, Google and Meta.

Batchu thinks the MCP paradigm is likely to evolve alongside other AI-driven API approaches. He points out that [OpenAI’s function calling](https://thenewstack.io/how-to-build-a-real-time-app-with-gpt-4o-function-calling/) already provides a way for AI models to interact with external services, though it lacks the standardized, open nature of MCP.

“There will be a little bit of schema wars for a while, I believe, until it settles out into something like OpenAPI, right, where there’s a standard,” he said.

“There will be a little bit of schema wars for a while.”

– Batchu
Regardless, Batchu thinks the time is ripe for API producers to experiment with MCP.

“API producers should invest in agent tools like MCP and, you know, make a GitHub repo, build it, put it out there.”

Likewise, he thinks API consumers should experiment, although he acknowledges that there will be more “disruption and chaos” for them — because standards are still in flux. But he has some advice for developers who are tasked with using APIs alongside AI.

“The first thing you can do is actually go look if the API has an MCP server. You can install that locally into your IDE or LLM desktop client, and actually just start to integrate through queries [via] natural language.”

Batchu also notes that the opportunity is there for developers to automate workflows and extract insights dynamically from APIs, using MCP alongside [agentic frameworks](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) like LangChain and AutoGen.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)