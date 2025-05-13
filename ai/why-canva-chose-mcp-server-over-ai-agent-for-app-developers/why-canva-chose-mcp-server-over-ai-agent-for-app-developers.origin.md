# Why Canva Chose MCP Server Over AI Agent for App Developers
![Featued image for: Why Canva Chose MCP Server Over AI Agent for App Developers](https://cdn.thenewstack.io/media/2025/05/09eb8dd0-canva_mcp_server_for_devs-1024x576.jpg)
[Canva launched](https://www.canva.dev/blog/developers/canva-dev-mcp-server/) Model Context Protocol (MCP) Server for its developer platform last month. Its use of [MCP](https://thenewstack.io/what-is-mcp-game-changer-or-just-more-hype/) over [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) provides a preview of what developers might expect in the near future from companies that host their own app marketplaces. It also shows how MCP could be a game-changer for building apps.
MCP is an emerging open standard [from Anthropic](https://www.anthropic.com/news/model-context-protocol) that provides a way for AI models to interact with external data sources and tools. Think of it as a universal language and set of rules that allow a [large language model](https://thenewstack.io/the-new-shadow-it-llms-in-the-wild/) to talk to systems outside itself. An MCP server translates an LLM’s requests into a language that a system understands, then bring information back to the LLM in a standardized format. This lets developers use models in new ways, by providing additional data or supporting more complex tasks — without having to build an AI agent or retrain LLMs.

## Canva’s MCP Use Case
[Anwar Haneef](https://www.linkedin.com/in/anwarhaneef/), head of ecosystem at Canva, explained to The New Stack that Canva’s MCP server will make it easier for the thousands of web developers that use their development platform — and the AI systems these coders rely on — to access Canva documentation and APIs.
Before the MCP server, [building a Canva app](https://thenewstack.io/canva-launches-developer-platform-eyes-generative-ai-apps/) was a lengthy process, he said. Developers had to go back and forth with Canva, which reviewed applications to ensure they adhered to Canva’s look and feel.

“Typically, what happens is an app is submitted then we have a review process,” he said. “Designers try to make sure that it’s designed well from a user experience standpoint.”

Canva has more than 600 apps on its [marketplace](https://www.canva.com/apps/), and Haneef estimated that around 150 are AI-enabled. The review process took time and involved additional reviews after every app change. Canva wanted to accelerate that process.

“With MCP, what we realized is we could effectively ‘shift left’ the work of using our development tools to developers outside of Canva,” he said. “We created an MCP server that allows easy access to the Canva developer APIs, SDKs and the documentation.”

With the MCP server, Canva effectively took that feedback expertise and brought it to the developer’s workspace, cutting the length of the feedback loop.

“Our intention is that when they submit the app, there’s so much feedback and so much of this automated in the development process itself, that the submission and publishing process becomes streamlined,” Haneef said.

The MCP server allows developers to stay within their IDEs while still getting the look and feel of the UI kit used by Canva, he added.

## MCP vs. Agents
Canva looked at building an [AI agent](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/) to assist developers, but decided against that route because so many are doing that and charging developers for it — including Windsurf and Cursor.

“Developers are already paying for them [agents] and using them in their day to day work today,” he said. “Us providing one more level of refinement to that might not as add as much, but ensuring that those LLMs have the right context to build the code relevant for our platform — that has a high impact.”

It’s a paradigm shift from what the tech industry previously expected with AI, which was that companies would train AI agents to perform specific task and the developer would have to use that organization’s AI.

Instead, the MCP server uses the local model that the developer is using. It’s invoked with a call from the developer’s AI to Canva, then it fetches information from Canva that the developer needs to create an app.

“Instead of them relying on our [AI] model and having all sorts of variations, we wanted the developer to use the tools that they are comfortable with — whether they use Gemini or Claude or GPT, or whatever that is,” Haneef said. “Basically, we’re providing input for their model to use and then surface it, which is why MCP is critical.”

## Deploying an MCP Server
Building an MCP server is a not a trivial task, Haneef said.

“There is [documentation](https://docs.anthropic.com/en/docs/agents-and-tools/mcp), but no clear standards,” he said. “Tools are still emerging.”

Canva worked with experienced companies that specialized in building MPC servers, he added. Canva’s job, then, was to provide the information in a lightweight and easy-to-digest format so that the AI can understand it, he explained. That meant going back to first principles and reevaluate its developer offerings.

Among the changes Canva made was to revamp its documentation to enable markup language access, so that AI agents can easily parse through it without navigating JavaScript or imagery. The company also rethought its entire process for supporting developers and the creation of applications. It choose MCP because it has gained traction with [IDEs](https://thenewstack.io/best-open-source-ides/), he said.

“The reality is the standard is evolving, so we wanted to make sure that we’re doing things that are thoughtful,” he said. ”We’re focusing on providing content atop context to the agent.”

The MCP server also avoids the problem of having developers send information to Canva, which organizations tend to frown on.

That makes it more comfortable for developers because they know data is being sent into their AI, but data is not leaving their AI or internal systems.

The MCP server is available now. Haneef added that another avenue for Canva developers is to use Zapier, which offers MCP server access to its integrations, including the Canva Connect API.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)