Google will soon make the infrastructure that powers its Gemini agents available to Google Cloud users in preview.

Announced on Thursday at the [Linux Foundation’s](https://thenewstack.io/agentic-ai-foundation-launch/) AGNTCon+MCPCon in San Jose, [Agent Compute Engine](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance) will become available in preview to Google Cloud users later this year. It will provide every AI agent with a hardware-isolated microVM that combines the speed of containers with the security of a sandbox.

## Who else offers agent sandboxes?

The idea of [agent sandboxes](https://thenewstack.io/cloud-agent-code-sandboxes/) is anything but new, of course. Startups like [E2B](https://e2b.dev/) and [Daytona](https://www.daytona.io/) offer them to developers (and support them on any cloud), as does AWS with [Bedrock AgentCore](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/).

E2B runs each sandbox in a [Firecracker](https://thenewstack.io/how-firecracker-is-going-to-set-modern-infrastructure-on-fire/) microVM, the open source virtualization technology AWS originally built for Lambda. It can pause a sandbox with its memory and filesystem intact and resume it in about a second. Daytona started out with containers but added microVM sandboxes in July. Those can pause a full machine or fork a running one into identical copies.

AgentCore also gives every agent session [its own microVM](https://thenewstack.io/agent-session-aware-runtime/). AWS doesn’t charge for CPU while an agent waits on a model or tool call, though memory keeps billing until the runtime reclaims it. Those sessions top out at eight hours. In August, AWS added EC2-based runtime instances that can keep shared sessions alive for up to 14 days.

It’s worth noting that Google itself isn’t new to this either. GKE already offers a managed version of [Agent Sandbox](https://thenewstack.io/google-debuts-gke-agent-sandbox-inference-gateway-at-kubecon/), the open source Kubernetes project Google launched last November. The company also sells code-execution and computer-use sandboxes through its [Gemini Enterprise Agent Platform](https://thenewstack.io/google-gemini-agent-platform/).

Agent Compute Engine, on the other hand, started out as internal infrastructure for Gemini, [Antigravity](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/), and Google’s own model training pipelines.

## Google’s take

Few companies — if any — run as many agentic workloads as Google, be that for its own internal use or its customers. According to the company, agentic workloads have quickly become one of the fastest-growing consumers of compute and storage across its fleet.

At this scale, the infrastructure services that power all of these autonomous agents don’t just need to be efficient and able to scale, but maybe more than anything, they need to be secure. Google, like some of its competitors, quickly realized that it needed to build a new purpose-built compute service to power all of these agents, similar to how it needed to build [Borg](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/), which later inspired Kubernetes, to manage compute in its early data centers.

As Rohit Jnagal and Ramanathan Venkatapathy, both distinguished engineers at Google, note in a technical deep dive, traditional VMs provide developers with a lot of control and flexibility, but at the cost of speed when it comes to booting, suspending, and resuming a machine. Given how fast agents start and shut down, that’s not an option.

Containers solve some of this, they note, “but there are multiple examples like coding agents and developer assistants that need complete isolation as well as kernel- and root-level control of the agentic environment.”

With Agent Compute Engine, Jnagal and Venkatapathy write, the team went back to first principles to build “a unified, agent compute platform for Google” (and now its customers).

## A persistent computer for every agent

At its core, it basically gives every agent a persistent, sandboxed computer to work with. That allows the agents to work with shell scripts, use a headless browser, and write code (with root permissions to that machine) in agent loops that could run for weeks.

But the team also built it for large-scale use cases like the eval loops that frontier labs use to test their models, AI benchmarking, and reinforcement learning.

In addition, the team also designed Agent Compute Engine to run sandboxed backends for Google’s own services.

Jnagal and Venkatapathy also note that agents spend most of their time waiting on the model or the user. So once an agent finishes a tool call, the host checkpoints its microVM, which then uses no active resources until the next call comes in.

## Nothing to steal inside the sandbox

The key feature here, besides speed, is to be able to trust that the agents can’t break out of their sandboxes. We’ve seen what happens when they do, after all.

Each agent session runs inside a single-tenant, memory-safe microVM. Those environments hold no secrets in memory or on the disk, and their only identity is a short-lived, session-scoped one delivered through a single per-VM local listener. All traffic is end-to-end encrypted in transit, and snapshots and disks are encrypted at rest.

The microVMs don’t get a standard network interface, either. All traffic runs through a proxy outside the sandbox, and when an agent needs to reach a service like Google Drive, Google’s Agent Gateway checks the user’s delegation and the sandbox’s identity before adding the actual credential, outside the sandbox.

The underlying host is basically a stateless appliance with a read-only filesystem, with the hardware and firmware cryptographically verified at each boot.

All of this is backed by Google’s own Titan and Titanium IPU [security platform](https://docs.cloud.google.com/docs/security/titanium-hardware-security-architecture). The microVMs themselves run on [Cloud Hypervisor](https://thenewstack.io/rust-based-cloud-hypervisor-heads-to-linux-foundation/), an open source virtual machine monitor, and each gets its own guest kernel and root access.

Jnagal and Venkatapathy use the example of an enterprise agent that manages a user’s inbox and reads an email with hidden instructions to find any API keys on the machine and send them to an outside address. Most of the time, they note, the model will ignore that, but not always.

“We started from one rule: Assume an attacker controls everything inside the sandbox, and make sure they find nothing there to use,” the team writes.

## Agent Substrate brings the same idea to Kubernetes

But not every team will want to have its agents run in a managed Google service. For them, Google also offers [Agent Substrate](https://github.com/agent-substrate/substrate), an open source runtime for the Google Kubernetes Engine (GKE) that it first announced in May.

Substrate builds on [Agent Sandbox](https://thenewstack.io/google-cloud-a-deep-dive-into-gke-sandbox-for-agents/), Google’s Kubernetes project, and adds a [lightweight control plane](https://thenewstack.io/kubernetes-ai-agent-runtime/) that Google says can handle millions of short-lived tool calls that would swamp Kubernetes.

Similar to Agent Compute Engine, Substrate snapshots an idle agent’s memory and returns the machine to the pool until the agent gets more work.

Google says that means up to 10 times the density of traditional compute. In a 200,000-agent benchmark, Substrate handled 500 activations per second, with agents suspending and resuming in under half a second, the company says.

Teams can isolate each sandbox with a microVM or [gVisor](https://thenewstack.io/how-to-implement-secure-containers-using-googles-gvisor/), and every agent gets its own cryptographic identity. As with Agent Compute Engine, egress proxies attach credentials outside the sandbox. Substrate runs on any Kubernetes cluster, and Google says it works with any harness, including Claude Code, [OpenClaw](https://thenewstack.io/openclaw-foundation-nonprofit-status/), and Nous Research’s [Hermes](https://thenewstack.io/openclaw-hermes-agent-harness/).

“We built Hermes Enterprise to enable customers to deploy into their existing infrastructure, while handling per-agent isolation and extensible access control,” Hervé Bizira, Nous Research’s chief business officer, notes in the announcement. “Agent Substrate addresses both at the platform layer in a way that also preserves valuable compute resources.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)