
<!--
title: Zed AI简介及其与Cursor AI的比较
cover: https://cdn.thenewstack.io/media/2024/09/368e729c-getty-images-qob-b3gfcxs-unsplash.jpg
-->

与 Cursor 类似，Zed AI 将大型语言模型集成到一个令人印象深刻的代码编辑器中。我们试用了 Zed AI 并将其与 Cursor 进行了比较。

> 译自 [An Introduction to Zed AI and How It Compares to Cursor AI](https://thenewstack.io/an-introduction-to-zed-ai-and-how-it-compares-to-cursor-ai/)，作者 David Eastman。

在我上一篇文章中重新审视了 [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) 之后，我认为现在也是时候重新审视 [Zed](https://zed.dev/) 了，它一直在忙于 [将 AI 集成](https://zed.dev/blog/zed-ai) 到其多人代码编辑器中。Zed AI 在“初始发布期间免费”，但我们应该很快就会看到收费——这样的功能可能是 Zed（一家由风险投资支持的初创公司）未来开始盈利的方式。

Zed [是一个从头开始编写的代码编辑器](https://thenewstack.io/zed-a-new-multiplayer-code-editor-from-the-creators-of-atom/)——它用 Rust 编写，并有效地利用了多核处理器和 GPU。它的创建者有经验，他们还创建了 Atom 和 Tree-sitter。因此，Zed 有机会完全控制 AI 的实现方式——与 Cursor 不同，Cursor 分叉了 Visual Studio Code。Cursor 在代码窗口和 AI 支持之间实现了清晰的分离，因此这将是一个有趣的比较。

默认情况下，Zed 还使用 Anthropic 的 [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)。但是，也可以插入不同的 LLM 提供商，或者使用 [本地选项](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/)。

我只使用 Zed 进行编辑；我会保持 VS Code 打开以进行构建。Zed 尚未在 Windows 上实现，也没有任何确切的计划这样做，这可能会影响你对该选项的看法。我将使用我的可靠的 MacBook。

我将继续使用我 [上一篇文章](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) 中的高分示例。

- 我们将把添加的分数转换为单独的 JSON 文件；
- 我们将加载 JSON 文件；
- 我们将添加一个排名。

这是我们在清除作弊用户 Kim 之后到达的地方：

```csharp
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
 
ts.PurgeUser(kim); 
 
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
  public int ScoreValue; public string Level = ""; 
  public RegisteredGame Game; 
  public User Player; 
  
  public int CompareTo(Sco re? other) { 
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
 
  public void AddScore(Score.RegisteredGame registeredGame, User user, int scorevalue, string level) { 
    Score score = new (registeredGame, user, scorevalue, level); 
    scores.Add(score); 
  } 
 
  public void PurgeUser(User user) { 
    scores.RemoveAll(score => score.Player.PlayerId == user.PlayerId); 
  } 
 
  public List<string> FormattedTopScoreTable(Score.RegisteredGame registeredGame) { 
    List<string> toptable = new List<string>(); //First sort it 
    List<Score> justOnegame = scores.FindAll(sc => sc.Game == registeredGame); 
    justOnegame.Sort(); //Grab subset 
    List<Score> topItems = (justOnegame.Count < TABLESIZE)?justOnegame:(List<Score>)justOnegame.Take(TABLESIZE); 
    topItems.ForEach(sc => toptable.Add($"{sc.ScoreValue} {sc.Player.KnownAs} ({sc.Level})")); 
    return toptable; 
  } 
}
```

## 助手面板和内联转换

当 Zed 更新时，没有线索表明 AI 是否开启，但当我尝试打开助手面板（相当于聊天式界面区域）时，我们得到了以下结果：

![](https://cdn.thenewstack.io/media/2024/09/2a3317fc-image.png)

然后，您会看到一个包含各种模型的清单，您可以选择连接其中一个。我选择连接 Anthropic，这意味着我需要获取一个密钥（注意：这在 Cursor 中已经为您完成）。我使用 [评估计划](https://console.anthropic.com/) 创建了密钥，但我似乎没有选择条款和条件。目前，这有点混乱。

当助手最终准备好后，一切运行良好。我的第一个任务是从文件中读取分数。

![](https://cdn.thenewstack.io/media/2024/09/918ce70a-image-1-1024x516.png)

结果是正确的，然后可以根据我的要求将其放置在单独的文件中：

```json
[ 
  { 
    "game": "MatterBlatter", 
    "player": "tim", 
    "score": 1000, 
    "level": "Level 3" 
  }, { 
    "game": "MatterBlatter", 
    "player": "tim", 
    "score": 1200, 
    "level": "Level 4" 
  }, { 
    "game": "MasterBlaster", 
    "player": "jim", 
    "score": 1000, 
    "level": "HellGate" 
  }, { 
    "game": "MasterBlaster", 
    "player": "tim", 
    "score": 1200, 
    "level": "FinalBoss" 
  }, { 
   "game": "MatterBlatter", 
   "player": "kim", 
   "score": 1000, 
   "level": "Level 3" 
  }, { 
    "game": "MatterBlatter", 
    "player": "kim", 
    "score": 3200, 
    "level": 
    "Level 5" 
  } 
]
```

这很好，因为它理解我想将枚举转换为字符串。（不幸的是，它还使用了局部变量名而不是 `PlayerId`，这将在以后造成问题。）

我的下一步将是请求读取 `scores.json` 文件的适当代码，并将其转换为 `TopScore` 对象的参数。我使用新的“斜杠”命令 `/file` 将我刚刚使用 JSON 创建的新分数文件添加到助手以供参考。可以将其视为 [额外的 RAG](https://thenewstack.io/enhancing-ai-coding-assistants-with-context-using-rag-and-sem-rag/) 之类的补充：

![](https://cdn.thenewstack.io/media/2024/09/a856ce06-image-2.png)

然后，我就可以构建提示：

![](https://cdn.thenewstack.io/media/2024/09/66c26834-image-3.png)

虽然这不是我通常进行的大量代码创建查询，但我们确实进行了很多 [使用 Llama 3 进行 JSON 持久化](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/)。当然，Claude 对此毫无问题。

它以旧式的 Main 样式编写了代码，我们将尝试使用内联转换在整个代码中添加更改。助手面板和代码本身的内联转换之间的相互作用是 Zed AI 将事物分开的方式。

因此，在这里，我要求内联助手将 `ScoreEntry` 类添加到 LLM 在右侧助手创建的主代码中：

![](https://cdn.thenewstack.io/media/2024/09/ccc32509-image-4.png)

它完成了：

![](https://cdn.thenewstack.io/media/2024/09/51a1206e-image-5-1024x520.png)

请注意，我可以使用勾号接受代码添加。

有趣的是，建议的 JSON 加载代码转换与助手中的原始建议不同：

![](https://cdn.thenewstack.io/media/2024/09/c3bf476c-image-6-1024x695.png)

更正产生了一个有趣的错误。它试图手动将玩家姓名与给定的用户进行匹配，而不是向 User 添加注册和按姓名搜索功能。但错误确实提醒了我自己没有在 JSON 中使用 PlayerId 的错误。

作为一名开发人员，即使有这些 LLM 错误，这仍然代表着效率的提高。这可能会让过度信任 LLM 解决方案的初学者陷入困境，但如果您只是将其视为一个可靠的起点，一切都会好起来的。我相信如果我想以这种方式清理代码，Claude 和我还可以进行进一步的对话。

在更正了 Users 代码后，我们回到了这样的结果（来自 VS Code）：

![](https://cdn.thenewstack.io/media/2024/09/2f14ee65-image-7.png)

最后，我们想添加一个排名以提高可读性。让我们看看是否可以要求这样做。

![](https://cdn.thenewstack.io/media/2024/09/1a0ce82c-image-8.png)

折叠的文本是整个文件，并使用 `/tab` 添加，它只是将整个打开的文件作为上下文添加。

我很难要求内联助手用新代码替换冗余代码。它不愿意删除旧代码——这可能是一件好事！

在为 Jim 添加了一些额外的分数以增加趣味性后，我们得到了一个漂亮的排名表：

![](https://cdn.thenewstack.io/media/2024/09/1a3831c2-image-9.png)

同样，Claude 立即理解了在这个高分表上下文中“排名”的含义，并创建了正确的代码。最终代码如下：

```csharp
using System.Text.Json; 
 
User tim = new ("12345","Timbo"); 
User jim = new ("45123","Jimbo"); 
User kim = new ("6534", "Kimbo"); 
 
TopScore ts = new TopScore(); 
 
string jsonString = File.ReadAllText("scores.json"); 
 
List<ScoreEntry> scoreEntries = JsonSerializer.Deserialize<List<ScoreEntry>>(jsonString); 
 
foreach (var entry in scoreEntries) { 
  ts.AddScore( 
    Enum.Parse<Score.RegisteredGame>(entry.game), 
    User.FindByPlayerId(entry.player), 
    entry.score, 
    entry.level 
  ); 
} 
 
ts.PurgeUser(kim); 
 
List<string> topscores = ts.FormattedTopScoreTable(Score.RegisteredGame.MatterBlatter); 
Console.WriteLine($"TOP SCORES FOR {Score.RegisteredGame.MatterBlatter}"); 
topscores.ForEach(sc => Console.WriteLine(sc)); 
 
public struct User { 
  public string PlayerId; 
  public string KnownAs; 
  private static List<User> registeredUsers = new (); 
  public User(string playerId, string knownAs) { 
    PlayerId = playerId; 
    KnownAs = knownAs; 
    registeredUsers.Add(this); 
  } 
  public static User FindByPlayerId(string id) { 
   return registeredUsers.FirstOrDefault(u => u.PlayerId == id); 
  } 
} 
 
public class ScoreEntry { 
  public string game { get; set; } 
  public string player { get; set; } 
  public int score { get; set; } 
  public string level { get; set; } 
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
 
  public Score(RegisteredGame registeredGame, User player, int scoreValue, string level = "") 
  { 
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
 
  public void AddScore(Score.RegisteredGame registeredGame, User user, int scorevalue, string level) { 
    Score score = new (registeredGame, user, scorevalue, level); 
    scores.Add(score); 
  } 
 
  public void PurgeUser(User user) { 
    scores.RemoveAll(score => score.Player.PlayerId == user.PlayerId); 
  } 
 
  public List<string> FormattedTopScoreTable(Score.RegisteredGame registeredGame) { 
    List<string> toptable = new List<string>(); //First sort it 
    List<Score> justOnegame = scores.FindAll(sc => sc.Game == registeredGame); 
    justOnegame.Sort(); //Grab subset 
    List<Score> topItems = (justOnegame.Count < TABLESIZE)?justOnegame:(List<Score>)justOnegame.Take(TABLESIZE); 
    for (int i = 0; i < topItems.Count; i++) { 
      Score sc = topItems[i]; 
      int rank = i + 1; 
      toptable.Add($"{rank,2}. {sc.ScoreValue,8} {sc.Player.KnownAs,-10} ({sc.Level})"); 
    } 
    return toptable; 
  } 
}
```

## 结论

我与 Zed AI 的合作相当不错——就 Claude 而言非常好，在 Zed 助手与内联转换之间的交互方面有时有点瑕疵。我喜欢 Cursor 和 Zed 用来在 Claude 和你的代码之间集成建议这两种尝试。目前，Cursor 在交互方面更熟练——但现在还是早期。

我喜欢在 Zed AI 中以类 RAG 的方式收集信息来增加上下文，并将其作为折叠文本添加的想法。但当然，我们永远不会确切知道需要什么，或者什么时候需要。

最大的可能是，在不到一年的时间内，随着一个更具示范性的添加/删除/替换机制，Cursor 和 Zed 都将成为使用 AI 的代码流的典范。