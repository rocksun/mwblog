# NVMe-oF Substantially Reduces Data Access Latency
![Featued image for: NVMe-oF Substantially Reduces Data Access Latency](https://cdn.thenewstack.io/media/2025/01/d1585232-light1-1024x574.png)
[DongIpix](https://www.shutterstock.com/g/Phantip+Tritreemak)on Shutterstock
Modeling hyperscaler cloud architecture is gaining significant momentum in enterprise data centers as many IT teams are repatriating their public cloud workloads back on premises, modernizing their data center for cloud native workloads or building their own specialized public cloud services. They want to integrate the best capability and efficiency aspects of the public cloud with on-premises control. Several key benefits of the public cloud are driving data-center requirements, which include efficiency, scalability, flexibility, automation and agility.

Technological innovations have emerged as key enablers of best-of-breed cloud architecture to achieve the benefits promised by the public cloud, which are [software-defined storage](https://thenewstack.io/a-cloud-architects-guide-to-e-commerce-data-storage/), open source orchestrators such as [Kubernetes](https://thenewstack.io/kubernetes/), and NVMe-oF (Nonvolatile Memory Express Over Fabrics). All are gaining popularity as foundational components of modern cloud architecture.

## What Is NVMe-oF?
The NVMe-oF v1.0 specification was released in June 2016. NVMe-oF is a network protocol that extends the parallel access and low latency features of Nonvolatile Memory Express (NVMe) protocol across networked [storage](https://thenewstack.io/storage/). Originally designed for local storage and common in direct-attached storage (DAS) architectures, [NVMe](https://thenewstack.io/how-nvme-will-propel-innovations-in-artificial-intelligence/) delivers high-speed data access and low latency by directly interfacing with solid-state disks. NVMe-oF allows these same advantages to be achieved in distributed and clustered environments by enabling external storage to perform as if it were local.

NVMe-oF supports various transport protocols, including Fibre Channel, InfiniBand, remote direct memory access (RDMA), Ethernet with RoCE v2, iWARP and Transmission Control Protocol (TCP). By using these protocols, NVMe-oF enables you to scale your storage without compromising performance, making it ideal for modern data-intensive workloads. It addresses use cases where high performance is critical.

![](https://cdn.thenewstack.io/media/2025/01/4af93ddc-image3-775x1024.png)
Source: Lightbits Labs

## How Is NVMe-oF Transforming Data-Center Storage?
While still relatively adolescent in its market penetration (5-20%, according to Gartner’s Hype Cycle for Storage Technologies, 2024), given all the technological and business benefits it offers, I expect that it will gain momentum as the main Tier-1 cloud storage connectivity. Early adopters of NVMe-oF are already reaping its benefits to their competitive advantage.

NVMe-oF substantially reduces data-access latency while ensuring more efficient connectivity between storage and servers. Storage targets can be dynamically shared among workloads, thus providing composable storage resources that provide flexibility, agility and greater resource efficiency.

The adoption of NVMe-oF is evident across industries where high performance, efficiency and low latency at scale are critical. Notable market sectors include: financial services, [e-commerce](https://thenewstack.io/a-cloud-architects-guide-to-e-commerce-data-storage/), AI and machine learning, and specialty cloud service providers (CSPs).

Legacy VM migration, real-time analytics, high-frequency trading, online transaction processing (OLTP) and the rapid development of cloud native, performance-intensive workloads at scale are use cases that have compelled organizations to modernize their data platforms with NVMe-oF solutions. Its ability to handle massive data flows with efficiency and high-performance makes it indispensable for I/O-intensive workloads.

The blazing speed and efficiency of [NVMe over TCP](https://www.lightbitslabs.com/nvme-over-tcp/?utm_source=TNS&utm_medium=article&utm_campaign=feb) (NVMe/TCP) makes it a promising cloud storage protocol for today’s performance-sensitive workloads at scale. It offers cloud-like simplicity, leveraging standard Ethernet, with an invisible fabric for a distributed storage network while maintaining high reliability and durability, as well as high performance and low latency requirements.

## What Is NVMe over TCP?
Technological advancements like NVMe/TCP can induce a paradigm shift in data-center architecture. NVMe/TCP, as a subset of NVMe-oF, combines the high performance of NVMe with the ubiquity and cost-efficiency of standard Ethernet networks using TCP as its transport layer.

Unlike alternatives like Fiber Channel (FC) or RDMA-based protocols, NVMe/TCP operates over ubiquitous and cost-effective Ethernet infrastructure. This architecture model ensures ultra-low latency and high throughput without custom hardware or proprietary drivers.

NVMe/TCP is ideally positioned to replace iSCSI (Internet Small Computer Systems Interface) and FC and become the de facto standard for data-center modernization and the underlying storage access protocol to support cloud native applications with a thirst for higher performance.

Technological innovations like NVMe/TCP have accelerated the adoption of NVMe by reducing the cost and complexity of deploying NVMe-oF. Developed by [Lightbits Labs](https://www.lightbitslabs.com/?utm_source=TNS&utm_medium=article&utm_campaign=feb) and donated to the Linux community, it is the next evolution of using [NVMe storage](https://www.lightbitslabs.com/nvme-over-tcp/?utm_source=TNS&utm_medium=article&utm_campaign=feb) over TCP Fabric.

Off-the-shelf, [software-defined storage](https://www.lightbitslabs.com/solution-guide/software-defined-storage/?utm_source=TNS&utm_medium=article&utm_campaign=feb) versions are easy to manage with latency as low as 170 microseconds while supporting up to 6 million IOPS with just two nodes. The ability to deploy the storage software on hardware of your choosing and use your existing Ethernet infrastructure makes it accessible and cost-effective for organizations looking to modernize their data-center systems or to replace their legacy FC infrastructure.

![](https://cdn.thenewstack.io/media/2025/01/0f06d116-image1-1024x267.png)
Source: Lightbits Labs

## 3 Business and Technological Benefits of NVMe-oF
NVMe-oF can transform the way modern storage systems are architected and used.

Here are three business benefits:

**1. Consolidation of Storage Resources for Better Efficiency**
With NVMe-oF, you can consolidate and share high-speed storage across multiple servers, reducing storage silos and maximizing resource utilization. Doing so can reduce CapEx and OpEx by eliminating the need to overprovision storage and infrastructure management resources.

By using ubiquitous Ethernet, NVMe/TCP delivers the best cost-efficiencies of all the network protocol options. This is a particularly ideal scenario for cloud service providers who can pass on savings to customers.

Offering faster storage services at competitive prices can be an advantage. It’s also an ideal scenario for companies looking to replace a virtual storage area network (vSAN). By eliminating overprovisioned storage, you can reduce your storage footprint by as much as 25%, cut energy costs and free up rack space in your data center.

**2. Low Latency and High Throughput for Accelerated Performance **
The ultra-low latency and high throughput benefits of NVMe-oF are unequaled. Fast access to big data accelerates application performance, time to market and time to answers, which are critical for real-time analytics, AI/machine learning workloads and high-frequency trading.

For this reason, early adopters of NVMe-oF are in the financial services and e-commerce sectors. Real-time fraud detection and online retail platforms can experience significant application performance degradation or timeouts using traditional direct-attached storage (DAS) and storage area network (SAN) storage due to high latency.

By deploying NVMe-oF, you will reduce latency from milliseconds to microseconds, enabling millions of transactions per second and tens of thousands of simultaneous user requests without bottlenecks or application timeouts. Such a highly performant data platform can improve customer satisfaction, trust and confidence while boosting revenue and operational efficiency.

**3. Scalability and Flexibility for Data-Center Modernization Initiatives**
NVMe-oF supports seamless scaling by enabling storage to be dynamically added or reallocated without disrupting operations. NVMe/TCP storage enables organizations to dynamically scale or reallocate storage resources between applications, and helps ensure uptime and optimize storage costs while supporting new projects without disrupting operations.

This is particularly prevalent in AI/ML. The more data that can be run through inference and training models, the better the AI and ML outcomes. The workloads are inherently data-intensive, requiring storage solutions that can handle massive data sets with high performance and efficiency.

NVMe/TCP’s high throughput allows AI/ML training and inference processes to access vast amounts of data efficiently, accelerating model training. As the scale of these workloads increases, the flexibility to scale storage and compute resources ensures that infrastructure remains agile and cost-efficient.

## The Future of NVMe-oF
The adoption rate of NVMe-oF is poised to accelerate as organizations continue to model hyperscale-like cloud architectures in their data centers. Key trends driving its adoption include enhanced protocol standardization and widespread vendor support, further simplifying deployment and interoperability. The industry has widely accepted that the NVMe-oF model will replace DAS and become the default protocol for disaggregated storage in cloud-modeled infrastructure.

The development of more cost-effective, high-capacity NVMe drives will complement NVMe-oF’s scalability, making it even more accessible to more organizations. And its ability to reduce power consumption and optimize resource utilization aligns with organizations’ sustainability initiatives.

Industry tech leaders like [Microsoft](https://techcommunity.microsoft.com/discussions/windowsserverinsiders/windows-server-preview-build-25997---how-to-activate-nvmetcp/3993617) have recognized the convergence of cloud native computing and modern data centers by jumping into the mix and democratizing the NVMe protocol with its announcement in 2023 at MSFT Ignite to support inbox NVMe/TCP, making it available now on all data-center operating systems.

Ultimately, NVMe-oF’s role as a foundational technology for modern data centers ensures its relevance well into the future. It’s already seen in new use cases, such as edge computing, where high-speed storage is critical to processing data closer to its source. Its capabilities will continue to empower businesses to meet the challenges of the cloud era with flexibility, performance and efficiency.

If you want to learn more about NVMe/TCP and its transformative benefits for data-center modernization, download the white paper we produced with IDC “[NVMe Over TCP Enables the Democratization of Disaggregated, NVMe Storage](https://www.lightbitslabs.com/idc-research-nvme-over-tcp-democratizes-nvme-storage/?utm_source=TNS&utm_medium=article&utm_campaign=feb).”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)