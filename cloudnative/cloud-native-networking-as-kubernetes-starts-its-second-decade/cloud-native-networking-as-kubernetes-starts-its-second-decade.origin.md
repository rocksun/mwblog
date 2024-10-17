# Cloud Native Networking as Kubernetes Starts Its Second Decade
![Featued image for: Cloud Native Networking as Kubernetes Starts Its Second Decade](https://cdn.thenewstack.io/media/2024/10/1de4f71f-networking-1024x576.jpg)
Kubernetes recently [turned 10.](https://kubernetes.io/blog/2024/06/06/10-years-of-kubernetes/) After all the celebrations over the course of the summer, I feel obliged, as a father of three, to forewarn Kubernetes administrators and operators: tweenagers are not easy to deal with.

Expect [Kubernetes](https://roadmap.sh/kubernetes) to enter its rebellious phase.

It will experience awkward growth spurts (as new use cases force Kubernetes to adapt); it might go through an identity crisis (is it a platform or is it an API?); it will ask for less supervision and more independence (and rely on AI-driven tooling to require less direct human oversight).

As Kubernetes matures into adolescence, let’s consider how its networking and security circulatory systems grow and adapt. With [KubeCon North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) in Salt Lake City soon approaching, I thought I’d review its session schedule and provide some observations and predictions on the future of cloud native networking.

## eBPF Will Be Ever-Present
The momentum behind [eBPF](https://ebpf.io/), the technology that lets you run custom programs within the Linux (and, soon, [Windows](https://thenewstack.io/ebpf-is-coming-for-windows/?utm_source=tldrdevops)) kernel, is not stopping. Beyond networking and security (and the [Cilium](https://cilium.io/) and [Tetragon](https://tetragon.io/) projects I work on), more use cases are emerging as you will learn during KubeCon:

- Measuring
[power consumption](https://sched.co/1iW8V): Let’s use eBPF. [Introducing chaos](https://youtu.be/_5Zabryx0nE?si=KhGFMmeay9LtoJ_-)to verify the resiliency of our environment: Let’s use eBPF.- Accelerating
[encrypted traffic](https://sched.co/1i7lP): Let’s use eBPF. [Detecting anomalies](https://sched.co/1i7ms)in high-volume encrypted traffic: Let’s use eBPF.
Will we get to the stage when not choosing eBPF as a platform to run networking programs is going to be an anomaly? I sincerely hope not: Although [eBPF is a powerful hammer](https://thenewstack.io/ebpf-security-power-and-shortfalls/), we shouldn’t treat every networking problem as a nail.

## The Coolest Kids Get Together: eBPF Meets OpenTelemetry
There’s one particular use case where eBPF’s ability to hook into every packet is powerful: network visibility.

OpenTelemetry continues to be one of the [most active Cloud Native Computing Foundation (CNCF) projects](https://www.cncf.io/reports/opentelemetry-project-journey-report/), only behind Kubernetes and just ahead of Cilium. OpenTelemetry provides a standard observability framework to create and manage telemetry data through simple instrumentation of applications.

Given that the network is often blamed for application performance, it’s encouraging to see efforts like [OpenTelemetry Network](https://sched.co/1how7), which uses eBPF to capture low-level telemetry straight from the Linux kernel. When the best observability tooling meets the most efficient Linux kernel tech, expect to see valuable insights into the health of your applications.

## Looking Back Before Looking Forward
After 10 years, we can look back at some of the design decisions made around Kubernetes networking and reflect whether they were correct or need to be rethought.

The Ingress API is an example of a Kubernetes choice that, while widely adopted, needed rethinking, with Gateway API its designated successor (more on that below).

Service meshes are also evolving from their bloated sidecar-based architecture to the sidecar-less approach proposed by [Cilium Service Mesh](https://isovalent.com/blog/post/cilium-service-mesh/) and Istio Ambient Mesh. The Istio community is feeling particularly introspective: The Istio leaders [can now look back at some of the decisions made](https://sched.co/1i7nP) and how they influenced its development and its future.

Perhaps the 10-year milestone is why we all feel in a reflective mood: Even the Kubernetes SIG-Network group is considering moving on from the [container network interface plugin model](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/). While the CNI has been the foundation of the Kubernetes networking model, it actually precedes Kubernetes.

Should we instead adopt a new framework — [Kubernetes Network Interface](https://github.com/kubernetes/enhancements/issues/4410) (KNI) is moot — designed for Kubernetes instead? Or should we just let CNI evolve to its 2.0 iteration? We should find out more in the “[CNI Update and Directions” session](https://sched.co/1how8).

## Time to Sunset the Ingress
[Gateway API](https://gateway-api.sigs.k8s.io/) is one of my favorite projects in the Kubernetes ecosystem, not just because it addresses some of the shortcomings in its predecessor, [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/), but because of the collaborative and inclusive nature of its development and maintenance.
Gateway API provides a new standard on load balancing and connectivity into and within Kubernetes clusters. With [nearly 30 implementations of Gateway API](https://gateway-api.sigs.k8s.io/implementations/) and its adoption steadily increasing as it soon reaches the 1.2 milestone, this year’s KubeCon Gateway API sessions go beyond introductory sessions. They will provide lessons learned on [Gateway API deployments](https://thenewstack.io/multicluster-deployment-strategies-with-the-kubernetes-gateway-api/).

The Ingress had a good run, but it’s time to move on: Even the maintainers of the very popular [NGINX ](https://www.nginx.com?utm_content=inline+mention)Ingress [expect new features and functionalities to only be built on their Gateway API implementation](https://sched.co/1hoxW).

In the [session previewing the future of Gateway API](https://sched.co/1hoxF), expect to see how Gateway API will finally close the gap with the remaining Ingress features so we can say goodbye once and for all.

## AI for Kubernetes Networking
Whenever I discuss [AI and networking](https://www.youtube.com/watch?v=mUbeiDF2B4k), I always prefer to break it down into “networking for AI workloads” and “AI to improve networking.” Let’s start with the latter.

As someone who works on what is considered the de facto CNCF cloud native network layer, Cilium, I’ve experimented with large language models (LLMs) to create networking policies and analyze logs. The results with both [Ollama](https://ollama.com/) and ChatGPT were inconsistent, to say the least. I’m looking forward to seeing whether [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) principal network engineer Doug Smith has more success in his “[A Mad Scientist’s Guide to Automating CNI with Generative AI](https://sched.co/1i7kI)” tutorial.

More broadly, I am hoping that AI will enable Kubernetes to make smarter networking decisions. While the Kubernetes scheduler is capable of placing workloads based on their memory and CPU requirements and usages, it generally lacks networking awareness. What if a bandwidth-hungry workload was automatically placed with workloads with minimal networking demand? Could network policies be automatically generated and enforced based on observed network traffic?

I imagine all these use cases will be a reality within the next couple of years.

## Kubernetes Networking for AI
Should we evolve Kubernetes networking to cater for the emerging AI workloads?

I’ve written before about how [AI workloads are imposing significant pressure on networks](https://isovalent.com/blog/post/cilium-the-network-and-security-platform-for-the-cloud-native-ai-era/). Kubernetes is clearly becoming the platform of choice to run AI/ML applications across clusters of GPUs. But AI workloads require not only access to local GPUs but also remote GPUs through remote direct memory access ([RDMA](https://en.wikipedia.org/wiki/Remote_direct_memory_access#:~:text=In%20computing%2C%20remote%20direct%20memory,in%20massively%20parallel%20computer%20clusters.)).

Could we use Kubernetes’ recent dynamic resource allocation ([DRA](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)) feature to request access to specialized hardware for networking purposes? That’s what the [Kubernetes Network Drivers](https://github.com/aojea/kubernetes-network-driver) (KND) project is proposing. It may or may not be adopted, but it bravely attempts to make Kubernetes fit for its second decade.

## Final Thoughts
Yes, Kubernetes will go through a teenager’s emotional changes. But it’s OK; it will have the support and guidance of a community that remains welcoming, supportive and determined to keep innovating to ensure Kubernetes grow into a well-balanced adult.

*To learn more about Kubernetes and the cloud native ecosystem, join us at **KubeCon + CloudNativeCon North America**, in Salt Lake City, Utah, on Nov. 12–15.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)