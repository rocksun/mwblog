*This is an excerpt from Chapter 3 of [“Running Virtual Machines on Kubernetes: A Practical Roadmap for Enterprise Migrations](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/),” a new eBook by acclaimed research analyst and technology expert Janakiram MSV and sponsored by Spectro Cloud.* *From exploring the architecture and life cycle of virtual machines (VMs) in a cloud native environment, to building cross-functional migration teams and selecting the right tools, this free book, [now available for download](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/), helps enterprise leaders* navigate this once-in-a-generation shift with confidence.

---

## KubeVirt Fundamentals: Bridging VMs and Containers

As organizations chart their course away from traditional virtualization, [KubeVirt](https://thenewstack.io/open-source-kubevirt-vm-management-with-kubernetes-is-a-work-in-progress/) emerges not just as a tool but as a foundational technology that makes a phased, pragmatic migration to Kubernetes possible. It acts as a bridge, enabling the coexistence of legacy virtual machines and modern containers on a single, unified platform: [Kubernetes](https://thenewstack.io/kubernetes/).

Understanding KubeVirt’s architecture and capabilities is the first step in leveraging it to derisk the migration process, consolidate infrastructure and accelerate the journey to a cloud native operating model.

This chapter explores the technical foundations, practical limitations and real-world implementation patterns that are essential for infrastructure evaluation.

## Architecture Overview: How KubeVirt Extends Kubernetes

KubeVirt’s design philosophy is straightforward and builds firmly on aspects where Kubernetes already excels. Instead of creating a new, parallel orchestration system for virtual machines, KubeVirt extends the reputable Kubernetes API and control plane, enabling it to manage VMs as native resources. It efficiently delegates core functions like scheduling, networking and storage directly to Kubernetes, while layering on the specific logic required for virtualization.

[![KubeVirt Architecture Stack](https://cdn.thenewstack.io/media/2025/12/96b4a2db-kubevirt-architecture-stack.png)](https://cdn.thenewstack.io/media/2025/12/96b4a2db-kubevirt-architecture-stack.png)

KubeVirt adds virtualization capabilities to Kubernetes.

At its heart, a KubeVirt VM is simply a process running inside a standard Kubernetes pod. This approach allows VMs and containers to run side by side on the same worker nodes, communicate over the same network and use the same storage resources, all managed through a single pane of glass.

To achieve this, KubeVirt introduces three main types of components into the cluster:

1. **Custom Resource Definitions (CRDs):** These are extensions to the Kubernetes API that define new object types. KubeVirt adds several CRDs, most notably VirtualMachine and VirtualMachineInstance (VMI). This allows administrators to define a VirtualMachine using a declarative YAML manifest, just as they would for any other Kubernetes object, such as a pod.
2. **Controllers:** These are cluster-wide components that contain the business logic for managing the new CRDs. They run as pods and watch the Kubernetes API for changes.
3. **Daemons:** These are node-specific agents, deployed as a DaemonSet, that are responsible for managing the VM life cycle on each worker node in the cluster.

## Key Components and Their Roles

The interplay between KubeVirt’s components creates a seamless virtualization layer within Kubernetes. While an operator can install all necessary components, understanding the individual roles of these components is key to troubleshooting and effective management.

* **VirtualMachine and VMI:** These are the two primary CRDs that users interact with. The VirtualMachine object represents the persistent, desired state of a virtual machine. It can be started and stopped while retaining its configuration and data. The VirtualMachineInstance represents the actual running instance of that VirtualMachine. A VMI is more ephemeral, existing only while the VirtualMachine object is in a running state, and is tightly coupled to the pod that hosts it.

* **virt-api server:** This serves as the HTTP API entry point for all virtualization flows, acting as an interface for the operations of VMI CRDs. It validates, processes and persists VMI and VirtualMachine resource definitions into Kubernetes, allowing the rest of the KubeVirt control plane to react.

* **virt-controller:** This is the central, clusterwide controller. Its primary job is to watch for the creation of new VMI objects. When a VMI is defined, virt-controller creates a corresponding pod that will ultimately host the VirtualMachine process. It handles high-level operations and orchestrates complex actions, such as live migrations.

* **virt-handler:** This is a DaemonSet, meaning an instance that runs on every worker node. It acts as the node-specific agent. When a VM’s pod is scheduled onto its node, virt-handler takes over. It communicates with the virt-launcher inside the pod to perform all the necessary operations to start, stop and manage the VM process on that specific host.

* **virt-launcher:** For every running VM, there is a dedicated pod, and the primary container within that pod runs the virt-launcher component. This component is the final link in the chain. It receives instructions from virt-handler and uses a local libvirtd instance to start and manage the actual [QEMU](https://github.com/qemu/qemu)/Kernel-based Virtual Machine ([KVM](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine)) process that constitutes the virtual machine. It also ensures a graceful shutdown by trapping signals from Kubernetes and passing them to the VM process.

* **libvirtd:** This is a hypervisor management daemon running inside the virt-launcher container. It exposes a control interface to QEMU/KVM, handling VM life-cycle commands such as start, stop, pause, resume and migrate. It abstracts away the complexities of interacting directly with QEMU by offering a stable API.

* **QEMU:** This is a user-space emulator and virtualizer invoked by libvirtd inside the virt-launcher container. QEMU emulates the VM’s hardware environment and executes the guest operating system with hardware acceleration through KVM when available. It handles device emulation, I/O operations and CPU virtualization.

[![Kubevirt Services Architecture](https://cdn.thenewstack.io/media/2025/12/9a01675d-kubevirt-services-architecture.png)](https://cdn.thenewstack.io/media/2025/12/9a01675d-kubevirt-services-architecture.png)

Communication and storage of additional controllers and daemons.

---

***To read more, download [“Running Virtual Machines on Kubernetes: A Practical Roadmap for Enterprise Migrations](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/)” today!***

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