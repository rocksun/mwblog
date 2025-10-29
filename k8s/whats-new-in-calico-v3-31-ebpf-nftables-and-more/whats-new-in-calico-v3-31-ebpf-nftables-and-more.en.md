We’re excited to announce the release of Calico v3.31,  🎉 which brings a wave of new features and improvements.

For a quick look, here are the key updates and improvements in this release:

* [Calico NFTables Dataplane is now Generally Available](#calico-nftables)
* [Calico eBPF Dataplane Enhancements](#calico-ebpf)
  + **Simplified installation:** new template defaults to `eBPF`, automatically disables `kube-proxy` via `kubeProxyManagement` field, and adds `bpfNetworkBootstrap` for auto API endpoint detection.
  + **Configurable cgroupv2 path:** support for immutable OSes (e.g., Talos).
* [Calico Whisker (Observability Stack)](#calico-whisker)
  + Improved UI and performance in Calico v3.31.
  + New policy trace categories: **Enforced** vs **Pending**.
  + Lower memory use, IPv6 fixes, and more efficient flow streaming.
* [Networking & QoS](#networking)
  + New bandwidth and packet rate QoS controls across all dataplanes.
  + DiffServ (`DSCP`) support: prioritize traffic by marking packets (e.g., `EF` for VoIP).
  + Introduces new `QoSPolicy` API for declarative traffic control.
* [Encapsulation & Routing](#encapsulation)
  + **Tech Preview:** Felix now handles encapsulation routes (`IP-in-IP`, `no-encap`) directly — no BIRD required!
* [NAT Control](#nat-control)
  + New `natOutgoingExclusions` config for granular NAT management.
  + Choose between `IPPoolsOnly` or `IPPoolsAndHostIPs` for flexibility.
* [BGP Enhancements](#bgp)
  + Support for custom local ASNs per peer, enabling `eBGP` and advanced route reflector setups.
* [Performance & Usability](#performance)
  + Even faster IP Address Management startup.
  + Reduced memory usage and improved selector indexing.
  + New `calicoctl validate` command to validate Calico resources offline and in CI/CD pipelines.
  + `AutoHostEndpoint` now supports both `InterfaceCIDRs` and `InterfaceSelectors`.

## Calico NFTables is now Generally Available (GA)!

VIDEO

We’re excited to announce that Calico’s `NFTables` data plane is now GA! As more Linux distributions adopt `NFTables` as the netfilter tool of choice, it’s clear that `NFTables` is becoming the successor to `IPTables` in cloud native networking.

Calico users have already been testing and adopting the `NFTables` data plane through our tech preview with Calico v3.29, and in this release we are making our `nftables` data plane GA. Compared to its predecessor, `iptables`, `NFTables` brings significant improvements in efficiency and performance by streamlining how networking changes are programmed in the Linux kernel, helping you run Kubernetes networking and security at scale with less overhead.

![kube-proxy ipvs vs nftables latency]()![kube-proxy ipvs vs nftables latency](https://www.tigera.io/app/uploads/2025/10/kube-proxy-ipvs-vs-nftables-latency-blog.png)

## Calico eBPF data plane

Calico v3.31 makes installation easier and more automated. The new installation template defaults to the `eBPF` data plane, automatically disables `kube-proxy` via the `kubeProxyManagement` setting, and uses `bpfNetworkBootstrap` to detect API server endpoints automatically. It also supports dynamic `cgroupv2` paths, improving compatibility with immutable operating systems like `Talos Linux`. If you want a step-by-step walkthrough, check out the following video:

VIDEO

### eBPF based installation resource

VIDEO

With Calico v3.31, installing the `eBPF` data plane using the Calico Operator on kubeadm-based Kubernetes clusters is now seamless. It no longer requires any manual steps. Simply use the new `eBPF` installation template.

* 📄 `eBPF` template: A new installation template now defaults to using `eBPF` as the data plane, reducing manual configuration.
* 🔑 New installation options: it’s now simpler to install directly with the `eBPF` data plane:

1. **`kubeProxyManagement`:** Automatically disables `kube-proxy`, since Calico `eBPF` fully replaces it.
2. **`bpfNetworkBootstrap`:** In an environment where `kube-proxy` exists before installing Calico, Calico learns the `kubernetes` service endpoints and programs the endpoints into the `eBPF` data plane automatically so that no manual configuration is needed.

This simplifies the installation/migration process and ensures that Calico’s `eBPF` data plane is configured optimally with minimal manual steps.

```
spec:
  calicoNetwork:
    bpfNetworkBootstrap: Enabled
    kubeProxyManagement: Enabled
...
```

### Configurable cgroupv2 path

VIDEO

Immutable Linux distributions are becoming increasingly popular, and each has its own way of managing system resources and storage. In Calico v3.31, we’ve added a new Felix configuration field:

* **`cgroupV2Path`:** Allows you to specify a custom cgroup mount path, improving `eBPF` compatibility with immutable OSes such as `Talos Linux` and others.

This ensures Calico’s `eBPF` data plane runs smoothly across a wide range of modern OS environments, making adoption easier and more reliable.

```
apiVersion: crd.projectcalico.org/v1
kind: FelixConfiguration
metadata:
 name: default
spec:
 cgroupV2Path: "/sys/fs/cgroup"
```

## Calico Whisker (Calico Observability Stack)

VIDEO

Whisker has quickly become a favourite in our community, with users loving its intuitive UI. In Calico v3.31, we’re taking it a step further by improving UI for policy traces, reduced memory use, IPv6 binding fixes, and more efficient flow streaming in Goldmane. Now, policies evaluated for each flow are clearly categorized into two groups:

* **Enforced**: Policies that are currently active and shaping traffic flows.
* **Pending**: If a flow matches a staged network policy, then the pending row will be populated by all the policies that could be applied to that flow if the staged network policy is enforced. The policies that would be enforced on any new connections matching this flow, if all staged policies were enforced.

## Networking

### Calico Bandwidth Management Quality of Service (QoS)

VIDEO

New burst and peak rate controls for bandwidth and packet rate QoS are now available in Linux multiple dataplanes: `eBPF`, `IPTables`, and `NFTables`.

These improvements give operators finer control and faster responsiveness when managing traffic QoS in OpenStack and Kubernetes environments.

```
annotations:
   # Bandwidth peakrate and minburst
   qos.projectcalico.org/ingressPeakrate: "1000000"   # in bits per second
   qos.projectcalico.org/egressPeakrate: "500000"     # in bits per second
   qos.projectcalico.org/ingressMinburst: "1500"      # defaults to MTU if lower
   qos.projectcalico.org/egressMinburst: "1500"

   # Packet rate limits with burst
   qos.projectcalico.org/ingressPackets: "1000"       # packets per second
   qos.projectcalico.org/egressPackets: "800"         # packets per second
   qos.projectcalico.org/ingressPktBurst: "200"       # burst packets
   qos.projectcalico.org/egressPktBurst: "200"
```

## Traffic classification

In Calico v3.31, we’re expanding Quality of Service (QoS) capabilities with Differentiated services (`DiffServ`) support for workloads and `hostendpoints`.

This enhancement allows you to classify and prioritize traffic leaving your cluster, ensuring that critical traffic is prioritized even when it leaves your cluster.

By setting the `qos.projectcalico.org/dscp` annotation on a Calico `hostendpoint`, Calico can apply the appropriate DSCP marking to egress packets. Think of it like slapping a VIP badge on your packets, no lineups—straight to the fast lane of your QoS-aware network.

This update introduces a new DSCP type supporting both numeric values (0–63) and common string values, and corresponding data plane logic to enforce DSCP marks in multiple dataplanes. Because DSCP is embedded in the 6-bit IP packet header, downstream devices in your network can use these markings for forwarding and prioritization, making it easier to integrate Kubernetes workloads into existing QoS-aware environments.

### How it works

* DSCP support for both numeric values (0–63) and string names (AF11, EF, CS5).
* New `QoSPolicy` API for Kubernetes-native traffic control.
* Enforced via data plane using `iptables` or `nftables`.

### Why it matters

* Prioritize critical workloads: latency-sensitive traffic like video or trading gets expedited handling.
* Simplify configuration: declaratively set QoS in manifests instead of manual DSCP configs.
* Future-ready: works across both `iptables` and `nftables` dataplanes.

```
apiVersion: projectcalico.org/v3
kind: HostEndpoint
metadata:
  name: hep-with-dscp
  annotations:
    qos.projectcalico.org/dscp: "cs5"

```

**Visualizing the impact:**

* 🟢 Video/Voice traffic → prioritized with EF
* 🔵 API traffic → marked with AF21
* ⚪ Batch jobs → default BE

## Encapsulation Routes programmed direct from Felix

Encapsulation isn’t new to Calico, but in v3.31, Felix takes over responsibility for IP-in-IP and no-encapsulation routing. Previously, BIRD handled this through BGP. Moving it into Felix simplifies operations, reduces dependencies, and speeds up live upgrades in large clusters.

```
apiVersion: crd.projectcalico.org/v1
kind: FelixConfiguration
metadata:
 name: default
spec:
 programClusterRoutes: Enabled

```

## Granular control over natOutgoing (A Community Contribution!)

Calico v3.31 introduces finer control over NAT outgoing. Previously, enabling `natOutgoing` SNATed all traffic leaving an IPPool, including local cluster traffic. Now, Felix introduces `natOutgoingExclusions`:

* **IPPoolsOnly** (default): Only traffic leaving the IPPool is SNATed.
* **IPPoolsAndHostIPs**: Both traffic leaving the IPPool and traffic to cluster hosts are SNATed.

Example patch command:

```
kubectl patch felixconfiguration --type=merge default -p='{"spec":{"natOutgoingExclusions":"IPPoolsAndHostIPs"}}'

```

## BGP Enhancements

Previously, Calico used the node’s global ASN for all BGP sessions. Now, you can override per peer, unlocking scenarios like eBGP with external routers and route reflector designs.

```
kind: BGPPeer
apiVersion: projectcalico.org/v3
metadata:
  name: asn_override
spec:
  asNumber: 64516
  localASNumber: 65002

```

## Performance & Usability

* **Faster IPAM:** Efficient server-side filtering speeds IP allocation in large clusters (1000+ blocks).
* **Parallel Startup:** Felix now loads BPF programs in parallel, reducing startup latency.
* **Memory Optimization:** Deduplicates resource label keys/values to reduce memory usage at scale.
* **Security & Compliance:** TLS ciphers now configurable for enterprise needs.
* **Performance Improvements:** Selector index deduplication, parallel BPF program loading, reduced memory usage.
* **`calicoctl validate`:** Validate input locally without applying changes.
* **AutoHostEndpoint:** Supports `InterfaceSelectors` and new `InterfaceCIDRs` option to match node IPs precisely.

Check out the full list of improvements in OpenStack and OpenShift in our [release notes](https://docs.projectcalico.org/release-notes/v3.31).

[Click here](https://demo.arcade.software/SZ028sCkdnwA8SF1Idlq?embed) to try Calico v3.31 Whisker UI Improvements in your browser