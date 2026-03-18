**KubeVirt** is an open-source project that brings virtual machines into the Kubernetes control plane, letting teams run VMs and containers side by side under the same orchestration, tooling, and lifecycle model. It packages VMs as Kubernetes objects so operators can manage both workload types with a single platform and the same CI/CD, observability, and policy tooling.

Adoption of KubeVirt has accelerated recently for pragmatic reasons. Organizations that historically relied on VMware are re-evaluating their virtualization stack, and many are looking to reduce vendor lock-in and consolidate infrastructure around Kubernetes. That shift is driving interest in container-native virtualization to modernize VM workloads without ripping and replacing them.

## What live migration means

**Live migration** is the ability to move a running VM from one host to another with minimal or no downtime. In traditional hypervisor environments (for example VMware vMotion), live migration preserves the guest memory, device state, and network connectivity so applications keep running while the VM moves. KubeVirt implements the same concept inside Kubernetes: it transfers memory and device state between nodes while the VM continues to run, enabling maintenance, load rebalancing, and non-disruptive failover.

> “Without shared storage, the target node cannot attach the VM disk while the source is still running, and live migration is not possible.”

A critical requirement for KubeVirt live migration is that the VM’s disk must be accessible from both source and target nodes simultaneously — in Kubernetes terms, the PersistentVolumeClaim backing the VM must support **ReadWriteMany (RWX)**. Without shared storage, the target node cannot attach the VM disk while the source is still running, and live migration is not possible.

## Why live migration matters

**Live migration** enables several operational capabilities that matter in production:

* **Zero or near-zero downtime maintenance:** Drain and upgrade nodes without stopping VMs.
* **Resource rebalancing:** Move heavy VMs to less loaded nodes to optimize utilization.
* **Planned failover and resilience:** Evacuate nodes before hardware failures or to react to degraded performance.

For cloud-native teams that want to treat VMs as first-class citizens in Kubernetes, live migration is a foundational capability.

## Mayastor and the RWX gap

**Mayastor** is a high-performance, container-native block storage engine in the OpenEBS family. It provides replicated block volumes and exposes them via [NVMe-over-Fabrics](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/) (NVMe-oF) targets for low-latency access. By design Mayastor focuses on **block** semantics and synchronous replication for durability and performance.

Out of the box, Mayastor does **not** present a native Kubernetes RWX block volume mode. The documented workaround is to [run an NFS server](https://thenewstack.io/linux-create-and-connect-to-an-nfs-share/) on top of a Mayastor volume and export that filesystem to provide shared ReadWriteMany access for VMs. OpenEBS documentation describes this pattern as a way to enable KubeVirt live migration with replicated Mayastor volumes by layering an NFS server pod and the NFS CSI driver.

**Is NFS on top of Mayastor a good idea?** It’s a pragmatic stopgap but not ideal for every workload. NFS introduces an extra software layer, changes performance characteristics (especially for I/O patterns that expect raw block semantics), and creates a single server process that must be highly available and correctly configured. For high-performance VM disks or workloads sensitive to latency and IO semantics, NFS can be a bottleneck and a source of complexity. A shared raw block device approach would be beneficial to reduce filesystem overhead by allowing kubevirt to directly access the underlying storage.

> “Is NFS on top of Mayastor a good idea? It’s a pragmatic stopgap but not ideal for every workload.”

Providing KubeVirt a raw block device also improves isolation compared with exposing a host‑mounted file, and taking the idea further by serving the VM via a direct virtio path (bypassing extra host filesystem/nvmf/block layers) can reduce attack surface and latency, but it also introduces engineering and operational tradeoffs that must be managed. For these reasons, NFS is useful as a compatibility shim but not a long-term substitute for a Kubernetes native multi-writer block solution.

## Exposing Mayastor block volumes as RWX for KubeVirt

Because KubeVirt’s virt-launcher handles VM I/O from both the source and target during migration, there is an opportunity to **safely** expose Mayastor block volumes as multi-node writable **specifically for KubeVirt**. Mayastor already exposes NVMe-oF targets and implements host access control for initiators; that means it can add additional initiator nodes to allow multiple hosts to attach the same namespace concurrently. In other words, the storage engine already has the plumbing to present block devices to multiple nodes.

The key enabler is a storage class and access mode policy that explicitly allows **multi-node writer** access but restricts it to KubeVirt use cases. Because KubeVirt coordinates the VM’s I/O during migration (ensuring only the virt-launcher processes are accessing the disk and that the VM’s device state is consistent), this controlled multi-writer mode can be safe — **but only** when the consumer is KubeVirt and follows the migration protocol.

## Safety, limits, and next steps

This approach must be guarded by policy and engineering controls:

* **Storage class scoping:** Create storage classes that advertise multi-node writer capability only for workloads labeled or annotated as KubeVirt VM disks.
* **Access control:** Use Mayastor’s NVMe-oF initiator allowlists and authentication to limit which nodes can attach a namespace concurrently.
* **Operational safeguards:** Ensure the migration protocol and virt-launcher semantics are respected so two independent writers never concurrently corrupt data.
* **Failure handling:** Design for partial failures during migration. If a migration is interrupted (network blip, node crash, or storage hiccup), the system must avoid deadlocks where both source and target think they own the disk. This is the next piece of the puzzle: robust coordination and recovery logic that can detect interrupted migrations and safely roll back or complete them without data loss.

## Conclusion

KubeVirt brings VMs into [Kubernetes to help teams modernize](https://thenewstack.io/kubernetes-helps-teams-modernize-faster-even-on-premises/) away from legacy hypervisors, and live migration is a must-have feature for production VM mobility. Mayastor’s architecture — replicated block storage plus NVMe-oF exposure — gives it a unique path to support KubeVirt live migration without the NFS shim, but doing so requires **careful, constrained** multi-writer semantics that are only safe when KubeVirt controls the I/O. The pragmatic route today is NFS on top of Mayastor for compatibility, but the cleaner, higher-performance future is a KubeVirt-only multi-node block mode with strong access controls and robust migration failure handling.

*This guest column is being published ahead of [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/), the Cloud Native Computing Foundation’s flagship conference, which will bring together adopters and technologists from leading open-source and cloud-native communities in Amsterdam, the Netherlands, from March 23-26, 2026.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/03/5e8321b8-tiagocastro.png)

OpenEBS maintainer and cloud-native storage engineer. He focuses on building resilient, high-performance container-native block storage for Kubernetes, contributing to core OpenEBS projects, and other Open-Source projects.

Read more from Tiago Castro](https://thenewstack.io/author/tiago-castro/)