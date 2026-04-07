Claude knows virtually everything that’s ever been publicly available on the internet by default. But it knows absolutely nothing about you or your data. Yes, you could always copy and paste an Excel sheet with your company’s monthly revenue, but if you’re looking at something like five years of historical enterprise sales data, it isn’t so easy to input those files.

Model Context Protocol (MCP) servers change this by connecting your data directly to Claude. Through an MCP server, Claude can suddenly bring its reasoning, judgment, and analytics to your data without requiring you to participate in any frustrating workarounds. (Raise your hand if you’ve sunk way too much time into an “it’s-so-easy” workaround.)

People are adopting AI. So why make customers load their own data? Anthropic made it pretty easy for companies to build MCP servers. The ecosystem has grown quickly in response.

Building your first MCP server isn’t so hard — and we’ll create a calculator app in an IDE (I use VS Code) and connect its functionality directly to Claude Desktop via an MCP server.

Why a calculator app? I wanted to build something easy that pulls the focus away from connecting to an external API or complicated business logic and brings it to what’s really important here: rules and best practices for building an MCP server. You can then take the skills learned in this simple application and apply them to something much more complicated next.

> Claude knows virtually everything that’s ever been publicly available on the internet by default. But it knows absolutely nothing about you or your data.

We are going to build our MCP using the TypeScript SDK ([open-source](https://github.com/modelcontextprotocol/typescript-sdk) [file here](https://github.com/modelcontextprotocol/typescript-sdk)). The Typescript and [Python SDKs](https://github.com/modelcontextprotocol/python-sdk) are the most commonly used MCP SDKs.

You will need the following to get started:

Let’s get started.

## Build an MCP server that connects to Claude

The first thing we need to do is set up our file structure and install packages in the terminal connected to your IDE.

Create a new folder and drop into it:

Initialize a Node project:

Install the MCP SDK:

Install the dependencies that allow you to compile and run Typescript locally:

Install Zod for input validation and schema generation

Build the `tsconfig.json`

Node can’t run Typescript directly. The `tsconfig.json` tells the TypeScript compiler how to convert Typescript code into JavaScript.

Add a `tsconfig.json` to your project’s root folder and paste the following code into it:

If you’re using VS Code, you may get an error in your `tsconfig.json` that says `no inputs were found in config file…..`. This is a weird thing I kept running into with VS Code. The solution, which seems like a problem itself, is to delete your `tsconfig.json` then remake the file, and paste in the same code. I don’t love it either (shrugs).

Update the `package.json` to include this expanded `scripts` object:

Create the `src` folder and `[index.ts](http://index.ts)`.

Your file structure should look like this:

### Build the MCP server

We’re going to build this all in one file, `src/[index.ts](http://index.ts)`. I’m going to paste the full code first, followed by a breakdown of what each section does, for anyone who wants to skip ahead.

**Section 1: Import the MCP SDK**

These are your import statements.

* `McpServer` creates the server.
* `StdioServerTransport` handles the communication with Claude.
* `z` validates the inputs Claude sends to our application.

**Section 2: Create the server with a name and version**

This section creates and names your server. Claude will use the name and version to identify which server it’s talking to. One of the most, if not the most important, concepts in this blog is in this section. The `server.tool()`’s name, description, Zod schema, and handler function are the heart of MCP.

**Section 3: Define the calculator tool**

Here is where we’ll build `calculate`, tell Claude what `calculate` does, what inputs it expects, and the logic to run. We’ll use the Zod schema to define the data’s shape.

**Section 4: The logic that runs when Claude calls the tool**

The business logic. This section receives Claude’s inputs, performs the requested mathematical operation, and handles edge cases.

**Section 5: Return the result as text context**

This sends the result back to Claude in the format MCP expects. Claude uses this value in its response to the user.

**Section 6: Connect over stdio**

Logic to start and connect the server to Claude Desktop using standard input/output.

We’re ready to build the project. Run the code below, and you’ll see a `dist/` folder appear in your file tree shortly after.

### Connecting to Claude

Open Claude Desktop and go to Settings > Developer > Edit Config. This will open a JSON file called `claude\_desktop\_config.json`. Add our new server to the `mcpServers` object. This file will likely launch in your IDE. Just edit and save as you would any other file.

Then quit Claude Desktop and relaunch. This is a necessary step as Claude Desktop only reads then config on startup.

After relaunching, open the top Chat section (not Cowork or Code). Then click the + icon in the bottom lefthand side of the chat input box.

![](https://cdn.thenewstack.io/media/2026/04/99fb5484-screenshot-2026-04-06-at-2.36.31-pm.png)

Then hover over Connectors and it should pop up a new menu with the calculator on it. Make sure calculator is toggled on.

![](https://cdn.thenewstack.io/media/2026/04/26f45fbe-screenshot-2026-04-06-at-2.38.05-pm.png)

Before running a calculation, tell Claude to use the calculator in the chat window. It will pop up a menu with always allow, allow once, or deny. Choose either “always allow” or “allow once”.

Now you’re ready to run a calculation. You can tell it’s using your tool while in progress because the word “request” will display under “calculate,” just below the orange Claude logo.

![](https://cdn.thenewstack.io/media/2026/04/8473d4e3-screenshot-2026-04-06-at-2.41.21-pm.png)

You can tell Claude uses your tool because it will say “Calculate >” just before it shows you the answer.

![](https://cdn.thenewstack.io/media/2026/04/a6850985-screenshot-2026-04-06-at-2.41.49-pm.png)

If you’ve made it here, you can officially say you built your first MCP. It only gets more complicated from there, but the fundamentals like defining tools with clear schemas, writing handlers that return structured responses, and connecting your server to Claude via a config file remain the same.

You now have the tools you need to connect any application you built to Claude Desktop.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)