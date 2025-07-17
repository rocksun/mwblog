After the enlightening [question-and-answer session](https://thenewstack.io/qa-how-warp-2-0-compares-to-claude-code-and-gemini-cli/) with Warp CEO [Zach Lloyd](https://www.linkedin.com/in/zachlloyd), I was ready to try out [Warp](https://www.warp.dev/) 2.0’s [agentic large language model ability](https://www.warp.dev/blog/reimagining-coding-agentic-development-environment). This feels strange, because I have Warp sitting in front of me most of the time.

I’ve written about Warp frequently (see [my original review from a year ago](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/)), but essentially it is a modern [terminal emulator app](https://thenewstack.io/warp-vs-ghostty-which-terminal-app-meets-your-dev-needs/). If you haven’t used one of those, well, you should. Warp is well suited for agentic tasks, as it has a  built-in awareness of multiple sessions through tabs, as well as tracking when sessions stop and restart. The block structure allows for a natural separation between query and response.

Warp has always included some basic AI capabilities, which have no doubt annoyed a few — heavy terminal users are not in the same Venn diagram loop as LLM supporters, in general. The LLM could attempt to fix common problems based on the (many) ways a Unix-like command could fail.

This is partly why Warp uses the slightly hyperbolic marketing term “[agentic development environmen](https://thenewstack.io/agentic-ai-is-quietly-replacing-developers)t” to mark this bigger offering. The actual version label gives us no clue:

[![](https://cdn.thenewstack.io/media/2025/07/ee36a530-image-1024x584.png)](https://cdn.thenewstack.io/media/2025/07/ee36a530-image-1024x584.png)

## Agentic Quality of Life

Earlier this week I made a list of the [quality of life expectations](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/) for agentic sessions and, in theory, Warp has an advantage here. The terminal prompt UI is already pretty good:

[![](https://cdn.thenewstack.io/media/2025/07/d5e7d731-image-1-1024x416.png)](https://cdn.thenewstack.io/media/2025/07/d5e7d731-image-1-1024x416.png)

It displays the model in use (currently Claude 4 Sonnet, but I’ll change to Opus 4 if I can). The prompt is in ‘auto detection mode,’ which guesses if I’m clearly writing in English or using a Unix-like command.

With `cmd-I` I can toggle between the straight terminal mode, agent mode and the auto guess (icons on the bottom left). We can see the directory we are in, and the git branch.

Before doing anything, I’ll check the permissions with `Settings > AI > Agents > Permissions`, so I can determine what the AI could do if let loose.

[![](https://cdn.thenewstack.io/media/2025/07/d18f16ba-image-2-1024x651.png)](https://cdn.thenewstack.io/media/2025/07/d18f16ba-image-2-1024x651.png)

There doesn’t seem to be a way to lock activity to one directory — perhaps there is no natural concept of a project directory here (and if there is the equivalent of a [Claude.md](http://claude.md/) file, I can’t see it). But what does catch my eye is a denylist. This is a very simple but nice idea. At the end of the day, tasks are executed via OS commands, so it is sensible to check with the user for permission before removing files, spawning new shells or hitting the internet.

I’m going to ask Warp to perform a simple merge task, as I did previously with [Gemini CLI](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/) and [OpenAI Codex](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/). I have two JSON files with city information, and I want to update the first file with contents of the other.

The two JSON files are in place:

[![](https://cdn.thenewstack.io/media/2025/07/b82325f5-image-4-1024x396.png)](https://cdn.thenewstack.io/media/2025/07/b82325f5-image-4-1024x396.png)

OK, now I’m ready to ready to ask for the merge. Here is the query (the same one I asked in the previous posts). I explicitly move to [agent mode](https://thenewstack.io/warp-goes-agentic-a-developer-walk-through-of-warp-2-0/) and ask:

*“please update the JSON file original\_cities.json with the contents of the file updated\_cities.json but if the ‘image’ field is different, please update or write a new ‘imageintended’ field with the new value instead”*

[![](https://cdn.thenewstack.io/media/2025/07/337e9fe3-image-5-1024x588.png)](https://cdn.thenewstack.io/media/2025/07/337e9fe3-image-5-1024x588.png)

I’m not sure what the point is in explicitly showing me [Python](https://roadmap.sh/python) code, unbidden. I started this conversation in English, after all. However, glancing at it (and the summary at the bottom of the code), I see no obvious problems.

As it asks for permission, it also checks if it can fix the trailing comma. I’m glad it spotted that, but it didn’t need to create a diff just for that!

I notice that it hadn’t quite understood the concept of a working directory, and wanted to do everything with absolute paths. But this might just be to make other tools happy.

The final summary was good (none of the models I’ve tested have had any real material problem with this task itself), again proving that the LLM understood both the problem and the context:

[![](https://cdn.thenewstack.io/media/2025/07/423d60fe-image-7.png)](https://cdn.thenewstack.io/media/2025/07/423d60fe-image-7.png)

Now, obviously there is the issue of who I’m paying. Warp has a [payment plan](https://www.warp.dev/pricing), but I’m not sure if I can pay Anthropic directly for using Claude Opus 4, for example. But I appear to have 150 requests per month on the free tier. There is no ongoing token usage data within the display yet — and as I don’t “quit” when I change tabs in the app, there is no chance to display usage stats at the end of a session.

## Code Editor

This release of Warp includes a code editor, which was clearly designed to work with diffs as above, but you can summon it for any code file.

If I list the files in my project folder, we see that Warp left its merge file:

[![](https://cdn.thenewstack.io/media/2025/07/f5fbdab5-image-8-1024x216.png)](https://cdn.thenewstack.io/media/2025/07/f5fbdab5-image-8-1024x216.png)

On my Mac, I left-click and then I can open the file in the Warp editor (“Open with Warp”). It places the file in a separate tab and it looks like the diff above. It is intended to work within a block, with the frame buttons — but without these, it is nicely sparse and quick. You can save any changes you make with ⌘-S. There is also language-specific colouring. My guess is it will gain a context menu in a few drops.

Adding a file editor may look fairly mundane, but as Lloyd mentioned to me in our Q&A, it isn’t going to be fully featured in any way (but it still represents a slightly aggressive move if you were, say, [Zed](https://thenewstack.io/an-introduction-to-zed-ai-and-how-it-compares-to-cursor-ai/)). It does take away the cognitive friction of changing tools, which is good.

## Conclusion

An agentic terminal should be able to handle much harder requests, where a large codebase is involved. However, because I have asked very specific and completable requests, all the agentic tools I’ve tested recently have managed perfectly well. And yes, Warp presented the solution efficiently.

The Warp terminal needs to add some visible usage stats, but as I’ve said, it already has the framework to allow the user to stay in control. Overall, I think Warp is in a good position to adapt to the [agentic era](https://thenewstack.io/qa-how-warp-2-0-compares-to-claude-code-and-gemini-cli/) because of its excellent terminal heritage.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)