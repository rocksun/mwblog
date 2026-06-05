It’s no secret that AI is becoming enterprises’ biggest and [least understood technology expense](https://thenewstack.io/finops-ai-token-economics/), and for many companies, the spending is well ahead of the accountability.

With that in mind, the Linux Foundation [announced on Wednesday](https://www.linuxfoundation.org/press/linux-foundation-announces-the-intent-to-launch-the-tokenomics-foundation-to-establish-open-standards-for-ai-cost-management) its intent to launch the [Tokenomics Foundation](https://www.tokeneconomics.com/), a new body tasked with establishing open standards, benchmarks, and best practices across the full AI token economy — from production and consumption to monetization.

The foundation is due to formally launch at [FinOps X](https://x.finops.org/) in San Diego later in June, where its leaders will share further detail on the technical roadmap and associated working groups. It has drawn initial support from a broad cross-section of the industry, including Google, Microsoft, IBM, JPMorgan Chase, KPMG, Oracle, and Salesforce.

## A new unit of enterprise spend

A token, for the uninitiated, is a unit of text that an AI model processes — and it sits at the center of every layer of the AI economy: It’s what the model thinks in, what the data center bills for, and what the enterprise ultimately pays for and extracts value from.

> “Tokens don’t behave like any cost category finance teams have dealt with before — even cloud, which took years to tame, had more predictable usage patterns.”

However, tokens don’t behave like any cost category finance teams have dealt with before — even cloud, which took years to tame, had more predictable usage patterns.

Back in April, fintech giant [Ramp announced it was pulling token-level data](https://thenewstack.io/ramp-ai-token-spend-management/) from AI providers to give finance teams visibility into how AI costs are generated and allocated. This was in response to a growing point of tension: unlike traditional software contracts, AI costs are tied to consumption and can escalate fast.

Ramp’s internal data showed that average monthly token spend has increased 13-fold since January 2025, with costs among heavy users jumping by 50% or more in a single quarter.

Data [published by Goldman Sachs in May](https://www.goldmansachs.com/insights/articles/ai-agents-forecast-to-boost-tech-cash-flow-as-usage-soars) backs this up, projecting that global token usage will grow 24-fold between 2026 and 2030, reaching 120 quadrillion tokens per month.

And that trajectory is already reshaping how AI products are priced and sold. GitHub’s move this week to retire Copilot’s flat-rate subscription model [in favor of token-based billing](https://thenewstack.io/github-copilot-token-billing/) is the clearest sign yet that the old economics have become untenable. As agentic coding sessions grew longer and more demanding, GitHub absorbed much of the escalating inference costs behind that usage, which became unsustainable.

The community backlash against GitHub’s change has been swift, with some Copilot subscribers characterizing it as a bait-and-switch and reporting that projected monthly bills jumped tenfold overnight.

That anxiety is precisely what the Tokenomics Foundation is designed to address — bringing some order to a cost structure that is currently opaque for buyers and sellers alike.

[J.R. Storment](https://www.linkedin.com/in/jrstorment/), executive director of the [FinOps Foundation](https://www.finops.org/), tells *The New Stack* that fragmentation is one of core issues at play.

“Each hyperscaler and each model provider and each hardware provider will have their own approach, their own data, their own value metrics,” Storment says. “We aim to align consistent models between them as we’ve done previously.”

## “A different operational muscle”

The Tokenomics Foundation will work closely with the FinOps Foundation, a nonprofit that has been building a shared discipline around cloud cost management as part of the Linux Foundation [since 2020](https://www.linuxfoundation.org/press/press-release/the-linux-foundation-brings-together-it-and-finance-teams-to-advance-cloud-financial-management-and-education). The hope is that the same thinking can now be applied to AI — bringing the same rigor to token spend that FinOps brought to cloud bills.

> Token economics introduces layers of complexity that cloud never had.

But that analogy only goes so far. Token economics introduces layers of complexity that cloud never had: Input and output tokens carry different price tags, cached tokens are billed differently again, and pricing structures vary enough between providers to make vendor comparisons genuinely difficult.

In a [press release](https://www.linuxfoundation.org/press/linux-foundation-announces-the-intent-to-launch-the-tokenomics-foundation-to-establish-open-standards-for-ai-cost-management) accompanying the announcement, Salesforce’s chief availability officer [Nishant Gupta](https://www.linkedin.com/in/nigupta/) argues that token economics is a categorically harder problem than cloud cost management — one that will require the industry to experiment collectively and pool its findings, rather than letting individual companies reinvent the wheel in isolation.

> “Token economics….requires a different operational muscle than the one the industry built for cloud.”

“Token economics is fundamentally more abstract and more opaque than anything we’ve managed at this scale before,” Gupta says. “It requires a different operational muscle than the one the industry built for cloud, and that muscle should evolve through broad experimentation across the industry, with the best ideas and practices contributed back so we can collectively establish durable standards around it.”

## Foundation in action

While much of the operational detail has yet to be announced — further specifics are expected at FinOps X on June 8 — the foundation’s broad structure is already taking shape. A technical committee will work on common specifications and benchmarks for measuring and reporting token costs, including extending [FOCUS](https://focus.finops.org/) — an open billing format already used across cloud providers — to cover AI token spending. A governing board will set strategic direction and allocate resources.

The founding supporter list spans the breadth of the AI economy: Accenture, Booking.com, Flexera, Google Cloud, IBM, JPMorgan Chase, KPMG, Microsoft, Oracle, Salesforce, SAP, and ServiceNow have all provisionally signed on. However, when asked what kind of financial support the likes of Google and Microsoft are providing, if any, a spokesperson for the foundation said that this is still under evaluation by the parties.

## Who’s absent?

Notably absent are the frontier model providers whose pricing sits at the heart of the problem — neither Anthropic nor OpenAI features among the initial backers. And that matters: as one recent analysis of [the token pricing crisis laid out](https://www.investing.com/analysis/the-ai-token-pricing-crisis-behind-openai-and-anthropics-revenue-race-200680777), enterprise budgets are already buckling under the weight of frontier model costs — Uber’s CTO [revealed recently](https://www.forbes.com/sites/janakirammsv/2026/05/17/uber-burns-its-2026-ai-budget-in-four-months-on-claude-code/) that the company burned through its entire 2026 AI budget in just four months, driven largely by surging Claude Code adoption across its engineering organization.

It is exactly this kind of pressure that the Linux Foundation is trying to address — organizations currently have no consistent, vendor-neutral way to measure what they owe, compare costs across providers, or make informed decisions about AI deployment.

## Token pricing varies wildly

There’s no ignoring the elephant in the room, though: Token pricing varies wildly between models and vendors — input tokens, output tokens, cached tokens, different multipliers, different structures. How do you build a common standard across that, and how do you get the frontier model providers who aren’t in the room to buy into it? Storment argues the cloud precedent is instructive — the hyperscalers didn’t help write FOCUS either, but they all adopted it once their customers demanded it.

> > “We did this already with cloud… We expect the same pattern here.”

“We did this already with cloud — we put out consistent frameworks and specs for cloud billing data and now every single hyperscaler supports the standards,” Storment says. “The clouds didn’t start in the room on day one, but based on their customers being there, they all joined. We expect the same pattern here.”

Perhaps more significant than the standards themselves is who is sitting at the table. With some of the world’s largest AI spenders now in the same room, the foundation has an opportunity to establish shared frameworks before the market calcifies around whatever each vendor unilaterally imposes.

“The large token consumers coming together to agree on the best approaches to maximize their consumption of the token-based services will be the fastest win in terms of frameworks, metrics, and guidance for efficient use to drive value and business outcomes,” Storment adds.

***Correction***: A previous version of this article described the Tokenomics Foundation as focused on the economics of AI token consumption. The foundation’s scope covers the full AI token economy — production, consumption, and monetization.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)