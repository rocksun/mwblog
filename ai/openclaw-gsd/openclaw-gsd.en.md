The speed at which ~~ClawdBot~~ ~~MoltBot~~ [OpenClaw](https://openclaw.ai/) climbed in popularity was quite phenomenal, and for good reason: It has an audience beyond the developer space, especially those who just want to experiment with digital assistance. Todays post continues my journey with GSD, but the LLM agent landscape is changing rapidly and this shooting star caught everyone’s eye.

At its core, OpenClaw is a locally hosted, open-source AI assistant that runs on your computer or server. You talk to it through apps you probably already use, like WhatsApp, Telegram, Discord, Slack, Signal, or even iMessage. And it really “does stuff” — sometimes *too* well. It is a gateway service that maintains WebSocket connections and includes a smart orchestration layer for working with LLM agents.

OpenClaw shows a strong technical focus on LLM agents; however, [its significant and varied security issues](https://thenewstack.io/openclaw-moltbot-security-concerns/) mean we must think more carefully about agent vulnerabilities before experimenting with them. But keep watching, even the odd sidetrack of the [AI church](https://thenewstack.io/moltbook-the-singularity-or-hype/) is genuinely intriguing. OpenClaw may be flawed, but it does show how laughably limited the available and entrenched digital assistants are compared to what agents can do. Now back to our scheduled program.

> OpenClaw may be flawed, but it does show how laughably limited the available and entrenched digital assistants are compared to what agents can do.

In my [first article on the popular Claude extension GSD](https://thenewstack.io/beating-the-rot-and-getting-stuff-done/), I set up a project to create a JSON viewer. GSD then asked many questions to create concrete plans before finally crunching a version 1 on its chosen platform, SwiftUI.

It had just presented its work when we stopped:

![](https://cdn.thenewstack.io/media/2026/02/f84309c7-image.png)

So first of all, let’s run the actual thing. I am following the advice carefully, as I am not a SwiftUI developer and I don’t use Xcode. Indeed, I had to get the update to 26.2 just to use it. I run it, and indeed it does what is described:

![](https://cdn.thenewstack.io/media/2026/02/ba988d48-image-1-1024x743.png)

So I approve the checkpoint. Yes, it’s just a titled window, but it tells me that all the assumptions are correct. It spends some time updating the roadmap and requirements.

And then we were ready for a second planning phase:

![](https://cdn.thenewstack.io/media/2026/02/b4e83275-image-2-1024x290.png)

Well, that percentage progress is creeping up. At the time, I thought it represented how close the project was to finishing.

I am running GSD within a [Warp](https://thenewstack.io/warp-goes-agentic-a-developer-walk-through-of-warp-2-0/) shell, but one downside of running in a single continuous session is that I can’t use Warp’s distinctive command-and-response blocks, which would give me the times of all the responses.

The phase goals and success criteria now roll into SwiftUI specifics, which I like. While I’m not a Mac developer, I can see that it is pulling in the common components it needs to operate:

![](https://cdn.thenewstack.io/media/2026/02/a264ff24-image-3-1024x360.png)

Despite my managerial role in this process, my developer head can follow the steps it is working through. After creating the plan, it executes it.

The human (that is, me) is now required again for verification – this time to check I can load a JSON file through the app:

![](https://cdn.thenewstack.io/media/2026/02/2f987125-image-4-1024x414.png)

I do indeed load a JSON file from my project with the expected Mac user interface, and it does count up all the objects within the file – and no more. I approve its progress in order to continue. Just before I do, I ask a quick question regarding token usage:

![](https://cdn.thenewstack.io/media/2026/02/60a07c42-image-5-1024x120.png)

Again, GSD wants my approval before continuing. I give it.

And finally, we hit my plan limit:

![](https://cdn.thenewstack.io/media/2026/02/60bb061e-image-6-1024x199.png)

So I clear the context window and attempt phase 3 again. Note the scary skull as the progress bar goes red.

![](https://cdn.thenewstack.io/media/2026/02/05da7359-image-7.png)

Anyway, now I know what that progress bar means! It resets when the window is clear. I also check my billing on the website. I am also warned that I am approaching my limit until the periodic reset:

![](https://cdn.thenewstack.io/media/2026/02/e1fb1424-image-8.png)

This is on the Pro plan, by the way. So I execute phase 3. For the record, here is the planning section:

![](https://cdn.thenewstack.io/media/2026/02/e5443f47-image-9-1024x350.png)

After waiting for my tokens to refill from the ~~magic fountain~~ Pro plan usage, we plough onwards. Now, GSD was working out how to implement a browsable list, bound to my JSON data.

Finally, GSD crunched a much more significant version, with much of the viewing capabilities apparently in place:

![](https://cdn.thenewstack.io/media/2026/02/0fcb2f10-image-10-1024x365.png)

And after firing up the app in Xcode, I can select objects at will from the JSON file I selected:

![](https://cdn.thenewstack.io/media/2026/02/8a309f39-image-11-1024x683.png)

For completion, here is the functional layout of the generated project within Xcode. The structure looks fine — and I’ve no problem continuing with this project. But we’ve gone far enough to prove GSD has what it takes to steer a development project without issue.

![](https://cdn.thenewstack.io/media/2026/02/9784efff-image-12-1024x356.png)

### Conclusion

While the GSD workflow uses a blizzard of organizational terminology — plans, requirements, phases, waves, checkpoints (they really didn’t leave any agile jargon behind) — I understand this is meant to tie everything together, retain “focus,” and put less pressure on the context window.

![](https://cdn.thenewstack.io/media/2026/02/e3124752-image-13.png)

And I was able to continue after running out of the window, running out of tokens, and the Mac having to restart. As I mentioned in the previous article, these restrictions are of their time — given the amount of global resources apparently now going towards AI infrastructure, I expect token costs to come down and the average context window to expand until it presents no restrictions. If I wanted to avoid the break between token refills, then I would have needed to upgrade my plan.

For a developer, seeing the project develop requirement by requirement is perfectly natural — but this might be slower than some imagined. For me, the value lies in pursuing a project whose language (SwiftUI) I can learn *after* seeing a working prototype. I feel GSD is a sensible route forward that I expect Anthropic will quietly absorb.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)