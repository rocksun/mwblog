Core Web Vitals (CWVs) are some of the most standardized, user-experience-based telemetry we have for monitoring frontend performance. They’re incredibly useful for getting a snapshot into fundamental performance aspects of a website, like load time and interactivity. But user expectations and industry tooling have both moved beyond static metrics, and CWVs, in isolation, aren’t enough to keep up with performance demands.

Often, these metrics are treated like SEO scores. And while CWVs are critical for website ranking and discoverability, there’s so much more we can do to use this data to troubleshoot and optimize our sites for the ever-increasing demands of end users for faster, more stable, more responsive sites.

Bringing CWVs into the true observability sphere, where typical backend monitoring practices are making their way to the frontend, is a good way to do this.

## Core Web Vitals Are Symptoms, Not Causes

The three Google-defined CWVs — [Largest Contentful Paint (LCP)](https://thenewstack.io/5-dev-tips-to-improve-your-largest-contentful-paint-lcp/), Cumulative Layout Shift (CLS) and Interaction to Next Paint (INP) — describe how users experience an app or site. They capture the foundational elements of a user experience (UX): load speed, stability and interactivity.

Yet they often live in a silo, disconnected from the broader [flows and goals](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app/) users are trying to accomplish. Engineering teams might shave half a second off LCP, for example, only to find that checkout conversion hasn’t improved. These metrics are great at describing what happened, but they don’t get at the *why*.

Observability exists to uncover exactly that. It follows the path from a slow API to a delayed render, linking technical behavior to human experience. By integrating CWVs into a [user-focused observability system](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=core-web-vitals), teams can enrich every trace with the context that explains those experiences.

## What User-Focused Observability Looks Like

What do we mean when we talk about user-focused observability? Essentially, it’s an evolution of traditional observability practices to ensure that the way we instrument, [monitor and analyze data revolves around real user impact](https://thenewstack.io/when-to-use-synthetic-monitoring-vs-real-user-monitoring/).

Where traditional observability focuses on systems and endpoints, user-focused observability extends that lens to people, capturing what they actually experience while using your product.

For example, endpoints can be healthy, but users may still struggle because of frontend rendering issues, JavaScript bottlenecks or local network conditions.

A user-focused approach closes that gap.

## Bringing Core Web Vitals Into Observability With OpenTelemetry

Making CWVs observable data points, rather than siloed metrics, is the key to getting richer, more actionable information that actually helps us optimize the experience for the end user. One way of doing so is by adopting a standard like [OpenTelemetry](https://opentelemetry.io/).

OpenTelemetry (OTel) has already become the industry standard for collecting distributed traces and metrics across microservices. The same model can now be applied to frontend performance by treating traditionally isolated metrics, like CWVs, as spans or [span events](https://opentelemetry.io/docs/concepts/signals/traces/#span-events) within a larger trace that provides more context.

In [Embrace’s](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=core-web-vitals) model, for example, CWVs appear as timestamped span events within the larger top-level span that represents a full user session. In Honeycomb’s model, it’s their instrumentation that creates a span for each CWV within a browser trace that represents the page load or user interaction, and attaches the values as span attributes.

These similar approaches preserve causality and context:

* Each CWV is nested inside a larger span or trace, rather than existing in isolation.
* CWVs can carry attributes like the DOM element responsible, the device and network conditions or the resource that caused the delay.
* These events can then be analyzed alongside adjacent technical spans, such as API calls, image fetches or JavaScript executions, to pinpoint exactly what degraded performance.
* CWV events can be correlated with backend performance degradations via different solutions like trace context propagation (if used in the same tool) or span forwarding integrations across OpenTelemetry-compatible tools. This [bridges the gap between frontend and backend performance](https://thenewstack.io/when-performance-is-product-bridging-the-gap/).

Rather than treating CWVs as standalone metrics, this approach treats them as observable moments in the lived experience of the user.

## Benefits of This Approach

Adopting this user-focused, OpenTelemetry-based approach to CWVs has some clear benefits:

* **You move from aggregates to individuals and gain a more precise way to troubleshoot.**

Traditional RUM tools and [Chrome UX (CrUX)](https://developer.chrome.com/docs/crux) reports operate at the 75th percentile, flattening the diversity of user experiences into a single number. But the long-tail users, those on slower devices, weaker networks or with complex app states, are often the ones who reveal the most critical performance issues. By modeling each Core Web Vital as a discrete event inside a user’s session timeline, you stop analyzing averages and start investigating real experiences. Every LCP, INP and CLS event is traceable to a specific user journey, complete with device context, network state and the technical operations that occurred around it.

* **You correlate UX to business outcomes and can prioritize performance issues that matter the most.**

Once CWV events live within a distributed trace, they can be correlated with higher-level product or revenue metrics. You can stop guessing whether a slow LCP “might” hurt conversions, and instead start quantifying it. For example, you may discover that sessions with an LCP event greater than 3 seconds convert 15% less often, or that a spike in CLS correlates with drop-offs in checkout completion. Because these CWV events sit within larger traces that can, via products like [trace propagation](https://opentelemetry.io/docs/concepts/context-propagation/) or network span forwarding, connect to the backend, you can measure the relationship between technical performance and user engagement across the full stack.

* **You close the loop between frontend and backend, avoiding endless cycles of trial-and-error fixes.**

Treating CWVs as span events lets frontend and backend teams finally see the same story unfold in one timeline. When a user experiences a slow LCP, it’s no longer a mystery buried in an aggregate report; it’s an event that sits directly next to the API call or third-party script span that caused it. This shared visibility eliminates the trial-and-error cycle that often plagues performance optimization. Instead of guessing which fix “might” help, engineers can trace the root cause in context, from the browser’s render thread to the database query.

## What’s Left To Do

The bridge between CWVs, OpenTelemetry and user-focused observability is being built, but it’s not yet standardized.

A few vendors are taking the span approach to modeling CWVs, which expands their usefulness in becoming true user-experience markers rather than singular metrics. For this to become universal, the OpenTelemetry ecosystem still needs to mature in key areas:

* **Standardization:** The official OTel semantic convention for `browser.web_vital` events remains in development; broader adoption and stabilization are needed for interoperability.
* **Native support:** The OTel JavaScript SDK doesn’t yet emit CWV events or map them into session traces by default.
* **Trace context propagation:** Consistently linking frontend CWV events to backend traces still requires careful header propagation and sampling alignment.
* **Cross-vendor convergence:** Vendors must agree on a common schema so CWV events, session traces and backend spans can be analyzed cohesively across tools.

The scaffolding exists, but the maturation isn’t quite there yet. However, as OpenTelemetry’s semantic standards mature, engineers will gain more flexible ways to integrate Core Web Vitals into user-focused observability systems.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/09/2283f93c-cropped-3d50bf42-virnasekuj.png)

Virna Sekuj is a product marketer at Embrace. She has nearly 10 years of experience in product management, marketing and research analysis. Prior to working at Embrace, Virna worked at Bose, Onside Sponsorship and GWI. In her time with Embrace,...

Read more from Virna Sekuj](https://thenewstack.io/author/virna-sekuj/)