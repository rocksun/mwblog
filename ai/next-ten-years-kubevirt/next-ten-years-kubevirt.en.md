**KubeVirt was founded** by Red Hat in 2016 around the idea that Kubernetes could run [virtual machines alongside containers](https://thenewstack.io/kubevirts-architecture-crds-controllers-and-daemons/). We wanted to allow users to run legacy workloads on the same platform as their modernized applications. That is still the job, but since v1.0 other projects have demonstrated that they can build on it and integrate KubeVirt in a broader ecosystem. Let’s discuss some of what the next 10 years of KubeVirt will bring.

Other projects such as Open Sovereign AI Cloud (OSAC) use it for VM, cluster, and bare-metal services. Cluster API Provider KubeVirt (CAPK) uses KubeVirt VMs as Kubernetes nodes. Flight Control runs a virt-launcher on the edge without the full KubeVirt control plane.

Today KubeVirt is a CNCF incubating project, with contributors from Nvidia, Microsoft, AMD, Intel, SUSE, and others. The community is working toward KubeVirt’s graduation as a CNCF project. The enhancement trackers for v1.8, v1.9, and v1.10 show what “next” means in practice. From v1.6 to v1.10 the queue went from a small set of items to more than a hundred. v1.9 included dozens of new proposals. The KubeVirt Enhancement Proposal (VEP) process is how we keep the core stable while that queue grows: designs before code, one tracker, and ownership by special interest groups (SIGs).

In this article, I will share some of the work that will shape the next releases: devices and new hardware, extending KubeVirt without growing core, confidential VMs, the VM as a sandbox, and pluggable virtualization stacks. My fellow KubeVirt contributors, Fan Zhang and Harshit Gupta, help explain the features they are working on.

## Devices, DRA, and new hardware

GPUs on VMs can already be claimed through Kubernetes [Dynamic Resource Allocation](https://thenewstack.io/kubernetes-dra-gpu-scheduling/) instead of using device-plugins. This functionality is beta in v1.9. The same claim model is being extended to generic host devices, network devices such as SR-IOV, and to CPUs. In the near future, a VM will be able to ask for a GPU, NIC, and CPUs and have Kubernetes allocate them as a coordinated set. There is also work to allow KubeVirt to build those claims from the VM spec and an input from vendor policy, instead of asking every user to write ResourceClaim objects by hand.

> “That follows the design principle that has guided the project from the beginning: to prefer Kubernetes native solutions and mechanisms rather than building isolated virtualization workarounds.”

That follows the design principle that has guided the project from the beginning: to prefer Kubernetes native solutions and mechanisms rather than building isolated virtualization workarounds. DRA allows us to improve the granularity of the devices and CPU allocations. But there were many other examples, such as Swap in Kubernetes, ImageVolumes, volume populators, and more, that allowed us to delete a KubeVirt-only path and use what the cluster already has.

KubeVirt contributors, including Nvidia engineers, have been working to enable KubeVirt to run on newer Nvidia hardware, such as the Grace Hopper, Grace Blackwell, and Vera Rubin systems. This functionality was developed first in the Accelerated Infrastructure Enablement working group and is moving upstream.

## Confidential VMs and trusted execution

Users increasingly want to run sensitive applications and AI workloads on shared infrastructure while [protecting their data](https://thenewstack.io/confidential-ai-sensitive-enterprise-data/) and models during execution. Confidential computing uses hardware-backed trusted execution environments to provide isolation, including protection against privileged host software within the platform’s threat model. Remote attestation lets workload owners evaluate evidence about that environment before entrusting it with secrets. KubeVirt is expanding support for confidential VMs and exploring integration with attestation and secret-release services, including Trustee from the Confidential Containers project.

**“**For AI, the trust boundary should extend across the full execution path—CPUs, accelerators, and the interconnects between them,” explained Fan Zhang, co-lead of Kubevirt’s AIE and Confidential Compute working groups. “Workload owners need to verify that environment through attestation before releasing sensitive data or model keys. KubeVirt offers an opportunity to bring confidential VMs, protected accelerators, and attestation together through familiar Kubernetes workflows. Collaboration with projects such as Confidential Containers and Trustee can make these protections more accessible while helping workload owners control access to their data and models.”

This work spans Intel Trust Domain Extensions (TDX), AMD Secure Encrypted Virtualization—including SEV-SNP—IBM Secure Execution, and emerging Arm Confidential Compute Architecture (CCA) support. In KubeVirt v1.9, the feature gate covering AMD SEV and SEV-SNP graduated to beta, Intel TDX support remained alpha, and IBM Secure Execution support reached general availability (GA). Arm CCA enablement remains under development.

> “Capability discovery helps determine where a VM can run; attestation helps workload owners decide whether to trust the environment in which it runs.”

Looking ahead, contributors are exploring more consistent discovery of TEE capabilities across cluster nodes, helping Kubernetes place confidential VMs on suitable infrastructure. Other proposals address attestation initialization data, evidence handling, and integration with external verification and secret-release services such as Trustee. Capability discovery helps determine where a VM can run; attestation helps workload owners decide whether to trust the environment in which it runs.

For accelerated workloads, the ambition extends to confidential device assignment and protected communication between CPUs and accelerators. These capabilities require coordinated support across hardware, firmware, the virtualization stack, guest software, and attestation services.

These efforts are at different stages of discussion and implementation. Their inclusion in future releases will depend on community review, integration, and testing.

## Extending KubeVirt without growing core

KubeVirt is a mature project. The core is protected on purpose. A feature does not land in kubevirt/kubevirt until we are willing to support it for everyone, for a long time, without breaking the clusters that already run. That takes time. Sometimes the community is not convinced that feature A belongs in the core at all. That should not stop someone from building it.

> “A feature does not land in kubevirt/kubevirt until we are willing to support it for everyone, for a long time, without breaking the clusters that already run.”

We are following the Kubernetes idea of extensibility. Users should be able to write a complete feature outside of core and still get the KubeVirt API guarantees.

Structured plugins are that path. A plugin is a cluster-scoped object: domain hooks, node hooks, admission. Domain changes can be a CEL expression, or a sidecar when the hook needs external state. An admin can see it and control it. This is alpha in v1.9.

## Pluggable virtualization stacks

The other half is the virtualization stack itself. libvirt, QEMU, and KVM are central in KubeVirt. That is still the default, and it was the right default. In v1.8 we added an in-tree Hypervisor Abstraction Layer and Microsoft’s MSHV backend as Alpha. However, the goal is to make the virtualization stack pluggable so users will be able to extend KubeVirt, letting Cloud Hypervisor, OpenVMM, or Firecracker live out-of-tree without forking KubeVirt. That work is still ongoing.

“KubeVirt enables customers to modernize VM workflows by bringing Kubernetes orchestration, storage, and networking to virtual machines,” said Harshit Gupta, senior software engineer, Microsoft. “Extending these benefits to virtualization solutions built on alternative stacks adds user flexibility. Our proposal builds on work to support alternate hypervisors and aims to fully decouple KubeVirt from its underlying virtualization stack through a pluggable virtualization framework. It follows KubeVirt’s move toward greater customization and flexibility. I’m excited to be working on this because it has the potential to broaden KubeVirt’s adoption across organizations.”

Pluggability will require re-architecting KubeVirt to use a plugin framework for choosing a specific virtual machine monitor and hypervisor, and initial work has begun to implement this. [KubeVirt Enhancement Proposal #82](https://github.com/kubevirt/enhancements/pull/311) outlines the main pluggability work. Beyond enabling other virtualization platforms, maintaining backends as plugins could support better testing and easier maintenance.

## The next 10 years

The project began a decade ago with a simple focus: assisting organizations as they shifted legacy VM workloads onto Kubernetes. Today, the mission has evolved toward empowering teams to deploy modern, next-generation platforms. From AI inference and edge deployments to hardened multi-tenant environments and emerging architectures, the community remains committed to advancing what virtual machines can do natively on the platform.

What started as an ambitious experiment to orchestrate VMs through Kubernetes has expanded into an entire ecosystem. The next decade will depend on how contributors turn these proposals into stable capabilities.

**KubeCon + CloudNativeCon is taking place in Salt Lake City from November 9 to 12.** [**Register Now**](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)**!**

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/10/af24c7a0-vladik-romanovsky-natalie-pazmino-sincavage.jpg)

Vladik Romanovsky is a Senior Principal Software Engineer at Red Hat and a maintainer of the KubeVirt project. He works on virtualization and Kubernetes integration and has been involved in the project’s development and community since its first year.

Read more from Vladik Romanovsky](https://thenewstack.io/author/vladik-romanovsky/)