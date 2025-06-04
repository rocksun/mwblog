# MCP Is RSS for AI: More Use Cases for Model Context Protocol
![Featued image for: MCP Is RSS for AI: More Use Cases for Model Context Protocol](https://cdn.thenewstack.io/media/2025/05/1f0dc7e7-steve-johnson-ujxqaehhzum-unsplashb-1024x576.jpg)
Like many an English major, I began my career in software as a technical writer. When a young friend recently asked for advice about entering that profession I realized that, after decades as a sleepy discipline, software documentation is now interesting in ways it has never been before.

This has been true for a while, as LLMs have ingested docs and made them more useful. An [MCP](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) server for a corpus of docs amplifies that benefit. You can think of it as [llms.txt](https://llmstxt.org/) on steroids, a kind of sitemap that works as an attention-focusing mechanism. When I built an MCP server for the software development tool I’m working on now, I realized that MCP invites us to explore synergies between how people interact with our stuff — docs, source code, examples — and how LLMs do.

It may sound impressive to say “I built an MCP” server, but the mechanics are delightfully trivial — which is why I’m inclined to think of MCP as RSS for AI. The beauty of RSS as a protocol was its simplicity. You can write an RSS feed by hand, or write very simple code to generate one. Writing an RSS reader was the starter project for many a beginning coder. It’s not quite that easy to work with MCP’s protocol, [JSON-RPC](https://www.jsonrpc.org/), but vastly easier than working with, say, the protocols spoken by Fediverse or Bluesky clients and servers.

The rapid uptake of MCP reminds me not only of RSS but also of a couple of other things that came together very quickly a few decades ago. One is RSS autodiscovery, which enables a browser to know about a site’s RSS feed. Still recoverable in the Wayback Machine is Mark Pilgrim’s [Important change to the LINK tag](https://web.archive.org/web/20060709143418/https://diveintomark.org/archives/2002/06/02/important_change_to_the_link_tag).

Thank you to everyone who has been working on making this come together in the past few days. It has been surprisingly painless and friction-free. Together, we have come up with a new standard that is useful, elegant, forward-thinking, and widely implemented. In 4 days.

Crack open the home page of the New York Times and you can see that it’s still happening.

12 |
<link data-rh="true" rel="alternate" type="application/rss+xml" title="RSS" href="https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"> |
There was also the [OpenSearch](https://github.com/dewitt/opensearch) protocol. You could drop something like this onto your site:

12 |
My Site Search Search MySite.com |
Along with a `<link rel="search"`
tag and browser support, this meant that when you visited the site the browser would light up *Add this search engine* and enable you to choose it from a set of both mainstream and bespoke search engines. Suddenly it was trivial to use this primitive form of federated search.
We tend to assume that breakthroughs like these were only possible during the early days of the web. It’s refreshing to see they can still happen.

## Pathways for Agents
When all else fails, the old joke goes, read the docs. I’m surely not the only butt of that joke. I’ll read an engaging overview of a software tool but when I’m trying to use the tool I don’t want to read reference docs, I want to answer tactical questions in the moment:

“Is there a component that does [X]?”

“What do the docs for [X] say about topic [Y]?”

“How does the source code implement [X]?”

“How is [X] is used in real projects?”

At the core of my MCP server is a switch statement like this:

1234567891011 |
case "list": toolName = "list_components"case "docs": toolName = "component_docs" args["component"] = argcase "search": toolName = "search" args["query"] = argcase "examples": toolName = "examples" args["query"] = arg |
This structure enables an agent to answer such questions. To figure out if there’s a component that does [X], Claude or Cursor or another agent can use the `list_components`
tool, with no arguments, to retrieve a list of components and descriptions. If the agent spots a likely candidate in the list it can then use `component_docs`
, passing the name of the component, to retrieve docs for that component. When pressed for details it can use the `search`
tool to scan the docs and sources made available by the server, and the `examples`
tool to find uses of component [X] and other material related to topic [Y].
Writing software docs will benefit from testing in the same way that writing code does. Now we can test whether docs actually work.

When I “built” the server — airquotes because, of course, I merely directed Claude to build it for me — I was immediately more productive as I worked through the exercise of expanding our tool’s documentation and creating sample apps. In [Code in Context: How AI Can Help Improve Our Documentation](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/), I wrote about an epiphany: writing software docs will benefit from testing in the same way that writing code does. Now we can test whether docs actually work. When an LLM that has read the docs fails to answer a question we expect the docs should answer, that might be an LLM bug, but more likely is a documentation bug. We can improve the docs and test whether that fixes the bug.

That miracle was already possible by giving LLMs raw access to the docs. With MCP, we can create pathways to guide LLMs to more fruitful interaction.

## Why Build an MCP Client?
MCP’s simplicity means that, like RSS autodiscovery and OpenSearch, it’s the kind of thing that can catch on quickly and deliver powerful leverage. Because MCP pipes JSON-RPC over stdio you can talk to a server by just echoing commands to it, and that’s how I always want to interact with simple protocols in order to grok how they work. In practice, I found JSON-RPC-over-stdio a bit challenging for that approach, so I “built” a client for my server. It’s a charming reminder of another, even older thing: The gopher.

123456 |
Available commands: list - List all components docs - Docs for a component search - Search code/docs examples - Search usage examples quit - Quit |
Although I could watch Claude and Cursor interact with my server and evaluate how to tune it to improve the flow, it was a powerful experience to step into their shoes and converse with my server in the same way they do.
I think the next thing I’ll add to the server’s kit will be a `topic`
tool that focuses on the concepts that our users will need to understand. We have long sought to structure docs primarily for the benefit of the people who read them, and secondarily for the machines that do. It’s tempting to think that as the tables turn and machines become primary readers, structure matters less. Just make sure you have the necessary raw material, throw it all into the bucket, and let the AIs figure it out. To a certain extent, they will. But structuring the interaction between machines and our documentation can turbocharge their ability to work with it. Happily, that’s just the sort of interaction people want too.

## Don’t Just Read the Docs, Also Talk to Them
We mostly don’t want to read the docs, but we do want to converse with them. When we build search interfaces for our docs, we have always tried to anticipate search intentions. People aren’t just looking for words; they need to use the material to solve problems and get things done. When you create an MCP server, you are forced to make those search intentions explicit. That will be as useful for us as it is for the robots, and will help us work with them more effectively.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)