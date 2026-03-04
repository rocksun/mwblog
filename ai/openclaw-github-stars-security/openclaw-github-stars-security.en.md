OpenClaw is in the ascension.

This open source autonomous AI agent has this year surpassed Linux on the GitHub all-time star leaderboard. The project has now racked up more stars than React, the open-source JavaScript library used to build web app user interfaces (UIs).

Having now amassed 250K+ stars in just four months, OpenClaw is the most-starred non-aggregator software project (i.e., a tool that generates original value and content rather than filtering and displaying existing information) on GitHub, as first reported by [star-history.com](https://www.star-history.com/blog/openclaw-surpasses-react-most-starred-software).

But developer love doesn’t always translate into long-term enterprise deployment success. The concept behind micro-kernels never eradicated monolithic Windows estates, and some argue that the Lisp language was something of an Edsel or DeLorean.

The question now, then, is whether OpenClaw is a flash in the pan (lobster stir-fry pun not intended), [a security risk waiting to happen](https://thenewstack.io/openclaw-moltbot-security-concerns/), or a *de facto* standard in the making.

## OpenClaw defined

OpenClaw uses large language models to serve as a personal AI assistant, acting as an agentic gateway that runs locally on a user’s machine.

Sometimes referred to as a personal AI assistant, OpenClaw provides agentic answer services inside WhatsApp, Slack, Telegram, Google Chat, Signal, Discord, iMessage, Microsoft Teams, and WebChat. Compatible across Mac OS X, iOS, and Android, Windows users are recommended to use OpenClaw via WSL2 (Windows Subsystem for Linux) rather than running it natively to ensure optimal compatibility and stability.

Why the lobster logo and theme? Because OpenClaw “pinches the toil” as it executes tasks on a user’s machine.

## Stars in their eyes?

According to a report citing the WeChat account New Intelligence Yuan, stars on GitHub are something of a “low-cost statement” and aren’t very far from bookmarks or likes. Translated from its original Chinese, the blog suggests that it’s common to see resource summaries, tutorials, and booklists at the top of developer fan lists.

“When you remove these resource libraries and event-type projects and really examine the basic software that can be installed and run, OpenClaw’s ascent to the top is extremely subversive. At the same time, hardcore developers are busy turning it into a 24/7 automatic code-writing machine. Along with the fanaticism comes the loss of control in the real world,” writes the author.

> “OpenClaw exploded in popularity for one key reason — everyone, technical or non-technical, wants a free personal AI assistant.”

In January and February of this year, OpenClaw’s third-party skills marketplace, ClawHub, was hacked in an orchestrated cybersecurity attack, so how far could the risks spread here?

[Michael Levan](https://www.linkedin.com/in/michaellevan/), AI architect at [Solo.io](https://www.solo.io/), tells *The New Stack*OpenClaw’s success is down to a seemingly universal desire: A personal assistant.

“OpenClaw exploded in popularity for one key reason — everyone, technical or non-technical, wants a free personal AI assistant. Although it’s impressive as it is, it introduces a complex set of security challenges ranging from centralized access control (who can do what with standard RBAC or more sophisticated protocols like ReBAC and ABAC) to LLMs, Agent Skills, and MCP Servers,” Levan says.

“Successful enterprise adoption of OpenClaw will require multiple layers of control, including an enterprise ExtAuth server for centralized authentication, enhanced observability into agentic traffic flows and runtime guardrails, including rate limiting and prompt guards,” said Levan.

## Move on from the model

There’s clearly a real shift happening here. OpenClaw’s rapid adoption reflects a shift toward systems that execute workflows and behave more like autonomous services (and, in some cases, more like employees) than traditional applications.

What’s driving this level of interest is not just the model itself, but the ability to automate real tasks across tools and systems, which developers have been trying to operationalize for years.

[Yossi Atlevet](https://www.linkedin.com/in/yossi-altevet-538340/?originalSubdomain=il), CTO and Co-Founder of [DeepKeep](https://www.deepkeep.ai/), tells *The New Stack* that OpenClaw adoption has gone beyond the norm.

“At that point, developers working with OpenClaw are no longer integrating a model; they are effectively deploying a distributed system that can take actions automatically across APIs, files, and internal infrastructure. That fundamentally changes the security model,” Atlevet says. “Traditional application security assumes deterministic behavior and clearly defined permissions. Still, agentic systems make decisions at runtime, chain tools together, and operate across multiple trust boundaries.”

As a result, says Atlevet, risks such as prompt injection, unsafe tool invocation, data exposure, and unintended actions are no longer random occurrences. They are inherent to how these systems operate, and they fall outside the scope of what most existing security controls were designed to handle.

For Atlevet, developers now need to close the gap and put security into the execution layer, monitoring and validating not just what the model generates, but what the agent actually attempts to do.

## Another Napster moment?

[Alexander Feick](https://www.linkedin.com/in/alexanderfeick/) at [eSentire](https://www.esentire.com/) believes OpenClaw’s popularity feels like a Napster moment for AI agents, but he agrees with his industry counterparts on risk.

“Users are embracing risk because the utility is tangible and immediate, and that’s exposing the shape of what governance needs to look like before anyone builds it. The market will push tools like OpenClaw far ahead of governance frameworks unless we embed control planes first, not as an afterthought,” Feick tells *The New Stack*.

“The fundamental gap isn’t just a missing checkbox — it’s the absence of a control plane capable of expressing fine-grained trust boundaries. People want to say ‘use my credit card’, but current agents can’t enforce limits like spend caps or merchant safelists; they can read email broadly, but can’t be scoped to specific inboxes or contacts. Without those controls, risk scales faster than adoption,” said Feick.

## Is OpenClaw greater than Linux?

Whether OpenClaw will now be seen as the next Twitter and be regarded as greater than Linux is uncertain. The installed base of Linux worldwide, its foundational role at the base of the Internet, and its warm embrace across previously proprietary strongholds surely guarantee its all-star status for the foreseeable future.

Pass the lobster rolls, please.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)