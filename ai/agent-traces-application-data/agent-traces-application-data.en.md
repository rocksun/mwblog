Say a test starts failing and a developer hands it to a coding agent. It digs into the relevant files, runs the test suite, changes two files, then runs targeted validation. The task view shows the files it touched, the commands it ran, what results those commands returned, and the diff it landed on.

Before accepting the patch, the developer reviews that activity. A teammate might reopen the same run later to see why the code changed. The team building the agent can compare thousands of runs to see whether a model or prompt update improved test success or just added more tool calls and cost.

That record needs somewhere to live. Developers and reviewers want a durable version of the run whenever they need it. Engineering wants the same execution data aggregated across runs, because the agent’s behavior is nondeterministic and shifts over time.

> “For many agentic products, that record turns out to be application data with a telemetry-shaped workload.”

For many agentic products, that record turns out to be application data with a telemetry-shaped workload. That’s the combination that changes the storage decision.

## When a trace becomes product data

Not every agent trace counts as application data. An internal diagnostic trace that can be sampled, expired, or discarded is still telemetry. That boundary can exist within the same trace, where raw diagnostic fields remain internal and the fields needed to reconstruct the user’s task move into product state.

The boundary moves once your product has to retrieve, display, or retain a durable execution record. A developer, for example, might need to see which files an agent inspected, or a reviewer might need to check which commands ran and whether the tests passed.

This doesn’t require exposing a model’s private chain of thought. The product can instead render a projection of observable execution, showing model invocations, tool calls, file reads, command results, errors, timing, and state transitions. That record lets users verify the result and decide how much they want to trust it. In some workflows, it also becomes an audit record, which changes its access and retention requirements.

> “Internal diagnostic fields don’t automatically belong in the product view just because they came from the same run.”

Once that execution record becomes product state, it must follow your application’s access model. Code, prompts, retrieved documents, tool arguments, and command output may carry tenant or user data, so the application must enforce the same authorization boundaries when storing and retrieving them. Internal diagnostic fields don’t automatically belong in the product view just because they came from the same run.

## Why one agent run produces so much data

Pull request volume scales with the number of patches submitted for review, and issue volume scales with the number of development tasks. Both are just counting units of work at the workflow boundary.

Agent traces scale differently, depending on the execution graph within each task. One request to fix a failing test can trigger multiple model calls, file reads, searches, command executions, test retries, and branches before the agent ever proposes a patch. Each of those steps can produce its own span or event.

[OpenTelemetry GenAI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai), still in development, define separate span types for model inference, tool execution, and retrieval. What gets captured depends on the span type and content-capture policy. Inference spans may carry model identifiers, token usage, and opt-in input and output messages, while tool-execution spans may carry opt-in arguments and results.

The span count tracks what the agent actually does inside each unit of work. If you add a new tool, a retry policy, or a branch, the data volume can increase even though the number of completed tasks hasn’t changed.

> “If you add a new tool, a retry policy, or a branch, the data volume can increase even though the number of completed tasks hasn’t changed.”

This same fan-out also shows up outside coding agents. In a case study, Laminar reported [more than 500,000 browser events per day](https://clickhouse.com/blog/how-laminar-reimagined-observability-for-ai-browser-agents). A browser-agent session could run for more than 30 minutes and generate hundreds of thousands of DOM diff events. Laminar used those events to reconstruct a video-like replay of what the agent saw.

Whether the [agent writes code](https://thenewstack.io/ai-agents-software-engineering/) or navigates a browser, the same data serves two different purposes. One person loads one trace to understand a single run, and the engineering team scans many traces to find patterns. That combination of point retrieval and cohort analysis gives this data its unusual shape.

## Why agent trace data behaves like telemetry

Most records in an agent trace are written once rather than updated. A model invocation or tool result describes an event that has already happened. Scores, annotations, and run status may change later, but teams can store those mutable fields separately or record the changes as new events.

The records also carry high-cardinality dimensions such as model version, prompt template, tool name, session ID, user ID, and outcome. Their value only shows up in context. On its own, an isolated tool-call span doesn’t say much, but a full trajectory can explain a failed run, while a cohort can reveal a regression.

The same dataset therefore serves several distinct readers:

| **Consumer** | **Read pattern** | **Example** |
| --- | --- | --- |
| Product interface | Point lookup | Load one coding-agent run for a developer or reviewer |
| Evaluation pipeline | Cohort scan | Compare test success, latency, and cost across agent versions |
| Platform team | Time-window aggregation | Group errors and latency by model, tool or deployment |

A primary application database can serve all three patterns at modest scale, but that changes when wide scans and high-cardinality aggregations start competing with product reads and writes on the critical path.

## Outgrowing the primary database

There is no universal event-count threshold for moving traces out of the primary database. The decision shows up in the workload.

The first signal is contention, where ingestion or retention work starts consuming enough I/O and CPU to affect transactional operations. Next comes analytical friction, where evaluations and debugging queries need to scan long time ranges or join large trace tables, and stop meeting your team’s latency target. Eventually, teams resort to forced sampling, discarding traces to protect the application database, even though the product or an audit process requires the complete record.

Langfuse documented both contention and analytical friction as it scaled its open-source [platform for LLM observability](https://thenewstack.io/agentic-ai-observability-auditing/), evaluation, and prompt management. It experienced Postgres IOPS exhaustion during ingestion and prompt API latency reaching seven seconds under heavy load. Langfuse [moved its tracing data from Postgres to ClickHouse](https://langfuse.com/blog/2024-12-langfuse-v3-infrastructure-evolution), while keeping transactional and latency-sensitive paths isolated.

### The store is only half the decision

The database move solved one class of problem, but the original data model created another. Langfuse initially carried separate trace, observation, and score tables into its analytical architecture. Updates required deduplication and cross-table analysis, adding join cost.

> “The store is only half the decision. The analytical storage engine addressed the workload, and a data model reduced cross-table work.”

Later, Langfuse [collapsed those records into a wide, mostly immutable observations table](https://langfuse.com/blog/2026-03-10-simplify-langfuse-for-scale), with one row per model call, tool execution, or agent step. Initial table loads for large datasets went from seconds to milliseconds, and dashboard load times for large projects improved by at least 10 times over longer time ranges.

Langfuse needed both changes. The analytical storage engine addressed the workload, and a data model reduced cross-table work.

## How to choose a storage pattern

Start with the reads your product must support, then choose the simplest architecture that meets those requirements.

At modest volume, keeping traces in the primary database avoids another operational boundary. As analytical contention grows, the application can send trace events to a dedicated analytical store while keeping mutable business records in its transactional database.

Some applications need both systems to share data. A Postgres-backed product might keep users, permissions, and workflow state in Postgres while sending agent events to ClickHouse for analytical queries. If relevant application data [already lives in Postgres](https://thenewstack.io/why-ai-workloads-are-fueling-a-move-back-to-postgres/), change data capture can replicate it into the analytical path.

## Start with who reads the trace

Who depends on the record and how they query it matters more than whether a trace looks like a log or a pull request.

If your product needs to reconstruct a durable record of a single run and the engineering team needs to compare behavior across thousands of runs, the trace has become application data with a telemetry-like storage workload.

Map the point lookups and cross-run scans before choosing a store. If both are product requirements, design for both from the first trace you retain.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/07/e3f55e06-manveerprofile_20845237de.avif)

Manveer is co-founder of Zenith, previously Director of Engineering at Confluent and led Growth Engineering at Dropbox.

Read more from Manveer Chawla](https://thenewstack.io/author/manveer-chawla/)