Investor Matt Turck, whose [fantastic podcast](https://www.mattturck.com/podcast) has hosted the people who built [ARC-AGI](https://arxiv.org/pdf/2603.24621), summed up Astra’s blockbuster benchmarks with three words: “[This is wild](https://x.com/mattturck/status/2095653093148885274?s=20).” Then he added four more in parentheses: “w/ its native harness.”

[ARC Prize ran GPT-6 Astra through its own standard harness](https://arcprize.org/blog/astra), and the model scored 62.7%. When run through OpenAI’s Provider Adapter, the same model in the same reasoning setting scored 98.6%. The model didn’t change, but the software around it did, adding 36 points to the score. And the better-performing system cost less: $17,332 with OpenAI’s adapter versus $26,098 with ARC Prize’s.

That’s why harness engineering is becoming as important as model selection. The software around the model can change both what it accomplishes and what it costs.

## The benchmark measures the system, not the model

ARC-AGI was built to resist the brute-force scaling that eats so many other benchmarks. ARC-AGI-3 raised the bar again this year by dropping a model into interactive environments with no instructions, no stated goal, and no stated rules, then scoring how efficiently it learns to operate. When [ARC Prize launched it this year](https://arcprize.org/blog/arc-agi-3-launch), humans scored 100%. Frontier AI scored 0.51%.

On Thursday, [Amanda Caswell covered OpenAI’s improving score on the ARC-AGI-3 benchmark](https://thenewstack.io/astra-arc-agi-benchmark/). As she noted, Astra ran under different settings from competing models. ARC Prize is specific about what those settings do. Its standard harness lets a model carry forward notes it chooses to keep. OpenAI’s adapter preserves the opaque reasoning state between requests and compresses longer conversations, so the model can resume its own thinking instead of reconstructing it.

ARC Prize published every reasoning level.

Same model, two harnesses

GPT-6 Astra on ARC-AGI-3, by reasoning effort. At every setting, the run
inside OpenAI’s Provider Adapter scored higher and cost less than the same model inside
ARC Prize’s standard harness.

| Reasoning effort | ARC Prize standard harness | OpenAI Provider Adapter |
| --- | --- | --- |
| Max | 62.7% for $26,098 | 98.6% for $17,332 |
| XHigh | 59.3% for $37,317 | 98.4% for $18,147 |
| High | 54.8% for $40,705 | 99.9% for $18,817 |
| Medium | 38.6% for $48,090 | 98.4% for $19,285 |
| Low | 17.5% for $38,166 | 98.0% for $21,298 |
| None | 35.2% for $49,791 | 96.7% for $23,457 |

Astra inside OpenAI’s harness with no reasoning effort at all scored 96.7% for $23,457. The same model at max reasoning within ARC Prize’s standard harness scored 62.7% and cost $26,098. The harness beat the reasoning dial outright. I’ve been arguing [the harness matters](https://thenewstack.io/cursor-sdk-harness/) for months. I didn’t expect the result to be this lopsided.

The score wasn’t the only gap. Across the 167 game-reasoning pairs both harnesses solved, ARC Prize clocked the Provider Adapter runs at 49% fewer tokens and roughly 3.66x faster.

OpenAI isn’t hiding the details: The adapter runs on documented Responses API capabilities anyone can call. What you can’t buy is the assembled system that scored 98.6%.

That’s also why OpenAI President Greg Brockman’s claim during a press briefing this week — “I think it’s not unreasonable to feel that we are now in the AGI era” — lands harder than it should. Brockman is describing a benchmark result produced by a particular system, not establishing that the underlying model is AGI. [Frederic Lardinois’ launch coverage for *The New Stack*](https://thenewstack.io/openai-gpt6-astra-benchmarks/) gets the distinction right: The framing goes well beyond what the evidence establishes. Maybe we’re in the AGI era. But this benchmark doesn’t prove it.

## The harness is becoming the product

On coding, the frontier models now cluster inside a few points. *Artificial Analysis* [scores its Coding Agent Index](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra) by running each model inside a harness rather than on its own: Astra in Codex at 67, Opus 5 and Fable 5 in Claude Code at roughly the same, Muse Spark 1.3 in Muse Code alongside them, and Fable 5.1 in Claude Code leading at 70. The unit being measured is already the pair.

The labs already figured this out. Back in April, [Janakiram MSV documented the four-way split](https://thenewstack.io/ai-agent-harness-pricing-split/): Anthropic, OpenAI, Google, and Microsoft all treat the harness as a product to sell, and disagree only on how to charge for it. Anthropic meters Managed Agents at $0.08 per session hour, in addition to token rates. OpenAI gave its Agents SDK away with no runtime fee at all. Google and Microsoft bill sessions, memory, code execution, and observability as separate line items.

Nobody is treating the harness as a free accessory to the model.

Other companies are moving the same way. Stripe paid a reported $8 billion for OpenRouter in August, [as Paul Sawers reported for TNS](https://thenewstack.io/stripe-acquires-openrouter-tokens/), acquiring a gateway that routes 10 trillion tokens a day across more than 400 models for 10 million developers. Patrick Collison’s framing was that tokens are the central currency for companies building with AI. Stripe bought the routing layer that sits in front of the models. Nvidia built a harness of its own.

We covered the proof two weeks ago. [Adrian Bridgwater reported](https://thenewstack.io/nvidia-avo-arcagi3-benchmark/) that Claude Opus 5 scores 30.2% on ARC-AGI-3’s public set on its own. Wrapped in Nvidia’s AVO, which gives it persistent memory and programmatic supervision that steps in when progress stalls, it cleared all 183 levels across 25 environments. That one isn’t the clean A/B that ARC Prize ran on Astra. Nvidia changed the memory, supervision, and context management at once. More than one variable moved.

Nvidia said it beautifully [here](https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform): “Model capability matters enormously, but the surrounding system determines how effectively that capability can be converted into sustained autonomous progress.”

## Harness engineering is the job

[Janakiram MSV found token usage varying](https://thenewstack.io/agent-harness-token-costs/) 70-fold across Aider, Claude Code, and OpenClaw running an identical model. Cache hit rates swung from about 70% down to 1.5% depending on the serving path. No model choice explains a spread like that.

The work itself is pretty ordinary. Deciding what an agent remembers and what it forgets. What it’s allowed to touch, and when it has to stop and check with a person. [Jeremy Daly’s piece on our site](https://thenewstack.io/building-ai-agent-harness/) is the version with the engineering, and it’s the one to read if you’re the one building.

I argued in June [that model triage was the skill worth hiring for](https://thenewstack.io/claude-fable-cost-model-triage/). I’d revise that. Picking the model is the easy half, and it gets easier every quarter as the frontier converges. A year from now, I think the people running agents will spend less of the week picking models and more of it building what goes around them.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)