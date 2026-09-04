**Perplexity希望其AI代理能够利用更多存在于Mac内部的计算能力。**该公司于周二推出了混合计算（Hybrid Compute），这是一项新功能，允许 [Perplexity Computer](https://thenewstack.io/perplexity-portable-computer-nvidia/) 在强大的云端模型与直接在 Apple silicon 上运行的较小模型之间迁移同一任务的部分工作。

这一时机意义重大。混合计算推出的当天，恰逢 [John Ternus](https://www.linkedin.com/in/john-ternus-908257356/) 担任 Apple 首席执行官的第一天。Ternus 此前领导 Apple 硬件工程部门，并在公司从 Intel 处理器转向自研 Apple silicon 的过程中发挥了关键作用，他接替了担任 CEO 15 年的 Tim Cook。Perplexity 现在正押注于同样的硬件，将其转化为自主 AI 代理背后的基础设施的一部分。

任务从云端开始。当某一步骤涉及敏感信息时，Computer 可以将该部分工作转移到在 Mac 上运行的模型，而无需重新开始。

> 当某一步骤涉及敏感信息时，Computer 可以将该部分工作转移到在 Mac 上运行的模型，而无需重新开始。

## 隐私网关（Privacy Gate）先行检查

Perplexity 训练的隐私网关（Privacy Gate）会在 Mac 本地运行，并寻找敏感信息，例如姓名、地址、账号和秘密。当它标记出某些内容时，用户可以决定任务的该部分是否应该保留在设备上。

用户可以在工作开始前审查系统想要保留在本地的内容，并确保它没有遗漏任何他们不想发送到云端的数据。他们还可以选择由哪个模型处理本地工作。

发布时，用户可以在 [Gemma E4B](https://thenewstack.io/google-gemma-local-ai/)、[Qwen3.6 35B-A3B](https://thenewstack.io/ollama-taps-apples-mlx/) 以及 Perplexity 自行微调的 Qwen3.6 35B 版本之间进行选择，后续还将计划支持更多模型。Perplexity 通过桌面应用处理安装过程，因此用户无需打开终端或自行设置模型。

## 本地 Token 不产生费用

一旦任务开始运行，应用程序会显示本地 CPU、GPU 和内存的利用率，以及消耗的 Token 数量。对于在 Mac 上本地运行的模型所生成的 Token，用户无需付费。除了隐私之外，这为 Perplexity 将工作转移到设备上提供了另一个理由，因为在本地运行模型也可以降低推理成本。（关于 [谁承担推理成本以及何时承担](https://thenewstack.io/openai-outcome-based-pricing/) 的问题正成为整个行业的一个竞争性议题。）

这是一种折中方案。Perplexity 在云端使用其能力最强的模型，而较小的模型则处理本地工作，因此将更多的任务保留在 Mac 上可以在牺牲一定能力的情况下提高隐私并降低成本。混合计算将选择权留给了用户。

> Perplexity 在云端使用其能力最强的模型，而较小的模型则处理本地工作，因此将更多的任务保留在 Mac 上可以在牺牲一定能力的情况下提高隐私并降低成本。

## 上下文跨越边界

更棘手的是，当任务的一部分转移到 Mac 上时，上下文会发生什么变化。云端模型仍然需要了解本地发生的事情，以便继续完成工作，同时又不能访问本应保留在本地的私密信息。

Perplexity 表示，Computer 可以将一个步骤从云端转移到本地模型，而无需重启任务或丢失上下文，并最终将云端和本地的工作合并为一个单一的结果。在公告中，它没有详细说明在这些环境之间到底传递了什么上下文，或者本地子代理产生的信息在返回更广泛的工作流之前是如何被过滤的。

本地子代理可以处理私密文件和数据，并在 Mac 上执行操作。用户还可以在 iPhone 上启动任务，并将本地工作移交给 Mac，而无需重新开始。

对于企业客户，Perplexity 增加了公司范围内的规则，规定哪些内容保留在本地，并记录每个设备传出的内容，从而将 [AI 代理面临的治理问题](https://thenewstack.io/enterprise-ai-agent-governance/) 降低到设备级别。

## DGX Spark 从本地开始

混合计算颠覆了 Perplexity 上周为 Nvidia 的 DGX Spark 引入的方法。DGX Spark 从本地开始，仅在获得许可的情况下才连接到前沿云模型，而 Mac 版本则从云端开始，并在需要时将工作转移到设备上。

在这两种情况下，代理编排器（agent harness）都会决定任务的每个部分在哪里运行。这种编排——[决定代理真正需要哪些工具和上下文](https://thenewstack.io/ard-agent-discovery-specification/)——随着代理获得对更多系统和数据的访问权限，正成为一个日益困难的工程问题。

## Apple silicon 成为代理栈的一部分

在本地运行如此多的代理任务仍然需要一台相当强大的 Mac。Perplexity 建议至少配备 32GB 统一内存、Apple silicon 和 macOS 15。该功能适用于 Pro 和 Max 订阅用户以及企业客户。

这些要求显示了当前本地 AI 的局限性。较小的模型可以在许多 Mac 上运行，但要让代理拥有足够的计算能力来处理有意义的工作，仍然需要相对高端的硬件。

随着 Mac 在运行更大模型方面变得越来越好，这种情况可能会改变。对于 Ternus 来说，更大的问题是现在发生在云端的人工智能工作，最终会有多少转移到 Apple 销售的机器上。

> 对于 Ternus 来说，更大的问题是现在发生在云端的人工智能工作，最终会有多少转移到 Apple 销售的机器上。