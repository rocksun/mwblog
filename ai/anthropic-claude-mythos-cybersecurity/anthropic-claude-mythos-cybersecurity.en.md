In late March, a [misconfiguration](https://fortune.com/2026/03/26/anthropic-leaked-unreleased-model-exclusive-event-security-issues-cybersecurity-unsecured-data-store/) in Anthropic’s content management system revealed that the company was working on [Claude Mythos](https://m1astra-mythos.pages.dev/), a new tier of models larger and more capable than its current flagship, Opus. That unpublished announcement also noted that Anthropic would take a more deliberate approach to launching the model to mitigate “potential near-term risks in the realm of cybersecurity.” That’s exactly what Anthropic is doing now.

Claude Mythos Preview, which the company described on Tuesday as a “general-purpose, unreleased frontier model,” will not be publicly available — at least not yet and not in its current form. Instead, Anthropic will make it available to a few select partners through what it calls Project Glasswing.

> Claude Mythos Preview won’t be public — only select partners get access.

Amazon, Apple, Broadcom, Cisco, CrowdStrike, the Linux Foundation, Microsoft, and Palo Alto Networks are the launch partners for this project. They and about 40 additional organizations will get access to the preview version of Claude Mythos for defensive security work so they can use it to scan and secure their own systems and open-source tools.

While Mythos wasn’t specifically designed for cybersecurity tasks, Anthropic notes that the model performs strongly in agentic coding and reasoning. On the [CyberGym benchmark](https://www.cybergym.io), which evaluates AI agents on vulnerability analysis tasks, Claude Mythos scores 83.1%. Opus 4.6, which until now led the rankings on this benchmark, scored 66.6%.

![](https://cdn.thenewstack.io/media/2026/04/37a60f92-project-glasswing-logos-1024x576.png)

Credit: Anthropic.

Anthropic, which, after all, was founded as an AI-safety-focused alternative to OpenAI, seems to believe that launching a model with these capabilities should be done cautiously to give defenders time to batten down the hatches before attackers gain access to it, too.

Cynics may argue that playing up these dangers also helps position these models as especially capable — and hence desirable — in the public eye. But as CrowdStrike CTO Elia Zaitsev notes, there is a real danger here.

“The window between a vulnerability being discovered and being exploited by an adversary has collapsed – what once took months now happens in minutes with AI,” he says in a statement. “Claude Mythos Preview demonstrates what is now possible for defenders at scale, and adversaries will inevitably look to exploit the same capabilities. That is not a reason to slow down; it’s a reason to move together, faster. If you want to deploy AI, you need security.”

> “Claude Mythos Preview demonstrates what is now possible for defenders at scale”

Already, Anthropic has used Mythos Preview to find what it describes as “thousands of zero-day vulnerabilities, many of them critical.” Often, these were very old, with the oldest being a bug in OpenBSD that remained unknown and unpatched for 27 years.

The model also managed to chain together several vulnerabilities in the Linux kernel to gain superuser access.

Security research like this is especially important for open-source projects. Linux Foundation Executive Director Jim Zemlin said security expertise was historically something large enterprises could afford but remained out of reach for smaller companies and open-source projects.

> “This is how AI-augmented security can become a trusted sidekick for every maintainer.”

“Open source maintainers — whose software underpins much of the world’s critical infrastructure — have historically been left to figure out security on their own,” he says. “By giving the maintainers of these critical open source codebases access to a new generation of AI models that can proactively identify and fix vulnerabilities at scale, Project Glasswing offers a credible path to changing that equation. This is how AI-augmented security can become a trusted sidekick for every maintainer, not just those who can afford expensive security teams.”

Eventually, Anthropic plans to launch Mythos-class models to its users, but for now, it’s restricted to Project Glasswing participants only. Anthropic is making $100 million in usage credits available to the participating companies, as well as $4 million in direct donations to open-source security organizations.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)