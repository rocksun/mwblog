# Can Cilium Be a Control Plane Beyond Kubernetes?
![Featued image for: Can Cilium Be a Control Plane Beyond Kubernetes?](https://cdn.thenewstack.io/media/2024/07/09b8afdd-can-cilium-be-a-control-plane-beyond-kubernetes-copy-2-1024x576.png)
SEATTLE – [Thomas Graf](https://www.linkedin.com/in/thomas-graf-73104547), one of the creators of [Cilium](https://thenewstack.io/cisco-gets-cilium-what-it-means-for-developers/), sees the cloud native security market changing, with the widespread adoption of containers used for AI APIs and new approaches to microsegmentation.

Cilium, a [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) graduate, is built on [eBPF](https://thenewstack.io/what-is-ebpf/) (extended Berkeley Packet Filter). Graf also helped develop [NSX](https://thenewstack.io/global-speech-networks-embraces-software-defined-networking-vmware-nsx/) and Open vSwitch at Nicira, which [VMware](https://tanzu.vmware.com?utm_content=inline+mention) acquired. At the heart of NSX is software-defined networking, which turns hardware switches into software.

Wildly popular, the question about Cilium now becomes: how much success will come of it, as AI becomes more predominant? Is it a futuristic solution or a hammer looking for a nail?

I sat down at [CloudNative SecurityCon](https://events.linuxfoundation.org/cloudnativesecuritycon-north-america/) in Seattle with [Graf](https://www.linkedin.com/in/thomas-graf-73104547/), CTO, and co-founder of [Isovalent](https://thenewstack.io/ciscos-strategic-move-in-the-isovalent-acquisition-ebpf/), to discuss how Cilium fits in the broader networking landscape. We tackled the swirling questions about AI and external factors, such as how to manage the deeper complexities of microsegmentation with the mainstream adoption of containers, APIs everywhere and AI in the data.

In January, [Torsten Volk ](https://thenewstack.io/author/torsten-volk/)[wrote for The New Stack](https://thenewstack.io/cisco-gets-cilium-what-it-means-for-developers/) that Cillium extends eBPF to the transport and application layers, providing more granular and flexible control over networking and security, which is particularly beneficial in cloud native environments.

In 2022, [Isovalent open sourced Tetragon](https://thenewstack.io/isovalent-open-sources-tetragon-ebpf-based-observability-platform/), [a Kubernetes-native tool](https://tetragon.io/) that leverages [eBPF for deep observability](https://thenewstack.io/groundcover-simplifying-observability-with-ebpf/?nab=1) with minimal performance impact. Tetragon tracks a wide range of activities, including process execution, privilege escalations, and network activity. Its in-kernel runtime policies, enforced using eBPF, offer robust security postures against unauthorized actions and [time-of-check time-of-use (TOCTOU)](https://cwe.mitre.org/data/definitions/367.html) race condition attacks.

## Kubernetes Networking and AI
Isovalent now works with companies building [large language models](https://thenewstack.io/llm/) with [Kubernetes](https://thenewstack.io/kubernetes/) clusters, which have complicated networking requirements primarily due to AI workloads that are so data-heavy, Graf said.

It’s impossible to imagine how much data is needed to construct language models, he said; when a highly paid research engineer builds these language models, the models must be kept private. At the same time, data is constantly needed to be pulled in to build the models.

In the meantime, however, the complexity of securing workloads that are always susceptible to lateral attacks increases. Generative AI can be powerful, but what happens if it taints the data lake?

Against this backdrop comes the need for better observability and control planes that can manage the deluge contextually.

When we talk about AI native, we’re talking about the next generation of machine learning or adaptive learning-based policy management. You no longer want to manually create all the policies yourself. You need automation to mitigate threats. If a CVE is coming up, you need to mitigate it. You recognize a threat, and you need to automatically reject that with automation. AI, then, is simply better automation.

But what role will Cilium play in this next-generation automation?

Cilium will be a universal data plane, Graf said. Cilium’s place in the cloud native world is established and Cilium will be applicable outside of Kubernetes, the distributed data plane for the broader industry. Cisco will be able to run on switches on [DPU](https://blogs.nvidia.com/blog/whats-a-dpu-data-processing-unit/) and [SmartNICs](https://thenewstack.io/where-service-mesh-and-smartnics-meet/). And with [the most recent acquisition by Broadcom of VMware](https://thenewstack.io/vmwares-private-cloud-solution-emerges-under-broadcom/), there’s a lot of interest in replacing NSX. He sees Cilium as a foundational technology that drives replacement products for NSX.

## Is eBPF the Answer?
Can an eBPF approach serve as a cornerstone for the cloud network? It’s a big question. eBPF is like a data hose and may be great for many things, but what about Layer 7 data? It’s not meant to monitor the data that transverses across the Internet. It can handle the services that run in the kernel on a Kubernetes platform, but that’s only part of what software engineers require now with such an expansive attack surface.

But as Volk notes, Cilium, which again is built on eBPF, provides programmable control to the transport layer (Layer 4) and the application layer (Layer 7), allowing “for the enforcement of network policies via protocols such as TCP, UDP, ATP, and MTCP, which provide end-to-end communication services for applications.”

Not everyone believes that eBPF answers all network issues. [Wesley Hales](https://www.linkedin.com/in/wesleyhales/), CEO at [LeakSignal](https://www.leaksignal.com/), sees eBPF as a hammer and any network problem as a nail. In particular, Hales cites sensitive data in transit classification. But let’s save that topic for another time.

## Cloud Native Security: Point vs. Platform
Earlier this year, [Cisco](http://cisco.com/?utm_content=inline+mention) [acquired Isovalent](https://thenewstack.io/ciscos-strategic-move-in-the-isovalent-acquisition-ebpf/). With an eBPF approach embodied in Cilium, I asked Graf how he views the cloud native security landscape, the role of the service mesh, micro-segmentation, and what covalent means for Cisco.

**Alex Williams: Tom, what does the full solution for cloud native security look like? What do customers need? **
**Thomas Graf:** Yep. So, starting at an application’s source, you need a solution that scans your source code and finds vulnerabilities in it.
Ideally, a code graph will tell you which vulnerabilities are reachable in your code. Then, you need solutions to secure the supply chain of your dependencies: vulnerability management. If you use libraries with [common vulnerabilities and exposures], you need to be able to track and fix them. Then, you need cloud posture management for your infrastructure. If your [virtual private cloud] is wide open, you’re not using security groups.

It would be best if you had a cloud posture management solution. Then, you need runtime security when you start running your applications — threat mitigation for Kubernetes for your cloud workloads. And then, of course, you need observability in all of this. Like, what are you running? What are you exposed to? What is your risk?

You need to prioritize that risk because, for most customers, there will be a very large number of findings, and you need to figure out what to look into first. Are people asking now for more comprehensive solutions? They’ve been picking up point solutions and seeing the complexity that it takes to integrate those solutions.

Most people have started with a broad solution first and then figured out that they’re not complete enough. Then, they went to point solutions, and it quickly became an absolute pain to manage because, mainly, the [[cloud native application protection platform](https://thenewstack.io/4-benefits-of-choosing-a-cnapp-for-cloud-security/)] space is not standardized with open source.

So customers are trying to go back and say, well, do we want to go back to a broad solution, or do we want to convince vendors to get broader and combine multiple-point solutions? This will be a critical discussion that will be had in the next couple of years. How do we get to a good enough solution that is also broad enough that it’s easy to manage?

## The Problems With Service Mesh
**Williams: What about the service mesh? It seems like service mesh has been a good follow-on to Kubernetes by providing that proxy capability through an API-centric environment, which you have in Kubernetes. And so it seems like a natural fit and a place, for companies to think about their overall security posture. Is that accurate? **
**Graf: **Yeah, I would say it’s accurate. I think service mesh is a nice little layer on top, and it conceptually absolutely requires that you need a logical connectivity layer that introduces identity, that is, introducing rich security mechanisms to implement [zero trust](https://thenewstack.io/what-is-zero-trust-security/) principles. The implementation on how service mesh was implemented so far was definitely not satisfying customers.
I think all vendors in the field have to do better and find a solution that is less visible, like just part of the infrastructure, instead of something that you need to actively manage. Also, the overhead and burden of running service meshes have to be dramatically lowered.

## Microsegmentation and NSX
**Williams: So why is a security solution the answer to NSX? **
**Graf:** Well, NSX is fundamentally at the core of a distributed firewall. Like just, if you look at Cilium, why is Cilium fascinating? Yes, it’s doing a lot of networking, but why it’s used is to do firewalling microsegmentation and encryption. And it’s exactly the same for NSX.
Moving the packets is almost like an implementation detail. What really matters is to do this securely. So when you buy the product, you buy it for a network security application, even though it’s clearly also just doing the connectivity. It’s almost like it’s an included detail.

Has that been a key selling point for NSX over the years? Absolutely, yes. Micro-segmentation is the primary selling point for NSX. And so now, what’s the primary selling point today? For Cilium, it’s exactly the same. A lot of NSX customers would say, well, Cilium is what NSX is, but for containers and Kubernetes, cloud native for containers, is identity-based.

So Cilium is one generation more advanced, right? It’s not just about scaling up for containers; it understands that identity is natively integrated into the cloud providers. It’s not just for [virtual machines] or virtualization, but the main applicable use case is the same.

## Cisco and Isovalent
**Williams: Thomas, we talked about these more comprehensive solutions that customers seek. What’s the Cisco Isovalent story related to that? **
**Graf:** So think. Isovalent played in the cloud native and in the Kubernetes fields very, very successfully. With Cisco, we’re now bringing the cloud native approaches we’ve built to the broader market into the data center, at the edge and to the public cloud.
So, we’ve built Cillium for network security, segmentation and cloud native networking with Tetragon runtime security, making that available in the data center, running Tetragon on servers, running Cillium on DHs, [data processing units] and switches, and essentially building a security fabric that can secure not only the Kubernetes part but your overall infrastructure.

So the security fabric fits within all of those point solutions that customers buy … And then, I think from a Cisco perspective, clearly bringing in CNAPP capability, like providing an overall rich platform that’s not just wide but also deep enough. Cisco has made significant acquisitions in the past few years to buy point solutions for each of them. and is now building a platform to unify them to give you the experience of a platform with strong point solutions in each vertical.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)