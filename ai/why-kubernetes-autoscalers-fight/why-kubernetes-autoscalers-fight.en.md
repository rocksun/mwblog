**Ask an SRE** a deceptively simple question: *What is the right size for* *`checkout-api`, and how many replicas should it run right now?*

Their Helm values specify `replicas: 3, cpu: 1000m`, and `memory: 2Gi`. But the live cluster tells a different story: HPA has scaled the app to 11 replicas on CPU load; VPA insists it is over-provisioned, recommending `cpu: 350m` and `memory: 3.1Gi`; KEDA demands 24 replicas due to an upstream Kafka lag spike; and Karpenter has provisioned two new nodes, sizing physical capacity strictly against declared requests rather than actual usage.

> “Five sources yield five contradictory answers. Each controller acts logically in isolation, but none sees the complete picture.”

Five sources yield five contradictory answers. Each controller acts logically in isolation, but none sees the complete picture. This gap between isolated observations and actual workload needs represents a core architectural failure in modern Kubernetes operations.

## The breakdown of the Unix philosophy in elastic systems

Kubernetes and its components were built on the Unix philosophy: *build small, modular tools that do one thing well.* For container orchestration, this principle seemed intuitive:

* **HPA** handles horizontal elasticity based on runtime resource utilization.
* **VPA** handles vertical container sizing based on historical consumption.
* **KEDA** bridges event sources to replica counts based on external queue lag.
* **Karpenter and Cluster Autoscaler manage** node capacity when pods are Pending.
* **GitOps (Argo CD / Flux)** [enforces baseline cluster state](https://thenewstack.io/make-your-kubernetes-apps-self-heal-with-argo-cd-and-gitops/) from version control.

In standard Unix environments, tools like grep and awk compose cleanly because they process immutable streams of text sequentially. One tool finishes and hands its output to the next.

Autoscaling controllers do not operate sequentially. They execute concurrently, acting on the same target workload and mutating the same API fields: `.spec.replicas, .resources.requests`, and the underlying node pool. Each runs in an [independent reconciliation loop](https://thenewstack.io/ai-agents-kubernetes-control/), assuming exclusive control over workload sizing without visibility into adjacent tools.

> “Determining workload capacity is a single, coupled mathematical equation. Splitting it across decoupled controllers creates thrashing instead of modular efficiency.”

Determining workload capacity is a single, coupled mathematical equation. Splitting it across decoupled controllers creates thrashing instead of modular efficiency.

## The four collisions: how autoscalers fight

When independent control loops manipulate interdependent variables, feedback loops destabilize into four common failure modes.

### 1. The denominator collapse: HPA vs. VPA

HPA calculates target replicas using pod CPU utilization as a percentage of declared requests:

`current metric = total actual usage / total declared requests`

Declared resource requests serve as the denominator. When VPA operates concurrently, it lowers CPU requests to eliminate waste. This shrinks the denominator. A minor traffic increase now pushes percentage utilization past HPA’s threshold, triggering an aggressive horizontal scale-out. As more pods split the traffic, per-pod usage drops, prompting VPA to shrink requests even further. The workload enters a death spiral: VPA continuously shrinks pod size while HPA creates an unmanageable fleet of microscopic containers.

### 2. Multi-writer race condition: native HPA vs. KEDA

When teams combine queue-based scaling via KEDA with standard CPU-based HPA, two controllers target the same deployment’s `/scale` sub-resource. If an event queue spikes, KEDA scales the deployment up to drain the backlog. However, if those worker pods are I/O-heavy with low CPU usage, the standalone HPA evaluates the low utilization, concludes the app is over-provisioned, and scales it back down. The API server records alternating rescale events while actual processing throughput stalls.

### 3. GitOps drift ping-pong: declarative IaC vs. dynamic runtime

GitOps engines enforce Git repositories as the source of truth. When HPA scales a deployment during a traffic spike, Argo CD flags the application as `OutOfSync`. If auto-sync is enabled, GitOps resets the live deployment back to its baseline, starving the application of capacity during peak demand. While engineers often configure GitOps to ignore replica differences, this breaks declarative infrastructure: Git no longer reflects production reality, and future rollouts risk quietly restoring outdated baselines.

### 4. The multiplier effect at the node layer

[Node autoscalers like Karpenter](https://thenewstack.io/how-amazon-eks-auto-mode-simplifies-kubernetes-cluster-management-part-1/) make placement decisions based strictly on declared container *requests*, not actual consumption. If a container requests `1000m` CPU but consumes only 150m, the scheduler still reserves the entire core. Karpenter provisions physical instances to satisfy phantom demand, multiplying upstream sizing inefficiencies into massive cloud bills. Across production fleets, average cluster CPU utilization hovers around 8% despite heavy node provisioning.

## The path to a better autoscaler

Every traditional autoscaler answers a narrow question: *“What should my individual setting be?”* But the real operational requirement is broader: *What combination of replicas, resource requests, limits, and scaling thresholds satisfies latency SLOs at the lowest cost, and when should that configuration change?*

Horizontal and vertical sizing are interlinked variables of a single optimization problem. A true autoscaler cannot rely on reactive, single-metric heuristics. It must function as a unified control plane defined by five core capabilities:

1. **Unified signal ingestion: Evaluating** CPU/memory metrics, queue depth, transaction rates, latency SLO compliance, node pricing, and IaC manifests simultaneously.
2. **Joint decision-making: Computing** a single action vector that defines horizontal limits and vertical resource requests in tandem, rather than delegating replicas to one tool and pod sizing to another.
3. **Continuous GitOps synchronization: Submitting** automated, reasoned pull requests against application repositories instead of forcing GitOps engines to ignore live cluster state, keeping version control aligned with real-world needs.
4. **Predictive and proactive capacity planning: Reactive** scaling is inherently flawed because initializing new compute resources takes time. Traditional reactive controllers wait for load to breach arbitrary thresholds, causing latency spikes during sudden demand surges. A true autoscaler incorporates predictive algorithms to analyze historical consumption, detect daily or weekly seasonality, and forecast workload demand. It pre-warms application capacity and resizes resources *before* traffic arrives, transforming scaling from a panicked reflex into a smooth, scheduled operation.
5. **Explainable auditing: Providing** clear operational rationale for every adjustment, giving SREs full transparency into trade-offs between cost savings, predicted demand, and latency boundaries.

## From reactive reflexes to true autonomy

The cloud-native ecosystem routinely conflates “*automated”* and “*autonomous*.”

Today’s autoscalers are *automated*: they act like biological reflexes, measure an isolated telemetry signal, and fire a predefined response. When an event occurs, HPA triggers, KEDA scales, or Karpenter provisions. But reflexes lack a central nervous system. When five independent reflexes fire simultaneously on the same limb, the system thrashes.

> “Today’s autoscalers are automated: they act like biological reflexes. But reflexes lack a central nervous system. When five independent reflexes fire simultaneously on the same limb, the system thrashes.”

*Autonomy* requires a closed loop that observes the entire operating environment, understands the tradeoffs between performance and cost, and assumes end-to-end accountability for the outcome.

The Unix philosophy remains the right blueprint for the execution layer: HPA, VPA, KEDA, and Karpenter should continue executing the specific API mutations they were designed to handle. What Kubernetes fundamentally lacks is the central intelligence layer that decides what those actuators should do.

The next time your platform team debates whether to implement HPA or VPA, step back and ask a broader question: *Who decides this workload’s size, and do they have the full picture?*

In modern clusters, nobody does. Solving Kubernetes rightsizing requires building a system that finally does.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/10/768a3b9f-sedai_nikhil_kurup-rich-bentley.jpg)

Nikhil Kurup is Senior Vice President of Engineering at Sedai. As a leading expert in building machine learning systems that operate at massive scale, Nikhil ensures that Sedai can safely manage and optimize the cloud at some of the world’s...

Read more from Nikhil Kurup](https://thenewstack.io/author/nikhil-kurup/)