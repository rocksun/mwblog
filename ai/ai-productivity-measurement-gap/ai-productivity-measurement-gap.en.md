AI is great at making individuals faster, but the surrounding systems are then slowing everything right back down. This result — or, rather, lack thereof — is amplified by company size and pull request size. To the point that, while AI investment has increased 28 times for most companies, velocity measures are stagnant and even down.

Such is the finding of the recently released State of AI Impact in Engineering from DX, which measures engineering organizations [across speed, effectiveness, quality, and impact](https://thenewstack.io/4-north-star-metrics-for-platform-engineering-teams/).

[Justin Reock](https://www.linkedin.com/in/justinreock/), deputy CTO of DX, tells *The New Stack*, “It is concerning because, when the cost has gone up 28x — which, literally, the only exponential metric is cost — and velocity is not exponential, we’re not shipping exponentially more.”

While AI spend continues to skyrocket, the [innovation ratio](https://getdx.com/research/benchmarks/) — the allocation of engineering effort spent on new feature work versus maintenance, toil, and operational overhead — remains flat. This means AI is not freeing up engineers’ time to spend on interesting business solutions, according to the report.

How is the industry spending so much more money on agentic and AI developer tools, while also doing layoffs, to no avail? Read on as we dive into these disturbing metrics.

## **Is developer experience trending down?**

“It is possible that we’re still in this inflection point where a lot of this saved time is still just being spent on tech debt, backlog stuff that may not necessarily be tagged as a new feature,” Reock says, still hopeful that the gap between the AI cost and benefit is just growing pains.

“But then, on the developer experience side of things, the specific tension in the report between code maintainability and change confidence is also concerning to me.”

These two drivers make up the Developer Experience Index (DXI) benchmark:

* **Code maintainability** – I feel comfortable making changes to the code. I can understand the code in front of me.
* **Change confidence** – I feel confident that when I release code into production, I will not break things.

Traditionally, code maintainability and change confidence have positively correlated, Reock explains, because the first makes engineers more comfortable releasing the second to production.

“AI is making it easier to understand what’s in front of you, and even to make changes to it. But change confidence is now in the negatives,” he says. “We’re more afraid to release the code. So we can understand the code, maintain the code, look at the code, and make changes to it more easily. But we trust less what we’re releasing.”

Which is costing even more. For every point of improvement in DXI, he explains, you return ten hours a year to each engineer. This is the first time that DX has witnessed a drop in this measurement, by two points industrywide.

## **Is AI the square peg to enterprises’ round hole?**

Smaller organizations spend more on AI and get more out of it, DX finds, while legacy software organizations are struggling to see any return on investment.

[Martin Davidson](https://www.linkedin.com/in/0x4d44/), CTO of micro-consultancy a2bic.ai, takes this to the extreme: He and his co-founder, with a combined experience of about 80 years, can wrangle teams of AI agents to do the work of 100 junior to mid-level engineers.

“Small orgs don’t have to pay the non-linear coordination and communication taxes that get worse with the size of the org. Remember [*the Mythical Man-Month*](https://en.wikipedia.org/wiki/The_Mythical_Man-Month): communication channels grow as *n(n−1)/2*, so a team of 10 has 45 channels of overhead,” Davidson explains to *The New Stack*. “Three of those people are effectively there just for alignment. But once you only have one or two people, the comms cost evaporates. As middle management is slashed, there’s no need for monthly all-hands at all levels of the org.”

Across people, processes, and technology, medium-to-large organizations are trying to fit — or shove — AI into existing systems. AI is a fundamental technological and operational paradigm shift. This is what he calls [the renovation problem](https://0x4d44.substack.com/p/the-renovation-problem), where some of these structures aren’t fit for purpose anymore.

“You can’t retrofit this. We’ve got processes and structures which were designed when writing code was the expensive thing. That’s no longer true — code-writing is now essentially free, but we still cling to the old structures. And they aren’t cheap,” Davidson continues. “Company structures are like buildings — at some point you realize they are no longer fit for purpose and they need to be demolished and rebuilt from the ground up.”

Of course this isn’t a new problem. It’s the same reasoning that has held back the vast majority of enterprises from fully moving to the cloud.

As Davison writes: “Maybe the companies that win won’t be the ones that successfully transform. Maybe the winners will be the ones that start fresh, unencumbered. That’s uncomfortable if you’re inside a legacy org. And probably even more so if you’re running one.”

Thankfully, AI is very good at pattern recognition, making it very useful at [unraveling the mystery of legacy systems, migrating them to the cloud](https://thenewstack.io/finally-platform-engineering-for-enterprise-cloud-migration/), and rewriting them with AI in mind.

## **AI exacerbates code bloat**

Of course, many teams — and their prompts — are ignoring universally accepted success patterns at the speed of AI, including how smaller batch sizes contribute to more stable releases.

The DX report finds that in July 2025, the median PR size was 42 lines of code, while a year later it’s at 72 lines of code.

To add to this, of all the DXI indicators measured over the last quarter, incremental delivery — engineers reporting that they get to work on small, incremental changes — took the biggest hit.

“Which carries all kinds of forward benefit — revert, less review, more understandable documentation, better unit test cases, like all this stuff,” Reock says. “That, in correlation with PR size, I think, is also concerning around quality.”

And it’s not just DX uncovering these worrying trends. [LinearB’s AI engineering productivity gap report](https://linearb.io/resources/ai-engineering-productivity-gap) ranks 253 organizations on their AI usage into four buckets. This research released this week finds that smaller pull request size directly ties to more successful AI adoption. “Elite organizations” sitting in the top 10% had average pull requests of less than 100 lines of code, while those at the bottom of the pack — labeled as “Needs focus” — have pull requests of more than 228 lines of code.

## **Can you improve what you don’t measure?**

Both DX’s and LinearB’s research draws on their own data, which comes from organizations using their products to measure the quantitative and qualitative developer experience, so neither result is the whole picture. It could actually be much worse for the rest of the industry.

According to research from LeadDev’s [AI Impact Report 2026](https://leaddev.com/the-ai-impact-report-2026-pre-register), due to publish later this August, only 31% of teams interviewed are measuring AI’s impact at all. LeadDev defined these measurements as:

* Real productivity gains
* Security risk
* Retention of core engineering skills
* Agentic AI governance
* Team restructuring
* Junior hiring and training

Among organizations that have actually started adopting AI-powered developer tools, the LeadDev report finds 70% now describe themselves as having adopted “widely or completely,” with only 26% reporting that AI has boosted engineering productivity by more than 25%. That 26%, [Michael Hill](https://www.linkedin.com/in/michael-hill-1a17b08b/), managing editor at LeadDev and report author, clarifies, includes respondents going on instinct, not just confirmed data.

“The productivity optimism — 26% seeing big gains — and the measurement gap — only 31% actually tracking it — are two separate findings from two different questions,” Hill tells *The New Stack*, which means that “most of the people reporting gains aren’t the same people who can prove it.”

As we know, engineering is a science, so you can’t improve what you don’t measure. But even for those measuring it, the results are worrying.

Reock points to the DXI score going down for the first time last quarter:

“We should really be paying attention to that because our customer base trends up, right? The data is heavily biased because they [DX customers] are investing in developer experience, like actively. They bought a product, and so that number tends to trend upward for our cohort of customers. So to see this actually go down is very concerning.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)