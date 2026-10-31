**Earlier this month, the team behind Hydro developed a new way** to check that a distributed system still works correctly when it resends messages after a failure.

This produced what [Shadaj Laddad](https://linkedin.com/in/shadaj) described to me as “like a 5000 line PR.” Hydro is an open-source Rust framework for distributed systems, the software that runs across many machines at once, and agents now write most of it with humans driving. The PR was difficult to split into smaller pieces as its components worked together.

VIDEO

That’s a lot of code to review for a tool developers count on to catch bugs. Laddad, research lead for the Hydro team at AWS, says it’s something the team spends a lot of time thinking about. I sat down with him last week at AGNTCon + MCPCon in San Jose. He was set to give a keynote the next day where he was going to argue code review can’t keep pace with how agents write code.

Agents have let the team aim higher, Laddad told me, saying PRs arrive faster and run longer. “You can have the feature work well in isolation, then you mix it with something else, and suddenly the guarantees break down,” he said.  
  
And you can’t just trust the tests. In most agent workflows, he says, the agent writes both the code and the unit tests. “Agents are great, but they’re unpredictable,” Laddad said. That unpredictability is part of what makes them creative, and it makes it hard for a human to review all those tests and confirm they do what the team wants.

His answer is shared Correctness checks outside the agent’s “zone of trust,” such as those enforced by a compiler. Rust’s borrow checker is his example: It catches race conditions before the code ever runs. Hydro does something similar for distributed systems, catching several types of bugs at compile time so an agent gets instant feedback on mistakes it introduced. The wider goal, which the team is still exploring, is domain-specific guardrails that agents can share.

To find candidates, the team studies historical projects for recurring patterns. Idempotency, ensuring a retried request doesn’t run twice, comes up repeatedly in design reviews, so the team is asking whether it can become a general-purpose guardrail. Laddad sees this as the next rung on an old ladder. C spared programmers from mangling function calls in assembly. Java took memory allocation off their plate. Agents, he argued, make the next layer more urgent.

Compilers have limits, though. As *The New Stack* reported in August, [AI-generated Rust can compile perfectly and still be wrong](https://thenewstack.io/canonical-c-rust-apparmor/).

The same team also built [Infinity](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/), an open-source agent runtime AWS announced on October 23. It suspends an agent while it waits on a tool call or a CI job instead of keeping it running. Laddad cited a benchmark showing 75,000 concurrent agents on a single Raspberry Pi. According to the AWS announcement, that figure is extrapolated from a server test in which each idle agent used about 100 KB.

Hydro itself is an early release, built for teams running high-throughput, low-latency services who are constantly worried about distributed systems bugs. Laddad noted that users should expect rough edges and a learning curve right now. The payoff is the confidence to change a system without fearing it will break a few months later.  
  
*Hydro and Infinity are open source at [hydro.run](https://hydro.run), built jointly by AWS and UC Berkeley.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)