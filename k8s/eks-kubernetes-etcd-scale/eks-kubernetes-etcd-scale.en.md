Amazon EKS runs hundreds of thousands of Kubernetes clusters across more than thirty AWS regions. Operating at that scale has taught us something that has shaped how we build the service and that we think is useful to anyone running Kubernetes at scale: most availability problems do not stem from a component failing. They come from a component reacting to a problem in a way that makes it worse. A cache that goes stale and serves wrong answers. A health check that restarts the very process keeping a cluster alive.

What separates a resilient control plane from a fragile one is not the number of faults. It is whether a fault stays a fault or becomes an outage. This post is the story of how we keep the EKS-managed Kubernetes control plane on the right side of that line at ever-growing scale: the foundational changes we made and why, and what operating at fleet scale taught us about building systems that tolerate faults rather than spreading them. These are the reasons our most demanding customers confidently run their mission-critical workloads on EKS.

## How AI and analytics workloads reshaped what “scale” means

Kubernetes was built for a particular rhythm of work. Pods came and went at predictable rates, and controllers had seconds or minutes to reconcile. The system’s design reflected that pace: strong data consistency, ordered watches, and consensus-replicated storage that puts correctness first. It worked beautifully for what it was designed to do, and it still does.

> “What separates a resilient control plane from a fragile one is not the number of faults. It is whether a fault stays a fault or becomes an outage.”

But the [workloads evolved faster](https://thenewstack.io/why-ai-workloads-are-fueling-a-move-back-to-postgres/) than anyone anticipated. Foundation model training runs scale-up training jobs on thousands of GPU nodes in minutes. Real-time inference services scale from a warm baseline to thousands of replicas, then drop back within the hour. Apache Spark analytics pipelines burst from zero to tens of thousands of executor pods, chew through a dataset, and vanish.

Emerging agentic AI workloads add yet another dimension: autonomous agents that spin up, fan out, execute tasks, and tear down in seconds or less. These workloads share a trait that distinguishes them from traditional microservices: they generate enormous volumes of state transitions within compressed time windows and are deeply intolerant of delays. This velocity of state change pushed us to reinvent some of the mechanics to support a scale that was previously impossible, and to contribute what we could upstream.

## How EKS reimagined Kubernetes storage foundation

Every Kubernetes cluster depends on etcd as its source of truth. Every application, every service endpoint, every scheduling decision is stored there. If etcd loses data, the cluster forgets everything it knows. Protecting that state is the most important job for a managed Kubernetes service.

Operating etcd for one cluster is well understood. Operating it for a fleet of millions is a different problem entirely. Hardware fails, networks blip, and disks degrade, so something has to handle those events without a human in the loop. And the operations etcd needs most, like replacing a failed member or recovering after a zonal event, are exactly the ones where a person acting under pressure can make a mistake that causes permanent data loss.

From the beginning, we built an operator agent that runs alongside every etcd instance and automates its entire lifecycle. The agent has two jobs. First, backup and recovery: it takes point-in-time snapshots and stores them durably outside the cluster. If too many instances are lost at once and the survivors cannot form a majority, the agent automatically detects the condition and rebuilds from the latest snapshot. Second, membership management: when an instance fails, the agent removes the terminated member and adds its replacement in an order that protects quorum and prevents split-brain.

A recent, more fundamental change was replacing etcd’s consensus mechanism, Raft, with a purpose-built journal that provides durable, ordered storage independently of etcd. In traditional etcd, a majority of members must agree on every write before it is committed. If two of three are unhealthy, the cluster becomes unavailable.

By offloading durability to the journal, etcd peers no longer negotiate quorum among themselves. Writes commit as soon as the journal acknowledges persistence, and that entire class of etcd quorum-loss failures disappeared. Since the journal handles persistence, etcd no longer needs to fsync writes to local disk, so its data store has moved to an in-memory filesystem. What was a disk-bound system became a compute-bound one, and storage latency was removed entirely from the critical path. For a deeper look at this architecture, read “[Under the hood: Amazon EKS ultra scale clusters](https://aws.amazon.com/blogs/containers/under-the-hood-amazon-eks-ultra-scale-clusters/).”

> “What was a disk-bound system became a compute-bound one, and storage latency was removed entirely from the critical path.”

For ultra-scale clusters, we went further and partitioned etcd into resource-specific shards. Each partition operates independently with its own storage budget and throughput capacity. The primary value is failure isolation. In a monolithic deployment, if the events keyspace exceeds its quota because a misbehaving controller creates objects faster than garbage collection can remove them, it blocks writes to everything, including node leases.

Suddenly, healthy nodes appear unhealthy because their lease renewals are being rejected. With partitioned etcd, the events partition hits its quota, but the leases partition continues operating normally. Nodes remain healthy. The scheduler keeps running.

## What replacing etcd’s consensus mechanism unlocked

Removing the quorum requirement allowed us to make a change we had wanted for a long time: running etcd on the same host as the API server. In the traditional layout, every read and write crosses the network between separate machines. Each trip is fast on its own, but at thousands per second, the travel time adds up. With collocation, the API server talks to its local etcd over a loopback interface, and pod scheduling and controller reconciliation get measurably faster. For workloads where job controller queue depth is the binding constraint, shaving milliseconds off each API call means many more jobs are processed per second before the queue starts growing.

![Diagram showing the evolution of EKS Kubernetes architecture](https://cdn.thenewstack.io/media/2026/06/0ebb7b12-image2-1024x779.png)

This is where the operator agent paid off. When etcd runs on the same host, an etcd member comes and goes whenever a control-plane host is replaced, which happens routinely. That only works if membership management is completely safe and automatic, which is exactly what the agent was already doing. We did not have to build a colocation from scratch; we built it on top of infrastructure that had been managing etcd membership safely since day one.

Collocation also taught us a lesson worth passing on: the convenient path needs a failover in case it breaks. The local etcd is the fast path, but if it becomes impaired, the API server fails over to another etcd member that is actively serving other API servers from the same journal. When you optimize for the common case, design just as deliberately for the moment that optimization is not available.

## Fixing bottlenecks across the stack

At extreme scale, you have to address [bottlenecks across the entire Kubernetes stack](https://thenewstack.io/ai-workloads-kubernetes-infrastructure-drift/), and most of them are not bugs in the traditional sense. They are design choices that were correct at the scale Kubernetes originally targeted and break down only when the numbers get large. Rather than working around them internally, we fix them upstream so the entire community benefits.

One example involved the watch cache, the in-memory layer that distributes state changes from etcd to every controller watching for updates. When a controller starts, it requests a full snapshot of the current state via a mechanism called WatchList, and the existing implementation holds a shared read lock for the duration of the response build.

At hundreds of thousands of objects, that work runs long enough to starve the writer that needs exclusive access, so the cache’s resource version cannot advance. Consistent reads see a stale cache and fail over to etcd, while the response building churns through hundreds of thousands of allocations under the lock. We identified this as a limitation in the watch-cache’s locking model and are working with the community to refactor the underlying data structures and interfaces to eliminate the contention.

The same shape appears elsewhere. In the Horizontal Pod Autoscaler, a single mutex protecting the scaling state becomes a serialization point at high HPA counts, where workers spend nearly all their time blocked rather than doing useful work. A redesigned data store (PR #[139142](https://github.com/kubernetes/kubernetes/pull/139142)) restores parallelism and raises reconciliation throughput by orders of magnitude. In the scheduler, we identified a bottleneck (issue #[138426](https://github.com/kubernetes/kubernetes/issues/138426)): every scheduling cycle rebuilds a set of in-use persistent volumes by scanning every node in the cluster, even for pods that do not use storage at all. The fix computes that information lazily, and only for pods that actually need it, restoring throughput at scale.

Each of these started from a real production workload hitting a cliff, and we are working on the fixes upstream so the improvements reach every Kubernetes user.

## From engineering to guarantees: EKS Provisioned Control Plane

The engineering described above made the EKS control plane more resilient and performant. But customers had a different problem: they could observe that the control plane kept up today, but they could not reserve its capacity the way they reserve compute or GPU capacity.

A team planning a thousand-node training run could secure the instances weeks in advance, yet had no equivalent mechanism for the orchestration layer that would coordinate them. [EKS Provisioned Control Plane](https://docs.aws.amazon.com/eks/latest/userguide/eks-provisioned-control-plane.html) fills that gap. It exposes the control plane’s performance as dimensions you size explicitly, backed by the same kind of commitment you expect from the rest of your infrastructure.

You choose a scaling tier that maps to concrete, measurable capabilities: API request concurrency, pod scheduling rate, and cluster database size. The tiers range from XL through 8XL. At the top end, 8XL on Kubernetes 1.34 provides 16,000 concurrent API request seats, 400 pods-per-second scheduling rate, and 16 GB of cluster database storage, all backed by a 99.99% availability SLA measured in one-minute intervals.

Tiers are not static. You step up before a GPU training run or a large sales event, step back down during quiet periods, or grow permanently as your platform matures. Configuration happens through the console, CLI, eksctl, CloudFormation, or Terraform on any cluster, without recreation or downtime.

For AI workloads, orchestration capacity is planned alongside GPU capacity, available when the compute comes online. For analytics platforms submitting hundreds of jobs per minute, the control plane is ready for the burst before it arrives. And for organizations that need environmental consistency across staging, production, and disaster recovery, the same tier guarantees consistent performance characteristics everywhere.

## Taking the same foundation to the edge

![Architectural diagram of Amazon EKS on AWS Outposts](https://cdn.thenewstack.io/media/2026/06/b641c1d2-image1-1024x753.png)

Some workloads cannot move to the cloud, whether due to data sovereignty requirements, latency constraints, or unreliable connectivity to the Region. Running Kubernetes in these disconnected environments introduces unique challenges: etcd must remain durable on hardware with only a few machines, the cluster must self-heal without reaching the cloud, and observability must survive network partitions that last days.

With the updated architecture for EKS local clusters on instance store Outposts, we brought edge clusters onto the same management plane and software stack as EKS clusters in the cloud.

The control plane lives in an EKS-managed account on the Outpost rather than in the customer’s account, so customers never manage control plane instances, etcd backups, or logging agents themselves, and they cannot accidentally break the thing keeping their cluster alive. The same machine images, container images, and operator agent run in both places, with edge-specific behaviors selected by configuration.

Because it is the same stack, new Kubernetes and EKS platform versions arrive in lockstep with their cloud release, and features like EKS add-ons, Pod Identity, and access entries work the same way they do in a Region.

The hardest part was keeping etcd healthy on hardware with only a few machines that may be cut off from the cloud for days at a time. We solved it by extending the same agent. It keeps a spare copy of the data continuously up to date and promotes it the instant a machine fails, so the cluster heals itself with no human involvement and no connection to the cloud.

[Observability](https://thenewstack.io/taking-your-observability-strategy-to-the-next-level/) survives the disconnect, too: the metrics agent continues collecting and writing to local disk, shedding the least critical data first when space runs short, so the signals that matter most are the last to go. When the link returns, the buffered data is flushed back with its original timestamps.

All of this only works because the system was designed from the start to operate without anyone logged in. That same design is what makes it possible to deploy changes safely across the entire fleet.

## Operating safely at fleet scale

Every one of these changes was deployed to a running fleet of hundreds of thousands of clusters. The journal migration and collocation required transitioning each cluster individually. Every migration follows a strict sequence: validate pre-conditions, create a point-in-time snapshot, perform the switchover, validate post-conditions. If any step fails, the system rolls back automatically.

Rollouts proceed cell by cell, zone by zone, region by region, with automated monitoring comparing latency, error rates, and throughput between updated and non-updated clusters. Any statistically significant deviation triggers an automatic halt.

What made all of this possible is that EKS is built to operate without human intervention at the individual cluster level. Through Zero Operator Access, the architecture prevents AWS personnel from having technical pathways to access customer content in the managed control plane. A system designed to work without human access must be observable, recoverable, and automatable from the start, and that same discipline is what enables operating at extreme scale.

Three operational lessons shaped how we approach this work.

The first is that a healthy leader is not the same as a working one. The control plane’s controllers run in an active-passive configuration, and early on, we treated an unhealthy standby as if cluster operations had halted. They had not; what matters is whether a leader exists. But the harder lesson: a leader can quietly stop making progress while still renewing its lease and passing every health check. The signal that caught this was watching the controller’s work queue depth. If the queue fills while the leader looks healthy, the system is falling behind in ways no liveness probe will catch.

> “A leader can quietly stop making progress while still renewing its lease and passing every health check. The signal that caught this was watching the controller’s work queue depth.”

The second is that maintenance ordering matters as much as the maintenance itself. etcd defragmentation is blocking, and the pause grows with database size. When it hit the leader, every write stalled. We taught the agent to move leadership to a healthy node before defragmenting, so the disruptive work always lands on a follower while writes keep flowing.

The third is that liveness is not readiness. A process can be alive but not ready while it warms caches, and routing based solely on liveness sends requests to an instance that cannot handle them. Equally, readiness flapping during graceful draining should never trigger a restart. We keep the two signals strictly separate: one decides recovery; the other decides routing.

None of this work is visible from the outside, and that is the point. The largest clusters taught us lessons that made every cluster faster. The riskiest migrations produced safety machinery that protects every upgrade. The upstream fixes we contributed for workloads at the edge of what Kubernetes can handle flow back to every user of the project.

> “None of this work is visible from the outside, and that is the point.”

When you deploy on EKS and your pods come up in seconds, even during a burst, even when something behind the scenes goes wrong, that speed is not accidental. It is the accumulated result of years of operating at scales where small problems can become big ones fast, and engineering the system to contain them before they do.

To explore the architectures referenced in this post, see [EKS Provisioned Control Plane](https://docs.aws.amazon.com/eks/latest/userguide/eks-provisioned-control-plane.html) and [local Amazon EKS clusters on AWS Outposts](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-local-cluster-overview.html).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/404962af-cropped-1d0a0b80-neelendra_bhandari-600x600.png)

Neelendra Bhandari is a Senior Software Development Manager at Amazon Web Services, where he leads teams building the Amazon EKS Kubernetes Control Plane. His work spans Kubernetes scalability, etcd reliability, and the systems that power EKS features like Provisioned Control...

Read more from Neelendra Bhandari](https://thenewstack.io/author/neelendra-bhandari/)

[![](https://thenewstack.io/wp-content/uploads/2026/06/7f8a61d7-srisaranbalaji-600x600.png)

Sri Saran Balaji Vellore Rajakumar is a Principal Engineer at Amazon Web Services and a founding engineer of Amazon EKS, where he has spent nearly a decade building the infrastructure that keeps the EKS control plane available and performant at...

Read more from Sri Saran Balaji Vellore Rajakumar](https://thenewstack.io/author/sri-saran-balaji-vellore-rajakumar/)