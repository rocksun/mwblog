I originally wanted to look at the OpenCode agentic command line interface (CLI), but this has now been renamed [Crush](https://github.com/charmbracelet/crush?tab=readme-ov-file). Given that the repository only changed hands on July 29, 2025, the title of this article reflects the recent transition.

So: Crush is a Go-based open source CLI application that brings AI assistance to your terminal. It provides a terminal user interface (TUI) for interacting with various AI models to help with coding tasks, debugging and more. Or as they say: “Your new coding bestie.”

[![](https://cdn.thenewstack.io/media/2025/08/2c5c79f2-image.png)](https://cdn.thenewstack.io/media/2025/08/2c5c79f2-image.png)

[Charm](https://charm.land/), I guess as in making pretty (or garish, depending on your taste) text user interface.

Since [I wrote about TUIs recently](https://thenewstack.io/user-interfaces-in-agentic-cli-tools-what-developers-need/), I should point out that this project uses the [BubbleTea](https://github.com/charmbracelet/bubbletea) project under the covers. Crush is multimodel and session-based, so you can choose from a wide range of large language models (LLMs) or add your own, and you can switch LLMs mid-session while preserving context.

You can also add your own Language Server Protocol roughly in the same way you would for an editor.

## Installing

Unlike some entries, this is happy to install via homebrew. As I’m using my MacBook M4, I’ll plump for that option:

[![](https://cdn.thenewstack.io/media/2025/08/6ae5dcf5-image-1.png)](https://cdn.thenewstack.io/media/2025/08/6ae5dcf5-image-1.png)

While Crush will ask when first run about keys, we can set up the LLM we want to work with by environment variables. So let’s do that for a fresh key from [Anthropic](https://console.anthropic.com/settings/keys):

[![](https://cdn.thenewstack.io/media/2025/08/3fda7959-image-2.png)](https://cdn.thenewstack.io/media/2025/08/3fda7959-image-2.png)

A number of models are supported: the expected ones, plus some I wasn’t aware of, including “Groq” ([which has nothing to do with Grok](https://www.byteplus.com/en/topic/404694?title=does-elon-musk-own-groq)). But it also includes Grok.

Typing “crush” starts things off:

[![](https://cdn.thenewstack.io/media/2025/08/471052aa-image-3-1024x788.png)](https://cdn.thenewstack.io/media/2025/08/471052aa-image-3-1024x788.png)

While clearly picking up my Anthropic key, I can choose from a few models. I went for [Opus 4, as that was what I was familiar with](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/). (GPT-5 should be available now).

If it can’t see a Crush config file, it will ask if it can initialize:

[![](https://cdn.thenewstack.io/media/2025/08/cc46b1ab-image-4-1024x344.png)](https://cdn.thenewstack.io/media/2025/08/cc46b1ab-image-4-1024x344.png)

This is a very nice way to both get you started in the codebase and to create the context file. Side note: While using informal language like “yep” and “nope” is fun, this is a little antagonistic if English is not your cultural language.

Steering into my project from within Crush was awkward, as it applies additional permissions for OS commands within Crush:

[![](https://cdn.thenewstack.io/media/2025/08/102203ad-image-5-1024x349.png)](https://cdn.thenewstack.io/media/2025/08/102203ad-image-5-1024x349.png)

Above, I typed `ls` and got a reply, and then tried `cd ..` and this caused a permission switch to check whether I actually wanted to move the directory.

## Permissions

This does lead on gently to checking how Crush deals with permissions. Initially, I wanted to know if it could make changes outside of the project directory. But I don’t think that is expressed yet (the project is by no means mature). If you look in the `crush.json` configuration file, you can manipulate the familiar “allow” list:

```
{ 
  "$schema": "https://charm.land/crush.json", 
  "permissions": { 
     "allowed_tools": [ 
       "view", 
       "ls", 
       "grep", 
       "edit" 
     ] 
  } 
}
```

These entries explain the behaviour I saw above. You can skip all permissions with the `--yolo` flag. (Yes, you may well be getting the feeling this project has a particular carefree vibe.)

## Process a Project

I let it process my main Unity development directory to see what the [CRUSH.md](http://CRUSH.md) would have and how it behaved:

[![](https://cdn.thenewstack.io/media/2025/08/4db3d691-image-6-1024x125.png)](https://cdn.thenewstack.io/media/2025/08/4db3d691-image-6-1024x125.png)

It was also looking out for any Cursor or Copilot instructions to incorporate. I assume it will eventually do this for more provider instruction files. In fact, the first pass agent looks for configurations, tests and project files.

The command line at the bottom includes a quit command, which is a nice, simple addition. Note that as I’m running within the Warp terminal, some commands will be swallowed by that. But this is a [general problem with terminal emulations within terminals](https://thenewstack.io/user-interfaces-in-agentic-cli-tools-what-developers-need/). Another example of this is that I cannot use the mouse to place the cursor while writing commands, which I can within Warp. Nor could I copy the text. Or copy the previous command.

I had thought the project processing had completed, but there was no [CRUSH.md](http://CRUSH.md) file — actually I ran out of ~~the new gold~~ tokens, so I topped up the meter at the Anthropic console. I deleted the `.crush` directory and let it try again. This time it finished up, having built a nice, concise CRUSH.md file, which it added to the .gitignore file:

[![](https://cdn.thenewstack.io/media/2025/08/0c075d77-image-7-1024x157.png)](https://cdn.thenewstack.io/media/2025/08/0c075d77-image-7-1024x157.png)

For testing, I’m going to ask it to generate a new class within a collection of strategies. This is a bit different from my normal test, but it is actually something I need to do in my game project. I’ll use some phrases that will force the LLM to pick up context within the project, but overall, it is not too much work. I just want to add a new type of game narrative, based on an old type:

[![](https://cdn.thenewstack.io/media/2025/08/96969771-image-8-1024x102.png)](https://cdn.thenewstack.io/media/2025/08/96969771-image-8-1024x102.png)

As usual, I’m not really trying to test the LLMs anymore — just how Crush represents the output and processes the permissions. Note that I didn’t add a C# LSP.

When it had established where to add the class and generated it, I was presented with a permission request:

[![](https://cdn.thenewstack.io/media/2025/08/85fc9d42-image-9-1024x594.png)](https://cdn.thenewstack.io/media/2025/08/85fc9d42-image-9-1024x594.png)

It correctly interpreted “farmer” as a character name and a type. It also correctly altered the name of the string from “PollutionBad” to “FreezingBad,” which is one of the benefits of LLMs: They understand English language context intertwined within a coding context.

It then asked permission to add the strategy to the list as required:

[![](https://cdn.thenewstack.io/media/2025/08/94e5b56f-image-10-1024x381.png)](https://cdn.thenewstack.io/media/2025/08/94e5b56f-image-10-1024x381.png)

It then had a good try at also adding instances of the new narrative in a similar way to others within the project, but it didn’t have enough information to do that properly. What it had done was fine, so I stopped it there.

While the separate tasks were not presented in a list before trying, it did organize the work sensibly so I could follow what it was doing. It allows you to use Tab to switch between the request block and response block.

## Conclusion

While Crush is still short of a good few UI necessities, it does have some interesting and novel additions. Right now, it is certainly weaker than using, say, Warp, with its agentic CLI integrated into the terminal. But Crush does have a consistent approach via its text user interface, so it might well punch above its weight as later innovations are joined by stronger basics via open source contributions.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)