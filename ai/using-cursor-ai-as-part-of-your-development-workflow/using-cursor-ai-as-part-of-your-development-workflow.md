
<!--
title: 将Cursor AI作为开发工作流程的一部分
cover: https://cdn.thenewstack.io/media/2024/09/a99dfe9f-alex-shuper-nacmb7m2rhi-unsplash.jpg
-->

我们知道 AI 在代码补全和创建测试方面很擅长。但它在正常的开发流程中表现如何呢？我们对 Cursor 进行了测试。

> 译自 [Using Cursor AI as Part of Your Development Workflow](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/)，作者 David Eastman。

自从我上次[回顾](https://thenewstack.io/testing-an-ai-first-code-editor-good-for-intermediate-devs/)以来，[Cursor AI](https://www.cursor.com/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) 已经变得[非常流行](https://thenewstack.io/5-ways-cursor-ai-sets-the-standard-for-ai-coding-assistance/)。普遍的报道是，在尝试了其他替代方案后，Cursor 产生了更好的结果。这可能是由于[Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) LLM 引擎，它通常被认为是[快速且准确的编码](https://www.tomsguide.com/ai/cursor-is-chatgpt-for-coding-now-anyone-can-make-an-app-in-minutes)工具。在我最初的评论中，我曾批评它直接依赖于[OpenAI](https://thenewstack.io/getting-started-with-openais-gpt-builder-and-how-it-uses-rag/) 及其 GPT 模型，因此这种改变显然是一个优势。而且你可以很容易地切换模型。

Cursor 是从 Visual Studio Code 的一个分支中开发出来的。我发现 VS Code 的设计有点挑剔，但它的灵活性是一个优势。正如我将在下面解释的那样，这确实给 Cursor 带来了一些问题。不幸的是，你实际上无法在 Cursor 中运行 .NET 程序并进行调试，因为 Microsoft 阻止了这种操作。

在过去的一年里，我们已经确定 AI 在将良好的模板引入你的编辑器方面非常出色，并且通常会提供良好的代码补全提示。我们已经看到了它在总结未知代码和创建测试方面的强大能力。我对通过聊天式界面从头开始开发代码不太感兴趣；大多数专业开发人员通常已经拥有正在进行的项目。

我将再次尝试它，作为正常开发流程的一部分。我必须小心演示，因为如果演示经常出现在网络上，它可能已经将其吸收了。但我的例子并不太模糊。

## 高分

我将用 C# 开发一个简单的排行榜。它所做的只是接收来自不同游戏的得分，然后按顺序显示给定游戏的得分。

- 我将编写代码（与 Cursor 分开）并要求 Cursor 总结它的功能。
- 我将要求它找出我将留下的一个错误。
- 我将添加删除特定分数的功能，并查看它如何提出建议。
- 然后我将要求它创建一些单元测试。

鉴于进展，我不认为这些任务中的任何一个会存在问题，但我更感兴趣的是事情是如何发生的。请注意，每个编辑器都会提供合理的自动完成建议，因此我不会关注这方面。

所以，我在 kosher VS Code 中编写了以下代码，使用[顶级语句](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/top-level-statements)，因此减少了样板代码：

```csharp
using System; 
using System.Collections.Generic; 
 
User tim = new ("12345","Timbo"); 
User jim = new ("45123","Jimbo"); 
User kim = new ("6534", "Kimbo"); 
 
TopScore ts = new TopScore(); 
ts.AddScore(Score.RegisteredGame.MatterBlatter, tim, 1000, "Level 3"); 
ts.AddScore(Score.RegisteredGame.MatterBlatter, tim, 1200, "Level 4"); 
ts.AddScore(Score.RegisteredGame.MasterBlaster, jim, 1000, "HellGate"); 
ts.AddScore(Score.RegisteredGame.MasterBlaster, tim, 1200, "FinalBoss"); 
ts.AddScore(Score.RegisteredGame.MatterBlatter, kim, 1000, "Level 3"); 
ts.AddScore(Score.RegisteredGame.MatterBlatter, kim, 3200, "Level 5"); 
 
List<string> topscores = ts.FormattedTopScoreTable(Score.RegisteredGame.MatterBlatter); 
Console.WriteLine($"TOP SCORES FOR {Score.RegisteredGame.MatterBlatter}");
topscores.ForEach(sc => Console.WriteLine(sc)); 
public struct User { 
  public string PlayerId; 
  public string KnownAs; 
  public User(string playerId, string knownAs) {
    PlayerId = playerId; 
    KnownAs = knownAs; 
  } 
} 
 
public class Score : IComparable<Score> { 
  public enum RegisteredGame { MatterBlatter, MasterBlaster, MinionPinion} 
  public DateTime Entrydate; 
  public int ScoreValue; 
  public string Level = ""; 
  public RegisteredGame Game; 
  public User Player; 
 
  public int CompareTo(Score? other) { 
    return (other.ScoreValue - ScoreValue); 
  } 
 
  public Score(RegisteredGame registeredGame, User player, int scoreValue, string level = "") { 
    Game = registeredGame; 
    Entrydate = DateTime.Now; 
    ScoreValue = scoreValue; 
    Level = level; 
    Player = player; 
  }  
} 
 
public class TopScore { 
  private List<Score> scores = new List<Score>(); 
  const short TABLESIZE = 10; 
  
  public void AddScore(Score.RegisteredGame registeredGame, User user, int scorevalue, string level) 
  { 
    Score score = new (registeredGame, user, scorevalue, level); 
    scores.Add(score); 
  } 
 
  public List<string> FormattedTopScoreTable(Score.RegisteredGame registeredGame) { 
    List<string> toptable = new List<string>();
    //First sort
    List<Score> justOnegame = scores.FindAll(sc => sc.Game == registeredGame); 
    justOnegame.Sort(); 
    //Grab subset 
    List<Score> topItems = (justOnegame.Count < TABLESIZE)?justOnegame:(List<Score>)justOnegame.Take(TABLESIZE); 
    topItems.ForEach(sc => toptable.Add($"{sc.ScoreValue} {sc.Player.KnownAs} ({sc.Level})")); 
    return toptable; 
  } 
}
```

这会输出：

![](https://cdn.thenewstack.io/media/2024/09/c6d9af35-screenshot-2024-09-13-at-14.09.37.png)

……高分榜上顺序错误。

只需在 [主页](https://www.cursor.com/) 上点击“Download for Free”按钮即可下载 Cursor 的 0.40.4 版本。就像你开始使用 VS Code 的现有项目一样，最好从命令行在根文件夹中运行 Cursor，这样它就可以在你的 shell 中获取上下文。为了帮助你，你可能需要打开命令面板并使用 `Shell Command: Install 'cursor'` 命令。

不幸的是，你实际上无法运行 .NET 程序并在 Cursor 中调试它，因为 Microsoft 阻止了它。如果 Cursor 是 VS Code 的插件，一切都会很好，但由于它是一个分支，Microsoft 无法识别它。我相信这很快就会解决，但现在这意味着你需要保持 VS Code 打开才能运行代码。

首先，总结一下。在打开聊天侧边栏（它正确地不会出现，除非你要求它）后，我要求 Claude 3.5 Sonnet “总结代码”。以下是重点：

1. 代码定义了一个简单的游戏计分系统，包含三个主要的类/结构体:

- `User`: 代表一个玩家，包含 ID 和姓名。
- `Score`: 代表一个游戏分数，包含游戏类型、玩家、分数值和等级等详细信息。
- `TopScore`: 管理分数列表，并提供添加分数和生成格式化高分榜的方法。

2. Score 类包含一个枚举 RegisteredGame，用于不同的游戏类型，并实现 IComparable<Score> 用于排序。*

3. TopScore 类具有以下方法:

- `AddScore`: 将新分数添加到列表中。
- `FormattedTopScoreTable`: 为特定游戏类型生成格式化的高分榜列表。

4. 主程序创建了一些示例用户和分数，将它们添加到 TopScore 实例中，然后打印“MatterBlatter”游戏的最高分数。

虽然这其中大部分使用了变量名的上下文，但“简单的游戏计分系统”和“生成格式化的高分榜”这两个总结很有用。我喜欢它理解到它正在打印名为“MatterBlatter”的游戏的最高分数，从枚举中提取了这个名字。

现在，对于程序来说，要发现我的表格从最低分数到最高分数打印，而传统的最高分数表格将最高分数放在第一位，这相当困难。尽管如此，我还是要让它找出任何错误。

是的，它发现了错误。这相当令人印象深刻，因为它理解了高分榜的人类上下文：

是的，代码中有一个重大错误。主要问题在于 TopScore 类的 FormattedTopScoreTable 方法。以下是问题所在:

```csharp
public List<string> FormattedTopScoreTable(Score.RegisteredGame registeredGame) { 
 // ... existing code ... 
 justOnegame.Sort(); 
 //Grab subset 
 List<Score> topItems = (justOnegame.Count < TABLESIZE)?justOnegame:(List<Score>)justOnegame.Take(TABLESIZE); 
 // ... existing code ... 
}
```

Bug 是：

- 对列表调用 Sort() 方法，但由于 CompareTo 在 Score 类中实现的方式，它按升序（从低到高）排序。
- 然后使用 Take(TABLESIZE) 方法选择顶部项目，但实际上它选择的是最低分，而不是最高分。

要修复此问题，您应该：

1. 反转 Score 类的 CompareTo 方法中的比较。
2. 在 FormattedTopScoreTable 方法中使用 OrderByDescending 而不是 Sort()。

改变比较在正常情况下起作用。建议反转比较是所有需要做的。同样，这是一个很好的点，因为代码具有功能性，但它理解的意思与我预想的不同。并且解释了这一点。在切换 compareTo 之后，情况就像它们应该的那样：

![](https://cdn.thenewstack.io/media/2024/09/d78945b7-screenshot-2024-09-13-at-14.30.16.png)

好吧，所以后来我发现 Kim 一直在作弊，所以我想从列表中移除她的所有分数。我们在最高分列表中将此称为“PurgeUser”。

我在聊天中询问，“我如何编写一个 PurgeUser 方法，以移除某个用户的所用分数？”

给出以下方法：

```csharp
public void PurgeUser(User user) { 
  scores.RemoveAll(score => score.Player.PlayerId == user.PlayerId); 
}
```

……以及如何使用它：

```csharp
ts.PurgeUser(userToPurge);
```

同时还指出一个要求：

```
“Note: This method assumes that PlayerId is unique for each user.”
```

这是一个显而易见的问题，但我喜欢它在其假设中提到了这一点。它了解到，我可能只是在不知道底层必需性的情况下使用了一个模式。

清除 Kim 运行良好。最后，我要求它提出单元测试——我以前使用 Codium 进行了此操作。所有这些都得到了全面的完成，但这里有一个示例：

```
 [Test]
 public void AddScore_AddsScoreCorrectly() {
    topScore.AddScore(Score.RegisteredGame.MatterBlatter, user1, 1000, "Level 1");
    var scores = topScore.FormattedTopScoreTable(Score.RegisteredGame.MatterBlatter);
    Assert.AreEqual(1, scores.Count);
    Assert.AreEqual("1000 Alice (Level 1)", scores[0]);
 }
```

它正确地扩展了字符串以使断言正确。

我注意到聊天面板的右上角有一个“应用”按钮，上面有测试：

![](https://cdn.thenewstack.io/media/2024/09/3b2fe0df-image.png)

它然后确认我想进行这个操作。然后它让你推送差异到你的 open code 文件。（实际上，在我的例子中这是无效的；测试应当放置在一个独立的文件中）

## 结论

我喜欢 Cursor 将聊天频道中提到的代码置于可通过 diff 合并到您的代码的单独面板中的方式。这感觉像做事情的正确方式。它还工作得非常快，并巧妙地进行自动完成建议。

总体而言，Cursor 走的是“工具”而不是“先知”的路线。这让我对 Cursor 参与您的工作流而不是试图取代它更有信心。

我认为它如何继续与 VS Code 协作将决定未来的成功。微软与 Cursor 合作以尝试给 AI 驱动的编码世界带来更多成功似乎很有可能。
