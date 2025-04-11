# Google’s Agent2Agent Protocol Helps AI Agents Talk to Each Other
![Featued image for: Google’s Agent2Agent Protocol Helps AI Agents Talk to Each Other](https://cdn.thenewstack.io/media/2025/04/c90e05a8-img_3909-edit-1024x576.jpg)
At its Cloud Next conference in Las Vegas, [Google](https://cloud.google.com/?utm_content=inline+mention) today announced a new open protocol that helps AI agents communicate with each other, no matter which framework the agent was built for.

[Agent2Agent](https://github.com/google/A2A), as it is called, is launching with the support of more than 50 of Google’s technology partners, including the likes of Atlassian, Box, Cohere, Intuit, Langchain, [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention), Salesforce, [SAP](https://www.sap.com/index.html?utm_content=inline+mention), [ServiceNow](https://www.servicenow.com/products/observability.html?utm_content=inline+mention), UKG, and Workday.
Antrophic’s [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP) has quickly become the de facto standard for connecting agents to external applications and data sources. Agent2Agent (A2A), Google stresses, is not meant to replace MCP in any way. Instead, it is meant to complement MCP by helping developers build systems where agents can more easily talk to each other, irrespective of the tools and frameworks they use to build those agents.

“MCP and A2A our agent to agent protocol, are complementary in that MCP allows you to access data in an open, standard way, whereas A2A allows for interoperability between different agents,” explained Amin Vahdat, the VP for ML, Systems and Cloud AI Google Cloud, in a press conference earlier this week.

“Think of MCP as model to data and A2A as allowing interoperability between agents, agent to agent. The two of these — for data and agent interactions — come together to make it very easy and productive to build very powerful agents.”

The new protocol, which supports text, audio and video, is based on existing standards (HTTP,SSE, JSON-RPC) and includes authentication and authorization capabilities, which Google says offer “parity to OpenAPI’s authentication schemes at launch.” The company also stresses that the new protocol provides support for long-running tasks, with A2A being capable of offering real-time feedback, notifications and status updates.

With A2A, agents are either a “client” or “remote” agents. Clients formulate and communicate tasks, while the remote agents act upon them. Remote agents can advertise their capabilities with the help of ‘agent cards’ in JSON format.

“A2A has the potential to unlock a new era of agent interoperability, fostering innovation and creating more powerful and versatile agentic systems. We believe that this protocol will pave the way for a future where agents can seamlessly collaborate to solve complex problems and enhance our lives,” Google notes in today’s announcement. “We’re committed to building the protocol in collaboration with our partners and the community in the open. We’re releasing the protocol as open source and setting up clear pathways for contribution.“

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)