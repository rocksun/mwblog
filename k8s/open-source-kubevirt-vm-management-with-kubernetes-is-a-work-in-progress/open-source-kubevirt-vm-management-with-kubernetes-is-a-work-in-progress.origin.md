# Open Source KubeVirt: VM Management With Kubernetes Is a Work in Progress
![Featued image for: Open Source KubeVirt: VM Management With Kubernetes Is a Work in Progress](https://cdn.thenewstack.io/media/2025/05/83e0f057-ibrahim-yusuf-vwjtyrfe_rw-unsplash-1024x683.jpg)
[Ibrahim Yusuf](https://unsplash.com/@its_ibrahim?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-man-sitting-in-front-of-a-laptop-computer-vWJtYRfE_rw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
KubeVirt is a recent and dynamic open source project that enables virtual machines to run alongside containers by integrating a virtual machine management layer into Kubernetes. Designed for organizations that have virtual machine workloads and want to adopt a Kubernetes control plane, KubeVirt serves as a platform that allows for VMs and containers to run side by side.

Organizations that run workloads on [containers and Kubernetes may consider KubeVirt to integrate](https://thenewstack.io/the-impact-of-containerization-on-apm-strategies/) virtual machines with their Kubernetes and container infrastructure. Backed by Red Hat, NVIDIA and other tech companies, the CNCF project aligns with the growing recognition that containers are not going to replace VMs — as many organizations have learned the hard way. The idea is that containers and VMs can and should run side by side. But while the concept is solid, several caveats remain for organizations that need to support critical at-scale VM workloads.

With KubeVirt, VMs run inside Kubernetes clusters, and specifically within pods. This structure is workable for specific use cases, but its limitations so far make it less viable for production scaling of VMs onto Kubernetes. Adoption requires significant changes to existing IT infrastructure, including storage, compute and network. Even once KubeVirt is successfully implemented, its functionality is significantly limited compared to established VM-management offerings, especially those that can extend to Kubernetes so applications running on containers or VMs are managed on a single platform.

## Functionality Want
The KubeVirt Kubernetes Virtualization API and runtime are designed to define and manage virtual machines. However, additional functionality is required that another tool provides: Libvirt is used to integrate VMs with a KVM hypervisor so they can be launched and managed within Kubernetes pods. According to the project’s [documentation](https://github.com/kubevirt/kubevirt?tab=readme-ov-file), KubeVirt is largely limited to declarative usages, such as:

- Create a predefined VM.
- Schedule a VM on a Kubernetes cluster.
- Launch a VM.
- Stop a VM.
- Delete a VM.
KubeVirt provides very basic hypervisor admin features and is limited in use; for integrating a limited number of VMs, the relative lack of functionality and advanced operational capabilities — such as storage-management integration — doesn’t align with the advanced features expected in VM management. Since VM-based infrastructure has been in use for several decades, VMs benefit from extensive industry understanding and ongoing innovation of management in this space. Ideally, VMs’ advanced capabilities should be available with containers in a common infrastructure.

According to Gartner, KubeVirt’s use cases include:

- Infrastructure provisioning to create and destroy short-lived non-production virtual environments (including development and lab environments).
- In addition to this, KubeVirt can be used for the provisioning of VMs when used to host Kubernetes clusters.
According to [Michael Warrilow](https://www.gartner.com/en/experts/michael-warrilow), a vice president and Gartner analyst, “most enterprises are likely to find that re-virtualization of existing production virtual workloads will be the most technically challenging, risky and difficult to justify through at least 2028.”

Integration with storage systems is not a default implementation feature of KubeVirt. Without a standardized storage element that attaches to, or is standard for KubeVirt, different storage vendors may or may not easily work with or offer support for it.

KubeVirt was created for Kubernetes-executing VMs, which means organizations using KubeVirt remain reliant on storage vendors that support the Container Storage Interface (CSI). According to Gartner, as of January 2025, among the listed CSI drivers:

- 54% do not support snapshots.
- 49% do not support read/write to multiple pods.
- 57% do not support expansion.
This will disrupt many storage environments that use above common features like snapshot, expansion. This stands in stark contrast to traditional storage solutions for virtual environments, whether based on external or software-defined storage. Proven, de facto APIs have enabled storage vendors to consistently offload storage functions for virtual workloads. Examples include cloning, migration, provisioning, reclamation and access control.

While organizations can manage existing VMs, the management capabilities are minimal and limited to basic hypervisor administration. VMs continue to exist within the infrastructure, but KubeVirt lacks many of the advanced operational and life cycle management features that enterprise-grade virtualization platforms provide.

## Kubernetes-Centric
KubeVirt is purpose-built for Kubernetes environments, yet the requirements for enterprise adoption remain considerable. The platform operates on the assumption that all workloads will eventually be migrated to Kubernetes. However, such transitions are rarely immediate; even upgrades between Kubernetes versions can take several months — or, in some cases, years. As a result, KubeVirt is most appropriate for organizations that are committed to fully containerizing their workloads and adopting Kubernetes as the exclusive control plane. Once implemented, the lack of functionality will make VM management more like managing cattle than pets.

In comparison to traditional VM platforms, Kubernetes introduces significantly more operational complexity. This architectural shift imposes substantial friction, as it requires organizations to move away from established VM management practices and toward a Kubernetes-centric approach. While Kubernetes offers powerful orchestration capabilities, it also demands a completely new skill set. Virtual infrastructure administrators must be retrained, and organizations must reskill entire teams to manage existing VM workloads through a new control plane.

For environments with large-scale VM deployments — ranging from 1,000 to 100,000 virtual machines — this shift is far from trivial. Many of these environments rely heavily on custom scripting, advanced features and automation, making the migration both technically and operationally demanding.

This perspective is consistent with observations made by Gartner, which has noted that vendors such as Red Hat — with its OpenShift platform — have adopted KubeVirt as a strategic entry into the VM management market. Developing a mature, enterprise-grade VM management platform typically requires years, if not decades, of sustained engineering and operational refinement, regardless of whether the solution is open source or proprietary.

Organizations continue to rely on virtual machines because they offer operational simplicity, proven efficiency and a lower total cost of ownership (TCO). Furthermore, the existing talent pool is better aligned with VM management; hiring skilled professionals in traditional VM environments remains considerably easier than sourcing equivalent expertise in containerized or Kubernetes-native infrastructures.

Today’s VM operations are supported by mature orchestration tools, advanced features and hardened security and compliance frameworks. Introducing virtual machines into a Kubernetes-native environment would require organizations to overhaul their tooling and significantly reskill technical teams — an effort that carries considerable cost and operational risk. As such, the rationale for running VMs inside Kubernetes clusters remains limited to highly specific use cases, and is not recommended for general enterprise adoption.

“This is an evident gap in skills that will need to be overcome to successfully adopt KubeVirt whether for production or not. Many existing I&O personnel will lack proficiency and experience in modern, cloud-native tools and methodologies,” Warrilow writes. “Implementing DevOps requires significant investment in both technology and training, which has proven to be a barrier to widespread adoption … KubeVirt will force this change.”

## Adolescent Promise
KubeVirt remains in the incubation stage after entering the CNCF as a sandbox project in 2019 and advancing to the incubation maturity level in 2022. While this represents meaningful progress, it also indicates that the project has not yet reached the level of maturity required for CNCF graduation. According to the CNCF, achieving graduation status will require significant additional development, stability, adoption and governance maturity. For CNCF’s largest projects, Kubernetes and OpenTelemetry, these are steps that have taken over a decade to achieve.

For organizations in regulated or mission-critical sectors — such as banking, federal, state and local governments, utilities or retail — the risks associated with adopting such a nascent technology are considerable. Unlike technology leaders such as NVIDIA, Google, or Meta, which have internal engineering capabilities to customize and support open source tools, most enterprises are not equipped to manage this level of technical complexity independently.

## Conclusion
We recommend that organizations with existing VM infrastructure adopt a platform with a proven track record for VM management capabilities. Many organizations already have well-established security and compliance frameworks in place for these mature platforms. Introducing VMs into a Kubernetes-native environment would require significant changes to tooling and extensive reskilling of operational teams — efforts that may not be justified given the maturity and efficiency of a VM platform versus the relatively limited scale of functionality for VMs that KubeVirt currently offers.

While very few organizations with significant resources can afford to rely on such a young project (Version 1.0 of KubeVirt was released in July 2023) to integrate VMs with Kubernetes and container infrastructure, it is recommended that for the foreseeable future its use remains limited to the management of small numbers of VMs — think a hundred VMs for a sandbox project and not a hundred thousand VMs that support critical operations.

Gartner estimates that through 2028, technical and operational limitations will restrict adoption of KubeVirt to less than 10% of on-premises production virtual workloads in enterprise environments.

“Adopting KubeVirt for the wrong reasons will incur significant, avoidable technical risk,” Gartner analyst Michael Warrilow writes in “KubeVirt Will Require Radical Changes to Traditional I&O.” “But using it purely as a means of revirtualizing production workloads is unlikely to generate sufficient ROI or improve availability, reliability or security.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)