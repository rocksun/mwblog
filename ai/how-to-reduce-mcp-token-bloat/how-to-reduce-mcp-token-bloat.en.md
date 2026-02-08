The Model Context Protocol (MCP) has reached an inflection point.

While some MCP deployments are still in the experimentation phase, many are moving the technology into operational, day-to-day use.

But as teams begin scaling MCP in real workflows, they’re discovering that running many [MCP servers](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/) simultaneously introduces severe bloat.

[Gil Feig](https://www.linkedin.com/in/gilfeig/), CTO and co-founder of [Merge](https://merge.dev), a unified API platform, tells *The New Stack* that teams rushing to add dozens of tools are now hitting scaling problems. “Agents can’t reliably choose the right tool, context windows fill with definitions, and latency compounds,” he says.

Heavy MCP usage can quickly flood an AI coding agent’s context window with memory, schemas, code, and data. Just the tool definitions alone are substantial. “We’ve seen tool metadata take 40-50% of available context,” adds Feig.

Overall, MCP adoption remains early, and best practices to curtail these issues are still emerging. [Christian Posta](https://www.linkedin.com/in/ceposta/), vice president and global field CTO at [Solo.io](http://Solo.io), a cloud-native infrastructure provider, says the answer depends on who you ask.

“If you ask me about enterprise users, it’s still very early, and some dangerous patterns are emerging,” Posta tells *The New Stack*. “The biggest downside is LLM confusion and context bloat.” As a rule of thumb, he recommends using no more than 10–15 tools at a time.

## How do we reduce MCP tool bloat?

So, the question is: how do we reduce MCP tool bloat? To optimize token usage and improve performance, experts point to several relatively straightforward shifts — such as minimizing server usage at runtime, grouping tools by domain, and deploying subagents.

Additional techniques, including just-in-time context loading, externalizing computational results, and more advanced data-filtering approaches, can also help.

Below, we’ll dive into these MCP token optimization strategies to see what the experts recommend in early 2026, and what teams are seeing when they put them into practice.

## 1. Design tools with intent

If you are [building MCP servers](https://thenewstack.io/when-is-mcp-actually-worth-it/), don’t lose scope. It’s not best to just layer MCP on top of existing REST APIs and [wrap them one-to-one](https://nordicapis.com/why-mcp-shouldnt-wrap-an-api-one-to-one/).

> “Most MCP servers simply wrap APIs and aren’t built for agentic workflows.”

Instead, the resounding recommendation is to create highly intentional MCP tools. [Alex Salazar](https://www.linkedin.com/in/alexsalazar/), co-founder and CEO, [Arcade.dev](https://www.arcade.dev/), an AI tool-calling platform, tells *The New Stack*, “Start with tool quality.”

“Most MCP servers simply wrap APIs and aren’t built for agentic workflows,” Salazar says. “Use or build MCP servers optimized for agents, with security, evals, and reliability built into the tool itself.” Done well, he adds, this approach can improve accuracy and lower token costs.

[Marcin Klimek](https://www.linkedin.com/in/klimekmarcin/), senior technical product manager, [SmartBear](https://smartbear.com/), an API management and testing company, tells *The New Stack*, “Improving token use and performance with MCP tools starts with keeping tools clear and focused on user intent.”

For Klimek, effective MCP tools are precise and return only what is needed to complete the task — nothing more. “Broad or vague requests waste tokens and slow things down,” he says. MCP tools, he adds, should have clear inputs, limited outputs, and a single purpose, much like production APIs.

In other words, an MCP tool should resemble a specific API method, not a bloated server that mirrors every endpoint in a platform.

Solo.io’s Posta makes a similar case for experience-driven API design in MCP tools. “The correct approach is to focus on MCP server design, which involves hiding multi-step, fine-grained API calls behind a single tool API,” he says.

## 2. Minimize upfront context

AI agents require the right amount of context — too little and they can’t function, too much and they drown in confusion. Therefore, when working with many MCP tools, experts recommend minimizing upfront context and expanding it only when necessary.

Context overflows often occur when tool descriptions include too much data, [Kevin Swiber](https://www.linkedin.com/in/kevinswiber/), API strategist at [Layered System](https://layered.dev/), an API and MCP consultancy, tells *The New Stack*. “It’s token-wasteful and makes it harder for the LLM to choose the right tool,” they say.

> “Load minimal schemas first and expand them only when a tool is actually used.”

Developers can reduce some of this context upfront. As [Neeraj Abhyankar](https://www.linkedin.com/in/neeraj-abhyankar-9040141/), VP of data and AI at [R Systems](https://www.rsystems.com/), a digital product engineering company, tells *The New Stack*, “Load minimal schemas first and expand them only when a tool is actually used.”

He adds that deduplicating and standardizing schemas, scoping tools into namespaces, and caching frequently used tool metadata can, in combination, cut token usage by 30–60% and boost responsiveness.

[Ori Yitzhaki](https://www.linkedin.com/in/ori--yitzhaki/), CPO at [Sonar](https://www.sonarsource.com/), agrees that schema minimization is crucial for optimizing token usage. “Developers often provide massive JSON schemas,” Yitzhaki tells The New Stack. Instead, he recommends stripping descriptions down to the essentials and using shorthand notations that the model can still interpret.’

## 3. Adopt progressive disclosure

Rather than exposing every tool at once, it’s best to limit the available MCP tools to those relevant to the task at hand.

Relevance matters, according to [Tom Moor](https://www.linkedin.com/in/tom-moor-b6213b1ba/), head of engineering at [Linear](https://linear.app/), the product management application whose MCP server has more than 250,000 users.

“Be very selective around which servers and tools you enable,” Moor tells *The New Stack*. “Most developers have only one or two core MCP servers that they make use of.”

Others agree that MCP tools should be enabled only when needed. [Matt Martin](https://www.linkedin.com/in/voxmatt/), co-founder and CEO of [Clockwise](https://www.getclockwise.com/), an AI-powered calendar company, makes a similar case.

> “Most developers have only one or two core MCP servers that they make use of.”

“You can’t have them all on at the same time,” Martin tells *The New Stack*. Teams can either enable tools manually or rely on case-specific agents to activate the required subset of tools, he adds.

“The answer keeps coming back to progressive disclosure,” says Swiber. Broadly defined, the practice involves providing only essential information upfront while hiding advanced capabilities until they are needed.

For MCP tools, this equates to separating discovery from execution, adds Feig. “Use progressive disclosure and consider building tool hierarchies where agents choose categories first, then specific tools,” he says.

## 4. Automate tool discovery

To enable progressive disclosure in an automated way, experts recommend a smart retrieval process to discover available tools. To aid this, MCP registries are emerging as catalogs to help index MCP tools and make them more searchable.

“Use progressive style discovery with search-tool style tools,” Posta says. This could involve first calling a meta tool as an abstraction. For instance, a simple `find_tool` tool could utilize an MCP registry to find tools based on semantics, authentication, capabilities, or token cost.

You can think of it as retrieval-augmented generation (RAG), but for tools themselves. “Treat the toolset like a library where only the ‘top-k’ most relevant tools are retrieved based on the user’s prompt,” says Yitzhaki. “This keeps the agent’s [working memory](https://thenewstack.io/is-agentic-metadata-the-next-infrastructure-layer/) lean and focused.”

> “Use lightweight retrieval to identify relevant tools based on requests”

Yitzhaki refers to this process as semantic routing. “Instead of loading fifty tools, load a single router tool,” he says. “The agent tells the router what it wants to do, and the router dynamically injects only the three relevant tools for that specific subtask.”

“Use lightweight retrieval to identify relevant tools based on requests, then load only those specific schemas,” recommends Merge’s Feig. This process could help narrow down 100 tools into a few relevant ones, he adds.

## 5. Use subagents

Building on that idea, some recommend using tool-specialized subagents, each with access to its own capabilities, rather than a single monolithic agent with access to all tools. Doing so can optimize token usage by keeping MCP tools use on a per-case basis.

[Ankit Jain](https://www.linkedin.com/in/ankitjaindce/), CEO, [Aviator](https://www.aviator.co/), a collaborative AI coding assistant, says a segmented approach gives each subagent clear boundaries. For instance, if you have fifteen total tools, you could seperate access to individual tools to subagents focused on specific domains, such as read-only MCP tools, file-editing-only tools, or testing-only tools.

“Token overhead drops 50-60%, and there’s no confusion about role,” Jain tells *The New Stack*.

Creating higher-level tools for tool groups can help case-specific agents understand what to access. “Bundle related operations into higher-level tools,” says Merge’s Feig. “Instead of separate create, update, and delete tools, create a management tool that handles common workflows.”

## 6. Try code-based execution

Another way around token inefficiencies is to use an architecture called [code mode](https://thenewstack.io/port-of-context-the-open-source-code-mode/), also known as a code execution style, in which agents write and execute code to call MCP servers.

This architecture prevents an LLM from having to orchestrate complex workflows and tool calls in natural language, reducing the amount of state that must be stored in context windows.

> “Delegate the workflow away from the context window”

“Delegate the workflow away from the context window into separate code execution,” recommends Swiber. “The LLM generates workflow code that runs elsewhere. The context window never sees intermediate results, and you save on tokens.”

Others also view code-execution-style tool calling as a promising direction. “Let the LLM model write code to call tools directly, again, based on some source of truth, MCP discovery, such as an MCP registry,” says Posta.

## 7. Perform semantic caching

[Semantic caching](https://thenewstack.io/what-is-semantic-caching/) is another process that can avoid direct calls to LLMs and context windows altogether. The approach attempts to match incoming user queries with semantically similar past queries and reuse cached responses before making requests to LLM APIs.

By caching frequently used data, such as tool definitions or other information that is unlikely to change, teams can avoid unnecessary LLM and MCP calls in some situations.

## 8. Remember prompt engineering

[Melissa Ruzzi](https://www.linkedin.com/in/melissa-r-94b25a28/), director of AI at [AppOmni](https://appomni.com/)), a SaaS security company, adds that [solid prompting practices](https://leaddev.com/software-quality/7-prompting-strategies-to-sharpen-your-ai-assisted-code) are key to avoiding unpredictable outcomes, which are heightened when using MCP.

“Prompt instructions and prompt examples are best practices when using any agent that has tools,” Ruzzi tells *The New Stack*. “This is because the tools are connected to the LLM, meaning the model will choose and use tools in an unsupervised fashion.”

## 9. Practice data hygiene

Other methods to reduce MCP bloat involve maintaining good data handling practices overall.

Marcin Klimek of SmartBear recommends fetching data incrementally — starting with small responses such as summaries or IDs, and requesting detailed data only when it’s clearly needed.

> “Use structured responses and reuse the same schemas across tools.”

“Keep data clean and compact, use structured responses and reuse the same schemas across tools, and do not repeat large outputs in later prompts,” says Klimek. “Summarize them instead.”

## 10. Consider externalizing control

Then, beyond tooling and orchestration, there are all the other operational aspects to consider that could bloat context windows. This could include governance, policy enforcement, authentication, and error handling.

There’s a growing case for externalizing these concerns into a runtime layer, rather than embedding them directly into every tool. “A runtime that handles these concerns centrally keeps tools lean, reduces failure modes, and avoids bloating the context window with redundant logic,” says Arcade.dev’s Salazar.

A platform to centralize MCP management could also help surface relevant tools to reduce token overhead. “A well-designed runtime can also handle dynamic tool selection automatically, removing the need for upfront restrictions while still keeping workflows efficient and accurate,” adds Salazar.

Posta similarly recommends using an agent gateway with virtual-MCP capabilities. To his point, numerous [MCP-compatible API gateways](https://nordicapis.com/10-api-gateways-that-support-mcp/) and AI gateways now support these functions.

## Reality is setting in

There are plenty of MCP early adopters, but many organizations are still figuring out how to roll MCP out at scale.

“MCP adoption is messy,” says Aviator’s Jain. “Individual developers are bolting on five to ten tools without thinking about cost. Enterprise teams are paralyzed by unpredictable token usage.”

Even so, MCP is becoming a core fixture of agentic software development. “It’s moving from a ‘cool feature’ to a core piece of enterprise architecture,” Yitzhaki adds.

With this momentum, friction in the realities of scaling MCP usage is starting to seep in. It’s forcing a rethink of how best to manage orchestration, tool calls, and context.

Thankfully, by following some of the tips above — limiting tool access, adopting progressive disclosure, and using smart context management with meta tools and sub-agents — teams can rein in token bloat without sacrificing capability.

In practice, MCP optimization is less about a single technique and more about disciplined system design.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/02/96a1456d-cropped-e7e1c083-bill-doerrfeld.jpg)

Bill Doerrfeld is a tech journalist and API thought leader. He is the editor-in-chief of the Nordic APIs blog, a global API community dedicated to making the world more programmable. He is also an active contributor to a handful of...

Read more from Bill Doerrfeld](https://thenewstack.io/author/bill-doerrfeld/)