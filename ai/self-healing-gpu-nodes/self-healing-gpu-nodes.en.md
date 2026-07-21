When you run Kubernetes at the scale we do on Amazon EKS, nodes break constantly. GPUs fall off the PCIe bus. Container runtimes wedge. Network interfaces disappear. Across tens of thousands of clusters, “rare” hardware failures happen multiple times a day, somewhere in the fleet.

For years, everyone responded the same way: an operator wakes up, reads a dashboard, SSHes into the node, cordons it, drains it, terminates the instance, and waits for a replacement. Every step is human-paced. Every step is toil. And if the failure lands at 3 a.m. on a weekend, the workload sits degraded for hours before anyone looks.

We built the [EKS Node Monitoring Agent](https://github.com/aws/eks-node-monitoring-agent) to help close that gap, which we open-sourced in April earlier this year. It detects node failures and writes Kubernetes NodeConditions that signal the problem to Karpenter, which then automatically replaces the node if required. The agent is one piece of a larger system. To understand where it fits, you need to understand what manages the nodes it monitors.

> “Across tens of thousands of clusters, ‘rare’ hardware failures happen multiple times a day, somewhere in the fleet.”

[AWS launched Amazon EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html) that fully automates Kubernetes cluster infrastructure: compute provisioning, scaling, networking, storage, OS patching, and security hardening, so teams focus on applications, not cluster operations. It dynamically selects optimal EC2 instances (including GPU instances like P5, P6, and G6 families), scales based on workload demand, consolidates underutilized nodes, and keeps the operating system patched. EKS Auto Mode ships with automatic node repair as the default behavior: detection, severity classification, and Karpenter-driven node replacement all run out of the box with no add-on to install, no controller to configure, and no repair policy to write.

This is the story of how we built automatic node repair, the design decisions that shaped the system, and the hard lessons that came from operating it at GPU scale.

## Six lessons from building self-healing Kubernetes nodes at scale

After operating this across thousands of clusters, the lessons compress into a short list. These are not unique to our system. The same patterns show up in NPD, NVSentinel, AKS Periscope, GKE’s auto-repair, and anyone building a custom node controller. They are folklore that should be a checklist. The [open-source repo](https://github.com/aws/eks-node-monitoring-agent) reflects each of these lessons in code, from the reason-code stability guarantees in the API to the jitter implementation that solved GPU workload interference.

> “Your reason codes are an API contract. Additions are features. Renames are breaking changes.”

1. **Your reason codes are an API contract.** Every downstream consumer (repair controllers, dashboards, customer automation) keys on them by literal string match. Additions are features. Renames are breaking changes. Severity changes are breaking changes. Plan for them the way you plan for API versioning.
2. **Absent and Unknown are not the same thing.** “We are not watching” and “we are watching but cannot tell” require different responses from downstream automation. If your disabled monitor writes Unknown, some controller somewhere will eventually act on it. Emit nothing when you are not watching.
3. **Don’t cross ownership boundaries.** The kubelet owns workload-driven conditions. Your node-health agent owns hardware and infrastructure failures. Crossing that boundary means your repair system is fighting the kubelet’s eviction system, and one of them will make the wrong call.
4. **Measure latency from the source.** The detection SLO includes every hop in the signal chain: hardware event to driver log, driver log to journald, journald to agent poll, agent poll to NodeCondition write. The longest hop dominates. For kernel-level signals, journald flush cadence is the bottleneck. For GPU telemetry through DCGM, push-based policy violations (DBE, XID, NVLink) are near-instant, but polled field watches (NVSwitch fabric health, clock throttle) have a 5-minute floor. Know which path each detection uses.
5. **Detection and diagnosis are separate systems with separate consumers.** Detection feeds automation (fast, continuous, minimal data). Diagnosis feeds humans (on-demand, detailed, heavyweight). Conflating them degrades both.
6. **Test telemetry interpretation against the spec, not empirical values.** Hardware telemetry interfaces are not boolean. We read a DCGM bitfield for GPU fabric health and treated non-zero as failure. When a driver update changed the healthy return value from zero to a spec-defined non-zero mask, every GPU node was flagged unhealthy at once. The safety breaker held (by design), giving us time to ship the fix. The lesson: if you’re parsing packed enums or bitfields from GPU firmware, your test fixtures must come from the vendor documentation, not from what the field happened to return on previous hardware.

## Node health detection in Kubernetes: Traps no one warns you about

Every node health agent in the Kubernetes ecosystem performs the same translation. Node Problem Detector (NPD), NVSentinel, GKE’s auto-repair, AKS’s Linux Extension, and the EKS Node Monitoring Agent all take noisy, low-level signals from a machine and translate them into a set of Kubernetes primitives: NodeCondition, Event, sometimes a CRD. The translation looks simple. It isn’t.

The output is a NodeCondition, which is just a type, a status (True/False/Unknown), a reason code, and a message. Four fields. But that surface area hides decisions that determine whether a repair action helps or hurts.

**Reason codes are a public API.** We learned this the hard way. In version 1.6.2, we changed NvidiaDeviceCountMismatch from Warning severity to Fatal. The technical reasoning was sound: once a GPU drops off the PCIe bus, it doesn’t come back without a node reboot or replacement. Leaving it as Warning meant GPU workloads kept getting scheduled onto degraded nodes, wasting expensive accelerator capacity. So we shipped the fix. Downstream automation broke. Customers had repair configurations keyed on the old severity. Dashboards that filtered on Warning stopped showing the fault. Automation that only acted on Fatal suddenly started draining nodes it hadn’t touched before. Dashboards that filtered on Warning stopped showing the fault. Automation that only acted on Fatal suddenly started draining nodes it hadn’t touched before. From that point, we treat every reason code addition as feature work and every rename or severity change as a breaking change.

**“Absent” must not equal “healthy.”** When we shipped per-monitor configurability in v1.6.0, we had to make a choice. A disabled monitor needs to produce some output (or no output). The three options: write True (your auto-repair now thinks the node is healthy because you’re not watching), write Unknown (ambiguous, might trigger repair depending on downstream logic), or omit the condition entirely. Only the third is safe.

This seems obvious in retrospect, but consider that NPD achieves the same result through a completely different mechanism: compile-time disable via build tags. NVSentinel delegates it to operator-authored CEL rules. The upstream Kubernetes spec defines what Unknown means, but if your repair automation treats Unknown as actionable, you will lose nodes for no reason. We chose to emit nothing when a monitor is off, and documented it as a hard contract.

**Detection latency is bounded by the source, not by the agent.** We originally told customers, “We detect kernel panics within 30 seconds.” This was wrong. Our agent’s detection time was under 30 seconds. But the kernel panic shows up in journald, and journald’s flush cadence is the actual bottleneck. If journald takes 45 seconds to write the line, our 30-second claim was incomplete.

For GPU faults, the picture is more nuanced because we use two detection paths with very different latency characteristics. The critical faults (double-bit ECC errors, XID errors, NVLink failures, page retirements, thermal and power violations) go through DCGM’s push-based policy violation channel. DCGM notifies our agent the moment it detects the violation; there is no polling interval. Detection of these faults is near-instant (sub-second in practice). A separate path uses a 5-minute field-value window to monitor NVSwitch fabric health, Fabric Manager status, and clock-throttle reasons. That window is the floor for those specific detections, but it does not apply to the critical GPU faults that trigger automatic repair. The lesson: the customer-facing SLO must include source-of-truth latency, and different signal paths within the same subsystem can have radically different floors.

## Two severities, one switch: How auto-repair decides which nodes to replace

The kubelet already reports DiskPressure, MemoryPressure, and PIDPressure. NMA complements those with five additional conditions covering domains the kubelet does not monitor: kernel health, container runtime, networking, storage, and accelerated hardware. Every detection carries one of two severities, and severity is the switch that decides whether the repair cycle fires.

**Condition severity** is a terminal fault. It flips the matching condition to False and makes the node eligible for automatic repair. GPU device-count mismatches, critical XID and double-bit ECC errors, NVLink and NVSwitch fabric failures, a missing Fabric Manager, and Neuron DMA and HBM uncorrectable errors. On the networking and runtime side: VPC CNI process down, IPAMD unable to reach the API server, fork failures due to PID exhaustion, and pods wedged, terminating behind a broken container runtime. These are faults that won’t recover on their own. On GPU nodes, a single degraded accelerator can corrupt training checkpoints or waste thousands of dollars in compute per hour.

**Event severity** is informational. It posts a Kubernetes event, the NodeCondition remains True, and operators get visibility without disruption. Bandwidth ceilings, connection-tracking limits, Amazon Elastic Block Store (Amazon EBS) IOPS throttling, I/O delays, filesystem fragmentation, clock drift, liveness and readiness probe failures, kube-proxy anomalies, GPU thermal and power warnings, PCIe link degradation, and page-retirement thresholds. These signal trouble building before it turns terminal.

Getting severity wrong in either direction is expensive. Too aggressive, and you terminate healthy nodes and needlessly displace workloads. Too conservative, and degraded nodes serve traffic for hours while a GPU with a failing memory bank corrupts training checkpoints. The classification principle: if the failure is deterministic and infrastructure-owned (hardware broke, firmware crashed, a physical link went down), it triggers replacement. If the signal could be application-induced or transient, it stays informational. You never want to terminate a healthy node because a misbehaving pod saturated a resource.

> “Getting severity wrong in either direction is expensive. Too aggressive, and you terminate healthy nodes. Too conservative, and degraded nodes serve traffic for hours.”

DiskPressure, MemoryPressure, and PIDPressure are the canonical examples. Every major auto-repair system (GKE, AKS, NPD) has independently converged on the same answer: don’t touch them. These are workload-driven conditions, not node-level faults. Replacing the node just moves the misbehaving workload to a fresh machine, where it will eat memory again. The correct response is kubelet-level pod eviction, not node replacement. If you’re building a node-health system, draw this boundary early and document it publicly.

## The agent that hurt what it was protecting: GPU workload interference from health monitoring

The hardest lesson came from a customer running large-scale distributed GPU training. Their workload used NCCL collectives across hundreds of GPU nodes, where every node in a communication group must complete its step before any can proceed. One slow node makes every node wait.

They found that NMA itself was causing periodic slowdowns. The agent’s monitors all ran on independent goroutines, and when their polling intervals aligned, dozens of goroutines would wake simultaneously and burst onto many CPU cores at once. On a general-purpose web service, this would be invisible. In a distributed training job, microseconds of jitter on one node can cascade across the entire GPU cluster, causing measurable throughput loss.

The customer disabled NMA entirely and saw an immediate improvement. That was the worst possible outcome for us: a health agent that interferes with the workload it exists to protect is worse than no agent at all.

The fix was straightforward once we understood the problem. We added a startup jitter to every monitor’s polling interval. Each goroutine delays its first tick by a random offset (up to 20% of its base interval), staggering the wake times so they don’t align on boot. We cached system calls that hit /proc on every poll. We consolidated handlers that shared an interval into a single sequential work queue, reducing the goroutine count for monitors that didn’t need their own thread. The result was an agent whose CPU profile is flat and predictable rather than bursty.

The lesson generalized: if your health agent runs on the same host as the workload, its resource consumption pattern matters as much as its resource consumption total. A process that uses 0.5% CPU spread evenly is invisible. A process that uses 0.5% CPU in concentrated bursts can disrupt latency-sensitive distributed GPU workloads in ways that show up as lost training time rather than a CPU alarm.

This is why per-monitor configurability matters. Not every monitor is relevant to every workload. A dedicated GPU training cluster with one pod per node and no pod churn doesn’t need IPAMD monitoring or environment scanning. We shipped the ability to disable individual monitors so customers can keep the health coverage they need without paying the overhead of coverage they don’t.

## How the repair cycle works

Karpenter is the compute controller that provisions and scales [EKS Auto Mode nodes](https://thenewstack.io/eks-auto-mode-kubernetes/). It already owns the lifecycle of every node it launched, and consuming our NodeConditions for repair is a natural extension of that ownership. There’s no separate repair backend, no sidecar controller, no webhook chain. The same system that created the node is the one that replaces it.

Karpenter’s AWS cloud provider declares repair policies: each one pairs a condition type with a status that means “replace this node.” The policies include toleration windows that prevent reacting to transient blips:

* Accelerated hardware faults: 10 minutes. These are unambiguous (a GPU is either present or absent) and expensive to leave running (a training job on a degraded node wastes GPU-hours).
* Everything else (kernel, runtime, networking, storage, kubelet NotReady): 30 minutes. Enough time for a transient network blip or a temporary runtime hiccup to resolve on its own.

The flow:

1. The agent detects a terminal fault and flips the matching condition to False with a reason code.
2. Karpenter’s health controller sees the transition and starts a timer.
3. If the condition clears before the window expires, the timer resets silently. The node was never touched.
4. Past the toleration window, a safety gate checks fleet health. Karpenter will not repair more than 20% of nodes in a NodePool simultaneously. If a correlated event (a bad AMI rollout, a control-plane hiccup, a zonal impairment) trips conditions across many nodes at once, the system holds. Auto-repair also stands down while an Amazon Application Recovery Controller zonal shift is active, so deliberate traffic movement away from an impaired Availability Zone is not mistaken for a fleet of broken nodes.
5. Inside the safety threshold, Karpenter taints the node to block new scheduling, gracefully drains running pods (respecting PodDisruptionBudgets), terminates the instance, and provisions a replacement sized for the displaced workload.

The replacement node comes up with a fresh agent monitoring it from boot. No operator in the path. In our testing, the full cycle from fault injection to replacement node running workloads took under 12 minutes. Detection landed in under a second (critical GPU faults use DCGM’s push-based policy channel, not polling). Then 10 minutes of toleration, and roughly 90 seconds for the replacement to launch and register.

## The part that surprised us: detection and diagnosis are not the same problem

Auto-repair handles the common case: broken node gets replaced, workload keeps running. But “why did that node fail?” is a different question, and one we initially tried to answer inside the detection path. That was a mistake.

Detection answers “is this node healthy?” It runs continuously with minimal overhead, and it needs to be fast: a condition flip that takes 5 minutes to produce is 5 minutes of degraded workload. Diagnosis answers “what went wrong?” It needs to collect detailed artifacts: full journald output, containerd state, network configuration, dmesg, GPU driver logs. In our testing, that collection completes in about 7 seconds and produces a compressed log bundle. Baking it into the detection hot path would have slowed down the thing customers care most about: how fast the system reacts.

We built them as separate concerns sharing an agent binary. The NodeDiagnostic CRD lets you request a full log bundle from any node through kubectl, without SSH. On EKS Auto Mode, where nodes are Amazon Elastic Compute Cloud (Amazon EC2) managed instances with no shell access by design, this is the only way to investigate after a GPU failure or any other node-level fault.

The experience is one command:

`kubectl ekslogs <node-name>`

The plugin creates a NodeDiagnostic resource. The agent on the target node detects it via a watch, collects system state into a compressed tarball, and stores it temporarily (available for 10 minutes). The plugin then downloads it through the kubelet’s Node Log Query API (KEP-2258, GA in Kubernetes 1.36). No SSH, no security groups, no key pairs.

This separation means detection doesn’t slow down to collect evidence, diagnosis doesn’t need to be always-on (saving node resources), and you can diagnose a node that auto-repair has already flagged but hasn’t yet terminated. The 10-minute window for accelerated hardware faults gives you exactly enough time to [grab the logs](https://thenewstack.io/observability-isnt-enough-its-time-to-federate-log-data/) before the node is gone. If you’re interested in further improvements, engage with us on [EKS public roadmap](https://github.com/aws/containers-roadmap/issues).

## What this means if you’re running EKS

On [EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html), all of this is on by default. [Auto Mode fully manages your cluster](https://thenewstack.io/how-amazon-eks-auto-mode-simplifies-kubernetes-cluster-management-part-1/) infrastructure (compute, networking, storage, patching, and security hardening) so you focus on applications, not cluster operations. The agent runs as a systemd service in the node image (not a DaemonSet you manage), Karpenter consumes its conditions as part of the compute lifecycle it already owns, and kubectl ekslogs gives you diagnostic access without SSH. There is nothing to install, configure, or operate. For GPU workloads, this means your expensive accelerator nodes are automatically monitored, classified, and replaced without any operator intervention.

On managed node groups or self-managed Karpenter, you can assemble the same loop: install the Node Monitoring Agent as an EKS add-on and opt each node group into auto-repair. The architecture is the same, just not pre-assembled.

The EKS Node Monitoring Agent is Apache 2.0 open source at [github.com/aws/eks-node-monitoring-agent](https://github.com/aws/eks-node-monitoring-agent).

The failure modes we hit when running it at scale, and the fixes that come out of them, flow back to anyone using it. If you’re building a node-health system or running ours and hitting an edge case, come build with us!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/07/fdc3cdcb-gundapun-576x600.jpg)

Sajjan Gundapuneedi is a Sr. Manager of Software Development at AWS leading EKS compute infrastructure. His teams own the full node lifecycle for Amazon EKS: provisioning (Karpenter, Auto Mode, Managed Node Groups, Fargate, Hybrid Nodes), runtime (AMIs, networking, container runtime),...

Read more from Sajjan Gundapuneedi](https://thenewstack.io/author/sajjan-gundapuneedi/)