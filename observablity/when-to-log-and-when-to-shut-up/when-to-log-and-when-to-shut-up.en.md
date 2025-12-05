Let’s be honest: Most logs are just noise.

|  |
| --- |
| [INFO] Starting process … probably.  [DEBUG] Made it to line 42 — still alive.  [TRACE] Function entered. Leaving soon.  [INFO] User clicked a button. Which one? No idea.  [WARN] Everything’s fine, just felt like warning you.  [DEBUG] Variable x = 7. Might change. Might not.  [INFO] Operation completed successfully (we think).  [TRACE] Loop iteration #12 of infinite sadness.  [DEBUG] Placeholder for meaningful message.  [INFO] Shutting down gracefully … except when not. |

As developers, we too often sprinkle logs like confetti — every function entry, every variable, every heartbeat. Before long, terabytes of meaningless lines pile up, filling dashboards no one reads.

We pay millions of dollars to observability vendors just to warehouse our junk. Every useless log line burns compute, disk and dollars. [Logging](https://thenewstack.io/how-to-evaluate-logging-frameworks-10-questions/) without intent isn’t [observability](https://thenewstack.io/introduction-to-observability/), it’s littering.

Even with modern observability platforms that [dramatically increase compression through columnar storage](https://clickhouse.com/blog/log-compression-170x), there’s no reason to log everything. It still turns root cause analysis into a needle-in-a-haystack problem, diluting the signal you actually need — and you’ll pay more for the privilege.

We need to be selective. Log what helps us understand the system, debug real issues or explain business impact — and shut everything else up.

## The Philosophy of a Log Line

Every log line is a choice, not a reflex. If it’s not helping your future self track down a bug at 3 a.m., delete it. Logging isn’t journaling; keep it minimal, clear and actually useful.

Before you hit `logger.info`, stop, and ask: Would I actually grep this?

If not, delete it. Logs aren’t narration; they’re evidence. They exist to tell you what the system was thinking when things went wrong.

Logs shouldn’t be relegated to the end of the observability chain. They’re not just a microscope for confirmation but a map for discovery. Sometimes the quickest way to insight is to explore raw text \_ grep, filter and follow intuition.

Logs invite curiosity — they reveal nuance that metrics might smooth over and context that traces can’t express. Treat them not as the final resort but as a living source of truth, open to exploration from the very start.

## Context or It Didn’t Happen

“Error occurred” without inputs, IDs or state means nothing. Add enough context to reconstruct the moment — request IDs, user IDs, input parameters, operation names. These days, with OpenTelemetry, you get trace and span IDs for free. Use them. Logs connected to traces (and even metrics) by trace IDs are infinitely more valuable than isolated lines of text.

Logs aren’t a standalone pillar; they’re the closing chapter of your root cause analysis. You alert on metrics, investigate through traces and then drop into logs to see what actually happened. When your logs are linked by trace and span IDs, they stop being noise and start being evidence — tightly scoped, contextual and directly tied to the path of a single request. That’s observability with intent, not a wall of text.

## Well-Structured, Not Free Text

Free-text logging is obsolete. Structured logs, whether JSON, CSV or key-value, aren’t just easier to query; they’re the foundation for analytics. Once logs have structure, patterns emerge:

* “This error started spiking last week.”
* “This happens mostly after event X.”
* “This warning correlates with this specific deployment.”

The future of logging isn’t reading one line; it’s seeing the pattern across thousands.

[![Structured logging makes charting easy and efficient](https://cdn.thenewstack.io/media/2025/12/057dadf0-image1.png)](https://cdn.thenewstack.io/media/2025/12/057dadf0-image1.png)

Structured logging makes charting easy and efficient.

While many observability platforms offer schema on read, that flexibility comes at a cost. Every query forces the system to scan and parse raw text, line by line, to infer a structure that should have existed in the first place. These queries are computationally expensive, slower and more difficult for a user to write.

Prestructured logs flip that inefficiency on its head. When your data already has shape, you can take advantage of [column-oriented storage and native aggregation](https://clickhouse.com/blog/breaking-free-from-rising-observability-costs-with-open-cost-efficient-architectures) — querying, visualizing and correlating events in milliseconds instead of minutes.

## Know When To Measure, Not Just When To Log

Not every [event belongs in the log stream](https://thenewstack.io/understanding-log-events-why-context-is-key/). Some things deserve structure and timing — exactly what spans and metrics are for. If you’re measuring latency, user flow or distributed causality, emit a span instead. Spans capture duration, context and relationships across services and tell you why something was slow or broken, where a log can only shout that it happened.

The same logic applies to metrics, turning repetitive logs into real signals you can alert on and aggregate efficiently. If you find yourself logging the same message hundreds of times per second, you’re not observing, you’re just wasting storage. Measure it once, summarize it, and let your metrics and traces do the heavy lifting.

## Log Levels Are For Humans, Not Machines

Logging isn’t a personal debugging diary; it’s a shared artifact for your future teammates. Every line should help someone understand what happened without guessing what you meant. Write logs for the next incident, not your current mood. Your logs tell the story of your system. Make it one worth reading, for example:

* **ERROR:** Page a human. Something’s broken.
* **WARN:** Unexpected but survivable. Investigate later.
* **INFO:** Routine system behavior worth knowing.
* **DEBUG/TRACE:** Temporary developer insight — should rarely leave your laptop.

Be deliberate. Don’t mark something as an error unless it truly requires action. Overusing ERROR numbs your alerts and trains teams to ignore what matters. Every log level should communicate intent: what needs fixing now, what needs watching and what can be ignored.

That said, trace logging has its place. For example, behind the scenes for ClickHouse Cloud, we [trace-log extensively to help our engineers diagnose performance issues](https://clickhouse.com/blog/scaling-observability-beyond-100pb-wide-events-replacing-otel) and support customers at scale. It’s a deliberate exception — necessary when you operate a distributed database serving thousands of workloads in real time. For most applications, though, this level of verbosity isn’t observability; it’s just noise.

## Tools To Help You Log Less and Log Smarter

Rich SDKs and powerful filters exist so you don’t have to just “log everything.” Use them.

Modern [OpenTelemetry Collector SDKs](https://opentelemetry.io/docs/specs/otel/logs/sdk/?utm_source=chatgpt.com) let you be prescriptive about what you log: You can instrument your code so that only meaningful log lines are created, and you can filter or drop everything else at ingest or collection time.

For example:

If administrators spot users generating frivolous logs, they can aggressively filter them, either in the pipeline or by forcing minimal logging policies. If you’re using a proprietary platform, these provide similar filtering or ingestion-control tools, even if they don’t shout about them publicly.

## Log With Purpose, or Don’t Log at All

Observability isn’t about volume. It’s about clarity. Every log line should earn its place by explaining something that metrics and traces can’t. Logging without intent just burns money and buries insight.

Be deliberate. Use structure. Add context. Know when to measure, when to trace and when to say nothing. Modern tools make it easier than ever to be disciplined, but the discipline still has to come from you.

In the end, great logging isn’t about capturing everything that happens. It’s about capturing what matters.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/4daa8bcf-cropped-b8ab0704-mikeshiheadshot.jpeg)

Mike Shi leads observability at ClickHouse, is the co-founder of HyperDX and co-creator of ClickStack. Mike remains a hands-on developer, contributor to the open source OpenTelemetry and ClickStack projects, and speaks regularly at observability-focused events. He believes that while observability...](https://thenewstack.io/author/mike-shi/)