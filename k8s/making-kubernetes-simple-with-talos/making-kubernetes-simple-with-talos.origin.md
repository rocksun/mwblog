Kubernetes marks its 10th anniversary this year with the release of version v1.30.0, solidifying its status as the cloud platform of choice. Self-managed Kubernetes clusters like EKS GKS and AKS represent 73% of the total cluster, remaining 27% are self-managed as per
[Dynatrace](https://assets.dynatrace.com/en/docs/wp/bae3218-wp-kubernetes-in-the-wild-en.pdf?_ga=2.202268564.403052509.1714528198-1455211400.1714528198). The last decade has been an era of public cloud but due to increasing costs, some businesses are trying to find a balance with the hybrid cloud. Approximately 76% of organizations now leverage multiple clouds which is a combination of public and private clouds as per [VMware](https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/docs/vmware-ebook-state-of-kubernetes.pdf). Kubernetes allows us to build a multi-cloud and private cloud layer on the hardware of choice and in a cost-effective way without committing to one specific cloud.
Despite Kubernetes' growing adoption, concerns persist around cost efficiency, reliability, and security. Transitioning from Kubernetes virtual machines to bare metal infrastructure offers performance benefits by eliminating the hypervisor layer, streamlining troubleshooting processes, and maximizing resource availability for applications. Bare metal setups empower organizations with complete control over hardware components, facilitating tailored optimization for specific workloads. With the right engineering practices and the integration of Kubernetes, organizations can achieve feature parity with public cloud offerings. Historically, running Kubernetes on bare metal posed challenges due to operational complexity, particularly in managing cluster lifecycles. However, these obstacles have been overcome with the introduction of
**Talos**, which we will explore further in this article.
Introduction to Talos
Talos is a very minimal operating system that is written in Golang. Talos was designed as an OS-specific for maintaining the Kubernetes cluster. To make Kubernetes infrastructure more reliable we need to make sure that each node runs the same version of the Operating system. Talos can help us keep Kubernetes infrastructure more reliable and consistent by adding the immutable idealogy on which Talos is built. Talos always runs as a SquashFS image which is a read-only file system in Linux. The total size of Talos SquashFS image is around 80M. Talos intentionally omits components such as systemd, GNU utilities, console packages, bash, or SSH binaries to minimize the attack surface and reduce the likelihood of security vulnerabilities. Instead, it relies on a modern API for managing system operations. Talos only contains what’s needed. Instead, everything is managed by a modern API. Talos focuses a lot on Immutable infrastructure ideology. But what is an immutable infrastructure?
Immutable Infrastructure
Once a system is deployed, you won't be able to make any changes to it; this concept is referred to as immutable infrastructure. If changes are needed in an immutable infrastructure, a new infrastructure is created with the desired modifications, rather than altering the existing one. Having an immutable infrastructure makes staging, pre-production, and production environments more consistent. And having consistency between nodes on bare metal k8s infrastructure is the most important. In this type of infrastructure, our applications are more tightly coupled with the operating system which is a disadvantage of immutable systems.
Benefits of using Talos
-
Talos maintains consistency throughout the system and avoids any configuration changes. Talos calls this “Predictability”.
-
Talos aims to make Kubernetes infrastructure completely immutable, thereby enhancing reliability, security, and consistency. This makes Talos an ideal choice for bare metal servers running Kubernetes.
-
Talos is designed to be immutable so it runs on RAM and not on disk. Because Talos is a SquashFS image it has fewer write points which are Ephemeral in nature.
-
Talos is highly secure.
-
Talos is a very lightweight Operating system that has around 12 Binaries all meant to run Kubernetes.
-
Talos is API-driven.
-
Talos follows the recommendation given by KSPP (Kernel Self Protection Project) -
[KSPP Documentation](https://docs.kernel.org/security/self-protection.html)
Use cases
Talos is great for self-managed Kubernetes clusters but platforms like
[CIVO](https://www.civo.com/docs/faq#why-does-civo-use-talos-linux) provide support for deploying Kubernetes clusters using Talos. Below are some use cases of running Kubernetes with Talos. **Edge Applications:**
To manage a massive fleet of edge devices, Kubernetes is one of the best choices available. Kubernetes is not only designed for container orchestration but can also effectively manage edge devices. To ensure that our edge applications are reliable and secure, it's essential to have a secure and reliable Kubernetes environment. Talos is an excellent fit for edge devices due to its security and reliability and immutable ideology.
**Kuberntes on Bare metal:**
Utilizing Kubernetes on bare metal eliminates unnecessary abstractions, providing our applications with total control over the hardware. Talos stands out as an excellent option for deploying Kubernetes on bare metal servers. It removes unnecessary configuration and troubleshooting and makes Kubernetes deployment easy on bare metal.
**AI & Machine Learning Workload:**
Kubernetes proves to be an ideal platform for testing and training new machine learning models, with the capability for seamless deployment to larger-scale environments. Maintaining consistency across deployments is crucial for ensuring safe and stable model deployment. Talos plays a key role in this by providing a consistent environment, enabling reliable scaling of models based on demand.
Architecture and Design
Talos Architecture consists of many different components that have a gRPC interface defined. All the communication between Talos components happens through gRPC.
Talos File System Partition
- EFI: Stores EFI boot data.
- BIOS: Used for GRUB second stage boot.
- Boot: Used for bootloader, stores initramfs and kernel data.
- Meta: Stores metadata about the Talos node.
- State: Stores machine configurations.
- Ephemeral: Mounted at /var, used for storing ephemeral data.
Talos has 3 layers to its file system:
- rootfs: It is the core layer with read-only squashfs. Squashfs is then mounted as a loop device into memory.
- tmpfs: This file system is used for runtime-specific needs.
- system: Required for internal operations.
For example, Talos will write to /system/etc/hosts and then bind it to /etc/hosts. Instead of making /etc writable, Talos only makes specific parts of /etc writable. /system is completely recreated on each boot. For persistence at boot, Talos creates overlay’s fs. /var is owned by Kubernetes. This directory is used by etcd to write data. This data is only deleted when the machine is upgraded or reset, to avoid this we add a "--preserve" option while upgrading.
Components
talosctl is a CLI tool that is used to interact with all the components in Talos. It is similar to how we use
kubectl to interact with kube-api. Similarly,
talosctl is used to interact with the apid.
**apid:**Talos is API-driven, and
apidis responsible for providing the gRPC endpoint to interact with different components.
apidis present on each node including the control plane.
-
**machined:**It is responsible for handling the API request from
apid, and does the resource and controller management.
-
**trustd:**It is a daemon that is used to establish trust across the system. It is used to establish trust between nodes.
-
**udevd:**It is used to set up necessary links in
/dev.
Controllers and Resources
-
**Resources:**They are similar to resources in Kubernetes, resources are of different types and contain metadata like namespace, type etc. A resource can uniquely identify by its namespace. The “MachineConfig” resource reflects the current machine configuration.
-
**Controllers:**In Talos, controllers run as threads. A controller can manage multiple resource types, and each resource type can have numerous resources. To avoid conflicts, only a single controller is responsible for managing a specific resource type within a namespace. Talos stores the resource types defined for controllers in the meta namespace.
Demo
In this article, we are using Docker to showcase the capability due to the unavailability of bare metal machines. Subscribe to our blog as we are planning to share how to run Talos on bare metal in future post. We will learn how to create a Kubernetes cluster using Docker.
Set up Docker and Talos Cluster
Prerequisites
Before proceeding, ensure you have the following installed:
[Docker Engine](https://docs.docker.com/engine/install/) [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
- talosctl
*Note: talosctl and Talos OS ISO image versions should be the same. For more information, check the releases.*
Mac:
brew install siderolabs/tap/talosctl
bash
Linux:
wget https://github.com/siderolabs/talos/releases/download/v1.7.0/talosctl-linux-amd64
chmod +x talosctl-linux-amd64
./talosctl-linux-amd64
sudo mv ./talosctl-linux-amd64 /usr/local/bin
bash
Installing a three-node cluster using docker and talosctl. The below command will create a 3-node cluster (controlplane, workernode-1, workernode-2).
talosctl cluster create --workers 2
bash
Let's check the number of nodes created along with the Operating system information
kubectl get nodes -o wide
kubectl get node talos-default-worker-1 -o json | jq -r '.status.nodeInfo.osImage'
bash
Let’s clean and delete the cluster
talosctl cluster destroy
bash
Conclusion
Talos plays a crucial role in managing Kubernetes environments. Its simplicity simplifies the configuration of Kubernetes clusters significantly. The immutable ideology of Talos greatly enhances infrastructure security and consistency.
FAQs
Talos vs k3s
There is no direct comparison between Talos and k3s. However, when considering the deployment of a Kubernetes cluster k3s requires an operating system and has other dependencies that vary based on the underlying OS. Whereas Talos focus is to run the Kubernetes cluster with its immutable idealogy keeping it secure and reliable. Talos makes Kubernetes deployment much simpler.
What are the binaries that Talos contains?
- The init binary in Talos is responsible for running kubelet and container runtime.
- Containerd is the runtime in Talos along with runc.
- Modprobe is used to load modules for some binaries. Modules can be added to Talos, or we can use pre-built ones from
[Image Factory](https://factory.talos.dev/).
- For volume management, lvm is used.
- udevd is used to collect messages from the kernel and pass them to other systems.
- Binaries like xfs_repair are used to repair the XFS file system.
Is Talos Free?
Talos is a free and open-source Operating system under Mozilla Public License Version 2.0 which allow commercial usage. Check more at
[Talos Github repository](https://github.com/siderolabs/talos).
Why Use Talos?
Talos makes the Kubernetes environment more secure and reliable. As we know Talos is meant for distributed systems like Kubernetes and if you want your Kubernetes environment to be more secure and reliable you should use Talos.
Can we run Talos on Bare metal?
If you're looking to configure Kubernetes on bare metal, Talos is the ideal choice. Stay tuned to learn how to deploy Talos on bare metal, subscribe to our post or reach out to directly to discuss this further.
Who provides additional support for Talos? [Sidero Labs](https://www.siderolabs.com/)
- CloudRaft for Implementation and Support.
[Connect with us](/contact-us)to discuss further.