# Using Cursor AI as Part of Your Development Workflow
![Featued image for: Using Cursor AI as Part of Your Development Workflow](https://cdn.thenewstack.io/media/2024/09/a99dfe9f-alex-shuper-nacmb7m2rhi-unsplash-1024x576.jpg)
Since I last [reviewed it](https://thenewstack.io/testing-an-ai-first-code-editor-good-for-intermediate-devs/), [Cursor AI](https://www.cursor.com/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) has gotten [very popular](https://thenewstack.io/5-ways-cursor-ai-sets-the-standard-for-ai-coding-assistance/). The common reported experience is that after trying alternatives, Cursor produces better results. This is perhaps due to the [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) LLM engine, which is generally seen to be [quick and accurate for coding](https://www.tomsguide.com/ai/cursor-is-chatgpt-for-coding-now-anyone-can-make-an-app-in-minutes). One criticism I had in my original review was that it directly depended on [OpenAI](https://thenewstack.io/getting-started-with-openais-gpt-builder-and-how-it-uses-rag/) and its GPT models, so this change has clearly been a benefit. And you can switch models quite easily.

Cursor is written from a fork of Visual Studio Code. I find the design of VS Code a bit finicky, but its flexibility is a strength. As I’ll explain shortly, this does present some problems for Cursor. Unfortunately, you cannot actually run a .NET program and debug it in Cursor, because Microsoft blocks that.

We have established over the past year that AI is very good at getting a good template into your editor and usually gives good code completion hints. We’ve seen a strong ability to summarize unknown code and create tests. I’m less interested in developing code from scratch via a chat-style interface; most professional developers generally already have a project that they are working on.

I’m going to try it out again, as part of a normal development flow. I have to be careful with demonstrations, because if a demo frequently appears on the web, it may have ingested it. But my example is not too obscure.

## High Score
I’m going to develop a simple High Score table in C#. All this does is receive scores from various games, then displays the scores for a given game, in order.

- I will write the code (separately from Cursor) and ask Cursor to summarize what it does.
- I will ask it to spot a bug that I will leave in it.
- I will add the ability to remove a particular score and see how it makes suggestions.
- I will then ask it to create some unit tests.
Given progress, I don’t believe any of these tasks should be problematic, but I am more interested in how things happen. Note that every editor makes sensible autocomplete suggestions, so I won’t focus on this aspect.

So, I wrote the following in kosher VS Code, using [top-level statements](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/top-level-statements), hence less boilerplating:

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869 |
using System; using System.Collections.Generic; User tim = new ("12345","Timbo"); User jim = new ("45123","Jimbo"); User kim = new ("6534", "Kimbo"); TopScore ts = new TopScore(); ts.AddScore(Score.RegisteredGame.MatterBlatter, tim, 1000, "Level 3"); ts.AddScore(Score.RegisteredGame.MatterBlatter, tim, 1200, "Level 4"); ts.AddScore(Score.RegisteredGame.MasterBlaster, jim, 1000, "HellGate"); ts.AddScore(Score.RegisteredGame.MasterBlaster, tim, 1200, "FinalBoss"); ts.AddScore(Score.RegisteredGame.MatterBlatter, kim, 1000, "Level 3"); ts.AddScore(Score.RegisteredGame.MatterBlatter, kim, 3200, "Level 5"); List<string> topscores = ts.FormattedTopScoreTable(Score.RegisteredGame.MatterBlatter); Console.WriteLine($"TOP SCORES FOR {Score.RegisteredGame.MatterBlatter}");topscores.ForEach(sc => Console.WriteLine(sc)); public struct User { public string PlayerId; public string KnownAs; public User(string playerId, string knownAs) { PlayerId = playerId; KnownAs = knownAs; } } public class Score : IComparable<Score> { public enum RegisteredGame { MatterBlatter, MasterBlaster, MinionPinion} public DateTime Entrydate; public int ScoreValue; public string Level = ""; public RegisteredGame Game; public User Player; public int CompareTo(Score? other) { return (other.ScoreValue - ScoreValue); } public Score(RegisteredGame registeredGame, User player, int scoreValue, string level = "") { Game = registeredGame; Entrydate = DateTime.Now; ScoreValue = scoreValue; Level = level; Player = player; } } public class TopScore { private List<Score> scores = new List<Score>(); const short TABLESIZE = 10; public void AddScore(Score.RegisteredGame registeredGame, User user, int scorevalue, string level) { Score score = new (registeredGame, user, scorevalue, level); scores.Add(score); } public List<string> FormattedTopScoreTable(Score.RegisteredGame registeredGame) { List<string> toptable = new List<string>(); //First sort List<Score> justOnegame = scores.FindAll(sc => sc.Game == registeredGame); justOnegame.Sort(); //Grab subset List<Score> topItems = (justOnegame.Count < TABLESIZE)?justOnegame:(List<Score>)justOnegame.Take(TABLESIZE); topItems.ForEach(sc => toptable.Add($"{sc.ScoreValue} {sc.Player.KnownAs} ({sc.Level})")); return toptable; } } |
This produces:
… which is in the wrong order for a High Score table.
Just pressing the “Download for Free” button on the [main page](https://www.cursor.com/) downloaded build version 0.40.4 of Cursor. As you would if you were starting an existing project with VS Code, it is best to run Cursor from the command line, within the root folder, so that it picks up the context in your shell. To help, you may want to open the Command Palette and use `Shell Command: Install 'cursor'`
command.

Unfortunately, you cannot actually run a .NET program and debug it in Cursor, because Microsoft blocks it. If Cursor was a plugin to VS Code, all would be fine, but as it is a fork, Microsoft doesn’t recognize it. I’m sure this will be resolved before long, but right now it means you need to keep VS Code open to run the code.

First, the summary. After bringing up the chat sidebar (which correctly doesn’t appear unless you ask for it), I asked Claude 3.5 Sonnet to “summarize the code.” Here are the highlights:

*1. The code defines a simple game-scoring system with three main classes/structs:*
`User`
: Represents a player with an ID and name.`Score`
: Represents a game score with details like game type, player, score value, and level.`TopScore`
: Manages a list of scores and provides methods to add scores and generate formatted top score tables.
*2. The Score class includes an enum RegisteredGame for different game types and implements IComparable<Score> for sorting.*
*3. The TopScore class has methods:*
`AddScore`
: Adds a new score to the list.`FormattedTopScoreTable`
: Generates a formatted list of top scores for a specific game type.
*4. The main program creates some sample users and scores, adds them to a TopScore instance, and then prints the top scores for the “MatterBlatter” game.*
While much of this uses the context of the variable names, the summary “simple game-scoring system” is useful, as well as “generate formatted top score tables.” I like the fact it understood that it was printing the top scores for a game called “MatterBlatter,” pulling the name from within the enumeration.

Now, it is quite tough for the program to spot that my tables print lowest score to highest, whereas a traditional top score table places the highest first. Nevertheless, I’ll ask it to spot any bugs.

Yes, it spotted it. This is quite impressive, as it understood the human context of the High Score table:

*Yes, there’s a significant bug in the code. The main issue is in the FormattedTopScoreTable method of the TopScore class. Here’s the problematic part:*
1234567 |
public List<string> FormattedTopScoreTable(Score.RegisteredGame registeredGame) { // ... existing code ... justOnegame.Sort(); //Grab subset List<Score> topItems = (justOnegame.Count < TABLESIZE)?justOnegame:(List<Score>)justOnegame.Take(TABLESIZE); // ... existing code ... } |
*The bug is:*
*The*`Sort()`
method is called on the list, but it’s sorting in ascending order (lowest to highest) because of how`CompareTo`
is implemented in the`Score`
class.*The*`Take(TABLESIZE)`
method is then used to select the top items, but it’s actually selecting the lowest scores instead of the highest.
*To fix this, you should:*
-
*Reverse the comparison in the*`CompareTo`
method of the`Score`
class.*Use*`OrderByDescending`
instead of`Sort()`
in the`FormattedTopScoreTable`
method.
Changing the compare around works just fine. The advice to reverse the comparison is all that is required. Again, this is a good spot because the code was functional, but it understood the meaning wasn’t as I intended. And it explained this. After switching around the <code>compareTo</code>, things are as they should be:

OK, so I have discovered subsequently that Kim has been cheating, so I want to remove all of her scores from the list. We’ll call it “PurgeUser” on the top score list.

I ask in the chat, “How can I write a PurgeUser method, to remove all the scores from a certain user?”

The method is given:

123 |
public void PurgeUser(User user) { scores.RemoveAll(score => score.Player.PlayerId == user.PlayerId); } |
… as well as how to use it:
1 |
ts.PurgeUser(userToPurge); |
It also spots one requirement:
`“Note: This method assumes that PlayerId is unique for each user.”`
An obvious point, but I like the fact it mentioned this as part of its assumptions. It understood that I might have just used a pattern without being aware of an underlying necessity.

Purging Kim works just fine. Finally I asked it to suggest unit tests — I previously did this with [Codium](https://thenewstack.io/make-your-dev-life-easier-by-generating-tests-with-codiumai/). These were all done comprehensively, but here is one example:

1234567 |
[Test] public void AddScore_AddsScoreCorrectly() { topScore.AddScore(Score.RegisteredGame.MatterBlatter, user1, 1000, "Level 1"); var scores = topScore.FormattedTopScoreTable(Score.RegisteredGame.MatterBlatter); Assert.AreEqual(1, scores.Count); Assert.AreEqual("1000 Alice (Level 1)", scores[0]); } |
It has correctly expanded out the string to make the right assert.
I noticed there was an Apply button on the top right of the chat panel with the tests:

It then checked that I wanted to do this. Then it lets you push the diffs over to your open code file. (Actually this didn’t work in my case; tests should be placed in a separate file)

## Conclusion
I like the way Cursor places any code mentioned within the chat channel inside separate panels that can later be integrated via diffs to your code. This feels like the right way to do things. It also did work very quickly and made autocompletion suggestions smartly.

Overall, Cursor has gone down the route of “tool,” not “seer.” This gives me much more confidence that Cursor is taking part in your workflow, not trying to replace it.

I think how it continues to work with VS Code will determine future success. It seems more than possible that Microsoft will collaborate with Cursor to try to bring more success to the AI-powered coding world.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)