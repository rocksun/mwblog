Every enterprise software vendor claims its AI agent is [production-ready](https://thenewstack.io/scaling-ai-agents-in-the-enterprise-the-hard-problems-and-how-to-solve-them/), but how to measure it remains up in the air.

The enterprise AI platform [DevRev](https://devrev.ai/), led by Nutanix co-founder [Dheeraj Pandey](https://www.linkedin.com/in/dpandey/), argues that while benchmarks like TAU-Bench and Agent’s Last Exam exist, none of them really test for the work employees actually do, where the ability to work across large context windows is often more important than pure reasoning power.

This week, DevRev released the first version of its [Enterprise AI Agent Benchmark](https://devrev.ai/enterprise-bench-methodology), an open test that makes the dataset, evaluation harness, judging criteria, [results](https://benchmark-dashboard-five.vercel.app/analysis?uuid=8f38e704-8491-4099-9aa9-fc7cac32d20c), and raw traces [available](https://benchmark-dashboard-five.vercel.app/headline), so any organization can run it against its own systems.

The release covers only the two lowest tiers, L1 and L2, of a four-level framework, and DevRev is counting on the community to help build out the more advanced tiers.

DevRev built the benchmark on Terminal Bench, the evaluation harness from the Laude Institute, whose researchers are affiliated with UC Berkeley and Stanford. It had the methodology reviewed by [Alexandros Dimakis](https://www.linkedin.com/in/alex-dimakis-b1b20320/), a UC Berkeley professor and co-founder of [Bespoke Labs](https://bespokelabs.ai/), which builds tasks for several of the benchmarks the frontier labs invest in.

The idea for a new test, Pandey and DevRev CTO Ahmed Bashir tell *The New Stack*, started as irritation. Sitting through conference after conference where every booth advertised the same thing, Bashir kept asking who was checking.

> “People could say that they have industry-leading AI, and I said, ‘Based on which metric?’ … There is no method. It’s ad hoc.”

“People could say that they have industry-leading AI, and I said, ‘Based on which metric?'” says Bashir. “There is no method. It’s ad hoc. It’s built on this idea that it’s a marketing concept. There is no benchmark. In a world of hundreds, if not thousands, of benchmarks that relate to AI, was there one that actually came to the essence of what enterprise was looking for?”

![](https://cdn.thenewstack.io/media/2026/07/59142e55-screenshot-2026-07-09-at-9.12.44-am-1024x351.png)

*Credit: DevRev*

## The data is the hard part

The benchmarks that matter to the frontier labs reward exotic reasoning, and enterprise work rarely looks like that, the DevRev team argues.

“We are not going to get closer to benchmarking the needs of enterprise by creating more complex tasks,” Bashir says. “What we needed to do was combine a moderate level of task complexity with an inordinate amount of complexity in terms of data organization, and data organization is about the source of the information, the shape of the information, and the permissions that control access to the information.”

> “We are not going to get closer to benchmarking the needs of enterprise by creating more complex tasks.”

Most enterprise tasks aren’t as hard as a chemistry problem. They’re moderate tasks that eat time because the data they run on is scattered across systems, shaped inconsistently, and locked behind permissions — data silos that never quite went away. Task complexity is a solved-enough problem, but data complexity, Bashir says, is “quite novel” as a thing to measure: “the data itself can be organized, shaped, and access controlled in ways that make it complex to access.”

To turn this into a benchmark, DevRev built what it calls scale-invariant ground truth. The dataset models a single mid-size software company at four sizes: 1x, 4x, 16x, and 64x. The correct answer to every task remains the same across all four. The additional data is noise that a correctly operating agent should never surface. At 1x, roughly 40 percent of the tickets are relevant to a given question. At 16x, only 2.5 percent are.

The team argues that this design targets the shortcut most systems rely on. Agents are good at finding a needle in a haystack when the context window is small, but that falls apart at production volume.

The benchmark scores agents on three axes: precision (does it get the right answer with a verifiable source and an auditable path?), efficiency (does the cost track the question or the data size?), and safety (are permission boundaries respected and every action traceable?).

An independent LLM judge verifies results against published criteria, and every run has to submit its traces alongside its score.

## Four levels, borrowed from self-driving

The L1–L4 framework describes graduated autonomy the way the levels of self-driving do.

Bashir describes an L1 task as retrieval and synthesis across “a maximum of two or three sources,” well-bounded and single- or few-turn. An L2 task “usually has to do with multi-step thinking, but it’s still single domain,” he says, where the planning is evident, but the agent still isn’t taking action. L3 moves up to cross-domain problem-solving over a mix of structured and unstructured data, and L4 is full autonomy, the level where, as Pandey puts it, “you have to change code for L4 to work.”

Pandey frames the progression as a “trifecta” of search, answers, and actions. Enterprise search, he says, “has been commoditized to a large extent,” which is why L1 is where most vendors already play. L2 is “where is my order, where is my cancellation, where is my refund.”

Actions, the part buyers actually want, start at L3, but DevRev argues most of the market is still stuck at search.

L3 and L4, larger datasets, and voice scenarios are on the roadmap, but Bashir says the company held them back to draw third-party submissions first. “We’d love to see a progression in the submission, so that it’s not just our submission but also third-party submissions,” says Bashir.

## Same model, different outcomes

To show the benchmark in practice, DevRev ran its own agent, Computer (an AI agent that works across enterprise systems on top of a shared, permission-aware memory layer), head-to-head against [Claude Code](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/). Both ran on the same Opus model family, were judged the same way, and performed identical L1–L2 tasks via protocol-faithful replicas of vendor APIs and [Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) servers. Computer ranked first overall.

In the L1–L2 results, DevRev’s Computer was more accurate by 22 to 35 points at every data scale tested, and it reached those answers on far fewer tokens: 268,000 per correct answer against Claude Code’s 902,000, or 3.4 times fewer. Scaling the dataset from 1x to 64x increased Computer’s token consumption by 11 percent, while Claude Code’s increased by 55 percent.

Because both agents used the same Opus-class model, DevRev attributes the gap to data-retrieval architecture rather than the model itself. The benchmark sorts enterprise AI systems into two kinds: those whose costs rise with data volume, and those whose costs track the complexity of the question. DevRev’s contention is that the first kind doesn’t survive contact with a real enterprise’s data.

## A vendor’s own yardstick

A vendor grading its own benchmark deserves skepticism, but DevRev did bring in third-party experts to validate it.

The benchmark’s central variable is noisy data at scale, which rewards selective retrieval and punishes loading everything into context. Not coincidentally, that’s the exact problem DevRev’s architecture is built to solve. The comparison target, Claude Code, is a coding agent pressed into service as a stand-in for a general enterprise agent, not a product Anthropic markets for this job, though Anthropic’s [Cowork](https://thenewstack.io/claude-cowork-cloud-mobile/) is built on the same foundation.

Bashir says the company had its tasks vetted outside its own walls, choosing to “submit these tasks for review by not just the Laude Institute, but also Bespoke Labs, so it has been independently verified.”

Publishing the dataset, the harness, and its own traces lets anyone rerun the tests or contest the scores, and the company invites competitors to submit to the public leaderboard. That raises the floor on trust, but it doesn’t change the fact that DevRev chose which axis to measure.

DevRev argues that this is the first open, vendor-neutral enterprise benchmark. But similar efforts exist. Salesforce’s CRMArena-Pro, out in 2025, simulates Salesforce orgs and grades agents on accuracy, cost, and safety. Sierra’s tau-bench tests tool-agent-user interaction and policy adherence in enterprise-style domains. Both come from vendors, too.

What’s different in DevRev’s benchmark is the data-scale axis and the decision to open-source everything down to the traces, not the idea of an enterprise agent benchmark. Meanwhile, SWE-bench, the coding benchmark that set the template, has been saturating, with frontier models clustered near the top and [contamination caveats piling up](https://openai.com/index/separating-signal-from-noise-coding-evaluations/).

## It’s the memory, not the model

On the benchmark, Anthropic’s Opus 4.6 and Opus 4.8 perform almost identically. “Both models can perform the task, provided that they have the data,” Bashir says. The models have gotten good enough at enterprise-grade tasks that a newer one barely moves the score, which means the differentiation now comes from somewhere else: the harness.

> “As you have more data sources, the ability to, at any given time, have a deep understanding of all the sources goes down … You’ll start forgetting things that you remembered.”

Bashir points to a minor Claude Code release that shipped prompt improvements aimed specifically at MCP. “It’s actually getting better outside of the release of models,” he says. The frontier labs are optimizing how agents handle data, he argues, not just how they reason.

That matters because, in Bashir’s description, MCP “is a hands-off relationship with the source data,” effectively stateless. “As you have more data sources, the ability to, at any given time, have a deep understanding of all the sources goes down,” he says. “If you have three or four sources, you’re going to start struggling. You’ll start forgetting things that you remembered.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)