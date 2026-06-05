We [knew it was coming](https://thenewstack.io/github-copilot-usage-billing/), and as of Monday, it’s here. GitHub has officially retired Copilot’s premium request model and [replaced it with](https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/) a [token-based billing system](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises) that ties your payments directly to how much you use.

The switch has been in the works for months, driven by a fundamental shift in how developers use Copilot. What started as an in-editor autocomplete tool [back in 2021](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/) has grown into a platform capable of handling long, autonomous coding sessions spanning entire repositories

## Usage-based billing goes live: what’s changed?

Until now, Copilot combined a fixed monthly subscription with so-called premium request units — an allowance that governed access to more compute-intensive features, such as advanced chat or longer-running agentic tasks, without directly tying them to cost. GitHub absorbed much of the escalating inference costs behind that usage, but as agentic sessions grew longer and more demanding, the model became unsustainable.

> “GitHub absorbed much of the escalating inference costs behind that usage, but as agentic sessions grew longer and more demanding, the model became unsustainable.”

Moving forward, each Copilot plan includes a monthly allotment of GitHub AI Credits rather than premium request units. Credits are consumed based on token usage — covering input, output, and cached data — at published rates for each model.

Plan prices are unchanged across the board. For individual subscribers, Pro users ($10/month) receive $15 in total monthly credits, and Pro+ users ($39/month) receive $70. Each plan includes a fixed base allotment matched 1:1 to the subscription price, plus a variable top-up that GitHub says it will adjust over time as model pricing and AI costs evolve. This so-called “flex allotment” top-up was introduced after users raised concerns that the original base amounts might not be sufficient for heavier agentic workloads.

[Joe Binder](https://www.linkedin.com/in/joe-binder-ba781ab2/), VP of product at GitHub’s parent company Microsoft, was explicit that the base credits are permanent, while the flex portion is more about future-proofing itself against shifts in the cost of AI infrastructure.

> “The flex allotment….is designed to adapt as the economics of AI evolve, including model pricing, new models, and improvements in efficiency,”

“The flex allotment is a variable part of your included usage; it is designed to adapt as the economics of AI evolve, including model pricing, new models, and improvements in efficiency,” Binder wrote in a [May blog post](https://github.blog/news-insights/company-news/github-copilot-individual-plans-introducing-flex-allotments-in-pro-and-pro-and-a-new-max-plan/).

Also going live is Copilot Max, a new top-tier individual plan built for developers who push Copilot hard.

Priced at $100 per month, it includes $200 in total monthly credits — $100 in base credits matched to the subscription price, plus a $100 flex allotment on top. That puts it well above Pro+, and is designed to support sustained, high-volume agentic work without users regularly bumping into their limits.

Existing Student, Pro, and Pro+ subscribers can upgrade to Max today; however, new user sign-ups [remain paused across all individual plans](https://thenewstack.io/github-copilot-signups-paused/) while GitHub manages demand, and the company says it expects to reopen sign-ups in the coming weeks.

![What usage-based billing looks like](https://cdn.thenewstack.io/media/2026/06/a37f3989-table.png)

*What usage-based billing looks like*.

One important caveat for annual plan subscribers: they remain on the existing premium request system until their plan expires, at which point they will move to the new monthly model. GitHub has raised model multipliers for annual subscribers in the interim.

For business and enterprise customers, per-seat pricing holds steady at $19 and $39 per user per month, respectively, with matching credit allotments. Unlike individual plans, however, business and enterprise tiers carry no flex allotment — each seat comes with credits matched exactly to the per-seat price, and no more. To ease the transition, both tiers receive boosted promotional credits through August — $30 per user for Business customers, $70 for Enterprise. Code completions and next edit suggestions are included in all paid plans and do not consume credits.

Alongside the billing changes, GitHub has also improved how Copilot code review operates. Code review now consumes GitHub Actions minutes in addition to AI credits — billed at the same per-minute rates as other Actions workflows — and organization admins can now set a default runner to be used automatically across all repositories. Previously, each repository had to be configured individually, which created overhead for larger teams. With the new organization-level runner setting, admins define it once, and it applies everywhere.

## On budget

Arguably the most interesting facet of the change, beyond the pricing itself, is a [new budget control system](https://docs.github.com/en/copilot/concepts/billing/budgets-for-usage-based-billing#user-level-budget) – and for organizations managing Copilot at scale, it’s more involved than it might first appear.

Under the new model, business and enterprise credits are pooled at the organization level rather than allocated as individual per-user buckets — meaning power users can draw more when they need it, while lighter users offset that consumption.

> “Power users can draw more when they need it, while lighter users offset that consumption.”

There are four controls that work in concert to govern how that pool is drawn down, and what happens when it runs out: a universal user-level budget, individual user-level budget overrides, cost center budgets, and an enterprise-wide budget. User-level budgets are always active and always enforce a hard stop — they cap how much any individual user can consume from both the shared pool and any metered overage. The other controls only kick in once the shared pool is exhausted and usage tips into metered territory.

The most important thing to understand is what the enterprise budget actually is, and what it isn’t. It doesn’t cap total monthly spend. It only limits metered charges accrued after the shared credit pool runs out. As per GitHub’s own example in its documentation, an organization with 400 Copilot Business seats at $19 per user per month carries $7,600 in license fees regardless. An enterprise budget of $5,000 on top of that means a maximum bill of $12,600, up from $5,000.

Needless to say, there’s a lot going on here and things could get unwieldy quickly. The long and short of it is that if user-level budgets collectively allow more consumption than the shared pool provides, the gap spills over into metered usage. If the enterprise budget is too low to cover that gap, users get cut off before they hit their individual limits — GitHub calls this the “lowest remaining headroom wins” rule, and it could catch admins off guard.

Whenever user-level budgets are raised, the enterprise budget calculation needs to be revisited. To illustrate: a user with $5 remaining in their individual budget could be blocked simply because the enterprise budget has only $1 left — their personal allowance is irrelevant at that point.

As one [enterprise user noted on Reddit](https://www.reddit.com/r/GithubCopilot/comments/1tbuneg/enterprise_perspective_on_copilots_usagebased/), a sensible response to all this is to treat it as a FinOps problem from day one.

“We’re running a FinOps-style analysis of usage, identifying power users, planning budget ceilings, [and] educating developers on model choice, prompt size, efficient usage,” they wrote, while acknowledging that their team is simultaneously exploring alternatives including direct OpenAI and Anthropic subscriptions and potentially [self-hosted models](https://thenewstack.io/jetbrains-mellum2-open-source-coding-model/).

## Token gesture: translating the new pricing

A move away from predictable flat-rate pricing was always going to trigger a wave of anxiety among users who suddenly have to think about something they didn’t have to before. In this case, that something is tokens — and for many development teams, now is the time to get acquainted with what they actually are.

The anxiety, however, is already playing out in the wild. On Reddit, some users have characterized the change as a classic bait-and-switch – one Pro+ subscriber claims their projected bill jumped from $39 to $847 for identical usage.

“I signed up for an unlimited subscription product,” the [user writes](https://www.reddit.com/r/github/comments/1ttcpw0/github_copilots_new_creditbased_pricing_is/). “Now it’s pay-per-use with a ‘generous’ allowance that covers maybe 2 days of normal work. This isn’t the product I paid for.”

Others have landed somewhere more pragmatic. “GitHub was losing too much money subsidizing power users,” writes [one user](https://www.reddit.com/r/GithubCopilot/comments/1tu93g4/i_understand_now_why_github_copilot_switched_to/), who claimed they had burned through 200 credits in a single prompt – work that previously had cost them a fraction of their $40 monthly allowance, which covered around 1,500 requests.

The math, they conceded, made GitHub’s decision hard to argue with.

So what exactly are people paying for? Tokens are a basic unit of text that an AI model processes — roughly three to four characters, or about three-quarters of a word. Every interaction with Copilot consumes them: input tokens for what you send to the model, output tokens for what it sends back, and cached tokens for context it stores and reuses across a session. Under the old premium request model, none of this was visible or relevant to users. Under the new one, it determines their bill.

Crucially, not all models cost the same. GitHub has [published](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing) a full per-token pricing breakdown for every model available in Copilot — and the differences are significant. On the OpenAI side, GPT-5 mini is a lightweight option at $0.25 per million input tokens, while [GPT-5.5](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/) — a more powerful model — comes in at $5.00 per million input tokens, which is 20 times the price.

On the Anthropic side, [Claude Haiku 4.5](https://thenewstack.io/anthropic-launches-claude-haiku-4-5/) costs $1.00 per million input tokens, while the [newly released Claude Opus 4.8](https://thenewstack.io/claude-opus-48-release/), built for heavy-duty tasks, runs at $5.00 per million input tokens. Put simply, the model choice now has a direct and visible impact on what teams spend — reaching for the most powerful model for every task is no longer cost-neutral.

The good news is that teams can select which model they use for different tasks, and Copilot also offers an auto mode that routes requests to the most appropriate model based on the work at hand. For straightforward queries, that may mean a cheaper lightweight model. For complex, multi-step agentic work, it will likely mean something more capable — and more expensive.

Getting familiar with the pricing table, and thinking about which model is actually needed for a given job, will be a big part of managing Copilot spend moving forward.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)