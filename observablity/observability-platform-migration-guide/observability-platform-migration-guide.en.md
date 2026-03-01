Observability platform migrations are rarely simple. You’re still balancing risk (don’t break on-call), scope (don’t try to move everything at once), and organizational change (getting teams to validate and adopt new workflows). The goal of this post is to share the common patterns that make it manageable when you’re ready to undertake it using open standards instrumentation.

We’ll focus on migrations where metrics, traces, and logs already flow through open-source and open-standard tools such as Prometheus, OpenTelemetry (OTLP), and [Fluent Bit](https://chronosphere.io/fluent-bit/). In those environments, you can typically migrate by rerouting pipelines, migrating only the dashboards and alerts that matter most, and dual-running until you trust the cutover.

> “Open standards can streamline the migration path, but getting to open standards may be its own migration wave.”

If you don’t have open standards instrumentation today, there’s an additional step: re-instrumenting. When you’re using proprietary agents, SDKs, or closed ingestion formats, moving platforms often means replacing instrumentation across services – an effort that can take weeks or even months depending on fleet size, release cadence, and coverage requirements. In other words, open standards can streamline the migration path, but getting to open standards may be its own migration wave.

From there, we’ll walk through the most reliable, step-by-step patterns teams use to migrate safely while keeping visibility intact throughout the process.

## How to migrate with open-source tooling

### Planning: Define what “success” means

Before starting the migration, document three things:

1. Which services are in scope for the first migration wave (ideally lower-impact services first)?
2. Which teams own those services and will be responsible for validation and sign-off?
3. Which dashboards and alerts are non-negotiable for day-to-day operations; everything else is secondary.

This documentation becomes your north star when prioritizing work across teams.

## Migration steps

### Step 1: Prioritize what actually matters

Before you inventory everything, identify what you actually need to migrate.

**Create a focused list:**

* Identify the dashboards that on-call engineers actually use during incidents, site reliability engineers (SREs) reference for service-level objective (SLO) reviews, or leadership relies on in weekly meetings. Often, you’re left with 10-20 dashboards.
* Document the alerts that page someone at night, appear in runbooks, or protect revenue-critical services. Typically, you’re left with 20-50 alerts.

Treat these as phase-one migration artifacts. Everything else can wait.

For each dashboard and alert, document:

* Where it lives in your current platform (URL, folder, owner).
* Which teams own and rely on it.
* Any known quirks (“this alert is noisy,” “we ignore that panel”) so the right people can validate and sign off during migration.

Understanding which data actually drives decisions is critical. Teams often discover they’re paying to store massive amounts of telemetry that nobody uses.

### Step 2: Inventory your telemetry

You can’t move what you haven’t mapped. For the in-scope services, document where telemetry originates and how it flows through your existing open source infrastructure.

* **Metrics**: How is your Prometheus setup configured? Document which services are scraped directly by Prometheus servers versus those using exporters (node, Kubernetes, database, cloud). Map how metrics reach your current platform — are you using native remote-write, multiple remote-write endpoints, or federation between Prometheus instances?
* **Traces**: Review your OpenTelemetry instrumentation. Which services use OpenTelemetry SDKs versus auto-instrumentation? Map the flow from instrumented services through your OpenTelemetry Collectors to your current backend. Document any processors, samplers, or transformations in your collector pipelines.
* **Logs**: Document your Fluent Bit configuration. Where are logs being collected from, and which output plugins are currently in use? If you’re using a centralized log pipeline or router, understand how data flows through that architecture.

> “Understand your current data routing so you can confidently add the new backend as a parallel destination without disrupting existing flows.”

The goal here is to understand your current data routing so you can confidently add the new backend as a parallel destination without disrupting existing flows.

### Step 3: Add the new backend as a second destination

Instead of ripping out your current platform, introduce the new backend as a shadow destination for a subset of services. Keep both systems up and running to ensure your team maintains visibility throughout the migration. Additionally, you want sufficient historical data in your new observability platform before switching over entirely. The amount of historical data varies by company and should be a key consideration.

#### Metrics

If you’re using Prometheus remote-write, add a second remote-write endpoint pointing to the new backend (or re-point non-critical services first). If you’re using Prometheus servers for scraping, either reconfigure them to write the new backend or mirror scraped data using remote-write or federation.

If your new platform is Prometheus-compatible, this is mostly wiring; you’re redirecting existing traffic to a different endpoint, not rebuilding your pipeline.

#### Traces

With the OpenTelemetry Collector, add an additional exporter pipeline that sends traces to the new backend in parallel (OpenTelemetry Protocol → new backend). Keep configs as similar as possible to your existing trace pipeline for direct comparison during the dual-run.

Platforms that speak OpenTelemetry Protocol (OTLP) natively make this simple; you reuse the same OpenTelemetry exporters and processors you already trust.

#### Logs

If using Fluent Bit, add another output that sends logs to the new backend’s ingestion endpoint. If you already have a centralized log pipeline or router, fan out from there rather than touching every application pod.

### Step 4: Convert queries and dashboards

#### Focus on core queries first

Most proprietary platforms either use a PromQL-like language or run their own DSL on Prometheus-style series and labels. Your new backend should offer PromQL compatibility or a clear mapping.

Start with the 80% use cases:

* **Simple time series**: single metrics with filters like  

  ```

  `{env="prod", service="api"`}
  ```
* ****Basic aggregations:****  

  ```

  `sum`, `avg`, `max`, `histogram_quantile`
  ```
* ****Tag → label mapping:****  

  ```

  `env:prod`→ `{env="prod"}`
  ```

Only after that’s solid, tackle:

* Cross-metric arithmetic
* Joins and multiseries expressions
* Vendor-specific or “magic” functions

#### Rebuild only critical dashboards

Use the priority list from Step 3 as the scope.

For each dashboard:

1. Export the dashboard definition (JSON/YAML/Terraform/etc.) from your platform.
2. Recreate it in the new backend using translated queries and equivalent panel types (time series, tables, single stats).
3. Preserve layout and names so on-call engineers don’t have to relearn muscle memory during incidents.

To avoid one-off work, define a few golden templates per service type (API, job, data pipeline) and parameterize them with labels/variables (services, env, region) for reuse.

**The outcome**: your most important dashboards and queries behave the same in the new backend, with minimal surprise for the people who rely on them.

### Step 5: Migrate alerts without losing coverage

Alerts are where risk lives – treat them carefully. Most platforms represent alerts as a query, an evaluation window, and notification targets.

#### Translate queries for behavioral parity

Reuse the work from Step 4. For each alert, translate the PromQL query (or equivalent) that describes the condition. Map thresholds and windows. If the old alert says “fire if > 80 for 5 minutes,” ensure the new rule expresses the same logic using range vectors or alerting windows.

At this stage, you’re aiming for behavioral parity, not redesign.

#### Keep routing simple initially

Map existing Slack/PagerDuty/email destinations to equivalent channels in the new backend. Mirror current behavior as closely as possible so teams can compare alerts one-to-one. Defer routing or escalation redesign until after dual-run is stable.

Start with the must-have alerts. Once those are stable and dual-running cleanly, you can decide which lower-priority alerts are worth migrating at all.

### Step 6: Dual-run and validate

At this point, in-scope services send the same telemetry to both backends, and your critical dashboards and alerts exist in the new system. Now you validate under real conditions.

Keep your current platform as the primary source of truth. Encourage on-call engineers to open new dashboards alongside the old ones. When an alert fires, check whether the corresponding alert in the new backend also fired, and compare the timelines and severity. This validation phase is critical. Evaluating an [observability](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/) vendor properly means confirming it works under real production conditions, not just test scenarios.

During this phase, you’re mainly checking for:

* **Gaps**: Alerts that fire in the old system but not in the new one
* **Extra noise**: Alerts that fire more often or with lower relevance in the new system
* **UX issues**: Panels that are hard to find or interpret under pressure

Capture issues in a shared doc or ticket queue so you can fix them systematically. Dual-run long enough to see a few real incidents, not just synthetic tests. Once those feel uneventful in the new backend and the owning teams have validated and signed off for that wave, you’re ready to move on.

### Step 7: Gradually shift to the new system

Once teams are comfortable, update runbooks and documentation so links and screenshots point to the new backend. Make the new UI the default view for on-call rotations, treating the legacy platform as a backup.

Next, turn down alerts in the old system:

1. Silence or downgrade informational alerts there first.
2. After several clean incidents, disable paging alerts so you’re not paged twice for the same issue.
3. Finally, reduce and then stop ingestion for fully migrated services.

Many teams keep the old backend in read-only mode for a defined historical window, then retire it once the data it contains is no longer needed. At that point, the new platform is your operational source of truth.

## Build your observability foundation with open standards

In this post, we walked through the core steps of migrating from one observability platform to the next — without a risky rip-and-replace. The approach is deliberately incremental: define what “success” means, prioritize only the dashboards and alerts that truly matter, map your telemetry flows, add the new backend as a parallel destination, translate what’s essential, dual-run to validate under real production conditions, and then shift traffic and ownership gradually.

At Chronosphere, we’ve also built internal tooling to help automate key parts of this process – so migrations are faster, more repeatable, and less disruptive for engineering teams. When you work with Chronosphere, you get a streamlined migration experience plus white-glove onboarding to help plan waves, validate parity, and confidently cut over.

Most importantly, Chronosphere is built to work with the open ecosystem you’re already using. We’re fully compatible with OpenTelemetry, Prometheus, and other open standards – so you can keep your existing instrumentation and pipelines while modernizing your backend on your terms.

**Get started:** [[Download the complete observability migration guide](https://chronosphere.io/resource/observability-platform-migration-5-step-practical-guide-to-upgrading-your-observability/)] | [[Schedule a 30-minute demo](https://chronosphere.io/demo-request/)] | [[Learn how to migrate observability tools](https://chronosphere.io/learn/migrating-observability-tools/)]

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/0f555e72-cropped-27bafa60-4944-4f0b-824a-d99b73a1e96c.jpg)

Katie Greenley is a Developer Audience Marketing Manager at Chronosphere, a Palo Alto Networks Company, with over a decade of experience building open source communities at scale. Having spent years at the Linux Foundation and CNCF shaping programs like KubeCon...

Read more from Katie Greenley](https://thenewstack.io/author/katie-greenley/)