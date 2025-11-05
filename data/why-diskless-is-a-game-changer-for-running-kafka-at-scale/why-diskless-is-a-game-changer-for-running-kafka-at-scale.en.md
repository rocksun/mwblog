[Apache Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/) is one of the most commonly used stream-processing applications. Its high performance, low latency and [open source license](https://thenewstack.io/open-source/) are just some of the reasons [80% of Fortune 100](https://kafka.apache.org/powered-by) enterprises use Kafka to power event-driven applications and deliver resilient data pipelines.

But when you start working with massive amounts of high-velocity data, you quickly run into cost, operational and complexity problems. For cloud native businesses, high replication costs when running Kafka across multiple cloud availability zones are a very serious issue.

Recently, the Kafka community has offered [three Kafka Improvement Proposals](https://cwiki.apache.org/confluence/display/KAFKA/The+Path+Forward+for+Saving+Cross-AZ+Replication+Costs+KIPs) designed specifically to address this problem. One of them, [KP-1150 Diskless Topics](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1150%3A+Diskless+Topics), “proposes a new class of topics in Apache Kafka that delegates replication to object storage,” wrote [Filip Yonov](https://www.linkedin.com/in/filipyonov/), head of streaming services at Aiven, which developed KP-1150, [in a blog post](https://aiven.io/blog/diskless-apache-kafka-kip-1150).

“Rather than eliminating disks altogether, Diskless abstracts them away — leveraging object storage (like S3) to keep costs low and flexibility high,” Yonov said.

## How To Improve Your Kafka Architecture

If running Kafka at scale is giving you headaches, join us on Nov. 20 at 8 a.m. PT | 11 a.m. ET for a special online event: **[Kafka at Scale: Smarter Architectures for Real-Time Business Impact](https://thenewstack.io/webinar/kafka-at-scale-smarter-architectures-for-real-time-business-impact/)**.

During this free webinar, [Greg Harris](https://www.linkedin.com/in/greg-harris-2b86a1126/), open source software engineer at Aiven (and lead author of KP-1150), [David Esposito](https://www.linkedin.com/in/davidespo/), streaming architect at Aiven, and [Chris Pirillo](https://www.linkedin.com/in/chrispirillo/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3Bfkz7tdMZSa2iGG%2BdhC%2FjwA%3D%3D), TNS host, will explore how leading companies are adapting their Kafka architecture to manage larger, faster data streams and deliver real business impact today.

In addition to discussing the pitfalls to avoid when scaling Kafka in the cloud, they’ll also share an exclusive sneak peek at Diskless Topics for Apache Kafka, a breakthrough that removes local disks to make Kafka up to 80% leaner, significantly reducing total cost of ownership (TCO) while simplifying operations and unlocking new ways to scale in the cloud.

## Register for This Free Webinar Today!

If you can’t join us live, [register](https://thenewstack.io/webinar/kafka-at-scale-smarter-architectures-for-real-time-business-impact/) anyway, and we’ll send you a recording following the webinar.

## What You’ll Learn

By attending this special online event, you’ll leave with best practices, real-world examples and actionable tips, including:

* The role of Kafka in driving growth, agility and customer experience for digital-native businesses.
* Common challenges when running Kafka in the cloud, including cost, rebalancing and cross-AZ replication.
* How to measure business impact from real-time streaming.
* Introduction to Diskless Topics (KIP-1150) and what it means for the future of Kafka.
* Real-world use cases: blending diskless and classic topics in a single cluster.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/02/58a0d6b5-vw_headshot.jpg)

As senior sponsor editor at The New Stack, Vicki collaborates with our sponsors to create and publish exceptional content that resonates with our readers. She has many years of experience (more than she would prefer to admit) in technology publishing...

Read more from Vicki Walker](https://thenewstack.io/author/vicki-walker/)