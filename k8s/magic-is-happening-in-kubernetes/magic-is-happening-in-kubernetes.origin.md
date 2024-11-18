# Magic Is Happening in Kubernetes
![Featued image for: Magic Is Happening in Kubernetes](https://cdn.thenewstack.io/media/2024/11/75c32dfe-kubernetes-1024x576.jpg)
As the Kubernetes community kicks off the [Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/) flagship conference this week in [Salt Lake City](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/), it dawns on me that the title “cloud native” means a lot of different things to different people. I will spare you a recap of what the term “cloud native” means. Google search will present to you a treasure trove of definitions, blogs, delicious Reddit debates, and GenAI-summarized nuggets of truth.

I find myself thinking about this phrase today because many projects, working groups and [special interest groups (SIGs)](https://thenewstack.io/how-and-why-to-get-involved-with-kubernetes-sigs/) across [Kubernetes](https://thenewstack.io/kubernetes/) are working hard to prepare the platform for 2025. In doing so, we all make the platform the premier destination for more than what we traditionally know as cloud native application services today. It sounds like our [understanding of “cloud native”](https://thenewstack.io/cloud-native/) is about to evolve.

From the first day I met [Red Hat OpenShift,](https://www.redhat.com/en/technologies/cloud-computing/openshift) it has been a platform that did not discriminate what application patterns it would allow. Besides cloud native, users also have database services, LAMP stacks, monolithic over-the-counter applications (COTS), event-driven API endpoint topologies, stateful, intelligent or AI endpoints, batch and HPC and on and on.

All of these patterns will place different requirements on the platform at the lowest of levels that don’t immediately surface in your mind. Some will require east/west and north/south networking. Some UDP instead of TCP. Some file instead of object or block storage. Some ordinality in how their components start. Some need to be Non-uniform memory access (NUMA) aware. Some have nuanced routing. Some have requirements in the way they get an IP address. Some need protection against split-brain scenarios. Some need shared hardware devices. And don’t even get me started on their authn/z and workload identity needs!

The list of platform-level functionality the world’s applications trigger is unending. We take for granted that the platform magically provides these constructs to our workloads. So, I wanted to draw your attention to some things that are evolving across the OpenShift user base and community that will once again rely on the platform magically helping out.

Artificial intelligence is driving people to want better ways to gain access to hardware accelerators, like GPUs, from a variety of vendors across a distributed system. The work coming out of the [dynamic resource allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/), instaslice, and [kueue](https://kueue.sigs.k8s.io/) projects will come together to offer a great experience on this front in 2025.

The ideas of the [LeaderWorkingSet](https://github.com/kubernetes-sigs/lws) group are opening up people’s minds to characteristics of applications that need something more than horizontally scaled replicas. The caching intelligence of a routing gateway that remembers where an object like a large language model (LLM) lives in the cluster will really expedite model training experiences. Security will demand better confidential computing attestation rules. Zero trust will require better workload identity automation that is cloud provider-specific and more generic for on-premises use.

More workloads will continue to move to the edge, and with them, they will bring requirements regarding new ways to achieve high availability for a cluster that is smaller than quorum algorithms allow today.

Virtual machines (VMs) as workloads will bring in new requirements on network segmentation and IP addressing at the Kubernetes namespace level. Application developers will want better networking control without becoming network administrators, which will cause meshes and routers to become more transparent to the end user.

This is just a taste of where we will see the OpenShift platform evolving to meet the needs of the workloads people want to run in 2025.

Platforms without workloads are pointless. We don’t build houses for no one to live in them. As we focus on what we use an application service to do or perform, be that making money for the business, allowing for a new human experience, sharing critical research, or simply telling someone you love them, it is easy to forget the magic that happens behind the scenes. Be prepared to be surprised at where the Red Hat OpenShift platform will let you go in 2025.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)