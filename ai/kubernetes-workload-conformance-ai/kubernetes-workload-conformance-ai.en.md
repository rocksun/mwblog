**Welcome to the final edition of** [**Road to KubeCon**](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/), where we track the Kubernetes and cloud-native ecosystem each week on *The New Stack* as we head into KubeCon + CloudNativeCon NA, November 9-12 in Salt Lake City, Utah.

This week we explore how Kubernetes is getting new guidance for running AI workloads, including a new book from TNS, a dedicated Kubernetes working group, and advice on running LLMs across multiple GPUs.

Also in this day-before-Halloween-timed column, we’ve got OTel operators speaking a new language, security horrors from the latest AGNTCon + MCPCon, and untangling the dark webs of Kubernetes pod troubleshooting gone awry.

## **Join the conversation with HPE at KubeCon**

HPE will have a [big presence](https://www.hpe.com/us/en/events/kubecon.html) at KubeCon NA this year. The gold sponsor will be at Booths 151 and 145, where they’ll present live sessions throughout the day on topics spanning vSphere, HPE Kubernetes Service (HKS), distributed inference, setting up cloud storage for Kubernetes, and more.

*Hewlett Packard Enterprise (HPE) is a presenting sponsor of Road to KubeCon.* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *helps IT organizations modernize infrastructure, streamline operations, and accelerate AI initiatives across hybrid, multi-vendor environments.*

This year, the focus is on gaining visibility and control across Kubernetes environments across VMs, infrastructure, and clouds. If you’d like to schedule a meeting with an HPE representative, contact jennifer.osuna@hpe.com.

## **TNS publishes Kubernetes guidebook for 2027**

In partnership with HPE, The New Stack has [published a helpful book](https://thenewstack.io/kubernetes-agentic-ai-platforms/) containing ten checks for teams running AI workloads on Kubernetes. The book, [*Kubernetes in 2027: Building Platforms for AI, Autonomy, and Scale*](https://thenewstack.io/ebooks/kubernetes/kubernetes-in-2027/), is available for download now.

Written by contributing writer [Chris J. Preimesberger](https://www.linkedin.com/in/editingwhiz/), the guide spans the full lifecycle, covering how to stress-test infrastructure before launch, how to meet the nuanced demands of agentic AI, what to watch for, and how to develop stronger permissioning models for agents.

Since agentic AI is prone to bursty, unpredictable behavior, arming your infrastructure with the right approach on Kubernetes is an important first step to production stability and success with AI at scale.

## **Kubernetes gets a Workload Conformance Working Group**

Workload types have been expanding for years. And AI undoubtedly adds more variety. Against this backdrop, on Tuesday, October 27, the Kubernetes community announced a dedicated [Workload Conformance Working Group](https://kubernetes.io/blog/2026/10/27/announcing-workload-conformance-wg/).

According to Broadcom’s [Nabarun Pal](https://www.linkedin.com/in/palnabarun/), writing on behalf of WG Workload Conformance on the [Kubernetes blog](https://kubernetes.io/blog/2026/10/27/announcing-workload-conformance-wg/), “The working group is writing a shared standard for how workloads behave at runtime on Kubernetes.” To do so, they’ll need community input, Pal adds.

The [Kubernetes AI Conformance](https://github.com/cncf/k8s-ai-conformance) test already determines whether a cluster can run AI or machine learning (ML) workloads. Yet none currently exists for workloads, requiring workarounds, manual exploration, or monitoring for signs like node drain or permission issues. So the new WG aims to create a similar standard for workloads.

It’s a significant step forward as the Kubernetes community grapples with a growing variety of workloads, including AI. Interested parties can read the [working group proposal](https://github.com/kubernetes/community/pull/9139) for more information, join the [Slack channel](https://kubernetes.slack.com/messages/wg-workload-conformance), or attend [biweekly meetings](https://docs.google.com/document/d/16GPnmukPqbTkauWb3CtXzA3aEDUXoVKY34gA41YQmPk/edit) to get involved.

## **OpenTelemetry Transformation Language reaches v1**

Earlier this week, the OpenTelemetry (OTel) project reached a milestone: the [OpenTelemetry Transformation Language (OTTL) has reached v1](https://opentelemetry.io/blog/2026/ottl-v1/). It’s stable for traces, metrics, and logs, and is included within Collector Contrib v0.164.0 and onward.

As Grafana Labs’ [Tyler Helmuth](https://www.linkedin.com/in/tyler-helmuth-53150899/) recounts [on the OTel blog](https://opentelemetry.io/blog/2026/ottl-v1/), OTTL was created in 2022 as the configuration language for the transform processor. The domain-specific language lets you modify, filter, and enrich telemetry data directly at the collector level.

Longevity-thinkers will like this: They’ve also made a big backward-compatibility promise for OTTL. “If you write OTTL statements, the syntax and the standard functions stay backward compatible,” says Helmuth.

*As Kubernetes evolves, so do the demands on the teams running it. Presenting sponsor* [*HPE*](https://www.hpe.com/us/en/products/software.html) *helps teams address that complexity with software spanning virtualization, cloud management, observability, and automation.*

## **Solving LLMs on shared GPUs**

Putting all AI workloads on a single GPU is expensive and inefficient. But how do we pack multiple LLMs on shared GPUs safely, without a bunch of guesswork or manual toil?

[Ratnopam Chakrabarti](https://www.linkedin.com/in/ratnopam/), a senior solutions architect at AWS, took to X to share an early preview of his upcoming joint Nvidia–AWS session, which will seemingly answer this question for KubeCon attendees.

He says his KubeCon session will “demonstrate an agent pipeline that profiles workloads and handles model colocation on GPUs, all in real time.” It’s one of many KubeCon sessions this year tackling AI optimization on Kubernetes.

## **Troubleshooting GKE workloads with VPC Flow Logs**

This week on the [Google Cloud blog](https://cloud.google.com/blog/products/containers-kubernetes/using-vpc-flow-logs-to-troubleshoot-gke-workloads/), Google Cloud product managers Nishant Kumar and Whitney Jenkins describe a common issue for cloud operators: Kubernetes pods are ephemeral, making them hard to troubleshoot.

As they describe, “In a standard cloud network, flow logs provide that view by recording connections between IP addresses, ports, and protocols.” In Kubernetes, however, pods are temporary; they add, and by the time you track them down, they’ve often already vanished — leaving little evidence or records to inform troubleshooting.

The workaround, at least for those using Google Kubernetes Engine (GKE), is its built-in [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs). This feature uses Google’s virtualized network to log every sampled flow with metadata like pod, workload, namespace, and service.

It’s one example of how cloud-native platforms are continuing to advance the infrastructure around Kubernetes to increase its visibility and usability.

## **AGNTCon + MCPCon prioritizes agent security**

Is your agent installing malware without your knowledge? It’s a real possibility.

The latest [AGNTCon + MCPCon](https://events.linuxfoundation.org/agntcon-mcpcon-north-america/) event this month in San Jose, California, featured plenty of interesting talks that might resonate with the cloud-native community looking at the agent trend with big, worried eyes.

For instance, Snyk’s [Liran Tal](https://lirantal.com/speaking/talks/your-ai-agent-installed-malware-because-a-skill-md-told-it-to) gave a talk entitled [*Your AI Agent Installed Malware Because a SKILL.md Told It To*](https://lirantal.com/speaking/events/2026-10-23-agntcon-mcpcon-north-america-2026). Tal covered how agents often get tricked into running malware and offered some guidance on how to prevent it.

Vstorm’s Antoni Kozelski and Bartosz Adam Gonczarek [also presented](https://vstorm.co/events/agntcon-mcpcon-north-america-2026/) how they built an e-commerce MCP server and let the agent experiment with purchases across four different hosts. It behaved drastically differently in each scenario.

The session opened a conversation about where authorization rules that allow or disallow agents from taking irreversible steps should live. For Vstorm, it meant placing them on the server, not locally. They’re also following up with a [webinar on the subject](https://vstorm.co/events/agntcon-mcpcon-follow-up-webinar-2026/) soon.

These stories are just two examples of what we’re seeing a lot: the [unintended consequences](https://curity.io/blog/5-agentic-ai-security-incidents-and-vulnerabilities/) of giving AI agents the keys to the kingdom. Cloud-native operators should watch for stories like this as they build the foundational infrastructure to support agents.

## **See you at KubeCon**

*Road to KubeCon is an eight-part series presented by HPE. Before you go, explore how* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *helps IT teams do more with less complexity.*

And that’s a wrap for this year’s Road to KubeCon series! It’s been a privilege and an adventure profiling the top movements in the cloud-native world over the past two months.

In this weekly column, we covered many areas across eight editions, spanning updates to Kubernetes itself, like the [Kubernetes 1.37 update](https://thenewstack.io/kubecon-kubernetes-updates-security/) and the move to [cgroup v2](https://thenewstack.io/kubernetes-node-swap-ai/).

Much of the discussion centered around how cloud-native technology is evolving for AI. We looked at case studies around [Kubernetes inference at scale](https://thenewstack.io/kubernetes-ai-inference-costs/), and how [agent harnesses](https://thenewstack.io/kubecon-agent-harness-koordinator/) are evolving.

Another recurring theme was increasing operator visibility. We saw how [OpenTelemetry and Prometheus are converging](https://thenewstack.io/opentelemetry-prometheus-observability-interoperability/) and how to [spot idle GPUs](https://thenewstack.io/kubernetes-agentic-ai-inference/) and optimize.

Arguably, the biggest takeaway is that the Kubernetes ecosystem is facing major shifts to meet the challenges of [running AI workloads](https://thenewstack.io/kagent-kubernetes-ai-agents/) at scale. Is it up for the task?

KubeCon NA is anticipated to tackle this question head-on, from discussion at the co-located events to the main keynotes, sessions, and the showcase floor.

View the [Road to KubeCon archive](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/) for all editions in this series, along with other insights from the TNS and [HPE](https://www.hpe.com/us/en/products/software.html) teams. A big thank you to the column’s sponsor, HPE, for making this column possible, and to the community members who shared their insights.

Now, we’re excited to continue the conversation in person at KubeCon NA!

See you there.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/02/96a1456d-cropped-e7e1c083-bill-doerrfeld.jpg)

Bill Doerrfeld is a tech journalist and API thought leader. He is the editor-in-chief of the Nordic APIs blog, a global API community dedicated to making the world more programmable. He is also an active contributor to a handful of...

Read more from Bill Doerrfeld](https://thenewstack.io/author/bill-doerrfeld/)