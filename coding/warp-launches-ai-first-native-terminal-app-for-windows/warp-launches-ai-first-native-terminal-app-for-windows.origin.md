# Warp Launches AI-First Native Terminal App for Windows
![Featued image for: Warp Launches AI-First Native Terminal App for Windows](https://cdn.thenewstack.io/media/2025/02/693db2de-warp-windows-feature-feb25-1024x576.jpg)
Warp, the command-line terminal app built for AI, has finally arrived on Windows. Previously it was available only on macOS and Linux, but today’s launch significantly broadens its potential user base.

I spoke with Warp’s founder and CEO, [Zach Lloyd](https://www.linkedin.com/in/zachlloyd/), about the news. We also discuss how [Warp](https://www.warp.dev/) is positioning itself among the raft of AI coding tools that have hit the market recently. It turns out, Lloyd has big plans — he thinks Warp can be “the next generation of AI tooling.”

Lloyd firstly noted that Warp is “a totally native app, so it’s not an Electron app [and] it’s not a VS Code clone.”

“This is, I think, the first time on Windows that people are getting a 100% native AI-first developer tool,” he said. “I think that’s a really big deal. Windows is the biggest developer platform, so I think that’s also important. This has been our number one feature request.”

## How Warp on Windows Was Built
Warp was originally built using Rust and Lloyd noted that 90-95% of the core code in the Windows version is the same as in the macOS and Linux versions. Where it differs is the code that involves integrating with the Windows system.

“It’s pretty similar to the experience you get on Mac and on Linux,” said Lloyd, “with the biggest difference being that it supports PowerShell, it supports Git Bash, [and] it has WSL support if you want to use the Windows subsystem for Linux.” (note: these are all shell programs, a type of program that allows users to interact with an operating system by typing commands.)

Lloyd noted that it took “a bunch of time” to make Warp “seamlessly interface with all those things in a similar way to what Windows Terminal does, where you can start sessions in different shell environments.”

“We do all of our own graphics calls; we have to integrate with graphics drivers on Windows and the event handling, and all that stuff,” said Lloyd. It also integrates with the Windows Package Manager, WinGet.

“We’ve been working with the Windows terminal team and people on various engineering teams to make sure the product is awesome for Windows developers,” Lloyd added.

## Why Swap Terminals?
Many Windows developers use the default Windows Terminal as their command line interface, or they might use the built-in terminal in Visual Studio Code. So I asked Lloyd what will be the pitch to those developers to switch to Warp?

He first mentioned the “really powerful AI integration” in Warp as a reason for adopting Warp.

“In Warp, you can enter ‘command’ and use it like a regular terminal, so it’s a totally backwards-compatible terminal. But you also can just instruct or prompt the terminal what you want it to do in English. And so if you’re […] setting up a new project, if you’re trying to debug a production issue, if you want to code-build a feature, you can simply tell Warp in natural language — like, hey, this is what I want to do — and then with varying degrees of autonomy, and the ability to gather context by running terminal commands, Warp will do it for you.”

Lloyd noted that AI integration is increasingly the main value proposition for new users. But he says that Warp also has “a different, reimagined user experience compared to a normal terminal.”

“…in Warp’s terminal, the input editor works like you’re in an IDE.”

– Zach Lloyd, Warp CEO
“In a normal terminal, very basic interactions feel very weird to a lot of users,” he said. “So, for instance, you can’t click and put the mouse cursor someplace in a normal terminal. And in Warp’s terminal, the input editor works like you’re in an IDE or something. It’s a real code editor. You have real selection support; you get auto-complete, you get syntax highlighting — all that stuff. So the input is much nicer.”

As well as the input, Warp’s **output** is also different from a normal terminal. Lloyd said that it’s structured output, “almost like you’re using a notebook or something.” This enables richer functionality within the Warp terminal — Lloyd gave the examples of attaching AI context, or filtering through past commands, or sharing what you do with teammates.

Warp also has a built-in knowledge store, he said, enabling a team of developers to store and share templated terminal commands.

Overall, Lloyd said that Warp “should be a drop-in replacement” for Windows Terminal. “There shouldn’t be any sort of step back for someone who’s coming from that experience, but it should be a very, very significant upgrade as well.”

## Terminal Apps As AI Dev Tool
Terminal apps have become a surprisingly vibrant category of dev tools over the past couple of years, especially with the emergence of AI. Two of The New Stack’s resident tutorial writers have provided reviews of Warp — David Eastman tested the [macOS version](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) and concluded that Warp “gives you the kind of IDE on your command line that you often assumed you would have, but you’ve never really had”; while Jack Wallen tried the [Linux version](https://thenewstack.io/warp-is-a-power-users-dream-terminal-for-linux/) and called it “a power user’s dream terminal.”

But we’ve also seen a bunch of new [AI coding tools](https://thenewstack.io/self-driving-software-solver-launches-autonomous-ai-coder/) come onto the market recently, with some — like [Bolt](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/), [Windsurf](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/) and Lovable — claiming to be [agentic IDEs](https://thenewstack.io/beyond-dx-developers-must-now-learn-agent-experience-ax/) capable of creating an entire app from scratch. And just this week, Google released an AI coding tool that [offers 90 times more code completions](https://thenewstack.io/google-ai-coding-tool-now-free-with-90x-copilots-output/) than its main competitor, GitHub Copilot.

“…we want to lean into our strengths where the terminal really shines […] The terminal is much more of a pro developer tool.”

– Lloyd
Given all this AI coding tool activity, I asked Lloyd how Warp fits into this already crowded landscape.

“I think that we want to lean into our strengths where the terminal really shines,” he replied. “What’s great about Bolt is that you can do it all in a web app, and you really don’t need to be a developer at all. The terminal is much more of a pro developer tool.”

That said, thanks to AI, he does see Warp expanding to do a lot more code generation — which hasn’t traditionally been the domain of terminals.

“You can in Warp, increasingly, have Warp write code,” said Lloyd. “It can create projects, it can debug errors. The really cool thing, though, is because of where we sit in the stack, it can do it across projects — which is really nice.”

He added that code deployment to production is more natural within a terminal, as is project setup.

“Our goal is to be the most productive interface for developers who want to work with AI.”

– Lloyd
“Our goal really is to be the most productive interface for developers who want to work with AI, whether it’s coding or other use cases.”

His argument is that because a terminal is a natural interface for pro developers (even though it’s confusing to most other people), it can become their default chat interface with AI.

“I think development is going to look less like people opening up a bunch of files and making code edits,” Lloyd said. “I think it’s going to look like […] people starting with: hey, here’s what I want to accomplish, let me work with you to accomplish it.”

He notes that AI is already good at code generation, but it will get “stuck” from time to time. So there will always be a need for a human developer to interact with the AI.

“And so I think what you want is […] an interface where it’s very easy for the developer, in a natural tool for them, to hop in and sort of correct what the AI is doing. I think that’s the direction things are going.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)