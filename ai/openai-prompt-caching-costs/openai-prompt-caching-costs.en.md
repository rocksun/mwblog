OpenAI released [GPT-6 Sol and Luna](https://thenewstack.io/openai-gpt-6-sol-luna-release/) on Tuesday, essentially more affordable versions of GPT-6 Astra that [come closer to Astra on alignment than GPT-5.6 Sol did](https://thenewstack.io/gpt-sol-alignment-gaps/), but still fall short of the flagship model.

Most notably, the AI company slashed token prices, making the new GPT-6 models significantly cheaper to use. Beyond token prices, though, OpenAI says better caching can also help developers push costs down even more.

Per [OpenAI](https://openai.com/index/introducing-gpt-6-sol-and-luna/): “Improvements in caching and inference let us serve these models at lower cost,” with API prices for Sol and Luna down 50% compared to their GPT-5.6 counterparts (58% lower for Luna output tokens).

What improvements? Namely, higher cache-hit rates by default, the ability to preserve earlier context even when reasoning effort and tool availability change, and new tools to monitor and diagnose caching performance.

## Reuse context without starting over

Prompt caching isn’t, of course, novel to the new GPT-6 models themselves. But the upgraded Sol and Luna come with improvements designed to keep more previously processed context reusable as the agent moves forward on a task.

> “We’ve improved prompt caching for GPT‑6 to deliver higher cache hit rates by default, helping agents reuse more context, respond faster, and benefit from discounts of 90% on cached input-token reads.”

That adds another opportunity to lower the already low API price tag, though the 90% cached-input discount matches GPT-5.6 pricing; what’s new is how often the cache gets hit. By using cached context to reuse work it’s already done, the model doesn’t have to process the same context again from scratch for every single call, thereby reducing latency — and token costs.

Beyond this higher default cache-hit rate, OpenAI says the new GPT-6 models offer more flexibility to optimize caching performance.

The new models let developers adjust reasoning effort and tool availability without having to break the cache. This way, an agent can scale reasoning effort up and down based on how difficult a step is, then make different tools available depending on what the task requires without disturbing earlier cached context — again, a win for both speed and cost.

## See what gets cached and what doesn’t

GPT-6 Sol and Luna also arrive with a Prompt Caching Dashboard, where OpenAI says developers can view caching performance to understand how much context is reused.

Specifically, they can see how much input is cached and how that amount changes over time. The diagnostics tool then flags missed caching opportunities to help developers understand what could use more efficient caching.

Rather than keeping cache performance largely hidden behind the scenes, the idea is to make it more visible so developers can actively measure and optimize cache reuse.

Altogether, OpenAI says these caching improvements are already making a difference. Per the AI company, GitHub reports, “these improvements have reduced the share of prompt tokens requiring fresh processing by more than 50% across billions of requests to OpenAI models.”

These results span the past “several months.”

## Token prices aren’t the only way to make agents cheaper

OpenAI’s pricing cuts for GPT-6 Sol and Luna made the biggest splash, with the AI company significantly dropping API prices from GPT-5.6 levels.

Compared to the current prices for GPT-5.6 [Sol](https://developers.openai.com/api/docs/models/gpt-5.6-sol) and [Luna](https://developers.openai.com/api/docs/models/gpt-5.6-luna), which stand at $4 and $0.20 per million input tokens and $20 and $1.20 per million output tokens, respectively (GPT-5.6 Sol’s rates are promotional pricing), the new GPT-6 models come in at just $2 and $0.10 per million input tokens and $10 and $0.50 per million output tokens, respectively.

> With GPT-6 Sol and Luna’s caching improvements and lower token pricing, OpenAI is making the case for tackling agent costs from both sides: charging less for fresh processing and reducing how often the same context needs to be reprocessed.

But as more AI model providers compete aggressively on pricing, it’s becoming clearer that [cheaper models alone won’t save your AI budget](https://thenewstack.io/agentic-ai-token-costs/) — and lower token prices aren’t the only way to make agents cheaper.

With GPT-6 Sol and Luna’s caching improvements and lower token pricing, OpenAI is making the case for tackling agent costs from both sides: charging less for fresh processing and reducing how often the same context needs to be reprocessed.

As agents continue to work on longer and more complex tasks, there will likely be more pressure to do both.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)