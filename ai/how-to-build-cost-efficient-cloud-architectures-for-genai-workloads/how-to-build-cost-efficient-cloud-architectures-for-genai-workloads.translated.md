# 如何构建经济高效的云架构以应对生成式AI工作负载

![用于：如何构建经济高效的云架构以应对生成式AI工作负载的特色图片](https://cdn.thenewstack.io/media/2025/01/60a9db5d-chuttersnap-m2-_grvwwg0-unsplash-1024x684.jpg)
[CHUTTERSNAP](https://unsplash.com/@chuttersnap?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/clouds-during-daytime-M2-_GRvWWg0?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).

从董事会会议到茶水间，生成式AI的热潮引发了过度投资、对底层云基础设施的需求不受控制、用例局部化以及商业价值有限等问题。IBM的一份报告指出，生成式AI是计算成本上升的重要因素，从2023年到2025年上涨了89%，到2028年将达到760亿美元。尽管如此，90%的CEO仍在等待生成式AI在其组织内超越实验阶段。

对云、团队和以生成式AI为重点的解决方案的大量投资未能产生预期的回报，迫使超过一半拥有活跃[生成式AI投资的企业在未来三年内暂停或放弃这些项目](https://thenewstack.io/3-reasons-tech-execs-are-slowing-down-genai-projects/)。

## 这里有三个主要原因：

### 大型语言模型的高总拥有成本

利用预训练大型语言模型（LLM）的企业会产生推理成本，根据模型的功能，API调用和任务完成的费用是分开计算的，这会根据使用情况、复杂性和数据量影响最终成本。例如，GPT-4模型可以针对更广泛的主题提供具有上下文感知的详细响应。它的价格高于其较新的专业版本GPT-4o，后者针对[速度进行了优化，但可能只提供](https://thenewstack.io/pushup-offers-speed-of-go-in-web-development-framework/)简洁的输出。

GPT-4还具有强大的记忆功能，可以跟踪更长的对话，而GPT-4o可能无法做到。在定价方面，对于128K上下文的1000个token提示，GPT-4模型的输入token收费为0.01美元，完成成本为0.03美元，总计0.04美元。相比之下，对于类似的参数，GPT-4o的输入成本为0.00250美元，完成成本为0.01000美元，总计0.0125美元——至少便宜三倍。如果企业不将LLM的功能与业务需求相权衡，最终将导致更高的[总拥有成本](https://thenewstack.io/why-latency-and-total-cost-of-ownership-matter-more-in-ai-apps/)。

### 资源过度配置

在云环境中设置LLM以增强[数据隐私的企业会大量投资于本地托管模型](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/)和设置生成式AI应用程序。这[需要一个可扩展的基础设施](https://thenewstack.io/platform-teams-automate-infrastructure-requirement-gathering/)，能够处理大量请求、大型数据存储并提供高性能。企业倾向于全天候配置这些云资源以避免模型延迟。虽然更容易预测生成式AI概念验证的资源需求，但大多数企业在扩展时往往会高估这些需求，导致难以管理或监控的云资源浪费，并导致超额收费。与生成式AI相关的云成本现在是底层模型成本的两倍。

### 对云定价模型缺乏了解

企业认为云是一种成本分摊措施，难以理解云资源是如何计费的。这使得难以可视化云支出。即使他们选择按使用付费——这是价格最高的云订阅选项之一——或选择合适的实例，考虑到企业并不完全了解成本结构或缺乏生成式AI部署的最佳利用策略，成本仍将呈上升趋势。

## 在预算范围内在云中运行生成式AI

虽然生成式AI将继续存在，但企业需要一种策略，在创建[可扩展、可持续和盈利部署的路线图时，要考虑生成式AI的成本](https://thenewstack.io/shreds-ai-creates-complex-software-in-java-and-javascript/) [复杂性和技术挑战]。以下是一种制定此策略的三管齐下的方法，重点关注成本效益分析和严格的FinOps原则：
- 优化云实例：企业应首先了解工作负载需求，以评估计算和内存需求。超大规模云提供商提供 AI 优化实例，有助于降低在云中运行 AI 工作负载的成本。监控和调整实例大小有助于避免过度配置并确保显著节省成本。例如，如果设计为容错的，预留实例是一个可行的选择，因为它们的价格最多可比按需实例便宜 90%。制定明确的扩展策略可以帮助使用预测模型准确地将资源与需求对齐，以预测需求峰值。实施预算上限可防止扩展超出指定的成本阈值。
- 大规模采用 FinOps：培养注重成本的文化，包括定期审查、审计和优化工作，对于确保持续效率和有效性至关重要。最好在[具有积极 FinOps 原则的云环境](https://thenewstack.io/finops-its-all-about-culture-and-automation/)中运行 GenAI。一个好的开始是商业 FinOps 工具，或超大规模云提供商提供的工具，结合 FinOps 实践，例如调整大小、成本跟踪和审计以及重新利用可用资源。增强的成本可见性将有助于做出更好的决策，而使用准确的标签分配成本将提供对成本分配的更深入了解。- 利用 AI 控制成本：AI 优化的硬件，例如 Google 张量处理单元 (TPU) 和 AWS Inferentia 等定制芯片，可提供针对 AI 任务量身定制的卓越计算能力，而不会超出成本。模型效率可以指导选择合适的特定功能大型语言模型，进一步优化性能和资源使用。企业可以采用先进的压缩技术来减少训练和推理期间的内存和计算需求。在函数即服务 (FaaS) 上运行的无服务器 AI 平台允许超大规模云提供商灵活地管理 AI 工作负载，无需传统的服务器基础设施。为保护数据，企业应采取大量的法规[合规性和数据](https://thenewstack.io/how-startups-can-thrive-with-borderless-data-strategies/)治理措施，确保数据保留在本地辖区内，同时通过匿名化和加密保护用户隐私。

## 基于平台的方法来治理 GenAI 成本

了解云成本结构、GenAI 工作负载的计算需求和底层模型是成本效率的关键。并非每个工作负载都需要处理高认知负荷的大型语言模型，这意味着并非每个 GenAI 应用程序都需要相同的[云中资源或实例或成本](https://thenewstack.io/engineers-guide-to-cloud-cost-optimization-engineering-resources-in-the-cloud/)。了解这些动态并将它们纳入 GenAI 战略可以帮助企业就预算、投资和运营成本做出明智的决策。

一种方法可能是用于 GenAI 部署的混合云环境，企业可以在其中编排满足其预算要求的最佳能力堆栈。一个收集资源利用率、成本中心和消费模式的仪表板可以使跟踪 GenAI 云投资更容易。这可以帮助企业为跨超大规模云提供商的 LLM 部署设置成本阈值或基于策略的定价。较便宜的 LLM 可用于常规用途。相反，较高的认知负荷需要更昂贵的 LLM——所有这些都来自不同的超大规模云提供商，通过使用量化来创建用于低成本虚拟机的较小模型的 GenAI 平台组装而成。

经济高效的 GenAI 部署取决于对云支出的细粒度可见性和 AI 工作负载的技术需求——所有这些都与实际交付的业务价值相关联。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以串流收听我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)