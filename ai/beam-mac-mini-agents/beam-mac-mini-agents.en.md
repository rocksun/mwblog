[Beam](https://beam.win) is a new Mac app that takes a window running on one Mac and puts it on another, where it behaves like a locally installed app. Why? Agents.

Serial founder [Hiten Shah](https://www.linkedin.com/in/hnshah/), who co-founded Crazy Egg and KISSmetrics, built it with Sam Asante under a company called Noats. It launched on Product Hunt on Tuesday and is aimed at the headless Mac Mini sitting in a closet running AI agents.

The pitch is great: Instead of opening Screen Sharing and steering a full remote desktop, a user picks a single window on the other machine, say a Terminal session or a browser window an agent is working in, and it opens alongside everything else on the Mac in front of them. It gets its own Dock icon and can be called using the `Command+Tab` switcher. Resizing the window resizes the window on the other Mac. Keyboard shortcuts work, files can be dragged across, and the app’s audio can play locally. The app itself never leaves the original machine. When one window isn’t enough, Beam can pull over a full display or the whole Mac.

Shah frames it around his own setup in his [Product Hunt launch post](https://www.producthunt.com/products/beam-win), describing Macs running agents and local models “with work continuing even when nobody’s sitting in front of them.” Getting to one of those machines usually means Screen Sharing and a second desktop to navigate. Beam is meant to cut that down to the one window that matters.

**Beam plays into the exploding ecosystem of Macs powering AI systems**, so the app runs only on macOS. And both Macs need Apple Silicon, macOS Sonoma or later, and Beam installed. The machines find each other on the same Wi-Fi network, or anywhere through Tailscale.

The company says windows, keystrokes, clipboard, and audio travel directly between Macs, encrypted, and never pass through its servers. It also says hidden windows and password managers never show up in the window picker.

For devices without Beam, a share link opens a single window in any browser, view-only unless control is granted, and expires after anywhere from an hour to a week.

Asante said on Product Hunt that native iOS and Android apps are on the way.

Pricing depends on the setup. Hosting a Mac and joining a share link are free. Using your own Mac is free for 20 minutes a day, then $12 a month, $84 a year, or $199 for a lifetime license.

Beam follows where agents’ hardware is growing. The Mac Mini is becoming the default home for always-on agents, driven initially by OpenClaw, but others like Perplexity followed. Apple credited agentic workloads on its April earnings call.

*The New Stack*‘s Janakiram MSV caught the trend early and covered the shift in May, writing, [“the Mac mini just became infrastructure.”](https://thenewstack.io/mac-mini-agent-infrastructure/)

Beam isn’t the first to this problem. I used Astropad’s Workbench for a few weeks, and it let me remotely access agents on my desktop and through iOS apps. Workbench bets on mobile devices, while Beam bets that the unit of remote access should be the window, not the screen. Jump Desktop, Screens and Apple’s own Screen Sharing all cover the basics too.

Still, the problem is real and growing. The Mac stashed in a closet or on a rack is becoming a normal part of a developer’s setup. Beam’s answer is to stop treating it like a second desktop at all.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)