# A New Approach to Two-Site HA Failover With K8s and Kubevirt
![Featued image for: A New Approach to Two-Site HA Failover With K8s and Kubevirt](https://cdn.thenewstack.io/media/2025/01/b8da5e73-main12-1024x614.png)
Twinned data centers have long been a staple of highly available systems. It’s a common practice in factories, hospital campuses and other mission-critical locations to duplicate the entire core IT infrastructure in a second server room or on-campus location, and have applications fail over to the second room when disaster strikes.

Of course, nobody wants a load of expensive servers sitting idle 99.9% of the time, so it’s also common practice to make the IT infrastructure virtual to create a single resource pool across both locations. When one location fails, you just have to restart the workloads from the failed location in the surviving location.

Over the past 20 years, [VMware](https://tanzu.vmware.com?utm_content=inline+mention) virtualization made this easier. With either a stretched vSAN or a backend storage array with synchronous replication, you could set up infrastructure across two locations and have it act as one. When a site failure occurs for any reason, all you’re really losing is 50% of the capacity for your VMs.

**Spanning Sites in a Cloud Native World**
But the world moves on. Today, many organizations are actively trying to[ reduce their dependency on VMware](https://www.spectrocloud.com/webinars/after-vmware-whats-next) and the post-[Broadcom ](https://broadcom-software.security.com/blogs/division/broadcom-software?utm_content=inline+mention)price increases. At the same time, more applications are now cloud native or at least containerized, meaning that a suitable alternative should provide a highly available platform for both virtual machines and containers.

As we’ve explored in the past, many enterprises are [looking to bare metal Kubernetes with KubeVirt to provide their new platform](https://www.spectrocloud.com/blog/production-ready-kubevirt-architecture-for-vms-on-kubernetes) for VM and container workloads in the data center.

But what about the common use case we described above: a two-room HA failover scenario at a campus edge location?

Several core components in Kubernetes are based on a majority quorum model, which means you need an odd number of instances to ensure quorum is maintained in the wake of any singular failure, and avoid a “split-brain” error situation.

But in a two-room situation where you may lose a full 50% of your infrastructure in one shot, it’s impossible to maintain quorum.

**Evaluating the Options**
If we want to run KubeVirt in a twinned data center environment to provide a highly available platform, we need to [solve some challenges](https://thenewstack.io/three-common-kubernetes-challenges-and-how-to-solve-them/).

You could, of course, run an entire Kubernetes cluster in one location, run a different Kubernetes cluster in the second location and implement replication across both clusters.

It’s definitely not a bad option, and you can do it today with [Portworx MetroDR](https://portworx.com/services/business-continuity-disaster-recovery/), which natively supports KubeVirt as documented [here](https://portworx.com/blog/disaster-recovery-for-red-hat-openshift-virtualization/). I have tested this personally, and it works as advertised.

There is, of course, the cost of [Portworx](https://portworx.com/?utm_content=inline+mention) itself and then an additional cost for MetroDR if you want continuous replication. This creates a bit of a barrier to entry, hurting the economic viability for smaller-scale deployments, especially at the campus edge, where you may need only one or a few rackmount servers for the workload.

So let’s look at some alternative technologies that can deliver the same benefits of a two-site HA solution on bare metal Kubernetes but in a simpler way to suit smaller deployments.

**Two-Node HA: Scaling Up From Boxes to Rooms?**
This is not the first time we have looked to solve the quorum issue and achieve high availability in a two-part architecture.

Our [two-node HA feature ](https://www.spectrocloud.com/blog/two-node-ha-kubernetes-for-edge-computing-cost-savings)was designed for far-edge locations like gas stations, stores and restaurants. Previously, organizations had the difficult choice of deploying just a single box to each of their thousands of sites (low cost but no redundancy) or deploying a three-node cluster (better availability but three times the cost — at scale).

We built a way to deploy a cluster with failover capability using just two nodes instead of the typical three: a middle option that provides hardware redundancy and 33% cost savings.

Palette two-node HA uses [kine](https://github.com/k3s-io/kine) to solve the quorum challenge associated with running etcd with only two nodes. The state store remains functional when one node goes offline.

A side effect of this capability is that such a Kubernetes cluster can survive a 50% infrastructure loss, which sounds exactly like the two-site HA failover use case.

Could we scale this same approach up to provide HA not just across two boxes but two rooms or proximate sites?

While the two-node HA feature tackles the etcd challenge, it’s up to the user to carefully select the remaining components in the Kubernetes stack to be able to survive a 50% loss of cluster nodes. Luckily, for most workloads higher up in the stack, this isn’t really an issue.

Even when an application is using quorum-based components, it can recover from failures by simply restarting lost pods from a deployment on the surviving node. It can be more difficult with daemonsets, as lost pods from a daemonset will stay down until the lost node is brought back online. But in most cases, daemonsets don’t require a majority quorum to function.

So, when it comes to the core framework of Kubernetes itself, we can support two-site HA architectures by leveraging the two-node HA feature in [Spectro Cloud Palette](https://thenewstack.io/virtual-kubernetes-clusters-with-spectro-cloud-palette/), running one control plane node in each location.

This solution also supports adding worker nodes to the [cluster to scale up the infrastructure](https://thenewstack.io/scaling-to-10000-kubernetes-clusters-without-missing-a-beat/). You could, for example, run four additional workers in each location and use those to provide a decent amount of capacity for KubeVirt to use for VM applications.

**The Storage Conundrum**
The real challenge is storage. If you’re using an external storage array, you would need either:

- Some sort of stretched array across both rooms/locations, or;
- Two arrays with replication implemented in such a transparent way that the container storage interface (CSI) is able to attach the same PersistentVolumeClaim (PVC) on the other side using the other array.
Dell, for example, has a Metro feature for its PowerMax and PowerStore arrays, which can [transparently mount the same volume from two linked arrays](https://dell.github.io/csm-docs/docs/replication/high-availability/powerstore-metro/) that are kept in sync on the backend. If you have such arrays, great! It can definitely make things more straightforward.

But let’s say that’s not an option and you need a more software-based approach to storage that will still work for this two-site environment. Let’s see what the options are.

Several software-defined Kubernetes storage solutions require a majority quorum to function:

Since we can’t recover from a 50% node loss with quorum-based products, these all are out of the running.

**Can I Get a Witness?**
In the case of Portworx, you do have the option to deploy a [witness VM](https://docs.portworx.com/portworx-enterprise/operations/operate-kubernetes/disaster-recovery/px-metro/witness-node-setup) in a third location to provide quorum participation.

However, the witness requires an external etcd cluster; you can’t use it with the internal key-value database (KVDB) option in Portworx. That would mean running the etcd cluster for Portworx in the third location as well, which adds a dependency on the WAN connection for the storage cluster to remain operational. It also requires a slightly modified installation to operate in non-MetroDR mode.

While we have tested Portworx with a witness VM (and it does work), the additional complexity of requiring both a self-managed external etcd cluster and a witness VM in a third location is probably too much for most users when it’s for near-edge or smaller campus deployments.

**Keeping It Simple With Longhorn and Piraeus**
Not all solutions require a majority quorum. Both [Longhorn ](https://longhorn.io/)and [Piraeus ](https://piraeus.io/)can replicate volumes to other nodes in the cluster and keep the surviving half of the storage cluster online when an outage takes out half the infrastructure.

Using the `topology.kubernetes.io/zone`
label, we can ensure the replica is kept in the other room so all VMs can be run in the surviving room.

Longhorn’s capability is based on the [2021 feature addition](https://github.com/longhorn/longhorn/blob/master/enhancements/20210216-volume-live-migration.md) to support live migration with block-mode PVCs. When setting the `migratable: "true"`
parameter for the Longhorn storageclass, you can create ReadWriteMany (RWX) volumes of the block volume mode that are suitable for KubeVirt and support live migration.

Performance of the volume also is quite a bit better compared to a regular filesystem-mode PVC in Longhorn, which is sorely needed to provide acceptable performance for KubeVirt VMs. However, some people in the community have had mixed results with Longhorn, and it’s generally recommended to stay away from using RWX volumes with it.

So we should take a closer look at the final option: Piraeus. This project is the free and open source version of [Linstor](https://linbit.com/), a distributed replicated block device (DRBD)-based technology that is both decently simple and decently performant. Similar to Longhorn, it supports RWX block volumes and KubeVirt live migration.

**Let’s Try Piraeus in the Two-Site Model**
**Defining the Stack**
Curious to see if it would work well, I made a CSI [pack ](https://www.spectrocloud.com/blog/take-the-pain-out-of-deploying-k8s-helm-charts)for Piraeus, put it in a Palette Cluster profile and deployed a four-node KubeVirt cluster with it:

This cluster has a two-node HA control plane and a single KubeVirt worker node for each room:

**Ensuring Separation With Zones and Taints**
The control plane nodes are very small and don’t participate in the KubeVirt cluster, which means that the secondary storage replica always goes from one worker node to the other. If we had multiple workers per room, though (or bigger control plane nodes that could participate in the storage cluster), we could configure Piraeus to ensure the second replica always lives in the other room:

123456789 |
apiVersion: piraeus.io/v1kind: LinstorNodeConnectionmetadata: name: selectorspec: selector: - matchLabels: - key: topology.kubernetes.io/zone op: NotSame |
From Palette we can control the labels and taints for each node pool so we use that to set unique zone labels for each worker pool:
![](https://cdn.thenewstack.io/media/2025/01/6208416c-image5a-300x148.png)
Image 1

![](https://cdn.thenewstack.io/media/2025/01/5773239b-image6a-300x146.png)
Image 2

This way, even if we have multiple workers in each room, they will never store both copies of the storage replica in the same room.

From there we can deploy virtual machines and be assured that if one server room goes down, the virtual machines in the other room keep running while the crashed virtual machines from the failed server room get restarted on the surviving side.

**Accelerating Failover With MediK8s**
When a Kubernetes node goes offline suddenly, the pods that were running on it can go into a perpetual Terminating state, as Kubernetes isn’t sure what to do with the workloads on the offline node (more info [here](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#non-graceful-node-shutdown)). This is problematic for both statefulsets and KubeVirt VMs, as we want those VMs to be restarted on surviving nodes as quickly as possible.

To speed up failover times, we turn to [Medik8s](https://www.medik8s.io/), which you’ll see in the screenshot of the cluster profile above. Medik8s provides automation logic to monitor node health and apply the `node.kubernetes.io/out-of-service`
taint to nodes that went offline, which causes Kubernetes to clear out the pods in the Terminating state from that node. The scheduler can then immediately reschedule the workloads on other nodes in the cluster.

**Putting the Two-Room Architecture Into Practice**
Once we have deployed the stack of the two-node HA kind store, Piraeus storage, KubeVirt and Medik8s across our cluster, we can test the HA capability.

After powering off half the nodes of our two-room cluster, within three minutes the VMs on the surviving side will be restarted.

Similar to VMware HA, your traditional virtualized application workloads can be back online in mere minutes after a site outage. And if your application requires near-zero downtime, you already have the Kubernetes infrastructure available to transition to a cloud native architecture that is more capable for active/active designs.

The end result? If you’re looking for high availability within a factory, hospital or other self-contained campus location, there is a viable cloud native alternative to the licensing costs of vSphere and vSAN.

If you’d like to learn more about this technology and get a sneak preview before it hits a forthcoming release of Palette, [don’t hesitate to reach out to us](https://www.spectrocloud.com/get-started).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)