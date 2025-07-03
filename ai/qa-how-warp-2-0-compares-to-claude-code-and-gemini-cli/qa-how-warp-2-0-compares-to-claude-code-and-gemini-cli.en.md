A couple of weeks ago, the [AI terminal app Warp](https://thenewstack.io/warp-launches-ai-first-native-terminal-app-for-windows/) released its [2.0 product](https://www.warp.dev/blog/reimagining-coding-agentic-development-environment), which it is calling an “Agentic Development Environment.” I will be reviewing this product shortly, but in the meantime, I carried out an email interview with Warp CEO [Zach Lloyd](https://www.linkedin.com/in/zachlloyd/). I’ve been a long-time fan (and user) of Warp, mainly because it is a great terminal available for every OS.

While AI assistance in the terminal is useful, it had seemed that with all the major LLMs competing to get into code editors, AI would eventually pull away from the command line — that is, until the [agentic era](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/) hit us. Warp seems well-placed to take advantage of agentic AI, since [Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/) resides in your aging terminal application. So I had plenty of questions for Zach.

**David: The very first thing I noticed about Warp 2.0 was that it now has its own code editor. I realise it’s just for quick and dirty hacking, but how strong was the wish in the team to create a code editor in Warp?**

**Zach:** Our philosophy is that coding by hand is going to become less common and go away entirely over time, but right now, there are definitely still times when you need to hop in and make manual changes.

The code editor in Warp isn’t designed for writing code from scratch. The main use case we’re focused on is human review of agent-written code. While most of the time people don’t need to use a code editor in Warp at all, when they do, we think there are two main ways for a human to intervene: one is by re-prompting the agent, and the other is by directly editing the code.

> “Our philosophy is that coding by hand is going to become less common and go away entirely over time.”  
> **– Zach Lloyd, Warp CEO**

So the goal with the editor is to make sure you don’t have to context-switch out of Warp just to make a small change. We want to take the editing functionality far enough that it’s usable and convenient within that workflow, without needing to jump into a separate IDE.

**David: It is amazingly sparse which is nice. How much functionality are you going to give it?**

**Zach:** You’re right that our editor is intentionally sparse. That’s by design. We’re not trying to recreate a full-featured IDE. But we do plan to add what we consider table-stakes functionality for basic editing: Things like formatting on save, linting, simple LSP support — just enough to make the experience smooth when you need it.

That said, we have a real advantage on the UI side compared to other tools in the space like [Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/), [Codex CLI](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/), or [Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/). Those products can’t build a WYSWYG editor at all — let alone a great code review experience.

**David: You have put LLMs in the faces of grumpy developers for some time, but even now people ask “Why do I need AI for a terminal?” Are you tempted to release a Warp Classic that removes the LLM aspect to leave a cleaner terminal?**

**Zach:** The solution we’ve landed on is pretty simple: there’s a single toggle in Warp’s settings where you can just turn AI off. It removes all AI features from Warp. We don’t think we need to make a totally separate app that’s just a terminal without AI, since it’s easy for users to disable it if they want to.

But personally, I really believe Warp is an incredible AI tool; and if you’re not using the AI features, you’re kind of handicapping yourself as a developer. We know not everyone sees that right away, so the real challenge for us is helping users reach that aha moment. Once they do, they usually don’t want to go back.

> “…if you’re not using the AI features, you’re kind of handicapping yourself as a developer.”

The most common way that happens is when someone hits an error in the terminal and Warp just fixes it for them — like your Python dependencies are messed up, or you’re stuck debugging a Docker issue, and Warp steps in and solves it. I want to keep giving even AI skeptics a chance to bump into those moments; because when they do, it can really change how they work.

**David: How are you going to maximize this ADE [Agentic Development Environment] moment before the LLM creators move the action back into the cloud?**

**Zach:** Yeah, this really feels like our moment. The zeitgeist is shifting toward terminal-based coding agents — a big move away from the traditional IDE. That’s because people are starting to get the value of the terminal interface. Whether it’s Warp’s ADE, Claude Code, Codex, Gemini CLI, or others, the idea of having a time-based log and an imperative interface — where you just tell the agent what you want and it does it — is emerging as the best way to work with AI.

That’s a much smoother experience than trying to use a side panel or chat window inside a VS Code clone. Those setups feel clunky by comparison and having the whole screen optimized for interacting with an agent just works better.

Since launching ADE, we’ve seen daily paid signups jump by about 5x — even accounting for discounts — so the traction is real.

> “…the idea of having a time-based log and an imperative interface — where you just tell the agent what you want and it does it — is emerging as the best way to work with AI.”

What’s wild is that most professional developers still haven’t changed their workflows — the people trying agentic tools today are mostly hobbyists, vibe coders, or AI early adopters. Our focus is on building for pros — developers working on real codebases — and giving them the right tools to manage, edit, and review agent-written code. That requires a much deeper interface than a typical terminal app can offer.

That’s why being the outer platform — with full control over the UI — is such an advantage. We’re really one-of-a-kind right now because we’re the only purpose-built agent platform that isn’t a VS Code clone or a CLI wrapper.

As for whether the action moves back to the cloud — if the question is whether we’ll support cloud-based agents like Devin or Factory, I think we probably will. But only if we can make the transition between local and remote feel seamless. That’s the bar we’re aiming for.

**David: It’s likely there will be an increased need for token use monitoring and process monitoring as agentic threads go wild. How do you plan to keep Warp’s UI advantage?**

**Zach:** Yes, we definitely have an advantage here because we have a really nice UX for managing agent multithreading.

As people start running more agents at once, costs can climb quickly. One big piece of feedback we’ve heard is that Warp can feel “token hungry,” so we have a major engineering effort underway to make it more efficient without sacrificing quality. This includes optimizing which models we use for different tasks and possibly raising limits, so users don’t hit them so fast.

> “As people start running more agents at once, costs can climb quickly.”

On the UI side, we have a big edge over CLI apps with a fully native agent management layer — including system notifications, in-tab updates, and a unified view to track all your agents. We’re going to keep pushing that further and make agent management an even more central, first-class part of the app. While the UI is still fairly minimal today, it already offers a much better way to see, control, and intervene — something only Warp can do given our place in the stack.

**David: Now that Warp works in Linux, Mac and Windows, are you slowly (or fast) losing your Mac-first startup mentality?**

**Zach:** Yes, we definitely try to be platform agnostic. Most of us started on Mac and still work on Mac daily, but we also have team members who use Warp on Windows and Linux every day.

I actually think we have a big advantage on Windows. Tools like Claude Code, Codex, and other CLI-based setups don’t really work in PowerShell as far as I know — you pretty much need WSL. So if you’re a Windows developer and you want to do agentic development without WSL, Warp is really the only great option. We definitely want to keep pushing to make Warp awesome across all platforms.

**David: Is Rust helping you keep the speed you want everywhere? I noticed that the new [Ladybird browser](https://thenewstack.io/ladybird-that-rare-breed-of-browser-based-on-web-standards/) has chosen Swift over Rust.**

**Zach:** Rust has been a pretty good choice. We looked at web tech with Electron early on, and I think there are basically two good options for cross-platform desktop development: Rust or Electron.

The big advantage of Electron is faster development time — no doubt about that. There are more libraries and a bigger ecosystem, so you have to rebuild less. We ultimately went with Rust, though, because we wanted higher performance and more control. Developing in a web sandbox can be a pain — with Rust, we get real threads, direct memory access, and much deeper system integration. You could probably do some of that with Electron, but it’s a lot more of a hassle. I also think Rust is just much faster overall.

> “We ultimately went with Rust […] because we wanted higher performance and more control.”

I don’t know much about Ladybird or why they chose Swift over Rust, but my understanding is that using Swift cross-platform is still kind of a research project rather than something production-ready. I think other teams have tried it, but it hasn’t really taken off yet. So, for us, picking something truly built for cross-platform like Rust just made more sense.

**David: MCP seems like a natural outlet for Warp, but so far it still feels experimental on most platforms — and a little awkward. In terms of control and UI, is Warp jumping on MCP or waiting to see how it catches on?**

**Zach:** I’ve hooked up our crash reporting, Sentry, to Notion, and it lets me do things like tell Warp, “Hey, fix this Linear issue,” and just paste in a Linear link, or “Help me debug this server crash,” and paste in a Sentry link.

We’re fully leaning into MCP. Where it really shines for Warp is when CLI integrations don’t exist. One of the powerful things about being at the terminal layer is that our first choice is always: is there a CLI tool that can gather the context? If there is, we’ll call that since it’s faster and more native.

For example, we’re not going to use a Git MCP server when we can just run a Git command, and we’ll always prefer the GitHub CLI over using the GitHub MCP server. Basically, if there’s a good CLI, we’ll use it.

But for a lot of tools, there isn’t a solid CLI — tools like Notion or Linear are great examples. For those, having a super easy MCP integration really opens up a lot of context.

We’re definitely jumping on MCP. We’re investing heavily to make it easier to install, easier to share, and easier to debug.

## A Final Note From David

Whether you are onboard with LLMs assisting development or not (and as Zach says, many professional developers have absolutely not changed their workflows), Zach’s insights should help you see why agentic developers will receive plenty of love from the professional tool community in the future.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)