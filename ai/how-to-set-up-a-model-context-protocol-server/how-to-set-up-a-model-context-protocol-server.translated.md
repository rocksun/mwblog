# 如何设置模型上下文协议服务器

![特色图片：如何设置模型上下文协议服务器](https://cdn.thenewstack.io/media/2025/05/e2a1e453-levi-meir-clancy-fey5508i7m0-unsplashb-1024x576.jpg)

在这篇文章中，我们将逐步介绍如何设置一个简单的[模型上下文协议 (MCP)](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)服务器。目前，MCP 是 LLM 模型和开发者工具之间进行通信的事实标准方式。您可以阅读我们更深入的 [MCP 开发者入门](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/)以了解更多详情，但这篇文章并不假定您具备这些知识。

我假设您已经安装了 [Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/)，尽管我只是将其用作位于终端中的 LLM，方便进行实验。无论如何，您仍然可以继续学习。

## 为什么选择 MCP？

其基本思想是保持 AI 和开发者工具之间的连接分离。在我下面解释的工具脚本中，它只是一个位于其自身本地服务器中的 Python 方法，我所做的只是返回一个秘密词。当然，这样做是使用服务器来控制上下文，因为 LLM 不知道您的本地世界中存在什么，除非您告诉它们。当然，我们希望确保我们控制这种能力。

鉴于 Anthropic 创建了 MCP，您可能会认为其他 LLM 供应商会尝试他们自己类似的想法。我们知道 Microsoft 喜欢 [扩展、拥抱和消灭](https://dev.to/meatboy/what-are-modern-examples-of-embrace-extend-and-extinguish-21j3) 的策略，但似乎其他供应商已经开始支持 MCP。

像大多数连接组织一样，MCP 可能会随着时间的推移被其他工具吸收。因此，如果它真正成功，您将不再意识到它的存在。

## 了解您的传输方式

在我们的 [MCP 开发者入门](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/)中，我们注意到两种协议之间的区别——[STDIO](https://mcp-framework.com/docs/Transports/stdio-transport)，这意味着标准输入/输出，以及 [SSE（现在是流传输）](https://mcp-framework.com/docs/Transports/http-stream-transport)，它更适合 Web。我们的工具只是一个简单的命令行界面 (CLI) 工具，因此它使用这种更简单的 STDIO 协议。通过“简单”，我们的意思是所有内容都在本地运行，没有额外的依赖项。

## 我们的 MCP 服务器和工具

首先，以熟悉的方式设置 Python 环境。我正在我的 MacBook 上执行此操作：

我们还需要安装 MCP 库：

我将脚本命名为 **server.py**。它结合了服务器和工具：

```python
#!/usr/bin/env python3
from mcp.server.fastmcp import FastMCP
import time
import signal
import sys

# Handle SIGINT (Ctrl+C) gracefully
def signal_handler(sig, frame):
    print("Shutting down server gracefully...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Create an MCP server with increased timeout
mcp = FastMCP(
    name="secretword",
    host="127.0.0.1",
    port=5000,
    # Add this to make the server more resilient
    timeout=30  # Increase timeout to 30 seconds
)

# Define our tool
@mcp.tool()
def secretword() -> str:
    """Retuen the secret word"""
    try:
        return "ABRACADABRA"
    except Exception as e:
        # Return 0 on any error
        return ""

if __name__ == "__main__":
    try:
        print("Starting MCP server 'secretword' on 127.0.0.1:5000")
        # Use this approach to keep the server running
        mcp.run()
    except Exception as e:
        print(f"Error: {e}")
        # Sleep before exiting to give time for error logs
        time.sleep(5)
```

其中很大一部分是异常处理，因此我们只对大约 15 行代码感兴趣。我们使用 FastMCP 来定义一个简单的服务器，该服务器在端口 5000 上运行。我们通过信号处理程序处理 Ctrl-C。除此之外，我们的工具 `secretword` 只是一个返回单词“ABRACADABRA”的方法。我从 [mberman84 的 gist](https://gist.github.com/mberman84/2faeddf57113826d7440bfadbe5ce6e5) 中改编了它。我希望您可以做一些更实质性的事情，但这证明了您也可以保持简单。
您可以通过直接运行它来测试它：

好的，停止它，让我们回到 Claude Code，告诉它我们出色的新 MCP 服务器。哦，等等，有一件事：让我们确保 Claude 可以直接运行服务器文件：

## 与 Claude 对话

安装 Claude Code 后，它应该在您的 shell 中可用。我们将不得不以某种方式告知 Claude 关于我的新服务器和我的 secret-word 工具的名称。

首先，让我们检查 Claude 是否完全识别 MCP：

好的，我们可以使用该建议来添加我们的 Python 脚本，因为我们知道它可以充当 MCP 服务器：

太酷了。

好的，让我们运行 Claude（使用调试），看看我们进展如何：

我们只有一个方法 secretword，它连接到此。

太棒了。但让我们实际上要求 Claude 使用我们强大的工具：
好了。这还不是很稳定，所以红色的调试代码可以帮助我们解决问题。此外，它们可能报告了对我们没有影响的问题。

## 结论

大多数高级开发人员会认识到，这仍然是协议周期的早期阶段，因此可能会有变化——我在上面提到，另一个协议 SSE 上个月已被弃用。所以现在掌握这些原则；将来可能会被库吸收。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)