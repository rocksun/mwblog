# Is OTel the Last Observability Agent You’ll Ever Install?
![Featued image for: Is OTel the Last Observability Agent You’ll Ever Install?](https://cdn.thenewstack.io/media/2025/03/de25c4fc-otel-last-observability-agent-1024x576.jpg)
Some things never seem to change. Until they do. And then the change is sudden. And irreversible.

In the past few years, collection of [observability](https://thenewstack.io/observability/) telemetry has undergone such a dramatic change.

What changed is not really *how* we collect telemetry. The techniques we use and what telemetry we collect have not changed that much in the past decade. The change is much more profound: It’s about the dynamics between end users and observability vendors.

## No Country for Proprietary Agents
What has drastically changed are the expectations and norms of telemetry collection. Nowadays, users demand that telemetry collection is performed in a way that is:

**Vendor-independent**: So long, proprietary software development kits (SDKs), and farewell to proprietary wire and trace context propagation formats and protocols. Welcome, open, community-driven standards.**Portable**: Your existing setup should work seamlessly with multiple vendors. If you are unhappy with what an observability tool does with your data, switching should be as easy as changing an endpoint configuration and authentication headers.**Entirely under their control**: Users want control over how telemetry is collected, how much telemetry to collect, and which to keep and which not, using[open source libraries and tools](https://thenewstack.io/open-source/).
This new reality stands in stark contrast with that of the past decade. Proprietary distributed tracing (and, to a lesser extent, metrics and log collection) was the norm. Proprietary SDKs were fiercely opposed only by a vocal minority of power users.

## Why Did the Change Occur?
The desire for vendor-independent, user-controlled collection of telemetry has been there all along. But we didn’t have a realistic way of attaining it.

The catalyst for this long-due change is [OpenTelemetry](https://thenewstack.io/opentelemetry-whats-new-with-the-second-biggest-cncf-project/) (OTel). We could already collect metrics and logs with high-quality open source tools. OpenTelemetry gave us the same ability for distributed tracing. The trifecta is now complete, and we can use open source to collect the overwhelming majority of the telemetry we need to monitor our production systems.

Today, we live in a world where collecting telemetry is largely a solved problem. There is certainly more room for improvement, especially in making adoption simpler and supporting new scenarios. There are also other signals in the works, like production profiling. But the foundational aspects — namely, the [OpenTelemetry protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/), the [Prometheus exposition format](https://prometheus.io/docs/instrumenting/exposition_formats/) and a variety of formats supported by various open source logging agents — are here to stay.

## What’s Next: Observability Tools As Utilities
The way telemetry is collected is effectively in the hands of end users. Telemetry is transmitted using community-driven, portable formats and protocols. Open source and the community have won.

What happens next? Short version: getting more value out of telemetry.

### Heightened Competition
Vendors now have to fiercely compete on the volume of insights that can be offered to you out of the box based on your telemetry, and how much that will cost you. Indeed, the two things are very connected: When I speak with people who gripe about their observability vendors (and it’s a large demographic), they complain about two things: the magnitude of the bill, and that they get so little in return in terms of insights.

Common standards allow the market to correct this: If all it takes to switch over to a different vendor is changing a few configurations, then there are no more lengthy, expensive proofs of concept holding you back. You don’t need to remove your current vendor’s agents and replace them with those of the other vendor before you try in earnest. Even better — you can send the same data to both, and compare apples to apples.

You have more negotiation power. Walking away is easier, so you don’t have as many shortcomings.

### An Expanding Market
Since telemetry collection is largely a solved problem, that is no longer a barrier of entry for new vendors. It has never been easier for new players to join the market and compete. And indeed, I hear of new observability vendors almost every week. At [KubeCon North America 2024](https://thenewstack.io/event/kubecon-cloudnativecon-north-america/) in November, you couldn’t throw a stone without hitting three observability booths on the way down. And it’s awesome! Only through competition can you expect the overall user experience of observability to improve. And the observability experience is ripe for some major disruption.

## Proprietary Telemetry Collection Held Us All Back
A decade ago, starting an observability company required you to invest a lot in supporting an ever-expanding amount of technology. It was a huge barrier of entry. Proprietary technology for telemetry collection is a strange form of capital expenditure (CapEx) that constrains a vendor’s capability to support what their users need to monitor.

As a vendor’s investment in proprietary tracing technology depreciates over time, supported libraries may drop in popularity (but never really go away). Meanwhile, more investment is needed all the time to support additional technologies or newer versions of existing ones. And it compounds: Successful vendors always need to accelerate by pouring in more and more resources, because more prospective customers always bring new technology that requires urgent support.

This was effectively an infinite, unwinnable arms race among vendors. Which is, in no small part, why pretty much every observability vendor now collaborates with the others within OpenTelemetry in a way that would have been unthinkable a decade ago. I am not quite sure it was the plan for OpenTelemetry to open up the observability market the way it did, but I am so very glad it happened.

## Eroding Moats
We are witnessing a renaissance of observability, spurred by the fact that the collection of observability telemetry is a solved problem, and achieved in a way that is open source, community-driven and portable.

Observability vendors, including those that currently dominate the market, have to work harder to win or retain your business. Their moats are eroding because you demand control over how telemetry is collected and, in so doing, you can send that telemetry to other vendors with virtually no effort.

Have a good, hard look at the tools you pay top dollars for. If you find that you have put up with unsatisfactory user experience, poor ratio of insights per dollar, or bill shocks, take a look around. It’s a brave new world out here, and someone somewhere is building an observability tool you will actually love.

*To learn more about Kubernetes and the cloud native ecosystem, join us at KubeCon + CloudNativeCon Europe in London on April 1-4.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)