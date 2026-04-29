For this episode of The New Stack Makers, we sat down with [Nimisha Asthagiri](https://www.linkedin.com/in/nasthagiri/), the data and AI advisor at Thoughtworks, to talk about why so many companies are struggling to move their AI projects from proof of concept to production, and what the latest edition of the Thoughtworks Technology Radar tells us about where the industry is headed.

VIDEO

> “The question that we’re hearing a lot from executives is, how do we go faster? I think the right question might be, what do we build, given the latest technology, that we couldn’t build before?”

In this episode, we discuss the PoC-to-production gap in agentic AI, why engineering fundamentals like test-driven development and mutation testing are making a comeback, and a provocative idea: that much of the code AI generates may not need to exist at all.

## The PoC-to-production gap

Gartner predicts that more than 40 percent of agentic AI projects will be canceled by the end of 2027, and the pattern Asthagiri sees at Thoughtworks lines up with that forecast. In part, that’s because companies went through a wave of proof-of-concept projects after generative AI took off in 2022. Now, many are stuck trying to figure out how to get those experiments into production.

The problem, as Asthagiri sees it, starts with the question executives are asking. “The question that we’re hearing a lot from executives and others is: how do we go faster? How do we keep relevant?” she tells *The New Stack*. “I think the right question — or another alternative, better question — here might be: what do we build, given the latest technology, that we couldn’t build before?”

Instead of bolting AI onto existing workflows, the companies that are succeeding are rethinking what this technology actually enables. It’s a systems-thinking argument, Asthagiri argues.

When asked what the more successful companies have in common, she pointed not to tooling but to organizational investment: “The ones that are successful are doing the due diligence. It is hard work, but it’s about the literacy and the enablement within your organization for the people.”

## Engineering fundamentals are back

The latest Thoughtworks Technology Radar argues that the industry needs to look backward before it can move forward. The Radar warns of accumulating [cognitive debt](https://www.thoughtworks.com/en-us/radar/techniques/codebase-cognitive-debt?utm_source=publisher-direct-TNS&utm_medium=digital-advertising&utm_campaign=sai_tsi_rp-gl-pspt_techradar_2026-04) by widening the gap between what AI produces and what developers actually understand about their own codebases.

Asthagiri is part of the global team that assembles the Radar.  The point of view at Thoughtworks is this: With so many AI tools and open-source projects coming online, no one can evaluate them all. In such circumstances, the prudent approach is to revisit many established techniques — not out of nostalgia but as a necessary counterweight to the speed at which AI tools can generate complexity.

Asthagiri points to test-driven development, mutation testing, DORA metrics, and zero-trust security architecture as practices that need to come back to the forefront. “A lot of traditional, fundamental ways of thinking about engineering discipline are really now coming back to the forefront,” she says.

With autonomous coding agents increasingly writing production code, the feedback loops are more important than ever. As Asthagiri puts it, “What are those feedback sensors? In addition to the feed-forward of your context that you provide your agents, what’s the feedback with the sensors, the tests, and linters, and a lot of those common practices?”

The same logic applies to security. As agents proliferate across developer workstations, the identity layer now needs to account for machine agents as well as human ones. Asthagiri says zero trust architecture is critical for “being able to know who did what, as well as the authentication and the authorization of the work that is happening.”

These days, those agents often work as part of a larger team. Asthagiri sees organizations moving toward intentionally designed multi-agent setups, with role-specific agents for backend, frontend, and other domains — but orchestrated by humans.

## Dark code and the case for ephemeral software

When we asked Asthagiri about the sheer volume of AI-generated code and the bottlenecks it creates downstream, she noted that the response shouldn’t be better review tooling. Instead, organizations should be asking whether the code needs to exist in the first place.

“There’s gonna be a lot of dark code,” she says, borrowing from the concept of dark data — the information organizations collect but never actually use. “Because code is going to become a commodity to generate, you don’t necessarily need to keep it.”

She breaks this into two ideas. First, organizations need to be explicit about the lifecycle of their code. Proof-of-concept code should be documented as having an expiration date and architecturally segregated so it can be deleted when it’s no longer needed.

Second, some code should be generated ephemerally, spun up for a single use, and then discarded. “If I don’t have the agent skill for it, and it’s not a necessarily reusable feature, then why not go ahead and dynamically generate it for that particular single fit-for-purpose use, and then you’re done?”

That connects to a technique the Radar team calls [sandboxed execution for coding agents](https://www.thoughtworks.com/en-us/radar/techniques/sandboxed-execution-for-coding-agents?utm_source=publisher-direct-TNS&utm_medium=digital-advertising&utm_campaign=sai_tsi_rp-gl-pspt_techradar_2026-04), which allows for the “running agents inside isolated environments with restricted file system access, controlled network connectivity and bounded resource usage.”

You can explore the full Thoughtworks Technology Radar here: [thoughtworks.com/radar](https://www.thoughtworks.com/radar?utm_source=publisher-direct-TNS&utm_medium=digital-advertising&utm_campaign=sai_tsi_rp-gl-pspt_techradar_2026-04).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)