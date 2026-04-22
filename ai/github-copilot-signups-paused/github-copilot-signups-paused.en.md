GitHub has announced that it’s pausing new sign-ups for its Copilot individual plans and tightening usage limits for existing users, a move that signals growing strain behind one of the most widely used AI coding tools.

[Joe Binder](https://www.linkedin.com/in/joe-binder-ba781ab2/), VP of product development at GitHub’s parent company Microsoft, [writes in a blog post published Monday](https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/) that the changes are designed to maintain a “reliable and predictable experience” for current customers, as demand for AI-assisted development surges.

“Agentic workflows have fundamentally changed Copilot’s compute demands,” Binder said. “Long-running, parallelized sessions now regularly consume far more resources than the original plan structure was built to support.”

> “Agentic workflows have fundamentally changed Copilot’s compute demands.”

GitHub first [launched Copilot in 2021](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/) as a code completion tool that suggests snippets and functions as developers type. Early versions focused on inline assistance inside the editor, helping speed up routine coding tasks without requiring much interaction beyond a prompt or partial line of code.

In the intervening years, Copilot has expanded far beyond autocomplete, embedding itself [deeply in the agentic realm](https://thenewstack.io/github-copilot-wants-to-become-your-peer-programmer/), with GitHub introducing [tools such as Copilot CLI](https://thenewstack.io/github-launches-its-coding-agent/), which allows developers to issue natural language commands directly in the terminal and have the system carry out multi-step tasks on their behalf.

As a result of all this, usage habits have changed. Instead of short bursts of code suggestions, developers are increasingly delegating more complex work to Copilot, asking it to debug, refactor, and build features over longer sessions.

“As Copilot’s agentic capabilities have expanded rapidly, agents are doing more work, and more customers are hitting usage limits designed to maintain service reliability,” Binder said. “Without further action, service quality degrades for everyone.”

> “As Copilot’s agentic capabilities have expanded rapidly, agents are doing more work, and more customers are hitting usage limits designed to maintain service reliability.”

Moving forward, GitHub’s decision will impact paid tiers, including Copilot Pro and Pro+, as well as student plans, with new subscriptions temporarily unavailable. Existing users will still be able to upgrade between plans, while Copilot Free remains open for new signups – after all, keeping an open entry point preserves a pipeline of future paying users.

But that’s not all. The update also introduces stricter usage caps, with GitHub adjusting how different models and features are allocated across plans. Pro+ plans now offer more than five times the usage limits of the standard Pro tier, though GitHub hasn’t shared specific figures or clarified how these caps have been tightened relative to before. GitHub said users who need higher limits can upgrade to Pro+, and that usage caps will now be displayed directly in tools such as Visual Studio Code and Copilot CLI.

Additionally, the company is also switching up access to its more advanced models. Opus models are no longer available in Pro plans, and the [newly released Opus 4.7](https://thenewstack.io/claude-opus-47-launch/) is limited to Pro+ tiers. GitHub has also confirmed that earlier Opus versions, including [Opus 4.5](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/) and [4.6](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/), are being removed from Pro+ as part of the transition.

## Access control

It’s worth noting that Copilot remains a subscription product, with existing users paying a flat monthly fee. But the introduction of tighter limits reflects a shift in how those subscriptions are managed.

Rather than offering effectively open-ended access within a paid tier, GitHub is leaning more heavily on usage controls — tracking requests and applying constraints once certain thresholds are reached. That brings Copilot closer to a usage-constrained service, even if billing itself hasn’t changed.

But there are reports that this approach could evolve further. Ed Zitron [in *Where’s Your Ed At*?](https://www.wheresyoured.at/news-microsoft-to-shift-github-copilot-users-to-token-based-billing-reduce-rate-limits-2/) suggests GitHub is exploring a shift toward token-based billing for individuals, which would tie costs more directly to consumption.

GitHub hasn’t confirmed any such plans, but Zitron cites company documents that indicate that “the weekly costs of running GitHub Copilot has doubled since the start of the year.”

For now, pausing new signups immediately reduces the flow of additional demand into the system. And tightening limits, through lower usage caps and stricter model access, reins in how much existing users can consume.

> “The introduction of tighter limits reflects a shift in how those subscriptions are managed. Rather than offering effectively open-ended access within a paid tier, GitHub is leaning more heavily on usage controls…”

## Pressure builds

GitHub’s latest move follows a similar step taken just days prior. In early April, the company [paused new Copilot Pro trials](https://github.blog/changelog/2026-04-10-pausing-new-github-copilot-pro-trials/), citing a “significant rise in abuse” of its free trial system. While that decision limits how new users could sample the product, the latest changes go further — and GitHub isn’t alone.

Anthropic, for its part, [has also adjusted](https://x.com/trq212/status/2037254607001559305) how usage limits are applied to its Claude models in recent weeks, redistributing session limits during peak hours so that some users reach [those caps more quickly](https://thenewstack.io/claude-code-usage-limits/).

Separately, Anthropic also recently moved to restrict how its subscriptions can be used with third-party [tools such as OpenClaw](https://thenewstack.io/persistent-ai-agents-compared/), with usage via third-party tools no longer covered by subscriptions and billed separately.

[Boris Cherny](https://www.linkedin.com/in/bcherny/), Anthropic’s Claude Code lead, [said on X](https://x.com/bcherny/status/2040206440556826908?s=20) earlier in April that this reflects a mismatch between how subscriptions were designed and how they are now being used.

“We’ve been working hard to meet the increase in demand for Claude, and our subscriptions weren’t built for the usage patterns of these third-party tools,” Cherny wrote. “Capacity is a resource we manage thoughtfully, and we are prioritizing our customers using our products and API.”

For both companies, the approach is similar: limit how users enter their systems, and place tighter controls on how they are used once inside.

For now, GitHub is addressing that pressure through access restrictions and usage caps. Whether that holds — or gives way to more direct forms of consumption-based pricing — will depend on how those underlying demands evolve.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)