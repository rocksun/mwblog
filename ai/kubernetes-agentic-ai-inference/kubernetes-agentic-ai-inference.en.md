**Welcome to another edition of [*Road to KubeCon*](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/)**! We’re tracking movements in the Kubernetes and cloud-native ecosystem as we count down to [KubeCon + CloudNativeCon North America 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/) November 9–12 in Salt Lake City.

Half of our column this week focuses on untangling Kubernetes as we add the demands of agentic AI: automating pod-restart troubleshooting, syncing communication between the scheduler and autoscaler, and maturing how we distribute inference across a cloud-native stack.

The other half goes deeper into what we need to look at closely in Kubernetes environments: What context’s missing, what slips through the gaps in metrics, and whether the AI agents you already use are really worth their salt as SREs.

Let’s get into it.

# HPE on automating pod restarts in AI development

As more enterprises turn to Kubernetes for large-scale AI and machine learning jobs, they’re hitting a common obstacle: pod restarts. This is something that [HPE](https://www.hpe.com/) has noticed as customers utilize its [HPE Private Cloud AI](https://www.hpe.com/us/en/products/private-cloud/pcai.html) (PCAI) to host long-running [AI/ML workloads](https://thenewstack.io/kagent-kubernetes-ai-agents/) on inherently ephemeral container-based infrastructure like Kubernetes.

*Hewlett Packard Enterprise (HPE) is a presenting sponsor of Road to KubeCon.* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *helps IT organizations modernize infrastructure, streamline operations, and accelerate AI initiatives across hybrid, multi-vendor environments.*

According to HPE system software engineer [Guoping Jia](https://www.linkedin.com/in/guoping-jia-934a6820?originalSubdomain=fr), Kubernetes provides some troubleshooting commands out of the box, but it still requires extensive manual investigation. “This operational workflow does not scale effectively in PCAI’s large-cluster environment,” [writes Jia on the HPE blog](https://developer.hpe.com/blog/automating-kubernetes-pod-troubleshooting-in-hpe-private-cloud-ai/).

His solution involves smarter automation for troubleshooting, using an open-source Kubernetes troubleshooting tool, [k8s-pod-restart-info-collector](https://github.com/airwallex/k8s-pod-restart-info-collector), to automatically gather details and send diagnostic information straight to a Slack channel. It’s one helpful strategy to improve usability for Kubernetes operators.

## Will the scheduler and autoscaler unite?

There’s been a lot of talk recently about how Kubernetes is evolving to meet AI’s new demands. This week, [AWS](https://aws.amazon.com/) senior software development managers [Sajjan Gundapuneedi](https://www.linkedin.com/in/sgundapu/) and [Neelendra Bhandari](https://www.linkedin.com/in/neelendrabhandari/) weighed in with [this blog post](https://www.cncf.io/blog/2026/10/19/how-ai-workloads-are-reshaping-kubernetes-autoscaling/) on how AI is reshaping Kubernetes autoscaling.

The core problem they highlight is friction between the scheduler, which places pods on existing nodes, and the autoscaler, which adds new ones, when managing GPU accelerators on Kubernetes. Often the two sides aren’t on the same page, leaving pods pending and pricey GPUs sitting idle. Capacity reservations, device topology, and GPU sharing complicate things further.

> “A scarce accelerator is only as useful as the agreement between the loop that schedules it and the loop that provisions it.”

“A scarce accelerator is only as useful as the agreement between the loop that schedules it and the loop that provisions it,” the authors write. “Inference is what makes this pressing rather than academic, since bursty serving and agentic workloads have no patience for a cold node.”

To them, solutions are already taking shape: [dynamic resource allocation](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/) (DRA)-aware autoscalers, [workload-aware scheduling](https://kubernetes.io/blog/2026/09/08/kubernetes-v1-37-advancing-workload-aware-scheduling/), and a companion mechanism, [provisioning requests](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/proposals/provisioning-request.md), to bridge the two sides. Still, they expect the autoscaler to grow into “a more scheduler-aware partner.”

Deeper integration is underway, too. A public proposal in the [SIG-Autoscaling group](https://groups.google.com/g/kubernetes-sig-autoscaling/c/CzuCD--BETM) sketches APIs that would let the two loops talk directly, so the scheduler could see capacity that could be provisioned, express placement preferences across it, and request it explicitly.

## Distributed AI inference grows up with llm-d v1.0 release

On Tuesday, at [PyTorch Conference North America](https://events.linuxfoundation.org/pytorch-conference-2026/), the CNCF sandbox project llm-d [reached v1.0](https://llm-d.ai/blog/llm-d-v1.0-state-of-the-art-inference-ready-for-day-2). The project now bridges AI application developers in the [PyTorch ecosystem](https://pytorch.org/) and the production cloud-native stack.

[Carlos Costa](https://www.linkedin.com/in/carlos-costa-9b9b1a1/), co-founder and lead maintainer of llm-d, and a distinguished engineer on IBM’s hybrid cloud platform for AI, says the v1.0 release signals maturity.

“This is the moment open source AI serving crosses from experimental projects into dependable infrastructure you can build on,” Costa tells *The New Stack*. Whereas earlier versions focused on proving state-of-the-art performance, v1.0 is about sustaining that performance in production, he adds.

llm-d has already seen plenty of use at [Tesla](https://llm-d.ai/blog/production-grade-llm-inference-at-scale-kserve-llm-d-vllm), AWS, [Oracle](https://blogs.oracle.com/ai-and-datascience/llm-inference-at-scale-with-llm-d-on-oci), Google, and beyond. Costa adds that [a recent IBM Research demonstration](https://www.ibm.com/downloads/documents/us-en/17f55bd44d44b0e3) found that an agent factory exploring quantum error correction hardware ran at 11.5x lower inference cost on open models with llm-d than on an all-proprietary configuration.

“This demonstration shows where llm-d really shines: agentic workloads,” he says, adding that it absorbs bursty agentic traffic and, in IBM’s test, pushed cache reuse to about 98%.

## From building models to operating frontier intelligence at scale

For a taste of the type of discussion to expect at KubeCon NA, let’s briefly visit the East. [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/), CTO at CNCF, set the stage very well at last month’s KubeCon + CloudNativeCon + OpenInfra Summit + PyTorch Conference China 2026 in Shanghai, in the talk [Operating Frontier Intelligence at Scale](https://www.youtube.com/watch?v=EyY90x3Z1GE) with Xiao Zhang.

As he puts it, it’s not just about models anymore. It’s about putting them all to work. “AI is essentially moving from just purely about building the greatest models [to] how do we actually make this run at scale, stitch it all together and run in different types of environments,” says Aniszczyk.

Cloudflare CEO Matthew Prince [recently declared](https://www.computing.co.uk/news/2026/ai/bot-traffic-overtakes-humans-online) that bot traffic, driven by AI agents, has passed human traffic online for the first time. Aniszczyk says that shift is putting tremendous pressure on systems, pointing to [recent GitHub outages](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/). As inference becomes the predominant workload, everything shifts.

> “It’s the craziest kind of technology change that I’ve seen probably in my career.”

This shift is causing all sorts of side problems, he notes, from building new infrastructure to building more data centers to ensuring enough power is available. “It’s the craziest kind of technology change that I’ve seen probably in my career,” says Aniszczyk.

Still, he’s an optimist, framing it as a fun problem and challenge for the cloud-native community to tackle together.

Plenty of AI site reliability engineer (SRE) platforms are emerging. But according to [Roy Libman](https://www.linkedin.com/in/roylibman/), CPO, [Radar](https://github.com/skyhook-io/radar) ([Skyhook.io](http://skyhook.io)), your next SRE hire might be right under your fingertips: the AI coding agent you already use. The trick is giving it the right context.

“The coding agent your engineers use, whether that’s Claude Code, Codex or Cursor, can already investigate a Kubernetes cluster,” writes Libman [on the CNCF blog](https://www.cncf.io/blog/2026/10/21/before-you-evaluate-an-ai-sre-give-your-existing-agent-context/). “What it usually lacks is context: what’s failing right now, and what changed before it broke.”

In his benchmark of 50 injected faults on a live cluster, Claude Code, given read-only context through MCP tools, diagnosed slightly more accurately than with shell and kubectl access. The bigger difference was speed: with context, it reached a correct diagnosis within two minutes on 86% of faults, versus 60% with a shell.

It’s an interesting sign that context is king for diagnosing complex errors, and that you might not need to shell (pun intended) out for another AI subscription just to triage issues.

# Industry take: what goes undetected in Kubernetes

A [previous Road to KubeCon](https://thenewstack.io/opentelemetry-prometheus-observability-interoperability/) asked what’s still missing with OTel and Prometheus. Well, one gap is state that isn’t a time series, like slowlog entries, client lists, and access control list (ACL) changes, shares [Kristiyan Ivanov](https://www.linkedin.com/in/kristiyan-i-8b3b5671/), former engineering manager at [Redis](https://redis.io/), current contributor to [Valkey](https://valkey.io/), and founding CTO of [BetterDB](https://www.betterdb.com/). “These get lost between scrapes,” he tells *The New Stack*.

> “Metrics count, but they don’t explain.”

Metrics count, but they don’t explain.” According to Ivanov, much goes undetected in Kubernetes because [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/ "Valkey") and Redis keep evidence in in-memory buffers, which Prometheus reduces to lengths and counters. “Kubernetes makes this even worse in several ways,” he says, noting that pod restarts, failovers, and ephemeral pod IPs worsen tracking.

“Almost everything in the ecosystem is an INFO scraper,” he says. “Missing across the board: durable history across restarts and failovers, attribution to a service or ACL user, an audit trail of ACL and config changes, and aggregation across shards.”

Emerging approaches are helping cloud operators see these gaps. He points to improvements in Valkey’s detection capabilities and OpenTelemetry eBPF Instrumentation to enable granular tracing. But eBPF can’t see evictions, ACL denials, or configuration changes, he says. Those require engine-level collection.

*As Kubernetes evolves, so do the demands on the teams running it. Presenting sponsor* [*HPE*](https://www.hpe.com/us/en/products/software.html) *helps teams address that complexity with software spanning virtualization, cloud management, observability, and automation.*

## Half can’t measure AI agents effectively

Eighty-seven percent of respondents say monitoring AI is a priority, yet over half admit they can’t effectively measure AI quality, like LLM response quality, or control AI costs, found [Splunk State of Observability 2026](https://www.splunk.com/en_us/pdfs/gated/ebooks/state-of-observability-2026.pdf), which surveyed 2,050 ITOps and engineering professionals and was released Oct. 20.

The report also found 83% are concerned about the unintended consequences of AI agents. This tracks with agentic AI’s tendency to take unexpected actions and create bursty traffic patterns, both of which are driving major infrastructure changes.

“Most companies will soon have far more agents at work than people,” said Jeetu Patel, president and chief product officer at Cisco, in the [press release](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m10/splunk-state-of-observability-2026-avoiding-the-hidden-costs-of-ai-agents.html). Monitoring AI is also driving more collaboration between observability and security teams, according to 81% of respondents.

## More updates from the cloud-native universe

The excitement around cloud native never sleeps. Here are a few more community, project, and vendor updates from the past week or so.

## One more stop on the Road to KubeCon

*Road to KubeCon is an eight-part series presented by HPE. Before you go, explore how* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *helps IT teams do more with less complexity.*

This series is almost over — only one edition remains.

We’ll be here next week to round things off with a special sign-off for Road to KubeCon. In the meantime, you can catch up on previous editions in the [Road to KubeCon archive](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/).

Bill Doerrfeld, the writer of this series, is open to community pitches. Feel free to share interesting takes, new releases, or tips on the best dive bar in Salt Lake City.

He accepts direct messages on [LinkedIn](https://www.linkedin.com/in/doerrfeldbill/), or you can reach him through his [personal contact page](https://www.doerrfeld.io/contact).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/12/b0ce81f3-cropped-5f5868db-nick-luchessi-2-600x600.png)

Nick Lucchesi serves as the editor-in-chief of The New Stack, where he directs editorial strategy and oversees coverage of the technologies and professionals driving software development, deployment and management at scale. Before joining The New Stack, Lucchesi held the position...

Read more from Nick Lucchesi](https://thenewstack.io/author/nick-lucchesi/)

[![](https://cdn.thenewstack.io/media/2024/02/96a1456d-cropped-e7e1c083-bill-doerrfeld.jpg)

Bill Doerrfeld is a tech journalist and API thought leader. He is the editor-in-chief of the Nordic APIs blog, a global API community dedicated to making the world more programmable. He is also an active contributor to a handful of...

Read more from Bill Doerrfeld](https://thenewstack.io/author/bill-doerrfeld/)