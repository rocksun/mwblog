The wonders of [containers](https://thenewstack.io/introduction-to-containers/) — their overall flexibility, portability, and logical encapsulation of everything needed to run an application — have made them a mainstream method of developing and deploying modern apps. The latter is enhanced through orchestration platforms like Kubernetes, particularly for deployments at scale.

Nonetheless, there are still questions about how to maximize containers’ utility. Should you run them on [bare metal](https://thenewstack.io/bare-metal-kubernetes-the-performance-advantage-is-almost-gone/) servers or on virtual machines (VMs)? Is there even a need for virtualization in the era of containers, Kubernetes, and [cloud native technologies](https://thenewstack.io/cloud-native/ "cloud native technologies")?

For the lone developer, the answers to these questions are immaterial. But for enterprises with strict requirements for operational flexibility, scalability, performance, service-level agreements (SLAs), compliance, and security, the answers are clear.

“Running containers and virtual machines in a virtualized environment is a much more modern approach, as compared to a bare metal approach that comes from the legacy days of 20, 30 years ago,” says [Mark Chuang](https://www.linkedin.com/in/chuangmark), head of product marketing, [VMware Cloud Foundation](https://www.vmware.com/?utm_content=inline+mention) at Broadcom.

## The operational flexibility of virtualized containers

Bare metal container deployments typically involve large physical clusters running one version of [Kubernetes](https://thenewstack.io/kubernetes/) that multiple applications depend on. However, containers running in VMs consist of multiple smaller clusters that can stretch the underlying physical infrastructure. Each cluster has the flexibility to run a different version of Kubernetes that is attuned to the needs of the specific applications on that cluster.

“If you want to update a version of Kubernetes, you can just do it for that cluster,” Chuang says. “You’re not impacting all the other applications at the same time.”

Conversely, on large bare metal clusters with multiple running applications, every application must be updated — which is time-consuming and compromises productivity. In large bare metal clusters, if one application needs the latest version of Kubernetes, all the applications in that cluster must adopt this latest version. Chuang warns that this may result in compatibility issues and be disruptive for application owners.

## Enhancing security for containerized applications

Users can fortify security isolation at multiple layers by running containers in virtualized environments. This preserves data integrity while enhancing data privacy and regulatory compliance.

It also minimizes the impact of expensive security breaches by minimizing the blast radius. Because deploying containers in VMs provides multiple layers of isolation, it can reduce an organization’s attack surface.

“If any of those layers is compromised, [the attack’s] not going to get out and spread,” Chuang says.

Security isolation occurs at multiple levels in a virtualized environment.

“In a VMware-based environment, there’s isolation at the vSphere cluster, the workload control plane, vSphere namespace, Kubernetes cluster, and Kubernetes namespace levels,” Chuang explains. “Additionally, you can establish microsegmentation at the networking layer on top of that.”

In bare metal container deployments, namespaces are the only point of isolation because Kubernetes namespaces are usually deployed 1:1 in a single Kubernetes cluster.

If a breach occurs, “all the applications on that host share that same Linux kernel, so if that kernel is ever impacted, you’ve got significant security concerns,” Chuang mentions.

## Optimizing performance and meeting SLAs

It’s difficult in a bare metal approach to match the performance SLAs of deploying many containers with virtualization, Chuang says. Both resource load balancing and performance SLAs are better on VMs than they are with containers on bare metal. This is especially true when encountering a “noisy neighbor” in a multiapplication or multitenant environment.

The noisy neighbor problem occurs when multiple apps are running on the same host or cluster, and there’s a spike in demand for resources (involving network, compute, memory, or storage) for one of them. That surge can negatively affect the resource’s availability for other applications, hindering their performance.

Virtualization allows users to uphold SLAs by specifying ahead of time “clear policies about how much of a resource a particular application is going to get,” Chuang says.

Additionally, technologies like live migration and advanced resource scheduling can move workloads to hosts that are not experiencing a surge in resources.

“In a virtualized cluster, you can nondisruptively migrate a workload from one physical host to another to give it the compute, storage, or networking performance it needs to run effectively, or [you can] let the platform perform those tasks automatically,” Chuang says.

This capability, along with specifying policies for resource allocation for applications, improves organizations’ ability to meet performance SLAs. It also reduces the overhead for spinning up and running those applications.

“If you’re not effectively getting the application the resources it needs, then you may have to procure and stand up more servers and more hosts,” Chuang says. “That increases costs.”

## Minding the total cost of ownership

A single platform for running virtualized and container workflows improves deployment efficiency — with attendant cost advantages — when internationalizing and scaling applications. Users can implement consistent processes when virtualized and container workloads run on the same underlying infrastructure, compared to running them in silos.

“Most organizations are running a mixture of containerized applications and ones on virtual machines,” Chuang says.

Simplifying the underlying architecture by running both workloads through virtualization provides numerous cost benefits. “You can get very high levels of utilization because you can mix and match; you don’t have any stranded capacity,” Chuang says. Those advantages are magnified for deployments at scale and positively impact cost, particularly at higher utilization rates.

“If you’re effectively maximizing usage of your underlying infrastructure, then you don’t have to purchase as much infrastructure because less of it is sitting idle in stranded siloes,” Chuang says.

Additionally, because deploying containers in virtualization environments can minimize security breaches from spreading, organizations may reduce exposure to costly penalties, regulatory woes, and litigation.

## Why virtualization is key for enterprise-grade production

Much of the value of deploying containers — and container orchestration platforms like Kubernetes or [Docker](https://www.docker.com/?utm_content=inline+mention) — with virtualization pertains to the enterprise. Flexibility for scaling operations is a pivotal concern for production settings. Organizations also require dependable security to meet data privacy, regulatory compliance, and data integrity requirements. Finally, high levels of performance are necessary for mission-critical workloads across industries and use cases.

Virtualized environments facilitate each of these benefits in a cost-effective way, making them worthy of your consideration. The ability to do this on a single platform for virtualized and container applications can reduce overall costs — which is why the hyperscalers ([AWS](https://aws.amazon.com/?utm_content=inline+mention), [Google Cloud](https://cloud.google.com/?utm_content=inline+mention), and [Microsoft Azure](https://aka.ms/modelmondays?utm_content=inline+mention)) function this way for the majority of customers’ workloads in their environments.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/ee3e39b7-cropped-52925a32-jelani-harper-110x110-1.jpg)

Jelani Harper has worked as a research analyst, research lead, information technology editorial consultant, and journalist for over 10 years. During that time he has helped myriad vendors and publications in the data management space strategize, develop, compose, and place...

Read more from Jelani Harper](https://thenewstack.io/author/jelani-harper/)