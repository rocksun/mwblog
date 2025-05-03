# How To Set Up a Model Context Protocol Server
![Featued image for: How To Set Up a Model Context Protocol Server](https://cdn.thenewstack.io/media/2025/05/e2a1e453-levi-meir-clancy-fey5508i7m0-unsplashb-1024x576.jpg)
In this post we’ll walk through setting up a simple [Model Context Protocol (MCP)](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) server. MCP is, for now, the defacto way to communicate between LLM models and developer tools. You can read our deeper [developer primer to MCP](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) for more details, but this post doesn’t assume that knowledge.

I am going to assume you have installed [Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/), although I’m just using it as an LLM that sits in the terminal — making it easy to play with. You can still follow along regardless.

## Why MCP?
The basic idea is to keep the connection between the AI and the developer tooling separate. In the tool script that I explain below, which is just a Python method sitting in its own local server, all I will do is return a secret word. Of course, what this is doing is using the server to control the context, because LLMs don’t know what exists in your local world, unless you tell them. And of course, we want to make sure we control that ability.

Given that Anthropic created MCP, you might think that other LLM suppliers will try their own similar ideas. We know what Microsoft are like with its tendency to [extend, embrace and extinguish](https://dev.to/meatboy/what-are-modern-examples-of-embrace-extend-and-extinguish-21j3), but it seems that other suppliers have started to support MCP.

Like most connective tissue, MCP will likely get absorbed within other tools over time. So if it becomes truly successful, you will no longer be aware of it.

## Know Your Transport
In our [developer primer for MCP](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/), we noted the difference between the two protocols — [STDIO](https://mcp-framework.com/docs/Transports/stdio-transport), which means standard input/output, and [SSE (now stream transport)](https://mcp-framework.com/docs/Transports/http-stream-transport), which is more for the web. Our tool is just a simple Command Line Interface (CLI) tool, so it uses this simpler STDIO protocol. By “simple,” we mean running everything locally with no extra dependencies.

## Our MCP Server and Tool
First, set up a Python environment in a familiar way. I’m doing this on my MacBook:

We also need to install the MCP libraries:

I’ll call the script **server.py**. It combines a server and tool:

123456789101112131415161718192021222324252627282930313233343536373839404142 |
#!/usr/bin/env python3from mcp.server.fastmcp import FastMCPimport timeimport signalimport sys# Handle SIGINT (Ctrl+C) gracefullydef signal_handler(sig, frame): print("Shutting down server gracefully...") sys.exit(0)signal.signal(signal.SIGINT, signal_handler)# Create an MCP server with increased timeoutmcp = FastMCP( name="secretword", host="127.0.0.1", port=5000, # Add this to make the server more resilient timeout=30 # Increase timeout to 30 seconds)# Define our tool@mcp.tool()def secretword() -> str: """Retuen the secret word""" try: return "ABRACADABRA" except Exception as e: # Return 0 on any error return ""if __name__ == "__main__": try: print("Starting MCP server 'secretword' on 127.0.0.1:5000") # Use this approach to keep the server running mcp.run() except Exception as e: print(f"Error: {e}") # Sleep before exiting to give time for error logs time.sleep(5) |
A good bit of this is exception handling, so our interest only lies in about 15 lines. We use FastMCP to define what will be a simple server, running on port 5000. We handle a Ctrl-C via the signal handler. Other than that, our tool `secretword`
is just a method that returns the word “ABRACADABRA.” I adapted this from [mberman84’s gist](https://gist.github.com/mberman84/2faeddf57113826d7440bfadbe5ce6e5). I expect you could do something more substantial, but this proves that you can keep it simple, too.
You can test it by running it directly:

Right, stop that and let’s go back to Claude Code and tell it about our fantastic new MCP server. Oh wait, one thing: let’s make sure the server file can be run directly by Claude:

## Talking to Claude
Once you’ve installed Claude Code, it should be available in your shell. We will have to somehow inform Claude about my new server and the name of my secret-word tool.

First of all, let’s check that Claude recognizes MCP at all:

OK, we can use that advice to add our Python script, since we know it can act as an MCP server:

That’s cool.

OK, let’s run Claude (with debugging) and see how we go:

We only have one method, secretword, and it is connected to this.

Great. But let’s actually ask Claude to wield our mighty tool:

There we go. This isn’t rock solid, so the debug code in red can help us with problems. Also, they may be reporting issues that don’t effect us.

## Conclusion
Most senior developers will recognize that this is still pretty early in the protocol cycle, so there will probably be changes — I noted above that the other protocol, SSE, was deprecated last month. So grok the principles for now; this will likely be absorbed by libraries in the future.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)