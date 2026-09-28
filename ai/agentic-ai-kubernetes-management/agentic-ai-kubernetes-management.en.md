**AI is changing expectations around infrastructure and operations**, including Kubernetes management. When models run close to the data they use, deployment, scaling, and governance responsibilities tend to shift to platform teams. And as clusters, environments, and operational signals continue to multiply, manual operations often strain under the added weight.

AI may simultaneously provide opportunities to lighten this growing load. Agentic software can now observe a system, reason about it, and act within predefined limits.

Ultimately, these platforms’ value depends on the quality of the context an agent can see and the boundaries you set. Without cluster state, policy, and access rules, an agent can only guess.

> Without cluster state, policy, and access rules, an agent can only guess.

For agentic AI to streamline multi-cluster management, you need clear lines between what the system observes, what it recommends, and what it changes. Drawn well, those lines let teams gain notable speed while still maintaining control.

## **The impact of AI on computing infrastructure**

Teams once treated AI as an application concern; models sat on top of existing systems, and the stack underneath stayed mostly unchanged. Today, AI reaches into more and more customer interactions, while data storage needs simultaneously expand and orchestration pressure grows. A [recent Forrester report](https://www.suse.com/c/the-new-ai-computing-stack-a-guide-for-tech-leaders-to-navigate-shifting-power-dynamics/) describes the modern AI computing stack as stretching from the models themselves into and across the infrastructure beneath them.

As AI workloads move into production, they place new demands on the infrastructure beneath them. Many lean on specialized compute, with resource needs that rise and fall through bursts of training and inference. Because conditions shift quickly, they can also call into question whether telemetry remains trustworthy. Each of these demands lands at the infrastructure layer, where the workloads run.

## **The infrastructure layer of the new AI stack**

The infrastructure layer covers compute, storage, and networking. It is a foundation that every workload running on the layer depends on. As AI workloads grow, choices about capacity, placement, and control will increasingly shape the performance of the data, intelligence, orchestration, and experience layers atop the infrastructure.

To operate the infrastructure layer efficiently across many machines and locations, a team may rely on orchestration instead of managing servers by hand. In cloud native contexts, [Kubernetes has become a control point](https://www.suse.com/c/the-ultimate-resource-for-choosing-a-hybrid-it-platform/) for scheduling workloads, applying policy, and presenting a consistent interface across environments. Kubernetes is especially well-suited to support organizations this way when teams need consistent control across an estate spanning data centers, clouds, and edge sites.

## **Agentic AI and Kubernetes: the future of the infrastructure layer**

Agentic AI can extend automation from fixed rules to systems that adapt to real-time conditions. Traditional automation runs the same script whether the environment has changed, while an agentic system observes the environment, reasons about what it finds, and then takes action.

When you apply agentic capabilities to multi-cluster management, the system follows this same sequence. An agent reads cluster state and operational data, proposes a diagnosis or next step, and then carries out actions based on an approved scope, usually after a person signs off. You can further reinforce these boundaries by routing each request to a specialized agent that receives only the metadata it needs.

The signals that an agent receives from the cluster, the context about policy and access, and the definitions of what the agent may change are the key elements that give agentic systems their value. They also separate [agentic AI on Kubernetes](https://thenewstack.io/ai-agents-vs-agentic-ai-a-kubernetes-developers-guide/) from a generic assistant.

## **Manual Kubernetes management is less efficient at scale**

Admittedly, agentic AI fits some settings better than others. On a small single-cluster footprint, the overhead may outweigh the benefit. Manual Kubernetes management often holds up on a handful of clusters, but it can become unreliable in a rapidly growing estate. After all, each new cluster adds lifecycle work across upgrades, patching, configuration, and renewal. Those tasks can quickly multiply and diverge in hybrid environments.

Configuration drift is a high risk in these situations. Settings that started identical can fall out of sync, and policies can apply unevenly from one team to the next. Individually, these gaps may be manageable, but collectively they raise the odds of an outage or a failed rollout.

Visibility can also erode in an unmanageable way. Clusters spread across data centers, clouds, and edge sites often leave teams with no single view of the whole landscape. When DevOps and platform engineers stitch together signals from separate tools, resolution can slow and become more error-prone. A unified view helps enable sound, efficient decision-making by people, agents, or both.

## **Kubernetes knowledge is fragmented, and existing AI tools lack business context**

Kubernetes expertise often sits unevenly across an organization. For example, senior engineers may hold deep operational knowledge that application teams lack. The most current information about a running system may also be fragmented if logs sit in one tool and metrics in another. Real-time understanding can be further clouded when policies, runbooks, access rules, and deployment history each live elsewhere.

Most well-trained AI models understand Kubernetes at a basic level, but they can’t know your unique cluster state, your policies, or your recent changes. Without that context, even a capable AI tool may fall short of providing meaningful Kubernetes management support.

> Most well-trained AI models understand Kubernetes at a basic level, but they can’t know your unique cluster state, your policies, or your recent changes.

When an agent can read current signals alongside the rules that govern them, its suggestions become specific, testable, and actionable. In an incident, agentic systems can correlate logs with a recent change. Ahead of a rollout, they can check the change against policy. During troubleshooting, they can account for access rules rather than guessing at them. Kubernetes decisions carry real operational consequences, which makes these details all the more important to consider.

## **Engineering “toil” isn’t time-efficient**

Site reliability teams use the word “toil” for repetitive manual work, especially tasks that keep systems running without adding lasting impact. In Kubernetes operations, toil takes the form of repeated triage, manual signal correlation, alert follow-up, and routine checks. The tasks aren’t particularly difficult, but they can consume significant time and attention for enterprise teams.

When engineers spend their days on this kind of investigation, proactive modernization efforts tend to stall and planned upgrades can slip behind schedule. In other words, the conditions that created the original toil perpetuate it, since teams lack the capacity to make related improvements. In a recent survey about how AI provides value to DevOps teams, [reducing toil](https://thenewstack.io/survey-where-ai-reduces-toil-and-where-it-still-falls-short/) emerged as one of the clearer opportunities.

> …the conditions that created the original toil perpetuate it, since teams lack the capacity to make related improvements.

Agentic AI can support repetitive investigations by gathering signals, correlating them, and proposing a likely cause for an engineer to weigh.

Kept under human review, it can take on some of the routine correlation that would otherwise fall to the team. That kind of support can give engineers more room to focus on the strategic work that most needs their judgment.

## **Building more intelligent infrastructure with agentic AI and Kubernetes**

As you consider building toward [intelligent infrastructure](https://www.suse.com/c/intelligent-infrastructure-in-the-age-of-agentic-ai-why-ecosystems-win/) without surrendering control, the following principles can inform your efforts:

* Start with observable context, giving agents access to current cluster state, policy, and history before they reason about a problem.
* Separate suggestions from actions, allowing agents to recommend freely while any change must wait for human approval and a defined scope.
* Connect agents to existing controls, routing their work through the access rules, identity, and audit paths the team already trusts.
* Keep the ecosystem open, favoring platforms that integrate with current tools and standards over those that lock work into a single stack.

Platforms like SUSE Rancher Prime and SUSE AI Factory embrace these principles and illustrate how Kubernetes management can become a foundation for agentic operations. These platforms can help you improve cluster and policy consistency without compromising your authority over AI. Built on open-source foundations, they can also help you avoid being trapped in a single vendor’s stack.

In SUSE Rancher Prime, the industry’s first [context-aware agentic AI ecosystem](https://www.suse.com/c/kubecon-eu-2026-first-agentic-ecosystem-platform/), its AI assistants work as a crew of specialized agents with an intelligent router. The platform draws on the cluster context already in place and acts through existing access controls. Through support for external Model Context Protocol (MCP) servers, teams can extend that crew to their own sources. In addition, human validation tools allow you to hold a proposed action for approval before the agent runs it.

Despite its potential, intelligent infrastructure is not universally beneficial. In situations where change control must stay fully manual, for example, agentic AI’s role may be strictly limited to observation and suggestion. Measure the technology’s value against the realities of your day-to-day operations. For those who are investing, agentic AI will have the greatest impact when it actively supports context, control, openness, and human judgment.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/09/60bed721-cropped-bfbd4737-rhys-200x200-1.jpg)

Rhys Oxenham is VP & General Manager, AI at SUSE, where he leads the company’s AI strategy and helps organizations build, deploy, and manage secure, open, and flexible AI infrastructure. He brings more than 15 years of enterprise technology experience...

Read more from Rhys Oxenham](https://thenewstack.io/author/rhys-oxenham/)