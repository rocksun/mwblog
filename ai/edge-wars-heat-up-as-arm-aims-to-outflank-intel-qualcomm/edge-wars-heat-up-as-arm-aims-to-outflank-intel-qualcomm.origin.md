# Edge Wars Heat Up as Arm Aims to Outflank Intel, Qualcomm
![Featued image for: Edge Wars Heat Up as Arm Aims to Outflank Intel, Qualcomm](https://cdn.thenewstack.io/media/2025/02/53e2e33e-getty-images-uyhsmgcshs8-unsplash-1-1-1024x683.jpg)
Chip designer [Arm](https://www.arm.com/) has a new [edge AI](https://thenewstack.io/edge-ai-how-to-make-the-magic-happen-with-kubernetes/) platform optimized for the [Internet of Things (IoT)](https://thenewstack.io/edge-computing/) that expands the size of AI models that can run on edge devices, includes a powerful new CPU, and enables developers to integrate more easily with popular AI frameworks.

It’s the first such platform based on the company’s v9 architecture and boasts numbers such as an eight-fold improvement in [machine learning](https://thenewstack.io/use-these-tools-to-build-accurate-machine-learning-models/) performance over Arm’s previous platform and a 70% improvement in [IoT](https://thenewstack.io/enabling-ai-in-iot-apps-with-a-cloud-to-edge-database/) performance.

Arm’s new platform marks at least the third move by a chip player this week to expand their presence at [the edge](https://thenewstack.io/what-the-heck-is-the-edge-and-why-should-you-care/), where the push is on to bring as much compute power, AI capabilities, data processing and analysis tools, and security features to where much of the data today is being created.

![](https://cdn.thenewstack.io/media/2025/02/e636c22d-arm-platform-1-1.png)
Arm Platform

“We can only realize the potential of AI if we move it to the physical devices and the environments that surround us,” [Paul Williamson](https://www.linkedin.com/in/paulwilliamson/), senior vice president and general manager of Arm’s IoT line of business, told journalists. “In the world of IoT, it’s AI at the edge that matters most. Just a few years ago, edge AI workloads were much simpler than today. For example, they were focused on basic noise reduction or anomaly detection. But now the workloads have become much more complex and they’re trying to meet the demands of much more sophisticated use cases.”

## Getting Crowded at the Edge
[Intel](https://www.intel.com/content/www/us/en/homepage.html) this week introduced the latest additions to its Xeon 6 processor lineup, [including a system-on-a-chip (SoC)](https://thenewstack.io/edge-computing-gets-supercharged-with-intels-new-soc/) aimed at AI workloads at the edge and in networks and featuring integrated acceleration, connectivity, and security technologies to enable more workloads to run on fewer, smaller systems.
For its part, [Qualcomm](https://www.qualcomm.com/), known for its Snapdragon line of power-efficient chips for smartphones and PCs, introduced a new product brand portfolio — [Dragonwing](https://www.qualcomm.com/dragonwing) — for industrial and embedded IoT, networking, and cellular use cases ranging from energy and utilities to retail, manufacturing, telecommunications and supply chain.

“Leading edge AI, high-performance, low-power computing and unrivaled connectivity are built into custom hardware, software and service offerings designed for speed, scalability and reliability,” [Don McGuire](https://www.linkedin.com/in/donnymac/), senior vice president and chief marketing officer for Qualcomm, [wrote in a blog post](https://www.qualcomm.com/news/onq/2025/02/unveiling-the-qualcomm-dragonwing-brand-portfolio).

Much of this is driven by the enterprise adoption of the edge and IoT, connected devices that can range from massive industrial systems on manufacturing floors and smaller servers on distant oil rigs to autonomous vehicles, small sensors on windmills, and everything in between. And their numbers are growing, from 18 billion last year to [39.6 billion by 2033](https://www.statista.com/statistics/1183457/iot-connected-devices-worldwide/), according to one estimate.

## Powerful and Power-Efficient
Chip makers are building more powerful — and power-efficient — CPUs, GPUs, and NPUs (neural processing units) to run in small and more capable systems from hardware makers to meet the rapidly growing demand for more compute, data processing, and security capabilities where the data is being created to reduce the latency and costs that come with sending massive amounts of data to the cloud. Now AI models and workloads are making their way to the edge, and all this is driving developers to develop AI and other software for the edge.

“We’re seeing the need for higher performance and better efficiency to run the latest AI models, frameworks, and agents,” Arm’s Williamson said. “We’re seeing the need for improved security to protect the high-value software surrounding those. And we’re seeing the need for developers to be able to update, refine, upgrade their software once it’s been deployed in the field.”

In use cases like industrial automation, smart cities, smart homes, “the value of AI inferencing at the edge is becoming more and more evident,” he said.

## Enter the New Cortex-320 CPU
Arm’s new v9 platform is designed to address much of that, creating the capability to run AI models with over 1 billion parameters on a device. It includes the designer’s new highly efficient Cortex-A320 CPU and Ethos-U85 edge accelerator and performance-enhancing tools like Scalar Vector Extension (SVE) 2 for machine learning jobs, support for BFloat16 for new data types, and Matrix Multiply Instructions for more efficient AI processing.

The Armv9.2 architecture also better addresses security issues key to computing at the edge. Features include Pointer Authentication (PAC), Branch Target Identification (BTI) and Memory Tagging Extension (MTE) that enable more memory safety, control-flow integrity, and software isolation.

![](https://cdn.thenewstack.io/media/2025/02/740cad73-arm-compute-security-1.png)
Arm Compute Security

“This isn’t just an incremental step forward,” Williamson said. “It represents a fundamental shift in how we’re approaching edge computing and AI processing. We believe it’s going to drive forward that edge AI revolution for years to come.”

## Taking a More Direct Route
A key is that the latest platform removes the need for a microcontroller, he said, adding that the solution last year “focused on transforming network execution. This year, we’ve taken Ethos-U85 and we’ve updated the drive so that it can be driven directly by a Cortex-A320 without the need of a Cortex-M in the loop. This will improve latency and allow Arm’s partners to remove the cost and complexity of using these separate controllers to drive the NPU.”

![](https://cdn.thenewstack.io/media/2025/02/058d0d47-arm-direct-drive-1-1.png)
Arm Direct Drive

Memory is also a key improvement, with the Cortex-A320 adding support for larger addressable memory than Cortex-M platforms. The CPU is also more flexible at handling multiple tiers of memory access latency, enabling the platform to handle edge AI use cases that have larger neural networks and need software flexibility.

“The continued demand for hardware to efficiently execute larger and multi-model networks is pushing memory size requirements, so systems with better memory access performance are becoming really necessary to perform these more complex use cases,” he said.

## Developers Get Options
For software developers, flexibility is the word. Arm for years has been [building IoT development platforms](https://thenewstack.io/enabling-ai-in-iot-apps-with-a-cloud-to-edge-database/), continuing that last year with the [introduction of Kleidi](https://newsroom.arm.com/blog/arm-kleidi) aimed at accelerating AI development with Arm’s CPU architecture. The first offerings through the program were KleidiAI libraries for AI frameworks and KleidiCV for computer vision jobs. With the v9 platform comes Kleidi for IoT. KleidiAI already is integrated into IoT frameworks like Llama.ccp and ExecuTorch to speed up the performance of models like [Meta’s Llama](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/) and [Microsoft’s Phi-3](https://thenewstack.io/copilot-pcs-understanding-microsofts-evolving-ai-pc-stack/).

It delivers as much as 70% improvement to the Cortex-320 when running Microsoft’s Tiny Stories dataset on Llama.ccp, according to Arm.

In addition, Cortex-A320 can run applications that use real-time operating systems, like Free RTOS and Zephyr, Williamson said. That said, through Arm’s A-Profile architecture there also is out-of-the-box support for Linux and portability capabilities for Android and other rich Oses.

![](https://cdn.thenewstack.io/media/2025/02/a7e4d797-arm-developers-1.png)
Arm Developers

“This brings unprecedented levels of flexibility and allows you to target multiple market segments, applications, or operating system offerings that our partners provide and gives you superb choice when you’re thinking about roadmaps for future products,” he said. “For developers working on Linux, they can easily and quickly deploy that rich operating system on the A320. That’s going to save them time, money and effort, leading to faster time-to-market for them and their products.”

Developers can take [PyTorch](https://thenewstack.io/why-pytorch-gets-all-the-love/) applications at high-level environments and deploy them at the edge via the accelerations in the Cortex-A320 CPU.

“We also allowed, with the implementation of the direct connect of the neural processor to the A-Class core, the ability for them for the first time to directly address the same memory system as the AI accelerator for these sorts of always-on tasks, which will make that development easier as well,” Williamson said.

With all that, “you will see some interesting, completely new configurations from people stretching the boundary of what would have previously been done in a microcontroller but also giving Linux-based developers optimized performance,” he said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)