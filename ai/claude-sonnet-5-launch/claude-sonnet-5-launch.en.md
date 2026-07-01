Anthropic on Tuesday [launched Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5), the latest model in its mainstream Sonnet series.

The company calls Sonnet 5 its “most agentic Sonnet model yet,” and in benchmark terms, its performance is close to [Opus 4.8](https://thenewstack.io/claude-opus-48-release/) and represents a notable improvement over [Sonnet 4.6](https://thenewstack.io/claude-sonnet-46-launch/). Anthropic specifically notes that it performs much better on tasks involving reasoning, tool use, software coding, and knowledge work.

Unlike with some previous Sonnet launches, it doesn’t quite outperform the most recent version of the larger Opus model, but it is close enough to be a more affordable alternative to Opus 4.8 for the time being — because Opus 5 can’t be far behind (assuming it isn’t [held back in the same way that Fable 5 was](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/)).

Anthropic stresses that Opus 4.8, especially at higher reasoning levels, will still offer higher accuracy. but also notes that “Sonnet 5 provides developers with lower-priced options that are of much higher quality than what was previously available.”

![](https://cdn.thenewstack.io/media/2026/06/679e5683-screenshot-2026-06-30-at-10.12.37-am-1024x481.png)

*Sonnet 5 benchmarks. Credit: Anthropic*

At its maxed-out Extra High reasoning level, Sonnet 5 performs about in line with Opus 4.8’s medium-to-high setting on the OSWorld-Verified and agentic search BrowseComp benchmarks. But since that’s also more expensive to run than Opus 4.8 at the comparable reasoning level, Opus 4.8 will still be the better option for some tasks.

![](https://cdn.thenewstack.io/media/2026/06/d5d68e3d-screenshot-2026-06-30-at-10.33.20-am-1024x570.png)

*Credit: Anthropic*

Sonnet 5, at least on the benchmark Anthropic has made available so far, always outperforms [Sonnet 4.6](https://thenewstack.io/claude-sonnet-46-launch/).

Benchmarks only tell part of the story, though. Model behavior also impacts how users perceive the model, and Anthropic says that its testers noticed that the model now often completes complex tasks,  
“where previous Sonnets would stop short,” for example.

## Sonnet 5 pricing

To make Sonnet 5 even more attractive to developers (and maybe free up some capacity from running Opus 4.8), Anthropic is offering an introductory price for API users at $2 per million input tokens and $10 per million output tokens until August 31. It will go up to $3/$15 per million input/output tokens, as Anthropic has previously charged for Sonnet models.

When asked if this is the first time Anthropic has offered introductory pricing, an spokesperson told *The New Stack*: “We want our customers to test Sonnet 5 against their real workloads at the lowest possible cost during the migration window.”

For the time being, Anthropic has also increased rate limits for Chat, Cowork, and Claude Code users to, as the company puts it, “to accommodate the higher token usage of higher effort levels.”

## Sonnet 5 safety

In terms of AI safety, which is obviously a focus for Anthropic, especially after Fable 5’s unceremonious departure, Anthropic notes that it didn’t “deliberately train Sonnet 5 on cybersecurity tasks” and that while it can handle some routing cyber tasks, its performance on these tests is far behind Opus 4.8 and, of course, Mythos. Still, Anthropic kept its cyber safeguards on for this model, but since the risk is low, those safeguards are not as strict as those for models like Fable 5.

The company explicitly notes that when trying to find exploits in [Firefox 147](https://www.firefox.com/en-US/firefox/147.0/releasenotes/), for example, “Sonnet 5 was never able to develop a full working exploit, but it does show a slightly higher rate of partial success than its predecessor, Sonnet 4.6.”

The risk of the U.S. government pulling Sonnet 5 out of circulation is quite low, then, it seems.

![](https://cdn.thenewstack.io/media/2026/06/7b24b9a5-screenshot-2026-06-30-at-10.42.15-am-1024x570.png)

*Credit: Anthropic*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)