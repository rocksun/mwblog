*This is the first of two parts.*

OpenTelemetry has been, in my opinion, one of the most engaging developments in the software community over the past few years. It’s proven incredibly valuable for instrumenting distributed systems, microservices and complex architectures. Because of it, teams are able to understand their systems with increasing efficacy and share that understanding across the organization.

With its rapid adoption, [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) is becoming increasingly prevalent on the frontend as well. However, we run into a problem: It feels awkward to use, [particularly in the browser](https://thenewstack.io/setting-up-opentelemetry-on-the-frontend-because-i-hate-myself/).

This isn’t necessarily anyone’s fault. It’s a natural consequence of having so many different languages using a single API; something is bound to feel off. The OpenTelemetry spec *does* state that [APIs should feel idiomatic to a language](https://opentelemetry.io/docs/specs/otel/specification-principles/#be-general), but the design awkwardness persists. I’m not sure why, but I suppose that when you put the needs of every community together along with the common denominator of language functionality, you inevitably end up with something that doesn’t feel quite natural in any given language.

That said, there’s a tremendous opportunity to build on top of this foundation and provide something that frontend developers would find more ergonomic. Several languages have already done similar work: Ruby, [Go](https://thenewstack.io/opentelemetry-for-go-is-almost-a-go/) and [Java](https://thenewstack.io/getting-started-with-opentelemetry-for-java/) have fairly ergonomic OpenTelemetry integrations, for example.

These ergonomic implementations share common factors: Language-specific functionality is used to create conveniences on top of the common API, and common control flow patterns fit naturally into the state machine that OpenTelemetry expects.

Sometimes, the language doesn’t have particularly common control flow patterns (like Haskell or Ruby), but both languages have the flexibility to shape control flow in ways that allow the instrumentation libraries to remain ergonomic despite that potential friction.

> We would benefit massively from disaggregating context management, data instrumentation and control flow in our systems.

In fact, I’m going to state a bold claim: The heart of OpenTelemetry is context management, which is a concept that is intentionally separated from the rest of the spec *specifically* so that context can be implemented in the most sensible way for the runtime environment. Despite the intent, we don’t seem to achieve the benefits of that separation of concerns in reality.

If we are to get those benefits and unlock truly ergonomic telemetry instrumentation, developing the ability to separate the control flow that OpenTelemetry expects from the control flow that makes sense in your program is essential. If there’s one thing I’d love for people to take away from this article, it’s that we would benefit massively from disaggregating context management, data instrumentation and control flow in our systems.

There’s a trade-off here, and it can be tricky to navigate. If you take the state machine of OpenTelemetry’s desired control flow and push it into the libraries themselves, they can become extremely cumbersome to use. On the other hand, if you rely on propagating that control flow implicitly, you’ll run into problems when OpenTelemetry’s required control flow differs from your program’s natural control flow.

## API Friction in OpenTelemetry

When control flow is tied to the way you annotate and instrument your code, you have to change code structure to match what OpenTelemetry expects. For JavaScript, that’s simply not something it does well, particularly on the frontend.

JavaScript also has the unique constraint of needing to provide the “same” language in the browser as well as in Node.js. On the frontend, you have an event-driven browser runtime that’s designed to do heavy lifting for you. Because of that, it’s fairly limited in terms of asynchronous code, threading context and managing low-level details. After all, the browser is supposed to handle all of that, and the browser APIs were originally designed in a world where frontend code was very simple.

Now that we have complex code on the frontend, you can run into mismatches between what you’d like to do and what the browser makes easy. On the backend, you have Node.js, which quickly deviated from the browser in order to add certain APIs that were necessary for running on an operating system, such as process handling and thread context; these deviations happen to make instrumentation significantly easier, but have no complement in the frontend (yet).

> If we step back and think about what we can do without changing the language, I like to frame it around two concepts: ‘annotation without structure’ and ‘don’t make me think.’

Even though Node.js might have better facilities for enabling ergonomic OpenTelemetry implementations, JavaScript is still deeply event loop-driven by design. OpenTelemetry’s model of Spans and Traces really doesn’t fit well with that pattern. As a consequence, it’s difficult to set up OpenTelemetry effectively in JavaScript.

The biggest improvements would probably require [language changes](https://github.com/tc39/proposal-async-context). But if we step back and think about what we can do without changing the language, I like to frame it around two concepts: “annotation without structure” and “don’t make me think.”

One of the most natural APIs for OpenTelemetry is to start a span, execute work inside that span and have the entire span wrapped up cleanly inside a parent function. If you have very clean, synchronous code, your life will be fairly nice. However, JavaScript was designed originally to be executed on a certain event, be invoked by the browser runtime and then exit. Consequently, the most natural instrumentation API for JavaScript is `console.log`. Every time you stray further from the ergonomics of `console.log`, you make your life harder and fight against the language’s natural patterns.

Go, by contrast, has a `defer` keyword that allows you to create implicit scoping in a semi-explicit way without breaking the control flow of your language. It also provides a context object that lets you thread context through your application without manual propagation. This is perfect for OpenTelemetry (and instrumentation in general). Java has support for thread-local state, decorators and metaprogramming, which allows one to build an ergonomic API on top of the foundations of OpenTelemetry’s base API.

You can see a fairly stark difference between ergonomics with the following (somewhat pointedly chosen) examples:

```
// https://github.com/open-telemetry/opentelemetry-go-contrib/blob/main/examples/dice/instrumented/rolldice.go#L38-L40
var (
    tracer  = otel.Tracer(name)
)
func rolldice(w http.ResponseWriter, r *http.Request) {
    ctx, span := tracer.Start(r.Context(), "roll")
    defer span.End()
    // rest of function
}
```

vs

```
// https://github.com/open-telemetry/opentelemetry-js/blob/main/examples/opentelemetry-web/examples/fetch/index.js#L60-L65
const webTracerWithZone = providerWithZone.getTracer('example-tracer-web');

const singleSpan = webTracerWithZone.startSpan('files-series-info');
context.with(trace.setSpan(context.active(), singleSpan), () => {
  getData(url).then((_data) => {
    trace.getSpan(context.active()).addEvent('fetching-single-span-completed');
    singleSpan.end();
  });
  // rest of function
});
```

While this example is chosen to show off the pain points, we can see what happens when friction occurs between a language’s feature-set and an API’s specification. Ideally, we’d like the code for the Go example and the JavaScript example to be nearly identical in ergonomics.

## Annotation Without Structure

So how do we facilitate the idea that the easiest instrumentation in JavaScript should feel like `console.log`, particularly when you don’t have a nice way to thread context? Asynchronous context in JavaScript is somewhat lacking on the backend and entirely absent on the frontend. You also don’t have thread-local primitives or the ability to share state implicitly in the language. So, what can you do?

I think the key is to look at the underlying specifications and protocols of OpenTelemetry. It turns out that traces, spans, span events and logs all build on top of an underlying primitive… That is, they’re all basically just events. In fact, almost everything in OpenTelemetry is events all the way down.

* Logs are events that are missing an EventName, for example. (*Pedantically* speaking, in the spec events are LogRecords with a non-empty EventName).
* Spans are events with certain types of metadata and semantics about how you should compose and build them.
* Traces are a series of spans, which are, again, just events.

In other words, the semantics around how you have to write the events, what order to send them and what information to put in the events are essentially the only thing causing this friction in the OpenTelemetry API. If you remove some of the restrictions around how you structure your events and enable the OpenTelemetry SDKs to push some of the metadata burden onto the collector, you can solve a lot of the complexity by moving the state machine management from your code control flow into the SDK, or potentially even the language runtime itself. You could even do this in a way that puts the burden of stitching spans and traces together onto something that could be designed to be stateful; while the OpenTelemetry collector is currently stateless, it would be a natural place for handling that state.

My big idea here, which might sound controversial, is this: What if we throw away the idea that spans and traces have to have a certain begin-and-end structure that corresponds with code structure? Instead, what if we annotate everything in a way that allows the state machine of beginning and ending spans to be handled in the collector?

Let’s just say if this piece were a span, I’d be worried about [OpenTelemetry’s ability to handle it](https://thenewstack.io/opentelemetry-challenges-handling-long-running-spans/). Since I’ve got a lot more to cover, I’m going to break it into two pieces. In the next piece, I’ll share my second concept for making a more ergonomic OpenTelemetry for JavaScript: “Don’t make me think.” I’ll then get into some ideas for the future state of telemetry as well as what we can do today to create better support for OpenTelemetry in the browser.

In the meantime, if you’d like to learn more about what the Browser Special Interest Group (SIG) is actively working on, check out this [on-demand webinar](https://get.embrace.io/web-otel-panel-typ?utm_source=the-new-stack&utm_medium=paid&utm_campaign=ergonomic-js). As always, the magic of OpenTelemetry for me has been in its community, and especially in this community’s willingness to come together and build a better future for everyone. [Come join the party!](https://github.com/open-telemetry/community?tab=readme-ov-file#get-involved)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/10/58af1826-cropped-06daf154-screenshot-2024-10-02-at-10.13.52%E2%80%AFam.png)

Hazel Weakly spends her days building out teams of humans as well as the infrastructure, systems, automation and tooling to make life better for others. She’s worked at a variety of companies, across a wide range of tech and knows...

Read more from Hazel Weakly](https://thenewstack.io/author/hazel-weakly/)