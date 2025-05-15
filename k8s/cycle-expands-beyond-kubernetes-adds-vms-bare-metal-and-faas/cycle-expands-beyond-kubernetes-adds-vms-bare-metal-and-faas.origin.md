# Cycle Expands Beyond Kubernetes: Adds VMs, Bare Metal, FaaS
![Featued image for: Cycle Expands Beyond Kubernetes: Adds VMs, Bare Metal, FaaS](https://cdn.thenewstack.io/media/2025/04/21f8663e-firat-sahin-wxqqvh-clq8-unsplash-1024x576.jpg)
[Firat Sahin](https://unsplash.com/@firatsahn?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/the-sky-is-filled-with-white-clouds-and-blue-sky-wXqqvH-cLQ8?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
*Disclosure: The author wrote this post on behalf of*
*cycle.io.*[Cycle.io](https://cycle.io/), the lowops Kubernetes alternative, has announced two new features that take it from cloud container orchestration to being a comprehensive compute platform for containers, virtual machines (VMs), and functions that you can run anywhere.
Cycle combines two things: Platform orchestration and infrastructure management. From an infrastructure standpoint, the vendor has historically focused on containers, with support for container images that are OCI-compatible or [Docker](https://www.docker.com/?utm_content=inline+mention)-based (using Docker Hub, Docker Registry, and Dockerfile).

The servers underneath appear as a pool of distributed resources that can now exist on multiple cloud providers ([AWS](https://aws.amazon.com/?utm_content=inline+mention), [Equinix Metal](https://metal.equinix.com/?utm_content=inline+mention), [GCP](https://cloud.google.com/?utm_content=inline+mention), and Vultr), as well as on bare metal, via a new virtual provider.

**Simplified Bare Metal and VM Deployment With CycleOS**
Support for bare metal is not new, per se. Cycle has offered an API for some time, allowing integration with other providers. However, the new virtual provider massively simplifies the process.

“We’ve made an easy button for bare metal,” Cycle’s co-founder and CEO, [Jake Warner](https://www.linkedin.com/in/jakewarner/), told The New Stack. “This means you can run Cycle anywhere — at the edge, on-prem, and colo.”

Instead of implementing an API, which was previously a lengthy requirement, you just use the provided wizard. Cycle initiates the process, and two minutes later, users are provided with a 4MB downloadable ISO, which is the [iPXE](https://ipxe.org) loader for CycleOS. This is a minimal [Linux](https://thenewstack.io/introduction-to-linux-operating-system/)-derived operating system that provides the basic networking, storage protocols, and plugins for the container layer running on top of it. The ISO can be used for network booting using iPXE or installed manually from a flash drive on any server.

Alongside virtual providers, Cycle has also added new support for VMs in the [Qcow2](https://www.linux-kvm.org/page/Qcow2) and raw formats. Here, CycleOS sits below the VMs, managing their networks, volume mounts, and so on.

When deploying a VM on Cycle, the platform creates a hidden container instance that runs a hypervisor with [QEMU/KVM](https://www.qemu.org) inside. The end user doesn’t need to interact with this hidden container at any point. There is no requirement for manual configuration since the platform manages the hypervisor container automatically behind the scenes.

VM images on Cycle can be sourced in three ways: from Cycle’s built-in base images, a remote URL, or using an iPXE script. As you would expect, unlike containers, VMs cannot be re-imaged after deployment.

**Cycle Supports Multicloud Compute With Containers, VMs, and FaaS**
Within the Cycle platform, a compute node can run VMs, containers, and functions in parallel. Users can also run CycleOS on top of, for example, an AWS EC2, GCP, or Vultr instance to turn that instance into a Cycle compute node. “It’s almost VM Inception,” Warner joked. “We can run CycleOS on a VM to host other VMs as long as the lowest VM supports nested virtualization.”

VMs can be migrated between servers that support hypervisors, including across regions, using the same system to migrate a VM as you would for a container instance. This means that volumes attached to the VM will also be migrated to the target instance. However, at the time of writing, while VM migrations work, they are not live migrations. A new copy of the VM will be started on the target server before traffic is redirected.

VMs have access to the same private network as the containers that exist within the same environment. Applications running inside VMs can use the discovery service to connect to other containers and VMs, without requiring additional configuration.

Providing an alternative way to run VMs, particularly for companies seeking a lower-cost option to Broadcom, Cycle also offers VM support for customers who require more control over their operating systems. Warner also foresees three other use cases. The first is for AI start-ups.

“We had companies working with AI who needed particular versions of the kernel and, say, Ubuntu,” he told us. “Previously, you didn’t have that control; you couldn’t bring your own kernel to Cycle because we were just [containers](https://thenewstack.io/introduction-to-containers/). You can now run your own OS as a VM on top of Cycle, parallel to your containers if you need to.”

A second use case involves Windows’ legacy support. “Some of our customers want to run old Windows applications, and use Cycle to run all their containers, plus the legacy Windows app,” said Warner. “Now they can.”

A third use case for VMs would be to run [Kubernetes](https://thenewstack.io/kubernetes/) on top of Cycle, using Cycle as just a control plane. “In theory, someone could install Cycle on all their bare metal, and run Kubernetes VMs on top; that would give them multicloud, hybrid-infrastructure Kubernetes,” Warner told us.

Rounding out the picture, Cycle also includes function containers that can be used for workloads that would otherwise be deployed on serverless or Functions as a Service (FaaS) architecture. These lend themselves to ephemeral tasks, batch processing, or event-driven tasks such as converting files, processing images, or training large language models.

Function containers are configured with a predefined number of hot instances, which have everything pre-defined and configured so that they can be started nearly instantaneously (with a sub-100ms start time). What’s more, because these are containers, users are not limited to specific runtimes; you can put whatever you want into them.

I’ll admit to being a fan of Cycle. While Kubernetes continues to dominate the space, I think Cycle offers a well-designed alternative for companies that are not locked into the Kubernetes way of doing things or are looking for a way out.

Admittedly, the VM implementation is less comprehensive than the existing container functionality. “These new VM capabilities are on the lighter side versus those of VMware,” Warner acknowledged. “Our goal has been to get to say 80% of feature-complete, enough to run a VM on Cycle properly. Then we’ll watch what our customers do with it and optimize accordingly.”

Combined, these three new capabilities could represent an inflexion point for the 2024 [Gartner Cool Vendor](https://cycle.io/blog/2024/12/gartner-cool-vendor/) as it approaches its tenth anniversary. I find myself thinking of a retail client who’s looking for an easier way to manage their ePOS systems across a large store estate and has been battling with Kubernetes, for instance. Likewise, for some alternative cloud providers seeking to capitalize on the burgeoning [sustainable software](https://thenewstack.io/ebooks/cloud-infrastructure/developers-guide-to-cloud-infrastructure-efficiency-and-sustainability/) movement, Cycle could be a great fit.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)