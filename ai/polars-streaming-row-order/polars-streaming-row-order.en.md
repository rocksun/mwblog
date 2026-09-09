**Working with large datasets can lead to slow queries** and out-of-memory errors. Polars, an open-source library that developers and data analysts use to clean, combine, and analyze tables of data, promises to ease both problems in its upcoming 2.0 release. But the first release candidate, out last week, comes with a catch: The new default can change the order of returned rows, potentially affecting code that depends on that order.

In announcing the first release candidate for [Polars 2.0](https://pola.rs/posts/announcing-polars-2/), the company says that calling collect on any LazyFrame query will now default to the streaming engine. Per [Polars](https://pola.rs/), users can expect “massive memory and performance improvements on most queries,” with the streaming engine expected to be “easily 5x faster” in aggregate.

But they need to keep an eye out for changes in row order.

## Move fast — and maybe re-order things?

Improved memory usage and performance are obvious upgrades for Polars users who rely on the library for data processing and analysis, and it’s the streaming engine that’s bringing it.

> “Streaming engine doesn’t guarantee row-order by default for certain operations.”

With streaming, Polars [says](https://docs.pola.rs/user-guide/concepts/streaming/) it can execute lazy queries in batches, rather than processing all data at once. This way, users can process datasets that don’t fit into available memory.

But changing how those queries execute could potentially lead to trouble down the line, as the streaming engine can also change the order in which rows are returned.

As Polars explains, the “streaming engine doesn’t guarantee row-order by default for certain operations.” That includes operations such as join, group\_by, and unpivot.

In its [Version 2.0-rc user guide](https://docs.pola.rs/releases/upgrade/2/), the company explicitly calls out the migration hazard and underscores its risk in a red “danger” box, acknowledging that the change “may silently impact the results of your pipelines.”

For users whose code expects rows to appear in a certain order, that could create more problems for downstream processes.

## You can enforce row order, but there’s a chance it may cost you some speed

All is not lost, though. If users are working with code that depends on incidental ordering or observable row order, Polars offers guidance on mitigating the migration risk that comes with the new default.

> The change “may silently impact the results of your pipelines.”

There are two main options: Sort explicitly or set maintain\_order=True where applicable.

Alternatively, users can keep the in-memory engine as default by setting the engine affinity.

## What else is coming in Polars 2.0

Making all LazyFrame queries default to the streaming engine isn’t the only change users can expect from Polars 2.0. Per the announcement, the biggest changes in the upcoming release are improved defaults (the streaming engine being the most significant) and a better API.

In the pre-release post, Polars explains that 2.0 also removes many ambiguous casts.

For example, it directs users to use `.str.to_date()/.str.to_datetime()` to parse strings to temporal data types. This way, Polars says users get “one obvious way to parse data.” More examples of improvements to strictness are in the [migration guide](https://docs.pola.rs/releases/upgrade/2/).

Why the pre-release before the upcoming Polars 2.0? Because Polars says it “[doesn’t] gate new features” and prefers to ship them as soon as they’re ready.

That said, the company assured users there’s more to look forward to for 2.x, hinting at a new IO-plugin design, a faster S3 reader, a cost-based planner, join reordering, and big SQL coverage improvements, among others.

For developers exploring the release candidate now, the takeaway is clear: Better memory and performance are worth getting excited about, but don’t forget to watch that row order.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)