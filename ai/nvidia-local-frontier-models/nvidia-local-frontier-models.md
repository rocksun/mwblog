<!--
title: “我们热衷于两者兼得的世界”：Nvidia如何看待本地模型与前沿模型的关系
cover: https://cdn.thenewstack.io/media/2026/07/45a2a83b-img_0484-scaled.jpg
summary: 本文介绍了Nvidia高管Joey Conway的观点，主张企业应结合本地开源模型与前沿云端模型，利用路由技术实现任务分层，从而降低成本、提升效率，并确保数据安全与隐私控制。
-->

本文介绍了Nvidia高管Joey Conway的观点，主张企业应结合本地开源模型与前沿云端模型，利用路由技术实现任务分层，从而降低成本、提升效率，并确保数据安全与隐私控制。

> 译自：["We love the world where we can use both": How Nvidia thinks about local and frontier models](https://thenewstack.io/nvidia-local-frontier-models/)
> 
> 作者：Frederic Lardinois

那些小到足以在你桌面设备上运行的模型正变得越来越出色，因此，一个有趣的问题不再是“你是否能运行它们”，而是“你能用它们做什么”，以及“组织如何从它们身上获得最大价值”。

Nvidia 生成式 AI 软件高级总监 [Joey Conway](https://blogs.nvidia.com/blog/author/joeyconway/) 在接受 *The New Stack* 采访时表示，本地模型和开源模型正越来越多地与前沿模型协同工作，通常在中间会使用一个 [路由器 (router)](https://thenewstack.io/cursor-ramp-meta-model-router/) 来决定使用哪一个，以及组织如何根据自身需求调整这些开源模型。

> “我们热衷于这样一个世界：我们可以同时使用前沿模型和开源模型。” —— Joey Conway, Nvidia

## 模型系统

Conway 对 *The New Stack* 表示，任务的复杂性各不相同，处理这些任务的模型也应有所不同。他指出了早期的开放推理模型，它们会通过繁琐的推理过程来解决简单问题，反复权衡数字逻辑和内存，仅仅是为了算出 2 加 2 等于几。“我只会直接说等于 4，”他说。

“能够将那些简单的事情路由到快速的本地模型，并将困难的事情路由到更复杂的模型，”Conway 说，这样可以“以更低的成本和更短的完成时间获得更好的结果。”

这与大多数人想象中由一个大模型处理所有事情的画面完全不同。在他的设想中，你构建的是一个专家团队。“你会有专门的智能体，它们因为每天专注于特定的任务而变得非常擅长这些任务，”他说，“而且它们在处理这些任务时会变得越来越好。”

对于用户来说，这一切都是不可见的。“感觉就像是一个统一的界面，”Conway 说，“但在该界面背后，将会有各种各样的模型处理各种各样的任务。”

实现这一目标主要是一个路由问题，Conway 表示，目前这还处于早期阶段。Nvidia 目前的贡献位于堆栈的底层，例如在其开源的 Dynamo 等推理服务软件中，该软件会将每个查询引导至最近处理过该查询的 GPU。至于哪个模型最适合哪项工作，Nvidia 将其留给更广泛的路由器领域，其中一些路由器本身就是模型，它们会权衡预算、延迟和模态。但 Conway 也表示，Nvidia 不排除在不久的将来会自行构建更多此类路由功能。

Nvidia 提到了与 LangChain 的合作，其 Deep Agents harness 运行在 [Nemotron 3 Ultra](https://thenewstack.io/nvidias-best-model-is-now-live/)（Nvidia 拥有 5500 亿参数的开源模型）上，在业务任务方面与顶尖的闭源模型表现持平，且 [成本降低了高达 10 倍](https://thenewstack.io/open-weight-models-frontier-costs/)，正如 Conway 所指出的。这不需要重新训练；收益完全来自对其周围环境的调整：即提示词、工具描述和中间件。

你短期内不会在桌面上运行 5500 亿参数的模型，但只要你有足够强大的硬件，在本地运行相对较大的模型现在已成为一种真正的可能性。对于企业而言，在数据中心建立一组加速器也不便宜，但这意味着拥有完全的控制权，且不会有意外的 Token 费用账单。

## 将 AI 带到数据所在地

自行运行模型可以节省资金，但 Conway 认为控制权更为重要。企业已经决定了数据存放在哪里以及交给哪些外部供应商，而开源模型赋予了它们更大的控制权。“将 AI 迁移到数据所在地，”他说，“或者将 AI 迁移到员工身边。”

企业希望将数据——尤其是知识产权——保留在内部，Conway 认为经过微调的开源模型正是存放它们的地方。“这就好比是一个员工，”他说，“你雇用了他们，他们就是你公司的一部分。”

本地部分运行在诸如 Nvidia 的 [DGX Spark](https://thenewstack.io/nvidia-dgx-spark-the-new-stack-developers-guide/) 等硬件上，这是一款售价 4699 美元的 Grace Blackwell 机器，拥有 128GB 统一内存，无需离开你的桌面即可处理高达约 2000 亿参数的模型。（此外还有 [DGX Station](https://www.nvidia.com/en-us/products/workstations/dgx-station/)，其体积更大、价格更高，拥有 748GB 内存，可运行更大的模型。）

“这就像是一个系统就在你身边，”Conway 说，在这个系统中“你无需考虑网络延迟。”为了安全地运行这些智能体，Nvidia 提供了 [NemoClaw](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/)，这是一个参考堆栈，它将像 [OpenClaw](https://thenewstack.io/openclaw-hermes-agent-harness/) 这样的开源智能体工具包封装在名为 OpenShell 的沙箱中，并配备了策略控制和本地 Nemotron 推理功能。

当你需要更强大的能力来处理更广泛的问题时，你可以使用云端的前沿模型。对于 Nvidia 来说，这都是好消息：无论是在你的桌面上还是在云端，模型系统总是运行在它的芯片上。