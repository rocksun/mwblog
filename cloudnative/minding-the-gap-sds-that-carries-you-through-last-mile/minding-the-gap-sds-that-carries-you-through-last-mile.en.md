Data center modernization is inevitable to keep pace with today’s performance-intensive workloads, which are growing especially rapidly in the financial services and e-commerce sectors.

[Software-defined storage (SDS)](https://thenewstack.io/modernization-storage-strategies-for-the-cloud-era/) offers the promise of greater agility, scalability and reduced costs, making it a compelling part of the platform architect’s vision of a streamlined, software-driven infrastructure.

A common priority for modernization is retiring traditional Fibre Channel (FC) SANs, which are perceived as legacy and complex. While still adequate for many application workloads, performance gaps exist in SDS block storage solutions that are engineered into legacy FC SANs, which cannot support the organization’s mission-critical application workloads.

Once reserved as the primary storage tier for traditional workloads, [block storage](https://www.lightbitslabs.com/blog/4-reasons-why-block-storage-is-gaining-momentum-in-the-enterprise/utm_source=TNS&utm_medium=article&utm_campaign=july) is evolving into a critical component of high-performance, accelerated data pipelines that propel businesses forward. Platform architects at the most innovative, fast-moving organizations are seeking to close the “last mile” gap for their critical workloads and eliminate the block storage bottlenecks of FC SAN, ultimately realizing their transition to a fully software-defined data center.

## The Promise and Reality of SDS

While some aspects of FC SAN management may involve software tools, the fundamental architecture and reliance on dedicated hardware significantly differentiate them from true SDS. SDS is about decoupling storage services from the underlying physical hardware, and FC SANs do not adhere to this core principle.

True SDS offers a compelling alternative to FC SAN. Its benefits are numerous, including hardware independence and greater flexibility, simplified management and automation through software control, as well as improved scalability and elasticity. SDS promises cost-effectiveness by leveraging commodity hardware and reducing vendor lock-in.

Open source [Ceph Storage](https://www.lightbitslabs.com/blog/ceph-storage/utm_source=TNS&utm_medium=article&utm_campaign=july) is widely used in data centers, demonstrating the viability of SDS solutions for a significant portion of enterprise workloads. Indeed, it’s proven successful for many applications, handling as much as two-thirds of an organization’s application workload storage needs. However, the remaining one-third — those applications with high-performance requirements at scale — often present a formidable challenge and the hurdle in the last mile to the platform architect’s total software-defined modernization vision.

## Identifying the Performance Bottleneck

Legacy block storage systems cannot support the various types of mission-critical applications commonly encountered in financial services and e-commerce.

These include high-transaction, low-latency applications, such as databases supporting financial trading platforms; I/O-intensive workloads, such as large-scale data analytics and real-time processing systems; and online transaction applications requiring consistent and predictable performance, where even brief spikes in latency can have significant consequences.

[Ceph Storage](https://www.lightbitslabs.com/blog/ceph-storage/?utm_source=TNS&utm_medium=article&utm_campaign=july) is an SDS system that offers file, block and object storage, serving as a replacement for traditional FC SANs. However, many organizations adopt Ceph primarily for its object storage capabilities and opt for other options for their block storage needs.

The block storage architecture limits its ability to support performance-intensive mission-critical workloads at scale. Here’s why: Originally intended for spinning hard disk drives (HDDs), Ceph has evolved its architecture incrementally over the past decade to take advantage of advances in flash storage. Recent versions of the software use solid-state drives (SSDs) for metadata operations, improving performance. However, many core design elements optimizing HDD behavior remain unchanged.

Ceph recently integrated [NVMe (Non-Volatile Memory Express)over TCP](https://www.lightbitslabs.com/nvme-over-tcp/utm_source=TNS&utm_medium=article&utm_campaign=july) connectivity. The implementation involves integrating Ceph’s NVMe-oF (NVMe-over Fabric) gateway. Figure 1 illustrates how the gateway exports RADOS Block Devices (RBD) to clients over NVMe/TCP. This implementation can increase storage networking latency caused by the extra hop and protocol translation. This model may improve Ceph’s interoperability, but it deviates from the originally intended design of NVMe/TCP fabric architectures.

[![Source: IBM Storage Ceph product documentation](https://cdn.thenewstack.io/media/2025/07/484e9ed8-image1.png)](https://cdn.thenewstack.io/media/2025/07/484e9ed8-image1.png)

Source: IBM Storage Ceph product documentation

For truly extreme I/O-intensive workloads, [NVMe-oF solutions](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/) offer significantly lower latency and higher IOPS compared to traditional Ethernet-based SDS. While

Ceph can leverage NVMe drives, but it doesn’t offer the same level of direct NVMe fabric optimization as dedicated NVMe-oF solutions.

Software overhead inherent in FC SAN architectures, including data virtualization and distributed storage management, introduces latency. Achieving consistent low latency with distributed storage across a network is inherently more complex.

Potential limitations of the underlying hardware, such as network bandwidth and SSD performance, can also become bottlenecks, especially under heavy load. While generally minimal, this overhead can become a significant performance factor when dealing with extremely high IOPS and low latency requirements at scale.

This performance differential creates a significant hurdle for organizations seeking to fully transition to SDS.

## The Last Mile Struggle — Real-World Scenarios

To drive this point home, let me walk you through two real-world scenarios.

A financial services organization aimed to replace its FC SAN with SDS to achieve better agility and cost efficiency. It successfully migrated many applications to the new SDS system.

However, its high-frequency trading platform, a critical revenue-generating application, could not be migrated. It required a block storage solution that could deliver sub-millisecond latency and millions of IOPS, performance levels that the new SDS solution could not consistently guarantee. The organization’s workaround was to maintain a portion of its FC SAN infrastructure specifically for this application, negating the goal of a fully software-defined data center.

The performance gap, in this case, represented the difference between successful trade execution and potential financial losses. To achieve the final vision, it replaced the legacy FC SAN with natively designed [NVMe over TCP block storage](https://www.lightbitslabs.com/utm_source=TNS&utm_medium=article&utm_campaign=july) and successfully cleared the last hurdle in its software-defined modernization.

A rapidly growing e-commerce platform used a popular block SDS for the majority of its storage needs, including website hosting and product catalogs.

However, its real-time inventory management system, crucial for accurate order fulfillment and preventing overselling, presented a significant performance challenge. The SDS solution struggled to deliver the required read/write latency and throughput. This storage bottleneck resulted in occasional delays in inventory updates, leading to order fulfillment issues and customer dissatisfaction.

To clear the hurdle, the organization augmented its Ceph storage, which it continues to use for less-critical data, with a high-performance NVMe-based block storage tier for the inventory database. This augmentation model optimized its SDS configuration to enhance performance while maintaining adherence to their software-defined strategy.

## Clear the Hurdle: Strategies and Solutions

Several strategies and solutions can help bridge the performance gap in SDS. Using NVMe and other high-performance storage technologies, both within the SDS cluster and as a separate tier, can address I/O bottlenecks. Investigating emerging NVMe-based SDS architectures and technologies designed specifically for higher performance, such as disaggregated storage and computational storage, is also crucial.

For truly extreme I/O-intensive workloads, [NVMe-oF solutions](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/) offer significantly lower latency and higher IOPS compared to traditional Ethernet-based SDS. While Ceph can leverage NVMe drives, it doesn’t offer the same level of direct NVMe fabric optimization as dedicated NVMe-oF solutions. Its implementation deviates from the originally intended design of NVMe/TCP fabric architectures, and therefore, its block storage component is not ideal for mission-critical application workloads at scale.

A holistic approach is essential, considering application requirements, infrastructure capabilities and cost implications. There is no one-size-fits-all solution. You must carefully evaluate your specific needs and choose the approach that best balances performance, cost and manageability.

The realization of a fully software-defined data center is often diminished by the challenges of block storage capabilities inherent in legacy systems and FC SANs. As you’ve seen here, there are a significant number of application workloads perfectly suited to legacy solutions, but fall short of meeting the performance demands of certain I/O intensive applications.

This “last mile” performance gap can be overcome with modern NVMe over TCP-based block storage solutions. It’s a technology with the promise of closing the performance gap completely, enabling organizations to fully realize the vision of a software-defined data center.

If you want to learn more about software-defined NVMe/TCP-based storage and its transformative benefits for data center modernization, download this IDC white paper: “[NVMe Over TCP Enables the Democratization of Disaggregated, NVMe Storage](https://www.lightbitslabs.com/idc-research-nvme-over-tcp-democratizes-nvme-storage/?utm_source=TNS&utm_medium=article&utm_campaign=julyutm_source=TNS&utm_medium=article&utm_campaign=july).”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/01/775818af-carolplatz.jpg)

Carol Platz brings over 25 years of technology evangelism and marketing leadership for high-performance data storage solutions to her role as vice president of marketing at Lightbits. Prior to joining the company, she directed marketing for storage startups like WekaIO,...

Read more from Carol Platz](https://thenewstack.io/author/carol-platz/)