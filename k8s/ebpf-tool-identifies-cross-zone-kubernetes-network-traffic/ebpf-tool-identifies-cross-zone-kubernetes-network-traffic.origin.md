# eBPF Tool Identifies Cross-Zone Kubernetes Network Traffic
![Featued image for: eBPF Tool Identifies Cross-Zone Kubernetes Network Traffic](https://cdn.thenewstack.io/media/2025/01/241cafef-poh-wei-chuen-boyqvkeveg4-unsplash-1024x683.jpg)
Like most cloud providers, Google does not charge users for networking traffic within a single availability zone. Google currently has [124 availability zones](https://cloud.google.com/about/locations), which are spread out over 41 regions.

Packets traveling across zones, however, have to pay a gatekeeper. At last check, packets traveling between the U.S. and Europe cost $0.05 per GB, and Europe to/from Asia, $0.08. It can add up quickly.

By the nature of its monitoring service, Polar Signals has an immense amount of Kubernetes cross-zone network traffic. [Polar Signals Cloud](https://www.polarsignals.com/docs/overview) is a hosted service to store and analyze continuous profiling data of users’ systems.

Continuous profiling collects data on the current stack from every process in a network infrastructure. And though it uses a relatively low sampling rate, user data still builds up, quick. By mid-2024, cross-zone traffic accounted for nearly half of the company’s [Google Cloud](https://cloud.google.com/?utm_content=inline+mention) bill.

With no tools that could measure cross-zone Kubernetes traffic specifically, company engineers built a monitor that was instrumental in cutting cross-zone traffic bills by 50%, according to a [case study](https://ebpf.foundation/case-study-polar-signals-uses-ebpf-to-monitor-internal-cross-zone-network-traffic-on-kubernetes-reducing-these-operating-costs-by-50/) posted Thursday by the [eBPF Foundation](https://thenewstack.io/ebpf-finds-a-home-with-a-new-foundation/).

The secret sauce? eBPF.

## eBPF to the Rescue
At first, the company turned to commercial and open source network monitoring tools to characterize this traffic. For its commercial platform, the company uses [Kubernetes](https://thenewstack.io/Kubernetes/) and [Cilium](https://cilium.io/) for container network management.

For Kubernetes, the [kubectl](https://thenewstack.io/kubecost-monitor-kubernetes-costs-with-kubectl/) has the *top nodes* command, which could deliver reports on network traffic (transmit and receive bytes) at the node level. Also, integrated into the [Kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet) is [cAdvisor](https://thenewstack.io/wavefront-monitors-containers/), which collects data on network traffic.

None of these tools, however, could easily identify the network traffic crossing across multiple Google zones. Cilium itself could only report daily aggregated costs of network traffic, with no granularity at the pod or workload level.

So, the company built one itself, using eBPF.

The company was no stranger to [eBPF](https://thenewstack.io/ebpf-is-coming-for-windows/). The company had already created memory tracker tool for its customers, called [Parca](https://www.parca.dev/), which uses[ eBPF](https://thenewstack.io/what-is-ebpf/).

eBPF is a new [Linux](https://thenewstack.io/introduction-to-linux-operating-system) kernel technology that has been generating interested across system providers over the past few years. It is, in effect a [sandbox environment](https://thenewstack.io/how-ebpf-turns-linux-into-a-programmable-kernel/) that runs within the [Linux kernel](https://thenewstack.io/linux-kernel-6-12-is-official-real-time-app-support-better-scheduling/) with minimal overhead.

Small[ eBPF programs](https://thenewstack.io/linux-technology-for-the-new-year-ebpf/) are triggered by hooks, or events, within the kernel, such as system calls or network events.

The initial requirements to build such a program consisted of the following:

- Accurately monitor and log cross-zone traffic,
- Integrate seamlessly with Kubernetes metadata,
- Provide real-time metrics.
## Introducing Kubezonnet
The resulting open source program, [Kubezonnet](https://github.com/polarsignals/kubezonnet) (KUBErnetes cross-ZONe NETwork monitoring), was released last week.

Built by four Polar Signals engineers, Kubezonnet monitors and measures Google cross-zone network traffic generated and consumed by Kubernetes clusters.

It was eBPF’s programmability, as well as its integration with Kubernetes metadata, that allowed Polar Signals to develop software specifically for monitoring pod traffic.

The software is deployed on Kubernetes, so installing it is as simple as applying the manifest. It requires [Cilium CNI](https://thenewstack.io/cilium-cncf-graduation-could-mean-better-observability-security-with-ebpf/) to be run in legacy host routing mode and a Linux Kernel 6.4 or above, for [Netfilter](https://blogs.oracle.com/linux/post/introduction-to-netfilter), a Linux kernel network traffic filter introduced in that edition.

The software uses eBPF to trace network packets and aggregate traffic data.

Kubezonnet has two components: an agent and a server.

An agent is deployed on each node.

As the engineers explained, Kubezonnet uses Netfilter post-routing hooks to trace the network packets leaving pods, aggregating traffic data over 10-second intervals.

The collected data is sent to a central server, or set of servers, which resolves the source and destination IPs to Kubernetes pods and nodes. This is the process determines the zones of the nodes to identify cross-zone traffic.

The statistics are exposed as [Prometheus metrics](https://thenewstack.io/prometheus-at-10-whats-been-its-impact-on-observability/) to monitor total cross-zone traffic by pod, as well as through flow logs to provide detailed insights into traffic patterns between specific pods.

Servers can be deployed on each cluster, or for each zone.

The software can produce metrics, such as the top 20 pods by cross-zone network traffic-per-second in the prior five minutes, as measured in megabytes.

It can also do cumulative amounts, such as the top 20 pods by cross-zone network traffic in the last week, as measured in gigabytes. Cumulatives such as this one can more useful in trying to suss why the cloud bill went through the roof.

## How Polar Signals Cut Cross-Zone Traffic
Deploying Kubezonnet on its own network, Polar Signals identified areas where cross-zone traffic appeared to be excessive.

One culprit were the databases.

Database traffic “was previously hard to detect because many services interact with the main database and many services move a lot of bytes over the network,” wrote Polar Signals founder [Frederic Branczyk](https://www.brancz.com/), in a [blog post](https://www.polarsignals.com/blog/posts/2025/01/09/introducing-kubezonnet) explaining the technology.

The flow logs revealed a single workload dominating the traffic. Fixing this issue was trivial, Branczyk wrote.

The largest boundary busters, however, were the many rule evaluations that traveled across the company’s monitoring stack. A bit of re-engineering mitigated this traffic jam; engineers simply set up a [Thanos stack](https://thenewstack.io/thanos-takes-scalable-highly-available-prometheus-monitoring-to-cncf-incubation/) in each zone, which not only cut traffic but improved the robustness of the monitoring system through redundancy.

Going forward, the company plans to set up an alert system so that engineers are notified when certain network thresholds are hit, preventing any surprisingly large cloud bills in the future. It also plans to build support for [IPv6](https://thenewstack.io/why-is-ipv6-adoption-slow/), as well add in even more traffic metrics.

Do you want to know how much of your Kubernetes traffic ([expensively](https://thenewstack.io/finops/)) travels across your cloud providers’ availability zones? Kubezonnet could help.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)