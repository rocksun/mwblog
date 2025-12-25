When people hear “software migration” or “migrating away from proprietary agents” they picture months of copying dashboards, rewriting alerts, redeploying agents and risky cutovers where something critical gets missed.

The reality? With the availability of various open source tools, migrations can take weeks, not months or years. Open source can help you laterally shift and transition. This would allow you to transition to an open-standards-compatible, vendor-managed [observability](https://thenewstack.io/introduction-to-observability/) platform without changing your application-level instrumentation and with manageable query changes, while preserving data portability.

## **Most Organizations Are Already Halfway There**

Many organizations either have, or are moving toward, an architecture like this:

Your collection layer is already open and portable. Only the backend is proprietary.

## **Migrating From a Vendor-Managed Architecture**

You’re operating in an “OSS-first, vendor-managed” architecture, which means you don’t need to re-instrument; you need to re-home.

1. **Redirect your data pipelines** to a new backend (staging first, then production).
2. **Convert** [**queries, dashboards and alerts**](https://chronosphere.io/learn/converting-datadog-queries-dashboards-and-alerts-to-open-source-standards/) that teams actually rely on.
3. **Dual-run both systems** until you trust the new one, then dial back the old backend.

This isn’t about reinventing your instrumentation; it’s about changing where your telemetry lands and how it’s queried. Teams completing this shift report better control and lower costs. For example, [Chronosphere customers report](https://www.prnewswire.com/news-releases/chronosphere-launches-new-framework-and-features-to-tackle-growing-observability-costs-301862762.html)[reducing low-value data volumes by 60%-80%](https://www.prnewswire.com/news-releases/chronosphere-launches-new-framework-and-features-to-tackle-growing-observability-costs-301862762.html) while maintaining or improving visibility through improved aggregation and retention controls.

Here are practical steps for executing that lateral shift safely and incrementally so migration feels like the next step, not a leap.

## **How to Migrate From a Proprietary Observability Platform**

This guide walks through migrating to an open source standard compatible platform without disrupting operations.

### **Planning: Define What ‘Success’ Means**

Before starting the migration, clarify your goals:

* Are you primarily trying to reduce cost?
* Do you want better control over data retention and aggregation?
* Are you trying to standardize on PromQL and open APIs across teams?

Document three things:

1. Which services are in scope for the first migration wave (ideally lower-impact services first)?
2. Which teams own those services and will be responsible for validation and sign-off?
3. Which dashboards and alerts are non-negotiable for day-to-day operations; everything else is secondary.

This documentation becomes your north star when prioritizing work across teams.

## **Migration Steps**

### **Step 1: Prioritize What Actually Matters**

Before you inventory everything, identify what you actually need to migrate:

**Create a Focused List:**

* Ten to 20 dashboards that on-call engineers actually use during incidents, site reliability engineers (SREs) reference for service-level objective (SLO) reviews or leadership relies on in weekly meetings.
* Twenty to 50 alerts that page someone at night, appear in runbooks or protect revenue-critical services.

Treat these as phase-one migration artifacts. Everything else can wait.

For each dashboard and alert, document:

* Where it lives in your current platform (URL, folder, owner).
* Which teams own and rely on it.
* Any known quirks (“this alert is noisy,” “we ignore that panel”) so the right people can validate and sign off during migration.

Understanding which data actually drives decisions is critical. Teams often discover they’re paying to store massive amounts of telemetry that nobody uses.

### **Step 2: Inventory Your Telemetry**

You can’t move what you haven’t mapped. For the in-scope services, document where telemetry originates and how it flows.

* **Metrics**: Do they come from Prometheus scraping, exporters (node, Kubernetes, database, cloud) or custom metrics via Prometheus client libraries? How do they reach your current platform (native remote-write, sidecar collector or vendor-specific gateway)?
* **Traces**: Are services instrumented with OpenTelemetry SDKs or auto-instrumentation? Do traces go through an [OpenTelemetry Collector or a vendor agent](https://thenewstack.io/telemetry-pipelines-collectors-and-agents-whats-the-difference/)?
* **Logs**: How are logs shipped — central log pipeline or multiple sidecars?

### **Step 3: Add the New Backend as a Second Destination**

Instead of ripping out your current platform, introduce the new backend as a shadow destination for a subset of services. Start by deploying this configuration in staging to validate behavior, then promote it to production once it looks good.

The less you change at once, the easier it is to validate behavior.

**Metrics**

If you’re using Prometheus remote-write, add a second remote-write endpoint pointing to the new backend (or re-point non-critical services first). If you’re using Prometheus servers for scraping, either reconfigure them to write the new backend or mirror scraped data using remote-write or federation.

If your new platform is Prometheus-compatible, this is mostly wiring; you’re redirecting existing traffic to a different endpoint, not rebuilding your pipeline.

**Traces**

With the OpenTelemetry Collector, add an additional exporter pipeline that sends traces to the new backend in parallel (OpenTelemetry Protocol → new backend). Keep configs as similar as possible to your existing trace pipeline for direct comparison during the dual-run..

Platforms that speak OpenTelemetry Protocol (OTLP) natively make this simple; you reuse the same OpenTelemetry exporters and processors you already trust.

**Logs**

If using Fluent Bit, add another output that sends logs to the new backend’s ingestion endpoint. If you already have a centralized log pipeline or router, fan out from there rather than touching every application pod.

Some managed platforms provide a central “telemetry pipeline” service built on OSS components, letting you manage routing in one place instead of editing dozens of daemonset configs.

**Watch the Cost of Dual-Run**

Running an old and new systems in parallel will temporarily increase telemetry volume and cost. Remote-write fan-out and duplicating traces/logs means sending the same data to multiple destinations. If you scope this phase to a limited set of services, you can validate behavior without creating a large cost spike.

At this point, the new backend receives the same metrics, traces, and logs as your current platform but no dashboards or alerts have moved yet. You’re only duplicating data flow.

### **Step 4: Convert Queries and Dashboards**

**Focus on Core Queries First**

Most proprietary platforms either use a PromQL-like language or run their own DSL on Prometheus-style series and labels. Your new backend should offer a PromQL compatibility or a clear mapping.

Start with the 80% use cases:

* **Simple time series:** single metrics with filters like `{env="prod", service="api"`}
* **Basic aggregations:** `sum`, `avg`, `max`, `histogram_quantile`
* **Tag → label mapping:** `env:prod` → `{env="prod"}`

Only after that’s solid, tackle:

* Cross-metric arithmetic
* Joins and multiseries expressions
* Vendor-specific or “magic” functions

If your new platform offers a query converter, PromQL compatibility layer or DSL translation tools, use them for edge cases instead of hand-porting everything.

**Rebuild Only Critical Dashboards**

Use the priority list from Step 3 as scope.

For each dashboard:

1. Export the dashboard definition (JSON/YAML/Terraform/etc.) from your platform.
2. Recreate it in the new backend using translated queries and equivalent panels types (times series, tables, single stats).
3. Preserve layout and names so on-call engineers don’t have to relearn muscle memory during incidents.

To avoid one-off work, define a few golden templates per service type (API, job, data pipeline) and parameterize them with labels/variables (services, env, region) for reuse.

**The outcome:** your most important dashboards and queries behave the same in the new backend, with minimal surprise for the people who rely on them.

### **Step 5: Migrate Alerts Without Losing Coverage**

Alerts are where risk lives — treat them carefully. Most platforms represent alerts as a query, an evaluation window and notification targets.

**Translate Queries For Behavioral Parity**

Reuse the work from Step 4. For each alert, translate the PromQL query (or equivalent) that describes the condition. Map thresholds and windows. If the old alert says “fire if > 80 for 5 minutes,” ensure the new rule expresses the same logic using range vectors or alerting windows.

At this stage, you’re aiming for behavioral parity, not redesign.

**Keep Routing Simple Initially**

Map existing Slack/PagerDuty/email destinations to equivalent channels in the new backend. Mirror current behavior as closely as possible so teams can compare alerts one to one. Defer routing or escalation redesign until after dual-run is stable.

Start with the must-have alerts. Once those are stable and dual-running cleanly, you can decide which lower-priority alerts are worth migrating at all.

### **Step 6: Dual-Run and Validate**

At this point, in-scope services send the same telemetry to both backends, and your critical dashboards and alerts exist in the new system. Now you validate under real conditions.

Keep your current platform as the primary source of truth. Encourage on-call engineers to open new dashboards alongside the old ones. When an alert fires, check whether the corresponding alert in the new backend fired too, and compare timelines and severity. This validation phase is critical. Evaluating an observability vendor properly means confirming it works under real production conditions, not just test scenarios.

During this phase, you’re mainly checking for:

* **Gaps:** Alerts that fire in the old system but not in the new one.
* **Extra noise:** Alerts that fire more often or with lower relevance in the new system.
* **UX issues:** Panels that are hard to find or interpret under pressure.

Capture issues in a shared doc or ticket queue so you can fix them systematically. Dual-run long enough to see a few real incidents, not just synthetic tests. Once those feel uneventful in the new backend and the owning teams have validated and signed off for that wave, you’re ready to move on.

### **Step 7: Gradually Shift to the New System**

Once teams are comfortable, update runbooks and documentation so links and screenshots point to the new backend. Make the new UI the default view for on-call rotations, treating the legacy platform as a backup.

Next, turn down alerts in the old system:

1. Silence or downgrade informational alerts there first.
2. After several clean incidents, disable paging alerts so you’re not paged twice for the same issue.
3. Finally, reduce and then stop ingestion for fully migrated services.

Many teams keep the old backend in read-only mode for a defined historical window, then retire it once that data is no longer needed. At that point, the new platform is your operational source of truth.

## **Migrations Should Be Boring**

The real win of this lateral shift isn’t just cost reduction or nicer dashboards — it’s owning your observability semantics. Your metrics are in Prometheus-style formats. Your traces and logs speak OpenTelemetry. Your dashboards are based on open or well-documented schemas. Your alerts are expressed in a query language and rule model that isn’t tied to one company’s UI.

**What this means:** If you ever need to change vendors again, you’re not starting from zero. If you want to run part of your stack self-hosted and part managed, you can. If your platform team wants to build internal tooling on top of your observability data, they can rely on stable, open interfaces.

Research from Mordor Intelligence shows that the [average enterprise juggles five or more monitoring tools](https://www.mordorintelligence.com/industry-reports/observability-market), with proprietary query languages restricting migration even when telemetry formats are open. This is a major reason many organizations see OpenTelemetry as a strong [enabler of vendor‑agnostic growth](https://www.mordorintelligence.com/industry-reports/observability-market).

In other words, this migration should be the last painful one. After this, observability changes become iterative. It’s about configuration, not reinvention.

## **Make This Your Final Migration (and Your Best One Yet)**

If your telemetry is already built on open standards, you’ve already done the heavy lifting. What lies ahead is a controlled, incremental transition that sets you up for long-term success — not a risky overhaul. Taking this step now means trading lock-in and rising costs for an observability foundation that grows and evolves exactly the way you need it to, on your own terms

**Get started:**

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/12/84ca0924-cropped-c61bc173-marjoriefreeman-scaled-1-600x600.jpeg)

Marjorie Freeman is a senior content marketing strategist who helps technical teams turn complex ideas into clear, impactful messages. She specializes in enhancing editorial operations and building scalable, cross-functional content programs. Her current focus is on answer engine optimization (AEO)...

Read more from Marjorie Freeman](https://thenewstack.io/author/marjorie-freeman/)