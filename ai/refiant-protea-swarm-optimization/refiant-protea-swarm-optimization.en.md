While the household-name [frontier models](https://thenewstack.io/googles-gemini-3-5-flash-beats-the-frontier-models/) race forward with version numbers and context windows of at least a million tokens, a new breed of upstart data science specialists is pushing the context window into double figures.

[Subquadratic debuted a](https://thenewstack.io/subquadratic-12-million-context-window/) 12-million-token window in May of this year, and Silicon Valley and South Africa-based [Refiant](https://refiant.ai/) launched its 10-million-token context-window model, Protea, on Wednesday. It’s a move that may signal the long-context AI race is now on.

## Model inefficiency & workarounds are commonplace

But [more context windows alone](https://thenewstack.io/do-enormous-llm-context-windows-spell-the-end-of-rag/) are not enough. This is because even the most capable models have a few hundred thousand tokens in working memory, which can force workarounds to compensate for what the model can’t access.

Refiant co-founder [Dr. Viroshan Naicker](https://www.linkedin.com/in/viroshan-naicker/) tells *The New Stack* that he believes modern LLMs “fail to be organically efficient at an elemental level” and that his organization’s approach mimics how systems in nature, from ant colonies to beehives, find efficient solutions to complex problems.

“This is no case of pseudoscientific puff; nature is the most computationally efficient system that we know, and many algorithms used in science are nature-inspired,” Naicker says. “This is a road well-traveled in science. There are multiple teams globally working in this particular (nature-inspired) direction, trying to bridge the gap between AI inference as we know it and the energy efficiency of natural systems.”

> “Fish and birds coordinate their movements to converge on the mathematically shortest, most efficient routes — honeybees, fireflies and bacteria are also programmed to use degrees of swarm-style optimization.”

## What can the birds & the bees teach us about AI?

Did Naicker just mention ant colonies and honeybees?

Yes, because Refiant uses swarm-style optimization. It’s seen in ant colonies, which initially move randomly until a food source is detected, after which they leave a pheromone trail for other ants to optimize their journeys. Fish and birds also coordinate their movements to converge on the mathematically shortest, most efficient routes. Honeybees, fireflies, and bacteria are also programmed to use degrees of swarm-style optimization.

Naiker, along with his co-founders, Siddharth Gutta and Mathew Haswell, form a team with experience spanning quantum mathematics, traditional finance, and commercial scaling. Applying swarm-style optimization to data in Protea means inference is performed through a combination of compression and context management.

“From our perspective, we are also advancing a technology which provides context-specific inference models grounded in data,” Naicker clarifies. “We think this has value for reducing model hallucinations, replacing RAG, and constructing better, more reliable, agentic workflows. This adds a layer of trust in sensitive application scenarios, rather like an added insurance, rather than taking it away.”

## Just how much is 10 million tokens?

The Refiant team describes 10 million tokens as equivalent to 7.5 million words in a single conversation (and we know from Anthropic’s own benchmarks this year that [Claude has a 1-million context window](https://www.claudecodecamp.com/p/claude-code-1m-context-window)), or five years of a user’s emails, 83 novels, or 830 podcast episodes, all held in active memory at the same time.

The team claims Protea is capable of working on entire enterprise codebases or decades of clinical trial data — datasets that previously had to be broken apart and fed to models in fragments — so they can be processed in a single pass with full fidelity. Engineers on Protea also submit that they can successfully tackle the “[lost in the middle](https://arxiv.org/html/2311.09198v2#:~:text=To%20overcome%20this%20crucial%20issue,step%20QA%20(PAM%20QA).)” problem — a limitation of million-plus-token windows, where models stay accurate at the start and end of the context but lose the thread of everything buried in between.

Refiant first applied these techniques to model compression, shrinking OpenAI’s GPT-OSS-120B so it could run on a MacBook Pro with 18GB of RAM.

> “Rather than publishing benchmarks, we’re inviting users to run the models and try them out.”

The Protea series is open and live, and Refiant is inviting teams to stress-test the context window across different industries and use cases. But should we trust sensitive hould enterprise data archives to a completely unproven startup founded only one year ago?

## Bring-your-own-cloud, a possible progression

“We adhere to data management best practices, processes and compliance requirements,” Naiker confirms. “This is reasonable for a startup at our particular stage. Privacy and data sovereignty are important values for us, and we are actively exploring edge, self-hosted, and bring-your-own-cloud data models.”

But a 10 million-token context window is big. Won’t that fall short when Protea starts to suffer from massive latency spikes when processing a full dataset? Naiker agrees that “latency is a core issue with long-context inference models,” but in the tests his company has run, it has delivered inference at a reasonable latency, even with large token windows.

“We have internal reports and tests that validate the technology, including [Ruler](https://arxiv.org/abs/2404.06654), [MRCR](https://llm-stats.com/benchmarks/mrcr) and [Babilong](https://arxiv.org/abs/2406.10149), but we aren’t asking anyone to take our word on this. Rather than publishing benchmarks, we’re inviting users to run the models and try them out,” adds Naiker.

## What comes next, a 100-million context window?

Although the technology industry is littered with apocryphal statements and Bill Gates almost certainly never said “64K ought to be enough for anyone” in real life, we have to ask ourselves today whether we’ll be laughing about those “silly little” 10 million token context windows by the end of the decade.

It may not take that long. Internally, Refiant maintains that it has already demonstrated a working prototype with a 100-million-context window and is exploring how best to benchmark and productionize it at that scale in the future.

Coming next, then, as [Dr. Evil from *Austin Powers*](https://www.youtube.com/watch?v=EJR1H5tf5wE) would say, the one-hundred-billion-context window, right?

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)