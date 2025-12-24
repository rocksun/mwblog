*This is an excerpt from Chapter 3 of [“Running Virtual Machines on Kubernetes: A Practical Roadmap for Enterprise Migrations,”](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/) a new ebook by acclaimed research analyst and technology expert [Janakiram MSV](https://thenewstack.io/author/janakiram/) and sponsored by Spectro Cloud.*

*From exploring the architecture and life cycle of virtual machines (VMs) in a cloud native environment, to building cross-functional migration teams and selecting the right tools, this free book, [now available for download](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/), helps enterprise leaders navigate this once-in-a-generation shift with confidence.*

---

Building a production-ready KubeVirt platform requires careful planning around networking, storage and security. Each area builds upon Kubernetes foundations while adding VM-specific capabilities and requirements.

## Storage Architecture

KubeVirt leverages Kubernetes-native storage concepts for VM disk management. VMs use Persistent Volume Claims (PVCs) to request storage rather than using traditional data stores. The storage characteristics, such as performance profiles and access modes, are defined through StorageClass objects, which connect to underlying storage systems via Container Storage Interface (CSI) drivers.

Live migration requires storage that multiple nodes can access simultaneously. This typically involves using StorageClass objects that provide ReadWriteMany (RWX) volumes through technologies such as Network File System (NFS), CephFS or distributed storage systems. For high-performance workloads such as databases, PVCs can be configured with volumeMode set to Block, providing raw block devices directly to VMs for optimal input/output (I/O) performance.

KubeVirt also supports storage operations, such as cloning and snapshots, when the underlying CSI driver provides these capabilities. This enables workflows such as creating VM templates from existing disks or taking point-in-time backups of running systems.

## Network Configuration

VMs connect to the Kubernetes pod network by default using a masquerade binding, which provides Network Address Translation (NAT) access to the cluster network. This approach integrates VMs seamlessly with existing Kubernetes networking and service discovery mechanisms.

More complex networking scenarios require additional tools. Multus serves as a Container Network Interface (CNI) meta-plugin that enables pods and their contained VMs to attach to multiple networks simultaneously. This capability supports use cases like connecting VMs to specific virtual LANs (VLANs) through bridge networks or providing high-performance connectivity via Single Root I/O Virtualization (SR-IOV) pass-through devices.

The choice of CNI plugin has a significant impact on the available networking features. Different CNI implementations offer varying levels of functionality to meet advanced networking requirements, including network segmentation, traffic shaping and performance optimization.

## Security Framework

KubeVirt inherits Kubernetes security models while extending them for VM workloads. Namespaces provide the primary isolation boundary, grouping related VMs and containers while controlling their access to cluster resources. This approach creates logical separation, similar to organizing VMs into folders or resource pools.

Role-based access control (RBAC) defines granular permissions for VM management. RBAC policies specify which users or service accounts can create, delete, modify or access VMs within specific namespaces. This enables fine-grained delegation of administrative responsibilities across different teams or projects.

Network policies control traffic flow between VMs and other cluster workloads. These policies provide basic network segmentation capabilities, though their effectiveness depends entirely on the CNI plugin implementation. Some CNI solutions offer more advanced policy enforcement and monitoring capabilities than others.

Pod Security Standards and admission controllers can enforce security policies on VM workloads just like containerized applications. This includes restrictions on privileged operations, resource limits and security contexts that govern how VMs operate within the cluster.

## Integration Considerations

VM management through KubeVirt inherits many advantages from the Kubernetes platform. Resource management uses the same quota and limit systems as containers. Network policies function consistently across both VMs and pods. Storage management adheres to standard Kubernetes patterns, utilizing persistent volumes and storage classes.

The declarative model means VM configurations can be version-controlled, reviewed and deployed through standard DevOps practices. Teams can apply the same GitOps workflows used for containerized applications to their VM infrastructure, bringing consistency to operations across different workload types.

The convergence of VM and container workloads on a single platform creates opportunities for unified management approaches. Storage policies can apply consistently across both workload types. Network segmentation strategies can encompass VMs and pods within the same policy framework. Security controls benefit from centralized management and consistent enforcement mechanisms.

However, this integration also requires careful planning to ensure that VM-specific requirements, such as live migration, console access and compatibility with legacy applications, are adequately addressed within the broader Kubernetes operational model.

---

*To read more, download [“Running Virtual Machines on Kubernetes: A Practical Roadmap for Enterprise Migrations”](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/) today!*

[!["Running Virtual Machines on Kubernetes" cover image](https://cdn.thenewstack.io/media/2025/11/87847543-spectro-ebook-hero-image.png)](https://cdn.thenewstack.io/media/2025/11/87847543-spectro-ebook-hero-image.png)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)