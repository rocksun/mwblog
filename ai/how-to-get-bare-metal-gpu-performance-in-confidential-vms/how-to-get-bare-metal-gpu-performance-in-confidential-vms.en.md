PARIS — At [OpenInfra Summit Europe 2025](https://summit2025.openinfra.org/), [NVIDIA](https://www.nvidia.com/fr-fr/) wanted to make it very clear to AI developers, operators and users: If you want to run [sensitive AI workloads](https://thenewstack.io/is-ai-a-trillion-dollar-bubble-or-a-world-changing-juggernaut/) on GPUs anywhere — on premises, in public clouds or [at the edge](https://thenewstack.io/6-design-principles-for-edge-computing-systems/) — you need both virtual machine (VM)-level sandboxing and hardware-backed memory confidentiality. That means, said [Zvonko Kaiser](https://www.linkedin.com/in/zvonkok/), NVIDIA principal systems engineer, you should combine [Kata Containers](https://katacontainers.io/) (lightweight VMs for containers) with [Confidential Computing](https://thenewstack.io/confidential-computing-is-transforming-data-encryption-in-healthcare-finance/) to preserve bare-metal GPU performance while preventing the cloud operator from inspecting your model and data.

[Kata](https://thenewstack.io/container-security-and-the-importance-of-secure-runtimes/), for those of you who don’t know, is an open source project that combines lightweight VMs with container runtimes. It uses hardware virtualization technology to launch a separate VM for each container, providing strong isolation between containers. Each container, in turn, runs a minimal, stripped-down Linux kernel. Kata Containers aim to offer the performance benefits of containers along with the security and workload isolation of VMs.

## Understanding Kata Containers and Lightweight VMs

“Kata is the micro-VM … it just fits into the cloud native space,” Kaiser told the audience. He argued that Kata gives the isolation container runtimes lack while still integrating with Kubernetes workflows.

What Confidential Computing brings to the table is in-memory data and application encryption. We’ve long had security by encryption when data is at rest or in transit on the network. Now, we have it in memory as well.

The point of combining them, Kaiser explained, is a flip of the traditional threat model. Classic [Kata usage](https://thenewstack.io/kata-containers-secure-lightweight-virtual-machines-container-environments/) assumes the workload is untrusted, so it protects the host from the container. Confidential Computing, using CPU security features such as SEV/TDX, holds that: “We do not trust the infrastructure.” Thus, by encrypting the VM, even your cloud provider cannot snapshot or inspect guest memory.

## The Role of Confidential Computing and Attestation

To make sure this actually works, he emphasized the importance of attestation as the mechanism that glues the stack together. Only after a cryptographic proof that the VM and its boot/guest state match an expected configuration should secrets or keys be released to a workload. This enables a full-stack trust model across the control plane, worker nodes and pods. “The process of proving that your state … is really the state that you are measuring” is core to confidential deployments, said Kaiser.

Where AI and NVIDIA come together is by using these to enable you to use GPUs like bare metal inside confidential VMs. Kaiser explained how NVIDIA is working to make GPU workloads “lift-and-shift” into Kata/confidential VMs without losing performance or functionality.

## Achieving Bare-Metal GPU Performance for AI Workloads

To do this, NVIDIA leverages Kubernetes building blocks, the GPU Operator and Container Device Interface (CDI) — so that drivers, libraries and device mappings are presented to containers exactly as they would be on bare metal. “We just took this pattern that we have already on bare metal and just put it into the end so that the container that’s running in Kata will feel and behave the very same as running on bare metal.”

That effort includes support for PCIe pass-through, [Single Root IO Virtualization (SR-IOV)](https://learn.microsoft.com/en-us/windows-hardware/drivers/network/overview-of-single-root-i-o-virtualization--sr-iov-), [GPUDirect](https://developer.nvidia.com/gpudirect) [Remote Direct Memory Access (RDMA)](https://www.digitalocean.com/community/conceptual-articles/rdma-high-performance-networking) and per-pod runtime configurations so one pod can use PF pass-through while another uses SR-IOV. Crucially, Kata’s reliance on the guest kernel decouples user space from host kernel changes. This reduces the risk that a host update will break GPU drivers inside the workload VM.

## Solving PCIe Topology Challenges With NVIDIA’s VRA

That may sound complex, but, according to Kaiser, the real hard part is the topology. NVIDIA’s answer is its [Virtualization Reference Architecture (VRA)](https://docs.nvidia.com/ai-enterprise/planning-resource/reference-architecture-for-multi-tenant-clouds/latest/architecture-overview.html). NVIDIA will soon be publishing in more detail this approach of addressing the thorny problem of PCIe topology and peer-to-peer GPU communication inside VMs. It supports two approaches:

* **Flatten the hierarchy:** In this approach, you simplify topology to make provisioning easier. Cloud providers are already sometimes using this for confidential AI deployments, but it comes at the cost of hiding useful peer-to-peer links.
* **Host-topology replication:** Detect the host’s PCIe/input–output memory management unit (IOMMU) layout and mirror it inside the guest, preserving PCIe Address Translation Services (ATS) and PCIe Access Control Services (ACS) flags, which enables GPU peer-to-peer DMA and GPUDirect behavior.

Why two? So “You can either flatten the hierarchy because you say you don’t care about the hierarchy … or you can say ‘I want host replication because I’m doing P2P objects.’ So both modes are supported,” Kaiser explained.

NVIDIA also explained practical workarounds for [IOMMU](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/conceptual/iommu.html) grouping and PCIe slot limits. For example, you can selectively map only required GPU devices to guest root ports while leaving unrelated peripherals on bridge ports. This avoids unnecessary device pass-through and complexity.

Kaiser said NVIDIA is collaborating with [Red Hat](https://www.openshift.com/try?utm_content=inline+mention), [IBM](http://www.ibm.com/products/webmethods-hybrid-integration?utm_content=inline+mention) and the open source Kata community to upstream the VRA and tooling, including host-topology detection and performance guides. Other upcoming publications covered CPU pinning, ACS/ATS settings, and GPUDirect/RDMA tuning for confidential VMs, and emphasized avoiding nested virtualization so operators can run VM as a Service patterns at L1 with consistent attestation across layers. In short, “We want to upstream everything so that people can replicate it as a reference architecture,” said Kaiser.

## Open Source Collaboration and Upstreaming Efforts

All that sounds great, but Kaiser was careful to note trade-offs. Combining Kata with Confidential Computing is not a silver bullet. VM breakouts remain a theoretical risk; confidential VMs reduce a provider’s ability to inspect memory but do not eliminate all attack surfaces. Still, the combined approach substantially reduces the opportunity for cloud operators or co-tenants to access sensitive model artifacts or training data.

Still, once published and available, NVIDIA’s approach to running sensitive AI workloads at scale will almost certainly lead to a new AI stack that combines lightweight VM isolation ([Kata](https://thenewstack.io/kata-containers-demo-a-container-experience-with-vm-security/)), hardware memory encryption and attestation (Confidential Computing) and GPU device mapping abstractions (CDI + GPU Operator) with careful handling of PCIe topology and IOMMU constraints to preserve security and performance.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)