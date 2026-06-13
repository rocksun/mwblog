On Tuesday, Anthropic debuted [Fable 5](https://thenewstack.io/anthropic-claude-mythos-fable-5/), the first — and much-anticipated — generally available Mythos-class model.

Anthropic says it can work autonomously for longer than other Claude models and also boasts enhanced memory capabilities and better programming skills for complex tasks.

Early community conversations suggest the new model is top-notch; some users are raising eyebrows over the short usage window, rather conservative guardrails, and not-optional data retention policy.

## Fable 5 price: It’s good, but it’ll cost you

Fable 5 knocks benchmarks out of the park. But you don’t get something for nothing, at least not for very long.

Fable 5 is now available for those with Claude Pro, Max, Team, and seat-based enterprise subscriptions via the API, Microsoft Foundry, Amazon Bedrock, and the Claude Platform on AWS. It costs $10 per million input tokens and $50 per million output tokens. That all goes away after June 22 when users will have to fork out usage credits to access the model — a necessary evil Anthropic says is due to capacity constraints, as covered by [*The New Stack*](https://thenewstack.io/anthropic-claude-mythos-fable-5/).

But judging from early community sentiment, some users seem to think the fabled Fable 5 is worth the extra spend.

For example, as one user posted on the forum [Hacker News](https://news.ycombinator.com/item?id=48463808): “Fable on ‘high’ is producing substantially better results than Op[us] 4.8 on xhigh.” They claim Fable “‘feels’ smarter,” too: “It’s more expensive but also more efficient. It’s been able to find some bugs that Opus missed.”

Users on Reddit echoed similar sentiments; one redditor wrote in [r/claudexpolorers](https://www.reddit.com/r/claudexplorers/comments/1u1bg4m/fable_5_is_out_megathread/): “The negative traits from Opus 4.7 and 4.8 are either absent or under control.”

Not everyone is an instant fan, though. As another user pointed out in the same Hacker Newsthread: “Always hard to say for sure because I’m not sitting around running the exact same situations through both models in parallel to compare them.”

## That burn rate, though

One emerging consensus in community forums is that Fable 5 can have a frustratingly short window of use. Even users who seem dazzled by the new model’s capabilities admit it can burn through usage limits at a breakneck pace.

On [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1u1cvkc/fable_5_is_insanely_good_but_watch_your_usage_i/), one redditor claiming to be on the Max20 plan said they watched their usage tick up to almost 2% per minute: “For context I never came close to hitting limits with Opus 4.8 doing the same kind of work.”

Other users chimed in with similar accounts:

“In mins, my 5x max account went from 0 to 43%”; “I burned through a entire 20x max plan in 45 min”; I burned through 20% of my max weekly and my initial 5 hour session with my first test prompt.”

With Fable 5, it seems that capabilities and usage are something of a give-and-take. While some users say the new model outperforms Opus, others lament what they say is its short usage window: “I’ve never come close before with Opus.”

## Guardrails are working over time (and not in a good way)

As covered by *The New Stack*, Fable 5’s guardrails are among its most defining features.

Back when [Anthropic launched Claude Mythos Preview](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/), only big-name players in Project Glasswing were granted access, as the model was deemed too powerful for public availability.

Hence the guardrails. Designed to prevent users from abusing the model’s sophisticated capabilities, Fable 5’s guardrails will stop the model from answering certain questions (namely those about cybersecurity, biology, chemistry) and then pass the buck to Opus 4.8

But early community conversations indicate that Fable 5 may pass the buck too often.

“It blocks all my work in geography, hydrology, and political ecology,” says one redditor in r/claudexpolorers. Another in r/ClaudeAI writes, “Asked it about hermitian matrices, a common concept in math. It switched back to Opus 4.8 for security reasons.”

Over in Hacker News, the conversation is more of the same: “It’s unusable for me due to the refusals. I’m using claude to find patterns in health data.”

## **Unavoidable data retention is an unwelcome surprise**

Something unexpected that appears to have snuck in under the radar for many users is Anthropic’s new retention policy for Fable 5:

“We will require 30-day retention for all traffic on Mythos-class models, on both first- and third-party surfaces,” writes Anthropic in its announcement blog post.

Unsurprisingly, users don’t seem enthused by what seems like a data retention surprise. Though Anthropic says it won’t use this data to train new Claude models, early responses on Hacker News express disappointment that even enterprise accounts with zero data-retention commitments are still caught up in the new data-retention reality.

Others predict this will likely disqualify Fable 5 for use within their organizations: “This makes it an instant non-starter for probably 95% of organizations.”

## Maybe Fable + Opus will end up being better together?

While there have been some initial grumblings about the high price, short usage window, somewhat conservative guardrails, and the non-negotiable data retention policy of Fable 5, the community consensus on the model’s actual performance is pretty warm.

For users burning through usage rates faster than anticipated, one redditor on r/ClaudeAI offers some advice: “Have it make the choice, tell it to offload to opus, sonnet, haiku or subagents when it seems prudent. Tell it to save its inference for the hard stuff.”

Another redditor muses if this will eventually become the default MO: “I imagine the future of Claude is to just do away with these user-selected levels and let Claude decide what level is needed per request, even spinning up agents at different tiers to handle different parts of the request.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)