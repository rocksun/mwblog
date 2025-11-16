There’s a lot of momentum behind bringing better observability practices to the frontend, and a great example is the launch of a dedicated Browser Special Interest Group (SIG) in the OpenTelemetry project. While OpenTelemetry was originally founded as a solution for the backend observability challenge of distributed tracing, engineering teams and organizations are increasingly embracing it as the open standard for observability across the entire tech stack.

While OpenTelemetry has [had support for collecting telemetry in the JavaScript](https://thenewstack.io/building-an-ergonomic-opentelemetry-for-javascript/) language, the API and SDK was designed for Node.js, a server runtime. To better support the nuances of the browser runtime, the OpenTelemetry project created the Browser SIG to create better instrumentation, tooling and semantic conventions for running JavaScript in frontend web applications.

I sat down with several key members of the Browser SIG for a [fun, movie-themed panel discussion](https://get.embrace.io/web-otel-panel-typ?utm_source=the-new-stack&utm_medium=paid&utm_campaign=web-otel-panel) on some key challenges in [browser observability](https://thenewstack.io/setting-up-opentelemetry-on-the-frontend-because-i-hate-myself/), what the group will be working on and how web developers can get started with OpenTelemetry. Panelists included:

* [Ted Young](https://www.linkedin.com/in/ted-young/), developer program director at [Grafana Labs](https://grafana.com/), OTel co-founder.
* [Purvi Kanal](https://www.linkedin.com/in/purvi-kanal/), senior software engineer at [Honeycomb](https://www.honeycomb.io/), OTel JavaScript approver and browser implementation engineer.
* [Martin Kuba](https://www.linkedin.com/in/kubamartin/), staff software engineer at Grafana Labs, OTel contributor and JavaScript SDK approver.
* [Jared Freeze](https://www.linkedin.com/in/jaredfreeze/), senior software engineer at [Embrace](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=web-otel-panel), OTel Browser SIG contributor.

## Key Challenges in Browser Observability

OpenTelemetry has had a [JavaScript implementation](https://thenewstack.io/javascript/ "JavaScript implementation") for a long time, and it can run in the browser. However, the implementation is primarily focused in a production setting for running in Node.js.

As Young explained, “It’s not really something that we consider, like, a professional product that stacks up against the other things that are out there. But it did work. But in terms of just resource management, the browsers, mobile, everything like that, it’s so different from server-side stuff. We knew that we needed to tackle it very intentionally.”

One reason the browser needs an approach different from backend systems is that the browser runtime is event-driven as opposed to request-driven. Kanal explained how the distributed tracing [approach to observability](https://thenewstack.io/a-user-focused-approach-to-core-web-vitals-via-opentelemetry/) doesn’t quite work in browsers.

“What’s challenging with the browser is that instead of going from this distributed tracing system, you go to an event-driven system with multiple inputs. So here we don’t just have one input. You kind of have multiple. You have the user doing something. You’re clicking around in the browser. You’re scrolling. Users are creating hundreds and hundreds of events, even like hundreds of events per second. Like browser apps are pretty complicated these days,” she said.

“So the user input, you have your application code input. So as the user is doing things, the application is potentially reacting to some of those things, but it also might be doing other things like fetching resources in the background or doing some other kind of background tasks, prefetching other resources.”

Browsers are all like an event loop, responding to event listeners from any number of input sources. They’re not well-designed to be perfectly traced, and it’s not easy to even decide where to start and end traces in the browser. So instead of just measuring individual requests or traces, it’s more helpful to observe frontend applications through the  [lens of user sessions](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app/). And unfortunately, OpenTelemetry does not have a well-defined data model for sessions.

## What Is the Browser SIG Working on?

Initially, the Browser SIG is not focused on creating a new JavaScript SDK for the browser. Instead, it is working on the OpenTelemetry API, instrumentations and data model for the browser runtime.

As Kuba said, “We know there are challenges with the existing instrumentation. So maybe we should step back and look at the API and the SDK and how that compares to other solutions out there.”

For example, there are core instrumentations that are either missing or need to be reevaluated, such as page load/unload, user events, resource timing, Core Web Vitals and errors. Add to that the gaps in the browser data model that need to be addressed, like defining the concept of a session.

Kuba said, “The session is something that ties many different events and many different traces or spans together. So we want to think about sessions as a resource. And it’s also interesting because sessions span page loads.”

Users launch websites and can navigate to several pages within a single experience. Freeze explained some of the challenges in modeling a user session in such situations.

“I like to use the e-commerce example, right? I’m on the homepage, there’s a bunch of products, and I’m opening products in a new tab, right? But I haven’t visited that page yet. It’s happened in the background. … And then like, I go to product one. I’m like, ‘That’s really cool.’ Put it in the cart. Track all those events, go back to the homepage. I’m still having the same experience. So, do you include that? What are the options?”

The sheer variety of web applications also means that engineering teams have different observability requirements based on their business needs. The [OpenTelemetry JavaScript SDK has not been optimized for the browser](https://thenewstack.io/how-to-make-opentelemetry-better-in-the-browser/), and the Browser SIG is working on updating the existing one.

As Kuba said, “Some applications just really care about the smallest bundle size as possible because the speed of the page load is the most important thing. … We’re moving away a little bit from span-based instrumentations to event-based instrumentations, I’m hoping that can make the bundle size smaller. Or at least give users the option of, if they want to collect only certain events, they don’t have to include the tracing SDK. They can just include the log SDK. The tracing is challenging as far as bundle size, because the API and SDK is larger and more complex.”

Giving developers flexibility to choose what they want to include in their bundle is key for the Browser SIG, as well as making updates to the existing JavaScript SDK to make it possible to do better tree shaking.

## How Web Developers Can Get Started With OpenTelemetry

Web developers can use the existing OpenTelemetry JavaScript SDK in their web applications today, with some caveats, the biggest being that it’s not built with a browser-first mentality. For example, web developers who want to use tracing will have a few hurdles when it comes to context propagation.

As Kanal said, “If you are thinking about context propagation across something like an async boundary, you will have to use a library called zone.js to do that, which I think is a tough sell because it’s huge. It comes in at like a megabyte by itself. And it’s also not super well-maintained. And it doesn’t work for async-await anyway. So it might be better to kind of let that go and tie things together through sessions instead of these perfect traces that encompass an entire session, which is the world we want to move towards anyway.”

As Kuba pointed out, “It’s definitely possible right now to just include the log SDK and generate your own events from different parts of your application. Some of the events are not difficult to capture. You can start with that. And then as we build official instrumentations, you can just replace that easily. We are working on semantic conventions right now for some of those events. So I think you could start by generating custom events with those semantic conventions and then just replace that with official instrumentation when it’s available.”

The OpenTelemetry JavaScript SDK already has some helpful browser instrumentation, such as for network requests, document load and user interactions.

The panelists agreed that the best place for web developers to learn about OpenTelemetry was to visit the [OpenTelemetry website](https://opentelemetry.io/) and try out the [OTel demo app](https://opentelemetry.io/docs/demo/). It includes a lot of different types of instrumentation, such as languages and SDKs, including the browser.

Young said, “The OTel demo app is a really great starting point because before you go trying to instrument things and stand everything up, it can be very helpful to just see the data in the product you’re going to be looking at the data in. And it’s something that’s well-instrumented, and has a load tester that can generate all the load and let you actually poke around and get a sense of what it should look like before you go try to do it yourself. That’s really helpful.”

Freeze mentioned another thing that helped him get familiar with OpenTelemetry was the [console exporter](https://opentelemetry.io/docs/languages/js/exporters/#console).

“You could run the libraries and not need an endpoint. You don’t have to start there. You can run in the browser. You can see everything that’s emitted in a well-structured way and be, like, ‘OK, cool, I have the right attributes. I did the right thing. I named this properly. Or I’m doing punctuation correctly for naming keys, whatever it might be.’”

Another option for web developers is to use the [Embrace Web SDK](https://github.com/embrace-io/embrace-web-sdk/). It’s open source, built on OpenTelemetry and connects to any OTel-compatible tooling, so it’s an alternative to using the OpenTelemetry JavaScript SDK for web apps.

To learn more, you can watch the full panel below.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)
[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/07/4a21bc0e-cropped-f8f0ce0e-cropped-21693427-colin-contreary1-600x600.png)

Colin Contreary is the head of content at Embrace. His career spans many roles across his three main passions of writing, technology and entertainment. Prior to working in tech, he wrote and performed for the stage and screen, and also...

Read more from Colin Contreary](https://thenewstack.io/author/colin-contreary/)