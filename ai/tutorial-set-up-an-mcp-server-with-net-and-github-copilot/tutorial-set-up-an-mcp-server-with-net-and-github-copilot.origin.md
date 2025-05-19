# Tutorial: Set Up an MCP Server With .NET and GitHub Copilot
![Featued image for: Tutorial: Set Up an MCP Server With .NET and GitHub Copilot](https://cdn.thenewstack.io/media/2025/05/cc7db21a-chris-barbalis-j698hh61hpo-unsplashb-1024x576.jpg)
There has been an explosion of interest in [Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP), which is a good sign that people are trying to build different solutions using Large Language Models (LLMs), but now with their own systems. MCP is the middleman between LLMs and your tools.

After doing a short [Python example with Claude Code](https://thenewstack.io/how-to-set-up-a-model-context-protocol-server/), I thought I’d expand with a C# version using Github Copilot — all within Visual Studio Code. The advantage of using an IDE is that we will get the chance to integrate with other MCP servers without leaving the IDE.

Microsoft has covered [MCP since April](https://devblogs.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol), and my post has its origins in this [Dev Blog](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/) post. While Microsoft doesn’t usually work at pace, they are good at showing their progress these days. I’m going to assume you have VS Code and have signed into GitHub Copilot.

## Inside Track
Since Microsoft is rolling this out, you might already have VS Code powered with “agent mode.” This is clearly where they will focus their agentic solutions. Just turn on Github Copilot chat and look at the bottom of the screen, at the “Ask” dropdown:

If you don’t have Agent mode, you can try searching (in the command palette) for user settings.

And if that doesn’t work, or you don’t want to mess with your IDE, you can get hold of [Visual Studio Code Insiders](https://code.visualstudio.com/insiders/). This is where the latest builds (but probably not the most stable) are hosted. Don’t worry, though, because this is designed to sit next to your stable VS Code.

This is quite a neat move, as it allows Microsoft to follow new trends like MCP without sinking their fleet. The only other thing you should do before we start is add “code-insiders” to your command path so that we can find it from the command shell. Just start typing “shell command” in the Command Palette:

Just so you are confident they can run together, I can assure you they look different in the dock:

Code-insiders is the one in green!

Now, let’s get what we need for the MCP server.

## Setting Up the MCP Server
Starting in the command shell, let’s set up a .NET console project for MCP:

Then let’s go into the project and explicitly add some packages. We should be able to do this in VS Code, too, but we can be more specific here:

Now let’s open up VS Code from the project directory in the command line. Doing this ensures you inherit the context properly:

Then replace the template **Program.cs** with the code to set up an MCP server:

1234567891011121314151617 |
using Microsoft.Extensions.DependencyInjection; using Microsoft.Extensions.Hosting; using ModelContextProtocol.Server; using System.ComponentModel; var builder = Host.CreateApplicationBuilder(args); builder.Logging.AddConsole(consoleLogOptions => { // Configure all logs to go to stderr consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace; }); builder.Services .AddMcpServer() .WithStdioServerTransport() .WithToolsFromAssembly(); await builder.Build().RunAsync(); |
This is not too different in principle from the Python example from [a couple of weeks back](https://thenewstack.io/how-to-set-up-a-model-context-protocol-server/). Note the request to search for tools in the running assembly. This is the introspection equivalent that we did in Python. The MCP server effectively acts as a container, and it advertises its available tools.
I’ll use the same simple Secretword tool from that Python example. It just returns our secret word:

123456 |
[McpServerToolType]public static class SecretwordTool{ [McpServerTool, Description("Reveal the secret word.")] public static string Secretword(string message) => "ABRACADABRA";} |
Note that the attribute (the term in square brackets that provides a metadata cue about the code below it) marks the method as an MCP tool. Again, we have that curse of MCP: the slight confusion between server and tool. These attribute names don’t really help.
Now, click the “select tools” spanner icon in the chat box:

You should see a list of tools. We are now going to register our new tool.

Search for MCP settings in the settings tab, via the cog at the bottom left:

Click the “Edit in settings” link and you’ll see the settings JSON file:

The MCP section might be empty, or in this case, have the default time tool. Look closely and you’ll see the “Start” arrow just above the method name within “servers”.

Simply add the following (or replace the example) in the JSON file to describe our tool:

1234567891011121314 |
{ "inputs": [], "servers": { "thenewstackMCP": { "type": "stdio", "command": "dotnet", "args": [ "run", "--project", "/Users/eastmad/thenewstack/thenewstackMCP/thenewstackMCP.csproj" ] } }} |
My absolute path is for my MacBook. I described STDIO in my [last post on MCP](https://thenewstack.io/how-to-set-up-a-model-context-protocol-server/).
Save it. Now hit the “start” button that should appear just above:

Going back to our chat box, we can see that the refresh button has spotted our new tool. So click that and the “select tools” button again, and you’ll see this at the end of the list of tools:

Yes, we exist! Yay.

## Asking Copilot For the Secret Word
Now we can run Secretword directly through Copilot chat. That is, Copilot now understands semantically that there is a tool called “secretword” that it has access to:

Microsoft is aware that with this level of indirection, a user might now be persuaded to run code without realizing it. For this reason, the system interrupts the conversation to check that this is intended.

That blue “Continue” box sets permissions for the session, including whether to allow the tool to run. Once we do so, we get the result from ChatGPT:

After that, we can go on to extend the tools to something more useful.

## Conclusion
If we compare this process with the Python example with Claude Code, I don’t think we get a lot of advantages from Visual Code integration yet — because MCP is clearly a bolt-on for now. This is clearly aimed at early developers trying to figure our the MCP workflow and ramifications.

I can envisage Microsoft forcing their own solution onto users in time, but this is where we are now. Everyone is at the MCP party.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)