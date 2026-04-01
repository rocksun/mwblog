Claude Code users say they’re reaching usage limits faster than before — an ongoing issue Anthropic confirms on Reddit and X.

On Monday on [Reddit](https://www.reddit.com/r/Anthropic/comments/1s7zfap/investigating_usage_limits_hitting_faster_than/), Anthropic acknowledged users’ suspicions, writing, “We’re aware people are hitting usage limits in Claude Code way faster than expected.”

An update came a few hours later via another comment: “Still working on this. It’s the top priority for the team, and we know this is blocking a lot of you. We’ll share more as soon as we have it.”

## Users take to Reddit and X to share woes

It seems the AI company is at a loss for what’s causing the hiccup — or at least they’re keeping mum about the root cause.

Users, meanwhile, are vocal about their difficulties.

[One redditor](https://old.reddit.com/r/Anthropic/comments/1s8ex9a/nothing_changed/) claims a single prompt cost them 10% of their limit, a sharp increase from what they say would normally only take 0.5–1%. Another redditor sympathizes, commenting on the same thread, “I use up Max 5 in 1 hour of working, before I could work 8 hours…”

Similar complaints litter X. “I have the $100/month plan and 30 minutes of coding now uses up 60% of my session limit,” laments [one user](https://x.com/alexoakdev/status/2025153521134567569). “A few months ago, this would have only used like 5%, I think.” [Another](https://x.com/thegupler/status/2037610036873052515) adds, “I’ve had two sessions that I haven’t been going that hard in, and I’m already at 91% usage.”

Still [another](https://x.com/om_patel5/status/2038757628323430844) claims usage begins to climb, starting with a simple salutation: “Saying ‘hello’ to Claude on the Pro plan now costs 2% of your entire session usage.”

The same statement issued by Anthropic on Reddit was [posted](https://x.com/lydiahallie) to X by a member of the Claude Code team, noting the company is “actively investigating, will share more when we have an update.”

## A user-identified bug may be behind the problem

While Anthropic hasn’t stated what’s causing the unexpected limit exhaustions, [one redditor claims](https://www.reddit.com/r/ClaudeCode/comments/1s7mitf/psa_claude_code_has_two_cache_bugs_that_can/) to have found the bug themselves after reverse-engineering the Claude Code binary, finding “two independent bugs that cause prompt cache to break, silently inflating costs by 10–20x.”

They posit that this bug is breaking cache history, forcing Claude Code to reprocess each prompt and driving up usage.

In an X thread discussing the user’s proposed bug, [Thariq Shihipar](https://www.linkedin.com/in/thariqshihipar/), member of technical staff at Anthropic, [responded](https://x.com/trq212/status/2038684294911279201): “We are actively looking into this in particular, but not sure it’s real yet; prompt cache bugs can be quite subtle.”

## Problems with usage limits come after recent policy updates

Interestingly, Claude Code users’ quota woes come after a series of recent policy changes.

Last week, Anthropic said it was reducing quotas during peak hours, with [Shihipar again taking to X](https://x.com/trq212/status/2037254607001559305) to explain: “To manage growing demand for Claude, we’re adjusting our 5-hour session limits for free/Pro/Max subs during peak hours.”

But Shihipar’s X post was the AI company’s only word on the subject, seemingly doing the work of any official announcement. Shihipar said Anthropic “landed a lot of efficiency wins to offset this” and only expected about 7% of users to “hit session limits they wouldn’t have had before, particularly in Pro tiers.”

This social media post coincided with [a two-week, limited-time promotion](https://thenewstack.io/anthropic-doubles-claude-usage-outside-peak-hours/) in which Anthropic doubled Claude users’ usage limits outside peak hours.

## Users are still waiting on a fix

It’s worth noting that Claude Code users aren’t the only ones feeling stiffed.

In the same [thread](https://old.reddit.com/r/Anthropic/comments/1s8ex9a/nothing_changed/) discussing the issue, another redditor adds:

“Not just Anthropic. I’m running 3x OpenAI Plus, 1x Gemini Pro, and Claude Max x5, and I’m hitting caps on all of them by week 3 of every month, and almost every 5hr cap. Every single one is delivering less than it was.”

Even so, some users have floated the idea of jumping ship to the OpenAI competitor, Codex, with one [writing](https://old.reddit.com/r/Anthropic/comments/1s8ex9a/nothing_changed/): “I just joined last week and already want to leave.”

Adding more confusion to the quandary, Anthropic doesn’t currently give exact usage limits for its plans. Support [documentation](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work?utm_source=chatgpt.com) on usage and length limits states that “Different subscription plans (Pro, Max, Team, etc.) have different usage allowances, with paid plans offering higher limits,” without spelling out exact allowances.

For now, it’s unclear when Claude Code usage limits will return to normal levels. Asked when users can expect a fix and what might be behind the issue, a spokesperson for Anthropic said investigations continue and an announcement will be forthcoming when progress is made.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)