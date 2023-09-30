<!-- 
# IDE 中的幽灵：测试 Replit 的 AI 助手 Ghostwriter
https://cdn.thenewstack.io/media/2023/09/d1afb4cf-syarafina-yusof-oy7ucwu-rlq-unsplash-1024x683.jpg
 -->


编程平台 Replit 正以 AI 精神为指引继续前进，其 Ghostwriter 产品获得成功的机会远不止一点半点，David Eastman 表示。

译自 [Ghost in the IDE: Testing Replit’s AI Helper, Ghostwriter](https://thenewstack.io/ghost-in-the-ide-testing-replits-ai-helper-ghostwriter/) 。

最近，我一直在尝试各种为软件开发者提供提示、帮助、调试建议或(在某些情况下)完整代码片段的工具，这些工具都受到我们现在称为人工智能的支持。我特别喜欢在编辑行上给出提示，就像 Visual Studio 已经实现的那样，Copilot 做的更多。考虑到我喜欢在线沙箱，而且也在研究人工智能工具，似乎有一个明显的工具我应该研究一下。

[Replit](https://replit.com/) 是一个已经非常流行的在线 IDE，您的项目托管在"Repls"(REPL 或 read-eval-print loop 一词是其名称的由来)上。 Replit 是一个托管的解决方案，因此协作已经内置在其中。最近，该公司推出了其 LLM 服务 [Ghostwriter](https://replit.com/site/ghostwriter)。

与 OpenAI 的通用能力不同，经济学家注意到，Replit 更倾向于使用 LLM 模型来[专注于开发](https://www.economist.com/business/2023/09/18/could-openai-be-the-next-tech-giant)。他们使用了 Nvidia 高度投入的 [Databricks](https://www.databricks.com/) AI 平台。

我无需安装任何东西，就直接用 Google 账号创建了一个 Replit 账号。当然，我也可以使用 GitHub 作为身份验证。有趣的是，Replit 不仅询问您的预期用途(个人、协作等)，还询问您完成了多少开发工作。我在仪表板上首先看到的是一个悬赏任务墙，这超出了我的预期。这充分体现了 Replit 不仅是一个工具，更是一个社区 - 因此它内置了方便的内部市场。

但我来这里是为了尝试它的代码助手功能。我注意到我可以用 10 美元购买 1000 次使用 Ghostwriter 服务；也就是说，10 美元可以获得 1000 个使用**周期**。至少 Replit 没有直接公开它们的 AI 服务定价，所以后台如果有调整，他们可以灵活处理。而且使用虚拟货币比较透明 - 这与《堡垒之夜》的做法类似。众所周知，《堡垒之夜》会精心设定价格，所以你总会发现自己还差一点点游戏币就可以买到想要的皮肤。

![](https://cdn.thenewstack.io/media/2023/09/94f6f7ed-untitled-1024x570.png)

我的目标是在 Replit 的代码编辑页面上使用 Ghostwriter，所以我先买了 1000 个周期试试看。我假设公共代码页面是免费的，这与 Github 的模式相似。

在之前的文章中，我使用了一个[小的代码类来试用 Copilot](https://thenewstack.io/the-changing-role-of-human-developers-in-an-ai-and-llm-world/)。 Copilot 根据方法名(遵循常规命名约定)以及它对 C# FlagsAttribute 的理解来补全我的方法代码。 FlagsAttribute 只是表示枚举可以作为位字段使用：

```csharp
[Flags] public enum OccurrenceType {
   None = 0， 
   OccurrenceA = 1， 
   OccurrenceB = 2， 
   OccurrenceC = 4， 
   OccurrenceD = 8
} 
... 
private OccurrenceType occurrences { get; private set; } = OccurenceType.None
```

这种技术可以紧凑地存储事件信息；检查事件是否发生也很高效。所以我可以通过在一个变量中按位或 OccurrenceA 和 OccurrenceC 来表示它们发生：

```c
0000 (Nothing has happened)
 
OR
 
0001 (OccurrenceA happened)
 
OR
 
0100 (OccurrenceC happened)
 
-----
 
0101
```

通过适当的掩码，我们可以很快检测到 OccurrenceC 是否发生。这应该比使用列表更高效。

所以，我在 Replit 上新建了一个 C# 项目。在生成了 C# 模板项目后，小助手向我展示了基本操作，但是界面保持着正常的窗口化显示。另外，它邀请我试用 Ghostwriter：

![](https://cdn.thenewstack.io/media/2023/09/70a2bbc9-untitled-1-1024x535.png)

奇怪的是，Run 按钮起初似乎不工作......然后我注意到 CPU 使用率达到了 100%，但它最终还是打印出了“Hello World”。唉，看来我需要多花些游戏币啊(记住这是运行在 Replit 的基础设施上的)。

不幸的是，Ghostwriter 起初没有响应。可能是网络问题，也可能只是它的反应比较慢。它没有给出任何解释。我能从 CPU 的运算中得到反馈，但没有从 Ghostwriter 那里得到反馈。虽然如果将工作外包给另一个服务是不可避免会有延时的，但平台本身需要做更多状态监控和提示。

当聊天窗口终于有反应时，我准备开始了。但遗憾的是，Ghost 并没有在代码编辑过程中实时给出任何提示，而只是可以在编辑窗口生成完整代码。所以我让它帮忙生成 SetOccurrences 方法的代码。

第一次尝试没有成功。

![](https://cdn.thenewstack.io/media/2023/09/abde638e-untitled-2-1024x288.png)

它生成了:

```csharp
public void SetOccurrences(OccurrenceType occurrence)  
{
    this.occurrences = occurrence;
}
```

这是错误的，因为我的要求不够明确：这个方法名本应该叫“AddOccurrence”更恰当。

我取消了该提示，并再次试了试，这次改进了一下方法名:

![](https://cdn.thenewstack.io/media/2023/09/0097abdc-untitled-3-1024x273.png)

这样就正确了。它是通过按位或的方式添加了新的事件标志，而不是直接覆盖设置。不过我本该再精确一些的方法名。

 Checking whether an occurrence happened 这个方法我比较倒霉，好几次提示都是错的。最后，它给出了正确的按位运算实现：

![](https://cdn.thenewstack.io/media/2023/09/92fd45c1-untitled-4-1024x263.png)

这是使用按位标志的正确方式。它将存储的标志值与要检查的标志进行按位与，实现掩码的效果。任何非零结果都表示对应的事件发生了。同样，如果我在方法名上给我的幽灵助手一个更明确的提示，比如 HasOccurrence，它可能更快给出正确的实现。

我还试着看看它是否可以使用 .NET 7 中新增的 HasFlag 方法。尽管它没能给出这个建议(从项目设置看它没有使用 .NET 7，所以也不会有这个建议)，但它的提示更简洁了：

```csharp
public bool IsOccurrence(OccurrenceType occurrence)
{
  return (occurrences & occurrence) == occurrence; 
}  
```

这是一个更好的表达。在 main.cs 文件中添加了一些测试代码和控制台输出后，这个小项目可以正常工作了：

![](https://cdn.thenewstack.io/media/2023/09/f38d28b4-untitled-5-1024x573.png)

最后一个调试任务。为了让 FlagsAttribute 正确工作，枚举中的值必须是标准的二进制表示。如果我把 OccurrenceD 改成 5 会发生什么呢？Ghostwriter 似乎没有注意到这个问题，而且也没有直接的调试选项。但是，当我让它“解释代码”时，在错误存在的情况下它给出了非常准确的回应：

![](https://cdn.thenewstack.io/media/2023/09/6849f3b1-untitled-6-1024x733.png)

这完全正确，它甚至在分析代码时就发现了这个 bug - 几乎达到了人的水平。

总体来说，虽然 Ghostwriter 对我并没有非常主动的性能，但它的设置确实比 Visual Studio 和 Copilot 简单快速得多。我猜如果有更多的计算资源，网络条件良好，它的表现会更加正面和直接。与任何合作伙伴的磨合都需要时间，不管是人还是 AI。随着 Ghostwriter 在 Replit 基础设施上的不断优化，我相信它的表现会变得更加可靠，状态监控也会更友好。简而言之，Replit 在人工智能辅助编程的道路上正在稳步前进。它完全有望发展出一个成功的AI编程助手。
