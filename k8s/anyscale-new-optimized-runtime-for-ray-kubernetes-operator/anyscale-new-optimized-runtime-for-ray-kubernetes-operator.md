
<!--
title: Anyscale：Ray的全新优化运行时，Kubernetes Operator
cover: https://cdn.thenewstack.io/media/2024/10/786be763-anyscale-new-optimized-runtime-for-ray-kubernetes-operator-2.png
-->

扩展平台使组织能够更快、更高效地构建和扩展 AI 应用程序。

> 译自 [Anyscale: New Optimized Runtime for Ray, Kubernetes Operator](https://thenewstack.io/anyscale-new-optimized-runtime-for-ray-kubernetes-operator/)，作者 Chris J Preimesberger。

Anyscale，作为开源 AI 计算引擎 Ray 背后的快速发展公司，在本周早些时候于旧金山举行的年度用户大会上发布了一系列新产品和服务。

其中包括： 根据客户反馈创建的经过优化的 Ray 运行时以及 Kubernetes Operator。

为期三天的 Ray 峰会活动于周四结束，吸引了近 1500 名开发者，还汇聚了 OpenAI、a16z、Meta 和 Runway 等公司的主要专家，共同探讨大规模开发 AI 的最新创新。

Ray 是一个统一的 AI 开发平台，企业将其部署以在其任何基础架构上扩展其 AI 和机器学习工作负载。该公司声称，Ray 使开发人员能够不花钱或不具备构建复杂基础架构的专业知识就能立即将应用从笔记本电脑扩展到云。

目前使用 Anyscale 的 Ray AI 平台的用户包括 Airbnb、Instacart、OpenAI、Netflix、Uber、Canva、Pinterest 和 Spotify。

Anyscale 宣布了一系列平台进步，包括进行的架构重建，使 Ray 原生支持 GPU。这意味着现在它能够针对分布式训练和模型服务等工作负载实现 GPU 间通信的高性能。

这家成立五年的旧金山公司还宣布推出 RayTurbo，一项经过优化的 Ray 运行时，旨在提高 AI 工作负载的性能和效率。该公司推出了适用于 Kubernetes 的 Anyscale Operator，使用户能够在他们控制的基础设施上优化他们的 AI 工作负载和 Kuberay API 服务器投资。

Anyscale 还更新了其 Anyscale Governance Suite，这是一组旨在管理计算资源和控制 AI 蔓延的可观测性工具。

## Ray 能够“启用任何人工智能工作负载”

Anyscale联合创始人Ion Stoica告诉The New Stack：“从第一天开始，我们就设计Ray用于构建和扩展AI应用程序。”“通过使用单个灵活的框架统一基础设施，Ray可以支持任何人工智能工作负载，从多模态数据处理到模型训练到模型服务等。”

Stoica说，RayTurbo是根据Ray用户意见而创建的。

“我们持续听到的一条反馈是，我们的用户需要最大化其资源利用率并最小化成本，”Stoica说。“现在，利用RayTurbo，我们在业界事实上的标准AI计算引擎之上进行了构建，使其更快、更具成本效益且更可靠。现在，所有用户都可以在Anyscale平台上使用RayTurbo。”

在大会上发布的其他产品包括Ray Data，这是一个用于大规模处理非结构化数据的库，连接Anyscale平台与Kubernetes的新直接集成，用于AI/ML开发，以及企业治理和可观测性工具。

## 新增支持的数据格式

Ray Data 全面可用后，该公司表示，所有用户都将能够访问新支持的数据格式，包括 Hudi、Iceberg 和 Delta Lake 等数据湖仓格式。

“Ray 的灵活性使其成为开发人员扩展任何 AI/ML 工作负载的理想平台，无论其多么复杂和精妙，”Stoica 说。“这就是为什么大多数主要的 AI 公司都在使用 Ray。现在我们已经重新架构了 Ray 以使其成为 GPU 原生，我们能够为分布式训练和模型服务等工作负载提供更好的性能。”

Stoica 将 Anyscale 放入了商业环境中，Anyscale 与 [AWS](https://aws.amazon.com/?utm_content=inline+mention) [CodeWhisperer](https://thenewstack.io/developer-tool-integrations-with-ai-the-aws-approach/), ChatGPT, [Github Copilot](https://thenewstack.io/go-big-or-go-home-what-github-learned-building-copilot/) 和 [MetaGPT](https://www.deepwisdom.ai/) 等产品竞争。

“我不确定人们是否意识到 Ray 为世界上一些最大、最知名的科技公司提供支持，”他说。

“例如，如果您在 Airbnb 上预订住宿，Ray 支持这些 AI 推荐。或者在 Instacart 上订购您的杂货以便在手机上取货，Ray 支持这一点。AI 基础设施对于支持这些公司改善用户体验至关重要，从而在过程中积极影响数百万人的生活。”
