Not your keys, not your coins. Not your model, not your data?

Over the summer, the tech industry was [consumed by a debate](https://www.cnbc.com/2026/08/03/palantir-karp-open-ai-anthropic-open-weight.html) about AI use in the enterprise and the need to protect IP. If an enterprise used proprietary models, was data leakage a necessary evil?

VIDEO

Companies seemed to have two options: They could use state-of-the-art, proprietary models and risk losing control of their data, or they could use open-weight models and never kiss the frontier.

Thankfully, a third option is emerging.

Consider the concern: Company A wants to use LLM B from AI Lab C, and they want to avoid training AI Lab C how to eat Company A’s lunch by building its capabilities into LLM B. A good way to resolve the tension would be to let Company A run LLM B on its own infrastructure, so there’s no risk of its information fleeing on the wind.

> AI agents are “creating a whole different set of requirements at the data layer.”   
> –Vast Data co-founder Jeff Denworth

But that raises *another* problem: AI Lab C doesn’t want to allow Company A to run LLM B on its own GPUs because it doesn’t want to hand over its model weights. It’s the same IP issue the company ran into, in reverse. You have to solve the trust problem in both directions!

Enter [VAST Data](https://www.vastdata.com/) co-founder [Jeff Denworth](https://linkedin.com/in/jeffreydenworth) and a new product called [DataEnclave](https://www.vastdata.com/press-releases/vast-data-introduces-dataenclave-to-bring-leading-ai-models-and-enterprise-data-together-on-trusted-infrastructure), which aims to let AI labs and enterprise-scale companies deploy proprietary models in secure compute environments without risking data transfer in either direction. (DataEnclave uses Nvidia’s Confidential Computing technology to make the system tick; Vast Data’s core product is AI OS, infrastructure that fits beneath a company’s AI applications.)

*The New Stack* had Denworth on the podcast to chat about the confidential computing market. I was curious about timing. *Why did Vast build DataEnclave now?* Nvidia began rolling out Confidential Computing [in a serious way](https://developer.nvidia.com/blog/?p=81376) in 2024, after all. Denworth argues that the market needed the core technology, yes, but also demand.

And until late 2025, AI demand was modest compared to today’s token totals. Once agentic coding tools took off, corporate demand for AI products soared. This led to the pricing crisis we saw in early 2026, and the secure AI usage debate we endured over the summer.

Performance drove demand, demand drove usage, and usage dug up fresh problems to solve. Now the question for the market is whether or not DataEnclave has solved enough concerns on both sides of the *proprietary AI-proprietary data* equation. The market will sort that out as it moves through early access and into general availability.

Our conversation goes deep into the arc of AI, where companies are in their AI journey today, and how much data remains to be unlocked inside the enterprise. If you want to feel the acceleration, it’s a fun one!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/04/03000ee4-cropped-4cd6e98e-image.png)

Alex Wilhelm is a journalist focused on technology and finance. He co-hosts the This Week in Startups podcast, and writes the Cautious Optimism newsletter. He was previously Editor in Chief of TechCrunch+.

Read more from Alex Wilhelm](https://thenewstack.io/author/alex-wilhelm/)