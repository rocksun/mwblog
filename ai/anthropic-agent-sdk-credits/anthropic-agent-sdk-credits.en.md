Anthropic announced this week that programmatic usage, including third-party apps built on Agent SDK, will draw from a new monthly credit pool, starting June 15.

## What’s changing

In a Wednesday [X post](https://x.com/claudedevs/status/2054610152817619388?s=46), the company stated that Claude paid-subscriptions will soon be eligible for a monthly [Agent SDK credit](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan). The credit covers programmatic usage, i.e., Claude Agent SDK, claude -p, Claude Code GitHub Actions, and third-party apps built on the Agent SDK.

The new policy draws a stark line in the sand between how programmatic usage and interactive usage are billed.

For example, chatting with Claude on the web, desktop, or mobile, using Claude Code in the terminal, and using Claude Cowork will still count against typical subscription limits. But when you use `claude -p` command in Claude Code, run Claude SKD usage in Python or TypeScript projects, or let third-party apps authenticate through Agent SDK, you’ll soon see that usage drain from your new monthly Agent SDK credit.

Before, Claude users didn’t need to concern themselves with such distinctions; programmatic and interactive usage pulled from the same subscription limits.

## How it works

As Anthropic outlines on X, Claude users must now claim a separate monthly credit to support the Agent SDK. But you only have to do it once. After that, all programmatic usage will automatically draw from your credit.

What happens if you max out that credit? You have two options.

If you turn on usage credits, you can keep working, sans effect — just know that your continued usage will be billed at pay-as-you-go API rates.

If you turn off usage credits, then you’ve essentially capped your programmatic usage for the month, and you’ll have to wait for your credit to refresh at the start of your next billing cycle.

What if you have unused credits left at the end of the billing cycle?

No luck, there. Anthropic says credits do not roll over and will simply expire at the end of the billing cycle.

## How much credit will you get?

The size of your Agent SDK credit pool depends on your plan.

Pro users get $20; Max 5x, $100; Max 20x, $200. Standard teams get credit at $20/seat; premium teams at $100/seat. Enterprise usage-based accounts cost $20; Enterprise Premium seats cost $200.

It’s worth noting that Agent SDK credits only apply to individual accounts. This means you can’t share, transfer, or pool credit across teams.

Plus, Claude Developer Platform accounts using an API key aren’t eligible for the credit. Instead, these users will simply continue on with pay-as-you-go billing.

On X, Anthropic’s developer communications account says, “third-party tools built on the Agent SDK like Conductor and OpenClaw work with your Claude plan, but will draw from your credit the same way your own scripts do.”

That means third-party tool usage will soon pull from users’ new Agent SDK credit pools — yet another shift in Anthropic’s stance on third-party tool usage.

Just a month ago, the AI company stopped allowing Claude users to apply their subscriptions to third-party tool usage. As [Boris Cherney](https://www.linkedin.com/in/bcherny/), Head of Claude Code at Anthropic, published to X on April 4, “Claude subscriptions will no longer cover usage on third-party tools like OpenClaw.” Instead, the then-new policy meant users had to buy extra usage credits or face pay-as-you-billing at API rates.

But Anthropic has changed its tune once again, ditching last month’s policy altogether in favor of the new Agent SDK credit system.

The policy goes into effect on June 15. Users don’t have to do anything for now, but should look out for an Anthropic email on June 8 to claim credits.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)