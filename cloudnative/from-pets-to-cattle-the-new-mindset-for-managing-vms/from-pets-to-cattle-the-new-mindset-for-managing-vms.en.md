*This is an excerpt from Chapter 4 of [“Running Virtual Machines on Kubernetes: A Practical Roadmap for Enterprise Migrations,”](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/) a new ebook by acclaimed research analyst and technology expert* *[Janakiram MSV](https://thenewstack.io/author/janakiram/) and sponsored by Spectro Cloud.*

*The book delivers a practical roadmap for cloud native organizations that are exploring migrating virtual machines (VMs) to Kubernetes. While covering the range of options for migrating VMs to Kubernetes, it focuses on KubeVirt, a [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) project that “provides a standardized way to run VMs using the same APIs, tools and operational practices used for containerized workloads,” Janakiram explains in [the book’s introduction](https://thenewstack.io/migrating-vms-to-kubernetes-a-roadmap-for-cloud-native-enterprises).*

*From exploring the architecture and life cycle of VMs in a cloud native environment to building cross-functional migration teams and selecting the right tools, this free book, [now available for download](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/), helps enterprise leaders navigate this once-in-a-generation shift with confidence.*

---

Moving virtual machine (VM) workloads to [Kubernetes](https://thenewstack.io/kubernetes/) using KubeVirt involves changes in how teams deploy and manage applications. While the underlying infrastructure technology shifts, the more significant impact often lies in adapting operational practices and team workflows to work effectively with cloud native tooling.

This chapter explores the practical aspects of migration planning, including assessing organizational readiness, building the right team capabilities and managing the transition from VM-centric operations to Kubernetes-native approaches.

## Understanding the Operational Shift

Organizations already running Kubernetes for containerized applications have established cloud native practices. However, extending these practices to VM workloads often reveals gaps in how traditional and cloud native operations intersect.

According to Spectro Cloud’s “2024 State of Production Kubernetes” research, VM adoption has been a significant barrier limiting Kubernetes adoption. The study found that “continued use of VMs alongside containers” and “cultural resistance to change” remain key factors that influence how organizations approach platform adoption.

The operational differences between VM management and Kubernetes-native practices create specific challenges. Traditional VM operations typically involve GUI-based tools, ticket-driven provisioning and careful change management processes. Kubernetes operations emphasize declarative configuration, automated deployment and rapid iteration cycles.

Consider how resource requests differ between these approaches:

* In traditional VM environments, developers typically submit requests for new virtual machines through service desk systems. Infrastructure teams review specifications, provision VMs from standard templates and provide access after approval processes that may take days or weeks.
* In Kubernetes environments, developers modify resource specifications in YAML files, commit changes to version control and watch automated systems deploy new configurations within minutes. This shift represents more than improved speed: It changes who makes decisions, how resources are allocated and where operational expertise resides.

Teams accustomed to VM operations may find the Kubernetes approach initially unsettling. The increased autonomy of developers and reduced centralized control can feel like a loss of oversight. However, this transition often leads to improved agility and more efficient resource utilization once teams adapt their processes.

## Application Deployment Patterns

Moving VM workloads to Kubernetes also affects how applications are deployed and managed. Traditional VM deployments often treat virtual machines as long-lived infrastructure that hosts applications for months or years. Teams carefully configure operating systems, install dependencies and tune performance settings specific to each workload.

KubeVirt enables a different approach where VMs become more like containers in terms of life cycle management. While the applications inside VMs may remain unchanged, the VMs themselves can be treated as [cattle rather than pets](https://thenewstack.io/how-to-treat-your-kubernetes-clusters-like-cattle-not-pets). This enables practices such as automated replacement, rolling updates and dynamic scaling, which are common in containerized environments.

This shift requires teams to reconsider how they handle VM configuration, application deployment and operational maintenance. Infrastructure as Code (IaC) practices become more relevant as VM specifications are defined in version-controlled manifests rather than manual configuration processes.

The transition also affects how teams approach monitoring, logging and troubleshooting. Kubernetes-native tooling provides new capabilities for observability and automation, but teams need to learn how these tools apply to VM workloads running under KubeVirt.

---

To read more, download [“Running Virtual Machines on Kubernetes: A Practical Roadmap for Enterprise Migrations”](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/) today!

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