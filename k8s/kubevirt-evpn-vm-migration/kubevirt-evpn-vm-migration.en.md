Your team has moved VMs to Kubernetes with [KubeVirt](https://kubevirt.io/). The workloads are running. The team is gaining confidence. Then someone asks: can we live-migrate a VM to the other cluster?

Disaster recovery, cluster upgrades, capacity rebalancing – the reasons pile up fast. And KubeVirt’s answer appears straightforward: decentralized live migration, which landed in v1.6, should handle this.

But your network team’s answer is more complicated. The VM likely needs to keep its IP and MAC address on the destination cluster. That means a stretched Layer 2 domain between sites. In traditional infrastructure, you’re looking at new VLANs, switch configurations, and possibly even new hardware. A change window. A ticket. Weeks.

> “In traditional infrastructure, you’re looking at new VLANs, switch configurations, and possibly even new hardware. A change window. A ticket. Weeks.”

The migration technology isn’t the problem. What gets in the way, more often than not, is the network.

![Image showing four objectives: Stretched L2 networks, routing between networks, reduced BUM traffic, and seamless workload mobility.](https://cdn.thenewstack.io/media/2026/08/415e061e-image-1024x572.png)

## Why the network is the hard part

Cross-cluster live migration has two network requirements that standard Kubernetes networking doesn’t address.

First, a **stretched L2 domain**. The VM must land on the destination cluster with the same MAC and IP, on the same broadcast domain. Without this, every migration means IP reassignment, DNS updates, and broken connections. Stateful applications — think PostgreSQL clusters using synchronous replication, or message queues with persistent TCP sessions —  can’t tolerate IP changes without manual intervention.

Second, a **dedicated migration path**. Migration transfers gigabytes of memory state in real time. Pushing that through the same network carrying application traffic creates congestion, unpredictable latency, and no way to independently monitor either traffic class.

![Diagram showing the VXLAN network overlay.](https://cdn.thenewstack.io/media/2026/08/6fa0c32a-image-1024x572.png)

In traditional virtualization platforms, these are solved with dedicated [migration VLANs and proprietary virtual](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/) switch constructs: hardware-coupled, vendor-specific, and often licensed per socket. The open source equivalent needs to work as an overlay, managed declaratively, without touching the physical network.

EVPN/VXLAN provides exactly this. [OpenPERouter](https://github.com/openperouter/openperouter) makes it a Kubernetes-native resource.

## EVPN as Kubernetes CRDs

OpenPERouter manages EVPN configuration through three Custom Resource Definitions. An `Underlay` CR establishes BGP peering between each Kubernetes cluster and its top-of-rack switch. An `L2VNI` CR creates a Layer 2 overlay network, implemented by a VXLAN segment identified by a VNI number and scoped to a VRF. Finally, the `L3VNI` CR enables IP routing between different subnets and connects your cluster to external networks.

The application network uses VNI 110 in VRF “red”:

```

apiVersion: openpe.openperouter.github.io/v1alpha1
kind: L2VNI
metadata:
  name: application-net
  namespace: openperouter-system
spec:
  vni: 110
  vrf: red
  hostmaster:
    type: linux-bridge
    linuxBridge:
      autoCreate: true
  l2gatewayips: ["192.170.10.1/24"]

```

Both clusters get an identical `L2VNI` resource, and VMs on either cluster share L2 adjacency on the 192.170.1.0/24 subnet. A VM on cluster A at 192.170.1.3 can reach a VM on cluster B at 192.170.1.30 as if they were on the same switch.

The migration network is a second `L2VNI`. It uses the exact same pattern but a different VNI:

```

apiVersion: openpe.openperouter.github.io/v1alpha1
kind: L2VNI
metadata:
  name: migration-net
  namespace: openperouter-system
spec:
  vni: 666
  vrf: rouge
  hostmaster:
    type: linux-bridge
    linuxBridge:
      autoCreate: true
  l2gatewayips: ["192.170.10.1/24"]

```

All the migration network needs is a unique VNI and VRF in the L2VNI CR — in this example, `666` and `rouge` —  and the migration traffic is isolated from the application network. This overlay rides on the existing IP connectivity between sites. The VXLAN tunnel endpoints don’t even need to be on the same network segment. As long as there’s IP reachability between sites (which can traverse any number of routed hops), the overlay converges.

> “Two CRDs define what used to require a network team and a change window.”

Two CRDs define what used to require a network team and a change window.

## Operating the migration

With the network fabric in place, here’s what an [operator actually does on Day](https://thenewstack.io/kubernetes-1-35-features-that-change-day-2-operations/) 2 when a VM needs to move.

**IP** [management across clusters](https://thenewstack.io/how-amazon-eks-auto-mode-simplifies-kubernetes-cluster-management-part-1/) needs an IPAM strategy that prevents conflicts without central coordination. The examples use [Whereabouts](https://github.com/k8snetworkplumbingwg/whereabouts) with complementary exclude ranges, which means that each cluster’s Network Attachment Definition covers the same 192.170.10.0/24 subnet but excludes the other cluster’s half. Cluster A allocates from the lower range, cluster B from the upper. But Whereabouts is a design choice, not a requirement; any IPAM provider that can partition ranges across clusters works here.

**The migration itself** is three resources:

The target VM must be provisioned by the user on cluster B with `runStrategy: WaitAsReceiver` – same MAC address, same IP configuration, sitting idle until it receives the incoming migration.

Afterward, a `VirtualMachineInstanceMigration` receiver on cluster B declares readiness:

```

apiVersion: kubevirt.io/v1
kind: VirtualMachineInstanceMigration
metadata:
  name: vmim-target
spec:
  receive:
    migrationID: cross-cluster-demo
  vmiName: vm-1

```

A matching sender on cluster A points to the receiver’s migration IP (obtained from the receiver’s `.status.synchronizationAddresses`) and initiates the transfer.

```

apiVersion: kubevirt.io/v1
kind: VirtualMachineInstanceMigration
metadata:
  name: migration-source
spec:
  sendTo:
    connectURL: "&lt;receiver VMI migration .status.synchronizationAddresses[0]>:9185"
    migrationID: cross-cluster-demo
  vmiName: vm-1
EOF

```

Under the hood, migration traffic flows over VNI 666, isolated from VNI 110. The VM is copied to cluster B with its identity intact. EVPN updates MAC/IP advertisements across the fabric – traffic to the VM starts arriving at the new cluster. No DNS changes, no IP reassignment, no connection resets.

## Who owns what

The real shift here is operational, not just technical. The configuration for the BGP EVPN — that is, the overlay networks, VRFs, and VNIs  —  moves from the network team’s domain into the Kubernetes admin’s hands.

> “The operational model shifts from ‘request physical network changes and wait’ to ‘apply a CR and the overlay converges.'”

The network team still owns the underlay: IP addressing for router endpoints and links, physical connectivity, and routing between sites. That doesn’t change. But once the underlay is in place, everything above it  —  stretched L2 domains, dedicated migration networks, VRF isolation  —  is declared through Kubernetes CRDs by the same platform team managing the clusters. No tickets to the network team to add a VLAN. No change windows to stretch a broadcast domain to a new site.

The following table highlights the shift in operational responsibilities compared to traditional virtualization stacks:

|  | **Network Admin Role** | **Kubernetes Admin Role** |
| --- | --- | --- |
| **Traditional Virtualization** | Manages physical switches, VLANs, and hardware configurations for every VM movement. | Dependent on the network team for tickets and manual change windows. |
| **KubeVirt + OpenPERouter** | Sets up foundational IP connectivity, router endpoints, and links. | Manages the overlay network, BGP/EVPN configurations, and VM mobility declaratively via K8s CRDs. |

The operational model shifts from “request physical network changes and wait” to “apply a CR and the overlay converges.” Platform teams manage VM mobility the same way they manage everything else in Kubernetes: declaratively, version-controlled, reviewable.

## Getting started

The network shouldn’t be the reason VMs can’t move between clusters. EVPN overlays — managed through Kubernetes CRDs — give multi-cluster KubeVirt deployments the same VM mobility that traditional platforms offered, without the physical network dependency or the licensing model.

For step-by-step walkthroughs, see [Stretched Layer 2 Network between Clusters](https://kubevirt.io/2025/Stretched-layer2-network-between-clusters.html) and [Dedicated Migration Network for Cross-Cluster Live Migration](https://kubevirt.io/2025/Dedicated-migration-network-for-cross-cluster-live-migration.html). Ready-to-use configuration files are in the [OpenPERouter examples](https://github.com/openperouter/openperouter/tree/main/examples/evpn/multi-cluster/).

**Note:** KubeVirt is a CNCF Incubating project, accepted in September 2019 and moved to Incubating maturity in April 2022. The decentralized live migration feature referenced here has been available since v1.6 (July 2025) and remains stable in v1.8 (March 2026).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/08/437bbf11-cropped-c2a2a8d6-captain-miguel-duarte-de-mora-barroso-600x600.jpg)

Miguel is a Principal Software Engineer for OpenShift Virtualization at Red Hat and maintainer for the CNCF incubating project, KubeVirt. His main interests are SDN / NFV, functional programming, containers, and virtualization. Miguel is a member of the Network Plumbing...

Read more from Miguel Duarte Barroso](https://thenewstack.io/author/miguel-duarte-barroso/)