# Has VMware Finally Caught Up With Kubernetes?
![Featued image for: Has VMware Finally Caught Up With Kubernetes?](https://cdn.thenewstack.io/media/2025/04/9df4f152-vmware-caught-kubernetes-1024x576.jpg)
Ever since containers became “a thing,” VMware has been one of the leading Kubernetes management and infrastructure services providers and one of the top three contributors to the [Kubernetes](https://thenewstack.io/kubernetes/) projects in the last decade. But that hasn’t been enough.

Prior to its acquisition by Broadcom in 2023, much of VMware’s Kubernetes intellectual property (IP) wasn’t being fully exploited by customers. VMware certainly had a lot to offer, but it didn’t have a common platform that enabled companies at different stages in their Kubernetes journey to meet all of their needs regarding virtual machines (VM) and Kubernetes containers.

But that’s been rectified; now VMware Cloud Foundation (VCF) becomes a [single platform](https://thenewstack.io/vmwares-private-cloud-shift-under-broadcom/) for VMs and containers, with many enhancements such as multicluster management and a number of other features for cloud native environments.

## A Catalyst for Focus
The Broadcom acquisition served as a [catalyst](https://thenewstack.io/vmwares-private-cloud-shift-under-broadcom/) for integrating VMware’s entire private cloud stack and services into VCF. While VMware previously had many infrastructure and management components within the VCF stack, Broadcom helped bring much-needed focus — and the ability to support organizations’ full range of Kubernetes runtime and unified management requirements. The Kubernetes runtime license is already included in VCF license, so there is no need for additional licenses.

“The Broadcom model emphasizes understanding customer needs — where customers are, and what they require to be successful on the platform. VMware has always had strong IP and cutting-edge technology, but prior to the acquisition, much of it was not being fully utilized, especially for newer container-based workloads,” [Timothy Carr](https://www.linkedin.com/in/timmycarr/), product management leader for Kubernetes offerings in the VCF Division at Broadcom, told me in an interview. “The acquisition clarified this distinction. It enabled VMware to identify valuable areas, recognize where new applications were heading, and determine what needed to be done to stay competitive and offer public cloud-like agility.”

The shift toward Kubernetes greatness through VCF largely involved the deeper integration of the Kubernetes runtime — vSphere Kubernetes Service (VKS), formerly known as [Tanzu](https://tanzu.vmware.com?utm_content=inline+mention) Kubernetes Grid — and its famous VMs and support infrastructure.

“This is VMware going back to basics, which it needs to do to convince customers that VCF is a viable platform for running containers and VMs side by side,” said [Torsten Volk](https://www.linkedin.com/in/torstenvolk), an analyst with TechTarget’s Enterprise Strategy Group. “VMware still has one large asset: legions of administrators that grew up with vSphere. Showing these VMware folks a clear path toward becoming part of the app modernization story will be critical to convincing enterprises to try out Kubernetes on [VCF].”

## Deep and Wide
![VCF is a single platform for running VMs and containers.](https://cdn.thenewstack.io/media/2025/04/f817653a-vmwarecloudfoundation.png)
VCF is a single platform for running VMs and containers. (Source: VCF)

A key component underpinning VCF’s support for Kubernetes consists of its VMware vSphere Supervisor. The Supervisor functions as a platform and a control plane on which a robust set of infrastructure and cloud services, including Kubernetes cluster services, can be provisioned. These include VKS (the Kubernetes runtime), multicluster management, VM services, vSphere Pods, network services, storage and backup services, identity and access control services, image registry, and many other capabilities.

“Previously, there were multiple disparate APIs spread across different areas for VMs, containers and networking services,” Carr said. “The advantage of the new approach is the integration of Kubernetes and VMs APIs with a single operating model. This enables streamlined processes for both workloads.”

For example, if you need to build and run an AI application, you must prepare a Kubernetes cluster with the Nvidia GPU operator. Additionally, data scientists require a workstation with access to GPU resources. “All of this can now be orchestrated using YAML configurations and operated by existing enterprise VMware infrastructure workflows, making the environment significantly more powerful,” Carr said.

“Ultimately, the platform now supports the delivery of various types of applications — whether virtual machine-based, Kubernetes-based or a combination of both. The extensibility provided by Kubernetes makes these capabilities resemble a cloud-like infrastructure, enhancing overall efficiency and flexibility,” he continued.

The integration of Kubernetes into VCF indeed has “come a long way” from an approach focused on scripting deployment and management tasks from the bottom up, Volk said. “VCF has evolved to offer a much more declarative and therefore consistent and scalable approach that is necessary for running cloud native apps,” Volk said.

## Kubernetes Updates Now
VMware’s engineers say they have broken with the past by prioritizing shipping the latest version of Kubernetes, targeting within two months of the upstream release. This helps ensure alignment with the latest versions used by hyperscalers, Carr said.

The goal was to create a deeply integrated Kubernetes offering on VCF, much like what hyperscalers have done, Carr said. “[AWS](https://aws.amazon.com/?utm_content=inline+mention) has EKS — the most integrated version of AWS Kubernetes. The same applies to AKS on Azure and GKE on [Google Cloud](https://cloud.google.com/?utm_content=inline+mention),” Carr said. “We achieved that same level of integration on VCF infrastructure with VKS and are already making additional progress toward that goal.”

Additionally, built-in security capabilities make it by far the most secure Kubernetes platform running on the company’s infrastructure, Carr claimed. It’s “something other vendors cannot fully replicate. We will continue to leverage this advantage, as it builds the best Kubernetes stack on VCF,” Carr said.

“Finally, it is important to note that this is not exclusively about Kubernetes — everything is built on top of the company’s virtualization platform, which has been successfully operated for over 20 years.”

With VCF, VMware offers a single platform with a built-in Kubernetes runtime and a [CNCF](https://cncf.io/?utm_content=inline+mention)-certified Kubernetes distribution for organizations to run modern containerized applications alongside traditional VMs on the same infrastructure. VCF was designed to simplify Kubernetes deployment and management while unifying compute, storage, networking and security — which VMware says reduces total cost of ownership and operational complexity. VMware is touting VCF as a major offering following the Broadcom acquisition. CIOs and anyone involved in DevOps operations should at least give it a strong look as a platform to standardize on.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)