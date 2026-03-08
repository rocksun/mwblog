**“**It’s complicated” can be used to describe relationships and how AI works — or doesn’t — with open source development.

According to longtime open source leader and AWS Head of Open Source Strategy [Stormy Peters](https://www.linkedin.com/in/stormy), in a speech at the recent [Linux Foundation Members Summit](https://events.linuxfoundation.org/lf-member-summit/), AI isn’t killing open source software, but it is actively undermining the social and economic assumptions projects have relied on for decades, and it’s doing it faster than most community leaders and executives are prepared to handle.

Some of this we’re already seeing. For example, Peters warned that AI is “creating a lot of noise, especially for maintainers.” [Daniel Stenberg](https://www.linkedin.com/in/danielstenberg), creator of the popular open source data transfer program, [cURL](https://curl.se/), will be happy to tell you all about [how AI slop bug reports have fouled up the cURL team’s security work](https://thenewstack.io/curls-daniel-stenberg-ai-is-ddosing-open-source-and-fixing-its-bugs/).

## AI slop is already flooding maintainers

> “I was worried that I would kill open source software because I would generate this code or this pull request so quickly that I wouldn’t see any value in it,” she said. “I generated it in three seconds. You could generate it in three seconds if you needed it. Why would I spend my time pushing it upstream when anyone could just generate it on demand?”

Some problems, however, haven’t appeared. Peters admitted she initially feared AI would *discourage* contributions because developers wouldn’t see the point of upstreaming code they could regenerate on demand.​

“I was worried that I would kill open source software because I would generate this code or this pull request so quickly that I wouldn’t see any value in it,” she said. “I generated it in three seconds. You could generate it in three seconds if you needed it. Why would I spend my time pushing it upstream when anyone could just generate it on demand?”

Reality turned out to be the opposite.“What has actually happened is that people are submitting all of the slop that they’re generating out of AI,” Peters said. “They’re not hesitating to donate it back.”

That led to another problem. While the AI-aided coder’s intent might be good — “it’s really quick, so I should, and it’s useful, so I should contribute it” — but the follow‑through is not. “What happens is, it’s not mine, and I don’t know how to maintain it. So if anybody asked me to simplify it or defend it, I can’t, and probably the maintainer of the project also can’t easily figure out what’s going on,” said Peters.

Nothing illustrated the new AI era’s perverse incentives better than the story Peters told about the aforementioned cURL security bounty program.“It’s in billions of devices around the world. It’s in your phones, your cars,” she reminded the audience. As part of a bounty program, cURL maintainers paid out “like $90,000 over six years” and fixed “like 80 something” vulnerabilities submitted by security researchers.

Then AI‑assisted bounty hunting came along, and it all went to hell. Peters pointed out that in an “eight-hour period, they got like 16 submissions, none of which solved a vulnerability.” This wasn’t just noise; it was a direct hit on scarce human time.

Moreover, despite industry hype that AI will supercharge developers, Peters pointed to data suggesting that for experienced engineers, the people most likely to be maintainers, AI can actually slow them down.

She described one study where developers, machine learning experts, and economists all predicted big productivity gains: “In reality, it made expert developers.  not beginning developers, but experts, the people that are like maintainers, [19% slower because of the time that they spend revisiting and looking at code](https://thenewstack.io/how-ai-coding-makes-developers-56-faster-and-19-slower/) and tweaking that almost perfect code,” Peters said.

> “Code that’s generated with AI tends to have 1.7 times more issues.”

Worse still, she highlighted one particularly stark, dark metric: “[Code that’s generated with AI tends to have 1.7 times more issues](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report).” The effect, she said, is that “maintainers are writing quick pull requests that are saving time by using the AI tool, and then it’s the maintainer that’s paying for that, for that time savings that the person that made the [pull] request submitted.”

The net result is a shift in who does the hard work. “It shifts the fun part, which is creating something, writing the code, solving the problem, to someone who’s able to do it quickly with less knowledge,” she said. “And then the maintainers are stuck with [the] part that I think is less rewarding — fixing things, tweaking it, making it all work together.”

## Governance scrambles to catch up

So, what can you do about these issues? According to Peters, “the first thing all the foundations and projects did was update their governance.” Some projects, such as Gentoo Linux, NetBSD, and QEMU, have outright banned the use of AI for coding. Others, such as Ghostty, have come close. A few, however, like Fedora Linux, welcome responsible use of AI. 

Peters observes, however, that even “when they banned AI, most people don’t disclose that they use AI. It turns out people don’t like to admit that [they use AI] when they submit pull requests… only 30% of them disclose it.”  That gap between reality and disclosure makes risk management and license compliance harder for everyone.

AI is also starting to shape which kinds of open source projects get created and adopted.

Peters pointed to an “interesting blog post by [Nolan Lawson” about his blob util‑style micro‑library](https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/). This is “a whole bunch of really useful little functions” that many projects,  5+ million weekly downloads, simply pulled in as a dependency. “His point is, we don’t really need to do that anymore,” she said. “It creates a dependency for all of those downstream projects, and we can generate that code really quickly with AI.”

She admitted she’s “really torn” about this. On one hand, reducing deep dependency chains could limit blast radius and simplify supply‑chain security. On the other hand, “I think a large portion of the open source software community got to where they are because they created something little that was really useful.”

Besides, she noted, noting that some of the world’s most serious vulnerabilities came from exactly these kinds of small but important and ubiquitous components: “It has also created some of our biggest vulnerability worldwide issues. […] Heartbleed and things were useful things that were complete in and of themselves.”

For Peters, the key risk is the *speed* of change. Open source had decades to evolve norms, licenses, and governance; AI is compressing that into a couple of years. We are now in a short, brutal transition period. “I don’t think this is a long-term problem. I think this is like a one-to-two-year problem, because it’s evolving so quickly.”  That said, we must pay attention. “If we want to continue to have open source,” we must address how we use AI now. 

Despite the grim statistics and anecdotes, Peters and other speakers stressed that AI also offers real upside… if communities and companies move quickly to put guardrails and practices in place. “There is a lot of potential for maintainers to be more effective and do things they wouldn’t do otherwise,” one participant argued, citing examples like filling in missing test coverage and using AI to produce better pull‑request descriptions. “I think all these things are actually making maintainer life better, but you have to use them the right way.”

Peters agreed “there’s a lot of potential,” and emphasized that “the person receiving the PR can use the tools if the person submitting it didn’t,” for triage and summarization.

## What can you do?

Her prescription for leaders and projects includes several concrete steps:

* **Invest in documentation for humans and AIs.** “Make sure the documentation is really good, because all of these AI tools are learning about your project from the documentation. They’re large language models, so they’re reading the documentation.”
* **Create explicit guidance for AI users.** When new contributors use AI to solve “an easy first fix thing,” such as “change the color from red to orange,”  they often paste the result straight into a PR. “We have to help them with guidelines and mentors and first steps on, how do you learn how to code and how do you first participate in an open source software project without driving them away?” Peters said. “All of these people that are submitting slop… want to be involved. They just think this is the way to do it.”
* **Attribute AI‑assisted code.** “I think it’s important that we attribute AI-assisted code,” Peters said. “I don’t think it shows that we were lazy. I don’t think it shows that we don’t know what we’re doing.” All the open-source projects welcome AI, demand that developers reveal they’ve used AI to write their code, and credit the tools they used. Attribution is a best practice. We must say ‘Claude did this, or Copilot did this.’” That could prove critical later: “Imagine that we find that one of those AI tools has consistently, always done this one thing, we’ll be able to trace it back to where it is.”
* **Don’t submit what you don’t understand.** “Whether you use AI or not, even though it’s really easy to generate something really quickly, don’t submit it upstream without reviewing it,” Peters warned. “Even if it’s just a bug report or a simple pull request, take the time to understand it.”
* **Re‑examine dependencies and sustainability.** Peters urged projects to “examine our dependencies, because this problem is amplified by your dependency chain” and to “reduce them as much as possible” where it makes sense. She also repeated a familiar call: “Please support your open source software projects. I think it’s really important that we fund them, that we continue to fund them.” Corporate users, she argued, must put more engineers on upstream: “[Companies that participate in the upstream get more value out of open source software than companies that don’t.](https://thenewstack.io/roi-open-source-contribution/) It actually ends up costing them more money if they don’t.”

So, is AI killing open source software? In a word, “No.”

“I don’t think it’s killing it,” Peters said after an audience member voiced that view, “but I think it’s creating a lot of noise, especially for maintainers. I think it’s corrupting our incentives.”  The more accurate picture is that AI is rapidly rewiring how contributions are created, how effort is distributed, and which projects thrive — and doing so on a timeline of “a year or two,” not a decade.

Peters’ bottom line to leaders and maintainers was simple: “If we want to continue that world of collaborative open source, “we have to pay attention now.” Amen, sister!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)