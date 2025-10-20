The category of software observability came of age during the peak of digital transformation, a time when backend services were scaling and shifting toward microservices, systems became increasingly distributed and the key challenge was tracing root causes of latency, outages and errors across sprawling infrastructure. If an API call failed or a service slowed down, engineers wanted to know why.

That mindset led to a telemetry arms race. Collect everything, store everything, query everything and hope answers would emerge through traces, logs and metrics.

But this framework, while still relevant for many backend systems, is fundamentally misaligned with today’s reality: Users don’t interact with your infrastructure; they interact with your product.

On mobile and web, performance issues aren’t just about CPU cycles or memory leaks. They’re about human perception, decision-making and engagement. That’s a more complex, less deterministic world. And it’s one that traditional observability simply isn’t built for.

## Performance Has a Human Impact

In the frontend world, disengagement can happen long before an error is thrown or a crash is detected. When latency increases, even modestly, users perceive your app as broken. They bounce. They stop transacting. They abandon flows.

Take an airline app: If it doesn’t load quickly, a traveler might give up and call into your call center, increasing operational costs and degrading customer experience. Or they’ll find another carrier. Or [consider a social media app:](https://thenewstack.io/hard-truths-to-consider-when-designing-slos-for-mobile-apps/) If a timeline doesn’t render instantly, the user exits, moves onto the next real-time app and you lose engagement, revenue and ad impressions.

And yet, product managers and designers often lack visibility into how load times or subtle UX hiccups affect engagement. The result? Blind spots. A [performance regression slips into production](https://thenewstack.io/when-performance-is-product-bridging-the-gap/). Notifications arrive too slowly. A layout shift causes frustration. And the only signal anyone sees is a dip in retention they cannot explain (or worse, no signal at all).

## The Binary Trap: Why Frontend Teams Stay in the Dark

Most frontend teams haven’t built a culture of measuring and iterating on performance in a nuanced way. They often treat performance as binary: Either it’s “fine” or “totally broken.”

But that’s not how users experience it. Performance exists on a spectrum, and most disengagement happens in the gray area, when things are slow enough to be frustrating, but not so broken that monitoring tools catch them.

This is the fundamental flaw in today’s observability practices: Companies built tooling that tells them whether a request failed, but not whether a [user gave up halfway through a booking flow](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app/). They can measure trace durations, but not whether UI responsiveness dropped below the threshold that makes users stick around.

It’s time for a new definition of observability, one that focuses on how performance affects end-user experience and behavior.

## A User-Centric Approach Cuts Out Guesswork

True user-focused observability asks simple questions, such as: “Can your team confidently measure how load times and latency affect real user engagement across key flows?” and “Do you know how to track the technical performance of your company’s most critical, revenue-impacting touch points on your site and mobile app?”

For most organizations, the answer is no. That’s a huge opportunity to improve.

By instrumenting standardized telemetry, user flows and behavioral signals, teams can begin to correlate performance with actual outcomes: Do users complete the action we intended? Do they drop off? Are they behaving differently after a release?

For example, when launching a new feature to production, teams should be able to see whether users engage with it, whether it performs reliably and if not, why. Was it a rendering delay? A confusing UI? A regression in load time? This isn’t a nice-to-have; it’s the key to delivering products that users actually want to use.

## Reframing Observability Around User Journeys

Think about the concept of a session timeline. It’s useful, but it’s only a slice of the picture. What we need are *user journeys* — maps that stitch together key steps, entry points, drop-offs and friction points. These journeys allow teams to visualize how performance, bugs or design mismatches derail engagement.

For example, we’ve seen critical drop-off points emerge from things as small as naming conventions or wording choices. When those details combine with latency, they compound into serious friction, yet traditional observability tooling rarely surfaces these nuances.

Instead of asking, “Did the backend return a 200 status?” we should ask, “Did the user actually complete the action?” And if not, “What signals can explain why?”

## Understanding Where Performance Affects Engagement

We need to go far beyond what product analytics, crash reporters and logging tools provide. We must solve the fundamental, yet often overlooked, problem: giving frontend and product teams the power to understand how performance affects user engagement.

Yes, we must care about crashes and application not responding (ANR) issues. But those are the tip of the iceberg. We must understand the long tail of issues that quietly erode trust and usage: retries that produce pulsing loading screens, minor layout shifts that frustrate users or performance regressions that escape notice until growth stalls.

Product analytics tools may show heat maps and rage clicks for product and marketing teams, but they don’t tell engineers the why. Oversimplified solutions may show error rates, but not the impact on user retention. We need to bridge that gap.

## The Future: Measuring What Matters

We believe engineering teams shouldn’t be asking, “What’s our ANR rate?” during standups. They should be asking, “Do any of our key flows show degraded user behavior since the last release?”

That’s the shift. And at Embrace, we’re building the tools to support it. By connecting telemetry with engagement signals, stitching together user journeys and making reliability visible (not just traceable), we hope to help teams make smarter decisions, faster.

To learn more about how user-focused observability can improve the performance and reliability of your user experiences, check out what we’re [building at Embrace](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=observability-stuck-in-the-past).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/10/49931773-cropped-5a6e2185-andrew-tunall.jpeg)

Andrew Tunall is president and chief product officer at Embrace. Prior to Embrace he was the vice president of product at New Relic where he built New Relic’s cloud observability practice, including development of serverless observability. Prior to New Relic....

Read more from Andrew Tunall](https://thenewstack.io/author/andrew-tunall/)