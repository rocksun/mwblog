# Is Model Context Protocol the New API?
![Featued image for: Is Model Context Protocol the New API?](https://cdn.thenewstack.io/media/2025/05/6e843875-agentic-1024x576.jpg)
As someone involved in the API standards space for a long time, I’ve always been interested in how software talks to software. One of the most exciting things to me about AI has been the possibility of automating key aspects of it, like making it possible to build powerful software agents that talk with the world of APIs around us.

Now, [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) has emerged as the AI-native standard for continuing on the path started by previous standards like REST, SOAP and XML-RPC. Introduced late last year by Anthropic, MCP is an open standard that simplifies connecting data and tools to [large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms), obviating the time-consuming need to create specific integrations, connectors or prompts for each database, tool or cloud service.

As agentic systems become increasingly complex and developers make more enterprise capabilities available as tools, having clear and agreed-upon rules is critical for the growth and success of autonomous workflows. It enables [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) to make decisions about which tools to use in the right order to accomplish a task.

It’s a lot like the way REST helped enable efficient data exchange, flexibility and scalability for APIs; MCP exhibits many similarities to what happened in the API world, and some important differences.

## Your Chat Window as Interaction Point
In the API world, we thought about APIs as either general-purpose, loosely coupled services that could be reused for a wide variety of use cases, or “experience” APIs, which were designed to provide the specific functionality necessary to support a specific UX pattern. Netflix was often our go-to example for experience APIs — it coined the term — but just about any mobile app you use relies heavily on experience APIs.

Now we have a new point of interaction: your ChatGPT window or your Claude Desktop.

Here’s an example. I want to edit an Excel spreadsheet or Google Sheet. Each has an MCP server that expresses capabilities in a manner that the application understands. An Excel MCP, for example, could literally state something like: “I provide an internal state in the form of a spreadsheet, which is a matrix of rows and columns that are addressed by letters and numbers, respectively. Each has a numerical formula, and I provide a set of tools (or functions) you can use to modify this spreadsheet.”

How does this sort of experience get built? It’s not through the purpose-specific experience APIs of the mobile age, but it’s also not achieved by returning to the cognitive burden of the web services or even the microservices eras. It requires something new: a capabilities-oriented approach that exposes tools and the semantic context for helping LLMs understand how to use those tools to satisfy the user’s request. MCP is designed to step into this gap.

A developer could virtually create this MCP server by copying and pasting this information from an Excel user manual.

MCP enables you to ask an agent a question (“make me a spreadsheet of how much I can spend on groceries over the next year”) and, behind the scenes, the agent has MCP servers available to expose these capabilities. Because the agent can reason — it can break down problems into tasks and execute them iteratively — it can use MCP to bring in additional context via other tools and APIs, and generate a highly relevant, useful response.

## Retrieval-Augmented Generation — and Then Some
So, the context is your prompt plus the context your agent has retrieved. Sound familiar? That’s because in many ways, MCP is an evolution of retrieval-augmented generation (RAG). But it takes it a big step further by providing a structured way of how APIs, services, tools or capabilities are described to an agent so it knows how to use them.

In simple terms, [RAG feeds external information into a model](https://thenewstack.io/boost-llm-results-when-to-use-knowledge-graph-rag/) at inference time. MCP provides a well-defined contract for which tools and capabilities are available, and more importantly, a rich semantic description of how they can be used.

This makes chat clients, which are sometimes derided as simple and elementary forms of AI — “just chatbots” — extremely powerful.

## Making Models Smart About Services
The idea of making it possible for LLMs to use tools originated in the [ReAct](https://arxiv.org/abs/2210.03629) paper in late 2022 and was widely discussed in 2023. Meta released its [Toolformer research paper](https://scontent-dfw5-2.xx.fbcdn.net/v/t39.2365-6/422713285_707735768229632_5302603543892954301_n.pdf?_nc_cat=104&ccb=1-7&_nc_sid=3c67a6&_nc_ohc=mYerYGIPnDAQ7kNvwFcdOpY&_nc_oc=AdnKg4q64Z5eBatZVV5Tf3lXao6nu-eLoeh4N8RQ9TMkl3k6Npjp0cO1XP7C-DURKKrzFXk9jm9pdIKMmcIMDHjM&_nc_zt=14&_nc_ht=scontent-dfw5-2.xx&_nc_gid=hpc349AG7QaGzzRG3SSHPw&oh=00_AfGmKUEV7l2sySmNuqGgeQcgkMzPOYl7k1lJKboxjkzeQg&oe=68183C8E) in February 2023, and OpenAI followed with its preview release of function calling and JSON schema support in March, paving the footpaths introduced by frameworks like LangChain.

At the same time, work was done to try to modularize and package the use of tools. [OpenAI’s ChatGPT plugins](https://openai.com/index/chatgpt-plugins/) were a good example of this. Also introduced in March 2023 and built on the OpenAPI specification, these plugins helped ChatGPT access up-to-date information, run computations or use third-party services. The plug-in model was also adopted by Microsoft, and DataStax was proud to be a design partner for the GitHub Copilot plugin model; we delivered the [Astra DB extension for GitHub Copilot](https://www.datastax.com/integrations/github-copilot?utm_medium=byline&utm_source=thenewstack&utm_campaign=MCP&utm_content=) at GitHub Universe in 2023.

Unfortunately, LLMs at the time had not yet become reasoning models, and so the utility of these plugins was limited. [Agentic use cases were possible with these models](https://thenewstack.io/supercharge-your-rag-app-with-agentic-hybrid-search/), but in practice, they were somewhat clunky.

The release of Anthropic’s Claude Sonnet 3.5 model in June 2024 was when we really saw things get serious in this area, making it possible for companies like Cursor and others to leverage these capabilities in the developer space and for Anthropic to increasingly promote general-purpose agentic use cases for its models, leading the introduction of MCP as a standard way of packaging and integrating tools into AI clients. This meant that developers could build MCP servers that delivered an out-of-the-box integration of their apps and services for agents to easily use.

## You Can Get MCP Wrong
With APIs, we learned that API design matters. Great APIs, like those from Stripe or Twilio, were designed for the developer. With MCP, design matters too. But who are we authoring for?

You’re not authoring for a human; you’re authoring for a model that will pay close attention to every word you write. And it’s not just design, it’s the operationalization of MCP that is also important and another point of parallelism with the world of APIs. As we used to say at Apigee, there are good APIs and bad APIs. If your backend descriptions are domain-centric — as opposed to business or end-user centric — integration, adoption and developers’ overall ability to use your APIs will be impaired. A similar issue can arise with MCP. An AI might not recognize or use an MCP server’s tools if its description isn’t clear, action-oriented or AI friendly.

A final thing to note, which in many ways is very new to the AI world, is the fact that every action is “on the meter.” In the LLM world, everything turns into tokens, and tokens are dollars, as [NVIDIA CEO Jensen Huang reminded](https://www.youtube.com/watch?v=_waPvOwL9Z8) us in his Nvidia GTC keynote this year. So, AI-native apps — and by extension the MCP servers that those apps connect to — need to pay attention to token optimization techniques necessary for cost optimization.

There’s also a question of resource optimization outside of the token/GPU space. An overly enthusiastic agent could melt down your enterprise backend service by making multiple calls to it to retrieve the [data it needs](https://thenewstack.io/ai-agents-in-doubt-reducing-uncertainty-in-agentic-workflows/). Your MCP server needs to keep this in mind and either reduce the burden through techniques like caching or advise the agent about the costs associated with leveraging the MCP’s tools in its reasoning processes, and suggest that it acts accordingly.

## Conclusion
As [I wrote earlier](https://thenewstack.io/ai-agents-are-about-to-blow-up-the-business-process-layer/), agentic AI has the potential to completely transform business processes. Unleashing the full automation and decision-making power agents can inject into enterprise architectures — and ensuring accurate, relevant results — requires the ability for them to call external functions, APIs and tools.

While MCP isn’t the only standard being developed right now to facilitate this, though it is the current front-runner, the important thing to understand is that facilitating software’s ability to talk to software is how we’ve progressed in all of the major technology waves we’ve experienced.

*Try out DataStax Astra DB over MCP.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)