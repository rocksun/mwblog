# Object Store Apps: Cloud Native’s Freshest Architecture
![Featued image for: Object Store Apps: Cloud Native’s Freshest Architecture](https://cdn.thenewstack.io/media/2025/02/660865a8-steps-3614468_1280-1024x682.jpg)
Perhaps even for the first time since 2006 when [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) had launched its [Simple Storage Service ](https://aws.amazon.com/pm/serv-s3)(s3), object storage is hot again.

An increasing number of start-ups and end-users find that using cloud object storage as the persistence layer saves money and engineering time that would otherwise be needed to ensure consistency.

Cheap object storage fuels the recent [open data format war ](https://thenewstack.io/showdown-at-the-lakehouse-databricks-muscles-up-with-tabular/)between Delta Lake and Apache Iceberg, as both rely on object stores to allow customers build out the much requested open data formats for analysis.

And object storage was also the secret behind the success of WarpStream, which used the technology to pioneer a new, much more cost-effective way of running Kafka.

Chief Kafka distribution provider [Confluent](https://www.confluent.io/?utm_content=inline+mention) took notice and bought the company. And Confluent competitor [Redpanda](https://redpanda.com/?utm_content=inline+mention) also uses the technology[ in a completely different way](https://thenewstack.io/how-to-introduce-real-time-data-predictions-with-redpanda/), to speed Kafka transactions through a tiered architecture.

“People have been asked me, like, why are you doing a talk on object storage, and why now? And isn’t that a bit boring?” admitted [Docker](https://www.docker.com/?utm_content=inline+mention) CTO [Justin Cormack](https://github.com/justincormack), in a talk, entitled “[Object Storage Is All You Need](https://www.youtube.com/watch?v=ei0wwTy6_G4),” at KubeCon+CloudNativeCon NA 2024.

“But what’s happened in the last few years is that people have started building real applications using object storage as the only back end. There’s been a lot of these, and they’ve been really interesting,” Cormack subsequently told TNS.

Start-ups are taking advantage of object storage as a persistent layer upon which they can build their applications. This approach sorts out all the tricky engineering issues such as managing concurrency and state, not to mention backups and redundancy.

Object storage means “infinite cheap storage,” he told TNS. And that is perfect for [cloud native development](https://thenewstack.io/cloud-native/). “Anything that is bounded is annoying for developers.”

It’s also been used to build databases, observability platforms, virtual disks and who knows what else?

“There’s a solution for almost every type of storage that you may need that uses object storage,” added [Keith Pijanowski](https://www.linkedin.com/in/keithpij/), an AI solutions engineer from [MinIO](https://min.io/?utm_content=inline+mention), which offers an [S3-like open source object store](https://min.io/product/overview) file system for enterprise use.

## High Latency, High Throughput
When coming up [with the idea](https://press.aboutamazon.com/2006/3/amazon-web-services-launches) of S3, Amazon head Jeff Bezos specified that he wanted “a `malloc`
for the Web.” This C programming language call allows provides a way for developer to allocate memory with a single line. The idea with S3 is that it should make it just as easy for cloud developers to easily allocate storage.

That said, S3, and object storage in general, has some performance characteristics that developers should know about. In other words, you have to know how to use it.

Object storage can infinitely scale, or if you are using an in-house version such as MinIO it is limited only by the physical storage it runs on.

![](https://cdn.thenewstack.io/media/2025/01/73a5be2e-justin-cormack-2-300x225.jpg)
Justin Cormack

Architecturally, an object store is basically a key value store accessible by an http API. But it is [non-POSIX](https://thenewstack.io/google-cloud-offers-posix-compliant-file-storage-red-hat-gluster/). It is not a full-featured file system. It has some file listing capability but few other interface commands. The biggest downside is that object files can not be updated incrementally. One change and the whole file must be updated.

Highly parallel, objects stores nonetheless have some latency, though they can be scaled up through greater parallelism.

You can run a single connection on AWS that from that will achieve 5 Gib throughput, *but* you can have as many connections as you want.

With a service like AWS S3, objects stores are replicated across availability zones, so you get replication, consistency and backup for free. As far as reliability, it offers 99.999999999% (“eleven nines”) of uptime, for up to 280 trillion objects.

And, object storage is by and large, cheap. Cheap to store data, cheap to network. Because it is simple to use, you can can write a really simple program that uses it.

“Having simple primitives allows you to invest into making them reliable. That gives you the assurance that you can safely build applications on them,” Cormack said.

## Good News for Databases
Over time, the S3 API became the de facto standard interface for object storage, paving the way for MinIO and [Ceph](https://thenewstack.io/ceph-20-years-of-cutting-edge-storage-at-the-edge/) and other implementations.

The original use case for object storage seemed to be chiefly for Web sites, which by and large were updated page by page. But further uses cases pushed the need for parallelism, which meant who writes what must be managed.

One favored approach to manage concurrency was to use a database, such as DynamoDB, to manage the concurrency. This is the approach that Docker takes with Docker Hub.

“It gives you a mutual exclusion concurrency primitive you can use to have multiple applications write something.

One big jump for app developer ease was [the 2024 addition](https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-s3-conditional-writes/) of a new command to the S3 interface to write an object if it doesn’t already exist (PUT with IF-NONE-MATCH), which is now supported by [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html), [Minio](https://github.com/minio/minio), and [Cloudflare R2](https://developers.cloudflare.com/r2/).

An application that could use this command to create as series of ordered files 001, 002, 003, etc. If there are more than one server writing files, then the files are still numbered incrementally on a first-come-first-serve basis.

In effect, these sequential files [can be a log](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying), a fundamental primitive for a database. This allows you to use the object store itself rather than a separate database to concurrency.

## Open Data Wars
“You can build any storage system from the logs,” Cormack said. These could be write-ahead logs, or commit logs, or transaction logs,

Apache Delta Lake [uses this primitive](https://dl.acm.org/doi/10.14778/3415478.3415560) to create acid-compliant data storage, and Apache Iceberg relies on object storage as well. Last year saw a big rush of customers to move to one or the other of these open formats, as a way to [keep their data in an open format](https://www.dremio.com/why-dremio/). Both use [Parquet files for tables](https://thenewstack.io/an-introduction-to-apache-parquet/).

Phil Eaton [offers an example](https://notes.eatonphil.com/2024-09-29-build-a-serverless-acid-database-with-this-one-neat-trick.html) of how to build a Delta Lake-based database using the [Go programming language](https://thenewstack.io/introduction-to-go-programming-language/).

“There’s a whole lot of nice properties that these things have that are fun for the developer,” Cormack said.

## ‘Bring Your Own Bucket’
WarpStream is a Kafka data store compatible implementation built on S3, one that [promises “zero disk” management and infinite scalability](https://www.warpstream.com/bring-your-own-cloud-kafka-data-streaming). The company was [recently acquired](https://thenewstack.io/with-warpstream-confluent-got-a-new-type-of-kafka-platform/) by Confluent, who subsequently offers it as its “Bring Your Own Cloud,” service

RedPanda touts faster throughput than [Confluent’s premium Kafka cloud offering](https://www.confluent.io/lp/confluent-cloud), in part by using SSDs as a caching layer and then offloadingg the final results to S3.

WarpStream went the other way, offering a slower service but one that was *way less* expensive to run.

Turns out, many users were didn’t mind a bit of latency for lower operating costs. Many apps just didn’t need the super-low latency.

Secret sauce: WarpStream was built on S3.

With AWS, you don’t have to pay for traffic across availability zones, so WarpStream’s genius was to use this to cut the costs of sending Kafka messages across availability zones, completely eliminating the cross-zone fees that using something like EBS would cost.

“It’s was the cheapest possible way of running Kafka,” Cormack noted.

Also, WarpStream offered a simple service model: Customers would manage their own S3 buckets, and WarpStream provided a control plane.

“It’s operationally very, very simple to manage because it’s just object storage and statements compute,” Cormack told TNS.

## Other Innovative Uses of Object Storage
A look around the ecosystem finds many other innovative uses of object storage.

An open source project for [virtual disks](https://dl.acm.org/doi/10.1145/3492321.3524271) uses the technology. To build scale-out disks, the researchers use a SSD for cache and then changes are sent to S3 as logs.

Theoretically, it could be a [cheaper alternative](https://github.com/asch/dis) to Amazon Elastic Block Storage (EBS).

[SlateDB](https://thenewstack.io/slatedb-bottomless-databases-built-on-cloud-object-stores/), a key-value store, takes advantage of this architecture. It has high write latency but offers full persistence and is infinitely scalable.
[TurboPuffer](https://turbopuffer.com/) is a [vector database](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/) built on object storage.
Because the object store does all the work of ensuring reliability, developers can just attach ephemeral components to build cloud native applications.

In the cloud native world, reliability is usually defined as having lots of pods. But if you build a database, ensuring persistence becomes a major part of the job, “but all those things are done for you if you use an object store,” Cormack said.

“You end up with a very different reliability story.”

## Bring Your Own Bucket
[Matt Klein](https://thenewstack.io/matt-klein-on-the-success-of-envoy-and-the-future-of-the-service-mesh/), of the [Envoy proxy fame](https://thenewstack.io/tetrate-bloomberg-collaborate-on-envoy-based-ai-gateways/), created [BitDrift](https://bitdrift.io/), for cutting the costs of observability through object storage with a “[bring-your-own-bucket](https://thenewstack.io/why-you-might-bring-your-own-s3-bucket-byob-to-the-observability-party/)‘ approach.
This has also been called, more genially, “[bring-your-own-cloud](https://thenewstack.io/should-you-bring-your-own-cloud/),” a term that WarpStream uses, [as does Buildkite](https://thenewstack.io/should-you-bring-your-own-cloud/) for its continuous delivery platform, which speeds testing but runs them in parallel.

“You can’t run one test after another. Otherwise, it would take weeks, months, years, and even some cases, to run tests sequentially. So you have to paralyze you have to run them concurrently,” Buildkite CEO Keith Pitt told TNS.

## You Don’t Need a Raft
Further possibilities abound.

It can be used to [do leader elections](https://www.morling.dev/blog/leader-election-with-s3-conditional-writes/) for cloud native apps.

“What you notice is that you don’t have to build a lot of distributed system primitives because you already got this consistent backend you can use,” Cormack said. “You got a concurrency primitive you can really build things on top of it.”

Any of the [Landscape technologies](https://landscape.cncf.io/) of the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) that require a [Raft implementation](https://thenewstack.io/raft-native-the-foundation-for-streaming-datas-best-future/) (Vitess, etcd) for load balancing and concurrency would be good candidates for rewriting to run on object storage, Cormack noted.

“You don’t have to do those things if you can avoid them,” Cormack said. “Building a persistence layer on object storage meaning you don’t have to do that.”

“It’s a really attractive option if you building something that involves data, which is pretty much everything,” Cormack said.

## Object Storage at Home
And while many of the applications were built on Amazon S3 — or other cloud object stores such as [DigitalOcean Spaces](https://www.digitalocean.com/products/spaces), [Azure Blob Storage](https://news.microsoft.com/?utm_content=inline+mention) and [Google Cloud Storage](https://cloud.google.com/?utm_content=inline+mention) the architecture can also be used in-house, MinIO’s Pijanowski noted.

MinIO has partnerships with [Dremio](https://www.dremio.com/why-dremio/) and [StarBurst](https://www.starburst.io/), offering customers to easily set up data warehouses on premises with unlimited scaling capability. For alternatives to cloud Kubernetes deployments, the company has also partnered with VMware for those wishing to build private deployments with [VMware Cloud Foundation](https://thenewstack.io/vmwares-private-cloud-shift-under-broadcom/).

The object store, once a somewhat niche technology, is now becoming a fundamental building block of the modern cloud, leading to a new wave of cloud native applications that are faster to develop, easier to maintain, and more cost-effective to run.

Cormack’s full talk can be enjoyed here:



[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)