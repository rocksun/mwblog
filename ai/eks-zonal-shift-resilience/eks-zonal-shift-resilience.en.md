Handling the obvious failures is the easy part: a server goes down, you spin up another. The failures that actually take out entire regions are the ones that aren’t obvious. A zone that’s slow but not dead, dropping some traffic but still passing health checks. An AWS Region spreads infrastructure across multiple Availability Zones with independent power, cooling, and networking, so if one zone experiences a power event, a network partition, or a cooling failure, your application keeps serving from the others. What makes this difficult in practice is that zones rarely fail by disappearing cleanly. In that gray space, the default behavior of most automated systems, to detect unhealthy and replace it, is the behavior that converts a single-zone problem into a regional outage.

We learned this by building zonal resiliency into Amazon EKS over years of engineering, refined through real production incidents. The system we built as a result protects every EKS cluster today. This post covers what we built into the Kubernetes control plane that EKS operates for every cluster, what we exposed in the data plane where your workloads run, and the principles that connect them. The single most important of those principles is static stability: during a zonal impairment, the most valuable thing a system can do is stop reacting, preserve existing capacity, route around the bad zone, and wait.

## Why a control plane needs zonal resiliency

[The EKS control plane](https://thenewstack.io/eks-kubernetes-etcd-scale/) consists of the API server (the endpoint your kubectl and controllers talk to) and the etcd datastore that holds the full state of your cluster. For resilience, these components are spread across multiple Availability Zones. If one zone becomes unreachable, the surviving instances in other zones continue serving. On paper, this works. The reason zonal resiliency required years of engineering rather than a diagram is what happens in the gray period before a zone is cleanly down.

## When zones fail in gray

The most [common failure mode](https://thenewstack.io/how-to-get-dns-right-a-guide-to-common-failure-modes/) in our early years involved health checks and Auto Scaling. The control plane instances sit behind a network load balancer, and an Auto Scaling group monitors their health. The health check logic is reasonable in isolation: If an instance fails checks several times over thirty seconds, mark it unhealthy and replace it.

> “The single most important of those principles is static stability: during a zonal impairment, the most valuable thing a system can do is stop reacting, preserve existing capacity, route around the bad zone, and wait.”

For a single sick host on an ordinary day, this is correct. During a zonal network impairment, it cascades. A brief partition causes the API servers in the affected zone to fail health checks because the network in front of them is impaired, not because the servers themselves are broken. The scaling group terminates them. It then attempts to launch replacements in the same impaired zone where provisioning is also failing, and when those launches fail, it backs off for up to thirty minutes.

The load balancer’s health check depends in part on whether the API server can reach etcd, so a network blip between zones can mark healthy instances as failed. The net effect: a thirty-second network blip could trigger terminations across a large fraction of the fleet, discard warm caches, add load to already-struggling dependencies, and then refuse to recover for thirty minutes after the underlying event resolved.

## Automated zonal shift for the control plane

![Architecture diagram showing the Kubernetes control plane zonal shift, where a monitoring system detects an unhealthy zone and triggers actions to stop new launches, reroute traffic, and block control-plane leases in the impaired availability zone.](https://cdn.thenewstack.io/media/2026/07/da188198-image2-1024x626.png)

We built an automated weight-shift mechanism that moves control plane activity out of an impaired zone within approximately two minutes. The shift fires in parallel against multiple systems.

* **At the DNS layer**, for clusters reachable over a public endpoint, the control plane sits behind a load balancer whose addresses are distributed via DNS with per-zone health checks. Shifting fails the health check for the impaired zone, DNS stops serving that zone’s records, and new connections land on healthy zones.
* **At the scaling group layer**, the group is instructed to stop responding to health-check failures in the impaired zone, thereby ending the termination cascade.
* **At the Kubernetes layer**, EKS runs leader-elected controllers (the scheduler, the controller manager, the Fargate scheduler, and the certificate controller), with only one instance active at a time.

Shifting forces any controller whose leader resides in the impaired zone to hand leadership to a healthy zone. Additionally, an API server in an impaired zone stops advertising its IP address, ensuring pods route requests to healthy API servers in other zones. The cluster continues to schedule and reconcile using infrastructure that works.

## Healthy zones do the work

The design principle underneath this mechanism is one we arrived at through first principles and then reinforced by incidents: corrective action must be taken by the healthy zones, never by the impaired one. It is tempting to build the logic, so the instance in the troubled zone notices its own trouble and steps aside.

An instance in an impaired zone is, by definition, the component you can least rely on to do anything correctly, including removing itself. So the mechanism is built so that survivors fence off the bad zone, with a deliberate fail-safe default.

## Cross-zone dependencies hiding inside a zonal failure

A failure scoped to one zone can still damage healthy zones through dependencies you did not realize crossed zone boundaries. We discovered this through etcd. The API servers maintain client connections to etcd instances, and etcd automatically syncs the cluster’s membership list with its clients.

> “An instance in an impaired zone is, by definition, the component you can least rely on to do anything correctly, including removing itself.”

During certain failures, a client in a healthy zone could pick up a stale membership entry pointing at an isolated etcd instance in the bad zone, attempt to use it, and fail its own health checks. A problem physically confined to one zone produced API server failures in the others.

The general lesson we took from this is that “zonal” describes the failure’s location, not automatically its blast radius. The gap between those two is where the worst surprises live, and auditing cross-zone dependency paths became a permanent part of how we evaluate new control plane components.

## The data plane: zonal shift for your workloads

The control plane work described above protects the infrastructure that EKS operates, but your application runs in the data plane on your worker nodes and in your pods, and a zonal event can hit that layer too. The worker nodes in an impaired zone may be unreachable, and traffic needs to move off them. The same principles apply, but here the decision authority is yours, because only you know your application’s capacity, its topology, and how much risk it can tolerate.

![Architecture diagram showing AWS Kubernetes dataplane zonal shift, where an operator triggers a zonal shift to reroute traffic away from an unhealthy availability zone toward healthy zones.](https://cdn.thenewstack.io/media/2026/07/54418cbb-image1-1024x832.png)

ARC zonal shift for Amazon EKS gives you that authority, built on the same Availability Zone-shifting primitive that other AWS services use via Amazon Application Recovery Controller. Once enabled on a cluster, you (or AWS on your behalf) can declare that workloads should move away from a specific zone, and EKS reshapes in-cluster networking to stop using that zone without spinning up additional capacity or discarding existing capacity.

When a shift is active, EKS cordons every node in the impaired zone, preventing the Kubernetes scheduler from placing new pods there. For managed node groups, it suspends Auto Scaling group AZ rebalancing and constrains the group to launch new nodes only in healthy zones. The EndpointSlice controller removes the impaired zone’s pod endpoints from your services’ EndpointSlices, so east-west traffic between pods and ingress through an ALB or NLB targets only pods in healthy zones.

Critically, it neither terminates nodes nor evicts pods in the impaired zone. Leaving them in place means that the moment the zone recovers or you cancel the shift, your capacity returns immediately with no cold-start scramble.

## Don’t evict, preserve capacity

The decision not to evict was based on [observing what happens in large clusters](https://thenewstack.io/kubernetes-auditing-and-events-monitoring-cluster-activity/) without this protection. When a zone becomes unhealthy and all its nodes become NotReady, the node lifecycle controller evicts all pods so they can be rescheduled elsewhere. On small and medium clusters, this works fine.

On large clusters, evicting that many pods at once drives a surge of capacity requests to other zones, eventually resulting in Insufficient Capacity errors. When the impaired zone recovers, workloads remain spread unevenly and stay that way until they are rolled again. With zonal shift enabled, we suppress those evictions, keeping applications from migrating across zones during the event. The tradeoff is that this depends on the cluster being prescaled to ride out a zonal failure, which is the same assumption underlying the rest of our zonal resilience design.

## What the incidents taught us

Our first principle is that a zonal shift must be fault-tolerant and safe to run at any point. We provision instances in the other zones so the healthy zones can absorb a full zone’s worth of traffic without disruption. To exercise this, we do not stop at pre-prod and smaller regions. We run the test at regular cadence in our largest regions (like IAD) to make sure the principle holds where it matters most. The largest regions, where our scale is most likely to break, are exactly where we would otherwise learn about gaps on the day of a real event.

Our second principle is that the system that detects a zonal failure and executes the shift must rely on core primitives rather than higher-order services. Higher-order services bring their own dependencies and their own zonal failure modes.

They tend to be unavailable when we need them most. We built our detection and shift path on the lowest-level building blocks available: state and signals between the detector and executors flow through S3, the components run on plain EC2 rather than managed services layered above it, and the whole system runs across all three zones. It depends on less onthan the workloads it protects, which is what lets it keep working when a zone does not.

We also learned that running zonal isolation tests through a managed service like AWS FIS is far simpler and more realistic than manipulating iptables and eBPF rules on each host. Host-level rules only exercise the path we thought to block, and they do not reproduce a zone genuinely going away. With FIS, we inject real packet loss and zonal isolation across the cluster, the way an actual event would. This surfaced problems our hand-rolled simulations never did, including a dependency-throttling bug on a control-plane call that would have blocked recovery during an outage.

The same approach is available to anyone running EKS: FIS can isolate an Availability Zone from the worker nodes and pods in that zone, allowing a team to confirm that their workloads ride through a zonal failure rather than assuming they will.

## How to turn it on

ARC zonal shift and zonal autoshift are available in Amazon EKS at no additional charge (you pay only for the instances you run), and they act only on the Kubernetes data plane; the EKS-managed control plane is already spread across zones and keeps running regardless. Enabling the capability is a single-cluster setting.

```

aws eks update-cluster-config --name my-cluster --zonal-shift-config enabled=true

```

You can also enable it at cluster creation, or through the console, eksctl, AWS CloudFormation, or Terraform, with no recreation or downtime. Once enabled, your cluster appears as a managed resource in ARC with two modes of operation. To respond to an impairment yourself, start a zonal shift from the ARC console, the AWS CLI, or the zonal shift API, specifying the zone and an expiry.

Shifts are temporary by design, and you can extend or cancel them. To hand the decision to AWS, enable zonal autoshift on the resource. AWS then monitors AZ health, automatically shifts when it detects an impairment, and ends the shift when the zone recovers. Autoshift also provides scheduled practice runs (roughly weekly) that shift you out of a zone under controlled conditions, so you can discover whether your cluster can handle the loss before a real event forces that discovery.

The feature only helps if your cluster is built to handle losing a zone, and that’s on you. Spread worker nodes across multiple AZs and run multiple replicas of each workload with topology-spread constraints, including CoreDNS, so service discovery survives the loss of a zone. Pre-scale and over-provision so the healthy zones can absorb the load of the one that left.

A shift moves traffic in seconds, but launching new nodes does not, and during a real impairment, the capacity you need may be contended for. Colocate interdependent pods in the same zone, with pod affinity, so that a single zonal loss does not sever a multi-service request path.

> “During a correlated failure, the most valuable thing an automated system can do is hold still.”

As a safety net, if a workload has all its endpoints in the impaired zone, EKS will keep sending traffic there rather than blackholing it, but that is a fallback, not a plan.

The customer-facing surface of all this work is meant to be uneventful: during a zonal event, your traffic moves to healthy zones, your control plane keeps answering, and your capacity is preserved rather than churned. If you have opted into autoshift, it happens without a page. That quiet is the goal, and it results from a single discipline: during a correlated failure, the most valuable thing an automated system can do is hold still.

What stays with you as an EKS operator is small and worth your attention. Spread your workloads across zones, provision so the survivors can carry the full load, and test that your application actually rides through a zone short. Get those right, and a zone going down becomes something you read about afterward rather than something you spend the night debugging. To learn more about and enable zonal shift, see our [AWS docs](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/07/11a79ba8-cropped-e91b5d34-raghavtripathi-scaled-1-600x600.png)

Raghav Tripathi is an Engineering Leader at Amazon Web Services, where he heads the engineering organization behind Amazon EKS, overseeing infrastructure that powers hundreds of thousands of Kubernetes clusters and millions of nodes. A founding engineer of Amazon EKS, he...

Read more from Raghav Tripathi](https://thenewstack.io/author/raghav-tripathi/)

[![](https://thenewstack.io/wp-content/uploads/2026/06/7f8a61d7-srisaranbalaji-600x600.png)

Sri Saran Balaji Vellore Rajakumar is a Principal Engineer at Amazon Web Services and a founding engineer of Amazon EKS, where he has spent nearly a decade building the infrastructure that keeps the EKS control plane available and performant at...

Read more from Sri Saran Balaji Vellore Rajakumar](https://thenewstack.io/author/sri-saran-balaji-vellore-rajakumar/)