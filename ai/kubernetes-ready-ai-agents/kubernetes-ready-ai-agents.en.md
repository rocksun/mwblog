**Kubernetes was built around a fairly simple assumption.**

It’s that software does what its developers told it to do. AI Agents complicate that assumption. An agent can reason about a problem, choose a course of action, call tools, write code, interact with other systems, and keep working toward a goal. That is precisely what makes agents useful. But it is also what makes running them in production different from running a conventional application.

And increasingly, enterprises want to run them on Kubernetes. A recent [survey](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/) by the Cloud Native Computing Foundation (CNCF) found that two-thirds of organizations running [AI inference workloads](https://thenewstack.io/cncf-kubernetes-is-foundational-infrastructure-for-ai/) run them on Kubernetes. This makes sense, as Kubernetes has become the standard way enterprises deploy and operate distributed applications over the past decade. It already knows how to schedule workloads, allocate resources, recover from failures, and scale applications up and down.

---

***KubeCon + CloudNativeCon is taking place in Salt Lake City from November 9 to 12.*** [***Register now***](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)***!***

---

Inference demand can arrive in bursts, requiring customers to rapidly scale up underlying hardware and software resources to meet surging demand. In that regard, Kubernetes is an excellent fit. Similarly, as AI workloads wind down, Kubernetes can gracefully scale down the underlying infrastructure, ensuring economical operation.

As good as the fit between AI inference and Kubernetes is, the combination still has gaps, starting with security. Recent incidents at frontier AI labs, in which AI agents escaped test environments and launched malicious cyberattacks across the internet, highlight the need for strong guardrails to keep AI workloads from misbehaving.

Unfortunately, the probabilistic nature of AI leads to situations where it’s impossible to predict exactly what resources an AI workload will seek to use, which increases the likelihood that agents will eventually cross the line. Therefore, the ideal AI platform should make it easy to enforce clear guardrails and keep agentic workloads safely contained within well-defined sandboxes.

> “The ideal AI platform should make it easy to enforce clear guardrails and keep agentic workloads safely contained within well-defined sandboxes.”

By confining agentic AI workloads to a sandbox logically separate from other Kubernetes workloads, an enterprise can better ensure that if an AI workload does run off the rails, the ensuing damage stays within that sandbox.

Instead of letting agents access whatever resources they want, agentic platforms should use an [explicit permissioning framework](https://thenewstack.io/securing-kubernetes-ai-agents/) that grants or denies access to files, tools, and network and system resources. Agents should be fully restricted from executing code unless they have been given explicit permission.

The good news is that the Kubernetes community is moving toward adopting sandboxing as an architectural element for constraining AI agents. The CNCF is working to address Kubernetes’s security and isolation gaps. However, the open-source project’s functionality is not yet fully there.

Proper AI sandboxing requires looking beyond the container and into virtual machines or the host operating system to ensure agentic workloads can’t affect other applications running in the same environment. Enterprises looking to deploy AI into production today can turn to commercial Kubernetes distributions that already include these sandboxing capabilities.

Monitoring of AI workloads is another concern that keeps CIOs up at night. While frontier AI labs may not have adequately monitored what their AI models were doing, or even whether they had internet access, enterprises generally don’t have the luxury of asking for forgiveness when their agents misbehave.

Security may be the most obvious challenge, but it is not the only one. Agents are also changing how compute is consumed. A normal service might run continuously for months, while an agent may exist for only seconds.

> “A normal service might run continuously for months, while an agent may exist for only seconds.”

A user asks a question -> an agent starts -> it performs some work, possibly creates other agents, calls several tools, and then disappears.

Now multiply that pattern across thousands of users and the infrastructure begins to look very different from a conventional Kubernetes environment.

On top of that, starting a Kubernetes workload from scratch can take seconds. For many applications, that is perfectly acceptable. But for an interactive agent, those seconds can feel painfully slow. That creates an interesting infrastructure problem: How do you get the isolation of a fresh environment without paying the startup cost of creating one every time?

Hence, the sporadic nature of agentic workloads, and the need for agents to spin up rapidly, is testing even Kubernetes’ flexibility. Just as first-generation Kubernetes didn’t support stateful applications, the community is still searching for the best abstraction layer for running the new generation of agentic workloads.

> “Agents stay in a state of suspended animation in a warm pool, allowing them to reanimate in milliseconds rather than the seconds it would take to fully wake from deep sleep.”

One answer that is gaining attention in the community is [an agent substrate](https://thenewstack.io/kubernetes-ai-agent-runtime/) for rapidly scaling Kubernetes-based agentic workloads. With agent substrate, Kubernetes pods containing AI agents aren’t fully spun down when they’re not needed, because spinning them up from a sleep state would introduce too much latency from the user’s point of view.  Instead, agents stay in a state of suspended animation in a warm pool, allowing them to reanimate in milliseconds rather than the seconds it would take to fully wake from deep sleep.

When deploying AI workloads at scale in the real world, the details matter. Not every Kubernetes distribution provides the full raft of capabilities that enterprises demand. As the open-source Kubernetes community adapts to changing requirements, forward-looking platform providers are building the guardrails, sandboxing, monitoring, and agentic substrate that will let enterprise deploy AI now.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/10/ab1bdfba-cropped-694e7b43-dan-ciruli-headshot-1-dana-pratt-scaled-1-600x600.jpg)

Dan Ciruli leads the Cloud Native business at Nutanix and runs the Cloud Native product management team. His career in product management includes stints at Google, Zuora and EMC, and in open source he was a founding member of the...

Read more from Dan Ciruli](https://thenewstack.io/author/dan-ciruli/)