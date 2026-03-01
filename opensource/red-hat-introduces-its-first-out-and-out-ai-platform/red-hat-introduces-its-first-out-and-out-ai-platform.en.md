[Red Hat](https://www.redhat.com/en) has been deploying AI in the enterprise for some time. For example, [Red Hat Enterprise Linux (RHEL) now comes ready to do AI work](https://thenewstack.io/red-hat-enterprise-linux-10-an-ai-driven-quantum-ready-platform/); [Red Hat has its own inference engine](https://thenewstack.io/red-hats-ai-platform-now-has-an-ai-inference-server/); and the company offers [AI-enabled sysadmin tools](https://thenewstack.io/red-hat-goes-all-in-on-ai-powered-lightspeed-system-admin-tools/).

Now, Red Hat is positioning itself as a full-stack AI platform vendor. The IBM-owned Linux powerhouse is doing this with a new [Red Hat AI Enterprise (RHAE)](https://www.redhat.com/en/products/ai/enterprise) suite and a jointly engineered [Red Hat AI Factory](https://www.redhat.com/en/about/press-releases/red-hat-ai-factory-nvidia-accelerates-path-scalable-production-ai) with NVIDIA.

**Red Hat AI Enterprise**

RHAE is a new integrated AI platform designed to deploy and manage models, agents, and applications across hybrid environments using RHEL and OpenShift as its foundation. Red Hat pitches it as a “metal-to-agent” stack that unifies the AI lifecycle, enabling IT to manage AI like any other enterprise system rather than isolated pilots that never reach production.

The platform bundles high-performance inference, model tuning and customization, and agent deployment and management, with support for “any model, any hardware, any environment” as long as it can be layered on top of Red Hat’s Linux and Kubernetes platforms. Red Hat argues that this approach offers a more consistent, security-hardened environment for running AI at scale, using the same tools and processes enterprises already have around OpenShift.

This is all part of the usual Red Hat integrated stack approach.

Alongside AI Enterprise, Red Hat is shipping [Red Hat AI 3.3](https://www.redhat.com/en/about/press-releases/red-hat-launches-red-hat-ai-enterprise-deliver-unified-ai-platform-spans-metal-agents?intcmp=RHCTG0260000475259). The release adds compressed, production-ready versions of models such as Mistral-Large-3, Nemotron-Nano, and Apertus-8B-Instruct via the OpenShift AI Catalog. It also supports newer models like Mistral 3 and DeepSeek-V3.2, as well as multimodal upgrades, including faster Whisper speech processing and enhanced tool calling for agentic workflows.

AI 3.3 also introduces a technology preview of models-as-a-service, giving internal users self-service access to privately hosted models via an API gateway, standardizing how AI is consumed within large organizations.

On the hardware side, Red Hat is broadening support to include generative AI on Intel CPUs for small language models, expanding certification for NVIDIA’s Blackwell Ultra GPUs and AMD’s MI325X accelerators, and adding internal GPU-as-a-service features such as automatic checkpointing to prevent long-running jobs from losing work.

To address governance and software supply chain concerns, Red Hat is adding a new AI Python Index as a trusted repository of hardened versions of key AI tools. These tools include Docling, an IBM-developed open-source toolkit for converting unstructured documents into machine-readable formats for model training, and SDG Hub, a framework for building synthetic data generation pipelines used to fine-tune large language models.

The company is also tightening AI observability and safety with more detailed telemetry across workloads and a tech preview of integrated NVIDIA NeMo Guardrails to enforce policy and alignment in AI interactions.

**Red Hat AI Factory**

This is a good time to also introduce the Red Hat AI Factory with NVIDIA. This is a direct follow-up to Red Hat’s recent [release of a customized RHEL for NVIDIA’s Vera Rubin AI Platform](https://thenewstack.io/red-hat-customizes-rhel-for-nvidias-vera-rubin-ai-platform/). This new co-engineered software platform partners RHAE up with NVIDIA AI Enterprise to create what the companies describe as an end-to-end AI stack optimized for large-scale deployments. 

The AI Factory is aimed squarely at enterprises trying to move from ad hoc AI projects to “industrial-scale” production systems. It’s meant to help operations teams manage both conventional infrastructure and AI-specific demands, from provisioning and GPU orchestration to model performance and security, under a single umbrella.

This joint platform focuses on three main themes: time-to-value, performance and cost, and enterprise security posture. For faster deployment, customers get streamlined workflows and immediate access to pre-configured models, including IBM’s indemnified Granite family as well as NVIDIA Nemotron and NVIDIA Cosmos open models delivered via NVIDIA NIM microservices, with NVIDIA NeMo available for enterprise data tuning.

On the performance side, the AI Factory relies on Red Hat’s inference stack, powered by vLLM, the popular open-source inference engine, and NVIDIA technologies such as TensorRT-LLM, Dynamo, and the BlueField data processing unit. This is coupled with built-in observability to help organizations meet strict service-level objectives and reduce AI total cost of ownership. 

[Chris Wright](https://www.linkedin.com/in/chris-wright-b733851/), Red Hat CTO, describes the AI Factory with NVIDIA as part of a broader shift from AI experimentation to “industrial-scale, enterprise-wide production,” arguing that managing the entire AI computing stack with the same rigor as core IT platforms is now a necessity for large organizations. In both cases, Red Hat is betting that its long-standing expertise in hybrid cloud infrastructure gives it an edge as enterprises seek to standardize AI across multiple environments.

Red Hat is also lining up ecosystem support, with players such as Cisco, Dell, Lenovo, Supermicro, TD SYNNEX, and WWT signaling plans to deliver validated infrastructure and channel offerings around AI Enterprise and the AI Factory. Their role is to package Red Hat’s software with AI-optimized hardware and services so customers can treat AI as a standard enterprise workload rather than a bespoke science project. So, if you like the idea of a single AI software stack based primarily on NVIDIA hardware, boy, does Red Hat want to talk to you. 

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)