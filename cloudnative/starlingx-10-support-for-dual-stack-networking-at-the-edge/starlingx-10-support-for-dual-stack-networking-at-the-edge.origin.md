# StarlingX 10: Support for Dual-Stack Networking at the Edge
![Featued image for: StarlingX 10: Support for Dual-Stack Networking at the Edge](https://cdn.thenewstack.io/media/2025/02/9815d818-starling-x-2-1024x576.jpg)
StarlingX has always been a great edge-computing cloud platform, but it can also be helpful in the core.

[StarlingX](https://www.starlingx.io/), the open source distributed cloud platform, has officially launched its much-anticipated version [10.0](https://docs.starlingx.io/releasenotes/index.html), marking a significant milestone in its evolution. Released Wednesday, this update brings many new features and enhancements to improve performance and user experience across various applications, particularly in [Internet of Things (IoT)](https://thenewstack.io/the-internet-of-things-on-the-edge/), 5G, and [edge computing environments](https://thenewstack.io/edge-computing/).
One of StarlingX 10.0’s standout features is its support for IPv4/IPv6 dual-stack networking. This enhancement allows users to operate both protocols simultaneously, ensuring compatibility as the industry transitions from IPv4 to IPv6, which is ongoing in many sectors.

While StarlingX has long-supported IPv6 networking, until now it didn’t work with dual network stacks. Now, “The latest enhancements now allow users to switch between single-stack and dual-stack networking configurations to allow [using both IPv4 and IPv6 address spaces](https://www.starlingx.io/blog/starlingx-release-10/),” wrote [Ildikó Váncsa](https://www.linkedin.com/in/ildiko-vancsa), the [Open Infrastructure Foundation](https://openinfra.org/)‘s director of community, in a post on the StarlingX blog,

Since StarlingX is often used by telecoms, whose data centers still often run IPv4 while their 5G mobile networks rely on IPv6, this new dual-stack support is a valuable addition.

## A New Framework To Simplify Deployment
This latest release also boasts a new Unified Software Management Framework, which simplifies the platform’s deployment and management. Users can now perform updates and upgrades through a single interface, accessible via REST API or CLI, streamlining operations for single and distributed cloud installations.

Specifically, the framework uses [OSTree](https://github.com/ostreedev/ostree) to install new software while the host continues running on the existing file system. Thus, a simple reboot then transitions to the new software, significantly reducing downtime compared to previous methods. It also enables simultaneous deployment of patches and updates. In short, this is a pure win.

Under the hood, StarlingX 10.0 includes an upgrade from its underlying [Linux kernel version 5.10 to 6.6](https://thenewstack.io/linux-kernel-6-12-is-official-real-time-app-support-better-scheduling/). This change enhances performance and expands support for a broader range of hardware platforms and device drivers. This update is based on the latest Long Term Support (LTS) [Yocto Linux distro](https://www.yoctoproject.org/) release. Yocto is a well-regarded, customizable embedded Linux.

As a result, the platform’s scalability has been significantly improved. It can now manage up to 5,000 remote sites per system controller, up from 1,000 in previous versions. This enhancement is crucial for large-scale deployments, making it easier to operate extensive networks.

## Enhanced Kubernetes Support
This release also comes with [Kubernetes’ Harbor](https://goharbor.io/) as its container registry. Harbor is an open source registry. It secures artifacts with policies and [role-based access control (RBAC)](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/). Harbor also ensures images are scanned and free from vulnerabilities; it also signs images. This enables users to securely manage cloud native artifacts such as container images and Helm charts.

As you’d expect, StarlingX continues integrating newer versions of various open source projects, including [Kubernetes](https://roadmap.sh/kubernetes) up to version 1.29, ensuring users can access the latest technologies within the platform.

The improved Kubernetes support is important because StarlingX relies on a Kubernetes service, [NUMA-aware Memory Manager](https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/), to prevent worst-case memory latency. This memory slowdown can happen when StarlingX’s cores run under a high load.

While all this strengthens StarlingX’s hand as an edge cloud, it would be a mistake to “pigeon-hole” StarlingX as an edge cloud, said [Paul Miller](https://www.linkedin.com/in/telecomcto/), CTO of [Wind River](https://www.windriver.com/), which commercially supports the project.

“Every single piece of cloud infrastructure in the [Boost Mobile](https://www.boostmobile.com/) network from the core to the center, over 20,000 sites, [is] all based on StarlingX” via [Wind River Studio Operator](https://www.windriver.com/studio/operator), Miller told The New Stack.

He’s not the only one happy with StarlingX’s latest changes. “We are delighted to see the launch of StarlingX 10.0,” said [Shuquan Huang](https://www.linkedin.com/in/shuquan-huang-a8b13b66), technical director of [99Cloud](https://www.99cloud.net/), an open source cloud provider, in a statement. “This release is a pivotal achievement in our quest to offer an enterprise-grade, open source distributed edge cloud platform.”

Those interested in exploring the new features or deploying StarlingX 10.0 can now download pre-built [Debian Linux ISO from the StarlingX repos](https://mirror.starlingx.windriver.com/mirror/starlingx/release/10.0.0/debian/monolithic/outputs/iso/). If you haven’t used StarlingX before, I highly recommend that you first go over the [project documentation](https://docs.starlingx.io/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)