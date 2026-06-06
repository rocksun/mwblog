**If there’s one big takeaway from the AI coding space this week**, it’s that the era of flat-rate, all-you-can-code pricing is coming to an end — and the bill is arriving faster than some might have anticipated.

The clearest illustration came from GitHub, which retired Copilot’s fixed subscription model in [favor of token-based billing](https://thenewstack.io/github-copilot-token-billing/), tying costs directly to consumption. The backlash, which was already brewing since the [announcement in April](https://thenewstack.io/github-copilot-usage-billing/), was real. Some subscribers reported projected monthly bills jumping tenfold overnight, with others characterizing the change as a bait-and-switch.

Then on Wednesday, the Linux Foundation [announced plans](https://thenewstack.io/tokenomics-foundation/) for the [Tokenomics Foundation](https://www.tokeneconomics.com/), a new industry body backed by the likes of Google, Microsoft, Salesforce, JPMorgan Chase, and others, with a mandate to build open standards and frameworks around AI token production, consumption, and monetization — an acknowledgment that enterprises currently have no consistent, vendor-neutral way to measure or control what they owe.

## Bringing visibility and control to the enterprise

[Cursor](https://cursor.com/home), for its part, has clearly been paying attention. On Monday, the AI coding agent company [restructured pricing](https://cursor.com/blog/teams-pricing-june-2026) for its Teams plan, cutting annual seat costs by 20% to $32 per user per month, while introducing a new Premium tier at $120 per month, with the promise of five times the usage of the standard seat at three times the price — explicitly targeting power users whose consumption had become hard to forecast.

Alongside this, Cursor added a dedicated usage pool for its [own first-party Composer model](https://cursor.com/blog/composer), separate from the allowance for third-party models from the likes of Anthropic and OpenAI.

The update also includes a rebuilt spend alert feature, letting admins configure alerts based on dollar thresholds — per member or team-wide — delivered via Slack or email before an unexpected charge lands.

![Spend alert](https://cdn.thenewstack.io/media/2026/06/08794395-spendalertgif.gif)

*Spend alert*

Fast-forward to Wednesday, and [Cursor launched](https://cursor.com/blog/organizations) an enterprise governance layer aimed squarely at the IT and finance teams now responsible for keeping AI spend in check.

The new “[organizations](https://cursor.com/docs/enterprise/organizations)” structure lets large companies manage multiple Cursor deployments from a single dashboard, with budgets, model access, and agent permissions all configurable at the department level.

> The idea is that different functions carry different risk profiles and different cost tolerances.

The idea is that different functions carry different risk profiles and different cost tolerances — a product or engineering team may warrant the full model roster and generous spending headroom, while a marketing or finance team might be locked to cheaper models, lower ceilings, and a requirement that agents get human sign-off before executing any command.

An org-level dashboard rolls up spend and token consumption across every team, filterable by user, team, or cloud agent, giving finance teams the visibility to run chargebacks by business unit.

![Usage analytics by team](https://cdn.thenewstack.io/media/2026/06/05061613-usageanalyticsgifyeah.gif)

*Usage analytics by team*

Collectively, these features are designed to bring visibility and control into enterprise settings, where unwieldy AI pricing is now top of mind for CFOs across sectors.

To understand why, it helps to follow the economics of tools like Cursor.

> These features are designed to bring visibility and control into enterprise settings, where unwieldy AI pricing is now top of mind for CFOs across sectors.

## The wrapper squeeze

Unlike Anthropic or OpenAI, which charge for inference directly on a per-token basis, Cursor is a wrapper — it buys inference from frontier model providers at API rates and resells access to developers, historically at a flat monthly fee. That model worked when usage was modest, but it stopped working as agentic coding sessions grew longer, heavier, and far more token-hungry.

The ringfenced Composer pool is Cursor’s most telling response to that squeeze. [Composer 2.5](https://thenewstack.io/cursor-composer-benchmarks/), Cursor’s own coding model, [costs](https://cursor.com/docs/models-and-pricing) $0.50 per million input tokens and $2.50 per million output tokens. Claude Opus 4.7 and 4.8, by comparison, run at $5.00 input and $25.00 output — a tenfold difference on the tokens that matter most.

By giving Composer its own separate allowance, and automatically falling back to it when a user exhausts their third-party API allocation, Cursor is structurally nudging users toward cheaper inference it controls — and protecting its own margins in the process.

> Cursor is structurally nudging users toward cheaper inference it controls — and protecting its own margins in the process.

This dynamic is playing out across the space. On Monday, [JetBrains open-sourced Mellum2](https://thenewstack.io/jetbrains-mellum2-open-source-coding-model/), a 12-billion-parameter coding model built for the infrastructure layer of agentic systems — routing, retrieval pipelines, and sub-agent tasks — as well as on-premises deployment in environments where hosted tools like Cursor and Claude Code can’t operate. While its predecessor, Mellum, handled code completion alone, Mellum2 is built for the broader coordination work that now defines how engineering teams deploy AI.

The method differs — Mellum2 is self-hostable, putting inference costs entirely in the hands of the team running it — but the underlying impulse is the same: reduce dependence on expensive third-party API calls.

## Pricing scars

With GitHub facing the wrath of angry users this week over its Copilot overhaul, it’s worth noting that Cursor too has navigated the tricky terrain of pricing before.

In June 2025, the company [launched](https://cursor.com/blog/new-tier) its $200-per-month Ultra plan — made possible by multi-year volume deals with Anthropic, OpenAI, Google, and xAI. But at the same time, it switched its Pro plan from request-based to compute-based billing, a change that caught many users off guard and led to unexpected charges.

The execution of that change was rough enough that Cursor had to [issue a public apology](https://cursor.com/blog/june-2025-pricing) and refunds to affected users.

The moves this week are a different kind of response to the same underlying pressure. While the 2025 changes focused on restructuring Cursor’s charges and how they’re applied, this week’s updates give organizations the visibility and controls to manage what they’re already spending.

Whether it succeeds will depend partly on transparency. Cursor still doesn’t publish the actual size of its included usage pools, describing them only as “generous” — a vagueness the Tokenomics Foundation was arguably created to address.

As [J.R. Storment](https://www.linkedin.com/in/jrstorment/), executive director of the FinOps Foundation, tells *The New Stack*, organizations currently have no consistent way to compare costs across providers or make informed decisions about AI deployment.

“Each hyperscaler and each model provider and each hardware provider will have their own approach, their own data, their own value metrics,” Storment says. “We aim to align consistent models between them as we’ve done previously.”

Until that changes, users on every platform are navigating the new token economy largely in the dark – which is why Cursor’s spend alerts, usage dashboards, and model access controls, however modest, are a step in the right direction.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)