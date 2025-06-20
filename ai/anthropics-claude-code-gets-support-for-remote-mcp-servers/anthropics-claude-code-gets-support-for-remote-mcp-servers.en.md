[Claude Code](https://www.anthropic.com/claude-code), Anthropic’s [AI coding agent](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/), has seen a 160% growth in its active user base since the company launched its [Claude 4 models](https://thenewstack.io/anthropic-launches-claude-opus-4-and-sonnet-4/) three months ago. Today, it is expanding Claude Code with support for remote Model Context Protocol (MCP) servers. This will allow developers to extend Claude Code’s toolchain and data access with data and tools from a far wider range of services, like other dev tools, project management services and knowledge bases. Previously, Claude Code was limited to using local MCP servers and while those could also connect to external sources, Anthropic notes that it’s now far easier to do so.

To integrate Claude Code with an MCP server, developers simply have to run a basic command using the tool’s command-line interface, run through OAuth authentication flow, and you’re good to go.

The new integration will support MCP servers that return Server-Sent Events (SSE) to stream their data back to Claude Code, as well as Standard Input/Output ([STDIO](https://naman1011.medium.com/model-context-protocol-mcp-stdio-vs-sse-a2ac0e34643c)).

Anthropic’s [Cat Wu](https://www.linkedin.com/in/cat-wu/) told me that the company received many requests from developers who wanted to customize Claude Code more. 

“We’ve always built Claude Code to be customizable, because we know developers love scripting their tools, bringing their own tools or system prompts. And so remote MCP was just a natural extension of that, where we found that developers wanted Claude Code to have access to more information that they have access to,” Wu said.

Developers will be able to pull in any remote MCP server, though some will obviously be more useful than others. Anthropic’s launch partners are application monitoring and error tracking service Sentry and Linear, the [increasingly popular](https://thenewstack.io/anti-agile-project-tracker-linear-the-latest-to-take-on-jira/) bug tracking and project management tool for development teams. 

“if you hired an engineer and you said, ‘Hey, you can’t look at any communications tools, you can’t look at any ticket management software, you can’t look at the errors, you can’t verify that your fixes worked,’ then you wouldn’t expect them to be very productive. We think this will be a big productivity boost for engineers using Claude Code,” said Wu.

Wu also noted that this latest generation of models has gotten far better at using tools, even if it sometimes takes them a few rounds of trial and error to figure out how a given tool works (at times, she noted, it helps to give Claude Code a bit of information about the tools it has access to when it’s not one of the more mainstream services).

At times, MCP servers can also overwhelm Claude Code with too much context, so one area where we will likely see some innovation going forward is having MCP servers that are smarter about which context they send to the agent.

It’s worth noting that some other agentic coding tools like Cursor and Windsurf also support [tool usage over MCP](https://docs.cursor.com/tools). In some way, that’s now becoming table stakes, given that there is such a plethora of potential use cases for these connections. 

At launch, Claude Code was only available to users on Anthropic’s Max plan, which starts at $100 per month, or those who opted for a pay-as-you-go approach by paying directly for the API usage of the tool (which can quickly add up). A few weeks ago, Anthropic also opened up access to the tool to users on its far more affordable $20 per month Pro plan, though as Wu noted, that’s more for working on weekend projects and small repos, given that its usage is capped at two hours of work every five hours (when the rate limit resets). The Pro plan comes with the same MCP support as the pricier plans, though. 

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)