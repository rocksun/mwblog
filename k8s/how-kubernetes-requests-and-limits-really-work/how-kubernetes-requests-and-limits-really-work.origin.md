# How Kubernetes Requests and Limits Really Work
![Featued image for: How Kubernetes Requests and Limits Really Work](https://cdn.thenewstack.io/media/2024/11/db6c17c5-wizard2-1024x576.png)
*“Any sufficiently advanced technology is indistinguishable from magic.”*
**— Author Arthur C. Clarke**
[Kubernetes](https://thenewstack.io/kubernetes/) is inarguably an elegant, refined, well-designed edifice of open source enterprise software. It is known.
Even so, the internal machinations of this mighty platform tool are shrouded in mystery. Friendly abstractions, like “[resource requests](https://thenewstack.io/understanding-kubernetes-resource-types/)” for CPU and memory, hide from view a host of interrelated processes — precise and polished scheduling algorithms, clever transformations of friendly abstractions into arcane kernel features, a perhaps unsurprising amount of math — all conjoining to produce the working manifestations of a user’s expressed intent.

Most team members in a typical software development or IT infrastructure group will [never have reason or need to dive into Kubernetes details](https://thenewstack.io/stop-setting-cpu-and-memory-requests-in-kubernetes/), to truly understand at a deep level how their YAML manifests are turned into a running reality.

Learn even a little bit about how it actually works, and others might start to mistake your newfound knowledge for sorcery.

At [StormForge](https://stormforge.io/), I work with a [complicated subsystem team](https://www.atlassian.com/devops/frameworks/team-topologies#:~:text=3.%20Complicated%2Dsubsystem%20team) (wizards?) wholly focused on one very specific, frequently mistaken for benign element of Kubernetes: resource management. But this article isn’t about what I do; it’s about what I’ve learned.

This is Chapter 1 of a four-part series peeling back the onion of how Kubernetes requests and limits actually work. Throughout the series, I’ll guide you down the path towards becoming a Kubernetes requests and limits wizard yourself.

By the time you reach the end of Chapter 4, you should have:

- A contextual end-to-end summary understanding of how resource management in Kubernetes is implemented.
- Clear knowledge of what the Kubernetes resources abstraction is good at, and what its weaknesses are.
- Exposure (like a tan) to the technical implementation details of requests and limits at the Linux kernel level.
- An improved ability to predict and debug the quirks and undesirable outcomes that come from improperly set requests or limits.
- A tidy, high-level handbook of Key Observations™ to help make rule-of-thumb management decisions about requests and limits, even when you aren’t thinking deeply about kubelet, kube-scheduler, cgroups or how the OOM Killer works.
Let’s get started.

## Big Picture View: Layers in the Looking Glass
To truly understand what requests and limits actually do, beyond the niceties of their abstraction, it is helpful to lay out each of the subsystems that relate to these inputs.

**Pod spec (kube-api)**
The user’s raw resource request and limit values are saved in the pod spec.**Node status (kubelet)**
Kubelet reports static capacity information as part of each node’s status.**Pod scheduling (kube-scheduler)**
The scheduler considers node capacity information, running pod requests and pending pod requests in deciding which nodes to schedule pending pods to run on.**Container configuration for CPU (container runtime)**
Kubelet and the container runtime (for example, containerd) will set cgroup parameters based on the values given as CPU requests and limits.**Container configuration for memory (container runtime)**
Like for CPU, kubelet and the container runtime will set cgroup and other parameters for each container and process, this time based on the values given as memory requests and limits.**Node pressure and eviction (kubelet)**
Kubelet periodically evaluates the node’s overall resource situation. If it notices too much resource pressure, it may take an action (for example, evicting one or more pods) to try and alleviate the issue.
We’ll peer into each of these layers somewhere along our journey.

## Pod Spec
This layer is small, but it’s still a layer because it’s important.

Every pod wants resources (BestEffort [QoS](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/) pods notwithstanding). Spec is just [desired state](https://github.com/open-gitops/documents/blob/v1.0.0/GLOSSARY.md#desired-state), so nothing really happens at this layer besides the desired state being recorded. It shouldn’t be taken lightly though. The resources containers want, and the limits that should be set, all start here.

There is a lot to pod spec, but right now, we only care about part of it. A useful incantation to examine just the resource settings in detail (for a fairly arbitrary selection of a single pod) can be composed out of `kubectl`
and `jq`
, thusly:

## Node Status
Pods want resources. Nodes have resources. While pod spec records what resources a pod wants, node status records what resources a node has. This makes node status the corresponding input to a pod/node resource matchmaking system. Both pod spec and node status need to be known and defined before any pod-running action can take place.

With pods constantly being scheduled and unscheduled on nodes, you might assume that the resources a node reports having would constantly change. But that’s not how it’s done. What each node reports is just a simple, static, allocatable capacity. This number never changes, regardless of how many pods the node is running. It’s not what is allocated, it’s just what the node could allocate in theory.

In the next few examples, we’ll show status information for an example node. For consistency, we’ll pick a node here by name and remember it.

Now consider the following command. This invocation can be used to display an example of what node status looks like, for allocatable CPU and memory. Just like pod spec, there is a lot going on in node status, but we want to strip away everything extraneous and focus just on the resources information for now.

Capacity is the raw measure of the node’s resources; allocatable is the portion of it that Kubernetes considers available to claim for running pods.

## Pod Scheduling
After a pod is created in the Kubernetes API, it must be scheduled on a node to run. It needs matchmaking. The first two layers we explored, pod spec and node status, come together in the act of scheduling.

The kube-scheduler’s job is to pick a specific node to run pods on, and a big part of its decisions will be based on whether the resources any given pod is asking for are available on a candidate node.

In the scheduling phase, the resources abstraction is still fully intact, but only half of it matters: requests.

Limits mean something later, but not here. Limits are completely ignored when deciding on which node to schedule new pods to run.

To decide if a node has resources available for a new pod, kube-scheduler just adds up requests made by all pods already running on the node and subtracts that number from the node’s allocatable capacity. If the pod’s requests are less, there is room to run it on the node. If the pod’s requests are higher, there isn’t room.

Critically, note that physical resource utilization has nothing to do with this decision. The node could theoretically be melting its CPUs into slag and have allocated every byte of its memory, but if the requests made by its pods don’t add up to the number it reports is allocatable, kube-scheduler will happily give it more pods to run.

Conversely, if the node’s CPUs are effectively idle and memory usage tiny, it might still be considered full by the scheduler. The resources don’t have to be actually used — only requested — to make a node logically full for this purpose.

## Node ‘Fullness’
Figuring out how full a node is isn’t reported directly, and it has to be computed anew whenever you or something else wants it. Luckily kubectl has this calculation built into its `describe`
output for nodes, if you’re ever curious to see it.

For the (im?)practical wizard, consider the following arcane synthesis of `kubectl`
and `awk`
.

The 1351m CPU allocated number will be the sum of CPU requests from all containers in the pods running on this node. If you’re curious to do a rough version of this calculation yourself, you can approximate it with CLI tools. Start by fetching all of the non-terminated pods scheduled on the node:

Then, output the pod list to JSON and add a jq script to collect all requests (for example, CPU requests) and sum them.

The number should match what `kubectl describe`
showed, demonstrating how kubectl and kube-scheduler get these numbers.

There’s one last `kubectl`
+ `jq`
incantation left in the (im?)practical portion of the article, before we transition more into theory. The following monstrosity of a command aims to demonstrate how much CPU is still available on a node, and thus how large of a CPU request a pod could make (in theory), and still be scheduled to run here.

At the end of the day, what these commands do is demonstrate this simple relationship:

### 💡Key Observation
A node becomes “full” and unable to accept additional workloads based on resource requests. The actual CPU or memory used on the node doesn’t matter in deciding whether the node can handle more pods.

If you want a node being “full” to mean its actual CPU and memory resources are being used efficiently, you need to make sure CPU and memory requests match up with actual usage.

Limits have no bearing on a node being “full” or not, and they are completely ignored at this stage.

## The Journey Continues: Deep Dive Into CPU
After the pod is assigned to a node (a match made in heaven, I’m sure), the node needs to run each of the pod’s containers as a Linux process. Linux doesn’t know anything about the Kubernetes resource abstraction though. How do resource requests and limits come into play at the Linux OS level? What does that implementation mean in terms of anticipating, predicting or guaranteeing outcomes based on pod spec and node status?

With Kubernetes scheduling out of the way, we will delve deep into Linux CPU resource implementation details in Chapter 2.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)