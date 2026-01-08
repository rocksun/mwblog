Even as AI offloads repetitive tasks and accelerates learning and productivity, you hear more anecdotes every day about AI systems that weren’t quite ready for production. Examples of AI-powered errors in [financial services](https://www.ft.com/content/9317776f-c7fb-4798-86f2-8edd1fba9274), [health care](https://futurism.com/neoscope/google-healthcare-ai-makes-up-body-part) and the [legal system](https://fortune.com/2025/05/18/anthropic-claude-lawyer-mistake-citation-legal-filing-large-language-model-llm-latham-watkins/) reveal what’s at risk when these systems are built on a fragmented data foundation.

Although we can’t count on AI to always get it right just yet, it’s not necessarily because the underlying models aren’t ready. Often, it’s because AI systems can’t access the data they need to [understand the current state of the business](https://thenewstack.io/why-agentic-ai-needs-a-context-based-approach/). Organizations that can effectively [serve “context”](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) to large language models (LLMs) in real time can build AI agents that are trained on [domain-specific knowledge](https://www.infoq.com/articles/beyond-chatbots-domain-specific-genai/) and make more optimal decisions based on fresh, contextualized information.

That’s why many enterprises are starting to care about the same migration initiatives cloud architects have been pushing for decades: moving on-premises databases and applications to more agile cloud environments.

## Common Errors Slow the Path To AI in Production

McKinsey research estimates that [75% of cloud migrations](https://www.mckinsey.com/~/media/mckinsey/industries/technology%20media%20and%20telecommunications/high%20tech/our%20insights/cloud%20migration%20opportunity%20business%20value%20grows%20but%20missteps%20abound/cloud-migration-opportunity-business-value-grows-but-missteps-abound_final.pdf) run over budget or off schedule, costing organizations a combined $100 billion every three years. The legacy “big bang” [migration model is the root of the problem](https://thenewstack.io/ai-wont-save-you-from-your-data-modeling-problems/), as it requires a single, high-risk cutover and often triggers cascading failures.

Consider these scenarios:

* Migration programs drag on for two years, require endless replanning and still fail to hit their deadlines.
* A dozen teams waste time staring at dashboards and debating issues between the new microservices and the legacy monolith.
* AI initiatives are perpetually stalled behind that one “last critical system,” pushing roadmaps back by quarters.

You can’t afford to take up the budget only to deliver these kinds of outcomes. Instead, you need to treat migration of your data systems as an evolutionary, testable process rather than a cliff-edge event. And you need an operating model that assumes and manages continuous change so ongoing projects can rely on live systems in the meantime.

The [strangler fig pattern](https://martinfowler.com/bliki/OriginalStranglerFigApplication.html), first described in 2004 by [Martin Fowler](https://martinfowler.com/), defines an ideal architectural approach to safely modernizing legacy, batch-based data systems while reducing migration costs and unlocking the real-time context AI agents need. By combining this pattern with proxy-based traffic steering, your engineering team can incrementally break up its monolithic databases and applications without service interruption.

## How Strangler Fig Works: Incrementally Replacing Monolith

The strangler fig pattern breaks up cloud migrations so a massive undertaking becomes manageable steps. Build new, cloud native services to replace existing capabilities; run both the legacy and cloud native services in parallel; validate the new service with gradual cutovers; and then retire the legacy system.

You repeat this process until the monolith is progressively starved and shrunk to nothing, and no single, high-stakes weekend cutover is ever required.

## How To Use the Proxy Layer for Safe, Reversible Cutovers

The architectural pattern demands sophisticated traffic control, which is where proxy-layer steering comes in. An API gateway, reverse proxy or service mesh acts as a critical traffic shield in front of your systems, requiring no client-side changes whatsoever. This enables incremental migration without risking downtime or lost data, as:

* All inbound requests hit the proxy before reaching any system.
* Routing rules automatically determine whether traffic goes to the legacy monolith path or the new microservice.
* You shift traffic from legacy to cloud gradually: 100% legacy → 90% legacy, 10% new → 75% legacy, 25% new → 50% legacy, 50% new → 100% new.

If any issues surface, you can instantly roll traffic back without involving clients.

The entire blueprint relies on a central, scalable event streaming backbone to manage the vast flow of business events across complex, hybrid environments.

## A Repeatable 4-Step Migration To Increase Data Availability

Your migration starts with a cloud readiness assessment using the 6Rs framework: rehost, replatform, refactor, repurchase, retire and retain. This framework forces a critical decision on a per-application basis: whether to replace the system (refactor/repurchase), modernize it (replatform) or leave it as is (retain/retire). For systems categorized as refactor or replatform, follow this four-step execution path:

1. **Select target domain:** Choose a domain or bounded context like “open account” or “send payment.” Route all traffic for this domain through a controllable proxy.
2. **Unify batch and real-time data:** Implement change data capture (CDC) flows from the legacy databases to the event streaming platform. Define robust schemas and contracts on Day 1.
3. **Build event-driven microservices:** Build new microservices that exclusively consume and produce streams. The platform establishes the single, canonical source of truth for the domain.
4. **Shift and retire:** The proxy gradually dials traffic to the new service. You rigorously monitor metrics and data quality. Once validated, you retire the legacy path. Then, repeat with the next domain.

This blueprint avoids common architectural pitfalls, including proxying without streaming (which creates silos) and streaming without data contracts (which leads to schema chaos). This is not just a theory. In fact, [Michelin](https://www.frontier-enterprise.com/michelin-powers-data-driven-inventory-system-with-confluent/) used this incremental model for a nine-month migration to the cloud, achieving a documented 35% cost savings and 99.99% uptime, with less than two hours of downtime per application, illustrating that speed and stability are not mutually exclusive.

Spread across a portfolio, this is the difference between accumulating additional unplanned costs and having the capital to fund the next wave of AI initiatives.

## Modernizing Your Data Estate Elevates Your AI Strategy

AI roadmaps are often casualties of brittle batch systems and migration friction, consuming time and budget. Using the strangler fig pattern empowers the [engineer as the new architect and orchestrator](https://thenewstack.io/the-engineer-in-the-ai-age-the-orchestrator-and-architect/):

* It enables incremental modernization with surgical precision, not major disruption.
* It delivers real-time business visibility directly to your AI models, eliminating stale data.
* It significantly reduces the migration tax that holds your initiatives captive.

Organizations that abandon “big bang” migrations for strangler fig and proxy-based steering position themselves to capture the next wave of value, saving vast portions of today’s migration overruns.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/06/1fb12dff-cropped-9ca9a4b7-joseph-morais-600x600.jpeg)

Joseph Morais serves as a technical champion and data streaming evangelist at Confluent. Before joining Confluent, Joseph was a senior technical account manager at AWS helping enterprise customers scale through their cloud journey. Joseph has also worked for Amino Payments,...

Read more from Joseph Morais](https://thenewstack.io/author/joseph-morais/)