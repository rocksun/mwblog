On Wednesday, Anthropic made available Claude Opus 4.7, a direct upgrade to Opus 4.6 that may outperform its predecessor on complex, long-running tasks but is “less broadly capable” than the now almost-mythic [Claude Mythos Preview](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) released last week.

Now available across all Claude products and Anthropic’s API (as well as Amazon Bedrock, Google Cloud’s Vertex AI, and Microsoft Foundry) at the same pricing as [Opus 4.6](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/), Anthropic’s announcement says Opus 4.7 boasts better instruction-following, vision, creativity, memory, and finance analysis.

## What Anthropic says Opus 4.7 does better

Anthropic reports that Opus 4.7’s early-access testers, including Intuit, GitHub, and Notion, had strong feedback.

For one, where previous Claude models may have read between the lines when following user instructions (or skipped directions entirely), the newest iteration is reportedly better at doing as it’s told.

> The newest iteration of Claude Opus is reportedly better at doing as it’s told.

Interestingly, Anthropic’s announcement notes that this updated capability means that “prompts written for earlier models can sometimes now produce unexpected results.” In turn, Claude users may need to adjust their prompt-writing style to account for Opus 4.7’s more literal instruction-following.

> “Prompts written for earlier models can sometimes now produce unexpected results.”

Better vision for high-resolution images is also promised — and with it, more multimodal uses. Opus 4.7 users should expect the model to accept images with more than three times the pixels as those previously, leading the way for more uses that rely on finer visual detail, such as reading dense screenshots.

More vaguely, Anthropic calls out Opus 4.7 as “more tasteful and creative when completing professional tasks,” pointing to feedback from some of its early-access testers to support the model’s reportedly “higher-quality” interfaces, slides, and docs:

> “The design taste is genuinely surprising — it makes choices I’d actually ship,” states Aj Orbach, co-founder and CEO of Triple Whale in Anthropic’s blog post.

“The design taste is genuinely surprising — it makes choices I’d actually ship,” states Aj Orbach, co-founder and CEO of Triple Whale, in Anthropic’s blog post.

Next on the Opus 4.7 menu is enhanced memory. Anthropic’s announcement states the new model is “better at using file system-based memory,” allowing it to both remember and reference notes from task to task, thereby freeing users from repeatedly providing up-front context.

Finally, in its announcement blog post, Anthropic highlights Opus 4.7 as state-of-the-art on [GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa), a third-party evaluation that tests large language models (LLMs) on real-world, economically valuable tasks in domains such as finance and law.

Meanwhile, the AI company says its internal test marks Opus 4.7 as “a more effective finance analyst than Opus 4.6” thanks to its rigorous analyses, more professional-looking presentations, and tighter integration across tasks.

## What about safety?

While Opus 4.7 touts improved instruction-following, vision, and memory, it makes little progress in the way of safety.

Stacked against Opus 4.6, which was released in February, the new model shows similarly low rates of deception, sycophancy, and cooperation with misuse, per Anthropic’s tests, with reported improvements in honesty and resistance to prompt-injection attacks.

But Opus 4.7 does have one safety downgrade: According to Anthropic, when it comes to the “tendency to give overly detailed harm-reduction advice on controlled substances, Opus 4.7 is modestly weaker.”

Overall, following Anthropic’s alignment assessment, the model is described as “largely well-aligned and trustworthy, though not fully ideal in its behavior.”

## The Mythos-shaped elephant in the room

Naturally, on the heels of Claude Mythos Preview’s release last week (and the [results of the succeeding ASI evaluation](https://thenewstack.io/claude-mythos-preview-simulation/)), the comparison to what an Anthropic spokesperson told [*Fortune*](https://fortune.com/2026/03/26/anthropic-leaked-unreleased-model-exclusive-event-security-issues-cybersecurity-unsecured-data-store/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) is “the most capable [model] we’ve built to date” is expected.

Three weeks on, the AI company’s tune has not changed. In its Opus 4.7 announcement blog post, Anthropic reaffirms Claude Mythos Preview’s status as “the best-aligned model we’ve trained.”

Furthermore, it says it’s following through on its promise to use less-capable models as a testing ground for new cyber safeguards — Opus 4.7 is the first less-capable model.

Anthropic says the model’s release includes safeguards that “automatically detect and block requests that indicate prohibited or high-risk cybersecurity uses.” Down the line, it hopes to use learnings from Opus 4.7 real-world deployment to work towards an eventual broader release of “Mythos-class models.”

When asked what the company hopes to learn about cyber safeguards from Opus 4.7’s deployment, Anthropic did not respond.

## But watch out for token usage

In a recent [spate of bad luck](https://thenewstack.io/anthropic-claude-code-leak/)[,](https://thenewstack.io/anthropic-claude-code-leak/) Anthropic was fielding complaints from users about [hitting usage limits faster than usual](https://thenewstack.io/claude-code-usage-limits/).

Now, as users plan to migrate from Opus 4.6 to Opus 4.7, the AI company highlights two changes that will affect token usage: Opus 4.7 uses an updated tokenizer and “thinks more at higher effort levels.”

While these changes should improve reliability and text processing, Anthropic cautions that Claude users may see increased token usage. To mitigate this, it directs users to use the effort parameter, adjust task budgets, or simply tell the model to be more concise.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)