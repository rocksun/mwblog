# Kubernetes 1.31 Arrives with New Support for AI/ML, Networking
![Featued image for: Kubernetes 1.31 Arrives with New Support for AI/ML, Networking](https://cdn.thenewstack.io/media/2024/08/05686cc8-kubernetes-1-31-1024x683.png)
Normally, a software release with a lot of [version numbers](https://thenewstack.io/rustlangs-semantic-versioning-still-breaks-too-many-apps/) in it isn’t what’s considered a [“major” release](https://thenewstack.io/tricks-api-versioning/). That’s known as a “point” release. The big ones are usually relegated to simple X.0 or XX.0 designations.

Well, don’t be fooled by overlooking Kubernetes’ v1.31.0, which became generally available today. Its release leader, [Angelos Kolaitis](https://github.com/neoaggelos), says he considers this a “major minor release,” and that it’s important enough to warrant more than cursory attention.

[Kubernetes](https://www.thenewstack.io/Kubernetes), also known as K8s and [originally developed](https://thenewstack.io/how-the-kubernetes-community-celebrated-its-10th-anniversary/) by [Google](https://cloud.google.com/?utm_content=inline+mention), is an open source platform designed to automate the deployment, scaling and management of containerized applications. It has skyrocketed in popularity and production use in IT systems in the last decade.
This latest edition (Kubernetes churns out three versions a year on a disciplined schedule) represents significant advancements in support of [AI/ML workload processing](https://thenewstack.io/ai/) and in [networking](https://thenewstack.io/networking/) generally, Kolaitis said.

**New Attributes of Kubernetes 1.31.0**
For support of AI/ML workloads, v1.31.0 introduces a volume type for [(OCI) images](https://thenewstack.io/how-bumblebee-eases-ebpf-observability-with-oci/), which enables developers to easily change a large language model used in a workload by simply changing out its image. OCI images are now used as volume sources in Kubernetes, so changing models or model weights is simplified.

“Developers using one particular model now can just change some OCI elements in the same way that they already know how to change images – for deployments when you want to upgrade or when you want to try something new. This is a very familiar process,” Kolaitis said.

OCI ([Open Container Initiative](https://thenewstack.io/open-container-initiative-creates-a-distribution-specification-for-registries/)) refers to a set of open standards and specifications that govern the creation, distribution and execution of container images.

The new edition exposes information about hardware devices used by pods, such as GPUs, in a more standardized and efficient way. Finally, it provides initial support for the new Device Resource Assignment (DRA) feature, which helps standardize the process of accessing and managing hardware accelerators, such as GPUs.

In networking, v1.31.0 improves Kube-proxy, a critical network component responsible for service discovery and load balancing within a cluster, with a new nftables bucket, which helps address performance limitations. Buckets are used to implement rate limiting and traffic-shaping mechanisms in nftables. They help prevent network congestion, ensure fair bandwidth allocation and protect against potential attacks, such as denial of service (DoS).

The new edition also continues to streamline and stabilize its core networking components, providing more reliability and robustness without requiring changes from users, Kolaitis said.

**What Does DRA Do?**
The Device Resource Assignment (DRA) feature is an important step forward in standardizing the process of accessing hardware accelerators, Kolaitis said. DRA enables the allocation and management of hardware devices, such as GPUs, field-programmable gate arrays (FPGAs) or network interface cards (NICs), to specific pods much more efficiently.

Key data points about DRA:

**Device plugins:**Kubernetes DRA uses device plugins to interface with the underlying hardware and make devices discoverable by the cluster.**Resource management:**Once devices are recognized, they become manageable resources within Kubernetes, similar to CPU or memory.**Pod assignment:**Users can request specific devices or device quantities in their pod specifications, and Kubernetes’ scheduler attempts to place those pods on nodes with matching available devices.**Exclusive access:**DRA ensures exclusive access to assigned devices, preventing multiple pods from contending for the same hardware resource.**Extended resource API:**The extended resource API in Kubernetes enables the representation and allocation of these specialized hardware devices.
## Other Improvements in Kubernetes 1.31
Other improvements in v1.31.0 include:

- Kubernetes support for AppArmor is now GA.
- Persistent Volume last phase transition time feature moved to GA in v1.31.
- The nftables backend moves to beta in v1.31, behind a newly added feature gate.
- Traffic distribution for Services moves to beta in v1.31 and is enabled by default.
- New restrictions included on anonymous API access.
[Go here](https://deploy-preview-47281--kubernetes-io-main-staging.netlify.app/blog/2024/08/13/kubernetes-v1-31-release/) to access the complete blog post detailing the v1.31.0 release.
[Go here](https://github.com/kubernetes/sig-release/tree/master/releases/release-1.31) for the GitHub release notes.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)