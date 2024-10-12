# How Nvidia Scaled Its Cloud Services With KubeVirt
![Featued image for: How Nvidia Scaled Its Cloud Services With KubeVirt](https://cdn.thenewstack.io/media/2024/10/531145bb-nvidia-kubevirt-1024x576.jpg)
In 2013, Nvidia decided that users should have the ability to play top-of-the-line games on top-of-the-line hardware without having to shell out $3,000 for a gaming PC. The company built GeForce NOW, an online service that made super fast GPU-backed gaming PCs in the cloud accessible to players anywhere in the world.

GeForce NOW grew in popularity to the point where it currently has 25 million subscribers. With all those users, the service isn’t in danger of sunsetting anytime soon, but there was a moment of truth for Nvidia around its original architecture. While Nvidia favors next-generation IT in almost all cases, GeForce NOW was built with virtual machines (VMs), not Linux containers, and this was causing problems for the service’s plans to scale out.

Scaling out such a service is an optimal use case for containers orchestrated by [Kubernetes](https://thenewstack.io/kubernetes/). But what happens if the original gaming platform was built on VMs, which are more rigid and less amenable to rapid scale out and scale down?

Enter [KubeVirt](https://kubevirt.io/), an open source platform for [running container and virtualization workloads](https://thenewstack.io/virtualization-and-containers-better-together/) on premises or in the cloud.

[Nvidia was built on high-end hardware](https://thenewstack.io/nvidias-hardware-roadmap-and-its-impact-on-developers/) for gaming. So how did Nvidia build an online gaming platform using containers and VMs?
First, some background.

## What Is KubeVirt?
KubeVirt presents a unified shared platform where developers and administrators can build, modify and deploy applications in containers and VMs. KubeVirt allows VMs to be managed with the same software used to manage Kubernetes, whether you use [Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift) or you roll your own (DIY).

![KubeVirt architecture](https://cdn.thenewstack.io/media/2024/10/327082ae-kubevirt-architecture-simple-1024x448.png)
Source: [KubeVirt](https://kubevirt.io/user-guide/architecture/)

KubeVirt places a virtual machine inside a Linux container. Thus you can manage VMs like other container-based assets on your platform. KubeVirt includes support for VM snapshots, live migration, memory hot plugging, non-uniform memory access (NUMA), [huge pages](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/performance_tuning_guide/s-memory-transhuge), virtual networking and storage. You get access to all the VM features you expect when dealing with virtual machines at scale, but manageable through the same tools you use for Kubernetes.

## How Nvidia Scaled KubeVirt
Nvidia had to satisfy thousands of gamers who expected a gaming experience equivalent to a PC on their desk, not in the cloud.

At KubeCon Paris 2024, [Ryan Hallisey](https://www.linkedin.com/in/ryan-hallisey-b680b279/) and [Alay Patel](https://www.linkedin.com/in/alaypatel07/) from Nvidia [presented some benchmarks](https://www.youtube.com/watch?v=pCgLYXevN3Y) for KubeVirt. The pair highlighted how the community drastically increased the performance of KubeVirt and showcased their benchmarking tools. The team wanted to move to a more microservices-based approach, said Hallisey. “How do we do this without completely abandoning our investment? This is where we looked at adopting KubeVirt. The next generation of GeForce NOW infrastructure is based on KubeVirt and Kubernetes.”

## Managing and Automating VM Infrastructure on KubeVirt
KubeVirt is the hosting plane for VMs in a Kubernetes platform, and other tools provide automation and management. [Ansible](https://kubevirt.io/2023/Managing-KubeVirt-VMs-with-Ansible.html) is an excellent automation tool for KubeVirt, as is [GitOps](https://kubevirt.io/user-guide/cluster_admin/gitops/), which maintains the state of clusters in a Git repository.

KubeVirt is a viable option for taking on workloads currently on other VM platforms. You can migrate them to KubeVirt using the open source project [Konveyor forklift](https://github.com/kubev2v/forklift.github.io/blob/main/index.md), as this [video demonstrates](https://www.youtube.com/watch?v=RnoIP3QjHww).

Once you’re up and running, there is a lot of activity within the platform’s open source community. At DevConf in June 2024, [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)’s [Lee Yarwood](https://www.linkedin.com/in/leeyarwood/) explored the [state of VM creation](https://www.youtube.com/watch?v=HqupumX5Zys) in KubeVirt. And at Cloud Native Rejekts 2023, Cloudera’s [Shane Kumpf](https://www.linkedin.com/in/shane-kumpf-024aa222/) showed how the company [moved toward a hyperconverged infrastructure](https://www.youtube.com/watch?v=kMyAkoiXXrg) using KubeVirt. [Join the community](https://kubevirt.io/community/) and interact with other users.

## Conclusion
KubeVirt scales to thousands of users, providing a side-by-side platform for VMs and containers managed by one set of tools. Combining the control plane and management of containers and VMs reduces the load on developers and systems administrators.

Migrating your workloads from another virtualization platform to KubeVirt can start with Konveyor and then be automated and managed by other tools. KubeVirt is a viable alternative virtualization platform offering standard VM features, an ecosystem of partners and scale-out performance.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)