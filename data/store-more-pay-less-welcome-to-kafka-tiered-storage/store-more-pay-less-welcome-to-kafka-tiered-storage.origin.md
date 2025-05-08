# Store More, Pay Less: Welcome to Kafka Tiered Storage
![Featued image for: Store More, Pay Less: Welcome to Kafka Tiered Storage](https://cdn.thenewstack.io/media/2025/05/e359d5fb-tiered-1024x576.jpg)
Longtime [Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/) users are familiar with a fork in the proverbial road as their applications scale and data accumulates and accumulates and accumulates. [Data storage isn’t free](https://thenewstack.io/battling-the-steep-price-of-storage-for-real-time-analytics/), and eventually, the moment of truth arrives when you have to decide to either hang on to all your historical data or keep your storage costs realistic.

The arrival of [Kafka’s Tiered Storage](https://kafka.apache.org/39/documentation/#tieredstorageconfigs) eliminates that dilemma with a third option: Why not both?

With Tiered Storage, the popular open source distributed event streaming platform now lets you automatically split data into two tiers: one that delivers high performance by storing recent and crucial hot data locally and another that places historical data in low-cost cloud object storage.

Tiered Storage transforms the way organizations can tap Kafka at scale, enabling new use cases while simplifying operations and ensuring longer-term data consistency. Here’s how it works and why it’s a game-changer for every data-hungry Kafka deployment.

## Cut Costs While Saving Business-Valuable Data
Kafka Tiered Storage preserves the platform’s core semantics and APIs, allowing existing applications and their Kafka producers and consumers to function without modification. The architecture functions as a write-through cache. Data initially lands on local storage before being asynchronously copied to remote storage once segments close. Consumers seamlessly read from either local or remote storage as needed, with the underlying complexity completely abstracted away.

As organizations grow, their data accumulation accelerates and eventually reaches a point where simply expanding broker storage becomes financially unsustainable. [Cloud object storage](https://thenewstack.io/object-storage-is-key-to-taming-cloud-costs/) costs a fraction of high-performance SSDs, making the economic case for tiered storage immediately compelling to financial stakeholders (in other words, Kafka Tiered Storage is going to make your CFO happy). Meanwhile, technical teams gain powerful new capabilities for historical data analysis and reprocessing that were previously cost-prohibitive.

## Building a Better Time Machine
While Kafka has always enabled enterprises to “time travel” through their data streams, unlocking critical insights and capabilities, the high cost of historical data retention has severely limited this functionality’s scope until now.

Kafka Tiered Storage makes extended time travel across years of historical data economically viable, opening up transformative opportunities. Teams can now train machine learning (ML) models on complete historical data sets rather than samples, execute seamless migrations to new sink systems and perform comprehensive compliance auditing across all past transactions.

This functionality also helps modernize application development practices. Engineering teams can address bugs by reverting to the exact state before they were introduced, even months after the fact. Applications can undergo thorough A/B testing using parallel processing pipelines against historical data.

Time-shifted operations, such as running accurate what-if simulations with historical operational data, have now become practical use cases. Even disaster recovery strategies evolve as organizations replace expensive hot infrastructure duplicates with far more affordable cold data storage that can be rapidly deployed on new Kafka clusters when needed.

## Managing Tiered Performance and Right-Sizing Capacity
Tiered storage means maintaining seamless high-performance access to mission-critical data. That said, a few smart adjustments can optimize performance when accessing historical data in cold cloud storage as well.

Retention policies should be a microcosm of your tiered storage strategy, keeping often-accessed data locally and using remote storage for less commonly needed data. That remote copying occurs asynchronously, meaning that Kafka producers will function the same as always. However, you should increase cluster CPU and network resources by around 10% to better perform those tiering operations.

Kafka Tiered Storage also changes the equation when planning how much capacity to make available. According to NetApp Instaclustr’s benchmark data, reads from hot local storage are often two or three times as fast as from remote cloud storage, with up to 20x degradation with small segment sizes. To maintain the correct capacity, separate workloads and determine your producer input rate, consumer patterns and data to store locally.

Looking at access patterns, rather than total volume, will help to right-size local retention. Size topics to best serve the parallel processing required for performant access to cloud-stored data, keeping in mind that the partition count greatly affects read performance. Increasing partitions for those topics processing historical data will increase cold storage throughput by enabling more consumers to read data concurrently. If you want to go deep into Kafka Tiered Storage sizing, my Instaclustr colleague Paul Brebner [has you covered](https://www.instaclustr.com/blog/how-to-size-apache-kafka-clusters-for-tiered-storage-part-1/).

## Kafka’s Evolutionary Leap Forward
Kafka Tiered Storage represents the first step in Kafka’s evolution toward invisible infrastructure, freeing development teams from storage management concerns to focus on business logic and application development. By automating the complex decisions around data retention and placement, Tiered Storage allows enterprises to concentrate on extracting value from their data rather than managing its underlying infrastructure.

Future Kafka releases will likely continue this trajectory, further automating operations while optimizing to meet organizations’ increasingly sophisticated data management requirements and rapidly scaling demands.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)