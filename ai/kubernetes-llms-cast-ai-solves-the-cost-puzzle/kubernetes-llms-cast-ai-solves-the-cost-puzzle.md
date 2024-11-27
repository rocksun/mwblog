
<!--
title: Kubernetes + 大模型：Cast AI解决成本难题
cover: https://cdn.thenewstack.io/media/2024/11/f651b0cb-alex-shuper-4kexemmkesw-unsplash-1.jpg
-->

Cast AI 利用其在 Kubernetes 自动化方面的专业知识，使 DevOps 和 AIOps 团队能够找到性能和成本最佳的 AI 模型。

> 译自 [Kubernetes + LLMs: Cast AI Solves the Cost Puzzle](https://thenewstack.io/kubernetes-llms-cast-ai-solves-the-cost-puzzle/)，作者 Jeffrey Burt。

几年前，[Cast AI](https://thenewstack.io/devfinops-and-ai-to-provision-exactly-the-right-cloud-spend/) 推出了一个自动化平台，用于管理 [Kubernetes](https://thenewstack.io/kubernetes/) 的运营和成本。鉴于 Kubernetes 和 AI 之间的共生关系，这家成立五年的初创公司也帮助组织及其开发人员管理 AI 运营成本也就不足为奇了。

这家位于佛罗里达州迈阿密的公司并非 AI 新手；其 Kubernetes 平台由机器学习算法驱动。生成式 AI 的快速兴起为 Cast AI 开辟了另一条途径。该供应商在四月推出了其 AI 优化器服务，该服务通过与任何与 OpenAI 兼容的 API 端点集成并识别 LLM（商业和开源）来自动降低部署[大型语言模型 (LLM)](https://thenewstack.io/llm/) 的成本，从而为最低的推理成本提供最佳性能。

Cast AI 还拥有其 Playground 交互式测试工具，允许开发人员比较 LLM 的性能和成本，然后自定义配置，而无需调整代码。

在最近的[KubeCon + CloudNative 北美大会](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 上，Cast AI 推出了 AI Enabler，这是 Playground 的产品化版本，它利用[供应商的 Kubernetes 基础设施优化能力](https://thenewstack.io/automating-the-security-of-kubernetes-clusters-in-the-cloud/) 将来自组织和 DevOps 人员的查询智能地路由到针对他们正在运行的任务的最佳、最具成本效益的 LLM（再次强调，商业或开源）。

![](https://cdn.thenewstack.io/media/2024/11/c2ece790-cast-ai-enabler-1.png)

Cast AI 的联合创始人兼首席产品官告诉 The New Stack，使用该工具的初始名称，“Playground 使团队能够揭开 LLM 性能和成本的神秘面纱。它不再是猜测。用户可以直接对模型进行基准测试，了解它们的权衡，并为其特定工作负载做出数据驱动的决策，所有这些都无需编写一行代码。”

## 成本高昂的 LLMs

Cast AI 的各种工具——包括 AI Optimizer 和现在的 AI Enabler（之前的 Playground）——旨在帮助开发人员掌握生成式 AI 领域，该领域的 LLM 数量及其运行成本正在迅速增长。在一篇[博文](https://cast.ai/blog/llm-cost-optimization-how-to-run-gen-ai-apps-cost-efficiently/) 中，该公司产品营销总监指出，OpenAI 的 LLM 模型的[定价页面](https://openai.com/api/pricing/) 有 10 页长，至少有 20 种不同的模型，用于不同的用例和定价模型。

鉴于此，开发人员和[AIOps](https://thenewstack.io/supercharge-aiops-efficiency-with-llms/) 团队由于时间紧迫而难以确定哪个模型最适合他们的特定需求，这通常是一项手动工作。然后是运行 LLM 的成本，这需要昂贵的组件，如 Nvidia GPU，并消耗大量能源。根据[国际能源署](https://www.iea.org/) 的说法，ChatGPT 查询[消耗的电力是谷歌搜索的 10 倍](https://www.goldmansachs.com/insights/articles/AI-poised-to-drive-160-increase-in-power-demand)。

成本可能会增加。一家成立两年的 AI 咨询公司 的创始人在一篇博文中写道，围绕 LLM 的成本增长速度有多快。指出，虽然自[两年前 ChatGPT 发布以来](https://thenewstack.io/how-to-create-software-diagrams-with-chatgpt-and-claude/)，LLM 一直是生成式 AI 的基础，但成本一直是组织实现其潜力的障碍。

“将 LLM 集成到您的应用程序中的费用范围从按需使用情况的几美分到在云环境中托管单个 LLM 实例的每月 20,000 美元以上不等，” 写道。“此外，还与微调、训练、向量搜索和扩展相关的巨额成本。”

## 控制成本

Cast AI 的 表示，控制这些成本可以使 DevOps 团队充分利用 LLM 的功能。
他写道：“一些团队可能没有意识到，使用默认的LLM或依赖单一提供商可能并非所有用例的最佳选择。”“结果，他们经常使用比必要更资源密集且昂贵的模型。他们没有探索其他选项或根据特定需求定制模型，错过了更高效、更经济的解决方案。这可能导致不必要的支出和资源利用效率低下。”

DevOps和MLOps团队负责构建和维护生成式AI工作负载的基础设施，但他们无法透明地了解计算资源、API调用或数据使用的成本，而转向云也无济于事，因为需要考虑数百个具有不同配置、性能和定价的计算实例。Radhakrishnan表示，自动化是关键。

## 仪表板和Playground

AI Enabler包含一个用于监控成本的仪表板，并创建一个报告，比较使用默认LLM与利用其他模型的支出。该仪表板汇总来自一系列LLM提供商的数据，以更清晰地了解每个LLM的成本。该工具还可以自动选择最佳LLM，无需额外配置。

![](https://cdn.thenewstack.io/media/2024/11/0123f562-cast-ai-cost-optimization-1.png)

他写道：“LLM代理智能地选择最优的LLM模型来处理用户查询，确保组织以最低的成本获得最佳性能。”“这种方法通过选择和执行具有较低推理成本的优化LLM来实现最大限度的节省。”

这与该供应商的AI Enabler非常契合，AI Enabler比较LLM并创建基准，开发人员可以使用这些基准来开发最适合其需求的配置，并做出更好的决策，以优化最适合性能和成本的LLM。

![](https://cdn.thenewstack.io/media/2024/11/ad725eae-cast-ai-playground-1.png)

使用AI Enabler，DevOps团队可以通过创建比较LLM、提供商和响应的场景来探索其选项，测试路由行为并可视化路由决策，以及配置和调整路由参数。

Gil说：“借助Cast AI Playground，我们将控制权交还给企业。”“通过允许团队并排比较LLM的性能和成本，我们正在帮助他们释放AI的全部潜力，同时确保每一美元都花得其所。”

## 在Kubernetes中迁移工作负载
在展会上，Cast AI还推出了其商业支持的容器实时迁移功能，该功能能够自动且不间断地迁移有状态和不可中断的工作负载——例如MySQL、[PostgreSQL](https://thenewstack.io/charles-schwab-adopts-postgresql-with-vmware-tanzu/)或MongoDB等NoSQL数据库以及AI应用程序——在Kubernetes中。该工具将使组织能够确保持续运行时间，创建更高效的操作并降低基础设施成本。

Radhakrishnan写道：“有状态的工作负载不能简单地停止和重新启动，而不会冒数据丢失或中断的风险。”“这就是为什么Kubernetes最初简化所有工作负载基础设施的承诺[未能满足](https://cast.ai/blog/how-to-migrate-stateful-workloads-on-kubernetes-with-zero-downtime/?_gl=1*1eacdrj*_up*MQ..*_ga*ODkxMTI4Njg4LjE3MzE5NTAxNDU.*_ga_YLDVPHF0WD*MTczMTk1MDE0NC4xLjAuMTczMTk1MDE0NC4wLjAuMA..)复杂、数据驱动型应用程序的需求。”

Cast AI正在将其新功能与其他自动化工具集成，包括Bin-Packing和Eviction、集群和节点重新平衡、Spot回退、Spot中断ML预测和Spot实例价格漂移重新平衡。

他写道：“运行资源密集型有状态应用程序的组织无法承受停机时间。”“由于没有广泛采用的商业解决方案可以将这些敏感的工作负载迁移到具有成本效益的资源，因此它们最终会在利用率不足且昂贵的节点上运行。”

借助容器实时迁移，组织可以自动将这些工作负载迁移到更少的优化节点中。这确保了资源的最大利用率以及最适合其需求的实例的选择，所有这些都降低了成本。
