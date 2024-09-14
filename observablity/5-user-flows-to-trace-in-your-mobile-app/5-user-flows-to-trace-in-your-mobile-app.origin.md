# 5 User Flows to Trace in Your Mobile App
![Featued image for: 5 User Flows to Trace in Your Mobile App](https://cdn.thenewstack.io/media/2024/09/4771331f-embrace-user-flows-featured-image-1024x576.png)
In a mobile application, as opposed to a system of microservices, tracing can occur between frameworks or simply in a single view. Regardless of the complexity, the goal is the same: evaluating the performance of the application and its effect on user experience. [Modern observability](https://dzone.com/articles/the-future-of-mobile-observability-is-opentelemetr) takes planned effort, but the work is worth it for the insight you gain.

But how will you know when to use a trace?

You should use a trace when you want to track the duration of an operation in your app’s ecosystem. Consider any process that you would describe in [a mobile app](https://thenewstack.io/why-your-mobile-app-needs-client-side-network-monitoring): You might want to see when a view enters the user interface (UI) or if a user completes a login. Tracing the individual steps in the process allows you to see whether it succeeded or failed, if the steps involved were effective, or if they were prone to error or led to unexpected outcomes.

## Tracing in Embrace
Most [tracing frameworks](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide) offer manual instrumentation so you can add traces where they’re needed. This can be daunting, as it requires code at each step in the process that you’re looking at. A good rule of thumb is to add the instrumentation you think you need — for the steps that are most important — and then refine your approach once you’ve analyzed the telemetry that’s being gathered.

I’ll use Embrace’s [iOS Performance Tracing](https://embrace.io/docs/ios/open-source/tracing/) instrumentation to demonstrate key flows in mobile applications. Embrace’s tracing instrumentation sits atop [OpenTelemetry tracing](https://opentelemetry.io/docs/concepts/signals/traces/), which allows for concepts like [SpanEvents](https://opentelemetry.io/docs/concepts/signals/traces/#span-events), [attributes](https://opentelemetry.io/docs/concepts/signals/traces/#attributes) and [child-parent span relationships](https://opentelemetry.io/docs/concepts/signals/traces/#spans).

[Spans are the key elements of traces](https://thenewstack.io/spans-what-are-they-and-why-should-mobile-engineers-care). The Embrace libraries use a specific span, the *root* span, to determine the trace’s name and relationship to other elements within it. A simple trace, with a parent Process A and child SubProcess B, would be instrumented like this:
123456789101112131415161718 |
let parentSpan = Embrace.client? .buildSpan(name: "Process A") // .markAsKeySpan marks the root span and makes // it a searchable key in the Embrace trace dashboard .markAsKeySpan() .startSpan()[...things happen]let childSpan = Embrace.client? .buildSpan(name: "SubProcess B") .setParent(parentSpan) .startSpan()[...]childSpan.end()[...]parentSpan.end() |
After completion, the parent-child trace will be displayed in the dashboard like this:
The parent-child relationship, indicated by the caret-down symbol (under “Spans” on the left side of the image above), will grow as you connect more units of work for a given process. This pattern of explicit instrumentation allows you to add spans and traces throughout your application. Additionally, the green bars indicate that the span completed successfully. In your instrumentation, you determine the success of the span when you end it; all spans must be ended. A failure would generate a red bar in Embrace’s dashboard.

Let’s take a look at the aspects that make up some common flows and see what they look like in the Embrace dashboard when the trace is completed.

## Tracing Search
A person might use your app to search for new information, look through inventory or simply look up their friends’ social media accounts. In any of these cases, they perform a live text search and expect to immediately see a set of results that they can look through and potentially select. You might add some helpful caching for phrases that have been typed during the interaction.

These real-time interactions can be captured using a trace of the search process in your app:

Note that you will want span names for specific actions to remain consistent and avoid a noisy dashboard experience. However, using Span Attributes, you can add more context for each of those spans. For example, if you want to see whether a request fails for a specific search phrase, you could add the text of that phrase as an attribute for each `Network/Search Text Request Made`
span created, and then analyze that information in the dashboard.

## Tracing Authentication
A user generally expects to log in to your application to keep their profile secure. However, there are many ways to get in, and many points where their authentication can fail. Tracing could involve such units as credential caching, login requests, two-factor authentication and even biometrics.

Of conceptual importance in this flow is the difference between user success and technical success. In user terms, the cached credential step and the biometrics step did not succeed in logging them in. However, these components of the app functioned correctly, so the spans are marked “successful” even though they didn’t lead to the “best” user result.

## Tracing Checkout
If you sell something in your app, your users will want to be able to check out! It’s intuitive to them, but for you, there are many steps to completing the sale: They’ll need to add items, you’ll need to check whether they’re in stock, you’ll need payment information, you’ll need to ensure that payment completed and the user received notice that they made a successful purchase.

Note here that I’ve marked the parts of the trace with the broad functionality each one encompasses. In a distributed trace between many microservices, the name of a span describes the service that originated its action. In a monolithic piece of software like a mobile app, adopting a similar naming system might point developers to the correct file or library to look at when evaluating performance or debugging an issue.

## Tracing Location (and Other Permission-Based Functionality)
If you use device-level permissions such as location for user actions, you’ll likely need to ask for those permissions at various points in the app’s UI. Because these occur entirely on the device, you might not have to worry about the app’s interaction with external services. However, these have the added risk of being called in many places, since you might need location access at various points in the app experience.

## Tracing Networking
Finally, I’ll cover the importance of [tracing network requests](https://embrace.io/blog/network-spans-in-traces/). Your app is a piece of software that interacts with networked services through the mobile device that it operates on to send and receive critical information and media. Some of the most common causes of [poor mobile app performance](https://get.embrace.io/10-app-performance-metrics-ebook/) stem from inconsistent or unreliable networking.

Networking ties into each tracing scenario I’ve laid out so far, as most user flows use external services to complete an action. Networking functionality can be entirely off the shelf, custom-built or even run through third-party libraries like Alamofire.

In any case, you might want to dig deep into the code that supports your networking, as the issue’s root cause can be a variety of device, application or user factors in the course of the request — adding headers, finding a working service, receiving data in the correct format and payload size or deserialization issues.

## Wrapping Up
As you can see from these tracing examples, there are many steps where you might wish to dig deeper with child spans. You probably won’t want to reproduce the traces above, as there are many smaller subunits to trace at a finer level of granularity. Depending on how your applications are built, you might want to build individual traces for each step of a process, rather than creating a single large trace with many children.

Tracing allows you to dig into the details of what’s affecting your user experience at the level that you can instrument your code. Being able to aggregate traces of user activity or app performance into a metric, and then unwind a lagging metric back to user activity, means you’ve started braiding your telemetry into a full picture of the user experience.

If you have visibility gaps, consider instrumenting a few traces in key user flows as a starting point. If you have questions or would like to learn more about tracing in mobile apps, you can join the [Embrace Slack Community](https://community.embrace.io/). In addition, check out [the Embrace website](https://embrace.io/) to learn more about how you can deliver the best user experiences.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)