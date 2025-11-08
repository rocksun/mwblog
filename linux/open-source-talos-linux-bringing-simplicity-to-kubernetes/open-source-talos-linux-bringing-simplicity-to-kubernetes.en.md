**Disclosure:** Sidero Labs paid for the author’s travel and lodging to TalosCon.

The last few years have seen a [huge shift from the public cloud](https://thenewstack.io/why-companies-are-ditching-the-cloud-the-rise-of-cloud-repatriation/) to on-premises and private cloud infrastructure, thanks to a range of drivers — including skyrocketing costs and data sovereignty concerns. This is, in turn, having a major effect on Kubernetes management.

[Sidero Labs](https://www.siderolabs.com/?utm_content=inline+mention)’ [Talos Linux](https://github.com/siderolabs/talos) offers a refreshing alternative to the high cost and complexity of managing disparate Kubernetes and other deployments.

In many ways, it does the opposite of [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)‘s Linux OpenShift, SUSE Rancher and other Kubernetes distributions. In all of these, Kubernetes is installed and runs on top of a general-purpose operating system.

Sidero Labs, with its open source [Talos Linux](https://thenewstack.io/set-up-talos-linux-on-your-machine/), argues that this entire foundation is not only unnecessary but a liability, especially for private cloud and edge use cases.

“If your goal is to run workloads which come in containers, and as an orchestrator for those workloads, you choose to use Kubernetes, there is not much that you need on the host operating system,” [Andrey Smirnov](https://www.linkedin.com/in/smirnovandrey/?originalSubdomain=ge), engineering lead at Sidero Labs, told me at the company’s mid-October TalosCon event in Amsterdam.

“Your workloads bring everything with them. They’re in containers already … so they shouldn’t interact with the host that much.”

## Security Through Minimalism

The big idea with Talos is to make the host minimal and secure, Smirnov said.

“We can improve the security of the system, both by making it minimal and also by implementing the best security practices, which are way easier to implement,” he said.

Sidero is stripping away decades of [Unix-like thinking](https://thenewstack.io/ken-thompson-recalls-unixs-rowdy-lock-picking-origins/) about multiuser systems, Smirnov said: “You don’t have users at all. All you run is your workloads and containers … and Kubernetes.”

This minimalism enables “best security practices,” he added, such as a “read-only immutable root file system. Some Linux distributions can go with that, or close to that, but it’s kind of hard.” But with Talos, “We own the full stack. So, for us, it’s easy. We just make it read only, period.”

Smirnov noted that while Kubernetes is the current standard, the architecture is flexible: “In theory, we could have used something like Nomad, for example.”

What this means in practice was outlined by [Thomas Comtet](https://www.linkedin.com/in/thomas-comtet-sncf), head of the cloud native platform team at French railway operator SNCF. After successfully migrating 70% of the organization’s apps to the public cloud, his team was left with 30% that had to remain in private data centers.

When building SNCF’s new private cloud platform using [OpenStack](https://thenewstack.io/openstack-flamingo-reduces-technical-debt-boosts-performance/), the team sought to replicate the efficiency of the managed services they used on [AWS](https://aws.amazon.com/?utm_content=inline+mention) and Azure.

The SNCF team had managed Kubernetes services on the public cloud and had gained experience in using [Bottlerocket](https://thenewstack.io/3-immutable-operating-systems-bottlerocket-flatcar-and-talos-linux/), a Linux-based, open source operating system for running containers, Comtet told me during TalosCon.

“We know very well how to operate Bottlerocket with EKS or Azure Linux with AKS clusters,” he said. “This is very, very efficient. In fact, we really like it, and we wanted to recreate the same experience.”

Therefore, he elaborated, “We chose Talos mostly because it can compete with Bottlerocket. What we want to do, as a platform team, is have the same experience in the data center, and we achieved that in a less costly way.”

## Case Study: The Singapore Exchange and Talos

For the Singapore Exchange (SGX), the key attraction of Talos was the level of control it offered.

When the organization began planning the end of life of its Red Hat OpenShift deployment, the available options were either costly, overly complex or not aligned with SGX’s infrastructure strategy. But its team discovered Talos Linux and quickly engaged in a proof of concept that would reshape the organization’s platform strategy.

“For us, Talos made sense,” [Rushan Ratha](https://www.linkedin.com/in/rushanratha/?originalSubdomain=uk), head of platform engineering, SGX FX Group, told me at TalosCon. “It was uber lightweight [and] it met our security model. A security audit for me … [meant asking] who’s got access to all these machines?

“Well, not anymore. You don’t have SSH access [or] a root user. Everything is tightly controlled that way.”

Ratha said the team made the switch from Red Hat OpenShift to Talos Linux in “less than 24 hours.”

## The Omni SaaS Creation

After creating Talos, the next question for Sidero was how to automate infrastructure on a bigger scale. Sidero Labs first tried the [Cluster API](https://thenewstack.io/is-cluster-api-really-the-future-of-kubernetes-deployment/), but it raised some design issues.

“Whenever you change something, Cluster API says it wants to replace that machine,” Smirnov said. “This works great in the cloud, but on bare metal, that’s a disaster.”

Talos was developed with the opposite approach in mind: “Changes in place, upgrades in place, everything in place.”

Sidero then tried Terraform, but had mixed success. “This was way better, but we still had problems with this higher-level orchestration, such as a Kubernetes upgrade,” Smirnov said. “It’s a pain to encode that kind of orchestration.”

This full circle led to the creation of Sidero Labs’ Omni, a Software as a Service (SaaS) product. “Omni started with the exact opposite idea. Instead of automatic provisioning, the model was bring your Talos,” Smirnov said.

“A user can put a Talos image anywhere, even on an obscure cloud, and it will connect to Omni, and now you can manage it. This approach works better for bare metal, where the inventory is actually static.”

After the creation of [Omni](https://www.siderolabs.com/omni-signup/), users asked for dynamic provisioning capabilities, such as the ability to burst into the cloud and temporarily scale up into AWS. This led to Sidero implementing infrastructure providers for environments like Proxmox, bare metal, [VMware](https://www.vmware.com/?utm_content=inline+mention) and AWS.

“For a private data center, a bare metal infrastructure provider can handle PXE booting your machines, discovering them, wiping the disks and using PMI,” Smirnov said. “This provider can run in the data center but connect to your SaaS, Omni.”

And, he said, a user can run Omni on premises as well, “But Omni becomes the central management place.”

The rise of Kubernetes has been accompanied by concerns about its complexity. These have been exacerbated by a shift to on premises or private cloud. Sidero has made a strong case for its minimalist, security-first approach with Talos Linux and Omni. But the verdict comes in its practical deployment by organizations like SNCF and SGX.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)