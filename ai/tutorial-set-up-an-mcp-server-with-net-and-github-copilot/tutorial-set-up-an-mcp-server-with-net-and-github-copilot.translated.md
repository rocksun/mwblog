# 教程：使用 .NET 和 GitHub Copilot 设置 MCP 服务器

![教程特色图片：使用 .NET 和 GitHub Copilot 设置 MCP 服务器](https://cdn.thenewstack.io/media/2025/05/cc7db21a-chris-barbalis-j698hh61hpo-unsplashb-1024x576.jpg)

人们对 [模型上下文协议](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) 的兴趣激增，这是一个好兆头，表明人们正在尝试使用大型语言模型 (LLM) 构建不同的解决方案，但现在使用他们自己的系统。 MCP 是 LLM 和您的工具之间的中间人。

在完成一个简短的 [使用 Claude Code 的 Python 示例](https://thenewstack.io/how-to-set-up-a-model-context-protocol-server/) 之后，我想我会使用 Github Copilot 扩展一个 C# 版本——全部在 Visual Studio Code 中。 使用 IDE 的优势在于，我们有机会与其他 MCP 服务器集成，而无需离开 IDE。

Microsoft 自 4 月以来一直在关注 [MCP](https://devblogs.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)，我的帖子源于这篇 [Dev Blog](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/) 帖子。 虽然 Microsoft 通常不会快速工作，但他们现在很擅长展示他们的进展。 我假设您已安装 VS Code 并已登录 GitHub Copilot。

## 内部消息

由于 Microsoft 正在推出它，您可能已经拥有由“代理模式”驱动的 VS Code。 显然，这将是他们专注于代理解决方案的地方。 只需打开 Github Copilot 聊天，然后查看屏幕底部的“Ask”下拉列表：

如果您没有代理模式，您可以尝试（在命令面板中）搜索用户设置。

如果这不起作用，或者您不想弄乱您的 IDE，您可以获得 [Visual Studio Code Insiders](https://code.visualstudio.com/insiders/)。 这是托管最新版本（但可能不是最稳定的版本）的地方。 不过，请不要担心，因为它的设计目的是与您稳定的 VS Code 并排存在。

这是一个非常巧妙的举动，因为它允许 Microsoft 追随像 MCP 这样的新趋势，而不会让他们的团队陷入困境。 在我们开始之前，您应该做的另一件事是将“code-insiders”添加到您的命令路径，以便我们可以从命令 shell 中找到它。 只需在命令面板中开始键入“shell command”：

只是为了让您确信它们可以一起运行，我可以向您保证它们在 dock 中的外观不同：

Code-insiders 是绿色的那个！

现在，让我们获取 MCP 服务器所需的内容。

## 设置 MCP 服务器

从命令 shell 开始，让我们为 MCP 设置一个 .NET 控制台项目：

然后让我们进入项目并显式添加一些包。 我们也应该能够在 VS Code 中执行此操作，但我们可以在这里更具体：

现在让我们从命令行中的项目目录打开 VS Code。 这样做可以确保您正确继承上下文：

然后将模板 **Program.cs** 替换为用于设置 MCP 服务器的代码：

```csharp
using Microsoft.Extensions.DependencyInjection; 
using Microsoft.Extensions.Hosting; 
using ModelContextProtocol.Server; 
using System.ComponentModel; 

var builder = Host.CreateApplicationBuilder(args); 

builder.Logging.AddConsole(consoleLogOptions => { 
    // Configure all logs to go to stderr 
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace; 
}); 

builder.Services 
    .AddMcpServer() 
    .WithStdioServerTransport() 
    .WithToolsFromAssembly(); 

await builder.Build().RunAsync();
```

从原则上讲，这与 [几周前](https://thenewstack.io/how-to-set-up-a-model-context-protocol-server/) 的 Python 示例没有太大区别。 请注意在运行程序集中搜索工具的请求。 这是我们在 Python 中所做的自省等效项。 MCP 服务器有效地充当容器，并宣传其可用工具。
我将使用与 Python 示例中相同的简单 Secretword 工具。 它只是返回我们的秘密词：

```csharp
[McpServerToolType]
public static class SecretwordTool
{ 
    [McpServerTool, Description("Reveal the secret word.")] 
    public static string Secretword(string message) => "ABRACADABRA";
}
```

请注意，属性（方括号中的术语，提供有关其下方代码的元数据提示）将该方法标记为 MCP 工具。 同样，我们有 MCP 的诅咒：服务器和工具之间的轻微混淆。 这些属性名称并没有真正帮助。
现在，单击聊天框中的“选择工具”扳手图标：

您应该会看到一个工具列表。 我们现在要注册我们的新工具。

通过左下角的齿轮在设置选项卡中搜索 MCP 设置：

单击“在设置中编辑”链接，您将看到设置 JSON 文件：

MCP 部分可能为空，或者在本例中，具有默认时间工具。 仔细观察，您会看到“服务器”中方法名称正上方的“启动”箭头。
```
1234567891011121314 |
```json
{ "inputs": [], "servers": { "thenewstackMCP": { "type": "stdio", "command": "dotnet", "args": [ "run", "--project", "/Users/eastmad/thenewstack/thenewstackMCP/thenewstackMCP.csproj" ] } }}
```
|
我的绝对路径是我的MacBook的路径。我在我[上一篇关于MCP的文章](https://thenewstack.io/how-to-set-up-a-model-context-protocol-server/)中描述了STDIO。
保存它。现在点击应该出现在上方的“开始”按钮：

回到我们的聊天框，我们可以看到刷新按钮已经发现了我们的新工具。所以点击它，然后再次点击“选择工具”按钮，你会在工具列表的末尾看到这个：

是的，我们存在！耶。

## 向Copilot询问秘密词
现在我们可以直接通过Copilot聊天运行Secretword。也就是说，Copilot现在在语义上理解存在一个名为“secretword”的工具，它可以访问：

微软意识到，在这种间接级别下，用户可能会在没有意识到的情况下被说服运行代码。因此，系统会中断对话，以检查这是否是故意的。

那个蓝色的“继续”框设置了会话的权限，包括是否允许该工具运行。一旦我们这样做，我们就会从ChatGPT得到结果：

之后，我们可以继续将工具扩展到更有用的东西。

## 结论
如果我们将这个过程与Claude Code的Python示例进行比较，我认为我们还没有从Visual Code集成中获得很多优势——因为MCP显然是现在的附加组件。这显然是针对试图弄清楚MCP工作流程和影响的早期开发人员。

我可以预见到微软会及时将他们自己的解决方案强加给用户，但这就是我们现在的处境。每个人都在参加MCP派对。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)
```