# Spegel: A Stateless Cache for Locally Storing Image Artifacts
![Featued image for: Spegel: A Stateless Cache for Locally Storing Image Artifacts](https://cdn.thenewstack.io/media/2025/02/462544f1-spegel-1024x683.jpg)
For those running a small, experimental cluster at home, these repository limits can be a “major pain point,” noted developer [Philip Laine](https://www.linkedin.com/in/phillebaba/),

Laine is the author of [Spegel](https://spegel.dev/), an [open source project](https://github.com/spegel-org/) that brings peer-to-peer file sharing to the world of container registries.

Spegel can help the hobbyists keep under their allotment, as well as help larger organization deploy their Kubernetes workload clusters much more quickly.

When Kubernetes starts or recovers a node, each node must pull each copy of the workload image from a nearby registry, be it cloud, public or individually self-hosted.

Spegel [sets up a distributed registry](https://spegel.dev/docs/) across each node, so each unique container can be downloaded once and then copied to other nodes.

Introducing the technology in a [FOSDEM talk](https://fosdem.org/2025/schedule/event/fosdem-2025-4934-cache-me-if-you-can-p2p-image-sharing-in-kubernetes-with-spegel/) earlier this month, the [Spegel](https://github.com/spegel-org/) creator posted [benchmarks](https://github.com/spegel-org/benchmark) showing that image retrieval times can be improved by 82%.

This approach also speeds workload startup times and reduces network traffic.

## Stateless Cluster Local OCI Registry
Cloud native current bottleneck is distributing the workloads to the runtime.

But operations can be thwarted by rate limits of the image registry, or come to a halt entirely should a registry go offline. Or images can disappear, such as [what happened](https://www.redhat.com/en/blog/about-the-quay.io-outage-post-mortem) with [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)‘s [Quay recently](https://github.com/migtools/mig-controller/issues/1149).

“There is no point of having a cluster that can scale to 10,000 nodes if you can’t pull down the image for the application you actually run,” Laine told the audience.

If the image extremely large, just the network travel time can slow things down, doubly so for rate limits: [Docker Hub](https://www.docker.com/?utm_content=inline+mention), for instance, limits download speeds to 100MB/s for images.

## Like BitTorrent, but for Containers
Laine recalled a meetup presentation from 2018 or so from a system administrator about how his organization worked through a Docker Hub outage during a dramatic increase of its own usership. Operations could not scale up because it depended on several critical images from the temporarily-offline Hub.

The sysadmin’s solution was to [ssh](https://thenewstack.io/dr-torq-go-remote-with-ssh/) into an old node, then exporting the images and then basically continuously [copy](https://thenewstack.io/linux-lesson-copy-files-over-your-network-with-scp/) the images to the new nodes as they came on line.

“It worked, even if it was a very dirty solution,” Laine said.

The workaround sparked an idea with Laine: “Why aren’t we always doing this?”

Thus began work on Spegel, an OCI-complaint read-only registry.

The implementation turned out to be surprisingly easy, according to Laine, who was also one of the core developers of [Flux](https://thenewstack.io/why-flux-isnt-dying-after-weaveworks/) GitOps tool.

An image is actually a collection of multiple components. At the top level is an index of all the other included components. It [references](https://oci.dag.dev/?image=ghcr.io%2Fspegel-org%2Fspegel%3Av0.0.30), in a JSON format, all the other layers with their digest or the cryptographic hash of the content itself.

The [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)‘s Open Container Interface (OCI) specifies how containers are structured. The OCI distribution spec describes how clients pull images from a[ registry](https://thenewstack.io/tutorial-host-a-local-podman-image-registry/), which is done layer by layer.

Spegel allows Kubernetes nodes to pull images from each other. If none of the nodes have the image, the requests falls back to the original registry.

One advantage that OCI’s [containerd format](https://thenewstack.io/dockers-quest-simplicity-evolution-containerd/) provides is that it stores uncompressed images layers on disk. The file names are the hashes.

“This means Spegel can piggyback off of Containerd. It is not doing any type of storage. So the role of the registry is to serve as proxy. “There is no state at all,” he said.

Each node has an OCI registry, which looks first on the local host for the layer. If one is not found, Spegel intercepts the request and looks on other nodes for the requested layer. If one is found, it proxies the request.

Speqel has three components: the registry, a routing and discovery component, and an advertising mechanism.

“It’s a bit like BitTorrent,” he said. “It’s a bunch of clients advertising to other clients.”

The registry looks at all the content on disk and then advertises it in a distributed hash table. The software uses a [Go implementation](https://github.com/libp2p/go-libp2p-kad-dht) of the widely used [Kademlia Distributed Hash Table](https://github.com/libp2p/specs/tree/master/kad-dht). When a request comes in, Spegel simply looks it up on the hash table.

## New Docker Rate Limits
Today, the majority of users of Spegel tend to be home lab enthusiasts who are hoping to avoid Docker Hub rate limiting, Laine said. Other uses can be in air-gapped deployments or running very large machine learning models, which would copied much more quickly if done locally.

On March 1, Docker Hub latest rate limits for pulling images from Docker Hub. The professional (paid) accounts no longer have rate limits for the number of image pulls, personal accounts [will be limited](https://www.docker.com/blog/revisiting-docker-hub-policies-prioritizing-developer-experience/) to 100 pulls an hour (10 if unauthenticated).

Spegel’s [Compatibility with cloud providers](https://spegel.dev/docs/getting-started/#compatibility) varies according to their adherence to the OCI specs. Spgel works great with the [Amazon Kubernetes Service](https://aws.amazon.com/?utm_content=inline+mention), somewhat with the [Azure Kubernetes Service](https://azure.microsoft.com/en-us/products/kubernetes-service) and thus far, not at all with the [Google Kubernetes Engine](https://cloud.google.com/?utm_content=inline+mention).

It also works great with [MiniKube](https://thenewstack.io/install-minikube-on-ubuntu-linux-for-easy-kubernetes-development/). It’s actually embedded in SUSE’s [K3s](https://thenewstack.io/ranchers-k3s-joins-cncf-sandbox-as-first-kubernetes-distribution/) and [RKE2](https://thenewstack.io/suse-upgrades-its-rancher-kubernetes-management-family/) Kubernetes distributions.

Ultimately, Spegel may help us rethink how image distribution could work through the power of peer-to-peer sharing, which would benefit the hobbyist and largest at-scale Kubernetes users alike.

*TNS Analyst Lawrence Hecht contributed to this post. NOTE: The post was updated on February 24 to reflect revised Docker Hub rate limits. *
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)