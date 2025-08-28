<!--
title: 用 Pydantic-AI 打造你的专属 CLI 编码助手
cover: https://martinfowler.com/logo-sq.png
summary: 本文介绍了如何使用 Pydantic-AI 框架和模型上下文协议 (MCP) 构建 CLI 编码代理，重点介绍了 MCP 的重要性，以及如何通过添加测试、指令、沙盒 Python 执行、文档、互联网搜索等功能来增强代理的能力。
-->

本文介绍了如何使用 Pydantic-AI 框架和模型上下文协议 (MCP) 构建 CLI 编码代理，重点介绍了 MCP 的重要性，以及如何通过添加测试、指令、沙盒 Python 执行、文档、互联网搜索等功能来增强代理的能力。

> 译自：[Building your own CLI Coding Agent with Pydantic-AI](https://martinfowler.com/articles/build-own-coding-agent.html)
> 
> 作者：Ben O'Mahony

## CLI 编码代理的浪潮

如果您尝试过 Claude Code、Gemini Code、Open Code 或 Simon Willison 的 [LLM CLI](https://github.com/simonw/llm)，那么您已经体验到了一些与 ChatGPT 或 Github Copilot 根本不同的东西。它们不仅仅是聊天机器人或自动完成工具，它们是能够读取您的代码、运行您的测试、搜索文档并异步更改您的代码库的代理。

但它们是如何工作的呢？对我来说，理解任何工具如何工作的最好方法就是尝试自己构建它。所以这正是我们所做的，在本文中，我将带您了解我们如何使用 Pydantic-AI 框架和模型上下文协议 (MCP) 构建我们自己的 CLI 编码代理。您不仅会看到如何组装各个部分，还会看到为什么每个功能都很重要，以及它如何改变您使用代码的方式。

我们的实现利用了 AWS Bedrock，但使用 Pydantic-AI，您可以轻松地使用任何其他主流提供商，甚至完全本地的 LLM。

## 能买到时，为什么要自己构建？

在深入研究技术实现之前，让我们先来看看我们为什么选择构建自己的解决方案。

答案很快就变得清晰了，使用我们的自定义代理，商业工具令人印象深刻，但它们是为通用用例而构建的。我们的代理是完全为我们的内部环境以及我们特定项目的所有小怪癖而定制的。更重要的是，构建它使我们深入了解了这些系统的工作方式以及我们自己的 GenAI 平台和开发工具的质量。

把它想象成学习烹饪。您可以永远在餐馆吃饭，但了解口味如何结合以及技术如何工作，会让您以不同的方式欣赏食物，并让您创造出自己想要的东西。

## 我们的开发代理的架构

在高层次上，我们的编码助手由几个关键组件组成：

* 核心 AI 模型：通过 AWS Bedrock 访问的 Anthropic 的 Claude
* Pydantic-AI 框架：提供代理框架和许多有用的实用程序，使我们的代理立即变得更有用
* MCP 服务器：独立的进程，为代理提供专门的工具，MCP 是定义包含这些工具的服务器的通用标准。
* CLI 界面：用户与助手交互的方式

神奇之处在于模型上下文协议 (MCP)，它允许 AI 模型通过标准化接口使用各种工具。这种架构使我们的助手具有高度的可扩展性 - 我们可以通过实现额外的 MCP 服务器轻松地添加新功能，但我们正在超前。

## 从简单开始：基础

我们首先创建一个基本的项目结构并安装必要的依赖项：

```shell
uv init
uv add pydantic_ai
uv add boto3

```

我们的主要依赖项包括：

* `pydantic-ai`: 用于构建 AI 代理的框架
* `boto3`: 用于 AWS API 交互

我们选择 Anthropic 的 Claude Sonnet 4（通过 AWS Bedrock 访问）作为我们的基础模型，因为它具有强大的代码理解和生成能力。以下是我们在 `main.py` 中配置它的方式：

```py
import boto3
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.providers.bedrock import BedrockProvider

```

```py
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

```py
if __name__ == "__main__":
  agent.to_cli_sync()

```

在这个阶段，我们已经有了一个功能齐全的 CLI，带有一个聊天界面，我们可以像使用 GUI 聊天界面一样使用它，对于这么少的代码来说，这非常酷！但是我们绝对可以改进这一点。

## 第一个能力：测试！

为什么不在每次编码迭代后让代理来运行测试，而不是我们自己运行测试呢？这似乎很简单，对吧？

```py
import subprocess

```

```py
@agent.tool_plain()
def run_unit_tests() -> str:
    """Run unit tests using uv."""
    result = subprocess.run(
        ["uv", "run", "pytest", "-xvs", "tests/"], capture_output=True, text=True
    )
    return result.stdout

```

在这里，我们使用与在终端中运行的相同的 pytest 命令（我已经为本文缩短了我们的命令）。现在发生了一些神奇的事情。我可以说“X 无法工作”，代理会：

* 1. 运行测试套件
* 2. 确定哪些特定测试失败
* 3. 分析错误消息
* 4. 提出有针对性的修复建议。

**工作流程的改变：** 我们现在给我们的代理提供关于我们代码库中任何问题的超级相关的上下文，而不是盯着测试失败或将终端输出复制粘贴到 ChatGPT 中。

但是我们注意到我们的代理有时会通过建议更改测试而不是实际实现来“修复”失败的测试。这导致了我们的下一个补充。

## 增加智能：指令和意图

我们意识到我们需要教我们的代理更多关于我们的开发理念，并引导它远离不良行为。

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

**工作流程的改变：** 代理现在了解我们围绕测试驱动开发和最小化更改的价值观。它停止建议进行大型重构，而只需要进行小的修复（大多数情况下）。

现在，虽然我们可以继续从绝对零开始构建所有内容，并花几天时间调整我们的提示，但我们希望快速行动并使用其他人构建的一些工具 - 进入模型上下文协议 (MCP)。

## MCP 革命：可插拔能力

在这里，我们的代理从一个有用的助手转变为接近商业 CLI 代理的东西。模型上下文协议 (MCP) 允许我们通过运行专门的服务器来添加复杂的功能。

> MCP 是一种开放协议，它标准化了应用程序如何向 LLM 提供上下文。将 MCP 视为 AI 应用程序的 USB-C 端口。正如 USB-C 提供了一种标准化方式将您的设备连接到各种外围设备和配件一样，MCP 提供了一种标准化方式将 AI 模型连接到不同的数据源和工具。
>
> -- [MCP 简介](https://modelcontextprotocol.io/introduction)

我们可以将这些服务器作为本地进程运行，因此没有数据共享，我们在其中与 STDIN/STDOUT 交互以保持简单和本地。 ([有关工具和 MCP 的更多详细信息](/articles/function-call-LLM.html))

## 沙盒 Python 执行

使用大型语言模型进行计算或执行它们创建的任意代码既无效又可能非常危险！为了使我们的代理更准确和安全，我们首先添加的 MCP 是 Pydantic Al 的默认服务器，用于沙盒 Python 代码执行：

```py
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

```py
agent = Agent(
    ...
    mcp_servers=[
        run_python
    ],
)

```

这为我们的代理提供了一个沙箱，它可以在其中测试想法、原型解决方案并验证其自己的建议。

注意：这与运行我们需要本地环境的测试非常不同，旨在用于使计算更加健壮。这是因为编写代码以输出一个数字，然后执行该代码比仅生成计算中的下一个标记更可靠、更易于理解、可扩展和可重复。我们从前沿实验室（包括他们泄露的说明）中看到，这是一种更好的方法。

**工作流程的改变：** 进行计算，即使是更复杂的计算，也变得更加可靠。这对于许多事情都很有用，例如日期、总和、计数等。它还允许简单 python 代码的快速迭代周期。

## 最新的库文档

LLM 主要在历史数据上进行批量训练，这给出了一个固定的截止日期，而语言和依赖项继续变化和改进，因此我们添加了 [Context7](https://context7.com/)，用于以 LLM 可消耗的格式访问最新的 python 库文档：

```
context7 = MCPServerStdio(
    command="npx", args=["-y", "@upstash/context7-mcp"], tool_prefix="context"
)

```

**工作流程的改变：** 当使用较新的库或尝试使用高级功能时，代理可以查找当前的文档，而不是依赖可能过时的训练数据。这使其在实际开发工作中更加可靠。

## AWS MCP

由于此特定代理是考虑到 AWS 平台而构建的，因此我们添加了 AWS Labs MCP 服务器，以实现全面的云文档和集成：

```py
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

**工作流程的改变：** 现在，当我提到“Bedrock 超时”或“模型响应被截断”时，代理可以直接访问 AWS 文档来帮助解决配置问题。虽然我们只使用了这两个服务器的表面，但这只是冰山一角 - [AWS Labs MCP
集合](https://awslabs.github.io/mcp/) 包括用于 CloudWatch 指标、Lambda 调试、IAM 策略分析等的服务器。即使只有文档访问权限，云调试也变得更加对话和情境化。

## 互联网搜索以获取当前信息

有时您需要的信息不在任何文档中 - 最近的 Stack Overflow 讨论、GitHub 问题或最新的最佳实践。我们添加了通用互联网搜索：

```py
internet_search = MCPServerStdio(command="uvx", args=["duckduckgo-mcp-server"])

```

**工作流程的改变：** 当遇到晦涩的错误或需要了解生态系统中最近的变化时，代理可以搜索当前的讨论和解决方案。这对于调试部署问题或了解依赖项中的重大更改特别有价值。

## 结构化问题解决

最有价值的补充之一是代码推理 MCP，它可以帮助代理系统地思考复杂的问题：

```py
code_reasoning = MCPServerStdio(
    command="npx",
    args=["-y", "@mettamatt/code-reasoning"],
    tool_prefix="code_reasoning",
)

```

**工作流程的改变：** 代理不会直接跳到解决方案，而是将复杂的问题分解为逻辑步骤，探索替代方法，并解释其推理。这对于架构决策和调试复杂问题非常宝贵。我可以问“为什么此 API 调用间歇性失败？”，并获得对潜在原因的结构化分析，而不仅仅是猜测。

## 优化推理

随着我们添加更多复杂的功能，我们注意到推理和分析任务通常比常规文本生成花费的时间更长 - 尤其是在第一次尝试时输出格式不正确的情况下。我们调整了 Bedrock 配置以使其更耐心：

```py
bedrock_config = BotocoreConfig(
    read_timeout=300,
    connect_timeout=60,
    retries={"max_attempts": 3},
)
bedrock_client = boto3.client(
    "bedrock-runtime", region_name="eu-central-1", config=bedrock_config
)

```

**工作流程的改变：** 更长的超时时间意味着我们的代理可以处理复杂的问题而不会超时。当分析大型代码库或推理复杂的架构决策时，代理可以花费所需的时间来提供彻底、合理的响应，而不是急于提供不完整的解决方案。

## 桌面指挥官：警告！能力越大，责任越大！

此时，我们的代理已经非常强大 - 它可以推理问题、执行代码、搜索信息以及访问 AWS 文档。此 MCP 服务器将您的代理从有用的助手转变为实际上可以在您的开发环境中*做*事情的东西：

```
desktop_commander = MCPServerStdio(
    command="npx",
    args=["-y", "@wonderwhy-er/desktop-commander"],
    tool_prefix="desktop_commander",
)

```

桌面指挥官提供了一个非常全面的工具包：文件系统操作（读取、写入、搜索）、带进程管理的终端命令执行、使用 `edit_block` 进行的手术代码编辑，甚至交互式 REPL 会话。它构建在 MCP 文件系统服务器之上，但增加了关键功能，如搜索和替换编辑以及智能进程控制。

**工作流程的改变：** 这就是一切结合在一起的地方。我现在可以说“身份验证测试失败，请修复问题”，代理将：

* 1. 运行测试套件以查看特定失败
* 2. 读取失败的测试文件以了解预期内容
* 3. 检查身份验证模块代码
* 4. 在代码库中搜索相关的模式
* 5. 查找相关库的文档
* 6. 进行编辑以修复实现
* 7. 重新运行测试以验证修复
* 8. 搜索其他地方可能需要更新的类似模式

所有这些都发生在单个对话线程中，代理在整个过程中保持上下文。它不仅仅是生成代码建议，它还在积极地调试、编辑和验证修复，就像一个结对编程伙伴。

安全模型也经过深思熟虑，具有可配置的允许目录、阻止命令和适当的权限边界。您可以在 [桌面指挥官文档](https://github.com/wonderwhy-er/DesktopCommanderMCP) 中了解有关其广泛功能的更多信息。

## 完整的系统

这是我们的最终代理配置：

```py
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

它如何改变我们的工作流程：

* 调试变得协作：您有一个智能合作伙伴，可以分析错误消息、提出假设并帮助测试解决方案。
* 学习加速：当使用不熟悉的库或模式时，代理可以解释现有代码、提出改进建议，并教您为什么某些方法效果更好。
* 上下文切换减少：您无需在文档、Stack Overflow、AWS 控制台和您的 IDE 之间跳转，而只需使用一个可以访问所有这些资源的界面，同时保持有关您的特定问题的上下文。
* 问题解决变得结构化：代理可以打破复杂的问题分解为逻辑步骤，探索替代方案，并解释其推理，而不是直接跳到解决方案。就像拥有一个真正的会说话的橡皮鸭！
* 代码审查得到改进：代理可以审查您的更改，发现潜在问题，并在您提交之前提出改进建议 - 就像有一位高级开发人员在您身边一样。

## 我们从 CLI 代理中学到了什么

构建我们自己的代理揭示了关于这种新兴范例的几个见解：

* MCP 几乎是您所需要的：神奇之处不在于任何单一能力，而在于它们如何协同工作。能够运行测试、读取文件、搜索文档、执行代码、访问 AWS 服务以及系统地推理问题的代理在质量上与只能执行任何单一任务的代理不同。
* 当前信息至关重要：访问实时搜索和最新的文档使代理对于实际开发工作更加可靠，在实际开发工作中，训练数据可能已过时。
* 结构化思维很重要：代码推理能力将代理从一个聪明的自动完成工具转变为一个可以分解复杂问题并探索替代解决方案的思考伙伴。
* 上下文至关重要：像 Claude Code 这样的商业代理之所以令人印象深刻，部分原因是它们在所有这些不同的工具中都保持了上下文。您的代理需要记住它从测试运行中学到的东西，才能进行文件更改。
* 专业化很重要：我们的代理对于我们的特定代码库比通用工具效果更好，因为它了解我们的模式、约定和工具偏好。如果它在任何领域中不足，那么我们可以去进行所需的更改。

## 前进的道路

CLI 代理范例仍在迅速发展。我们正在探索的一些领域：

* AWS 特定的工具：AWS Labs MCP 服务器
  (https://awslabs.github.io/mcp/) 为云原生开发提供了令人难以置信的深度 - 从 CloudWatch 指标到 Lambda 调试再到 IAM 策略分析。
* 工作流程增强：教代理我们常见的开发工作流程，以便它可以端到端地处理例行任务。将代理连接到我们的项目管理工具，以便它可以了解优先级并与团队流程协调。
* 基准测试：[Terminal Bench](https://www.tbench.ai) 看起来像一个很棒的数据集和排行榜，可以针对大型公司测试这个玩具代理！

## 为什么这很重要

CLI 编码代理代表着从 AI 作为写作助手到 AI 作为开发合作伙伴的根本转变。与 Copilot 的自动完成或 ChatGPT 的问答不同，这些代理可以：

* 了解您的整个项目上下文
* 跨多个工具执行任务
* 在复杂的工作流程中保持状态
* 从您的特定代码库和模式中学习

自己构建一个 - 即使是一个简单的版本 - 可以让您深入了解这项技术的未来发展方向，以及如何在商业工具到来时充分利用它们。

软件开发的未来不仅仅是更快地编写代码。而是拥有一个智能合作伙伴，它足够了解您的目标、您的约束和您的代码库，以帮助您思考问题并协作实施解决方案。

而了解未来的最佳方式？自己构建它。