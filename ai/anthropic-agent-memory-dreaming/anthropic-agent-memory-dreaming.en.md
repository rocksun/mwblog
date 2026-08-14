During [AI DevCon](https://tessl.io/devcon/) in London this summer, [Lamis Mukta](https://www.linkedin.com/in/lamis-mukta/), member of technical staff at [Anthropic](https://thenewstack.io/anthropic-claude-text-watermark/), hosted a [stage presentation session](https://x.com/i/status/2085338685747167652) entitled ‘Learning while you sleep, beyond memory to dreaming’.

Mukta set out to examine where state-of-the-art memory management sits today in a world where (as she put it) “context is often orthogonal to the model intelligence” at hand.

“The newest model we’ve just released isn’t going to go out of the box and know exactly what it takes to succeed in your organization and what tasks you want it to do,” said Mukta. “It’s like agents [initially] not knowing their way around a codebase or knowing enough about your own user preferences.”

To steer agentic services the right way, systems obviously need access to memory to create a context window.

## A brief history of Anthropic memory management

Providing a brief history of Anthropic memory management, Mukta said that traditional approaches made use of [CLAUDE.md](http://claude.md), a file that Claude reads at the start of every conversation (that includes [Bash commands](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/#heading-definition-of-bash-scripting), code style, and workflow rules) to give Claude persistent context that it can’t infer from code alone.

Effective to a degree, this technique becomes hard to manage over time, especially when a file with very important preferences gets very, very long.

“So a second avenue that we investigated was memory tools, and this is interesting because it leans into the idea of what happens if we let agents autonomously manage their own memory systems? We let them decide when they read, when they write, and when they update memories,” explained Mukta.

This process happens [in-band](https://www.reddit.com/r/homelab/comments/xxenm0/whats_the_difference_between_inband_and_outofband/) i.e. within the context of a session. When dovetailed with so-called [progressive disclosure](https://docs.claude-mem.ai/progressive-disclosure), the agent only looks at the light metadata at Layer 1, before reaching for full content and original source files in Layers 2 and 3, respectively, so that the system doesn’t overload the model’s context.

“The way I like to think about it is as if I’d had a bookshelf in my room, and every time someone talks to me, I can kind of scan and look at my list of books and see if any of the titles might be relevant to the conversation, and then pick that off the shelf and read it when I need to,” explained Mukta.

But the bottleneck here is that we’re still driven by humans and agents working together i.e. we’re still being quite opinionated about what things need skills. The additional problem here is that memories can go stale and become irrelevant to an organization’s needs. Add the fact that a memory file may be written incorrectly or even maliciously injected and you can see why a lot of guardrails need to be in place.

> “We introduced the concept of dreaming, which is a process that runs asynchronously in batch with its own allocated resources, to ensure that memories themselves are effective, up to date, and [so we can] help the agents learn over time.”

## Dreaming consolidates memory & cuts irrelevance

“So we introduced the concept of [dreaming](https://thenewstack.io/anthropic-managed-agents-dreaming-outcomes/), which is a process that runs asynchronously in batch with its own allocated resources, to ensure that memories themselves are effective, up to date, and [so we can] help the agents learn over time,” explained Mukta. “[This process allows us] to consolidate memory and cut things that are no longer relevant, add things that agents are missing, and clean up and organize memory systems.”

In Anthropic’s world of slumber, dreaming is an out-of-band asynchronous process which the organization says solves the in-band limitation, where agents must split effort between completing and executing tasks, while also concurrently curating memory for their future selves. Dreaming spots recurring failure patterns where agents are consistently failing (wrong units, missing topics, broken tool configs, stylistic tics like overused em dashes), and proposes memory-store updates, again for human review, but hopefully at a more effecient level.

This architecture underpins Anthropic’s Managed Agents memory and API approach at this level, so has the frontier model company won over developers?

## Bad memories can outlive sessions

Staff software engineer, cloud architect and independent researcher in AI agent systems, [Jayakumar Ramalingam](https://www.linkedin.com/in/jayakumarramalingam), tells *The New Stack* that “dreaming is useful, but it also creates a dangerous promotion path” i.e. one that leads from repeated mistakes to persistent policy.

“A bad answer normally dies with the session; a bad memory can influence thousands of future sessions. Human review sounds reassuring, but at fleet scale it can easily become a rubber stamp for recommendations nobody has time to reconstruct,” Ramalingam says.

> “The industry has spent too much time treating memory as a context window problem when it is really a state management problem.”

He insists that every proposed memory should “carry provenance, evidence and an expiration condition”, and not just exist as a pattern that recurred often enough to look real. Otherwise, he thinks that dreaming may help agents remember more while making organizations forget why the memory was trusted.

“Anthropic is getting one important thing right: its agent memory should look more like versioned infrastructure than artificial cognition. The industry has spent too much time treating memory as a context window problem when it is really a state management problem,” underlines Ramalingam.

His point is – if an agent cannot show who changed a memory, why it changed and how to roll it back, it does not have production memory, so it becomes an unaudited configuration file with an AI attached.

## Dreaming is the right instinct aimed at the wrong evidence

Enterprise AI architect and founder of Besk Tech, [Vladimir Beskorovainyi](https://vladimir.besk.tech), tells *The New Stack* that “dreaming is the right instinct aimed at the wrong evidence”, because the failures it catches (wrong units, broken tool configs, too many em dashes etc) are all visible on the surface of a transcript.

“The failure that actually costs you is an agent reaching for the wrong tool for a reason that looked perfectly defensible at the time,” Beskorovainyi says. “In the systems I run in production, the log records the decision rather than the API call, and that is the only reason a review pass like this finds anything worth finding.”

> “When the ‘lately’ factor quietly becomes true. That leaves us at a point where versioning tells us what changed and when, not what is correct.”

He points to what he calls “a worse problem underneath the agent’s decision” i.e. if updates are proposed from recent batches, the memory store drifts towards whatever the agent fleet happened to do lately, and so the “lately” factor quietly becomes true. That leaves us at a point where versioning tells us what changed and when, not what is correct.

“The industry spent two years insisting that memory meant embeddings, and Anthropic solved it with a filesystem and [grep](https://thenewstack.io/the-grep-command-in-linux/) [a Linux command that searches for patterns in files] and that is the most interesting decision in this whole discussion,” insists Beskorovainyi.

He says the reason it matters is legibility. A memory store a developer can open and read is a memory store an engineer can audit, and (he insists) “no vector database has ever offered that”, while everything else in the architecture (the versioning, the hashes, the tiered permissions), is ordinary distributed systems engineering we have known how to do for decades.

## Dreaming is the clever (but worring) part

Founder of autonomous AI penetration testing company [Penetrify](https://www.penetrify.cloud), [Viktor Bulanek](https://www.linkedin.com/in/bulanekv/), tells *The New Stack* that when the industry spent two years convinced that agent memory was a vector database problem, and Anthropic shipped grep, that was a useful thing.

“In terms of what Anthropic is getting right… a memory store you can [cat](http://geeksforgeeks.org/linux-unix/cat-command-in-linux-with-examples/), diff and code review is one you can actually operate, whereas nobody has ever successfully debugged an embedding that quietly ranked the wrong chunk third,” Bulanek says.

> “Anthropic’s approach to dreaming is the clever part and also the part that worries me most, because it points an automated writer at session transcripts, and transcripts are full of content the agent did not author.”

He thinks that the versioning matters here far more than the auditability framing suggests and reminds us that “rollback is not a compliance feature”; it is the undo button for a poisoned memory a software engineer discovers three weeks after it was written, which is the incident every serious agent deployment is going to have eventually.

“But to add balance here, Anthropic’s approach to dreaming is the clever part and also the part that worries me most, because it points an automated writer at session transcripts, and transcripts are full of content the agent did not author,” Bulanek cautions.

“Anthropic is right that human review is the answer, but bulk review of proposed diffs is exactly the control that decays fastest once the suggestions are mostly good. The other gap is that nothing in this architecture says when a stored fact stops being true. Versioning tells you what changed, it does not tell you what rotted, and a confident note about a system that was refactored last month is worse than no memory at all,” he advises.

Bulanek’s work sees him run autonomous agents in production that perform penetration testing and run for hours unsupervised with real credentials against live systems, so memory for his team is both an operational cost and a security boundary at the same time.

## The Anthropic way of doing things has an endearing lack of flair to it

Co-founder and CTO of [Noah Labs](https://www.noahlabs.ai/), [Berk Yilmaz](https://www.linkedin.com/in/berkyy/), tells *The New Stack* that the Anthropic way of doing things has “an endearing lack of flair to it” in his view.

“Everyone wants memory to feel like the newest incarnation of machine intelligence, and their pitch goes something like: just give it a filesystem, versioning, searchability, and don’t let a thousand processes stamp all over each other,” Yilmaz says. “This is closer to how production AI should be done. While we have spent a long time improving models, the supporting infrastructure has not kept up, failing in incredibly prosaic engineering ways.”

Yilmaz is behind a company that develops an AI-native IDE for government and regulated systems, built for air-gapped environments and legacy codebases. He reminds us that once a memory decision is made on *which past behavior should become future behavior*, memory itself ceases to be inert.

“A hallucination that dies after a single session is a pain in the neck, but a hallucination that outlives a thousand sessions is infrastructure. The same thing applies to security; if an attack succeeds in writing to memory, it has become persistent. Provenance becomes absolutely critical here, how was the system taught this, where did it learn it from, who certified it, and can I undo it? In enterprise AI, sometimes forgetting is a safety measure,” adds Yilmaz.

## A pragmatist would remember that Anthropic gets paid for usage, not efficiency

AI, product & data science leader and former [Meta](https://thenewstack.io/meta-abandons-llama-spark/) employee, [Kerstin Frailey](https://www.linkedin.com/in/kefrailey/), tells *The New Stack* that at face value, dreaming (for her money) “certainly sounds like it has the potential to blow up AI bills” right now.

“A cynic would say this is designed to fill the revenue hole left by tokenmaxxing before [Anthropic’s IPO](https://www.wsj.com/tech/ai/anthropic-tries-to-shore-up-investor-confidence-ahead-of-blockbuster-ipo-0ff736ad),” Frailey says. “An optimist would hope for a beautifully thrifty design. A pragmatist would remember that Anthropic gets paid for usage, not efficiency. A skilled practitioner would run incremental pilots, aggressively monitor costs, and routinely test for measurable improvements.”

> “As a nice bonus, dreaming offers potential system improvement, too. But its familiar predecessors – garbage collection and storage compaction – are comparatively deterministic and controlled.”

She continues and notes that dreaming offers cleanup and consolidation, which she defines as a “reasonable development” for any system that constantly generates new files.

“As a nice bonus, it offers potential system improvement, too. But its familiar predecessors – garbage collection and storage compaction – are comparatively deterministic and controlled. Unlike its namesake or those analogues, dreaming appears neither cheap nor efficient: pay an AI to do the work once, then pay AIs to regularly review, revise, and restructure it,” she adds.

Dreaming as part of Anthropic’s Managed Agents memory and API approach isn’t alone. The notion of AI model dreaming (or automatic out-of-band background memory consolidation if we’re being formal about things) is also [being popularised by OpenAI](https://openai.com/index/chatgpt-memory-dreaming/) for ChatGPT, in stateful agent coding platform [Letta](https://docs.letta.com/configuration/memory) and elsewhere.

The bottom line here may be a realization that, in AI modeling terms at least, memory is actually maintenance.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)