Bare metal for the last decade has offered a performance edge when running [Kubernetes](https://thenewstack.io/kubernetes/) and container infrastructure compared to containers on VM abstraction layers. But that may not be the case for much longer.

Some results indicate that [containers](https://thenewstack.io/containers/) over VMs are catching up in terms of performance, with netperf benchmark tests showing that instances of VMs retain 99% of the performance compared to bare metal. Meanwhile, there has long been a consensus that VMs offer more direct operational control, isolation, security, and other benefits compared to bare metal.

For those who look to the large cloud vendors as an example, Azure, GCP, and [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) all run Kubernetes container infrastructure on VMs, rather than relying on bare metal.

The concept of running on bare metal emerged roughly a decade ago. Part of the rationale was that running everything on bare metal would be simpler. But the biggest motivation was performance — bare metal was believed to have less overhead.

At that time, the technology case was sound. But since then, IT complexity has increased, with technology teams required to support multiple workloads, enforce stricter security, meet tighter SLAs, and adopt a cloud operating model. And now, it is clear, the performance gap is closing. So, CIOs, platform teams, and architects today must seriously consider whether bare metal is still the right approach.

## Virtual vs. Metal

[![](https://cdn.thenewstack.io/media/2025/07/102cbb65-screenshot-2025-07-07-at-7.36.04%E2%80%AFpm-1024x565.png)](https://cdn.thenewstack.io/media/2025/07/102cbb65-screenshot-2025-07-07-at-7.36.04%E2%80%AFpm-1024x565.png)  
A bare-metal node is a machine without any virtualization layer, unlike virtual machines (VMs) or containers. A physical server runs an operating system or application directly on the physical infrastructure, rather than through a hypervisor or container engine. These two environments have a significant bearing on how [containers are deployed at scale](https://thenewstack.io/kubernetes-gets-back-to-scaling-with-virtual-clusters/), isolation and other considerations.

Namespaces enforce only “soft” resource limits in a bare metal configuration. Soft resource limits are allocations that are not strictly enforced by the operating system. Through namespaces, they can be exceeded if other workloads require those resources. This means that while resources — such as CPU and memory — are assigned to a container or process, they are not guaranteed to be available. Other processes may appropriate them, potentially impacting performance.

Instead, VM-based deployments enforce “hard” resource limits — such as CPU, memory, and disk — at the hypervisor level. Hard resource limits are strictly enforced, meaning the assigned resources are reserved and cannot be used by other workloads, regardless of demand elsewhere on the system. This strict enforcement provides strong isolation between tenants.

The relationship between VM isolation and hard resource limits is direct. Since VM isolation is achieved through the enforcement of hard resource limits by the hypervisor, public cloud providers can more precisely guarantee service-level agreements (SLAs).

Meanwhile, “noisy neighbor” issues become more prevalent without VM isolation through hard resource limits. In multitenant environments, performance interference from CPU- or memory-intensive workloads can degrade the experience of others, since soft resource limits alone cannot prevent one workload from impacting another. For example, when analyzing a massive amount of astrophysics data from a telescope feed, a single misbehaving container can monopolize resources and affect overall cluster stability.

A notable performance gap previously existed between Kubernetes running on bare metal and VMs, but recent benchmark tests indicate that the disparity is becoming increasingly negligible. These results thus cast further doubt on the main benefit of relying on bare metal over containerized infrastructure. However, performance benchmarks indicate that these benefits have diminished.

According to benchmarks (ReveCom has not yet verified these results, but will shortly), containers running on VM layers demonstrate that performance has largely caught up to that of bare-metal servers. The Broadcom [VMware](https://www.vmware.com/?utm_content=inline+mention) benchmark [reported results](https://www.vmware.com/docs/vsphere8-virtual-topology-perf) comparing vSphere 8 to bare-metal hardware, showing negligible differences and even lower latency, depending on the CPU configurations.

For AI/ML workloads using vGPU, [MLperf](https://www.nvidia.com/fr-fr/data-center/resources/mlperf-benchmarks/) benchmark tests show how instances of Broadcom’s VMware Cloud Foundation VM platform [retain 99% of the performance compared to bare metal](https://blogs.vmware.com/cloud-foundation/2025/04/17/broadcom-delivers-near-bare-metal-performance-for-virtualized-ai-ml/), for example. Specifically, the results were based on MLPerf Inference v5.0 workloads virtualized using MLCommons and with VMware vSphere 8.0 U3 on a SuperMicro SuperServer SYS-821GE-TNRT and a Dell PowerEdge XE9680. These results imply significant cost reductions associated with virtualizing AI/ML workloads running in GPU environments.

A key performance factor for node instances is whether they run natively on the ESX hypervisor or are part of guest clusters using third-party Kubernetes distributions, [according to Torsten Volk](https://www.linkedin.com/in/torstenvolk), an analyst with TechTarget’s Enterprise Strategy Group. “If the pods run directly on the hypervisor, performance loss stays minimal. At the same time, ESX provides a lightweight [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) Kernel for Kubernetes applications to share,” Volk said.“Even if there was a little overhead in virtualized environments, the ability for centralized policy-driven management is much more critical, as declarative management is the foundation for scalability.”

In a “[Solution Path for Cloud-Native Infrastructure With Kubernetes](https://www.gartner.com/en/documents/4022711),” Gartner notes that a shift to bare metal often requires DevOps teams to abandon their “tried-and-trusted virtual infrastructure and associated know-how.” They must begin anew in many ways when managing a new bare-metal environment.

## Big Public Clouds

[![](https://cdn.thenewstack.io/media/2025/07/aeec5753-screenshot-2025-07-07-at-9.01.png)](https://cdn.thenewstack.io/media/2025/07/aeec5753-screenshot-2025-07-07-at-9.01.png)

IT organizations often look to public cloud providers to understand how they manage their infrastructure, and the big three cloud vendors put these claims to the test for hyperscaling. By relying on VM abstractions on which containers are run, Kubernetes services from AWS, GCP, Azure, or other cloud providers are almost exclusively not running their public Kubernetes offerings directly on bare metal. These cloud vendors state in their official documentation and presentations that, for most workloads, the performance difference between containers on VMs and bare metal is largely negligible, thanks to modern hyperscale and hardware virtualization improvements.

A continued emphasis on hyperscaling with VMs is nothing new, supporting the claim that even when a closing performance gap exists between VMs and bare metal, the significant security and operational benefits of virtualization far outweigh the marginal performance impact. Again, the loss of latency, CPU, and memory performance, as well as other related benchmarks, remains negligible.

As far back as 2020, an official [AWS presentation](https://aws.amazon.com/blogs/aws/reinvent-2020-liveblog-infrastructure-keynote/) at re:Invent noted that, for many instance types, “the performance difference between EC2 instances and bare metal is negligible for most workloads.” AWS has also stated that its Nitro hypervisor provides near-bare-metal performance for most workloads.

In its document, Microsoft notes that for most workloads, the performance difference between VMs and bare metal is negligible, thanks to advances in virtualization technology. [Microsoft also claims](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/compute-benchmark-scores) that “Azure VMs offer near bare-metal performance for most workloads, especially with the latest generation of hardware and hypervisor improvements.”

Likewise, Google states that for most workloads running on Google Cloud, the [performance difference](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance) is thanks to advances in virtualization technology.

## The Verdict

The performance benefits that can be achieved by running Kubernetes and containers on bare metal are minimal for the vast majority of workloads. Granted, that does not mean they’re never beneficial — they’re just not appropriate for most use cases when weighed against the risks inherent in bare metal deployments and the benefits delivered by virtualization.

As mentioned above, there are always [security](https://thenewstack.io/security/) concerns of bare metal. Workloads are running on the same kernel, and so once an attacker accesses the server OS, that means the entire workload — all the workloads — are accessible.

Conversely, when containers are running on VMs, a single container, cluster, or application that is compromised remains isolated thanks to the VM’s isolation configuration.

Ten years ago, bare metal offered tangible performance advantages. Today, with modern CPUs and infrastructure innovations, VM-based container performance rivals or exceeds bare metal in most scenarios. [Tests consistently show VM-based Kubernetes](https://thenewstack.io/kubernetes-troubleshooting-primer/) platforms achieving 90-110% performance relative to bare metal.

Major public cloud providers that operate container services at a billion-dollar scale opt for VM-backed Kubernetes. Thanks to the architecture’s strict isolation, enforced resource limits, and operational consistency, these decisions provide compelling validation for enterprise IT leaders to reconsider bare metal deployments.

Any organization considering a bare metal strategy must articulate clear, specific technical or business reasons for doing so. Without strong justification, VM-based container architecture remains the default best practice.

When evaluating platform strategy, IT decision-makers should examine the number of microservices deployed per physical host and the fault domain present in a single bare-metal deployment. Attention must also be given to the number of [Kubernetes versions actively supported and how Custom Resource](https://thenewstack.io/flexibility-matters-when-setting-kubernetes-resource-limits/) Definitions (CRDs) are managed across multiple applications. Consideration should be given to the time required for a typical Kubernetes upgrade and how the surface area of Kubernetes is being reduced.

Such questions challenge existing assumptions. Often, IT leaders adopt inherited practices without reassessing their fit. A reevaluation of bare-metal strategies may reveal that benefits once relevant are now eclipsed by modern requirements.

Certain very niche use cases can still require bare metal when every millisecond of latency counts. These instances may include high-frequency trading applications or when compliance mandates require bare-metal servers for certain contracts. However, as the performance gap is largely closed, investing in VM [infrastructure that supports containers](https://thenewstack.io/terraform-beta-supports-multicloud-complex-environments/) and Kubernetes is the best allocation of resources at this time for the vast majority of usage cases.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)