# Developer Review of Warp for Windows, an AI Terminal App
![Featued image for: Developer Review of Warp for Windows, an AI Terminal App](https://cdn.thenewstack.io/media/2025/03/287fd338-mathew-schwartz-sb7rurrmac4-unsplashb-1024x576.jpg)
While I have been [using the Warp terminal](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) on my MacBook for some time, there has always been one problem: it never had a Windows version.

While most tech these days is Linux-based, there are still a lot of Windows devices and services out there, which means that most software developers have to be ready to work with Windows. If you work across industry sectors, this is entirely unavoidable. As a game developer, for example, the PC remains a dominant platform.

So I’ve always wanted to have one terminal that can be used anywhere. Finally, [Warp for Windows has emerged](https://thenewstack.io/warp-launches-ai-first-native-terminal-app-for-windows/). And although it isn’t quite ready for prime time yet, it is already delivering the power of Warp’s modern editing to Windows.

My development Windows machine is an old AMD Phenom II processor box running Windows 10. Microsoft proudly tells me that as the machine is too old to run Windows 11, it will soon only be good for the scrap heap. But it happily runs all my development tools. Until today, it couldn’t run Warp, though, due to a well-known issue with the old chip (SSE4.1 compatibility). But I had expected it to work — after all, my machine also runs Fortnite.

The other issue with Windows is that the original command shell (CMD) is not supported by Warp, as it is too primitive to integrate with. But before we get into this, let’s first start up Warp for Windows.

You no longer need to sign in. I’ve already praised the fact that Warp is run as a company, but logging in had put a lot of people off. If you unreservedly ascribe evil to this activity, then you were probably not aligned to the Warp project anyway. But now, only a few extended tasks require login.

We open a tab to start a session, and then choose which shell to use. You can see that Warp recognises both PowerShell and my installed preference, which is the [Git Bash](https://gitforwindows.org/) shell. The Git Bash shell is a favourite with developers because it allows a proper integration of Unix-like commands for use with git. Unfortunately, that shell didn’t work for me, but it has for others and is fully supported by the team. On newer machines, you can also use Windows Subsystem for Linux (WSL) in Warp.

Most developers haven’t learned much PowerShell, as it is fairly obscure and ugly. However, it does have a few Unix aliases, which is nice. This leads us to how Warp uses AI. Like most developers, I have reservations about using Large Language Models (LLMs), but they are pretty useful in the option flag filled world of operating systems. Let’s see how that works.

For most Windows users, the ability to use Warp blocks that wrap commands and responses and allow full editing will be the biggest delight. For example, if I simply type `tree`
in a root directory, it puts the 38 seconds worth of lengthy response into a block, but doesn’t render the whole shell unusable:

I still think Warp has gone too all-in with AI, but in this example I wanted to do a bit more with `tree`
, so I used a prompt to talk in chat style to the LLM:

This is a slightly fake question, as `tree`
already shows directories but doesn’t print them. Note how the LLM (Claude Sonnet in this case) reasons with itself about what it could do and shows a response I could use. I can then run it, if I wish:

In fact, after running this it went on to correct itself and used a PowerShell script to do exactly what I asked, although I think it ran out of tokens doing so. Afterwards, I could go back to that block and apply commands with right click:

So I can search using “find within block” and in this example I just look for the sequence “time”:

This was all useful, as I have no wish to learn PowerShell. But Warp offers much simpler advantages — like suggested completions. In this example I call for help incorrectly, and Warp suggests what I actually need:

Similarly, while typing directories Warp intervenes intelligently to suggest the available alternatives:

These are the relatively simple things that a command shell should always have provided, and that Warp finally gives us.

As I mentioned when looking at [Ghostty](https://thenewstack.io/warp-vs-ghostty-which-terminal-app-meets-your-dev-needs/), controlling sessions with tabs is a major boon, and this works much as it does on my MacBook. For example, it is just a right click to rename or apply colours to tabs:

(Yes, that folder is from 2012)

[Warp Drive and Workflows](https://docs.warp.dev/features/warp-drive) I’ve covered before, but they are time investments into the Warp system that may well be worth making. These effectively allow you to name and store parameterised commands, and share them across a team. For example, sharing the same git statements across a team is a good idea:
This facility probably comes into its own for DevOps, when a number of team members of various skill levels need to run commands across a number of systems.

Unfortunately there are many configurations that count as a Windows PC, and it will take the Warp team more time to apply their full engineering expertise to this new old world. But given what they have already produced, I’m confident that Warp will successfully spread its advantages across the whole Windows platform fairly soon.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)