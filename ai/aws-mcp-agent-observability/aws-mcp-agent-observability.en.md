**Many MCP servers do one thing.** An agent asks for data, and the server hands it back. AWS’s [James Ward](https://www.linkedin.com/in/jamesward/) thinks that leaves a lot on the table. The protocol works best, he told me, when the server acts less like a database and more like another voice in the conversation.

Ward is a principal developer advocate at AWS and sits on the technical committee of the Agentic AI Foundation, the Linux Foundation group that now houses MCP. I sat down with him last week at AGNTCon + MCPCon in San Jose the day before he and co-presenter Alexander Ioffe were set to give a session on moving MCP from a basic API to an agent integration interface.

VIDEO

“Many times our MCP servers are just these APIs, like ‘get me the customers,’ and that is a good place to start,” Ward said. “I imagine MCP as the third person in this conversation, or a fourth or a fifth, depending on how many MCP servers you have.”

In practice, that means a tool response carries guidance with the data. It tells the agent what it just did, what it might want to do next, and where to find more.

The other half of his pitch is visibility. Web developers can trace a click on a page all the way down to the database. “MCP by default doesn’t have any way to do trace ID,” Ward said.

The workaround AWS uses is rather low-tech. Add a session ID parameter to the tools and tell the agent to pass it on every call, so individual calls can be stitched into one journey. A second parameter can carry the user’s prompt or a summary of their goal. Teams can then compare what the user wanted with the path the agent took, build an eval around it, adjust a tool description or parameter, and measure whether more tasks get completed. Ward said AWS built much of this for the MCP servers its own developers use.

In May, AWS opened its [MCP Server](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) to everyone and added [Lambda diagnostics in September](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-mcp-server-serverless/). In an [Agentic AI Foundation profile](https://aaif.io/blog/james-ward-thinks-your-mcp-server-could-use-some-work) published before the conference, Ward described an agent fetching customer records one at a time because the server only offered a one-record tool. Watching the full journey is how teams spot that pattern and build a batch tool to fix it.

Ward didn’t present MCP as the only solution. AWS also ships a CLI and skills, he said, partly because MCP’s OAuth model can’t toggle between AWS user profiles the way the CLI can. Which works best depends on the model, the tool descriptions, and how the agent discovers tools, so AWS tests them against each other with evals.

None of this is exotic, and Ward knows it. “There’s nothing new under the sun,” he said. Observe the journey, reproduce it, measure it, and improve it. The difference is that teams now have to understand the path a human and an agent take together, and test whether changes to their tools actually help them finish the task.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)