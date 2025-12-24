With both data center electricity and hardware prices skyrocketing, most organizations will soon be looking to squeeze more efficiencies from their current investments, especially those embarking on [resource-heavy AI projects](https://thenewstack.io/the-ai-competition-is-now-a-high-stakes-construction-race/) running on Kubernetes.

Over the past year, a cross-foundational working group from the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) had been fiendishly developing an enhancement to the Kubernetes scheduler that would allow users to be far more specific in how they allocate jobs to CPUs, network cards, GPUs and various AI accelerators in their nodes, thus allowing them to enjoy all sorts of efficiency and performance improvements.

With the recent releases of both [Kubernetes 1.34](https://thenewstack.io/kubernetes-v1-34-introduces-benefits-but-also-new-blind-spots/) and, last week, [Kubernetes 1.35](https://thenewstack.io/kubernetes-1-35-timbernetes-introduces-vertical-scaling/), the core bits of DRA have been installed and are ready for production.

“User-defined resource placement is the biggest improvement I ever seen in this community in the last six or seven years,” enthused [Byonggon Chun](https://www.linkedin.com/in/byonggonchun/), technical staff of Fluidstack, during one talk at [KubeCon + CloudNativeCon 2024 North America](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/).

## What Is DRA?

You can think of DRA, exposed as a set of new extensible Kubernetes APIs, as a richer replacement for device plug-ins, noted [Patrick Ohly](https://github.com/pohly), Intel senior software engineer, in another [talk](https://youtu.be/Op4DNDTij1U) at KubeCon, “DRA is GA!”

The old school of plug-ins could only provide a count of how many devices were available on a node. With DRA, each device is described with a set of attributes, called `ResourceSlice`, that may include the amount of memory available, or number of compute cores.

This info is provided to the Kubernetes’ built-in job scheduler,`kube-scheduler`(there are also many high-performance third-party schedulers for Kubernetes, so if you are using on these, check to see if its supports DRA yet).

When submitting jobs, users submit a`ResourceClaim`specifying the components a job requires, such as a GPU. The scheduling matches the requests to the available pool of devices and executes the job.

“You can arbitrarily mix-and-match at arbitrarily as needed by your workload,” Ohly explained.

The user can even specify configuration settings, ones that even tell how the device to configure the underlying hardware.

[![](https://cdn.thenewstack.io/media/2025/12/663981bf-kubernetes-dra-01.jpg)](https://cdn.thenewstack.io/media/2025/12/663981bf-kubernetes-dra-01.jpg)

DRA would be ideal for scheduling work on a cluster of both GPUs and CPUs. “When you put your request in for a GPU, the scheduler knows how to find the nodes that have the GPUs, instead of the CPU-only nodes,” explained [Kevin Klues](https://www.linkedin.com/in/klueska/?originalSubdomain=de), Nvidia distinguished engineer, in the “DRA is GA” talk.

A number of companies have already posted DRA-compatible drivers, including [Intel](https://github.com/intel/intel-resource-drivers-for-kubernetes), [Nvidia](https://github.com/NVIDIA/k8s-dra-driver-gpu), [Google](https://github.com/google/dranet), [AMD](https://github.com/ROCm/k8s-gpu-dra-driver) and [Furiosa](https://github.com/furiosa-ai/furiosa-dra-driver-guide).

[Google](https://cloud.google.com/?utm_content=inline+mention) and [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) have also collaborated on [DRANET](https://dranet.dev/docs/), a Kubernetes network driver for high-performance workloads that the two companies [donated to the CNCF](https://youtu.be/KOqyTeFf6K8?list=PLj6h78yzYM2PEePwKKCnyqIQQrHvDZko-).

## Optimizing DRA

But DRA is ultimately more than just finding the right nodes for the job, but also for optimizing the scheduling of resources, so the user gets the best performance from their hardware.

DRA helps solve the problem of misalignment, explained [Gaurav Ghildiyal](https://www.linkedin.com/in/gaurav-kumar-ghildiyal/?originalSubdomain=in), Google software engineer (who has worked on DRANET), in another KubeCon talk, “Achieving Peak Performance Through Hardware Alignment in DRA.”

If you run AI/ML jobs on a cluster with CPUs and GPUs, you might have noticed a wide variance in performance.

In benchmarks, Ghildiyal and Chun have demonstrated how a workload could dip to only 40% of full efficiency in the best of times.

[![diagram of a server's architecture.](https://cdn.thenewstack.io/media/2025/12/177ed4ab-kubecon-hardware-alignment.jpg)](https://cdn.thenewstack.io/media/2025/12/177ed4ab-kubecon-hardware-alignment.jpg)

A modern server may have multiple CPUs and can host multiple GPUs, which may be on different PCI data busses, or have separate memory areas (Ghildiyal).

Moving data between two GPUs, even on the same node, can result in significant performance variability, depending on if the data must cross different CPUs or memory regions on that same server.

And when a CPU traffic must cross the memory boundary to a GPU, data transfer times between the two are elongated. Or the GPU and the network card are on different memory or PCI domains, the data takes longer to cross between them.

Traditionally, K8s wouldn’t understand to assign the CPU to the GPU on the same bus.

[![](https://cdn.thenewstack.io/media/2025/12/4bfe39c6-gaurav_ghildiyal-byonggon_chun-300x225.jpg)](https://cdn.thenewstack.io/media/2025/12/4bfe39c6-gaurav_ghildiyal-byonggon_chun-300x225.jpg)

Google’s Gaurav Ghildiyal (left) and FluidState’s Byonggon Chun (Photo by Joab Jackson/TNS)

DRA sets the stage for the user to be able to specify, for instance, that the GPU and network card should be on the same PCI bus.

DRA exposes device locality to the scheduler, so the scheduler can then do locality-aware scheduling. The user can file a`ResourceClaim` with the specific resources they need, and the scheduler can search through an index of `ResourceSlice`s for available resources.

“The key point is now we have a way to advertise device local quality with a generic scheduler, which wasn’t possible for a long long time,”  explained Chun, in the Hardware Alignment talk.

## Resource Alignment

There are a number of workloads that benefit greatly from a bit of resource alignment, Ghildiyal noted.

One would be for LLM inference and training, a distributed workload problem, where multiple GPUs want to communicate with each other (often through RDMA). Ideally, the network card should be on the same PCI bus as the GPU.

In cases where GPUs are separate from the network card, the workload data may experience not only longer travel times but also create a “high amount of congestion” on the intersocket fabric across the CPUs.

[![chart comparing performance times.](https://cdn.thenewstack.io/media/2025/12/d932fa40-kubecon-hardware-alignment-02.jpg)](https://cdn.thenewstack.io/media/2025/12/d932fa40-kubecon-hardware-alignment-02.jpg)

Performance variance due to hardware misalignment (Ghildiyal).

A DRA-based preventive may have a resource constraint (“*resource.kubernbetes.io/pcieRoot*“) attached to the `ResourceClaim` that tells the scheduler to only pick the node where the network card and GPU are on the same PCI bus.

Another workload that would benefit would be that of loading LLM data into GPUs. Here, aligning CPUs to GPUs could be a real time-saver, as shown in the following illustration:

[![Illustration of CPU/GPU alignment on the same server ](https://cdn.thenewstack.io/media/2025/12/39176102-kubecon-hardware-alignment-03.jpg)](https://cdn.thenewstack.io/media/2025/12/39176102-kubecon-hardware-alignment-03.jpg)

CPU/GPU alignment on a single server.

In a similar vein, an alignment between a CPU and a network card would be beneficial for network-bound applications, such as databases.

In benchmark tests the two presenters did, a misaligned set of resources only had 71% of the throughput of a fully aligned set of resources (which would benefit even further with greater network bandwidth, Ghildiyal said).

Ohly said that while the core components of DRA are ready for use, the working group plans to build out more capability for even greater resource control, such as the ability to extend hardware topologies. So for the next several years will be interesting ones for the Kubernetes scheduler.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)