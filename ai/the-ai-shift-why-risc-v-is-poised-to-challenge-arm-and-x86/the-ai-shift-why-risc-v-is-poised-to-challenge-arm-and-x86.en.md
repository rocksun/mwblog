The [RISC-V](https://thenewstack.io/risc-v-finds-its-foothold-in-a-rapidly-evolving-processor-ecosystem/) standard has evolved and matured to the extent that performance drawbacks have largely disappeared compared with the long-tried and tested – and much pricier – Arm and x86 processors.

This is great news for those looking for a more cost-effective way to program their chips or for developers who want to optimize their chips’ CPU performance—not only because of the significant costs associated with Arm licensing but also because of the freedom to implement instruction sets without having to obtain Arm’s permission each time.

This, combined with its inherent vector capabilities, is why RISC-V is particularly well-suited for AI, where multiple processes need to run in parallel—a workload for which RISC-V is especially well-adapted.

Perhaps one of the most understated and lesser-known watershed moments in AI at the chip level was last year’s communication of [Nvidia’s plans](https://thenewstack.io/nvidias-hardware-roadmap-and-its-impact-on-developers/)—specifically, that [CUDA](https://thenewstack.io/nvidia-making-radical-changes-to-cuda-after-nearly-20-years/) would support RISC-V instruction sets. Also last year, the Linux kernel updates implementation drivers and patches for RISC-V, adding a final missing essential element in what should be a long-run open source push to migrate to open source RISC-V devices. [Canonical’s Ubuntu](https://thenewstack.io/canonical-extends-ubuntu-linux-support-for-up-to-15-years/) support RISC-V as well.

What this means is that developers and device makers can now program and implement RISC-V processors compatible with Linux incorporating instruction sets in conjunction with Nvidia CUDA GPUs in much the same way as they do with x86 and Arm processors. This represents a significant boost at a time when there is a shortage of relatively expensive CPUs and Arm processors, compared with the now cheaper RISC-V alternatives.

Nvidia has not commented extensively on this in its documentation or provided input in response to messages sent asking for clarification, but the development was widely reported by the [RISC-V International](https://thenewstack.io/open-source-risc-v-serving-a-side-of-software-with-chips/) organization.

As a caveat, although it is clear that this could be a boon for AI development—particularly for the large number of edge and embedded devices where RISC-V is well suited—Nvidia has not formally stated that this support is specifically intended as a major AI expansion strategy. That said, developers are now able to create and implement instruction sets at will for AI on Nvidia GPUs – without having to worry about Arm and x86 licensing and costs.

“AI frameworks are changing constantly, while CUDA dominates,” [Yuning Liang](https://archive.fosdem.org/2025/schedule/speaker/yuning_liang/), founder and CEO of RISC-V OEM [DeepComputing](https://deepcomputing.io/), told me. “New frameworks keep appearing. And amid all of this, software remains key.”

Engineers doing what they want on RISC-V processors is nothing like working with Arm and Intel or AMD licenses for CPUs. “In the old days, you couldn’t ask Intel to do anything. All you could do was be stuck with it. But now with RISC-V, you can use all your imagination, do whatever you like, and make the best out of it,” he said.

## Nobody saw this coming

Before the AI boom, before LLMs and the Google’s famous Tranformer research paper, “nobody saw this coming. “Before AI came, I had no idea where RISC-V high-performance SoCs would go,” Liang said. “Luckily AI came and so we are going all-in on AI.”

In the [RISC-V International 2025 annual report,](https://riscv.org/wp-content/uploads/2026/01/RISC-V-Annual-Report-2025.pdf) [Krste Asanović](https://www.linkedin.com/in/krste-asanovic/), chief architect, RISC-V, assessed status at the end of the year and what 2026 is bringing:

“In 2025 we took that effort further, launching targeted campaigns that articulate how RISC-V’s unique characteristics address specific challenges in specific vertical markets,” he said. “As a result, RISC-V is now firmly part of the vocabulary, roadmaps, and procurement choices of decision makers in key sectors. Today, we’re focused on a number of key verticals.

“In embedded & IoT we already have significant deployment. In data center and automotive, we see ever-growing interest in general-purpose RISC-V compute. Meanwhile, markets that are smaller in socket volume but demanding in capability, such as space and high-performance computing (HPC), are already providing outsized opportunities.

And then, of course, there is AI. “Alongside security, AI cuts horizontally across every vertical,”Asanović said. “There has been a sea change throughout 2025, and it’s safe to say that almost every new AI accelerator project I’ve seen is using RISC-V. This is no accident: we designed RISC-V from the beginning to support scalar, vector, and matrix computation, so it just works. The same cores can handle control and numeric workloads, scale across performance tiers, and evolve with AI. All the major industry players are starting to recognize that RISC-V will soon be the dominant open ISA. In so many vertical markets, we’ve moved past if. The conversation is now about how, when and where RISC-V will be adopted.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)