*Editor’s Note: This article is an excerpt from the Manning book “*[*Latency*](https://www.manning.com/books/latency)*.” This book will help you better diagnose latency problems and master the low-latency techniques that have been predominantly “tribal knowledge” until now. You can* [*download three chapters free*](https://lp.scylladb.com/latency-book-offer) *from ScyllaDB. And learn more from the author Pekka Enberg at the upcoming “*[*Building Low Latency Apps Masterclass*](https://lp.scylladb.com/low-latency-apps-masterclass-register)*” (free and virtual).*

When adding caching to your application, you must first consider your caching strategy, which determines how reads and writes happen from the [cache and the underlying backing store](https://thenewstack.io/cache-vs-database-how-architecture-affects-performance/), such as a database or a service.

At a high level, you need to decide if the cache is passive or active when there is a cache miss. In other words, when your application looks up a value from the cache, but the value is not there or has expired, the caching strategy mandates whether it’s your application or the cache that retrieves the value from the backing store. As usual, different caching strategies have different trade-offs on latency and complexity, so let’s get right into it.

## Cache-Aside Caching

Cache-aside caching is perhaps the most typical caching strategy you will encounter. When there is a cache hit, data access latency is dominated by communication latency, which is typically small, as you can get a cache close by on a cache server or even in your application memory space.

However, when there is a cache miss with cache-aside caching, the cache is a passive store updated by the application. That is, the cache just reports a miss, and the application is responsible for fetching data from the backing store and updating the cache.

Figure 1 shows an example of cache-aside caching in action. An application looks up a value from a cache by a caching key, which determines the data the application is interested in.

If the key exists in the cache, the cache returns the value associated with the key, which the application can use. However, if the key does not exist or is expired in the cache, we have a cache miss, which the application has to handle. The application queries the value from the backing store and stores the value in the cache.

Suppose you are caching user information and using the user ID as the lookup key. In that case, the application performs a query by the user ID to read user information from the database. The user information returned from the database is then transformed into a format you can store in the cache. Then, the cache is updated with the user ID as the cache key and the information as the value. For example, a typical way to perform this type of caching is to transform the user information returned from the database into JSON and store that in the cache.

[![With cache-aside caching, the client first looks up a key from the cache. On cache miss, the client queries the database and updates the cache.](https://cdn.thenewstack.io/media/2025/08/0248b3f6-image2-941x1024.png)](https://cdn.thenewstack.io/media/2025/08/0248b3f6-image2-941x1024.png)

Figure 1. With cache-aside caching, the client first looks up a key from the cache. On a cache miss, the client queries the database and updates the cache.

Cache-aside caching is popular because it is easy to set up a cache server such as Redis and use it to cache database queries and service responses. With cache-aside caching, the cache server is passive and does not need to know which database you use or how the results are mapped to the cache. It is your application doing all the cache management and data transformation.

In many cases, cache-aside caching is a simple and effective way to reduce application latency. You can hide database access latency by having the most relevant information in a cache server close to your application.

However, cache-aside caching can also be problematic if you have data consistency or freshness requirements. For example, if you have multiple concurrent readers that are looking up a key in the cache, you need to coordinate in your application how you handle concurrent cache misses; otherwise, you may end up with multiple database accesses and cache updates, which may result in subsequent cache lookups returning different values.

However, with cache-aside caching, you lose transaction support because the cache and the database do not know each other, and it’s the application’s responsibility to coordinate updates to the data. Finally, cache-aside caching can have significant tail latency because some cache lookups experience the database read latency on a cache miss. That is, although in the case of a cache hit, access latency is fast because it’s coming from a nearby cache server; cache lookups that experience a cache miss are only as fast as database access. That’s why the geographic latency to your database still can matter a great deal even if you are caching, because tail latency is experienced surprisingly often in many scenarios.

## **Read-Through Caching**

Read-through caching is a strategy where, unlike cache-aside caching, the cache is an active component when there is a cache miss. When there is a cache miss, a read-through cache attempts to read a value for the key from the backing store automatically. Latency is similar to cache-aside caching, although backing store retrieval latency is from the cache to the backing store, not from application to backing store, which may be smaller, depending on your deployment architecture.

Figure 2 shows an example of a read-through cache in action. The application [performs a cache lookup](https://thenewstack.io/cache-vs-database-has-performance-converged/) on a key, and if there is a cache miss, the cache performs a read to the database to obtain the value for the key. The cache then updates itself and returns the value to the application. From an application point of view, a cache miss is transparent because the cache always returns a key if one exists, regardless of whether there was a cache miss or not.

[![With read-through caching, the client looks up a key from the cache. Unlike with cache-aside caching, the cache queries the database and updates itself on cache miss.](https://cdn.thenewstack.io/media/2025/08/e9243bd5-image4-1024x1016.png)](https://cdn.thenewstack.io/media/2025/08/e9243bd5-image4-1024x1016.png)

Figure 2. With read-through caching, the client looks up a key from the cache. Unlike with cache-aside caching, the cache queries the database and updates itself on a cache miss.

Read-through caching is more complex to implement because a cache needs to be able to read the backing store, but it also needs to transform the database results into a format for the cache. For example, if the backing store is a SQL database server, you need to convert the query results into a JSON or similar format to store the results in the cache. The cache is, therefore, more coupled with your application logic because it needs to know more about your data model and formats.

However, because the cache coordinates the updates and the database reads with read-through caching, it can give transactional guarantees to the application and ensure consistency on concurrent cache misses. Furthermore, although a read-through cache is more complex from an application integration point of view, it does remove cache management complexity from the application.

Of course, the same caveat of tail latency applies to read-through caches as they do to cache-aside caching. An exception: As active components, read-through caches can hide the latency better with, for example, refresh-ahead caching. Here, the cache asynchronously updates the cache before the values are expired, therefore hiding the database access latency from applications altogether when a value is in the cache.

## **Write-Through Caching**

Cache-aside and read-through caching are strategies around caching reads, but sometimes, you also want the cache to support writes. In such cases, the cache provides an interface for updating the value of a key that the application can invoke. In the case of cache-aside caching, the application is the only one communicating with the backing store and, therefore, updates the cache. However, with read-through caching, there are two options for dealing with writes: write-through and write-behind caching.

Write-through caching is a strategy where an update to the cache propagates immediately to the backing store. Whenever a cache is updated, the cache synchronously updates the backing store with the cached value. The write latency of write-through cache is dominated by the write latency to the backing store, which can be significant. As shown in Figure 3, an application updates a cache using an interface provided by the cache with a key and a value pair. The cache updates its state with the new value, updates the database with the new value and waits for the database to commit the update until acknowledging the cache update to the application.

[![With write-through caching, the client writes a key-value pair to the cache. The cache immediately updates the cache and the database.](https://cdn.thenewstack.io/media/2025/08/c65b4bfa-image1-1024x950.png)](https://cdn.thenewstack.io/media/2025/08/c65b4bfa-image1-1024x950.png)

Figure 3. With write-through caching, the client writes a key-value pair to the cache. The cache immediately updates the cache and the database.

Write-through caching aims to keep the cache and the backing storage in sync. However, for nontransactional caches, the cache and backing store can be out of sync in the presence of errors. For example, if write to cache succeeds, but the write to backing store fails, the two will be out of sync. Of course, a write-through cache can provide transactional guarantees by trading off some latency to ensure that the cache and the database are either both updated or neither of them is.

As with a read-through cache, write-through caching assumes that the cache can connect to the database and transform a cache value into a database query. For example, if you are caching user data where the user ID serves as the key and a JSON document represents the value, the cache must be able to transform the JSON representation of user information into a database update.

With write-through caching, the simplest solution is often to store the JSON in the database. The primary drawback of write-through caching is the latency associated with cache updates, which is essentially equivalent to database commit latency. This can be significant.

## **Write-Behind Caching**

Write-behind caching updates the cache immediately, unlike write-through caching, which defers the database updates. In other words, with write-behind caching, the cache may accept multiple updates before updating the backing store, as shown in Figure 4, where the cache accepts three cache updates before updating the database.

[![With write-behind caching, the client writes a key-value pair to the cache. However, unlike with write-through caching, the cache updates the cache but defers the database update. Instead, write-behind cache will batch multiple cache updates to a single database update.](https://cdn.thenewstack.io/media/2025/08/27a2a049-image3-1024x953.png)](https://cdn.thenewstack.io/media/2025/08/27a2a049-image3-1024x953.png)

Figure 4. With write-behind caching, the client writes a key-value pair to the cache. However, unlike with write-through caching, the cache updates the cache but defers the database update. Instead, write-behind caching will batch multiple cache updates to a single database update.

The write latency of a write-behind cache is lower than with write-through caching because the backing store is updated asynchronously. That is, the cache can acknowledge the write immediately to the application, resulting in a low-latency write, and then perform the backing store update in the background. However, the downside of write-behind caching is that you lose transaction support because the cache can no longer guarantee that the cache and the database are in sync. Furthermore, write-behind caching can reduce durability, which is the guarantee that you don’t lose data. If the cache crashes before flushing updates to the backing store, you can lose the updates.

## **Client-Side Caching**

A client-side caching strategy means having the cache at the client layer within your application. Although cache servers such as Redis use in-memory caching, the application must communicate over the network to access the cache via the Redis protocol.

If the application is a service running in a data center, a cache server is excellent for caching because the network round-trip within a data center is fast, and the cache complexity is in the cache itself. However, last-mile latency can still be a significant factor in user experience on a device, which is why client-side caching is so lucrative. Instead of using a cache server, you have the cache in your application.

With client-side caching, a combination of read-through and write-behind caching is optimal from a latency point of view because both reads and writes are fast. Of course, your client usually won’t be able to connect with the database directly, but instead accesses the database indirectly via a proxy or an API server. Client-side caching also makes transactions hard to guarantee because of the database access indirection layers and latency.

For many applications that need low-latency client-side caching, the local-first approach to replication may be more practical. But for simple read caching, client-side caching can be a good solution to [achieve low latency](https://thenewstack.io/high-performance-on-a-low-budget/). Of course, client-side caching also has a trade-off: It can increase the memory consumption of the application because you need space for the cache.

## **Distributed Caching**

So far, we have only discussed caching as if a single cache instance existed. For example, you use an in-application cache or a single Redis server to cache queries from a PostgreSQL database. However, you often need multiple copies of the data to reduce geographic latency across various locations or scale out to accommodate your workload.

With such distributed caching, you have numerous instances of the cache that either work independently or in a cache cluster. Distributed caching comes with complications and considerations related to replication and partitioning. With distributed caching, you don’t want to fit all the cached data on every instance, but instead have cached data partitioned between the nodes. Similarly, you can replicate the partitions on multiple instances for high availability and reduced access latency.

Overall, distributed caching is an intersection of the benefits and problems of caching, partitioning and replication, so watch out if you’re going with that.

*To keep reading, download the [three-chapter “Latency” excerpt](https://lp.scylladb.com/latency-book-offer) free from ScyllaDB or [purchase the complete book](https://www.manning.com/books/latency) from Manning. Also, you can learn from the author, Pekka Enberg, at the upcoming “[Building Low Latency Apps Masterclass](https://lp.scylladb.com/low-latency-apps-masterclass-register)” (free and virtual).*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/08/df1fe7ce-cropped-fe90b14b-pekka-enberg-.png)

Pekka Enberg is a software professional with a background and experience in operating systems, databases and distributed systems and a research interest in low-latency networked systems. In the past, Pekka has worked on the Linux kernel as a maintainer of...

Read more from Pekka Enberg](https://thenewstack.io/author/pekka-enberg/)