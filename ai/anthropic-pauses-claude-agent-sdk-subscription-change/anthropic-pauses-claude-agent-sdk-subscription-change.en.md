Anthropic has hit pause on a billing change affecting developers who use its Claude [Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) through a paid subscription — pulling back on the very day it was scheduled to go live.

The announcement comes after a [turbulent week](https://thenewstack.io/anthropic-fable-mess-explained/) for Anthropic. On June 9, [the company released](https://thenewstack.io/anthropic-claude-mythos-fable-5/) Fable 5 and Mythos 5 — its first generally available [Mythos-class models](https://thenewstack.io/anthropic-glasswing-mythos-cybersecurity/), built with hardened cybersecurity guardrails — only for the US government [to issue an export control directive days later](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/), forcing Anthropic to pull both models for all customers worldwide.

Now, it seems, Anthropic is looking to bring a little good news to its global user base, by holding off on a billing change that may have cost many developers and third-parties more for their automated Claude usage.

## Splitting usage

Back in May, [Anthropic told subscribers](https://x.com/ClaudeDevs/status/2054610152817619388) it was splitting its usage allowance in two. Until now, everything a Claude subscriber does — chatting, writing code in the terminal, or using third-party tools built on the Agent SDK — draws from a single monthly pool. From June 15, the company said, Agent SDK usage would move to a separate, capped monthly credit for Pro, Max, Team, and Enterprise subscribers, ranging from $20 for Pro users up to $200 for top-tier Max and Enterprise seats.

For third-party tools like [Zed](https://zed.dev/) that rely on the Agent SDK to connect users’ Claude subscriptions to their products, the change wasn’t insignificant. In a [blog post published](https://zed.dev/blog/anthropic-subscription-changes) the day after the May announcement, Zed’s head of growth and marketing [Franciska Dethlefsen](http://www.linkedin.com/in/franciskadethlefsen/) noted that subscriptions had previously subsidised that kind of usage at roughly 15 to 30 times the equivalent API cost — a figure [gleaned from analysis](https://fazm.ai/blog/claude-pro-vs-api-cost-comparison) by engineer and entrepreneur [Matthew Diakonov](https://fazm.ai/about) — and that the new credits would be billed at full API rates.

Dethlefsen did point to one workaround, though: users who ran Anthropic’s official Claude CLI directly in a terminal inside Zed, rather than through the Agent SDK, would have remained on their existing subscription limits.

The same tool, billed differently depending on how you invoked it.

## Pausing changes

On Monday, though, Anthropic started emailing subscribers saying the planned change was off, as per reports on [forums such as Hacker News](https://news.ycombinator.com/item?id=48546618). The company’s [support documentation has also now been updated](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) to match, confirming that Agent SDK usage continues to draw from standard subscription limits and that no separate credit exists to claim.

“We’re pausing the changes to Claude Agent SDK usage described below,” the message notes. “For now, nothing has changed.”

![Pausing the change](https://cdn.thenewstack.io/media/2026/06/834bb16a-screenshot-2026-06-16-at-11-09-17-use-the-claude-agent-sdk-with-your-claude-plan-claude-help-center.png)

*Pausing the change*

The timing created an awkward situation for companies that had already communicated the change to their own users. [Conductor](https://www.conductor.build/), a multi-agent coding tool built on the Claude Agent SDK, [published a post](https://www.conductor.build/blog/claude-subscription-update) telling customers they were in the clear for now. “Anthropic has delayed the subscription updates to Claude plans,” the Conductor team wrote. “You can continue to use your Claude plan with Conductor as normal.”

## A bumpy few months on billing

The June 15 pause is the latest in a series of billing changes Anthropic has made around third-party Agent SDK access, and the underlying tension is one the whole industry is grappling with. As Anthropic’s head of Claude Code [Boris Cherny put it back in April](https://x.com/bcherny/status/2040206441756471399?lang=en), when announcing an earlier restriction on third-party tool access, subscriptions “weren’t built for the usage patterns of these third-party tools” — an acknowledgement that flat-rate pricing and open-ended agentic usage don’t mix well.

GitHub arrived at the same conclusion and acted on it, [retiring](https://thenewstack.io/github-copilot-token-billing/) Copilot’s flat premium request model in June in favour of token-based billing — a change that drew its share of complaints but went ahead regardless.

In the same week as Anthropic’s billing reversal, [a proposed class action lawsuit was filed](https://www.wsj.com/tech/ai/anthropic-sued-over-limits-on-its-200-a-month-ai-plans-e2a109e4) in a California federal court, [alleging](https://www.vacadaffanlaw.com/post/kahn-v-anthropic-pbc) that Claude’s Max subscription tiers fall well short of their advertised usage multipliers during heavy coding sessions.

On the billing front, Anthropic hasn’t said when a revised approach will arrive, saying only that it’s “working to update the plan to better support how users build with Claude subscriptions.”

What we do know is that the company is feeling the heat from the US government over Fable and Mythos. Coupled with its [plans to become a publicly traded company](https://www.anthropic.com/news/confidential-draft-s1-sec), and [rumored price cuts](https://www.wsj.com/tech/ai/openai-considers-drastic-price-cuts-anticipating-war-for-users-with-anthropic-9b8c178e) from its fierce rival OpenAI, it’s clear Anthropic is trying to keep its developer base onside — and the billing pause is one way it can do that for now.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)