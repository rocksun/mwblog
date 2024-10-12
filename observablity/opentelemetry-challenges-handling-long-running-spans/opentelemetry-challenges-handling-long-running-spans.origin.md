# OpenTelemetry Challenges: Handling Long-Running Spans
![Featued image for: OpenTelemetry Challenges: Handling Long-Running Spans](https://cdn.thenewstack.io/media/2024/10/8cc613c6-long-running-span-observability-challenge-1024x576.jpg)
OpenTelemetry (OTel) has taken the observability landscape by storm, and for good reason! At some point in the last decade, the software world quietly started viewing protocols as standards, evolving them in the open and embracing community-driven open source. Riding on this momentum, OTel quickly grew into the second-highest velocity project in the [CNCF](https://cncf.io/?utm_content=inline+mention) ecosystem. With a focus on vendor neutrality and language interoperability, allowing engineers to focus on understanding their systems instead of debugging their debuggers, OTel’s success feels almost obvious in hindsight.

That said, for all the energy around [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/), it’s not always a frictionless experience. There are some things that can be really [challenging](https://thenewstack.io/hard-truths-to-consider-when-designing-slos-for-mobile-apps) to address in OpenTelemetry’s mental models and assumptions. One of those huge hurdles to address in the real world is long-running [spans](https://thenewstack.io/spans-what-are-they-and-why-should-mobile-engineers-care).

## Long … Running? What?
Long-running spans! Well, OK, I’ll back up a little bit and explain a few things. The OTel landscape can be overwhelming at first since it has so many concepts to know before you get started. When people talk about OpenTelemetry, they’re usually talking about distributed tracing. While I’ll focus only on the relevant bits, here’s a [thorough overview](https://opentelemetry.io/docs/concepts/observability-primer/) if you’re interested.

When you debug a system, your first question is typically something like, “What action happened?” However, one action from the end user’s perspective translates to several from the system’s perspective. To reconcile that, OTel has the concept of a span, which is an action from the end user’s perspective. Inside that span, you have more spans that represent all the actions from the system’s perspective. We call the “span that represents the user viewpoint” [a trace](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app) … usually.

However, the relevant part of a span for us is the fact that it contains a few things: an ID, a trace ID, a start time and an end time. When you ship off your little bundle of joy into your observability backend, it comes with all four pieces of information (and the actual data, too). But that means that spans have a duration, which has some profound implications.

It also turns out that, in practice, a lot of tooling *really* doesn’t want the length of a span to be longer than … well, not very long.

Why does the tooling care about this? There are a few big reasons! A huge one is that the OTel API specification states something very important: All spans must be ended, and this is the responsibility of the implementer. Further, it states that if a developer forgets to end the span, the API implementation may do pretty much anything with it. The software development kit (SDK) specification provides built-in [span processors](https://opentelemetry.io/docs/specs/otel/trace/sdk/#span-processor), but those operate only on finalized spans.

In other words, the user perspective is a span, and any incomplete spans will probably be lost forever. If the incomplete span happens to be the root span, all of the inner spans that were sent will appear orphaned, if the backend can even handle them existing at all. Practically speaking, it means that root spans that are longer than about five seconds are likely going to cause issues.

Another reason why tooling cares about this is sampling. When you send buckets of data from one place to another, it’s reasonable to ask how you can represent that data better, and maybe avoid sending some of it. That’s where sampling comes in. The sampling service takes the telemetry and decides whether or not to send it to the backend or not (plus some fancy math adjustments that make it all work out). Neato! Except, there’s a small problem: How does it decide when something is relevant to send or not? Sampling decisions have to work on a complete span, and often operate on an entire trace’s worth of spans. That doesn’t work if you lose the root span!

So, awkwardly, not only are incomplete spans probably lost forever, and not only are the most likely spans to be lost often the most valuable ones, but all of your cost, network and compute optimizations break. Ouch.

## Have You Tried Not Having Long Spans?
A great solution to a problem is to fix it, but an amazing solution to a problem is to not have it! Can we … just not have long spans? It’s a noble thought, but it turns out that we’ll encounter this problem regardless of how long our spans are. We’ve been talking about long spans, but this is actually more about interrupted and incomplete spans.

The reason for that is that spans are basically the same as a database transaction in terms of their data model. So, whenever you run into a situation where you need to send transactions over the wire between multiple systems, you’ve encountered a scenario that experts like to call “being in for a real bad time.”

You could try a lot of solutions! Here’s a few that people have used:

- Refactor your code to represent actions in smaller chunks.
[Break a long action into intervals](https://www.honeycomb.io/blog/ask-miss-o11y-long-running-requests).[Make fewer traces and carry more data in the child spans](https://opentelemetry.io/docs/specs/otel/context/api-propagators/#global-propagators).- Manually end the root span early.
[Do unsound and sketchy transformations on your data to rewrite span IDs, trace IDs and links](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/7ec6396c393c7456ddd03ce060a94e4a2d5b55fb/processor/transformprocessor#warnings). (Repeat after me: “I solemnly swear to probably avoid this in production.”)[Unset the trace ID and utilize links instead](https://opentelemetry.io/docs/specs/otel/overview/#links-between-spans).[Ensure your trace context is correct and you’re not inventing a root span on accident](https://www.iankduncan.com/articles/2023-08-28-opentelemetry-gotchas-phantom-spans).
Unfortunately, none of those address the fundamental issue: When we said spans must be ended and we gave a duration, we made them transactions — and handling transactions across systems is *hard*.

To make matters worse, while you might think that interrupted spans don’t happen very often, it turns out that they happen quite frequently:

- In the backend: Whenever an application restarts mid request, or crashes, or the network fails, or …
- On the frontend: Whenever a web client navigates around, closes or refreshes a tab, cancels an action, or the browser event loop gets interrupted, or …
- In mobile: All of the above and much more!
However, fortune favors the creative. Now that we know we’re really dealing with a transaction semantics problem (that just happens to look like a “don’t have long-running spans” problem), we can look at all the existing literature on this. Surely someone’s solved this — or, uhh, at least tried?

## Creative Solutions to Chonky Spans
Putting our thinking caps and research glasses on, there’s a wealth of information surrounding databases, event streams and distributed transactions in general. However, there is a bit of a problem: Not much of that looks like OTel, and it’s hard to see how the solutions apply. But what if we stretched the definition of a span a little, and, given the constraints … cheated a tiny bit? Would that let us repurpose some solutions from other technology with similar constraints, maybe?

There are two frequently recurring themes in handling transactions: snapshots and write-ahead logs. In fact, [logs as a data abstraction](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying) are one of the fundamental building blocks of distributed systems. Logs as an append-only ordered data structure end up being the perfect thing to build snapshots on top of, and it turns out that the span processors in the OpenTelemetry SDK can be thought of as an in-memory write-ahead log. OK, you’ve got to squint a bit to think of it like that, but really, it is.

Awesome! Not only do we have an industry adopted pattern for handling transactions in the form of logs, but we already have most of the pieces required to build snapshots! Snapshots won’t solve all of our problems, but it’s a massive improvement, and it makes partial data usable — which is invaluable for debugging.

So, uh, how do we do that?

First, we’ve got to reframe the process: Instead of sending spans to our backend, we’re writing spans to a log and then replicating that to the backend consistently.

So, uh, how do we do that?

Good question! It turns out that [Embrace](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=long-running-spans) has implemented this solution and explained [why they did so](https://www.cncf.io/blog/2024/06/14/why-embrace-created-span-snapshots-for-mobile-observability-with-opentelemetry/). As for the *how*, while log replication has a huge range of possible solutions, a simple one requires only a few small changes to both the client and the server.

- First, the client has to send the snapshots of in-progress spans (this requires a custom span processor and exporter).
- Second, the backend needs to process and store these and wait for them to be finalized.
- Third, if those spans are never finalized, they still have to be massaged into an OTel-compliant shape gracefully and sent upstream. (OK, I lied. It’s not simple. We’re omitting a lot of details here.)
This seems like a lot of work, but Embrace’s SDK and backend does all of this for you, including handling the cases where interruptions occur and spans aren’t finalized. Even better, the spans are fully OTel-compliant when they’re done, which means there’s nothing stopping this solution from making its way into OpenTelemetry.

## Tracer.getInstance().endSpan()
Whew! We covered a lot of ground here. First, we talked about what long-running spans are, why we run into them, why they’re a problem and how you can’t avoid them no matter how hard you try. In fact, not only are you going to run into them, but any type of situation that involves incomplete or interrupted spans is subject to many of the same failure modes, which we identified as a transaction semantics problem.

Luckily, it turns out that transaction semantics are a well-studied problem, and we were able to go over a great solution and introduce a sketch of how that might work with OpenTelemetry.

If you’re coming from a traditional backend-focused approach to observability, you’d be surprised just how fundamentally different the mobile environment is. Embrace has a helpful on-demand webinar if you’d like to learn more: [What DevOps and SREs need to know about mobile observability](https://get.embrace.io/mobile-devops-sre/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=long-running-spans). There’s also a helpful guide: [Overcoming key challenges in mobile observability: A guide for modern DevOps and SRE teams](https://get.embrace.io/mobile-observability-guide?utm_source=the-new-stack&utm_medium=paid&utm_campaign=long-running-spans).

Long-running spans are hard, transactions are hard, but embracing creative problem-solving to find useful answers is what observability is all about.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)