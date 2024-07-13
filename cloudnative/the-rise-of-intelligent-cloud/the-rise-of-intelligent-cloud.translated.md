# 智能云的崛起

![智能云的崛起特色图片](https://cdn.thenewstack.io/media/2024/07/646beb97-sky-414199_1280-1024x682.jpg)

想象一个世界，云环境不仅仅是存储、计算和可扩展性的平台，而且能够学习、适应和发展。这就是“智能云”的承诺——生成式 AI 和 [云计算](https://thenewstack.io/cloud-native/) 的强大协同作用。虽然我们今天正处于这场技术革命的顶峰，但让我们问问：这种协同作用将如何重塑企业未来构建、部署和管理其云基础设施的方式？

根据最近的一项 [麦肯锡研究](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/in-search-of-cloud-value-can-generative-ai-transform-cloud-roi)，到 2030 年，云计算预计将产生 3 万亿美元的 EBITDA，其中 GenAI 将为 ROI 贡献额外的 75 到 110 个百分点。这是由于新的业务用例、降低的迁移成本以及通过 AI 驱动的自动化和优化提高的生产力。

作为一名云架构师和策略师，我大部分的对话都是建议向 GenAI 转变。我正在见证该领域正在形成强大的协同作用，有望在云技术方面取得重大进展。

尽管关于 [本地 vs. 云](https://thenewstack.io/choosing-the-right-database-strategy-on-premises-or-cloud/)、[GPU vs. CPU](https://blogs.nvidia.com/blog/whats-the-difference-between-a-cpu-and-a-gpu/) 和 [LLM 微调 vs. RAG](https://thenewstack.io/rag-vs-fine-tuning-models-whats-the-right-approach/) 的争论激烈，但最终的最佳选择取决于个别企业及其特定的用例。因此，对于企业领导者、云和 AI 架构师、工程师以及任何对 GenAI 云未来感到兴奋的人来说，本文提供了有关 GenAI 如何改变云平台的见解。它提供视角和整体指导，帮助为即将到来的挑战和机遇做好准备。

## 下一代智能应用程序：AI 如何重塑格局

如今，软件开发人员在编写代码的同时，还协调数据、模型和 AI 服务的融合，以创建高级应用程序。这还包括集成不同的数据源并利用大型语言模型 ([LLM](https://www.ibm.com/topics/large-language-models))。从平台的角度来看，云提供商服务，如 [微软的 Azure AI Studio](https://azure.microsoft.com/en-gb)、[谷歌 Vertex AI](https://cloud.google.com/products/ai?hl=en) 和 [亚马逊 SageMaker](https://aws.amazon.com/ai/) 使这些功能变得触手可及。

对于企业来说，这些工具使即使是最小的初创公司也能快速部署复杂的 AI 驱动的服务。同时，大型企业可以通过高级 AI 模型增强其分析能力，从而改变应用程序开发和部署的每个阶段。

毫无疑问，这些进步至关重要，但对于企业来说，取得长期成功还取决于解决五个基础支柱：

- 建立 DevOps 文化
- 利用云原生架构和模式
- 启用平台工程
- 执行数据整合并制定数据策略
- 拥抱创新和工程文化

## AI 驱动的云：从自动化到自主

在当今的形势下，尽管自动化工具层出不穷，但管理和运营云越来越复杂。问问任何 DevOps 或 SRE 工程师，他们都会告诉你“工具蔓延”或“云服务蔓延”的挑战。虽然许多组织努力标准化和优化其流程，但他们经常需要添加新的工具或服务，这些工具或服务会使情况更加复杂，而不是解决问题。在这种情况下，将传统 AI 与 GenAI 功能集成在一起，为向前迈进提供了一条有希望的道路，简化了操作并显着提高了整体云管理。

在不久的将来，[AI 代理](https://aspiringforintelligence.substack.com/p/ai-agents-and-new-age-of-software) 将通过持续学习和实时决策来改变云管理。这些智能程序将自动处理诸如在流量高峰期间扩展资源、部署针对威胁的安全措施以及使用预测分析优化资源分配等任务。通过自动化这些复杂的操作，AI 代理将使 DevOps、SRE 和运营团队能够专注于更具战略意义的高价值任务，最终提高整体生产力。

## 模糊界限：物理和数字融合
随着云计算和生成式人工智能 (GenAI) 技术的不断发展，物理世界和数字世界之间的界限将逐渐模糊。边缘计算和物联网 (IoT) 与 GenAI 驱动的云服务相结合，将实现本地边缘数据处理和集中式云功能之间的无缝连接。这种演变促进了 [微云](https://ubuntu.com/engage/introduction-to-micro-clouds)（本地边缘）和宏云（公共/私有云环境）之间的持续连接。

**注意：** 公共云提供商已经通过 [AWS Outposts](https://aws.amazon.com/outposts/), [Google Anthos](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/install-edge-profile) 和 [Azure Stack Edge](https://azure.microsoft.com/en-us/products/azure-stack/edge/) 等解决方案推动了这种混合方法，这些解决方案目前支持边缘部署。

想象一家配备了 IoT 传感器的工厂，用于收集性能数据，其中轻量级 LLM 模型 ([SLM](https://www.version1.com/the-emergence-of-small-language-models/)) 不断监控设备数据，立即标记异常模式。这些现场模型与复杂的基于云的 [LLM](https://www.ibm.com/topics/large-language-models) 相结合，将快速的本地响应与深入的分析相结合，以优化制造流程。这种双重方法将使预测分析和主动决策成为可能，推动未来几年效率和创新的提升。”

让我在这里告诉你一些事情：乍一看，这可能听起来很简单，也很花哨，但事实可能并非如此；云提供商和消费者可能需要做很多工作才能达到这一点。

## 驾驭智能云革命
虽然智能云的前景乐观且具有前瞻性，但我们也必须解决它带来的复杂性和挑战。确保数据隐私、促进负责任的人工智能开发和维护合规性至关重要。最重要的是，培养人工智能原生思维将是驾驭这些动态的关键。

GenAI 不再仅仅是技术对话——它已经发展成为商业对话，影响着商业战略的各个方面。

智能云之旅的第一步应侧重于识别商业价值、确保投资回报率、确保在旅程早期产生切实的影响，并更多地关注：

- 强调业务成果
- 做出明智的决策
- 严格测试并衡量进度
- 建立稳固的架构基础，其中治理至关重要
- 与社区互动
**行动号召：** 始终牢记，踏上转型之旅需要一个稳固的战略。采用“爬行、行走、奔跑”的方法对于实现持久成功和投资回报至关重要。
[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)