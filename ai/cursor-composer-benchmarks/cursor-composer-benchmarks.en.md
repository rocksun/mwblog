Cursor announced this week that Composer 2.5 is available in Cursor, only two months after the [release of Composer 2](https://thenewstack.io/cursors-composer-2-beats-opus/), which beat Opus 4.6 on coding benchmarks at a fraction of the price. It’s another burst in the company’s streak of model releases, marking the fourth Composer in the last seven months.

Cursor says the latest iteration brings major upgrades to long-running coding tasks, complex instruction-following, and training efficiency, as well as behavioral improvements in “communication style and effort calibration,” but time will tell whether benchmark gains translate into real-world improvements.

## A cheaper contender in the coding model line-up

Like its predecessor, Composer 2.5 is built on [Moonshot Kimi K2.5](https://github.com/MoonshotAI/Kimi-K2.5), an open-source native multimodal agentic model, but should now outperform Composer 2 on intelligence and behavior.

In its [announcement](https://cursor.com/blog/composer-2-5#targeted-rl-with-textual-feedback), Cursor attributes these improvements to scaled training, more complex Reinforcement Learning (RL), and new learning methods. When you look at the benchmarks, it’s easy to see how Composer 2.5 has leveled up from Composer 2, moving from a 61.7% score on [Terminal-Bench 2.0](https://www.tbench.ai/) to 69.3% and from 52.2% to 63.2% on its own CursorBench v3.1.

And while Composer 2.5 still hasn’t surpassed Opus 4.7’s and GPT-5.5’s scores (save inching past GPT-5.5 by 2% on [SWE-Bench Multilingual](https://www.swebench.com/multilingual.html)), it’s definitely giving Anthropic and OpenAI a run for their money.

> But benchmarks are just that — benchmarks.

![](https://cdn.thenewstack.io/media/2026/05/2e01da0c-cursor-benchmarks.webp)

Image: Cursor

While the benchmarks offer an interesting, high-level comparison of the industry’s main contenders, they don’t provide any real assurance for how these models will perform in the real world.

As one [Redditor](https://www.reddit.com/r/vibecoding/comments/1tgyqoj/cursor_annonced_a_model_that_beats_opus_47_and/) commented: “Haven’t tested it yet but the benchmarks are wild. What’s interesting is that raw model performance doesn’t always translate to actual coding productivity. I’ve seen plenty of ‘better’ models still generate code that needs heavy cleanup or doesn’t fit the project context properly.”

> “Anyone who’s used Claude or GPT-4 for actual projects knows that intelligence on benchmarks ≠ usefulness in practice.”

Instead, they posit the real test of Composer 2.5 will come once it’s used to handle multi-file changes and if it can then maintain consistency with existing codebases: “Anyone who’s used Claude or GPT-4 for actual projects knows that intelligence on benchmarks ≠ usefulness in practice.”

## Cursor aims to improve long-running agent work

Cursor also says Composer 2.5 has leveled up on long-running coding tasks, for which it trained the model with targeted textual feedback to tackle tricky credit assignment during RL: “The idea is to provide feedback directly at the point in the trajectory where the model could have behaved better.”

By constructing and inserting short hints into the local context, Cursor aims to target specific mistakes while still retaining the bigger-picture RL objective.

With barely a day since release, it’s still too early to tell if this training will make a real difference, but an early glimpse at user feedback suggests the problem could still give developers trouble.

As one [Redditor](https://www.reddit.com/r/cursor/comments/1tha71k/composer_25_suddenly_believes_its_in_ask_mode/?show=original) notes, “Composer 2.5 starts to work in agent mode, then all of a sudden it thinks it’s in ask mode and stops to work. When I prompt it to continue it tries to understand where it was in the task and only finishes what it just was working on, yet forgets about everything else in the pipeline.”

## More synthetic data training, more unexpected reward hacking

According to Cursor, Composer 2.5 was trained on 25 times as many synthetic tasks as Composer 2, using a range of approaches to generate them. But such a breadth of synthetic task creation had at least one sour side effect: unexpected reward hacking.

As Cursor itself admits: “As the model became more adept, Composer 2.5 was able to find increasingly sophisticated workarounds to solve the task at hand,” such as reverse-engineering a Python type-checking cache.

## Are you always getting what you pay for?

Composer 2.5 costs $0.50 per million input tokens and $2.50 per million output tokens. Upgrading to the “faster” tier will put you back $3.00 per million input tokens and $15.00 per million output tokens — but you’re left with the same intelligence.

Whether or not the better latency is worth the sixfold price increase, one thing is for certain: Composer 2.5 is considerably cheaper than both [Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) and [GPT-5.5](https://openai.com/api/pricing/), with Anthropic’s model standing at $25 per million output tokens, OpenAI’s at $30 per million output tokens, and both companies at $5 per million input tokens.

Whether lower prices are enough to push developers to make the switch is the question. “We have to ask ourselves if Opus 4.7 is 10x better,” comments one Redditor, to which another replies: “For some tasks — yes. I’m not a huge fan of Composer for UI. But it’s great for small, targeted tasks. Also, he is excellent at explaining details.”

Either way, Cursor says an improvement is already in the works. Last month, Cursor announced a [partnership](https://cursor.com/blog/spacex-model-training) with SpaceX on model training. The company now teases that it is working with SpaceXAI to train “a significantly larger model from scratch, using 10x more total compute” that it expects “to be a major leap in model capability.”

Developers will have to wonder, given this week’s news about Composer 2.5’s prices, how much it’ll cost.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)