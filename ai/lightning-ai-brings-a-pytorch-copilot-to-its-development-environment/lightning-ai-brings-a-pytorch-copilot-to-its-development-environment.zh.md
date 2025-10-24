[Lightning AI](https://lightning.ai/)，即致力于消除使用 [PyTorch](https://thenewstack.io/why-pytorch-gets-all-the-love/) 复杂性的 [PyTorch Lightning 项目](https://thenewstack.io/pytorch-lightning-and-the-future-of-open-source-ai/) 背后的公司，今天宣布在其商业产品中推出多项新工具和功能。这些更新应能让 AI 团队更容易在其端到端 PyTorch 平台上进行构建。

## PyTorch Lightning

开源的 [PyTorch Lightning 项目](https://github.com/Lightning-AI/pytorch-lightning) 是一个轻量级框架，它消除了大量 PyTorch 工作中的样板代码，同时使创建结构化的 PyTorch 项目变得更容易。

尽管 Lightning 是 Lightning AI 工作的核心，但该公司的平台远不止于此，它包括基于云的 Lightning Studio 开发环境（用于训练和部署模型）、基于 Jupyter 的笔记本环境、GPU 市场以及用于托管和构建 AI 和机器学习应用程序的基础设施服务。

## Lightning AI 更新

这些更新包括为其 Lightning Studios 和 Notebooks 环境提供新的 AI 代码编辑器，以及 Lightning Environments，后者本质上是沙盒化但可扩展的环境，用于探索、训练和扩展分布式 AI 工作负载。这些更新还包括支持 [Meta](https://about.meta.com/?utm_content=inline+mention) 专为 PyTorch 设计的 Monarch 分布式编程框架以及 Forge（Meta 的新型强化学习框架，它利用了 Monarch 的分布式基础设施）。

“我们的目标是让世界上每个开发者都成为 PyTorch 开发者，”Lightning AI 首席执行官兼 PyTorch Lightning 创建者 William Falcon 补充道。“无论您是在单个 GPU 还是数百个 GPU 上训练模型，Lightning 都能为您提供同样紧密、交互式的循环，现在由 AI 提供强大动力，并即时连接到您所需的计算资源。”

[![](https://cdn.thenewstack.io/media/2025/10/f1669819-lightning-ai-studio-1024x578.png)](https://cdn.thenewstack.io/media/2025/10/f1669819-lightning-ai-studio-1024x578.png)

（来源：Lightning AI）

新版本的主打功能是 AI 代码编辑器。您可以将其视为 Lightning 版本的一个副驾驶风格的代理，现已内置于 Lightning Studios（其 IDE）和 Notebooks（类似 Jupyter）中。它具有由专门训练成为 PyTorch 专家的模型支持的 AI 代理，用于帮助开发者完成训练、推理和强化学习任务。

这些代理还可以使用 [Lightning 模型 API](https://lightning.ai/models?section=allmodels)，该 API 提供了对各种专有和开放权重模型的访问。

## 可共享环境

Lightning AI 的另一个核心功能是其环境，公司将其描述为“独立的、交互式的空间，开发者可以在其中探索、训练和扩展强化学习以及分布式 AI 工作负载。”

现在的新功能是开发者可以通过公司称之为 Environments Hub 的方式共享这些设置。这应该会大大简化新开发者在该平台上启动项目。

[![](https://cdn.thenewstack.io/media/2025/10/cb11d360-environment-gallery-1024x655.png)](https://cdn.thenewstack.io/media/2025/10/cb11d360-environment-gallery-1024x655.png)

（来源：Lightning AI）

## Meta 的 Monarch 登陆 Lightning AI

本次发布还包括对 [Monarch](https://pytorch.org/blog/introducing-pytorch-monarch/) 的支持，这是 Meta 的新型分布式编程框架，旨在使 PyTorch 集群的使用像使用单机一样简单。

PyTorch Monarch 使集群规模的训练具有交互性和持久性。开发者可以实时迭代实验、调试问题和修改代码，所有这些都无需重新启动或重新分配其计算资源。

当与 Lightning 的多机训练服务集成时，这允许开发者例如从 Lightning Studio 中的单个笔记本扩展到多个云提供商的数百个 GPU，同时仍保持其熟悉的 PyTorch 工作流程。

[![](https://cdn.thenewstack.io/media/2025/10/eaa0ca2b-5-1.png-1024x634.avif)](https://cdn.thenewstack.io/media/2025/10/eaa0ca2b-5-1.png-1024x634.avif)

（来源：Meta）

“Monarch 重新定义了分布式训练的体验，”Lightning 的首席技术官兼 PyTorch 基金会技术咨询委员会主席 Luca Antiga 表示。“我们与 Meta 的 PyTorch 团队一起，正在使大规模开发像本地实验一样具有交互性和灵活性。这使得下一代 AI 构建者能够以前所未有的速度前进。”

Meta 最近还推出了 [TorchForge](https://github.com/meta-pytorch/torchforge)，这是一个基于 PyTorch 的强化学习（RL）框架，它构建在 Monarch 之上。它允许开发者用伪代码编写他们的 RL 算法，由 Monarch 处理执行。

Lightning AI 现在支持 TorchForge 以及 Meta 用于打包和共享 RL 环境的新型 OpenEnv 开放标准。