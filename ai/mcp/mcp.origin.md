# MCP Protocol: a new AI dev tools building block
### The Model Context Protocol that extends IDEs’ AI capabilities is gaining rapid popularity. Why is this, and why should us developers pay attention to it?
*Before we start: this is the last week of the “What’s in your tech stack?” survey. If you’ve not yet done so, please fill out this survey and tell us about it. If you take part and fill out the survey, you will receive the full results early, plus some extra, exclusive analysis from myself and Elin. (Full results, minus the exclusive analysis will be published in The Pragmatic Engineer). It takes as little as 5 minutes to fill — thank you for your help!*
One hot topic at the intersection of AI coding tools and developer tooling has been the MCP Protocol (Model Context Protocol), [introduced](https://www.anthropic.com/news/model-context-protocol) in November 2024 by Anthropic. It has exploded in popularity, with AI models and developer tools keen to add support for it.

An analogy for MCP is that it’s a “USB-C port of AI applications”, in that it creates a universal extension point for LLMs and dev tools to connect to each other with; databases, ticketing systems, etc. The concept is becoming popular in other areas, but MCP began as a way to extend the capabilities of developer IDEs like Claude Desktop, Claude Code, VS Code, Cursor, Windsurf and others. Today, we focus on this area, covering:

**What is MCP? A practical example**. Previously, I used a separate tool to query my database in the production application. But with MCP, I can “talk” to my database from the IDE, which feels like a game changer!**Origin of MCP.**Two engineers at Anthropic – David Soria Parra and Justin Spahr-Summers – scratched an itch to make Claude Desktop work better with developer tools.**Understand Language Server Protocol (LSP) to understand MCP.**Many core ideas of MCP come from Microsoft’s approach to make it easier for IDEs to add programming language support.**MCP architecture.**Clients and servers, where servers are often processes running locally.**Inside an MCP server’s source code.**How a simple, local MCP server helps us understand how it works.**Security threats.**Protection looks woefully fragile with the current MCP implementation, and attackers are likely to jump at chances to get SSH keys and other private credentials which local MCP servers can easily get unauthorized access to. This area needs to get better, and fast.**Futuristic use cases.**Connecting Figma with VS Code, 3D modeling via Cursor, and controlling a 3D printer from Windsurf; all this is possible with MCP. Also: MCP is gaining momentum beyond IDEs.
*For this piece, I talked with MCP co-creator, David Soria Parra, software engineer at Anthropic. Thank you for the input!*
## 1. What is MCP? A practical example
I have an API that powers [this microsite](https://api.pragmaticengineer.com/kagi_and_perplexity) where annual paid members can request a promo code for 12 months of complimentary access to Perplexity and 3 months of Kagi. The site runs on Node.js, using TypeScript, and uses PostgreSQL as its database.

Whenever I tweak the back or frontends and modify data, I have two things open:

My IDE with the code itself, plus the in-IDE terminal

A database admin interface to query the tables or modify schemas, if needed. I use PgAdmin.

IDEs are getting ever smarter with LLM functionality; Windsurf and Cursor have agentic capabilities, so can suggest edits to multiple files at once. However, they cannot connect to my PostgreSQL database to query data. But with MCP, they can – and so can I.

MCP stands for Model Context Protocol, and is a bridge to allow LLM tools such as AI-enhanced IDEs like Cursor, Windsurf and others, to access additional tools.

Here’s how I use LLM prompts to make my database accessible inside of my IDE. For this example, I used Windsurf, but the same can be done in Cursor, Zed, and VS Code.

#### Adding a PostgreSQL MCP Server to my IDE
To start, in Settings, under Cascade (Windsurf’s agentic capability), I select “Add MCP Server.” Here, a dropdown with pre-built ones are shown:

Adding it means configuring the connection string to your database, which can be to a local Postgres database running on your machine, or remotely. I used a remote connection string to connect to the one on my server. Once added, the connected database shows up as an MCP Server, ready to use:

Going forward, for any command inputted to the Cascade interface, the LLM can decide to use this server. Let me start with a question about promotional codes:

“How many users claimed kagi promo codes in the last 10 days?”

The LLM tries to generate an SQL server to get the answer, but hallucinates the table name (which is typical-enough for LLMs):

**However, this is where the “magic” begins, thanks to the LLM iterating more — using this new database tool it can utilize. **The LLM turns to my PostgreSQL instance to find the correct table name:
![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24913b96-1fa3-45f0-90b9-30d40cf17588_1600x707.png)
![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24913b96-1fa3-45f0-90b9-30d40cf17588_1600x707.png)
It then makes another query:

D’oh! – the column names are wrong, again! But it queries the table definition and corrects it rapidly:

Finally, it gets it right:

What’s so impressive is that the process took a few seconds, and I never had to add any input. The LLM “figured out” the correct table and column names by having access to the database.

#### LLM layer above PostgreSQL
Now I’ve added my database as an MCP server, I can “talk” to my data using natural language, and the LLM does the conversion to SQL, and then re-converts to my question. This is not limited to simple questions with a simple SQL query, but also to more ambiguous ones.

Other questions I’ve asked:

"Has there been an unusual spike of signups the last 2 months?"

"Which suspicious-looking emails have signed up recently? Any patterns?"

"Which domains have the most signups?"

"How many unclaimed promo codes are left?"

**Being able to converse with dev tools through my IDE feels like “the future”. **It’s not that I couldn’t find answers to the questions above without it; I *could have* written SQL commands, or a series of them, or a small program to loop commands, and summarized them. However, I probably wouldn’t bother because it takes time to type out SQL. But because I can easily type questions, I did!
Think about what happens when you can “talk” to your developer tools via the IDE. For example, using natural language to interact with:

Source control system (“can you create a pull request with all changes except for the one in index.ts?”)

Databases (“can you create a new table for signup logging. Use an incremental counter for primary key and store the timestamp for each log”)

Ticketing/bug tracking system (“are there bugs filed relating to this feature?”)

Observability provider (“has there been any spikes related to login errors or logout errors in the last week?”)

Feature flags / experimentation system (“which flags have been fully rolled out for at least a week? Can you help identify these and make a PR that removes them?”)

It makes work easier to be able to use these tools from the IDE. Also, if we can use them, then so can AI agents, meaning they can do more complex tasks.

**It feels to me that the MCP concept could be another step forward for developer productivity.** It will likely also boost AI agents’ capabilities because they have extra tools for more complex tasks. It’s hard to foresee commercial vendors *not* scrambling to add MCP servers, which will let customers use tools more easily from IDEs.
As developers, we’ll be able to experiment with tools to make us more productive. *A caveat is that the MCP is still early-stage and lacks vetted marketplaces, support in IDEs for MCP is barely a few months old, and also MCP implementations have many worrying security gaps – covered in “Security threats” below.*

## 2. Origin of MCP
The MCP protocol was conceived and built by two software engineers at Anthropic, [David Soria Parra](https://www.linkedin.com/in/david-soria-parra-4a78b3a/) and [Justin Spahr-Summers](https://www.linkedin.com/in/jspahrsummers/). David shared the origin story in a [Latent Space podcast episode](https://www.latent.space/p/mcp).

“In July 2024, I was working on internal developer tooling. There was an effort to empower more employees at Anthropic to integrate really deeply with the models we have and dogfood our model as much as we can.

Coming from a development tooling background, I quickly started to appreciate how amazing Claude Desktop is – with features like Artifacts – but got frustrated by how it had a limited feature set, with no way to extend it. At the same time, I do my day-to-day work in the IDE. The IDE has access to things like the local file system, but doesn’t have a tool like Artifacts or something similar.

I was constantly copying things back and forth between Claude Desktop and the IDE, which got me frustrated. I thought I knew how to build all integrations, but what would I need to do to let these IDEs build integrations?

When you look closer, you see that the “AI integration” problem is an MxN one. You have M applications (like IDEs) and N integrations.

While mulling this problem, I was working on a

[Language Server Protocol](LSP) project internally – and this project did not go anywhere. But put these ideas together; an LSP, plus frustration with IDE integrations, let it cook for a few weeks, and out comes the idea of ‘let’s build some protocol to solve for it.’”
For more on the history of the MCP protocol, you can listen to [this Latent Space podcast episode](https://www.latent.space/p/mcp).

#### Open sourcing the MCP protocol
David teamed up with fellow engineer, Justin, and they built early prototypes, kept iterating, and six weeks later had the first working MCP integration for Claude Desktop.

They shared the prototype internally, and engineering colleagues at Anthropic were excited. While preparing to open source the protocol, people built a variety of interesting applications at an internal Anthropic hackathon, including an MCP server controlling a 3D printer. It confirmed David and Justin’s sense that MCP could be very useful in the real world.

They did more polishing and [announced](https://www.anthropic.com/news/model-context-protocol) the open sourcing of the MCP Protocol on 25 November, last year. At that time, MCP protocol was:

[A website](https://modelcontextprotocol.io/introduction)that outlines the protocol; how to implement an MCP server; and guides for clients (like IDEs on how to integrate the protocol)[The specification](https://spec.modelcontextprotocol.io)of the protocol itself[SDKs](https://modelcontextprotocol.io/introduction)for Python, TypeScript, Java, Kotlin and C#[Examples](https://modelcontextprotocol.io/examples)of server and client implementations for reference
#### Rapid industry adoption
In just four months, MCP went from being a neat protocol that Claude Desktop used, and which was open sourced, and to all major IDEs, with AI tools adding MCP support, including OpenAI:

Jul 2024: development on MCP starts inside Anthropic

Aug:

January 2025:

February:

March:

April:

**VS Code**[adds](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)MCP support**GitHub**launches its[official MCP server](https://github.blog/changelog/2025-04-04-github-mcp-server-public-preview/)(in public preview)**Zapier**[launches](https://zapier.com/blog/mcp/)a list of MCP servers**CI/CD services like**and[Bitrise](https://bitrise.io/blog/post/chat-with-your-builds-ci-and-more-introducing-the-bitrise-mcp-server)(CI/CD) launch their MCP servers[CircleCI](https://github.com/CircleCI-Public/mcp-server-circleci)
The only notable IDE currently absent is JetBrains IDEs, which [is set to introduce](https://www.reddit.com/r/Jetbrains/comments/1jqjqnw/someone_please_create_a_mcp_client_plugin/) MCP support in the next IDE release, expected soon. It’s rare to see such fast adoption across all major IDEs. Clearly, MCP is providing a big benefit for developers using AI tools, so IDEs want to add it. *Coincidentally, the top IDEs that engineers most frequently mentioned as IDEs with AI functionality they love – Cursor, VS Code, Windsurf, Zed, Neovim and Cline – have all been amongst the first to ship MCP support!*

But how do they work?

## 3. Understand LSP to understand MCP
Let’s take a diversion into the world of Language Server Protocols because this is the solution that inspired MCP.

A common problem that IDEs had for decades was that they wanted to add support for as many programming languages as possible, which also meant adding support for things like:

Syntax highlighting

Code completion (autocomplete)

Marking of warnings / errors inline

Offering simple refactoring operations

Assuming there are M IDEs out there, and N programming languages, this is an MxN problem. The naive solution was for each M IDE to build manual support for each N language, as best as possible. For IDE vendors, this was a lot of work, and work that must be repeated whenever a new programming language starts to spread:

For us developers, this meant IDEs only supported only a limited number of languages well. For example, good luck trying to code using C# in Android Studio!

**Extensions / plugins** are a workaround for an IDE to do the heavy lifting: IDEs supporting extension/plugin frameworks could have third-party developers build plugins like syntax highlighting for a specific language. This is better than nothing, but is a lot of work for devs. Also, many IDEs don’t provide extension capabilities that offer a pleasant developer experience for things like autocompletion and syntax highlighting.
In 2016, Microsoft released the **Language Server Protocol (LSP)** specification, a protocol originally developed for Visual Studio Code. The idea is that for each language, an LSP server implementation can provide language features. Editors could now use the LSP server – an existing implementation that’s often open source – not build their own:

This transformed how many IDEs are developed:

New and existing IDEs can easily add language support for new languages, thanks to an easy-to-follow protocol (the LSP)

For most languages, there’s an official LSP implementation provided by the language maintainers (like

[gopls](https://github.com/golang/tools/tree/master/gopls)for Go), and often several LSP implementations developers or IDE vendors can choose from. For example, for C#, popular LSPs include[OmniSharp](https://github.com/OmniSharp/omnisharp-roslyn)and[csharp-ls](https://github.com/razzmatazz/csharp-language-server)
Today, IDEs that support LSP include:

**VS Code**Thanks to this, all VS Code folks like

**Cursor**,**Windsurf,**etc
**Zed**Editor**IntelliJ**IDEs**Eclipse, Neovim, Emacs**Many other smaller editors like Atom,

[Helix Editor](https://helix-editor.com/),[Kate](https://kate-editor.org/en-gb/), and more
Notable absentees include:

Visual Studio – Microsoft’s flagship IDE (not to be confused with VS Code). Uses proprietary language tools to support languages

XCode – there is an official Swift LSP Server, but XCode relies on its proprietary code intelligence system

Android Studio: no LSP support due to the IDE being based on the IntelliJ Community Edition, therefore supporting a more limited set of programming languages than fully fledged IntelliJ IDEs

## 4. MCP architecture
What David and Justin took from the success of LSP was that the protocol allowed: