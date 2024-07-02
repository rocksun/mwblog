# How To Manage 45 Billion Client Records With Aerospike
![Featued image for: How To Manage 45 Billion Client Records With Aerospike](https://cdn.thenewstack.io/media/2024/06/c91ac4d6-aerospike-storage-06-adjust-1024x591.png)
When your operations outgrow the capabilities of a single database, what are your options?

For the Berlin-based mobile measurement service provider [Adjust](https://www.adjust.com/), the answer came with [Aerospike](https://aerospike.com?utm_content=inline+mention), a real-time, high-performance NoSQL key-value store that can be run across multiple data centers.

At Aerospike’s [Real-Time Data Summit](https://www.realtimedatasummit.com/) last week, Adjust Senior Software Engineer [Bubunyo Nyavo](https://www.linkedin.com/in/bubunyonyavor/?originalSubdomain=de), explained how the company used Aerospike to help clients track their return on investment of their marketing channels.

Adjust’s service can generate 52 million requests every minute on average. These requests can set off the need for an operation of some sort, such as a query, and, of course, to reconcile state. A customer may post material on Meta, LinkedIn, or some other social media outlet, and the Adjust gathers the number of people who viewed the content and how many clicked on it

“Depending on what operation it is, we fetch some data, we write some data. Sometimes we write in batches, sometimes delete data, and then we return a response for these requests,” Nyavor said.

Overall, the company keeps about 45 billion records in [Aerospike](https://thenewstack.io/from-db2-to-real-time-with-aerospike-founder-srini-srinivasan/), and these are just recording the states of devices. With an average of 512 Bytes per record, these results in 351TB worth of data.

The data is stored in three separate three separate clusters, located in geographically-dispersed data centers. Each cluster has 64 nodes and runs on bare metal, with [Gentoo Linux](https://www.gentoo.org/) serving as the operating system. Each server has about 400GB of RAM and 16TB of solid-state of [NVMe disk space](https://thenewstack.io/why-nvme-is-a-better-choice-for-your-data-center/), and a 10 Gigabit network card. Either two or three copies of the data are kept as backup.

“So that if single rack goes offline, it doesn’t send us into a tailspin,” Nyavor said.

![A chart showing the average number of devices connecting to Aerospike.](https://cdn.thenewstack.io/media/2024/06/498a9684-aerospike-storage-06-adjust-05-1024x587.png)
A chart showing the average number of devices connecting to Aerospike.

## Beyond Key-Store Values
The Aerospike key-value store [was launched](https://thenewstack.io/from-db2-to-real-time-with-aerospike-founder-srini-srinivasan/) in 2009 (originally as CitrusLeaf) and quickly found an audience in the online advertising industry for storing and subsequently analyzing customer [cookies at rapid speed](https://thenewstack.io/improving-price-performance-lowers-infrastructure-costs/).

Subsequent releases [expanded the analytics](https://thenewstack.io/aerospike-gets-sql-powered-by-starburst/), [incorporated batch processing](https://thenewstack.io/latest-aerospike-update-supports-large-scale-data-models/), and introduced [secondary indexes and cross-data center replication](https://thenewstack.io/aerospike-database-6-secondary-index-queries-json-and-more/).

At the Real-Time Data Summit, Aerospike Senior Developer Experience Engineer [Art Anderson](https://www.linkedin.com/in/artdanderson/) discussed how Aerospike could also do graph and vector data formats, which can help online shops easily build out recommendation systems.

For Adjust, low latency was critical. Customers wanted data updated as close to real-time as possible. This is a challenge given the cross-cluster communications.

As with any distributed system with duplicate data, Adjust must trade-offs between consistency and availability of the data (two of the three pillars of the [CAP Theorem](https://thenewstack.io/acid-transactions-change-the-game-for-cassandra-developers/)).

In a consistent mode, accurate data will always be delivered, though it may take some time. In an availability-oriented mode, data will be returned to the requester as quickly as possible, though it may not include the most recent changes (as it takes to propagate new data across different clusters).

![Operational modes of Aerospike: Consistency and Available.](https://cdn.thenewstack.io/media/2024/06/e736a74e-aerospike-storage-06-adjust-01-1024x581.png)
Operational modes of Aerospike: Consistency and Available.

“You will get fast responses but there’s no guarantee on the freshness of the data,” Nyavor explained, especially since Adjust writes a lot more data to disk than reads it.

There are several tools that help. Aerospike offers an [intelligent client driver](https://download.aerospike.com/download/client/) that knows which nodes on a cluster to send the requests to. The database system also allows Adjust to store secondary indexes on the speedy solid-state hard drives, an advantage given that it would be cost-prohibitive to store them on the server’s own main memory.

“Aerospike does sufficiently well to be able to help us take advantage of cheaper hardware,” Nyavor said.

Overall, the system can do, on average about 1.2 million write operations per second, and 2 million *get* operations per second.

![Aerospike operations per second at Adjust.](https://cdn.thenewstack.io/media/2024/06/ea38688d-aerospike-storage-06-adjust-02-1024x579.png)
Aerospike operations per second at Adjust.

About 50% of all requests take less than 500 milliseconds or less, an impressive feat given the vastness of the database itself, Nyavor said.

![Aerospike operations under 500 milliseconds (Chart).](https://cdn.thenewstack.io/media/2024/06/6c50f4d1-aerospike-storage-06-adjust-03-1024x590.png)
Aerospike operations under 500 milliseconds.

Scanning is one of the larger operations. It is necessary to delete user records, when requested or when a customer leaves the program. Scanning an entire cluster takes about three days.

“It is a slow and intensive process because it takes a lot of resources to scan,” he said. The good news is that Aerospike can run the scan operations as a background task, temporarily suspending them when reads and writes are needed to be executed.

## How Aerospike Is Upgraded
There is still work on Aerospike that needs to be done, according to Nyavor.

For instance, the upgrade process is still pretty manual-intensive.

The process involves going through the change log to ensure nothing has been broken in the upgrade process.

But overall, the database is very configurable, and you need to understand all the options to get the most out of it, Nyavor said.

And if you don’t know something, ask. The Aerospike support team has been really helpful in answering questions, he added.

“Don’t take anything in the documentation that you don’t understand for granted, because it can snowball and bite you in the ass,” he said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)