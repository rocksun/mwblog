MiniMax released M3.1 Flash on Monday, saying it cuts agent costs by 70 percent. Per-token prices fell by half, which accounts for part of that claim. The rest depends on how many tokens an agent spends to finish a job, and MiniMax hasn’t said how it measured that.

The [company](https://www.minimax.io/blog/minimax-m31f) lists $0.15 per million input tokens, $0.60 per million output tokens and $0.015 per million cached input tokens, and claims inference nearly three times faster than its predecessor, M3. That 70 percent figure is the one to test; a cheaper rate card only helps if the agent also finishes in fewer loops.

> That 70 percent figure is the one to test; a cheaper rate card only helps if the agent also finishes in fewer loops.

## What a task costs

A [study of token consumption in agentic coding tasks](https://arxiv.org/abs/2604.22750) found that repeated runs of the same task can use up to 30 times as many tokens, with input tokens accounting for most of the usage, which makes MiniMax’s 70 percent savings claim difficult to assess without knowing which workloads it tested.

[Artificial Analysis](https://artificialanalysis.ai/models/minimax-m3-1-flash) provides an independent comparison. In its [announcement](https://x.com/ArtificialAnlys/status/2112211865128608002), the firm puts the average cost per Intelligence Index task at $0.22 for M3.1 Flash, down from $0.51 for M3, a 57 percent reduction. That’s below MiniMax’s claimed 70 percent savings, though the two figures come from different workloads.

## Coding and computer use

The coding scores barely separate. M3.1 Flash lands at 73.7 percent on DeepSWE v1.1, a hair behind the 74 percent MiniMax lists for Claude Opus 5, its chosen comparison, and a point ahead of GPT-5.6 Sol at 73. *[VentureBeat](https://venturebeat.com/technology/minimaxs-new-m3-1-flash-beats-deepseek-and-opus-5-on-a-key-business-benchmark-at-lower-cost-but-with-a-high-hallucination-rate)* puts DeepSeek V4.1 Flash 1017 at 77 in the same table. Anthropic’s newer Opus 5.5 isn’t in that table, so if you’re benchmarking against the current Opus, run your own evals. On Artificial Analysis’s Intelligence Index, M3.1 Flash scores 42, tied with GLM-5.3 Flash, ahead of Gemini 3.8 Flash at 41 and behind DeepSeek V4.1 Flash 1017 at 45.

> Computer use is where the model looks weakest.

Computer use is where the model looks weakest. It scores 61.7 on OSWorld V2, which MiniMax says leads Chinese models, but VentureBeat notes it trails the strongest Anthropic and OpenAI models.

MiniMax also reports 82 percent on CyberGym and says its internal security experts rated the model strong at code auditing, patching, penetration testing, malware analysis, and reverse engineering. The launch post doesn’t say how those evaluations were run, so treat the security claims as MiniMax’s own until someone independent tests them.

## Confident answers, uncertain accuracy

The most consequential finding in the launch comes from Artificial Analysis’s AA-Omniscience benchmark. M3.1 Flash answered 56 percent of factual questions correctly, ahead of DeepSeek V4.1 Flash at 43 percent.

It attempted nearly every question, though, and about 93 percent of its non-correct responses were wrong answers rather than abstentions. Its overall Omniscience score was 16. [Artificial Analysis summarized the result](https://x.com/ArtificialAnlys/status/2112211865128608002) as high accuracy offset by a high hallucination rate.

Outside analysts reached a similar view. [*The Decoder*](https://the-decoder.com/minimax-m3-1-flash-shows-chinas-ai-price-race-has-no-floor-in-sight/) described the model as attempting every test question and not declining when it was unsure, so businesses using the model for knowledge-heavy work might want to add verification, retrieval, guardrails, or human review.

## When DeepSeek’s discount applies

DeepSeek is the natural comparison. Its [V4.1 Flash pricing](https://api-docs.deepseek.com/quick_start/pricing/) matches MiniMax’s $0.15 input and $0.60 output rates off-peak. Peak hours, 01:00 to 04:00 and 06:00 to 10:00 UTC on weekdays, double those rates, excluding Chinese public holidays. DeepSeek’s cached input costs $0.003 per million tokens, against MiniMax’s $0.015.

For a team in New York or San Francisco working in daytime hours, most requests land in DeepSeek’s off-peak window., but overnight batch jobs would fall in peak hours. The study above found that input tokens drive most agent costs, so the cache rate may matter more than the headline price.

## Space Bunny and what’s still unknown

Space Bunny was the mystery model that processed more than 200 trillion tokens before MiniMax confirmed it was an early build of M3.1 Flash. The release supports a one-million-token context window, so a large codebase fits in a single prompt. If you tested the preview, though, don’t assume its behavior matches the shipped version. Models change between preview and release.

The weights are coming, [reportedly on October 23](https://venturebeat.com/technology/minimaxs-new-m3-1-flash-beats-deepseek-and-opus-5-on-a-key-business-benchmark-at-lower-cost-but-with-a-high-hallucination-rate), though MiniMax’s own post just says “later.” The license is still unpublished, an important consideration for anyone thinking about running the model on your own hardware. A stronger Pro model is also on the way, with no date yet.

> A stronger Pro model is also on the way, with no date yet.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)