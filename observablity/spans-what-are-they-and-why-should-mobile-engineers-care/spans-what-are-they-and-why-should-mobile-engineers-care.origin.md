# Spans: What Are They and Why Should Mobile Engineers Care?
![Featued image for: Spans: What Are They and Why Should Mobile Engineers Care?](https://cdn.thenewstack.io/media/2024/08/969de6d9-embrace-featured-image-what-is-a-span-1024x538.png)
Mobile engineers are very familiar with application crashes and the importance of keeping crash rates within acceptable bounds. While not as drastic and obvious a failure as a crash, application hangs and slowness can have equally negative impacts on long-term user engagement.

People’s patience is finite, and most will tolerate slow, frustrating experiences for only so long before deleting an app, as this data shows.

![Likelihood that users will delete an application based on slow behavior. Data from The State of Mobile Experience report by Embrace.](https://cdn.thenewstack.io/media/2024/08/06bd8516-embrace-state-of-mobile-experience-results.png)
Likelihood that users will delete an application based on slow behavior. Data from [The State of Mobile Experience](https://get.embrace.io/state-of-mobile-experience-2023/) report by [Embrace](https://embrace.io/).

So, what can you do to understand where your app is running slow?

This is where spans come in. They help you measure the performance of key actions within your application so you can quickly address problems.

## What Is a Span?
Conceptually, spans are quite simple and consist of three key things:

- They have a start time and end time, and thus measure a duration. This is different from crashes and error logs, which are anchored to a single point in time.
- They have an outcome: Did what you were measuring succeed or fail?
- They can have parent-child relationships with other spans.
![Example of a parent span and its child spans that measure the performance of add-to-cart functionality.](https://cdn.thenewstack.io/media/2024/08/79f24c70-embrace-span-example-1024x536.png)
Example of a parent span and its child spans that measure the performance of add-to-cart functionality.

Spans are incredibly flexible in what they can be used for. Spans that monitor larger functions in the app, e.g., the entire time a user spends on a checkout page in an e-commerce app, are typically used by product organizations. However, I will discuss [performance spans](https://embrace.io/blog/what-is-performance-tracing/), which focus on more granular tasks and are typically more helpful to mobile engineers working to understand and fix performance issues.

A performance span measures the duration of actions and flows in your app that are not directly dependent on user interactions. In other words, performance spans measure how long it takes a given action to complete (e.g., add to cart).

## What Are the Benefits of Using Spans?
Spans can help [mobile engineers](https://thenewstack.io/intertwined-worlds-platform-and-mobile-app-engineering/) in several ways.

### Understand Performance and Identify Slowness
Spans help you understand the true performance of your app once it has been released. Actions may be fast and never hang while testing a clean install of your app on a modern iOS or Android device with a fast network connection. But they may behave very differently for a significant subset of your real-world users.

Unless you instrument performance spans, you won’t know what your user population really experiences. Maybe average [startup duration](https://embrace.io/blog/top-5-factors-slow-down-app-startup/) on some devices jumps significantly due to a new ad SDK version. Perhaps payment processing is slow for users in certain countries. Unless you measure these things, you will not know the frustration building with significant parts of your user population.

![Example of a span that shows a combination of acceptable and unacceptable durations. For about 65% of users, this span duration was fine, but for the remaining 35% the duration is unacceptably long.](https://cdn.thenewstack.io/media/2024/08/541ef2d7-embrace-span-durations-graph-1024x597.png)
Example of a span that shows a combination of acceptable and unacceptable durations. For about 65% of users, this span duration is fine, but for the remaining 35%, the duration is unacceptably long.

As a mobile engineer, it can be incredibly helpful to know the extent of a problem. Did your app get a few bad reviews for slow behavior but the issue doesn’t affect a large proportion of your users? Or do the negative reviews indicate a problem that affects a larger percentage of users?

Having span data makes it much simpler to decide whether to prioritize improving the performance of various parts of your app. In the sample chart above, a real problem exists for about 35% of users.

### Use a Shared Language With Your DevOps Team
Your backend team already uses spans to understand service and infrastructure health, and your [DevOps team](https://roadmap.sh/devops) is familiar with how to analyze and monitor them. Adopting a shared telemetry language allows you to standardize how you instrument the pieces of your mobile and web apps. Using a shared language also simplifies how you can connect the spans that start in the mobile app with all the backend services they interact with.

By tracing key actions and flows through the entire journey [from client to backend](https://thenewstack.io/why-your-mobile-app-needs-client-side-network-monitoring) and back to the client, you get a complete picture of what is really causing the slowness that end users experience.

## What Parts of Your Mobile App Need Spans?
Spans are incredibly versatile, so how you can best use them for your application will depend on your business and technical goals. I will use an e-commerce app as an example for understanding what makes sense to instrument. In general, though, [enumerating the parts or flows](https://embrace.io/product/performance-profiling-embrace/) in your app that are most critical to a good user experience is a good starting point for deciding where to add spans.

Critical flows in most e-commerce apps include:

### Login
While some apps allow purchasing as a guest, in most cases buyers have to log in. While this may seem like a simple process, modern logins have many components that were not common a decade ago, such as biometric inputs and [two-factor authentication (2FA)](https://thenewstack.io/githubs-2fa-push-boosts-adoption-among-developers/). You can have a root span for the login and child spans for the individual components, such as accessing biometric data and getting input for 2FA.

### Product Search
How long does it take for search results to appear? How well does delivering search results work over challenging network connections? How long does it take to render the search results? You can use a root span for the search operation and break it down.

### Adding an Item to the Shopping Cart
When a user clicks a button to add an item to their cart, how long does it take to succeed? Are there network calls? Will it work with a poor network connection?

### Checkout
The most important part of an e-commerce app is enabling users to successfully make purchases, so monitoring the actual order submission process is incredibly important. You can add a span that measures the time from when a “Submit order” button is clicked until the “Order confirmed screen” appears. Then you can add child spans that measure individual steps in that journey, like making a call to a third-party payment provider.

## How You Can Get Started Adding Spans to Your Mobile App
Instrumenting a few spans manually is typically not a challenging task, and when you use an observability SDK like the [ones we have built at Embrace](https://github.com/embrace-io/), you will also get auto-instrumented spans for common tasks such as network requests. You can start by instrumenting one or two critical flows in your app and then expand from there. You don’t need to exhaustively instrument every single flow in your app before you can derive value.

Choosing observability SDKs that are [OpenTelemetry (OTel)-compliant](https://embrace.io/opentelemetry-for-mobile/) gives you a great deal of flexibility in how you collect and analyze your performance span data. Embrace provides a hosted service, but you can also choose to send your data to an [OTel](https://thenewstack.io/why-the-latest-advances-in-opentelemetry-are-significant)-compatible collector.

To learn more about how performance spans can help you deliver a better end-user experience, feel free to [check out Embrace’s website](https://embrace.io/) or join [our Slack community](https://community.embrace.io/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)