# KubeCon Europe: Kubernetes vNode, From the Makers of vCluster
![Featued image for: KubeCon Europe: Kubernetes vNode, From the Makers of vCluster](https://cdn.thenewstack.io/media/2025/04/a607bf27-vnode-1024x683.png)
Kubernetes administrators wandering around the show floor at [KubeCon + CloudNativeCon Europe 2025](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/) this week (in London) should stop by the [LoftLabs](https://www.loft.sh/company/about) at Booth S281 to learn about that company’s latest technology, [Kubernetes vNodes](https://www.loft.sh/blog/vnode-kubernetes-node-isolation-multi-tenancy).

A capability to isolate individual nodes within a Kubernetes cluster, vNode follows up on an open source technology the company introduced in 2021 called [vCluster](https://thenewstack.io/loft-labs-vcluster-provides-secure-multitenant-kubernetes-clusters/), which virtualized Kubernetes control planes to make multitenancy easier, to improve security and use resources more efficiently.

The company claims vNode, a lightweight runtime, takes the next step in this process, offering isolation at the node level, for greater sharing of clusters while maintaining strong isolation between workloads.

The software will target enterprise IT teams that require secure multi-tenancy and [privileged container access](https://thenewstack.io/kubecon-eu-2025-edera-protect-offers-a-secure-container/), and it integrates with all major Kubernetes cloud providers and conformant standalone Kubernetes clusters.

Unlike [vCluster](https://thenewstack.io/vcluster-to-the-rescue/), however, vNode will not be open source, and instead remain a commercial product, noted [Lukas Gentele](https://www.linkedin.com/in/gentele/), CEO of LoftLabs, in an interview with TNS.

## Isolation Challenges
Originally, [multitenancy](https://www.f5.com/glossary/multi-tenant-cloud-architecture) was not an [immediate priority](https://www.ibm.com/think/topics/kubernetes-history) to the [designers of Kubernetes](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/), who saw the use case for the container orchestrator as one of primarily being used by single teams to manage their own clusters.

Nonetheless [Kubernetes multitenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/), in which multiple parties can share a cluster, has become an important operational mode as enterprises and cloud providers all offer Kubernetes services for different and sometimes competing clients.

![Multi-tenancy diagram](https://cdn.thenewstack.io/media/2025/04/48f288c5-multi-tenancy.png)
Courtesy of Kubernetes.io

## Namespaces Alone Aren’t the Answer
[Namespaces](https://thenewstack.io/what-are-linux-namespaces-and-how-are-they-used/), which helped tame the [Kubernetes](https://thenewstack.io/kubernetes/) control plane through technologies such as vCluster, can’t help much with isolating individual nodes within a cluster, Gentele explained.
Kubernetes was not designed to separate nodes nor isolate resources such as I/O and bandwidth at the node level. Pods from different namespaces running on the same node are not isolated from each other, nor are they immune to the negative effects of noisy neighbors or other pods that take more than their fair share of resources. Managing all that at the node level is a headache.

Placing tenants into their own separate nodes does offer strong isolation but can be expensive in terms of resource allocation, given not all resources may be used in each node.

There have been different approaches to solving this problem, like[ Kata Containers](https://thenewstack.io/the-road-to-kata-containers-2-0/), Google’s [GVisor](https://thenewstack.io/google-launches-gvisor-an-open-source-sandboxed-container-runtime/), and [Docker’](https://www.docker.com/?utm_content=inline+mention)s [Sysbox](https://github.com/nestybox/sysbox).

Each has its drawbacks, Gentele explained.

[Kata Containers](https://katacontainers.io/) (often called “micro-VMs”) come with their own individual kernels and can have high overhead. Nor do they work with every cloud provider.
Google [gVisor](https://gvisor.dev/) filters traffic through a system call, which slows performance and is largely limited to Google Cloud. Sysbox, which works most closely to how vNode works, is primarily aimed for use on the [Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/).

## The vNode Way
How does [vNode](https://www.vnode.com/) work? It is a runtime that sits between the Kubernetes control plane and underlying worker nodes. There, it isolates workloads within a lightweight virtualization layer within shared physical nodes.

In a [video](https://youtu.be/woqIVrnbGuE), LoftLabs demonstrated how a privileged workload pod executed into a privileged pod can still have access to other resources on that pod, such as the Kubelet or CoreDNS, leaving them open for [container breakout](https://thenewstack.io/leaky-vessels-vulnerability-sinks-container-security/) attacks.

To install vNode, the user configures a Helm chart to install a vNode [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) onto each node on the cluster, which will automatically place privileged pods into a virtual node (Alerting the containerd runtime not to run this pod). So attackers that break out of the pod itself are still isolated in the vNode, rather than running amuck on the host node.

This approach maintains strict boundaries while remaining resource-efficient and offering high performance. Users can carve up nodes for different teams, projects and applications without resorting to virtual machines.

![vNode comparison chart](https://cdn.thenewstack.io/media/2025/04/1de9e1a0-vnode-03.webp)
Courtesy of LoftLabs.

## vCluster Integration
While virtual clusters provide workload separation, they can still share underlying nodes. Use of vNode ensures that tenant workloads remain isolated even when they share the same cluster.

By combining vCluster and vNode, according to LoftLabs, customers will be able to balance cost efficiency of shared resources while maintaining strong isolation.

In addition to demonstrating vNode, the LoftLabs booth will also showcase some new features with vCluster itself, including new snapshot and restore features and a stronger [Rancher Labs integration](https://thenewstack.io/suse-upgrades-its-rancher-kubernetes-management-family/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)