This has been quite the month for “agentic” products. I had a good experience with [Claude Code in one post](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/) and then compared it to [Google Jules](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/). Meanwhile, you can read elsewhere about the new [Gemini CLI,](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/) and I’ll cover Warp’s “Agentic Development Environment” shortly.

But with this post I’ll look at [OpenAI Codex](https://openai.com/codex/), released last month, which OpenAI describes as a “cloud-based software engineering agent.” As with the other products I’ve mentioned, Codex works in the Command Line, not in an editor.

Codex doesn’t have the bells and whistles that a “vibe coder” might desire; and indeed, it is very likely to have been conceived purely as a tool for experienced developers.

## Starting With OpenAI Codex CLI

Let’s start up this “experimental” project — [still only a GitHub page](https://github.com/openai/codex/blob/main/README.md) — with a very straightforward npm package.

In some respects, Codex is a bit more ”down home,” as it asks you to tie your API key straight into an environment variable:

|  |  |
| --- | --- |
|  | export OPENAI\_API\_KEY="your-api-key-here" |

You can find your OpenAI keys [here](https://platform.openai.com/settings/organization/api-keys). It will be quite long. You can also use a settings file.

To start an interactive session, just use the command `codex`:

[![](https://cdn.thenewstack.io/media/2025/06/a70d1f83-image-1024x308.png)](https://cdn.thenewstack.io/media/2025/06/a70d1f83-image-1024x308.png)

It actually has a better starting summary than its agentic competition, like Claude Code, because it immediately states that it makes suggestions and seeks approval before doing anything [destructive](https://help.openai.com/en/articles/11096431-openai-codex-cli-getting-started). We can also see the model, and the working directory — it doesn’t appear to want or need a context file. Typing “Exit” will let you leave.

## Updating JSON Content

My task is simply updating the contents of one JSON file compared to another. This is based on a recent issue I had with a colleague because we weren’t sharing a JSON file on git, so we suddenly got a little out of sync.

A JSON file is just a set of key/value pairs. Some people refer to the key as the name field. In the example below, the file just holds city information (some text and an image) and there is an ‘id’ key that allows for direct comparison. Think of the entries as data for a website.

The interesting nuance is that the “image” key is probably pointing to a real resource, so instead of updating it with a new image reference directly (that may not exist yet), I asked my colleague to create a “imageintended” key to hold image updates.

Of course, navigating indistinct human descriptions is one of the challenges for LLMs. If the LLM always needs exact input, then the dreams of development democracy will evaporate as an experienced developer will always need to be on hand. JSON data isn’t explicitly designed to be compared in this fashion, so a little care must be taken.

OK, now to set up out the JSON files. I created the first poorly written *original\_cities.json* file in the working directory:

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 | {  "cities": [    {      "id": "London",      "text": "London is the capital of the UK",      "image": "BigBen"    },    {      "id": "Berlin",      "text": "Great night club scene",      "image": "Brandonburg Gate",      "imageintended": "Reichstag"    },    {      "id": "Paris",      "text": "Held the Olympics of 2024",      "image": "EifelTower",    }  ]  } |

Note the trailing comma in the Paris entry, as well as the misspelling of “EifelTower” — even though it is just an image name. Also note the spelling and poor format of the Berlin image name.

Here is the *updated\_cities.json* file:

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25 | {    "cities": [      {        "id": "London",        "text": "London is the capital and largest city in Great Britain",        "image": "BigBen"      },      {        "id": "Berlin",        "text": "Great night club scene but a small population",        "image": "BrandenburgGate",        "imageintended": "Reichstag"      },      {        "id": "Paris",        "text": "Held the Olympics of 2024",        "image": "NotreDame"      },      {        "id": "Rome",        "text": "The Eternal City",        "image": "TheColleseum"      }    ]  } |

Note that the image name is corrected, but that means it can no longer reference the original.

Now here is my roughly put request to Codex:

*“please update the JSON file original\_cities.json with the contents of the file updated\_cities.json but if the “image” field is different, please update or write a new “imageintended” field with the new value instead”*

In other words, updated contents is fine, but preserve the image name as updating this could cause issues.

While thinking about this problem, I got back plenty of permission requests, mainly for `sed` commands:

[![](https://cdn.thenewstack.io/media/2025/06/50ec83c7-image-1-1024x185.png)](https://cdn.thenewstack.io/media/2025/06/50ec83c7-image-1-1024x185.png)

Of course, this assumes I know what the `sed` command will do! Finally, it produced a patch:

[![](https://cdn.thenewstack.io/media/2025/06/4f2992ae-image-2-790x1024.png)](https://cdn.thenewstack.io/media/2025/06/4f2992ae-image-2-790x1024.png)

And then it finished:

[![](https://cdn.thenewstack.io/media/2025/06/3498833d-image-3-1024x578.png)](https://cdn.thenewstack.io/media/2025/06/3498833d-image-3-1024x578.png)

It had indeed modified the original\_cities.json file correctly:

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26 | {    "cities": [      {        "id": "London",        "text": "London is the capital and largest city in Great Britain",        "image": "BigBen"      },      {        "id": "Berlin",        "text": "Great night club scene but a small population",        "image": "Brandonburg Gate",        "imageintended": "BrandenburgGate"      },      {        "id": "Paris",        "text": "Held the Olympics of 2024",        "image": "EifelTower",        "imageintended": "NotreDame"      },      {        "id": "Rome",        "text": "The Eternal City",        "image": "TheColleseum"      }    ]  } |

## Conclusion

Claude Code actually made a bit of a mess of this, but Codex not only does the merge well, it also provided a very good set of notes about why it did what it did.

It fixed up the minor format error, but didn’t get confused by English spelling errors and understood the need to preserve the image reference. However, it clearly did understand the changes it was making — the notes make subtle reference to the purpose.

During the thinking process, it asked for permission plenty of times, as we knew it would.

Unlike Claude Code, it did not exactly create a transparent plan to follow. It just outputs a heap of `sed` commands, but these clearly proved good enough when executed. This makes it much less controllable from a vibe coding point of view, because someone inexperienced with code needs to know what will be happening.

I wonder whether this is the prototype for a bigger product, or whether OpenAI will cede ground for the moment to Anthropic, Google and Warp — honing its experiment before coming out with its own view of the perfect agentic experience.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)