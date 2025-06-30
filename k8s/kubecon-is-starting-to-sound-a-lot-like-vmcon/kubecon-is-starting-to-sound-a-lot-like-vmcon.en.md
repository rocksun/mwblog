For much of the past decade, “cloud native” has been synonymous with the rise of containers, and, by extension, the slow erosion of virtual machines as the dominant abstraction for workloads. But at this year’s KubeCon EU in London, the narrative began to shift. In hallway tracks, project pavilions, and mainstage talks, a recurring theme surfaced: VMs aren’t going away; they’re converging with (or at least becoming adjacent to) containers, and Kubernetes is becoming the universal control plane for both.

This growing overlap signals more than just workload coexistence. It marks the beginning of a major replatforming wave, one where Kubernetes isn’t just orchestrating pods, but emerging as the operating model for running VMs, legacy apps, and future-forward workloads alike. What’s taking shape is not just a technical migration, but a redesign of how infrastructure teams think about system boundaries, operational responsibility, and the abstractions they use to deploy and secure applications.

Some of the most revealing clues were on display at KubeCon, where open source momentum, market pressure, and new tooling have begun to solidify a once-fringe idea: Kubernetes as the substrate for all workloads. And with that comes some fascinating implications.

## An Urgent Requirement To Move Somewhere

A long period of “stability” is perceived to be coming to an end, especially when we talk about virtualized workloads. The incumbent platform for virtual workloads is currently causing various types of turmoil for its customers and end-users. Changes to licensing are expected to dramatically increase operational expenditure, forcing small to medium-sized customers to quickly find alternatives. Additionally, removing flexibility in selecting which products are actually required, and demanding customers purchase the entire portfolio again increases costs, forces a complex platform and utilisation of more unnecessary resources.

Unfortunately, at the moment, the future isn’t certain as people try to determine where this “somewhere” will be where they re-platform their virtual workloads. That being said, this was KubeCon. It is a safe assumption that Kubernetes will (if not already) feature as a platform for workloads within their infrastructure shortly. This inevitably leads to a conversation about what is required to build the potential “one platform for all workloads” conversation!

## What Components Are Required To Build a Cloud Native VM Platform

The basis for the next generation VM platform inevitably was going to be Kubernetes, which unfortunately has a bit of (personally speaking) bad reputation for being difficult to actually get up and running. This may have been more true in the early days of Kubernetes, where various OpenSSL magic and copying certificates back and forth were required along with various etcd tinkering.

Good news, however, those days are very much behind us, the Kubernetes project has tooling like kubeadm or cluster-API that automates the standing up of Kubernetes nodes or even the entire cluster. Additionally, if you want a complete out-of-the-box experience, then there are a number of certified, vendor-backed Kubernetes distributions that will provide enterprise-grade installation and support.

The ecosystem around Kubernetes and cloud native is arguably one of the most thriving, so it should come as no surprise that several projects have been created to enable the running of virtual machines alongside your containerized workloads. A quick search around GitHub has some projects that are over 9 years old! However, it has become pretty clear that one project has become the de facto standard for enabling virtual workloads on Kubernetes, and that is the[kubevirt](http://kubevirt.io) project, which is also the same project most of the Enterprise Kubernetes offerings are based on!

This project packages up all of the components required in order to run a virtual machine on a Linux host (namely qemu, libvirt and other helper tooling), and further enhances Kubernetes with additional objects such as the virtual machine. Now, a single control plane can retrieve running pods with kubectl get pods or virtual machines with kubectl get virtual machines in the exact same manner.

## Migrating Workloads

There have been multiple types of workload migrations over the years, and we’re currently in the “Modernising to cloud native” era. However, before all these workloads needed to be moved to a virtual platform, and that was largely done through P2V software, which is a physical to virtual conversion. The process for this was often to install an agent within the physical machine that would be able to read the contents of the disk(s), this agent would then connect to the virtual platform where a target VM would be created with the copied contents of the disk. A simple sounding process, however, physical machines have a huge variety of physical devices, each of which would require a variety of device drivers. Often, after a p2v, you will find that your virtual machine will no longer boot correctly, as these device drivers wouldn’t find the hardware, or devices would now look different.

These concerns exist today, moving from one hypervisor to another is referred to as v2v and still comes with the same caveats as different hypervisors emulate different devices. Moving to kubevirt usually means moving to a [virtio](https://wiki.osdev.org/Virtio) device, which again can mean a system that is confused/broken when it is booted up after being moved.

## Silo’d Expertise

A lot of the conversation brought into focus the large amount of time and investment a lot of companies had already put into hiring and training a team to manage their current virtualization platform. This raises big questions about who (which team) is going to build the platform, how workloads share the platform, there should be a cluster per workload (VMs and Containers) and ultimately, who is going to [operate and own the cluster](https://thenewstack.io/how-to-cut-through-a-thicket-of-kubernetes-clusters/) from a day-to-day perspective.

Building a brand new platform from the required [open source components will require significant experience with Kubernetes](https://thenewstack.io/open-source-kubevirt-vm-management-with-kubernetes-is-a-work-in-progress/) and can provide the capabilities to run virtual workloads. However, it’s no secret that this experience of using this platform will be worlds away from what people will have been used to before. A clean user interface for creating virtual machines or moving a VM to a different network simply doesn’t exist. As with all things Kubernetes, it’s going to be YAML, and a whole lot of YAML.

## What Does the Future Potentially Look Like?

It’s not all doom and gloom, fortunately! A lot of work is being done in order to improve the experience. A number of projects initially appeared to handle the running of virtual machines; however, the ecosystem appears to have settled on kubevirt being the obvious choice. This has led to an influx of committers to the kubevirt project, adding multiple new features and stability improvements. Additionally, end-to-end solutions are being developed to reduce operational complexity, such as the Harvester project from SUSE or OpenShift Virtualization from Red Hat.

In order for any new virtualisation platform to be successful, there are certainly going to be a few key things that will need addressing:

* Expected like-for-like features, that are a given in their current incumbent platform, will need to be implemented, think dynamic resource management combined with workload migration capabilities
* A clean and efficient method of moving virtual machines from one platform to another
* Reduced operational overhead, allowing easy management of a new virtualisation platform

There are still gaps in the current state of alternative virtualisation platforms (built on Kubernetes), however, because this is all [open source, there is nothing stopping anyone from contributing](https://thenewstack.io/open-source-founders-need-community/) and helping move things along!

We’re seeing the first wave of this with virtual machines being brought under the Kubernetes umbrella. But look closer, and you’ll find similar collisions across the stack: load balancers becoming service meshes, firewalls running inside DPU-enabled switches, and [observability pipelines feeding directly into security engines](https://thenewstack.io/spans-what-are-they-and-why-should-mobile-engineers-care/). What used to be hard boundaries are becoming blurry zones of convergence.

If VMs and containers are no longer opposites but peers in the same platform, what other dichotomies are next to fall?

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.