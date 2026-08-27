[Perplexity](https://www.perplexity.ai/hub) 与 Nvidia 合作，将其代理 AI 助手 [Computer](https://www.perplexity.ai/products/computer) 带到了桌面端，命名为 Portable Computer。

尽管目前人们对本地 AI 的兴趣高涨，但入门门槛依然很高，而且价格昂贵。Portable Computer 确实降低了上手难度，但要运行它，你需要合适的硬件设备。

## 本地 AI 的硬件账单

目前，主要有两个选择。最简单的方法是购买 Nvidia 的 DGX Spark 工作站并运行 DGX OS。如果你拥有运行 Ubuntu 系统且采用 ARM 或 x64 架构的传统 PC，并且配备了至少 24GB 显存的 Nvidia RTX 显卡，同样可以运行。

一台 DGX Spark 售价高达 4,800 美元，即使是配备 24GB 显存的旧款 RTX 3090 显卡，目前的成本也远超 1,500 美元。

由于 [RAMmageddon](https://en.wikipedia.org/wiki/2025%E2%80%93present_global_memory_supply_shortage)，短期内硬件价格不太可能下降。

将 Computer 带到桌面端不仅是把云端模型替换为小型模型那么简单。它需要具备本地读取和编辑文件、运行 shell 命令以及处理 PDF 的能力，同时还需要连接外部服务。所有这些都需要一个用于运行 Agent 的本地沙盒。

Nate Kupp（Perplexity 计算机企业与基础设施副总裁）告诉 *The New Stack*，为了适配这些小型模型，团队不得不“重新审视了整个技术栈”。他说，公司复用了 Computer 的许多功能，但针对本地硬件修改了框架和模型配置。

Kupp 表示，框架设计占据了大部分工程工作量。模型仍需规划任务、调用工具、管理文件并执行多步骤任务，且参数量远小于 Perplexity 云服务中使用的庞大模型。

Perplexity 表示，负责维护 Agent 循环的调度器是确定性代码，而非另一个 AI 模型。在该系统中，本地模型提出行动方案，而调度器负责汇编上下文、执行策略，并在 OS 级沙盒中运行已批准的工具调用。

## 本地框架内部

据该公司介绍，该沙盒限制了进程、文件系统路径和网络访问。如果沙盒不可用，框架会在进行任何工具调用前自我禁用，而不是在沙盒外运行它们。

该框架的设计也充分考虑了模型的实际上下文限制。Perplexity 表示，Qwen3.8-27B 支持 260,000 个 token 的上下文窗口，但在超过 100,000 个 token 后开始变得吃力。因此，Portable Computer 保持核心提示词和工具集精简，仅在需要时加载额外技能。

此外，Perplexity 还将常用的连接器转换为命令行工具，而不是直接向模型公开其大型模型上下文协议 (MCP) 定义。

最近几周，框架对于 Agent 性能的重要性日益凸显，Kupp 在简报中也提到了这一点。

在相同的 Qwen3.8-27B 基础模型和 DGX Spark 硬件上，Computer 在 Perplexity 内部的 53 项本地知识工作基准测试中得分 82.6%，相比之下 Pi 为 77.6%，Hermes 为 74%。在涵盖图表、布局、表格、文本和格式的 100 项任务基准测试 ParseBench-100 中，Computer 得分 65.1%，而 Hermes 仅为 34.6%，Pi 为 13.9%。

Perplexity 表示计划开源该内部基准测试。

## 当本地任务离开机器时

使用 Portable Computer，每个任务都从本地设备开始。如果本地模型无法完成某一步骤，它可以寻求云端模型的建议。Perplexity 表示，框架会选择相关上下文，标记潜在的敏感信息，向用户展示将要发送的内容，并在进行调用前征求批准。

云端模型返回文本指导，但无法直接访问设备的本地文件或工具。本地调度器保留执行控制权，并将建议整合到当前的本地运行中。

在一次演示中，Portable Computer 在 [Nvidia DGX Spark](https://thenewstack.io/nvidia-dgx-spark-the-new-stack-developers-guide/) 上查看了一文件夹的税务文件；在第二次演示中，本地 Agent 分析了一个 CSV 文件并将其结果发布到 Slack，展示了 Agent 跨越本地机器的能力。

Portable Computer 包含 Google Drive、Gmail、Slack 和 GitHub 的连接器。使用时，网页搜索和连接器调用会离开设备，而 Perplexity 表示模型推理和私有文档处理依然留在本地。

Perplexity 的核心论点是便利性和隐私。想要完成所有必要步骤的开发者本就可以将本地模型服务器与工具和执行环境结合起来。尽管如此，Kupp 认为 Portable Computer 是即开即用的。“你不需要折腾推理过程，”他说。

尽管名字相似，Portable Computer 并非 [Personal Computer](https://thenewstack.io/mac-mini-agent-infrastructure/)（Perplexity 用于处理本地文件和原生应用的 Mac 和 Windows 应用程序）。Portable Computer 在本地运行模型和框架，但 Kupp 表示“我们目前还没做到‘计算机使用’（computer use）级别”。

## 从 Nvidia 开始

在发布时，用户可以在 [Qwen3.8-27B](https://thenewstack.io/qwen38-27b-local-inference/) 和 PPLX 27B（Perplexity 对该模型进行训练后的版本）之间进行选择。

Nvidia 的 [Nemotron 3.5 Lightning](https://thenewstack.io/nvidia-nemotron-lightning-switchyard/) 将在稍后推出。用户也可以使用自己的模型和推理服务器。

遗憾的是，即使你拥有一台性能非常强劲的 Mac（或者正在预订新款 Mac），Portable Computer 目前也无法使用。不过，Windows 支持计划在 9 月跟进。

Kupp 表示：“目前，Perplexity 非常专注于 Nvidia 的 DGX 和 RTX 系列，”不过他也提到公司正在考虑其他硬件。

Portable Computer 将向 Perplexity Pro、Max、Enterprise Pro 和 Enterprise Max 的订阅用户开放。只要系统不需要连接 Perplexity 的云端模型，本地完成的任务就不会消耗使用配额。