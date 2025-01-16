# Cloud Monitoring’s Blind Spot: The User Perspective
![Featued image for: Cloud Monitoring’s Blind Spot: The User Perspective](https://cdn.thenewstack.io/media/2025/01/40b9c1d8-cloud-monitor-blind-spot-1024x576.jpg)
The evolution of internet-centric application delivery has worsened IT’s visibility gaps into what impacts an end user’s experience. This problem is exacerbated when these gaps lead to negative business consequences, such as loss of revenue or lower Net Promoter Scores (NPS). The need to address this worsening visibility gap problem is reinforced by Gartner’s recent publication of its first [Magic Quadrant for Digital Experience Monitoring (DEM)](https://www.catchpoint.com/asset/2024-gartner-magic-quadrant-for-digital-experience-monitoring).

A good way to understand what visibility really should look like is through the perspective of first- versus last-mile monitoring.

## First- vs. Last-Mile Monitoring: Where You Monitor Matters
The first mile represents cloud networks and platforms like [AWS](https://aws.amazon.com/?utm_content=inline+mention), [Azure](https://news.microsoft.com/?utm_content=inline+mention), [Google Cloud](https://cloud.google.com/?utm_content=inline+mention) and even “Joe’s network closet.” These environments are stable, well-optimized and critical for hosting applications. Monitoring from the first mile focuses on ensuring that the core infrastructure and code of your applications are performing as expected.

The last mile, however, is where real users connect to your applications; it’s where experiences occur. This includes backbone networks (e.g., regional ISPs like BT, AT&T and Comcast), last-mile providers (fiber or wireless like Verizon, Sky or T-Mobile) and wireless connections. [Monitoring](https://thenewstack.io/whats-the-difference-between-observability-and-monitoring/) the last mile reveals the real-world challenges users face, such as latency spikes, packet loss and internet service provider (ISP)-specific issues that are invisible from the first mile.

Think of it like the Domino’s “[Paving for Pizza”](https://pavingforpizza.com/) ad campaign — it’s not just about ensuring the pizza is perfect when it leaves the store (first mile); it’s about fixing the potholes in the roads so the pizza arrives intact at the customer’s door (last mile). The same principle applies to digital experiences: Monitoring the first mile isn’t enough if the last mile isn’t delivering. Monitoring from the last mile paints the clearest picture of performance from your users’ perspective.

## Why First-Mile Monitoring Alone Falls Short
Your applications are most likely hosted in a cloud provider’s data center, often within the same [Border Gateway Protocol](https://thenewstack.io/how-a-popular-combo-provides-ddos-protection/) (BGP) autonomous system (AS) as your monitoring tools. This means that monitoring so close to the source does little more than verify the availability of your infrastructure. In other words, this type of “inside of the house” setup offers limited visibility into real-world issues.

**User perspective lost:**Internet Performance Monitoring (IPM) monitors health from the user’s perspective, which cloud-only monitoring can’t do.**Observability risks:**When the first mile goes down — a more frequent occurrence than many realize — your[observability strategy](https://thenewstack.io/observability-in-2025-opentelemetry-and-ai-to-fill-in-gaps/)goes with it. This isn’t just a theoretical risk; it’s something we’ve seen play out time and time again in real-world outages, such as the[Lumen and AWS micro-outage](https://www.catchpoint.com/blog/dont-get-caught-in-the-dark-lessons-from-a-lumen-aws-micro-outage)in August 2024. In this incident, critical systems were disrupted, rippling across interconnected ecosystems and catching businesses off guard.
## Rethinking Observability: Availability and Reachability
When it comes to delivering a flawless digital experience, observability relies on four key pillars: **availability, reachability, performance** and **reliability**. Each plays a critical role in understanding how your applications are performing and how users experience them.

I’ll focus on the first two: availability and reachability. Availability is about whether your application is up and running. Reachability, on the other hand, measures whether users can actually connect to your application, factoring in network latency, packet loss and the number of hops between them and your servers.

I’ll illustrate the difference between monitoring from the cloud versus end-user networks, and how what looks perfect in the cloud often falls apart in the wild.

### Visualizing the Difference: Availability Across Network Types
Cloud monitoring data often paints an overly rosy picture. As the chart below shows, monitoring from the cloud (green line) reports near-perfect availability, consistently hovering around 99.99%. But this data tells only part of the story — it reflects the controlled environment of cloud infrastructure, not the real-world experience of users.

Now, compare this to the backbone (the blue line), last mile (the red line) and wireless (the purple line) data. These fluctuations highlight the everyday challenges users face, from regional ISP disruptions to last-mile instability. The takeaway? While cloud monitoring data might make dashboards look good, it doesn’t account for the realities of real-world networks where your users connect. To truly understand availability, you need to monitor across all these network types.

### Cloud vs. End-User Network Maps
Here is another example. The top map shows monitoring results from the cloud, while the bottom map shows end-user networks.

The cloud shows all green, indicating near-perfect first-mile performance. The bottom map shows the reality from the end-user perspective; the red and yellow markers represent performance issues that are not visible to cloud-only monitoring.

This disparity underscores the critical need for monitoring where your users actually connect. While the cloud may look pristine, end-user networks tell a very different story.

Now why is this?

The above image shows that the path it takes for a user to get to the cloud from an external ISP is more volatile than a cloud ISP (as shown in the image below). This is due to the numerous BGP autonomous systems and hops that exist between a cloud-hosted application and the user. Each AS network represents a different administrative domain. As the traffic traverses these domains, it passes through multiple network hops. These hops can include diverse routing policies, peering agreements and congestion points.

Cloud-based monitoring lacks insight into these intermediate hops, particularly across transit providers and peering exchanges, resulting in a fragmented view of network performance and true user experience.

In contrast, [backbone](https://thenewstack.io/how-meta-is-reinforcing-its-global-network-for-ai-traffic/) monitoring provides a more comprehensive perspective by capturing data closer to the core of the internet, offering visibility into the paths your end user traffic takes and potential bottlenecks along the way.

### Average Response Times: Cloud vs. Backbone ISPs
It’s one thing to know whether your application is up and running, but what about the quality of the connection? The chart below compares response metrics between backbone networks and cloud networks.

On the left, monitoring from backbone networks reveals significant variability in key metrics like **load time** and **wait time**. The spikes represent the challenges users face when traversing real-world networks. Compare that to the cloud on the right, where everything looks stable, smooth and controlled. But most users aren’t connecting from the cloud. Without monitoring from backbone and last-mile networks, you’re only seeing part of the story.

Here’s another example of how cloud monitoring data might make everything look perfect when the reality is far from it. The chart below, showing monitoring from [AWS](https://aws.amazon.com/?utm_content=inline+mention), reports a near-instant response time of 44.79 milliseconds.

But what happens when you shift the perspective to backbone ISPs? In this CenturyLink example, response times skyrocket to 730.67 milliseconds.

This kind of variability isn’t an outlier — it’s the reality users face every day when connecting to your application through different networks. And unless you’re monitoring from these networks, you’re missing the full picture of your application’s reachability.

## Putting It All Together
The data in these charts tell a clear story. It shows what first-mile monitoring alone cannot: the variability, instability and challenges users face every day on backbone, last mile and wireless networks.

The takeaway? To truly understand how your applications are performing, you need to monitor beyond the cloud. Backbone, last mile and wireless networks aren’t just part of the picture — they are the picture. The ability to monitor the entire Internet Stack, including those “eyeball” networks where your users actually connect, is what sets [Catchpoint Internet Performance Monitoring (IPM)](https://www.catchpoint.com/internet-performance-monitoring) apart.

To learn more about how Catchpoint IPM can help you achieve Internet Resilience, [request a demo](https://www.catchpoint.com/guided-product-tour) or [schedule a chat](https://www.catchpoint.com/learn-more) with our solution engineers.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)