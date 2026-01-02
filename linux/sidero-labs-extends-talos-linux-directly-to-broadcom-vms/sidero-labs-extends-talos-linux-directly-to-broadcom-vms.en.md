ATLANTA — [Sidero Labs](https://www.siderolabs.com/?utm_content=inline+mention)’ Talos [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) was created to offer an alternative to the high cost and complexity of managing disparate [Kubernetes](https://thenewstack.io/kubernetes/) and other deployments. It serves as a lightweight but highly scalable operating system designed for Kubernetes.

In many ways, it does the opposite of [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)‘s Linux OpenShift, [SUSE Rancher](https://thenewstack.io/suse-upgrades-its-rancher-kubernetes-management-family/) and other Kubernetes distributions. In all of these, Kubernetes is installed and runs on top of a general-purpose operating system. Sidero Labs, with its open source Talos Linux, argues that this entire foundation is not only unnecessary but a liability, especially for private cloud and edge use cases.

It can also support virtual machines (VMs), although there remain limited VMs that run on Kubernetes, and in the case of Broadcom’s vSphere, workarounds are required to integrate it with Talos Linux.

But now Omni, Sidero Labs’ Software as a Service (SaaS) built on Talos Linux, can be used to [automatically provision Talos nodes in vSphere](https://github.com/siderolabs/omni-infra-provider-vsphere).

“Talos has always worked great on all VMs,” Sidero Labs CEO [Steve Francis](https://www.linkedin.com/in/francissteve/) told me during [KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/). “What is new is the infrastructure provider for Broadcom [VMware](https://www.vmware.com/?utm_content=inline+mention) on Omni — this means Omni can create VMs on VMware infrastructure in order to create clusters, scale them out, etc.”

The integration of systems with operating systems is an interesting development, such as when projects incorporate or integrate with different operating systems. However, the specific work being discussed with [VMs](https://thenewstack.io/the-challenges-of-uniting-vms-and-containers-on-a-single-platform/) was built internally and was not in relationship with VMware.

“A lot of our customers are still running on virtual machines. Many of them are using VMware for that infrastructure, certainly for the next three years,” Francis said. “Our customers wanted a way that they could easily scale up and scale down clusters on VMware. This capability was needed without having to go to their VMware provisioning group to create new virtual machines statically. As a solution, a provisioner was written for Omni, which is our multicluster management SaaS.”

The Omni SaaS allows the user to plug in an infrastructure provider. If a cluster needs to scale up, it will create the VM on your VMware infrastructure dynamically. It can do this as many times as it needs to hit that scaling constraint, and it can scale it down and destroy the machines. This basically makes it completely transparent to scale your clusters up and down on VMware infrastructure.

“The provisioning system supports VM infrastructure. It supports Kubernetes and also has similar functionality for bare metal. We also have similar functionality now for Oxide’s hyperconverged infrastructure.”

## Bare Metal vs. VMs and Talos Linux

Almost everything, the vast majority of infrastructure, container and infrastructure, is on VMs now. However, in Sidero Labs’ customer base, a lot of them run bare metal. The provisioning system will work with containers running on bare metal. There is an infrastructure provider for bare metal, where it can actually turn the machines on using methods like Intelligent Platform Management Interface (IPMI) or Redfish.

“The philosophy is that you are better off running Kubernetes directly on the bare metal rather than in a virtual machine,” Francis said. “If you do need to use a VM, that’s where the VMware provider comes in. The Talos Linux operating system was oriented more towards bare metal.”

The virtual provider for VMware was built because people have a large investment in their VMware infrastructure for running a lot of VMs. Groups that wanted to adopt Talos Linux often had to face the constraint that “all we can get is VMs.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)