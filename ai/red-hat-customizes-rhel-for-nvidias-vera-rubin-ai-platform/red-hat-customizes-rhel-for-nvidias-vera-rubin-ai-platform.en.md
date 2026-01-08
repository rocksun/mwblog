Building on continual partnership work with the chip company, [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) has pledged to offer “Day 0” support for Nvidia’s newly-announced [Vera Rubin Platform](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer), when it arrives later this year.

The enterprise open source software company is aiming to close the release gap between the launch of Nvidia’s hardware platform and the general availability release of its own supporting stack of software, a custom version of its flagship operating system, Red Hat Enterprise Linux (RHEL), designed for Rubin.

Nvidia’s Vera Rubin platform is built to cut the costs of AI inference. It is built on a new CPU, GPU, and Digital Processing Unit (DPU), all of which are closely tied to other components.

## Hardware and Software on the Same Release Schedule

Both the platform and Red Hat’s software are expected in the latter half of 2026, according to a Red Hat spokesperson.

When Rubin comes to town, Red Hat repositories will have ready-validated Nvidia GPU OpenRM drivers and the CUDA toolkit.

Red Hat’s software will also be able to run AI lifecycles within the envelope of Nvidia’s newly unveiled [Confidential Computing](https://www.nvidia.com/en-us/data-center/solutions/confidential-computing/) security architecture, which provides cryptographic proof of workload protection.

In addition to RHEL, Red Hat will also release the [Red Hat OpenShift](https://thenewstack.io/red-hat-openshift-4-20-boosts-ai-security-hybrid-cloud/) platform for Kubernetes for Rubin, and the [Red Hat AI platform](https://thenewstack.io/choosing-the-right-red-hat-ai-solution-rhel-ai-vs-openshift-ai/) will expand support for distributed inference with Nvidia’s open source models on Red Hat AI Inference Server, Red Hat Enterprise Linux AI and Red Hat OpenShift AI.

## Introducing Vera Rubin

Nvidia CEO [Jensen Huang](https://www.linkedin.com/in/jenhsunhuang/) introduced [Vera Rubin](https://www.nvidia.com/en-us/data-center/technologies/rubin/) during in his keynote for the 2026 Consumer Electronics Show ([CES](https://thenewstack.io/ces-2025-worst-in-show-betas-for-a-dystopian-future/)). It is named after American astronomer [Vera Florence Cooper Rubin](https://airandspace.si.edu/stories/editorial/meet-vera-rubin), who identified dark matter as a thing that takes up most of our universe.

This platform tackles another difficult mission: Reducing the skyrocketing computer (and electricity use) costs of running large-scale [AI inference workloads](https://thenewstack.io/5-reasons-to-use-kubernetes-for-ai-inference/).

By engineering the components to work more closely together, Vera Rubin can reduce the inference token cost to train models by a factor of 10, while using 4 times fewer GPUs, compared with using the Nvidia [Blackwell platform](https://thenewstack.io/developers-can-now-uber-gpus-with-nvidias-lepton-platform/), traditionally used for such tasks, the company asserted.

The platform’s Ethernet photonics switch systems promise to deliver five-fold improved power efficiency as well.

Vera is the name of [the 88-core CPU](https://www.nvidia.com/en-us/data-center/vera-cpu/) for the platform, and Rubin is the name of the GPU, which [offers 50 PFLOPs](https://youtu.be/0NBILspM4c4?list=TLGGTaKMRZHNIn4wNjAxMjAyNg&t=9875) of mathematical crunch (5x offered by Blackwell). Further computational acceleration is also locked in with the [Nvidia BlueField-4 DPU](https://www.nvidia.com/en-us/networking/products/data-processing-unit/). These processing units are all closely intertwined with the [NVLink 6 Switch](https://www.nvidia.com/en-us/data-center/nvlink/), [Nvidia ConnectX-9 SuperNIC](https://www.nvidia.com/en-us/networking/products/ethernet/supernic/), and [Nvidia Spectrum-6 Ethernet Switch](https://www.nvidia.com/en-us/networking/ethernet-switching/) — all made with Nvidia chips.

## The Cost of Inferencing

As companies ramp up their AI efforts, they are finding that inferencing work, which is done most efficiently through GPUs, is getting more expensive.

This week, [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) (AWS) [hiked](https://www.theregister.com/2026/01/05/aws_price_increase/) the cost of its GPUs [by 15%](https://x.com/MuthaNagavamsi/status/2008339575346000252).

The cost of inferencing has indeed been on the minds of Nvidia executives. The company also inked a [$20 billion licensing deal](https://www.fierce-network.com/cloud/heres-why-nvidia-dropping-20b-groqs-ai-tech) with Groq for its inferencing and compiler technologies.

In his keynote, Nvidia’s Huang talked about the dramatic increase of inferencing that is taking place within AI systems even recently. Not only are the models themselves getting larger, but the amount of inference itself has skyrocketed. No longer is inferencing used to produce a single “one-shot” answer, but is a “thinking process” often involving multiple models and additional post-training.

So more inferencing is needed.

“You now have reinforcement learning, [which is] essentially the computer trying different iterations learning how to perform a task,” Huang said. “The amount of computation for pre-training. for post-training, for test time scaling has exploded as a result of that.”

“The efficiency gains in the Nvidia Rubin platform represent the kind of infrastructure progress that enables longer memory, better reasoning and more reliable outputs,” noted Dario Amodei, cofounder and CEO of Anthropic, in a statement.

In addition to Red Hat (which is owned by IBM), other companies that have pledged their support to the Rubin platform include:

AWS, Anthropic, [Cisco](http://cisco.com/?utm_content=inline+mention), CoreWeave, Dell, [Google](https://cloud.google.com/?utm_content=inline+mention), [HPE](https://www.hpe.com/us/en/ezmeral.html?utm_content=inline+mention), Lambda, Lenovo, Meta, Microsoft, Mistral AI, OpenAI, the [Oracle Cloud Infrastructure](https://www.oracle.com/developer?utm_content=inline+mention) (OCI), among many others.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)
[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)