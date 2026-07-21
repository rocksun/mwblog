A conversion-rate alert fires 30 minutes after a pricing engine deploys updated discount rules. The analytics platform holds millions of checkout events for the relevant window. An agent retrieves 50 session logs showing cart abandonment and reports a probable pricing regression.

But retrieval alone can’t answer the questions that matter. Did the conversion rate actually drop across the full buyer population, or is the sample skewed toward a single region? Are price-sensitive customer segments disproportionately affected? Did page load time spike at the same time, making this a performance problem rather than a pricing one?

The agent found relevant records. It didn’t measure how the observed population changed.

## Where retrieval alone falls short

Retrieval locates candidate evidence: log lines, session recordings, and documents that match a query. Analytics measures a population. It computes a rate, compares time windows, aggregates across dimensions, and quantifies change.

> “The agent found relevant records. It didn’t measure how the observed population changed.”

An agent that reads 50 abandonment logs and concludes “the pricing change caused drop-off” has skipped the step where you verify that the conversion rate decreased after deployment, compare affected and unaffected customer segments, and test whether technical metrics show the same shift.

For agents reasoning about fast-changing live systems, the decisive context often [can’t be retrieved](https://thenewstack.io/retrieval-ai-agent-architecture/) or prepared in advance. It has to be computed against current data.

## What an evidence packet should contain

If the analytical layer is going to [serve an LLM](https://thenewstack.io/introduction-to-vllm-a-high-performance-llm-serving-engine/), the interface between them needs a contract. The simplest version is the SQL query itself: return the query alongside the result so someone can re-run it.

But SQL alone doesn’t tell the agent whether the data is complete, whether the calculation is approximate, or whether competing explanations were tested. What if the response included all of that?

One approach is a bounded evidence packet: a structured response that carries the measurement along with everything required to interpret, question, or re-execute it.

An `as_of` timestamp tells the agent when the query ran. Per-source `ingest_watermarks` tell it how current the underlying data is for each region or pipeline. A `known_gaps` field makes incomplete coverage explicit rather than leaving the agent to assume completeness.

If EU checkout events are lagging by 90 seconds, that fact belongs in the packet, not buried in a runbook. A `data_cutoff` clause anchored to ingestion time makes the result auditable and re-executable even after late-arriving events land.

The packet should also reference a versioned metric definition and a parameterized query template, not just a query ID or hash. When an agent reports that checkout conversion dropped 22%, reviewers need to see which calculation produced the number, over which population, with which parameters.

These identifiers should resolve to immutable versions in a durable registry, with the referenced definitions retained or cached alongside the packet for incident use.

Many analytical computations use approximate algorithms like t-digest percentiles and HyperLogLog cardinalities. Both are legitimate, but the agent shouldn’t present an approximate result as exact. A `calculation` field that states the method and flags approximation keeps this visible.

A single metric in isolation invites cherry-picking, so the packet should include counterchecks: related metrics tested against their own baselines. If conversion dropped while average order value rose and page load time remained flat, that would weaken a site-performance hypothesis and direct the investigation toward price sensitivity in specific customer segments.

Drill-down session IDs help human investigators, but the packet needs to make it clear that the example sessions illustrate the aggregate. They don’t prove it.

Here’s what this could look like for the checkout conversion scenario:

```

json

{
  "observation": {
    "metric": "checkout.conversion_rate",
    "unit": "percent",
    "current_value": 3.28,
    "baseline_value": 4.21,
    "change": { "relative_pct": -22.1, "absolute_percentage_points": -0.93 }
  },
  "baseline_definition": {
    "description": "Mean conversion rate for the same 30-minute interval",
    "lookback": "previous 7 days"
  },
  "scope": { "service": "pricing-engine", "deployment": "pricing-2026-06-15.1" },
  "time_window": { "start": "2026-06-15T10:15:00Z", "end": "2026-06-15T10:45:00Z" },
  "as_of": "2026-06-15T10:46:03Z",
  "ingest_watermarks": { "default": "2026-06-15T10:45:58Z", "eu-west-1": "2026-06-15T10:44:31Z" },
  "known_gaps": [{ "region": "eu-west-1", "detail": "checkout events delayed ~90s" }],
  "data_cutoff": "ingested_at &lt;= 2026-06-15T10:45:58Z",
  "metric_definition": { "id": "checkout-conversion-v2.1", "registry_uri": "https://metrics.internal/defs/checkout-conversion-v2.1" },
  "query": {
    "template": { "id": "post-deployment-conversion-v1", "registry_uri": "https://metrics.internal/queries/post-deployment-conversion-v1" },
    "parameters": { "deployment": "pricing-2026-06-15.1", "window_start": "2026-06-15T10:15:00Z", "window_end": "2026-06-15T10:45:00Z", "data_cutoff": "2026-06-15T10:45:58Z" },
    "query_id": "query-b8d4e2f7"
  },
  "coverage": { "sessions_observed": 142380, "sampling_policy": "unsampled" },
  "calculation": { "method": "exact count ratio", "approximate": false },
  "drilldown_examples": ["session-a91f", "session-d47c", "session-02eb"],
  "segment_breakdown": [
    { "segment": "discount-sensitive buyers", "segment_definition": "segment-discount-sensitive-v1", "current_value": 2.41, "baseline_value": 3.62, "unit": "percent", "change": { "relative_pct": -33.4, "absolute_percentage_points": -1.21 } }
  ],
  "counterchecks": [
    { "metric": "avg_order_value", "current_value": 87.40, "baseline_value": 72.15, "unit": "usd", "materiality_threshold_pct": 10, "result": "above baseline" },
    { "metric": "page_load_time_p95", "current_value": 1.82, "baseline_value": 1.79, "unit": "seconds", "materiality_threshold_pct": 15, "result": "within baseline" }
  ]
}

```

## Separating database observations from agent interpretation

An evidence packet is only as trustworthy as the system that produces it.

For established metrics, a governed layer should expose [approved definitions and governed query paths](https://clickhouse.com/blog/visa-conversational-agents). The agent selects a template and supplies parameters. The query engine executes with read-only credentials and resource limits, then returns results through an evidence adapter that applies the structured response schema.

> “An evidence packet is only as trustworthy as the system that produces it.”

For unforeseen investigations, a governed exploratory path on a read-only replica with SQL validation, audit logging, and strict cost limits can [support ad hoc analysis and arbitrary SQL without opening unrestricted access](https://clickhouse.com/blog/announcing-managed-clickstack-mcp-server).

This separation keeps database observations and model interpretations visibly distinct. The database doesn’t produce conclusions. It produces auditable, re-executable observations. The LLM interprets those observations and recommends an action.

A policy gate or human reviewer can then inspect the packet, re-run the query, and decide whether the interpretation holds. Without that separation, the agent’s confidence becomes indistinguishable from the system’s certainty.

## Supporting the agent evidence workload

Supporting governed agentic analytics changes the workload profile. Each agent interaction can trigger dozens of concurrent queries as it explores datasets and reasons through parallel possibilities. A single user question becomes a burst of analytical queries, and that shift in concurrency is [redrawing what databases need to handle](https://clickhouse.com/blog/ai-redrawing-database-market).

![Diagram showing the changing nature of modern BI workloads and their impact on the data warehouse](https://cdn.thenewstack.io/media/2026/07/9aea591f-image-1024x376.png)
> “The useful agent isn’t the one that can consume the most data. It’s the one whose system can show exactly what it measured, how it measured it, and what remains uncertain.”

## What makes an agent trustworthy

The useful agent isn’t the one that can consume the most data. It’s the one whose system can show exactly what it measured, how it measured it, and what remains uncertain. Start with the evidence contract. Trustworthiness begins with the [auditability](https://thenewstack.io/agentic-ai-observability-auditing/) of what the agent receives.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/07/e3f55e06-manveerprofile_20845237de.avif)

Manveer is co-founder of Zenith, previously Director of Engineering at Confluent and led Growth Engineering at Dropbox.

Read more from Manveer Chawla](https://thenewstack.io/author/manveer-chawla/)