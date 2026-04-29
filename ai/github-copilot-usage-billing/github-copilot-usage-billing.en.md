The rumors were true: GitHub announced today that it’s overhauling how it charges for Copilot, shifting to a usage-based billing model that ties costs directly to developers’ usage of its AI coding tools.

The change, set to take effect on June 1, keeps Copilot’s subscription plans in place but replaces the internal system that governs usage. Today, Copilot combines a fixed monthly fee with so-called “premium request” units — an allowance that limits access to more compute-intensive features, such as advanced chat or longer-running tasks — without directly tying them to cost.

That system is being replaced with a credit-based model linked to token consumption. Each plan will include a monthly allotment of GitHub AI credits, with the option to pay for additional usage once those credits are exhausted.

In a [blog post](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) published on Monday, [Mario Rodriguez](https://www.linkedin.com/in/mariorodriguez3/), GitHub’s chief product officer, writes that the change is designed to create a more “sustainable” pricing model.

“This change aligns Copilot pricing with actual usage and is an important step toward a sustainable, reliable Copilot business and experience for all users,” Rodriguez explained.

> This change aligns Copilot pricing with actual usage and is an important step toward a sustainable, reliable Copilot business and experience for all users.

The move follows a series of measures GitHub introduced to manage demand, including halting [free Copilot Pro trials](https://github.blog/changelog/2026-04-10-pausing-new-github-copilot-pro-trials/), pausing [new sign-ups for some Copilot plans](https://thenewstack.io/github-copilot-signups-paused/), and tightening usage limits for existing users. Rumors [also emerged last week](https://www.wheresyoured.at/news-microsoft-to-shift-github-copilot-users-to-token-based-billing-reduce-rate-limits-2/) that these changes were laying the groundwork for GitHub to transition to token-based billing.

GitHub, for its part, isn’t alone in responding to those pressures. Anthropic [has also adjusted](https://x.com/trq212/status/2037254607001559305) how limits are applied to its Claude models in recent weeks, redistributing usage during peak periods so that [some users hit caps sooner](https://thenewstack.io/claude-code-usage-limits/). The company has also moved to restrict how subscriptions apply to [third-party tools like OpenClaw](https://thenewstack.io/persistent-ai-agents-compared/), with usage through those integrations now billed separately.

Collectively, these changes reflect mounting pressure on AI coding services as usage shifts toward longer, more compute-intensive sessions, forcing companies to rethink how access is priced and managed.

## Unpacking the changes

Since its [launch in 2021](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/), Copilot has been sold largely as a fixed-price subscription, with developers paying a monthly fee for access to AI-powered coding assistance.

Under the new model, usage will be calculated based on tokens — covering input, output, and cached data — using rates tied to specific models.

GitHub says the shift reflects how Copilot now handles longer, multi-step coding work across projects, rather than short bursts of in-editor assistance.

“Copilot is not the same product it was a year ago,” Rodriguez writes. “It has evolved from an in-editor assistant into an agentic platform capable of running long, multi-step coding sessions, using the latest models, and iterating across entire repositories. Agentic usage is becoming the default, and it brings significantly higher compute and inference demands.”

> Copilot is not the same product it was a year ago.

Digging deeper into the details reveals that base plan pricing remains the same across all tiers, and core features such as code completions and Next Edit suggestions will continue to be included without drawing down credits. The fallback system is also being removed, meaning users who hit their limits will no longer be shifted onto lower-cost models. Copilot code review will now draw on GitHub Actions minutes alongside AI credits, linking usage more directly to existing compute billing.

It’s worth noting that the changes apply across both individual and business Copilot plans.

For individual users, Copilot Pro and Pro+ will now include a monthly allowance of AI credits, tied to each plan’s cost. Pro users will receive $10 in credits per month, while Pro+ users will receive $39. Those on annual plans will stay on the existing system until their subscription ends, at which point they will move onto the new monthly model, with the option to convert earlier and receive prorated credits.

For business and enterprise customers, per-seat pricing remains unchanged. Copilot Business continues at $19 per user per month, and Enterprise at $39 per user per month, with each tier receiving a matching amount of monthly credits.

GitHub is also introducing pooled usage for organizations, allowing unused credits from one user to be shared across a team. Administrators will be able to set spending limits at different levels, including per user or across the entire organization, and decide whether to allow additional usage once those limits are reached.

To ease the transition, GitHub is offering higher credit allowances for business and enterprise customers over the summer, giving teams time to adjust before the new system fully takes hold. Admins will also be able to set spending limits at different levels, from individual users up to the entire organization, and choose whether to allow additional usage once those limits are reached or cut it off.

Those controls are designed to give teams a way to manage how usage translates into cost under the new model, as more demanding workloads have become harder to absorb within a flat fee.

“Usage-based billing fixes that,” Rodriguez explained. “It better aligns pricing with actual usage, helps us maintain long-term service reliability, and reduces the need to gate heavy users.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)