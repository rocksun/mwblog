When building data platforms for large institutions, we often make decisions based on what we can see, ignoring blind spots, or what we call “invisible data,” which can be more dangerous than bad data. That invisible data includes exceptions, approvals, context, undocumented institutional knowledge, cross-system syntheses, and judgment calls that help run the business but rarely make it into any system.

I’ve seen this pattern across every industry I’ve worked in. My team at a large social media company conducted a metadata audit that revealed most production datasets were orphaned, unowned, or redundant. Nobody had a reliable count of running APIs. Traditional catalog tools delivered stale metadata upon arrival. To solve it, we built graph-based connectors from scratch, stitched together asset lineages, and recovered hundreds of [millions in savings](https://thenewstack.io/amazon-to-save-millions-moving-from-apache-spark-to-ray/).

But even after we solved the visibility problem for structured data, we kept hitting the same wall: the reasoning behind the data was nowhere to be found in the system.

For decades, losing that reasoning was an acceptable cost. Teams could regain it through experience and onboarding. Decisions grew inconsistent, and the inconsistency stayed invisible. AI agents expose those inconsistencies.

## The wall every agent hits

Consider what happens when an AI agent handling a customer renewal must decide whether to approve a 20% discount, even though the policy caps renewals at 10%. A well-instrumented agent can pull the customer’s revenue from the CRM, check open support tickets, scan recent incidents, and evaluate the relevant policy document. That is the visible layer.

> “But even after we solved the visibility problem for structured data, we kept hitting the same wall: the reasoning behind the data was nowhere to be found in the system.”

What it cannot access is the reasoning that lives in the heads of people who’ve done this job long enough to accumulate it, a history of exceptions to the discount rate and undocumented changes in decision-making after a reorg.

Without that reasoning, the agent makes the wrong call, escalates to a human who reconstructs the same logic from scratch, or applies written policy rigidly in situations the organization has consistently handled with judgment. All three are failures, and they compound at scale.

## Why incumbents cannot close this gap

The constraint is architectural, not a product gap any vendor can close with a roadmap item.

Operational systems of record — CRM, ERP, and HRIS — store the current state. When an exception is approved, the context that justified it disappears. You can see that the discount changed, but you cannot replay the state of the world at the moment someone made that call, query it, or use it as a precedent for future reasoning.

Data platforms face a different problem. They receive data via Extract, Transform, Load (ETL) pipelines after decisions have already been made. By the time a record lands in the warehouse, the reasoning context has already evaporated. These platforms can show you history, but not causality, because causality requires being present in the execution path at commit time.

> “By the time a record lands in the warehouse, the reasoning context has already evaporated.”

Every major software vendor now builds agent capabilities, and those agents perform well within their own system boundaries, but they inherit the parent system’s constraints. A CRM agent does not see the [infrastructure incident in the monitoring](https://thenewstack.io/getting-started-with-infrastructure-monitoring/) system. A support platform agent does not see the churn signal buried in an internal thread. The cross-system synthesis that experienced humans perform instinctively stays invisible to any agent confined within a single vendor’s perimeter.

## The missing dimension

Most enterprise knowledge systems track which entities exist, how they relate to one another, and how their states change over time.

A fourth dimension is almost universally absent: decision events, or [structured records](https://thenewstack.io/understanding-log-events-why-context-is-key/) of the moments when organizational judgment turned context into action. Most teams don’t record which inputs drove a decision, which policy version applied, or what conditions an approver attached.

That reasoning evaporates in Slack threads, on calls, and in onboarding conversations with people who eventually leave. Before agents, this was a manageable loss. An experienced employee could reconstruct the reasoning through memory and relationships.

In an agent-driven environment, the gap becomes critical. Agents need to understand not just what the policy says, but also how the organization has historically addressed it in practice. A living, queryable record of organizational judgment, captured at the moment decisions are made, is what makes that possible.

The case for building this layer grows stronger with every decision the organization makes. Each captured decision trace becomes a searchable precedent. Each exception calibrates future exception routing. The organizational knowledge that previously walked out the door with departing employees becomes a lasting resource that survives restructurings and acquisitions.

## What to do about it

The architectural constraint doesn’t require waiting for a vendor to solve it. The following five practices help build the missing layer incrementally, without replacing existing infrastructure.

**Audit your exception surface.** Map the decisions your organization makes that written policy does not fully explain: pricing exceptions, approval overrides, compliance carve-outs. These are the gaps where agents will fail first. Prioritize which to capture rather than trying to capture everything at once.

**Instrument the execution path, not just the outcome.** Most logging captures what happened. Decision capture also requires recording why, including which inputs were considered, which policy version applied, who approved, and what conditions they attached. Add structured event emission to consequential workflows before deploying agents into them.

**Evaluate vendors on cross-system reasoning.** When assessing [agent platforms](https://thenewstack.io/google-gemini-agent-platform/), ask specifically how they handle decisions that require context from multiple systems. If the answer depends entirely on pre-built integrations or a single data model, the structural gap will surface as a production failure.

**Start with high-frequency, high-stakes flows.** Customer renewals, security exception reviews, incident escalations, and vendor approvals are strong starting points. They happen often enough to quickly build a meaningful corpus of precedents, and agent errors here carry real cost.

> “Agents reason from what is explicitly available at execution time, at a scale and speed no human knowledge-transfer mechanism can match.”

**Design for replay, not just retrieval.** A useful decision record is a structured artifact that teams can query, compare to prior decisions, and use to validate whether a proposed action is consistent with how the organization has actually behaved.

## The deeper implication

Agents reason from what is explicitly available at execution time, at a scale and speed no human knowledge-transfer mechanism can match.

The enterprises that extract lasting value from AI agents will not be the ones with the most sophisticated models. They will be the ones who did the work of making their organizational judgment queryable by capturing not just what their data says, but how their organization has chosen to act on it over time.

The iceberg is real, and the agents are here. Every decision your organization makes without capturing its reasoning is institutional knowledge you will never get back.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/07/144335cf-nitin-singhal-600x600.jpeg)

Nitin Singhal is the VP of Data and Monetization Engineering at GitLab.

Read more from Nitin Singhal](https://thenewstack.io/author/nitin-singhal/)