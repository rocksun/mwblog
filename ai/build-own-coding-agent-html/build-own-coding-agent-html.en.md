## The wave of CLI Coding Agents

If you have tried Claude Code, Gemini Code, Open Code or Simon
Willison’s [LLM CLI](https://github.com/simonw/llm), you’ve experienced something fundamentally
different from ChatGPT or Github Copilot. These aren’t just chatbots or
autocomplete tools - they’re agents that can read your code, run your
tests, search docs and make changes to your codebase async.

But how do they work? For me the best way to understand how any tool
works is to try and build it myself. So that’s exactly what we did, and in
this article I’ll take you through how we built our own CLI Coding Agent
using the Pydantic-AI framework and the Model Context Protocol (MCP).
You’ll see not just how to assemble the pieces but why each capability
matters and how it changes the way you can work with code.

Our implementation leverages AWS Bedrock but with Pydantic-AI you could
easily use any other mainstream provider or even a fully local LLM.

## Why Build When You Can Buy?

Before diving into the technical implementation, let's examine why we
chose to build our own solution.

The answer became clear very quickly using our custom agent, while
commercial tools are impressive, they’re built for general use cases. Our
agent was fully customised to our internal context and all the little
eccentricities of our specific project. More importantly, building it gave
us insights into how these systems work and the quality of our own GenAI
Platform and Dev Tooling.

Think of it like learning to cook. You can eat at restaurants forever
but understanding how flavours combine and techniques work makes you
appreciate food differently - and lets you create exactly what you
want.

## The Architecture of Our Development Agent

At a high level, our coding assistant consists of several key
components:

* Core AI Model: Claude from Anthropic accessed through AWS Bedrock
* Pydantic-AI Framework: provides the agent framework and many helpful
  utilities to make our Agent more useful immediately
* MCP Servers: independent processes that give the agent specialised
  tools, MCP is a common standard for defining the servers that contain these
  tools.
* CLI Interface: how users interact with the assistant

The magic happens through the Model Context Protocol (MCP), which
allows the AI model to use various tools through a standardized interface.
This architecture makes our assistant highly extensible - we can easily
add new capabilities by implementing additional MCP servers, but we’re
getting ahead of ourselves.

## Starting Simple: The Foundation

We started by creating a basic project structure and installing the
necessary dependencies:

```
uv init
uv add pydantic_ai
uv add boto3

```

Our primary dependencies include:

* `pydantic-ai`: Framework for building AI agents
* `boto3`: For AWS API interactions

We chose Claude Sonnet 4 from Anthropic (accessed via AWS Bedrock) as
our foundation model due to its strong code understanding and generation
capabilities. Here's how we configured it in our `main.py`:

```
import boto3
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.providers.bedrock import BedrockProvider

```

```
bedrock_config = BotocoreConfig(
    read_timeout=300,
    connect_timeout=60,
    retries={"max_attempts": 3},
)
bedrock_client = boto3.client(
    "bedrock-runtime", region_name="eu-central-1", config=bedrock_config
)
model = BedrockConverseModel(
    "eu.anthropic.claude-sonnet-4-20250514-v1:0",
    provider=BedrockProvider(bedrock_client=bedrock_client),
)
agent = Agent(
    model=model,
)

```

```
if __name__ == "__main__":
  agent.to_cli_sync()

```

At this stage we already have a fully working CLI with a chat interface
which we can use as you would a GUI chat interface, which is pretty cool
for how little code this is! However we can definitely improve upon
this.

## First Capability: Testing!

Instead of running the tests ourselves after each coding iteration why
not get the agent to do it? Seems simple right?

```
import subprocess

```

```
@agent.tool_plain()
def run_unit_tests() -> str:
    """Run unit tests using uv."""
    result = subprocess.run(
        ["uv", "run", "pytest", "-xvs", "tests/"], capture_output=True, text=True
    )
    return result.stdout

```

Here we use the same pytest command you would run in the terminal (I’ve
shortened ours for the article). Now something magical happened. I could
say “X isn’t working” and the agent would:

* 1. Run the test suite
* 2. Identify which specific tests were failing
* 3. Analyze the error messages
* 4. Suggest targeted fixes.

**The workflow change:** Instead of staring at test failures or copy
pasting terminal outputs into ChatGPT we now give our agent super relevant
context about any issues in our codebase.

However we noticed our agent sometimes “fixed” failing tests by
suggesting changes to the tests, not the actual implementation. This led
to our next addition.

## Adding Intelligence: Instructions and intent

We realised we needed to teach our agent a little more about our
development philosophy and steer it away from bad behaviours.

```
instructions = """
You are a specialised agent for maintaining and developing the XXXXXX codebase.

## Development Guidelines:

1. **Test Failures:**
   - When tests fail, fix the implementation first, not the tests
   - Tests represent expected behavior; implementation should conform to tests
   - Only modify tests if they clearly don't match specifications

2. **Code Changes:**
   - Make the smallest possible changes to fix issues
   - Focus on fixing the specific problem rather than rewriting large portions
   - Add unit tests for all new functionality before implementing it

3. **Best Practices:**
   - Keep functions small with a single responsibility
   - Implement proper error handling with appropriate exceptions
   - Be mindful of configuration dependencies in tests

Remember to examine test failure messages carefully to understand the root cause before making any changes.
"""

```

```
agent = Agent(
instructions=instructions,
model=model,
)

```

**The workflow change:** The agent now understands our values around
Test Driven Development and minimal changes. It stopped suggesting large
refactors where a small fix would do (Mostly).

Now while we could continue building everything from absolute scratch
and tweaking our prompts for days we want to go fast and use some tools
other people have built - Enter Model Context Protocol (MCP).

## The MCP Revolution: Pluggable Capabilities

This is where our agent transformed from a helpful assistant to
something approaching the commercial CLI agents. The Model Context
Protocol (MCP) allows us to add sophisticated capabilities by running
specialized servers.

> MCP is an open protocol that standardizes how applications provide
> context to LLMs. Think of MCP like a USB-C port for AI applications.
> Just as USB-C provides a standardized way to connect your devices to
> various peripherals and accessories, MCP provides a standardized way to
> connect AI models to different data sources and tools.
>
> -- [MCP Introduction](https://modelcontextprotocol.io/introduction)

We can run these servers as a local process, so no data sharing, where
we interact with STDIN/STDOUT to keep things simple and local. [(More details on tools and MCP)](/articles/function-call-LLM.html)

## Sandboxed Python Execution

Using large language models to do calculations or executing arbitrary code they create is not effective and potentially very dangerous! To make our Agent more accurate and safe our first MCP addition was Pydantic Al’s default server for sandboxed Python code execution:

```
run_python = MCPServerStdio(
    "deno",
    args=[
        "run",
        "-N",
        "-R=node_modules",
        "-W=node_modules",
        "--node-modules-dir=auto",
        "jsr:@pydantic/mcp-run-python",
        "stdio",
    ],
)

```

```
agent = Agent(
    ...
    mcp_servers=[
        run_python
    ],
)

```

This gave our agent a sandbox where it could test ideas, prototype
solutions, and verify its own suggestions.

NOTE: This is very different from running the tests where we need the
local environment and is intended to be used to make calculations much
more robust. This is because writing the code to output a number and then
executing that code is much more reliable and understandable, scalable and
repeatable than just generating the next token in a calculation. We have
seen from frontier labs (including their leaked instructions) that this is
a much better approach.

**The workflow change:** Doing calculations, even more complex ones,
became significantly more reliable. This is useful for many things like
dates, sums, counts etc. It also allows for a rapid iteration cycle of
simple python code.

## Up-to-Date library Documentation

LLMs are mostly trained in batch on historical data this gives a fixed
cutoff while languages and dependencies continue to change and improve so
we added [Context7](https://context7.com/) for access to up to date python
library documentation in LLM consumable format:

```
context7 = MCPServerStdio(
    command="npx", args=["-y", "@upstash/context7-mcp"], tool_prefix="context"
)

```

**The workflow change:** When working with newer libraries or trying to
use advanced features, the agent could look up current documentation
rather than relying on potentially outdated training data. This made it
much more reliable for real-world development work.

## AWS MCPs

Since this particular agent was built with an AWS platform in mind, we
added the AWS Labs MCP servers for comprehensive cloud docs and
integration:

```
awslabs = MCPServerStdio(
    command="uvx",
    args=["awslabs.core-mcp-server@latest"],
    env={"FASTMCP_LOG_LEVEL": "ERROR"},
    tool_prefix="awslabs",
)
aws_docs = MCPServerStdio(
    command="uvx",
    args=["awslabs.aws-documentation-mcp-server@latest"],
    env={"FASTMCP_LOG_LEVEL": "ERROR", "AWS_DOCUMENTATION_PARTITION": "aws"},
    tool_prefix="aws_docs",
)

```

**The workflow change:** Now when I mentioned “Bedrock is timing out”
or “the model responses are getting truncated,” the agent could directly
access AWS documentation to help troubleshoot configuration issues. While
we've only scratched the surface with these two servers, this is the tip
of the iceberg—the [AWS Labs MCP
collection](https://awslabs.github.io/mcp/) includes servers for
CloudWatch metrics, Lambda debugging, IAM policy analysis, and much more.
Even with just documentation access, cloud debugging became more
conversational and contextual.

## Internet Search for Current Information

Sometimes you need information that's not in any documentation—recent
Stack Overflow discussions, GitHub issues, or the latest best practices.
We added general internet search:

```
internet_search = MCPServerStdio(command="uvx", args=["duckduckgo-mcp-server"])

```

**The workflow change:** When encountering obscure errors or needing to
understand recent changes in the ecosystem, the agent could search for
current discussions and solutions. This was particularly valuable for
debugging deployment issues or understanding breaking changes in
dependencies.

## Structured Problem Solving

One of the most valuable additions was the code reasoning MCP, which
helps the agent think through complex problems systematically:

```
code_reasoning = MCPServerStdio(
    command="npx",
    args=["-y", "@mettamatt/code-reasoning"],
    tool_prefix="code_reasoning",
)

```

**The workflow change:** Instead of jumping to solutions, the agent
would break down complex problems into logical steps, explore alternative
approaches, and explain its reasoning. This was invaluable for
architectural decisions and debugging complex issues. I could ask “Why is
this API call failing intermittently?” and get a structured analysis of
potential causes rather than just guesses.

## Optimising for Reasoning

As we added more sophisticated capabilities, we noticed that reasoning
and analysis tasks often took much longer than regular text
generation—especially when the output wasn't correctly formatted on the
first try. We adjusted our Bedrock configuration to be more patient:

```
bedrock_config = BotocoreConfig(
    read_timeout=300,
    connect_timeout=60,
    retries={"max_attempts": 3},
)
bedrock_client = boto3.client(
    "bedrock-runtime", region_name="eu-central-1", config=bedrock_config
)

```

**The workflow change:** The longer timeouts meant our agent could work
through complex problems without timing out. When analyzing large
codebases or reasoning through intricate architectural decisions, the
agent could take the time needed to provide thorough, well-reasoned
responses rather than rushing to incomplete solutions.

## Desktop Commander: Warning! With great power comes great responsibility!

At this point, our agent was already quite capable—it could reason
through problems, execute code, search for information, and access AWS
documentation. This MCP server transforms your agent from a helpful
assistant into something that can actually *do* things in your development
environment:

```
desktop_commander = MCPServerStdio(
    command="npx",
    args=["-y", "@wonderwhy-er/desktop-commander"],
    tool_prefix="desktop_commander",
)

```

Desktop Commander provides an incredibly comprehensive toolkit: file
system operations (read, write, search), terminal command execution with
process management, surgical code editing with `edit_block`, and even
interactive REPL sessions. It's built on top of the MCP Filesystem Server
but adds crucial capabilities like search-and-replace editing and
intelligent process control.

**The workflow change:** This is where everything came together. I
could now say “The authentication tests are failing, please fix the issue”
and the agent would:

* 1. Run the test suite to see the specific failures
* 2. Read the failing test files to understand what was expected
* 3. Examine the authentication module code
* 4. Search the codebase for related patterns
* 5. Look up the documentation for the relevant library
* 6. Make edits to fix the implementation
* 7. Re-run the tests to verify the fix
* 8. Search for similar patterns elsewhere that might need updating

All of this happened in a single conversation thread, with the agent
maintaining context throughout. It wasn't just generating code
suggestions—it was actively debugging, editing, and verifying fixes like a
pair programming partner.

The security model is thoughtful too, with configurable allowed
directories, blocked commands, and proper permission boundaries. You can
learn more about its extensive capabilities at the [Desktop Commander
documentation](https://github.com/wonderwhy-er/DesktopCommanderMCP).

## The Complete System

Here's our final agent configuration:

```
import asyncio


import subprocess
import boto3
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.providers.bedrock import BedrockProvider
from botocore.config import Config as BotocoreConfig

bedrock_config = BotocoreConfig(
    read_timeout=300,
    connect_timeout=60,
    retries={"max_attempts": 3},
)
bedrock_client = boto3.client(
    "bedrock-runtime", region_name="eu-central-1", config=bedrock_config
)
model = BedrockConverseModel(
    "eu.anthropic.claude-sonnet-4-20250514-v1:0",
    provider=BedrockProvider(bedrock_client=bedrock_client),
)
agent = Agent(
    model=model,
)


instructions = """
You are a specialised agent for maintaining and developing the XXXXXX codebase.

## Development Guidelines:

1. **Test Failures:**
   - When tests fail, fix the implementation first, not the tests
   - Tests represent expected behavior; implementation should conform to tests
   - Only modify tests if they clearly don't match specifications

2. **Code Changes:**
   - Make the smallest possible changes to fix issues
   - Focus on fixing the specific problem rather than rewriting large portions
   - Add unit tests for all new functionality before implementing it

3. **Best Practices:**
   - Keep functions small with a single responsibility
   - Implement proper error handling with appropriate exceptions
   - Be mindful of configuration dependencies in tests

Remember to examine test failure messages carefully to understand the root cause before making any changes.
"""


run_python = MCPServerStdio(
    "deno",
    args=[
        "run",
        "-N",
        "-R=node_modules",
        "-W=node_modules",
        "--node-modules-dir=auto",
        "jsr:@pydantic/mcp-run-python",
        "stdio",
    ],
)

internet_search = MCPServerStdio(command="uvx", args=["duckduckgo-mcp-server"])
code_reasoning = MCPServerStdio(
    command="npx",
    args=["-y", "@mettamatt/code-reasoning"],
    tool_prefix="code_reasoning",
)
desktop_commander = MCPServerStdio(
    command="npx",
    args=["-y", "@wonderwhy-er/desktop-commander"],
    tool_prefix="desktop_commander",
)
awslabs = MCPServerStdio(
    command="uvx",
    args=["awslabs.core-mcp-server@latest"],
    env={"FASTMCP_LOG_LEVEL": "ERROR"},
    tool_prefix="awslabs",
)
aws_docs = MCPServerStdio(
    command="uvx",
    args=["awslabs.aws-documentation-mcp-server@latest"],
    env={"FASTMCP_LOG_LEVEL": "ERROR", "AWS_DOCUMENTATION_PARTITION": "aws"},
    tool_prefix="aws_docs",
)
context7 = MCPServerStdio(
    command="npx", args=["-y", "@upstash/context7-mcp"], tool_prefix="context"
)

agent = Agent(
    instructions=instructions,
    model=model,
    mcp_servers=[
        run_python,
        internet_search,
        code_reasoning,
        context7,
        awslabs,
        aws_docs,
        desktop_commander,
    ],
)


@agent.tool_plain()
def run_unit_tests() -> str:
    """Run unit tests using uv."""
    result = subprocess.run(
        ["uv", "run", "pytest", "-xvs", "tests/"], capture_output=True, text=True
    )
    return result.stdout


async def main():
    async with agent.run_mcp_servers():
        await agent.to_cli()


if __name__ == "__main__":
    asyncio.run(main())

```

How it changes our workflow:

* Debugging becomes collaborative: you have an intelligent partner
  that can analyze error messages, suggest hypotheses, and help test
  solutions.
* Learning accelerates: when working with unfamiliar libraries or
  patterns, the agent can explain existing code, suggest improvements, and
  teach you why certain approaches work better.
* Context switching reduces: rather than jumping between
  documentation, Stack Overflow, AWS Console, and your IDE, you have a
  single interface that can access all these resources while maintaining
  context about your specific problem.
* Problem-solving becomes structured: rather than jumping to
  solutions, the agent can break down complex issues into logical steps,
  explore alternatives, and explain its reasoning. Like having a real life talking rubber duck!
* Code review improves: the agent can review your changes, spot
  potential issues, and suggest improvements before you commit—like having a
  senior developer looking over your shoulder.

## What We Learned About CLI Agents

Building our own agent revealed several insights about this emerging
paradigm:

* MCP is (almost) all you need: the magic isn't in any single
  capability, but in how they work together. The agent that can run tests,
  read files, search documentation, execute code, access AWS services, and
  reason through problems systematically becomes qualitatively different
  from one that can only do any single task.
* Current information is crucial: having access to real-time search
  and up-to-date documentation makes the agent much more reliable for
  real-world development work where training data might be outdated.
* Structured thinking matters: the code reasoning capability
  transforms the agent from a clever autocomplete into a thinking partner
  that can break down complex problems and explore alternative
  solutions.
* Context is king: commercial agents like Claude Code are impressive
  partly because they maintain context across all these different tools.
  Your agent needs to remember what it learned from the test run when it's
  making file changes.
* Specialisation matters: our agent works better for our specific
  codebase than general-purpose tools because it understands our patterns,
  conventions, and tool preferences. If it falls short in any area then we
  can go and make the required changes.

## The Road Ahead

The CLI agent paradigm is still evolving rapidly. Some areas we're
exploring:

* AWS-specific tooling: the AWS Labs MCP servers
  (https://awslabs.github.io/mcp/) provide incredible depth for cloud-native
  development—from CloudWatch metrics to Lambda debugging to IAM policy
  analysis.
* Workflow Enhancements: teaching the agent our common development
  workflows so it can handle routine tasks end-to-end. Connecting the agent
  to our project management tools so it can understand priorities and
  coordinate with team processes.
* Benchmarking: [Terminal Bench](https://www.tbench.ai)
  looks like a great dataset and leaderboard to test this toy agent against
  the big boys!

## Why This Matters

CLI coding agents represent a fundamental
shift from AI as a writing assistant to AI as a development partner.
Unlike Copilot's autocomplete or ChatGPT's Q&A, these agents can:

* Understand your entire project context
* Execute tasks across multiple tools
* Maintain state across complex workflows
* Learn from your specific codebase and patterns

Building one yourself—even a simple version—gives you insights into
where this technology is heading and how to make the most of commercial
tools when they arrive.

The future of software development isn't just about writing code
faster. It's about having an intelligent partner that understands your
goals, your constraints, and your codebase well enough to help you think
through problems and implement solutions collaboratively.

And the best way to understand that future? Build it yourself.

---