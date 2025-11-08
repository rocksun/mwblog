The season is changing for frontend observability, as we’re seeing great community involvement in improving  [OpenTelemetry support for web apps and mobile apps](https://thenewstack.io/what-new-data-tells-us-about-opentelemetry-adoption-for-mobile/). For example, there’s a new Browser Special Interest Group (SIG) in the OpenTelemetry project, and they’re working to improve OTel support for the [browser runtime](https://thenewstack.io/how-to-make-opentelemetry-better-in-the-browser/). You can learn more about what they’ll be working on in this [on-demand panel discussion](https://get.embrace.io/web-otel-panel-typ?utm_source=the-new-stack&utm_medium=paid&utm_campaign=fall-otel-panel).

The OTel community also has dedicated Android and Swift SIGs for improving the APIs, instrumentation libraries and semantic conventions for collecting telemetry on the two [native mobile app platforms](https://thenewstack.io/how-to-instrument-a-react-native-app-to-send-otel-signals/). And organizations are taking note, with a recent survey conducted by Enterprise Management Associates (EMA) revealing that [adoption of OpenTelemetry for mobile data collection](https://thenewstack.io/what-new-data-tells-us-about-opentelemetry-adoption-for-mobile/) is set to triple in the next 12 to 24 months.

I sat down with several key members of the Android and Swift SIGs for a [fun, fall-themed panel discussion](https://get.embrace.io/fall-otel-panel-typ?utm_source=the-new-stack&utm_medium=paid&utm_campaign=fall-otel-panel) on the key challenges in mobile telemetry collection and the state of OpenTelemetry support for mobile. Panelists included:

* [Ari Demarco](https://www.linkedin.com/in/ariel-demarco-a4b34aa0/), iOS software engineer at [Embrace](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=fall-otel-panel), OTel Swift maintainer.
* [Bryce Buchanan](https://www.linkedin.com/in/brycebuchanan/), principal engineer at [Elastic](https://www.elastic.co/), OTel Swift maintainer.
* [Hanson Ho](https://www.linkedin.com/in/hanson-ho/), Android architect at Embrace, OTel contributor and OTel Android approver.
* [Jason Plumb](https://www.linkedin.com/in/jasonplumb/), senior principal software engineer at [Splunk](https://www.splunk.com/), OTel Android maintainer and OTel Java approver.
* [Nacho Bonafonte](https://www.linkedin.com/in/nachob/), senior software engineer, OTel Swift maintainer.

## Challenges With Collecting Telemetry on Mobile Platforms

When mobile developers use OpenTelemetry, they must be mindful of the sheer scale of [data that mobile apps can generate](https://thenewstack.io/how-time-plays-a-crucial-role-in-aggregating-mobile-data/). Buchanan mentioned that while backend systems run on thousands of clients under tightly controlled conditions, mobile apps can run on millions of clients.

Demarco chimed in, “That also leads to the problem of data volumes, because depending on the app, a mobile application can generate an enormous amount of telemetry. So, unlike backends that you can control sampling centrally, in mobile, the sampling decisions probably should be made on-device with kind of limited visibility into the bigger picture. And then you have the question, if you oversample, you’ll waste a lot of bandwidth or battery. […] But if you undersample, you probably miss critical telemetry that is necessary to identify issues or understand behaviors.”

Mobile developers are also hyper-focused on the performance of their apps, which can be affected by the operational cost of capturing telemetry. Plumb mentioned several things developers must keep in mind, including which API calls the app must make to the platform, how long the app spends in those callbacks or event handlers and also the payload size of network requests on the wire.

“Efficiently handling those payloads is also something people, I think, are specifically challenged with on mobile that doesn’t exist in other platforms, and we don’t have the luxury of just …[scaling] horizontally, like, fire up a few more instances,” said Plumb.

The platforms that mobile apps run on are also tightly controlled by Google and Apple. As Bonafonte said, “The privacy that the platform puts you in is something that’s difficult.” Mobile developers need support from the operating system to collect data, so if the system doesn’t allow them to collect certain types of telemetry, they’re limited in how they can effectively observe their applications.

Unlike servers, mobile apps have a life cycle complexity, which can make it incredibly difficult to understand the conditions that lead to issues.

As Demarco pointed out, “Mobile apps don’t run continuously, so they are suspended, backgrounded, terminated, killed by OS, there’s a crash, … the OS can pre-warm your application, the application could launch because of a push notification, a background fetch or because a human tapped into the icon. So, when do you flush your telemetry? … How do you track session continuity across app restarts? What happens to, I don’t know, [in-flight spans whenever there’s a crash](https://www.cncf.io/blog/2024/06/14/why-embrace-created-span-snapshots-for-mobile-observability-with-opentelemetry/), or the OS kills your process? So there’s a bunch of complexity in terms of what do you decide to do in those cases? And it’s not trivial … just solving one of those questions is not a one-liner thing you’ll solve in your code. It’s something you really have to think through to actually solve that.”

## Challenges Mobile Devs Have With Observability Practices

Traditionally, observability is seen as being within the purview of backend teams, and as such, mobile developers frequently don’t understand it. Ho mentioned that mobile developers generally interact with OpenTelemetry because they’re told to as opposed to being something they themselves reach for.

“Tracing and … telemetry is not a core competency of mobile developers … because, you know, the challenges that they face are different. … There’s so much to actually teach a team, and the architecture, the mobile app architectures also aren’t super well designed for maintainable instrumentation,” said Ho.

Product managers might want better visibility to explain the performance (or lack thereof) in a new feature, so they ask mobile developers to collect more observability data. But neither the mobile developer nor the product manager knows what to collect. This lack of clarity when it comes to observability instrumentation for mobile apps was a common thread in our discussion.

Buchanan mentioned that even something as simple as when you should start a [span](https://thenewstack.io/spans-what-are-they-and-why-should-mobile-engineers-care/) is not trivial on a mobile device. “On a backend, it’s very trivial. It’s like, ‘Oh, when I get a request, that’s when a span starts.’ But for a mobile developer, … should I do it when somebody clicks a button? When a network starts? … There’s no right answer to that, like, how should you instrument that? It really depends on what your app does and what you’re trying to monitor.”

Plumb agreed that OpenTelemetry doesn’t have excellent guidance for developers around some of these client-side use cases.

“We don’t yet have a really good data model or just a conceptual description of what sessions are.”

He contrasted this challenge with backend observability tooling that has several use cases very well-defined at this point. For example, every vendor that has a tracing solution is going to have a trace waterfall view, and every [real user monitoring (RUM)](https://thenewstack.io/when-to-use-synthetic-monitoring-vs-real-user-monitoring/)  vendor is going to have a way to analyze funnels.

As Ho pointed out, “When you’re a backend service, the goal is to take the request and shoot out the response. You want to log how long that took and if there’s anything interesting that’s happening in the middle. The goal is simple. The goal of a mobile app is to be defined.”

What the Uber Eats team cares about is different from the Pinterest team, which is different from a banking app.

“To understand the goals and translating that into what kind of telemetry is a non-trivial leap. It seems trivial, if you haven’t done it, but when you do it, you’re, like, ‘I care about everything.’ Do you really care about everything?” said Ho.

## Better OpenTelemetry Support for Android and Swift

The Android and Swift SIGs are improving the developer experience of using OpenTelemetry. Beyond manually capturing key OpenTelemetry signals of logs and traces, both SDKs can also capture mobile-specific telemetry:

* The Android SDK has instrumentation for [Application Not Responding (ANR) errors](https://embrace.io/blog/how-does-an-anr-work/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=fall-otel-panel), crash reporting, view tracking and network calls.
* The Swift SDK has instrumentation for network calls made using URLSession as well as session events that trigger off app lifecycle changes.

The Swift SIG also addressed a key challenge that stems from working in Apple’s tightly controlled mobile platform. Apple’s official package manager, Swift Package Manager, requires downloading all dependencies of all libraries in your projects, even if you don’t use them in your application. As a consequence, the OpenTelemetry Swift repository was very large, which meant mobile developers faced large package download sizes to use OTel in their iOS apps.

As Bonafonte shared, “[OpenTelemetry Swift] had to support a protobuf OTLP [OpenTelemetry Line Protocol] protocol with protobuf, and that means that you have a dependency on Apple on a library from Apple that has a dependency of another library from Apple, and it has a dependency of another library and another and another and another.”

Ari chimed in, “Whenever you have to download it, or compile your application, run tests, run this in CI, build the application and deploy that, all that takes a bunch of time, and obviously, for example, in terms of CI, minutes is money, so … for every single iOS developer, it was going to be a pain. And probably, maybe they just wanted to use the API or just our implementation of the OpenTelemetry SDK.”

As a solution, the Swift SIG divided the code into two separate repositories. The official OpenTelemetry Swift repository is the main repository, and it contains everything needed to work with OTLP. The maintainers created another repository called OpenTelemetry Swift Core, which only contains the OpenTelemetry Swift API and OpenTelemetry Swift SDK. Those two pieces are the bare minimum to get started, create traces and emit logs. iOS developers can now instrument applications, process data and export it without all the overhead of the main repository.

The Android SIG is working on three main improvements. The first is better stabilization for the initialization API for the Android agent, and is expected to be completed soon. The second is broadening the instrumentation, which includes enhancing support for build-time auto-instrumentation.

As Plumb said, “The third category, which is, I think, maybe just as important, are semantic conventions. … With every bit of instrumentation, with every kind of new feature that we’re adding, we’re trying to mirror that in the semantic conventions, even if the first pass is in development or experimental, at least having that out there and documented, what it means, what the intent is when you see a piece of data marked with this name, what these attributes hang off of it mean.”

The challenge is being inclusive of all the different opinions when it comes to observing mobile apps. An example Ho gave for the complexity in defining a mobile session was the problem of foreground vs. background app behavior. When should a session start for a podcast app that runs mostly in the background? What happens for apps that are mostly run in the foreground, but have background [activities that trigger content refreshes and user interface (UI) updates](https://thenewstack.io/how-to-make-sense-of-ios-user-activity-with-opentelemetry/) to be ready on the next app launch? What should a session be for point-of-sale (POS) apps that run constantly in the foreground for many hours at a time?

Ho then shared an Android SIG development in Embrace’s [Kotlin API donation proposal](https://opentelemetry.io/blog/2025/kotlin-multiplatform-opentelemetry/) to OpenTelemetry. Kotlin is the official language of Android development; however, the OpenTelemetry Android SDK currently utilizes the OpenTelemetry Java SDK under the hood to record telemetry. Adopting a Kotlin API and SDK would make it easier for mobile developers to use OpenTelemetry because the Kotlin programming language is more familiar, idiomatic and usable in modern mobile application development.

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