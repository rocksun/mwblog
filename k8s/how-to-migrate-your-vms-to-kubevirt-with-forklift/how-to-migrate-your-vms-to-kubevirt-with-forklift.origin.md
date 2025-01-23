# How To Migrate Your VMs to KubeVirt With Forklift
![Featued image for: How To Migrate Your VMs to KubeVirt With Forklift](https://cdn.thenewstack.io/media/2025/01/77fcecf2-migration-1024x576.jpg)
As companies increasingly move to the cloud, they’re running into a problem: Many large, legacy, virtualized workloads cannot be easily refactored to be cloud native, and organizations are opting to keep them running as virtual machines, while slowly introducing containers and Kubernetes for new applications. In short, VMs are here to stay.

But something that’s not often mentioned is exactly how to move your virtualized workloads to a Kubernetes cluster — and that matters when you have potentially hundreds or thousands of them.

Let’s explore what it really takes to [migrate a virtual machine](https://thenewstack.io/the-future-of-vms-on-kubernetes-building-on-kubevirt/) from VMware to Kubernetes, how some open source projects can help automate parts of the migration, and how Spectro Cloud’s new VM Migration Assistant makes the process straightforward and replicable, even if you’re not a Kubernetes expert yet.

## The Very Manual Way: virt-v2v
First, let’s do it the hard way and see how we can manually migrate a virtual machine from VMware vSphere into a KubeVirt-enabled K8s cluster.

### Guest Conversion
Under the hood, [KubeVirt runs VMs](https://thenewstack.io/the-future-of-vms-on-kubernetes-building-on-kubevirt/) using a kernel-based virtual machine (KVM), a Linux-native, Type 1 hypervisor. So as a start to our migration, we’ll want to convert our VMware virtual machines to be compatible with KVM. There are a few tools that can be used to accomplish this. We’ll look at virt-v2v, an open source offering for converting guest operating systems from a number of proprietary hypervisors to KVM.

To get started, we’ll need virt-v2v installed on a jump host. Virt-v2v is available through most package managers. We’ll want to make sure our jump host has access to both our vCenter and the target Kubernetes cluster.

Next, we’ll need access to the machine in question. Virt-v2v supports local file paths, as well as directly accessing the virtual machine disk over a network. At this stage, we should power off the VM to prevent data loss or corruption. It is also a good idea to back up the disk using snapshots.

When our jump host is set up, the virtual machine we wish to migrate is powered off and the disk is accessible. We can now begin the conversion process.

Once the conversion process is complete, we can inspect the working directory to see that a converted disk is available. Aside from converting the disk, this process also removed VMware Guest Tools (they won’t be needed anymore) and installed VirtIO drivers, which are crucial for the VM to function properly after the migration.

Now that our virtual machine disk has been converted to RAW, a KVM-friendly format, we need a [way to make it available inside our Kubernetes cluster](https://thenewstack.io/cluster-api-offers-a-way-to-manage-multiple-kubernetes-deployments/).

### Disk Import
Containers are typically thought of as ephemeral. Because of this, the idea of virtual machines running in Kubernetes seems somewhat odd, given that they are persistent between power cycles by design. However, using K8s primitives such as DataVolumes (PVs) and PersistantVolumeClaims (PVCs), we can persist a virtual machine disk, even when the VM is powered off.

To get started, we’ll want to make sure that [Containerized Data Importer (CDI)](https://github.com/kubevirt/containerized-data-importer) is configured in our KubeVirt cluster. CDI is a persistent storage [management add-on for Kubernetes](https://thenewstack.io/managing-kubernetes-clusters-for-platform-engineers/), primarily used to provide a declarative way to build virtual machine disks on PVCs for Kubevirt VMs.

Next, using virtctl, a KubeVirt CLI for interacting with virtual machines in a Kubernetes cluster, we can begin the data import, using CDI to import our disk to the cluster. By choosing to upload to a DataVolume, CDI will automatically configure a PVC with the appropriate settings, based on the default StorageClass for the cluster.

Once the data upload is complete, our virtual machine disk is ready to be bound to a pod.

### Virtual Machine Template
Now that the disk is imported, we can define what our virtual machine should look like. This is done with a custom resource (CR) called a VirtualMachine. Here, we can define things such as resource requests and attached disks. To attach our imported disk, we will reference it in the disks and volumes sections.

Finally, we can install this VirtualMachine into our KubeVirt cluster. Now, using virtctl, we can power on our virtual machine. And voilà — we have successfully migrated a VMware vSphere virtual machine into a Kubernetes cluster.

The running VM can now be accessed using virtctl or by accessing the Virtual Machine Orchestrator (VMO) dashboard in Palette.

Simple, right? Now, just do this for every machine, on every host, in every data center. (This might get messy.)

## The Less Manual Way: Forklift
Higher abstraction tooling has emerged around virt-v2v to help automate conversions and migration at scale — no Bash required. Projects like [Forklift](https://github.com/kubev2v/forklift) aim to provide a Kubernetes-native way to migrate multiple machines from VMware to KubeVirt. Forklift does this by introducing a controller, which reconciles a number of custom resources to orchestrate the migration.

To get started, we’ll need a running Kubernetes cluster with KubeVirt configured. Next, we can install Forklift. This involves deploying components such as Operator Lifecycle Manager (OLM), Certificate Manager, Forklift Operator, Forklift Controller and several supporting operators to handle validation. Once the relevant Custom Resource Definitions (CRDs) are installed and the operators are deployed, we can begin setting up a migration.

### Custom Resources
Forklift performs migrations using six Kubernetes CRs:

**Provider**: a representation of a VM platform. This can either be vCenter (the source) or KubeVirt (the destination — our target cluster). The provider contains information such as the source URL and references to secrets containing credentials.**Host**: an optional reference to a specific ESXi host. This can help speed up migration by bypassing vCenter and accessing the disk directly from the hypervisor.**Storage map**: a way of mapping vCenter storage to Kubernetes storage classes.**Network map**: a way of mapping vCenter network configuration to Kubernetes networking.**Plan**: the central resource bringing all data related to a migration together. It references providers, hosts and maps, as well as detailing all the VMs that should be migrated.**Migration**: represents a running or finished plan.
Most of these resources rely on information from vCenter or ESXi. For example, we need to [know which networking and storage devices](https://thenewstack.io/honey-i-secured-your-boot-edge-trusted-boot-with-kairos/) our VMs are using, as well as the IDs of the VMs. This can be queried using tools such as VMware’s govc.

Additionally, several secrets and ConfigMaps are used to configure the provider and certain aspects of the plan. All of these should be created alongside the six custom resources.

### Running a Migration
To begin the migration, install all the custom resources and their accompanying configuration into your Kubernetes cluster. Once they are all reconciled and enter “Ready” state, the migration will begin, signified by the migration CR transitioning to “Executing” state. You can monitor the progress of the migration using tools such as kubectl.

The process of the migration can be generally outlined as follows:

**Disk allocation**: PV and PVC are created.**Image conversion**: A pod is created to run the virt-v2v process.**Disk transfer**: The converted image is uploaded using CDI.**VM creation**: A VirtualMachine manifest is installed in the cluster.
Once the plan reaches “Success” status, the migration is complete and a virtual machine has been created in the target namespace.

## The VM Migration Assistant Way
Having a controller to orchestrate the migration for you is convenient. But managing plans, fetching and filling out VM metadata, and manually handling storage and network mapping is tedious and error-prone.

At a large scale, filling out this much YAML starts to feel like you are still doing the migration completely manually. And if you’re coming from vCenter’s UI and just getting into the world of Kubernetes, you might be looking for a more familiar interface. Enter VM Migration Assistant.

Building on the core functionality of Forklift, Spectro Cloud Palette’s VM Migration Assistant is a web-based UI for planning, configuring, managing and running migrations.

Whether you want to migrate a couple or a couple hundred virtual machines (up to 500 in a single plan!), the Migration Assistant UI handles the complexities of setting up and deploying CRs, ConfigMaps and secrets for you, so you can focus on the more important task of planning a mass infrastructure migration.

### Using the Assistant
With the VM Migration Assistant pack installed in your Palette-managed cluster, you can access the UI in your browser.

You’ll be guided through configuring a provider, with validation handled for you and any issues transparently displayed. Once your provider is deployed and ready, you can start setting up your plan.

Using the provider, VM Migration Assistant fetches all the virtual machines in your source environment. You can filter, sort and inspect the VMs to easily construct a plan. Warnings about potential issues with the VMs — such as names not conforming to RFC 1123, or Changed Block Tracking being disabled — are clearly visible to help you make informed decisions.

Once all the desired VMs have been selected, options for storage and network mapping are presented. Sensible defaults are preconfigured, but additional mappings can be manually added if custom configuration is required. A target namespace can also be specified.

When you create the plan, all necessary custom resources are created on the cluster. After a few seconds, the plan will go into “Ready” state, meaning it can be started. In the plan overview, you can further customize the plan by selecting a custom source network to use for the migration, or adding hooks — a way of performing operations on your VMs before or after the migration.

Once started, you can monitor the migration progress in the UI, with a step-by-step breakdown for each VM included in the plan. You can also monitor migration statistics and inspect any resource related to the migration.

### Warm Migrations
So far, we’ve been covering cold migrations, where the source virtual machine is powered off the entire time. These migrations are technically more simple, but require more downtime. Warm migrations offer an alternative, using snapshots.

Warm migrations can be carried out using VM Migration Assistant. To get started, set up a plan the same way as a cold migration. At the plan overview screen, toggle the “Warm” switch to mark the migration as warm. When the migration starts, your source virtual machine will continue running. Snapshots of the disk will be taken at predetermined intervals and imported to the Kubernetes cluster. You can then schedule a “cutover” — the moment at which the VM will be briefly powered off and any new data since the last snapshot will be transferred. Finally, once the transfer is complete, the VM will be powered on inside the Kubernetes cluster.

By transferring most of the disk data while the VM is still running, warm migrations help minimize downtime and allow the lengthy portion of the migration to be carried out asynchronously.

Of course, warm migrations come with their own set of challenges. Since multiple data transfers may need to take place during the course of one migration, and the cutover stage will still require some downtime, they should be planned carefully to ensure minimal downtime and to reduce strain on the host network. Post-migration validation of data also is crucial to verify that no data loss or corruption occurred at the moment of the cutover.

### Importing OVAs
An Open Virtual Appliance (OVA) is a popular format for packaging virtual machines. It is a single, portable archive that contains the complete definition and content of a virtual machine.

In a traditional VMware data center, an OVA can be quickly imported to deploy a new virtual machine. OVAs typically contain not only a VM spec but also the application running on it. These applications often require OVF XML configuration obtained from the VMware Tools daemon when the machine first boots up.

VMware has a suite of tools to facilitate this, but when the guest OS is converted, these tools are removed, as they are typically not needed for KVM-based machines. This means that not only does the application not have access to the environment, but you as the administrator don’t even have access to set the environment.

Since OVAs play a critical role in administering virtualized workloads and OVF environments are a crucial piece of the puzzle, it was important for us to address this issue and build a workaround.

When you create an OVA provider, VM Migration Assistant will parse all the OVAs that are present in the source. The required OVF environment variables will be extracted. When creating a plan, you will have the opportunity to configure any VM that needs to have environment variables set up. The variables will be attached to the VirtualMachine as a disk, and made available to the imported appliance as soon as it is started up.

## An Important Piece of a Bigger Puzzle
A complete VMware-to-K8s migration is a much bigger task than we discussed today. It involves careful planning, maintaining multiple parallel environments, configuring networking and ingress to ensure your users are not disrupted in any way, and much more.

It also needs to be done in a slow and controlled manner, and will likely take months or even years, depending on the size of the workload being moved. Unfortunately, this means it will take a long time for organizations to completely change their infrastructure.

Given all the complications of an undertaking as large as an infrastructure migration, you need all the help you can get. We have compiled a number of [webinars](https://www.spectrocloud.com/webinars/the-new-home-for-your-vms-kubernetes), [blogs](https://www.spectrocloud.com/blog/the-future-of-vms-on-kubernetes-building-on-kubevirt) and [reference architectures](https://www.spectrocloud.com/resources/collateral/vmo-architecture-pdf) to help facilitate the move.

A manual VM migration approach can be useful as a proof of concept for one or two machines, but as the scale grows, you need more automated tooling using Forklift or VM Migration Assistant.

To learn more about the VM Migration Assistant, [check out our docs](https://docs.spectrocloud.com/vm-management/vm-migration-assistant/), and be sure to [book a demo](https://www.spectrocloud.com/get-started) with our experts to see how we can help.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)