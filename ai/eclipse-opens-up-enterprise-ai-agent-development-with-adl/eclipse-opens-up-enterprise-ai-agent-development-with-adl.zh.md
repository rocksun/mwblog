[Eclipse 基金会](https://www.eclipse.org/) 昨日推出了 [代理定义语言（ADL）](https://github.com/inference-gateway/adl)，这是一个旨在使企业 AI 开发更易用、可靠和可扩展的新工具，向专有 AI 平台发起挑战。

Eclipse 将 [ADL](https://eclipse.dev/lmos/docs/arc/adl/) 定位为 [Eclipse LMOS](https://eclipse.dev/lmos/)（语言模型操作系统，目前处于 alpha 阶段）的核心。该组织表示，Eclipse LMOS 是一个开源平台，旨在重塑大型组织构建和部署 AI 代理的方式。通过此举，它[直接瞄准了主导企业 AI 领域的闭源替代方案](https://thenewstack.io/ibms-mellea-tackles-open-source-ais-hidden-weakness/)。

## 源于真实世界的需求

Eclipse LMOS 项目负责人 Arun Joseph 于 2023 年开发了该平台，当时他正领导德国电信的 AI 项目。他的任务是在 10 个欧洲国家部署 AI 以支持销售和服务运营。但他很快碰壁了，他告诉 The New Stack。

[![](https://cdn.thenewstack.io/media/2025/10/dd4aad9b-res-increased-1-210x300.jpg)](https://cdn.thenewstack.io/media/2025/10/dd4aad9b-res-increased-1-210x300.jpg)

Arun Joseph，Eclipse LMOS 项目负责人

Joseph 在最近的一次简报中解释说：“我们开始时，像 [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) 这样的新兴框架已经出现，但它们都是用 [Python](https://thenewstack.io/what-is-python/) 编写的。”“德国电信的整个企业堆栈，像大多数电信公司和企业一样，都构建在 [JVM](https://thenewstack.io/how-do-javas-virtual-threads-help-your-business/) [Java 虚拟机] 上。我们意识到我们必须从头开始重建一切。”

然而，问题不仅仅是 [编程语言](https://thenewstack.io/introduction-to-java-programming-language/)。德国电信的 API 很复杂，拥有数百个属性和多年积累的领域知识，这些都融入了客户端库中。从头开始构建 Python 堆栈意味着放弃这些机构知识，并迫使团队重建已经存在的东西。

于是，Joseph 和他的团队采取了不同的方法。他们使用 [Kotlin](https://thenewstack.io/angular-18-kotlins-new-compiler-astro-adds-react-19-support/) 构建了自己的堆栈，这是一种 JVM 语言，可以利用现有的基础设施、API 和 [DevOps](https://thenewstack.io/introduction-to-devops/) 实践。到 2023 年底，他们为德国电信推出了第一个代理。

AI 驱动的开发安全平台提供商 [Arcjet](https://thenewstack.io/arcjet-brings-ai-security-analysis-local-into-your-code/) 的首席执行官 David Mytton 告诉 The New Stack，这“看起来是一个真实信号，表明代理正在从演示走向运营。”“其他人也探索过‘代理定义’的想法，但 Eclipse 的治理和 Java 足迹对于普及至关重要，因为 JVM 在所有严肃的企业中都得到了广泛使用。”

## Jira 工单问题

但解决技术集成挑战后，又出现了另一个更微妙的问题：Joseph 问道，你如何定义 AI 代理应该做什么？

Joseph 说：“在传统的应用程序开发中，业务人员会提交一个 [Jira](https://thenewstack.io/open-source-jira-alternative-plane-lands/) 工单，说‘我想要这个按钮，当我点击它时，它应该将商品添加到购物车中’。”“但是你如何描述一个代理的需求呢？你如何编写一个工单来解释当客户问‘我的账单为什么这么高？’时，机器人应该如何回应？”

Joseph 说：“确实，你如何编写 Jira 工单？”“以账单为例。通常，企业有领域划分，对吗？产品领域、账单领域……所以，如果你必须编写需求，不是工程需求，而是最终用户体验需求，这对于代理式对话系统来说非常困难。”

答案就是 ADL，这是一种结构化语言，使业务领域专家能够将代理行为编写为标准操作规程，而无需成为 [提示工程师](https://thenewstack.io/prompt-engineering-get-llms-to-generate-the-content-you-want/)。他说，通过基于网络的界面，业务用户可以定义用例，立即测试它们，并迭代，而无需等待工程工单在冲刺中循环。

Joseph 指出：“我们希望让定义代理行为像描述业务流程一样直观，同时保留工程师所期望的严谨性。”“它消除了基于提示设计的脆弱性。”

## Eclipse LMOS 的三大支柱

Eclipse LMOS 包含三个协同工作的核心组件：

*   **Eclipse LMOS ADL** 提供了一种结构化、模型中立的语言和可视化工具包，让领域专家能够定义代理行为并与工程师协作。它旨在可版本化和可维护，解决传统提示工程的混乱问题。
*   **Eclipse LMOS ARC 代理框架** 提供了一个 JVM 原生框架，带有用于开发和测试 AI 代理的 Kotlin 运行时。它包括一个内置的可视化界面，用于快速迭代和调试，让工程师能够专注于集成特定领域的 API，而不是与 AI 基础设施作斗争。
*   **Eclipse LMOS 平台** 作为一个开放的编排层，用于代理生命周期管理、发现、语义路由和可观测性。它构建在 [云原生计算基金会（CNCF）](https://cncf.io/?utm_content=inline+mention) 堆栈之上，目前处于 alpha 发布阶段。

[![](https://cdn.thenewstack.io/media/2025/10/754091d2-defining_adl_lmos-1.png)](https://cdn.thenewstack.io/media/2025/10/754091d2-defining_adl_lmos-1.png)

Mytton 说：“将业务上下文带入 AI 工作流和应用程序对于它们能够大规模做出高质量决策至关重要。”“自然语言提示不可版本化，也无法审计——这是企业面临的痛点，这也是编程语言存在的原因——所以这为两者之间提供了解决方案。”

## 不同的理念

Eclipse LMOS 的方法代表了与当前 AI 工具格局的哲学上的不同，Joseph 将其描述为对企业而言存在问题。

在向 The New Stack 演示时，Joseph 展示了一张讽刺性的幻灯片，展示了典型的企业 AI 堆栈：一个 Python 代码库导入了来自多个风险投资支持的初创公司的 SDK，每个初创公司都解决了一个难题的一部分——遥测、内存、评估——而一个简单的装饰器就能为基础设施添加整个容器集群。

Joseph 说：“我看到过一个评估工具，仅一个功能就需要 25 个容器。”“这意味着 25 个容器运行一个自定义的 [Kubernetes](https://thenewstack.io/kubernetes/) 运算符，只为了一行代码。企业无法承受这种蔓延。”

相反，Eclipse LMOS 与企业已经运行的技术集成，包括 Kubernetes、[Istio](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/) 和基于 JVM 的应用程序。该平台旨在与组织多年来构建的现有 DevOps 实践、可观测性工具和 API 库协同工作。

## 已通过大规模验证

Joseph 表示，德国电信已将 Eclipse LMOS 部署在欧洲最大的多代理企业系统之一中，为 [Frag Magenta OneBOT 助手](https://www.telekom.com/en/company/digital-responsibility/details/artificial-intelligence-at-deutsche-telekom-1055154) 和其他面向客户的 AI 系统提供支持。此次部署已处理了跨多个国家的数百万次服务和销售交互。

Joseph 说，在许多 AI 平台承诺企业就绪但很少能以面向客户的部署所需的可靠性在电信规模上运行的行业中，这种真实世界的验证至关重要。

他说：“我相信应用 AI 的最佳方式是运营，句号。没有比运营更好的应用 AI 的领域了。”“你的整个企业堆栈以及工程师和运营都在 JVM 中，然后你有数据科学家和这些新的库，它们只是不断地添加，但如果没有数据管道，你将无法前进。”

## 标准重要吗？

[Constellation Research](https://www.constellationr.com/) 的分析师 Holger Mueller 告诉 The New Stack：“标准对于新兴技术很重要，因为它们允许重用、交互和投资保护。”“考虑到 [MCP](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) [模型上下文协议] 和 [A2A](https://thenewstack.io/google-brings-the-a2a-protocol-to-more-of-its-cloud/) [代理到代理]，代理式 AI 的标准提出很快，采纳更快。这并不意味着 Eclipse 的 LMOS 等标准没有更多空间——但这将是一场艰苦的战斗——因为代理大多在云中运行，云标准已经建立，并且人们正在为它们构建代理。对于 Eclipse 基金会来说，这将是一场艰苦的战斗。”

[The Futurum Group](https://futurumgroup.com/) 的分析师 Brad Shimmin 倾向于同意 Mueller 的观点。

他说，目前关于代理式平台、框架和工具的噪音实在太多，以至于更传统的标准化工作往往显得过于老旧和缓慢，无法帮助公司解决眼前的紧迫问题。

Shimmin 说：“因此，我担心 Eclipse 基金会这种极其全面的‘平台’概念可能会输给发展更快、尽管更零散的架构工具，如 MCP、A2A 等。”“同样，每个前沿模型制造商和超大规模提供商都力求将自己打造成代理平台提供商。在这方面，我无法想象这些参与者会将控制权交给一个可能威胁其竞争差异化的平台。尽管如此，随着时间的推移，我希望公司能够将 LMOS 或其他此类全面、开放且主权保护的理念视为管理跨越这些封闭代理平台代理系统的一种手段。”

## 市场时机

ADL 公布的时机与代理式 AI 的爆炸性增长预测相符。[根据 Gartner 的数据](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)，到 2028 年，15% 的日常业务决策将通过代理式 AI 自主完成，33% 的企业应用程序将包含此类功能——高于 2024 年的不到 1%。

Eclipse 基金会执行董事 Mike Milinkovich 在一份声明中表示：“代理式 AI 正在重新定义企业软件，但迄今为止，除了专有产品之外，还没有开源替代方案。”“通过 Eclipse LMOS 和 ADL，我们正在交付一个强大、开放的平台，任何组织都可以用它来构建可扩展、智能和透明的代理系统。”

## 可靠 AI 运动

Joseph 的工作与一场更广泛的运动相关联，这场运动倡导他所称的在企业环境中的“可靠 AI”。他是[可靠代理式 AI 宣言](https://github.com/reasonable/reliable-ai/blob/main/reliable-ai-manifesto.md) 的贡献者之一，与 Jonas Bonér、James Ward 和 Eric Meijer 等著名软件工程界人士一道，推动优先考虑操作可靠性而非前沿实验的方法。

这份宣言反映了 AI 行业中创新型初创公司（基于 Python 构建）与在基于 JVM 的基础设施上投入巨资的现有企业之间日益增长的紧张关系。Eclipse LMOS 坚定地站在后者阵营，认为通往可靠 AI 的道路是通过现有企业能力，而不是绕过它们。

## 企业优势

与专有替代方案相比，Eclipse LMOS 提供多项架构优势，包括开放架构、多代理协作、云原生可扩展性、模块化和可扩展性以及多租户功能。

## 超越电信

虽然 Joseph 已离开德国电信，并创办了自己的初创公司 [Masaic](https://masaic.ai/)，专注于运营智能，但 Eclipse LMOS 继续作为 Eclipse 基金会下的开源项目。该平台旨在为代理式 AI 带来 Eclipse IDE 为 Java 开发所带来的东西：创建一个供应商中立、社区驱动的基础，任何组织都可以在其上进行构建。

与此同时，Joseph 的新公司将自己定位为 [Palantir](https://www.palantir.com/) 的开放替代方案，专注于运营 AI。他说，该公司使用 Eclipse LMOS 作为其开放核心，展示了该平台如何作为商业产品的基础，同时仍对社区免费开放。

Joseph 说：“应用 AI 的最佳方式是运营。”“让公司实现 AI 原生化的最佳方式是赋能那些已经了解其系统的工程师，而不是引入外部顾问来构建黑盒子。”

## 参与其中

Eclipse 基金会邀请开发者、企业和研究人员加入 Eclipse LMOS 社区，为开源代理式 AI 的演进做出贡献。该项目是 Eclipse 基金会更广泛的 AI 计划的一部分，其中包括涵盖云、边缘、物联网（IoT）、汽车和其他领域的 400 多个开源项目。