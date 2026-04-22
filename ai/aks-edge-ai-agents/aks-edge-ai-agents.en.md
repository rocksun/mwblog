For this episode of *The New Stack Makers*, we sat down with [Jorge Palma](https://www.linkedin.com/in/jpalma21/), the PM lead for Azure Kubernetes Service at Microsoft, at KubeCon Europe 2026 in Amsterdam.

VIDEO

He had just delivered a keynote demo of agentic operations for Kubernetes, using an agent that troubleshot an application issue, mitigated the problem, and delivered a root cause analysis in about two minutes.

But for this discussion, we focused on demoing the mechanics of running AI at the edge, the emerging abstraction layer for inference engines, and how Microsoft is rethinking security for agents.

“We don’t want them to have permissions forever,” Palma tells *The New Stack*, “but in their identity to be very, very scoped down and then have temporary permissions to do the task that it’s been requested to do that the user approved.”

## The cloud-to-edge continuum for AI

The pitch for edge AI may sound familiar: process locally for low latency and data residency, and then offload the heavy lifting to the cloud. Palma acknowledges that the vision predated today’s AI tooling. “It was easier said than done,” he says of early hybrid promises.

What changed is the maturity of the primitives, he says. Microsoft’s Arc as the bridge for managing non-Azure resources, for example, and Azure Kubernetes Service (AKS) at the edge, combined with improved fleet management, is what is making AI at the edge in the Microsoft ecosystem much easier now.

What’s different from the edge computing pitch of a few years ago is the connecting tissue. Kubernetes spans both environments, and fleet management now automates what used to be manual GitOps workflows.

“GitOps has been allowing folks to transition between edge and cloud for a long time, but it has been a manual process,” Palma says. “I have one cluster here, one cluster there, and I’m going to use GitOps to deploy to one and then manually or automatically — but something I script — to deploy to the edge.

“With things like fleet, you can automate that; you still leverage GitOps for source syncing and deployment, but fleet management handles rollouts because it understands the roles of those environments. It understands that maybe one is test, one is dev, one is prod.”

## AI Runway and the portability bet

If Kubernetes is the connecting tissue between cloud and edge, the inference engine layer still lacks a common interface. The landscape has gotten crowded fast. NVIDIA’s Dynamo, Microsoft’s KAITO, and llm-d (recently contributed to CNCF) are all viable options, but they differ.

AI Runway, [which Microsoft introduced at KubeCon](https://github.com/kaito-project/airunway), provides a Kubernetes API for inference workloads. Teams standardize on a higher-level interface while swapping engines underneath. A cloud deployment might run one engine; an edge deployment might use something lighter, but the promise is that the API stays the same.

Palma frames this as a natural extension of what made Kubernetes popular. “You can use any of those, but you can standardize on a higher-level API,” he says. “You can even pick different engines in the cloud, different engines at the edge, and you’re able to make use of that with the same common API. It’s a bit of a Kubernetes principle applied to AI.”

The project lets you pick a model from HuggingFace, checks that the GPU is sufficient, and calculates cost estimates.

## Securing agents that don’t follow a script

Portability and abstraction only matter if the workloads running on top are trustworthy. Given that agents are non-deterministic, that’s one of the biggest challenges for enterprise deployments.

“You need to start thinking about how you put policy engines around [agentic systems], and how you’re actually able to control them,” Palma says. “You need to have your agents give you a plan of what they’re executing and then have that validated against some sort of business policy […]. The agent is, to some degree, delivering on what was asked,” Palma says, “but it’s not bound by any constraints, by any policies, and so it might do it in a way that was unexpected.”

His solution borrows from how Microsoft manages its own employees’ access: scoped identities, temporary permissions, and automatic revocation when the task is done. Applied to agents, this means an agent submits an execution plan, a policy engine validates it against business rules, and if the plan doesn’t align, “it shouldn’t be executed, and it should be rethought and tinkered again.”

At the infrastructure level, that translates to pod-level sandboxing on AKS. Microsoft recently open-sourced the [Agent Governance Toolkit](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/), which deploys as a sidecar container and enforces policies at sub-millisecond latency. The toolkit, Microsoft says, addresses all [10 OWASP agentic AI risks](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).

Palma frames the broader challenge as building for a future that won’t sit still. “Trying to build solutions that you know you want them to be static and unchanged for the next three years is a very challenging thing,” he says.

The cloud-native ecosystem solved portability and abstraction once, for containers. Now those same primitives, from Kubernetes to fleet management to policy engines, are tasked with absorbing the AI workload shift without requiring teams to start over. The statefulness problems Palma raises toward the end of our conversation (session persistence for agents, pod live migration for long-running inference jobs) suggest that even this more mature toolkit is still catching up with the workloads being thrown at it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)