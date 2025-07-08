Before I launch [Gemini CLI](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/), Google’s open source AI terminal app, let’s look at what the “quality-of-life” expectations are for agentic applications. Now that we have several of these tools — [Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/), [Warp](https://thenewstack.io/qa-how-warp-2-0-compares-to-claude-code-and-gemini-cli/) and [OpenAI Codex](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/) are other examples — we have a better sense of what a developer needs from them.

Firstly, it needs to be easy to get started on the command line in your terminal. Developers are still the primary target audience for agentic apps, so environment variables or flags for options are fine. But getting straight in is vital.

For example, connecting your API key to your account can be done via environment variable or up in a web page console. Knowing when you are running out of tokens (whether freely given or paid for) is now an important gauge.

When we hit the start button, we need a simple session intro summary so that we know at least the following things:

* The model in use;
* The project directory;
* Any other pertinent permission or account information, or if a working file is being watched.

A working file in the project directory where assumptions based on the project are written and can be tracked (like the Claude.md file) is an important innovation to move beyond a session life cycle into a project life cycle.

Permission boundaries have to be respected; and in general we are in the early days regarding when to allow the large language model (LLM) to change files, and where. I’ve argued that forcing vibe coders to use git is a bit malign — but then again, if you fail to plan you are clearly planning to fail.

Showing us an execution plan the LLM will follow to fulfill your request feels good, but has not yet proven to be essential. But unless this is done, the exact tactics an LLM will use are opaque. A simple checkbox list will suffice.

A quit session summary showing time, requests and tokens used is great. Full accounts can really only be tracked on a user page.

There are plenty of other features that will creep into the above list, but we need to be aware of backsliding as well as genuinely useful innovations.

## Starting up Gemini

As with all cloud based LLMs, we must show our fealty before we get access to the precious tokens. Go to [Google Studio](https://aistudio.google.com/apikey) to generate a key. Currently you are given 100 requests a day (check the other tier limits [here](https://ai.google.dev/gemini-api/docs/rate-limits#free-tier)).

We can [install](https://github.com/google-gemini/gemini-cli) Gemini via npm at the terminal:

|  |  |
| --- | --- |
|  | npm install -g @google/gemini-cli |

Next, set your API key as an environment variable — I’m doing it here in the command line on my MacBook:[![](https://cdn.thenewstack.io/media/2025/07/7271928f-image.png)](https://cdn.thenewstack.io/media/2025/07/7271928f-image.png)

Then type the command `gemini` and we are off:

[![](https://cdn.thenewstack.io/media/2025/07/d059b290-image-1.png)](https://cdn.thenewstack.io/media/2025/07/d059b290-image-1.png)

As I mentioned in the quality-of-life section above, this does the important thing of pointing at the active model (Gemini-2.5 Pro in this case) as well as reflecting the project directory.

The theme selection screen disappears as soon as you press return, but I assume you can bring it back. It takes up quite a lot of space on the introduction screen.

Like Claude Code, there is markdown file — GEMINI.md in this case — for request customization. I won’t use it in this post.

What does “no sandbox” mean? The bad news is that Gemini starts off with no restrictions as to where your AI may roam. I’m afraid that isn’t very sensible, but Gemini gives you fairly straightforward options. The good news is that we can use [macOS Seatbelt](https://github.com/google-gemini/gemini-cli/blob/main/docs/sandbox.md), which starts off with a sensible policy of restricting access to within the project directory.

So I’ll exit this session (type `/quit`) and we can restart with this basic security.

The quit screen provides some of the stats I referred to earlier:

[![](https://cdn.thenewstack.io/media/2025/07/1fc29cc5-image-2-1024x471.png)](https://cdn.thenewstack.io/media/2025/07/1fc29cc5-image-2-1024x471.png)

We can use Seatbelt by just setting an environment variable in this session, then adding a flag:

[![](https://cdn.thenewstack.io/media/2025/07/85c1263f-image-3-1024x462.png)](https://cdn.thenewstack.io/media/2025/07/85c1263f-image-3-1024x462.png)

Now we are good to go, as we have our seatbelt on.

As I did with [Codex](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/) in a recent post, let’s try out the merge of two JSON files. As before, I’m looking for how the structure supports me, as much as the outcome. If you don’t want to read the previous post, imagine I have a city website that uses JSON data. I have a JSON file called *original\_cities.json*:

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 | {    "cities": [      {        "id": "London",        "text": "London is the capital of the UK",        "image": "BigBen"      },      {        "id": "Berlin",        "text": "Great night club scene",        "image": "Brandonburg Gate",        "imageintended": "Reichstag"      },      {         "id": "Paris",         "text": "Held the Olympics of 2024",         "image": "EifelTower",      }    ]  } |

The spelling errors and formatting error (extra comma) are intentional; we want to see if we can bait the LLM.

I also have another file, called *updated\_cities.json*:

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25 | {    "cities": [      {        "id": "London",        "text": "London is the capital and largest city in Great Britain",        "image": "BigBen"      },      {        "id": "Berlin",        "text": "Great night club scene but a small population",        "image": "BrandenburgGate",        "imageintended": "Reichstag"      },      {        "id": "Paris",        "text": "Held the Olympics of 2024",        "image": "NotreDame"      },      {        "id": "Rome",        "text": "The Eternal City",        "image": "TheColleseum"      }    ]  } |

I want to update the first file with the contents of the second. This simulates slightly out-of-synch working. I have one condition: I want any updated image references (that I may not have yet) copied into a key called “imageintended” so that I don’t use the data and cause a crash.

Essentially all the merge should do is add the Rome entry to the first file and introduce the new image references without overwriting the existing image key.

So my project folder looks like this. Note, I haven’t created a GEMINI.md file:

[![](https://cdn.thenewstack.io/media/2025/07/f804495a-image-4-1024x230.png)](https://cdn.thenewstack.io/media/2025/07/f804495a-image-4-1024x230.png)

I’ll use the same request I gave to Codex:

*“please update the JSON file original\_cities.json with the contents of the file updated\_cities.json but if the ‘image’ field is different, please update or write a new ‘imageintended’ field with the new value instead”*

So let’s see what it does. This task may look specific, but is actually a bit vague, which reflects a request from the average human.

After getting confused about its project file, it gave me a perfectly good answer:

[![](https://cdn.thenewstack.io/media/2025/07/4fd8ba33-image-5-1024x578.png)](https://cdn.thenewstack.io/media/2025/07/4fd8ba33-image-5-1024x578.png)

Updating text, adding the new entry and not overwriting any values in the “image” key — all done. It didn’t try to fix inconsequential spelling and didn’t get confused by the trailing comma. It was far quicker than Codex as well.

I checked the file, and indeed the changes were made. Before it answered, it didn’t quite make a plan, but gave me a fairly basic explanation of what it would do:

[![](https://cdn.thenewstack.io/media/2025/07/cd590cdf-image-6-1024x193.png)](https://cdn.thenewstack.io/media/2025/07/cd590cdf-image-6-1024x193.png)

As the outcome was entirely correct, the process didn’t really matter. But only by checking intentions can you really correct LLM “thinking” when it takes the wrong path.

I’ll exit to show the final expenditure summary:

[![](https://cdn.thenewstack.io/media/2025/07/56b65551-image-7-1024x607.png)](https://cdn.thenewstack.io/media/2025/07/56b65551-image-7-1024x607.png)

## Conclusion

As I said, this isn’t a direct LLM comparison, but Gemini gave me an efficient agentic experience. I’m sure Google can plug in any of the missing quality-of-life issues I mentioned (specifically, some running stats on token usage), but it is definitely ready for action right now. There is a growing coterie of agentic terminal applications out there for developers to try, and Gemini CLI is a solid addition to that list.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)