As the frontier model race accelerates, AI devotees are splitting their loyalty across the major providers at both the user and developer levels. Differences in inference are an accepted norm — but most assume that, at the highest level, frontier LLMs would agree on basic, real-world facts.

Except that’s not the case.

An analysis published this month on the claim-verification platform [Lenz](https://lenz.io/research/llm-disagreement) found that across 1,000 recent real-user fact-check claims — statements about the world asserted as true — a panel of five frontier LLMs split on 67% of them, meaning at least one model dissented from the majority verdict, or no clear majority formed at all.

## Pick a verdict from a 4-bucket rubric

The five models ([GPT](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/)-5.4, [Claude Opus 4.7](https://thenewstack.io/claude-opus-47-launch/), [Gemini 3 Pro](https://thenewstack.io/google-launches-gemini-3-pro/), [Gemini 3 Pro](https://thenewstack.io/googles-gemini-3-1-pro-is-mostly-great/) + Search, [Sonar Pro](https://thenewstack.io/how-developers-can-take-advantage-of-perplexitys-sonar-llms/)) were each given the same real-world claim and asked to pick a verdict from a 4-bucket [rubric](https://en.wikipedia.org/wiki/Rubric_(academic)) (True / Mostly True / Misleading / False). Because only one bucket can be correct per claim, any disagreement among the panel means at least one model is label-inconsistent.

According to Lenz, the “split across these five models is intentional” because it covers the spread of inference modes that are common in production AI systems.

## How many types of inference are there?

[Spanning from](https://www.gocodeo.com/post/from-data-to-understanding-how-ai-inference-works---engines-optimization-tricks-and-production-frameworks?utm_source=copilot.com) latency-sensitive inference to throughput-aware, resource-constrained and scalable inference, inference is typically divided into low-latency high-throughput inference (e.g. for interactive chatbots) and offline or batch inference, where processes accumulate data before it is subsequently analyzed, once optimized for cost.

> “Unlike the standard benchmark questions, the models have not seen these claims during training — i.e., it’s a fresh real-world corpus across science, healthcare, politics, law, and other domains.”

Research informing the May 21 paper was led by [Kosta Jordanov](https://www.linkedin.com/in/kjordanov/), founder of Lenz and co-founder of [Wiser](https://wisertech.com/), an IT consulting and software engineering group headquartered in Sofia, Bulgaria.

Jordanov tells *The New Stack* that the claims his team used in the research are real claims that users have fact-checked on Lenz since February 15, 2026.

## A fresh, real-world corpus of data

“We’ve excluded private claims, near-duplicate claims, and any claims containing personally identifiable information (PII),” Joranov says. “The interesting thing about this corpus is that, unlike the standard benchmark questions, the models have not seen these claims during training — i.e., it’s a fresh real-world corpus across science, healthcare, politics, law, and other domains on topics that people care about and fact-check.”

> Beyond the 67% dissent metric, 34% of the claims are substantially disagreed on

Beyond the 67% dissent metric, 34% of the claims are substantially disagreed on (2+ buckets apart), and 21% are polar opposites (at least one model says False and at least one says True). At this level, we can start to see the path from dissent to disagreement having a real impact on live production AI systems and tools.

> “If a software engineering team operates a system where legal, financial, or reputational risk is involved – and it delivers untrue or hallucinated content to users, you should think about the ways in which you validate the AI-generated content before it reaches users.” —Kosta Jordanov.

## What should AI developers think about this disconnect?

The practical takeaway is that on real-world claims, a single frontier LLM gives one opinion from a visibly unstable distribution. A second model often gives another.

“For many applications, that’s fine,” Joranov clarifies. “But if a software engineering team operates a system where legal, financial, or reputational risk is involved — and it delivers untrue or hallucinated content to users — you should think about the ways in which you validate the AI-generated content before it reaches users.”

The question arises, then, why do frontier models converge confidently at True/False poles but fracture badly on middle-ground verdicts? Unfortunately, that’s a hard question to answer based on this research. One hypothesis Joranov puts forward is that the Mostly True and Misleading categories are a bit more ambiguous than the True and False categories.

“What we measured, though, is that some models use the middle buckets way less often than others – Gemini is quite ‘confident’ and classified only 6% of the claims in the two middle buckets vs. 45% for Opus 4.7,” he says.

## Is Anthropic especially out of line?

Looking at the potential howlers here, if [Claude Opus 4.7](https://thenewstack.io/claude-opus-47-launch/) (which had [received early criticism](https://thenewstack.io/claude-opus-47-flaky-performance/)) aligned with the peer majority least often at 70%, should that concern Anthropic?

“Not necessarily,” clarifies Joranov. “Our limited preliminary research shows that the majority is often wrong, and sometimes we see wrong unanimous verdicts; i.e., having a different opinion than the majority does not necessarily mean being wrong.”

This research does not use any “ground truths” (indisputable real-world facts that have been widely validated and verified) and only measures the differences between the models’ verdicts. It cannot answer which model is correct for which claim.

> “Our analysis [of LLM accuracy] reveals that apparent convergence in benchmark accuracy can conceal deep epistemic divergence.” – Cornell University’s Yang & Wang.

## Other studies in this space

Academic and commercially underpinned model research appears to be turning to this space right now. A [study](https://arxiv.org/abs/2602.11898) by Eddie Yang and Dashun Wang at Cornell University published in February notes that benchmarks underpin how progress in large language models (LLMs) is measured and trusted.

“Yet our analyses reveal that apparent convergence in benchmark accuracy can conceal deep [epistemic divergence](https://www.linkedin.com/pulse/epistemic-divergence-predictive-artificial-when-machines-diamond-ggjse/). Using two major reasoning benchmarks — MMLU-Pro and GPQA — we show that LLMs achieving comparable accuracy still disagree on 16-66% of items, and 16-38% among top-performing frontier models,” wrote Yang & Wang in February.

## Humans in the loop next

Joranov confirms that this analysis is the first step.

“We do plan a follow-up where we measure the models against human-provided labels, and also measure the source-based multi-step multi-model Lenz pipeline against those labels and against the frontier models,” Joranov says. “The time-consuming part is the methodologically correct labeling by human experts in all of those domains, but we aim to publish in the coming months.”

This report concluded with a statement to explain that the point of this work isn’t to create a leaderboard.

The point is to map the structure of disagreement, i.e., where do frontier panels systematically diverge from a human consensus, where does Lenz diverge from both, how each individual model and Lenz align with the same human reference, and what categories of claims drive each kind of divergence (rubric ambiguity, temporal framing, domain specialization, calibration drift).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)