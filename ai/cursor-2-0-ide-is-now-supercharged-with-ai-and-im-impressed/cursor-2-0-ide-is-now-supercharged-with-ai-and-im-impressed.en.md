The [Cursor IDE](https://thenewstack.io/install-cursor-and-learn-programming-with-ai-help/) has been recently updated to version 2.0, and it carries with it some powerful [AI integration](https://thenewstack.io/six-reasons-youll-want-to-use-mcp-for-ai-integration/). This new update landed at the end of October, and it includes a new feature called Composer, which is a frontier model that is purported to be four times faster than similar models.

The new version has been built for low-latency agentic coding within Cursor and was trained with several tools, including codebase-wide semantic search. This training makes Cursor much more capable of understanding and working with larger codebases.

[Cursor 2.0](https://cursor.com/blog/2-0) also has a new, cleaner interface, so it should be even easier to hit the ground running. You’ll also find plenty of agents to enable/disable, such as:

* Composer 1
* Sonnet 4.5
* Gemini 3 Pro
* GPT-5.1 Codex High
* GPT-5.1
* GPT-5.1 Codex Mini
* Grok Code
* Gemini 2.5 Flash
* Deepseek V3.1
* Ollama
* GPT-5.1 Codex Fast

The above list is just scratching the surface (Figure 1).

[![](https://cdn.thenewstack.io/media/2025/11/ae083f47-cursor1.jpg)](https://cdn.thenewstack.io/media/2025/11/ae083f47-cursor1.jpg)

Figure 1: As you can see, there are tons of agents that can be used with Cursor 2.0.

Other features found in Cursor 2.0 include:

* Multiple agents (up to 8) can be run in parallel.
* Combined diff view when using multiple agents.
* New dedicated Agent view.
* Support for multistep coding tasks.
* Integrated Chrome DevTools.
* Seamless switching between integrated and regular Chrome browser.
* Teams can now define and share custom commands and rules to streamline workflows.
* Built-in speech-to-text functionality.
* Enhanced language-specific features to make it easier to navigate and debug code.
* Shell commands run in a secure, sandboxed environment.

I decided to give Cursor 2.0 a try and see how well it works. I used an old [Python](https://thenewstack.io/what-is-python/) script I wrote for rolling D&D dice to see how well the agent could improve the code (and how the code functions).

The problem I had with the original code was the format for the dice to be rolled. Originally, the format was like “3d6+2,” which meant roll three six-sided dice and add two to the total. But what if I wanted to simply roll a single die or add a negative modifier? Maybe I want to notate the dice roll with spaces, such as “3 d 6 + 2”? There are all sorts of permutations for dice-rolling input formats, and my original code couldn’t handle them.

Before I get to that, let’s talk about installing and setting up Cursor.

## Installing Cursor

This is actually quite easy. If you’re using macOS or Windows, simply download the associated installer file, double-click it, and walk through the installation wizard. Simple.

For Linux, you’ll need to download the required installer (such as .deb or .rpm). If your distribution is set up properly, you might be given the option to open the file with your default app store. If not, let the file download complete and run the installation command, such as:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo dpkg -i cursor\*.deb -y |
|  | suro ym install cursor\*.rpm -y |

Once the installation is completed, you should find a Cursor launcher in your desktop menu. Launch the app and get ready to rock.

## Configuring Cursor

Cursor works right out of the box. In fact, I opened my Python project, opened the agent, typed my query, and let it do its thing.

However, you might want to take care of a few configurations. To access the settings, click the gear icon near the top right of the main window. This will open a new tab, where you will see all the available options.

Click the Agents tab, and you can customize a few options, such as:

* Default mode (Agent, Plan, Ask, Last used mode).
* Default location (Editor or Pane).
* Text size (Small, Default, Large, Extra Large).
* Auto-Clear Chat (enable/disable).
* Max Tab Count.
* Queue Messages (Send immediately, Send after current message, Stop & send right away).
* Usage Summary (Auto, Always, Never).
* Custom Mode (enable/disable) — this feature is in beta.
* And more.

Next, you should go to the Models tab, where you can enable or disable any/all models you want to use. At the bottom of that tab, you can also add various API keys (if necessary), such as [OpenAPI](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/), [Anthropic](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/), [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-foundry/models/openai/) and more. You can also set up a Cloud Agent, which requires a folder that contains a Git repository.

After going through the various options, close the Settings tab, and you’re ready to go.

## Working on My Python Project

After opening the project (which was saved on local storage), I first ran the app (by clicking the right-pointing arrow near the top of the editor pane) to make sure the app still ran. When I attempted to use it, I remember why I wanted to fix the input format because I wound up with an error.

With the project open, I clicked the Agent button near the top right corner (looks like an arrow pointing up right) and then queried:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | Using the current project, can you simplify the dice\_notation format so it's more user-friendly? |

That was all I said.

Cursor then set its agents to work on improving the script. It took Cursor about two minutes to fix the problem. Here’s what the agents reported that they did (Figure 2):

* Simplified single die notation: You can now use “d6” instead of “1d6” — it defaults to one die.
* Spaces allowed: Formats like “3 d 6 + 2” or “2d10 – 1” work (spaces are ignored).
* Case insensitive: “3D6+2” works the same as “3d6+2.”
* Better error messages: More descriptive errors when the format is invalid.
* More robust parsing: Uses regex for more reliable parsing.

[![](https://cdn.thenewstack.io/media/2025/11/f08b0dfc-cursor2.jpg)](https://cdn.thenewstack.io/media/2025/11/f08b0dfc-cursor2.jpg)

Figure 2: The Cursor agents did a great job improving my original code.

I then reran the Python app to see if Cursor really did improve the script and, lo and behold, it did. I could enter multiple formats for dice, and it worked to perfection.

What probably would have taken me more than an hour to do took Cursor a couple of minutes.

That alone is worth the price of entry.

Speaking of which …

## Cursor Pricing

Here’s how the Cursor pricing breaks down:

* Hobby (Free): One-week Pro trial, limited agent requests and limited tab completions.
* Pro ($20/mo): Everything in Hobby plus extended limits on agent, unlimited tab completions, background agents and maximum context windows.
* Pro+ ($60/mo): Everything in Pro plus three times usage on all OpenAI, [Claude](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/) and Gemini models.
* Ultra ($200/mo): Everything in Pro+ plus 20 times usage on all OpenAI, Claude and Gemini models, and priority access to new features.

If you like the idea of having AI agents help improve your code, do yourself a favor and give Cursor 2.0 a try.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)