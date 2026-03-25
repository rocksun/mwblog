Broadcom VMware [announced](https://news.broadcom.com/news/2026-kubernetes-ecosystem) on Monday that it will donate Velero to the CNCF sandbox project, a move the company describes as a way to extend VMware vSphere Kubernetes Service to Kubernetes user organizations in both private and public clouds.

Taking a cue from user-organization feedback, Broadcom VMware’s expanding integration with open-source options gives users more freedom to mix and match Kubernetes infrastructure support. Broadcom is also expanding the VMware vSphere Kubernetes Service with API compatibility for more third-party open-source suppliers – in addition to its donation of Velero to the CNCF – including F5, Tigera Calico Enterprise, and Kong API Gateway.

During a briefing with the press before the announcement, Broadcom VMware representatives sought to reassure the community that it is ramping up open-source support and contributions — especially for Kubernetes, the largest CNCF project — using KubeCon + CloudNativeCon Europe as the venue to make these announcements.

With the VMware donation of Velero, more of the open-source community and user organizations can integrate their needs more easily by contributing to the project, with CNCF support as well. That aspect should help the project serve the larger community’s needs as its direct and governance control shifts away from Broadcom. At the same time, for Broadcom, this strengthens its position as a full-stack Kubernetes provider across cloud-native and private cloud spaces.

> “Backup and [disaster recovery] is a big pain point for many organizations as they are trying to bring together the new cloud native world with the traditional world of enterprise IT.”

## Backup gaps Kubernetes can’t fill

Donating Velero to CNCF is a great way for Broadcom to gain cloud-native “street cred,” [Torsten Volk](https://www.linkedin.com/in/torstenvolk), an analyst with Omdia, tells *The New Stack*. Adding enterprise backup and data migration to distributed applications is not simple, but it’s critical for success in any brownfield environment, he says.

“Backup and [disaster recovery] is a big pain point for many organizations as they are trying to bring together the new cloud native world with the traditional world of enterprise IT. And without backup and DR, you can’t do that,” Volk says. “If VMware can position Velero as the Backup, DR, and migration tool of choice for Kubernetes users, this would significantly boost the company’s cloud native story.”

## Velero finds a neutral home

Broadcom has submitted Velero to the CNCF sandbox to transition the project to neutral community governance. Velero is an open-source, Kubernetes-native tool for backing up, restoring, and migrating clusters and applications. It protects cluster-level resources and persistent data, enabling disaster recovery and workload portability. This is critical because Kubernetes does not provide built-in cluster-level backup by default.

Velero traces its origins to Heptio, which VMware acquired over five years ago. As an API-centric project, Helptio was founded by former Google and Kubernetes co-creators Joe Beda and Craig McLuckie. Broadcom has also remained a top contributor to Kubernetes, according to metrics from ESG and CNCF. Under CNCF’s tutelage, organizations will likely have greater confidence in relying on Velero for stateful application recovery and workload portability across different environments.

“Velero truly helps protect cluster-level resources and persistent data, thereby enabling our customers with disaster recovery and workload portability,” [Prashanth Shenoy](https://www.linkedin.com/in/prashanthshenoy/), vice president of product marketing, VCF division at Broadcom, said during a press and analyst briefing. “Velero is very critical for organizations, because Kubernetes, by default, doesn’t provide built-in cluster-level backup or recovery.”

Velero knows it is an open source Kubernetes native tool for backup, restore, and migration of Kubernetes clusters and applications.”

Following the retirement of the ingress-nginx project in March 2026, Broadcom is positioning its [Avi Load Balancer](https://www.vmware.com/products/cloud-infrastructure/advanced-services/avi-load-balancer) as a native replacement and architectural upgrade. The Avi Load Balancer is not a fork of NGINX. Avi is leveraging the NGINX HTTP protocol processing engine, which is an undifferentiated component. Avi’s software-defined architecture itself is purpose-built, as are many software modules that deliver capabilities (related to performance, scale, operational simplicity, high availability, elasticity, analytics, VCF integrations, etc.).

Additionally, new validations and partnerships have been announced with industry leaders, including F5 (for Big-IP Container Ingress Service), Kong (for API Gateway), and Tigera (for Calico Enterprise). “Broadcom has the AVI conversion tool or app that helps automate the migration from ingress nginx to Hubby, turning what could have been a very potentially disruptive change into a very smooth, automated transition for our customers,” Shenoy said.

As part of the VKS 3.6 release,  Shenoy said “foundational changes” to networking and performance management for VCF have been made. A major update is the “bring your own CNI” model, which allows customers to explicitly select interfaces such as Isovalent (Cilium) or Tigera (Calico Enterprise) at cluster creation, Shenoy said. Furthermore, to support AI workloads and databases, VKS now uses QD profiles to automate complex OS customizations that “were previously manual and prone to configuration drift,”  Shenoy said.

> “Think of the QD profiles as performance recipes, so you create a profile once that says, hey, here’s how these database servers should be configured…This applies automatically across all of the Kubernetes clusters.”

With VKS 3.6, Broadcom has also introduced QD profiles, designed to simplify the management of Stateful applications, such as databases, modern data engines, and AI workloads. “Think of the QD profiles as performance recipes, so you create a profile once that says, hey, here’s how these database servers should be configured,”  Shenoy said. “This applies automatically across all of the Kubernetes clusters. So there’s no need for any of this manual tweaking and no more configuration drifts.”

During the last quarter of 2025, Broadcom began to integrate Canonical Ubuntu directly into VMware Cloud Foundation (VCF). For those who want to continue relying on Photon OS (already available by default), Broadcom is expanding the options for platform engineers and developers with Ubuntu OS.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)