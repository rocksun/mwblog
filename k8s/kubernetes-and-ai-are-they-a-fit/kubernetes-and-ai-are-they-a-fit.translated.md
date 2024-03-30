## Kubernetes 和 AI：它们是否合适？

![Kubernetes 和 AI：它们是否合适？的特色图片](https://cdn.thenewstack.io/media/2024/03/67dab3fc-kubcon-paris-2-1024x576.jpg)

巴黎——假设一位机器学习研究人员阅读了一篇研究论文，并希望在 PyTorch 环境中使用基于 Python 的 GPU 对其进行测试。她要求她的工程团队访问一个带有两个 GPU 及其所有库的 [Jupyter notebook](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/)。

工程团队告诉她这将需要三天时间。他们必须采购 GPU，创建一个堆栈，然后授予对 [JupyterHub](https://jupyter.org/hub) 的访问权限。

“这正是 [DevOps](https://thenewstack.io/devops/) 在 10 年前经历过的，”独立分析师兼 [The New Stack](https://thenewstack.io/author/janakiram/) 的 [常客](https://janakiram.com/) Janakiram MSV 在本月举行的 [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 上的一次谈话中说道。

“因此，现在的整个想法是，我们如何加速这一进程，并使企业 IT 能够将基础设施提升到一个点，使其随时可供 ML 研究人员、工程师和开发人员使用，他们可以快速将其想法转化为代码？”

新角色反映了 [大型语言模型](https://thenewstack.io/what-is-a-large-language-model/)（LLM）对云原生社区的影响，并引发了关于身份和 [Kubernetes](https://thenewstack.io/kubernetes/) 角色的问题。数据科学家是否还需要 Kubernetes 才能将他们的模型投入生产？

“在 NVIDIA 的 GTC 大会上，他们宣布了一项名为 [Nim](https://developer.nvidia.com/blog/nvidia-nim-offers-optimized-inference-microservices-for-deploying-ai-models-at-scale/) 的功能，”独立分析师 [Sanjeev Mohan](https://www.sanjmo.com/) 在为 The New Stack Makers 的即将播出的剧集录制的一段录音中说道。“NVIDIA 推理微服务 Nim 是由 Kubernetes 编排的 [Docker](https://www.docker.com/?utm_content=inline+mention) 容器。这仅仅发生在上周，当时我们在 KubeCon，而 [NVIDIA GTC](https://thenewstack.io/nvidia-gtc-hyperscaler-happiness-and-enterprise-indigestion/) 也在同时举行。”

数据的有状态特性和变化速度使得 Kubernetes 成为以数据为中心的挑战变得困难。数据在 Kubernetes 社区中从未发挥过如此重要的作用。Kubernetes 社区从未像现在这样需要适应生成式 AI、模型开发、集成、部署和管理带来的新需求。

如果没有数据模型在 Kubernetes 上部署的标准方法，那么未来的工作将要求社区通过新的硬件集成和项目来适应新的数据角色。

## Kubernetes 和 LLM

但实际上，Kubernetes 在 AI 中的作用是什么？角色问题将此事提到了最前沿。Kubernetes 是一个控制平面——是的，这很有道理。自 2014 年以来，它一直作为 DevOps 的应用程序架构。

因此，Mohan 提出一个问题变得更加相关：Kubernetes 是为 AI 而生，还是 AI 是为 Kubernetes 而生？

在 KubeCon，我们看到了很多 Kubernetes 如何为 AI 服务，作为控制平面。NVIDIA 在主题演讲中登台，他们谈到了动态资源分配以分配部分 GPU。这样可以节省成本。因此，这是 Kubernetes 为 AI 服务。Mohan 说，所有这些开发都进行得非常好，我们将看到越来越多的 Kubernetes 成为通用 AI 的控制平面。

但是，Mohan 问，AI 如何让 Kubernetes 变得更加强大，例如使用 LLM？

他说：“我还没有看到很多关于这方面的内容，也许在下一届或再下一届 KubeCon，我们将开始看到更高的集成。”

[OpenAI](https://thenewstack.io/openai-chats-about-scaling-llms-at-anyscales-ray-summit/) 证明了 Kubernetes，该公司使用 Kubernetes 来 [启动和扩展实验](https://kubernetes.io/case-studies/openai/)。

在 KubeCon 上，甲骨文的高级副总裁 Sudha Raghavan 问道，Kubernetes 如何在不考虑数据科学家和数据工程师如何配置它、如何最有效地使用任何硬件 GPU 的情况下，成为所有 AI 工作负载的默认选择。

Raghavan 也在 KubeCon 的一个小组讨论中谈到了一个世界，在这个世界中，基于每个工作负载的工作变得更容易，工程师可以配置开箱即用的模板，了解这些是尚未到来的 AI 工作负载的模式，并为它们预定义模板。

因此，任何想要做实验的数据科学家都不必自己学习，而是可以了解 [Oracle](https://developer.oracle.com/?utm_content=inline+mention) 的
[云原生计算基金会](https://cncf.io/?utm_content=inline+mention) 可以为人工智能和机器学习社区提供其生态系统。英特尔开放生态系统副总裁兼总经理 [Arun Gupta](https://www.linkedin.com/in/arunpgupta/) 在一个小组讨论中表示，云原生社区的责任是弥合差距。必须对作为数据科学家的客户感同身受。他表示，一篇新的 [云原生人工智能论文](https://www.cncf.io/wp-content/uploads/2024/03/cloud_native_ai24_031424a-2.pdf) 解决了此类挑战。[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 的首席产品经理 [Lachlan Evenson](https://www.linkedin.com/in/lachlanevenson/) 在与 Gupta 同一小组讨论中表示，Kubernetes 社区中的新角色还包括人工智能工程师，他们介于数据科学家和基础设施工程师或平台工程师之间。

Evenson 在小组讨论中指出，人工智能工程师不仅需要了解人工智能世界中所有术语，还需要了解如何大规模使用这些分布式系统并构建这些新平台。

## 可扩展性的承诺

Kubernetes 创始人使 Kubernetes 无状态，然后构建了有状态技术以与其分布式平台集成。

Evenson 说：“因此，这不仅说明了这个社区，还说明了我们通过这个社区构建到该平台中的可扩展性。” “这并不容易，你必须成为这些大公司之一。我同意其他人的说法，我们需要让每个人都更容易运行。

“我们需要提供开源替代方案和开源平台，以便希望开始投资并了解人工智能如何影响其业务的公司，他们可以采用模型，而不必担心数据治理或安全问题，并开始在本地环境中对其进行调整并熟悉它们。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)