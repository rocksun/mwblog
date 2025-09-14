I started using Warp as my default terminal some time ago, as it has useful tools — for example, time to run a shell command. Other products give you controllable tabbed terminals, but because Warp has written the UI from the ground up with Rust, it has a speed and intentional design that is impressive. Since then, Warp has gone big-time into LLM integration. Originally, I had little interest in that move until the “agentic era” started.

With agentic CLIs, suddenly the LLM has stepped away from the IDE, [towards the humble terminal](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/) — right onto Warp’s patch.

To summarise what Warp Code offers, think of the different views you need to do simple tasks: file view, editor, diffs, etc. Now Warp gives those to you while coding with the LLM. Older developers will remember that guy or gal who can “do everything from Emacs”. Warp Code is moving in that direction, which we’ll talk about in an interview with Warp CEO Zach Lloyd below.

## The Warp Code Changes

Starting with the familiar tabbed screen that we looked at in [my review of Warp 2.0](https://thenewstack.io/warp-goes-agentic-a-developer-walk-through-of-warp-2-0/), we can see some new work already. At the top left, we have three new icons: </>, a magnifying glass, and a +/- sign.

This is access to the file tree, file search and changes view.

The query window at the bottom is slightly busier, with the terminal icon selected in blue (so Warp will interpret text as strictly OS commands) and we can see some extensive git commit stats and which model we are working with:

[![](https://cdn.thenewstack.io/media/2025/09/f1f41d23-image-2.png)](https://cdn.thenewstack.io/media/2025/09/f1f41d23-image-2.png)

I’m going to continue using my simple Rails app for creating conversations, which I also used in my review of [Augment CLI or “Auggie”](https://thenewstack.io/developer-walk-through-of-auggie-cli-an-agentic-terminal-app/). As before, we simply want to introduce more Bootstrap into one of the views.

Let’s start with a formal codebase indexing. We switch to “agent mode” and use the “/init” command, as we have in other Agent CLIs, to perform the same operation:

[![](https://cdn.thenewstack.io/media/2025/09/ac66bf2c-image-3.png)](https://cdn.thenewstack.io/media/2025/09/ac66bf2c-image-3.png)

This is a more formal recognition of indexing, and I’ll let it start. It also invites me to start a WARP.md file. I can also instruct the agent directly with new Agent Profiles.

It takes time to go through this, then it allows me to inspect the WARP.md file, which collects a few of the important command tools for future use:

[![](https://cdn.thenewstack.io/media/2025/09/e15f3e6e-image-4-862x1024.png)](https://cdn.thenewstack.io/media/2025/09/e15f3e6e-image-4-862x1024.png)

## Working Through a Query

Let’s ask Warp if it can enhance one more Rails view with Bootstrap.

Looking at my app running, the Rails view of the Voices model uses nice Bootstrap buttons:

[![](https://cdn.thenewstack.io/media/2025/09/aa5a8056-image-5-1024x393.png)](https://cdn.thenewstack.io/media/2025/09/aa5a8056-image-5-1024x393.png)

But the equivalent Archetypes view does not:

[![](https://cdn.thenewstack.io/media/2025/09/045f3dca-image-6-1024x410.png)](https://cdn.thenewstack.io/media/2025/09/045f3dca-image-6-1024x410.png)

We don’t need to know anything about the models or indeed what these represent — we just need to ask Warp to change the archetype view. We could simply describe the class, but we can do better.

First we’ll use the file tree (on the left) to select the good example view, so we can refer to the file directly in the query. Note that the selected file view fills the right pane:

[![](https://cdn.thenewstack.io/media/2025/09/e92c83a2-image-7-1024x561.png)](https://cdn.thenewstack.io/media/2025/09/e92c83a2-image-7-1024x561.png)

To supply what is called “agent context,” we can use the “@” symbol to specifically reference the two files. Let’s look at the query I used during the [Auggie review](https://thenewstack.io/developer-walk-through-of-auggie-cli-an-agentic-terminal-app/):

*“change the view file app/views/voices/show.html.erb so that it uses Bootstrap classes, using app/views/tags/show.html.erb as an example”*

So apart from the different example and target, using the @ symbol I can create the query for Warp:

[![](https://cdn.thenewstack.io/media/2025/09/c0b6ee68-image-8-1024x429.png)](https://cdn.thenewstack.io/media/2025/09/c0b6ee68-image-8-1024x429.png)

This allows me to capture the files directly, which happen to have the same name in Rails, just different view folders:

[![](https://cdn.thenewstack.io/media/2025/09/0a3b6ddb-image-9-1024x254.png)](https://cdn.thenewstack.io/media/2025/09/0a3b6ddb-image-9-1024x254.png)

Let’s go with that. We get the usual diff view, which we can accept or reject:

[![](https://cdn.thenewstack.io/media/2025/09/32950165-image-10-1024x479.png)](https://cdn.thenewstack.io/media/2025/09/32950165-image-10-1024x479.png)

Remember we have the “view changes” button, so we can come back to this any time. In fact, I can even see the git changes from the previous query I made for the Auggie review. (These take quite a few seconds to load at the moment.)

To wrap it all up, let’s just refresh the page on my app to confirm we are good:

[![](https://cdn.thenewstack.io/media/2025/09/e4dd5a40-image-11-1024x427.png)](https://cdn.thenewstack.io/media/2025/09/e4dd5a40-image-11-1024x427.png)

## The Direction of Warp

I’ve only touched on the new stuff in my review, but because Warp Code represents more of a breakout towards what Warp has described as the “Agentic Development Environment” (ADE) as opposed to a specific improvement in the mechanics of LLMs, I asked [Zach Lloyd](https://www.linkedin.com/in/zachlloyd/) (Warp CEO) some questions to help see where this is all going.

---

**David Eastman: I think Warp is now peculiarly vulnerable because you are moving into new (if familiar) territory. Other Agentic CLI products simply don’t have enough control right now over the shell/terminal to come very close to what you are doing with views. How are you going to pull the coding Overton window towards Warp?**

**Zach Lloyd:** The UI features and what we can do at the view level is a huge differentiator, because we can build a different type of developer experience than a purely CLI-based tool that’s only able to output text and can’t take any mouse input.

Everyone else is retrofitting AI into their app, whether it’s a chat bar in VS Code or a CLI app. What we’re trying to design is what the UI should be for working with agents. As people see that they can have something that feels like a CLI-based agent, but lets them edit the output or review diffs like they’re reviewing a PR in GitHub, we’re going to get the primitives right in a way that’s very hard for apps with other UI constraints to do.

**DE: In a related question, are you hoping that other products try to develop or extend the shell itself, so you at least have common marketing ground with the competition?**

ZL: I’m a little split on this one. On one hand, we want ADEs to become a category, which is already kind of happening. If you look at Conductor, it’s probably the best other example of people building UIs on top of Claude Code.

Whether we want it or not, what’s actually happening is that the competition is already moving towards us. If you look at Cursor, for instance, they’re slowly stripping away a lot of the editing features and building something that looks a lot more like Warp.

**DE: Given the heavy AI integration with Warp, are you just going to leave the basic tabbed shells to Ghostty, et al?**

ZL: I’m still cool with people who want to just use Warp as a terminal, although our product focus has definitely moved away from that. There are threads online about this, where people are a little frustrated that we’re adding AI and they just want to use our terminal features, like the rich text editor and block output.

We’ve talked internally about not just making a “turn off AI” mode, but making a basic terminal mode or Warp Classic as a new binary. I still think it’s unlikely we’ll do two binaries, but I do think it’s quite possible that we’ll do something as part of the onboarding experience — just “I’m here for the terminal and I don’t like AI.” But overall, that’s really not our focus moving forward.

**DE: You are clearly gunning for the modern version of the 90s Emacs or Vim, where the developer sets up their preferred layout and then lives in that setup for the whole time. Are you going to try to set up some community “plugin” development to support other views (e.g., git branch trees, etc)?**

This is an awesome idea. I’ve never quite thought of it that way. If you look at the history of how these things evolved, I remember working in Emacs where I would have everything — a file tree, code editor, everything — all in Emacs. People do the same thing in Vim. The evolution went from those to IDEs, and I think it’s fair to say that now Warp is trying to continue that evolution with the ADE.

An ecosystem around it where people can plug in at the view layer is a super cool idea. I can’t really say in all honesty that we’re building it right this second, just because we have so many other things that we’re working on. But I actually love that idea and think it’s a smart place for us to invest in making Warp, the app itself, more accessible.

**DE: To get into the position to have the backend control and the fast windowing, you have obviously worked hard on the Rust windowing control primitives. Is that now a separate sub-team within the Warp team? For those looking to hand you a CV, what do you look for?**

The UI framework that we have, which is what we call the windowing primitives and the rendering engine, is pretty stable at this point.

The general policy that we’ve always had at Warp with respect to building features is that you build them end-to-end. So if you are building a feature that touches AI, for instance, you are building the UI for it, you’re building the prompting, and you’re building the evals — you’re responsible for the overall end-user experience.

When someone wants to come work at Warp, what I’m looking for is general problem-solving and CS skills and aptitude — someone who’s really smart, cares about what we’re building, wants to help developers, and is very product-focused. Meaning they have the ability to, when they’re building something, not just nerd out on the code, but always focus on: why am I building this thing? How should the feature work? Is it solving the end-user’s problem?

Some things we don’t look for: specific language knowledge, Rust experts, and heavy terminal users. We’re looking for people who want to help developers ship software more quickly.

## David’s Conclusion

Warp is both defining its new Agentic Development Environment strategy, as well as competing in the new Agentic Era. Warp Code uses flexible views to get it nearer to that Emacs feel of a highly integrated system suitable for long-term development.

My feeling is that not only does Warp have the right technical background to deliver this, it is the right innovation to help move Agentic CLIs into deeper maturity.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)