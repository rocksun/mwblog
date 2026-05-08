Two new protocols, one from Stripe and one from a fintech startup called iWallet, are attempting to solve the same problem: the payments infrastructure we have was built for humans. AI agents that need to buy things, route funds, and settle multi-party transactions are running into walls. Here’s what has to change.

When Stripe launched in 2010, it solved a specific problem: collecting money on the internet was unnecessarily hard. Stripe abstracted away the banking relationships, the merchant accounts, and the fraud logic. Suddenly, anyone could accept a credit card in an afternoon. It was infrastructure for humans trying to do commerce online.

We’re now in a different moment. AI agents, the software that plans, acts, and evaluates outcomes autonomously, are starting to need to spend money. Not just authorize a transaction that a human later reviews, but actually complete purchases, route payments across multiple parties, and settle complex multi-vendor financial relationships without anyone touching a keyboard. The infrastructure Stripe built for human-driven ecommerce wasn’t designed for this, and the gap is becoming a real bottleneck.

Two recent developments make this tension obvious. Tempo and Stripe have jointly released the Machine Payments Protocol (MPP), a standard for programmatic transactions between [AI agents and the services they need](https://thenewstack.io/why-ai-agents-need-their-own-identity-not-yours/) to use. Separately, iWallet, a fintech company serving the home services industry, has sketched out what it calls an Autonomous Settlement Protocol (ASP), designed for scenarios in which verified physical events, such as a completed HVAC repair, automatically trigger multi-party financial settlements. These are two different teams, attacking two different layers of the same problem. Neither is sufficient on its own. Together, they reveal how much the payments stack needs to change.

## **Payments were built for the people**

Today’s payment infrastructure assumes a human is in the loop. Creating accounts requires identity verification. Selecting a pricing tier requires reading the UI. Entering billing details requires a form. Even the most developer-friendly payment APIs assume a human engineer configured them at some point, and that a human cardholder is authorizing the charge.

AI agents break these assumptions. An agent that autonomously schedules a cloud compute job, calls a paid API, and then routes the cost to the appropriate cost center needs to transact without human intervention. The same agent that books a flight leg as part of a multi-step travel itinerary can’t stop to enter its corporate card details in a checkout form. The moment you introduce a required human touchpoint, you’ve interrupted the autonomy that makes agents useful.

This [problem grows harder as agentic systems](https://thenewstack.io/ai-agents-in-legacy-systems-the-problem-no-one-talks-about/) become more capable. Simple API calls charging per-token are already happening. The more interesting and difficult cases involve agents that need to purchase services, trigger real-world actions, and manage ongoing financial relationships on behalf of users or organizations, without turning every transaction into a support ticket.

## **Layer one: The machine payments protocol**

The Tempo/Stripe Machine Payments Protocol targets the transactional layer directly. The protocol establishes a standard for how an AI agent can request a resource, authorize payment, and complete a transaction programmatically. Businesses accept these payments through existing Stripe infrastructure, with cards, buy-now-pay-later options, and stablecoins all supported, while retaining the same reporting, fraud protection, and settlement pipelines they already use.

Early use cases demonstrate the range of what’s already working: agents paying per API call, purchasing services on demand, and triggering real-world actions such as sending physical mail or placing food orders. These are relatively simple, discrete, single-party, human-configured transactions at the merchant end, even if the buyer side is automated.

What MPP doesn’t address is the settlement layer: what happens after money changes hands when multiple parties are owed portions of that money. That’s a different problem, and it’s where the home services industry offers an unexpectedly instructive case study.

## **Layer two: Multi-party settlement in the physical world**

Home services generate over a trillion dollars annually in the United States. A single HVAC installation might involve a manufacturer, a regional distributor, a licensed contractor, a financing company, and one or more utility rebate programs. Each participant expects their portion of the transaction. Today, every one of those relationships is resolved through manual invoicing, spreadsheets, and reconciliation that can take days or weeks after the job is complete.

> “Payments move money from the customer… Settlement determines where that money ultimately goes. Our goal is to automate that entire process for the service economy.”   
> —Jim Kolchin, CEO of iWallet

[Jim Kolchin](https://www.linkedin.com/in/jimkolchin/), CEO of iWallet, frames this as a settlement problem rather than a payments problem. “Payments move money from the customer,” Kolchin says. “Settlement determines where that money ultimately goes. Our goal is to automate that entire process for the service economy.” The distinction matters because the two layers require different solutions.

iWallet already processes hundreds of millions of dollars in payment volume for contractors and service companies. Its existing platform handles mobile payments, financing integrations, rebate processing, and post-job fund distribution. The next version of the platform, internally called iWallet 4.0, introduces what Kolchin describes as a programmable settlement layer: once a payment is captured, a defined set of rules automatically determines how funds move through every participant in the job’s supply chain.

The more technically interesting addition is machine verification. Home services environments are increasingly data-rich. Modern HVAC systems transmit performance telemetry. Installers photograph completed work. Equipment carries serialized identifiers that can be checked against manufacturer records. Energy efficiency programs collect installation data to determine if customers qualify for rebates.

The ASP design uses AI agents to analyze these signals, job documentation, equipment data, installation images, and IoT device readings and confirm that a service event was completed correctly. That verification event then automatically triggers the settlement sequence. No paperwork submission. No waiting for a rebate program to process a form. The event itself closes the financial loop.

## **Why this is hard: The technical gaps**

Both approaches are directionally right, and both run into [real engineering problems](https://thenewstack.io/nvidia-nemoclaw-openclaw-security/).

Machine-to-machine payment authorization requires solving identity and trust in ways current systems don’t support cleanly. When an AI agent presents credentials to complete a purchase, who is the accountable party? How are spending limits enforced? What happens when an agent makes an error or is manipulated into a bad transaction? Card networks, bank risk systems, and fraud detection pipelines were trained on human behavioral signals. Agent-initiated transactions will look anomalous by default.

The settlement layer adds another dimension of complexity. Programmable fund distribution requires formalized agreement structures between parties that don’t currently exist in standardized form. A contractor, a manufacturer, and a utility rebate program each have different systems, different timelines, and different conditions under which they expect to receive payment. Getting those parties to agree on a machine-readable settlement specification before a job starts is a coordination problem that goes well beyond software.

Machine verification introduces its own reliability questions. Computer vision confirming that an installation photograph matches expected standards, or that sensor telemetry indicates a repair was successful, needs to perform at a level where disputed outcomes don’t create more overhead than the manual processes they replace. False positives trigger payments for incomplete work. False negatives delay legitimate contractors.

And underneath all of this is a regulatory layer that hasn’t kept pace with the technology. Automated fund disbursement across multiple parties is starting to look like money transmission, which is one of the more heavily licensed activities in financial services. How regulators treat agent-authorized transactions, and who bears liability when they go wrong, isn’t settled.

## **The stack that needs to exist**

If you map what’s required for autonomous economic loops to close reliably, you get something like this:

At the transactional layer, protocols like MPP need to mature beyond early use cases to handle authorization, identity, and error recovery in ways that financial systems find trustworthy. The stablecoin support in MPP is notable here. Stablecoins sidestep some of the friction in legacy card networks and could become the native currency of agent-to-agent commerce precisely because they’re programmable.

At the settlement layer, the work is more about standardization than technology. The software to route funds conditionally already exists. What doesn’t exist is a shared specification language that multiple parties, equipment suppliers, financing companies, warranty administrators, and rebate programs can agree to encode their payment terms in. iWallet is effectively trying to create that specification for one vertical. The harder question is whether it generalizes.

At the verification layer, the requirement is for AI systems capable of confirming real-world service events with sufficient reliability to justify triggering financial consequences. This is where the intersection of physical IoT systems and agentic AI becomes genuinely novel engineering territory. The signals exist: equipment telemetry, image documentation, and serialized component tracking, but integrating them into a pipeline that settlement logic can trust requires infrastructure investment that most service industries haven’t made.

## **What’s actually shipping**

To be direct about the state of play: MPP is real and live, handling discrete agent-to-service transactions in production. iWallet’s existing platform is real and processing significant payment volume. The ASP roadmap is a forward-looking design, not a shipping product.

The gap between what MPP handles today and what ASP envisions is actually a useful map of the work ahead. Paying for a single [API call is a solved problem](https://thenewstack.io/solving-the-problems-that-accompany-api-sprawl-with-ai/). Automatically distributing the proceeds of that call across ten counterparties based on machine-verified physical outcomes is several years of infrastructure work away from being routine.

> The agents people are building today are, at best, authorized to trigger human-reviewed payments. The agents people will be building in three years will need to close economic loops autonomously.

But the direction is clear enough that developers building agentic systems should be thinking about it now. The agents people are building today are, at best, authorized to trigger human-reviewed payments. The agents people will be building in three years will need to close economic loops autonomously. The [infrastructure](https://thenewstack.io/how-oracle-is-meeting-the-infrastructure-needs-of-ai/) [those agents need](https://thenewstack.io/how-oracle-is-meeting-the-infrastructure-needs-of-ai/) doesn’t yet fully exist, and the teams building it are only beginning to coordinate.

The fintech revolution of the 2010s made it easy to collect money from humans on the internet. The next decade’s version of that build will make it possible for software to manage money on behalf of humans, and eventually between machines, with the reliability that financial relationships require. The Tempo/Stripe and iWallet work are early bets on what that infrastructure looks like. The ground-floor engineering problems are still wide open.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/05/3fbe23aa-cropped-21fb730d-biggs-4881-square1.jpg)

John Biggs is an entrepreneur, consultant, writer, and maker. He spent fifteen years as an editor for Gizmodo, CrunchGear, and TechCrunch and has a deep background in hardware startups, 3D printing, and blockchain. His work has appeared in Men’s Health,...

Read more from John Biggs](https://thenewstack.io/author/john-biggs/)