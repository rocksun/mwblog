Chinese frontier model outfit [Z.ai](https://z.ai) released [GLM-5.3](https://z.ai/blog/glm-5.3) on Friday, a model hewn from the same codebase as its predecessor GLM-5.2, with every gain [engineered as a result of post-training](https://thenewstack.io/glm-5-3-post-training-coding/). The latest release is claimed to be much better at complex coding and long-horizon tasks.

Rarely considered to be a defined process that follows a single immutable script (as in song sheet, not as in code script), post-training model optimization processes are especially significant here and will have included reasoning alignment, supervised fine-tuning, and Reinforcement Learning from Human Feedback (RLHF).

“Over the past month we kept scaling on this [GLM-5.2] stack: more environments, more diverse tasks, and more compute spent training on them,” stated Z.ai, in an anonymously authored blog.

## A model trained on a much broader range of production workflows

The company clarified further, saying that the widened and more complex model training environments now cover “a much broader range of production workflows”, with “diverse task categories” designed around how engineering and research work is actually carried out in practice. Some tasks constituted what would represent several days of work for an experienced engineer.

“In an ML infrastructure task, for example, the model may be given the same working environment as an engineer, with access to compute clusters, storage systems, internal documentation, codebases, and experiment results. It must diagnose bottlenecks across the training stack, implement optimizations, run experiments, and deliver a measurable end-to-end speedup while preserving correctness,” stated Z.ai.

If in-house benchmarks are of any worth, the organization’s newly introduced Z.ai Code Bench measures GLM-5.3’s coding abilities at a 50% improvement over GLM-5.2. Pledging to be scrupulously virtuous, the company thinks that private benchmark “reduces the risk of contamination from public test sets” to provide a more faithful measure of real-world user experience.

Other public benchmark positions are also openly showcased by the company, here spanning TerminalBench 3.0, DeepSWE, Agents’ Last Exam, AutomationBench, HLE w/ Tools: Humanity’s Last Exam (HLE), an independent academic benchmark, as well as OpenAI’s GDPVal-AA v2.

## What do AI developers make of these moves?

Outside these yardsticks and benchmarks, what do real world developer practitioners think of what’s happening in the open-weight model universe?

Co-founder of long-horizon autonomous software engineering company [NonBioS.ai](http://nonbios.ai), [Nishant Soni](https://www.linkedin.com/in/nishantsoni/), tells *The New Stack* that when he considers what Z.ai has done in relation to scaling for real-world long-horizon tasks, he “would take it with a pinch of salt” based upon his own real-world experiences.

“To my knowledge, no benchmarks objectively demonstrate the claimed superior long-horizon capability of GLM-5.3 in real world tasks,” Soni says. “The specific orchestration that Z.ai describes seems unlikely to provide the differentiated and comprehensive datasets required to engender such capability in frontier models.”

“I suspect this is largely an effort to deflect from the model’s true source of frontier capability – which shows a pattern consistent with industrial-scale distillation of Anthropic models,” he adds.

In internal testing at NonBioS, Soni explains that his team has seen “striking similarity” between Kimi/GLM outputs and Claude’s outputs. In contrast, other frontier models – notably Gemini and Grok – show greater diversity compared to Claude’s outputs.

> “I suspect this is largely an effort to deflect from the model’s true source of frontier capability – which shows a pattern consistent with industrial-scale distillation of Anthropic models,” he adds.

## Meet the model halfway to real results

Founder at AI benchmarking specialist [Megaton](https://megaton.ai/), [Sherif Higazy](https://www.linkedin.com/in/sherif-higazy-159a638b/), tells *The New Stack* that he can see sense in any frontier model company (or user, or team) laying down an internal evaluation system that measures tokens and spend against tasks (cybersecurity or otherwise).

“When a model is trained for benchmarks, versus delivering promised capability, that’s generally a good thing,” Higazy says. “But ultimately, getting consistently useful work from an agent requires meeting the model halfway so that teams adapt their working environments around how agents work (for example, forcing repeated test runs or making inputs & outputs machine-readable and verifiable) to get the best results.”

> Getting consistently useful work from an agent requires meeting the model halfway so that teams adapt their working environments around how agents work (for example, forcing repeated test runs or making inputs & outputs machine-readable and verifiable) to get the best results.”

“Z.ai is claiming that developers can shift this burden upstream into model training to get better task performance. If you can train the agent to work within a more diverse and realistic environment, it will perform better on longer and more complex tasks without as much supervision. Perhaps not everybody has drunk the Kool-Aid in terms of this approach yet, but it’s worth bringing it into the mix,” he adds.

Co-founder and CEO at AI tool data accuracy enforcement company Sphinx, [Rohan Kodialam](https://www.linkedin.com/in/rohan-kodialam-31b5a9234/) tells *The New Stack* that the pace of improvement in models is exactly why he wouldn’t build enterprise infrastructure around whichever model happens to lead today.

“OpenAI, Anthropic, Google and increasingly Chinese open-weight models are leapfrogging each other constantly,” Kodialam says. “We think business context should live independently of the underlying model, so companies can move between models without having to reteach the new system how their organization works. Model agnosticism is becoming less of a technical preference and more of a hedge against an AI market where nobody knows who will have the best model six months from now.”

He reminds us that once several models reach roughly comparable capability, choosing between them becomes much more about the workload than the leaderboard. Cost, latency, privacy, deployment model, tool use, and performance on your specific tasks can matter more than a few points on a benchmark.

> “Enterprises should avoid making their own model choices irreversible and build for portability as capabilities, economics, and infrastructure evolve.”

“But there’s also a global model choice happening beyond any individual enterprise: availability of compute shapes which models can actually operate at massive scale, and today far more infrastructure is dedicated to providers like OpenAI and Anthropic than newer alternatives like Z.ai’sn GLM,” adds Kodialam.

Even if every company wanted to switch tomorrow, the market as a whole couldn’t necessarily move with them, which is why Kodialam says developer teams should avoid making their own model choices irreversible and build for portability as capabilities, economics, and infrastructure evolve.

> “To put it simply – the Chinese labs use all the time that American labs do pre-release testing to keep hillclimbing on benchmarks.”

## Is Z.ai benchmaxxing the bencmarks?

Of the comparatively limited [posts on Hacker News](https://hn.algolia.com/?q=GLM-5.3) discussing GLM 5.3, ML researcher [Nathan Lambert](https://www.linkedin.com/in/natolambert/) is perhaps the most insightful. He cross-references [a post on his own Interconnects](https://www.interconnects.ai/p/glm-53-how-chinese-labs-keep-stride) site which questions just exactly how the Chinese labs keep up with Silicon Valley’s frontier glitterati.

First questioning whether or not the Far East frontier players are “[benchmaxxing](https://ctaio.dev/en/labs/benchmaxxing/)” i.e. pointing models at test sets to achieve good benchmark scores that fail to replicate in real world deployment scenarios (despite Z.ai telling us that it has built the latest model based on complex real world developer workflows), Lambert thinks that if there is any going on, it’s only to a subtle level.

“It is very, very likely that OpenAI and Anthropic have far better internal models than Z.ai and Moonshot AI. Still, these American companies [tend to take months to release their models to the public](https://www.theguardian.com/technology/2026/aug/08/openai-astra-security-concerns), which massively flatters the Chinese labs in adoption decisions at the frontier. To put it simply – the Chinese labs use all the time that American labs do pre-release testing to keep hillclimbing on benchmarks,” wrote Lambert.

## Autoregressively engineered to cloze the gap

The modestly titled GLM derives its name from the General Language Model training algorithm upon which the current model is now built. It relies on autoregressive blank infilling techniques, a model training technique that deletes or occludes sections of model data using [cloze tests](https://en.wikipedia.org/wiki/Cloze_test) to develop model vocabulary, comprehension and reasoning.

Fully open source, Z.ai confirmed it will release the GLM-5.2 weights two weeks after launch (approximately the last day of Aug 2026), once safety evaluation and hardening are complete.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)