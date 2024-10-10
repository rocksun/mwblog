# Kubernetes Advances Cloud Native Data Protection: Share Feedback
![Featued image for: Kubernetes Advances Cloud Native Data Protection: Share Feedback](https://cdn.thenewstack.io/media/2024/10/a0d41f8b-kubernetes-cloud-native-data-protection-1024x576.jpg)
When IT, virtualization, backup, storage and operations teams explore [Kubernetes](https://thenewstack.io/kubernetes/), they compare storage and data protection capabilities with traditional bare metal and virtual machine (VM) facilities. Because cloud native architecture is inherently distributed, API-driven and loosely coupled, cloud native operations require new tooling and skills to achieve the same [disaster recovery](https://thenewstack.io/k8s-backup-and-disaster-recovery-is-more-important-than-ever/) (DR) business outcomes. While many cloud native storage benefits are impressive, one critical area is still missing: changed block tracking (CBT).

In the simplest case, CBT improves backup efficiency with [incremental backup](https://en.wikipedia.org/wiki/Incremental_backup) — finding and transmitting only the difference between what currently lives in storage and the most recent backup image. CBT can find that there has been little to no change since the last backup and make a nearly instantaneous new backup with minimal consumption of time, CPU, memory or storage. Making backup windows short and lightweight also helps organizations perform backups at an increased frequency, which reduces the recovery point objectives (RPOs) or the amount of data loss incurred.

CBT is a feature of storage systems. Most of these systems offer the ability to snapshot volumes, which creates a read-only view of your volume at the time the snapshot is taken. With CBT enabled, the storage system will track every block written and can provide a list of blocks that have changed between the two snapshots. If a block is written multiple times between snapshots, it only needs to be copied once since the state at the time of the snapshot backup is the only one that needs to be kept. This makes volume backup very efficient, particularly since blocks that have never been written don’t need to be backed up.

Because nearly every storage provider offers CBT, it is surprising that cloud native storage with Kubernetes lacks this capability. Why? A longer answer follows, but the short answer is that after two years of work, Kubernetes CBT is almost here! Storage and backup vendors and projects can prototype, give feedback and improve CBT into an industry-wide solution as it enters the Kubernetes alpha phase.

## Stateful Kubernetes Workloads and Storage
[Ten years](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/) after Kubernetes debuted, stateful workloads are commonplace. But when Kubernetes released [StatefulSets](https://www.veeam.com/blog/stateful-vs-stateless-kubernetes.html) in 2018, it took time for cloud native storage to accelerate.
The Container Storage Interface (CSI) version 1.0 was also adopted in 2018 with [Kubernetes 1.13](https://kubernetes.io/blog/2018/12/03/kubernetes-1-13-release-announcement/). CSI provides a uniform API for different storage providers and is an independent consortium that publishes industry-wide specifications. It has been adopted by leading platforms, such as [Cloud Foundry](https://www.cloudfoundry.org/?utm_content=inline+mention), [Apache Mesos](https://mesos.apache.org/) and [HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) Nomad.

Storage vendors create CSI drivers, which are installed onto [Kubernetes](https://roadmap.sh/kubernetes) clusters. All the proprietary “in-tree” storage drivers in the Kubernetes codebase have been (or are in process of being) removed in favor of CSI.

The [Kubernetes Data Protection Working Group](https://github.com/kubernetes/community/blob/master/wg-data-protection/README.md) (DPWG) was formed in 2020 by the [Kubernetes Storage Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-storage) (SIG-Storage). Also in 2020, the CSI specification published `VolumeSnapShot`
, which was released in Kubernetes 1.20. Previously, Kubernetes backup and recovery could only deal with file systems via CSI or resort to proprietary storage drivers. CSI block storage backup quickly became possible and more robust than filesystem backup.

## A Community-Driven Effort
Here’s a quick rundown of how CBT was added to CSI and Kubernetes.

In May 2022, DPWG began [Kubernetes Enhancement Proposal (KEP) #3314: Changed Block Tracking](https://github.com/kubernetes/enhancements/pull/4082). With guidance and review from SIG leadership, peer SIGs, vendors (including [Veeam](https://www.veeam.com/)) and the Kubernetes community, KEP 3314 went through three major redesigns. Each progressed through repeated conceptual phases to design review and defense, with each step improving the scope to address issues and gaps. This CBT design improved after the API and Security Special Interest Groups (SIG API and [SIG Security](https://thenewstack.io/cncfs-special-interest-group-for-security/)) helped incorporate Kubernetes architecture and security best practices. Finally, in 2023, the third design was approved by the DPWG, a code prototype was completed, and a proposal was made to add CBT to the CSI specification.

The [CSI specification 1.11.0](https://github.com/container-storage-interface/spec/releases/tag/v1.10.0) with CBT via the `SnapshotMetadata`
service was published and updated KEP-3314’s status to “implementable” in June 2024. The first target was Kubernetes 1.31 as alpha APIs with the prototype code, but gearing up pipelines to test, add documentation and learn other Kubernetes and CSI maintainer tasks has caused it to slip to Kubernetes 1.32.

## Cloud Native CBT Design
The intended audience for CSI CBT implementation is Kubernetes cloud native backup and storage vendors. The CBT design process includes two new areas:

- Storage vendors and projects should adopt and deploy the SIG-Storage CSI CBT metadata service sidecar container and custom resource(s). Then, the CSI driver should implement:
- Add new
`SnapshotMetadata`
service to allow the container orchestrator to obtain allocated or changed block metadata for snapshots. See: - Backup vendors and projects should adopt new Kubernetes APIs, which consume CBT via gRPC
- The KEP is currently a
[“v1alpha” implementation](https://github.com/kubernetes/enhancements/pull/4082)of the CSI specification
- The KEP is currently a
- Add new
The following security diagram shows how backup software and cluster storage can orchestrate and provide CBT access to a `VolumeSnapShot`
:

More technical resources:

[KEP 3314 Design Slides and Diagrams](https://docs.google.com/presentation/d/11nCmMkOEm5sY7zGQeXmsAV2wR7mb8HUYPKWyXhyD86o/edit#slide=id.p)- Cloud Native Rejekts 2023 talk: “Revolutionizing Data Backup in Kubernetes: Unlocking the Power of Change Block Tracking With CSI”
[abstract](https://cfp.cloud-native.rejekts.io/cloud-native-rejekts-na-chicago-2023/talk/HGPYB3/)and[video](https://www.youtube.com/watch?v=sV1skj7OW7Y&list=PLnfCaIV4aZe-4zfJeSl1bN9xKBhlIEGSt&index=29)(30 minutes) [DPWG: Data Protection Workflows](https://github.com/kubernetes/community/blob/master/wg-data-protection/data-protection-workflows-white-paper.md)white paper
## Please Share Your Feedback
The journey to cloud native CSI CBT has just begun its implementation phase. The Kubernetes DPWG and CSI Consortium want your feedback on CSI CBT.

As CSI CBT enters its alpha phase, you can help with adoption and improvements. Please spread the word and provide feedback that can be incorporated into the beta phase.

**For storage vendors and projects:**Is adopting CSI CBT as simple as exposing existing functionalities via the new CSI CBT sidecar container API? That depends on the current architecture of the CSI driver and your underlying storage CBT functionality. Please let us know if this example is helpful.**For backup vendors and projects:**Shouldn’t CSI CBT adoption be as easy as consuming the new Kubernetes APIs with a supporting CSI CBT storage vendor? Where are the mock providers and tests, and do they meet your needs?**For the Kubernetes community:**Reach out to your backup and storage vendors and projects and ask them to adopt CSI CBT to improve your data protection.
Help CSI CBT be a success. Join the [DPWG bi-weekly meeting or reach out on the Slack channel and mailing list](https://github.com/kubernetes/community/blob/master/wg-data-protection/README.md#meetings); we are available to answer questions. Plus, register to attend the [Kubernetes Data Protection Working Group Deep Dive](https://kccncna2024.sched.com/event/1hovn/kubernetes-data-protection-wg-deep-dive-dave-smith-uchida-veeam?iframe=no&w=100%25&sidebar=yes&bg=no) talk on Wednesday, Nov. 13 at KubeCon + CloudNativeCon North America.

Every day, more people ask, “Is now the time to migrate to Kubernetes?” Bringing CSI CBT to cloud native storage removes longer RPOs, a critical disadvantage when compared to traditional infrastructure. We are eager to collaborate with the cloud native ecosystem and community to implement CSI CBT and drive world-class cloud native data protection forward.

*To learn more about Kubernetes and the cloud native ecosystem, join us at **KubeCon + CloudNativeCon North America**, in Salt Lake City, Utah, Nov. 12–15, 2024.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)