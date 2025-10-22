Kubernetes has established itself as the backbone of modern containerized applications, yet a growing discussion in enterprise IT is whether it should also become the home for virtual machines (VMs). This is not simply about consolidating platforms. It speaks to broader questions of skills, expectations and migration that are now shaping strategic decisions in boardrooms and at industry conferences.

The ability to run VMs alongside containers under a single control plane has clear appeal. It promises operational consistency, potential cost savings and a simplified view of infrastructure for platform teams. However, this convergence is not without significant challenges. The shift demands new skills, it places new requirements on [Kubernetes](https://thenewstack.io/kubernetes/) itself, and it introduces a complex migration problem.

## The Skills Gap for VM Operators

Operators who have built their careers around [VMware](https://tanzu.vmware.com?utm_content=inline+mention), Hyper-V or [Nutanix](https://www.nutanix.com/solutions/cloud-native?utm_medium=redirect&utm_content=inline-mention) understand concepts like data stores, port groups and snapshots instinctively. These constructs map closely to physical servers and traditional IT practices. Kubernetes, by contrast, requires a new mindset.

Pods are ephemeral. Deployments and services define desired state. Networking is policy-driven and storage is abstracted. Management is often through YAML files and APIs rather than graphical consoles. As a former VMware administrator, I was used to dragging and dropping VMs around vCenter; this is not something a platform engineer would even consider doing with their pods. For teams used to steady state VMs, this can feel like a disorienting shift.

The open source [KubeVirt](https://thenewstack.io/open-source-kubevirt-vm-management-with-kubernetes-is-a-work-in-progress/) project is at the forefront of addressing this gap. It extends Kubernetes to manage VMs in much the same way as containers, exposing familiar constructs through the Kubernetes API. [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) has taken this further with a standalone license for [OpenShift Virtualization](https://thenewstack.io/virtualization-and-containers-better-together/), aimed at organizations that still want Kubernetes as their control plane but need to focus on hosting VMs.

Interest in this topic is evident. My own deep dive guide, “[KubeVirt for vSphere Admins](https://veducate.co.uk/kubevirt-for-vsphere-admins-deep-dive-guide/),” has become one of my most read posts, a sign that VM operators are actively looking for ways to bridge their skills into Kubernetes environments.

## Different Expectations for the Kubernetes Platform

Running VMs on Kubernetes also alters what enterprises expect from the platform itself. Containers are designed to be stateless and transient, while VMs are often stateful, long-lived and tied to persistent storage. Bridging these two models requires flexibility in scheduling, storage handling and life cycle management.

Networking illustrates the challenge most clearly. VM workloads frequently rely on static IPs, VLANs and firewall constructs. Kubernetes assumes a flat network with dynamic addressing and network policies. Reconciling these worlds is not trivial.

This is where projects such as [Cilium](https://thenewstack.io/breaking-the-chains-of-kube-proxy-with-cilium/) enter the conversation. Cilium brings an [eBPF](https://thenewstack.io/what-is-ebpf/)-powered networking model that feels familiar to VM operators who have worked with solutions like NSX. It provides microsegmentation, visibility and security controls that echo the features of traditional VM SDN platforms, but applied consistently to both VMs and containers. For enterprises exploring this convergence, it demonstrates how Kubernetes networking can evolve to meet VM-centric expectations without fragmenting operational models.

## The Migration Dilemma

Even if Kubernetes can meet the operational needs of VMs, the question of migration remains. Moving workloads into a Kubernetes-based platform involves far more than copying a disk file.

VMs are tied to hypervisor-specific settings. Their disks often reside on proprietary storage systems. Their networking relies on constructs that may not exist in the Kubernetes environment. Mapping all of these into a new set of abstractions is a considerable task.

It is also important to recognize that we are unlikely to see a wholesale migration of VMware estates. Most enterprises have only recently completed their virtualization programs. Moving every workload off to containers could take decades, just as mainframe and physical server workloads still run today. What is more realistic is a selective migration. Organizations may start with the easier workloads: CI and build systems, batch jobs, web frontends or certain databases where the migration effort is justified.

Vendors are beginning to innovate in this area. Red Hat’s Migration Toolkit for Virtualization (MTV) provides a framework for moving VMs into Kubernetes environments, handling many of the translation tasks that would otherwise be manual. Similarly, projects such as the Isovalent Network Bridge, introduced at Cisco Live 2025, focus on simplifying network transitions. It allows migrated VMs to maintain communication with existing data center environments, reducing the disruption caused by shifting platforms.

These innovations highlight the growing recognition that migration is not just a technical task, but a strategic barrier to adoption. Enterprises will not fully embrace Kubernetes as a home for VMs until the process of moving workloads becomes less risky and more predictable.

## What This Means for Enterprises

The convergence of VMs and containers on Kubernetes is not an abstract idea. It is a live conversation shaping strategies in enterprises today. Platform leaders are weighing the cost of maintaining separate infrastructures against the complexity of unifying them. CIOs are assessing whether Kubernetes can truly serve as the universal substrate for workloads, or whether it risks becoming burdened with too many responsibilities.

This topic is set to dominate discussions at conferences such as the upcoming KubeCon North America 2025. Expect to hear more about projects like KubeVirt, advances in Kubernetes networking and the evolving ecosystem of migration tools. Behind each of these technical debates is a deeper question: How do enterprises align their infrastructure choices with broader goals of digital transformation, efficiency and resilience?

For readers interested in following this topic further, the [KubeVirt community](https://kubevirt.io/community/) maintains an active Special Interest Group (SIG) and regular community calls. Red Hat publishes updates on OpenShift Virtualization and MTV, and the [Cilium community](https://cilium.io/get-involved/) regularly posts deep dives on networking advances. These are valuable places to watch for best practices and lessons learned.

## Conclusion

Kubernetes has already transformed the way organizations deliver software. Its next test may be whether it can also take on the role of managing VMs, uniting old and new workloads on a single platform. The challenges are clear: reskilling operators, adapting the platform to different workload expectations and navigating the migration of complex configurations, storage and networks.

These are not small obstacles, yet they are attracting growing attention from both open source communities and enterprise vendors. The outcome will determine whether Kubernetes remains a container platform or evolves into a universal foundation for enterprise computing.

*KubeCon + CloudNativeCon North America 2025 is taking place Nov. 10-13 in Atlanta, Georgia.* [*Register now*](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/bf4d71f1-cropped-935e44ff-dean-lewis-600x600.jpeg)

Dean Lewis is a senior technical leader at Isovalent, the company behind the open source cloud native solution Cilium. Dean has worked in various technology fields, from support to operations to architectural design and delivery at IT solutions providers based...

Read more from Dean Lewis](https://thenewstack.io/author/dean-lewis/)