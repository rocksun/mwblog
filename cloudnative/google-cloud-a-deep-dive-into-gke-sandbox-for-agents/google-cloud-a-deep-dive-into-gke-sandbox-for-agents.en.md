Google Kubernetes Engine (GKE) [Agent Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox) is a new [Kubernetes](https://thenewstack.io/kubernetes/) extension designed to run workloads, such as AI agents, that execute untrusted or specialized code in isolated, secure environments. In essence, it [provides](https://thenewstack.io/google-debuts-gke-agent-sandbox-inference-gateway-at-kubecon/) a lightweight “VM-like” sandbox within a Kubernetes cluster, leveraging technologies such as [gVisor](https://gvisor.dev/) to achieve strong [kernel-level isolation](https://thenewstack.io/interview-google-gvisor-and-the-challenge-of-securing-multitenant-containers/).

This deep dive will explore what GKE Sandbox for Agents is, its role in the GKE ecosystem, and the architectural components and implementation details that Kubernetes engineers should know.

## What Is GKE Sandbox for Agents?

GKE’s Sandbox for Agents (often just called Agent Sandbox) is a Kubernetes-native mechanism to create ephemeral, isolated runtime environments on demand. It was introduced to address emerging use cases such as AI/ML agents that generate and execute code, or any scenario where untrusted code needs to run within a cluster without risking the host or other workloads.

Running arbitrary code or third-party agents directly on cluster nodes can pose security risks. Agent Sandbox mitigates these risks by providing process, storage, and network isolation for the code it runs, using a sandboxing layer powered by gVisor. In practice, this means that even if the code running in the sandbox is malicious or vulnerable, it’s far less likely to escape and affect the host kernel or neighbouring pods.

Importantly, Agent Sandbox is not a proprietary GKE-only feature but an [open source project](https://github.com/kubernetes-sigs/agent-sandbox), which is currently in the [Kubernetes SIG Apps](https://github.com/kubernetes/community/blob/master/sig-apps/charter.md) group. It introduces a new Kubernetes Custom Resource Definition (CRD) and a corresponding controller called Sandbox. This CRD serves as a higher-level abstraction for managing a single-container, long-running workload with VM-like qualities, such as a stable identity and persistent state, within Kubernetes.

In GKE, Google integrates and supports this CRD so that cluster operators can easily enable sandboxed agents on both standard and Autopilot clusters. In fact, on [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters, gVisor-based sandboxing is enabled by default on all nodes, whereas on standard GKE clusters, you need to explicitly create node pools with gVisor support to use Agent Sandbox.

[![](https://cdn.thenewstack.io/media/2025/12/2502e33c-k8s-agent-sandbox-1024x394.jpg)](https://cdn.thenewstack.io/media/2025/12/2502e33c-k8s-agent-sandbox-1024x394.jpg)

At the core of the implementation is the Sandbox CRD itself and its controller. This CRD defines the desired state of an isolated sandbox environment. When a Sandbox custom resource is created, the Agent Sandbox controller launches and manages a corresponding pod to fulfill the sandbox. Unlike a normal Deployment or StatefulSet, a Sandbox CRD represents a singleton pod — always exactly one pod per sandbox — with special handling for lifecycle and identity. Key architectural features of the Sandbox CRD include:

**Stable Identity:** Each sandbox is assigned a stable name (hostname and network identity) that remains consistent even if the underlying pod is restarted. In other words, the sandbox behaves like a single VM or node with a fixed identity, rather than ephemeral pod names that Kubernetes typically assigns. This is useful for applications that require a consistent hostname or IP address. The controller ensures the sandbox’s pod always uses the same name, and often a headless service or similar approach is used for DNS.

**Persistent Storage:** A sandbox can be configured with a PersistentVolumeClaim, so it retains state across restarts. This allows the sandbox to maintain data and installed tools over time, much like a VM’s disk. For example, an AI agent sandbox might install libraries or cache data on its first run, which persists on a volume for subsequent use.

**Lifecycle Management:** The Agent Sandbox controller creates the pod, monitors its health, and supports operations such as hibernation (pausing) and resumption. If a sandbox is not needed, it might be stopped (pod removed) while preserving its volume, and later brought back (pod re-created and state restored from the volume). This ability to hibernate/resume is a distinctive feature, as vanilla Kubernetes does not natively support pausing a pod’s execution. It’s beneficial in scenarios where an agent may be idle for extended periods but should resume quickly when needed.

To enable these capabilities, the Agent Sandbox project also defines some extension CRDs on top of the core Sandbox object:

**SandboxTemplate:** A reusable template that defines the spec (container image, resources, etc.) for sandboxes. This helps when you need to launch many similar sandboxes — instead of repeating the pod spec each time, you define a template once.

**SandboxClaim:** A higher-level abstraction that allows users (or other controllers) to “claim” a sandbox from a template without worrying about the details. The claim triggers the controller to create an instance of a Sandbox using a specified template. This pattern decouples the requestor from the implementation, useful in multitenant or on-demand scenarios (similar to how PersistentVolumeClaim works for volumes).

**SandboxWarmPool:** This extension keeps a pool of pre-warmed sandbox pods ready to improve performance. When a new sandbox is needed, instead of creating a pod from scratch (which can be slow when using heavy isolation), the controller can allocate one from the warm pool almost instantly. The pool is then replenished in the background. This design is crucial for reducing latency.

Under the hood, the Sandbox controller is implemented in Go and runs as a cluster deployment, much like other Kubernetes controllers. It watches for Sandbox and related CRD events and, for each Sandbox object, manages a corresponding Pod along with a PersistentVolumeClaim.

The controller ensures the Pod’s spec matches the template in the Sandbox CRD and that it’s scheduled on a node that supports the required runtime. Notably, the Sandbox CRD’s spec includes a podTemplate field where you specify the container image, command, and other Pod settings, including any desired runtime class for sandboxing (e.g. gVisor). In effect, the Sandbox resource is a “wrapper” around a pod with added constraints and features.

## Integration With Kubernetes and GKE Internals

Because Agent Sandbox is delivered as a CRD and controller, it integrates naturally with Kubernetes API machinery. You install the CRDs and controller in your cluster, and then you can create Sandbox resources much like you would create Deployments or Pods. The design as a native extension means tools like kubectl or Argo CD can manage sandboxes declaratively. The resource API (agents.x-k8s.io/v1alpha1) is standardized and open, enabling community contributions and interoperability. In fact, Google worked with the Kubernetes community to build this as a [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) project from the start, signaling its intent to make it a standard capability rather than a proprietary one.

On GKE Standard clusters, using the Agent Sandbox typically requires some setup: you need to enable GKE’s sandboxing support on the nodes where these pods will run. This is done by creating a node pool with the “Enable GKE Sandbox (gVisor)” option enabled (or via the `--sandbox type=gvisor` flag with gcloud or Terraform). Those nodes will have the gVisor runtime installed and configured with containerd. Then, any pod (including an Agent Sandbox-managed pod) scheduled on that node with the appropriate runtimeClass will automatically run in isolation within gVisor.

On GKE Autopilot clusters, Google has made this even easier. Autopilot clusters come with gVisor enabled by default on all nodes. An agent sandbox can be deployed on Autopilot without special node pool configuration; you merely need to specify the sandbox’s runtime as gVisor, and Autopilot handles sandbox execution. This automatic integration lowers the barrier to using sandboxed agents for those who prefer the fully-managed Autopilot mode.

GKE also provides features to tackle the performance and scalability challenges of running many isolated sandboxes. One such feature is [Pod Snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots), which is currently a GKE-exclusive capability in preview. Pod Snapshots allow the state of a running pod (memory, CPU state, and even GPU memory) to be checkpointed to durable storage and later restored into a new pod. When combined with Agent Sandbox, this means you could snapshot a fully-initialized sandbox environment and then spin up new instances of that sandbox rapidly by restoring the snapshot, rather than initializing each one from scratch.

Google has reported that using Pod Snapshots can reduce startup times for complex sandboxed workloads from minutes to seconds. It also enables economic efficiency. You can suspend idle sandboxes (saving their state to storage and removing the pod) to free up resources, and then resume them on demand by restoring the snapshot. This is a game-changer for expensive workloads like GPU-accelerated AI agents — you no longer need to leave them running idle and consuming resources when not in use.

Another integration point is in networking and identity. GKE encourages pairing the Agent Sandbox with tight network policies and [GKE Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). Each sandbox pod can be constrained by a Kubernetes NetworkPolicy (and, by default, gVisor provides some network isolation of its own).

In practice, one would adopt a “default deny” network posture for these sandboxes, allowing egress only to specific API endpoints or resources the agent absolutely needs. Likewise, using Workload Identity, each sandbox can be assigned an isolated IAM identity with minimal permissions, so that even if compromised, it cannot access other cloud resources. These are not built-in features of the sandbox itself, but recommended operational practices that GKE supports to bolster the overall security of agent workloads.

## Conclusion

GKE Sandbox for Agents represents a significant step in bridging the gap between traditional virtual machines and container workloads in Kubernetes. By providing a Kubernetes-native way to launch secure, isolated single-container environments, it empowers cluster operators to support new classes of workloads with far less risk.

Its architecture, built on a Sandbox CRD and controller that leverage gVisor’s novel user-space kernel model, offers an elegant solution for running “untrusted” code on a shared cluster without sacrificing security. At the same time, the integration with GKE’s ecosystem (like Autopilot automation, Warm Pools, and Pod Snapshots) shows that performance and usability concerns are being addressed through innovation.

For Kubernetes engineers, the Agent Sandbox is a tool that provides fine-grained control over how certain pods run. It exemplifies the direction of cloud-native infrastructure: offering flexibility and safety at scale. As the project matures, we can expect it to become a staple in GKE and potentially other Kubernetes platforms, enabling a new wave of applications that require both the power of Kubernetes orchestration and the peace of mind of VM-level isolation.

In summary, GKE Sandbox for Agents adds an essential option to our toolbox — one that allows us to say “yes” to running more adventurous or untrusted workloads on Kubernetes, confidently and securely.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)