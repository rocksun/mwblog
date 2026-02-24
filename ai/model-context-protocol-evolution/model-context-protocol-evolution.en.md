One thing I didn’t do last year was go to any [Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) conferences, largely because I couldn’t see why one very young protocol could represent the wide world of LLMs. But with the speed of AI development, MCP is now looking for a gym membership and checking its pension plan.

Going to the London [MCPconference](https://www.mcp-conference.com/) last week (they are worldwide now) allowed me to dip into the issues that developers are seeing in the area of LLM and tool connections – and perhaps how tool vendors are responding to these. Obviously, some are pushing “Secure MCP Gateways” or “Governed MCP Infrastructure” for their enterprise customers, and naturally, some visitors are looking for these solutions.

Although it has yet to establish itself fully, MCP has already had a near-death experience.

![](https://cdn.thenewstack.io/media/2026/02/53efb9a1-image-1024x377.png)

[Slide from Teo Borschberg of ogment.ai](https://www.linkedin.com/in/teo-borschberg-94a44945/)

OpenClaw was never directly mentioned, but it was definitely the ghost at the feast. MCP may have opened the door a little too wide – before we fully understood the security implications. (There is some irony here: OpenClaw is effectively an MCP client app – just one without opinions about invoking native MCP.)

### MCP is still finding itself

Maybe it isn’t surprising that, in such a fast-moving environment, no single technology has had the time or space to establish itself properly. In terms of implementation, MCP servers are still mainly “internal,” that is, used behind a company firewall. It is still the case that going from a quick vibe-coded solution to production remains a problem. The protocol was supposed to democratise access to existing services, and it has. Many companies have experimented with connecting incoming bug reports through email and creating issues in Salesforce or JIRA. After that, though, things are less clear.

I noticed that “tools” and “skills” were sometimes used interchangeably. Technically, tools are single-purpose instructions, whereas creating a Claude agent skill is just creating a folder that contains a `SKILL.md` file. The skill can also contain resources and tools. But I’m wondering if the two terms stand in for  “more MCP” these days.

“A2A” appeared on many slides without comment. Mentioning Google’s Agent-to-Agent Protocol is probably an offhand way to make a talk sound more general. I saw almost no mentions of Agent Communication Protocol (AGP).

### “Something, something, security”

Inevitably, questions about security have been gnawing (or clawing) at MCP servers. Although MCP was designed to keep the route from agent to your data as friction-free as possible, with security as optional, security is still there. [Duncan Doyle](https://www.linkedin.com/in/duncan-doyle-9601642/) gave a nice, practical talk on MCP security with OAuth 2.1; the tenet of which (as with many other speakers) was “please implement security”.

As usual, the core problem is trust. While MCP can define what can be done, OAuth is left with the harder task of working out which entity is allowed access to what in a workflow. Duncan introduced the idea of **security****elicitation,** which arises from problems that occur when servers request additional information from users via clients during interactions.

The more you think about this, the worse it gets. How does an MCP server securely ask a client for your GitHub credentials? You soon realise that the MCP client must support an approval process for the user and clearly identify the intended recipient. The demo during the talk walked through the many MCP authorisation steps and just proved that a properly implemented server was no quick task. The finishing statement, “it has never been easier to get hijacked,” was as much a sign of the times as it was a direct criticism of the technology.

### Opening the window

The other big takeaway was that tools take up space in the context window, so returning 100 “useful” tools is usually a bad idea.

Simply reducing the number of tools the LLM is told about during a query saves space. This leads to the idea of **progressive disclosure**, which initially sounds like something from the Moulin Rouge, but is actually the idea of just responding to tool requests only with the tools needed next. Similarly, too much data returned by a query also helps fill the window of a long-running conversation. I also heard reference to “episodic memory”.

A few talks declared “**code mode**” as some sort of win – when you connect to an MCP server, the Agents SDK will fetch the MCP server’s schema, and then convert it into a TypeScript API, complete with doc comments based on the schema.

But as we saw with [GSD](https://thenewstack.io/beating-the-rot-and-getting-stuff-done/), if the LLM can write enough notes that other sub-agents can pick up and read, the context window size problem can be continually averted.

### Buying and selling the chat

“ChatGPT is the number one place to be right now” was not a statement to feed my developer mind, but it should attract some attention. ChatGPT apps are the settled name for the OpenAI tech I talked [about at the end of last year](https://thenewstack.io/openais-apps-sdk-a-developers-guide-to-getting-started/), and are clearly intended to replace the web. The idea is that MCP servers are effectively brands or corporate services. Here, discovery is the driving force, and a tool call might result in a chance to buy some pizza. Processing payments presents an inherent dilemma: How do you reduce friction while still ensuring security? And here we bounce back to the security issues.

![](https://cdn.thenewstack.io/media/2026/02/8b19f4f2-image-1-1024x454.png)

[Aaron Koivunen, Berlin MCP Community](https://www.linkedin.com/in/aaron-koivunen/)

But there is no doubt that when a user is conversing on ChatGPT, there is no context switching, and the learning curve for most tasks is pretty short.

### Conclusion

However you do it, it is still the developer’s job to build a service and expose it in an agent-friendly way. But while context windows have a finite size and security considerations are still not always implemented in full, there are clearly several paths MCP could take successfully. Maybe with some rigorous workouts, the middle-age spread can be halted.

And to end with the good advice of [**Teo Borschberg**](https://www.linkedin.com/in/teo-borschberg-94a44945/), here are some hints for starting your first internal MCP implementation:

* Pick one internal system that people constantly ask questions about
* Build one MCP server with read-only access
* Give it to five people who aren’t engineers

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)