# Changed Block Tracking Is Here for Kubernetes Resilience
![Featued image for: Changed Block Tracking Is Here for Kubernetes Resilience](https://cdn.thenewstack.io/media/2025/03/38e60fab-changed-block-tracking-kubernetes-resilience-1024x576.jpg)
When IT, virtualization, backup, storage and operations teams explore [Kubernetes](https://thenewstack.io/kubernetes/), they compare its storage and data protection capabilities with traditional bare metal and virtual machine (VM) facilities. Because [cloud native architecture](https://thenewstack.io/cloud-native/) is inherently distributed, API-driven and loosely coupled, cloud native operations require new tooling and skills to achieve the same business outcomes as older technologies.

Business continuity covers backup, [disaster recovery (DR)](https://thenewstack.io/k8s-backup-and-disaster-recovery-is-more-important-than-ever/), cyber resilience against ransomware and audit compliance; it is often measured by two metrics: [recovery point objectives (RPOs) and recovery time objectives (RTOs)](https://thenewstack.io/defining-low-data-loss-downtime-tolerances-in-kubernetes/). When endeavoring to meet these metrics quickly, one critical area is often missing from cloud native data protection compared to traditional offerings: [changed block tracking (CBT)](https://thenewstack.io/kubernetes-advances-cloud-native-data-protection-share-feedback/).

## How the Kubernetes Community Built CSI-Aligned CBT
Since 2018, Kubernetes has deprecated “in tree” storage drivers in favor of the Container Storage Interface (CSI) specification for industrywide collaboration and standardization. CBT radically improves backup efficiency, so proprietary storage drivers with CBT have been required to meet business needs.

For over two years, the [Kubernetes Data Protection Working Group (DPWG)](https://github.com/kubernetes/community/blob/master/wg-data-protection/README.md) has worked to bring CBT to meet the CSI specification and Kubernetes API and to remove this barrier to Kubernetes adoption.

In May 2022, the DPWG began [Kubernetes Enhancement Proposal (KEP) #3314](https://github.com/kubernetes/enhancements/pull/4082) for CBT. With guidance and review from Kubernetes special interest group (SIG) leadership, peer SIGs, vendors and the Kubernetes community, the KEP went through three major redesigns. Each redesign progressed through conceptual and design phases, and each step improved its scope to address issues and gaps.

After reviews with the API and Security SIGs, the CBT design was incorporated into Kubernetes architecture and security best practices. Finally, in 2023, the third design was approved by the DPWG, a code prototype was completed, and a proposal was made to add CBT to the CSI specification.

The [CSI specification 1.11.0](https://github.com/container-storage-interface/spec/releases/tag/v1.10.0) augments VolumeSnapshot with CBT via the SnapshotMetadata service; it was published, and KEP-3314’s status was moved to “implementable” in June 2024. Since then, as Kubernetes and CSI maintainers, the DPWG has implemented alpha APIs with end-to-end testing pipelines.

## What Kubernetes CSI Changed Block Tracking Does
Now storage vendors and projects can adopt and deploy the SIG-Storage CSI CBT metadata service sidecar container and custom resources. Backup vendors and projects can adopt the new “v1alpha” Kubernetes APIs, which consume CBT via gRPC.

Enhancing the combination of cloud native storage and backup with Kubernetes CSI CBT means that Kubernetes data protection can compete with the traditional industry precedents for business continuity metrics.

The cloud native ecosystem and community is implementing Kubernetes CSI CBT and driving world-class cloud native data protection forward!

For more information, join us at [KubeCon + CloudNativeCon Europe 2025](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/), in London, for “Kubernetes Backup Legitimized: CSI Changed Block Tracking Has Arrived,” an advanced-level talk in the data processing and storage track, on Wednesday, April 2, from 17 – 17:30 BST at [Level 1 | Hall Entrance S10 | Room D](https://kccnceu2025.sched.com/venue/Level+1+%7C+Hall+Entrance+S10+%7C+Room+D). This talk will feature an overview of the architecture, security, testing and scalability of Kubernetes CSI CBT, including a demonstration, updates on vendor and project alpha feedback, and how you can collaborate.

*To learn more about Kubernetes and the cloud native ecosystem, join us at *[ KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/),
*in London, on April 1-4.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)