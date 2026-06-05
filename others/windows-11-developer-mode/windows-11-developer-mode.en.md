At its Build developer conference on Tuesday, Microsoft is launching so many new features for developers, it’s hard to keep up.

But the most important one is pretty straightforward: dark mode — and it’s on by default.

This is part of a new, developer-optimized Windows 11 experience that quiets down the operating system and turns off widgets, notifications, and in-product recommendations, with more than 30 settings retuned for how developers work. The point is to get out of the way (and even if you are *not* a developer, turning off most of these features makes Windows 11 better anyway).

[Jatinder Mann](https://www.linkedin.com/in/jatinder-mann/), partner director of product management at Microsoft, told *The New Stack* in an interview ahead of the conference that this is all about listening to developers.

“Before anything agentic or AI, developers just want a clean, fast, distraction-free dev environment where they can jump in, stay in the flow, ship faster,“ he says. What developers want, he says, is for Microsoft to make Windows 11 “snappy, make it calm, make it resource sensitive and respect that muscle memory I have.”

## Microsoft is clearly trying to get developers to switch

That muscle memory, of course, would come from years of using Macs and Linux machines, since Microsoft is clearly trying to get developers to switch away from those operating systems.

> “We know developers want to make the environment their own.” Jatinder Mann, Microsoft.

When we asked him if this is Microsoft playing offense or defense, courting new developers or winning back the ones who left for other operating systems, Mann didn’t take the bait. “It’s really listening to feedback — how do we land the best possible experience for customers?”

## What’s in the box

The configuration bundles defaults rather than introducing a new product. It pre-configures VS Code, GitHub Copilot, WSL, and PowerShell 7, and pre-installs PowerToys, [Oh My Posh](https://ohmyposh.dev/), and [Nerd Fonts](https://www.nerdfonts.com).

File extensions are visible, hidden files are shown, and Git version control lives in File Explorer. The taskbar can finally sit on the left, right, or bottom of the screen (yay!).

“We know developers want to make the environment their own,” says Mann.

Developers can get this experience in three ways: pre-installed on new OEM dev boxes, as a developer-optimized image for a Windows 365 Cloud PC, or as a downloadable configuration script that runs on any existing Windows 11 machine. It’s also bundled into PowerToys. The settings apply per user, the way setting up your own profile would, not across the whole machine.

## The Mac and Linux tell

There are a few other major new features that show how Microsoft is trying to persuade Mac and Linux developers to love Windows.

Microsoft is adding 75 Unix core utilities that run natively in PowerShell, rather than only inside WSL, built as a port of uutils, a cross-platform reimplementation of GNU Coreutils in Rust.

“If you type grep, ls, touch in PowerShell, it just works now. No more jarring reminders that you’re in a different OS,” Mann explains.

For those developers who spend a lot of time in the [Windows Subsystem for Linux](https://thenewstack.io/how-to-install-windows-subsystem-for-linux-on-windows-11/) (WSL), there is now also a new set of setup scripts that brings tools like starship, homebrew, zsh, and others to Windows.

WSL itself, which Microsoft open-sourced at Build 2025, is also getting a containers feature: a built-in CLI and API for spinning up Linux containers on Windows without third-party tooling.

“Windows should just feel familiar, feel like home, regardless of where you came from,” Mann says.

## Staying in the flow: the Intelligent Terminal

Maybe the most interesting part of this new developer experience in Windows is the experimental Intelligent Terminal that drops a coding agent directly into the shell.

“You’re in terminal, you hit an error, you copy it, you switch to your chat window with your favorite agent, you paste it, explain the context, get an answer, and you switch back,” he says. “That feels broken.”

Intelligent Terminal builds on the existing Windows Terminal by adding an agent pane that tracks the shell’s live state. When a command fails, it surfaces the context and suggests a fix the developer can run. Developers choose the agent, including Claude Code, OpenAI’s Codex or Copilot (or turn this feature off).

If this sounds familiar, it’s likely because you’ve been using Warp. While Warp itself is free to use, it meters its users’ AI usage, with a paid tier starting at $20 a month. Microsoft is shipping its version for free, and somewhat unfinished. “We’re shipping this as an experimental branch on purpose,” Mann says. “We want devs to co-author the design with us.”

## The other bet: Windows as the place to run agents

No announcement these days is complete without mentioning AI agents, and at Build, Microsoft is extending its existing work to make Windows a platform for agents to run on.

“We want to make sure Windows is the best place to build and run agents, so you can run them safely, securely, with confidence,” Mann says.

The marquee feature here is Microsoft Execution Containers (MXC), a policy-driven layer that lets developers declare what an agent can touch (say files, network, processes) and enforces those boundaries at runtime. MXC offers a spectrum of isolation, Mann explains, from process-level for lightweight actions up to full virtual machines and, at the far end, a separately managed Cloud PC.

Windows also assigns each agent a local ID or a cloud-provisioned Microsoft Entra ID and attributes its activity to that ID, so a developer can tell human from agent and audit every file and network call. OpenClaw may be the agentic tool that needs the most security constraints, and Microsoft worked with the team to make the agent runtime run natively on Windows inside an MXC container.

For developers building Windows apps, Windows Development Skills provide a coding agent with structured context for building a native Windows app, from WinUI 3 to packaging and identity. Since these are standard skills.md files, they will work with any agent and, as Mann notes, will allow them to work in a more token-efficient way.

## “Unmetered intelligence” on Windows

The cheapest tokens, of course, are those generated by local models. That’s something Microsoft is also focusing on with Windows: “How do we help make every Windows machine a token factory on your desk?” asks Mann.

To make Windows a better surface for apps that could benefit from local AI features, Microsoft is expanding its Windows AI APIs beyond the NPUs in Copilot+ PCs — which always seemed like a weird limitation — to CPUs and GPUs. It is adding an on-device speech recognition API and bringing its small-language-model-based inbox to more hardware. What the GPU requirements are, however, remains unclear.

There are also two new on-device models: Aion 1.0 Instruct is a smaller, faster successor to the current Windows SLM, and will be available with [open weights on Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) in July.

There is also Aion 1.0 Plan, a 14-billion-parameter reasoning and tool-calling model with a 32K context window that will ship as part of Windows. This model is built to run agentic workflows entirely on the device. Currently, you need 9 GB of disk space to install Windows 11. A 14-billion-parameter model will likely take up just as much (depending on the quantization). It’ll be interesting to see what the hardware requirements are for running this model, given that few Windows users will have a GPU with enough memory.

## Is Microsoft finally listening?

For Mann, though, it all comes back to giving users what they want. “Almost every single item here has come from some customer asking,” he says.

That’s good to hear, given that Microsoft has long been criticized for doing the exact opposite. Users have complained about Copilot AI features being force-fed through OS updates, the lack of UI customization options, and more.

Listening is one thing, though. Taking action based on what you hear is another. It seems like Microsoft is now sufficiently spooked to actually make significant changes to Windows 11.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)