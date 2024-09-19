# An Introduction to Zed AI and How It Compares to Cursor AI
![Featued image for: An Introduction to Zed AI and How It Compares to Cursor AI](https://cdn.thenewstack.io/media/2024/09/368e729c-getty-images-qob-b3gfcxs-unsplash-1024x683.jpg)
After revisiting [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) in my last post, I thought it was also time to revisit [Zed](https://zed.dev/), which has been busy [integrating AI](https://zed.dev/blog/zed-ai) into its multiplayer code editor. Zed AI is “free during our initial launch period” but we should expect a cost soon — features like this are probably how Zed, a VC-backed startup, will start to earn revenue in the future.

Zed is [a code editor that was written from the bottom up](https://thenewstack.io/zed-a-new-multiplayer-code-editor-from-the-creators-of-atom/) — it was written in Rust and efficiently leverages multi-core processors and GPUs. Its creators have form, having also created Atom and Tree-sitter. Accordingly, Zed has the chance to fully control how AI is implemented — unlike Cursor, which forked Visual Studio Code. Cursor has achieved a clean separation between code window and AI support, so that will be an interesting comparison.

By default, Zed also uses Anthropic’s [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). However, it is also possible to plug in different LLM providers, or use [local options](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/).

I will only use Zed for editing; I’ll keep VS Code open for builds. Zed is still not implemented on Windows, and has no solid plans to do so, which may affect how you view this option. I’ll be using my trusty MacBook.

I’ll continue working on the High Score example from my [previous post](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/).

- We’ll convert the added scores to a separate JSON file;
- We’ll load the JSON file up;
- We’ll add a rank.
This is where we got to after we purged our cheating user, Kim:

12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970 |
User tim = new ("12345","Timbo"); User jim = new ("45123","Jimbo"); User kim = new ("6534", "Kimbo");TopScore ts = new TopScore(); ts.AddScore(Score.RegisteredGame.MatterBlatter, tim, 1000, "Level 3"); ts.AddScore(Score.RegisteredGame.MatterBlatter, tim, 1200, "Level 4"); ts.AddScore(Score.RegisteredGame.MasterBlaster, jim, 1000, "HellGate"); ts.AddScore(Score.RegisteredGame.MasterBlaster, tim, 1200, "FinalBoss"); ts.AddScore(Score.RegisteredGame.MatterBlatter, kim, 1000, "Level 3"); ts.AddScore(Score.RegisteredGame.MatterBlatter, kim, 3200, "Level 5"); ts.PurgeUser(kim); List<string> topscores = ts.FormattedTopScoreTable(Score.RegisteredGame.MatterBlatter); Console.WriteLine($"TOP SCORES FOR {Score.RegisteredGame.MatterBlatter}"); topscores.ForEach(sc => Console.WriteLine(sc)); public struct User { public string PlayerId; public string KnownAs; public User(string playerId, string knownAs) { PlayerId = playerId; KnownAs = knownAs; } } public class Score : IComparable<Score> { public enum RegisteredGame { MatterBlatter, MasterBlaster, MinionPinion} public DateTime Entrydate; public int ScoreValue; public string Level = ""; public RegisteredGame Game; public User Player; public int CompareTo(Sco re? other) { return (other.ScoreValue - ScoreValue); } public Score(RegisteredGame registeredGame, User player, int scoreValue, string level = "") { Game = registeredGame; Entrydate = DateTime.Now; ScoreValue = scoreValue; Level = level; Player = player; } } public class TopScore { private List<Score> scores = new List<Score>(); const short TABLESIZE = 10; public void AddScore(Score.RegisteredGame registeredGame, User user, int scorevalue, string level) { Score score = new (registeredGame, user, scorevalue, level); scores.Add(score); } public void PurgeUser(User user) { scores.RemoveAll(score => score.Player.PlayerId == user.PlayerId); } public List<string> FormattedTopScoreTable(Score.RegisteredGame registeredGame) { List<string> toptable = new List<string>(); //First sort it List<Score> justOnegame = scores.FindAll(sc => sc.Game == registeredGame); justOnegame.Sort(); //Grab subset List<Score> topItems = (justOnegame.Count < TABLESIZE)?justOnegame:(List<Score>)justOnegame.Take(TABLESIZE); topItems.ForEach(sc => toptable.Add($"{sc.ScoreValue} {sc.Player.KnownAs} ({sc.Level})")); return toptable; } } |
## Assistant Panel and Inline Transformations
When Zed updated, there was no clue if the AI was on, but when I tried to open the Assistant panel, which is the equivalent of the chat-like interface area, we got this:

There is then a laundry list of possible models that you can connect with. I chose to connect with Anthropic, which meant I needed to get a key (note: this is all done for you with Cursor). I created the key with an [evaluation plan,](https://console.anthropic.com/) but I had somehow not selected terms and conditions. This is all a bit messy at the moment.

When the Assistant was finally ready, everything worked well. My first task is to read scores from a file.

The results were correct, and could then be placed in a separate file, as I required:

12345678910111213141516171819202122232425262728293031323334 |
[ { "game": "MatterBlatter", "player": "tim", "score": 1000, "level": "Level 3" }, { "game": "MatterBlatter", "player": "tim", "score": 1200, "level": "Level 4" }, { "game": "MasterBlaster", "player": "jim", "score": 1000, "level": "HellGate" }, { "game": "MasterBlaster", "player": "tim", "score": 1200, "level": "FinalBoss" }, { "game": "MatterBlatter", "player": "kim", "score": 1000, "level": "Level 3" }, { "game": "MatterBlatter", "player": "kim", "score": 3200, "level": "Level 5" } ] |
This was good, understanding that I wanted to convert the enumeration into a string. (Unfortunately, it also used local variable names instead of the `PlayerId`
, which will cause a problem later.)
My next step will be to ask for the appropriate code to read from the `scores.json`
file and convert to arguments for the `TopScore`
object. I used the new “slash” command `/file`
to add the new scores file that I just made with the JSON into the Assistant for context. Think of this as [extra RAG](https://thenewstack.io/enhancing-ai-coding-assistants-with-context-using-rag-and-sem-rag/)-like additions:

I was then able to build the prompt:

While this isn’t the type of bulk code creation query I normally make, we did a lot of [JSON persistence with Llama 3](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/). Of course, Claude had no problem with this.

It wrote the code in an old style Main, and we’ll try and use the inline transformations to add changes to the code across. The interplay between the Assistant panel and inline transformations in the code itself is how Zed AI keeps things separated.

So here, I ask the inline assistant to add the `ScoreEntry`
class to the main code that the LLM created in the Assistant to the right:

And it’s done:

Note that I can accept the code addition with the tick.

Interestingly, the suggested JSON loading code transformation is different from the original suggestion in the Assistant:

The correction has made an interesting error. It tries to hand-match the player name with the given Users, instead of adding registration and search by name functionality to User. But the error does alert me to my own error of not using the PlayerId in the JSON.

As a developer, even with these LLM errors, this still represents an efficiency saving. This might sink a beginner who overly trusts the LLM solution, but if you just treat it as a solid start, all will be well. I’m sure Claude and I could have further conversations if I wanted to clean things up that way.

With the Users code corrected, we get back to a result (from VS Code) like this:

Lastly, we want to add a rank for readability. Let’s see if we can ask for that.

The folded text is the whole file, and added with `/tab`
, which just adds the whole open file as context.

I had difficulty asking the inline assistant to replace the redundant code with the new code. It was loathe to delete old code — which may be a good thing!

After adding a few more scores from Jim for flavor, we get a nice ranked table:

Again, Claude understood immediately what “ranked” meant in this context of a high score table and created the right code. The final code is as follows:

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596 |
using System.Text.Json; User tim = new ("12345","Timbo"); User jim = new ("45123","Jimbo"); User kim = new ("6534", "Kimbo"); TopScore ts = new TopScore(); string jsonString = File.ReadAllText("scores.json"); List<ScoreEntry> scoreEntries = JsonSerializer.Deserialize<List<ScoreEntry>>(jsonString); foreach (var entry in scoreEntries) { ts.AddScore( Enum.Parse<Score.RegisteredGame>(entry.game), User.FindByPlayerId(entry.player), entry.score, entry.level ); } ts.PurgeUser(kim); List<string> topscores = ts.FormattedTopScoreTable(Score.RegisteredGame.MatterBlatter); Console.WriteLine($"TOP SCORES FOR {Score.RegisteredGame.MatterBlatter}"); topscores.ForEach(sc => Console.WriteLine(sc)); public struct User { public string PlayerId; public string KnownAs; private static List<User> registeredUsers = new (); public User(string playerId, string knownAs) { PlayerId = playerId; KnownAs = knownAs; registeredUsers.Add(this); } public static User FindByPlayerId(string id) { return registeredUsers.FirstOrDefault(u => u.PlayerId == id); } } public class ScoreEntry { public string game { get; set; } public string player { get; set; } public int score { get; set; } public string level { get; set; } } public class Score : IComparable<Score> { public enum RegisteredGame { MatterBlatter, MasterBlaster, MinionPinion} public DateTime Entrydate; public int ScoreValue; public string Level = ""; public RegisteredGame Game; public User Player; public int CompareTo(Score? other) { return (other.ScoreValue - ScoreValue); } public Score(RegisteredGame registeredGame, User player, int scoreValue, string level = "") { Game = registeredGame; Entrydate = DateTime.Now; ScoreValue = scoreValue; Level = level; Player = player; } } public class TopScore { private List<Score> scores = new List<Score>(); const short TABLESIZE = 10; public void AddScore(Score.RegisteredGame registeredGame, User user, int scorevalue, string level) { Score score = new (registeredGame, user, scorevalue, level); scores.Add(score); } public void PurgeUser(User user) { scores.RemoveAll(score => score.Player.PlayerId == user.PlayerId); } public List<string> FormattedTopScoreTable(Score.RegisteredGame registeredGame) { List<string> toptable = new List<string>(); //First sort it List<Score> justOnegame = scores.FindAll(sc => sc.Game == registeredGame); justOnegame.Sort(); //Grab subset List<Score> topItems = (justOnegame.Count < TABLESIZE)?justOnegame:(List<Score>)justOnegame.Take(TABLESIZE); for (int i = 0; i < topItems.Count; i++) { Score sc = topItems[i]; int rank = i + 1; toptable.Add($"{rank,2}. {sc.ScoreValue,8} {sc.Player.KnownAs,-10} ({sc.Level})"); } return toptable; } } |
## Conclusion
My experience with Zed AI has been quite good — very good with reference to Claude, a little flaky at times with regards to the interplay between Zed Assistant and inline transformations. I like both of the attempts that Cursor and Zed use to integrate suggestions between Claude and your code. At the moment, Cursor is a bit more proficient at the interplay — but these are early days.

I like the idea in Zed AI of gathering information in a RAG-like fashion for added context, and adding these as folded text. But of course, we never know quite what is needed, or when.

Most likely, in less than a year and with a more demonstrative add / remove / replace mechanism, both Cursor and Zed will become exemplars of code flow using AI.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)