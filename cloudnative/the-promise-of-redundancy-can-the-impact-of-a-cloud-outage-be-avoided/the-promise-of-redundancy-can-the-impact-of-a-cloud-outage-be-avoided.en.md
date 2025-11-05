The [October 20 AWS outage](https://thenewstack.io/a-cascade-of-failures-a-breakdown-of-the-massive-aws-outage/) was a powerful reminder of just how interconnected today’s applications and services have become. From banking to streaming, healthcare to logistics, organizations of all sizes and industries rely on a complex web of public cloud and other third-party services. As we saw, a single disruption can quickly cascade, affecting not just one company but entire industries and millions of end users.

Faced with such disruption, it’s natural to ask: Why aren’t more companies able to build effective redundancies to shield themselves from disruptions like these? The answer lies in complexity.

## **The Hidden Complexity Behind Modern Applications**

The seamless digital experiences customers and employees expect are powered by a dense fabric of infrastructure and service components, often sourced from third parties. Modern applications depend on myriad underlying services, including cloud platforms, managed databases, serverless functions and external APIs that may themselves rely on the same [cloud providers or similar external dependencies](https://thenewstack.io/cloud-dependencies-need-to-stop-f-ing-us-when-they-go-down/). This intricate web makes it [operationally and economically challenging to build](https://thenewstack.io/building-reliable-ai-requires-a-lot-of-boring-engineering/) fully redundant systems.

Even with engineered failovers, such as switching to another cloud provider region, these strategies are far from straightforward. Each additional layer of redundancy introduces its own set of [dependencies and management](https://thenewstack.io/unlocking-the-power-of-automatic-dependency-management/) challenges.

## **Full Redundancy Isn’t Possible**

For organizations that do have some redundancy in place, knowing when to invoke failover is a difficult calculus. Redundancy can be architected in several ways: Maintaining multiple discrete failure zones, where instances and workloads are [distributed across different cloud](https://thenewstack.io/why-developers-need-to-care-about-distributed-cloud-computing/) providers (multicloud), or employing active-active architectures where workloads run in parallel and service can be maintained if either becomes unavailable. For example, an e-commerce platform might replicate its critical databases and application servers across two distinct regions within the same [cloud provider to ensure service](https://thenewstack.io/how-to-ensure-cloud-native-architectures-are-resilient-and-secure/) continuity if one region experiences an outage.

However, failovers and remediation actions can themselves be disruptive and require time to execute. Data consistency, session state synchronization and DNS propagation delays can all introduce complications and potential service degradation during a transition. In some cases, a failover might create new issues if the secondary environment isn’t fully up to date or if it shares hidden dependencies with the primary one.

Making the right decision depends on understanding the outage’s scope (localized or widespread), duration (temporary or prolonged), the behavior of underlying dependencies and the real impact on users and business outcomes. Without this insight, remediation can be delayed or even worsen the situation by disrupting users or compounding technical challenges.

## **The Case for Visibility and Dependency Mapping**

To meet these challenges, organizations should prioritize improving visibility into the environments they depend on, whether they are self-managed or provided by third parties.  Mapping application and service dependencies is essential for [uncovering hidden risks](https://thenewstack.io/leaky-data-pipelines-uncovering-the-hidden-security-risks/), such as unknown single points of failure, and for forming redundancy strategies. During an outage, real-time insight into how each dependency is performing and how end users are affected becomes critical for making fast, informed decisions.

Provider status [updates can be delayed or too general to address](https://thenewstack.io/linkerd-service-mesh-update-addresses-more-demanding-user-base/) a specific company’s situation. Direct visibility into service behavior and user impact enables organizations to communicate clearly and act decisively, minimizing business disruption.

## **The Role of Digital Resilience**

Cloud provider outages remind us that resilience depends not only on smart architecture, but also on intelligence and visibility across the entire service. As organizations continue to embrace cloud, SaaS and now AI workloads, whose architectures often increase dependency complexity, it’s essential to recognize that each introduces both tremendous opportunity and new categories of risk.

The ability to navigate outage events and other disruptions depends not just on redundancy, which can never be perfect, but on how effectively organizations can see, understand and respond to their environments under duress. This environmental awareness requires end-to-end visibility, making it a cornerstone of digital resilience.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/10/7abac03b-il20250603021714-vaccaroj-scaled-150x150-1.jpg)

Joe Vaccaro is the vice president and general manager of the Cisco ThousandEyes business. He is responsible for the overall strategy and growth of ThousandEyes, a platform that provides end-to-end visibility and intelligence across every network that matters to assure...

Read more from Joe Vaccaro](https://thenewstack.io/author/joe-vaccaro/)