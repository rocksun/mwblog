LONDON — [Craig Loewen](https://www.linkedin.com/in/craig-loewen), Microsoft’s senior product manager in charge of [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/about), and [Clint Rutkas](https://www.linkedin.com/in/clintrutkas), principal product manager lead who oversees WSL, at [Canonical](https://canonical.com/)‘s [Ubuntu 25.10 Summit](https://ubuntu.com/summit) told the tale for the first time of how [WSL was finally open sourced](https://thenewstack.io/the-windows-subsystem-for-linux-is-now-open-source/). It was a long, strange trip.

## The Origins of WSL in Project Astoria

You see, WSL’s story began back in 2010 with [Project Astoria](https://trungnt2910.com/astoria-windows-android/), aka Windows Bridge for Android. This stillborn project was intended to enable people to run Android apps on Windows Phone via a translation layer in the Windows 10 Mobile kernel. Since you’re unlikely to have a working Windows Phone in your pocket, you know how that turned out.

The initial prototype translated [Linux system calls](https://thenewstack.io/introduction-to-linux-operating-system/) into Windows NT kernel calls, laying the groundwork for the [2016 launch of Bash and Ubuntu on Windows](https://www.zdnet.com/article/ubuntu-not-linux-on-windows-how-it-works/). This initial effort, which Canonical helped build, recompiled [Cygwin’s open source utilities](https://www.cygwin.com/) to run natively on Windows. Dustin Kirkland, then a member of Canonical’s Ubuntu Product and Strategy team, explained, “We’re talking about bit-for-bit, checksum-for-checksum [Ubuntu ELF binaries running directly in Windows](https://www.zdnet.com/article/ubuntu-not-linux-on-windows-how-it-works/).”

## The First Iteration: The WSL 1.0 Compatibility Layer

At the time, Kirkland said, “A team of sharp developers at Microsoft [had] been hard at work adapting some Microsoft Research technology to basically perform real time translation of Linux syscalls into Windows OS syscalls. Linux geeks can think of it as sort of the inverse of [WINE,](https://www.winehq.org/) [the open source program that enables people to run Windows programs on Linux] — Ubuntu binaries running natively in Windows.”

This was the predecessor of [WSL 1.0](https://www.zdnet.com/article/windows-subsystem-for-linux-graduates-in-windows-10-fall-creators-update/). This was a compatibility layer that enabled people to run Linux distributions, such as Ubuntu, openSUSE and Fedora, by translating Linux system calls into Windows NT kernel calls, using a mechanism called “[pico processes](https://learn.microsoft.com/en-us/archive/blogs/wsl/pico-process-overview).” It was released in 2017 as part of the Windows 10 Fall Creators Update.

## A New Approach: The Rise of WSL 2 and its Popularity

Users, who were primarily developers, liked it, but they all reported that WSL 1.0 was slow. So, Microsoft backed off, looked it over and tried a new way to run Linux and its applications. The team decided to [develop their own Linux kernel](https://www.zdnet.com/article/hell-freezing-over-microsoft-releases-its-own-linux-for-windows/). Thus, WSL 2 took a fundamentally different approach. Instead of emulation, WSL 2 uses a lightweight managed virtual machine (VM) to run the Microsoft Linux kernel, which is updated via Windows Update.

This version became extremely popular among developers, particularly after its stable release in May 2020. [Millions of users adopted it for programming, system administration and cloud engineering workflows](https://ubuntu.com/blog/wsl-ubuntu-2022-year-in-review). Its popularity accelerated between 2021 and 2023, with the percentage of developers using WSL as their primary operating system growing nearly fivefold in a single year, from 3% to over 14% according to the [Stack Overflow Developer Survey of 2022](https://survey.stackoverflow.co/2022).

## The Internal Push to Open Source WSL at Microsoft

Within Microsoft, WSL’s developers began to push to open source WSL 2.0. As Loewen said, it only made sense. After all, “Linux is open source, right? And we are working on a Linux product that brings Linux to the Windows operating system. We want it to be integrated with what the community is and be where the community is. It makes sense we’re there. And so that’s business value, embracing the community.”

Loewen added, “It couldn’t have happened any earlier “because WSL was initially so tightly coupled to the Windows kernel that we couldn’t open source it. Even if we wanted to, we wouldn’t be allowed to. And then over time, we started doing it, because we were like, ‘This needs to be open source!’ So we started removing all of the private calls, decoupling everything, and that’s what let us get to where we are.”

## Overcoming Challenges to Decouple WSL from Windows

This took a long time. Loewen said, “Years were spent decoupling private APIs and refactoring long-standing dependencies, allowing Microsoft to eventually publish the full code responsible for WSL.”

The push to open source WSL internally in Microsoft involved three main strategies: celebrating community involvement, demonstrating business value and thoroughly evaluating both benefits and costs. Internally, the team argued that open sourcing WSL dovetailed with Microsoft’s broader strategy of supporting developer tool users. Linux, being open source by nature, requires a community-centric approach for user trust and effective evolution in the Windows environment.

It was a hard slog at times. Rutkas acknowledged that “open sourcing is rewarding, but it takes time and effort. You must convince your stakeholders.”

## The Immediate Success of an Open Source WSL

Once done, though, it was a smashing success. Rutkas said, “As soon as we open sourced, it went from 15,000 stars to 30,000 plus stars on GitHub. So that was good — and that was in one day. It skyrocketed. It was on [Hacker News](https://news.ycombinator.com/), where it was the number one post for, I think, 24 hours, which is unheard of. So, we knew we made the right move.”

This transition reinforced that not all technologies need to be proprietary. Yes, even in Microsoft. WSL’s real value, the pair said, was enabling developer productivity, not “secret sauce” differentiation. The team said it was proof that open source can drive mission value that outweighs competitive concerns. By embracing the open source model, Microsoft empowered external developers to unlock solutions and improvements at a pace private teams could not match.

## A Blueprint for Future Open Source Projects at Microsoft

The WSL team’s open source efforts now guide best practices at Microsoft. It’s been the blueprint for other major Microsoft programmer-oriented projects such as Windows Terminal, PowerToys and [Microsoft’s new CLI editor, Edit](https://devblogs.microsoft.com/commandline/edit-is-now-open-source/). The result of prioritizing open source-first, the pair say, has proven to be measurable, positive and a blueprint for future open source transformation at Microsoft.

Microsoft an open source software leader? Who would have thought even a decade ago?

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)