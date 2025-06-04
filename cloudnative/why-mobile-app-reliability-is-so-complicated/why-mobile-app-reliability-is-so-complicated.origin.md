# Why Mobile App Reliability Is So Complicated
![Featued image for: Why Mobile App Reliability Is So Complicated](https://cdn.thenewstack.io/media/2025/05/a581826a-apps-1024x576.jpg)
Mobile development doesn’t get enough credit. While web and backend engineers often benefit from relatively standardized environments, mobile developers face a sprawling, fragmented landscape that makes delivering performant, reliable apps very difficult.

At Embrace, we [analyzed data](https://get.embrace.io/mobile-app-complexity-6-charts?utm_source=the-new-stack&utm_medium=paid&utm_campaign=mobile-app-complexity) from the many mobile app customers using our observability SDKs to understand just how expansive and chaotic the mobile environment really is. The numbers paint a clear picture: Mobile is messy. We’re sharing the data for engineering leadership and reliability teams to see the scale of complexity that mobile teams confront every day and how this can affect end users.

Here’s a glimpse into why mobile is so complicated.

## Companies Often Support Dozens of Mobile App Versions
Unlike browser-based apps that update automatically, [mobile apps are often tied to user behavior](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app/), especially when it comes to updates. Users skip versions, ignore notifications or are restricted by outdated OSes. That leads to a staggering number of active app versions in the wild.

- 31% of apps run five to 10 active versions simultaneously.
- 25% of apps support more than 10 versions.
- 6% of apps have 50+ versions live in production.
Supporting this range of legacy versions isn’t just a test coverage challenge. It’s a performance, crash and observability nightmare. Older versions are often slower, less stable and more vulnerable to regressions. Yet, engineering teams are expected to keep all of them running smoothly. Fun!

## Hardware Variation Is Worse Than You Think
Device types create their own challenges, as [mobile phones operate](https://thenewstack.io/choosing-manual-or-auto-instrumentation-for-mobile-observability/) with different levels of memory and processing power. The Android ecosystem is notoriously fragmented, with 26% of Android devs seeing their apps used across more than 1,000 unique device types.

With each device offering different levels of memory, CPU and OS-level features, optimizing performance at scale becomes nearly impossible. The iOS ecosystem is more controlled when it comes to unique device types, but still far from simple.

## Network Connectivity Is Wildly Inconsistent
The network picture varies across iOS and Android and by geography. Mobile app users rely on different mixes of Wi-Fi and cellular, and this inconsistency can lead to [unpredictable app experiences](https://thenewstack.io/best-practices-for-monitoring-network-conditions-in-mobile/) depending on local infrastructure. For example, 30% of users in Africa and 50% of users in Asia rely exclusively on cellular networks for connectivity.

## Delays in Sending Monitoring Data Back to the Server
Mobile telemetry can be [significantly delayed](https://thenewstack.io/why-your-mobile-app-needs-client-side-network-monitoring/) in reaching the server due to network interruptions, app crashes or user behaviors. Mobile users don’t live in a vacuum — they move! They hop between cellular networks, Wi-Fi connections and dead zones. They lose packets, go offline mid-session and resume hours later. Just think of your favorite hiking trail app. While you’re off the grid, the mobile engineers are in the dark. These connectivity gaps introduce unpredictable telemetry delays.

- 17% of mobile telemetry data arrives more than an hour late.
- 7% takes more than 12 hours to reach observability backends.
This often means engineers are operating with an [incomplete picture of app health](https://www.cncf.io/blog/2024/03/25/why-you-may-be-dropping-key-mobile-data-from-your-observability-solution/). They can’t fix what they don’t know is broken. Luckily, a lot of thinking has gone into [how time plays a crucial role in aggregating mobile data](https://thenewstack.io/how-time-plays-a-crucial-role-in-aggregating-mobile-data/) for observability and what the best practices are.

## Observability Is Evolving for Real-World Complexity
Traditional observability tools were built for stable, server-side environments, but [mobile operates in the wild](https://get.embrace.io/mobile-observability-guide?utm_source=the-new-stack&utm_medium=paid&utm_campaign=mobile-app-complexity). Engineers need visibility into what’s happening on real user devices, across unpredictable network conditions and hardware variations they can’t control. Relying solely on backend signals [misses key mobile performance issues](https://thenewstack.io/sending-mobile-signals-to-the-opentelemetry-collector/) perceived by users. Think of app freezes, slow launches, crashes on specific devices, blank screens, network dropouts, misbehaving third-party SDKs, inconsistent behavior across app versions and unresponsive UI interactions. Today’s observability strategies must include real user context, including what the user saw, when it happened and why it matters for a successful mobile business.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)