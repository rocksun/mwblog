# Why JioCinema Skipped Redis for Recommendation Bloom Filters
![Featued image for: Why JioCinema Skipped Redis for Recommendation Bloom Filters](https://cdn.thenewstack.io/media/2025/02/6dd1e3d9-streaming-1024x576.jpg)
When you log in to your favorite streaming service, first impressions matter. The featured content should instantly lure you into binge-watching mode. If it’s full of shows and movies you’ve already seen, your brain quickly shifts into “Hmmm, is it time to cancel this service?” mode.

At a technical level, ensuring fresh recommendations is something every streaming platform faces. But the standard solutions weren’t a good fit for JioCinema, a prominent Indian streaming service known for its affordability and extensive content library. It’s experiencing explosive growth with world-record–breaking 620 million Indian Premier League (IPL) viewers, peaking at over 20 million concurrent viewers.

Instead of building its own Bloom filters or using common solutions like [Redis](https://redis.com/?utm_content=inline+mention) Bloom filters, the company took a different path: using ScyllaDB’s built-in Bloom filter support to check watch status in real time.

JioCinema’s Charan Kamal, a backend developer, and Harshit Jain, a software engineer, recently shared why they took this unconventional path, including the trade-offs of the more obvious solutions and the logistics of implementing this with ScyllaDB.

Watch their complete tech talk below, or read on to skim the highlights.

*Enjoy engineering case studies like this? Choose your own adventure through 50+ tech talks at **Monster Scale Summit** (free + virtual). You can learn from experts like Martin Kleppmann, Kelsey Hightower and Gwen Shapira, plus engineers from Discord, Disney+, Slack, Atlassian, Uber, Canva, Medium, Cloudflare and more. *
## Challenge: “Watch Discounting” for Fresh Recommendations
JioCinema is a leading “over the top” (OTT) streaming platform. The service features top Indian and international entertainment, including live sports (from IPL cricket to LaLiga European football to NBA basketball), new movies, HBO originals and more. The massive content library spans 10 Indian languages.

The JioCinema app uses customized content trays like “Because You Watched” to keep users engaged and help them discover new content. For example, after a user completes “Game of Thrones,” the platform might commonly recommend “House of the Dragon” — but if the user has already watched it, it will suggest something else.

As Jain put it, “These personalized trays not only keep the customers engaged but also enhance content discoverability, fostering long-term engagement and reducing churn rates. However, personalization comes with its own challenges, particularly the issue of recommending content that the customers have already watched. To address this, we have implemented a solution and termed it ‘Watch Discounting.’”

This service must cost-efficiently satisfy low-latency requirements at an impressive scale (10 million daily active users consuming hundreds of thousands of shows and films per day). Kamal explained, “Keeping the sheer size of our customer base and catalog in mind, we had to use a data structure that was space-efficient as well as blazing fast. While we want to keep our recommendations fresh, we also want to avoid over-engineering and making the system overly complex. We could tolerate occasional false positives here. So this led us to Bloom filters — space-efficient probabilistic data structures designed for rapid membership lookup in a set.”

## The Problem with Custom and Redis Bloom Filters
Okay, but *which *Bloom filters were the best fit here?

The team first considered building a custom Bloom filter to store and serve content. Although this “fun exercise” would have provided complete control over the implementation, it presented significant scaling challenges. They didn’t trust that a simple map of Bloom filters would scale vertically to keep pace with JioCinema’s massive and rapidly growing user base. Horizontal scaling would have required either implementing sticky sessions, where specific pods would hold Bloom filters for particular users, or replicating data across every pod in the system. While this would have been an interesting engineering challenge, it just didn’t make sense from a business perspective.

The next option they explored was [Redis with Bloom filter capabilities](https://thenewstack.io/redis-data-types-the-basics/). Their initial testing with an [open source Redis cluster](https://thenewstack.io/valkey-whats-new-and-whats-next/) revealed an interesting issue with Redis’ cluster topology. During high load, nodes would occasionally get hot and trigger failovers, promoting replicas to primary nodes. This created a cascade effect where entire nodes within the cluster became unusable while primary-replica promotions continued in an endless loop.

Looking to avoid that risk, they explored Redis Enterprise. This approach showed significant [performance improvements](https://thenewstack.io/the-architects-guide-to-open-table-formats-and-object-storage/) and indeed met their service-level agreement requirements. However, there was a catch. JioCinema’s business requires millisecond-level latency across multiple regions**. **

According to Kamal, “Even with Redis Enterprise, we faced a choice between an active-active deployment to maintain low latency or compromising the customer experience in certain regions. The latter was unacceptable for our use case. Additionally, Redis Enterprise imposed substantial charges for each operation and replication, making it challenging to justify the return on investment of this feature for our business. This led us to explore ScyllaDB.”

## Implementing Watch Discounting with ScyllaDB
Kamal continued, “ScyllaDB not only supported Bloom filters out of the box, but we also had prior experience using it for different personalization use cases. Knowing its exceptional speed and ability to replicate data into multiple regions and serve customers from locations close to their origin, ScyllaDB seemed like a comprehensive solution. This allowed us to concentrate on developing what mattered most for our customers and enabled us to go to market fast.”

As the following diagram shows, the Watch Discounting feature was powered by two ingestion pipelines.

Batch processes compute users’ watch history within a specified time window, determining if a piece of content meets the completion criteria to be considered “watched.” If so, the system updates the ScyllaDB table with a time-to-live (TTL) attribute, ensuring content only becomes rediscoverable after a specified amount of time.

Short videos (30- to- 60-second videos that drive high engagement) require a different treatment. Here, content must be marked as “viewed” immediately, so real-time event streaming is used to update the watch discounting repository.

## Why ScyllaDB
Kamal concluded, “As mentioned earlier, adopting ScyllaDB enabled us to prioritize developing new functionality over creating data structures. This approach allowed us to keep our nodes small and maintain a clear separation of concerns between Bloom filters and filtering watched content. The unmatched performance of ScyllaDB became evident, especially when dealing with high cardinality of partitions and small data sizes — precisely the characteristics of our data set. TTLs made cleanups easy and permitted the discovery of watched content after a specified period. Moreover, reading from `LOCAL_QUORUM`
ensured that we could access data from the closest region to the user, resulting in high throughput and lower latencies. This strategic combination of features in ScyllaDB significantly contributed to the efficacy and effectiveness of our system.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)