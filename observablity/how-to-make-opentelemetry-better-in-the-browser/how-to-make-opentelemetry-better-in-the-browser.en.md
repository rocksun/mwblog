*This is the second of two parts. Read Part 1:*

In Part 1, I covered some of the reasons why it’s difficult to use OpenTelemetry in the browser, including how the event loop-driven design of JavaScript is at odds with [OpenTelemetry’s model of spans and traces](https://thenewstack.io/opentelemetry-challenges-handling-long-running-spans/). I’ll pick up where I left off by sharing another approach to make [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) more ergonomic for [JavaScript](https://thenewstack.io/30-years-of-javascript-10-milestones-that-changed-the-web/). I’ll then cover some starry-eyed ideas for the future that I’d love to see happen, before wrapping up with some immediate improvements we can make today.

Now, as a reminder of where we left off last time, remember that traces, spans, span events and logs are all built on top of the same underlying primitive. That is, they’re all basically just events.

## Don’t Make Me Think

If we accept that OpenTelemetry is just events all the way down, then in theory, all you really have to do is write something like `trace.info()` and pass in an object. That’s it. You can have `trace.info`, `trace.error`, `trace.warn` and so on. Given the ubiquity of logging information, it shouldn’t be terribly surprising that most logging-like APIs are a quite natural interface for instrumentation. It [works perfectly for JavaScript and many other languages](https://thenewstack.io/javascript-framework-reality-check-whats-actually-working/), including those that don’t have the ability to provide metaprogramming-style abstractions, thread-local state or other facilities that make OpenTelemetry’s API more ergonomic.

> While addressing the OpenTelemetry API’s design might make instrumentation more ergonomic, improving that alone isn’t really sufficient for improved ergonomics.

While addressing the OpenTelemetry API’s design might make instrumentation more ergonomic, improving that alone isn’t really sufficient for improved ergonomics. It’s a huge improvement! But certain additional functions would be really helpful. It’s still challenging to design telemetry and propagate it in a way that’s maximally useful.

Taking inspiration from other types of instrumentation can give us some ideas of what might be useful here: What if there were a function to add metadata to the root span, regardless of where it is? Implementing this function would be tricky because span immutability is deeply central to the OpenTelemetry API, and violating that would break other things.

However, another way to approach that would be durable reference values to sets of attributes, which could then be mutable. That would also potentially massively cut down on network bandwidth.

Going further into the inspiration and ideas: What if there was a function to add a new span, but only if a parent span didn’t already exist, or otherwise attach things to the existing span? What if there were a function to take data and add it to every child span, maybe even recursively? What if there were a way to write instrumentation for a single function, but have that instrumentation remain useful when that function is called in a loop? And how could you write all of this without having to create custom processors or custom code to glue everything together in a way that makes sense for your use case?

## Imagining the Future

This brings up a fascinating design space for me: If I were to look far into the future and imagine what telemetry could look like, what might be possible?

Let’s take a step into this hypothetical future and imagine: What if the instrumentation library didn’t really exist in the traditional sense, and the code you were writing was actually going to be generated on the fly and rewritten by the compiler? You could use this to make instrumentation code very lightweight and minimal, essentially being custom-built for your application at compile time. You could use the compiler’s information to insert code structure automatically, add lifetime annotations, control flow information, call stack data and maybe even rewrite the telemetry to make more sense for your application’s needs.

This could facilitate very advanced instrumentation rewriting, minimization and compression as well; imagine a source map-style construct where you send binary pointers to certain common sets of data. You could even imagine normalizing or denormalizing telemetry automatically. Or enabling code to be written for both streaming and batch use cases without code changes. Collectors could roll and unroll telemetry for you, collapse certain pieces of data or even completely rewrite the telemetry tree as needed.

Browsers and language runtimes could also improve existing limitations by ensuring proper thread-local storage support, context propagation and support for context propagation inside async-like scopes.

> I’d love to see a world with extremely rich data for local debugging and the ability to naturally reduce that data for production deployment.

The ability to propagate information in a “magical” metadata object could also be a huge facilitator for building these types of structures, which could be thought of as similar to the reference of metadata idea I brought up earlier. If the language runtimes included explicit instrumentation support as well, then that instrumentation could be written in a heavily optimized manner, which would enable garbage-collected languages to benefit from low-to-zero overhead instrumentation. I find this exciting because it is an actual goal of the OpenTelemetry project, so the potential isn’t out of reach, but it’ll take a lot of coordination.

In addition, I’d love to see a world with extremely rich data for local debugging and the ability to naturally reduce that data for production deployment. Then you wouldn’t blow up everything with verbose debugging data when deploying to remote servers, but when debugging something locally, you could easily go all the way down to the system call level or even inspect the hardware to get extremely granular views of every interface, no matter how highly abstracted.

Just because a language is high-level doesn’t mean you shouldn’t be able to examine the details when you need or want to. I think we could build languages in the future that allow this ergonomically, letting you instrument code for production while getting rich instrumentation for development, without having to instrument the system twice. Luckily, much of what is described here is an explicit outcome of the upcoming [OpenTelemetry Profiling signal](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/profiles/0212-profiling-vision.md), so I hope to see a lot of progress in the next few years.

> Let’s step back and return to reality. The future is fun to think about, but what can we start with today?

If instrumentation were more tightly embedded into languages, then one could also imagine the uniform integration of other metadata, such as: debugging information, performance profiling, feature flags, marketing data, security events and experimentation data. Instead of each platform building its own SDKs and needing their own implementations, they could use instrumentation features built deeper into the language runtime itself. You could instrument once and feed that data into various platforms — from [observability and monitoring](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "observability and monitoring") to security and experimentation — all using the same code.

I like to imagine that future as being one where cross-functional collaboration is more accessible and where understanding the complex system being built becomes a truly company-wide endeavor. I’d love to see that happen.

## Getting to Better

All of that starry-eyed and sparkly future musing is great, but we might not realistically see those types of changes for years or even decades. It’d also require a lot of coordination, and it’s not clear whether the communities involved even want this to happen. So let’s step back and return to reality. The future is fun to think about, but what can we start with today?

Here’s my thinking: Since events already exist in OpenTelemetry, and since almost everything is events under the hood, we could build support for “just sending events” as an OpenTelemetry specification — think of it as an alternative representation of spans, traces, logs and span events. This would give us a ton of freedom to write whatever library SDKs are needed for a language while retaining full compatibility with vendors. We’re pretty close to being able to do this today, as all it would require would be a modified SDK implementation and a modified stateful OTel Collector. If those two things happened, vendor compatibility would stay the same, and we’d get to experiment with what an event-based representation could look like.

Some observability vendors are already adopting this telemetry flexibility mindset in their products, particularly those involved in the mobile space. One great example of that is [Embrace’s User Journeys](https://embrace.io/blog/user-journeys-walkthrough/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=ergonomic-js) functionality, where you can create custom user flows from existing telemetry you’re already collecting without having to restructure your code. If you’re interested in learning more, you can check out their [upcoming live webinar](https://get.embrace.io/user-journeys-webinar?utm_source=the-new-stack&utm_medium=paid&utm_campaign=ergonomic-js) on Sept. 16 at 10 a.m. PT/1 p.m. ET.

An event-based representation of telemetry data would also facilitate interoperating between traces, spans, logs and span events. It would also allow us to more easily migrate from logs to traces using the same code. This doesn’t mean that I think we’re going to get rid of the current SDK, however. It’s very useful for the backend and also represents a well-done “pay now” API where the client does some more work to handle the stateful nature of telemetry and, in exchange, the collector can be stateless. That means it’s very easy for vendors to be OpenTelemetry-compatible.

I can easily see a future in which people choose between the “pay now” model, where state complexity lives on the client, versus a “pay later” model, where state complexity is in the collector, depending on what makes sense for their environment. High-volume microservices likely benefit from a “pay now” model, and the frontend works best with a “pay later” model.

Putting the two together and being able to tie it all into a coherent context would unlock the next generation of understanding our systems. I can already see bits of this starting to happen, and it makes me really excited for the future of OpenTelemetry in the browser.

I’ve mentioned in other blog posts that the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) has a new dedicated Browser Special Interest Group (SIG) for it, which is actively working on improving browser support. I think that is going to create fascinating developments, and I truly look forward to seeing what it becomes one day. If you’d like to learn more about what the Browser SIG is working on, check out this [on-demand webinar](https://get.embrace.io/web-otel-panel-typ?utm_source=the-new-stack&utm_medium=paid&utm_campaign=ergonomic-js).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/10/58af1826-cropped-06daf154-screenshot-2024-10-02-at-10.13.52%E2%80%AFam.png)

Hazel Weakly spends her days building out teams of humans as well as the infrastructure, systems, automation and tooling to make life better for others. She’s worked at a variety of companies, across a wide range of tech and knows...

Read more from Hazel Weakly](https://thenewstack.io/author/hazel-weakly/)