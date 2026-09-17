**[Red Hat](https://thenewstack.io/red-hat-introduces-its-first-out-and-out-ai-platform/) released Red Hat AI 3.5 this week**, a move designed to let software engineering teams run AI with the same operational rigor as enterprise apps on [mission-critical](https://thenewstack.io/smarter-ai-for-critical-operations-why-data-matters/) infrastructure.

Echoing both the “pilots-to-production” and “single control plane for infrastructure, models, and agents” narratives playing out across much of the tech industry, Red Hat’s key move here seems to be its expansion of platform capabilities to run enhanced multi-tenancy for AI service providers.

Crucially, the new AI platform release is built to run AI use cases that require complete hardware-to-software isolation (needed when AI workloads have to wrangle [sensitive data](https://thenewstack.io/protect-sensitive-data-and-prevent-bad-practices-in-apache-kafka/), proprietary models, and regulated information), as well as handle [priority-aware service requests](https://arxiv.org/pdf/2503.09304?) (where mission-critical workloads execute in favor of lower-grade tasks) with native multi-tenancy on a shared [GPU infrastructure](https://thenewstack.io/vultr-nvidia-ai-infrastructure/).

Red Hat’s Senior Director of Product for Red Hat AI is [Tushar Katarki](https://www.linkedin.com/in/katarki/). He tells *The New Stack* that running enterprise AI without safety controls is “like driving a supercar blindfolded” in real terms.

“With [Red Hat AI 3.5](https://www.redhat.com/en/products/ai?sc_cid=RHCTE0250000437915&gclsrc=aw.ds&gad_source=1&gad_campaignid=22183537126&gbraid=0AAAAADsbVMShE5A5QHDrbm3iw5ib9zxpu&gclid=Cj0KCQjwh4TVBhCWARIsAG0czmpCwai8R3s0h7IB0SYbOJOQwdBghMJyUvUtl7Wil74eCImlFT54elIaAhyTEALw_wcB), we are delivering the operational guardrails, verifiable trust, and multi-tenant controls needed to run AI as a mission-critical service rather than an unpredictable experiment,” Katarki says. “You can’t scale what you can’t measure, and you certainly shouldn’t deploy what you can’t verify. By unifying pre-deployment safety benchmarking, real-time observability, and GPU resource management, we are giving platform teams the power to turn isolated AI pilots into a fully governed enterprise architecture.”

## Every GPU request now becomes a priority decision

Applied mathematician, data scientist, and fractional CMO [Joshua Estrin](https://www.linkedin.com/in/joshua-estrin-phd-37861217a/), Ph.D., tells *The New Stack* that Red Hat’s work is of the time and of the moment; primarily because “every GPU request now becomes a priority decision”, so one developer’s internal experiment cannot be treated with the same urgency as a financial close.

“Looking at the state of AI infrastructure players out there now, Red Hat has clearly seen that priority-aware multi-tenancy lets companies use expensive compute more efficiently, but efficiency without isolation is just a faster way to create a security and reliability crisis,” Estrin says.

> “Every GPU request now becomes a priority decision.”

He thinks that the winners in this market (he tags [Nvidia](https://thenewstack.io/palantir-nvidia-sovereign-ai/), [Nutanix](https://thenewstack.io/how-nutanix-is-taming-operational-complexity/), [Suse](https://thenewstack.io/suse-ai-infrastructure-kubernetes/) with [Rancher](https://thenewstack.io/can-rancher-deliver-on-making-kubernetes-easy/), [HPE Ezmeral](https://www.hpe.com/uk/en/products/software/ezmeral-unified-analytics.html) and [VMware Cloud Foundation](https://thenewstack.io/vmware-cloud-foundation-is-now-an-ai-native-platform/) under [Broadcom](https://thenewstack.io/broadcom-vcf-kubernetes-platform/) as usual suspects) will be the organizations that can “share capacity while still proving what happened where” in live production.

“That means proving whose workload actually executed and ran, who had access, what it cost, and what happens when demand spikes. Those answers rarely come from the infrastructure diagram; they get settled in the boardroom, usually after someone’s critical workflow has slowed down, but regardless, this sums up where AI infrastructure is now,” adds Estrin.

## What are the elevated multi-tenancy pain points?

To unpack what’s happening here, let’s remind ourselves that GPUs are expensive, obviously. As organizations move to live production use cases of agentic AI, they will want to maximize their GPU state’s ability to serve multiple workloads across multiple teams, multiple customers, multiple apps, and so on.

This all means that the breadth of AI infrastructure efficiency becomes the new agentic bottleneck.

The priority-aware services above for native multi-tenancy on shared GPU infrastructure are important right now; this function dynamically allocates GPU capacity based on workload priority. When lower-priority workloads can be run on spare (or cheaper) capacity (rather than separately provisioned GPU resources having to be spun up for lesser jobs), then everyone gets to go home earlier on Friday.

> “The breadth of AI infrastructure efficiency becomes the new agentic bottleneck.”

But that’s not all the balls being juggled here; Red Hat mentioned isolation too, and that’s a concurrently complex AI infrastructure discipline challenge. GPU compute resources managed through isolation techniques enable AI services to run without accessing or interfering with another service’s data, models, or compute environment.

In other words, this combines hardware consolidation with strong tenant isolation.

## What new Red Hat technologies are on offer?

Red Hat says this release lets developers verify models before deployment through [EvalHub](https://github.com/eval-hub), enabling risk-focused safety benchmarking and regulatory compliance certifications.

New observability dashboards give platform teams metrics for a real-time view of inference health, GPU utilization, and AI model performance. Non-admin users can access dashboards for per-user token consumption showback (another term for token tracking) and distributed inference workloads.

Also new is shared GPU control for multi-tenant inference. So-called “fair-share GPU scheduling” manages resource allocation across tenants, while priority-aware serving provides admission control and priority-based request routing to protect real-time inference. As suggested above. it also allows background workloads to use available capacity.

VP of product management at Nutanix, [Anindo Sengupta](https://www.linkedin.com/in/anindose/), tells *The New Stack* that running multi-tenant AI at scale does indeed require secure tenant isolation.

“The essential isolation is best achieved through virtualization,” Sengupta says. “For specialized at-scale AI workloads, the choice could be to run Kubernetes on bare metal. On top of that, to create real value, agents need access to both LLMs that run on containers and enterprise systems (databases, business systems, etc.) that run on traditional infrastructure. For hybrid AI to run efficiently, the platform must manage both these environments in a performant way, with a common operating model.”

## Observability & model-as-a-service showback

Built-in observability and MaaS showback in Red Hat’s latest release are present to provide per-user token metering, performance dashboards for models and agents, MLflow visual agentic tracing, and GPU utilization dashboards for operational and usage transparency.

For efficient GPU memory management, the general availability of CPU offloading and the developer preview of storage offloading allow models to handle longer conversations and larger documents without additional GPU hardware.

Red Hat AI Hub also introduces agent templates and starter kits with pre-configured reference implementations for common enterprise patterns, including code review, document processing, and research workflows.

> Red Hat is hoping its Red Hat AI 3.5 version release gets us to a state where GPU-based AI resources are viewed as a policy-controlled infrastructure pool.

## Power without interconnect bandwidth is botched.

As enterprise AI pilots succeed and initial results show some returns, IT teams must then address the need to deliver at scale. But scaling AI across the business demands the same operational rigor as any mission-critical infrastructure: verified safety before deployment, precise resource controls across shared GPU environments, governed agent behavior and transparent usage metrics.

[Yoram Novick](https://www.linkedin.com/in/yoramnovick/), CEO of sovereign AI edge cloud provider [Zadara](https://www.zadara.com/), has previously been [on the record](https://www.itpro.com/infrastructure/networking/why-networking-is-just-as-important-as-compute-in-ai-data-centers) on this exact topic. He has said that when teams need to scale AI, “Simply adding more GPUs without ensuring adequate interconnect bandwidth can lead to diminishing returns” in the modern AI era.

Overall, with its ability to direct priority-aware inference, tenant isolation, capacity sharing, and observability, Red Hat hopes its Red Hat AI 3.5 release gets us to a state where GPU-based AI resources are viewed as a policy-controlled infrastructure pool.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)