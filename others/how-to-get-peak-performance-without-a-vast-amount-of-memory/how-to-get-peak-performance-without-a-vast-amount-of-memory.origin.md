# How to Get Peak Performance without a Vast Amount of Memory
![Featued image for: How to Get Peak Performance without a Vast Amount of Memory](https://cdn.thenewstack.io/media/2024/04/ab569452-buffalo-1024x576.jpg)
Have you heard of the buffalo theory? According to this theory, a herd of buffalo can only move as fast as the slowest buffalo.” Surprisingly, this wisdom finds a parallel in computer program operation: The speed of an application is constrained by its slowest subprocess.
Let’s consider the website of an online retailer. The task of loading a product page is far from trivial — it demands the seamless execution of multiple suboperations, including but not limited to:
- Retrieving detailed product descriptions
- Loading product images and videos
- Fetching customer reviews
- Generating suggestions for similar products
- Compiling recommendations for commonly bundled items
- Accessing user account details
- Summarizing the shopping basket’s contents
- Displaying recently viewed items
- Presenting available discounts
Many of these tasks require
[database queries](https://thenewstack.io/data/). If we were to chart the time the database takes to provide the necessary information for each suboperation, the pattern would resemble the following:
Clearly, the
[page loading time](https://thenewstack.io/deferable-views-page-load-improvements-coming-to-angular/) cannot surpass the duration of the most time-consuming suboperation, which in this scenario is suboperation 5. In efforts to streamline performance, the conventional approach involves deploying a cache in front of the [database](https://roadmap.sh/datastructures-and-algorithms). This strategy would change the response times to:
Some operations will benefit from the cache, swiftly retrieving data, whereas others will require direct database access, which will be as slow as before. Given that the overall page loading speed only depends on the slowest task, the introduction of a cache yields a minimal effect on total page load time.
The term “minimal” is used deliberately because, in practice, introducing a cache might slightly improve the response times for operations that do not hit the cache. Essentially, placing a cache in front of the database reduces its workload, which might result in a slightly better performance. However, that improvement is unlikely to be drastic unless the database is massively underprovisioned.
Nonetheless, this marginal enhancement might not justify the investment, considering that similar improvements could be achieved by simply allocating more resources to the database. That strategy would not complicate the application or infrastructure as adding a cache system might.
One might speculate whether a sufficiently high cache hit rate could decisively improve performance. Unfortunately, the answer remains negative. This optimism fails to consider a crucial detail: enhancing average latency does not affect maximum latency. As the number of subprocesses increases, the likelihood of achieving a cache hit for all operations drops exponentially, highlighting the constrained effectiveness of caching as the subprocesses accumulate.
The following chart illustrates the diminishing efficacy of caching strategies as the number of subprocesses increases:
It’s important to highlight that even with an impressive 99% cache hit rate, achieved by maintaining a substantial cache size, the probability of a page load involving five suboperations being served solely from the cache would not exceed %95 (=%99^5). Although a 95% efficiency level is noteworthy, most businesses aim to ensure optimal performance for 99% of user requests, highlighting a gap between the ideal and the actual outcomes with such a caching strategy.
## Redefining the Solution
Addressing the core issue is essential for solving the problem. The issue with caching is that it improves the average latency of subprocesses, which has minimal impact on the overall application latency. To significantly enhance performance, the focus must shift to reducing the maximum latency among subprocesses (specifically, the higher percentile latency).
Put simply, if data access is slowing down your application, the only solution is a faster database, not a cache. Multiple vendors boast that they offer sub-millisecond latency figures; however, most achieve these numbers through reliance on an internal caching layer. It’s important to note that the limitations of caching strategies, as discussed previously, are equally applicable to these internal caches as well.
Look for a
[database technology](https://aerospike.com/products/database/?utm_source=prnewswire&utm_medium=press&utm_campaign=2024Q1PR&utm_content=Aerospike-Database) like Aerospike capable of delivering [sub-millisecond latency](https://aerospike.com/products/features/hybrid-memory-architecture/?utm_source=prnewswire&utm_medium=press&utm_campaign=2024Q1PR&utm_content=sub-millisecond-response) without depending on a caching layer. By delivering data directly from disk — accessing any segment of data, even when the memory-to-disk ratio is as low as 1% — it achieves performance on par with technologies that require data to be served from memory to accomplish rapid response times.
## Case Study: Transforming a Large E-Commerce Company
A leading online retailer’s transformation illustrates the impact of strategic database optimization.
The retailer relies on complex data analysis to provide effective product recommendations and ad placements. After migrating to Aerospike, the company saw a 6% increase in customer cart size and a 30% decrease in cart abandonment. These figures underline the transformative potential of optimizing data access in the digital commerce landscape.
Visit our website to learn more about
[Aerospike Database](https://aerospike.com/products/database/?utm_source=prnewswire&utm_medium=press&utm_campaign=2024Q1PR&utm_content=Aerospike-Database). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)