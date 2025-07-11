When most developers think about [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/), they picture backend tracing, metrics and logs, not [mobile app performance](https://thenewstack.io/testing-mobile-apps-for-real-world-network-conditions/). But new data shows that’s starting to change.

A [recent survey](https://get.embrace.io/opentelemetry-for-mobile-whats-now-and-whats-next?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-mobile-report) conducted by Enterprise Management Associates (EMA) reveals that mobile observability is becoming a key part of modern observability practices. Organizations with mature observability cultures are not only investing in mobile telemetry, they’re also looking to OpenTelemetry (OTel) as the future of unified instrumentation across both backend and frontend.

Here’s what the numbers say about where OpenTelemetry is headed when it comes to mobile and real user monitoring, and what it means for engineering teams.

## **Mobile Observability Signals Observability Maturity**

Almost two-thirds of the study’s participants reported that their organization has mature observability practices, and more than half said they had fully integrated mobile telemetry. In contrast, only 18% of all other organizations said the same.

This makes sense: True end-to-end visibility requires [visibility into the mobile client](https://get.embrace.io/mobile-observability-guide?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-mobile-report). Without telemetry from the device itself, [you’re missing the origin of user requests](https://thenewstack.io/why-your-mobile-app-needs-client-side-network-monitoring/) and many of the performance problems that affect real people.

Even more striking, 75% of mature organizations reported correlating mobile and backend observability data, giving them a unified view across the stack. That’s compared to just 11% of the less mature orgs.

[![](https://cdn.thenewstack.io/media/2025/07/aeacfd4e-image3-1024x544.png)](https://cdn.thenewstack.io/media/2025/07/aeacfd4e-image3-1024x544.png)

Source: Enterprise Management Associates.

## **OpenTelemetry Adoption: Poised to Triple for Mobile**

Adoption of OpenTelemetry for [mobile data collection](https://thenewstack.io/best-practices-for-monitoring-network-conditions-in-mobile/) is still in its early days. Only 6% of organizations report using it today. But that number is expected to triple in the next 12 to 24 months, according to the EMA survey.

Driving this adoption is a desire to standardize instrumentation across systems. Mobile telemetry is often collected using vendor-specific SDKs or homegrown solutions that don’t interoperate well with the rest of the stack. OpenTelemetry, by contrast, offers an open, vendor-neutral format that enables consistent correlation of mobile, web and backend signals.

Still, OTel support for mobile is evolving. Some teams cited concerns about OpenTelemetry’s maturity, but 62% overall still rated it as a “very important” or “critical” enabler of observability. Furthermore, 83% think OpenTelemetry integration is very important or critical when evaluating new mobile monitoring tools.

[![](https://cdn.thenewstack.io/media/2025/07/f3423cb5-image2-1024x523.png)](https://cdn.thenewstack.io/media/2025/07/f3423cb5-image2-1024x523.png)

Source: Enterprise Management Associates.

## **Integration and Interoperability Are Top Priorities**

When evaluating mobile observability solutions, respondents overwhelmingly prioritized integration. “Easily integrates with other observability tools” was the No. 1 priority, followed by “the ability to share or forward mobile data into other systems” and “mobile issue specialization like [ANRs](https://embrace.io/blog/how-does-an-anr-work/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-mobile-report) [application not responding] and [client-side networking issues](https://embrace.io/blog/best-practices-for-monitoring-network-conditions-in-mobile/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-mobile-report).”

This highlights a broader trend: Engineers are tired of tool sprawl and data silos. Whether they’re focused on backend services, web apps or native mobile apps, teams want unified data and visibility that stretches [from the user’s device to the database](https://thenewstack.io/the-case-for-user-focused-observability/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-mobile-report). OTel SDKs for iOS and Android that reflect the context and nuances of the mobile experience are critical to accomplishing this.

OpenTelemetry supports this unification. Instead of treating mobile as a disconnected edge case, the spec can standardize client-side signals and flow them into existing observability platforms, whether that’s a vendor’s dashboard or a self-hosted Grafana instance.

## **The Next Frontier: Real User Monitoring**

While tracing remains the most common use case for OpenTelemetry, survey respondents signaled strong interest in expanding into user-focused telemetry. In fact, real user monitoring (RUM) was a top data type or source that engineers wanted to see added to OpenTelemetry, second only to generative AI performance data.

In addition, among respondents who say they will conduct more experimentation with OpenTelemetry in the next 12 to 24 months, monitoring real user behavior is tied as the most likely thing they will experiment with.

[![](https://cdn.thenewstack.io/media/2025/07/abab2122-image1-1024x498.png)](https://cdn.thenewstack.io/media/2025/07/abab2122-image1-1024x498.png)

Source: Enterprise Management Associates.

Why does this matter? While traditional backend observability can tell you what your infrastructure is doing, RUM answers what users are experiencing: what screens they’re seeing, how long it takes for content to load and where in the flow they drop off.

As mobile workflows become more complex, the need for client-side tracing and real-time behavior monitoring becomes critical. This aligns with what modern DevOps and site reliability engineering (SRE) teams are already doing: using tracing to connect the dots across distributed systems, now with the client included.

## **The Value of OTel to Capture the Full User Journey**

OpenTelemetry is often described as a movement toward more open, unified observability. Organizations that have fully embraced an OTel strategy look to break down silos and reduce vendor lock-in. [Mobile RUM](https://embrace.io/product/mobile-rum/) is becoming a bigger part of this vision.

The data in this report suggests that OTel-based mobile instrumentation and observability methods will play a major role in the next phase of OpenTelemetry adoption. The trend lines are clear:

* Teams in mature observability organizations are prioritizing mobile as a part of the whole.
* OpenTelemetry adoption for mobile is set to grow significantly.
* RUM and user-focused telemetry are top areas of planned experimentation.
* Purchase decisions for mobile tools are increasingly influenced by OTel support.

Vendors in the observability space are already taking notice. More and more tools are expanding their support for OpenTelemetry, either by facilitating more versatile data ingestion or reworking their agents and SDKs to follow the instrumentation standard.

Many are also getting involved with open source communities, making code contributions and building relationships with the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention), the incubators of the OpenTelemetry project.

End users are no longer an afterthought in observability, and as a key consumer touchpoint, mobile performance is becoming more and more critical to understand, with OpenTelemetry driving standardization and innovation.

For engineering teams investing in long-term observability strategies, this is the moment to pay attention and learn about how OpenTelemetry can play a critical role in the end-user journey.

If you’d like to learn more, you can [download the full “OpenTelemetry for mobile” report here](https://get.embrace.io/opentelemetry-for-mobile-whats-now-and-whats-next?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-mobile-report).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/09/2283f93c-cropped-3d50bf42-virnasekuj.png)

Virna Sekuj is a product marketer at Embrace. She has nearly 10 years of experience in product management, marketing and research analysis. Prior to working at Embrace, Virna worked at Bose, Onside Sponsorship and GWI. In her time with Embrace,...

Read more from Virna Sekuj](https://thenewstack.io/author/virna-sekuj/)