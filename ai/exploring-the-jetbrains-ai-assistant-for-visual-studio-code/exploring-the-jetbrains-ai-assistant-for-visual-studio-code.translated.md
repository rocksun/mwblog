# 探索适用于 Visual Studio Code 的 JetBrains AI 助手

![适用于：探索适用于 Visual Studio Code 的 JetBrains AI 助手的特色图片](https://cdn.thenewstack.io/media/2025/05/14b2239b-alex-shuper-8-zt2ne-vnk-unsplashb-1024x576.jpg)

前段时间，我研究了 [JetBrains AI 助手在其自身的 IDE 产品中的应用](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/)，但现在我们可以通过扩展在 [Visual Studio Code 中使用 JetBrains AI 助手](https://www.jetbrains.com/aia-vscode/)。正如我之前提到的，我在 VS Code 中切换大型语言模型 (LLM) 代码扩展时遇到了一些困难，因此在安装此公共预览版时我会格外小心。

JetBrains 在 IntelliJ 上的工作备受推崇，所以我不太确定该公司为什么要为其 AI 助手编写 VS Code 扩展——该助手相对较晚才加入 LLM 阵营。给出的原因是“为了覆盖更广泛的开发者社区，并展示我们对与 IDE 无关的 AI 辅助的承诺”，但无论如何，我很高兴对其进行测试。

在这篇文章中，我将详细介绍这款 AI 助手——但如果您只想即插即用，那么只需阅读 JetBrains 与标准助手行为不同的部分即可。现在，我希望大多数开发人员都熟悉在编码时使用 LLM。

首先，我想停止 VS Code 中的 Copilot，它是默认情况下存在于 VS Code 中的 LLM。安装 JetBrains AI 助手后，您可以看到它们的图标都位于底部功能区上。

即使我尚未登录 JetBrains，它们似乎都已“准备就绪”。但是，我可以从扩展视图中禁用 Copilot。Copilot 图标仍然存在，但上面有一个叉号。

现在您可以登录您的 JetBrains 帐户（我还有上次审查后剩余的许可证）。您将看到对其 LLM 服务的巧妙解释：

底部附近是小的聊天和上下文框：

与 Github Copilot 类似，下拉菜单具有聊天、多文件编辑和代理选项。每一个都会消耗更多的新黄金：令牌。请注意，**GPT-4o** 是默认模型。模型下拉列表包括其他常见的选项。

在这篇文章中，我将重点介绍 LLM 可以在 IDE 中执行的操作（即，不离开界面进行聊天）。首先是代码完成：

这仍然是 LLM 的主要功能。您必须训练您的肌肉记忆来记住 Tab 键，否则如果您在建议上键入内容，建议将消失。这是代码完成的默认行为。由于我在之前的文章中使用 [模型上下文协议 (MCP)](https://thenewstack.io/tutorial-set-up-an-mcp-server-with-net-and-github-copilot/) 服务器代码，因此我仍然在打开的选项卡中保留该代码。作为建议的一个示例，在现有代码下方，我键入了一个类签名和字母“He”，并且在光标之后完成了其余的操作：

这是一个典型的“文本处理”。它所做的是有效地为最小的 MCP 服务器工具创建一个模板——这是它从文件中读取的上下文。（在某些时候，AI 抛出了几个它没有解释的内部错误，但这没有外部影响。请记住，这只是一个公共预览版。）

然后我们有代码解释，这是快速掌握不熟悉的代码库的方法：

同样，这是任何 LLM 代码助手的标准。两个菜单深度对于此选项来说是合适的，因为它对于代码片段来说并不经常需要：

应用于我们上次的现有 MCP 工具，它会生成大量详细解释所有内容的文字。但重要的部分是摘要：

*“因此，总而言之，这个类将用作 MCP 服务器中的一个工具，当它被调用时，它将始终返回单词‘ABRACADABRA’。”*

这非常有用，因为它既理解代码的上下文（在本例中，它是用于 MCP 的），也理解它所做的事情（只是返回静态字符串）。这才是真正的价值所在；我建议应该优先返回这个，而不是详细的内容，这些内容主要是多余的。

在从“解释这个”创建的文字之后，可以轻松创建文档也就不足为奇了。这是作为对我们原始片段的正确放置的注释来完成的：

```csharp
/// <summary> 
/// Represents a tool within the McpServer framework used for secret word handling. 
/// </summary> 
/// <remarks> 
/// This tool provides a method to reveal a predefined secret word upon invocation. 
/// It can be extended or used as part of McpServer tool functionalities. 
/// </remarks> 
[McpServerToolType] 
public static class SecretwordTool { 
    [McpServerTool, Description("Reveal the secret word.")] 
    public static string Secretword(string message) => "ABRACADABRA"; 
}
```
这相当简单，但我喜欢它能够理解注释与原始解释之间的区别——它不会假装“ABRACADBRA”这个词是设计的一部分。再说，语义解释正是 LLM 所擅长的。

下一个操作不太直接：

虽然我没有使用 VS Code 来管理源代码控制，但我所有的示例文件都在一个 git 仓库中。

我打开了“源代码控制”选项卡，以确认我最近没有提交任何内容。但是，JetBrains 的螺旋图标确实存在：

不幸的是，我没有任何暂存文件，并且它创建的消息（关于错误处理）毫无意义，因为我不知道它指的是什么。在 git 中，代码必须先暂存（通常使用 **add** 命令），然后才能提交。JetBrains 需要在这方面投入更多精力。

这样就只剩下聊天式的 LLM 了，它不需要 VS Code 界面，因此，没有必要对此进行检查。如果您根本不需要打开 IDE，我建议使用类似 [Claude Code](https://thenewstack.io/zh-cn/claude-code-and-the-art-of-test-driven-development/) 的工具。即使是多文件编辑，也并不能真正从 IDE 的存在中受益。

## 结论

正如我所指出的，我不太清楚 JetBrains 通过这个扩展实现了什么，除了让用户通过其后端服务花费 token。这不是 JetBrians IDE，他们也没有声称要制造 LLM。也许“与 IDE 无关的 AI 助手”市场不仅仅是营销。

然而，JetBrains 并没有真正创造出引人注目的 UI 体验。也就是说，我认为许多 .NET 开发人员会很乐意信任 JetBrains 品牌，也许这个立足点将在未来带来一些更有趣的产品。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可观看我们所有的播客、访谈、演示等。
](https://youtube.com/zh-cn/thenewstack?sub_confirmation=1)