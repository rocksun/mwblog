**In 24 hours last week**, OpenAI and DeepSeek made opposite bets on what frontier AI is worth. One says it is a closed product that just got more expensive. The other says it is open infrastructure that just got dramatically cheaper. The price gap between the two ends of the market is now wider than it has been in years, and the comfortable middle that most coding agents have been routing through is thinning out.

Until last week, you could pick a model on a fairly smooth price-performance curve. There was a top tier, a middle tier, and a budget tier, and most workloads found a comfortable home somewhere on the slope. That curve still exists, but it has stretched. What used to be a continuous gradient now looks more like two clusters with a gap in between, and developers building agents, coding assistants, and high-volume inference pipelines now have to think harder about which side to route to.

> The comfortable middle that most coding agents have been routing through is thinning out.

## The 24-hour split

On April 23, OpenAI shipped [GPT-5.5](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/), priced at $5 per million input tokens and $30 per million output tokens. That is exactly double the GPT-5.4 rate of $2.50 and $15. The model uses a 1M token context window and scores 82.7% on Terminal-Bench 2.0, up from 75.1% on GPT-5.4. OpenAI argues that the price hike is offset by token efficiency, claiming that GPT-5.5 uses fewer tokens to complete the same Codex task. The company has not published a precise effective-cost figure on its launch page, so the per-task economics depend on the workload.

On April 24, DeepSeek [released](https://api-docs.deepseek.com/quick_start/pricing) V4-Pro and V4-Flash. V4-Pro is listed at $1.74 per million input tokens and $3.48 per million output tokens, with a launch discount documented through May 5, 2026. V4-Flash is priced at $0.14 input and $0.28 output. Both ship under the MIT license with full open weights on Hugging Face, and both default to a 1-million-token context window. V4-Pro hits 80.6% on SWE-bench, verified per the model card, within striking distance of Claude Opus 4.6.

Two pricing announcements in one weekend, in opposite directions. At list price, V4-Pro output tokens cost roughly one-ninth as much as GPT-5.5 output. Under the launch discount, the gap widens further. V4-Flash sits another order of magnitude below that. The arithmetic is striking. The framing matters more.

## The widening gap for AI costs

| **Model** | **Input (per 1M)** | **Output (per 1M)** | **Context** |
| --- | --- | --- | --- |
| **Open AI GPT-5.5** | $5.00 | $30.00 | 1M Tokens |
| **Anthropic** **Opus 4.7** | $5.00 | $25.00 | 1M Tokens |
| **DeepSeek** **V4-Pro** | $1.74 | $3.48 | 1M Tokens |
| **DeepSeek** **V4-Flash** | $0.14 | $0.28 | 1M Tokens |

## What OpenAI is actually selling

GPT-5.5 is not just a smarter model. It is the centerpiece of a stack. [Codex](https://thenewstack.io/openais-codex-is-now-on-windows/) inherits the upgrade with expanded computer use, browser interaction, and longer agentic runs. ChatGPT is the default for the Plus, Pro, Business, and Enterprise tiers. The API gets it with the same 1M context window the consumer surface now has.

The bet is that intelligence, the serving stack, the agent harness, and computer use are one product, and that product is worth twice the per-token price of the previous generation. Greg Brockman framed it during the launch briefing as a model that takes a sequence of actions, uses tools, checks its own work, and keeps going until a task is finished. The customer is the enterprise that wants the whole thing from a single vendor, with a single API key, a single safety review, and a single billing line. OpenAI is not selling tokens. It is selling outcomes, and outcomes are now priced accordingly.

> OpenAI is not selling tokens. It is selling outcomes, and outcomes are now priced accordingly.

This also explains the cadence. [GPT-5.4](https://thenewstack.io/openai-launches-gpt-5-4/) shipped in early March. GPT-5.5 followed six weeks later. That is not a benchmark race. It is an enterprise procurement strategy. OpenAI is releasing fast enough to stay the default in every Q3 budget conversation, and pricing high enough to fund the next training run without diluting the premium positioning. The closed product is the moat.

OpenAI has not retired the cheaper tiers. GPT-5.4, GPT-5.4 mini, and GPT-5.4 nano remain on the price list, alongside Batch, Flex, Priority, and cached input rates. The middle of the OpenAI catalog still exists. What changed is where the flagship sits, and the flagship is what coding agents and frontier workloads default to.

## What DeepSeek is actually shipping

V4 is not a price war move. The pricing is downstream of three different decisions.

The first is architectural. V4-Pro is a Mixture-of-Experts model with 1.6 trillion total parameters and 49 billion active per token. V4-Flash runs 284 billion total with 13 billion active. DeepSeek’s [model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) describes a hybrid attention scheme that combines compressed sparse attention with heavily compressed attention, designed to reduce 1M-token inference FLOPs and KV cache. The model achieves near-frontier benchmark scores while activating a small fraction of its weights per token. Smarter architecture, less compute.

The second is distribution. The MIT license is the most permissive open-source license available. Anyone can download the weights, host them, fine-tune them, embed them in a product, and ship that product commercially. V4-Flash at 13B active parameters runs on a multi-GPU cluster that mid-size teams can afford. V4-Pro requires more serious infrastructure, but the option exists. DeepSeek is betting that frontier intelligence becomes infrastructure the way Linux did, and that the lab releasing the weights captures the ecosystem rather than the runtime margin.

> DeepSeek is betting that frontier intelligence becomes infrastructure the way Linux did, and that the lab releasing the weights captures the ecosystem rather than the runtime margin.

The third is hardware. On the same day, Huawei [announced](https://www.huaweicentral.com/ascend-ai-supernode-fully-supports-deepseek-v4-model-huawei/) that its Ascend supernodes offer full support for V4 inference. Reuters [reported](https://www.investing.com/news/economy-news/factboxdeepseekv4-the-chinese-ai-model-adapted-for-huawei-chips-4636025) that V4 was adapted for Huawei’s most advanced Ascend AI chips and that Huawei said its chips were used for part of V4-Flash’s training.

DeepSeek did not say whether V4-Pro was trained on the same hardware as the earlier V3 and R1 models, which ran on Nvidia. SMIC, the Chinese contract manufacturer that fabricates Ascend silicon, jumped 10% in Hong Kong trading on the news.

Hua Hong Semiconductor jumped 15%. The narrower signal is that high-end open-weight inference, and at least part of one model’s training, can be adapted to the Ascend stack. That is not the same as full independence from Nvidia, but it is the first frontier-tier release where the question is even worth asking.

One important caveat: DeepSeek V4 is text-only at launch. DeepSeek has stated that multimodal capabilities are in progress, but image and video are not yet supported. For workloads that require multimodal reasoning, V4 is not a drop-in alternative to GPT-5.5 or Opus 4.6 today.

Cheaper inference is the consequence of these three decisions, not the strategy. The strategy is to make text intelligence look like a commodity.

## The middle is thinning, not gone

Before last week, a developer building a coding agent had a comfortable middle option. GPT-5.4 at $2.50 and $15 sat in a sweet spot. Cheap enough to scale, smart enough for most agentic work, hosted by a vendor everyone trusts. That tier is still on the price list, but it is no longer the flagship, and the new flagship costs twice as much.

GPT-5.5 took the upper slot at $5 and $30. V4-Pro took the lower slot at one-ninth of GPT-5.5 on output, before any discount. V4-Flash sits another order of magnitude below that. [Anthropic’s Opus 4.7](https://thenewstack.io/claude-opus-47-launch/) at roughly $5 input and $25 output sits next to GPT-5.5 in the premium tier, not in the gap between premium and open-weight.

For developers, the choice is no longer purely about which model is on a smooth curve. The choice is which economics to route to for which task. Pay for the integrated product or run the open infrastructure. Many production stacks will end up routing across both because the price gap is now wide enough to justify the engineering cost of routing logic.

## What this means for the harness layer

Three concrete shifts follow from the polarization.

The first shift is that agent harnesses become more model-agnostic by necessity. Cursor, Claude Code, OpenAI Codex, and the open-source harnesses OpenClaw and Hermes Agent now all benefit from clean routing logic that can move workloads between the two economies based on task complexity.

A coding agent that uses GPT-5.5 for the planning step and V4-Flash for the bulk-edit step is no longer exotic. It becomes an obvious architecture once the price gap is this wide. DeepSeek has noted that V4 is optimized for agent tools, including Claude Code and OpenClaw, suggesting the harness ecosystem has been waiting for this.

The second is that self-hosting math changes for the first time in two years. V4-Flash at 284B total parameters and 13B active runs on multi-GPU setups that mid-size teams can afford. The trade-off is real. You give up the managed reliability of a hyperscaler API in exchange for predictable inference costs and full control over the model. For workloads where token volume is the binding constraint and multimodality is not required, that trade-off is now sharper than it was a week ago.

The third is that the Nvidia-only assumption is starting to look less absolute. The market reaction to V4 was not solely about DeepSeek. It was about the realization that a frontier-tier model can ship optimized for non-Nvidia silicon, and that Chinese AI infrastructure is closer to running on domestic chips than most observers assumed a year ago. For developers, this expands the long-run set of viable inference targets. For Nvidia, it tightens the timeline on the China question.

## What’s next

The cost frontier no longer behaves like a smooth curve. It is two clusters of economics with a stretched gap in the middle, and the gap is not going to close on its own in the near term. OpenAI will continue to release fast and price up, because the integrated product is the moat. DeepSeek will continue to release open weights and price down, because the commodity infrastructure thesis depends on adoption. Both can be right for different workloads, and the same agent can route between both within a single task.

Anthropic’s Claude Opus 4.7 sits in the premium tier with OpenAI for now, but the next 90 days will reveal whether anyone tries to defend the thinning middle. The Chinese open-weight competition behind DeepSeek (Qwen, Kimi, GLM) will face pressure to match V4’s pricing and feature set, or risk ceding ground. And the harness layer is about to become the most interesting place in the stack, because routing logic across two economics is no longer optional. The next piece will look at how the open-source harnesses are positioning for exactly this moment. Stay tuned.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)