The last time I [profiled Augment Code](https://thenewstack.io/augment-code-an-ai-coding-tool-for-real-development-work/), back in February, I found it to be one of the better LLM extensions. While the company has refreshed its offering recently, it took a bit longer to release a genuine Agentic CLI. But we now have [Auggie CLI](https://docs.augmentcode.com/cli/overview) in beta form. You will have to wait to see Auggie CLI until Aug. 28, but I have been trialing the private beta version.

As is common, [Auggie uses Node](https://docs.augmentcode.com/cli/setup-auggie/install-auggie-cli) and they suggest 22 or later, along with a “compatible shell like zsh, bash or fish.” As usual, I’ll install it in my Warp terminal:

[![](https://cdn.thenewstack.io/media/2025/08/aadb23e5-image.png)](https://cdn.thenewstack.io/media/2025/08/aadb23e5-image.png)

Augment names some “modern” terminals that it recommends, including [Ghostty](https://thenewstack.io/ghostty-will-get-you-excited-about-using-a-terminal-again/), iTerm2, Alacritty, and Kitty.

When I logged in via the terminal, I was forwarded to a website with a similar login, which seemed to give me a code as a JSON string:

[![](https://cdn.thenewstack.io/media/2025/08/cfc705a1-image-1-1024x628.png)](https://cdn.thenewstack.io/media/2025/08/cfc705a1-image-1-1024x628.png)

This was indeed reflected back in the terminal:

[![](https://cdn.thenewstack.io/media/2025/08/9fc3e2d6-image-2-1024x515.png)](https://cdn.thenewstack.io/media/2025/08/9fc3e2d6-image-2-1024x515.png)

I logged back into Augment Code, only to be told my previous subscription had expired, and that the “Community plan was unavailable at this time.” I fixed this on the website, along with some help from Augment as I realised I had crashed a closed beta.

These trips from terminal to browser are reasonable at this point in development; obviously, one assumes that jumping out of the terminal will not be the main experience in the future.

As usual, you can also set up with your token using an environment variable: `AUGMENT_SESSION_AUTH`.

And finally, we see Auggie in all its glory:

[![](https://cdn.thenewstack.io/media/2025/08/b0329acc-image-3-1024x998.png)](https://cdn.thenewstack.io/media/2025/08/b0329acc-image-3-1024x998.png)

As I was not in a valid project, and didn’t want the indexing overhead (which started automatically) I exited quickly. Using my [“Quality of life” expectations](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/), I would be happier if the intro screen mentioned which directory was being indexed and what model was in use. Also, I’ve no idea how many tokens or requests I have to spend. It does mention that commands will run automatically — though this is not a very wise default state. (On closer inspection, it does tell you which directory Auggie has been opened in under the query box on the right, but it wasn’t immediately clear.)

Before we move back into interactive mode, let’s try a one-shot, silent or non-interactive mode command. This should only be done with a safe command that doesn’t need permissions. I’ll ask it to summarise my Ruby on Rails tool project that I use in developing conversations for my game. My assumption is that it will index it behind the scenes. This took about 30 seconds to return (Warp timed it at about 38 seconds, as you can see) — the risk being that you don’t know how much time it will take, nor how it is progressing. Hence why this is not a good idea for possibly open-ended tasks.

[![](https://cdn.thenewstack.io/media/2025/08/36ec5b19-image-4-1024x618.png)](https://cdn.thenewstack.io/media/2025/08/36ec5b19-image-4-1024x618.png)

The markdown paragraphs included *Key Features* and *Technical Stack*. The only mistakes are that it saw some template deployment code for [Kamal](https://thenewstack.io/how-to-exit-the-complexity-of-kubernetes-with-kamal/) (because this is Rails; and Kamal is also from the [37 Signals](https://37signals.com/) stables) and mistakenly thought this was the deployment method. It isn’t.

In addition, it had a shot at the *Use Case*, and correctly understood that it was a tool for a game developer to manage branching dialogue and multi-character interactions.

It also added an interesting final parting remark: “The numerous backup SQL files suggest this is an actively developed tool with regular data snapshots, likely used in production for content creation.” This is exactly correct, but also a big boon as “proof of life” is rather important. As a consultant, I’ve often wasted time looking at very nice code that I only later realised was hardly ever used.

## Workspace

Auggie has a slightly more mature recognition of the project directory or workspace than other Agentic CLIs. If you run from a. git directory, it will index that. Otherwise, it will create a context workspace for you. This is important for limiting where an LLM can roam and for understanding all code in a project.

As usual, there are security issues set off by sending your code up to a third-party cloud. You can use **.augmentignore** to stop this indexing behavior for certain files. What I didn’t see was an instruction file.

## Interactive

Working interactively in the terminal is how we associate using Agentic CLI. I was interested to see if it recorded the summary — but if it did, I couldn’t see where. The project was clearly indexed, however, hence the time taken on that first non-interactive command.

When I wrote a unix command in the query box, it executed that and added some extra information:

[![](https://cdn.thenewstack.io/media/2025/08/6047dd8b-image-5-1024x885.png)](https://cdn.thenewstack.io/media/2025/08/6047dd8b-image-5-1024x885.png)

There is an organizational problem here. While it did the correct thing and executed my shell query ([in the strange world of a shell within a shell](https://thenewstack.io/user-interfaces-in-agentic-cli-tools-what-developers-need/)) it curtailed the response in order to make its own observations. If you are working from a multitab terminal, obviously, you can execute shell commands in a separate tab — but as I did ask for a listing, I’m not sure why it thought to curtail it.

As I did for [Google’s Jules,](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/) I’m going to ask Auggie to apply Bootstrap into a part of the Ruby on Rails application where I haven’t got round to doing it.

After starting the application, a quick side-by-side comparison can see that for one view, Tags, I have nice Bootstrap buttons for the standard CRUD links:

[![](https://cdn.thenewstack.io/media/2025/08/11d3ae23-image-6-966x1024.png)](https://cdn.thenewstack.io/media/2025/08/11d3ae23-image-6-966x1024.png)

But they have not been reproduced in the Voice view:

[![](https://cdn.thenewstack.io/media/2025/08/f023b11a-e71a-4edf-9257-f5dce7092b93-1024x282.png)](https://cdn.thenewstack.io/media/2025/08/f023b11a-e71a-4edf-9257-f5dce7092b93-1024x282.png)

Here is the relevant *show.html.erb view* to show information for an individual tag:

```
<div> 
  <%= link_to "Edit this tag", edit_tag_path(@tag), :class => "btn btn-warning" %> 
| <%= link_to "Back to tags", tags_path, :class => "btn btn-outline-success" %> 
  <%= button_to "Destroy this tag", @tag, method: :delete, :class => "btn btn-danger mt-2" %> 
</div>
```

Those class entries are enough to alter the appearance. Naturally, the equivalent Voice view file doesn’t have these as yet.

So let’s ask Auggie to apply bootstrap to the Voice view:

[![](https://cdn.thenewstack.io/media/2025/08/eca4ee5b-image-7-1024x57.png)](https://cdn.thenewstack.io/media/2025/08/eca4ee5b-image-7-1024x57.png)

I’ve been fair and pointed to the two files directly.

Auggie starts correctly by reading the two files and the section in question:

[![](https://cdn.thenewstack.io/media/2025/08/bcb1f833-image-8-1024x561.png)](https://cdn.thenewstack.io/media/2025/08/bcb1f833-image-8-1024x561.png)

It then produces the diff:

[![](https://cdn.thenewstack.io/media/2025/08/9c6e3fc0-image-9-1024x180.png)](https://cdn.thenewstack.io/media/2025/08/9c6e3fc0-image-9-1024x180.png)

I like the way it says, “Now I can see the pattern.” This tells me it fundamentally understands that this is a change made by comparison. It then gave a summary of changes:

[![](https://cdn.thenewstack.io/media/2025/08/05ea4655-image-10-1024x226.png)](https://cdn.thenewstack.io/media/2025/08/05ea4655-image-10-1024x226.png)

Note that it went to the lengths of finding out what visual effect the classes would have on the links.

It didn’t stop to ask permission for making changes — remember this was stated in the start screen. And we can see that all is now ship-shape:

[![](https://cdn.thenewstack.io/media/2025/08/7b32486d-0f11-429b-8173-bff8962795a4-1024x470.png)](https://cdn.thenewstack.io/media/2025/08/7b32486d-0f11-429b-8173-bff8962795a4-1024x470.png)

After this, I’d be confident in asking it to work on all the model views without interruption.

## Conclusion

There has been no attempt to tell me what costs have been used, either from Augment or via the model providers. In fact, I still don’t know what model was ever in use — Google tells me they use Claude 3.7 Sonnet in the main model — but this needs to be upfront, even if it is a brew.

Reporting usage stats should also be on by default. I couldn’t see how to change the permission model but — as I should repeat — this is technically still in closed beta, so there is plenty of time for a bit more structure to be added.

You can cycle through responses, but the single-line query box is not really what I want to write complex prompts in (that might include code).

What I did like was the sense that Augment is working a little harder to figure out your project, and how it works. From noting the number of backup files, to understanding that I was asking for a comparison between views, the responses were just a bit more intelligent. Speedy insight is what LLMs should be all about, and I think Augment gets this. I look forward to seeing how this progresses in what has been a busy year for Agentic CLI.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)