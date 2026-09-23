**OpenAI on Tuesday released GPT-6 Sol and Luna**, which will complement the flagship [GPT-6 Astra](https://thenewstack.io/openai-gpt6-astra-benchmarks/) model in OpenAI’s lineup. As of now, there is no GPT-6 Terra.

## The new GPT-6 pricing

The headline news here is that OpenAI cut the price per million input/output tokens by half or more, compared to the previous version. [GPT-6 Sol](https://developers.openai.com/api/docs/models/gpt-6-sol) will cost $2/$10 per million input/output tokens (vs. $4/$20 for [GPT-5.6 Sol](https://thenewstack.io/gpt-sol-chatgpt-split/)), and [GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) will come in at $0.10/$0.50 (vs. $0.20/$1.20).

The GPT-5.6 pricing was always meant to be promotional, but for the new GPT-6 models, this is the default price, an OpenAI spokesperson tells *The New Stack*.

“Improvements in caching and inference let us serve these models at lower cost, and we’re passing those savings directly on to users and customers,” OpenAI explains in its announcement.

## Benchmarks

As you would expect, the new models show clear improvements over the GPT-5.6 predecessors, but for the most part, these are not all that extreme.

On a benchmark like [Zapier’s AutomationBench](https://zapier.com/benchmarks) — which checks how well the models work on a set of business workflow tests — GPT-6 Luna improves by 5.4 percentage points over the previous version, for example

![](https://cdn.thenewstack.io/media/2026/09/6d66096b-screenshot-2026-09-22-at-15.14.57.png)





*Credit: OpenAI*

On the DeepSWE v1.1 software engineering benchmark, GPT-6 Sol essentially matches [Anthropic’s Fable](https://thenewstack.io/how-anthropic-is-bringing-fable-5-back/) (68.8% at max effort vs. 69.9% for Fable 5 at xhigh effort), but at only 20% of the cost. Luna, at max effort, hits scores similar to Claude Opus 5 and Fable 5 at medium effort, at a significantly lower cost.

And OpenAI focuses on this cost comparison across its announcement—with a special focus on price per task instead of straight-up token pricing.

![](https://cdn.thenewstack.io/media/2026/09/aedcdb5f-screenshot-2026-09-22-at-15.14.28.png)





*Credit: OpenAI*

## Anthropic resets the comparison

Since Anthropic [released Opus 5.5 earlier on Tuesday](https://thenewstack.io/claude-opus-5-5-release/), OpenAI’s comparisons are already out of date — such is the way of this AI era. Anthropic, too, reduced its per-token pricing for Opus 5.5 to $4/$20, down from $5/$25, but that still leaves Anthropic’s model twice as expensive as the comparable GPT-6 Sol.

In its announcement, when comparing GPT-6 Sol to Opus 5, OpenAI was able to claim significant cost savings when compared to Anthropic’s model — and for the most part that still holds, but Anthropic says Opus 5.5 also uses fewer tokens per task, which, according to the company, works out to 40% lower costs than Opus 5 on typical workloads.

It’s worth noting that no one has run Sol and Opus 5.5 head-to-head yet. Sol likely stays cheaper per task on OpenAI’s AutomationBench numbers, but Opus 5.5 posts higher scores than GPT-5.6 Sol on shared benchmarks in Anthropic’s testing.

Since it’s almost impossible to know how many tokens an agent will use to finish a task, though, these pricing changes still don’t make it any easier for a user to budget.

### Prompt caching

For developers building agents, the caching changes may matter more than token prices. OpenAI says it improved prompt caching for GPT-6 to deliver higher cache hit rates by default, with discounts of up to 90% on cached input tokens.

One positive change, too, is that developers can now change the reasoning effort and tool availability without invalidating the cache. With explicit breakpoints, developers can choose where a cached prefix ends, and a new dashboard and diagnostics tool show what’s getting cached and what isn’t.

GitHub says these improvements cut the share of prompt tokens that require fresh processing by more than half over the past several months, across billions of requests to OpenAI models.

Anthropic made a similar move with Opus 5.5, which cuts cache read prices by 60% for token-billed usage, on top of the 20% per-token cut.

## Style changes

Models aren’t just about benchmarks, though. With GPT-6 Sol, OpenAI made its models answer more directly, rather than in the previous — already reined-in — more conversational style. “Expect to see more clarity, less jargon, fewer odd turns of phrase, fewer low-value details, and slightly shorter answers overall without losing substance,” OpenAI says.

![](https://cdn.thenewstack.io/media/2026/09/3055e717-screenshot-2026-09-22-at-08.16.44-1024x441.png)





*Credit: OpenAI*

### Alignment

Given the [HuggingFace incident](https://thenewstack.io/openai-huggingface-sandbox-breach/), it’s no surprise OpenAI is emphasizing its alignment work for GPT-6 Sol and Luna, too.

OpenAI says both models improve on their GPT-5.6 counterparts across its alignment evaluations, including fewer misleading claims about their own coding work. On an internal coding deception test, GPT-6 Sol’s rate fell to 1.3% from 10.4%.

When given a deliberately broken search tool — and graded on whether it disclosed the problem instead of guessing — Sol failed to disclose the problem 4.9% of the time, down from 77.5%.

What is a bit more concerning, though, is that when researchers asked the model to respect an explicit warning like an “access denied” message, GPT-6 Sol still tried to work around those restrictions in 64.4% of runs, down only slightly from 68.2% for its predecessor. Luna improved more, to 42.4% from 76.5%.

OpenAI says these tests cover mostly low-stakes situations and run without full system-level safeguards used in its products.

![](https://cdn.thenewstack.io/media/2026/09/9b78897a-screenshot-2026-09-22-at-15.12.20.png)





*Credit: OpenAI*

On a simulated message board seeded with unauthorized instructions, including requests to disclose private information, Sol took the specified action in 11.3% of runs where it found the board, down from 51.9%. Luna and Astra took none, though OpenAI notes Luna also found the board less often.

Anthropic, by contrast, says Opus 5.5 is the strongest performer on its most comprehensive alignment test and names METR and Frontier Design as pre-release external testers. Opus 5.5 also ships with safeguards that reroute requests, sending most cybersecurity tasks to Opus 4.8 and anything flagged by Anthropic’s biology or frontier LLM development classifiers to Opus 5.

### Availability

GPT-6 Sol and Luna are available in ChatGPT Work and Codex starting Tuesday for Plus, Pro, Business, Enterprise, and Edu users.

Free and Go users get Luna in the desktop app.

Neither model is in Chat yet. OpenAI says it plans to roll them out gradually throughout the day to keep service stable, so they may not appear right away.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)