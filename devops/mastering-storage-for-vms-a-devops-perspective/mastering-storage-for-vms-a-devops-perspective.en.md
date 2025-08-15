Sparked by escalating costs and risks, virtualization is a hot topic for many DevOps professionals. The interest of organizations looking to migrate their virtual machines (VMs) and modernize their IT infrastructure cannot be underestimated. As many have already discovered, infrastructure modernization and moving applications from legacy VMs have their benefits: accelerated application delivery, reduced operational costs and minimized business risks, such as vendor lock-in.

Yet, while compute is often the focus, storage is critical for successful VM migrations, affecting factors most important for DevOps, such as performance, scalability and reliability. Here is a new approach to migrating virtualized applications, with a focus on the DevOps perspective.

## Storage Considerations for Virtualized Applications

When migrating applications from legacy VMs, DevOps teams must carefully [evaluate storage options](https://thenewstack.io/no-more-waiting-eliminate-application-timeouts/) to meet modern demands. Key considerations should be fast provisioning and management, scalability, flexibility, data availability and resilience.

In legacy virtualized environments, persistent storage was commonly provisioned via dedicated storage area networks (SANs), using protocols like Fibre Channel (FC), iSCSI (Internet Small Computer System Interface) or Network File System (NFS).

While these technologies provided a stable foundation for many deployments, their inherent rigidity and scaling limitations often present challenges in modern, agile infrastructure paradigms. As DevOps practices drive the need for increased agility, scalability and cost optimization, traditional storage architectures can become bottlenecks. Evolving storage strategies are crucial to align with Infrastructure as Code principles and the dynamic nature of [modern application deployments](https://thenewstack.io/a-cloud-architects-guide-to-e-commerce-data-storage/).

While NFS, iSCSI and FC have historically been prevalent, the DevOps landscape is seeing a rise in more adaptable and efficient solutions, such as [NVMe over TCP](https://www.lightbitslabs.com/nvme-over-tcp/) (NVMe/TCP). This transition is fueled by the maturity of [software-defined storage](https://www.lightbitslabs.com/product/) (SDS) platforms and the imperative for highly scalable and cost-effective storage backends that can be provisioned and managed programmatically.

## Increased Adoption of Software-Defined Storage

For block storage, legacy SAN infrastructure using FC is still in play. Historically, FC’s dedicated bandwidth and the robust feature sets of traditional storage arrays justified this choice, particularly given the limitations of older networking hardware. However, the landscape is shifting.

Networking advancements and the rise of SDS are fundamentally altering the way we architect storage for modern virtualization. A key driver for SDS adoption is cost-effectiveness; Ethernet-based storage solutions offer significant savings compared to traditional SANs and provide greater scalability.

Technologies like [Ceph storage](https://www.lightbitslabs.com/ceph-vs-lightbits-comparison/), iSCSI, and the increasingly popular NVMe/TCP provide software-defined block volumes. Notably, NVMe/TCP is gaining significant traction due to its ability to deliver high performance at a considerably lower cost point by using existing Ethernet infrastructure. This makes it a compelling alternative to traditional FC SANs for demanding block-level workloads, aligning with the DevOps focus on efficiency and agility.

As network bandwidth advances and Ethernet technology innovations continue, organizations will move away from the constrained limitations of traditional FC SAN to more flexible and scalable network-based storage, with NVMe/TCP a clear frontrunner.

## Enabling Live Migrations of VMs

VMs traditionally require seamless state, or the ability of a VM to move from one physical host server to another without any noticeable interruption of applications, services or user sessions. Throughput and network connectivity during live migrations between hosts typically follow an ephemeral model, being provisioned fresh on a new host with network cutover upon startup.

However, technologies like NVMe/TCP enable VMs to maintain high I/O throughput not just during steady-state operation, but crucially, throughout the live migration process. This capability bridges the gap in agility between VMs by minimizing performance impact during critical infrastructure operations, contributing to smoother application availability and resilience.

The team at Lightbits Labs recently tested how VMs using NVMe/TCP-based storage were able to sustain consistent IOs while being migrated. A VM backed by three persistent volume claims (PVCs) was used — one for the operating system (vda) and the other two (vdc and vdd) for the application. The results of the FIO (Flexible I/O Tester) script show a tiny decrease in IOPS and a tiny bump in latency, between a regular run of FIO (VM is not migrating) and a run that continuously sends IOs to the storage during the live migration.

[![](https://cdn.thenewstack.io/media/2025/08/dfaa04fb-image1.png)](https://cdn.thenewstack.io/media/2025/08/dfaa04fb-image1.png)

## Conclusion

One of the biggest challenges in virtualization modernization is maintaining the availability of applications, services and user sessions during live migrations. Traditionally, FC SANs have provided the storage infrastructure, but modern software-defined NVMe/TCP storage solutions are changing the way organizations design their virtualized environments.

And while every customer’s journey is unique, there are core fundamental considerations when planning and architecting the next generation of an organization’s virtualization infrastructure. These generally revolve around the VM storage integration. Software-defined NVMe/TCP storage provides performance, scalability and reliability to accelerate DevOps workflows.

* **Fast provisioning and management:** DevOps teams require the ability to quickly provision and manage storage for VMs. SDS solutions, such as NVMe over TCP, enable dynamic provisioning and management of storage volumes, improving efficiency.
* **Scalability and flexibility:** Modern applications require scalable and flexible storage. SDS solutions, such as NVMe/TCP, provide the ability to scale storage as needed and offer more cost-effective options than traditional SANs.

For DevOps teams, software-defined storage with NVMe/TCP is interesting for virtualized applications. It provides fast provisioning, scalability, flexibility, resilience, and persistent and sustained high-performance needed for modern applications that traditionally needed a SAN-based fabric to run.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/01/775818af-carolplatz.jpg)

Carol Platz brings over 25 years of technology evangelism and marketing leadership for high-performance data storage solutions to her role as vice president of marketing at Lightbits. Prior to joining the company, she directed marketing for storage startups like WekaIO,...

Read more from Carol Platz](https://thenewstack.io/author/carol-platz/)