It’s not often a vendor makes a choice that delights both the developer and operations sides of the house. But [Broadcom’s](https://www.broadcom.com/) [decision](https://blogs.vmware.com/cloud-foundation/2025/08/26/broadcom-canonical-partnership/) to integrate [Canonical](https://canonical.com/) Ubuntu directly into [VMware Cloud Foundation (VCF)](https://www.vmware.com/products/cloud-infrastructure/vmware-cloud-foundation) will likely solve several pain points for both communities when it comes to cloud native.

For those who want to continue to rely on Photon OS (already available by default), Broadcom is expanding the choice for platform engineers and developers with Ubuntu OS.

Developers working with VCF should appreciate direct access to [a favorite Linux distribution](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) fully maintained by Canonical, and which Broadcom supports. Integrating Linux drivers, managing updates and other operations jobs are not what developers and admins want to spend time on. Indeed, developers [devote an estimated full workday per week to such operational tasks](https://thenewstack.io/why-do-developers-lose-1-day-a-week-to-inefficiencies/), according to a 2024 survey by Atlassian.

Operations teams, meanwhile, will appreciate VCF’s life cycle management capabilities when bringing workloads to production. Additionally, they will appreciate being able to rely on VCF’s and Ubuntu’s enterprise features for security hardening, managed updates and other operational support. Previously, many of these tasks had to be handled manually.

All of this is in addition to VCF’s integration with Argo CD, which adds a [GitOps](https://thenewstack.io/webinar/the-state-of-gitops-2025-key-findings-and-what-they-mean-to-you/) platform for direct-to-git [Kubernetes deployments](https://thenewstack.io/streamlining-kubernetes-implementation-with-gitops-best-practices/). (We will explore that aspect of [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) and the GitOps approach in another soon-to-be-published article.)

## Why Ubuntu Is a Favorite Linux Distribution

Ubuntu is a favorite leading Linux operating system (or distro) for several good reasons. It works well on both the desktop and server, and add-ons and updates are consistent. In particular, Ubuntu is well-suited for AI and well-designed to host AI applications running on GPUs.

Developers have long favored Ubuntu. Developers don’t want to spend a significant amount of time ensuring that applications in development meet compliance and security specifications or adhere to the demands of the product environment.

## How Ubuntu Integration Reduces Workloads and Complexity

Previously, when working in VCF, developers had to keep in mind that their applications would eventually need to run on Linux — typically a RHEL or SUSE Linux environment. Now, within VCF, developers can work directly with Ubuntu in context, streamlining the process.

Chiseled containers are also on offer, which are seeing [increased adoption.](https://canonical.com/blog/chiseled-ubuntu-containers-openjre) These containers are lighter images, with reduced attack surfaces and fewer security concerns. This translates into fewer common vulnerabilities and exposures (CVEs) and a faster, more efficient CI/CD pipeline.

## How Operations Teams Benefit From Ubuntu on VCF

For operations, what this obviously takes away is the complexity of managing multiple environments. Everything becomes unified in VCF as a single platform, with the use of a popular and reliable hypervisor and full private cloud stack. Ubuntu, combined with VCF — or Ubuntu developed by Canonical — streamlines operations management, as opposed to separately managing different systems. It also includes security updates.

Indeed, the removal of operating system complexity — especially kernel and user space differences — as a source of hard-to-detect issues is critical for the development life cycle, according to [Torsten Volk,](https://www.linkedin.com/in/torstenvolk) an analyst with TechTarget’s Enterprise Strategy Group. Linux distribution variations, he noted, are responsible for many problems developers face, especially with cloud native applications.

“A unified OS layer helps IT teams simplify their patch and compliance flows, which decreases management effort and operational risk,” Volk said.

## Enhanced Security With Chiseled Containers

Like their developer counterparts, operations also benefit from the reduced attack surface that chiseled containers offer. A chiseled container can be configured so that peripheral libraries unnecessary for running an individual container can be removed. Fewer CVEs mean reduced attack surfaces and fewer vulnerabilities attackers can exploit.

It was shown during the [VMware Explore 2025 annual users conference](https://www.vmware.com/explore/video-library/video/6377276035112) in August how a chiseled container can reduce vulnerabilities from 16 CVEs to one, with the remaining issue identified as a false positive. Efficiency gains were also demonstrated, with container size reduced from 200MB to 50MB. This reduction translates into faster development cycles, as fewer libraries require less testing and reduce dependency complexity.

## Streamlining AI Deployments in Air-Gapped Environments

The partnership also streamlines AI deployments in air-gapped environments by including precompiled virtualized GPU drivers, minimizing reliance on external repositories.

The ability to patch in air-gapped systems further strengthens security, ensuring these environments can remain enclosed. This is particularly valuable for industries with strict compliance requirements, such as defense, finance and healthcare, where security concerns are paramount. Instead of managing RHEL, SUSE, Ubuntu and container images separately, everything is consolidated into a single platform.

“While all major Linux distributions support air-gapped patching, standardizing on one operating system cuts down on managing mirrors and patch pipeline, which gives [site reliability engineers] one central set of playbooks and controls,” Volk said.

This is just one more way that Broadcom’s selection of Ubuntu as its distro of choice can potentially make life easier for both Devs and Ops (again, Photon OS remains available as well). While we have not yet tested VCF and Ubuntu in tandem, we can affirm that VCF has solidly built on its core features with Broadcom’s backing and remains a leading platform for cloud native computing.

We also rely heavily on Ubuntu as one of our favorite distros of choice. There is no reason that Broadcom will not pull this off, for the benefit of developers and operations.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)