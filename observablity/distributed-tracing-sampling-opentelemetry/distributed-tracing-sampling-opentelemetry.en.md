In modern observability, distributed tracing is often considered the most expressive signal. It can be used to capture much of what logs provide, while adding rich execution context. This shift would not be feasible in practice without OpenTelemetry, which enables span collection across an enormous variety of frameworks, libraries, and technologies.

Distributed tracing, however, can also be expensive. In an age of (sometimes gratuitously) distributed systems, even moderately sized environments can generate oceans of spans. While storing large amounts of data has generally become cheaper, our ability to query spans at a massive scale has not kept pace with our ability to produce them.

## Sampling to the rescue

If we cannot effectively query all the tracing data we collect, an intuitively correct way to tackle the problem is to reduce the size of that haystack. **Sampling**, that is the practice of selectively retaining only a portion of the tracing data generated, is as old as distributed tracing itself. It appears prominently in the original [Dapper](https://static.googleusercontent.com/media/research.google.com/en//archive/papers/dapper-2010-1.pdf) paper, from 2010, which is widely credited as the origin of the modern industry-standard approach that eventually led to OpenTelemetry. Earlier distributed-tracing papers such as [X-Trace](https://www.usenix.org/legacy/events/nsdi07/tech/fonseca.html) mention sampling as well.

Sampling approaches to distributed tracing generally fall into two categories:

* **Head sampling**, which decides upfront whether to create spans for a given request, typically when the request reaches the first traced component
* **Tail sampling**, which records tracing data for all requests but selectively stores only a subset

The two approaches come with very different trade-offs.

> “Sampling, that is the practice of selectively retaining only a portion of the tracing data generated, is as old as distributed tracing itself.”

Oh, by the way: when talking with people outside of the [observability](https://thenewstack.io/taking-your-observability-strategy-to-the-next-level/) circles, they tend to get surprised that the word “sampled” stands for “this span we keep”; instead, it is often assumed that sample is a synonym for filtering, rather than the opposite. I had the same confusion back when, and used the mental image of plucking juicy raspberries out of a platter to remind myself of the meaning.

## Head sampling

Head sampling is conceptually straightforward. When a new trace is about to start, you decide immediately whether you want to collect it.

### The theory of head sampling

Head sampling decisions can be based on request attributes, but in practice it is most often random, derived from the trace identifier using a deterministic rule such as a modulo operation.

Sampling randomly is commonly called **consistent probability sampling** or **deterministic sampling**. It assumes that, statistically, all traces are equally likely to be valuable. Or, at least, that with a sufficiently high sampling rate and amount of traces to samples from, important signals such as errors and latency spikes will still be sufficiently visible and statistically well represented.

In reality, especially at single-digit sampling rates, this assumption breaks down. Consistent probability sampling tends to miss or underestimate localized problems, where a small subset of requests behaves very differently from the rest.

### The practice of head sampling in OpenTelemetry

In OpenTelemetry, head sampling can be implemented in two main ways: the more flexible approach propagates the sampling decision through [trace context](https://www.dash0.com/knowledge/what-is-distributed-tracing), the same mechanism used to “glue” spans together in a trace. The simpler approach, limited to consistent probability sampling, can be done entirely in the observability pipeline.

#### Propagating sampling decisions through trace context

In OpenTelemetry, the sampling decision is made when a new root span is created. The SDK consults a configured sampler, most commonly [TraceIdRatioBased](https://opentelemetry.io/docs/specs/otel/trace/sdk/#traceidratiobased) for consistent probability sampling. The sampler inspects the trace ID and deterministically decides whether the trace should be sampled. The same trace ID will always produce the same decision, regardless of which service evaluates it.

That decision is encoded as a single bit, the sampled flag, in the trace flags and propagated downstream as part of the trace context. To make this concrete, consider the traceparent header defined by the [W3C Trace Context](https://www.w3.org/TR/trace-context/) specification, which standardizes trace propagation over HTTP:

**traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01**

```

             ^  ^                                ^                ^

       version  trace id                         span id          trace flags
```

The final byte encodes the sampling decision: 01 means “sampled” and 00 means “not sampled”.

When a downstream service receives a traceparent header with the **sampled** flag set, its SDK honors that decision and produces spans for the trace. When the flag is not set, spans are not exported at all.

Another widely used format is [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-tracingheader), which follows a similar model, encoding the sampling decision in the X-Amzn-Trace-Id header.

The result is that a single decision made at the head of the trace is applied consistently across all services, without requiring any centralized coordination.

For completeness, there are more refined [approaches](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.53.0/oteps/trace/0235-sampling-threshold-in-trace-state.md) that aim to make sampling *more reliably random* at the cost of a more complex implementation. From a technical perspective, these approaches are interesting, but in practice I find them mostly unnecessary.

#### Constant probabilistic sampling in the observability pipeline

Another way of randomly sampling traces is to always create spans via the [AlwaysOn](https://opentelemetry.io/docs/specs/otel/trace/sdk/#alwayson) sampler, but discard unsampled traces later in a cheap and distributed manner.

In this model, SDKs in applications always generate spans. OpenTelemetry Collectors near the applications then discard spans belonging to traces whose trace identifiers do not meet some deterministic criterion, such as falling outside a configured hash range. The OpenTelemetry Collector [probabilisticsampler](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/probabilisticsamplerprocessor) processor makes this easy:

```

processors:
  probabilistic_sampler:
    sampling_percentage: 10

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [probabilistic_sampler]
      exporters: [otlp]
```

Each Collector instance independently hashes the trace id and keeps only the spans belonging to traces that fall within the configured percentage. Because the decision is deterministic on the trace identifier, all Collector instances in the fleet agree on which traces to keep, without needing to communicate with one another.

This approach is appealing in its simplicity. It does waste some resources by creating spans that may later be dropped, but it is easy to deploy consistently across large fleets of Collectors, which are typically managed centrally by a platform team, and relies on the the fact that AlwaysOn is the default sampler in OpenTelemetry SDKs.

## Tail sampling

Tail sampling starts from a truth every observability practitioner knows: not all traces are equally valuable. The idea is simple in theory. Collect all spans for a trace, then decide whether the trace is worth keeping. When implemented well, tail sampling can be extremely effective. Unfortunately, it is also very difficult to implement well.

### Tail sampling criteria

Most tail sampling strategies I encounter resemble some variation of: “keep all traces with errors, and keep X percent of the rest as a baseline.”

The baseline matters. You need a statistically meaningful sample of normal behavior to understand how your system behaves under everyday conditions.

Focusing exclusively on sampling traces that contain errors is overly simplistic. A more useful mental model for tail sampling is grounded in how *interesting* a trace is. Not all errors are interesting. Think of the recurrent, benign, or recoverable errors amassing in your logs and traces.

Conversely, many interesting traces do not contain errors at all. Operations with high business impact or strong user visibility are worth observing, even when they succeed.

And, above all else and often overlooked, the *unusual* is particularly interesting. Rarely executed code paths are often valuable to trace, as are operations that produce unexpected outcomes, such as discovering that an API can return [HTTP status code 418](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/418).

### Tail sampling in OpenTelemetry

Regardless of the specific criteria, tail sampling at scale is **hard** for several reasons.

At its core, tail sampling requires a **time-deferred, centralized decision**. All spans belonging to a trace must be considered together. This runs counter to the design strengths of the OpenTelemetry Collector, which excels at live, stateless, streaming processing.

Bridging that gap requires more complex architectures in the observability pipelines:

![A common architecture to implement tail sampling with two layers of OpenTelemetry Collectors.](https://cdn.thenewstack.io/media/2026/03/796317fc-picture1.png)

*A common architecture to implement tail sampling with two layers of OpenTelemetry Collectors.*

The first tier is an **agent layer**, with one Collector instance per node (for example, on Kubernetes, as a DaemonSet or per pod as a sidecar), sitting close to the applications. OpenTelemetry SDKs use by default the **AlwaysOn** sampler, so every span is created and sent to the nearby agent. Logs and metrics are forwarded directly to the backend, as they are considered not to require tail sampling. (And as you can surely read between the lines, I have strong opinions on this matter, but I am keeping it for a future article, as this one is already massive enough as it is.) Traces are handled differently. Agents use the **loadbalancingexporter** to consistently hash the trace identifier and route all spans of a trace to the same Collector in the second tier.

The second tier is the **sampling layer**, a pool of Collector instances, running the **tailsamplingprocessor**. Because the **loadbalancingexporter** guarantees that all spans of a trace arrive at the same instance, that Collector can buffer them, evaluate the configured sampling policies (error status, latency thresholds, rate limits, and so on), and either forward the trace to the backend or drop it.

The architecture works, but it is operationally complex. The two tiers must be scaled and monitored independently. Consistent hashing must remain stable during scaling events. Using DNS as a system of record of which collectors exist in the second layer, and the resulting eventual consistency, is very hard to troubleshoot. (Because, you know, it’s always DNS.)

There are deeper challenges as well.

From the perspective of individual spans, there is *no indication* that a trace is complete. Distributed tracing has nothing comparable to an EOF marker in file systems. Once a sampling decision is made, it must be remembered so that late-arriving spans are handled consistently. It is common to hear statements like, “our traces are fast, they finish in under a minute.” The slow traces in such systems are often *very interesting* and almost every environment contains [long-running batch jobs](https://thenewstack.io/pgq-queuing-for-long-running-jobs-in-go-written-atop-postgres/) that perform business-critical work such as reconciliation or billing.

The sampling layer is inherently stateful, buffering spans while waiting for enough data to arrive to make a decision. Ideally, tail sampling would allow decisions to be deferred for a *significant time*. Doing so requires storing spans durably enough to survive that delay, while still being able to delete them efficiently if the trace is ultimately dropped. Today, the OpenTelemetry Collector stores pending spans in memory, which leads to difficult sizing problems. There are community [proposals](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42326) to offload this buffering to disk, but I am not aware of a production-ready solution from the community.

Tail sampling, implemented as shown above, also conflicts with how resilient distributed systems are designed. Services are spread across availability zones or regions to avoid correlated failures. Spans are therefore scattered across those zones. Tail sampling requires all spans of a trace to converge in one place, which means routing data across zones to a specific Collector instance, which undermines architectural principles designed to avoid central choke points. The observability pipeline ends up concentrating traffic in ways the application architecture was explicitly built to avoid.

Last but not least: networking costs. The routing of spans to the “right Collector” can incur significant cloud networking costs due to cross-availability-zone network traffic. In my experience, once teams start looking into the networking costs of their observability pipelines, the results are often eye-watering.

## Sampling alone does not give observability

There is a fundamental limitation of sampling that is easy to miss: **you cannot compute accurate metrics from sampled traces.**

RED metrics — request rate, error rate, and duration distributions — are foundational to observability. They power dashboards, SLOs, and alerts. Their value, however, depends on precision, which puts them in tension with sampling.

Imagine calculating RED metrics using consistent probability sampling at 10 percent, and multiplying the result by 10. Request and error counts can be off by as much as 90 percent, and duration histograms are likely to be dramatically underestimated, since the slowest requests have a comparatively high probability of not being recorded.

> There is a fundamental limitation of sampling that is easy to miss: you cannot compute accurate metrics from sampled traces.

With tail sampling that retains only errors, slow requests, and a small fraction of normal traces, the bias shifts in the opposite direction. Errors become overrepresented, and duration histograms are heavily skewed toward the unhappy path. (Some observability vendors compensate for this by annotating “multiplicity” on spans during the sampling process, which does curtail the error margin, but this article focuses on the approaches available in OpenTelemetry.)

In neither case can accurate RED metrics be reconstructed by querying only the spans that survive sampling. As a result, any architecture that samples traces must **materialize metrics before sampling discards data**.

This is why, in the two-tier architecture described earlier, the sampling layer runs a connector such as **spanmetricsconnector** or the newer **signaltometricsconnector** before the **tailsamplingprocessor**. The connector sees every span and produces accurate counts and histograms. Only afterward does sampling occur.

The metric generation itself is not trivial. OpenTelemetry metrics have a concept of [temporality](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#temporality). Metrics can be **cumulative**, representing totals since process start, which is how we usually conceptualize metrics or **delta**, representing changes since the last reporting interval. The two are not interchangeable, and different backends have diametrically opposed preferences. If metrics are emitted in the wrong temporality, stateful processors such as **deltatocumulative** or **cumulativetodelta** are required, adding memory overhead, routing and cognitive complexity, and statefulness.

At this point, it is natural to ask “if creating RED metrics in the pipeline is so hard, why not generate the metrics we need in the traced applications?”. “Could the SDKs not emit accurate RED metrics directly?”

In principle, they can. The OpenTelemetry specification defines semantic conventions for [HTTP metrics](https://opentelemetry.io/docs/specs/semconv/http/http-metrics/), [gRPC metrics](https://opentelemetry.io/docs/specs/semconv/rpc/grpc/), and others. These metrics are carefully specified to avoid high-cardinality problems, which happens when metrics carry attributes such as full URLs, user identifiers, or full query strings, which can have a lot of different values and makes the metric series explode combinatorially.

I really like OpenTelemetry semantic conventions, and the ones about metrics are among my favorites. But it is not a list of metrics that covers all scenarios. For example, I know of no semantic convention for “headless” operations, like when you [schedule a job to run regularly](https://thenewstack.io/linux-how-to-use-cron-to-schedule-jobs/).

In practice, SDK support for these metrics is uneven, especially across the wide range of auto-instrumentation libraries. As a result, in many real-world deployments, the observability pipeline, not the SDK, is where RED metrics are actually produced.

And even when SDKs emit metrics, the problem is not solved. With each collector potentially creating metric data points for each service, you need aggregation for metrics further down in the pipeline to curb metric cardinality, which sometimes results in a third layer of OpenTelemetry Collectors, further (albeit smaller, compared to the one for spans) cross-availability-zone network traffic, and yet more complexity.

## Conclusion

Observability is not simple. We generate enormous volumes of data, and turning that data into something useful and cost-effective requires careful engineering.

Sampling is an unavoidable necessity in the practice of observing large distributed systems. While the idea is simple, the reality is complex. This complexity ripples outward, especially in how RED metrics are produced and preserved.

The good news is that progress continues. Proposals for disk-based buffering for the **tailsamplingprocessor** aim to reduce the operational pain of tail sampling. Newer connectors like **signaltometricsconnector** make it more practical to generate accurate metrics even in heavily sampled pipelines.

Alas, there is no single silver bullet. The path forward is a blend of better tooling, smarter defaults, and a clear-eyed understanding that sampling is a set of trade-offs, not a problem that can be solved once and be then forgotten. There are also interesting ideas out there like the “[exemplar based tail sampling on storage](https://www.youtube.com/watch?v=qq8hTct8zm4)” that, while a mouthful, is based on a simple intuition: keep all data “hot” for a short period of time, and sample later, which can be implemented relatively easily with OpenTelemetry Collectors duplicating incoming data to a short-lived, full-precision stream, and a sampled one using the other techniques explained in this article.

The philosopher’s stone remains elusive, but the alchemy is continuously improving.

*This guest column is being published ahead of [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/), the Cloud Native Computing Foundation’s flagship conference, which will bring together adopters and technologists from leading open-source and cloud-native communities in Amsterdam, the Netherlands, from March 23-26, 2026.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/03/08ff8f2a-michelemancioppi.jpeg)

Michele is a man of simple tastes: he likes software boring and observability powerful and easy. Chief Architect and Head of Open Source and Community at Dash0. Engineer by day, Product by night. Unrepenting observability nerd.

Read more from Michele Mancioppi](https://thenewstack.io/author/michele-mancioppi/)