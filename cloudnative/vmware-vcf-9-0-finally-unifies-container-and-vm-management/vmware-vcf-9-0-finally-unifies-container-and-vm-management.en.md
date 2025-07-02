Usage and customer feedback during the coming months and weeks will determine whether [VMware](https://www.vmware.com/?utm_content=inline+mention) has managed to pull off a remarkable R&D feat: With the general availability release of Broadcom’s VMware Cloud Foundation (VCF) 9.0, VMware has ostensibly achieved what has been a sore missing point in [DevOps](https://thenewstack.io/devops/) for a number of years.

That is, a platform that can allow containers on a [Kubernetes](https://thenewstack.io/kubernetes/) infrastructure and virtual machines (VMs) to run side by side in an infrastructure in which neither benefits from all the capabilities both have to offer. In this way, containers and VMs benefit from enhanced management capabilities that were previously unavailable in a single VMware platform.

Before the release, VMware largely led VM development for a number of years. And its Kubernetes platform was arguably on par with other Kubernetes platform providers while remaining one of the largest Kubernetes contributors. But previously, the best tools and processes were not available together. With VCF 9.0, VMware has managed to incorporate both infrastructures more completely for unified management.

According to [Broadcom](https://thenewstack.io/vmware-alternatives-a-strategic-guide-to-modern-virtualization/), with 9.0, it has enhanced the overall set of capabilities by adding more services, enhanced support for multiple [K8s](https://thenewstack.io/kubernetes/) versions and the ability to upgrade vSphere Kubernetes Service (VKS) and Supervisor independently from vSphere for faster releases and upgrades, while bringing in multicluster management, etc.

The private cloud is a big part of VCF 9.0. While among the different ways that public clouds have been lacking, VCF 9.0 now enables the infrastructure to deploy under a single platform for various environments, VMware says. These often include on-premises deployments in different data centers, co-location and [edge environments](https://thenewstack.io/edge-computing/), or as a managed service through hyperscalers or cloud service providers.

Such a platform should be able to run VM and container workloads, as well as modern AI workloads — which VCF 9.0 does, VMware says. Life cycle and policy are managed through the platform across all of these environments, VMware says.

## Side by Side

Again, VCF is touted as a single platform for running VMs and containers on multi- and private clouds. A key component underpinning VCF’s support for Kubernetes consists of its VMware vSphere Supervisor, which for VCF 9.0 is the vSphere Supervisor.

The Supervisor now extends its functionality as a platform and a control plane on which a set of infrastructure and cloud services, including Kubernetes cluster services, can be provisioned. These include VKS (the Kubernetes runtime), multicluster management, VM services, vSphere Pods, network services, storage and backup services, identity and access control services, image registry and many other capabilities provided as part of the packages included with VKS. Additionally, since VMware delivers a [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention)-certified Kubernetes distribution, the platform is open and extensible to third-party services that are CNCF-compliant.

The vSphere Supervisor in VCF 9.0 is the “secret ingredient that finally enables [containerized apps](https://thenewstack.io/containers/) to natively run side by side with virtual machines,” [Torsten Volk](https://www.linkedin.com/in/torstenvolk), an analyst with TechTarget’s Enterprise Strategy Group, told me. “The fact that this works with different Kubernetes distributions and different versions of upstream Kubernetes is key, as the Supervisor allows current VMware customers to manage much of their current Kubernetes environments through the vSphere console.”

Ever since containers became “a thing,” VMware has been one of the leading Kubernetes management and infrastructure services providers and one of the top three contributors to the Kubernetes projects in the last decade. But that hasn’t been enough.

Prior to its [acquisition by Broadcom](https://thenewstack.io/vmware-to-be-acquired-by-broadcom-in-a-61-billion-deal/) in 2023, much of VMware’s Kubernetes intellectual property (IP) wasn’t being fully exploited by customers. VMware certainly had a lot to offer, but it didn’t have a common platform that enabled companies at different stages in their Kubernetes journey to meet all of their needs regarding VMs and Kubernetes containers.

The shift toward Kubernetes through VCF largely involved the deeper integration of the Kubernetes runtime — VKS, formerly known as Tanzu Kubernetes Grid Service — and its famous VMs and support infrastructure.

The Broadcom acquisition served as a catalyst for integrating VMware’s entire private cloud stack and services into VCF. While VMware previously had many infrastructure and management components within the VCF stack, Broadcom helped bring much-needed focus — and the ability to support organizations’ full range of Kubernetes runtime and unified management requirements. The Kubernetes runtime license is already included in the VCF license, so there is no need for additional licenses.

“It does make a lot of sense to have one license for running VMs and containers, all under management of the same vCenter, as this is tremendously important for consistent policy-driven management across workloads and locations,” Volk said.

## Bare Metal Loses Favor

As it presented VCF 9.0, VMware has offered a substantial argument in favor of opting for a structure of containers on VMs as opposed to bare metal infrastructure.

While bare metal infrastructure previously served as an optimized way to achieve improved runtime efficiency versus the abstraction that running containers on VM layers provided, the evidence points to how containers on VMs have largely caught up in performance to that of bare metal servers. In addition to VMware, the major public cloud providers have also adopted the structure for deploying containers on VMs. This includes [AWS](https://aws.amazon.com/?utm_content=inline+mention) and how it runs [EKS on EC2 VMs](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) by default at this time, as well as [Google](https://cloud.google.com/?utm_content=inline+mention) Platform’s use of [Compute Engine VMs](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) as the underlying nodes. [Azure employs VMs](https://learn.microsoft.com/en-us/azure/aks/core-aks-concepts) on the infrastructure as well.

Additionally, there are security benefits associated with isolation and other aspects of security when comparing VM layers to containers running on bare metal. This is because containers running on bare metal depend on the kernel directly and can suffer from a lack of isolation compared to when running on the abstraction of VMs and the isolation that such deployments provide.

According to VMware, the benchmarks of containers running on VM layers show how the performance has largely caught up to that of bare metal servers. According to [MLPerf benchmark](https://github.com/mlcommons/inference) tests, VCF retains 99% of the performance compared to bare metal, [Prashanth Shenoy](https://www.linkedin.com/in/prashanthshenoy/), vice president of product marketing for Broadcom VMware said during a call with journalists and analysts. “Okay, so there’s negligible performance overload, while it provides all of the critical virtualization benefits that customers have relied on over the last 25 years.”

However, performance hinges on whether vSphere Pods are running natively on the ESX hypervisor or if guest clusters are based on third-party Kubernetes distributions, Volk said. “As vSphere Pods run directly on the hypervisor, performance loss stays minimal. At the same time, ESX provides a lightweight Linux Kernel for Kubernetes applications to share,” Volk said. “Closely tying together the Linux Kernel and Kubernetes Pods is critical, due to the myriad of interdependencies between both components of the app stack.”

The results are different when VCF manages guest clusters based on third-party Kubernetes distributions, Volk said. “These run in VMs based on their own standard [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) distribution, creating a certain level of performance and Linux management overhead, while at the same time providing a unified management plane in the form of the vSphere Supervisor,” Volk said. “In general, I find the ability for seamless and unified multicluster management much more critical than the bare metal debate. Even if there was a little overhead in virtualized environments, the ability for centralized policy-driven management is much more critical, as declarative management is the foundation for scalability.”

## AI Treatment

VCF also does more than just provide perfunctory AI and agent support, VMware says. During the conference call with analysts and journalists, Roger Joyce, principal technology strategy advisor for Alaska-based telecom [GCI Communications](http://GCI%20Communications), said GCI has relied on VCF 9.0 as a customer beta tester.

He highlighted the importance of supporting heterogeneous hardware platforms with VCF 9.0 and said GCI plans to leverage VCF 9’s advanced services, including private AI and data services. VCF 9.0 data services provide enterprise support for [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/), [MySQL](https://thenewstack.io/linux-back-up-a-mysql-database-from-the-command-line/) and other databases, and private AI updates include air-gapped support, GPU as a service and GPU monitoring, Joyce said.

Joyce emphasized the importance of building a secure, high-performing private cloud infrastructure to meet GCI’s operational and regulatory demands. “As Alaska’s largest telecommunications provider, GCI faces unique latency and connectivity challenges due to its distance from major hyperscalers. This geographical reality made a public cloud-first strategy impractical,” Joyce said.

Instead, Joyce and his team opted for a private cloud approach with VCF, which provided them with the technical capabilities necessary to deliver cloud-like self-service and automation in a “local, secure environment,” Joyce said.

While Joyce didn’t explicitly highlight GPUs, his description of GCI’s evolving private cloud capabilities aligns with VMware’s enhancements in VCF 9.0, particularly around support for private AI. These include GPU as a Service, enhanced GPU monitoring, and support for air-gapped environments — all crucial for running modern AI workloads securely and efficiently in regulated industries like telecommunications.

The goal, as he framed it, was to empower internal development teams to innovate quickly and securely without defaulting to public cloud options. VCF enabled GCI to provide the same speed and flexibility as public cloud platforms, while maintaining strict data governance and leveraging capital investments — a critical requirement for AI workloads involving sensitive data and high-performance computing.

Broadcom’s additional improvements to the Advanced Services for VCF 9.0 include:

* Enhanced disaster recovery and ransomware protection through VMware Live Recovery. This includes support for recovery to an isolated on-premises or secondary data center.
* Enhanced vSAN Storage Clusters that allow independent storage expansion from compute clusters.
* VMware vDefend, for what VMware calls “self-service micro-segmentation” and lateral security.
* VMware Avi Load Balancer that integrates the consumption experience with VCF 9.0, as well as life cycle management, single sign-on and password rotation for Avi controllers.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)