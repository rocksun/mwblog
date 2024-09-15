# 将 Cursor AI 融入开发工作流程

![Featued image for: Using Cursor AI as Part of Your Development Workflow](https://cdn.thenewstack.io/media/2024/09/a99dfe9f-alex-shuper-nacmb7m2rhi-unsplash-1024x576.jpg)

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
using System.Collections.Generic;

// 存储分数的字典
var scores = new Dictionary<string, List<int>>();

// 添加分数
scores.Add("游戏1", new List<int> { 10, 20, 30 });
scores.Add("游戏2", new List<int> { 5, 15, 25 });

// 打印分数
foreach (var game in scores)
{
    Console.WriteLine($"游戏 {game.Key}:");
    foreach (var score in game.Value)
    {
        Console.WriteLine(score);
    }
}
```

使用 System;
使用 System.Collections.Generic;

public struct User
{
    public string PlayerId;
    public string KnownAs;

    public User(string playerId, string knownAs)
    {
        PlayerId = playerId;
        KnownAs = knownAs;
    }
}

public class Score : IComparable<Score>
{
    public enum RegisteredGame { MatterBlatter, MasterBlaster, MinionPinion }

    public DateTime Entrydate;
    public int ScoreValue;
    public string Level = "";
    public RegisteredGame Game;
    public User Player;

    public int CompareTo(Score? other)
    {
        return (other.ScoreValue - ScoreValue);
    }

    public Score(RegisteredGame registeredGame, User player, int scoreValue, string level = "")
    {
        Game = registeredGame;
        Entrydate = DateTime.Now;
        ScoreValue = scoreValue;
        Level = level;
        Player = player;
    }
}

public class TopScore
{
    private List<Score> scores = new List<Score>();
    const short TABLESIZE = 10;

    public void AddScore(Score.RegisteredGame registeredGame, User user, int scorevalue, string level)
    {
        Score score = new(registeredGame, user, scorevalue, level);
        scores.Add(score);
    }

    public List<string> FormattedTopScoreTable(Score.RegisteredGame registeredGame)
    {
        List<string> toptable = new List<string>();

        //First sort List<Score>
        List<Score> justOnegame = scores.FindAll(sc => sc.Game == registeredGame);
        justOnegame.Sort();

        //Grab subset List<Score>
        List<Score> topItems = (justOnegame.Count < TABLESIZE) ? justOnegame : (List<Score>)justOnegame.Take(TABLESIZE);

        topItems.ForEach(sc => toptable.Add($"{sc.ScoreValue} {sc.Player.KnownAs} ({sc.Level})"));

        return toptable;
    }
}

User tim = new("12345", "Timbo");
User jim = new("45123", "Jimbo");
User kim = new("6534", "Kimbo");

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

// 这将产生：
// … 这对于高分榜来说顺序不对。
// 只需在 [主页](https://www.cursor.com/) 上点击“免费下载”按钮即可下载 Cursor 的 0.40.4 版本。就像你开始使用 VS Code 的现有项目一样，最好从命令行在根文件夹中运行 Cursor，这样它就可以在你的 shell 中获取上下文。为了帮助你，你可能需要打开命令面板并使用 `Shell Command: Install 'cursor'`
// 命令。

// 不幸的是，你实际上无法运行 .NET 程序并在 Cursor 中调试它，因为 Microsoft 阻止了它。如果 Cursor 是 VS Code 的插件，一切都会很好，但由于它是一个分支，Microsoft 无法识别它。我相信这很快就会解决，但现在这意味着你需要保持 VS Code 打开才能运行代码。

// 首先，总结一下。在打开聊天侧边栏（它正确地不会出现，除非你要求它）后，我要求 Claude 3.5 Sonnet “总结代码”。以下是重点：

// *1. 代码定义了一个简单的游戏计分系统，包含三个主要的类/结构体:*
// `User`
// : 代表一个玩家，包含 ID 和姓名。`Score`
// : 代表一个游戏分数，包含游戏类型、玩家、分数值和等级等详细信息。`TopScore`
// : 管理分数列表，并提供添加分数和生成格式化高分榜的方法。
// *2. Score 类包含一个枚举 RegisteredGame，用于不同的游戏类型，并实现 IComparable<Score> 用于排序。*
// *3. TopScore 类具有以下方法:*
// `AddScore`
// : 将新分数添加到列表中。`FormattedTopScoreTable`
// : 为特定游戏类型生成格式化的高分榜列表。
// *4. 主程序创建了一些示例用户和分数，将它们添加到 TopScore 实例中，然后打印“MatterBlatter”游戏的最高分数。*
// 虽然这其中大部分使用了变量名的上下文，但“简单的游戏计分系统”和“生成格式化的高分榜”这两个总结很有用。我喜欢它理解到它正在打印名为“MatterBlatter”的游戏的最高分数，从枚举中提取了这个名字。

// 现在，对于程序来说，要发现我的表格从最低分数到最高分数打印，而传统的最高分数表格将最高分数放在第一位，这相当困难。尽管如此，我还是要让它找出任何错误。

// 是的，它发现了错误。这相当令人印象深刻，因为它理解了高分榜的人类上下文：

// *是的，代码中有一个重大错误。主要问题在于 TopScore 类的 FormattedTopScoreTable 方法。以下是问题所在:*
// 1234567 |

```csharp
public List<string> FormattedTopScoreTable(Score.RegisteredGame registeredGame) { // ... existing code ... justOnegame.Sort(); //Grab subset List<Score> topItems = (justOnegame.Count < TABLESIZE)?justOnegame:(List<Score>)justOnegame.Take(TABLESIZE); // ... existing code ... } 

public void PurgeUser(User user) { 
    scores.RemoveAll(score => score.Player.PlayerId == user.PlayerId); 
} 

ts.PurgeUser(userToPurge); 

[Test] 
public void AddScore_AddsScoreCorrectly() { 
    topScore.AddScore(Score.RegisteredGame.MatterBlatter, user1, 1000, "Level 1"); 
    var scores = topScore.FormattedTopScoreTable(Score.RegisteredGame.MatterBlatter); 
    Assert.AreEqual(1, scores.Count); 
    Assert.AreEqual("1000 Alice (Level 1)", scores[0]); 
} 
```