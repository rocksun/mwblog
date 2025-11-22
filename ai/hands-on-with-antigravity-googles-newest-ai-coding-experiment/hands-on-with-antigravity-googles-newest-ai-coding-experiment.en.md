When Google [launched a new agentic development platform](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/) called [Antgravity](https://antigravity.google/) this week**,** the first question I had was: “What about [Jules](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/) and [Gemini CLI](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/)?” But remember, this is Google; they throw a lot of mud against the wall just to see what sticks (very little is the answer, as their [graveyard](https://killedbygoogle.com/) attests). So Google considers Antigravity and Jules to be experiments that examine the same technology from different angles.

Let’s now look at Antigravity, which appears to be ready for “public preview” on all platforms, not just the Mac:

[![](https://cdn.thenewstack.io/media/2025/11/3a7f968e-image-1024x592.png)](https://cdn.thenewstack.io/media/2025/11/3a7f968e-image-1024x592.png)

Like [Verdent](https://thenewstack.io/first-look-at-verdent-an-autonomous-coding-agent-from-china/), it isn’t a CLI for the terminal — it’s an IDE app. So I downloaded it for my MacBook and slid it into the Applications folder.

## First Impressions and Setup Process

Sensibly, it asks the user to select a theme during setup. Most people set the theme once (dark or light) and rarely touch the option again:

[![](https://cdn.thenewstack.io/media/2025/11/0508b799-image-1-1024x630.png)](https://cdn.thenewstack.io/media/2025/11/0508b799-image-1-1024x630.png)

This next setup question is quite intriguing:

[![](https://cdn.thenewstack.io/media/2025/11/27969cec-image-2-1024x698.png)](https://cdn.thenewstack.io/media/2025/11/27969cec-image-2-1024x698.png)

This feels like it wants to possibly move towards a [parallel runner](https://thenewstack.io/a-hands-on-review-of-conductor-an-ai-parallel-runner-app/) model, with little human intervention (parallel runner means letting an agentic task run in the background while you start another — in other words, each task is run on isolated branches). Or perhaps Antigravity will be more like document-driven solutions like [Kiro](https://thenewstack.io/aws-kiro-testing-an-ai-ide-with-a-spec-driven-approach/). As you can guess, this post is just to set the scene for developers, not to deeply examine what is, after all, an experiment. So I’ll go with the “assisted development” option, which feels like more conventional territory.

After signing in with Google (using its internal 2FA), Antigravity asks you to open a folder or to clone. To create an isolated branch, like a parallel runner it would need a git clone. It also finds likely-looking projects in your user folder.

[![](https://cdn.thenewstack.io/media/2025/11/816f34bb-image-3-1024x674.png)](https://cdn.thenewstack.io/media/2025/11/816f34bb-image-3-1024x674.png)

As you see, I chose Claude Sonnet from the currently available models:

[![](https://cdn.thenewstack.io/media/2025/11/30653df3-image-4.png)](https://cdn.thenewstack.io/media/2025/11/30653df3-image-4.png)

## A Familiar IDE With AI-Powered Suggestions

As usual for releases such as this, you get a bunch of free tokens with the proviso that abuses will be curtailed. When it has finished initialising (scanning the project, I assume) we get the standard layout:

[![](https://cdn.thenewstack.io/media/2025/11/1d9a4f49-image-5-1024x676.png)](https://cdn.thenewstack.io/media/2025/11/1d9a4f49-image-5-1024x676.png)

Does this look familiar? Yes, it does seem to be some sort of VS Code fork. I’ve written about the [dangers of these](https://thenewstack.io/agentic-coding-and-the-weakness-of-extensions-for-ides/) — but really I don’t know why Google has done this.

On the right I chose “planning mode”; the alternative “fast” mode “is helpful for when speed is an important factor, and the task is simple enough that there is low worry of worse quality” — which is slightly comical, but we know what the writer means.

As far as I can tell, “Agent manager” is closer to the parallel runner agentic CLI mode, since you don’t interact with the editor. The following diagram refers to this:

[![](https://cdn.thenewstack.io/media/2025/11/ed731b89-image-6-1024x448.png)](https://cdn.thenewstack.io/media/2025/11/ed731b89-image-6-1024x448.png)

Having said that, the language used here is rather strange. The text below on the left confirms the parallel tasks model. But the text at the top mentions “Deep research,” which is an odd term to use for software development. Plus, the expectation now is that any task is “background” unless the user has asked for constant intervention. This does not feel like it was written in the same spirit of recent “agentic” code editor releases.

Looking at the Editor window first (right side of diagram), I get good quick code completion and suggestions. I select one of those awkward bits of project code that can be improved — a bounds checker.

```
public void CalculateMapBound(MapSector sec) { 
  Vector2 topleft = sec.GetAbsoluteTopLeft(); 
  Vector2 size = sec.GetSize(); 
  TagDebug.Log($"Topleft and size for sector {sec.Name} {topleft} {size}");

  if (topleft.x < leftbound) leftbound = topleft.x; 
  if (topleft.x + size.x > rightbound) rightbound = topleft.x + size.x; 
  if (topleft.y > topbound) topbound = topleft.y; 
  if (topleft.y - size.y < bottombound) bottombound = topleft.y - size.y; 
  TagDebug.Log($"Calculate bound for sector {sec.Name} {leftbound} {rightbound} {topbound} {bottombound}"); 
}
```

After selecting it, I’m given the chance to add it to the query, so we have:

[![](https://cdn.thenewstack.io/media/2025/11/02ea3bdd-image-7.png)](https://cdn.thenewstack.io/media/2025/11/02ea3bdd-image-7.png)

It suggested I use the Min/Max functions. Given I am not pushed for speed, this sounds right. The text in the chat box stated the changes and benefits, and I could accept the changes in context by the code:

[![](https://cdn.thenewstack.io/media/2025/11/34269420-image-8-1024x955.png)](https://cdn.thenewstack.io/media/2025/11/34269420-image-8-1024x955.png)

Of course, I’m not brave (or foolish) enough to try transplanting my whole build environment into an experimental app. But I will keep the changes and check them later.

## Exploring Antigravity’s Agentic Capabilities

So now let’s try the agentic side. Unfortunately, it doesn’t seem to work with independent branches (or doesn’t expect to work this way), so you can probably only work within the same workspace folder:

[![](https://cdn.thenewstack.io/media/2025/11/16153e1f-image-9.png)](https://cdn.thenewstack.io/media/2025/11/16153e1f-image-9.png)

I think a “conversation” maps to a task. I’ll ask it to improve another method that works with bounds. But it isn’t really designed to keep the task manager open, since it continually shuts it for space for the chat box and (for example) the changes view:

[![](https://cdn.thenewstack.io/media/2025/11/f2440c6e-image-10-1024x614.png)](https://cdn.thenewstack.io/media/2025/11/f2440c6e-image-10-1024x614.png)

One aspect I did like was the following statement:

[![](https://cdn.thenewstack.io/media/2025/11/59781264-image-11-1024x75.png)](https://cdn.thenewstack.io/media/2025/11/59781264-image-11-1024x75.png)

This proves it has contextual understanding of its last conversation and the resultant changes. And it is correct — Min/Max is neater (though I would expect it will be far slower).

So, looks like I should retract the idea that this was designed to work on parallel tasks in the same project — it clearly wasn’t. Perhaps Google is waiting for responses to see how they should react.

## Conclusion: An Experiment With an Unclear Direction

At this stage, I decided to stop as I don’t quite know what this product is truly going for. It is an app, but it appears to be partly a VS Code clone. It offers an Agent manager, but doesn’t really offer the parallel tasks I’d expect. But it manages to do what Gemini CLI does, or for that matter, what Jules does.

I recognise that Google creates projects from independent teams, and sometimes there are great ideas (I still remember [Google Wave](https://en.wikipedia.org/wiki/Google_Wave)) that Google as a company go on to ignore. But often they are misaligned with current trends. I’m going to wait until Google works out what they want to do with this before giving it a fresh look later in its development evolution.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)