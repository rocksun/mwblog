# Exploring the JetBrains AI Assistant for Visual Studio Code
![Featued image for: Exploring the JetBrains AI Assistant for Visual Studio Code](https://cdn.thenewstack.io/media/2025/05/14b2239b-alex-shuper-8-zt2ne-vnk-unsplashb-1024x576.jpg)
A while ago I looked at the [JetBrains AI assistant for its own stable of IDEs](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/), but we can now work in [Visual Studio Code with JetBrains AI Assistant](https://www.jetbrains.com/aia-vscode/) as an extension. As I’ve noted before, I’ve had some difficulties switching between Large Language Model (LLM) code extensions within VS Code, so I will tread carefully when installing this public preview.

JetBrains is respected for its work on IntelliJ, so I wasn’t entirely sure why the company wrote a VS Code extension for its AI Assistant — which was relatively late to the LLM party. The reason given is “in order to reach a broader developer community and demonstrate our commitment to IDE-agnostic AI assistance,” but either way I was happy to put it through its paces.

In this post, I’ll go over this AI assistant in detail — but if you only want to plug in and play, then just read the bits that contrast what JetBrains does compared with standard assistant behaviour. By now, I expect most developers will be familiar with using LLMs while coding.

First of all, I want to stop Copilot in VS Code, which is the LLM that inhabits VS Code by default. After installing JetBrains AI Assistant, you can see both their icons are on the bottom ribbon.

Both appear to be “ready” even though I haven’t logged into JetBrains yet. However, I am able to disable Copilot from the extensions view. The Copilot icon is still present, but with a cross through it.

You can now log into your JetBrains account (I had a licence left over from the previous review). You’ll arrive at a smart little explanation of their LLM services:

Near the bottom is the small chat and context box:

Like Github Copilot, the dropdown has options for chat, multi-file Edit, and Agent. Each one takes a greater quota consumption of the new gold: tokens. Note that **GPT-4o** is the default model. The model dropdown list includes the other usual suspects.

In this post, I’ll focus on actions the LLM can take within the IDE (i.e., not leaving the interface for the chatbot). The first is code completion:

This remains the LLM staple. You have to train your muscle memory to remember Tab, otherwise suggestions will disappear if you type over them. This is the default behaviour for code completion. As I was working with [Model Context Protocol (MCP)](https://thenewstack.io/tutorial-set-up-an-mcp-server-with-net-and-github-copilot/) server code in a previous post, I still have that code in an open tab. As an example of a suggestion, below our existing code I typed a class signature and the letters “He” and completion did the rest after the cursor:

This is a typical bit of “text wrangling.” What it did was to effectively create a template for a minimal MCP Server tool — which is the context that it read from the file. (At some point, the AI threw several internal errors that it did not explain, but this had no outward effect. Remember, this is just a public preview.)

We then have code explanation, which is the fast way to get to grips with an unfamiliar codebase:

Again, this is a standard for any LLM code assistant. Two menus deep is about right for this option, because it isn’t regularly needed very often for a code fragment:

Applied to our existing MCP tool from last time, it produces a large verbiage explaining everything in detail. But the important part is the summary:

*“So, to summarize, this class is going to be used as a tool in a MCP server, and when it’s called, it will always return the word ‘ABRACADABRA’.”*
This is very useful, as it understands both the context of the code (in this case, it’s for MCP) as well as what it does (just return the static string). This is where the true value is; I would recommend that this should be returned in preference to the detailed stuff, which is mainly superfluous.

After the verbiage created from Explain This, it is hardly surprising that documentation can be easily created. This is done as a correctly placed comment on our original fragment:

123456789101112 |
/// <summary> /// Represents a tool within the McpServer framework used for secret word handling. /// </summary> /// <remarks> /// This tool provides a method to reveal a predefined secret word upon invocation. /// It can be extended or used as part of McpServer tool functionalities. /// </remarks> [McpServerToolType] public static class SecretwordTool { [McpServerTool, Description("Reveal the secret word.")] public static string Secretword(string message) => "ABRACADABRA"; } |
This is fairly trivial, but I like the fact that it understands how a comment differs from raw explanation — it doesn’t pretend that the word “ABRACADBRA” is part of the design. Then again, semantic interpretation is exactly what LLMs do well.
The next action is less straightforward:

While I’m not using VS Code to manage source control, all my example files are within a git repository.

I opened Source Control and got the tab to confirm that I haven’t checked anything in recently. However, the JetBrains spiral icon is indeed present:

Unfortunately, I had no staged files, and the message it created (about error handling) was meaningless, as I have no idea what it was referring to. In git, code must be staged (usually with the **add** command) before it is committed. JetBrains needs to put a little more work into this.

That leaves the chat-style LLM, which doesn’t need the VS Code interface, and therefore, there is little point in examining this. I would recommend using something like [Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/) if you don’t need the IDE open in the first place. Even multifile edits do not really benefit from the presence of an IDE.

## Conclusion
As I’ve indicated, I don’t exactly know what JetBrains achieves with this extension, apart from making a user spend tokens via its backend services. This isn’t a JetBrians IDE and they don’t claim to be making LLMs. Perhaps the “IDE-agnostic AI Assistance” market is more than just marketing.

However, JetBrains hasn’t really created a compelling UI experience here. That said, I think many .NET developers will be happy to trust the JetBrains brand, and perhaps this foothold will precede some more interesting offerings in the future.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)