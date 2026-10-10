*I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

Elon Musk posted an “[important note](https://x.com/elonmusk/status/2107724314451878104)” on Wednesday about Grok Bot, the AI agent SpaceX launched in beta in August: “Important note regarding Grok @Bot: Going forward, @SpaceX will use the best back end model for any given task, including Claude Opus 5.5, MidJourney, Suno and other leading APIs. Whatever is most likely to give you the best outcome.”

Grok Bot is a joint product of SpaceXAI, the Musk AI lab now folded into SpaceX, and Cursor, which SpaceX [agreed in June to buy](https://thenewstack.io/spacex-cursor-ai-coding/) for $60 billion in stock, a deal that closed in August.

In August, [I wrote](https://thenewstack.io/grok-4-6-matched-fable-5-max/) that when models converge on price, the money moves to whoever decides which model gets the job. This trend is happening across organizations increasingly relying on AI and trying to balance rising costs.

I heard this firsthand this week. At least 10 of the 22 company leaders we interviewed at an [AI event this week](https://scaleup.events/) described the same habit: pick the model by the task, and keep the expensive one for the work that needs it.

## Model triage is how companies are controlling AI costs

I’m in New York City this week with Alex Wilhelm of the [Cautious Optimism newsletter](https://www.cautiousoptimism.news/) and Nick Lucchesi of [*The New Stack*](https://thenewstack.io/), and we spent Monday and Tuesday at Insight Partners’s ScaleUp:AI conference interviewing the people running 22 of Insight’s portfolio companies. Please note, Insight Partners owns *The New Stack*, and we shot these interviews for a video series Insight is producing. I’m not naming anyone here or pushing any of their products. These are real companies run by experienced operators, and what they told us about running AI matches what the rest of the market is doing, as the OpenRouter numbers below show.

The most common model triage setup we heard about was a funnel. One security company runs a rules engine over everything first and passes what survives to small models. Larger models only see what’s left. One of its executives told us that running a petabyte of data through any model, even a small one, would cost millions of dollars. Another company runs requests to its agent through a cheap model to figure out what the user wants before the expensive model does anything.

Cost was the reason most of them gave. One executive said his company started with unlimited AI budgets and is now asking what all those tokens actually bought. Another said his employees kept reaching for the most advanced model even when it was overkill, so the company now teaches staff which model fits which job. A third put the incentive bluntly: The labs do better when you spend more tokens. Of course, a couple of the people we talked to sell small models for a living, so I’m weighing their enthusiasm accordingly.

Switching has its own risk. One engineering leader told us his team swapped in a newer model three days before a demo for an important prospect because the benchmarks said it was cheaper and just as good. The workflow broke, and his team rolled back over a weekend. His lesson was evals, a set of tests that would have caught the problem before his team had to find it by hand. *The New Stack*’s Amanda Caswell [found the vendor version](https://thenewstack.io/claude-opus-agent-migration/) of that story last month, when Anthropic made Opus 5.5 20% cheaper than Opus 5 and broke four things agents depend on.

In short, test before you switch, and follow the ABS rule: Always Be Switching.

## OpenRouter’s leaderboard shows cheap models doing the volume

OpenRouter is a service developers use to reach hundreds of models through one connection, and it publishes what flows through it. In the week through October 7, four of its ten most-used models were “Flash” models, the cheap, fast versions labs ship alongside their flagships. Anthropic just made its own cheap tier cheaper. [Haiku 5.5 launched Wednesday](https://thenewstack.io/anthropic-claude-haiku-5-5/) at $.10 per million input tokens, a 90% cut for requests under 100,000 tokens, and small models like it typically handle high-volume jobs like classification and routing.

Cheap models carry the volume. The frontier model is growing fastest.

Selected models from OpenRouter’s top 10 by tokens processed in the week through Oct. 7, 2026, and the change from the week before.

| Model | Maker | Tokens | Change |
| --- | --- | --- | --- |
| DeepSeek V4.1 Flash | DeepSeek | 33.6T | +48% |
| GLM 5.3 Flash | Z.ai | 10.5T | -1% |
| MiMo-V2.6-Flash | Xiaomi | 10.1T | +11% |
| GPT-6 Luna | OpenAI | 6.46T | +28% |
| Claude Opus 5.5 | Anthropic | 3.37T | +74% |
| Jev 1.13 | TypeSafe | 3.32T | +12% |

The frontier model is growing too. Claude Opus 5.5 is ninth by volume and grew 74% in a week, the fastest of any model in the top 10. It also ranks first on OpenRouter’s Artificial Analysis intelligence index. That’s what triage looks like from the outside: The expensive model gets more of the work each week without coming close to the top of the list.

For TNS, Jessica Wachtel tested that twice this week: Claude Sonnet 5.5 [passed all 15 of her coding runs](https://thenewstack.io/claude-sonnet-5-5-vs-opus-5-5/) at 42% less than Opus 5.5, which passed 13, though four Sonnet runs only passed after she raised its output-token limit. The day before, she found [GPT-6.1 Sol matched GPT-6 Astra’s accuracy](https://thenewstack.io/gpt-6-1-sol-vs-gpt-6-astra/) at 18% of the cost. The cheaper model held up both times.

Models are turning over fast right now. DeepSeek V4.1 Flash didn’t exist a month ago and is now OpenRouter’s top model. Decision models, which pick an answer from a set of options instead of writing one, are showing up too. [TypeSafe’s Jev](https://thenewstack.io/typesafe-jev-system-one/) is 10th, and [OpenAI’s GPT-6 Luna Decisions](https://thenewstack.io/openai-decision-api-luna/) is new on the trending list.

The obvious objection is that OpenRouter’s customers are developers who chose a router, so they’ll switch. It’s fair. Its own page notes that token counts don’t measure users or spend, and enterprise contracts are stickier.

But at least 10 companies we interviewed run their AI the same way, and as of Wednesday, so does Elon Musk.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)