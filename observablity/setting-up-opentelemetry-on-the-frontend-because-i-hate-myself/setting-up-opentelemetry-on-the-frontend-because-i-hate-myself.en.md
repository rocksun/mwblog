Picture this: You’re having a lovely afternoon, you’ve cooked a delicious dinner, you took a walk around the neighborhood and you’re feeling delightful. Well, that just won’t do. Delightful? In this economy? I have the perfect solution! Setting up [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) in your favorite [ReactJS](https://thenewstack.io/instrumenting-a-react-app-using-opentelemetry/) frontend side project. It’s the ideal fix for when you’re feeling cheerful and need to put a solid scowl back on your face come Monday morning.

With just 82 confusing instructions that might not work with your favorite toolchain, you, too, can get lost in a maze of subtle fiddly details. In fact we’ll throw in a free [performance penalty for your app’s asynchronous code](https://github.com/angular/angular/blob/main/packages/zone.js/MODULE.md)!

But wait, there’s more! It’s not enough to install the dependencies, you’ve got to use them, too. Luckily, using OpenTelemetry to instrument the frontend is sure to bring out a frown. From facing context woes correlating [server-side rendering](https://github.com/open-telemetry/opentelemetry-demo/blob/96b292d5f3281d1bbde0309a8d9325475f356a4b/src/frontend/pages/_document.tsx#L22) with [client hydration](https://github.com/open-telemetry/opentelemetry-demo/blob/96b292d5f3281d1bbde0309a8d9325475f356a4b/src/frontend/pages/_app.tsx#L27-L28), to watching [user sessions break on page navigation](https://github.com/open-telemetry/opentelemetry-demo/blob/96b292d5f3281d1bbde0309a8d9325475f356a4b/src/frontend/gateways/Session.gateway.ts) unless you [carefully thread it through local storage](https://github.com/open-telemetry/opentelemetry-demo/blob/96b292d5f3281d1bbde0309a8d9325475f356a4b/src/frontend/utils/telemetry/SessionIdProcessor.ts), to [dealing with telemetry dying when users close or switch the tab](https://github.com/highlight/highlight/blob/881eb80b8065b13c7b388d9b3907bfb2a98a7bb9/sdk/highlight-run/src/client/otel/exporter.ts#L13-L20), you’re sure to find a way to experience exasperation.

If that’s not enough, you can always trigger an existential crisis by asking yourself how to add an attribute to the “main” span. Is there an API method for that? Of course not. Luckily all the cool kids know to cite Jeremy’s blog post for [a neat workaround](https://jeremymorrell.dev/blog/a-practitioners-guide-to-wide-events/#write-a-middleware-to-help-you) (naturally, making it work on the browser is left as an exercise to the reader).

OK, there’s a bit of exaggeration going on and things are improving over time, but the friction is pervasive, especially when compared to [Java](https://thenewstack.io/introduction-to-java-programming-language/) or [Go](https://roadmap.sh/golang) on the backend. That said, hmm… Wait a minute, aren’t frontend developers the majority of the industry? Haven’t they needed high cardinality observability for decades? How did we get here, anyway? Maybe we need to take a step back and ask if we’re approaching frontend observability the wrong way.

## You’re So Context, Baby, and You Don’t Even Know It

Let’s take that step back for a minute and talk about how OpenTelemetry for the frontend got here in the first place. To start, the OpenTelemetry [JavaScript implementation](https://thenewstack.io/javascript/ "JavaScript implementation") is doing the best it can. All things considered, the implementation (and its team of maintainers) are doing a great job! While it’s cathartic to moan about how annoying things are for the frontend, knowing the history of how we got here is crucial to identifying ways that we can realistically improve things.

Stepping back a bit, what we’re really seeing is a combination of the difficulties of implementing the SDK and API specification of OpenTelemetry in JavaScript, plus the implementation quirks of how the implementation was designed.

To take a trip down history lane, OpenTelemetry was originally designed to be used by backends that were stateless and serving multiple tenants with short-lived requests. Those requests would typically live less than 200 milliseconds or so and involved a manually instrumented call chain of child services that was very shallow in depth. Persistent concepts like user sessions were naturally carried in on every request, so handling long-lived state was never really an issue for the server to deal with.

Given that the backend was hosted in a data center, the network was fast and reliable, so minimizing payload for the telemetry itself was rarely a big concern. In addition, due to the service focus of the original implementations, visualizing and designing traces as callstacks made a lot of sense; this callstack design is deeply pervasive in the API, SDK and data specifications.

None of those choices were bad in context, and they still make sense for most backend systems today. Unfortunately, the frontend doesn’t play nicely with a lot of those assumptions, and it makes using OpenTelemetry particularly challenging at times.

An easy example of that is using it for asynchronous code that works in an event-loop architecture: something experienced in ReactJS apps. Another example is harder to see, but it turns out that handling event-driven architectures and [long-running spans in OpenTelemetry](https://thenewstack.io/opentelemetry-challenges-handling-long-running-spans/) require similar approaches. This isn’t a coincidence. Both architectures have several similarities, with the salient one here being the need to represent incomplete information inside the telemetry pipeline (a concept analogous to a write-ahead log).

## The Shape of Data Flow

When we build systems, developers are used to tightly correlated data flow and code structure. However, this isn’t the case with telemetry. With telemetry, developers need to consider how the [users engage with the system](https://thenewstack.io/the-case-for-user-focused-observability/). In other words, we use OpenTelemetry to tell stories about system behavior so  that that we better understand it.

For the backend, often the users and the developers are the same people, so the narrative can closely match the code structure, especially if you practice a DevOps culture where teams operate the systems they build. For the frontend, in contrast, the split between the user and the developer widens because user interaction will have zero resemblance to code structure.

Which is fine. Well, unless your tooling assumes a strong correlation between code structure and user interaction. Whoops! This innocent assumption ends up making life quite troublesome in the frontend. Ideally, understanding the frontend involves looking at a temporal stream of events as users interact with the system. Every user interaction tells a story that developers need to be able to piece together to know what’s going on. However, this introduces friction because it runs counter to the way the tooling was originally built.

Imagine this tension as being the difference between giving people music albums to play versus letting them play songs in any order. With albums, you know the song order, so you can make the album very coherent. Then came music streaming: Now people pick the song order and blend between albums, which means there’s no way to reason about how your song appears in the context of their listening experience. Over time, that encourages changes in the way you write the music and publish it. Indeed, we’ve gone from designing albums as a coherent artifact to stating that songs need a hook every seven seconds.

Drawing a parallel back to tech: Users are unpredictable, they’ll use the same app from multiple tabs, and they might start on one device and continue on another. The real world is messy and never maps nicely to your code’s structure. Nothing makes that more obvious than when the instrumentation of your frontend and backend join together into a chaotic soup of contextual mud.

So, what does that mean for designing effective instrumentation that works for both? Well, it means you’re probably going to have a bad time. It also means you’ll likely reach for different data structures, code patterns and instrumentation techniques (which could be an entire series by itself). Except we don’t really have that option with OpenTelemetry. To understand why, we’re going to need to dig a bit further

## Correlate Now vs. Correlate Later

First, we need to talk about observability vendors. How they store and ingest data has very deep implications for how instrumentation libraries then go on to evolve. To put it shortly, the ideal case for an observability vendor is if the customer sends complete data such that the vendor can append the data to its data store as-is. This is largely the case for OpenTelemetry today (using out-of-the-box capabilities), but taking this approach causes a lot of data duplication over the wire since the data is maximally denormalized. For example, OpenTelemetry’s semantic conventions recommend using a `service.address` set, but it will be repeated on every span ever sent — despite it being a value that will never change.

If one imagines adding useful debugging data such as a build ID, service version, user ID or user agent information, this adds up extraordinarily quickly. That increase in bandwidth is even more painful in the browser since browser OpenTelemetry exporters [don’t support compression yet](https://github.com/open-telemetry/opentelemetry-js/issues/5686).

In a world where networking is both fast and reliable, the trade-off makes perfect sense. Unsurprisingly, OpenTelemetry developed a bandwidth-heavy but compute-light specification. Pushing that complexity of data processing toward the customer makes even more sense given that many of the original vendor implementations were inspired by in-house tooling where, historically, the same company built the instrumentation, the libraries *and* the telemetry backend.

Once you go into the world of frontend services, all of those constraints start to change. The frontend has [significantly restricted compute and network bandwidth](https://embrace.io/blog/best-practices-for-monitoring-network-conditions-in-mobile/), which is exacerbated when you consider that the mobile browsing accounts for over half of all traffic on the web. As a consequence, offloading the complexity of data management to the observability vendor by deduplicating data and having the vendor correlate it would be ideal. For error detection and bandwidth reasons, [sending incomplete traces as snapshots](https://www.cncf.io/blog/2024/06/14/why-embrace-created-span-snapshots-for-mobile-observability-with-opentelemetry/) — rather than keeping the entire trace in memory — also makes sense. Naturally, this is the opposite of what most existing tooling, libraries and vendors support, although this story is slowly changing.

You can think of this tension as “correlate now” vs. “correlate later.” In a “correlate now” system, you need to send a complete span containing all the data in it that you want to query in one go, with no later updates. “Correlate later” systems mean you can send whatever data when you have it, but you have to do the work later to correlate it (via indices), and that can become prohibitively expensive. Sound familiar? It’s the old database debate that we’ve been having for decades. Indices or no indices? One table or many? Should we use schemas? Do we normalize the data?

Ultimately, it depends, but the problem we’re going to run into is that while it does depend, the frontend and backend are most likely going to end up with different ideals; when the two meet, it gets messy.

## What’s the Deal With JavaScript?

Phew! That was a lot, but it was useful background context. That said, we started talking about JavaScript, and it feels like we got sidetracked a bit… What does all of that talk about context and streaming and correlation have to do with JavaScript on the frontend web?

The answer starts by first observing that JavaScript is in a unique position as the only programming language supported by web browsers that can directly interact with the browser’s document object model (DOM); it also happens to be immensely popular on the backend. Because of that, it encounters these issues in a particularly frustrating way: The initial OpenTelemetry instrumentation libraries in JavaScript were built for NodeJS and running in a backend environment, which means they introduce significant friction in the frontend. Egads!

Can we do anything about that? It’d be great if we could. Maybe we “simply” tweak the JavaScript libraries, make some [browser-friendly versions](https://github.com/embrace-io/embrace-web-sdk) and then bam, perfection? Perfect! Everyone’s happy and all is right with the world. I can already hear the unicorns frolicking in the meadows. Wait, what’s that? Unicorns don’t frolic? I’m going to pretend I didn’t hear that.

Coming back down to reality, if you’re wondering why browser-friendly OpenTelemetry libraries are insufficient, ask yourselves the question, “How do we send data to an OpenTelemetry-compliant backend in a way that’s friendly for frontend users in real-world network conditions?”

The answer is going to be a bit horrifying: It turns out that you kind of can’t (at least, out of the box with OpenTelemetry: [Embrace](https://embrace.io/?utm_content=inline+mention), however, works [around that issue](https://www.cncf.io/blog/2024/06/14/why-embrace-created-span-snapshots-for-mobile-observability-with-opentelemetry/)). Are we stuck, then? Forever doomed to wander in a land of mediocre tooling and quirky libraries and frustrating language support because the data model that OpenTelemetry currently implies doesn’t match the data model that frontend applications use? If we’re aiming for perfection, one could argue that, but if we don’t let perfect be the enemy of good, we can solve several immediate challenges for the frontend now, even without changing how OpenTelemetry works.

## A Pragmatic Path Forward

Frontend developers deserve something better for OpenTelemetry, especially since they stand to benefit so much from adopting high-cardinality and high-context instrumentation. Understanding the user experience, especially when interaction is so unconstrained, is a game changer.

I think we can get there. Here’s the pitch:

1. Let’s figure out what the frontend web needs most right now.
2. We make that happen as soon as possible, incrementally, without breaking all the other JavaScript users.
3. Then, use feedback from the community to improve OpenTelemetry itself.
4. Collaboratively build a more powerful observability experience for everyone.

Are you sold? I know I am, and I’m not the only one. It just so happens that the OpenTelemetry community started a frontend browser Special Interest Group (SIG) dedicated to improving OpenTelemetry in the browser. Some of my favorite initiatives of the [Frontend Browser SIG](https://github.com/open-telemetry/community/blob/main/projects/browser-phase-1.md) are:

* Improving handling of loading and unloading in the browser
* Better session support without breaking existing OpenTelemetry data models
* Better logging models for client events, dependency sizes and tracking context across async boundaries

Those are huge and that’s just the start. What I love about this is that no matter how difficult improving OpenTelemetry for the frontend might seem, there’s an international community of people passionate about making things better one step at a time. Today’s development pains will become, slowly but surely, a thing of the distant past. It won’t happen overnight, but it will happen. We’ll be able to work together every step of the way to make understanding our users and improving their experiences a happier and more productive experience for everyone involved.

If you’d like to learn more about what’s in store for OpenTelemetry support for the browser, [check out this live panel discussion](https://get.embrace.io/web-otel-panel/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-on-the-frontend) on July 31 at 10 a.m. PT, hosted by [Embrace](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-on-the-frontend).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/10/58af1826-cropped-06daf154-screenshot-2024-10-02-at-10.13.52%E2%80%AFam.png)

Hazel Weakly spends her days building out teams of humans as well as the infrastructure, systems, automation and tooling to make life better for others. She’s worked at a variety of companies, across a wide range of tech and knows...

Read more from Hazel Weakly](https://thenewstack.io/author/hazel-weakly/)