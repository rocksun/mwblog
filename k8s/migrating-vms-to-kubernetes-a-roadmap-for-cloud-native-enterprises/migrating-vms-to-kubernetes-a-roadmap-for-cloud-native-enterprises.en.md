*This is an excerpt from the upcoming TNS eBook “[Running Virtual Machines on Kubernetes: A Practical Roadmap for Enterprise Migrations](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/)” by Janakirm MSV. Preregister now for early access to the book when it’s released later this month.*

The enterprise IT landscape has been undergoing a fundamental transformation for years. Organizations across industries are adopting cloud native technologies, embracing containers and modernizing their application delivery practices. This shift represents more than just technological change. It reflects a new approach to building and operating software that prioritizes agility, scalability and resilience.

Kubernetes has emerged as the foundation of this transformation. What began as [Google](https://cloud.google.com/?utm_content=inline+mention)‘s internal container orchestration system has become the universal control plane for modern applications. Organizations are standardizing on [Kubernetes](https://thenewstack.io/kubernetes/) — not just for new cloud native applications, but as their primary platform for all workloads, including legacy applications running in virtual machines (VMs).

Recent market events have accelerated this evolution. [Broadcom](https://www.vmware.com/?utm_content=inline+mention)‘s acquisition of [VMware](https://tanzu.vmware.com?utm_content=inline+mention) in 2023 created a pivotal moment, transforming a gradual modernization journey into an urgent business priority. The shift to [subscription licensing, product bundling and significant price increases](https://thenewstack.io/vmware-users-adjust-to-broadcom-subscription-licensing/) forced many organizations to accelerate their cloud native adoption timelines.

However, this urgency has also created an opportunity. Organizations already invested in Kubernetes now have compelling business justification to consolidate their infrastructure around a single, open platform.

## The Virtual Machine Challenge

Despite the momentum toward containerization, most enterprises still operate thousands of virtual machines. These workloads represent decades of application development and often include business-critical systems that cannot be easily rewritten or replaced. Legacy applications, commercial software with specific operating system (OS) requirements and complex monolithic systems all require VM-based deployment models.

This creates a fundamental challenge for Kubernetes adopters. How do you standardize on cloud native infrastructure while maintaining the virtual machines that your business depends on?

> How do you standardize on cloud native infrastructure while maintaining the virtual machines that your business depends on?

Traditional approaches force organizations to maintain separate infrastructure stacks: VM workloads run on hypervisor platforms while containerized applications run on Kubernetes clusters. This division creates operational complexity, duplicated tooling and inefficient resource utilization. Since each stack requires a unique skill set, different teams need to manage and operate the environments.

## The KubeVirt Solution

[KubeVirt](https://thenewstack.io/open-source-kubevirt-vm-management-with-kubernetes-is-a-work-in-progress/) addresses this challenge by extending Kubernetes to orchestrate virtual machines alongside containers. As a [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) project, KubeVirt provides a standardized way to run VMs using the same APIs, tools and operational practices used for containerized workloads.

This approach enables a true infrastructure consolidation. Teams can manage both VMs and containers through a single control plane, using consistent security policies, networking configurations and resource management practices. The result is simplified operations and more efficient resource utilization.

KubeVirt also provides a practical migration path. Organizations can move existing VMs onto their Kubernetes platform without requiring application changes. This “lift and shift” approach enables immediate infrastructure consolidation, allowing time to plan modernizing applications as separate initiatives.

[![Running Virtual Machines on Kubernetes: A Practical Roadmap for Enterprise Migrations](https://cdn.thenewstack.io/media/2025/10/8a2207e3-runningvirtualmachinesonkubernetesapracticalroadmapforenterprisemigrations.png)](https://cdn.thenewstack.io/media/2025/10/8a2207e3-runningvirtualmachinesonkubernetesapracticalroadmapforenterprisemigrations.png)

## What You’ll Learn

The upcoming eBook “**[Running Virtual Machines on Kubernetes: A Practical Roadmap for Enterprise Migrations](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/)“** will provide comprehensive guidance for implementing VM management on Kubernetes using KubeVirt. It covers the technology, processes and organizational considerations needed for successful adoption.

### Technical Foundation

The book explores KubeVirt’s architecture and core components, explaining how virtual machine concepts are translated into Kubernetes resources. You’ll learn about VM life-cycle management, networking, storage and security within the Kubernetes ecosystem.

### People and Process Transformation

Successful implementation requires more than technology deployment. The book addresses the cultural shift from traditional VM operations to cloud native practices. This includes evolving from graphical user interface (GUI)-based management to declarative, code-driven approaches using [Infrastructure as Code](https://thenewstack.io/introduction-to-infrastructure-as-code/) (IaC) and GitOps methodologies.

The transformation follows the [People, Process and Technology framework](https://web.archive.org/web/20151122232441/http://www.boozallen.com/media/file/People-Process-Technology-Enterprise2.pdf). It requires upskilling teams, establishing new operational practices and implementing the right technical solutions.

### Migration Strategies

The book covers practical migration approaches, from simple VM rehosting to more advanced replatforming strategies. It examines both native Kubernetes tools and specialized migration platforms that automate the process at scale.

### Operational Excellence

Beyond initial migration, the book explores ongoing operations in a unified environment. This includes monitoring, optimization, security and leveraging the broader Kubernetes ecosystem for advanced capabilities.

## A Path Forward

Organizations already committed to Kubernetes are well positioned to extend their platform to handle VM workloads. This approach builds on existing investments while simplifying infrastructure management.

The journey requires careful planning and execution, yielding substantial benefits. Unified infrastructure reduces operational complexity, improves resource efficiency and provides a foundation for continued modernization.

This book serves as your guide through the entire process, from initial planning through long-term operations. It provides the practical knowledge needed to successfully implement VM management on Kubernetes and realize the full benefits of infrastructure consolidation.

The cloud native future isn’t just about containers: It’s about creating a unified, efficient and agile platform that can handle all your workloads. KubeVirt makes that future possible today.

**Learn more about “[Running Virtual Machines on Kubernetes: A Practical Roadmap for Enterprise Migrations](https://thenewstack.io/ebooks/kubernetes/running-virtual-machines-on-kubernetes-a-practical-guide-for-enterprise-migrations/),” supported by Spectro Cloud, and register to be among the first to receive our newest eBook.**

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)