# AI 正在快速发展——开发者如何跟上步伐

![Featued image for: AI Is Evolving Rapidly — Here’s How Developers Can Keep Pace](https://cdn.thenewstack.io/media/2025/01/d53fca28-tirza-van-dijk-i8ohou-wlo4-unsplash-1024x683.jpg)

[Tirza van Dijk](https://unsplash.com/@tirzavandijk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/person-facing-tuned-on-macbook-pro-I8OhOu-wLO4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

我与开发者密切合作多年，经历了许多技术阶段。我可以自信地说，[AI 创新的速度](https://thenewstack.io/whats-ahead-for-ai-assisted-coding-open-source-and-more/)与我们之前见过的任何事物都不同。效率是开发者跟上这一步伐的关键，也是行业达到 AI 可以为所有人带来益处的程度的关键。这是通过无缝的软硬件集成来部署基于 AI 的工作负载来实现的。

了解训练和推理背后的[计算需求](https://thenewstack.io/whats-driving-the-rising-cost-of-observability/)对于在各种设备上扩展高效部署至关重要。

**访问最快和最高效的部署方法**

在实际应用中部署 AI 时，速度和效率是不容谈判的。例如，边缘 AI 必须处理靠近源头的数据，通常具有低延迟，以实现实时响应。这对于远程医疗、自动驾驶汽车和在线游戏应用程序尤其重要。

开发者需要正确的部署工具来加速模型迭代，从而帮助更快地将解决方案推向市场。像 [TensorFlow](https://thenewstack.io/python-tutorial-use-tensorflow-to-generate-predictive-text/) 和 [PyTorch](https://thenewstack.io/why-pytorch-gets-all-the-love/) 这样的框架提供了强大且对开发者友好的环境。最新的 Llama 3.2 1B/3B 模型，结合[最近的 ExecuTorch Beta 版本](https://pytorch.org/blog/executorch-beta/)，使开发者能够在移动电话和微控制器等边缘设备上导出和运行 PyTorch 模型，从而简化了 AI 模型部署，而无需考虑平台。

对于寻求平衡速度和效率的开发者来说，理解这些框架的重要性至关重要。它们能够实现快速、迭代的开发，并将 AI 工作负载更靠近边缘，即使在资源受限的情况下也能确保最佳的应用程序性能。

**在开源生态系统中实现可扩展的 AI**

随着 AI 技术的扩展，建立互操作性至关重要。标准化的 API 和库提供了一致性，允许开发者在各种平台上构建和部署模型，而无需不断地重新配置其代码。这大大减少了项目开发时间，使开发者能够专注于创新，并通过其独特的应用程序功能创造差异化的价值，而不是解决兼容性问题。

我在 Arm 的职责是致力于提高互操作性，正如我们在与 Meta 的 PyTorch 团队的最新合作中所见，我们正在支持一项使命，即提供一个模型交换框架，以促进 AI 生态系统中模型和算法的互操作性和兼容性。通过集成计算库、性能优化和微内核来支持底层的 Arm 架构，我们实现了 Arm 服务器（如云中的 AWS Graviton）和边缘的终端设备（无论是智能手机还是像 Raspberry Pi 这样的单板计算机）的兼容性和性能增强。开发者可以直接使用最新的 Llama 3.2 模型、Pytorch 和 Executorch 框架，而无需额外的修改或优化，从而节省时间和资源。

我们在整个生态系统中采用这种赋能方法，包括其他几个基础框架，如 TensorFlow 和开源推理库（如 Google 的 XNNPACK），以普及和简化全球数十亿个基于 Arm 的设备的 AI 开发。开发者可以使用工具和框架生态系统更有效地交付强大且可扩展的 AI 解决方案。

**构建用于优化性能的协作生态系统**
重要的是要强调，人工智能的演进超越了开源框架，并且在很大程度上取决于开发人员、硬件供应商、ML 和 DevOps 独立软件供应商 (ISV) 以及研究社区之间的合作。协作有助于硬件团队微调 AI 模型及其在底层硬件上的执行，确保它们在不牺牲效率的情况下最大限度地提高性能。一个很好的例子是 [AWS 通过在 Graviton 上使用 torch .compile 来加速 Pytorch 推理的工作](https://aws.amazon.com/blogs/machine-learning/accelerated-pytorch-inference-with-torch-compile-on-aws-graviton-processors/)。与运行基于 Arm 的服务器的云服务提供商的合作建立在早期开源计划的基础上，将特定于硬件的优化整合到工作流程中。这简化了开发过程，因此开发人员不必自己处理这些优化。

像 Databricks 这样的 ML ISV 也发挥着关键作用，它们为开发人员提供智能平台、运行时和工作流程，以支持像 AWS Graviton 这样的 Arm 优化资源，从而应对部署挑战，同时推进在 AI 可扩展性和性能方面的共同目标。

当然，模型开发、MLOps 和 DevOps 至关重要。开发人员使用像 HuggingFace 和 GitHub 这样的平台进行协作、创新和部署最新的模型和框架。它们使 AI 开发成为基础和普遍存在的。

最近，GitHub 提出了一个 [简化的 MLOps 配方](https://github.blog/enterprise-software/ci-cd/streamlining-your-mlops-pipeline-with-github-actions-and-arm64-runners/)，用于简化开发。一个很好的例子是 [GitHub 最近提出的一个简化的 MLOps 配方，用于简化开发](https://github.blog/enterprise-software/ci-cd/streamlining-your-mlops-pipeline-with-github-actions-and-arm64-runners/)。我们采用了他们的提议，并[创建了一个教程来实现 GitHub 的配方](https://learn.arm.com/learning-paths/servers-and-cloud-computing/gh-runners/)，以消除各地开发人员对 MLOps 的神秘感。我们与 GitHub 的合作以及使开发人员能够通过基于 PyTorch 的真实示例快速入门的学习路径，有助于确保即使是刚开始的开发人员也能从第一天起就拥有简化的 MLOps 工作流程和优化的性能。

**结论**

我们正面临着人工智能领域千载难逢的机遇，而开发人员——以及他们在硬件和软件领域的合作者——掌握着释放这项技术全部潜力的关键。我职业生涯的大部分时间都在人工智能社区工作。自从去年加入 Arm 以来，我的使命一直是赋能全球开发人员在 Arm 上创建尖端的人工智能和应用程序功能，使其成为地球上最普及的平台。

扩展人工智能以满足全球行业和社区需求的道路包括三个重点领域：效率、互操作性和协作。通过无缝的硬件-软件集成、强大的开源框架以及简化和增强人工智能开发合作伙伴关系，我们可以继续以一种可访问、可持续且对每个人都具有影响力的方式来实现人工智能的增长。

[YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)