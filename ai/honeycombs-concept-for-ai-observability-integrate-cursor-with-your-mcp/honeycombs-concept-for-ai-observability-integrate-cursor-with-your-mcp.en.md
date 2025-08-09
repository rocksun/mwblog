[Honeycomb](https://thenewstack.io/honeycomb-says-dont-give-up-on-frontend-observability/) has created a [Model Context Protocol (MCP)](https://thenewstack.io/what-is-mcp-game-changer-or-just-more-hype/) server for [observability](https://thenewstack.io/introduction-to-observability/) that represents an ambitious concept, as observability expands both its usage and intelligence. At the same time, it takes the obvious step of figuring out how to integrate observability through its MCP.

Honeycomb integrates your AI model of choice — such as [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/), Claude Code, Claude Desktop or VS Code — directly into the IDE. When great or terrible things happen, whether for debugging or analyzing certain situations in your operations or DevOps environment, you simply query it directly in the IDE and unleash ICP, the MCP for Honeycomb queries, as Honeycomb CEO [Christine Yen](https://www.linkedin.com/in/christineyen/) described it: “It solves agent context issues elegantly and accelerates AI-assisted debugging workflows.”

According to Honeycomb’s documentation:

* The AI agent can investigate a latency spike by prompting it inside your IDE, and it’ll use MCP to run Honeycomb queries and analyze trace data remotely.
* The MCP tooling is optimized to avoid chat context overload, so tools like column search and trace view ensure agents fetch only relevant telemetry.

Specifically, Honeycomb’s MCP server can access all of your resources in your environments, explained Honeycomb Director of Open Source [Austin Parker](https://www.linkedin.com/in/austinlparker/). These include boards, triggers, [SLOs](https://thenewstack.io/hard-truths-to-consider-when-designing-slos-for-mobile-apps/), queries and others. When running the MCP server in an appropriate client, like Claude Desktop, VS Code or Cursor, you can give agents open-ended tasks and they can use these tools to accomplish them, Parker said.

If you have an SLO “that’s burning down,” the Cursor agent can inspect that SLO and perform investigations in Honeycomb to find more data that it can use in conjunction with analysis of your codebase to find and fix bugs or improve performance, Parker wrote in a blog post. “A really neat trick is asking the agent to improve the instrumentation of a new or existing service based on what is seen in other services (or a specific one)—it can use Honeycomb to figure out specific idioms and attributes that are already in use, then follow those patterns when editing more code,” Parker wrote. “It’s very good at using Honeycomb in conjunction with other data added to an agent context—for instance, OpenTelemetry Semantic Conventions—to discover opportunities for telemetry refactoring (e.g., converting existing log-based telemetry to spans).”

## Under Construction

The biggest challenge Honeycomb has faced in its design of the MCP server is “the sheer amount of tokens that our query data API returns for anything more than extremely basic query,” Parker wrote. “While this can be somewhat worked around by prompting, it’s really only the tip of the iceberg. Some Honeycomb accounts can have tens of thousands of columns, thousands of triggers, and hundreds of datasets,” Parker wrote.”It’s extremely easy for an agent to get itself in a doom loop of queries and hallucinations where it constantly forgets the name of attributes, gets confused about dataset names, and more.”

This issue is not just Honeycomb’s problem. Other Software as a Service (SaaS) tools will face similar issues when they build MCP servers and add other integrations. However, each [large language model (LLM)](https://thenewstack.io/what-is-a-large-language-model/) interface design is unique. “The kind of response that you return through your standard JSON API that’s suitable for programmatic access is probably not what you should return to an LLM,” Parker wrote. “MCP servers do provide a nice abstraction layer for you to address this in flight—you can edit the responses before you return them to simplify data structures, remove unneeded fields, and so forth.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)