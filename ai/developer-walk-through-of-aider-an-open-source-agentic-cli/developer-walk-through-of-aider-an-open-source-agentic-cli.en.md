In my journey through agentic command-line interfaces (CLI), I have finally come to a community-led open source effort, [Aider](https://aider.chat/). Ironically, this is one of the original agentic CLIs, and as you’ll see, it somewhat shows its age. I’ll see how it figures against my set of [quality-of-life features for agentic AI](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/) and my short test.

The elevator pitch *“*Aider lets you pair program with LLMs to start a new project or build on your existing codebase*”* is one that chimes with my argument about [where agentic CLIs excel](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/). Subtle but well stated, large language models (LLMs) are best seen as engineering tools working across your project as a whole — not so much as editing help while writing code.

## Installation

Aider [installs as a Python project](https://aider.chat/docs/install.html). Python between 3.8-3.13 is suggested:

[![](https://cdn.thenewstack.io/media/2025/07/6a4a832c-image.png)](https://cdn.thenewstack.io/media/2025/07/6a4a832c-image.png)

Homebrew isn’t mentioned immediately, so I will start a virtual as one is encouraged to do. I drop down a directory to set up venv:

[![](https://cdn.thenewstack.io/media/2025/07/4580d386-image-1.png)](https://cdn.thenewstack.io/media/2025/07/4580d386-image-1.png)

Note the tell-tale project name that venv gives you at the prompt.

To complete the install, I type the following:

```
> aider-install
```

The documentation then gives choices between models from DeepSeek, OpenAI and Anthropic. I have a key for Anthropic, so I’ll use that. I sign in and use the [console](https://console.anthropic.com/settings/keys) to create a key. To start Aider, I type:

```
> aider --model sonnet --api-key anthropic=sk..
```

Having said that, I can see ways of [starting Aider with many other LLMs](https://aider.chat/docs/llms.html), including [Ollama self-hosted LLMs](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/).

We get a simple start session:

[![](https://cdn.thenewstack.io/media/2025/07/cbfda785-image-2-1024x283.png)](https://cdn.thenewstack.io/media/2025/07/cbfda785-image-2-1024x283.png)

So Aider runs its own CLI, in this case within [my Warp console](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/). (If I resize my terminal, that green line no longer fits the width. A full line isn’t a very sensible design in a terminal. Later on there are further small problems with Aider’s pseudo terminal, like repeating prompt symbols.)

You’ll note that the git directory is below the working directory, which caused an issue as I don’t have the contents checked in. But this isn’t a usual problem. Just a warning of possible confusion.

So what is the difference between the main model and the weak model? Fortunately, I was able to ask Aider. It suggests that the weaker model is used for short, quick (and hopefully cheaper) interactions:

* Simple code completions
* Basic refactoring tasks
* When the main model is unavailable
* Cost-sensitive operations
* Quick iterations where perfect code isn’t critical

In short, the main model is used for agentic tasks.

Looking at the end of that last response, I note that it gives a running total of costs. This is something I look for in my agentic quality-of-life features:

[![](https://cdn.thenewstack.io/media/2025/07/b28004c2-image-3-1024x118.png)](https://cdn.thenewstack.io/media/2025/07/b28004c2-image-3-1024x118.png)

Listing the models in use is also a necessity. I have not seen any clue to permissions or restrictions.

## The Standard JSON Merge Test

As in previous [agentic CLI reviews](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/), I’ll merge two JSON files together with a simple caveat.

Note that this does not represent any form of standardized test (go to [terminal-bench](https://www.tbench.ai/) for something like that). I simply want a straightforward, yet possibly ambiguous test that I know an LLM can manage so we can see how the interface works.

Aider has the concept of files in focus, that you can “add to the chat” as it puts it. Although I see that it is getting confused scanning my repo, it understands a set of files that it should be focusing on, so that it can stage itself into git.

What I’ll do is add my two familiar city JSON files to the current directory, and then /add them to Aider. I’ll do this in a separate tab:

[![](https://cdn.thenewstack.io/media/2025/07/171f4898-image-4-1024x317.png)](https://cdn.thenewstack.io/media/2025/07/171f4898-image-4-1024x317.png)

Those directories were added by Aider, and we’ll see why shortly.

As before, I will ask for the JSON merge using this request:

*“Please update the JSON file original\_cities.json with the contents of the file updated\_cities.json but if the “image” field is different, please update or write a new “imageintended” field with the new value instead.”*

## But First, Restrictions

I have to say, I can’t quite find simple references to where Aider might roam. It can see the repo, and it will only think it owns files that are added with `/add` — this is probably because it was developed before the power (and risk) that the newer models provide. I add this note because, in general, before you use any agentic tool, you must understand what changes to your file system it believes it is allowed to make.

Now, as I get on with the request, we get a clear indication of what I mentioned before: It wants files ‘added’ to ‘the chat’. This should help clear up security concerns:

[![](https://cdn.thenewstack.io/media/2025/07/62a68641-image-5-1024x190.png)](https://cdn.thenewstack.io/media/2025/07/62a68641-image-5-1024x190.png)

I then hit two problems. Firstly, I didn’t read the warning that all files are relative to the git directory, not the current directory. Secondly, I noticed that it got confused by its own `.gitignore` file.

It then struck me what was going on: It clearly thought my `aider` directory was also its aider directory! A simple directory name clash. So I restarted in a new directory. This would also give me the chance to use the `--subtree-only` flag to stop it scanning the whole repo:

[![](https://cdn.thenewstack.io/media/2025/07/4c07075c-image-6-1024x115.png)](https://cdn.thenewstack.io/media/2025/07/4c07075c-image-6-1024x115.png)

I copied the files over to the new directory and added them to Aider:

[![](https://cdn.thenewstack.io/media/2025/07/202c83ae-image-7-1024x161.png)](https://cdn.thenewstack.io/media/2025/07/202c83ae-image-7-1024x161.png)

I gave the previous request, and finally we were on our way:

[![](https://cdn.thenewstack.io/media/2025/07/48d4603f-image-8-1024x145.png)](https://cdn.thenewstack.io/media/2025/07/48d4603f-image-8-1024x145.png)

This is a good summary of what it needed to do. It then showed the git diff style for the change suggested for original\_cities.json.

```
<<<<<<< SEARCH
{
  "cities": [
    {
      "id": "London",
      "text": "London is the capital of the UK",
      "image": "BigBen"
    },
    {
      "id": "Berlin",
      "text": "Great night club scene",
      "image": "Brandonburg Gate",
      "imageintended": "Reichstag"
    },
    {
      "id": "Paris",
      "text": "Held the Olympics of 2024",
      "image": "EifelTower",
    }
  ]
}
=======
{
  "cities": [
    {
      "id": "London",
      "text": "London is the capital and largest city in Great Britain",
      "image": "BigBen"
    },
    {
      "id": "Berlin",
      "text": "Great night club scene but a small population",
      "image": "Brandonburg Gate",
      "imageintended": "BrandenburgGate"
    },
    {
      "id": "Paris",
      "text": "Held the Olympics of 2024",
      "image": "EifelTower",
      "imageintended": "NotreDame"
    },
    {
      "id": "Rome",
      "text": "The Eternal City",
      "image": "TheColleseum"
    }
  ]
}
>>>>>>> REPLACE
```

Because it used git, it didn’t really have to ask permission as it was just local commits:

[![](https://cdn.thenewstack.io/media/2025/07/bfaf9460-image-9-1024x341.png)](https://cdn.thenewstack.io/media/2025/07/bfaf9460-image-9-1024x341.png)

Of course, I didn’t make either commit, but Aider correctly added itself as a co-author.

## Conclusion

There is no doubt that Aider doesn’t have great control over the terminal compared to more recent agentic examples like Claude Code, Gemini CLI and Warp. I didn’t find Aider a particularly nice experience; or perhaps it is more accurate to say that its distance from the recent agentic models is palpable.

However, use of git makes the experience more efficient, even though git itself is quite anti-“vibe.” Of course, that is perfectly intentional — this product isn’t for vibe coders. I think some of the uncomfortable behavior (like scanning the whole repo) could be handled via flags.

Overall I wouldn’t recommend Aider, given the superior options I mentioned. But it is open source, and therefore could easily be improved. That said, at this point Aider feels like bringing a knife to a gun fight.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)